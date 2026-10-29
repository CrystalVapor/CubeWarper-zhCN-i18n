# Start the hexahedron rebuild process
tellraw @p {"text":"正在尝试重建六面体内部的技术组件。（Attempting to rebuild the technical bits inside the Hexahedron.）","bold":true,"color":"gold"}
tellraw @p {"text":"在此过程中，请让你的手和同伴都留在载具内部。（Please keep your hands and friends inside the vehicle during this procedure.）","color":"yellow"}

# Force everyone on board
execute in minecraft:overworld run tp @a 0.5 98 6.5


# Terminate existing outer hexahedron
execute as @e[tag=outer_core] at @s run fill ~-8 ~-8 ~-8 ~8 ~8 ~8 air


# Remove old portals
execute as @e[type=minecraft:marker] unless entity @s[tag=anchor] unless entity @s[tag=hex_anchor] run kill @s
kill @e[type=immersive_portals:portal]


# Portals
execute positioned 0 105.5 0 in overworld run summon marker ~ ~ ~ {Rotation:[0.0f,-90.0f],NoGravity:1b,Tags:["core"]}

execute positioned 0 105.5 0 in overworld run summon marker ~ ~8.51 ~ {Rotation:[0.0f,-90.0f],NoGravity:1b,Tags:["portal","y"]}
execute positioned 0 105.5 0 in overworld run summon marker ~ ~-8.51 ~ {Rotation:[0.0f,90.0f],NoGravity:1b,Tags:["portal","-y"]}

execute positioned 0 105.5 0 in overworld run summon marker ~8.51 ~ ~ {Rotation:[270.0f,0.0f],NoGravity:1b,Tags:["portal","x"]}
execute positioned 0 105.5 0 in overworld run summon marker ~-8.51 ~ ~ {Rotation:[90.0f,0.0f],NoGravity:1b,Tags:["portal","-x"]}

execute positioned 0 105.5 0 in overworld run summon marker ~ ~ ~8.51 {Rotation:[0.0f,0.0f],NoGravity:1b,Tags:["portal","z"]}
execute positioned 0 105.5 0 in overworld run summon marker ~ ~ ~-8.51 {Rotation:[180.0f,0.0f],NoGravity:1b,Tags:["portal","-z"]}


# Vents
execute positioned 0 100.5 0 in overworld run function hexahedron:build_hexahedron/17x17_debug


# Make connection
execute as @e[type=minecraft:marker,tag=portal] at @s run portal cb_make_portal 17 17 @s @s main_cube
execute as @e[type=immersive_portals:portal,name=main_cube] at @s run portal set_portal_destination minecraft:overworld ~ ~ ~
function hexahedron:build_hexahedron/tag_portals
execute as @e[type=immersive_portals:portal,name=main_cube] at @s run portal complete_bi_way_portal


# Schedule proper landing in the hexahedron_graveyard
tag @e[tag=core] add pre_runtime
tellraw @p {"text":"完成！正在将你传送至零号维度，以完成此过程。（Done!, sending you to dimension zero to complete the process.）","color":"green"}