import json,pathlib,re

ROOT=pathlib.Path(__file__).resolve().parent.parent

def main():
    fields=0
    for backup in (ROOT/'localization/backups/quests').glob('*.snbt'):
        live=ROOT/'config/ftbquests/quests/chapters'/backup.name
        original=backup.read_text(encoding='utf-8')
        translated=live.read_text(encoding='utf-8')
        pattern=r'"(?:\\.|[^"\\])*"'
        old_strings=re.findall(pattern,original)
        new_strings=re.findall(pattern,translated)
        assert len(old_strings)==len(new_strings),backup
        assert re.sub(pattern,'STRING',original)==re.sub(pattern,'STRING',translated),backup
        for old,new in zip(old_strings,new_strings):
            old=json.loads(old);new=json.loads(new)
            if old!=new:
                assert new.endswith('（'+old+'&r）'),(backup,old)
                fields+=1
        print(backup.name+': syntax structure, original English and functional literals verified')
    base=ROOT/'localization/backups/patchouli/ritual_circle/en_us'
    for backup in base.rglob('*.json'):
        live=ROOT/'patchouli_books/ritual_circle/zh_cn'/backup.relative_to(base)
        old=json.loads(backup.read_text(encoding='utf-8'))
        new=json.loads(live.read_text(encoding='utf-8'))
        for key in old:
            if key not in ('name','description','pages'):
                assert old[key]==new[key],(backup,key)
        if 'pages' in old:
            index=0
            for page in old['pages']:
                translated=new['pages'][index]
                for key in page:
                    if key not in ('title','text'):
                        assert page[key]==translated[key],(backup,key)
                index+=1
                if 'text' in page:
                    assert new['pages'][index]['text']==page['text'],backup
                    index+=1
        print(str(backup.relative_to(base))+': functional fields and original English verified')
    print('Verified translated quest fields:',fields)

if __name__=='__main__':main()
