# SVG Visual Fallback

当模型不能生成位图、图片工具不可用、外部素材不可用、图片生成被拒绝，或用户明确要求纯 SVG 时，启动本策略。

## 定位

SVG fallback 不是占位图。它是受控的视觉资产替代模式，用 SVG 原生能力补足页面的视觉表现力，同时避免伪造真实图片。

## 触发条件

- 图片生成工具不可用或调用失败
- 图片生成结果不满足任务目标
- 外部图片搜索、下载或授权不可用
- 内容策略导致图片无法生成
- 用户要求 `纯 SVG`、`仅 SVG`、`不要图片`
- 当前交付环境只允许 HTML/CSS/SVG

## 决策规则

| 原需求 | SVG fallback 处理 |
|--------|-------------------|
| 真实人物、真实地点、真实商品 | 不伪造真实照片，只能改为品牌化抽象视觉、信息卡或装饰层 |
| 空状态、引导页、封面 | 可生成 SVG 插画、场景、图形隐喻 |
| 数据看板、AI、科技、金融 | 优先使用数据图形、网格、发光描边、仪表环、波形 |
| 活动页、品牌页、潮流视觉 | 可使用路径切割、噪点、渐变、遮罩和大图形构成 |
| 图标和功能符号 | 放入 `icons/`，保持单色或 `currentColor` 可适配 |
| 装饰插画、背景、场景 | 放入 `visuals/`，允许多色、渐变、滤镜和纹理 |

## 输出目录

```
design-output/
├── icons/      # 功能图标，必须轻量、可复用、可适配颜色
└── visuals/    # SVG 视觉资产：插画、背景、空状态、封面、装饰场景
```

`icons/` 和 `visuals/` 不能混用。导航、按钮、状态符号属于 `icons/`；hero、空状态、背景装饰、数据插画属于 `visuals/`。

## 高美感构成

SVG fallback 至少使用以下能力中的 3 类，避免退化为普通几何占位：

- 渐变：`linearGradient`、`radialGradient`、透明度高光、渐变描边
- 滤镜：`feDropShadow`、`feGaussianBlur`、`feTurbulence`、`feColorMatrix`
- 遮罩：`clipPath`、`mask`、渐变透明层
- 路径：贝塞尔曲线、波形、数据线、分段环、异形容器
- 复用：`defs`、`symbol`、`use`、可命名图层
- 质感：内阴影、高光描边、噪点肌理、局部辉光

详细构成技巧和质量标准见 [svg_generation_prompts.md](svg_generation_prompts.md)。

## 风格映射

| 风格 | SVG 方案 | 详细 Prompt |
|------|----------|-------------|
| glass | 半透明 surface、模糊背板、高光描边、柔和阴影 | [svg_generation_prompts.md §3.1](svg_generation_prompts.md#31-glass-风格) |
| editorial | 大字号排版块、非对称路径、图形裁切、低饱和强调色 | [svg_generation_prompts.md §3.2](svg_generation_prompts.md#32-editorial-风格) |
| data | 环形进度、网格、曲线、柱状、状态点、微光轨迹 | [svg_generation_prompts.md §3.3](svg_generation_prompts.md#33-data-风格) |
| geometric | 大形状组合、硬边遮罩、强对比色块、结构化留白 | [svg_generation_prompts.md §3.4](svg_generation_prompts.md#34-geometric-风格) |
| neumorphic | 内阴影、柔和凸起、浅底低对比、细高光 | [svg_generation_prompts.md §3.5](svg_generation_prompts.md#35-neumorphic-风格) |
| neon | 深底、发光描边、多层透明线、局部高饱和强调 | [svg_generation_prompts.md §3.6](svg_generation_prompts.md#36-neon-风格) |

每种风格的详细矢量技法要求、质量标准和负面约束见 [svg_generation_prompts.md](svg_generation_prompts.md)。

## 禁止项

- 禁止用 SVG 假装真实照片、真实人物或真实商品图
- 禁止只放灰色矩形、默认插画或无语义装饰当作完成
- 禁止大面积高斯模糊覆盖整屏
- 禁止复杂滤镜叠加到所有节点
- 禁止文字全部转曲，常规 UI 文本必须保持 `<text>` 或 HTML 文本
- 禁止把装饰 SVG 放进 `icons/` 凑数量

## SVG 质量要求

- 每个独立 SVG 必须包含 `viewBox`
- 面向用户可见的 SVG 应包含 `<title>` 或 `<desc>`
- 复杂 SVG 必须有分层命名：背景、主体、装饰、状态、高光
- 滤镜范围要收窄，避免默认 `filterUnits` 导致大范围重绘
- 可复用图形放入 `<defs>`，避免重复 path 堆叠
- 颜色必须来自 `tokens.json` 或 `DESIGN-GUIDE.md` 中定义的 palette
- 动画必须轻量，避免大面积 blur、noise 或 path morph 常驻运行

### 量化质量指标

| 维度 | Icon 最低 | Icon 推荐 | Visual 最低 | Visual 推荐 |
|------|----------|----------|------------|------------|
| 矢量元素类型 | ≥2 种 | ≥3 种 | ≥3 种 | ≥5 种 |
| 色彩层次 | — | — | ≥4 色阶 | ≥6 色阶 |
| 分层 `<g>` 组 | — | — | ≥3 层 | ≥5 层 |
| 渐变使用 | 禁止 | 禁止 | ≥1 个 | ≥2 个 |
| 滤镜使用 | 禁止 | 禁止 | 0-2 个 | 1-3 个 |
| `<defs>` 复用 | — | — | ≥1 个 | ≥2 个 |
| 文件大小 | ≤5KB | ≤3KB | ≤50KB | ≤30KB |
| viewBox | 必须 | 24x24 | 必须 | 匹配设计尺寸 |
| title 标签 | 必须 | 有描述 | 必须 | title+desc |

详细的自动检查命令见 [svg_generation_prompts.md §4.3](svg_generation_prompts.md#43-质量指标自动检查)。

## DESIGN-GUIDE 标注

进入 SVG fallback 后，`DESIGN-GUIDE.md` 必须新增一节。完整模板见 [svg_generation_prompts.md §7](svg_generation_prompts.md#7-design-guide-标注模板)。

## 视觉审查附加门禁

视觉审查师必须额外检查：

- 是否明确说明 fallback 触发原因
- 是否没有伪造真实图片
- 是否与当前品牌、tokens、组件系统一致
- 是否达到高美感构成要求（≥3 类）
- 是否控制滤镜、动画和路径复杂度
- 是否正确区分 `icons/` 与 `visuals/`
- 是否按 [svg_generation_prompts.md](svg_generation_prompts.md) 填入了完整 Prompt 并写入 DESIGN-GUIDE.md
- 是否通过量化质量指标（文件大小、矢量元素、色彩层次等）
