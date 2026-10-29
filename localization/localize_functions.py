"""Localize display components while preserving selectors and function logic."""
from __future__ import annotations
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/'localization'
BACKUPS=BASE/'backups/functions'
TEXTS={
    'Attempting to rebuild the technical bits inside the Hexahedron.':'正在尝试重建六面体内部的技术组件。',
    'Please keep your hands and friends inside the vehicle during this procedure.':'在此过程中，请让你的手和同伴都留在载具内部。',
    'Done!, sending you to dimension zero to complete the process.':'完成！正在将你传送至零号维度，以完成此过程。',
    'Generating world, please hold...':'正在生成世界，请稍候……',
    'Non-Player joined the game':'非玩家加入了游戏',
}
FILES={
    'kubejs/data/hexahedron/functions/hexahedron_rebuild.mcfunction':3,
    'kubejs/data/hexahedron/functions/first_init/old/blindfold.mcfunction':1,
    'kubejs/data/hexahedron/functions/processors/travel_actionbar.mcfunction':4,
    'kubejs/data/hexahedron/functions/effects/missing_start.mcfunction':2,
}
COMMAND=re.compile(r'^(tellraw\s+\S+\s+|title\s+\S+\s+actionbar\s+)(.+)$')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def source_bytes(relative):
    path=ROOT/relative
    backup=BACKUPS/relative
    current=path.read_bytes()
    if not backup.exists():
        backup.parent.mkdir(parents=True,exist_ok=True)
        backup.write_bytes(current)
    return path,backup,current,backup.read_bytes()

def localized_component(original):
    chinese=copy.deepcopy(original)
    if isinstance(original,dict):
        english=original.get('text')
        if english not in TEXTS:
            raise ValueError(f'Unreviewed display text: {english!r}')
        chinese['text']=TEXTS[english]+'（'+english+'）'
        return chinese
    if not isinstance(original,list):
        raise ValueError('Unexpected JSON component type')
    found=0
    for node in chinese:
        if isinstance(node,dict) and 'Traveling to dimension: # ' in node.get('text',''):
            node['text']=node['text'].replace('Traveling to dimension: # ','正在前往维度：# ')
            found+=1
    if found != 1:
        raise ValueError('Travel text component count differs from expected')
    # Each language keeps an independent copy of the original dynamic score component.
    result=chinese+[{'text':'（'}]+copy.deepcopy(original)+[{'text':'）'}]
    original_scores=[node for node in original if isinstance(node,dict) and 'score' in node]
    new_scores=[node for node in result if isinstance(node,dict) and 'score' in node]
    assert new_scores==original_scores+original_scores
    return result

def convert_function(raw):
    original_lines=raw.decode('utf8').splitlines(keepends=True)
    new_lines=[]
    changed=[]
    for number,line in enumerate(original_lines,1):
        body=line.rstrip('\r\n')
        ending=line[len(body):]
        match=COMMAND.fullmatch(body)
        if not match:
            new_lines.append(line)
            continue
        prefix,component_json=match.groups()
        original=json.loads(component_json)
        localized=localized_component(original)
        converted=prefix+json.dumps(localized,ensure_ascii=False,separators=(',',':'))+ending
        # Parsing confirms valid JSON; the command prefix retains selectors exactly.
        assert COMMAND.fullmatch(converted.rstrip('\r\n')).group(1)==prefix
        json.loads(COMMAND.fullmatch(converted.rstrip('\r\n')).group(2))
        new_lines.append(converted)
        changed.append({'line':number,'command_prefix':prefix,'original_component':original,
                        'localized_component':localized})
    assert len(original_lines)==len(new_lines)
    for number,(before,after) in enumerate(zip(original_lines,new_lines),1):
        if number not in {entry['line'] for entry in changed}:
            assert before==after
    return ''.join(new_lines).encode('utf8'),changed

NARRATIVE='kubejs/assets/kubejs/textures/exploration_team_1/day_12.txt'
DIALOGUE={
    '/  So what is going on with those eyes?':'/  那些眼睛是怎么回事？',
    '// The pillars you mean?':'// 你是指那些柱子吗？',
    '/  Yes.':'/  是的。',
    "// Well what happens to your memory of a place if you haven't been there a long time?":'// 如果你很久没有去过一个地方，对那里的记忆会有什么变化？',
    '/  It fades?':'/  会逐渐淡忘？',
    '// Exactly.':'// 正是如此。',
    '// Now what if I would tell you that given enough time that idea can be applied to not just memories?':'// 如果我告诉你，只要时间足够久，这个规律也会作用于记忆以外的事物呢？',
    "/  I don't think I follow.":'/  我好像没听明白。',
    '// Its exactly like I said, if something is not observed for a long period of time in these dimensions it will simply stop existing.':'// 就像我说的，在这些维度里，如果某个事物长时间没有被观察，它就会直接消失。',
    '/  Like a fading memory?, that sounds completely insane.':'/  就像逐渐淡忘的记忆？这听起来太疯狂了。',
    '// Yes, like a fading memory and most good revelations do indeed sound insane at first.':'// 是的，就像逐渐淡忘的记忆。大多数重要发现刚提出时，确实都听起来很疯狂。',
    "/  You still haven't answered my question.":'/  你还是没有回答我的问题。',
    "// I'm pretty sure I just did.":'// 我很确定，我刚才已经回答了。',
}

def convert_narrative(raw):
    translated=[]
    turns=[]
    for number,line in enumerate(raw.decode('utf8').splitlines(keepends=True),1):
        body=line.rstrip('\r\n')
        ending=line[len(body):]
        if body.strip():
            if body not in DIALOGUE:
                raise ValueError(f'Unreviewed narrative line {number}: {body!r}')
            translated.append(DIALOGUE[body]+(ending or '\n'))
            turns.append({'line':number,'english':body,'chinese':DIALOGUE[body]})
        translated.append(line)
    result=''.join(translated)
    # Every source line remains intact in its original order, including empty lines.
    source_lines=raw.decode('utf8').splitlines(keepends=True)
    output_lines=result.splitlines(keepends=True)
    index=0
    for line in source_lines:
        if line.strip():
            index+=1
        assert output_lines[index]==line
        index+=1
    return result.encode('utf8'),turns

def write_safe(path,current,original,localized):
    same_text=current.decode('utf8').replace('\r\n','\n').rstrip('\n')==localized.decode('utf8').replace('\r\n','\n').rstrip('\n')
    if current not in (original,localized) and not same_text:
        raise ValueError(f'File changed since backup: {path}')
    path.write_bytes(localized)

def main():
    report={'function_files':[],'narrative_files':[],'changed_display_commands':0,
            'validation':{'selectors_unchanged':True,'non_display_lines_byte_preserved':True,
                          'json_valid':True,'dynamic_score_duplicated_for_both_languages':True,
                          'original_english_preserved':True},
            'untouched_displays':['Numeric countdown components in final_countdown.mcfunction and final_countdown_sec.mcfunction',
                                 'Hidden CustomName missing in missing_start.mcfunction'],
            'texture_review':{'directory':'kubejs/assets/kubejs/textures/exploration_team_1',
                              'images':['memory.png','rune_tablet.png','rune_tablet2.png','rune_tablet3.png','rune_tablet4.png'],
                              'finding':'Five images visually inspected: rune-like pixel symbols; no readable English prose detected.',
                              'edited':False},
            'narrative_classification':'day_12.txt is a two-speaker fictional conversation about observation and memory, rather than developer commentary. No textual reference to its path was found in kubejs, patchouli_books or quest configuration; runtime presentation remains unverified.'}
    for relative,expected in FILES.items():
        path,backup,current,original=source_bytes(relative)
        localized,changes=convert_function(original)
        assert len(changes)==expected,(relative,len(changes))
        write_safe(path,current,original,localized)
        report['function_files'].append({'path':relative,'backup':backup.relative_to(ROOT).as_posix(),
                                         'original_sha256':digest(original),'localized_sha256':digest(localized),
                                         'changes':changes})
        report['changed_display_commands']+=len(changes)
    path,backup,current,original=source_bytes(NARRATIVE)
    localized,turns=convert_narrative(original)
    write_safe(path,current,original,localized)
    report['narrative_files'].append({'path':NARRATIVE,'backup':backup.relative_to(ROOT).as_posix(),
                                    'original_sha256':digest(original),'localized_sha256':digest(localized),
                                    'dialogue_turns':len(turns),'translations':turns})
    (BASE/'functions_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'function_files':len(report['function_files']),'display_commands':report['changed_display_commands'],
                      'narrative_turns':len(turns),'report':'localization/functions_report.json'},ensure_ascii=False))

if __name__=='__main__':
    main()
