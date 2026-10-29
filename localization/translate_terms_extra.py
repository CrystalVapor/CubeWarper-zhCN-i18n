import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent
pending=json.loads((BASE/'pending_main.json').read_text(encoding='utf8'))
namespaces='alexscaves biomesoplenty caverns_and_chasms darkerdepths endergetic environmental neapolitan windswept farmersdelight miners_delight malum tconstruct undergarden brewinandchewin chimes immersiveengineering immersivepetroleum'.split()
rows='''
Licowitch casts hex|甘草女巫施放咒术
Licowitch casts peppermints|甘草女巫施放薄荷糖
Licowitch summons monster|甘草女巫召唤怪物
Licowitch celebrates|甘草女巫庆祝
Licowitch cries|甘草女巫哀嚎
Licowitch grunts|甘草女巫闷哼
Licowitch cackles|甘草女巫咯咯怪笑
Ninni - Fusion|Ninni - 融合
Ninni - Tasty|Ninni - 美味
%1$s was punctured to death|%1$s 被刺穿而死
%1$s got caught in bramble whilst trying to escape %2$s|%1$s 在试图逃离 %2$s 时被荆棘缠住了
%1$s was steamed alive|%1$s 被活活蒸熟了
%1$s took a fatal steam bath due to %2$s|%1$s 因 %2$s 而享受了一场致命的蒸汽浴
Tim Rurkowski - Wanderer|Tim Rurkowski - 漫游者
Blood drips|血液滴落
Pus Bubble pops|脓液气泡破裂
Spider Egg breaks|蜘蛛卵破裂
I've got Zirconia pants|我有氧化锆裤子
Do You Like How I Dance?|你喜欢我的舞姿吗？
Foil|箔片
hatsondogs - Analogue|hatsondogs - 模拟
RENREN - Epilogue|RENREN - 尾声
Chef|厨师
Embedded|嵌入
Exsanguinated|失血殆尽
Isolation|孤立
Knight|骑士
Noir|黑色电影
Pit|深坑
prototype_701|原型机 701
Squirmy|蠕动
Starry Night|星夜
The Enigma|谜团
Bottle a Void Soul with a Glass Bottle|使用玻璃瓶收集虚空之魂
Bottle O'Void Souls|虚空之魂瓶
Visit the Catacombs Structure|探索地下墓穴结构
The Lost Souls|迷失的灵魂
Fly through a geyser burst with an Elytra|使用鞘翅飞过喷发的间歇泉
Inverse Rocketry|反向火箭技术
Visit the Glowshroom Forest biome|探索荧光菇森林生物群系
Luminous Depths|发光的深处
Give a Crystal Husk a Diamond|给予死寂活晶一颗钻石
Back From the Dead!|起死回生！
Visit the Molten Cavern biome|探索熔融洞窟生物群系
It's Getting Hot in Here!|这里越来越热了！
Obtain a Forsaken Bronze Scrap from the Catacombs|从地下墓穴中获得遗弃青铜碎屑
Titan's Slag|泰坦熔渣
Obtain a Glowshroom Cap from a Glowshroom Monster|从荧光菇怪身上获得荧光菇帽子
Glow In the Dark|暗中发光
Thank you for installing Darker Depths!|感谢安装 Darker Depths！
Visit the Sandy Catacombs biome|探索砂质迷穴生物群系
Desert but Underground?|地下沙漠？
Set a Death Anchor with a Void Soul Requiem|使用虚空魂安魂曲设置死亡锚点
Soul Pact|灵魂契约
Use a Crystal Melon|使用水晶西瓜
Feel the POWAH!|感受力量！
Darkslate Pillar|暗板岩柱
Duskrock Pillar|暮色岩柱
Glimmering Vine Plant|微光藤蔓植株
Grimestone Pillar|沉垢岩柱
Mob Placer|生物放置器
Petrified Bookshelf|石化木书架
Petrified Hanging Sign|悬挂式石化木告示牌
Petrified Roots Plant|石化根植株
Scorched Remains|焦灼残骸
Block of Scorched Remains|焦灼残骸块
Scorcher Light Block|灼烧者光源方块
Reduces Stiletto dash cooldown by 25% per level.|每级使短剑冲刺冷却时间缩短 25%。
Dealing damage during a Stiletto dash instantly recharges dash cooldown.|在短剑冲刺期间造成伤害，会立即重置冲刺冷却。
Scorcher|灼烧者
Scorcher Spawn Egg|灼烧者刷怪蛋
Legacy item no longer obtainable.|旧版物品，现已无法获取。
Catch a Puff Bug in a bottle|用瓶子捕捉一只泡泡虫
Alien Bug Catcher|异星捕虫者
Eat a Bolloom Fruit|食用膨生莲果
Feelin' Floaty|飘飘然
Find an Eetle Nest|找到末影甲虫巢穴
An End Bug's Life|末地虫虫的生活
Find a Poise Forest|找到幽仪森林
A Poised Place|幽仪之地
Kill a Brood Eetle|击杀一只育母末影甲虫
End Exterminator|末地除虫者
Acquire a Booflo Vest|获得浮跃背心
Boofing Power|浮跃之力
Tame a Booflo by feeding it Bolloom Fruits and backing away to let it eat|喂浮跃牛蛙膨生莲果，然后退开让它进食，以驯服它
Inflatable Friend!|可充气的朋友！
Attach yourself with four or more bolloom balloons to float upwards|为自己系上至少四个膨生气球，向上漂浮
Up, Up and Away!|向上，飞向远方！
Chiseled Poise Bookshelf|雕纹幽仪木书架
Poise Hanging Sign|悬挂式幽仪木告示牌
Poise Wall Hanging Sign|墙上的悬挂式幽仪木告示牌
Trapped Poise Chest|幽仪木陷阱箱
RENREN - Kilobyte|RENREN - 千字节
Zonkey|斑驴
Zorse|斑马杂交马
Banner Pattern|旗帜图案
Helper|帮手
hatsondogs - Leaving Home|hatsondogs - 离家
RENREN - Slabrave|RENREN - 板鱼狂欢
Zonkey Spawn Egg|斑驴刷怪蛋
Zorse Spawn Egg|斑马杂交马刷怪蛋
Archive|档案
Bouquet|花束
In Plains Sight|平原视野
Lone Plum|孤独的李子
Marshpath|沼泽小径
Optimal Aerodynamics|最佳空气动力学
Snake Block|蛇形方块
The Place Within The Pines|松林深处
Yak charges|牦牛冲锋
Yak rams|牦牛撞击
Zonkey whinnies|斑驴嘶鸣
Zonkey dies|斑驴死亡
Zonkey eats|斑驴进食
Zonkey hurts|斑驴受伤
Zorse whinnies|斑马杂交马嘶鸣
Zorse dies|斑马杂交马死亡
Zorse eats|斑马杂交马进食
Zorse hurts|斑马杂交马受伤
Strawberry Fields|草莓田
Magic Beans|魔豆
RENREN - Hullabaloo|RENREN - 喧闹
Cone|甜筒
Dawn|黎明
Neapoleon|那不勒仑
Scream|呐喊
Eating|进食
rose - bumblebee|rose - 熊蜂
rose - rain|rose - 雨
rose - snow|rose - 雪
Al-lu Pine|阿卢松
Aurorae|极光
Cliffside|悬崖边
Dress Codes|着装规范
Ecotonal Pareidolia|生态交错带的幻视
Hearth Rug|壁炉地毯
The Foils|箔片
Berries|浆果
Bread|面包
Wheat Bread|小麦面包
Cooked Beef|熟牛肉
Cooked Chicken|熟鸡肉
Cooked Eggs|熟鸡蛋
Cooked Fishes|熟鱼
Cooked Cod|熟鳕鱼
Cooked Salmon|熟鲑鱼
Cooked Mutton|熟羊肉
Cooked Pork|熟猪肉
Cabbage Crops|卷心菜作物
Onion Crops|洋葱作物
Tomato Crops|番茄作物
Wheat Dough|小麦面团
Eggs|鸡蛋
Grains|谷物
Rice Grains|稻米
Wheat Grains|小麦
Milk|牛奶
Milk Buckets|牛奶桶
Milk Bottles|牛奶瓶
Pasta|意面
Raw Beef|生牛肉
Raw Chicken|生鸡肉
Raw Eggs|生鸡蛋
Raw Fishes|生鱼
Raw Cod|生鳕鱼
Raw Salmon|生鲑鱼
Tropical Fish|热带鱼
Raw Meat|生肉
Raw Mutton|生羊肉
Raw Pork|生猪肉
Salad Ingredients|沙拉食材
Cabbage Salad Ingredients|卷心菜沙拉食材
Vegetables|蔬菜
Beetroots|甜菜根
Carrots|胡萝卜
Potatoes|马铃薯
Tomatoes|番茄
Fake Meatloaf|仿制肉糕
Glazed Arachnid Limbs|蜜汁节肢
Potted Gossypium|棉花盆栽
It's too sticky to put your hand in!|太黏了，无法把手伸进去！
Lingering Potion of Mining Fatigue|滞留型挖掘疲劳药水
Potion of Mining Fatigue|挖掘疲劳药水
Kultik - Aesthetica|Kultik - 美学
Kultik - Arcane Elegy|Kultik - 奥术挽歌
Cthonic Exchange|冥界交换
Grotesque Expulsion|怪诞驱逐
Hexing Transmission|咒术传递
Idle Mending|静息修复
Manabound Enhancement|魔力束缚增幅
Marine Spoil|海洋馈赠
Terran Unearthing|大地发掘
Bright|明亮
Dim|昏暗
Faded|褪色
Vague|模糊
Vivid|鲜明
Warped Time|扭曲时间
Aesthetica|美学
Arcane elegy|奥术挽歌
Completed ritual ambience|已完成仪式的环境音
Ritual absorbs item|仪式吸收物品
Ritual absorbs spirit|仪式吸收精魂
Ritual beginning ambience|仪式开始的环境音
Ritual begins|仪式开始
Ritual completed|仪式完成
Ritual evolution ambience|仪式进化的环境音
Ritual evolves|仪式进化
Ritual forms|仪式形成
Screem - Gloomper Anthem|Screem - 阴郁者之歌
Screem - Limax Maximus|Screem - 巨蛞蝓
Screem - Mammoth|Screem - 猛犸
Screem - Relict|Screem - 遗存
%smin|%s 分钟
Customizable|可自定义
%1$s IF / tick|%1$s IF / 刻
The Ace|王牌
Ancient|远古
Angel's Thesis|天使的纲领
Argo|阿尔戈
Astartes|阿斯塔特
Love them both|两者皆爱
Crimson Lotus|绯红莲花
Dark Fire|暗火
Dominator|支配者
Dragon's Breath|龙息
Erruption|喷发
Exia|能天使
Eyas|雏鹰
Felix|菲利克斯
Fox|狐狸
Boys love Boys|男孩爱男孩
Glacis|冰川
Harrowed|受难者
Hawk|鹰
Hollow|空心
The Kindled|燃火者
Girls love Girls|女孩爱女孩
Locus|轨迹
Lusus Naturae|自然异形
Magnum|马格南
Mass Fusion|质量聚变
Matrix|矩阵
Microshark|微型鲨鱼
Netherforged|下界锻造
Normandy|诺曼底
OmniTool|万能工具
Phoenix|凤凰
Regal|皇家
Rosequartz|蔷薇石英
Sharkface|鲨鱼脸
Sponsor|赞助者
Sunstrike|日击
Sutherland|萨瑟兰
Taken|夺取者
Terra|大地
Break the Cis-tem|打破顺性别体系
Twili|暮光族
Usurper|篡位者
Vanguard|先锋
Vault-Tec|避难所科技
WAAAGH!|哇啊啊！
Warbird|战鸟
360 No-Scope|360 度不开镜
An|一处
'''
exact=dict(line.split('|',1) for line in rows.strip().splitlines())
colors={'Black':'黑色','Blue':'蓝色','Brown':'棕色','Cyan':'青色','Gray':'灰色','Green':'绿色','Light Blue':'淡蓝色','Light Gray':'淡灰色','Lime':'黄绿色','Magenta':'品红色','Orange':'橙色','Pink':'粉色','Purple':'紫色','Red':'红色','White':'白色','Yellow':'黄色'}
exact.update({c+' Helper':zh+'帮手' for c,zh in colors.items()})
out,excluded,residual={},{},{}
for ns in namespaces:
    out[ns],excluded[ns],residual[ns]={},{},{}
    for key,en in pending.get(ns,{}).items():
        if key.endswith('.author') or '.commendations.' in key or '.tuning_fork.note.' in key or en in {'mB','%s°C','%s FE','-%s','+%s','%1$s: %2$s/%3$smB','%1$s %2$s mB','%1$s%%'}:
            excluded[ns][key]={'english':en,'reason':'author_credit_musical_note_or_unit'}
        elif en in exact:
            out[ns][key]=exact[en]
        else:
            residual[ns][key]=en
for name,data in [('manual_mod_translations_terms_extra.json',out),('manual_mod_exclusions_terms_extra.json',excluded),('manual_terms_extra_residual.json',residual)]:
    (BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print({'translated':sum(map(len,out.values())),'excluded':sum(map(len,excluded.values())),'remaining':sum(map(len,residual.values()))})
