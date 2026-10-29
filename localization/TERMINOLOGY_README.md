# 术语提取与补译资料

运行 `python localization/extract_terminology.py` 可从当前安装文件重新建立词典。脚本只写入 `localization/`。

- `extracted/` 原样保存模组与自动汉化资源包中的中文语言文件，包含简体、繁体和香港繁体。文件的 SHA-256、原始存档路径与条目路径见 `language_inventory.json`。
- `all_pairs.json` 和 `all_pairs.tsv` 按 namespace 与相同翻译 key 对齐中英文，保留不同语言地区、不同存档和译文冲突。
- `effective_zh_cn.json` 提供后续翻译可引用的简体中文映射；`missing_zh_cn.json` 保留英文文本与原始来源；`missing_summary.json` 记录各 namespace 缺失规模。
- `conflicts.json` 保留不同译文和英文覆盖候选；`namespace_english_sources.json` 列出实际提供英文的存档；`statistics.json` 记录总体规模。

参考选择次序为模组 JAR 文件名排序、已安装自动汉化资源包、KubeJS 本地语言文件。KubeJS 英文覆盖仍使用相同 key 配对，但自定义英文含义发生变化时，必须人工判断中文能否继续复用。此排序用于术语参考，实际游戏资源优先级由加载器与已启用资源包决定。

扫描范围为 `mods/*.jar` 及其中递归嵌套 JAR 的 `assets/<namespace>/lang/` 的 `en_us`、`zh_cn`、`zh_tw` 和 `zh_hk` JSON 与旧式 `.lang` 文件；另扫描已安装的 `Minecraft-Mod-Language-Modpack-Converted-1.20.1.zip` 简体中文及 `kubejs/assets/*/lang/`。部分模组存档含其他模组 namespace 的英文资源，来源记录予以保留。嵌套 JAR 的完整路径链保存在 `nested_archives` 字段。

语言 JSON 采用 UTF-8 读取，支持字符串外的末尾逗号。Pretty Rain 的繁体中文包含此类逗号；提取存档保持原始字节。Botania 的格式符原始表示为 `\u00a7`，Thermal 的格式符为 UTF-8 `C2 A7`；输出 JSON 中均正确保持 `§`。PowerShell/Python 控制台编码不一致时可能显示乱码，可通过指定 UTF-8 的文件读取检验。

`translate_terms.py` 为 Untagged 与 Forestry 提供逐条人工译文及经过检查的物品名称词组组合。组合仅应用于已选中的完整物品、方块、实体和生物群系名称，不应用于任务段落或逻辑文件。`translate_terms_extra.py` 提供分配给本代理的额外 namespace 补译。两者分别输出 `manual_mod_translations_terms*.json` 和 `manual_mod_exclusions_terms*.json`。作者署名、纯数字、专有标识、音符与单位具有明确排除记录。译文输出采用 namespace → key → 中文结构，中英拼接由主构建脚本统一处理。
