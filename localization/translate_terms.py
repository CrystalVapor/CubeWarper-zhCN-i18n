"""Reviewed exact-string translations and bounded item-name composition."""
import json, re
from collections import defaultdict
from pathlib import Path
BASE = Path(__file__).resolve().parent
missing = json.loads((BASE / 'missing_zh_cn.json').read_text(encoding='utf8'))
effective = json.loads((BASE / 'effective_zh_cn.json').read_text(encoding='utf8'))
index = defaultdict(set)
for values in effective.values():
    for value in values.values():
        if re.search(r'[\u3400-\u9fff]', value['chinese']):
            index[value['english']].add(value['chinese'])

def table(text):
    return dict(line.split('|', 1) for line in text.strip().splitlines() if line.strip())

exact = table('''
Checkered Tile Block|棋盘格瓷砖方块
Checkered Tile Slab|棋盘格瓷砖台阶
Checkered Tile Stairs|棋盘格瓷砖楼梯
Dimensional Lock|维度锁
Fragile Pot|易碎陶罐
Green Screen Block|绿幕方块
Inverted Dirt|反转泥土
Nullified Dirt|虚化泥土
Nullon Light|空子灯
Red Wallpaper|红色墙纸
Rope|绳索
Short Grass|矮草
Sky|天空
Skybox Missing|缺失天空盒
Meteor|陨石
ructures and things that straight |型结构，以及一些直接 
Mobs|生物
Buy|购买
Exchange|兑换
Microwave|微波炉
Play|播放
Midnight|午夜
Radio|收音机
Sorting Cabinet|分类柜
Off|关闭
Destroy|摧毁
Failure|失败
Single|单音
None|无
Note|音符
Meteor Event|陨石事件
Dog|狗
Missing|缺失
Sunflowers|向日葵
Glass shatters|玻璃破碎
Cough|咳嗽
Distant explosion|远处爆炸
Rain|降雨
Breakthrough|突破声
Parry|招架
Silence|寂静
Typing|打字声
Voice|语音
Phosphor Lantern|荧光粉灯笼
Phosphor Torch|荧光粉火把
Redstone Flux|红石通量
%1$s / %2$s mB|%1$s / %2$s mB
Activate the Alpha Core by using a diamond|使用钻石激活阿尔法核心
I'm The Alpha|我是阿尔法
Check out this new cave game!|来看看这款新的洞穴游戏！
Be in the presence of Anchor Stands|来到锚架附近
You Have Alerted The Horde|你惊动了群体
Slay a Doomwad|击杀一只厄运团
Faces Of Doom|厄运之面
Drink from a bottle of blood|喝下一瓶血液
NOT FUEL, NOT FUEL|不是燃料，不是燃料
Encounter The Delusioner.|遭遇妄想者。
Kinda delulu..|有点妄想……
Enter Alpha|进入阿尔法
We went too far|我们走得太远了
Enter The Furniture Store|进入家具商店
100% OFF!|全部免费！
Enter The Hub by finding a Hub Gateway|找到枢纽传送门并进入枢纽
Quite Dimensional Doors|颇具维度特色的门
Enter the minelands|进入矿地
I call them “cities”|我称其为城市
Explore all Alpha biomes|探索所有阿尔法生物群系
Nostalgia Slop|怀旧杂烩
Fling yourself to the moon|将自己弹射到月球
SPAAAAAACE!|太空！
Enter The Upturned|进入颠倒之地
Mankind Is Dead|人类已亡
Kill a displayant|击杀一只显示者
I'm Still Standing|我依然屹立
Kill a vain.|击杀一只虚妄者。
In vain|徒劳无功
Use rats as lab rats|将老鼠用作实验鼠
Lab Rats|实验鼠
Obtain Alpha Cobblestone|获得阿尔法圆石
Cave Game|洞穴游戏
Obtain a bloomer|获得一把盛放者
Ok Bloomer|好的，盛放者
Obtain a common compact disc|获得一张普通光盘
350 million copies|三亿五千万份
Obtain a rare compact disc|获得一张稀有光盘
Rare finds|稀有发现
Obtain a special compact disc|获得一张特殊光盘
One of a kind|独一无二
Obtain a coffe mug!|获得一杯咖啡！
Eeffoc...|啡咖……
Obtain the killing mace|获得杀戮钉锤
Calm down woody..|冷静点，伍迪……
Swim in acid|在酸液中游泳
Acid Trip|酸液之旅
Swim in blood|在血液中游泳
My lungs are iron|我的肺是铁打的
The wacky dimensions of Untagged & Untitled|Untagged & Untitled 的奇异维度
Dimensional Exploration|维度探索
Meatdow|血肉草甸
Peering Pines|窥视松林
Rows|行列
Aberrant Torch|异常火把
Aeral Land|空灵之地
Aeral Lava|空灵熔岩
Aeral Water|空灵之水
Alpha Cobble Support|阿尔法圆石支架
§7minecraft:§fmissing_texture_block|§7minecraft:§f缺失纹理方块
Ballpit Balls|球池彩球
Block Of Fate|命运方块
Box Fan|箱式风扇
Box Of Books|书箱
Can|罐头
Carved Stone|雕刻石
Cheese Fence gate|奶酪栅栏门
Cheese trapdoor|奶酪活板门
Clatterflower|喧响花
Clay Mine|黏土地雷
Crater Maker|弹坑制造器
§1Dealer|§1商人
Dimensional Sorting Cabinet|维度分类柜
Endless Town Generator Block|无尽城镇生成器方块
Eye Lilid|眼百合
Eyecube|眼立方
Forcefield|力场
Full Grass Block|完整草方块
Globe|地球仪
Hardflower|硬花
Hellfire Bush|地狱火灌木
Hellstone|地狱石
Epic Block|史诗方块
Iron Tubes Block|铁管方块
Lightpoint|光点
Liminal Void|阈限虚空
Mineolith|矿地巨石
Mineolith Base|矿地巨石基座
Blocks/§ffull§7/§fMissing/§fblack|方块/§f完整§7/§f缺失/§f黑色
Blocks/§ffull§7/§fMissing/§fpink|方块/§f完整§7/§f缺失/§f粉色
Glass§7_§fPane§7/§fMissing|玻璃§7_§f板§7/§f缺失
Mob Reactor|生物反应器
Mycirium|菌丝体
Nerval Bush|神经灌木
Nerveweed|神经草
Nothing|虚无
Slab Of Nothing|虚无台阶
Stairs Of Nothing|虚无楼梯
Nullon Sheets|空子板
Paper Trash|废纸
Parking Pole|停车柱
Potential|潜能
Slab Of Something|某物台阶
Stairs Of Something|某物楼梯
Underbark|幽层树皮
Underfed|幽层菇
Understalk|幽层菌柄
Underwood|幽层木
Wallpiercer|穿墙者
Wasted Potential|荒废的潜能
Zeropoint Walll|零点墙
%1$s has melted in a puddle of acid|%1$s 在一滩酸液中融化了
%1$s has melted in acid due to %2$s using %3$s|%1$s 因 %2$s 使用 %3$s 而在酸液中融化了
%1$s has melted in acid due to %2$s|%1$s 因 %2$s 而在酸液中融化了
%1$s bled out|%1$s 失血过多而亡
%1$s bled out due to %2$s using %3$s|%1$s 因 %2$s 使用 %3$s 而失血过多而亡
%1$s bled out whilst trying to escape %2$s|%1$s 在试图逃离 %2$s 时失血过多而亡
%1$s was flattened by a falling meteor|%1$s 被坠落的陨石压扁了
%1$s was found by obunga|%1$s 被奥邦加找到了
%1$s was found by obunga%2$s|%1$s 被奥邦加%2$s 找到了
%1$s burned in boiling blood|%1$s 在沸腾的血液中被烧死了
Bleeding|流血
Loading Terrain|加载地形
Parrying|招架中
Slipping|滑倒
AnXor|安克索尔
Anchor Stand|锚架
Clatter|喧响者
Cleeper|克利珀
Cleepers|克利珀
Delusioner|妄想者
Displayant|显示者
Doomwad|厄运团
Duplicant|复制体
Flinging Point|弹射点
Obunga|奥邦加
Patterpillar|踢踏毛虫
Redactor|删改者
SLime|史莱姆
Televiewer|电视观察者
UFX Beam|UFX 光束
UFX Square|UFX 方块
Vain|虚妄者
Weaving Couch|游走沙发
Minecraft Open Server Beta v0.3.1|Minecraft 开放服务器测试版 v0.3.1
close range.|近距离。
Go to page...|跳转至页面……
arning, this book has been created|学习后，本书编写而成
At some point after learning about|在了解一段时间之后
bookmarks that lead you to other|书签，可前往其他
to teach everyone about the basics|旨在向所有人介绍基础知识
in the world. Such as doors that|世界中。例如那些门会
tructures and things that straight |型结构，以及一些直接 
After a lot of exploration and le-|经过大量探索与学—
On the next page you will find|下一页可以找到
pages.|页面。
Players started noticing oddities|玩家开始发现异常现象
lead to seemingly endless megas-|通往似乎无穷无尽的大—
the world of §kMinecraft.|§kMinecraft 的世界。
up shouldn't happen.|出现本不应发生的事。
abilities like sprinting, bunnyh-|具备疾跑、连续跳—
glowing white faces.|发光的白色面孔。
Keep your distance and pick them |保持距离，将它们 
like cheese, which can be used to|例如奶酪，可用于
Non-players are player-like mobs|非玩家是类似玩家的生物
off one by one.|逐一解决。
or entities, observing them at|或实体，并在
oups, sharing player range and|成群结队，具有玩家的互动距离和
ping, and eating to heal.|跃以及进食回血等能力。
Rats are neutral cave rodents that|老鼠是中立的洞穴啮齿动物，会
tame them.|驯服它们。
Their fur drops upon death.|死亡时掉落毛皮。
They show interest in nearby items|它们对附近物品感兴趣
They’re dumb but dangerous in gr-|它们不聪明，但成—
with missing-texture bodies and|具有缺失纹理的身体和
1 MS skin....|一种 MS 皮肤……
EXCHANGE|兑换
Deal.err|交易.错误
Page 1|第 1 页
Page 2|第 2 页
§bConfetti Cannon: §rBuy if you like parties!!|§b彩纸礼炮：§r喜欢派对就买吧！
§bHyper Confetti Cannon: §r5x the usage!|§b超级彩纸礼炮：§r五倍使用次数！
§bCoffee: §rWho doesn't like coffee??|§b咖啡：§r谁会不喜欢咖啡呢？
Exchange compact discs for a different item|用光盘兑换其他物品
Exchange compact discs for XP or another form of currency|用光盘兑换经验或其他货币
§bTrumpet: §rI like making noise!|§b小号：§r我喜欢制造声音！
§bCassette Tape: §rMmmmusic..|§b盒式磁带：§r音——乐……
§bLarge Potion: §rWonder what it does...|§b变大药水：§r好奇它有什么作用……
EXchang.err|兑换.错误
Input.err|输入.错误
Coins appear here|硬币出现在此处
Exchange reward appears here|兑换奖励出现在此处
Input discs you want to exchange here|在此处放入要兑换的光盘
Input discs you want to sell here|在此处放入要出售的光盘
New Folder|新建文件夹
Hang on!|请稍候！
We're building terrain for you |正在为你生成地形 
Heat Up|加热
OGG Player|OGG 播放器
Toggle Rain|切换降雨
Default Skin|默认皮肤
Only compatible blocks work|仅兼容的方块有效
Propsetter|道具设置器
Player Comments|玩家评论
Certain actions will cause text to appear, similar to undertale|某些行为会触发文字显示，类似 Undertale
§9It's raining bombs: §rCleepers will naturally spawn in the overworld|§9炸弹雨：§r克利珀会在主世界自然生成
Wakka.chnl|瓦卡.频道
City.chnl|城市.频道
Golf.chnl|高尔夫.频道
Static.chnl|雪花.频道
Pow!|砰！
Put on a show|开始表演
Voice Selection|语音选择
Chat Voice Selection|聊天语音选择
Furniture Store Announcement Event|家具商店广播事件
Archive Rain Event|档案馆降雨事件
Bingledorp|宾格尔多普
Furniture Store Blackout Event|家具商店停电事件
Bloomer|盛放者
Bugging Stick|故障棒
literally a piece of land|确实是一块土地
Cassette Tape|盒式磁带
§dCassette Tape|§d盒式磁带
Cassette Tape?|盒式磁带？
Clay Bomb|黏土炸弹
Compact Disc|光盘
Confetti Cannon|彩纸礼炮
Cooked Flesh|熟血肉
Cooked Meatball|熟肉丸
Cooked Sausage|熟香肠
Crumpled Paper Ball|皱纸团
Dimensional USB|维度 U 盘
Erraxer|错误消除器
Executable|可执行文件
Firework Confetti Cannon|烟花彩纸礼炮
Hyper Confetti Cannon|超级彩纸礼炮
Epic Disc|史诗光盘
Job Application|求职申请
Meataxe|血肉斧
Nonnac Ittefnoc Repyh|炮礼纸彩级超
Items§7/§fNullpoint|物品§7/§f空点
Render Pearl|渲染珍珠
Mob Scrambler|生物扰乱器
Sharpshooter|神射手
Slipaxe|滑移斧
Splash Potion Of Big|喷溅型变大药水
Splash Potion Of Normal|喷溅型正常体型药水
Splash Potion Of Small|喷溅型缩小药水
Swurd|斯沃德剑
Mob Unscrambler|生物复原器
Unstable Compound|不稳定化合物
Vain Bone|虚妄者骨头
Untagged|未标记
UM: Building|UM：建筑
UM: Creative|UM：创造
UM: Functional|UM：功能
UM: Items|UM：物品
UM: Mobs|UM：生物
UM: Natural|UM：自然
UM: Tools|UM：工具
Operator Commands|管理员命令
Killing Mace Parry|杀戮钉锤招架
Open Vocal Ui|打开语音界面
No-Strike|无打击
Bricken|砖块
Chill|悠闲
Cleepet|克利珀宠物
Coucher De Soleil|日落
Gip|吉普
Granana|格拉纳纳
Hydrogen|氢
Loss|失落
Middle|中间
Rigged|操纵
Sanguinisch|血色
Sundown|日暮
Unpacked|已拆包
Wad|团块
Something is coming|有东西正在接近
Speaker announcement|扬声器广播
Ambient|环境音
Ambience|环境音
Acid flows|酸液流动
Chair is sat on|椅子被坐上
Clay mine activates|黏土地雷激活
Dimensional lock openns|维度锁开启
Fragile stone returns|易碎石复原
Metal barrel closes|金属桶关闭
Metal barrel opens|金属桶打开
Microwave dings|微波炉叮响
Microwave hums|微波炉嗡鸣
Mineolith chants|矿地巨石吟唱
Missing noises|缺失纹理发出声响
Mob reactor spawns|生物反应器生成生物
Nullified block noises|虚化方块发出声响
Cabinet closes|柜子关闭
Cabinet opens|柜子打开
Surface lamp turns off|表面灯熄灭
Surface lamp turns on|表面灯亮起
Button clicked|按钮被点击
Television noise|电视机发出声响
Television transforms|电视机变形
Vent cover used|通风口盖被使用
wuh oh!|糟糕！
Oh no, oweee, i cannot handle forks, owe, ouch! AAAAA AA A A A|糟了，痛死了，我受不了叉子，哎哟！啊啊啊啊！
Wallpiercer scans|穿墙者扫描
Chair creaks|椅子吱响
Dimension Entered|进入维度
Anger|愤怒声
Cannon ball hits|炮弹击中
Clatter hurts|喧响者受伤
Clatter exists|喧响者发出声响
Delusioner hurts|妄想者受伤
Delusioner breathes|妄想者呼吸
Thuds|沉闷撞击声
Horrific yell|恐怖的叫喊声
Doomwad clatters|厄运团喧响
Doomwad rattles|厄运团嘎嘎作响
Doomwad screams|厄运团尖叫
Duplicant attempts mitosis|复制体尝试有丝分裂
Duplicant dies|复制体死亡
Duplicant hurts|复制体受伤
Duplicant Clips|复制体穿模
Duplicant jumps|复制体跳跃
Non-player dies|非玩家死亡
Non-player hurts|非玩家受伤
Non-player communicates|非玩家交流
Mitosis|有丝分裂
Patterpillar hurts|踢踏毛虫受伤
Patterpillar oogles|踢踏毛虫发出声响
Rat hurts|老鼠受伤
Rat examines|老鼠观察
Something screams in agony|某个东西痛苦地尖叫
Something shifts position|某个东西转移位置
Vain dies|虚妄者死亡
Vain hurts|虚妄者受伤
Vain Rattles|虚妄者嘎嘎作响
Mystery opens|神秘之物开启
Microphone sing|麦克风传出歌声
Trumpet noise|小号发出声响
Acid rusts metal|酸液腐蚀金属
Acid emptied|酸液被倒出
Camera takes picture|相机拍照
Confetti pops|彩纸弹出
Cannon fires|炮发射
Paper ball hits|纸团击中
Paper ball thrown|纸团被投掷
Render pearl teleports|渲染珍珠传送
Scrambler used|扰乱器被使用
Scrambler Scrambles|扰乱器扰乱生物
Soap used|肥皂被使用
Trumpet makes music|小号奏乐
Bingledorp speaks|宾格尔多普说话
Meteor falls|陨石坠落
Meteor hits|陨石撞击
Mob is removed|生物被移除
Fling|弹射声
Heavy bleeding|大量出血
Item prints|物品打印
misc.jumpscare|突发惊吓声
Good luck|祝你好运
Mob mutates|生物变异
Odd noise|奇异声响
spop ittefnoC|出弹纸彩
Sharpshooter fires|神射手开火
Mob spawned|生物生成
Spawning in|正在生成
Something appears|某个东西出现
beautiful sounds that make you fly like the little butterfly you are|美妙的声音让你如小蝴蝶般飞翔
Music ends|音乐结束
horror|恐怖声
Yaaayyy!!|耶！
Something eats|某个东西进食
It speaks|它说话了
Harvest some Charcoal and Ash from a burnt Log Pile|从烧过的原木堆中采集木炭和灰烬
Flame Grilled|烈焰炙烤
Wear down a Survivalist's Tool to breaking point|将生存家工具用到损坏
I Didn't Hear No Bell!|我还没听到结束铃声！
Research all Bee Species|研究所有蜜蜂品种
Master Apiarist|养蜂大师
Research all Tree Species|研究所有树木品种
Master Arborist|树木培育大师
Apply some Refractory Wax to wood to make it fireproof!|在木材上涂抹耐火蜂蜡，使其耐火！
Non-Inflammable|耐火处理
Craft a Manual or Managed Farm|制作一座手动农场或自动农场
Farming Simulator|农场模拟器
Assemble a Multiblock Farm|搭建一座多方块农场
Feed the World!|养活全世界！
Obtain your first Drone, Princess or Queen|获得你的第一只雄蜂、公主蜂或蜂后
This Is Where The Series Ends...|本系列到此结束……
Collect all the different types of Honeycomb|收集所有种类的蜂窝
Honey, I'm Comb!|亲爱的，我带蜂窝回来了！
Collect all the different types of Fruit|收集所有种类的水果
The Fruits of my Labour|劳动的果实
Assemble an Alveary, a versatile beekeeping structure|搭建一座蜂房组，这是一种多用途养蜂设施
Al-very Nice!|蜂房组，真不错！
Acquire an upgrade for your Alveary|获得一项蜂房组升级
Make a House a Home|让蜂房成为家园
Craft a Portable Analyzer to help with identifying different specimens|制作便携式分析仪，帮助鉴定不同标本
iPad Kid|平板儿童
Craft a full set of Apiarists Armor to protect yourself against even the angriest of bees|制作一整套养蜂人护甲，以抵御最愤怒的蜜蜂
The Beekeeper|养蜂人
Craft an Apiary, which allows your bees to mutate into new species|制作蜂房，使蜜蜂可以突变为新品种
Beevolutionary!|蜜蜂进化！
Obtain and research a Grandidier's Baobab Sapling|获得并研究格氏猴面包树树苗
The Tree of Life|生命之树
Research a Bumble Bee, obtained by using a scoop on a wild bee|研究使用捕虫网从野生蜜蜂身上获取的熊蜂
Buzzy Bees!|嗡嗡蜜蜂！
Craft a Bee House for your bees to happily live and work in|制作简易蜂房，让蜜蜂在其中愉快地生活和工作
Bee House, Sweet Bee House|甜蜜的简易蜂房
Obtain a Bucket of Biomass|获得一桶生物质
Green Means Clean!|绿色意味着清洁！
Acquire some bronze ingots by alloying Copper and Tin in a Smelter|在熔炼炉中将铜和锡合金化，获得青铜锭
Lightly Bronzed|初识青铜
Craft a Burn Barrel to turn excess wood products into Ash|制作焚烧桶，将多余木制品变成灰烬
Ashes to Ashes|尘归尘，灰归灰
Craft some Tin Cans|制作一些锡罐
I Can, Can You?|我能装罐，你呢？
Craft a Carpenter|制作木工机
Next Level Crafting|更进一步的合成
Craft a Centrifuge|制作离心机
You Spin Me Right Round|旋转不停
Obtain and research a Chestnut Sapling|获得并研究栗树树苗
Roasting on an Open Fire|明火烘烤
Craft an Engine to power your machines|制作引擎，为机器供能
Powering Up|启动动力
Acquire an Escritoire, to help you discover more about the bee and tree species of this world|获得写字台，深入了解世界中的蜜蜂和树木品种
When Is a Raven Like a Writing Desk?|乌鸦何时像一张写字台？
Craft a Thermionic Fabricator|制作热电子加工台
Glass Crafting|玻璃加工
Turn some Apatite into Fertilizer|将磷灰石制成肥料
No Thanks, I Already Ate|谢谢，我已经吃过了
Successfully crossbreed your first new species of tree|成功杂交出你的第一个树木新品种
Branching Off|分枝发展
Get some Frames for use in your Apiaries|获取一些框架，用于蜂房
I've Been Framed!|我被装进框架了！
Obtain and research a Giant Sequoia Sapling|获得并研究巨型红杉树苗
Fee-Fi-Fo-Fum!|巨人之歌！
Obtain and research a Ginkgo Sapling from a sniffed-up Amber Fossil|从嗅探出的琥珀化石中获得并研究银杏树苗
The Living Fossil|活化石
Craft a Grafter to guarantee sapling drops from your trees|制作剪枝器，确保树叶掉落树苗
Minegraft|嫁接工艺
Process some Honeycomb into Honey Drops and Beeswax|将蜂窝加工成蜂蜜滴和蜂蜡
Honey (Sugar, Sugar)|蜂蜜（甜蜜，甜蜜）
Craft an Impregnated Casing|制作浸渍外壳
how casing get pragnent|外壳怎么浸渍了
Obtain and research a Jacaranda Sapling|获得并研究蓝花楹树苗
What Else Can I Do?|我还能做什么？
Obtain and research a Kauri Sapling|获得并研究贝壳杉树苗
Tane Mahuta|塔内马胡塔
Acquire a Bucket of Liquid Honey|获得一桶液态蜂蜜
Bee Juice|蜜蜂果汁
Obtain and research a Large-Leaved Mahogany Sapling|获得并研究大叶桃花心木树苗
That is Mahogany!|那可是桃花心木！
Craft a Moistener|制作加湿机
Moisturize Me!|给我保湿！
Research a Monastic Drone, acquired by trading with an Apiarist villager|研究与养蜂人村民交易获得的僧侣雄蜂
What a Deal!|成交！
Research a Pirate Drone, found washed up in a shipwreck|研究在沉船中发现的海盗雄蜂
Yellow-and-Blackbeard|黄黑胡子
Trade with an Arborist Villager to acquire a Proven Grafter|与树艺师村民交易，获得标定剪枝器
The Gift of the Graft|嫁接的馈赠
Trade with an Apiarist Villager to acquire a Proven Scoop|与养蜂人村民交易，获得标定捕虫网
Ol' Reliable|可靠老伙计
Research a Relic Drone, found preserved inside a sniffed-up Amber Fossil|研究保存在嗅探出的琥珀化石中的遗迹雄蜂
The Land Beefore Time|史前蜂地
Craft a Scoop, allowing you to collect wild bees|制作捕虫网，以收集野生蜜蜂
Here's the Scoop!|捕虫网来了！
Craft a Smelter, used for alloying metals|制作熔炼炉，用于熔炼金属合金
Alloy There!|合金来了！
Craft a Bee Smoker to stop wild bees from stinging you|制作驱蜂烟雾，防止野生蜜蜂蜇伤你
Zonked Out|熏得昏沉
Craft a Solar Panel|制作太阳能板
Walkin' on the Sun|漫步阳光下
Make some Spectacles to help with finding hives and pollinated leaves|制作眼镜，以帮助寻找蜂巢和授粉树叶
I See What's Going On Here...|我看清情况了……
Craft a Squeezer|制作榨汁机
Freshly Squeezed|新鲜压榨
Research a Steadfast Drone, found hidden deep underground|研究隐藏在地下深处的坚定雄蜂
Dungeon Flyer|地牢飞行者
Research a Valiant Drone, found hiding out in wild hives|研究藏在野生蜂巢中的勇者雄蜂
I'm Different!|我与众不同！
Obtain and research a White Willow Sapling|获得并研究白柳树苗
The Wind in the Willows|柳林风声
Craft a Worktable|制作工作站
Remember Me!|记住我！
Bring a bee from the Nether into the Overworld and research it after it transforms...|将一只蜜蜂从下界带到主世界，待其转化后进行研究……
Zombeefication|蜜蜂僵尸化
Complete a raid whilst wearing a full set of Apiarists Armor|穿着整套养蜂人护甲完成一次袭击
Sting Operation|蜂刺行动
Wind your clockwork engine just a little too much...|给发条引擎稍微多上些发条……
Wound Up|发条过紧
Use an Iodine Capsule or Dissipation Charge on a Rainmaker to start or stop the rain!|对造雨机使用碘酒胶囊或驱云药弹，开始或停止降雨！
Make It Rain!|让雨下起来！
Obtain your first research note|获得你的第一份研究笔记
Eureka!|发现了！
Big Green Cale|大型绿色蜡烛
Generates RF from liquid fuels.|消耗液体燃料产生 RF。
Gathers RF from attached solar panels.|收集连接的太阳能板产生的 RF。
Liquid Experience|液态经验
Molten Wax|熔融蜂蜡
Fluid Experience|液态经验
Fluid Wax|液态蜂蜡
Red Metal Lacquered Plating|红色涂漆金属板
Block of Silicon|硅块
Generates RF from the sun's rays.|利用阳光产生 RF。
Engine Upgrade|引擎升级
Socketed Engines|带插槽的引擎
Solar Engines|太阳能引擎
Socketed Solar Engines|带插槽的太阳能引擎
No Coolant|缺少冷却液
This engine requires coolant to run. Refill the coolant tank.|此引擎需要冷却液才能运行。请补充冷却液储罐。
No Solar Panels|缺少太阳能板
Attach some Solar Panels to this engine to start generating electricity!|为此引擎连接太阳能板以开始发电！
No Sunlight|缺少阳光
Solar Panels cannot generate any energy during the night|太阳能板在夜间无法产生能量
Needs fire!|需要点火！
Ensure there are burnable items inside the barrels inventory, then right click with a Flint and Steel or Fire Charge to start burning!|确保桶内有可燃物品，然后使用打火石或火焰弹右键点火！
Not warm enough|温度不足
This machine isn't warm enough to operate. Ensure power is connected.|此机器的温度不足以运行。请确保已连接电源。
Biogas Overclock|沼气引擎超频
Increases output to 200%|将输出提升至 200%
Lava now constantly consumed|持续消耗熔岩
Decreases efficiency by 20%|效率降低 20%
Efficiency I|效率 I
Increases efficiency by 10%|效率提高 10%
Efficiency II|效率 II
Increases efficiency by 20% (MAX 160%)|效率提高 20%（最高 160%）
Boost|增压
Increases output by 100%|输出提高 100%
Decreases efficiency by 15%|效率降低 15%
Choke|节流
Decreases output to 50%|将输出降低至 50%
Increases efficiency by 30%|效率提高 30%
will mutate.|将发生突变。
signal on the matching side of the control block.|控制方块对应一侧的信号。
Array Size: %s|阵列大小：%s
Array Size Bonus: x%s|阵列大小加成：x%s
Insolation: %s|日照强度：%s
Current temperature: %1$s/%2$s |当前温度：%1$s/%2$s 
Required melting temperature: %s|所需熔化温度：%s
Life|生命
You can use a smelter to alloy metals. Before any smelting can occur, the Smelter must warm up to a sufficient temperature!|可以使用熔炼炉制备金属合金。开始熔炼之前，熔炼炉必须预热到足够的温度！
Tinkering and Constructing!|匠艺与建造！
Peat that has been mixed with other compounds to aid it in drying out, causing it burn much slower than normal peat, lasting over twice as long.|与其他化合物混合以帮助干燥的泥炭，其燃烧速度远低于普通泥炭，燃烧时间超过普通泥炭的两倍。
Extra inventory that automatically picks up potion-related items.|提供额外储物空间，自动拾取与药水相关的物品。
Can be put in the Squeezer and turned into Liquid Experience. You can then put a Glass Bottle in the Squeezer's fluid container slot to recieve a Bottle o' Enchanting.|可以放入榨汁机转化为液态经验。随后将玻璃瓶放入榨汁机的流体容器槽，即可获得附魔之瓶。
Can be placed underwater.|可以放置在水下。
The Scoop is used to break bee hives found in the world, it will collect the bees inside. It can also be used to catch butterflies by right-clicking them. Is much stronger and more reliable than a normal scoop. They can only be purchased from villagers.|捕虫网用于破坏世界中的蜂巢，并收集其中的蜜蜂。也可以右键点击蝴蝶来捕捉。标定捕虫网比普通捕虫网更加坚固可靠，只能从村民处购买。
Brewing Backpack|酿造背包
Woven Brewing Backpack|编织酿造背包
Liquid Experience Bucket|液态经验桶
Molten Wax Bucket|熔融蜂蜡桶
Silicon Electron Tube|硅电子管
Guarantees saplings drop from broken leaves.|确保破坏树叶时掉落树苗。
Package|包裹
Letter|信件
Parcel|小包裹
Magmatic Drop|岩浆滴
Phosphorescent Jelly|磷光胶冻
Proven Scoop|标定捕虫网
Break hives to collect bees.|破坏蜂巢以收集蜜蜂。
Solar Cell|太阳能电池
Forestry Building Blocks|林业建筑方块
Cage|笼子
Deku|德库
Jazz|爵士
Lewis|刘易斯
Mousetree|鼠树
Mystical Tree|神秘之树
Site Bee|工地蜜蜂
Suspicious Looking Tree|可疑的树
The Hunny Tree|蜂蜜树
There Is Not A Man Here|这里没有人
Cow Tools|牛的工具
Wasphol|沃斯波尔
Sequoia of Wisdom|智慧红杉
''')

lexemes = table('''
Fully Rusted|完全锈蚀的
Very Rusted|严重锈蚀的
Slightly Rusted|轻微锈蚀的
Heavy Metal|重金属
Vent Cover|通风口盖
Fence Gate|栅栏门
Pressure Plate|压力板
Light Blue|淡蓝色
Light Gray|淡灰色
Dark Gray|深灰色
Refractory Waxstone|耐火蜂蜡石
Refractory Wax|耐火蜂蜡
Lacquered Metal Plating|涂漆金属板
Metal Plating|金属板
Alpha|阿尔法
Ashen Wax|灰烬蜡
Honeystone|蜂蜜石
Waxstone|蜡石
Wax|蜂蜡
Ash|灰烬
Burn Barrel|焚烧桶
Crispy Honey|脆蜂蜜
Combustion Engine|内燃引擎
Solar Engine|太阳能引擎
Phosphor|荧光粉
Plywood|胶合板
Smelter|熔炼炉
Solar Panel|太阳能板
Tin|锡
Cork|软木
Turf|草皮
Silicon|硅
Refractory|耐火
Rainbow|彩虹
Jumbo|特大型
Big|大型
Black|黑色
Blue|蓝色
Brown|棕色
Cyan|青色
Gray|灰色
Green|绿色
Lime|黄绿色
Magenta|品红色
Orange|橙色
Pink|粉色
Purple|紫色
Red|红色
White|白色
Yellow|黄色
Dyed|染色
Bricks|砖
Brick|砖
Slab|台阶
Stairs|楼梯
Wall|墙
Fence|栅栏
Button|按钮
Trapdoor|活板门
Trapoor|活板门
Bars|栏杆
Block|方块
Door|门
Grate|格栅
Planks|木板
Carpet|地毯
Grid|网格
Grass|草
Grass Block|草方块
Mesh|网片
Redstone Lamp|红石灯
Rose|玫瑰
Cobblestone|圆石
Cheese|奶酪
City|城市
Corroded|腐蚀的
Cracked|裂纹
Stone|石
Tile|瓷砖
Television|电视机
Dead|枯萎的
Leaves|树叶
Log|原木
Wood|木
Dev|开发
Dimensional|维度
Divine|神圣
Flesh|血肉
Blood|血液
Fluorescent Lamp|荧光灯
Redstone|红石
Soul|灵魂
Fragile|易碎
Hazard|危险警示
Inverse|反转
Inverted|反转
Iridescent|虹彩
Clay|黏土
Oak|橡木
Sapling|树苗
Sand|沙
Glass|玻璃
Core|核心
Arcade|街机
Banana Peel|香蕉皮
Barrier|屏障
Basal|基底
Long|长
Meat|肉
Metal Barrel|金属桶
Microwave|微波炉
Moonrock|月岩
Coal Ore|煤矿石
Pillar|柱
Mossy|苔藓
Music Trigger|音乐触发器
Nullified|虚化
Nullon|空子
Nullpoint|空点
Chair|椅子
Support|支架
Table|桌
Painted|涂漆的
Parking Concrete|停车场混凝土
Polished|磨制
Radio|收音机
Rotten|腐烂的
Small|小型
Smooth|平滑
Soap|肥皂
Soil|土壤
Something|某物
Sorting Cabinet|分类柜
Lamp|灯
Surface|表面
Tar|焦油
Antennas|天线
Tendon|肌腱
Lawn|草坪
Vibrant|鲜艳
Window|窗户
Wire|电线
Wooden Pallet|木托盘
Zeropoint|零点
Acid|酸液
Bottle|瓶
Bucket|桶
Ball|球
Banana|香蕉
Key|钥匙
Camera|相机
Chocolate Bar|巧克力棒
Coffee|咖啡
Energy|能量
Folder|文件夹
Fork|叉子
Ingot|锭
Nugget|粒
Large|大型
Microphone|麦克风
Mug|马克杯
Music Disc|音乐唱片
Rat Fur|鼠毛
Raw|生
Meatball|肉丸
Sausage|香肠
Spoon|勺子
Trumpet|小号
Realistic|写实
Obunga|奥邦加
Rat|老鼠
Hair|毛发
Minelands|矿地
Barrens|荒地
Town|城镇
Corridors|走廊
Foggy Plains|迷雾平原
Furniture Store|家具商店
Forest|森林
Foggy|迷雾
Library|图书馆
Old|古老
Sparse Desert|稀疏沙漠
Archives|档案馆
Hub|枢纽
Candle|蜡烛
Chiseled|雕纹
Cobbled|碎
Bronze|青铜
Copper|铜
Gold|金
Iron|铁
Netherite|下界合金
Chain|锁链
Gear|齿轮
''')
pattern = re.compile('|'.join(re.escape(k) for k in sorted(lexemes, key=len, reverse=True)), re.I)
lower_lexemes = {k.lower():v for k,v in lexemes.items()}

def compose(text):
    result = pattern.sub(lambda m:lower_lexemes[m[0].lower()], text.strip())
    if re.search('[A-Za-z]', result):
        return None
    return result.replace(' ', '')

translations, exclusions, residual = {}, {}, {}
for ns in ['untagged_mobs', 'forestry']:
    translations[ns], exclusions[ns], residual[ns] = {}, {}, {}
    for key, record in missing[ns].items():
        en = record['english']
        if key.startswith('_comment') or key.endswith('.author') or not en.strip() or re.fullmatch(r'[\d\s#?:().x/%$+-]+', en):
            exclusions[ns][key] = {'english': en, 'reason': 'comment_author_empty_numeric_or_symbol'}
            continue
        if key.endswith('.symbol') or en in {'MJ','Tesla','AER§7.OS','UVY','seat_entity','KeyB','Tzzt','Cazy','NonP','AnCr','DupL','Erro','Leny','SmPL','Tnna','1 - NONP','ASMR'} or (key.endswith('.desc') and en.startswith('ListedNightmare -')):
            exclusions[ns][key] = {'english': en, 'reason': 'proper_name_identifier_or_unit'}
            continue
        if en in exact:
            translations[ns][key] = exact[en]
        elif len(index[en]) == 1:
            translations[ns][key] = next(iter(index[en]))
        elif key.startswith(('block.', 'item.', 'biome.', 'entity.', 'fluid.')) and (zh := compose(en)):
            translations[ns][key] = zh
        else:
            residual[ns][key] = en
(BASE / 'manual_mod_translations_terms.json').write_text(json.dumps(translations, ensure_ascii=False, indent=2), encoding='utf8')
(BASE / 'manual_mod_exclusions_terms.json').write_text(json.dumps(exclusions, ensure_ascii=False, indent=2), encoding='utf8')
(BASE / 'manual_terms_residual.json').write_text(json.dumps(residual, ensure_ascii=False, indent=2), encoding='utf8')
print({ns:{'translated':len(translations[ns]),'excluded':len(exclusions[ns]),'remaining':len(residual[ns])} for ns in translations})
