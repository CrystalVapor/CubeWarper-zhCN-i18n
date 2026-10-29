[CmdletBinding()]
param(
    [string]$GameDirectory = '',
    [switch]$RestoreBackup,
    [string]$BackupId = ''
)

$ErrorActionPreference = 'Stop'
$Utf8 = New-Object System.Text.UTF8Encoding($false)
$AutomaticPack = 'file/Minecraft-Mod-Language-Modpack-Converted-1.20.1.zip'
$LocalPack = 'file/CubeWarper-Chinese-Bilingual'
if ([string]::IsNullOrWhiteSpace($GameDirectory)) { $GameDirectory = $PSScriptRoot }
$GameRoot = [System.IO.Path]::GetFullPath($GameDirectory).TrimEnd('\', '/')
if (-not (Test-Path -LiteralPath $GameRoot -PathType Container)) {
    throw 'GameDirectory must be an existing modpack instance directory.'
}
$RootPrefix = $GameRoot + [System.IO.Path]::DirectorySeparatorChar

function Resolve-Target([string]$Relative) {
    if ([string]::IsNullOrWhiteSpace($Relative) -or [System.IO.Path]::IsPathRooted($Relative)) {
        throw "Invalid relative path: $Relative"
    }
    $Result = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($GameRoot, $Relative))
    if (-not $Result.StartsWith($RootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path escapes GameDirectory: $Relative"
    }
    # Junctions and symbolic links could otherwise redirect a verified path.
    $Ancestor = $Result
    while ($Ancestor -and $Ancestor.Length -ge $GameRoot.Length) {
        if (Test-Path -LiteralPath $Ancestor) {
            $Item = Get-Item -LiteralPath $Ancestor -Force
            if (($Item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "Reparse points are unsupported in target paths: $Ancestor"
            }
        }
        if ($Ancestor -eq $GameRoot) { break }
        $Ancestor = [System.IO.Path]::GetDirectoryName($Ancestor)
    }
    return $Result
}

function Ensure-Parent([string]$Path) {
    $Parent = [System.IO.Path]::GetDirectoryName($Path)
    if (-not (Test-Path -LiteralPath $Parent)) {
        [void][System.IO.Directory]::CreateDirectory($Parent)
    }
}

function Write-Utf8([string]$Path, [string]$Content) {
    Ensure-Parent $Path
    [System.IO.File]::WriteAllText($Path, $Content, $Utf8)
}

function Read-Utf8([string]$Path) {
    return [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
}

function Set-JsonProperty($Object, [string]$Name, $Value) {
    if ($Object.PSObject.Properties[$Name]) { $Object.$Name = $Value }
    else { $Object | Add-Member -NotePropertyName $Name -NotePropertyValue $Value }
}

function Merge-PackOrder($Packs) {
    $Result = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Pack in @($Packs)) {
        if ($null -ne $Pack -and $Pack -ne $AutomaticPack -and $Pack -ne $LocalPack) {
            $Result.Add([string]$Pack)
        }
    }
    $Result.Add($AutomaticPack)
    $Result.Add($LocalPack)
    return ,$Result.ToArray()
}

function Merge-Options([string]$Path) {
    $Lines = @()
    if (Test-Path -LiteralPath $Path) {
        $Lines = @([System.IO.File]::ReadAllLines($Path, [System.Text.Encoding]::UTF8))
    }
    $Packs = @('vanilla', 'mod_resources')
    foreach ($Line in $Lines) {
        if ($Line.StartsWith('resourcePacks:')) {
            $Packs = ConvertFrom-Json -InputObject ($Line.Substring(14))
            break
        }
    }
    $PackJson = ConvertTo-Json -InputObject (Merge-PackOrder $Packs) -Compress
    $Output = New-Object 'System.Collections.Generic.List[string]'
    $HadLang = $false
    $HadPacks = $false
    foreach ($Line in $Lines) {
        if ($Line.StartsWith('lang:')) {
            if (-not $HadLang) { $Output.Add('lang:zh_cn'); $HadLang = $true }
        } elseif ($Line.StartsWith('resourcePacks:')) {
            if (-not $HadPacks) { $Output.Add('resourcePacks:' + $PackJson); $HadPacks = $true }
        } else { $Output.Add($Line) }
    }
    if (-not $HadLang) { $Output.Add('lang:zh_cn') }
    if (-not $HadPacks) { $Output.Add('resourcePacks:' + $PackJson) }
    Write-Utf8 $Path (($Output.ToArray() -join "`r`n") + "`r`n")
}

function Merge-Overrides([string]$Path) {
    if (Test-Path -LiteralPath $Path) {
        $Data = Read-Utf8 $Path | ConvertFrom-Json
    } else {
        $Data = [pscustomobject]@{ schema_version = 2; default_packs = @('vanilla', 'mod_resources') }
    }
    if (-not $Data.PSObject.Properties['pack_overrides']) {
        Set-JsonProperty $Data 'pack_overrides' ([pscustomobject]@{})
    }
    Set-JsonProperty $Data 'default_packs' (Merge-PackOrder $Data.default_packs)
    $Overrides = $Data.pack_overrides
    foreach ($Name in @($AutomaticPack, $LocalPack)) {
        if (-not $Overrides.PSObject.Properties[$Name]) {
            Set-JsonProperty $Overrides $Name ([pscustomobject]@{})
        }
        $Pack = $Overrides.$Name
        Set-JsonProperty $Pack 'required' $true
        Set-JsonProperty $Pack 'force_compatible' $true
        if ($Name -eq $LocalPack) {
            Set-JsonProperty $Pack 'default_position' 'TOP'
            Set-JsonProperty $Pack 'fixed_position' $true
        }
    }
    if ($Overrides.PSObject.Properties['locked_group']) {
        $Dedicated = @($Overrides.PSObject.Properties | Where-Object {
            $_.Name -ne 'locked_group' -and -not $_.Name.StartsWith('$$')
        } | ForEach-Object { $_.Name })
        $Locked = @($Overrides.locked_group | Where-Object { $_ -notin $Dedicated })
        Set-JsonProperty $Overrides 'locked_group' $Locked
    }
    Write-Utf8 $Path ((ConvertTo-Json -InputObject $Data -Depth 100) + "`r`n")
}

$BackupBase = Resolve-Target '.cube-warper-localization-backups'
if ($RestoreBackup) {
    if (-not (Test-Path -LiteralPath $BackupBase)) { throw 'No patch backup was found.' }
    if ($BackupId) {
        if ($BackupId -notmatch '^\d{8}-\d{6}-\d{3}$') { throw 'BackupId must be a timestamp folder name.' }
        $Selected = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId)
    } else {
        $Candidate = Get-ChildItem -LiteralPath $BackupBase -Directory |
            Where-Object { $_.Name -match '^\d{8}-\d{6}-\d{3}$' } |
            Sort-Object Name -Descending | Select-Object -First 1
        if (-not $Candidate) { throw 'No patch backup was found.' }
        $BackupId = $Candidate.Name
        $Selected = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId)
    }
    $ManifestPath = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId + '/manifest.json')
    $Manifest = Read-Utf8 $ManifestPath | ConvertFrom-Json
    $RestoreActions = @()
    foreach ($Entry in $Manifest.files) {
        $Target = Resolve-Target $Entry.path
        $Saved = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId + '/files/' + $Entry.path)
        if ($Entry.existed -and -not (Test-Path -LiteralPath $Saved -PathType Leaf)) {
            throw "Backup is incomplete: $($Entry.path)"
        }
        $RestoreActions += [pscustomobject]@{ target=$Target; saved=$Saved; existed=$Entry.existed }
    }
    foreach ($Action in $RestoreActions) {
        if ($Action.existed) {
            Ensure-Parent $Action.target
            Copy-Item -LiteralPath $Action.saved -Destination $Action.target -Force
        } elseif (Test-Path -LiteralPath $Action.target -PathType Leaf) {
            Remove-Item -LiteralPath $Action.target -Force
        }
    }
    Write-Host "Restored backup $BackupId. Empty directories and the backup are retained."
    exit 0
}

$PayloadRoot = Join-Path $PSScriptRoot 'payload'
if (-not (Test-Path -LiteralPath $PayloadRoot -PathType Container)) {
    throw 'payload directory is missing. Extract the complete patch archive first.'
}
$PayloadPrefix = [System.IO.Path]::GetFullPath($PayloadRoot).TrimEnd('\', '/') + '\'
$Copies = @()
$ChangedPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
foreach ($File in Get-ChildItem -LiteralPath $PayloadRoot -File -Recurse) {
    $Relative = $File.FullName.Substring($PayloadPrefix.Length)
    $Target = Resolve-Target $Relative
    if ($Relative.Replace('\', '/') -eq ('resourcepacks/' + $AutomaticPack.Substring(5)) -and (Test-Path -LiteralPath $Target -PathType Leaf)) {
        if ((Get-Item -LiteralPath $Target).LastWriteTimeUtc -gt $File.LastWriteTimeUtc) {
            Write-Host 'Keeping the newer local automatic language archive.'
            continue
        }
    }
    $Copies += [pscustomobject]@{ source=$File.FullName; target=$Target; relative=$Relative }
    [void]$ChangedPaths.Add($Relative)
}
foreach ($Relative in @('options.txt', 'config/defaultoptions/options.txt', 'config/resourcepackoverrides.json')) {
    [void](Resolve-Target $Relative)
    [void]$ChangedPaths.Add($Relative)
}

# Validate merge inputs before changing any instance files.
foreach ($Relative in @('options.txt', 'config/defaultoptions/options.txt')) {
    $Path = Resolve-Target $Relative
    if (Test-Path -LiteralPath $Path) {
        foreach ($Line in [System.IO.File]::ReadAllLines($Path, [System.Text.Encoding]::UTF8)) {
            if ($Line.StartsWith('resourcePacks:')) { [void]($Line.Substring(14) | ConvertFrom-Json) }
        }
    }
}
$OverridesPath = Resolve-Target 'config/resourcepackoverrides.json'
if (Test-Path -LiteralPath $OverridesPath) { [void](Read-Utf8 $OverridesPath | ConvertFrom-Json) }
$BackupId = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$ManifestPath = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId + '/manifest.json')
$Entries = @()
foreach ($Relative in $ChangedPaths) {
    $Target = Resolve-Target $Relative
    $Existed = Test-Path -LiteralPath $Target -PathType Leaf
    if ((Test-Path -LiteralPath $Target) -and -not $Existed) { throw "Expected a file: $Relative" }
    if ($Existed) {
        $Saved = Resolve-Target ('.cube-warper-localization-backups/' + $BackupId + '/files/' + $Relative)
        Ensure-Parent $Saved
        Copy-Item -LiteralPath $Target -Destination $Saved -Force
    }
    $Entries += [pscustomobject]@{ path=$Relative; existed=[bool]$Existed }
}
Write-Utf8 $ManifestPath ((ConvertTo-Json -InputObject ([pscustomobject]@{
    version=1; created=(Get-Date).ToString('o'); files=$Entries
}) -Depth 10) + "`r`n")
foreach ($Copy in $Copies) {
    Ensure-Parent $Copy.target
    Copy-Item -LiteralPath $Copy.source -Destination $Copy.target -Force
}
Merge-Options (Resolve-Target 'options.txt')
Merge-Options (Resolve-Target 'config/defaultoptions/options.txt')
Merge-Overrides $OverridesPath
Write-Host "Installed the patch. Backup: $BackupId"
Write-Host 'Resource order: automatic Chinese pack, then the local bilingual patch.'
Write-Host 'Start Minecraft normally after the script finishes.'
