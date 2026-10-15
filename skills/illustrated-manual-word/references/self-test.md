# 本地技术自测

技术自测验证脚本和文件链路，不替代主题事实核查、逐页阅读或素材权利检查。

## 运行

```text
python <skill>/scripts/manual.py preflight
python <skill>/scripts/test_manual.py
python <skill>/scripts/test_media.py
python <skill>/scripts/test_distribution.py
python <skill>/scripts/smoke.py --project <throwaway-project>
```

`preflight` 报告依赖，不安装软件。回归测试覆盖来源和部件索引、状态声明、路径边界、SVG 安全、图片与媒体记录、Word 原生文字、分页规则、中性元数据及分发检查。`smoke.py` 实际生成图形、Word 和渲染页图，但文件明确标为技术测试。

## 验收边界

测试成功不代表主题原理或视觉通过。正式书稿需重新研究主题，核对图形与状态，并查看最终全部页图。示例的固定来源日期和摘录不能被当作新检索结果。未看图时保留 `reviewed=false`；未测试的系统或宿主明确标注。

Anatomy 的上游许可、来源和下载校验记录位于 `assets/vendor/anatomy/`，不随中性化而删除。
