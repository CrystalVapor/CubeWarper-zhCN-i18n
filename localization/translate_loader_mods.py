import json,re
from pathlib import Path
root=Path(__file__).parent
missing=json.loads((root/'missing_zh_cn.json').read_text('utf-8'))
names=['clanginghowl','unusual_furniture','incision','infernalexp','delightfulcreators']
table={}
def add(en,zh): table[en]=zh
def pairs(text):
    for line in text.strip().splitlines():
        en,zh=line.split('=',1); add(en.strip(),zh.strip())
pairs('''
Acacia=金合欢木
Bamboo=竹
Birch=白桦木
Cherry=樱花木
Crimson=绯红木
Crimson Planks=绯红木板
Dark Oak=深色橡木
Jungle=丛林木
Mangrove=红树木
Oak=橡木
Spruce=云杉木
Warped=诡异
Warped Planks=诡异木板
Black=黑色
Blue=蓝色
Light=浅色
Brown=棕色
Cyan=青色
Gray=灰色
Green=绿色
Light Blue=淡蓝色
Light Gray=淡灰色
Lime=黄绿色
Magenta=品红色
Orange=橙色
Pink=粉红色
Purple=紫色
Red=红色
White=白色
Yellow=黄色
Carved=雕刻
Bench=长椅
Beam=梁
Chair=椅子
Celling Lamp=吸顶灯
Coffee Table=茶几
Drawer=抽屉
Open Riser Stairs=开放式楼梯
Railing=栏杆
Shelf=置物架
Stool=凳子
Table=桌子
Curtain=窗帘
Sofa=沙发
Cat Plush=猫咪毛绒玩偶
Cow Plush=牛毛绒玩偶
Pig Plush=猪毛绒玩偶
Cattail=香蒲
Small Cattail=小香蒲
Blackboard Menu=黑板菜单
Blackstone Pot=黑石花盆
Danger Barrier=危险隔离栏
Decorated Iron Beam=装饰铁梁
Toolbox=工具箱
Emergency Fire Hydrant=应急消防栓
Fire Hydrant=消防栓
Floor Lamp Decoration=落地灯装饰
Fudge Pot=软糖花盆
Greek Pot=希腊式花盆
Hanging Pot=悬挂花盆
Iron Beam=铁梁
Huge Pot=巨型花盆
Industrial Coffee Table=工业茶几
Industrial Table=工业桌
Street Lantern=路灯
Large Hanging Pot=大型悬挂花盆
Manhole=检修井盖
Bag of Mushrooms=蘑菇袋
Mystery Furniture Crate=神秘家具箱
Bag of Pebbles=鹅卵石袋
Poster=海报
Works Barrier=施工隔离栏
Scum=浮沫
Small Lily Pad=小睡莲
Sphere Lantern=球形灯笼
Wooden Floor Lamp=木制落地灯
Stone Pot=石制花盆
Tall Terracota Pot=高陶瓦花盆
Trash=垃圾
Bag of Tropical Plants=热带植物袋
Bauhaus Pot=包豪斯式花盆
Wall Mushroom Patch=壁挂蘑菇丛
Wall Tropical Plant=壁挂热带植物
Warning Barrier=警示隔离栏
Bag of Water Plants=水生植物袋
Wooden Barrier=木制隔离栏
Wooden Clock=木制时钟
Wooden Hanging Pot=木制悬挂花盆
Sit=座位
Place items here!=将物品放在这里！
Inventory=物品栏
Classic=经典
Item Rotation Settings=物品旋转设置
Random=随机
Found a bug? Suggestions? Furniture ideas?=发现了错误？有建议或家具设计想法？
UnusualSquad.com/discord=UnusualSquad.com/discord
squeak=吱呀声
Right Click with a Wrench to toggle redstone mode=手持扳手右键点击以切换红石模式
Mystery Crate item=神秘箱中的物品
Right Click to open=右键点击打开
Right Click to change the number of arms=右键点击以调整灯臂数量
React to the day cycle=根据昼夜变化切换状态
Placable on dirt, pots and walls=可放置在泥土、花盆和墙面上
Give an non craftable piece of furniture=提供一件无法合成的家具
Has 7 random variations=具有 7 种随机变体
Placable on dirt and water=可放置在泥土和水面上
Stackable=可堆叠
Apple Cider=苹果酒
Baked Cod Stew=烤鳕鱼炖菜
Beef Stew=炖牛肉
Beetroot Soup=甜菜汤
Bone Broth=骨头汤
Chicken Soup=鸡汤
Cooked Rice=米饭
Dog Food=狗粮
Fish Stew=炖鱼
Glow Berry Custard=发光浆果奶冻
Hot Cocoa=热可可
Melon Juice=西瓜汁
Mushroom Stew=蘑菇煲
Noodle Soup=汤面
Pumpkin Soup=南瓜汤
Rabbit Stew=兔肉煲
Ratatouille=普罗旺斯杂烩
Tomato Sauce=番茄酱
Vegetable Soup=蔬菜汤
Mechanical Cutter=机械切割机
Delightful Creators=机械美食家
Apple Pie=苹果派
Bacon And Eggs=培根煎蛋
Bacon Sandwich=培根三明治
Chicken Sandwich=鸡肉三明治
Dumplings=饺子
Egg Sandwich=鸡蛋三明治
Fried Rice=炒饭
Fruit Salad=水果沙拉
Grilled Salmon=烤鲑鱼
Hamburger=汉堡
Honey Glazed Ham=蜜汁火腿
Horse Feed=马饲料
Mixed Salad=混合沙拉
Mushroom Rice=蘑菇饭
Mutton Wrap=羊肉卷
Nether Salad=下界沙拉
Pasta Dish=意大利面
Pasta With Meatballs=肉丸意大利面
Pasta With Mutton Chop=羊排意大利面
Pumpkin Pie=南瓜派
Rice Roll Medley=什锦饭卷
Roast Chicken=烤全鸡
Roasted Mutton Chops=烤羊排
Shepherds Pie=牧羊人派
Squid Ink Pasta=墨鱼汁意大利面
Steak And Potatoes=牛排配马铃薯
stuffed potato=填馅马铃薯
Stuffed Pumpkin=填馅南瓜
Sweet Berry Cheesecake=甜浆果芝士蛋糕
Vegetable Noodles=蔬菜面
Almost done=即将完工
Grit, spit, and a whole lot of duct tape!=决心、汗水，再加上大量胶带！
Culinary engineer=烹饪工程师
Application of engineering knowledge in cooking!=将工程知识应用于烹饪！
Culinary inventions are waiting for you!=烹饪发明正等着你！
Cutting Items with the Mechanical Cutter=使用机械切割机切割物品
The Mechanical Cutter can process cutting board recipes on items provided beneath it=机械切割机可以按照砧板配方加工下方的物品
The Input items can be dropped or placed on a Depot under the Cutter=原料可以直接丢在切割机下方，也可以放在下方的置物台上
When items are provided on a belt...=当物品通过传送带运来时……
The Cutter will hold and process them automatically=切割机会自动固定并加工这些物品
Cut in a Mechanical Cutter=使用机械切割机切割
Cutting=切割
Barrier of Extraterrestrial Activity=地外活动屏障
Cryogenic Icicle=低温冰锥
Hanging Technoflesh=悬垂机械血肉
Blaze Fuel Cylinder=烈焰燃料罐
Broken Crystal Former=损坏的晶体生成器
Broken Steel Lamp=损坏的钢灯
Burnished Extraterrestrial Stone=抛光地外石
Calcite Tile=方解石瓦
Calcite Tiles=方解石瓦
Carved Extraterrestrial Stone Bricks=雕纹地外石砖
Carved Fireproof Steel=雕纹耐火钢
Carved Steel Plate=雕纹钢板
Charged Extraterrestrial Stone Bricks=充能地外石砖
Consummate Nest=完备巢穴
Corrugated Steel=波纹钢
Cracked Calcite Tiles=裂纹方解石瓦
Cryogenic Frost=低温霜
Crystal Former=晶体生成器
Damaged Carved Steel Plate=破损雕纹钢板
Damaged Steel Plate=破损钢板
Extraterrestrial Activity Radar=地外活动雷达
Extraterrestrial Column=地外石柱
Extraterrestrial Energy Cluster=地外能量晶簇
Extraterrestrial Energy Crystal=地外能量晶体
Extraterrestrial Pebble=地外卵石
Extraterrestrial Steel=地外钢
Extraterrestrial Steel Grate=地外钢格栅
Extraterrestrial Steel Grate Panel=地外钢格栅板
Extraterrestrial Steel Ore=地外钢矿石
Extraterrestrial Stone=地外石
Extraterrestrial Stone Brick=地外石砖
Extraterrestrial Stone Bricks=地外石砖
Fireproof Steel=耐火钢
Flame Spewer=火焰喷射器
Frozen Technoflesh=冻结机械血肉
Huge Extraterrestrial Energy Cluster=巨型地外能量晶簇
Incandescent Extraterrestrial Stone=炽热地外石
Meteorite Steel Ore=陨石钢矿石
Motion Sensor=运动传感器
Nerve Endings=神经末梢
Raw Extraterrestrial Steel=粗地外钢
Redstone Cable=红石电缆
Redstone Cable Distributor=红石电缆分配器
Redstone Steel Lamp=红石钢灯
Smooth Extraterrestrial Stone=平滑地外石
Stationary Charging Station=固定充电站
Steel Bridge=钢桥
Steel Lamp=钢灯
Steel Plate=钢板
Steel Rod=钢杆
Technoflesh=机械血肉
Technoflesh Membrane=机械血肉膜
Technoflesh Nest=机械血肉巢穴
Tubular Technoflesh=管状机械血肉
Feet=脚部
Heart=心脏
Legs=腿部
When on feet:=穿在脚上时：
When on heart:=装在心脏处时：
When on legs:=穿在腿上时：
Attraction=吸引
Beyond Flesh=超越血肉
Cosmic Irradiation=宇宙辐照
Deep Burn=深度灼伤
Enlightened=显形
Internal Heat=内热
Neurotoxin=神经毒素
Overdrive=超载
Sawing Up Health=生命锯削
Weakened Defense=防御削弱
Chain Burn=连锁燃烧
Ecological Energy=生态能源
Energy Efficiency=能源效率
Exceeding The Limit=突破极限
Fuel Burst=燃料爆发
Fuel Saving=节省燃料
Full Power=全功率
Killer Charge=击杀充能
Napalm Stream=凝固汽油流
Soul Burner=灵魂燃烧
Tunnel Driller=隧道钻掘
Blood Clot=血凝块
Blood Spreader=鲜血散播者
Blood Trail=血迹
Bloody Copy=血肉复制体
Carcass=尸骸
Extraterrestrial Reaper=地外收割者
Flesh Maiden=血肉少女
Heart of Decay=腐败之心
Hematoma=血肿
Prowler=潜行者
Extraterrestrial Small Meteorite=地外小陨石
Spit=唾液
Advanced Chainsaw=高级链锯
Advanced Chainsword=高级链锯剑
Advanced Electronics=高级电子元件
Advanced Energy Battery=高级能量电池
Advanced Hand Drill=高级手持钻机
Attraction Device=吸引装置
Battery Panel=电池面板
Blaze Burner=烈焰燃烧器
Blaze Fuel=烈焰燃料
Bloody Battery=血能电池
Chainsaw Teeth=链锯锯齿
Chunk of Technoflesh=机械血肉碎块
Cryogenic Fuel=低温燃料
Diamond Diode=钻石二极管
Drill Bit=钻头
Energy Barrier Generator=能量屏障发生器
Energy Battery=能量电池
Energy Fiber=能量纤维
Energy Glove=能量手套
Energy-Intensive Battery=高容量电池
Extraterrestrial Axe=地外斧
Extraterrestrial Hammer=地外锤
Extraterrestrial Hoe=地外锄
Extraterrestrial Pickaxe=地外镐
Extraterrestrial Shovel=地外锹
Extraterrestrial Steel Ingot=地外钢锭
Extraterrestrial Steel Nugget=地外钢粒
Extraterrestrial Steel Plate=地外钢板
Extraterrestrial Sword=地外剑
Fireproof Steel Coating=耐火钢涂层
Flamethrower=火焰喷射器
Hematoma Lump=血肿块
Industrial Adjustable Wrench=工业活动扳手
Jet Boots=喷气靴
Large Extraterrestrial Energy Cluster=大型地外能量晶簇
Medium Extraterrestrial Energy Cluster=中型地外能量晶簇
Netherrack Shavings=下界岩碎屑
Piece of Extraterrestrial Steel=地外钢碎片
Portable Charger=便携充电器
Reanimation=复苏
Reanimator=复苏器
Redstone Wire=红石导线
Small Energy Battery=小型能量电池
Small Extraterrestrial Energy Cluster=小型地外能量晶簇
Techno Heart=机械心脏
Techno Optics=机械光学组件
Tendon Strengthener=肌腱强化器
X-Ray Goggles=X 射线护目镜
Clanging Howl=铿锵嚎声
Curio Activate=激活饰品
Energy capacity:=能量容量：
Fuel:=燃料：
While equipped:=装备时：
Press Shift to show tooltip=按住 Shift 查看说明
This gadget does not have enough energy=此装置的能量不足
The tool does not have enough energy=此工具的能量不足
Flamethrower is low on fuel=火焰喷射器的燃料不足
Immunity to slowness=免疫缓慢效果
Meteor shower is currently occurring=当前正在发生流星雨
Meteor shower will occur tonight=今晚将发生流星雨
Next meteor shower will occur in %s days=下一场流星雨将在 %s 天后发生
Next meteor shower will occur in 1 day=下一场流星雨将在 1 天后发生
Meteor shower is already occuring!=流星雨已经在发生！
Meteor shower is already about to occur!=流星雨已经即将发生！
World is not compatible!=此世界不兼容！
Set a meteor shower to occur on upcoming night=已设置流星雨于下一个夜晚发生
Started a meteor shower=已开始流星雨
No meteor shower is occurring!=当前没有流星雨！
Stopped current meteor shower=已停止当前的流星雨
Stopped upcoming meteor shower=已取消即将发生的流星雨
%1$s has been incinerated by %2$s=%1$s 被 %2$s 烧成了灰烬
%1$s has been incinerated by %2$s using %3$s=%1$s 被 %2$s 使用 %3$s 烧成了灰烬
%1$s was impaled by icicle=%1$s 被冰锥刺穿了
%1$s was impaled by icicle while fighting %3$s=%1$s 在与 %3$s 战斗时被冰锥刺穿了
%1$s was struck by %2$s=%1$s 遭到了 %2$s 的电击
%1$s was struck by %2$s using %3$s=%1$s 被 %2$s 使用 %3$s 电击了
%1$s's nervous system has shut down=%1$s 的神经系统停止了运作
%1$s's nervous system shuts down while fighting %2$s=%1$s 在与 %2$s 战斗时神经系统停止了运作
Entities within 20 blocks will follow, or target if monster, the affected.=20 格内的实体会跟随效果持有者，怪物则会将其作为攻击目标。
Certain affected will transform into a techno-flesh creature after effect nearly finishes.=部分效果持有者会在效果即将结束时转变为机械血肉生物。
Decreases max health by 15%% and attack damage by 10%%; higher levels decreases further.=最大生命值降低 15%%，攻击伤害降低 10%%；效果等级越高，降幅越大。
Increases incoming fire damage by 60%%.=受到的火焰伤害增加 60%%。
Affected will glow green and receive 30%% more damage from physical damage.=效果持有者会发出绿色光芒，受到的物理伤害增加 30%%。
Emits non-destructive explosion that gives effect, and sets fire, to other entities.=产生不破坏方块的爆炸，使其他实体着火并获得此效果。
Inflicts damage over time, when moving; higher levels do more damage per second.=移动时持续受到伤害；效果等级越高，每秒伤害越高。
Increases melee damage by 4 and movement speed by 45%%.=近战伤害增加 4，移动速度增加 45%%。
Decreases max health by 5%%; higher levels decreases further.=最大生命值降低 5%%；效果等级越高，降幅越大。
Decreases armor by 40%%; higher levels decreases further.=护甲值降低 40%%；效果等级越高，降幅越大。
You may not rest now; a meteor shower is occurring=现在无法休息，正在发生流星雨
The cosmos calmed down...=宇宙恢复了平静……
Discharged=放电声
Drilling=钻孔声
Electric Shock=电击声
Energy barrier impact=能量屏障受到冲击
Overdrive starts=超载启动
Infection=感染声
Injection=注射声
Malfunctioning electrics=电气故障声
Meteorite impact=陨石撞击声
Smoke releases=烟雾喷出
Rapid tearing of flesh=血肉快速撕裂声
Flesh whipping=血肉鞭打声
Flesh rupturing=血肉正在破裂
Flesh ruptures=血肉破裂
Howl of technoflesh=机械血肉嚎叫
Techno Flesh=机械血肉
Calcium Legos=钙质积木
Fall into the maws of the Eroded Yard=落入侵蚀庭园的巨口之中
Mom's Spagetti=妈妈的意大利面
Consume intestines=食用肠子
Eroded Yard=侵蚀庭园
Sediment Peaks=沉积山峰
Blinking Hamstring=眨动肌腱
Intestines=肠子
Blood Sprout=血芽
Carrion=腐肉
Carrion Eye=腐肉眼
Weatherrack=风化下界岩
Clottage=凝血岩
Clottage Brick=凝血岩砖
Clottage Bricks=凝血岩砖
Conductor Nerve=传导神经
Eyebulb=眼球茎
Goreshed=血染岩
Gory Weatherrack Bricks=血染风化下界岩砖
Gory Brick=血染砖
Gummy Trapdoor=胶质活板门
Hamstring=肌腱
Incision Carrion=切口腐肉
Incisor Growth=门齿增生体
Lens Glass=晶状体玻璃
Lens Glass Pane=晶状体玻璃板
Carrion Maw=腐肉巨口
Mooch=寄食体
Nerve (Temporary Blockmodel)=神经（临时方块模型）
Staring Door=凝视之门
Stitched Carrion=缝合腐肉
Tarnished Bars=锈蚀栏杆
Tarnished=锈蚀
Tarnished Shingle=锈蚀瓦
Tarnished Shingles=锈蚀瓦
Incision=切口
Boiling Tongue=沸腾舌头
Eyeball Yolk=眼球卵黄
Stomach=胃
Vile Fang=邪恶獠牙
Whoopie Cushion=放屁坐垫
acid hit=酸液击中
purger dies=清除者死亡
purger gurgles=清除者发出咕噜声
purger hurts=清除者受伤
purger pukes=清除者呕吐
seer dies=先知死亡
seer hisses=先知嘶鸣
seer hurts=先知受伤
whoopie cushion farts=放屁坐垫发出屁声
Basalt Sand=玄武岩沙
Polished Basalt=磨制玄武岩
Polished Basalt Brick=磨制玄武岩砖
Polished Basalt Bricks=磨制玄武岩砖
Shimmer Stone=微光石
Shimmer Stone Brick=微光石砖
Shimmer Stone Bricks=微光石砖
Dullstone=黯淡石
Dimstone=暗光石
Dwarf Spruce with Glowlight Torches=带荧光火把的矮云杉
Dwarf Spruce Plant with Glowlight Torches=带荧光火把的矮云杉植株
Glimmer Gravel=微光沙砾
Glowlight Brazier=荧光火盆
Glowlight Campfire=荧光营火
Glowlight Fire=荧光火焰
Glowlight Glass=荧光玻璃
Glowlight Glass Pane=荧光玻璃板
Glowlight Jack o'Lantern=荧光南瓜灯
Glowlight Lantern=荧光灯笼
Glowlight Torch=荧光火把
Hollowblight=枯萎空心菌
Hollowbright=明亮空心菌
Hollowlight=发光空心菌
Hollownight=暗夜空心菌
Large Glowlight Jack o'Lantern Slice=大型荧光南瓜灯片
Luminous=发光
Phosphor Hollowlight=磷光空心菌
Phosphor Shroomlight Tear=磷光菌光体之泪
Glowstone=荧石
Shimmer Sand=微光沙
Shroomblight Tear=枯萎菌光体之泪
Shroombright Tear=明亮菌光体之泪
Shroomlight Tear=菌光体之泪
Shroomnight Tear=暗夜菌光体之泪
Volatile Geyser=易爆喷泉
Waxed Glowstone=涂蜡荧石
You are already in the Nether!=你已经在下界了！
No safe spot found.=未找到安全地点。
The Nether dimension could not be found!=无法找到下界维度！
Teleported safely to the Nether!=已安全传送至下界！
Disarming=缴械
Illuminating=照明
Lashing=鞭笞
Leaping=跃进
Chance to cause mobs to drop their held item, or disable a player's held item for a short duration.=有概率让生物丢下手持物品，或短暂禁用玩家的手持物品。
Applies the Luminous effect to the target. Incompatible with Fire Aspect.=使目标获得发光效果。与火焰附加互斥。
Increases the damage dealt when attacking with this weapon.=提高使用此武器攻击时造成的伤害。
Propels the wielder forward when used in the air, or causes them to rebound off the target upon a successful hit.=在空中使用时使持有者向前冲刺，成功击中目标时则使其反弹。
Glowsilk Arrow=荧丝箭
Dullrocks=黯淡石块
Glowcoke=荧光焦炭
Bottle of Glowsilk Moth=荧丝蛾瓶
Glowsilk String=荧丝线
Infernal Expansion=下界扩展
Warped Shell=诡异甲壳
Glowstone Canyon=荧石峡谷
The Fallen Ones=堕落者
Blindsight=盲视兽
Glowsilk Moth=荧丝蛾
Glowsquito=荧光蚊
Voline=熔岩兽
Glowsquito Temptation Items=荧光蚊诱引物品
Voline Food=熔岩兽食物
Kill a Blindsight while afflicted with Luminous=在受到发光效果影响时击杀一只盲视兽
Deer in Headlights=灯下惊鹿
Freeze a sleeping Voline with a snowball=使用雪球冻结一只睡着的熔岩兽
Freeze, Punk!=冻住吧，小子！
Catch a baby Voline in a Lava Bucket=使用熔岩桶捕获一只幼年熔岩兽
Hot Pocket=炽热口袋
Feed a baby Voline enough Magma Cream to make it reach adulthood=喂给幼年熔岩兽足够的岩浆膏，使其成长为成年熔岩兽
Magma Mia!=岩浆妈妈咪呀！
Activate a Volatile Geyser using Redstone=使用红石激活易爆喷泉
Pressure Cooker=高压锅
Whip cracks=鞭子抽响
Client Settings=客户端设置
Common Settings=通用设置
Geyser Content=喷泉设置
Geyser Steam Height=喷泉蒸汽高度
Determines the maximum height of the steam particles produced by the geyser.=设置喷泉产生的蒸汽粒子的最大高度。
Miscellaneous Content=杂项设置
Glowsilk Bow Speed=荧丝弓速度
Determines the speed at which arrows are fired from the Glowsilk Bow.=设置荧丝弓射出箭矢的速度。
Luminous Fungus Activate Distance=发光菌激活距离
Determines the radius in blocks around Luminous Fungus that will cause them to light up.=设置发光菌周围触发其发光的半径，单位为格。
Mob Interactions Content=生物互动设置
Blindsight Eat Baby Mobs=盲视兽吞食幼年生物
If enabled, Blindsights will target and eat baby mobs.=启用后，盲视兽会攻击并吞食幼年生物。
Blindsight Extinguish Fire=盲视兽灭火
If enabled, Blindsights will stomp out fire sources.=启用后，盲视兽会踩灭火源。
Glowsquito Block Sucking=荧光蚊吸食方块
Determines if Glowsquitos should drink from Glowstone and Shroomlight blocks.=设置荧光蚊是否吸食荧石和菌光体方块。
Voline Content=熔岩兽设置
Voline Get Big=熔岩兽成长
If enabled, Volines will grow in size when they eat Magma Cream.=启用后，熔岩兽食用岩浆膏会长大。
Voline Magma Cream Amount=熔岩兽所需岩浆膏数量
Determines the amount of Magma Cream a Voline needs to eat to grow.=设置熔岩兽成长所需食用的岩浆膏数量。
Voline Sleep When Fed=熔岩兽进食后睡眠
If enabled, Volines will fall asleep after eating Magma Cream.=启用后，熔岩兽食用岩浆膏后会睡着。
Voline Turn Into Geyser=熔岩兽转化为喷泉
If enabled, sleeping Volines will transform into Volatile Geysers when hit with a snowball.=启用后，睡着的熔岩兽被雪球击中时会转化为易爆喷泉。
World Generation Content=世界生成设置
Enable Buried Bone=启用埋藏骨骼
Determines whether Buried Bone will generate in the world and be placeable.=设置埋藏骨骼是否在世界中生成，以及是否可以放置。
Enable Planted Quartz=启用植生石英
Determines whether Planted Quartz will generate in the world and be placeable.=设置植生石英是否在世界中生成，以及是否可以放置。
Infernal Expansion Config=下界扩展配置
''')

suffixes={' Spawn Egg':'刷怪蛋',' Bucket':'桶',' Block':'块',' Slab':'台阶',' Stairs':'楼梯',' Stair':'楼梯',' Wall':'墙',' Door':'门',' Trapdoor':'活板门',' Button':'按钮',' Pressure Plate':'压力板',' Planks':'木板',' Fence Gate':'栅栏门',' Fence':'栅栏',' Hanging Sign':'悬挂告示牌',' Sign':'告示牌'}
prefixes={'Incomplete ':'未完成的','Block of ':'','Chiseled ':'錾制','Cracked ':'裂纹','Polished ':'磨制','Carved ':'雕纹','Lingering Potion of ':'滞留型','Splash Potion of ':'喷溅型','Potion of ':'','Arrow of ':''}
actions={' quakes':'震动',' spit':'吐出唾液',' steps':'脚步声',' cuts':'切割声',' idle':'空转声',' crackles':'噼啪作响',' closes':'关闭',' charges up':'充能',' ejects items':'喷出物品',' opens':'打开',' spawns':'生成',' dies':'死亡',' starts':'启动',' burns':'燃烧',' emission':'喷射声',' hurts':'受伤',' wheeze':'喘息声',' activate':'启动',' roars':'咆哮',' croaks':'鸣叫',' leaps':'跳跃',' licks':'舔舐',' flutters':'扑翼',' buzzes':'嗡嗡作响',' slurps':'吸食',' grunts':'哼叫'}

# This resolver only accepts entire display names and explicitly known affixes.
def translate(s,depth=0):
    if s in table:return table[s]
    if s=='' or re.fullmatch(r'[%\d\s/+:().-]+',s):return s
    if depth>5:return None
    if s.startswith('§'):
        prefix=re.match(r'^(?:§[0-9a-fklmnor])+',s).group()
        t=translate(s[len(prefix):],depth+1)
        if t is not None:return prefix+t
    if s.startswith('§f\ue800§r - '):return '§f\ue800§r - '+{'Furniture':'家具','Props':'装饰物','Building Blocks':'建筑方块'}[s.split(' - ')[1]]
    for affix,zh in sorted(suffixes.items(),key=lambda x:-len(x[0])):
        if s.endswith(affix):
            t=translate(s[:-len(affix)],depth+1)
            if t is not None:return t+zh
    for affix,zh in prefixes.items():
        if s.startswith(affix):
            t=translate(s[len(affix):],depth+1)
            if t is not None:
                if affix in ['Potion of ','Lingering Potion of ','Splash Potion of ']:return zh+t+'药水'
                if affix=='Arrow of ':return t+'之箭'
                if affix=='Block of ':return t+'块'
                return zh+t
    for material in ['Light Blue','Light Gray','Dark Oak','Acacia','Bamboo','Birch','Cherry','Crimson','Jungle','Mangrove','Oak','Spruce','Warped','Black','Blue','Light','Brown','Cyan','Gray','Green','Lime','Magenta','Orange','Pink','Purple','Red','White','Yellow']:
        if s.startswith(material+' '):
            t=translate(s[len(material)+1:],depth+1)
            if t is not None:return table[material]+t
    for affix,zh in actions.items():
        if s.endswith(affix):
            t=translate(s[:-len(affix)],depth+1)
            if t is not None:return t+zh
    return None

pairs('''
Steel=钢
Copper Celling Lamp=铜吸顶灯
%s/%s=%s/%s
Chainsaw cuts=链锯切割声
Chainsaw idle=链锯空转声
Techno Flesh attacks=机械血肉攻击
Thin Vericose Stalk (Temporary Blockmodel)=细静脉曲张茎（临时方块模型）
Vericose Stalk=静脉曲张茎
Weatherrack Brick=风化下界岩砖
Weatherrack Bricks=风化下界岩砖
Corrosive Door=腐蚀门
Corrosive Plate=腐蚀板
Corrosive Shingle=腐蚀瓦
Creative Icon=创造模式图标
Eyeball=眼球
Gorey Weatherrack Bricks=血染风化下界岩砖
Gorey Brick=血染砖
Molar Carrion=臼齿腐肉
%1$s was consumed by the Eroded Yard=%1$s 被侵蚀庭园吞噬了
%1$s was killed by %2$s using %3$s=%1$s 被 %2$s 使用 %3$s 杀死了
%1$s died whilst trying to escape %2$s=%1$s 在试图逃离 %2$s 时死亡了
Consumption=吞噬
Cooldown=冷却
Melting=熔化
Purger=清除者
Seer=先知
Skeletoncultist=骷髅教徒
???=???
witherskeletonspawn=凋灵骷髅生成体
Burial Knife=埋葬刀
Puke=呕吐物
Nekomaster=Nekomaster
LazTheArtist=LazTheArtist
Applies to Flamethrowers. Gives entities Internal Heat that will cause them to emit a blast upon death that gives effect to other nearby entities.=适用于火焰喷射器。使实体获得内热效果，在死亡时产生爆炸，并将此效果传递给附近的其他实体。
Applies to all advanced tools. Passively charges when the holder is exposed to direct sunlight. When the holder is struck by lightning, charges 400 energy=适用于所有高级工具。持有者直接暴露于阳光下时会被动充能。持有者遭到雷击时充入 400 能量。
Applies to all advanced tools. For each level, reduces energy consumption by one.=适用于所有高级工具。每级减少 1 点能量消耗。
Applies to Advanced Chainswords. Increase melee damage by 0.5 and increases max Sawing Up Health effect level stack to 10.=适用于高级链锯剑。近战伤害增加 0.5，并将生命锯削效果的最高叠加等级提高至 10。
Applies to Flamethrowers. Change the Flamethrower to only shoot a short burst that damages and pushes away entities. Increases fuel consumption.=适用于火焰喷射器。将喷射方式改为短促爆发，对实体造成伤害并将其推开。增加燃料消耗。
Applies to Flamethrowers. For each level, reduces fuel consumption by one.=适用于火焰喷射器。每级减少 1 点燃料消耗。
Applies to Advanced Chainsaws. Makes chainsaw to rapidly damage enemies in front when using it, slowly causing it to overheat. Increases energy consumption.=适用于高级链锯。使用时会快速伤害前方的敌人，并逐渐过热。增加能量消耗。
Applies to Advanced Chainswords. Cause an electrical surge after killing, damaging other entities and charges all advanced tools in inventory.=适用于高级链锯剑。击杀后产生电涌，伤害其他实体，并为物品栏中的所有高级工具充能。
Applies to Flamethrowers. For each level, increases flamethrower damage and fire duration. Increases fuel consumption.=适用于火焰喷射器。每级提高伤害并延长燃烧时间。增加燃料消耗。
Applies to Advanced Chainsaws. Grants Overdrive effect when using item, increasing movement speed and damage. Increases energy consumption.=适用于高级链锯。使用时获得超载效果，提高移动速度和伤害。增加能量消耗。
Applies to Flamethrowers. Increases flame damage by one and inflicts slowness for a short time. Nearby entities dying by fire fuels held flamethrower a bit.=适用于火焰喷射器。火焰伤害增加 1，并施加短暂的缓慢效果。附近实体被火焰烧死时，为手持的火焰喷射器补充少量燃料。
Applies to Advanced Drills. Dig in a 3x3 area unless sneaking. Increases energy consumption.=适用于高级钻机。在未潜行时挖掘 3x3 区域。增加能量消耗。
''')
specific={'clanginghowl':{}}
def cl(key,zh):specific['clanginghowl'][key]=zh
for key,zh in {
'info.clanginghowl.block.barrier':'§7保护半径为 128x128 格的区域免受流星雨影响',
'info.clanginghowl.block.broken_former':'§7在周围形成无法控制的寒冷区域',
'info.clanginghowl.block.charger':'§7逐渐补充放置其上的高级工具的§e能量§7储备。',
'info.clanginghowl.block.flame_spewer.1':'§8启用时会喷出一道火焰',
'info.clanginghowl.block.flame_spewer.2':'§8施加红石信号或使用工业活动扳手可以开启和关闭火焰喷射器',
'info.clanginghowl.block.former.0':'§8启用时会在周围形成小片寒冷区域。',
'info.clanginghowl.block.former.1':'§8启用时，§7地外能量晶体§8会逐渐在其表面生长。生物群系越冷，晶体能够长得越大。',
'info.clanginghowl.block.former.2':'§8施加红石信号或使用工业活动扳手可以开启和关闭晶体生成器。',
'info.clanginghowl.block.radar':'§8在流星雨期间输出红石信号',
'info.clanginghowl.block.sensor':'§8当视野中 15 格以内存在实体时输出红石信号',
'info.clanginghowl.event.meteor_shower.start':'§c你感觉有东西正在从天上落下……',
'info.clanginghowl.item.attraction_device':'§7右键点击使你获得§9吸引 (0:25) §7效果，并消耗装置的耐久度',
'info.clanginghowl.item.barrier.1':'§7受到的伤害降低 §b50§b%',
'info.clanginghowl.item.barrier.2':'§7能量消耗较高，并随你受到的伤害增加。',
'info.clanginghowl.item.barrier.3':'§7可使用便携充电器或固定充电站为此装置充能',
'info.clanginghowl.item.battery.1':'§c+15% 受到的伤害',
'info.clanginghowl.item.battery.2':'§7造成或受到伤害时，为物品栏中的其他装置和高级工具充能，充能量等于造成或受到的伤害量',
'info.clanginghowl.item.boots.1':'§9+1 护甲值',
'info.clanginghowl.item.boots.2':'§9-35% 摔落伤害',
'info.clanginghowl.item.boots.3':'§7在空中可以进行§6火箭跳跃§7。火箭跳跃会消耗燃料，并使此装置进入短暂冷却。',
'info.clanginghowl.item.boots.4':'§7装置燃料耗尽后使用时，若物品栏中有烈焰燃料罐，会自动补充燃料并消耗一个燃料罐。',
'info.clanginghowl.item.chainsaw.0':'§7按住鼠标右键可以快速采掘木质和植物方块。',
'info.clanginghowl.item.chainsaw.1':'§7每秒使用都会消耗能量。可使用便携充电器或固定充电站为此工具充能。',
'info.clanginghowl.item.chainsword.0':'§7暴击使敌人的最大生命值降低 §45§4%§7，连续暴击会增强此效果，最高可降低 §425§4%。',
'info.clanginghowl.item.chainsword.1':'§7攻击对§4机械血肉§7生物造成更高伤害。',
'info.clanginghowl.item.chainsword.2':'§7攻击会消耗能量。可使用便携充电器或固定充电站为此工具充能。',
'info.clanginghowl.item.charger.0':'§7被动将内部存储的电池中的§e能量§7输送至你物品栏中的高级工具。',
'info.clanginghowl.item.charger.1':'§8右键点击以打开电池存储界面。',
'info.clanginghowl.item.drill.0':'§7按住鼠标右键可以快速采掘石质和土质方块。',
'info.clanginghowl.item.drill.1':'§7每秒使用都会消耗能量。可使用便携充电器或固定充电站为此工具充能。',
'info.clanginghowl.item.extraterrestrial':'§8-攻击使敌人获得§5宇宙辐照§8效果，并对§4机械血肉§8生物造成更高伤害。',
'info.clanginghowl.item.flamethrower.0':'§7按住鼠标右键会喷出火焰，焚烧前方的一切。被火焰击中的敌人受到的火焰伤害会提高。',
'info.clanginghowl.item.flamethrower.1':'§7每秒使用都会消耗燃料。若物品栏中有§e烈焰燃料罐§7，可以替换燃料罐。',
'info.clanginghowl.item.glove.1':'§9+1 攻击伤害',
'info.clanginghowl.item.glove.2':'§7暴击时产生§b电涌§7，造成范围伤害，使所有命中的实体减速，并为你其他的装置和高级工具充入 20 点能量。',
'info.clanginghowl.item.glove.3':'§7触发时，此装置进入短暂冷却并损失部分储存能量。可使用便携充电器或固定充电站为其充能',
'info.clanginghowl.item.hammer':'§8-右键点击部分工业方块会使其损坏。',
'info.clanginghowl.item.hematoma_lump':'§9吸引 (0:15)',
'info.clanginghowl.item.reanimator.1':'§7激活时产生电涌，使你免受致命伤害；之后完全放电并进入短暂冷却。',
'info.clanginghowl.item.reanimator.2':'§7复苏器需要充满能量并结束冷却后才能再次工作。可使用便携充电器或固定充电站为其充能',
'info.clanginghowl.item.tendon.2':'§6+10§6% §7移动速度',
'info.clanginghowl.item.tendon.3':'§6+15§6% §7疾跑时额外移动速度，以及 §6+50§6% §7疾跑时跳跃高度。',
'info.clanginghowl.item.tendon.4':'§7此装置在疾跑时消耗能量。可使用便携充电器或固定充电站为其充能',
'info.clanginghowl.item.wrench.0':'§8-右键点击部分工业方块可以将其§2开启§8和§4关闭§8，也可以修复其损坏的版本。',
'info.clanginghowl.item.wrench.1':'§8-也可以右键点击以修复损坏的傀儡和机器人。',
'info.clanginghowl.item.x_ray.0':'§7潜行时按下 §2%s §7键可以开启或关闭此装置。',
'info.clanginghowl.item.x_ray.1':'§7启用时，你会获得夜视效果，并使视线内的其他生物§a显形§7，能够透过障碍物看到它们。显形的生物受到的物理伤害增加 30%，暴露其弱点。',
'info.clanginghowl.item.x_ray.2':'§7每秒使用都会消耗能量。可使用便携充电器或固定充电站为此装置充能',
}.items():cl(key,zh)
# Prefer established mod terminology for complete names. Context-specific nouns
# in the hand-authored descriptions are reconciled separately below.
effective=json.loads((root/'effective_zh_cn.json').read_text('utf-8'))
for source_ns in ['farmersdelight','infernalexp']:
    for key,row in effective.get(source_ns,{}).items():
        if key.startswith(('item.','block.','entity.','effect.')) and re.search(r'[\u4e00-\u9fff]',row['chinese']):
            if source_ns=='farmersdelight' and row['english'] not in table:continue
            table[row['english']]=row['chinese']
for en,zh in list(table.items()):
    if any(word in en for word in ['Voline','Blindsight','Luminous','Buried Bone','Planted Quartz']):
        for old,new in [('熔岩兽','熔岩吞噬兽'),('盲视兽','黑石盲蛙'),('发光菌','荧光菌'),('发光效果','荧光效果'),('埋藏骨骼','埋骨'),('植生石英','下界石英')]:
            zh=zh.replace(old,new)
        table[en]=zh
pairs('''
Example Block=示例方块
Example Item=示例物品
Example Mod Tab=示例模组物品栏
Balm=Balm
You do not have %s installed. Please install %s version %s to play on this server.=你尚未安装 %s。请安装 %s 的 %s 版本以进入此服务器。
The server does not have %s installed. Please remove the mod from your game or install it on the server as well.=服务器尚未安装 %s。请从客户端移除此模组，或同时在服务器上安装它。
Version mismatch for %s. The server expects version %s, but you currently have %s installed. Please install the correct version.=%s 的版本不匹配。服务器要求 %s 版本，而你当前安装的是 %s。请安装正确版本。
Black Dyes=黑色染料
Blue Dyes=蓝色染料
Brown Dyes=棕色染料
Cooking Oil=食用油
Cyan Dyes=青色染料
Diamonds=钻石
Dyes=染料
Eggs=鸡蛋
Emeralds=绿宝石
Gems=宝石
Gold Nuggets=金粒
Gray Dyes=灰色染料
Green Dyes=绿色染料
Ingots=锭
Iron Ingots=铁锭
Iron Nuggets=铁粒
Light Blue Dyes=淡蓝色染料
Light Gray Dyes=淡灰色染料
Lime Dyes=黄绿色染料
Magenta Dyes=品红色染料
Nuggets=粒
Orange Dyes=橙色染料
Ores=矿石
Pink Dyes=粉红色染料
Purple Dyes=紫色染料
Red Dyes=红色染料
Stones=石头
White Dyes=白色染料
Wooden Chests=木箱
Wooden Rods=木棒
Yellow Dyes=黄色染料
Certain Questing Additions=任务扩展
Settings for specific animations=特定动画设置
Quest panel appearance animation=任务面板出现动画
Animation on hovering over panel buttons=鼠标悬停于面板按钮时的动画
Animation on hovering over a quest=鼠标悬停于任务时的动画
Smooth chapter panel opening animation=平滑的章节面板展开动画
Smooth zooming in and out of the quest panel=平滑缩放任务面板
Appearance settings=外观设置
Button hover glow opacity (0-255)=按钮悬停光晕不透明度 (0-255)
Quest hover glow opacity (0-255)=任务悬停光晕不透明度 (0-255)
Shader background for quest screen=任务界面着色器背景
Smooth animations with easing functions=使用缓动函数平滑动画
Entity opacity=实体不透明度
Auto rotate=自动旋转
Entity=实体
Entity ID / spec=实体 ID / 规格
Unknown entity: %s=未知实体：%s
Look at cursor=看向光标
Entity draw order=实体绘制顺序
Player name=玩家名称
Show player name=显示玩家名称
Player skin=玩家皮肤
Entity tint=实体染色
any=任意
none=无
Basalt Generator=玄武岩生成器
Cobblestone Generator=圆石生成器
Stone Generator=石头生成器
Blacklisted Dimensions:=维度黑名单：
Dimensions=维度
Max Y:=最大 Y 坐标：
Min Y:=最小 Y 坐标：
Weight:=权重：
Whitelisted Dimensions:=维度白名单：
Command Executor Block=命令执行方块
Soul Goop=灵魂黏液
Fan behind Acid=酸液后方的鼓风机
Bulk Corroding=批量腐蚀
Charred  Remnant=焦黑残骸
Depth Charge=深水炸弹
Notor Gizmo=诺托装置
Occult Gem=秘术宝石
Polymer Plate=聚合物板
Telecore=传送核心
Default Difficulty=默认难度
The default difficulty selected for newly created worlds.=新建世界默认选择的难度。
Default Resource Packs=默认资源包
Resource pack IDs to have enabled by default on the first run.=首次运行时默认启用的资源包 ID。
Lock Difficulty=锁定难度
Set to true if the difficulty for new world's should be locked to the specific default. This cannot be unlocked by players without external tools! Probably a bad idea. I don't recommend. Why am I adding this option?=设为 true 时，新世界的难度将锁定为指定的默认值。玩家需要外部工具才能解除锁定！这可能不是一个好主意，我不建议这样做。我为什么要添加这个选项？
Default Options=默认选项
Exasperatingly Nimble=灵敏得令人焦躁
Unreasonably Quick=快得超乎常理
Lightning Speed=闪电般的速度
Maximally Performant=极致性能
Fastest table in the West=西部最快的工作台
Unnervingly Responsive=响应快得令人不安
Faster than the average table=比普通工作台更快
Firefly Bush=萤火虫灌木丛
Firefly Bush Backport=萤火虫灌木丛移植
Fireflies buzz=萤火虫嗡嗡作响
Failed to process config from server: %s=处理服务器配置失败：%s
(Made for a newer version of Fusion)=（适用于较新版本的 Fusion）
No=否
Yes=是
Do you want to enable the resource pack anyway?=仍要启用此资源包吗？
Installed version:=已安装版本：
This resource pack is made for a newer version of Fusion and may not work correctly with the currently installed version of Fusion.=此资源包适用于较新版本的 Fusion，可能无法在当前安装的 Fusion 版本中正常工作。
Required version:=所需版本：
Fusion version warning=Fusion 版本警告
Fertilizer=肥料
Turn on rain to see the fertilizer model!=开启下雨以查看肥料模型！
Gecko Habitat=壁虎栖息地
Bat=蝙蝠
Bike=自行车
Cool Kid=酷小孩
Fake Glass=仿制玻璃
Gremlin=捣蛋鬼
Mutant Zombie=变异僵尸
Gave %1$s to the entity=已给予实体 %1$s
Parasite=寄生虫
Race Car=赛车
Gecko Armor Boots=壁虎盔甲靴子
Gecko Armor Chestplate=壁虎盔甲胸甲
Gecko Armor Helmet=壁虎盔甲头盔
Gecko Armor Leggings=壁虎盔甲护腿
Jack-in-the-Box=惊吓盒
Opening the Jack-in-the-Box!=正在打开惊吓盒！
Wolf Armor Boots=狼盔甲靴子
Wolf Armor Chestplate=狼盔甲胸甲
Wolf Armor Helmet=狼盔甲头盔
Wolf Armor Leggings=狼盔甲护腿
Geckolib Examples=Geckolib 示例
Adaptive UI Scaling=自适应界面缩放
Debug=调试
Advanced Debugging Settings for Guide development=指南开发的高级调试设置
Full Width Layout=全宽布局
User Interface=用户界面
Guides=指南
Ignore Guide Translations=忽略指南译文
Always load the original version of GuideME guides, regardless of the currently selected UI language=始终加载 GuideME 指南的原始版本，不受当前界面语言影响
Debug GUI Overlays=调试界面覆盖层
GuideME Configuration=GuideME 配置
Blasting=高炉冶炼
Close=关闭
Close Full Width View=关闭全宽视图
This command only works in single-player.=此命令仅可在单人游戏中使用。
Content from=内容来源
Crafting=合成
Full Width View=全宽视图
Hide Annotations=隐藏注释
Go back one page=返回上一页
Go forward one page=前往下一页
Hold [%s] to open guide=按住 [%s] 打开指南
Invalid guide id set: %s=设置的指南 ID 无效：%s
No guide id set=尚未设置指南 ID
Reset View=重置视图
Runs Command:=执行命令：
Search=搜索
Enter a Search Query=输入搜索内容
No Results=无结果
Crafting (Shapeless)=合成（无序）
Show Annotations=显示注释
Smelting=熔炼
Zoom In=放大
Zoom Out=缩小
Guide=指南
GuideME=GuideME
Open Guide for Items=打开物品指南
Multiblock with Hammer=使用工程师锤形成多方块结构
Magic Damage=魔法伤害
Magic Proficiency=魔法熟练度
Magic Resistance=魔法抗性
World setup for not-annoying development work=为方便开发而设置世界
Command Successful, enjoy your screenshake.=命令执行成功，享受画面震动吧。
All World Events are already frozen=所有世界事件均已冻结
Froze %s World Events=已冻结 %s 个世界事件
The specified World Event is already frozen=指定的世界事件已冻结
Froze the specified World Event: %s=已冻结指定的世界事件：%s
All World Events of type %s are already frozen=所有 %s 类型的世界事件均已冻结
Froze %s World Events of type %s=已冻结 %s 个 %s 类型的世界事件
There are %s active World Event(s)=共有 %s 个活动中的世界事件
%s | %s | UUID: %s=%s | %s | UUID: %s
%s event(s) are frozen=已有 %s 个事件冻结
There are no active World Events=没有活动中的世界事件
Could not remove any World Events=未能移除任何世界事件
Removed %s Active World Event(s)=已移除 %s 个活动中的世界事件
The specified World Event is already inactive=指定的世界事件已处于非活动状态
Removed the specified World Event: %s=已移除指定的世界事件：%s
No active World Events of type %s were found=未找到活动中的 %s 类型世界事件
Removed %s World Events of type %s=已移除 %s 个 %s 类型的世界事件
No World Events are currently frozen=当前没有冻结的世界事件
Unfroze %s World Events=已解除 %s 个世界事件的冻结
The specified World Event is not frozen=指定的世界事件尚未冻结
Unfroze the specified World Event: %s=已解除指定世界事件的冻结：%s
No World Events of type %s are currently frozen=当前没有冻结的 %s 类型世界事件
Unfroze %s World Events of type %s=已解除 %s 个 %s 类型世界事件的冻结
Fire Overlay Offset=火焰覆盖层偏移
Offsets the fire overlay effect downwards, clearing up your vision.=将火焰覆盖层向下偏移，以改善视野。
Screenshake Intensity=画面震动强度
Controls how much screenshake is applied to your screen.=控制画面震动的强度。
Mana=魔力
Bucket of Mana=魔力桶
Moyai=摩艾石像
Moyai-shaped=摩艾石像形
Yo, Angelo=哟，安杰罗
Don't ever talk to me or my son ever again=再也不要和我或我的儿子说话
Hmm Gum Gum=嗯，嚼嚼
Moyai Moves=摩艾石像移动
Moyai Thinks=摩艾石像思考
Moyai Boom=摩艾石像轰鸣
Hold %s to copy=按住 %s 复制
Copied!=已复制！
Copy Pack Id=复制资源包 ID
Hold %s to reload=按住 %s 重新加载
Reloaded!=已重新加载！
Reload Settings=重新加载设置
Hold %s to toggle=按住 %s 切换
Toggled!=已切换！
Toggle Pack Ids=切换资源包 ID 显示
Backup completed in %s (%s | %s)=备份完成，用时 %s (%s | %s)
Backup started...=备份已开始……
Backups paused=备份已暂停
Merging backups completed successfully=备份合并成功
A merge operation is already in progress=合并操作正在进行中
Not only modified files are being backed up, please check your configuration file=当前备份范围包含未修改的文件，请检查配置文件
Not enough space on disk to create backup. Aborted!=磁盘空间不足，无法创建备份。已中止！
rain on ametyst=雨落在紫水晶上
rain on fabric=雨落在织物上
Rain on leaves=雨落在树叶上
Rain on glass=雨落在玻璃上
Rain sizzling=雨水滋滋作响
Rain on metal=雨落在金属上
Rain on sand=雨落在沙子上
Rain splashing=雨水飞溅
Rain on wood=雨落在木头上
Thunder rumbling=雷声隆隆
Thunder Strike=雷击声
Distant Thunder=远处雷声
Nearby Thunder=附近雷声
Could not determine parameters=无法确定参数
Parameters at position %s %s %s: %s=位置 %s %s %s 的参数：%s
''')
# Keep explicitly meaningful trailing spacing used by concatenated UI labels.
for en in ['Max Y: ','Min Y: ','Weight: ']:table[en]=table[en.rstrip()]+' '
table[' Distant Thunder']=' 远处雷声'
names += [ns for ns,rows in missing.items() if rows and len(rows)<=40 and not effective.get(ns) and ns not in names and ns not in ['geckolib','lodestone']]
pairs('''
Allowed models=允许的模型
All=全部
Known only (Mostly Vanilla / OptiFine)=仅已知模型（主要为原版 / OptiFine）
Determines what models EMF will try to interact with. Note: this is not perfect, some mods just use the vanilla namespace ids and there is little EMF can do about it=设置 EMF 尝试处理的模型。注意：此判断存在局限，部分模组直接使用原版命名空间 ID，EMF 对此难以处理。
Unknown only (Mostly Modded)=仅未知模型（主要为模组模型）
Armor copies custom animations=盔甲跟随自定义动画
In 1.21.9+ armor no longer naturally copies the custom animations of the base model, this replicates that old behaviour.=在 1.21.9 及更高版本中，盔甲不再自动跟随基础模型的自定义动画，此选项恢复此前的行为。
Compiled animation math=编译动画数学表达式
Will cause log spam, you probably don't need this unless the dev asked you to provide a log with this.=会产生大量日志，通常仅在开发者要求提供此类日志时需要启用。
Export rotations=导出旋转值
Log compiled math state=记录已编译数学表达式的状态
Parrot shoulder follows player animations=肩部鹦鹉跟随玩家动画
Will automatically make parrot shoulder position follow the animated player position by default, this is not equivalent to the `parrot_left` and `parrot_right` attachment points as these will not rotate.=默认使肩部鹦鹉的位置自动跟随玩家动画。此行为与 `parrot_left` 和 `parrot_right` 附着点不同，因为这些附着点不会旋转。
Sulfur Cube block default animation=硫磺立方体内部方块默认动画
Will automatically make Sulfur Cube internal blocks animate by default, this is equivalent to having a 'sulfur_cube_block' attachment in the model's 'cube' part with offset 0,0,0.=默认自动为硫磺立方体内部方块添加动画，相当于在模型的 'cube' 部件中设置偏移为 0,0,0 的 'sulfur_cube_block' 附着点。
Search...=搜索……
Random / Custom mobs settings=随机 / 自定义生物设置
§xYou need to select an action first!=§x请先选择一个操作！
FancyMenu Toast=FancyMenu 提示消息
Buddy=伙伴
+%s XP=+%s 经验
Browser initialization failed!=浏览器初始化失败！
Check the game log for details.=请查看游戏日志了解详情。
Browser is starting...=浏览器正在启动……
Waiting for Rinku to finish initializing.=正在等待 Rinku 完成初始化。
new_folder=新建文件夹
Glass, sandstone, bookshelves=玻璃、砂岩、书架
Default Connected Textures=默认连接纹理
Cull faces between glass panes=剔除玻璃板之间的面
Glass Pane Culling Fix=玻璃板面剔除修复
Amethyst Tiles=紫水晶瓦
Small Amethyst Tiles=小型紫水晶瓦
Void Steel Bars=虚空钢栏杆
Block of Void Steel=虚空钢块
Void Steel Ladder=虚空钢梯子
Void Steel Scaffolding=虚空钢脚手架
Direct Capture Mods=直接捕获模组
Color Picker=颜色选择器
Dropdown Chooser=下拉选择器
<blank>=<空白>
Night Vision=夜视
Reset the portal shape=重置传送门形状
Sculpt the portal=雕刻传送门
Resets the portal shape to the default rectangular shape=将传送门形状重置为默认矩形
Sculpts the portal shape by the blocks that it's intersecting with=根据与传送门相交的方块雕刻其形状
Discover cool features=探索精彩功能
Immersive Portals Peripherals=沉浸式传送门扩展
Portal Sculpted. Area Reduced: %s  Area Before: %s  Area After: %s=传送门雕刻完成。减少面积：%s  原始面积：%s  当前面积：%s
Running portal sculpting...=正在雕刻传送门……
Show Mid Point=显示中心点
Edge Radius=边界半径
Down Range=向下范围
1.18 Migration Done=已完成 1.18 迁移
Horizontal Range=水平范围
Ignore Layer=忽略层
Ignore Spawnlist=忽略生成列表
Safe Light Level=安全亮度
Simple Check=简单检查
Use Number Overlay=使用数字覆盖层
Update Interval (Frames)=更新间隔（帧）
Up Range=向上范围
Chunk: Edge Color=区块：边界颜色
Chunk: Grid Color=区块：网格颜色
Chunk: Thick Lines=区块：粗线条
Chunk: Line Width=区块：线宽
Chunk: Middle Color=区块：中心颜色
Spawn: Color=生成：颜色
Spawn: Line Width=生成：线宽
Spawn: Night Color=生成：夜间颜色
Spawn: Number Size=生成：数字大小
Spawn: Safe Color=生成：安全区域颜色
Search Custom=自定义搜索
Search Box Color=搜索框颜色
Enable Search=启用搜索
Max Search Results=最大搜索结果数
Slot Transparency=物品槽透明度
Slot Color=物品槽颜色
Search Tooltip=搜索提示信息
More Overlays Updated Settings=更多覆盖层更新版设置
Mood=氛围值
Drip Chance=滴落概率
Sound Category=声音类别
Use Dripstone Sounds=使用滴水石锥音效
Absolute Cinema=绝对电影
ESM: Anchor list not found; Creating empty Anchor list=ESM：未找到锚点列表；正在创建空列表
ESM: Muffled list not found; Creating empty Muffled list=ESM：未找到消音列表；正在创建空列表
''')
pending=json.loads((root/'pending_main.json').read_text('utf-8'))
client_names=['entity_model_features','entity_texture_features','fancymenu','continuity','createutilities','exposure','extremesoundmuffler','yet_another_config_lib_v3','immersive_portals','moreoverlays','pehkui','betterf3','waterdripsound','vista']
for ns in client_names:
    if ns not in names:names.append(ns)
    missing[ns]={key:missing[ns][key] for key in pending.get(ns,{})}
specific['entity_model_features']={
'entity_model_features.config.asmmaths.tooltip':'通常建议开启此选项。\n关闭后，动画系统会使用计算开销更大的表达式树，这种方式可能更适合调试。',
'entity_model_features.config.export_rotations.tooltip':'导出的 jem 模型通常应省略旋转值，因为模型会继承原版部件的旋转值\n 不过，部分模型编辑器可能需要包含这些值\n 此选项会在导出的 jem 文件中包含旋转值',
}
specific['entity_texture_features']={
'config.entity_texture_features.property_explanation.client_game_mode':'客户端玩家的游戏模式列表\n原版模式：0=生存，1=创造，2=冒险，3=旁观\n§aclientGameMode.<n>=<list>',
'config.entity_texture_features.property_explanation.difficulty':'难度列表\n原版难度：0=和平，1=简单，2=普通，3=困难\n§adifficulty.<n>=<list>',
'config.entity_texture_features.property_explanation.hardcore':'极限模式\n检查世界是否为极限模式\n§ahardcore.<n>=<true/false>',
'config.entity_texture_features.property_explanation.regional_difficulty':'区域难度列表\n 数值范围为 0.0 至 6.75，各区块不同\n 参见 https://minecraft.wiki/w/Difficulty#Regional_difficulty\n§aregionalDifficulty.<n>=<list>',
'config.entity_texture_features.property_explanation.resourcepack':'资源包\n检查各个已加载资源包的名称\n§aresourcepack.<n>=<resourcepack_list|regex|pattern>',
'config.entity_texture_features.property_explanation.usingShaders':'使用光影\n检查是否正在使用 Iris 光影\n§ausingShaders.<n>=<true/false>',
}
specific['extremesoundmuffler']={
'log.error.loadAnchorList':'ESM：加载锚点列表时出错：\\n %s',
'log.error.loadMuffledList':'ESM：加载消音列表时出错：\\n %s',
'log.error.saveAnchorList':'ESM：保存锚点列表时出错\\n %s',
'log.error.saveMuffledList':'ESM：保存消音列表时出错：\\n %s',
'main_screen.side_screen.radius_edit':'半径： ',
}
specific['waterdripsound']={'tooltip.config.waterdripsound.useDripstoneSounds':'启用时，使用 1.17 添加的滴水石锥\n 水滴 / 熔岩滴落音效。\n关闭时，使用此模组较早\n 版本中的音效。'}
for key,en in pending.get('pehkui',{}).items():
    kind='最大值' if 'Maximum' in en else '最小值'
    specific.setdefault('pehkui',{})[key]='缩放类型 '+en.split('scale type ')[1]+' 的'+kind
for ns in client_names:
    for key,row in missing[ns].items():
        en=row['english']
        literal=(ns=='vista' and '.tooltip' in key) or (ns=='vista' and key.endswith('.desc')) or any(w in key for w in ['.shortcut','.shortcuts.','.shadertoy','.markdown','.cape.']) or (ns=='betterf3' and key!='text.betterf3.line.mood') or (ns=='exposure' and key!='exposure.configuration.force_direct_capture_default_mods') or re.fullmatch(r'%s%%',en)
        if literal: specific.setdefault(ns,{})[key]=en
out={};unresolved={}
for ns in names:
    out[ns]={};unresolved[ns]={}
    for key,row in missing[ns].items():
        t=specific.get(ns,{}).get(key,translate(row['english']))
        if t is None:unresolved[ns][key]=row['english']
        else:out[ns][key]=t
(root/'manual_mod_translations_loader.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'loader_unresolved.json').write_text(json.dumps(unresolved,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Translated:',{ns:len(v) for ns,v in out.items()})
print('Unresolved:',{ns:len(v) for ns,v in unresolved.items()})
for ns,rows in out.items():
    for key,zh in rows.items():
        en=missing[ns][key]['english']
        assert re.findall(r'§[0-9a-fklmnor]',en)==re.findall(r'§[0-9a-fklmnor]',zh),(ns,key,'format')
        assert re.findall(r'%(?:\d+\$)?[sd]|%%',en)==re.findall(r'%(?:\d+\$)?[sd]|%%',zh),(ns,key,'parameter')
