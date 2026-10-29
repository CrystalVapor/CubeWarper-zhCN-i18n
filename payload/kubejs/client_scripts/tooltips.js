ItemEvents.tooltip(event => {

  event.addAdvanced('kubejs:vector_operator_basic', (item, advanced, text) => {
    text.add(1, Text.gray("加 1（Adds 1）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_charged', (item, advanced, text) => {
    text.add(1, Text.gray("乘以 3（Multiplies by 3）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_fluix', (item, advanced, text) => {
    text.add(1, Text.gray("加 2（Adds 2）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_nuclear', (item, advanced, text) => {
    text.add(1, Text.gray("乘以 4（Multiplies by 4）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_blaze', (item, advanced, text) => {
    text.add(1, Text.gray("乘以 6（Multiplies by 6）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_lightning', (item, advanced, text) => {
    text.add(1, Text.gray("乘以 8（Multiplies by 8）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_eye', (item, advanced, text) => {
    text.add(1, Text.red("除以 0（Divides by 0）").bold(true))  
  })

  event.addAdvanced('kubejs:vector_operator_infinite', (item, advanced, text) => {
    text.add(1, Text.red("将所有目的地坍缩为同一个目的地（Collapses all destinations into one）").bold(true))  
  })

  event.addAdvanced('alexscaves:frostmint', (item, advanced, text) => {
    text.add(1, Text.blue("在冷冻机中使用时不会被消耗（Will not be consumed when used in the Chiller）"))  
  })

//Final Vectors
  event.addAdvanced('kubejs:vector_operator_infinite_empty', (item, advanced, text) => {text.add(1, Text.gray("步骤 1 → 右键点击远古红石（Step 1 -> Right-Click on Ancient Redstone）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step2', (item, advanced, text) => {text.add(1, Text.gray("步骤 2 → 在维度 8 的祭坛上进行陈化 （Step 2 -> Age With the Shrine in Dimension 8 ）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step3', (item, advanced, text) => {text.add(1, Text.gray("步骤 3 → 使用注液器注入荧光液（Step 3 -> Spout with Lumisene）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step4', (item, advanced, text) => {text.add(1, Text.gray("步骤 4 → 在精魂祭坛中与符文进行精魂灌注（Step 4 -> Spirit Craft with Runes in a Spirit Altar）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step5', (item, advanced, text) => {text.add(1, Text.gray("步骤 5 → 与烈焰燃料结合（Step 5 -> Combine with Blaze Fuel）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step6', (item, advanced, text) => {text.add(1, Text.gray("步骤 6 → 在闪电祭坛充能（Step 6 -> Charge at the Lightning Shrine）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step7', (item, advanced, text) => {text.add(1, Text.gray("步骤 7 → 在电弧炉中与金属结合（Step 7 -> Combine with metals in the Arc Furnace）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step8', (item, advanced, text) => {text.add(1, Text.gray("步骤 8 → 投入悲泣之井（Step 8 -> Drop into the Weeping Well）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step9', (item, advanced, text) => {text.add(1, Text.gray("步骤 9 → 在仪式法阵中与 8 个模块化反应堆结合（Step 9 -> Combine with 8 Modular Reactors in the Ritual Cricle）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step10', (item, advanced, text) => {text.add(1, Text.gray("步骤 10 → 在仪式法阵中与 8 个遗弃者木偶结合（Step 10 -> Combine with 8 Forsaken Idols in the Ritual Cricle）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step11', (item, advanced, text) => {text.add(1, Text.gray("步骤 11 → 在仪式法阵中与 8 台超级计算机结合（Step 11 -> Combine with 8 Super Computers in the Ritual Cricle）").bold(true))  })
  event.addAdvanced('kubejs:vector_operator_step12', (item, advanced, text) => {text.add(1, Text.gray("步骤 12 → 在 10 分钟内将其放回矢量调谐器（Step 12 -> Place this back on the Vector Tuner within 10 minutes）").bold(true))  })


  //(1) +1 → total 3  → +3 → [1, 2, 3]
  //(2) *3 → total 6  → +3 → [4, 6, 9]
  //(3) +2 → total 11 → +5 → [5, 7, 8, 12, 18]
  //(4) *4 → total 15 → +4 → [10, 16, 24, 32]
  //(5) *6 → total 20 → +5 → [13, 14, 36, 48, 72]
  //(6) *8 → total 24 → +4 → [17, 64, 96, 128]
  //(7) /0 → total 26 → +1 → [undifined]

  //(8) *5 → total 33 → +7 → [20, 25, 30, 40, 50, 60, 80]
  //(9) *7 → total 43 → +10 → [21, 28, 35, 42, 49, 56, 70, 84, 98, 112]

})