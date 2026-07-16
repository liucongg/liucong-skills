# liucong-skills

刘聪 NLP 的 Skill 仓库。每个 Skill 都放在 `skills/<skill-name>/` 下，可以按需安装和使用。

## 已包含的 Skills

| Skill | 用途 |
| --- | --- |
| [`painterly-3d2-cinema`](skills/painterly-3d2-cinema/) | 把一句话扩展成三渲二动作短片提示词生产包，覆盖剧情方向、角色、场景、Midjourney V8.1 故事板和 Seedance 视频提示词。只生成提示词，不直接生成图片或视频。这个 Skill 在视频平台的 Agent 上使用，效果更佳。 |
| [`gzh-title-strategist`](skills/gzh-title-strategist/) | 分析微信公众号文章，基于文章真实价值、目标读者、事实证据和历史数据生成、改写、批评并排序多风格标题，同时检查标题党、关键词堆砌与时效风险。 |

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

[Apache License 2.0](LICENSE)
