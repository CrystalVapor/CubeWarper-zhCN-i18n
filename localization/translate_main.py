"""Exact English matches and explicitly scoped UI/name patterns; no file-wide replacement."""
import json,re
from pathlib import Path
P=Path(__file__).parent
DATA=json.loads((P/'remaining_main.json').read_text(encoding='utf-8'))
TABLE='''
Ok|确定
the|该
Lens of Disruption|扰乱透镜
+01:00, -1 Level|+01:00，等级 -1
Weight:|权重：
Metadata|元数据
Condenser|物质聚合器
Content from|内容来自
Crystal Resonance Generator|晶体共振发电机
%s [Connected]|%s [已连接]
%s [Disconnected]|%s [已断开连接]
A test world can only be set up in a Superflat world!|测试世界只能在超平坦世界中建立！
Fluix Researcher|福鲁伊克斯研究员
Configure Imported Types|配置导入类型
Configure Visible Types|配置可见类型
Generation Capacity: %s|发电能力：%s
Incompatible with cell|与存储元件不兼容
Missing Channel|缺少频道
Out of Power|电量耗尽
Uses fluids directly|直接使用流体
Substitutes alternate items|使用替代物品
Use # to search in tooltips (#looting)|使用 # 搜索工具提示（#looting）
Explode|爆炸
Throw in %s|投入 %s
Creative ME Storage Cell|创造 ME 存储元件
Missing Content|缺失内容
Wrapped Generic Stack|封装的通用物品堆
Modifier for Mouse-Wheel Items|鼠标滚轮物品操作修饰键
Suppressed|已抑制
Charged Redstone Crystal Block|充能红石晶体块
Portable FE Cells|便携 FE 能量元件
Creative ME FE Cell|创造 ME FE 能量元件
Harden Insulating Resin|硬化绝缘树脂
Induction Card|感应卡
Allow AE devices to accept or send energy|允许 AE 设备接收或发送能量
Allow Portable FE Cell to charge player's inventory|允许便携 FE 能量元件为玩家物品栏中的物品充能
Insulating Resin|绝缘树脂
MEGA FE Cell Housing|巨型 FE 能量元件外壳
Redstone Crystal|红石晶体
Sky Insulating Resin|陨石绝缘树脂
King|王者
Inner Arts|内在技艺
Childhood Blues|童年忧郁
Noisy Lover Soul|喧闹的恋人之魂
Packet Hero|数据包英雄
Segments Blue|蓝色片段
Donut Hole|甜甜圈洞
Rockbell|洛克贝尔
World Calling|世界的呼唤
Odds and Ends|零碎杂物
Sky of Beginning|起始之空
An Ecstatic Vivace|狂喜的快板
Mythologia's End|神话的终焉
Heisei Cataclysm|平成灾变
After-School Stride|放学后的步伐
A Fake, Fake Psychotropic|虚假的精神药物
Arithmetic|算术
Hand in Hand|手牵手
World's End Dancehall|世界尽头的舞厅
M'aider Stranded Girl|求救的受困少女
Under of Fragments|碎片之下
World Domination How-To|世界征服指南
Rotten Heresy and Chocolate|腐朽的异端与巧克力
Vivid Wave|鲜明的波浪
Imagination Forest|想象森林
Deja Vu|似曾相识
Decorator|装饰者
Drop Pop Candy|缤纷雨滴糖
I can take off my (redacted)|我可以脱下我的（已删改）
Dancer in the Dark|黑暗中的舞者
Remote Paranoia|遥远的偏执
One Step Layered|层叠的一步
Heart Shooter|心灵射手
Blessing|祝福
Just Be Friends|只是朋友
Builds walls, creates worlds|筑起墙壁，创造世界
Tilting the umbrella too much|雨伞倾斜得太多
Nudistoooooooooo|天体主义者——
Lurk moar|继续潜伏
At that time, we had little true structure to our civilization, living in simple huts of Dreamwood. This made rebuilding little more than a chore of gathering materials, especially as we had prior warning.|那时，我们的文明还没有形成完善的社会结构，人们居住在简单的梦之木小屋中。重建基本只需要收集材料，尤其是我们已经提前收到了警告。
MY BRAND|我的品牌
bun pls|请给我面包
$(o)Stick around, would ye$()?|$(o)留下来，好吗$()？
$(o)(n)spooky(n+2)me$().|$(o)(n)吓人(n+2)的我$()。
...everell|……埃弗雷尔
Rosa Arcana disenchants|奥秘玫瑰解除附魔
DO IT!!|行动吧！！
Woohoo!!!|欢呼！！！
It's not my birthday today, though.|不过，今天并不是我的生日。
Thank you anyway! I hope you're satisfied with your speedrun.|还是谢谢你！希望你对这次速通感到满意。
Granted all missing lexicon progression advancements.|已授予所有尚未获得的植物魔法辞典进度。
Blessing%%|祝福%%
Defeat Gaia Guardian I|击败盖亚守护者 I
Defeat Gaia Guardian II|击败盖亚守护者 II
Obtain Dreamwood|获得梦之木
Fancy Skybox|精美天空效果
Fancy Skybox in non-GoG Worlds|在非空中花园世界中启用精美天空效果
Flight Bar Height with Breath Bar|显示氧气条时的飞行能量条高度
Bore Lens Harvest Level|钻孔透镜采掘等级
Weight Lens Harvest Level|重力透镜采掘等级
Inverted Magnet Ring Controls|反转磁力指环控制方式
Seasonal Features|季节性效果
Spreader Trace Time|魔力发射器轨迹显示时间
Fertilizer|肥料
Turn on rain to see the fertilizer model!|开启下雨天气以查看肥料模型！
Gecko Habitat|壁虎栖息地
Bat|蝙蝠
Bike|自行车
Cool Kid|酷小孩
Fake Glass|假玻璃
Gremlin|小妖精
Mutant Zombie|变异僵尸
Gave %1$s to the entity|已将 %1$s 给予该实体
Parasite|寄生虫
Race Car|赛车
Gecko Armor Boots|壁虎护甲靴子
Gecko Armor Chestplate|壁虎护甲胸甲
Gecko Armor Helmet|壁虎护甲头盔
Gecko Armor Leggings|壁虎护甲护腿
Jack-in-the-Box|惊吓盒
Opening the Jack-in-the-Box!|正在打开惊吓盒！
Wolf Armor Boots|狼护甲靴子
Wolf Armor Chestplate|狼护甲胸甲
Wolf Armor Helmet|狼护甲头盔
Wolf Armor Leggings|狼护甲护腿
Geckolib Examples|Geckolib 示例
Magic Proficiency|魔法熟练度
World setup for not-annoying development work|为便捷开发设置世界
Command Successful, enjoy your screenshake.|命令执行成功，屏幕震动已启用。
All World Events are already frozen|所有世界事件均已冻结
Froze %s World Events|已冻结 %s 个世界事件
The specified World Event is already frozen|指定世界事件已冻结
Froze the specified World Event: %s|已冻结指定世界事件：%s
All World Events of type %s are already frozen|类型为 %s 的所有世界事件均已冻结
Froze %s World Events of type %s|已冻结 %s 个类型为 %s 的世界事件
There are %s active World Event(s)|共有 %s 个活动世界事件
%s event(s) are frozen|已有 %s 个世界事件被冻结
There are no active World Events|没有活动世界事件
Could not remove any World Events|无法移除任何世界事件
Removed %s Active World Event(s)|已移除 %s 个活动世界事件
The specified World Event is already inactive|指定世界事件已处于非活动状态
Removed the specified World Event: %s|已移除指定世界事件：%s
No active World Events of type %s were found|未找到类型为 %s 的活动世界事件
Removed %s World Events of type %s|已移除 %s 个类型为 %s 的世界事件
No World Events are currently frozen|当前没有被冻结的世界事件
Unfroze %s World Events|已解冻 %s 个世界事件
The specified World Event is not frozen|指定世界事件未被冻结
Unfroze the specified World Event: %s|已解冻指定世界事件：%s
No World Events of type %s are currently frozen|当前没有类型为 %s 的被冻结世界事件
Unfroze %s World Events of type %s|已解冻 %s 个类型为 %s 的世界事件
Fire Overlay Offset|着火覆盖层偏移
Offsets the fire overlay effect downwards, clearing up your vision.|将着火覆盖层向下偏移，改善视野。
Screenshake Intensity|屏幕震动强度
Controls how much screenshake is applied to your screen.|控制屏幕震动效果的强度。
Entities with scale NBT|具有缩放 NBT 的实体
Entities with scale value|具有缩放值的实体
Entities with scale type|具有缩放类型的实体
Unknown easing '%s'|未知缓动方式 '%s'
Unknown scale modifier '%s'|未知缩放修饰器 '%s'
Unknown scale type '%s'|未知缩放类型 '%s'
Mixin environment audit complete!|Mixin 环境审计完成！
Mixin environment audit (client) complete!|Mixin 环境审计（客户端）完成！
Starting Mixin environment audit...|正在开始 Mixin 环境审计……
Starting Mixin environment audit (client)...|正在开始 Mixin 环境审计（客户端）……
Config "%s" was changed from "%s" to "%s"|配置 "%s" 已从 "%s" 更改为 "%s"
Config "%s" is currently set to "%s"|配置 "%s" 当前设置为 "%s"
%s config entries have been reset to their default values|已将 %s 个配置项重置为默认值
Config "%s" was reset from "%s" to default "%s"|配置 "%s" 已从 "%s" 重置为默认值 "%s"
Invalid UUID "%s".|无效的 UUID "%s"。
Tests succeeded: %d/%d|测试通过：%d/%d
Delay: %s ticks|延迟：%s 刻
Easing: %s|缓动方式：%s
Easing: default (%s)|缓动方式：默认（%s）
Scale: %s|缩放：%s
Scale: %s (1/%s)|缩放：%s（1/%s）
Persistent: default (false)|持久化：默认（false）
Persistent: default (true)|持久化：默认（true）
Persistent: false|持久化：false
Persistent: true|持久化：true
Whether the collision of Nether Portals should be adjusted to fit the selection box|是否调整下界传送门的碰撞范围以适应选择框
Whether commands such as /scale should be enabled|是否启用 /scale 等命令
Whether internal debugging commands should be enabled|是否启用内部调试命令
Whether all scales should not get reset on respawn|是否在重生时保留全部缩放值
Minimum value for the projection matrix's camera depth. Vanilla defaults to 0.05|投影矩阵的摄像机深度最小值。原版默认值为 0.05
Whether the attack damage scales should be enabled|是否启用攻击伤害缩放
Whether the defense scale should be enabled|是否启用防御缩放
Whether the explosion scale should be enabled|是否启用爆炸缩放
Whether fall damage should scale based on the motion scale|是否根据移动缩放调整摔落伤害
Whether the health scale should be enabled|是否启用生命值缩放
Whether the item drop scale should be enabled|是否启用掉落物缩放
Whether the motion scale should be enabled|是否启用移动缩放
Whether the shot projectile scale should be enabled|是否启用发射的弹射物缩放
Whether the reach scales should be enabled|是否启用触及距离缩放
A list of scale type IDs that should not be reset on respawn|重生时需要保留的缩放类型 ID 列表
Redstone Flux Limiter|红石通量限制器
Fluiduct Filter|流体管道过滤器
Fluiduct Servo|流体管道伺服器
Fluiduct Turbo-Servo|流体管道涡轮伺服器
RF Distribution Interface|RF 分配接口
Fluxduct|能量管道
Fluid Distribution Interface|流体分配接口
Fluiduct|流体管道
Fluiduct (Windowed)|流体管道（带窗）
Logistical Item Buffer|物流物品缓存器
Limits the amount of energy flowing through it.|限制经过此处的能量流量。
Can be configured to allow different amounts in each direction.|可以分别配置各方向允许通过的流量。
Bidirectional Filtering|双向过滤
Outbound (From Duct) Filtering|输出过滤（从管道流出）
Inbound (To Duct) Filtering|输入过滤（流入管道）
Additional options can be used to fine-tune filtering.|可使用附加选项精细调整过滤设置。
Redstone Control can be used to temporarily disable filtering.|可使用红石控制暂时禁用过滤。
Redstone Control is used to enable extraction.|通过红石控制启用抽取。
A much faster Servo, with limited filtering.|速度更快的伺服器，过滤功能有限。
Place items containing fluid in the filter slot.|将含有流体的物品放入过滤槽。
Additional options can be used to fine-tune filtering and extraction amount.|可使用附加选项精细调整过滤设置和抽取量。
Restricts quantity and flow of items.|限制物品数量及传输流量。
Set desired items and quantities using the left grid.|使用左侧网格设置所需物品及数量。
Mouse wheel can be used to fine-tune item quantity.|可使用鼠标滚轮精细调整物品数量。
Latch I/O requires all items to be present before extraction is allowed.|锁存输入/输出模式仅在所有所需物品齐备后允许抽取。
Very useful for maintaining specific item ratios.|适用于维持特定的物品比例。
I/O: Normal|输入/输出：普通
I/O: Latch|输入/输出：锁存
Attachment: Redstone Flux Limiter|附件：红石通量限制器
Attachment: Filter|附件：过滤器
Attachment: Servo|附件：伺服器
Attachment: Turbo-Servo|附件：涡轮伺服器
Test Block: (Asset)|测试方块：（资源）
Test Block: (Base)|测试方块：（基础）
Test Block: (Twenty-Four Rotation)|测试方块：（二十四向旋转）
Test Block: (Machine)|测试方块：（机器）
%s Casing|%s机壳
%s Chunk|%s矿块
%s Clump|%s碎块
Crushed %s|粉碎%s
Dense %s Plate|致密%s板
Dense %s Rod|致密%s棒
%s Dust|%s粉
%s Flakes|%s碎片
%s Gear|%s齿轮
%s Grindings|%s研磨料
%s Ingot|%s锭
%s Nugget|%s粒
%s Pebbles|%s小石
%s Plate|%s板
Purified %s Grindings|纯净%s研磨料
Reinforced %s Plate|强化%s板
%s Rod|%s棒
Small %s Dust|小撮%s粉
%s Stone|%s石
Titanium Resources|Titanium 资源
Locks:|锁定：
Progress: |进度： 
<Right-Click to drain from item>|<右键点击从物品中抽取>
<Left-Click to fill from item>|<左键点击从物品中注入>
Amount: |数量： 
Can drain from item|可以从物品中抽取
Can fill from item|可以从物品中注入
Empty |空 
Fluid: |流体： 
Can't fill or drain from item|无法从物品中注入或抽取
<Not hovering with a tank>|<未手持储罐悬停>
Unlocks:|解锁：
Headlight|头灯
Aw man!|哎呀！
The One Probe|检测器
Under Pressure|承受压力
CHOO CHOO!|呜——呜！
Benzol|苯
Petroleum Gas|石油气
Not enough Power|能量不足
Bucket of Benzol|苯桶
Bucket of Petroleum Gas|石油气桶
Blue ASHPD|蓝色光圈科技手持传送门装置
Storage Cube|储物方块
Companion Cube|同伴方块
Orange ASHPD|橙色光圈科技手持传送门装置
Truss: Posts must have at least 1 blocks of space between.|桁架：两根立柱之间必须至少间隔 1 格。
Truss: Both posts must be of the same material.|桁架：两根立柱必须由相同材料制成。
Truss: Next post out of range or does not exist.|桁架：下一根立柱超出范围或不存在。
Extendable Posts|可延伸立柱
Splash Potion of Mining Fatigue|喷溅型挖掘疲劳药水
Arrow of Mining Fatigue|挖掘疲劳之箭
Arthropod|节肢动物
Baked Spider Leg|烤蜘蛛腿
Bat Cookie|蝙蝠曲奇
Bat Rolls|蝙蝠卷
Bat Soup|蝙蝠汤
Bat Soup Cup|蝙蝠汤杯
Bone Broth Cup|骨汤杯
Cave Hamburger|洞穴汉堡
Cooked Arthropod|熟节肢动物
Copper Carrot|铜胡萝卜
Crunchy Bar|酥脆能量棒
Glow Ink Pasta|荧光墨汁意面
Golden Nutritional Bar|金营养棒
Insect Sandwich|昆虫三明治
Insect Stew|昆虫炖菜
Insect Stew Cup|昆虫炖菜杯
Insect Wrap|昆虫卷饼
Moss|苔藓
Nutritional Bar|营养棒
Onion Soup Cup|洋葱汤杯
Plate Of Fake Meatloaf|素肉饼餐盘
Plate Of Glazed Arachnid Limbs|蜜汁蛛腿餐盘
Seasoned Arthropods|调味节肢动物
Spider Leg|蜘蛛腿
Squid Sandwich|鱿鱼三明治
Takoyaki|章鱼烧
Tentacles On A Stick|触手串
Vegan Hamburger|素食汉堡
Vegan Patty|素肉饼
Vegan Steak And Potatoes|素牛排配土豆
Vegan Wrap|素食卷饼
Soothing honey center!|舒缓的蜂蜜夹心！
IO Key|输入/输出钥匙
IO Key (Both)|输入/输出钥匙（双向）
IO Key (Input)|输入/输出钥匙（输入）
IO Key (None)|输入/输出钥匙（禁用）
IO Key (Output)|输入/输出钥匙（输出）
Hopper Upgrade|漏斗升级
Hopper-like in-world item collection|像漏斗一样收集世界中的物品
Magnet Upgrade (I)|磁铁升级（I）
Magnet Upgrade (II)|磁铁升级（II）
Magnet Upgrade (III)|磁铁升级（III）
Collect items around drawers|收集抽屉周围的物品
Adds %s collecting range|增加 %s 格收集范围
Collects %d stack per %dt|收集 %d 组，每 %dt 一次
Personal Key (FTB)|私人钥匙（FTB）
Personal Key (Admin)|私人钥匙（管理员）
Unlocks any drawer locked by another player's personal key|解锁任何被其他玩家私人钥匙锁定的抽屉
Pull Upgrade (I)|抽取升级（I）
Pull Upgrade (II)|抽取升级（II）
Pull Upgrade (III)|抽取升级（III）
Pull items from an adjacent inventory|从相邻容器中抽取物品
Pulls %d items per %dt|抽取 %d 个物品，每 %dt 一次
Push Upgrade (I)|推送升级（I）
Push Upgrade (II)|推送升级（II）
Push Upgrade (III)|推送升级（III）
Push items into an adjacent inventory|将物品推送至相邻容器
Pushes %d items per %dt|推送 %d 个物品，每 %dt 一次
Pause Key|暂停钥匙
Paused|已暂停
General|常规
Always spawn weather particles|始终生成天气粒子
Tint water particles based on biome colors|根据生物群系颜色为水粒子着色
Cloud height|云层高度
Spawn fog particles|生成雾粒子
Spawn ground fog particles|生成地面雾粒子
Spawn rain particles|生成雨粒子
Play rain sounds|播放雨声
Spawn rain ripples on water|在水面生成雨水涟漪
Spawn dust particles above sand|在沙地上方生成尘埃粒子
Play wind blowing sand sounds|播放风沙声
Spawn shrub particles|生成灌木粒子
Spawn smoke on hot blocks|在高温方块上生成烟雾
Spawn snow particles|生成雪粒子
Play snow sounds|播放雪声
Spawn rain splashing on the ground|生成雨滴落地飞溅粒子
Spawn streak particles on block edges|在方块边缘生成水流粒子
Fog Particle Options|雾粒子选项
Relative density|相对密度
Size|大小
Ground Fog Particle Options|地面雾粒子选项
Spawn height|生成高度
Spawn time|生成时间
Maximum particle amount|最大粒子数量
New weather particles will not be spawned if there are this many already in the world|世界中已有的天气粒子达到此数量时停止生成新粒子
Particle density|粒子密度
The number of times weather particles will try to spawn per tick during normal rain|普通降雨期间每刻尝试生成天气粒子的次数
Particle radius|粒子半径
How many blocks away particles will spawn from the camera|粒子生成位置距离摄像机的最大格数
Particle density during thunderstorms|雷暴期间粒子密度
The number of times weather particles will try to spawn per tick during storms|暴风雨期间每刻尝试生成天气粒子的次数
Rain Particle Options|雨粒子选项
Opacity|不透明度
How see-through the particles are from fully transparent (0) to fully opaque (100)|粒子不透明度，范围从完全透明（0）到完全不透明（100）
Splash density|飞溅密度
Wind strength during thunderstorms|雷暴期间风力
Wind strength|风力
Render default weather|渲染原版天气
Ripple Particle Options|涟漪粒子选项
Amount of ripples to spawn|生成涟漪的数量
Resolution|分辨率
Use resource pack resolution|使用资源包分辨率
Sand Particle Options|沙尘粒子选项
Size of individual sand grains that bounce along the ground|沿地面弹跳的单个沙粒大小
Spawn above blocks tagged with:|在具有以下标签的方块上方生成：
Grain size|沙粒大小
Spawn on ground|在地面生成
Shrub Particle Options|灌木粒子选项
Bounciness|弹跳程度
Rotation speed|旋转速度
Snow Particle Options|雪粒子选项
Rotation speed during thunderstorms|雷暴期间旋转速度
Spawn weather particles above cloud height|在云层高度上方生成天气粒子
Sync registry|同步注册表
Disable this if players can't connect to your LAN server|玩家无法连接局域网服务器时请禁用此项
Tick default rain splashing|更新原版雨水飞溅
Tint water / sky color mix|水色与天空颜色混合比例
Mix of color between the biome water color (0) and the biome sky color (100)|生物群系水色（0）与天空颜色（100）之间的混合比例
Y-level wind adjustment|随 Y 高度调整风力
Particle Rain|粒子降雨
'''
MAP=dict(line.split('|',1) for line in TABLE.splitlines() if '|' in line)
MAP.update({
 'Scale: %s | (%s)':'缩放：%s | (%s)',
 'Scale: %s (1/%s) | (%s)':'缩放：%s（1/%s）|（%s）',
 'Cycle drawer side through IO modes\nCrouch and use to cycle key':'循环切换抽屉面的输入/输出模式\n潜行使用以切换钥匙模式',
 'Toggle drawer side for input/output\nCrouch and use to cycle key':'切换抽屉面的输入/输出状态\n潜行使用以切换钥匙模式',
 'Toggle drawer side for input\nCrouch and use to cycle key':'切换抽屉面的输入状态\n潜行使用以切换钥匙模式',
 'Toggle drawer side to block IO\nCrouch and use to cycle key':'禁止该抽屉面输入/输出\n潜行使用以切换钥匙模式',
 'Toggle drawer side for output\nCrouch and use to cycle key':'切换抽屉面的输出状态\n潜行使用以切换钥匙模式',
 'Protect access from other players\nAllows access to your team':'阻止其他玩家访问\n允许你的队伍成员访问',
 'Pauses controller I/O\nand most upgrade actions':'暂停控制器输入/输出\n以及大多数升级功能',
})
COLORS={'Black':'黑色','Blue':'蓝色','Brown':'棕色','Cyan':'青色','Gray':'灰色','Green':'绿色','LightBlue':'淡蓝色','Lime':'黄绿色','Magenta':'品红色','Orange':'橙色','Pink':'粉红色','Purple':'紫色','Red':'红色','Silver':'淡灰色','White':'白色','Yellow':'黄色'}
PATTERNS={}
for color,zh in COLORS.items():
 for obj,cn in {'Actually Additions Manual':'实用拓展手册','Drill':'钻头','Leaf Blower':'落叶清扫机','Phantom Connector':'幽灵连接器'}.items():
  PATTERNS[f'{color} {obj} Pattern']=zh+cn+'图案'
for material,zh in {'Aluminium':'铝','Concrete':'混凝土','Constantan':'康铜','Copper':'铜','Electrum':'琥珀金','Gold':'金','Iron':'铁','Leaded Concrete':'含铅混凝土','Lead':'铅','Nether Brick':'下界砖','Nickel':'镍','Silver':'银','Steel':'钢','Uranium':'铀','Wooden':'木'}.items():
 PATTERNS[material+' Truss']=zh+'桁架'
for n in ['16M','1M','256M','4M','64M']:
 PATTERNS[n+' ME Energy Storage Component']=n+' ME 能量存储组件'
 PATTERNS[n+' ME FE Storage Cell']=n+' ME FE 能量存储元件'
for n in ['1k','4k','16k','64k','256k','1M','4M','16M','64M','256M']:
 PATTERNS[n+' Portable FE Cell']=n+' 便携 FE 能量元件'
for name,zh in {'Bat':'蝙蝠','Bike':'自行车','Cool Kid':'酷小孩','Fake Glass':'假玻璃','Gremlin':'小妖精','Mutant Zombie':'变异僵尸','Parasite':'寄生虫','Race Car':'赛车'}.items():
 PATTERNS[name+' Spawn Egg']=zh+'刷怪蛋'
for typ,cn in {'attack':'攻击','attack_speed':'攻击速度','base':'基础','block_reach':'方块触及距离','defense':'防御','entity_reach':'实体触及距离','eye_height':'视线高度','falling':'下落','flight':'飞行','health':'生命值','height':'高度','hitbox_height':'碰撞箱高度','hitbox_width':'碰撞箱宽度','jump_height':'跳跃高度','knockback':'击退','mining_speed':'挖掘速度','model_height':'模型高度','model_width':'模型宽度','motion':'移动','projectiles':'弹射物','step_height':'跨步高度','third_person':'第三人称','view_bobbing':'视角晃动','visibility':'可见性','width':'宽度'}.items():
 for level,zh in [('Maximum','最大值'),('Minimum','最小值')]:
  PATTERNS[f'{level} value for the scale type pehkui:{typ}']=f'缩放类型 pehkui:{typ}（{cn}）的{zh}'
PATTERNS['Maximum value for the scale type pehkuiview_bobbing:']='缩放类型 pehkui:view_bobbing（视角晃动）的最大值'
MAP.update(PATTERNS)

DELEGATED={'ftbquests','ftblibrary','ftbultimine','jade','modernfix'}
out={};pending={};exclusions={}
for ns,values in DATA.items():
 if ns in DELEGATED:continue
 for key,en in values.items():
  if en in MAP: out.setdefault(ns,{})[key]=MAP[en]
  elif re.fullmatch(r'(?:[IVXLCDM]+|[A-Z][A-Z0-9_./() -]{0,12}|(?:%\d*\$?[sd] ?[/|: -]?)+|\d*[xX]?[0-9a-f]+|HH:mm:ss)',en) or key.endswith(('.keyword','_extra_msg')) or '.roman' in key or '.rank' in key or '.value.' in key and re.fullmatch('[IVX]+',en):
   exclusions.setdefault(ns,{})[key]={'english':en,'reason':'符号、单位、搜索关键词或内部格式，无需文本翻译'}
  elif ns=='actuallyadditions' and '.manualName.' in key:
   out.setdefault(ns,{})[key]={'Actual Additions':'真实拓展','Actually Addiction':'实用成瘾','Actual Edition':'真实版本','Actual Addition':'真实添加','Actually Addons':'实用附加','Additional Addons':'额外附加'}.get(en,'实用拓展')
  else: pending.setdefault(ns,{})[key]=en
(P/'manual_mod_translations_main.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'pending_main.json').write_text(json.dumps(pending,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'excluded_main_details.json').write_text(json.dumps(exclusions,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Translated',sum(map(len,out.values())),'Pending',sum(map(len,pending.values())),'Excluded',sum(map(len,exclusions.values())))
print('\n'.join(f'{ns}: {len(m)}' for ns,m in pending.items()))
