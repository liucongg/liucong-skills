# 图解 Word 手册

`illustrated-manual-word` 将主题或技术资料制作成含结构图、原理图和步骤图的可编辑 Word 手册。包含资料核查、SVG 绘图、已有图片或生成图片的选择、Word 构建、实际渲染和验收脚本。

## 目录

- `SKILL.md`：输入、输出、制作步骤、中性内容要求和验收标准。
- `references/`：资料、图形、图片使用、版面和验收规范。
- `scripts/`：构建、栅格化、渲染、媒体检查、分发检查和回归测试。
- `templates/`：书稿和媒体清单结构示例，不是已完成的读物。
- `assets/vendor/anatomy/`：第三方绘图工具及其原始许可证。
- `examples/v03/`：表带操作与活塞泵样章、输入、图片和生成记录；仅分发包附带。

## 环境

Python 3.9 或更新版本；依赖见 `scripts/requirements.txt`。Word 构建需要 python-docx、Pillow；渲染需要 LibreOffice、PyMuPDF；SVG 栅格化需要 rsvg-convert、CairoSVG 或 Chrome。Anatomy 示例另需 Node。

已验证的系统为 macOS；其他系统和 Agent 平台需运行本地测试。未安装渲染器时可以构建 Word，但不能报告排版验收完成。API 或图片工具由宿主提供，本包不包含账号和凭据。

## 使用

读取 `SKILL.md`，运行 `manual.py preflight`，再运行 `test_manual.py`、`test_media.py`。新书稿按核查、绘图、构建、渲染、逐页审阅的顺序执行。

示例重建见 `references/v03-example.md`。复用附带图片不调用生成服务；再次生成需使用宿主工具，可能计费且结果不保证相同。新文件需重新检查，不能沿用旧文件的审阅记录。

## 中性输出

Word 不写入作者、最后修改者、个人介绍、助手署名或内部协作信息。标题、正文、图注和表格为原生 Word 内容，插图为 PNG；SVG 另行保留。分发前运行 `scripts/distribution_check.py`，并人工检查全部页图。自检不等于品牌认证或出版质量保证。

## 许可与范围

方法和自有代码采用 [MIT 许可](LICENSE)。Anatomy 的许可与来源位于 `assets/vendor/anatomy/`，应随依赖保留；不要求将许可文本放入手册正文。本包许可不覆盖品牌素材、出版社页面或生成服务的条款。

样章为非官方教学示意，不提供制造、医疗、带压装置设计或产品维修指导。平台发布前需核对素材的使用权。
