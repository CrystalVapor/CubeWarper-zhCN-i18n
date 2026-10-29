import json,re
from pathlib import Path
P=Path(__file__).parent
DATA=json.loads((P/'pending_main.json').read_text(encoding='utf-8'))
TABLE='''
<i>     Machines Primus|<i>     初代机器
ESDs|物品分配器
AE Infinity Booster|AE 无限增幅器
connect block inf|连接方块信息
Entity Links are small, cute buttons!|实体链接是小巧可爱的按钮！
Link Example|链接示例
Citadel Book!!!|Citadel 手册！！！
Space Station|空间站
Space Station (Gray)|空间站（灰色）
Space Station (Red)|空间站（红色）
None|无
Type:|类型：
Cape Customization|披风自定义
Cape Customization...|披风自定义……
No Modded Cape|无模组披风
Rotate Distance|旋转距离
Rotate Height|旋转高度
Rotate Speed|旋转速度
Citadel Patreon Customization|Citadel Patreon 赞助者自定义
Citadel Patreon Customization...|Citadel Patreon 赞助者自定义……
Reset|重置
Citadel Book|Citadel 手册
Potion Effect|药水效果
Fancy Item|精美物品
Icon Item|图标物品
Cloth Config Wiki|Cloth Config 维基
%1$s got knifed by %2$s!|%1$s 被 %2$s 用刀刺死了！
%1$s was poked by %2$s using %3$s!|%1$s 被 %2$s 使用 %3$s 刺死了！
Configured|模组配置
A->Z|A→Z 升序
Z->A|Z→A 降序
Boioioing!|弹——跳！
am|上午
pm|下午
Ticks|刻
Signal mode is controlled by computer|信号模式由计算机控制
Casings|机壳
Additionally, you can power the burner with redstone to make it burn even quicker|此外，还可以用红石信号驱动燃烧器，使其燃烧得更快
Recent ingredients:|最近使用的材料：
Blocks|方块
%s Block(s)|%s 个方块
{Player} was pricked to death|{Player} 被刺死了
Aversion Obelisk|排斥方尖碑
Copied data: %s|已复制数据：%s
Pasted data: %s|已粘贴数据：%s
Switched conduit probe mode to %s|导管探针模式已切换为 %s
Allows multiple chemical types to be transported on the same line|允许在同一条管线中传输多种化学品
Conduit Probe|导管探针
Soul Filter|灵魂过滤器
Change Probe Mode|切换探针模式
Allows multiple fluids to be transported on the same line|允许在同一条管线中传输多种流体
Transfer Rate %s mB/t|传输速率 %s mB/t
Mode: %s|模式：%s
Contains copied conduit data:|包含已复制的导管数据：
Copy/Paste|复制/粘贴
Probe|探测
Assembler Matrix Craft Core|装配矩阵合成核心
Assembler Matrix Frame|装配矩阵框架
Assembler Matrix Pattern Core|装配矩阵样板核心
Assembler Matrix Speed Core|装配矩阵加速核心
Assembler Matrix Wall|装配矩阵壁板
Success Chance: %s|成功概率：%s
Assembler Matrix|装配矩阵
Stop all crafting jobs and return ingredients|停止所有合成任务并退回材料
Only accepts crafting pattern|仅接受合成样板
Running Jobs: %s|运行中的任务：%s
Search pattern|搜索样板
Change search mode|切换搜索模式
Current: Output|当前：输出
Current: Input|当前：输入
Current: Input and Output|当前：输入与输出
Search by input, output or pattern provider name.|按输入、输出或样板供应器名称搜索。
Entro Shard|熵变碎片
Find Me|物品定位
Pull 1 Item From Nearby Inventories|从附近容器中抽取 1 个物品
Pull 1 Stack From Nearby Inventories|从附近容器中抽取 1 组物品
Team Property Defaults|队伍属性默认值
Allow Fake Players by ID|按 ID 允许模拟玩家
Named Fake Players|具名模拟玩家
Recipe Sync Warning|配方同步警告
Show a chat warning when the server doesn't provide synced recipes to JEI (e.g. vanilla servers, or servers without JEI installed).|服务器未向 JEI 提供同步配方时显示聊天警告（例如原版服务器或未安装 JEI 的服务器）。
Visibility of the top page buttons. Use AUTO_HIDE to only show it when there are multiple pages.|顶部翻页按钮的可见性。使用 AUTO_HIDE，仅在存在多页时显示。
Enable Crashing Test Items|启用崩溃测试物品
Adds ingredients to JEI that intentionally crash, to help debug JEI.|向 JEI 添加会故意引发崩溃的物品，以协助调试 JEI。
JEI is missing recipes. Please install JEI on the server to sync recipes to the client.|JEI 缺少配方。请在服务器安装 JEI，以便向客户端同步配方。
Next Recipe|下一个配方
Texture ID: %s|纹理 ID：%s
Gave %d players +%d hunger|已为 %d 名玩家增加 %d 点饥饿值
Gave %s +%d hunger|已为 %s 增加 %d 点饥饿值
Set %d players' hunger to %d|已将 %d 名玩家的饥饿值设为 %d
Set %s's hunger to %d|已将 %s 的饥饿值设为 %d
Gave %d players -%d hunger|已为 %d 名玩家减少 %d 点饥饿值
Gave %s -%d hunger|已为 %s 减少 %d 点饥饿值
Expected resource key '%s' to belong to registry '%s'.|资源键 '%s' 应属于注册表 '%s'。
Failed to save JSON at '%s'.|无法在 '%s' 保存 JSON。
Successfully removed biome modifier '%s' in %s seconds. Run /reload to activate pack at %s|已移除生物群系修饰器 '%s'，耗时 %s 秒。运行 /reload 以激活位于 %s 的资源包
Successfully emptied structure set '%s' in %s seconds. Run /reload to activate pack at %s|已清空结构集合 '%s'，耗时 %s 秒。运行 /reload 以激活位于 %s 的资源包
Enable Fluid Fog Fix|启用流体雾效修复
Sky Bronze Block|陨石青铜块
Sky Osmium Block|陨石锇块
%s not installed.|未安装 %s。
Sky Bronze Ingot|陨石青铜锭
Sky Osmium Ingot|陨石锇锭
Broken tags in Mekanism recipes detected, please check server logs for details. You will be missing some recipes and machines may not accept expected inputs.|检测到 Mekanism 配方中存在损坏的标签，请查看服务器日志了解详情。这会导致部分配方缺失，机器也可能无法接收预期的材料。
Need a server? Get one with %s|需要服务器？可通过 %s 获取
Bombs|炸弹
dynamic runtime resources|动态运行时资源
Virtual Resourcepack|虚拟资源包
Rubberwood Hanging Sign|橡胶木悬挂式告示牌
Rubberwood Wall Hanging Sign|墙上的橡胶木悬挂式告示牌
'''
MAP=dict(x.split('|',1) for x in TABLE.splitlines() if '|' in x)
MAP.update({
 'Flügel Tiara Flight Bar Height':'天翼族之冠飞行能量条高度',
 'Kain Vinosec - Endure Emptiness':'Kain Vinosec - 忍受空虚',
 'Kain Vinosec - Fight For Quiescence':'Kain Vinosec - 为宁静而战',
 'Hlzfss - Pancake Music':'Hlzfss - 松饼音乐',
 'Hlzfss - Heave Ho!':'Hlzfss - 嘿哟！',
 '§lEnable or disable individual effects':'§l启用或禁用各项效果',
 '§lSound Options':'§l声音选项', '§lPerformance Options':'§l性能选项',
 '§lParticle Options':'§l粒子选项', '§lCompatibility Options':'§l兼容性选项',
 'Hold §e§oShift§r and/or §e§oCtrl§r to fine tune amounts.':'按住 §e§oShift§r 和/或 §e§oCtrl§r 可精细调整数量。',
})
EXCLUDE_NS={'actuallyadditions','ae2','cofh_core','corpse','create','createdieselgenerators','creativecore','enderio','jei','mekanism','placebo','sophisticatedcore','supplementaries','lodestone'}
out={};excluded={}
for ns,m in DATA.items():
 for key,en in m.items():
  if en in MAP:out.setdefault(ns,{})[key]=MAP[en]
  elif ns in EXCLUDE_NS:
   excluded.setdefault(ns,{})[key]={'english':en,'reason':'格式模板、单位、命令参数、专有名称或作者署名'}
  elif ns=='botania' and key=='botania.subtitle.way':
   out.setdefault(ns,{})[key]='歌声吟唱'
(P/'manual_mod_translations_main_extra.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'excluded_main_extra.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Extra translated',sum(map(len,out.values())),'excluded',sum(map(len,excluded.values())))
