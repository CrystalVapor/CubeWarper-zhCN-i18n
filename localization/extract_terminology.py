"""Extract installed language resources without modifying game files."""
from __future__ import annotations
import csv
import hashlib
import io
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'localization'
PACK = ROOT / 'resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.20.1.zip'
LANG_PATH = re.compile(r'^assets/([^/]+)/lang/(en_us|zh_cn|zh_tw|zh_hk)\.(json|lang)$', re.I)

def remove_trailing_commas(text):
    result, in_string, escaped = [], False, False
    for index, character in enumerate(text):
        if in_string:
            result.append(character)
            if escaped:
                escaped = False
            elif character == '\\':
                escaped = True
            elif character == '"':
                in_string = False
        elif character == '"':
            in_string = True
            result.append(character)
        elif character == ',' and text[index + 1:].lstrip().startswith(('}', ']')):
            continue
        else:
            result.append(character)
    return ''.join(result)

def read_language(raw, extension):
    text = raw.decode('utf-8-sig')
    if extension.lower() == 'json':
        parsed = json.loads(remove_trailing_commas(text))
        if not isinstance(parsed, dict):
            raise ValueError('Language JSON must be an object')
        return {str(k): str(v) for k, v in parsed.items() if isinstance(v, str)}
    result = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        result[key.strip()] = value
    return result

def save_json(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

def nested_archives(z, chain=()):
    for entry in z.infolist():
        if not entry.filename.lower().endswith('.jar'):
            continue
        raw = z.read(entry)
        try:
            with zipfile.ZipFile(io.BytesIO(raw)) as child:
                child_chain = chain + (entry.filename,)
                yield child, child_chain
                yield from nested_archives(child, child_chain)
        except zipfile.BadZipFile:
            continue

def main():
    OUT.mkdir(exist_ok=True)
    files, errors, pairs = [], [], []
    languages = defaultdict(lambda: defaultdict(list))
    archives = [(p, 'mod') for p in sorted((ROOT / 'mods').glob('*.jar'))]
    if PACK.exists():
        archives.append((PACK, 'resourcepack'))
    for archive, kind in archives:
        try:
            with zipfile.ZipFile(archive) as z:
                archive_lang = defaultdict(dict)
                for entry in z.infolist():
                    match = LANG_PATH.fullmatch(entry.filename)
                    if not match:
                        continue
                    namespace, locale, extension = match.groups()
                    locale = locale.lower()
                    if kind == 'resourcepack' and locale != 'zh_cn':
                        continue
                    raw = z.read(entry)
                    rel = Path('extracted') / kind / archive.name / entry.filename
                    if locale.startswith('zh_'):
                        destination = OUT / rel
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        destination.write_bytes(raw)
                    source = {'archive': archive.relative_to(ROOT).as_posix(), 'entry': entry.filename,
                              'kind': kind, 'sha256': hashlib.sha256(raw).hexdigest()}
                    try:
                        data = read_language(raw, extension)
                    except Exception as e:
                        errors.append({**source, 'error': str(e)})
                        continue
                    files.append({**source, 'namespace': namespace, 'locale': locale, 'keys': len(data),
                                  'extracted_path': rel.as_posix() if locale.startswith('zh_') else None})
                    languages[namespace][locale].append((data, source))
                    archive_lang[namespace][locale] = (data, source)
                for namespace, locales in archive_lang.items():
                    if 'en_us' not in locales:
                        continue
                    english, en_source = locales['en_us']
                    for locale, (chinese, zh_source) in locales.items():
                        if not locale.startswith('zh_'):
                            continue
                        for key in english.keys() & chinese.keys():
                            pairs.append({'namespace': namespace, 'key': key, 'english': english[key],
                                          'chinese': chinese[key], 'locale': locale,
                                          'english_source': en_source, 'chinese_source': zh_source})
        except Exception as e:
            errors.append({'archive': archive.relative_to(ROOT).as_posix(), 'error': str(e)})
    nested_count = 0
    for archive, kind in archives:
        if kind != 'mod':
            continue
        with zipfile.ZipFile(archive) as outer:
            for nested, chain in nested_archives(outer):
                nested_count += 1
                for entry in nested.infolist():
                    match = LANG_PATH.fullmatch(entry.filename)
                    if not match:
                        continue
                    namespace, locale, extension = match.groups()
                    locale = locale.lower()
                    raw = nested.read(entry)
                    source = {'archive': archive.relative_to(ROOT).as_posix(), 'nested_archives': list(chain),
                              'entry': entry.filename, 'kind': 'mod', 'sha256': hashlib.sha256(raw).hexdigest()}
                    rel = Path('extracted/mod') / archive.name / 'nested' / '/'.join(chain) / entry.filename
                    if locale.startswith('zh_'):
                        destination = OUT / rel
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        destination.write_bytes(raw)
                    try:
                        data = read_language(raw, extension)
                    except Exception as e:
                        errors.append({**source, 'error': str(e)})
                        continue
                    files.append({**source, 'namespace': namespace, 'locale': locale, 'keys': len(data),
                                  'extracted_path': rel.as_posix() if locale.startswith('zh_') else None})
                    # Nested sources precede resourcepack and KubeJS language overrides.
                    languages[namespace][locale].insert(0, (data, source))
    for path in sorted((ROOT / 'kubejs/assets').glob('*/lang/*')):
        match = LANG_PATH.fullmatch(path.relative_to(ROOT / 'kubejs').as_posix())
        if not match:
            continue
        namespace, locale, extension = match.groups()
        locale = locale.lower()
        raw = path.read_bytes()
        source = {'archive': 'kubejs', 'entry': path.relative_to(ROOT / 'kubejs').as_posix(),
                  'kind': 'kubejs', 'sha256': hashlib.sha256(raw).hexdigest()}
        try:
            data = read_language(raw, extension)
        except Exception as e:
            errors.append({**source, 'error': str(e)})
            continue
        rel = Path('extracted/kubejs') / source['entry']
        if locale.startswith('zh_'):
            destination = OUT / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        files.append({**source, 'namespace': namespace, 'locale': locale, 'keys': len(data),
                      'extracted_path': rel.as_posix() if locale.startswith('zh_') else None})
        languages[namespace][locale].append((data, source))
    effective, missing, conflicts = {}, {}, []
    for namespace, locales in sorted(languages.items()):
        en_candidates, zh_candidates = defaultdict(list), defaultdict(list)
        for data, source in locales.get('en_us', []):
            for key, value in data.items():
                en_candidates[key].append({'value': value, 'source': source})
        for locale, language_files in locales.items():
            if not locale.startswith('zh_'):
                continue
            for data, source in language_files:
                for key, value in data.items():
                    if key not in en_candidates:
                        continue
                    for en in en_candidates[key]:
                        pairs.append({'namespace': namespace, 'key': key, 'english': en['value'],
                                      'chinese': value, 'locale': locale,
                                      'english_source': en['source'], 'chinese_source': source})
        for data, source in locales.get('zh_cn', []):
            for key, value in data.items():
                zh_candidates[key].append({'value': value, 'source': source})
        effective[namespace], missing[namespace] = {}, {}
        for key, candidates in sorted(en_candidates.items()):
            en = candidates[-1]
            zh = zh_candidates.get(key, [])
            for locale, entries in [('en_us', candidates), ('zh_cn', zh)]:
                if len({c['value'] for c in entries}) > 1:
                    conflicts.append({'namespace': namespace, 'key': key, 'locale': locale, 'candidates': entries})
            if zh and zh[-1]['value'].strip() and zh[-1]['value'] != en['value']:
                effective[namespace][key] = {'english': en['value'], 'chinese': zh[-1]['value'],
                                             'english_source': en['source'], 'chinese_source': zh[-1]['source']}
            else:
                missing[namespace][key] = {'english': en['value'], 'english_source': en['source'],
                                          'reason': 'identical_to_english' if zh else 'no_zh_cn',
                                          'existing_chinese': zh[-1]['value'] if zh else None}
    pairs = list({json.dumps(p, sort_keys=True, ensure_ascii=False): p for p in pairs}.values())
    pairs.sort(key=lambda p: (p['namespace'], p['key'], p['locale'], p['chinese_source']['archive']))
    save_json('language_inventory.json', files)
    save_json('namespace_english_sources.json', {ns: [source for _, source in locales.get('en_us', [])]
                                               for ns, locales in sorted(languages.items()) if locales.get('en_us')})
    save_json('all_pairs.json', pairs)
    save_json('effective_zh_cn.json', effective)
    save_json('missing_zh_cn.json', missing)
    save_json('missing_summary.json', {ns: len(values) for ns, values in missing.items() if values})
    save_json('conflicts.json', conflicts)
    save_json('extraction_errors.json', errors)
    with (OUT / 'all_pairs.tsv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['namespace', 'key', 'english', 'chinese', 'locale', 'english_archive', 'english_nested_archives', 'english_entry', 'chinese_archive', 'chinese_nested_archives', 'chinese_entry'])
        for p in pairs:
            writer.writerow([p['namespace'], p['key'], p['english'], p['chinese'], p['locale'],
                             p['english_source']['archive'], ' > '.join(p['english_source'].get('nested_archives', [])),
                             p['english_source']['entry'], p['chinese_source']['archive'],
                             ' > '.join(p['chinese_source'].get('nested_archives', [])), p['chinese_source']['entry']])
    stats = {'mod_jars': sum(kind == 'mod' for _, kind in archives), 'language_files': len(files),
             'nested_jars': nested_count,
             'chinese_files_in_mod_jars': sum(f['kind'] == 'mod' and f['locale'].startswith('zh_') for f in files),
             'resourcepack_chinese_files': sum(f['kind'] == 'resourcepack' for f in files),
             'pairs_all_locales_and_sources': len(pairs),
             'effective_simplified_pairs': sum(map(len, effective.values())),
             'missing_simplified_keys': sum(map(len, missing.values())),
             'conflicting_keys': len(conflicts), 'errors': len(errors),
             'selection_policy': 'Archive filename order; resourcepack zh_cn overrides jar zh_cn; KubeJS language files override both. This is a translation reference, not a claim about runtime resource priority.'}
    save_json('statistics.json', stats)
    print(json.dumps(stats, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
