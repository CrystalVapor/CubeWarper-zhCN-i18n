import json,re
from pathlib import Path
p=Path(__file__).parent
missing=json.loads((p/'missing_zh_cn.json').read_text(encoding='utf-8'))
pairs=json.loads((p/'effective_zh_cn.json').read_text(encoding='utf-8'))
lookup={}
for ns, values in pairs.items():
    for key,v in values.items():
        en,zh=v['english'],v['chinese']
        if re.search('[\u3400-\u9fff]',zh): lookup.setdefault(en,set()).add(zh)
skip={'untagged_mobs','forestry','clanginghowl','unusual_furniture','incision','infernalexp','delightfulcreators'}
reused={};remaining={};excluded={}
for ns,values in missing.items():
    if ns in skip: continue
    for key,v in values.items():
        en=v['english']
        matches=lookup.get(en,set())
        if len(matches)==1:
            reused.setdefault(ns,{})[key]=next(iter(matches))
        elif key.startswith('_') or not re.search('[A-Za-z]',en) or re.fullmatch(r'(?:https?://|[a-z_]+:)[^\s]+',en):
            excluded.setdefault(ns,{})[key]=en
        else: remaining.setdefault(ns,{})[key]=en
(p/'manual_mod_translations_reused.json').write_text(json.dumps(reused,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'remaining_main.json').write_text(json.dumps(remaining,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'excluded_main.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Reused',sum(map(len,reused.values())),'Excluded',sum(map(len,excluded.values())),'Remaining',sum(map(len,remaining.values())))
print('\n'.join(f'{ns}: {len(m)}' for ns,m in remaining.items()))
