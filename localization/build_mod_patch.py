"""Merge reviewed translations by resource key and safely reuse format arguments."""
import collections,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'localization'
PACK=ROOT/'resourcepacks/CubeWarper-Chinese-Bilingual'
FORMAT=re.compile(r'%(?:(\d+)\$)?([-#+0,(<]*)(\d*)(\.\d+)?([tT][A-Za-z]|[bBhHsScCdoxXeEfgGaAn%])')

def indexed(text):
    count=0;previous=0;signature=[]
    def replace(m):
        nonlocal count,previous
        explicit,flags,width,precision,typ=m.groups()
        if typ in ('%','n'):return m.group()
        if explicit:idx=int(explicit)
        elif '<' in flags:idx=previous
        else:count+=1;idx=count
        previous=idx
        signature.append((idx,typ.lower()))
        return '%'+str(idx)+'$'+flags.replace('<','')+width+(precision or '')+typ
    return FORMAT.sub(replace,text),signature

def bilingual(zh,en,key):
    if zh==en:return en
    if key.endswith(('.keyword','_extra_msg')):
        return zh+','+en
    zh_idx,zh_sig=indexed(zh)
    en_idx,en_sig=indexed(en)
    if collections.Counter(zh_sig)!=collections.Counter(en_sig):
        raise ValueError(f'Placeholder mismatch {key}: {zh_sig} vs {en_sig}')
    reset='§r' if '§' in en or '§' in zh else ''
    return zh_idx+reset+'（'+en_idx+reset+'）'

def main():
    missing=json.loads((P/'missing_zh_cn.json').read_text(encoding='utf-8'))
    files=['manual_mod_translations_reused.json','manual_mod_translations_terms.json','manual_mod_translations_loader.json','manual_mod_translations_terms_extra.json','manual_mod_translations_terms_nested.json','manual_mod_translations_quest_ui.json','manual_mod_translations_main.json','manual_mod_translations_main_extra.json','manual_mod_translations_final.json']
    translated={};sources={};conflicts=[]
    for name in files:
        path=P/name
        if not path.exists():continue
        for ns,m in json.loads(path.read_text(encoding='utf-8')).items():
            for key,zh in m.items():
                if key in translated.get(ns,{}) and translated[ns][key]!=zh:
                    conflicts.append({'namespace':ns,'key':key,'previous':translated[ns][key],'chosen':zh,'source':name})
                translated.setdefault(ns,{})[key]=zh
                sources[(ns,key)]=name
    exclusions={}
    for name in ['excluded_main.json','excluded_main_details.json','excluded_main_extra.json','manual_mod_exclusions_terms.json','manual_mod_exclusions_terms_extra.json','manual_mod_exclusions_terms_nested.json','manual_mod_exclusions_quest_ui.json']:
        path=P/name
        if not path.exists():continue
        for ns,m in json.loads(path.read_text(encoding='utf-8')).items():exclusions.setdefault(ns,{}).update(m)
    report={'translated':0,'identity_preserved':0,'excluded':0,'unresolved':{},'conflicts':conflicts,'format_checked':0,'namespaces':{}}
    pairs=[]
    for ns,m in translated.items():
        target=PACK/'assets'/ns/'lang/zh_cn.json'
        data={}
        for key,zh in m.items():
            if key not in missing.get(ns,{}):continue
            en=missing[ns][key]['english']
            if zh==en:
                report['identity_preserved']+=1
                continue
            data[key]=bilingual(zh,en,key)
            report['format_checked']+=1
            pairs.append({'namespace':ns,'key':key,'english':en,'chinese':zh,'source':sources[(ns,key)]})
        if data:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            report['translated']+=len(data)
            report['namespaces'][ns]=len(data)
    for ns,m in missing.items():
        for key,record in m.items():
            if key in translated.get(ns,{}):continue
            if key in exclusions.get(ns,{}):report['excluded']+=1
            else:report['unresolved'].setdefault(ns,{})[key]=record['english']
    (P/'patch_translations.json').write_text(json.dumps(pairs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (P/'mod_patch_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Translated',report['translated'],'Identity',report['identity_preserved'],'Excluded',report['excluded'],'Unresolved',sum(map(len,report['unresolved'].values())),'Conflicts',len(conflicts))

if __name__=='__main__':main()
