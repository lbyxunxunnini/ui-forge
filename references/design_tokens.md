# 设计Token

以下数值是示例，不是强制配色或固定风格。已有产品优先复用其设计系统；新产品按品牌和需求确定。

## 语义与可访问性

- 在目标项目的 Token 中按用途定义页面/卡片背景、主要/次要文字、边框和强调/成功/警告/错误状态；组件引用语义角色，具体命名遵循项目惯例。
- 仅在目标项目支持或需求要求多主题时，为各主题提供对应语义值并分别检查可读性；不强制新增深色模式。
- 检查文字与背景的对比度、交互元素的可见焦点和键盘操作；装饰性图标从无障碍树隐藏，纯图标按钮提供可访问名称。适用平台的既有无障碍要求优先。
- 图标优先复用已有体系，没有时选择适合的体系；保持语义、风格、线宽和尺寸一致，并按交付规则导出。

## 颜色系统

- Primary: #667eea
- Secondary: #764ba2
- Neutral: #f5f5f7 - #0f172a
- Success: #22c55e
- Warning: #f59e0b
- Error: #ef4444

### 颜色使用规范

- 主色调用于按钮、链接、激活状态
- 中性色用于背景、文字、边框
- 成功色用于成功提示
- 警告色用于警告提示
- 错误色用于错误提示

## 字体系统

- Primary: -apple-system, BlinkMacSystemFont, 'SF Pro Display'
- H1: 24px, Bold
- H2: 20px, Semibold
- Body: 16px, Regular
- Caption: 14px, Regular

### 字体使用规范

- H1用于页面标题
- H2用于卡片标题
- Body用于正文内容
- Caption用于辅助文字

## 间距系统

- XS: 4px
- SM: 8px
- MD: 16px
- LG: 24px
- XL: 32px
- XXL: 48px

### 间距使用规范

- XS用于图标与文字间距
- SM用于列表项间距
- MD用于组件内边距
- LG用于卡片内边距
- XL用于页面内边距
- XXL用于大区块间距

## 圆角

- Small: 8px
- Medium: 14px
- Large: 20px
- XLarge: 24px

### 圆角使用规范

- Small用于小按钮、标签
- Medium用于输入框、按钮
- Large用于卡片
- XLarge用于弹窗、模态框

## 阴影

- Small: 0 2px 8px rgba(0, 0, 0, 0.06)
- Medium: 0 4px 16px rgba(0, 0, 0, 0.08)
- Large: 0 8px 32px rgba(0, 0, 0, 0.1)

### 阴影使用规范

- Small用于按钮、标签
- Medium用于卡片、下拉菜单
- Large用于弹窗、模态框
