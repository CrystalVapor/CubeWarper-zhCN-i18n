import json, pathlib, re, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'localization'
STR = re.compile(r'"((?:\\.|[^"\\])*)"')

def visible_strings(source):
    active = False
    for line in source.splitlines(keepends=True):
        if re.match(r'\s*description:', line):
            active = True
        if active or re.match(r'\s*(title|subtitle):', line):
            for match in STR.finditer(line):
                value = json.loads('"' + match.group(1) + '"')
                if value and not value.startswith('{image:') and not value.startswith('/'):
                    yield value
        if active and ']' in line:
            active = False

def bilingual(chinese, english):
    # Reset active styling at the boundary; the English replays its exact codes.
    return chinese + '&r（' + english + '&r）'

def apply_quests():
    mapping = json.loads((OUT / 'quest_translations.json').read_text(encoding='utf-8'))
    report = []
    for path in sorted((ROOT / 'config/ftbquests/quests/chapters').glob('*.snbt')):
        backup = OUT / 'backups/quests' / path.name
        backup.parent.mkdir(parents=True, exist_ok=True)
        if not backup.exists():
            shutil.copy2(path, backup)
        source = backup.read_text(encoding='utf-8')
        needed = set(visible_strings(source))
        missing = needed - mapping.keys()
        if missing:
            raise ValueError(f'{path.name}: missing translations: {sorted(missing)}')
        active = False
        lines = []
        count = 0
        for line in source.splitlines(keepends=True):
            if re.match(r'\s*description:', line):
                active = True
            if active or re.match(r'\s*(title|subtitle):', line):
                def replace(match):
                    nonlocal count
                    value = json.loads('"' + match.group(1) + '"')
                    if value not in needed:
                        return match.group(0)
                    count += 1
                    return json.dumps(bilingual(mapping[value], value), ensure_ascii=False)
                line = STR.sub(replace, line)
            lines.append(line)
            if active and ']' in line:
                active = False
        result = ''.join(lines)
        path.write_text(result, encoding='utf-8', newline='')
        report.append({'file': str(path.relative_to(ROOT)), 'translated_fields': count})
    (OUT / 'quest_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__':
    apply_quests()
