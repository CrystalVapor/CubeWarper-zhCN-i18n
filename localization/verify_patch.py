import json,re,subprocess
from pathlib import Path
from build_mod_patch import bilingual,indexed
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'localization'
PACK=ROOT/'resourcepacks/CubeWarper-Chinese-Bilingual'

def no_duplicates(items):
    result={}
    for key,value in items:
        assert key not in result,('duplicate JSON key',key)
        result[key]=value
    return result

def main():
    report={}
    languages={}
    files=list(PACK.rglob('*.json'))+[PACK/'pack.mcmeta']
    for path in files:
        data=json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=no_duplicates)
        if path.parent.name=='lang':
            assert all(isinstance(k,str) and isinstance(v,str) for k,v in data.items()),path
            languages[path.parents[1].name]=data
    report['resourcepack_json_files']=len(files)
    kube=json.loads((P/'kubejs_translations.json').read_text(encoding='utf-8'))
    records=json.loads((P/'patch_translations.json').read_text(encoding='utf-8'))
    checked=0;overrides=0
    for record in records:
        ns,key,en,zh=record['namespace'],record['key'],record['english'],record['chinese']
        if key in kube.get(ns,{}):
            overrides+=1
            continue
        assert languages[ns][key]==bilingual(zh,en,key),(ns,key)
        checked+=1
    report['mod_bilingual_keys_checked']=checked
    report['custom_name_overrides']=overrides
    js=(ROOT/'kubejs/client_scripts/zz_cube_warper_zh_cn.js').read_text(encoding='utf-8')
    jskeys={}
    for line in js.splitlines():
        if line.strip().startswith('event.add('):
            args=line.strip()[len('event.add('):-1]
            key,value=json.loads('['+args+']')
            jskeys[key]=value
    for ns,m in kube.items():
        for key,v in m.items():
            assert jskeys[key]==languages[ns][key],key
            assert v['english'] in languages[ns][key],key
    report['kubejs_keys_checked']=len(jskeys)
    for rel in ['kubejs/client_scripts/zz_cube_warper_zh_cn.js','kubejs/client_scripts/tooltips.js','kubejs/server_scripts/!main/commandblock_check.js']:
        subprocess.run(['node','--check',str(ROOT/rel)],check=True,capture_output=True)
    report['javascript_syntax_files']=3
    configs=[ROOT/'options.txt',ROOT/'config/defaultoptions/options.txt']
    expected=['file/Minecraft-Mod-Language-Modpack-Converted-1.20.1.zip','file/CubeWarper-Chinese-Bilingual']
    for path in configs:
        options=path.read_text(encoding='utf-8')
        value=next(line[len('resourcePacks:'):] for line in options.splitlines() if line.startswith('resourcePacks:'))
        assert json.loads(value)[-2:]==expected,path
        assert 'lang:zh_cn' in options.splitlines(),path
    override=json.loads((ROOT/'config/resourcepackoverrides.json').read_text(encoding='utf-8'))
    assert override['default_packs'][-2:]==expected
    overrides=override['pack_overrides']
    for group,entries in overrides.items():
        if isinstance(entries,list):
            assert not set(entries).intersection(k for k,v in overrides.items() if isinstance(v,dict) and not k.startswith('$$')),group
    report['load_configuration_checked']=3
    report['in_game_validation']='尚未启动游戏验证排版和资源重载'
    (P/'verification_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
