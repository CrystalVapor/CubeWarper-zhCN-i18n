# Cube Warper 简体中文双语汉化

适用于 Minecraft 1.20.1 / Forge 的 Cube Warper 整合包。中文译文后保留英文原文；长篇手册使用相邻的中英文页面。

## 覆盖范围

- FTB Quests：8 个章节、576 个显示字段。
- 模组补译：3,910 个语言键；KubeJS 自定义内容另含 153 个名称键和提示、函数消息。
- 自定义仪式指南、模组手册补充和叙事对话。

术语整理扫描了 170 个顶级模组 JAR 及 153 个嵌套 JAR，建立 80,565 条带来源的英中配对。译文按 namespace 和翻译键处理，保留占位符、格式标记及原始英文。数据统计对应 2026-10-12 的补丁快照。

## 安装

### 解压覆盖安装

[下载解压覆盖补丁 ZIP（约 5.1 MB）](https://github.com/CrystalVapor/CubeWarper-zhCN-i18n/raw/refs/heads/main/downloads/CubeWarper-zh_CN-Bilingual-Overlay-2026-10-12.zip) · [SHA-256](downloads/CubeWarper-zh_CN-Bilingual-Overlay-2026-10-12.zip.sha256)

1. 退出游戏，备份实例的 `config/ftbquests`、`kubejs` 和 `patchouli_books`。
2. 将 ZIP 全部内容直接解压到整合包根目录，覆盖同名文件；`config`、`kubejs`、`resourcepacks` 等目录应与 `mods` 处于同一层。
3. 启动游戏并选择简体中文。在资源包菜单中启用两个汉化资源包，将 `CubeWarper-Chinese-Bilingual` 放在已选列表最上方，`Minecraft-Mod-Language-Modpack-Converted-1.20.1.zip` 紧随其下。

此安装方式无需运行脚本。压缩包内直接包含游戏相对路径，资源包启用与排序通过游戏菜单完成。若已有较新的自动汉化 ZIP，解压时可保留本地同名文件。详细步骤和恢复方式见 [解压覆盖安装说明](docs/OVERLAY-INSTALL.md)。

### 脚本安装

使用脚本安装包或本仓库的完整内容。退出游戏后，在 Windows PowerShell 中运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-Patch.ps1 -GameDirectory "你的 Cube Warper 实例目录"
```

安装器先备份文件，再合并语言与资源包设置。自动汉化资源包排在本地双语补丁之前；较新的本地自动汉化资源包会保留。恢复命令和详细步骤见 [安装说明](docs/INSTALL.md)。

## 构建分享补丁

Python 3.10 或更高版本，无第三方依赖：

```powershell
python tools/build_release.py
```

生成脚本安装包和解压覆盖包，均保存在 `dist/`。构建过程检查全部 payload 文件的 SHA-256，验证 ZIP 内容、CRC，并实际解压覆盖包逐文件核对。

更新仓库中的直接下载文件：

```powershell
python tools/build_release.py --publish-overlay
```

此命令将已验证的覆盖包及校验文件复制到 `downloads/`。GitHub Actions 也会构建两种安装包，可在对应工作流运行页面下载构建产物。

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
