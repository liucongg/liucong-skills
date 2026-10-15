# liucong-skills

刘聪 NLP 的 Skill 仓库。每个 Skill 都放在 `skills/<skill-name>/` 下，可以按需安装和使用。

## 已包含的 Skills

| Skill | 用途 |
| --- | --- |
| [`design-led-website-builder`](skills/design-led-website-builder/) | 从简短需求出发，先锁定网站用途，再研究同类真实网站、收集可用视觉素材，最后完成有明确设计方向的网站或改版。适合新建网站和视觉重构，不用于普通 Bug 修复或文案微调。 |
| [`illustrated-manual-word`](skills/illustrated-manual-word/) | 将技术资料制作成含结构图、原理图和步骤图的可编辑 Word 手册，包含来源核查、图片与 SVG 制作、排版渲染和逐页验收。 |
| [`liucong-model-eval`](skills/liucong-model-eval/) | 初始化并运行可追溯的多模型同题对照测评，支持内置演示题、自有题库和权威视觉 benchmark 子集；隔离被测进程，保留首轮回答、工具轨迹、产物与验收记录。 |
| [`painterly-3d2-cinema`](skills/painterly-3d2-cinema/) | 把一句话扩展成三渲二动作短片提示词生产包，覆盖剧情方向、角色、场景、Midjourney V8.1 故事板和 Seedance 视频提示词。只生成提示词，不直接生成图片或视频。这个 Skill 在视频平台的 Agent 上使用，效果更佳。 |
| [`gzh-title-strategist`](skills/gzh-title-strategist/) | 分析微信公众号文章，基于文章真实价值、目标读者、事实证据和历史数据生成、改写、批评并排序多风格标题，同时检查标题党、关键词堆砌与时效风险。 |
| [`llm-wiki-ops`](skills/llm-wiki-ops/) | 在飞书知识库中初始化、绑定和运维 LLM Wiki，支持资料与文章入库、来源标注、词条双链、索引维护、知识查询和健康度体检。 |

## 安装 `painterly-3d2-cinema`

先确认所使用的 Agent 或视频平台的 Skills 目录，并将它设置为 `SKILLS_HOME`。推荐使用软链接，仓库里的更新会立即生效。

```bash
git clone https://github.com/liucongg/liucong-skills.git
cd liucong-skills
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
ln -s "$(pwd)/skills/painterly-3d2-cinema" "$SKILLS_HOME/painterly-3d2-cinema"
```

如果目标路径已经存在，先确认它是否是旧链接或旧副本，再自行移除或备份；不要直接覆盖仍在使用的 Skill。

也可以复制安装：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
cp -R skills/painterly-3d2-cinema "$SKILLS_HOME/"
```

复制安装后，仓库更新不会自动同步，需要重新复制。安装完成后，重新加载平台的 Skills 列表或重启对应 Agent，使 Skill 被重新发现。

## 使用 `painterly-3d2-cinema`

在 Agent 对话中显式调用 Skill：

```text
$painterly-3d2-cinema 做一条 15 秒的三渲二动作短片，白发男光剑士在雨夜湖岸迎战机械敌人。
```

也可以直接描述需求；当任务涉及三渲二角色、场景、动作故事板或短片提示词时，支持自动识别 Skill 的 Agent 可以自动触发它。

默认工作流为：

1. 提供 3 个剧情方向并等待选择。
2. 锁定剧情与每 15 秒一个 Segment 的节奏。
3. 依次制作角色、角色人物信息画板、场景和对手提示词。
4. 为每个 Segment 制作一张 Midjourney V8.1 的 15 格动作故事板提示词。
5. 根据故事板输出对应的 Seedance 视频提示词。

该 Skill 只交付提示词。图片需要在 Midjourney 外部生成，视频需要在 Seedance 外部生成，再把结果上传给 Agent 检查和继续迭代。

## 安装 `gzh-title-strategist`

推荐使用软链接安装，仓库里的修改会立即同步到 Agent 的 Skills 目录：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
ln -s "$(pwd)/skills/gzh-title-strategist" "$SKILLS_HOME/gzh-title-strategist"
```

也可以复制安装：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
cp -R skills/gzh-title-strategist "$SKILLS_HOME/"
```

## 使用 `gzh-title-strategist`

将完整文章、草稿或已有标题交给 Agent，并显式调用 Skill：

```text
$gzh-title-strategist 根据这篇文章生成一组公众号标题，并选出最值得发布的 3 个。
```

也可以让它复盘已有标题：

```text
$gzh-title-strategist 结合这些文章的阅读和互动数据，分析哪些标题写法有效，哪些可能只是选题或发布时间带来的影响。
```

该 Skill 会先诊断文章类型、目标读者、核心结论、事实证据和可交付内容，再生成稳健准确型、网感点击型、专业权威型、数据关键词型和长期型标题。默认会对前 5 名进行评分，并给出 1 个主标题、2 个备选标题及风险提示。

涉及热词或历史数据时，它只使用 Skill 内置的历史样本或用户提供的证据，不会把关键词相关性描述为微信推荐算法规则，也不会为了点击率添加正文没有依据的公司、产品、数字或夸张结论。

## 安装 `design-led-website-builder`

推荐使用软链接安装，便于持续获取仓库更新：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
ln -s "$(pwd)/skills/design-led-website-builder" "$SKILLS_HOME/design-led-website-builder"
```

也可以复制安装：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
cp -R skills/design-led-website-builder "$SKILLS_HOME/"
```

这个 Skill 需要 Agent 具备网页检索、浏览器查看与前端代码编辑能力。素材研究阶段还需要图片搜索或图片生成能力。Skill 自带的目录检索和校验脚本使用 Python 3.11 及 PyYAML；如需运行这些脚本，可在 Skill 目录中安装锁定依赖：

```bash
cd skills/design-led-website-builder
uv sync
```

## 使用 `design-led-website-builder`

给出网站服务的对象、建站目的和必须展示的内容即可：

```text
$design-led-website-builder 我是一名独立 AI 研究者，希望做一个个人网站，用来展示研究方向、代表项目、文章和联系方式。整体克制、编辑感强。
```

也可以同时提供现有品牌、参考网站 URL、截图或明确的视觉风格。若需求可能对应多种网站产品，Skill 会先用一轮问题锁定意图并等待回答；意图明确时会直接开始。

默认工作流为：

1. 识别现有品牌、内容和参考资料，判断网站的核心任务。
2. 必要时只进行一轮意图确认。
3. 研究 3–5 个同类真实网站，并收集可授权使用或可生成的纹理、艺术作品、编辑图片等视觉素材。
4. 汇报设计方向、参考来源、已收集素材和明确不会照搬的部分。
5. 在同一轮继续完成网站实现，并按内置质量标准检查视觉、响应式、可访问性与基本工程质量。

该 Skill 不会虚构客户、奖项、业绩、人物照片或职业经历，也不会复制参考网站的标志性布局、文案和资产。用户自己的品牌与参考资料优先于内置目录；缺少个人作品或照片时，会保留清晰标注的高保真占位，而不会伪造证明材料。

## 安装和使用 `llm-wiki-ops`

这个 Skill 需要飞书登录态以及 `lark-cli`，或宿主 Agent 提供的等价飞书知识库和云文档工具。推荐复制安装，让每个 Agent 独立维护自己的绑定状态：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
cp -R skills/llm-wiki-ops "$SKILLS_HOME/"
```

在 Codex 中，可安装到个人 Skills 目录：

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/llm-wiki-ops "$HOME/.agents/skills/"
```

首次调用时，Skill 会检查 `config/wiki-binding.json`。如果没有有效绑定，它会引导用户绑定已有知识库或创建新的 LLM Wiki：

```text
$llm-wiki-ops 帮我初始化或绑定一个 LLM Wiki。
```

绑定后可以直接入库、查询和体检：

```text
$llm-wiki-ops 把这份资料入库，提取值得沉淀的词条并补全双链。
```

真实的 `config/wiki-binding.json` 是本地运行时状态，已通过 Skill 自带的 `.gitignore` 排除。仓库只提供脱敏的配置示例，任何知识空间 ID、节点 token 和文档 ID 都不应提交。完整说明见 [`skills/llm-wiki-ops/README.md`](skills/llm-wiki-ops/README.md)。

## 安装和使用 `liucong-model-eval`

推荐使用软链接安装，便于持续获取仓库更新：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
ln -s "$(pwd)/skills/liucong-model-eval" "$SKILLS_HOME/liucong-model-eval"
```

这个 Skill 的模型执行器目前只支持 macOS，需要 Node.js 22 或以上、Claude Code，以及用户自己的火山 Agent Plan 套餐、专属 Key 和可用模型 ID。其他系统仍可编辑和导入题库，但执行器会拒绝在未经验证的隔离环境中运行。只有从 Hugging Face 导入远程 benchmark 子集时才需要 uv 与 Python 3.11。

首次使用，在 Skill 目录初始化并检查本机环境：

```bash
cd skills/liucong-model-eval
node scripts/setup.mjs init --model=glm-5.3-flash
node scripts/setup.mjs doctor
node scripts/runner.mjs isolation-check
```

然后由用户本人在一个终端运行 `node scripts/connect.mjs`，按隐藏输入提示粘贴 Agent Plan Key，并保持进程运行。Key 默认只保存在该连接进程内存中，不应发到聊天、写进命令参数、题库或报告。

在另一个终端先完成当前连接和所需能力检查，再运行正式测评：

```bash
node scripts/runner.mjs run --cases=connection --model=glm-5.3-flash
node scripts/runner.mjs run --cases=visioncheck --model=glm-5.3-flash
node scripts/runner.mjs run --cases=toolscheck --model=glm-5.3-flash
node scripts/runner.mjs run --dry-run --tier=simple --count=3
node scripts/runner.mjs run --tier=simple --count=3
node scripts/runner.mjs status
node scripts/runner.mjs export
```

视觉检查只在测图片题时需要，工具检查只在测代码题时需要。执行器默认把配置、运行记录和导出包放在 `~/.local/share/liucong-model-eval/`，而不是 Skill 目录；私有题库、图片和导出结果公开前需自行筛选。内置题仅用于演示和回归，少量导入题应称为“某 benchmark 子集”，不能冒充完整官方榜单成绩。

显式调用示例：

```text
$liucong-model-eval 用我的题库对照测试两个模型，先做 dry run，把题号、模型和预算列给我确认。
```

## 安装和使用 `illustrated-manual-word`

将 Skill 链接到 Agent 的 Skills 目录，或复制 `skills/illustrated-manual-word/` 整个目录。示例、模板、绘图库及其许可证都在此目录内：

```bash
export SKILLS_HOME="/path/to/your-agent/skills"
mkdir -p "$SKILLS_HOME"
ln -s "$(pwd)/skills/illustrated-manual-word" "$SKILLS_HOME/illustrated-manual-word"
```

脚本需要 Python 3.9 或更新版本。Word 构建依赖 `python-docx` 和 Pillow；要完成渲染验收，还需要 PyMuPDF 和 LibreOffice。SVG 栅格化需安装 rsvg-convert、CairoSVG 或 Chrome。建议在独立虚拟环境安装 Python 依赖，并先检查本机工具：

```bash
cd skills/illustrated-manual-word
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/manual.py preflight
```

在 Agent 中提供对象、型号或版本、读者和用途；缺省按中文、A4 纵向、非专业读者制作。可以直接调用：

```text
$illustrated-manual-word 根据这份产品资料制作一份图解 Word 手册，先做小样章，说明结构、工作原理和操作步骤。
```

Skill 会先核查资料与图片使用权，再制作图文、生成可编辑 `.docx`、实际渲染并逐页检查。`examples/v03/` 提供表带操作与活塞泵样章及离线重建材料；示例的最终科学与逐页验收记录尚未完成，不能直接当作已认证手册。当前只在 macOS 验证过工具链，Linux、Windows 及其他 Agent 宿主需本地测试。详细命令与限制见 [Skill 说明](skills/illustrated-manual-word/README.md)。

## 更新

软链接安装时，只需更新仓库：

```bash
cd liucong-skills
git pull
```

复制安装时，更新仓库后需要重新复制对应 Skill。

## 添加新的 Skill 到仓库

每个 Skill 使用独立目录：

```text
skills/
└── my-skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    ├── scripts/
    └── assets/
```

其中只有 `SKILL.md` 是必需文件；其他目录按需添加。Skill 目录名应与 `SKILL.md` frontmatter 中的 `name` 一致，并使用小写字母、数字和连字符。

添加后，确认 `SKILL.md` 包含合法的 YAML frontmatter，至少具有 `name` 和 `description`；目录名应与 `name` 完全一致。如果所用平台提供 Skill 校验工具，再按平台说明执行结构校验。

最后在本 README 的“已包含的 Skills”表格中补充入口和用途说明。

## License

仓库默认采用 [Apache License 2.0](LICENSE)。`illustrated-manual-word` 的自有代码和方法按其目录内的 [MIT License](skills/illustrated-manual-word/LICENSE) 发布；随附 Anatomy 绘图库保留自己的 [MIT 许可证和来源记录](skills/illustrated-manual-word/assets/vendor/anatomy/)。第三方图片及品牌素材不因本仓库许可证而获得再授权。
