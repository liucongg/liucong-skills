# 历史磨豆机示例：技术回归

该示例用于验证图形导出、Word 构建和分页，不作为合格的结构或视觉基准。题材为通用锥刀手摇磨豆机，外观和尺寸不对应特定型号，不提供官方使用、维修或制造依据。

## 复现

在独立项目目录运行：

```text
python <skill>/scripts/manual-example-manuscript.py <project>
node <skill>/scripts/manual-example-figures.mjs <project>/figures
```

使用 `manual.py raster` 将各 SVG 导出为至少 2200 像素宽的 PNG，再按 validate、build、inspect、render 的顺序运行。逐页检查后记录审阅并运行 qa；命令成功不代表视觉通过。

历史文件含八张 PNG、可编辑正文和图注、七个原生表格，曾由 LibreOffice 渲染为九页。重新构建后需重新检查分页，不继承旧文件的审阅记录。来源日期固定为原来的实际回读日，重跑不代表完成新检索。

## 限制

- 部分视图未完全共用同一结构模型，操作图存在剖面与实际开盖状态的表达差异，详见 `benchmark-review.md`。
- 示例不是品牌外观复刻、出版质量保证或科学认证。
- 没有验证所有 Word 客户端和操作系统的分页一致性。
- 正文、图注和表格可编辑；内嵌图为 PNG，零件不在 Word 内独立编辑。
- 改题材时重新核查来源、部件和机制，不能复用磨豆机的事实依据。
