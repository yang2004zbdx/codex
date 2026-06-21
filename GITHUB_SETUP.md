# GitHub 发布说明

## 1. 建议仓库信息
- 仓库名称：`review-writing-sci`
- 仓库描述：通用 SCI/中文核心综述写作 Skill，覆盖选题、Zotero、文献筛选、框架搭建、正文撰写、图表、润色与 Cover Letter
- 可见性：Public
- 初始化：不要自动生成 README、LICENSE、.gitignore（使用本仓库自带版本）

## 2. 建议仓库 Topics
- review-writing
- scientific-writing
- zotero
- literature-review
- skill-template
- academic-writing

## 3. 本地初始化命令
在 `D:\Desktop\阶跃星辰\综述文献-催化层结构设计\_review-writing-sci` 目录执行：

```bash
git init
git add .
git commit -m "chore: init review-writing-sci template"
git branch -M main
git remote add origin https://github.com/yang2004zbdx/review-writing-sci.git
git push -u origin main
```

## 4. GitHub 发布 Checklist
- [ ] 仓库描述已填写
- [ ] Topics 已设置
- [ ] README.md 已显示正常
- [ ] LICENSE 已确认
- [ ] Releases 已创建 v1.0.0
- [ ] Issues / Discussions 已开启（可选）

## 5. 建议发布说明（Release Notes）
### v1.0.0
- 支持已有文献驱动型综述写作
- 提供 25 步标准化流程
- 内置 Zotero 导入与终检流程
- 内置图片 fallback 占位模板
- 支持任意主题复用

## 6. 常见问题
- 若遇到中文文件名乱码，可启用 Git 对 UTF-8 的支持。
- 若需要分发，可直接把仓库设为模板仓库。
