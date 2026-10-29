"""Build the installable ZIP from the versioned payload using the standard library."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def digest(content):
    return hashlib.sha256(content).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    expected = set(manifest['files'])
    actual = {p.relative_to(ROOT / 'payload').as_posix()
              for p in (ROOT / 'payload').rglob('*') if p.is_file()}
    if actual != expected:
        raise ValueError(f'Payload differs from manifest: missing={expected-actual}, extra={actual-expected}')
    for relative, record in manifest['files'].items():
        contents = (ROOT / 'payload' / relative).read_bytes()
        if digest(contents) != record['sha256'] or len(contents) != record['bytes']:
            raise ValueError(f'Manifest mismatch: {relative}')
    args.output.mkdir(parents=True, exist_ok=True)
    target = args.output / f"CubeWarper-zh_CN-Bilingual-Patch-{manifest['version']}.zip"
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(expected):
            archive.write(ROOT / 'payload' / relative, 'payload/' + relative)
        archive.write(ROOT / 'manifest.json', 'manifest.json')
        archive.write(ROOT / 'Install-Patch.ps1', 'Install-Patch.ps1')
        archive.write(ROOT / 'docs/INSTALL.md', 'README.md')
        archive.write(ROOT / 'NOTICE.md', 'NOTICE.md')
        for path in sorted((ROOT / 'reports').glob('*')):
            if path.is_file():
                archive.write(path, 'reports/' + path.name)
        for path in sorted((ROOT / 'localization').glob('*translations*.json')):
            archive.write(path, 'translation-reference/' + path.name)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError('Archive CRC verification failed')
        for relative, record in manifest['files'].items():
            if digest(archive.read('payload/' + relative)) != record['sha256']:
                raise ValueError(f'Archive content differs: {relative}')
    checksum = digest(target.read_bytes())
    target.with_suffix('.zip.sha256').write_text(checksum + '  ' + target.name + '\n', encoding='ascii')
    print(json.dumps({'archive': target.name, 'payload_files': len(expected),
                      'bytes': target.stat().st_size, 'sha256': checksum}))


if __name__ == '__main__':
    main()
