# SCI 综述写作 Skill 使用说明

## 这个 Skill 能做什么
- 帮助你从已有文献出发，完成一篇 SCI/中文核心综述。
- 提供从选题、梳理文献、搭框架、写正文，到润色、查重、投稿前准备的全流程提示。
- 统一管理 Zotero 文献库、参考文献格式、图表规划和图片版权备注。
- 支持任意主题，不绑定具体论文、作者或期刊。

## 适用人群
- 已有部分文献，想快速写成综述。
- 需要参考综述范文结构后再开始写作。
- 希望在写作过程中保持目录、图表、参考文献格式一致。

## 快速开始
1. 复制 `review-writing-sci` 目录作为你的工作副本。
2. 在 `SKILL.md` 或你自己的项目说明里替换占位符：
   - `<TOPIC>`
   - `<TARGET_JOURNAL>`
   - `<REFERENCE_STYLE>`
   - `<FIGURE_FOLDER>`
   - `<LITERATURE_FOLDER>`
   - `<OUTPUT_DOC>`
   - `<BENCHMARK_PAPERS>`
   - `<CORE_LITERATURE>`
   - `<DATABASE_LIST>`
3. 按 `references/mapping/25step_mapping.md` 顺序执行。
4. 使用 `references/templates/` 生成标准化内容。
5. 使用 `references/checklists/` 自查质量。

## 两种常用流程
- **已有文献流（推荐）**
  - Step 1：已有文献盘点
  - Step 2：导入 Zotero 并整理
  - Step 3：参考综述格式抽取
  - Step 8：三级文献筛选
  - Step 9：文献批注精读
  - Step 10：文献归类分组
  - Step 12：标准综述框架搭建
  - Step 15：先写核心进展章节
  - Step 16：文献转述改写
  - Step 17：对比评述嵌入
  - Step 22：逻辑闭环自查
  - Step 23：降重与润色
  - Step 24：格式与参考文献终检
- **从选题开始流**
  - Step 4：选题收敛
  - Step 5：综述类型与核心主线确定
  - Step 6：预摘要撰写
  - Step 7：检索策略设计
  - 其余步骤按顺序执行

## Zotero 使用说明
- Step 2 负责导入题录、补全字段、分组、打标签。
- Step 8、10、24 负责在写作过程中持续维护和终检。
- 建议分类：
  - 参考综述
  - 研究论文
  - 方法论文
  - 背景文献
- 每篇文献至少记录：研究问题、方法、关键结论、创新点、局限性、可引用点、是否可做图表来源。

## 图片使用说明
- 优先从已有文献中选取可引用图片，并检查版权。
- 若无法自动提取或生成图片，请使用 `references/templates/figure_placeholder_template.md`。
- 每个图片占位块必须写清：建议图名、建议位置、图表目的、推荐引用来源、版权状态、可执行动作。

## 定制建议
- 若你的学科有固定摘要结构，可在 `references/templates/` 中新增模板。
- 若你有特定期刊格式要求，可在项目根目录新增 `journal_style.md`，写作时作为格式补充。
- 若你需要中英文双语写作，可在模板中增加中英文字段。

## 常见问题
- **Q：我只有几篇 PDF，没有题录文件怎么办？**
  - A：先手动提取标题、作者、年份、DOI，再导入 Zotero 补全字段。
- **Q：图片版权不清楚怎么办？**
  - A：先按占位模板备注来源、页码和版权状态，投稿前统一处理。
- **Q：综述写偏了怎么办？**
  - A：回到预摘要与核心主线，对照 `quality_checklist.md` 和 `consistency_checklist.md`。
