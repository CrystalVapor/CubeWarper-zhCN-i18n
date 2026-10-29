import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent
missing=json.loads((BASE/'missing_zh_cn.json').read_text(encoding='utf8'))
rows=r'''
Saved successfully|保存成功
Not enough command arguments|命令参数不足
Unknown config '%s'|未知配置 '%s'
Range: [%s;%s]|范围：[%s;%s]
After game restart|重启游戏后
In main menu|在主菜单中
Always|始终
Synchronized|已同步
Saved: %s|保存：%s
Advanced|高级
Character field cannot be empty!|字符字段不能为空！
Value '%s' is not a valid number!|值 '%s' 不是有效数字！
Value '%s' is not from interval <%s;%s>!|值 '%s' 不在区间 <%s;%s> 内！
Value '%s' does not match pattern \%s\!|值 '%s' 不匹配模式 \%s\！
Advanced mode|高级模式
Will toggle rendering of advanced configuration fields for all mods|切换所有模组高级配置字段的显示
Alpha: %s|透明度：%s
Blue: %s|蓝色：%s
Green: %s|绿色：%s
Red: %s|红色：%s
Select color|选择颜色
Cancel|取消
Confirm|确认
Select config|选择配置
Child value validation failed|子项值验证失败
Child value contains warnings|子项值存在警告
Requires game restart to be applied|需要重启游戏才能应用
Add element|添加元素
Apply|应用
Back|返回
Disabled|已禁用
Open|打开
Revert changes|还原更改
Rollback changes|回滚更改
Are you sure you want to discard your currently made changes?|确定要放弃当前更改吗？
Use default config|使用默认配置
Are you sure you want to reset config back to default values?|确定要将配置重置为默认值吗？
Revert to default|恢复默认值
Save & Close|保存并关闭
Enabled|已启用
And %d more...|以及另外 %d 项……
This is usually caused by a mismatched mod set between the client and server.|这通常由客户端和服务器的模组不一致导致。
Unknown backend '%s'|未知后端 '%s'
The current Flywheel backend is '%s'|当前 Flywheel 后端为 '%s'
The Flywheel backend is now '%s'|Flywheel 后端已设为 '%s'
The requested backend '%s' is not available|请求的后端 '%s' 不可用
Update limiting is currently disabled|当前已禁用更新限制
Update limiting is currently enabled|当前已启用更新限制
Update limiting is now disabled|更新限制已禁用
Update limiting is now enabled|更新限制已启用
Not using light directions|当前未使用光照方向
Using light directions|当前正在使用光照方向
Set light directions to off|光照方向已关闭
Set light directions to on|光照方向已开启
values|个值
value|个值
Client Config|客户端配置
Common Config|通用配置
Discard Changes|放弃更改
Click here to discard all the changes you made|点击此处放弃所有更改
Discarding %1$s unsaved %2$s|正在放弃 %1$s %2$s，尚未保存
Don't Save|不保存
Go Back|返回
Leaving with %1$s unsaved %2$s for this config|退出此配置时仍有 %1$s %2$s 尚未保存
Access Configs of other Mods|访问其他模组的配置
Access Configs for Mod:|访问模组配置：
This Mod does not have any configs registered or is not using Forge's config system|此模组未注册配置，或未使用 Forge 配置系统
At least one changed value will require you to relog to take full effect|至少一项更改需要重新进入世界才能完全生效
Reset All|全部重置
Click here to reset all settings to their default value|点击此处将所有设置重置为默认值
Resetting all settings of the %s config. Are you sure?|即将重置 %s 配置的所有设置。确定吗？
At least one changed value will require you to restart your game to take full effect|至少一项更改需要重启游戏才能完全生效
Save Changes|保存更改
Click here to save your current changes|点击此处保存当前更改
Save|保存
Saving %1$s changed %2$s|正在保存 %1$s 个已更改的 %2$s
Ctrl + F to Search...|按 Ctrl + F 搜索……
Server Config|服务器配置
Locked|已锁定
You do not have enough permissions to edit the server config; you can still look at the current values here though|你没有编辑服务器配置的权限，仍可在此查看当前配置值
Stored individually per World|每个世界独立存储
Gameplay settings can only be accessed from the in-game menu after joining a World or Server|进入世界或服务器后，才能通过游戏内菜单访问游戏设置
Unlocked|已解锁
You have enough permissions to edit the server config; changes you make here will be synced with the server when you save them|你具有编辑服务器配置的权限；保存后，此处的更改将同步至服务器
changes|项更改
change|项更改
Range|范围
Changing this value will require a _relog_ to take full effect|更改此值需要 _重新进入世界_ 才能完全生效
Changing this value will require a _restart_ to take full effect|更改此值需要 _重启游戏_ 才能完全生效
Temporarily set %1$s's Flying Speed to %2$s|将 %1$s 的飞行速度临时设为 %2$s
Unable to find the specified config|无法找到指定配置
Ponder|思索
%1$s had their world rocked!|%1$s 的世界被震碎了！
%1$s was tragically enlightened!|%1$s 被闪电启迪，悲惨身亡！
%1$s met a frigid fate!|%1$s 遭遇了冰冷的命运！
'''
exact=dict(line.split('|',1) for line in rows.strip().splitlines())
exact.update({
    ' See the client logs for more details.\nThe following registry entry namespaces may be related:\n\n':' 详情请查看客户端日志。\n以下注册表条目命名空间可能与此有关：\n\n',
    'Received %d registry entries that are unknown to this client.\n':'收到了 %d 个此客户端无法识别的注册表条目。\n',
    'Received a registry entry that is unknown to this client.\n':'收到了一个此客户端无法识别的注册表条目。\n',
})
out,excluded,residual={},{},{}
for ns,values in missing.items():
    for key,record in values.items():
        if not record['english_source'].get('nested_archives'):
            continue
        en=record['english']
        if key.startswith('_comment') or key.endswith('.keyword') or en in {'PNT','MC 1.20.1','Ctrl +'}:
            excluded.setdefault(ns,{})[key]={'english':en,'reason':'metadata_search_keyword_or_unit'}
        elif en in exact:
            out.setdefault(ns,{})[key]=exact[en]
        else:
            residual.setdefault(ns,{})[key]=en
for name,data in [('manual_mod_translations_terms_nested.json',out),('manual_mod_exclusions_terms_nested.json',excluded),('manual_terms_nested_residual.json',residual)]:
    (BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print({'translated':sum(map(len,out.values())),'excluded':sum(map(len,excluded.values())),'remaining':sum(map(len,residual.values()))})
