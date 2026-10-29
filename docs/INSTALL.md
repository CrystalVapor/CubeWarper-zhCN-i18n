# Cube Warper 中文双语补丁

本补丁包含任务书、KubeJS 自定义内容、仪式指南书及模组缺失译文。中文后保留英文原文；仪式指南的长正文使用紧随中文页的英文页。

## 安装

安装及恢复前，请完全退出 Minecraft。脚本只安装文件，不启动游戏。

1. 将补丁 ZIP 完整解压到 Cube Warper 的实例根目录，使 `Install-Patch.ps1`、`payload` 与实例的 `mods`、`config` 文件夹位于同一层。
2. 在该目录打开 Windows PowerShell，运行：

   ```powershell
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1
   ```

3. 脚本完成后，从启动器正常启动该实例。

也可以保留补丁解压目录，通过参数指定实例根目录：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1 -GameDirectory "D:\Game\Minecraft\.minecraft\versions\Cube Warper"
```

脚本适用于 Windows PowerShell 5.1。它会逐文件备份修改前的内容，再复制 `payload` 内的补丁文件。配置文本使用 UTF-8 无 BOM 写入；已有任务进度和存档不在补丁文件范围内。

资源包顺序会保留其他资源包，使自动中文包位于倒数第二，本地双语补丁位于最后。`options.txt` 和 `config/defaultoptions/options.txt` 中的语言设置为 `zh_cn`。已有的自动中文 ZIP 如果修改时间更新，将保留本地版本。自动汉化更新模组后续更新该 ZIP 时，本地补丁仍通过独立资源包提供译文。

`resourcepackoverrides.json` 采用合并方式更新。天空资源包的专属配置和其他配置会保留；拥有专属配置的资源包会从 `locked_group` 的重复成员中移除。补丁设置为顶部固定且必须启用，自动中文包设置为必须启用。遇到符号链接或目录联接的目标路径，脚本会终止，以确保所有写入均位于所指定的实例内。

## 恢复

备份保存在实例根目录的 `.cube-warper-localization-backups\时间戳`。恢复最新一次安装前的状态：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1 -RestoreBackup
```

指定实例和备份：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1 -GameDirectory "D:\Game\Minecraft\.minecraft\versions\Cube Warper" -RestoreBackup -BackupId "20261012-010000-000"
```

恢复会按照 `manifest.json` 还原此前已有的文件，并逐个删除安装时新增的文件。空目录和备份目录会保留。恢复也会还原备份中的语言和资源包配置。安装后对这些文件做出的其他修改，会被所选备份覆盖。

重复安装会生成新的备份。若需要完全撤回多次安装，请从最新备份开始逐次恢复，再指定较早的备份。建议保留 ZIP 和备份目录，以便复核或重新安装。

## 手册补充与范围

补丁补充了沉浸工程、沉浸立柱、匠魂手册中的 11 份缺失中文页面，以及林业手册的一处电路板标题。手册正文保留英文后续页面；中文专用索引将匠魂英文原始页排列在相应中文页之后。分页标记、配置占位符和链接目标保持有效。实际分页与显示效果仍需在游戏中检查。

Alex's Caves 的 68 份普通洞穴手册资源已有原模组中文对应文件。探洞台小游戏的 6 份词库继续使用英文：小游戏使用专用符文字体、逐字布局、目标词选择与揭示逻辑，中文词库需要额外的字体及匹配行为验证。Citadel、EnderIO 和 Mantle 的示例或测试手册保留原文。此次补丁的覆盖范围不包含所有 Java 代码内直接写入的文本。

详细检查范围及验证结果记录于压缩包中的 `reports/book_scope.json`，新增资源清单记录于 `reports/book_supplement_manifest.json`。术语表及原始中文文件另存于配套术语资料 ZIP；将其解压到实例根目录后可在 `localization/` 中查阅。
