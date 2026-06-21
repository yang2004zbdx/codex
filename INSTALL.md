# 可直接安装使用

## 1. 安装方式
将 `SKILL.md` 及其同级目录完整复制到你的本地 skill 目录。

常见安装位置：
- Windows: `%USERPROFILE%\.codex\skills\review-writing-sci`
- macOS/Linux: `~/.codex/skills/review-writing-sci`

## 2. 安装后结构
安装后必须保留以下结构：
- `SKILL.md`
- `USER_GUIDE.md`
- `README.md`
- `references/mapping/25step_mapping.md`
- `references/workflow/*.md`
- `references/templates/*.md`
- `references/checklists/*.md`
- `scripts/validate_skill.py`

## 3. 配置占位符
首次使用前，替换以下占位符：
- `<TOPIC>`
- `<TARGET_JOURNAL>`
- `<REFERENCE_STYLE>`
- `<FIGURE_FOLDER>`
- `<LITERATURE_FOLDER>`
- `<OUTPUT_DOC>`
- `<BENCHMARK_PAPERS>`
- `<CORE_LITERATURE>`
- `<DATABASE_LIST>`

## 4. 调用方式
按主题调用：
- “用 skill 帮我写一篇关于 `<TOPIC>` 的综述”

按步骤调用：
- “执行 Step 2：导入 Zotero 并整理”
- “执行 Step 15：先写核心进展章节”
- “执行 Step 14：图表规划”

## 5. 验证安装
运行校验脚本：
```bash
py scripts/validate_skill.py
```

通过输出示例：
```text
校验通过：未发现明显特化内容。
```

## 6. 使用示例
示例输入：
- “我有 10 篇 `<TOPIC>` 相关 PDF，请按 skill 帮我盘点并导入 Zotero。”
- “请按 `<TARGET_JOURNAL>` 格式，帮我生成 Step 21 的摘要、引言和关键词。”
- “这张图无法提取，请按图片占位模板给我一个可插入的占位块。”

## 7. 版本信息
- 当前版本：`1.0.0`
- 适配场景：已有文献驱动型综述
- 适配格式：中文/英文 SCI、中文核心

## 8. 卸载方式
直接删除安装目录即可：
```bash
rm -rf <skill安装目录>
```
