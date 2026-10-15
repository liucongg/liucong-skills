# Word 编排与验收

## 文档不是一张长图
正文、标题、目录、图注、表格、页码与来源必须是真实Word段落/字段/表格。只把图本体嵌成图片；不能把整页PNG当Word页。所有图都有alt_text。字段结果由Word/LibreOffice渲染计算，写入字段不代表目录已更新。

## v0.3 的嵌图决定
通用脚本采用 PNG 兼容层：SVG图保留SVG源，已有/生成/混合图保留其真实源文件与记录，不伪造SVG套壳；DOCX内嵌PNG。这样可以稳定进入python-docx与LibreOffice，不声称Word图可以任意无损放大。后续若实现OOXML原生SVG须独立验证Windows/Mac/LibreOffice兼容与PNG fallback，不能偷偷改交付语义。

默认A4，左右约18–20mm，深灰文字，实际可用中文字体。正文11pt、图注9pt左右；跨平台不能只测试英文字母。页眉简短书名，页脚真页码。正文主要用单栏；双栏只在实际阅读受益时使用。尽量内嵌图，避免浮动图层遮文字。

页眉只使用中性书名或系列名，页脚只保留页码。作者、最后修改者、备注和关键词默认留空，不写入个人介绍、团队署名、内部协作过程和无关制作说明。正文、表格、图注及图片替代文字使用客观措辞；保留主题来源、必要的生成图片披露和安全限制。最终文件运行 `scripts/distribution_check.py`，批注、修订和隐藏文字另行检查，不将未处理的审阅信息带入公开副本。

## book.json 核心结构
- title/subtitle/reader/mode/scope：整本定位。
- sources：真实回读来源，ID稳定。
- claims：事实或演示假设，绑定sources。
- parts：全书术语/件号。
- figures：method/role/asset_id、PNG相对路径（SVG图另有svg）、caption、kind、question、alt_text、part/claim/source IDs。schema_version=0.3关联media_manifest并检查文件/hash/方法/角色。
- pages：编辑规划的内容页，title/kicker/lead/blocks。每块为paragraph、figure、table、callout或steps。文字可写引用标记如[S01]，但sources必须真实。

路径相对于book.json所在项目目录；不得逃出该目录读取个人文件。图源和导出图都保留。与样书无关的私密档案不得被读进文档。

## 真实渲染
脚本用独立临时LibreOffice profile和headless转换，避免干扰用户已有Office窗口。转换有超时和明确退出结果。PDF生成后用PyMuPDF逐页渲染PNG和contact sheet，不把Chrome画的同风格HTML当作DOCX渲染证据。

每次改稿后重新渲染，QA对应最终文件的SHA256。review.json记录此hash、实际页数、逐页reviewed、issues与修正。不得写“所有页已看”但实际上只看了一张contact sheet：总览能筛异常，复杂/密集页必须看全页/局部。

## 机器检查与人工检查
机器：引用ID、critical claim状态、素材存在、安全SVG、body文字/图片、包关系、最终文件hash、PDF/页图、review.json所有页有明确结果。结构脚本通过不是科学正确性证明。

视觉：缺字/字体回退、图是否被裁、图注是否同页、孤行/空页、标签和细线是否可读、图的比例、章节节奏。图版还检查部件一致、剖切/接触/流向、状态对比是否回答问题。

未修的问题不得仅写“PASS”，要在交付中声明风险。真实维修、制造、医疗等用途不能用这份科普验收替代专业审查。
