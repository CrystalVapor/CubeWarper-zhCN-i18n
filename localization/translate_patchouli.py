import copy, json, pathlib, shutil

ROOT=pathlib.Path(__file__).resolve().parent.parent
BOOK=ROOT/'patchouli_books/ritual_circle'
T={
'Conducting Rituals':'仪式操作指南',
'This book looks back at you. $(br2)A guide to the Unnatural.':'这本书也在凝视着你。$(br2)一本关于超自然事物的指南。',
'Rituals':'仪式',
'Conducting various rituals':'执行各种仪式',
'Introduction':'引言',
'The Dark Shrine':'黑暗祭坛',
'Inside of dimension 64, also known to some as Carrion-485, there exists a shrine that is capable of channelling an insane amount of dark energy. $(br2)This construct consists of 8 pillars standing in a circle around one central pillar.':'维度 64，又被称为腐肉-485，其中有一座能够引导极大量黑暗能量的祭坛。$(br2)这个结构由八根围成圆形的石柱与一根中央石柱组成。',
'Bringing Forth the Missing':'召唤缺失者',
'The Missing or The Non-Players are strange deadly entities consisting of missing textures. $(br2)They will attack the player when provoked and drop a Missing Core uppon death. $(br2)Know that they can do any action that a normal player can do when fighting them, this makes then incredibly lethal.':'缺失者，又称非玩家，是由缺失纹理构成的奇异致命实体。$(br2)受到挑衅后，它们会攻击玩家，死亡时掉落缺失核心。$(br2)与它们战斗时需要注意，它们能够执行普通玩家的所有操作，因此极为危险。',
'Corrupting a Vector':'腐化矢量算子',
'This ritual will corrupt a Vector Operator by trapping a Crimson Eye inside of it. $(br2)The applications for this are unexplored...':'这个仪式会将绯红之眼囚禁在矢量算子内部，使算子腐化。$(br2)它的用途尚待探索……',
'Recapturing Consciousness':'重新捕获意识',
'The Crimson Eyes seem to be bound to the ancient pillars in some way. $(br2)With this ritual it is possible to reverse engineer this system by trapping it inside our own Consciousness Container.':'绯红之眼似乎以某种方式被束缚在远古石柱上。$(br2)利用这个仪式，可以逆向解析这套系统，将眼睛囚禁在我们自己的意识容器中。',
'Summoning Darkness':'召唤黑暗',
'This ritual will bring forth Pure Darkness. $(br2)After sacrificing the required items, three pieces of True Darkness will jump out from the middle pedestal.':'这个仪式会召唤纯粹黑暗。$(br2)献祭所需物品后，三份纯粹黑暗会从中央基座中跃出。'
}

def bi(value,separator='（',end='）'):
    return T[value]+separator+value+end

def main():
    backups=ROOT/'localization/backups/patchouli'
    backups.mkdir(parents=True,exist_ok=True)
    original=backups/'ritual_circle'
    if not original.exists():shutil.copytree(BOOK,original)
    meta=json.loads((original/'book.json').read_text(encoding='utf-8'))
    meta['name']=bi(meta['name'])
    meta['landing_text']=T[meta['landing_text']]+'$(br2)'+meta['landing_text']
    (BOOK/'book.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for source in (original/'en_us').rglob('*.json'):
        data=json.loads(source.read_text(encoding='utf-8'))
        for k in ('name','description'):
            if k in data:data[k]=bi(data[k])
        if 'pages' in data:
            pages=[]
            for page in data['pages']:
                translated=copy.deepcopy(page)
                if 'title' in page:translated['title']=bi(page['title'])
                if 'text' in page:translated['text']=T[page['text']]
                pages.append(translated)
                if 'text' in page:
                    # Patchouli has fixed-size pages. Keep English as the next
                    # page so both language versions remain fully readable.
                    pages.append({'type':'patchouli:text','title':page.get('title',''),'text':page['text']})
            data['pages']=pages
        target=BOOK/'zh_cn'/source.relative_to(original/'en_us')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Patchouli: 19 display fields translated; five English companion pages added.')

if __name__=='__main__':main()
