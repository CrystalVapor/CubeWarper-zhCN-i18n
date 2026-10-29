# Cube Warper 简体中文双语汉化

适用于 Minecraft 1.20.1 / Forge 的 Cube Warper 整合包。中文译文后保留英文原文；长篇手册使用相邻的中英文页面。

## 覆盖范围

- FTB Quests：8 个章节、576 个显示字段。
- 模组补译：3,910 个语言键；KubeJS 自定义内容另含 153 个名称键和提示、函数消息。
- 自定义仪式指南、模组手册补充和叙事对话。

术语整理扫描了 170 个顶级模组 JAR 及 153 个嵌套 JAR，建立 80,565 条带来源的英中配对。译文按 namespace 和翻译键处理，保留占位符、格式标记及原始英文。数据统计对应 2026-10-12 的补丁快照。

## 安装

下载发布的补丁 ZIP，或使用本仓库的完整内容。退出游戏后，在 Windows PowerShell 中运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1 -GameDirectory "你的 Cube Warper 实例目录"
```

安装器先备份文件，再合并语言与资源包设置。自动汉化资源包排在本地双语补丁之前；较新的本地自动汉化资源包会保留。恢复命令和详细步骤见 [安装说明](docs/INSTALL.md)。

## 构建分享补丁

Python 3.10 或更高版本，无第三方依赖：

```powershell
python tools/build_release.py
```

生成文件位于 `dist/`。构建过程检查全部 payload 文件的 SHA-256，并验证生成 ZIP 的内容和 CRC。

## 维护译文

`payload/` 保存已验证的可安装资源；`localization/` 保存人工译文映射、提取脚本及原始任务文本。大型术语表和原始提取数据可从安装完整整合包的实例重新生成，未纳入 Git 历史。

如需重新提取和生成资源，将本仓库的 `localization/` 目录复制到整合包实例根目录，保留实例原有的 `mods/`、`kubejs/` 与资源包，然后在该实例运行：

```powershell
python localization/extract_terminology.py
python localization/build_mod_patch.py
python localization/build_kubejs.py
python localization/verify_patch.py
```

修改验证完成后，将对应文件同步回仓库 `payload/`，并更新 `manifest.json` 中的文件摘要。完整术语数据格式见 [术语说明](localization/TERMINOLOGY_README.md)。

## 验证与已知范围

JSON、JavaScript 语法、任务功能字段、格式参数和安装恢复测试已通过。实际游戏中的分页、排版及资源重载尚待验证。探洞台英文小游戏词库涉及符文字体与匹配逻辑，保持原文；示例手册与 Java 代码直接写入的文本详见 [手册检查报告](reports/book_scope.json)。

仓库包含汉化补丁、安装工具及维护资料。文件来源和第三方资源说明见 [NOTICE](NOTICE.md)。
