"""Build exact-key KubeJS localization; only player-visible literals are changed."""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'localization'
PACK = ROOT / 'resourcepacks/CubeWarper-Chinese-Bilingual'
NAMES = {
    'Warping Interface':'跃迁接口', 'Broken Warping Interface':'损坏的跃迁接口',
    'Warping Exhaust':'跃迁排气口', 'Warping Controls':'跃迁控制器',
    'Launch Button':'启动按钮', 'Time Warper':'时间跃迁器', 'Eye Breaker':'眼球破碎器',
    'Empty Vector Operator':'空白矢量算子', 'Old Vector Operator':'古旧矢量算子',
    'Charged Vector Operator':'充能矢量算子', 'Fluix Vector Operator':'福鲁伊克斯矢量算子',
    'Nuclear Vector Operator':'核能矢量算子', 'Blazing Vector Operator':'烈焰矢量算子',
    'Lightning Vector Operator':'闪电矢量算子', 'Broken Vector Operator':'损坏的矢量算子',
    'Infinity Vector Operator':'无限矢量算子', 'Crimson Eye':'绯红之眼', 'Hexahedron':'六面体',
    'Warping Frame':'跃迁框架', 'Warping Frame Slab':'跃迁框架台阶',
    'Warping Frame Platform':'跃迁框架平台', 'Rusted Warping Frame':'锈蚀的跃迁框架',
    'Warping Vent':'跃迁通风口', 'Rusted Warping Vent':'锈蚀的跃迁通风口',
    'Crimson Statue':'绯红雕像', 'Eye Pillar':'眼球立柱', 'Ancient Bricks':'远古石砖',
    'Ancient Brick Stairs':'远古石砖楼梯', 'Ancient Brick Slab':'远古石砖台阶',
    'Ancient Brick Wall':'远古石砖墙', 'Ancient Runes':'远古符文',
    'Chiseled Ancient Bricks':'雕纹远古石砖', 'Lightning Plinth':'闪电基座',
    'Bottom of a Machine Frame':'机器框架底部', 'Top of a Machine Frame':'机器框架顶部',
    'Soul Cube':'灵魂立方体', 'Ancient Redstone Core':'远古红石核心',
    'Emergency Fuses':'应急保险丝', 'Gold Coins':'金币', 'Bag of Gold Coins':'金币袋',
    'Opened Nuclear Bomb':'打开的核弹', 'Computer':'计算机', 'Supercomputer':'超级计算机',
    'Recaptured Consciousness':'重新捕获的意识', 'Consciousness Container':'意识容器',
    'Modular Reactor':'模块化反应堆', 'Empty Modular Reactor':'空模块化反应堆',
    'Vector Tuner':'矢量调谐器', 'Block of Shiny Ingot':'闪亮锭块',
    'Light Engineering Frame':'轻型工程框架', 'Heavy Engineering Frame':'重型工程框架',
    'Error Cube':'错误立方体', 'Lightning in a Bottle':'瓶装闪电', 'Crowbar':'撬棍',
    'Unbaked Guano Blast Brick':'未烧制的鸟粪高炉砖', 'Guano Blast Brick':'鸟粪高炉砖',
    'Cooling Unit':'冷却单元', 'Alpha Particles':'α粒子', 'Empty Shell':'空弹壳',
    'Energized Redstone':'充能红石', 'Soul Tube':'灵魂管', 'Recall Tube':'召回管',
    'Shiny Ingot':'闪亮锭', 'Plastic':'塑料', 'Empty Circuit Board':'空白电路板',
    'High-Tech Circuit Board':'高科技电路板', 'Peeking Circuit':'窥探电路',
    'Seeking Circuit':'寻踪电路', 'Grains of Infinity':'无限粉',
    'Party Popper':'派对礼炮', 'Tiny Confetti Popper':'迷你彩纸礼炮', 'Adilette':'阿迪拖鞋',
    'Chocolate Chip':'巧克力碎', 'Cobblestone':'圆石', 'Mossy Cobblestone':'苔石',
    'Bricks':'红砖块', 'Solder Alloy':'焊料合金', 'Solder Alloy Bucket':'焊料合金桶',
    'Redacted':'已删改', 'Seared Alloy':'焦黑合金', 'Gold Hand':'金质机械手',
    'Power Casing':'动力机壳', 'Soldering Machine':'焊接机', 'Missing Core':'缺失核心',
    'Nuclear Dynamo':'核能发电机', 'Block of Seared Alloy':'焦黑合金块',
    'Seared Girder':'焦黑梁', 'Seared Scaffolding':'焦黑脚手架', 'Seared Door':'焦黑门',
    'Seared Casing':'焦黑机壳', 'Seared Funnel':'焦黑漏斗', 'Seared Tunnel':'焦黑隧道',
    'Seared Table Cloth':'焦黑桌布', 'Seared Bars':'焦黑栏杆', 'Seared Ladder':'焦黑梯子',
    'Hardened Insulating Resin':'硬化绝缘树脂', 'Blood':'血液',
    'Block of Blood Quartz':'血石英块', 'Blood Quartz Lamp':'血石英灯',
    'Blood Quartz Tiles':'血石英砖', 'Small Blood Quartz Tiles':'小型血石英砖',
    'Blood Quartz Lamps':'血石英灯',
    'Blood Quartz Lamps activate on a Redstone signal':'血石英灯接收到红石信号时会亮起',
    'Polished Blood Quartz':'磨制血石英', 'Blood Quartz':'血石英',
    'Polish some Blood Quartz':'磨制一些血石英', 'Droop Soup':'垂挂果汤',
    'Timestone':'时间石', 'Shiverstone Osmium Ore':'寒栗石锇矿石',
}
TOOLTIPS = {
    'Adds 1':'加 1', 'Adds 2':'加 2', 'Multiplies by 3':'乘以 3',
    'Multiplies by 4':'乘以 4', 'Multiplies by 6':'乘以 6', 'Multiplies by 8':'乘以 8',
    'Divides by 0':'除以 0', 'Collapses all destinations into one':'将所有目的地坍缩为同一个目的地',
    'Will not be consumed when used in the Chiller':'在冷冻机中使用时不会被消耗',
    'Step 1 -> Right-Click on Ancient Redstone':'步骤 1 → 右键点击远古红石',
    'Step 2 -> Age With the Shrine in Dimension 8 ':'步骤 2 → 在维度 8 的祭坛上进行陈化 ',
    'Step 3 -> Spout with Lumisene':'步骤 3 → 使用注液器注入荧光液',
    'Step 4 -> Spirit Craft with Runes in a Spirit Altar':'步骤 4 → 在精魂祭坛中与符文进行精魂灌注',
    'Step 5 -> Combine with Blaze Fuel':'步骤 5 → 与烈焰燃料结合',
    'Step 6 -> Charge at the Lightning Shrine':'步骤 6 → 在闪电祭坛充能',
    'Step 7 -> Combine with metals in the Arc Furnace':'步骤 7 → 在电弧炉中与金属结合',
    'Step 8 -> Drop into the Weeping Well':'步骤 8 → 投入悲泣之井',
    'Step 9 -> Combine with 8 Modular Reactors in the Ritual Cricle':'步骤 9 → 在仪式法阵中与 8 个模块化反应堆结合',
    'Step 10 -> Combine with 8 Forsaken Idols in the Ritual Cricle':'步骤 10 → 在仪式法阵中与 8 个遗弃者木偶结合',
    'Step 11 -> Combine with 8 Super Computers in the Ritual Cricle':'步骤 11 → 在仪式法阵中与 8 台超级计算机结合',
    'Step 12 -> Place this back on the Vector Tuner within 10 minutes':'步骤 12 → 在 10 分钟内将其放回矢量调谐器',
    '⚠ Command blocks are disabled on this server. ⚠':'⚠ 此服务器已禁用命令方块。⚠',
    'This will break the pack down the line, so please enable them.':'这会使整合包后续流程无法正常运行，请启用命令方块。',
    'Set enable-command-block=true in server.properties.':'请在 server.properties 中设置 enable-command-block=true。',
}

def bilingual(zh, en):
    reset = '§r' if '§' in zh or '§' in en else ''
    return f'{zh}{reset}（{en}{reset}）'

def translate_name(en):
    if en == '§4§l§kUnknown§r§4§l Vector Operator':
        return '§4§l§k未知§r§4§l矢量算子'
    prefix = re.match(r'(?:§[0-9a-fk-or])*', en).group()
    bare = en[len(prefix):]
    if bare not in NAMES:
        raise ValueError(f'Name requires translation: {en}')
    return prefix + NAMES[bare]

def main():
    entries = {}
    def add(ns, key, en):
        entries.setdefault(ns, {})[key] = {'english':en, 'chinese':translate_name(en)}
    for file in sorted((ROOT/'kubejs/startup_scripts').glob('*.js')):
        text = file.read_text(encoding='utf-8')
        kind = 'item' if file.name == 'init_fluids.js' else 'block'
        if file.name == 'init_fluids.js':
            add('kubejs', 'fluid.kubejs.solder_fluid', 'Solder Alloy')
            add('kubejs', 'block.kubejs.solder_fluid', 'Solder Alloy')
            add('kubejs', 'item.kubejs.solder_fluid_bucket', 'Solder Alloy Bucket')
            add('kubejs', 'fluid_type.kubejs.solder_fluid', 'Solder Alloy')
            continue
        for section in re.split(r"StartupEvents\.registry\('(block|item)'", text):
            if section in ('block','item'):
                kind = section
                continue
            for match in re.finditer(r"event\.create\(['\"`]([^'\"`$]+)['\"`](?:,\s*['\"][^'\"]+['\"])?\)\s*\.displayName\(['\"`]([^'\"`$]+)['\"`]\)", section):
                ident, en = match.groups()
                add('kubejs', f'{kind}.kubejs.{ident}', en)
            for match in re.finditer(r'rotatable(?:_side)?\("([^"\n]+)",\s*"([^"\n]+)"', section):
                ident, en = match.groups()
                add('kubejs', f'block.kubejs.{ident}', en)
            for match in re.finditer(r'operator\("([^"\n]+)",\s*"([^"\n]+)",\s*\x27([^\x27]+)\x27', section):
                ident, name, color = match.groups()
                add('kubejs', f'block.kubejs.vector_operator_{ident}', f'{color}{name} Vector Operator')
            for ident in re.findall(r'eye\("([^"\n]+)"\)', section):
                add('kubejs', f'block.kubejs.{ident}', 'Crimson Eye')
    for step in range(2,13):
        add('kubejs', f'block.kubejs.vector_operator_step{step}', '§8§lBroken Vector Operator')
    renames = (ROOT/'kubejs/client_scripts/renaming.js').read_text(encoding='utf-8')
    for kind, ident, en in re.findall(r'rename_(item|block)\("([^"\n]+)",\s*"([^"\n]+)"\)', renames):
        ns, name = ident.split(':')
        add(ns, f'item.{ns}.{name}', en)
        if kind == 'block':
            add(ns, f'block.{ns}.{name}', en)
    add('untagged_mobs', 'fluid_type.untagged_mobs.fluid_blood', 'Blood')
    for path in (ROOT/'kubejs/assets').glob('*/lang/en_us.json'):
        for key, en in json.loads(path.read_text(encoding='utf-8')).items():
            add(path.parents[1].name, key, en)
    OUT.mkdir(exist_ok=True)
    (OUT/'kubejs_translations.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    merged = {}
    for ns, values in entries.items():
        path = PACK/'assets'/ns/'lang/zh_cn.json'
        path.parent.mkdir(parents=True,exist_ok=True)
        data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
        for key, item in values.items():
            data[key] = bilingual(item['chinese'],item['english'])
            merged[key] = data[key]
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # KubeJS language events override generated startup names and runtime renaming.
    js = '// Generated by localization/build_kubejs.py\nClientEvents.lang(\'zh_cn\', event => {\n'
    for key, val in sorted(merged.items()):
        js += f'  event.add({json.dumps(key,ensure_ascii=False)}, {json.dumps(val,ensure_ascii=False)})\n'
    js += '})\n'
    (ROOT/'kubejs/client_scripts/zz_cube_warper_zh_cn.js').write_text(js,encoding='utf-8')
    for rel in ('kubejs/client_scripts/tooltips.js','kubejs/server_scripts/!main/commandblock_check.js'):
        path = ROOT/rel
        backup = OUT/'backups/kubejs'/rel
        backup.parent.mkdir(parents=True,exist_ok=True)
        if not backup.exists():
            shutil.copy2(path,backup)
        original = backup.read_text(encoding='utf-8')
        def replace(match):
            en = match.group(2)
            if en not in TOOLTIPS:
                raise ValueError(f'Tooltip requires translation: {en}')
            return match.group(1) + json.dumps(bilingual(TOOLTIPS[en],en),ensure_ascii=False) + ')'
        translated = re.sub(r"(Text\.(?:gray|red|blue)\()'([^'\n]*)'\)",replace,original)
        path.write_text(translated,encoding='utf-8')
    print(f'KubeJS exact keys: {len(merged)}; visible literals: {len(TOOLTIPS)}')

if __name__ == '__main__':
    main()
