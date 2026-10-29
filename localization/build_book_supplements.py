"""Supplement eleven book resources with Chinese pages and English continuation."""
from pathlib import Path
import json,zipfile,re,copy
ROOT=Path(__file__).resolve().parent.parent
PACK=ROOT/'resourcepacks/CubeWarper-Chinese-Bilingual'
inventory=json.loads((ROOT/'localization/book_resource_inventory.json').read_text('utf-8'))
line_translations={}
def pairs(s):
    for line in s.strip().splitlines():
        en,zh=line.split('=',1);line_translations[en]=zh
pairs('''
Industrial Dyes=工业染料
Definitely Perfectly Harmless=绝对完全无害
Metal compounds have many uses in industrial dyes, and the most useful of these is lead.=金属化合物在工业染料中有广泛用途，其中最实用的是铅。
Lead compounds can be crafted into large quantities of red and white dye.=铅化合物可以制成大量红色和白色染料。
Yellow dye has not been produced in quantity from lead, as several ingredients cannot be found in quantity to make lead chromate.=由于制造铬酸铅所需的部分原料难以大量获取，无法使用铅大量生产黄色染料。
By combining the carbon dioxide fumes from rotting material and the acetic acid from spoiled ethanol, lead metal can be crafted into §lLead Carbonate§r, commonly known as Lead White.=将腐烂物质产生的二氧化碳与变质乙醇中的乙酸结合，可以将金属铅制成§l碳酸铅§r，通常称为铅白。
Dye produced this way can be made without the need to farm copious numbers of skeletons to grind their bones.=这种制法无需大量刷取骷髅并研磨其骨头来获取染料。
By oxidizing lead metal nuggets in a §2Furnace§r at high temperature, lead metal can be converted into §lLead Oxide§r, more commonly known as Red Lead.=在§2熔炉§r中高温氧化铅粒，可以将金属铅转化为§l氧化铅§r，通常称为铅丹。
This dye can be produced without the need for a flower farm or the cloche for copious amounts of red flowers.=这种染料的生产无需使用花卉农场或园艺玻璃罩种植大量红色花朵。
Clinker Bricks=烧结砖
Glass Houses and Stones=玻璃屋与石头
The art of baking bricks has progressed past wasting several parts of the batch producing clinker for being too close to the fire.=烧砖技术已经得到改进，砖块不会再因为过于接近火焰而烧结变形，造成整批砖块的部分损耗。
Those looking to recreate the iconic look of clinker brick facades may, however, heat bricks in the §2Smoker§r to vitrify and char the external bricks, turning them into §2Clinker Bricks§r.=若想重现烧结砖外墙的独特外观，可以在§2烟熏炉§r中加热砖块，使其表面玻璃化并焦化，变成§2烧结砖§r。
To complement the look of facades made from them, clinker bricks can be combined with terracotta to produce several decorative variants for facades: §2Clinker Brick Quoins§r and §2Sills§r.=为了搭配烧结砖外墙，可以将烧结砖与陶瓦组合，制成装饰变体：§2烧结砖隅石§r和§2窗台§r。
Clinker Bricks can also be formed into stairs, slabs, and walls.=烧结砖也可以制成楼梯、台阶和墙。
§2Clinker Brick Walls§r have a small sill of baked brick on the top-most layer.=§2烧结砖墙§r的最上层带有一小段烧制砖窗台。
Electromagnet=电磁铁
Unnaturally attractive=超乎寻常的吸引力
An Electromagnet is simply a big coil of wire wound around a ferromagnetic core which creates a magnetic field when provided with electric current.=电磁铁是缠绕在铁磁性磁芯上的大型导线线圈，通电后会产生磁场。
This field attracts nearby items to the magnet, making it ideal for collecting the spoils of a (mob-)farm.=磁场会将附近的物品吸向电磁铁，非常适合收集农场或刷怪场的产物。
The magnet runs continuously while it is being supplied with power, but can be disabled with a redstone signal. This behavior can be inverted by sneaking and rightclicking it with an Engineer's Screwdriver.=电磁铁在供电时持续工作，红石信号可以使其停止。潜行时手持工程师螺丝刀右键点击，可以反转这一控制方式。
Extendable Post=可延长立柱
The Sky's the Limit.=向天空延伸。
Used as the start of the custom-sized posts.=用作自定义尺寸立柱的底座。
(See <link;immersiveposts:usage;§1Usage§r;start> on how to use it.)=（使用方法请参阅<link;immersiveposts:usage;§1使用说明§r;start>。）
The base can be hidden simply by holding a block in your hand, right-clicking, and it will pretend to be that block.=手持方块右键点击即可伪装底座，使其显示为该方块的外观。
Sneak + right-click removes the cover.=潜行时右键点击可移除伪装。
It only accepts solid and opaque blocks as cover, however.=仅可使用实体且不透明的方块作为伪装。
Accepted Blocks=可用方块
Hm, what to pick..=嗯，该选什么呢……
1 Index Page=1 索引页
Treated-Wood.=防腐木。
Aluminum.=铝。
Steel.=钢。
Nether Bricks.=下界砖。
Iron.=铁。
Gold.=金。
Copper.=铜。
Lead.=铅。
Silver.=银。
Nickel.=镍。
Constantan.=康铜。
Electrum.=琥珀金。
Uranium.=铀。
Emits a little bit of light, though it seems only as much as a redstone torch?=会发出少量光，亮度似乎只有红石火把的程度。
Concrete.=混凝土。
Leaded Concrete.=含铅混凝土。
How to Use=使用方法
You're going to need the hammer and a material of your choice.=你需要准备工程师锤和选定的材料。
See <link;immersiveposts:posts;this;start> for a detailed list of things able to be used.=完整的可用材料列表请参阅<link;immersiveposts:posts;此处;start>。
Then with your chosen material in hand right-click the base with it and it should look like what's being shown in the image above.=随后手持选定的材料右键点击底座，即可形成上图所示的结构。
Note: It always has to be of the same type! A wooden post for example only accepts §oTreated Wood Fences§r nothing else!=注意：材料类型必须始终保持一致！例如，木制立柱只接受§o防腐木栅栏§r。
From here you can also right-click the post itself which makes it easier to see how high you've already made it.=之后也可以右键点击立柱本身进行加高，这样更容易看清当前高度。
Isn't that neat?=很方便吧？
Now, to get the 1-Wide arm you simply right-click with your hammer in hand at the desired side and height. To remove it right-click the side of the post the arm is on. (Or break it with an axe)=若要添加宽度为 1 格的横臂，手持工程师锤在所需侧面和高度右键点击即可。右键点击横臂所在的立柱侧面可以移除横臂，也可以用斧头将其破坏。
§nNote: It won't appear if there is a block in the way.§r=§n注意：若有方块阻挡，横臂将无法出现。§r
Right-clicking the arm itself will turn it into a 2-Wide arm and vise-versa.=右键点击横臂本身，可以在 1 格宽和 2 格宽之间切换。
Like with the 1-Wide, if there isn't enough space it will not change.=与 1 格宽横臂相同，空间不足时无法切换。
The one 1-Wide Arm flips up-side-down if it detects any block below it, §oeven§r if there is already one above it.=1 格宽横臂检测到下方存在方块时会倒置，§o即使§r上方已经有方块也是如此。
For §ostability§r reasons, the 2-Wide Arm however can §lnot§r flip up-side-down.=出于§o稳定性§r考虑，2 格宽横臂§l无法§r倒置。
§nPost Arm§r=§n立柱支臂§r
Placing non-solid blocks on the sides (Like connectors/relays) makes these cute little arms appear, making sure whatever you attached doesn't look like it's floating in the air.=在侧面放置非实体方块，例如连接器或继电器，会出现小型支臂，使附着的方块看起来有支撑。
§nHorizontal Truss§r=§n水平桁架§r
Line up two posts with at least 1 block (up to <config;i;maxTrussLength>) of empty space in between.=将两根立柱对齐，两者之间至少留出 1 格空隙，最多为 <config;i;maxTrussLength> 格。
Sneak + Right-click with the hammer on inner side of them. Do the same if you want to remove an already existing truss.=潜行时手持工程师锤右键点击立柱内侧即可添加桁架。使用相同操作可以移除已有桁架。
''')
link_terms={'Treated_Wood':'防腐木','Aluminium':'铝','Steel':'钢','Netherbrick':'下界砖','Iron':'铁','Gold':'金','Copper':'铜','Lead':'铅','Silver':'银','Nickel':'镍','Constantan':'康铜','Electrum':'琥珀金','Uranium':'铀','Concrete':'混凝土','Concrete_(Leaded)':'含铅混凝土'}

def manual_translate(text):
    raw=text.splitlines(); nonempty=[s for s in raw if s.strip()]
    # Title and subtitle are fixed leading lines in the IE manual format.
    headers=nonempty[:2] if nonempty[0]!='How to Use' else nonempty[:1]
    translated=[]
    for line in nonempty:
        prefix=re.match(r'^(?:<&[^>]+>)*',line).group()
        body=line[len(prefix):]
        suffix=''
        while body.endswith(('<np>','<br>')):
            token='<np>' if body.endswith('<np>') else '<br>'
            body=body[:-len(token)];suffix=token+suffix
        if not body:translated.append(prefix+suffix);continue
        zh=line_translations.get(body.strip())
        if zh is None:
            def trlink(m):
                return m.group(1)+'§1'+link_terms[m.group(2)]+'§r'+m.group(3)
            if re.fullmatch(r'\s*\d+ <link;immersiveposts:posts;§1[^§]+§r;[^>]+>',body):
                zh=re.sub(r'(<link;immersiveposts:posts;)§1([^§]+)§r(;[^>]+>)',trlink,body)
            else:raise ValueError(body)
        assert re.findall(r'§.',body)==re.findall(r'§.',zh),(body,zh)
        if line in headers:translated.append(prefix+zh+'（'+body+'）'+suffix)
        else:translated.append(prefix+zh+suffix)
    original_body='\n'.join(nonempty[len(headers):])
    # English continuation has no duplicate anchor definitions; links/styles persist.
    original_body=re.sub(r'<&[^>]+>','',original_body)
    return '\n\n'.join(translated)+'<np>\n\nEnglish original\n\n'+original_body+'\n'

tconstruct_text={
'Designing Tools':'工具设计',
'Stuck on design? Let me teach you the Thruul method! Start with a goal: want a strong melee weapon? ore miner? wither killer? The more precise your goal the stronger the tool.':'不知道如何设计工具？让我教你瑟鲁尔的方法！首先确定目标：你想要强力近战武器、采矿工具，还是用于击杀凋灵的武器？目标越明确，工具就越出色。',
'Next, identify the most important stats and modifiers to the goal. For melee, might be damage or damage per second. Ore mining may want luck or mining speed. Don\'t forget "deal breakers", like if you need cheap repair.':'接下来，确定对目标最重要的属性和强化。近战武器可能需要伤害或每秒伤害；采矿工具可能需要时运或采掘速度。还要考虑必须满足的条件，例如维修成本要低。',
'Finally, match tool type, materials, and modifiers to whats important. For materials, check the tip icon in the top corner. Also remember conditional modifiers like smite may be stronger than simple stat boosts if you can meet their conditions.':'最后，根据关键需求选择工具类型、材料和强化。查看上角的提示图标可以了解材料。也请记住，只要满足条件，亡灵杀手等条件性强化可能比直接提高属性更有效。',
'Tool Tips':'工具建议',
'Alright Tinker, you are about to learn about one of the most powerful ways to improve tools, abilities. Before you do, let me give you some quick advice.':'工匠，你即将了解提升工具的强大方式之一：能力强化。在此之前，让我给你一些简短的建议。',
'First, you might think the goal of tinkering is to create the best tool, but its not! Your goal is to make a good tool, and its hard to fail that. You can always improve your tool later.':'首先，打造工具的目标是制作一件好用的工具，这通常容易实现。你可以随时继续改进它。',
'Also, you might be wondering, "Is something worth using?". Simple! Just try them all! If you hate it, you can always recycle the tool, or just hide it in a chest. No rush to try each modifier, just start with what sounds fun!':'如果你想知道某个功能是否值得使用，亲自尝试就可以了！如果不喜欢，随时可以回收工具，或将它存放在箱子里。无需急着尝试所有强化，先选择你感兴趣的就好！',
'Cobalt Shards':'钴碎片',
'Cobalt shards cannot be found from slimes, only appearing in ichor geodes. They are primarily useful as an alternative source of the ore.':'史莱姆不会掉落钴碎片，钴碎片只出现在灵浆晶洞中。它们主要可作为钴矿石的替代来源。',
'Tool Tanks':'工具储液罐',
'Modifiers such as spitting, melting, and smashing will give the tool a tank. Fluid can be inserted or extracted by interacting with a tank while holding the tool. You can also fill and empty it in the smeltery GUI using the bucket slot (4) or by clicking a fluid in the tank (2) with the tool.':'喷洒、熔炼和迸射等强化会为工具增加储液罐。手持工具与储液罐交互，即可注入或抽出流体。也可以在冶炼炉界面中使用桶槽位 (4)，或手持工具点击储液罐中的流体 (2)，为工具注入或抽出流体。',
'Cobalt Ore':'钴矿石',
'Cobalt ore can be found scattered around the nether. It is most common near ancient debris between elevations of 8 and 32, though it can be located at any height in smaller quantities. Since the ore often appears exposed to air, it can often be easily spotted by its distinct hue in the walls or ceiling of the Nether.':'钴矿石零散分布于下界各处，最常见于高度 8 至 32 的远古残骸附近，在其他高度也有少量分布。钴矿石通常暴露于空气中，其独特的颜色使它在下界墙壁或顶部容易被发现。',
}

def json_translate(data):
    if isinstance(data,list):return [json_translate(v) for v in data]
    if isinstance(data,dict):return {k:(tconstruct_text[v] if k in ['title','text'] and isinstance(v,str) else json_translate(v)) for k,v in data.items()}
    return data

manifest=[]
sections={}
for row in inventory:
    ns=row['english'].split('/')[1]
    if ns not in ['immersiveengineering','immersiveposts','tconstruct'] or row['jar_chinese'] or row['auto_chinese']:continue
    with zipfile.ZipFile(ROOT/row['archive']) as z:
        original=z.read(row['english']).decode('utf-8')
        target=row['english'].replace('/en_us/','/zh_cn/')
        dest=PACK/target;dest.parent.mkdir(parents=True,exist_ok=True)
        if ns!='tconstruct':dest.write_text(manual_translate(original),encoding='utf-8')
        else:
            data=json.loads(original);translated=json_translate(data)
            dest.write_text(json.dumps(translated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            parts=row['english'].split('/')
            book=parts[3];group=parts[5];stem=Path(parts[-1]).stem
            section_path=f'assets/tconstruct/book/{book}/sections/{group}.json'
            sections.setdefault(section_path,{'rows':json.loads(z.read(section_path)),'after':{}})['after'][stem]=row['english']
        manifest.append({'source_archive':row['archive'],'source_path':row['english'],'output_path':target,'english_retained':'following pages'})

for section,info in sections.items():
    translated_section=[]
    for row in info['rows']:
        translated_section.append(row)
        if row['name'] in info['after']:
            english=copy.deepcopy(row)
            english['name']+='__english_original'
            english['data']='tconstruct:'+info['after'][row['name']].removeprefix('assets/tconstruct/')
            translated_section.append(english)
    localized=section.replace('/sections/','/zh_cn/sections/')
    target=PACK/localized;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(translated_section,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest.append({'output_path':localized,'purpose':'Chinese-only localized section index with English continuation pages referencing original jar resource paths'})
# Forestry pages otherwise resolve their text through normal language keys.
forestry=next(p for p in (ROOT/'mods').glob('forestry-*.jar'))
source='assets/forestry/patchouli_books/foresters_manual/en_us/entries/core/circuit_board.json'
with zipfile.ZipFile(forestry) as z:
    data=json.loads(z.read(source))
def replace_literal(node):
    if isinstance(node,list):return [replace_literal(v) for v in node]
    if isinstance(node,dict):return {k:('电路板（Circuit Boards）' if k=='title' and v=='Circuit Boards' else replace_literal(v)) for k,v in node.items()}
    return node
data=replace_literal(data)
target=source.replace('/en_us/','/zh_cn/')
dest=PACK/target;dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest.append({'source_archive':str(forestry.relative_to(ROOT)),'source_path':source,'output_path':target,'english_retained':'same title field','purpose':'Single direct literal; language-key references remain unchanged'})
(ROOT/'localization/book_supplement_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Supplemented books:',len(manifest),'files (12 pages plus 2 localized indexes)')
