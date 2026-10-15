# 表带操作与活塞泵样章：重建方法

示例包含滑入式表带的更换操作和单作用活塞泵的教学原理。表带图为非官方操作示意，泵图为教材模型；不提供机型、尺寸、压力或维修认证。来源为 Apple 官方指南、Virtual Labs 和 Engineers Edge；保留实际回读日期，重建不代表重新检索。

## 图片

- 六张 SVG 技术图：同一对象的多个视图共用结构与状态。
- 一张生成的水流情境图：仅表达情境，不证明泵的结构。
- 本示例不包含已有产品原图加独立标注层的成品页；混合标注分支需另行测试。
- 官方原图仅用于研究，不随示例分发。第三方资料与生成图片的使用条件分别核对。

## 离线重建

将 `examples/v03/` 复制到独立项目目录；不要改动 Skill 根目录。

```text
python <skill>/scripts/example-v03-figures.py <project>/figures
```

将生成的每个 SVG 用 `manual.py raster` 导出为 2400 像素宽 PNG，再执行：

```text
python <skill>/scripts/example-v03-manuscript.py <project>
python <skill>/scripts/media.py check <project>/media.json
python <skill>/scripts/manual.py validate <project>/book.json
python <skill>/scripts/manual.py build <project>/book.json --out <project>/out/book.docx
python <skill>/scripts/manual.py render <project>/out/book.docx --out-dir <project>/qa
python <skill>/scripts/manual.py inspect <project>/out/book.docx
python <skill>/scripts/distribution_check.py <project>/out/book.docx
```

复用附带 `water-context.png` 和 `generation.json` 不调用生成服务。重新生成需使用宿主工具，可能计费且不保证像素一致。脚本拒绝没有实际图片或生成记录的占位输入。

## 验收范围

新 Word 需重新渲染、逐页检查并填写匹配最终 hash 的记录，不能继承旧文件的 `reviewed=true`。macOS 已验证构建与渲染；其他系统和 Agent 平台需当地测试。离线回归不验证外部 API、素材许可或科学与视觉质量。

正文、表格、图注和来源为原生 Word 内容；内嵌图为 PNG，SVG 另行保留。示意图不能用于制造、维修或带压装置设计。
