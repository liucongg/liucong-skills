---
name: illustrated-manual-word
description: 制作含结构、原理和步骤插图的可编辑 Word 手册。
license: MIT
metadata:
  version: 0.3.1
  supported_platforms: [macos, linux, windows]
  hermes:
    tags: [word, technical-illustration, svg, image-search, image-generation, manual]
---

# 图解 Word 手册

将主题或技术资料制作成可编辑的 Word 手册，包含结构图、原理图、步骤图、说明文字和可追溯来源。流程包括资料核查、图片选择或绘制、Word 编排、实际渲染和逐页检查。

## 适用范围

- 产品部件与操作说明、机械和科学原理图解、带剖面与状态图的读物、软件机制的概念类比。
- 输入可以是对象、机制、仓库或资料。默认中文、A4 纵向，面向无专业背景的成年人；读者和用途可按任务调整。
- 不用于认证维修手册、制造公差或压力设计、医疗和危险操作指南。纯润色、PDF 转 Word、统计报告不适用本流程。

## 输入与输出

在 `BRIEF.md` 记录对象、型号或版本、读者问题、真实结构或概念类比、适用范围、排除事项、用途与篇幅。仅在缺项会改变事实或安全结论时询问。

输出可下载的 `.docx`；保留 `book.json`、`media.json`、来源、图形源码和生成记录。PDF 与逐页预览用于验收，不替代 Word。标题、正文、步骤、图注、表格和来源为 Word 原生内容；内嵌插图为 PNG，图内零件和短标签不承诺在 Word 中独立编辑。

先完成小样章，再扩展全书。`delivery_kind=sample-chapter` 必须声明 `sample_objectives` 和 `sample_limits`；完整书使用 `production`，最低编辑单元、图数、视图和字数只用于识别空壳，不证明出版质量。`technical-smoke` 只用于技术测试，不作为成品交付。

## 中性内容与平台分发

- 描述只说明用途、输入、输出和操作方法，不加入本 Skill 的作者介绍、个人称呼、团队署名、开发故事、推广语或内部调度说明。
- Word 正文、封面、图注、表格、页眉页脚及图片替代文字只保留主题内容。页眉用书名或中性系列名，页脚用页码；不加入制作人、助手人设、平台推荐和无关制作说明。
- 构建器不写入作者或最后修改者；清空备注、关键词等默认模板元数据。保留中性的主题标题和适用范围，不把旧书稿的作者字段自动带入新文件。
- 用准确、客观的说明替代自我评价和夸张措辞；型号差异、来源、AI 图片披露、必要警告和适用限制不得因中性化而删除。
- 分发前检查文档属性、隐藏文字、批注、修订及外部链接。未解决的审阅记录不能静默删除或视为通过；生成干净副本并保留原稿。
- 包内不含个人绝对路径、账号、凭据、内部沟通记录、缓存或临时日志。第三方依赖的许可证和必要版权声明独立保留，不混入手册正文。本 Skill 的许可不替代外部图片或品牌素材的许可。

## 前提

通过当前宿主的命令工具运行 `python <skill>/scripts/manual.py preflight`。Word 构建需要 python-docx 和 Pillow；排版验收需要 PyMuPDF 和 LibreOffice。SVG 需要 Node 或 Python 绘图，以及 rsvg-convert、CairoSVG、Chrome 中至少一种栅格工具。依赖见 `scripts/requirements.txt`，在项目虚拟环境安装，不修改宿主全局环境。

搜图和生图使用宿主已有工具，不绑定模型、平台或账号。图片搜索不可用时回到来源网页或 PDF；不读取凭据、不打包密钥、不虚构工具执行结果。官方图片也需要核对使用权。

## 命令

`<skill>` 为本 Skill 根目录，`<project>` 为独立书稿目录。路径均可替换；脚本不会自动安装服务、调用另一个 AI 或执行发布。

```text
python <skill>/scripts/manual.py preflight
python <skill>/scripts/media.py plan <project>/figure-brief.json
python <skill>/scripts/media.py fetch https://public.example/image.png --out <project>/research/image.png --allow-host public.example
python <skill>/scripts/media.py check <project>/media.json --out <project>/qa/media-check.json
python <skill>/scripts/media.py contact <project>/media.json --out <project>/qa/contact.png
python <skill>/scripts/manual.py raster <project>/figures/figure.svg --out <project>/figures/figure.png --width 2400
python <skill>/scripts/manual.py validate <project>/book.json
python <skill>/scripts/manual.py build <project>/book.json --out <project>/out/book.docx
python <skill>/scripts/manual.py render <project>/out/book.docx --out-dir <project>/qa
python <skill>/scripts/manual.py inspect <project>/out/book.docx --out <project>/qa/package.json
python <skill>/scripts/distribution_check.py <project>/out/book.docx
python <skill>/scripts/manual.py qa <project>/book.json <project>/out/book.docx --qa-dir <project>/qa
python <skill>/scripts/test_manual.py
python <skill>/scripts/test_media.py
```

下载示例域名是占位符，需替换为已核实的来源。`media.py` 不调用生图 API；下载限公开 HTTPS 白名单和 20 MB。`plan` 仅提供初步方法建议。

## 制作流程

### 1. 核对事实与解释目标

读取 `references/research.md` 和 `references/editorial.md`。每章回答一个读者问题，每图声明 `question/kind/caption/alt_text/source_ids/claim_ids/part_ids`。真实对象不编造内部结构；概念类比明确对应关系和限制。

优先读取官方手册、教材或机构原文，保留摘录、日期和用途；扫描 PDF 需检查页图。核心结论绑定实际读取的来源，至少一项权威来源直接支撑结构或机制。冲突和高风险结论另做交叉核查，可通过 `min_verified_sources` 提高门槛。计算和状态测试使用实际代码输出。

完成条件：任务说明、术语、部件、结论和来源可互相追溯；未读取的资料只列为候选。

### 2. 逐图选择图片方法

读取 `references/image-workflow.md`，参照 `templates/media.example.json`。

- 产品外观和接口：使用有使用权的实拍或官方素材；资料充分时重绘。
- 精确连接、数量、数据或状态：使用 SVG 或确定性绘图。
- 材质、人物、环境和情境：使用已有图或生成图片，披露用途和生成性质。
- 在实物图上解释：保留原图和独立标注层。
- 生成的技术插画：必须逐项核对结构与跨图一致性，不作为独立事实证据。

回到来源页核对原图、型号和许可；缩略图与搜索摘要不是已验证素材。`media.json` 记录方法、用途、权利范围、实际文件和 hash；`schema_version=0.3` 将书稿与媒体清单互锁验证。

完成条件：每图有明确用途、方法依据、文件和权利记录；生成图有真实生成记录。

### 3. 绘制一致的结构与状态

读取 `references/figures.md`、`references/benchmark-review.md` 及 Anatomy 的 `craft.md`、`walkthrough.md`、`verify.md` 和最接近的完整示例。几何工具及许可位于 `assets/vendor/anatomy/`。

总览、剖面、爆炸和步骤图共享结构、坐标、部件与状态。检查真实接合、支撑、遮挡、连接和运动方向；不能只保持编号而改变实体。整体需辨认对象，4× 局部检查穿透、断线、悬空和错误遮挡。箭头和件号有明确语义，不用剖面代替开盖动作。

SVG 自包含，禁止脚本、事件、远程资源和 `foreignObject`。动画转换成表达因果的状态序列，图片中的长段文字不能替代原生正文。

完成条件：结构与状态测试实际运行；最终图与参照在同尺寸下比较，关键局部经过检查并记录修正。

### 4. 编排原生 Word

读取 `references/word-layout.md`。先确定图文单元和阅读顺序，再安排页型；图注与图同页，警告紧邻相关操作。默认流式排版，完整图版可固定分页。固定分页需真实渲染，不能靠额外空段落产生空页。

按内容调整字号、行距、功能色和图宽，避免夸张标题、无效留白和为凑页数而重复图。检查最终尺寸下的细线与标签，不只检查图片分辨率。

完成条件：原生正文可回读；实际 DOCX 页图无孤段、空白页、挤字、截断和图注错页；中性内容检查通过。

### 5. 分别验收

读取 `references/acceptance.md`，记录四项结果：事实与安全、图形与状态、版面与阅读、技术与可迁移性。

机器检查只证明声明和文件匹配，不证明科学或视觉正确。实际看过最终页图后才能填写 `reviewed=true`。修改 DOCX 后旧 hash 和旧审阅结果失效；缺工具、未测试环境和未解决问题分别报告。

完成条件：最终每页和关键局部已审阅，来源与状态可核查，结构、媒体和中性内容检查通过，记录匹配最终文件。

### 6. 交付与分发

交付所需 Word 及必要预览，简短说明主题、实际页数、图片格式和限制。公开发布前另核素材权利与发布权限。打包排除秘密、个人路径、参考专用版权原页、临时日志和内部交流记录，保留必要许可证。

复制或解压到新目录后重新运行脚本；重建产物需重新渲染和审阅，不能继承旧文件的通过声明。

## 示例与限制

`references/v03-example.md` 说明表带操作与活塞泵两个样章的重建方法。示例采用 SVG 技术图和已有生成情境图，不需要再次付费生图。历史磨豆机脚本只供技术回归，不作为合格视觉基准。

已验证的宿主环境为 macOS；其他操作系统和 Agent 平台需本地测试。Word 内嵌图为 PNG；教学重绘不构成品牌授权、尺寸认证、制造图或维修指导。

## 常见问题

- 搜索摘要、模型回答和 `verified=true` 不能替代来源回读。
- 图精致不代表结构正确；生成图不能补充未知事实。
- 页数、图数和回归通过不代表成品质量。
- 没有真实渲染器时只能报告文件构建完成，不能报告排版验收完成。
- 去除本 Skill 的署名不等于可以删除第三方许可证、来源或必要的权利披露。

## 验收记录

保留 `qa/render.json`、`review.json`、`media-check.json`、`package.json`、中性内容检查结果、来源、结构测试和修正记录。以实际最终文件为准；未验证的能力和环境明确标注。
