# SVG 生成 Prompt 模板

## 定位

当 SVG Visual Fallback 触发时，交付工程师必须将当前设计设定填入以下模板，并把完整 Prompt 写入 `DESIGN-GUIDE.md` 的 `SVG Visual Fallback` 章节。不得只写"画一个空状态插画"。

本文件包含 3 类 Prompt 模板（Icon / Visual / 风格细化）和质量标准，供交付工程师和视觉审查师使用。

---

## 一、SVG Icon 生成 Prompt 模板

用于 `design-output/icons/` 目录的功能图标。目标：轻量、可复用、可适配颜色。

```text
Generate a clean SVG icon named {icon_name}.svg.
Canvas: viewBox="0 0 {24|48|64}". Output exactly one SVG file.

Subject:
- Icon purpose: {功能描述，如"手机号输入框前缀图标"}
- Semantic meaning: {语义，如"phone / mobile / lock"}
- Style: {line|filled|duotone}
- Stroke width: {1.5px|2px}
- Color: currentColor（默认）或 {指定色值，如品牌主色 #667eea}

SVG implementation requirements:
- Use <path> as primary shape, supplement with <circle>, <rect>, <line>, <polyline>
- Keep paths clean and minimal (target: under 5 path commands per icon)
- Use stroke-linecap="round" stroke-linejoin="round" for rounded icons
- Add <title>{icon description}</title> for accessibility
- All styling self-contained, no external references, scripts, or fonts
- Use <defs> for reusable sub-shapes if needed
- Set fill="none" stroke="currentColor" for line icons; fill="currentColor" for filled icons

Quality bar:
- Pixel-perfect at 24px render size
- Optical center aligned (not just bounding box center)
- Consistent visual weight with other icons in the set
- Recognizable silhouette at 16px
- Path data optimized (no redundant points)

Negative constraints:
- No gradients (icons should be single-color or currentColor)
- No filters, blur, or shadow effects
- No text or labels inside the icon artwork
- No clipPath or mask (keep paths clean)
- No stroke widths below 1px or above 3px
- No raster images or base64 data
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
- Style: {glass|editorial|data|geometric|neumorphic|neon}

SVG implementation requirements:
- Use layered <g> groups with clear ids: background, midground, foreground, accents, highlights
- Use <path>, <circle>, <ellipse>, <polygon> for shapes
- Use <linearGradient>, <radialGradient> for color transitions
- Use <clipPath>, <mask> for composition and reveal effects
- Use <filter> sparingly: feDropShadow, feGaussianBlur (max 2-3 filter nodes per asset)
- Reuse shapes via <defs> + <use>
- Add <title> and <desc> describing the asset purpose and content

High-aesthetics requirements (use at least 3 of 6):
- Gradients: linearGradient, radialGradient, opacity highlights, gradient strokes
- Filters: feDropShadow, feGaussianBlur, feTurbulence, feColorMatrix
- Masks: clipPath, mask, gradient transparency layers
- Paths: bezier curves, waveforms, data lines, segmented rings, irregular containers
- Reuse: defs, symbol, use, named layers
- Texture: inner shadows, highlight strokes, noise texture, local glow

Quality bar:
- At least 6 meaningful color levels
- Visible depth through layering (not flat)
- Balanced composition with clear focal point
- Consistent with page tokens and brand palette
- File size under 50KB

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

High-aesthetics requirements (use at least 3 of 6):
- Gradients: linearGradient on envelope body
- Paths: bezier curves for envelope shape, star paths
- Reuse: defs + use for repeated star shapes
- Texture: subtle inner shadow on envelope

Quality bar:
- At least 6 color levels
- Clear focal point (envelope)
- Consistent with tokens: primary #667eea, secondary #764ba2

Negative constraints:
- No rect grid
- No gray placeholder
- No full-screen blur
```

---

## 三、六种风格 SVG Prompt 细化

以下为每种风格的 SVG 实现要求，填入对应模板的 `Style` 字段后附加。

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

### 4.1 SVG Icon 质量指标

| 维度 | 最低要求 | 推荐值 | 检查方法 |
|------|---------|--------|----------|
| 矢量元素类型 | ≥2 种（path + 1 other） | ≥3 种 | 统计 SVG 元素类型 |
| path 命令数 | ≤10 个 | ≤6 个 | 统计 d 属性中的命令数 |
| 文件大小 | ≤5KB | ≤3KB | 文件字节数 |
| viewBox | 必须有 | 0 0 24 24 | 检查 viewBox 属性 |
| title 标签 | 必须有 | 有描述性文本 | 检查 `<title>` |
| 颜色使用 | currentColor 或 1 色 | currentColor | 检查 fill/stroke 值 |
| 可识别性 | 16px 可识别 | 12px 可识别 | 缩小渲染测试 |

### 4.2 SVG Visual 质量指标

| 维度 | 最低要求 | 推荐值 | 检查方法 |
|------|---------|--------|----------|
| 矢量元素多样性 | ≥3 种类型 | ≥5 种 | 统计 path/circle/rect/polygon/ellipse |
| 色彩层次 | ≥4 色阶 | ≥6 色阶 | 统计唯一 fill/stroke 颜色数 |
| 分层 `<g>` 组 | ≥3 层 | ≥5 层 | 统计 `<g>` 标签数 |
| 渐变使用 | ≥1 个 | ≥2 个（linear+radial） | 统计 gradient 定义数 |
| 滤镜使用 | 0-2 个 | 1-3 个 | 统计 `<filter>` 数量 |
| `<defs>` 复用 | ≥1 个 | ≥2 个 | 统计 `<defs>` 中的元素 |
| 文件大小 | ≤50KB | ≤30KB | 文件字节数 |
| viewBox | 必须有 | 匹配设计尺寸 | 检查 viewBox 属性 |
| title + desc | 必须有 | 描述性文本 | 检查标签存在 |
| 高美感构成 | ≥3 类 | ≥4 类 | 检查渐变/滤镜/遮罩/路径/复用/质感 |

### 4.3 质量指标自动检查

交付工程师输出 SVG 后，视觉审查师必须执行以下检查：

```bash
# Icon 检查
# 1. 文件大小
ls -la design-output/icons/*.svg | awk '{if($5 > 5120) print $9, "EXCEEDS 5KB"}'

# 2. viewBox 存在
grep -L 'viewBox' design-output/icons/*.svg

# 3. title 存在
grep -L '<title>' design-output/icons/*.svg

# 4. 无渐变/滤镜
grep -l 'Gradient\|<filter' design-output/icons/*.svg  # 应无输出

# Visual 检查
# 1. 文件大小
ls -la design-output/visuals/*.svg | awk '{if($5 > 51200) print $9, "EXCEEDS 50KB"}'

# 2. 渐变数量
grep -c 'Gradient' design-output/visuals/*.svg

# 3. g 层数量
grep -c '<g' design-output/visuals/*.svg

# 4. rect 网格检测（超过 200 个 rect 且 path 不足 20 → 疑似网格冒充）
grep -c '<rect' design-output/visuals/*.svg
grep -c '<path' design-output/visuals/*.svg
```

---

## 五、分类负面约束汇总

### 5.1 按资产类型

| 类型 | 禁止项 |
|------|--------|
| `icons/` | 无渐变、无滤镜、无 blur、无文字转曲、无 clipPath、无 stroke<1px、无 raster |
| `visuals/` | 无 rect 网格、无灰色占位、无全屏模糊、无伪造真实图片、无 raster |

### 5.2 按风格

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
  → 选择风格（glass / editorial / data / geometric / neumorphic / neon）
  → 填入对应 Prompt 模板（本文档第一/二节）
  → 附加风格细化要求（本文档第三节）
  → 生成 SVG 文件
  → 对照量化指标自检（本文档第四节）
  → 写入 DESIGN-GUIDE.md 的 SVG Visual Fallback 章节
  → 视觉审查师按指标和约束审查
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
| 文件名 | 用途 | 风格 | viewBox | 高美感构成 |
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
