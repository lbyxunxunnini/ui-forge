# SVG 生成 Prompt 模板

## 定位

当 SVG Visual Fallback 触发时，交付工程师必须将当前设计设定填入以下模板，并把完整 Prompt 写入 `DESIGN-GUIDE.md` 的 `SVG Visual Fallback` 章节。不得只写"画一个空状态插画"。

本文件包含 3 类 Prompt 模板（Icon / Visual / 风格细化）和质量标准，供交付工程师和视觉审查师使用。

---

## 一、SVG Icon 生成 Prompt 模板

用于 `design-output/icons/` 目录的功能图标。优先复用已有图标体系，以下为新建图标的可调整示例；资产表达和无障碍处理应符合实际用途及项目约定。

```text
Generate a clean SVG icon named {icon_name}.svg.
Canvas: viewBox="{适合项目图标体系的画布}". Output exactly one SVG file.

Subject:
- Icon purpose: {功能描述，如"手机号输入框前缀图标"}
- Semantic meaning: {语义，如"phone / mobile / lock"}
- Style: {遵循已有图标体系，或选择适合用途的风格}
- Stroke width: {按图标体系选择，若适用}
- Color: {按图标体系选择；可适配的单色图标优先 currentColor}

SVG implementation requirements:
- Match the existing icon set in shape, line weight, sizing and color treatment
- Use the simplest suitable geometry and rendering techniques for this icon
- Provide accessible naming or hide decorative icons according to actual use
- Keep the asset appropriate for the target environment

Quality bar:
- Recognizable at its intended rendered size
- Optically aligned and consistent with the icon set
- Keep file size and complexity appropriate for the purpose
```

### Icon Prompt 填写示例

```text
Generate a clean SVG icon named search.svg.
Canvas: viewBox="0 0 24 24". Output exactly one SVG file.

Subject:
- Icon purpose: 搜索功能入口图标，用于导航栏右侧操作区
- Semantic meaning: search / magnifying glass
- Style: line
- Stroke width: 2px
- Color: currentColor

SVG implementation requirements:
- Use <path> as primary shape for the magnifying glass lens and handle
- Use stroke-linecap="round" stroke-linejoin="round"
- Add <title>Search</title> for accessibility
- All styling self-contained

Quality bar:
- Pixel-perfect at 24px render size
- Optical center aligned
- Recognizable silhouette at 16px

Negative constraints:
- No gradients, filters, blur, or shadow
- No text inside icon
- No clipPath or mask
```

---

## 二、SVG Visual Asset 生成 Prompt 模板

用于 `design-output/visuals/` 目录的插画、背景、空状态、hero 装饰、数据可视化。目标：高质感、有层次、与品牌一致。

```text
Generate a high-quality SVG visual asset named {asset_name}.svg.
Canvas: viewBox="0 0 {width} {height}". Output exactly one SVG file.

Subject:
- Purpose: {illustration|background|empty_state|hero_visual|data_decoration}
- Scene description: {场景描述，如"空状态：一只猫坐在月亮上，周围有星星"}
- Mood: {情绪关键词，如"温暖/科技感/轻松/专业"}
- Color palette: {主色/辅色/点缀色，含 HEX，必须来自 tokens.json}
- Style: {目标项目的已有或自定义风格；可参考 glass/editorial/data/geometric/neumorphic/neon}

SVG implementation requirements:
- Choose shapes, grouping, gradients, masks, filters and reuse only as appropriate to the design intent
- Keep filters and animation proportionate to performance needs
- Provide an accessible name for meaningful assets or hide decorative assets from assistive technology, according to context

Quality bar:
- Composition and visual detail fit the purpose, content and chosen style; flat and minimal assets are valid
- Clear focal point when the asset needs one
- Consistent with page tokens and brand palette
- Appropriate file size and rendering performance for the delivery environment

Negative constraints:
- No dense repeated <rect> grid
- No placeholder gray boxes or empty containers
- No full-screen gaussian blur covering the entire canvas
- No text converted to paths (keep <text> for UI text)
- No clipPath covering entire canvas as mask
- No raster images or base64 data
- No broken anatomy or duplicated elements
```

### Visual Prompt 填写示例

```text
Generate a high-quality SVG visual asset named empty-state.svg.
Canvas: viewBox="0 0 375 400". Output exactly one SVG file.

Subject:
- Purpose: empty_state
- Scene description: 空邮件收件箱——一封漂浮的信封，周围有散落的小星星和云朵
- Mood: 轻松、友好、不焦虑
- Color palette: primary #667eea, secondary #764ba2, accent #f093fb, neutral #f5f5f7
- Style: geometric

SVG implementation requirements:
- Use layered <g> groups: background, envelope_body, envelope_flap, stars, clouds, accents
- Use <path> for envelope shape and star outlines
- Use <linearGradient> for envelope body color transition
- Use <clipPath> for envelope flap reveal
- Add <title>Empty inbox</title> and <desc>No messages yet - friendly empty state illustration</desc>

Selected techniques for this example:
- Gradients: linearGradient on envelope body
- Paths: bezier curves for envelope shape, star paths
- Reuse: defs + use for repeated star shapes
- Texture: subtle inner shadow on envelope

Quality bar:
- Clear focal point (envelope)
- Consistent with tokens: primary #667eea, secondary #764ba2

Negative constraints:
- No rect grid
- No gray placeholder
- No full-screen blur
```

---

## 三、六种风格 SVG Prompt 细化

以下六种风格仅为可调整的示例，并非完整列表或强制规则。按已有设计系统、用户要求和实际用途选择或改写；可使用其他风格。

### 3.1 glass 风格

```text
Style-specific requirements for glass:
- Semi-transparent surfaces: use opacity 0.6-0.8 on foreground shapes
- Background blur effect: apply feGaussianBlur (stdDeviation 8-16) on a background layer,
  then overlay glass surface with opacity
- Highlight strokes: 1px white/light stroke at 20-40% opacity on top and left edges
- Soft shadows: feDropShadow with low dx(0-2)/dy(2-4), high stdDeviation(6-12), low opacity(0.1-0.2)
- Layer order: blurred background → glass surface → content → highlight edges
- Color: use tokens primary/secondary with reduced opacity for glass panels
- Avoid: solid opaque fills, harsh edges, high-contrast borders, heavy shadows
```

### 3.2 editorial 风格

```text
Style-specific requirements for editorial:
- Asymmetric path compositions as visual anchors
- Large geometric shapes (circles, rectangles, diagonal lines) as background elements
- Muted accent colors: low saturation, high contrast with background
- Use clipPath for image-mask-like reveals and shape intersections
- Typography blocks as compositional elements (keep as <text>, not paths)
- Generous whitespace, intentional negative space
- Color: 1-2 dominant colors + 1 muted accent from tokens
- Avoid: symmetric layouts, busy decorations, gradients overload, rounded corners everywhere
```

### 3.3 data 风格

```text
Style-specific requirements for data visualization:
- Ring/arc progress: use stroke-dasharray on <circle> with calculated dash/offset values
- Grid lines: low-opacity strokes (0.1-0.2) for background reference grids
- Curve charts: <path> with smooth bezier (C or S commands), not jagged polylines
- Bar charts: <rect> with rx/ry 4-8px for rounded tops
- Status dots: small circles with subtle glow via feDropShadow (colored shadow matching status)
- Micro-light trails: thin strokes (1-1.5px) with gradient opacity from 1.0 to 0.0
- Axis labels: minimal, use tokens neutral colors, keep as <text>
- Color: data palette from tokens (primary for main, secondary for compare, accent for highlight)
- Avoid: 3D effects, decorative elements that distract from data, pie charts without clear labels
```

### 3.4 geometric 风格

```text
Style-specific requirements for geometric:
- Large shape combinations: circles, triangles, rectangles as primary compositional forms
- Hard-edge masks with clipPath for shape intersections and reveals
- High-contrast color blocks: 2-4 bold colors from tokens
- Structural whitespace as a design element (not empty space)
- Minimal or no gradients: if used, single-direction linear only
- Sharp edges: no rx/ry, no rounded corners on geometric shapes
- Color: bold primaries from tokens, avoid pastels
- Avoid: soft shadows, blur effects, organic curves, rounded corners, gradients
```

### 3.5 neumorphic 风格

```text
Style-specific requirements for neumorphic:
- Raised elements: light shadow top-left (dx=-4, dy=-4, stdDeviation 8, white at 0.7)
  + dark shadow bottom-right (dx=4, dy=4, stdDeviation 8, black at 0.15)
- Pressed/inset elements: invert shadows (inner light top-left, inner dark bottom-right)
- Background: low-contrast neutral (#e0e5ec or similar light gray from tokens)
- Subtle highlights: 1px semi-white (0.3-0.5 opacity) stroke on top edges
- All elements share same background color family (no contrasting fills)
- Shadows must be layered: use two feDropShadow in <filter> or two separate filters
- Color: monochromatic from tokens neutral palette, accent sparingly
- Avoid: strong borders, high contrast, saturated colors, flat solid fills
```

### 3.6 neon 风格

```text
Style-specific requirements for neon:
- Dark background: #0a0a0a to #1a1a1a (from tokens or fixed)
- Glowing strokes: feGaussianBlur (stdDeviation 4-8) + feMerge for layered glow effect
- Multiple transparent stroke layers: 3-4 layers with decreasing opacity (1.0 → 0.6 → 0.3 → 0.1)
  to create depth in the glow
- High-saturation accent colors: cyan #00fff5, magenta #ff00ff, lime #00ff88 (or from tokens)
- Thin base strokes: 1-2px for the core line, wider glow around it
- Glow color matching: shadow/glow color must match the stroke color
- Color: dark bg + 1-2 neon accents from tokens, no pastels
- Avoid: solid fills, flat colors, white backgrounds, thick strokes (>3px), muted colors
```

---

## 四、量化质量指标

### 4.1 SVG Icon 质量检查

- 检查图标在实际尺寸下的识别性、视觉对齐、语义和与既有图标体系的一致性。
- `viewBox`、颜色适配、文件大小和几何复杂度应满足交付环境；不以 path 数量、元素种类、单色或固定尺寸作为通用门槛。
- 根据实际用途提供可访问名称或隐藏装饰图标，避免重复朗读。

### 4.2 SVG Visual 质量检查

- 根据资产用途、品牌和风格检查构图、可识别性、可读性与完成度；纯色、少色、平面和简洁构图均可通过。
- 检查 `viewBox`、适合用途的无障碍信息、交付环境下的文件大小和渲染性能。
- 渐变、滤镜、色阶、元素类型、分组和复用均按需选择，不以数量或是否使用作为美感及放行指标。

### 4.3 质量检查方法

查看 SVG 结构与文件大小，并在可用环境中按实际尺寸渲染检查；对装饰性资产及有语义的资产分别检查其无障碍处理。自动统计只能辅助发现性能或结构问题，不能替代视觉判断，也不能把效果数量当作评分。

---

## 五、分类负面约束汇总

### 5.1 按资产类型

| 类型 | 禁止项 |
|------|--------|
| `icons/` | 符合既有图标体系和交付环境；避免无用途的复杂效果 |
| `visuals/` | 无 rect 网格、无灰色占位、无全屏模糊、无伪造真实图片、无 raster |

### 5.2 按风格

以下为示例风格的倾向，不是通用禁令；按设计意图和项目约定调整。

| 风格 | 禁止项 |
|------|--------|
| glass | 无不透明填充、无硬边、无高对比边框、无重阴影 |
| editorial | 无对称布局、无过度装饰、无渐变滥用、无全圆角 |
| data | 无 3D 效果、无干扰数据的装饰、无无标签饼图 |
| geometric | 无柔和阴影、无模糊效果、无有机曲线、无圆角 |
| neumorphic | 无强边框、无高对比、无饱和色、无纯白/纯黑 |
| neon | 无纯色填充、无白色背景、无粗线条(>3px)、无暗淡色 |

---

## 六、使用流程

```
SVG Visual Fallback 触发
  → 交付工程师判断资产类型（icon / visual）
  → 选择已有或自定义风格（第三节可选参考）
  → 填入对应 Prompt 模板（本文档第一/二节）
  → 按需调整并附加风格细化建议（本文档第三节）
  → 生成 SVG 文件
  → 按用途、风格与交付约束自检（本文档第四节）
  → 写入 DESIGN-GUIDE.md 的 SVG Visual Fallback 章节
  → 视觉审查师按用途、风格和约束审查
```

---

## 七、DESIGN-GUIDE 标注模板

进入 SVG fallback 后，`DESIGN-GUIDE.md` 必须新增一节：

```markdown
## SVG Visual Fallback

### 触发原因
{图片生成工具不可用 / 外部图片不可用 / 用户要求纯SVG / 交付环境只允许SVG}

### 替代策略
{品牌化抽象视觉 / 数据图形 / SVG插画 / 装饰层}

### 使用资产

#### icons/
| 文件名 | 用途 | 风格 | viewBox |
|--------|------|------|---------|
| search.svg | 搜索图标 | line | 24x24 |

#### visuals/
| 文件名 | 用途 | 风格 | viewBox | 采用的表现方式 |
|--------|------|------|---------|-----------|
| empty-state.svg | 空状态插画 | geometric | 375x400 | 渐变+路径+复用 |

### 生成 Prompt
{粘贴填入后的完整 Prompt}

### 视觉能力
渐变 / 滤镜 / 遮罩 / 路径 / 复用 / 质感（勾选实际使用的）

### 性能控制
- 滤镜数量：{N} 个
- 最大文件：{N}KB
- 动画：{无 / 轻量}

### 不替代的真实图片范围
{真实人物照片 / 真实商品图 / 真实场景照片}
```
