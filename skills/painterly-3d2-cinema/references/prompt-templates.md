# Prompt Templates

通用规则：所有图片资产默认使用 Midjourney V8.1，只输出提示词，不询问模型、不调用生成工具；中文-only；MJ V8.1 提示词 <1000 字符；角色 <700 字符；模型和画幅写在提示词外；不要尾随参数。每次图片提示词后都请用户在 Midjourney 外部生成并上传成图或回复“已生成”；收到成图后检查结果并主动引导下一阶段。

## 角色：稳定全身概念图

用于魔幻少年、信使、法师、民族服饰朋克化角色。

```text
白底全身人物概念设定图，[地域/世界观][身份]，[年龄]，[叙事功能]。粗粝厚涂美漫角色设计，3D体块基础结合2D手绘笔触，强块面光影，低饱和电影色彩，[服饰]朋克化剪影。比例夸张，高瘦但有少年感，长腿，小头，窄肩，手脚偏大。脸型瘦长，颧骨轻微突出，五官不用清楚，[发型]，眼神[情绪]。[外层大色块]；[内层大色块]；[下装]，[鞋]。配件少而明确：[橘色视觉钩子]、[身份物]、[工具]。[动作]。白色背景，脚下粗糙手绘阴影。不要写实摄影、Q版、道具堆叠、可读文字、logo
```

示例：

```text
白底全身人物概念设定图，藏区高原火铃少年，16岁，雪原驿路上的年轻信使。粗粝厚涂美漫角色设计，3D体块基础结合2D手绘笔触，强块面光影，低饱和电影色彩，民族服饰朋克化剪影。比例夸张，高瘦但有少年感，长腿，小头，窄肩，手脚偏大。脸型瘦长，颧骨轻微突出，五官不用清楚，黑色短乱发，眼神倔强、警惕。深靛蓝厚外袍到小腿，一侧肩膀滑落；旧米白羊毛内衫，深灰宽裤，旧棕高筒靴。配件少而明确：亮橘色编绳护身符、旧铜铃项链、小皮信筒。一手握短木杖，另一手拽着橘色风带。白色背景，脚下粗糙手绘阴影。不要写实摄影、Q版、道具堆叠、可读文字、logo
```

## 角色人物信息画板

触发：角色设计确认后，询问用户是否需要更详细的角色人物信息画板；用户确认后直接输出 Midjourney V8.1 提示词，不再询问模型，也不生成图片。也可在用户主动说“固定人物信息、角色信息版、角色身份画板、identity board、用参考图锁人物、先做人物信息板”时使用。用途是让后续图像/视频保持同一张脸、发型、服装、身形、姿态语言和情绪范围。它不是三视图、不是目录式设定页、不是普通 character reference sheet。

优化原则：角色板优先服务“后续生成一致性”，不是炫技拼贴。必须清楚锁定：正脸、侧脸、发型剪影、全身比例、服装大色块、手部、鞋、核心道具、表情范围、动作姿态语言。不要塞太多小图导致身份漂移。

询问话术：

```text
角色设计已经定下来了。要不要制作一张更详细的 16:9 角色人物信息画板？它会锁定这个角色的脸、发型、服装、身形、姿态和表情范围，方便后面做场景、分镜和视频参考。

若用户回答需要，直接交付 Midjourney V8.1 提示词，并补充：`请在 Midjourney 中生成后上传成图或回复“已生成”，我会检查一致性并继续场景设计。`
```

```text
模型：Midjourney V8.1
用途：角色人物信息画板 / CHARACTER IDENTITY BOARD FOR GENERATION LOCK
提示词：
Create a 16:9 CHARACTER IDENTITY BOARD for [角色名/角色身份]. Use the provided character reference as the identity source. This board is for future image and video generation consistency, not a decorative poster.

BACKGROUND: pure white or soft off-white studio background. No environment, no logo, no watermark, no UI.

VISUAL MEDIUM: stylized anime-painterly, painterly 3D-to-2D animation, cel-shaded large color blocks, rough dry-brush edges, matte surfaces, low-saturation cinematic color with one controlled accent color: [橘色/暗红/金色/项目强调色].

LAYOUT: premium animation artbook layout, asymmetrical but clean. Keep large breathing space. Do not use a rigid grid, blueprint sheet, catalog page, fashion collage, or overlapping figures.

MAIN ANCHOR: place one large clean full-body hero pose slightly off-center. It must clearly show head size, body proportion, silhouette, clothing layers, hands, shoes, and main prop.

SUPPORT STUDIES: arrange separated smaller studies around the anchor:
1 neutral front full-body, 2 side profile full-body, 3 back view, 4 close-up face front, 5 close-up face profile, 6 hair silhouette, 7 hand/weapon/prop detail, 8 shoes/lower-body detail, 9 two subtle expression portraits, 10 one action attitude pose.

IDENTITY LOCK: every study must preserve the same face, same facial proportions, same hair silhouette, same outfit, same body proportions, same posture language, same mood, same prop scale. No age shift, no beautification, no different hairstyle, no costume redesign, no alternate versions.

READABILITY RULE: keep bodies and portraits separated. No cropped face, no hidden limbs, no stacked bodies, no merged poses, no tiny unreadable details. Prioritize clear silhouette and clean large shape design.

MINIMAL TEXT BLOCK: add one small elegant CHARACTER ID block only: NAME / ROLE / CORE MOOD / VISUAL SIGNATURE. Keep labels minimal and not dominant.

NEGATIVE: no environment scene, no extra characters, no long text, no readable paragraphs, no logos, no watermark, no realistic photography, no plastic toy CGI, no over-detailed noisy AI texture.
```

## 角色：三视图

仅用户明确要三视图时使用。

```text
白底三视图人物设定图，正面、侧面、背面，同一[角色]、同一服装；严肃动画式夸张比例，头部略小，四肢修长，[剪影特征]，[极简五官/面具化几何头部]，[2-3层服装大色块]，[一个道具]；3渲2厚涂赛璐璐运动动画，大色块设计，整块整块的平涂色面，硬朗图形化明暗切面，粗粝干刷笔触，避免碎乱AI噪点，不是写实摄影，不是光滑CGI，不要塑料玩具感、Q版、文字、Logo
```

## 角色：怪物/动物头职业人

用于 FILTH CLUB、动物头职业、脏旧朋克。

```text
白底或浅灰底单人全身角色展示，[职业身份]，[动物/怪物]头部面具化、雕塑化、几何化，不是真实动物头，眼睛极简，[身形比例和姿态]；[外层职业服大色块]、[内层大色块]、[手套/靴子]形成三四个大色块，最多三件道具：[道具1]、[道具2]、[道具3]，衣物有大块污渍/胶带/破纸片，脚下粗糙投影；3渲2厚涂赛璐璐运动动画，大色块设计，硬朗图形化明暗切面，粗粝干刷笔触，不要写实动物头、真实毛发、浮空道具、可读文字、Logo、光滑CG
```

## 场景

```text
[时代地域]的[场景类型]，[季节/时间/天气/情绪]。前景[遮挡物]形成纵深；中景是主要行动区：[建筑/道路/火堆/角色位置/关键道具]；背景延伸至[远山/森林/城镇/帐篷/天空]，雾气/烟尘/风雪降低对比。建筑与自然物用大块形状概括，材质哑光磨损。16:9电影构图，[低机位/平视/远景]，视觉中心明确，背景不抢主体。粗粝厚涂三渲二动画，强块面光影，边缘粗糙，低饱和电影色彩，[暖橘/暗红]只作局部情绪色。不要真实品牌、可读文字、字幕、Logo、UI
```

现代城市现实场景：

```text
粗粝厚涂三渲二场景概念图，普通[城市][车站/楼道/小餐馆/街角]，生活化小空间，[长椅/冷灰地面/行李/车灯]，[人物动作或情绪瞬间]。前景[物体/地面边缘]，中景[主要行动]，背景[灯光/雾气]，磨损表面，柔和空气透视，低饱和电影色彩，强块面光影，边缘粗糙。不要真实品牌、其他可读文字、Logo
```

## 角色在场景关键帧

```text
电影感动画关键帧，[角色锚点]置身[场景锚点]，面对[对手/障碍]，[镜头]，决定性瞬间：[动作]，前景[遮挡物]，轮廓清晰，天气运动，衣服和头发有手绘拖影，[强调色]只出现在[元素]；粗粝厚涂三渲二动画，强块面光影，边缘粗糙，低饱和电影色彩，不要Logo、可读文字、字幕、UI
```

## 手绘动作故事版

触发：人物、场景和剧情都确认后，用户需要“手绘分镜、故事版、动作预演、稳定镜头、功夫动作拆解、fight previs”。直接输出 Midjourney V8.1 提示词，不询问模型、不生成图片。用途是用黑白粗铅笔 15 格 storyboard 锁定动作节奏、身体势能、镜头角度、镜头切换、环境反应和 VFX 标注。不是最终彩色分镜。提示词交付后请用户在 Midjourney 外部生成并上传成图，收到后检查连续性并主动进入下一阶段。

时长规则：先根据剧情阶段的 Segment 表执行。一张 15 格 storyboard 只代表一个 15 秒以内 Segment。7-15s 用 1 张；16-30s 用 2 张；31-45s 用 3 张，以此类推。多张时，每张都单独生成一张 16:9 15 格图，命名为 Storyboard Ref 01 / 02 / 03。后一张第 1 格必须从前一张最后一格的最终动作、角色位置、镜头方向和能量状态开始，形成连续动作链，不能重新开场。禁止把 30 秒或 45 秒内容塞进一张 storyboard。

```text
模型：Midjourney V8.1
用途：手绘动作故事版 / 15格 high-density fight choreography storyboard
提示词：
Create a 16:9 cinematic action storyboard sheet for [Segment XX / time range] only. Use @[Char ref] for C1: [角色锚点]. Use @[Opponent/Obstacle ref] for C2 if available. Use @[Scene ref] for the environment. This single storyboard sheet represents ONLY this one video segment. Do not include action from other segments.

[PROJECT CARD]
TITLE: [短标题]
META LINE: [场景类型] / [动作类型] / [核心视觉冲突] / [结尾动作]
PRIORITY: make the action visually strong and cinematic. Emphasize [启动动作/压迫感/角色情绪], face close-ups, hand/prop close-ups, footwork, enemy or obstacle pressure, environmental reaction, fast readable camera cuts, attack/defense exchange, close-range entry, and final impact.
MICRO BRIEF: [一句话说明本段动作：主角如何启动、遭遇压力、推进、反击、完成结尾动作]

[STORYBOARD PURITY]
15 cinematic panels, compact 5x3 storyboard sheet. Panel artwork must be black and white rough pencil only: fast gesture lines, strong silhouettes, clear body motion, minimal detail. No color inside panels, no subtitles, logos, UI, readable long text, duplicate bodies, ghost poses, or diagrams inside panels.

[CHARACTER LOCK]
C1: [角色身份、体型、发型、服装、核心道具、姿态语言、情绪]
C2 / OBSTACLE: [敌人/障碍/环境压力的轮廓、位置、攻击方式]

[SCENE PACKET]
LOCATION: [前景/中景/背景/固定地标/可战斗空间]
START -> END: [起点动作/状态] -> [终点动作/状态]
MUST READ: [观众必须看懂的动作与情绪]

[PANEL HEADERS]
P01 / macro hand or prop / [启动前细节]
P02 / face close-up / [角色眼神或能量启动]
P03 / low wide / [空间关系揭示]
P04 / enemy or obstacle macro / [威胁启动]
P05 / low environment insert / [攻击划过水/尘/地面/墙面]
P06 / medium clash / [第一次接触或防御]
P07 / footwork close-up / [滑步/跳步/急停/踩水/踏尘]
P08 / side tracking / [闪避或侧向推进]
P09 / wide environment reaction / [大动作影响场景]
P10 / overhead tactical / [被包围/路径选择/攻防位置]
P11 / POV or threat view / [从敌人/障碍视角看主角逼近]
P12 / handheld close / [爆发突进，衣料/头发/呼吸]
P13 / orbiting shot / [绕到侧翼/进入破绽/反转]
P14 / macro impact / [核心命中/武器接触/能量爆裂]
P15 / low hero aftermath / [倒塌/余波/主角定格]

[CAMERA VARIETY REQUIREMENTS]
Use strong cinematic shot variation. Do not keep the same camera distance or angle for more than two panels in a row. Include hand close-up, face close-up, low wide shot, enemy/obstacle POV, footwork close-up, environmental reaction shot, overhead tactical shot, side tracking shot, orbiting shot, macro impact insert, and low hero finish. Each camera change must support action clarity, emotion, impact, spatial geography, enemy pressure, or environmental reaction.

[ENVIRONMENT REACTION]
Show [水面/尘土/雾气/树木/墙面/玻璃/火花/碎片/衣料/头发/倒影] reacting to every major action. The environment must visibly change during the fight instead of staying as a static background.

[DIRECTOR STRIP]
CAMERA PATH: P01 [macro] -> P02 [face close-up] -> P03 [low wide] -> P04 [enemy macro] -> P05 [environment insert] -> P06 [clash] -> P07 [footwork] -> P08 [side track] -> P09 [wide reaction] -> P10 [overhead] -> P11 [POV] -> P12 [handheld burst] -> P13 [orbit] -> P14 [macro impact] -> P15 [low finish].
ACTION PATH: P01 [启动准备] -> P02 [能量/情绪启动] -> P03 [站位清楚] -> P04 [威胁启动] -> P05 [攻击到来] -> P06 [首次接触] -> P07 [位移] -> P08 [闪避/推进] -> P09 [大动作改变环境] -> P10 [压力峰值] -> P11 [主角逼近] -> P12 [爆发] -> P13 [反转入位] -> P14 [命中] -> P15 [余波].
RHYTHM TRACK: held breath -> ignition hit -> reveal -> build -> burst -> impact -> whip -> dodge beat -> flow -> pressure peak -> threat POV -> burst -> orbit beat -> final hit -> held finish.
ESCALATION MAP: L1 calm -> L3 rise -> L4 threat -> L5 spike -> L5 pressure -> L5 clash -> L4 evasive flow -> L5 danger -> L5 counterflow -> L5 peak -> L5 pursuit -> L5 surge -> L5 entry -> L5 release -> L3 aftermath.
STATE TRACK: [道具/能量off] -> [on] -> [空间清楚] -> [威胁蓄力] -> [攻击激活] -> [火花/冲击] -> [环境扰动] -> [闪避线] -> [场景被照亮/撕开] -> [包围/压力] -> [距离缩短] -> [速度爆发] -> [破绽显露] -> [核心命中] -> [倒塌/静默].

[ACTION REQUIREMENTS]
Every panel must show readable physical momentum. Avoid static standing poses after P03. C1 must use at least five action types: [启动/防御/闪避/突进/反转/命中]. Attack direction must stay readable. Main VFX must clearly originate from the correct source. Cloth, hair, water/dust/sparks/smoke/reflections must react to motion. No timestamps, dialogue, singing, extra characters unless required, logos, or watermark.
```

## Seedance 故事版视频提示词

触发：角色、剧情、场景、Midjourney V8.1 手绘动作故事版都确认后，默认输出 Seedance 视频提示词。必须把手绘动作故事版当作连续镜头顺序，不照搬示例具体角色，不发明替代镜头；每次根据当前项目重写情绪、声音和 beats。

硬规则：最后只输出 Seedance 提示词，不询问视频模型，不调用视频生成工具，不提交生成，不替用户点击生成；由用户手动把 Seedance prompt 和参考图放入视频工具，并在生成后上传结果以便检查。视频必须按 15 秒 Segment 生成：每张 storyboard = 一个 15 秒以内 Seedance 片段。若有多张 storyboard，必须拆成多条 Seedance 提示词：Segment 01 只引用 `@[Storyboard Ref 01]`，Segment 02 只引用 `@[Storyboard Ref 02]`。先分别生成，再剪接。不要默认输出“一条30秒Seedance提示词”。若用户坚持单条长视频，必须先提示失控风险并让用户确认。

优化原则：Seedance 提示词不要写成“风格作文”。必须写成执行单：输入引用、身份优先级、空间连续、镜头路线、动作路线、节奏、状态变化、逐 panel beats、禁止项。默认故事版为 15 格并输出 P01-P15；只有用户明确要求轻量版时才可改成 12 格。

```text
模型：Seedance
用途：根据手绘动作故事版生成单个 15 秒以内视频片段
提示词：
[INPUT PACKAGE]
Use @[Storyboard Ref XX] as the only storyboard for this video segment. This prompt is only for [Segment XX / time range]. Do not use storyboard refs from other segments in this generation.
Use @[Char ref] as C1 identity reference. If available, use @[Opponent ref] as C2 reference and @[Scene ref] as environment reference.

[REFERENCE PRIORITY]
1. Character reference controls C1 face, body proportions, hair, wardrobe, silhouette, attitude, and main prop.
2. Opponent reference controls C2 shape, scale, silhouette, weapon/limb design, and material.
3. Scene reference controls location geography, light direction, atmosphere, and stable landmarks.
4. Storyboard reference controls staging, motion, panel order, camera angle, rhythm, continuity, and effect logic.
Do not redesign, age-shift, beautify, duplicate, merge, or replace any referenced subject.

[SEGMENT RULE]
Generate one continuous cinematic video segment under 15 seconds. Treat each storyboard panel as one consecutive shot or beat. Follow panel order exactly from P01 to P[实际格数]. Do not skip panels, reorder panels, add alternate coverage, or invent a new intro. Recreate the filmed sequence implied by the storyboard, not the sketch style itself.
If this is Segment 02 or later, the first shot begins from the previous segment's final state: same screen direction, same spatial relationship, same body momentum, same emotional pressure, same VFX state.

[SCENE PACKET]
PREMISE: [一句话说明本段发生什么]
LOCATION: [地点、前景、中景、背景、固定地标]
START -> END: [本段起点动作/状态] -> [本段终点动作/状态]
ACTION CHAIN: [动作1] -> [动作2] -> [动作3] -> [动作4] -> [结尾动作]
PROP / EFFECT STATE: [关键道具、能量、火、水、烟、碎片、球、武器等如何从起点变化到终点]
MUST READ: [观众必须看懂的一句话]

[CONTINUITY LOCK]
Keep C1 identity, outfit, body proportion, prop, and movement direction consistent across all shots. Keep C2 / obstacle position consistent. Keep environment geography stable: [例如：球门在远处、街灯在画面右侧、水面在前景、森林在背景]. Only camera distance, angle, pose, cloth motion, VFX intensity, debris, smoke, reflection, and impact state may change.

[STYLE CONTINUITY]
[项目三渲二风格锚点]。Keep painterly 3D-to-2D cinematic animation look, cel-shaded large shape lighting, matte surfaces, controlled accent color, readable silhouettes. Do not turn into live-action, glossy CGI, plastic toy render, game cutscene, anime cute style, or noisy over-detailed AI texture.

[EMOTIONAL ARC]
Valence: [情绪从A到B到C].
Arousal: [启动 -> 升压 -> 高压动作 -> 反转/停顿 -> 释放].
Show emotion through eye-line, footwork, body weight, breathing, cloth snap, prop height, opponent drive, impact, recovery, and final stillness.

[AUDIO]
No background music unless user asks. Use only diegetic ambience, foley, impacts, texture, and silence: [环境声]；[脚步/呼吸/衣料]；[道具声]；[撞击声]；[元素/VFX声]；[结尾余波].

[SHOT VARIATION PLAN]
The video must feel like edited action cinema, not one continuous medium shot. Use frequent but readable shot changes:
P01 macro hand/prop close-up
P02 face close-up with key light or energy across eyes/hair
P03 low wide geography reveal
P04 enemy/obstacle macro
P05 low environment insert showing incoming force
P06 medium clash impact
P07 footwork close-up
P08 side tracking dodge or advance
P09 wide environment reaction
P10 overhead tactical shot
P11 enemy/obstacle POV or threat view
P12 handheld close-up burst
P13 orbiting flank/reversal
P14 macro impact/core/contact
P15 low hero aftermath

[ENVIRONMENT REACTION]
During combat, show [water/dust/mist/trees/walls/glass/craft/ground/reflections] reacting to movement: ripples, torn mist, flashing surfaces, sparks landing, debris, smoke, cloth and hair motion. The environment must change visibly across the sequence.

[DIRECTOR STRIP]
CAMERA PATH: P01 [镜头/焦段/运动] -> P02 [...] -> P03 [...] -> ... -> P[实际格数] [...]
ACTION PATH: P01 [动作] -> P02 [动作] -> P03 [动作] -> ... -> P[实际格数] [动作]
RHYTHM TRACK: P01 [hold/slow reveal/build/burst/impact/pause/recover/final hit] / [short/medium/long block] / [clean/match/smash/held/whip beat] -> ...
ESCALATION MAP: P01 [L1 calm/L2 tension/L3 rise/L4 surge/L5 peak] / [flat/rise/spike/drop/release] -> ...
STATE TRACK: P01 [角色/道具/VFX状态] -> P02 [...] -> ... -> P[实际格数] [...]

[BEATS]
P01: [镜头大小 + 机位 + 动作 + 角色位置 + VFX/声音]
P02: [镜头大小 + 机位 + 动作 + 角色位置 + VFX/声音]
P03: [...]
P04: [...]
P05: [...]
P06: [...]
P07: [...]
P08: [...]
P09: [...]
P10: [...]
P11: [...]
P12: [...]
P13: [若15格，写反转/入位/侧翼/压迫变化]
P14: [若15格，写宏观命中/核心接触/爆裂]
P15: [若15格，写低机位结尾/余波/环境反应]

[CAMERA RULES]
Use action-film cutting rhythm. Change shot size and angle often while preserving screen direction. Mix macro inserts, face close-ups, low wide shots, side tracking, overhead tactical view, enemy/obstacle POV, handheld burst, orbiting reversal, and low hero finish. Do not hold one generic medium shot. Every cut must reveal emotion, footwork, impact, spatial geography, enemy pressure, or environmental reaction. One primary camera movement per beat.

[VFX / MATERIAL RULES]
VFX must follow the storyboard progression: early subtle, middle stronger, final strongest. Effects must be physical and cinematic, not superhero-like unless the project explicitly asks. Make cloth, hair, dust, water, sparks, smoke, debris, light shafts, reflections, and surfaces react to motion.

[LIMITS]
The storyboard is the source of truth. No alternative coverage, no scene rewrite, no panel skipping, no reordered action, no new intro, no extra characters unless already in storyboard, no changed costume, no changed face, no changed prop, no dialogue unless requested, no singing, no subtitles, no logos, no watermark, no UI.
```

## 一键完整方案格式

```text
【三渲二方向】...
【剧情设计】Logline / 主题 / 冲突 / 结尾画面
【固定锚点】角色 / 场景 / 对手 / 色彩 / 镜头
【角色 Prompt】模型：Midjourney V8.1 提示词：...
【场景 Prompt】模型：Midjourney V8.1 提示词：...
【手绘动作故事版】模型：Midjourney V8.1 提示词：...
【Seedance 视频 Prompt】...
【负面限制】...
```
