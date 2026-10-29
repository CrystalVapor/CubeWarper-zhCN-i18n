import json, pathlib, re
from translate_quests import visible_strings

ROOT=pathlib.Path(__file__).resolve().parent.parent
DESC={
0: '''登上六面体，按下红色大按钮！
在这个奇异的新维度中，你可以找到旧式矢量算子。
将它们放在六面体内部的三个插座上，即可前往新的维度。
每个旧式矢量算子
都会使数值加 1。例如，连续放置两个算子就会将你送往维度 2。
按住默认的 &o波浪号&r键（~），即可同时挖掘大量相邻且类型相同的方块。
这个实用工具可以减少任务中的重复劳动。
你可以在控制设置的 FTB Ultimine 分类中重新绑定该按键。
使用 FTB 地图可以强制加载区块，使设施在你离开所在区域后仍能运行。
点击物品栏界面左上角的第二个地图图标，即可认领区块。
在地图上按住 Shift 并右键点击已加载的区块，即可强制加载它们。
阿卡什宝典收录了你所需的全部指南书。
如果不确定某项操作的方式，请查阅对应模组的指南书。
将宝典变为某本指南书后，左键点击即可将其还原为阿卡什宝典。
考虑到整合包的运行机制，建议将渲染距离控制在 12 个区块以内。
这项建议主要适用于六面体移动到全新维度的过程。
如果六面体发生意外故障，执行下列命令可以解决许多问题：
该命令会重建六面体内部的技术组件。
你的基地将完整保留。''',
1: '''挖掘巨大的圆石柱，可以获得制作基础工具和熔炉所需的石材。
整合包提供连锁挖掘功能，可以帮助你快速收集大量圆石。
利用已经产生的电力，你可以为空白矢量算子充能，将其变为充能矢量算子。
切制铜块可以熔炼成铜锭。
熔炼前需要先刮除表面的氧化层。
泥炭引擎可以提供你的第一份电力。
为它提供泥炭和红石信号即可。
请注意，这台发电机只能燃烧泥炭。
泥炭是高效的天然燃料。使用泥炭可以节省木材。
生食垂果的营养有限，但足以维持生存。
可以制作垂果汤，提高其营养价值。
植物向下生长时才会生成新的果实。''',
2: '''冶炼炉可以将维度 1 中获得的炮弹熔化为熔融铅。
熔融铅可以浇铸成铅锭或铅块。
磨粉机可以将多种材料加工成粉末。
先将机器框架的下半部分放置在世界中，再用上半部分右键点击，即可组合成完整框架。
结晶器在水供应充足时可以生成多种晶体。
多驱冲压机可以使用多种模具，将金属加工成所需形状。
赤脉旷野中可以找到神秘的方块。
破坏这些方块后，会掉落全部五种压印模板。
现在可以将物品存储在存储元件中。
AE2 的大多数组件成本较低，便于你在早期建立自动化设施。
铁域-6 的顶部生长着赛特斯石英晶体。
熔岩发电机可以利用熔岩产生能量。
目前需要用桶手动添加熔岩。在下一章中，你将能够把这个维度中的无尽熔岩湖自动泵送到六面体内部。
使用磨粉机可以将方铅矿加工成硅。
请注意，铁域-6 中的刷石机会生成方铅矿。
使用铜和少量铁即可制作被动运行的蒸汽引擎。
使用流体管道和伺服器可以向锅炉供水。
这样便能获得基础而稳定的旋转动力。
挖掘镶金黑石可以获得金。
机械压力机能够缓慢压碎物品，让你重现液压机视频中的场景。
你很快就能将陨石磨成陨石粉。
建议提前储备一些，减少反复返回这个维度的次数。
使用切石机可以将铁板加工成几乎所有压印模板。
使用赤脉旷野中的第一座祭坛，可以将红石转化为充能红石。
手持红石右键点击远古红石核心，即可进行转化。
手动操作有短暂的冷却时间。机械手等自动化设备不受该冷却时间影响。
建议在此设置一台被动运行的蒸汽引擎，减少反复返回这个维度的次数。
赤脉旷野中的刷石机会生成粗红石。
之后可以通过磨粉获得可再生的红石。
&l刷石机生成的石材因所在维度而异。&r
余烬地平线中的刷石机会生成焦黑圆石。
压制任意原木即可获得橡胶。熔炼橡胶可以得到硫化橡胶。
使用输入或输出总线，可以输入、输出任意物品或流体。
机械手可以自动完成许多操作。建议尽早在合适的位置进行部署。
感应炉可以制作机械动力所需的焦黑合金。后期可以改用机械搅拌器完成这项加工。
使用由合成单元组成的多方块结构，可以实现配方自动化。
请查阅 AE2 指南，或将鼠标悬停在物品上并按住 [G] 获取更多信息。
使用分子装配室可以自动完成工作台合成配方。''',
3: '''核熔炉可以使用八个核熔炉组件建造。
使用铀棒作为燃料时，它可以进行以下转化：
&lo&r 空白矢量算子 → 核能矢量算子
&lo&r 空弹壳 → 裂变核心
在加工过程中，核熔炉会积累核废料。
提供金属桶可以将核废料取出。
&l如果内部废料储槽达到容量上限，核熔炉就会发生核熔毁，摧毁自身及周围的一切。&r
使用热电子加工机，现在可以制作新的空白矢量算子。
你需要拆除核弹，才能获得内部的裂变核心。
首先使用撬棍撬开核弹顶部。
然后使用钢丝钳剪断其中一根导线。
左键点击会剪断红色导线。
右键点击会剪断绿色导线。
其中一根导线会解除核弹，另一根会使装置在 10 秒后爆炸。
正确的导线始终完全随机……
ME 控制器可以大幅增加 ME 系统可用的频道数量。
银色森林中存在无尽的白银海洋。
手持装满液体的桶右键点击冶炼炉排液口，可以将液体加入冶炼炉。
也可以将任意液体直接泵入冶炼炉排液口。
热电子加工机可以使用能量和沙子制作电子管。开始加工前，需要先将沙子加热成熔融玻璃。
锇压缩机可以使用锇来处理材料。
任意花朵都可以转化为对应颜色的神秘花瓣。霜花风暴中稀有的雪花莲可以提供制作白雏菊所需的白色花瓣。
白雏菊可以将深板岩转化为辉煌深板岩。
核熔炉需要使用铀棒作为燃料。
防化服可以防护辐射，并让穿戴者在酸液中游泳。
这个维度的地下寒颤石之间可以找到锇。
货币连续体中的绿宝石块可以分解成绿宝石。
在物品栏中按住 Shift 并右键点击铀棒，可以为耗尽能量的射线枪充满电。
手持空瓶右键点击有毒地热喷口，可以装入氡气。
利用核熔炉，现在可以持续生产裂变核心。
将蒸汽引擎放在正在运行的核熔炉上方，可以自动达到&l最高加热等级&r。
让黏液在核熔炉中循环处理，即可保持运行。这实际上能够组成一套核反应堆系统。
右键使用召回管，可以传送到六面体内部，即使六面体处于另一个维度也有效。
富集仓可以将铀碎片提炼成黄饼铀。
木材湖泊的地表之下全部由青灰岩构成。
开采并磨碎这种矿物，即可持续生产锌锭。
利用木材湖泊中的祭坛，可以倒转某些方块的时间。
转化关系如下：
&lo&r 铁块 → 闪亮金属块
&lo&r 空白矢量算子 → 旧式矢量算子
&lo&r 绿宝石块 → 时间石
这个维度中可以找到自然生成的活石巨砾。
该维度中的刷石机也会生成活石。
粉碎辐射岩可以持续获得铀。
裂变原野中的刷石机会生成辐射岩。
粉碎或磨碎寒颤石可以获得锇粒。
霜花风暴中的刷石机会生成寒颤石。
&l跨维度收发器是建立跨维度自动化设施的关键方块。&r
&l步骤 1&r
首先将收发器放在主基地内，连接到有电力供应的 ME 系统，然后点击 Mode（模式），将其设为发送端。
&l步骤 2&r
点击 Add（添加），创建一个任意名称的频道，然后在列表中点击该频道进行选择。
&l步骤 3&r
发送端设置完成后，可以在任意位置放置任意数量的收发器，在频道列表中选择刚创建的频道，即可全部连接到同一个发送端。
较为稀有的钻石灯可以粉碎成钻石。
熔化金币可以持续获得金。货币连续体中的刷石机会生成金币。
利用时间石中储存的时间，可以加速机器。
将空白矢量算子放在基座上，再按下按钮倒转时间，即可制作新的旧式矢量算子。
现在可以将电力存储在 ME 系统中。
这项功能现在很方便，之后建立跨维度 ME 系统时更为关键。
你可以制作使用铀燃料棒的发电机。
一根铀棒可以燃烧
30 分钟，并持续输出
500 RF/t，前提是发电机能够将电力输出。
冷冻血肉可以熔炼成皮革。维度 2 中的香蒲可以用于制作线。
这样就可以制作背包了。''',
4: '''火焰喷射器是一种强力武器，可以对目标直接造成范围燃烧伤害。
将点燃的 TNT 投入硫木平原祭坛的中央孔洞，会使祭坛喷发并产生一只烈焰人。
熔岩炉可以将荧石熔化为充能荧石。
神秘花瓣与魔力结合，可以制作符文。
你需要找到颜色正确的花朵。
使用灵魂坩埚可以制作荧石，再通过熔岩炉熔化为液态充能荧石。
充能荧石是制作烈焰燃料的重要材料。
使用盆盖可以在置物盆中制作熔融钢，随后将其浇入合适的模具。
粉碎轮可以将烈焰人燃烧室粉碎成烈焰粉，还能高效粉碎石材。
全速运行的粉碎轮可以在数秒内处理数组石头。
借助它，你可以快速粉碎来自不同维度的各类石材。
这个维度中偶尔可以找到符文木。请保留一些活树，以便采集树液。
手持瓶子右键点击剥皮原木上渗出树液的位置，可以采集符文树液。
在结晶器中，将血液与任意石英粉结合
即可得到血石英。
制作粉碎轮需要使用机械合成器。
制作急速冷冻机以及催化其中的反应，需要使用薄荷粉和霜薄荷。
灵魂祭坛可以制作多种魔法物品。
加工时，祭坛会使用基座上的物品材料。
加工还需要灵魂，可以直接将它们放在灵魂祭坛上。
祭坛可以储存超过当前配方所需数量的灵魂。剩余灵魂会保留，供下次加工使用。
使用灵魂坩埚和不同的&o驱动核心&r，可以生成多种资源。
将符文放在砧板上敲碎，或使用磨粉机处理，可以获得灵魂。
用少量流明燃液通过注液器灌注软糖环，可以复制软糖环。
合理配置设施后，就可以持续生产流明燃液。
使用冶金灌注机可以制作控制电路。
使用正确的压印模具冷却熔融巧克力，可以制作巧克力碎片。
也可以将现有的巧克力物品放在加热的置物盆中熔化，取得所需原料。
使用石灰岩、余烬面粉和灰烬可以制作焦炉砖。
可燃物完全烧毁后，使用铲子可以收集灰烬。
将大型发酵器竖直堆叠，并从底部加热，可以制作烈焰燃料。
物品必须使用漏斗送入该结构。
使用粉碎轮粉碎烈焰人燃烧室，可以获得烈焰粉和烈焰棒。
利用烈焰人燃烧室，可以从维度 16 的无尽血海中提取铁。
你似乎并不关心这些血液的来源……
这个维度中的刷石机会生成硫磺石。
粉碎硫磺石可以获得下界岩、硫以及少量钴。
将提取机放在原木上，并在机器旁放置熔岩和炼金灰块，即可持续提取树液。''',
5: '''利用图腾魔法，可以扭曲并腐化周围的自然环境。
在底部放置图腾基座，再在上方堆叠五个符文原木，构成图腾。
进行仪式需要将五份奥术灵魂放在图腾上。
手持图腾法杖右键点击图腾基座，即可开始仪式。灵魂木生长体有较高概率出现，但仍可能失败。使用骨粉可以加快生长。
利用风暴群岛中的祭坛，可以借助当地天气的能量强化特定物品。
请按下方图片，在祭坛顶部建造一座小型避雷针结构。
将需要转化的物品放在结构下部的基座上。
&l只有避雷针中的蓄电器完全充满电，按下结构底部的按钮才会启动转化。&r
使用充能台，现在可以制作灌注合金。
避雷针多方块结构经过了一些改进。
现在，由闪电弹等来源产生的人工闪电击中任意钢栅栏，也能产生电力。
&l闪电祭坛可以将铜粉转化为闪电弹。&r
这种方式需要先消耗电力来发电。根据避雷针电力输出的速度，每次雷击应能带来约 200,000 RF 的净收益。
炼油厂可以使用三氧化硫和水生产硫酸。
这座噪声极大的设施几乎可以熔化或合金化所有材料。
请配戴合适的听力防护装备。
这座高 16 个方块的多方块结构可以对原油进行分馏，供进一步加工使用。
可以使用投影仪辅助建造，确保结构正确。
高压精炼装置可以根据输入的是重油还是轻油，分别制作塑料或电路板。
建议为两种配方分别配置专用机器。
使用弓或发射器发射大型箭矢，可以射击外星丘陵中的奇异结构。
命中结构后，隐藏的外星晶体会显露出来。
这些晶体仅会存在数秒，因此需要迅速挖掘。
实现挖掘自动化后，每支箭矢能够获得更多晶体。
高科技电路板是最终阶段机器的重要基础组件。
现在可以制作轻型工程块，用于建造工业发酵机。
重型工程块可以用于建造更复杂的多方块结构。
如果不确定多方块结构的建造方式，请使用投影仪辅助。
利用焊接机，可以开始制作基础组件。
这台机器需要预先配置配方，因此建议制作多台。
使用乙醇和处于超热状态的搅拌器，可以制作酚醛树脂。
某个维度几乎全部由蛋糕层组成，因此制作烈焰蛋糕应当容易得多。
清洗灵魂沙可以获得下界石英。
在这个维度中，水和熔岩可以生成熔渣，粉碎后能够持续获得灵魂沙。
粉碎暗板岩有小概率获得灵魂石。
失落山谷中可以找到灵魂立方体。
手持灵魂石右键点击它，会消耗灵魂石并召唤一支亡灵军队。
这些亡灵会立即攻击你，但它们穿着死灵金属盔甲。
死灵金属的配方已经失传。将这些盔甲放入电弧炉中熔化，可能是获得死灵金属锭的唯一方法。
格隆密林中的格隆幼兽很有用。
向它们喂食不同物品，可以获得以下珍贵资源：
&lo&r 符文树液 → 火药
&lo&r 诅咒树液 → 无限粉末
手持任意斧子右键点击剥皮灵魂木，可以使树中隐藏的诅咒树液显露出来。
向格隆幼兽喂食诅咒树液，它就会排出无限粉末。
化学氧化机可以制作三氧化硫。
三氧化硫以气体形式产出，使用回转式气液转换机可以将其转化为液体。
回收亡灵留下的死灵金属盔甲，可以制作虚空机架。
下界岩通过半自动磨粉机加工得到的下界岩刨屑，可以用于制作耐火钢涂层。
半自动磨粉机将是你的第一台末影接口机器。
末影接口机器需要在内部安装电容才能正常运行。
能量机壳可以用于制作实用拓展中的大多数机器。
向格隆幼兽喂食符文树液，它就会排出火药。
这个维度中的白垩可以粉碎成铝土矿。
此外，风暴群岛中的刷石机会生成白垩。
焊接机可以制作多种电子组件。
需要向它提供焊接合金，焊接合金由熔融铅和熔融锡制作。
固定式充能站利用外星晶体技术，可以随时间免费为高级工具充能。
这个维度中的暗板岩可以粉碎成粗镍。
此外，暗影海中的刷石机会生成暗板岩。
粉碎外星石可以获得锡。
外星石不会自然生成，只能通过外星丘陵中的刷石机获得。
磁轨炮几乎可以发射任何杆状物，命中时造成大量伤害。
可以在充能站中为磁轨炮充能。''',
6: '''一座废弃的六面体中，静置着一个损坏的矢量算子……
损坏的矢量算子可以修复，但必须预先规划，并迅速完成整个过程。
总共十二道加工步骤，必须依次完成。
第十二道也是最后一道步骤，是&l在 10 分钟内&r将损坏的矢量算子放回矢量调谐器。
在任意阶段，都可以将尚未完成的算子放回矢量调谐器，重置时间，并从第一步重新开始。
过程并不轻松，但你已经走到了这里。事先做好规划，你就能够完成它。
你能够做到，祝你好运！
如果损坏的矢量算子意外丢失，可以站在矢量调谐器旁执行下列命令，将其重置：
现实边缘的真实情况尚无记载。
只有亲自抵达这里，才能知道需要做些什么……''',
8: '''跃迁通量可以将某些材料转化为其他材料。
纯粹黑暗是重要的合成材料。
请查阅《仪式操作指南》，了解该仪式的执行方式。
将特定物品投入薰衣草原野中的垂泪之井，可以进行转化。转化需要数秒。
建议将该过程自动化。
使用两个破眼器可以破坏眼柱的外壳，显露内部的绯红之眼。
在眼睛两侧各放置一个破眼器，再右键点击其中一个即可。
破坏腐肉之眼可以获得眼球卵黄。
窥视电路用于多种后期机器和高级组件。请将它及其材料的生产自动化。
本章科技路线中的多种配方需要使用玄钢。
在遗弃平原中，使用掘地箭命中虚空灵魂骑士，可以剥落一部分盔甲。
拾取遗弃熔渣后，可以用来制作遗弃青铜或魂金。
利用仪式法阵，可以将绯红之眼束缚在矢量算子中。它会将你带往何处尚不明确。
只有亲自尝试才能知道……
合金炉可以制作强化合金和魂金。
制作科技光学组件需要使用切片拼接机。
开始进行仪式前，需要先制作荒寂匕首。
随后请仔细阅读指南书，了解仪式法阵的使用方式。
使用化合机，可以将这个维度中的阿尔法花加工成阿尔法粒子。
阿尔法玫瑰和阿尔法蒲公英都可以使用有机灌注机生产。
默认立方体可以使用阿尔法黏土制作。
放置缺失核心，再手持阿尔法粒子右键点击，会将周围环境腐化成缺失方块；采集这些方块可以获得缺失物品。
将缺失物品献祭给垂泪之井，可以获得零点物品。
击败非玩家后，会掉落缺失核心。
请查阅《仪式操作指南》，了解该仪式的执行方式。
你可以重新捕获这些眼睛，用于自己的机器。
请查阅《仪式操作指南》，了解该仪式的执行方式。
手持跃迁通量右键点击魔力钻石块，可以将其转化为龙石块。
手持跃迁通量右键点击已经放置的金属块，可以进行金属转化。
现在可以进行以下转化：
&lo&r 铅 → 锡
&lo&r 锡 → 铜
&lo&r 铜 → 铁
&lo&r 铁 → 银
&lo&r 银 → 金
在薰衣草原野的任意位置，手持瓶子右键点击即可装入末影空气。
梦之木会自然生长在薰衣草原野，因此可以直接获取。
使用灵魂灌注祭坛可以制作神秘宝石。
遗弃神像的成本较高，但可以实现完整的自动化生产。
开始正式生产前，请将它的组件生产妥善自动化。
超级计算机是最终阶段的物品之一。
开始正式生产前，请将它的组件生产妥善自动化。
腐肉-485 的地面中偶尔可以找到腐肉巨口。
向它喂食巧克力蛋糕，它就会吐出甜食牙。
制作模块化反应堆需要使用这三台机器。
使用反应室可以将错误立方体加工成反物质。
将反物质结晶，可以获得原子合金。
建造模块化反应堆并不容易。开始正式生产前，请将它的组件生产妥善自动化。
遗弃平原各处可以找到远古废料。将其与金结合，即可制作下界合金。
粉碎末地石可以获得末影粉。
使用离心机处理反转沙，可以获得萤石粉。
两种眼睛都可以在灵魂祭坛中持续生产。'''
}

TITLE_PAIRS='''Press the Big Red Button|按下红色大按钮
Getting Started|开始旅程
I will Break all the Things!|我要挖掘所有方块！
Excavate all the Things|挖掘一切
The Chunks will be Loaded|区块将保持加载
Loading Chunks|加载区块
Hand over the Library|交出图书馆
The Akashic Tome|阿卡什宝典
Understood|已了解
Load Chunks with care|谨慎加载区块
In Case of Emergency|紧急情况处理
Collecting Rocks|收集石材
Droop Soup|垂果汤
Dimensional Tourist|维度旅客
Machine Frame|机器框架
Universal Cable|通用线缆
Alien Tech|外星科技
Inscribing|压印加工
Digital Storage|数字存储
Silicon|硅
Getting the Presses|获取压印模板
Redstone Generator|红石生成器
Seared Cobblestone Generator|焦黑圆石生成器
Utility Machines|实用机器
Making Rubber|制作橡胶
Busy Hands|忙碌的机械手
Auto Crafting|自动合成
Constructing a Nuclear Furnace|建造核熔炉
Petal Apothecary|花药台
Defusing a Nuclear Bomb|拆除核弹
Endless Silver|无尽白银
Pure Daisy|白雏菊
Hazmat Suit|防化服
Collecting Radon|收集氡气
Creating more Cores|制作更多核心
The Goop Cycle|黏液循环
Zinc Quarry|锌矿采掘场
Rewinding Time|倒转时间
Osmium Mining|开采锇
Interdimensional Transceiver|跨维度收发器
Hoarding Diamonds|储备钻石
Renewable Gold|可再生金
Obtaining a Timestone|获取时间石
Time has been Folded|时间已折叠
Timewarping Vectors|矢量算子的时间跃迁
Upload your Power|上传电力
Nuclear Power|核能发电
Pack your Bags|准备背包
Catching a Blaze|捕获烈焰人
Runic Altar|符文祭坛
Energized Glowstone|充能荧石
Building a Foundry|建造铸造设施
Crushing Wheels|粉碎轮
Runic Sap|符文树液
Mechanical Crafting|机械合成
Take a Mint|来一份薄荷
Smashing Runes|粉碎符文
Collecting all the Rings|收集所有环
I have cycled the gummies|已建立软糖循环
The Infinite Gummy Cycle|无限软糖循环
Coke Oven|焦炉
Bulk Fermenter|大型发酵器
Sacrificing Blazes|献祭烈焰人
Renewable Iron|可再生铁
Wireless Terminal|无线终端
Brimstone Generator|硫磺石生成器
Infinite Sap Extraction|无限树液提取
Blaze Vector Operator|烈焰矢量算子
Totem Magic|图腾魔法
Lightning in a Bottle|瓶装闪电
Harnessing the Power of the Gods|利用神明的力量
Generatring Extraterrestrial Crystals|生成外星晶体
Advanced Electronic Component|高级电子元件
The Soul Cube|灵魂立方体
Grains of Inifinity|无限粉末
Infusing with Oxygen|氧气灌注
Void Chassis|虚空机架
Renewable Diamonds|可再生钻石
Renewable Gunpowder|可再生火药
Renewable Aluminium|可再生铝
Renewable Nickel|可再生镍
Renewable Tin|可再生锡
The Infinity Vector|无限矢量算子
The Final Process|最终加工流程
Lost Vector Reset|重置丢失的算子
I must Investigate this Further|需要进一步调查
The Edge of Reality|现实边缘
Ritual of Darkness|黑暗仪式
The Weeping Well|垂泪之井
Breaking Out the Crimson Eyes|取出绯红之眼
Peeking Circuits|窥视电路
Dark Steel|玄钢
Obtaining Forsaken Bronze|获取遗弃青铜
The Ritual Circle|仪式法阵
Alpha Particles|阿尔法粒子
Default Cube|默认立方体
Duplicate that what is Missing|复制缺失之物
Ritual of the Missing|缺失者仪式
Ritual of Binding|束缚仪式
Transmuting into a Dragonstone|转化为龙石
I am a Alchemist now|我已成为炼金术士
Lead into Gold|点铅成金
Ender Air Bottle|末影空气瓶
Supercomputer|超级计算机
Obtaining a Sweet Tooth|获取甜食牙
Nuclear Industries|核工业
Modular Reactor|模块化反应堆
Ender Dust|末影粉
Renewable Eyeballs|可再生眼球'''

SUB_PAIRS='''Pressing the Big Red Button|按下红色大按钮
See Where it Takes you|看看它会带你去哪里
Yes there is Veinminer|这里提供连锁挖掘
Loading what you are not Observing|加载视野之外的区块
Knowlege is Power|知识就是力量
This is my Rock Collection|这是我的石头收藏
I've got the Power|我有电力了
Visiting the Scrap Yard|参观废料场
Firing up the Engines|启动引擎
Burning Dead Things|燃烧死去的植物
The Fruit Would Droop|果实向下垂落
Take a Polaroid Picture|拍一张拍立得照片
Almost Autocrafting|接近自动合成
The Beginning of Everything|万物的开端
What Happened to the Fridge?!|冰箱发生了什么？！
Become Dust!|化为粉末！
Needs Flex Tape™|需要 Flex Tape™ 胶带
Your items on a Disk|把物品存进磁盘
Why is it Blue?|为什么是蓝色？
Powered by a Magma Ocean|由熔岩海供能
Magnetic Rock|磁性岩石
They Call it a Mine|他们称之为矿井
Hydaullic Press|液压机
Not From Outer Space|来自外太空以外的地方
In My Talons, I Shape Clay|在利爪中塑造黏土
Power is Power!|力量就是力量！
Not Glue|橡胶
The Basics of Automation|自动化基础
What is my Purpose?|我的用途是什么？
Electrical Kiln|电力窑炉
Making Machines that Make more Machines|制造能够制造机器的机器
3.6 Roentgen|3.6 伦琴
Now I am Become Death|现在我成为死神
I got this from a Chance Cube|这是从幸运方块中获得的
Pools of Silver|白银之池
Ther-mi-o-nic|热电子技术
Wedding Bouquet|婚礼花束
Taste the Flames of Sulfuron!|品尝萨弗隆的烈焰！
Say my name|说出我的名字
Breaking News!|突发新闻！
No Portal Fluid Needed|无需传送门流体
This Place is Still Better than Bilewater|这里仍然比胆汁水域好
Beryllium Shell|铍制外壳
Fast Travel|快速旅行
We're Rich!|我们富有了！
Let that Zinc in|让锌进入
Timey Wimey|奇妙的时间
Kovarex Enrichment Process|科瓦雷克斯浓缩处理
Thinking Out of the Box|突破思维局限
Shine Bright|闪耀光芒
King under the Mountain|山下之王
I Have Come to Bargain|我是来谈条件的
Its Rewind Time|时间倒转了
Thats Lapis|那是青金石
Please Download Additional RAM|请下载更多内存
May all your Bacon Burn|愿你的培根全部烧焦
An Endoflame, what is that?|火红莲是什么？
Pour it While its Hot|趁热浇铸
Crushing It|粉碎处理
Tree Juice|树木的汁液
Evil Create|邪恶的机械动力
Might and Magic|力量与魔法
"I Didn't Enjoy Eidolon"|我不喜欢 Eidolon
Rings of Power|力量之环
Safe for Consumption|可以安全食用
Big Furnace|大型熔炉
Fermenting in Bulk|大规模发酵
Hell is Full, Blood is Fuel|地狱已满，鲜血为燃料
There are no Strings on me|我已摆脱束缚
Liquifying a Dimension|液化一个维度
Twisting Trees|扭曲树木
Ride the Lightning|驾驭闪电
Raw Unlimited Power|原始而无限的力量
Bvvzzzzzzzt|嗡嗡嗡滋滋滋
This Will Make the Biters Angry|这会激怒异虫
What am I Supposed to do \\nwith Heavy Oil Residue?|该如何处理\\n重油残渣？
Making a Rock do the Thinking|让石头进行思考
Smarter Thinking Component|更先进的思考组件
The Sun is a Deadly Lazer|太阳是致命的激光
Dance with the Dead|与亡者共舞
I Got a Pet|我有宠物了
Beep-Beep, Oxygen, 30 Seconds|哔哔，氧气，剩余 30 秒
For the God Emperor|为了神皇
Conceptual Erasure|概念抹除
Parallel Cowboy Universe|平行牛仔宇宙
Venture out into the Unknown|深入未知领域
404|404
To Odin, from Odin|献给奥丁，来自奥丁
I See You|我看见你了
Start to worry when your Electronics start to look back|电子设备开始回望你时，就该担心了
Divided by Zero|除以零
I'm sorry Dave, I'm Afraid I can't do that|抱歉，戴夫，恐怕我无法这样做
We are Friends. Welcome. Sit and Rest.|我们是朋友。欢迎。请坐下休息。
What?|什么？
Who?|谁？
Agh Burzum-ishi Krimpatul|在黑暗中束缚它们
Is this how the Elves do it?|精灵也是这样做的吗？
Full Metal Alchemist|钢之炼金术师
Bottle of Nothing|空无之瓶
The Words Become Flesh|言语化为血肉
Is Anyone There?|有人在吗？
We are the Music Makers, and we are the Dreamers of Dreams|我们创造音乐，也编织梦想
Super Powerful Kettle|超强力热水壶
Dans|Dans
Eye Spy|眼睛的窥视'''

DIMENSIONS={'Stranded-233':'搁浅-233','Copper Graveyard':'铜之墓地','The Fenspire Deep':'沼塔深渊','The Redvein Expanse':'赤脉旷野','Ferrum-6':'铁域-6','The Horizon of Cinders':'余烬地平线','The Silver Forest':'银色森林','The Coin Continuum':'货币连续体','The Fission Fields':'裂变原野','The Frostbloom Storm':'霜花风暴','Timber Lakes':'木材湖泊','The Brimwood Planes':'硫木平原','The Sugarscape':'糖境','The Azurewood':'蔚蓝森林','Blood Ocean':'血海','Extraterrestrial Hills':'外星丘陵','The Umbral Sea':'暗影海','The Lost Valley':'失落山谷','Storm Islands':'风暴群岛','The Gronglegrowth':'格隆密林','The Edge of Reality':'现实边缘','The Overworld':'主世界','Carrion-485':'腐肉-485','The Forsaken Planes':'遗弃平原','Lavender Fields':'薰衣草原野','Alpha-201':'阿尔法-201'}

def main():
    mapping={}
    titles=dict(line.split('|',1) for line in TITLE_PAIRS.splitlines())
    subtitles=dict(line.split('|',1) for line in SUB_PAIRS.splitlines())
    for path in sorted((ROOT/'config/ftbquests/quests/chapters').glob('*.snbt')):
        backup=ROOT/'localization/backups/quests'/path.name
        source=(backup if backup.exists() else path).read_text(encoding='utf-8')
        desc=[]; active=False
        for line in source.splitlines():
            if re.match(r'\s*description:',line):active=True
            if active:
                for raw in re.findall(r'"((?:\\.|[^"\\])*)"',line):
                    text=json.loads('"'+raw+'"')
                    if text and not text.startswith(('{image:','/')):desc.append(text)
            if active and ']' in line:active=False
        chinese=DESC[int(path.stem.split('_')[1])].splitlines()
        if len(desc)!=len(chinese):raise ValueError((path.name,len(desc),len(chinese)))
        mapping.update(zip(desc,chinese))
        for text in visible_strings(source):
            if text in mapping:continue
            clean=re.sub(r'^(?:&[0-9a-fk-or])+','',text).rstrip()
            prefix=re.match(r'^(?:&[0-9a-fk-or])*',text).group()
            if clean in titles:mapping[text]=prefix+titles[clean]
            elif clean in subtitles:mapping[text]=prefix+subtitles[clean]
            elif re.match(r'Chapter \d+$',text):mapping[text]='第 '+text.split()[-1]+' 章'
            elif any(text.endswith(name) for name in DIMENSIONS):
                name=next(n for n in DIMENSIONS if text.endswith(n))
                before=text[:-len(name)]
                before=before.replace('Welcome to dimension','欢迎来到维度').replace('Enter to dimension','进入维度').replace('Enter dimension','进入维度').replace('Enter the final destination','进入最终目的地').replace('Enter:','进入：')
                mapping[text]=before+DIMENSIONS[name]
            else:raise ValueError(('untranslated',text))
    # Corrections reviewed against namespace-qualified extracted terminology.
    corrections={'热电子加工机':'热电子加工台','赛特斯石英晶体':'塞特斯石英水晶','寒颤石':'寒栗石','辐射岩':'辐射石','核熔炉':'核能熔炉','雪花莲':'雪滴花','灵魂祭坛':'精魂祭坛','灵魂坩埚':'精魂坩埚','奥术灵魂':'奥术精魂','符文树液':'符文树脂','诅咒树液':'诅咒树脂','流明燃液':'荧光液','格隆幼兽':'油绿蚧','荒寂匕首':'荒芜匕首','遗弃神像':'遗弃者木偶','甜食牙':'蛀牙','无限粉末':'无限粉','霜薄荷':'冰雪薄荷糖','薄荷粉':'薄荷糖粉','垂果':'垂挂果','回转式气液转换机':'回旋式气液转换机','掘地箭':'采掘箭','灵魂灌注祭坛':'精魂灌注祭坛'}
    for key,value in list(mapping.items()):
        for old,new in corrections.items():value=value.replace(old,new)
        # Galena here is the Alex's Caves stone used by the generators.
        if 'Galena' in key:value=value.replace('方铅矿','方铅岩')
        if 'Mechanical Press' in key:value=value.replace('机械压力机','动力冲压机')
        if 'Spirits' in key or 'spirits' in key:value=value.replace('灵魂','精魂')
        mapping[key]=value
    (ROOT/'localization/quest_translations.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Mapped',len(mapping),'unique texts')

if __name__=='__main__':main()
