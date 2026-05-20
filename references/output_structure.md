# 输出结构

## 两个体系分离

**内部记忆和设计输出是两个独立体系：**

| 体系 | 目录 | 用途 | 用户可见 |
|------|------|------|----------|
| 内部记忆 | `.design-doc/` | 进度追踪、需求记录、设计摘要 | 否 |
| 设计输出 | `/design-output/` | HTML/CSS、图标、截图、设计文档 | 是 |

**向用户展示时，只展示 `/design-output/` 的内容，不展示 `.design-doc/` 的内容。**

## 画廊展示规范

**index.html 是设计画廊页面——所有页面平铺展示，不是 iframe 切换：**

- 所有页面以手机外框 mockup 形式平铺在同一个网页上
- 同一模块的页面在一组内横向排列
- 不同模块上下排列，整个网页可滚动浏览
- 每个页面有独立的手机外框（375x812 或项目指定尺寸）
- 待实现页面也有占位 mockup（灰色占位+标注"待实现"）
- 模块分组标题清晰（如"消息模块""队伍模块"）
- 每个 mockup 下方标注页面名称和文件路径

**展示布局：**
```
[整个网页，可上下滚动]

── 模块标题：消息 ──────────
  ┌──────────┐  ┌──────────┐
  │ 消息列表  │  │ 聊天详情  │
  │ (phone)  │  │ (待实现)  │
  └──────────┘  └──────────┘

── 模块标题：队伍 ──────────
  ┌──────────┐
  │ 队伍页面  │
  │ (phone)  │
  └──────────┘

── 模块标题：发现 ──────────
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ 发现页面  │  │ 骑友详情  │  │ 活动详情  │
  │ (phone)  │  │ (待实现)  │  │ (待实现)  │
  └──────────┘  └──────────┘  └──────────┘
```

## 设计输出目录结构

### 单页面输出

```
/design-output/
├── index.html              # 主页面（可直接浏览器打开）
├── style.css               # 样式文件
├── tokens.json             # 设计token（JSON格式）
├── icons/                  # SVG图标（所有用到的图标都要导出）
│   ├── logo.svg
│   ├── phone.svg
│   ├── lock.svg
│   ├── sms.svg
│   ├── wechat.svg
│   ├── apple.svg
│   ├── eye.svg
│   ├── eye-off.svg
│   └── ...（其他图标）
├── screenshots/            # 截图/效果图
│   ├── preview.png
│   └── components.png
├── responsive/             # 响应式版本
│   ├── mobile.html
│   ├── tablet.html
│   └── desktop.html
├── DESIGN-GUIDE.md         # 设计规范文档
└── REQUIREMENTS.md         # 交互需求文档（供LLM生成APP代码）
```

### 项目级输出（3+页面时）

```
/design-output/
├── index.html              # 首页/Dashboard
├── style.css               # 全局样式（所有页面共享）
├── tokens.json             # 设计token（锁定后不可私自修改）
├── components/             # 共享组件库
│   ├── button.html         # 按钮组件（含所有状态）
│   ├── input.html          # 输入框组件（含所有状态）
│   ├── card.html           # 卡片组件
│   ├── navbar.html         # 导航栏组件
│   ├── modal.html          # 弹窗组件
│   ├── toast.html          # 提示组件
│   └── ...（其他共享组件）
├── pages/                  # 所有页面
│   ├── login.html          # 登录页
│   ├── register.html       # 注册页
│   ├── home.html           # 首页
│   ├── profile.html        # 个人中心
│   └── ...（其他页面）
├── icons/                  # SVG图标
├── routing.json            # 页面路由表
├── screenshots/            # 截图/效果图
├── responsive/             # 响应式版本
├── consistency-report.md   # 跨页面一致性校验报告
├── DESIGN-GUIDE.md         # 设计规范文档
└── REQUIREMENTS.md         # 交互需求文档（供LLM生成APP代码）
```

## REQUIREMENTS.md 规范（核心）

**用途：** 与HTML/CSS设计文件配合，供LLM理解交互逻辑后生成真实APP代码。

**与 DESIGN-GUIDE.md 的区别：**
- DESIGN-GUIDE.md = 视觉规范（长什么样）
- REQUIREMENTS.md = 交互规范（怎么运作）

### 文档结构

```markdown
# 交互需求文档

## 页面清单
| 页面 | 文件 | 核心交互 |
|------|------|----------|
| 登录 | pages/login.html | 表单验证、登录请求、第三方跳转 |

## 全局规则
- 网络错误统一toast提示，3秒后消失
- 所有请求超时时间10秒
- 键盘弹起时页面上推，不遮挡输入框

## 页面：登录页

### 组件状态
| 组件 | 状态 | 触发条件 | 表现 |
|------|------|----------|------|
| 登录按钮 | default | 页面加载 | 渐变色可点击 |
| 登录按钮 | loading | 点击后 | 显示旋转动画，禁用点击 |
| 登录按钮 | disabled | 表单未填完 | 灰色，不可点击 |
| 密码输入框 | normal | 默认 | 显示密码圆点 |
| 密码输入框 | visible | 点击眼睛图标 | 显示明文 |
| 验证码按钮 | idle | 默认 | 显示"获取验证码" |
| 验证码按钮 | countdown | 点击后 | 显示"60s"倒计时 |

### 交互流程
1. 用户输入账号 → 实时校验格式（邮箱/手机号）
2. 用户输入密码 → 实时校验长度≥6
3. 账号+密码均合法 → 登录按钮变为可点击
4. 点击登录 → 按钮变loading → 发送POST /api/auth/login
5. 成功 → 跳转首页
6. 失败 → 按钮恢复 → 显示错误toast

### API对接
| 接口 | 方法 | 参数 | 成功响应 | 失败响应 |
|------|------|------|----------|----------|
| /api/auth/login | POST | {account, password} | {token, user} | {code, message} |
| /api/auth/sms | POST | {phone} | {success} | {code, message} |
| /api/auth/sms/verify | POST | {phone, code} | {token, user} | {code, message} |

### 异常处理
| 场景 | 触发条件 | 处理方式 |
|------|----------|----------|
| 网络断开 | 请求失败 | toast"网络连接失败，请检查网络" |
| 密码错误 | 返回401 | toast"账号或密码错误" |
| 验证码过期 | 返回410 | toast"验证码已过期，请重新获取" |
| 频繁请求 | 返回429 | toast"操作太频繁，请稍后再试" |
| 账号不存在 | 返回404 | toast"账号不存在" |

### 边界情况
| 场景 | 处理方式 |
|------|----------|
| 输入框为空时点击登录 | 按钮disabled，不发请求 |
| 密码含特殊字符 | 前端不转义，后端处理 |
| 快速连续点击登录 | loading态防抖，忽略重复点击 |
| 页面切换时输入未保存 | 丢弃输入，不缓存 |
```


## 图标导出规则（核心）

**设计中用到的所有图标必须单独导出为SVG文件，存放在 `design-output/icons/` 目录：**

### 导出要求

1. **所有图标都要导出** - 不管是内嵌SVG还是图片引用，都要单独导出
2. **命名规范** - 使用英文小写+连字符，如 `phone.svg`、`lock.svg`、`wechat.svg`
3. **格式统一** - 全部使用SVG格式，确保清晰度
4. **颜色适配** - 图标颜色使用 `currentColor` 或设计主色，便于适配不同场景

### 常见图标清单

| 图标 | 文件名 | 用途 |
|------|--------|------|
| Logo | logo.svg | 应用图标 |
| 手机 | phone.svg | 手机号输入框 |
| 锁 | lock.svg | 密码输入框 |
| 验证码 | sms.svg | 验证码输入框 |
| 微信 | wechat.svg | 微信登录 |
| Apple | apple.svg | Apple登录 |
| 眼睛 | eye.svg | 显示密码 |
| 眼睛-关闭 | eye-off.svg | 隐藏密码 |
| 返回 | back.svg | 导航返回 |
| 关闭 | close.svg | 关闭按钮 |
| 搜索 | search.svg | 搜索功能 |
| 更多 | more.svg | 更多选项 |
| 分享 | share.svg | 分享功能 |
| 收藏 | favorite.svg | 收藏功能 |
| 编辑 | edit.svg | 编辑功能 |
| 删除 | delete.svg | 删除功能 |

### HTML引用方式

```html
<!-- 方式1：内嵌SVG（推荐，性能好） -->
<button class="social-btn">
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path d="..." fill="currentColor"/>
  </svg>
</button>

<!-- 方式2：图片引用（图标文件已导出） -->
<img src="icons/wechat.svg" alt="微信登录" width="28" height="28">
```

**无论HTML中使用哪种方式，图标文件都必须单独导出到 `design-output/icons/` 目录。**

## 用户输出格式

**设计完成后，向用户输出：**

```
---
设计输出

文件位置：design-output/index.html
打开方式：在浏览器中直接打开即可预览

设计文件
- design-output/index.html — 主页面
- design-output/style.css — 样式文件
- design-output/icons/ — SVG图标（所有图标）
- design-output/screenshots/ — 效果图
- design-output/DESIGN-GUIDE.md — 设计规范

如需调整任何细节，直接告诉我即可。
---
```

## 文件说明

### index.html

主页面文件，包含完整的HTML结构。**用户直接打开即可预览。**

### style.css

样式文件，包含所有CSS样式。

### tokens.json

设计token文件，包含颜色、字体、间距等设计变量。**必须是JSON格式，不是markdown。**

```json
{
  "color": {
    "primary": "#667eea",
    "secondary": "#764ba2"
  },
  "font": {
    "family": "-apple-system, BlinkMacSystemFont, sans-serif",
    "size": {
      "xs": "12px",
      "sm": "13px",
      "base": "14px"
    }
  }
}
```

### icons/

图标目录，包含所有用到的SVG格式图标文件。**必须导出所有图标，不能遗漏。**

### screenshots/

截图/效果图目录，包含设计预览截图。

### responsive/

响应式版本目录，包含不同屏幕尺寸的适配版本。

### DESIGN-GUIDE.md

设计规范文档，必须精确到逐元素标注。**不只是概要描述，而是可直接交给前端实现的精确规格。**

#### 必须包含的内容

```markdown
# 设计规范

## 1. 设计Token
- 颜色系统（主色/辅色/强调色/状态色/中性色，每个色值+用途）
- 字体系统（字体族+字号+字重+行高，逐级定义）
- 间距系统（xs/sm/md/base/lg/xl/xxl，每个值+使用场景）
- 圆角系统（sm/md/base/lg/xl/full，每个值+使用组件）
- 阴影系统（sm/md/lg/glow，每个值+使用场景）

## 2. 页面布局
- 页面结构图（ASCII 或描述）
- 各区域尺寸（px 值）
- 安全区域定义
- 响应式断点及适配规则

## 3. 组件规范（逐个组件）
### 组件名：XXX
- 尺寸：宽 x 高（px）
- 位置：距顶部/左侧/右侧（px）
- 背景：颜色/渐变（精确值）
- 边框：宽度/颜色/样式
- 圆角：px 值
- 阴影：精确值
- 内边距：上/右/下/左（px）
- 文字样式：字号/字重/颜色/行高/对齐
- 图标：尺寸/颜色/间距
- 状态：
  - default：（精确值）
  - hover/pressed：（精确值）
  - active/selected：（精确值）
  - disabled：（精确值）
  - loading：（精确值）
  - error：（精确值）

## 4. 图标规范
- 尺寸定义（Tab 图标/操作图标/状态图标的尺寸）
- 颜色规则（currentColor / 设计主色 / 状态色）
- 选中/未选中状态

## 5. 动效规范
- 过渡动画：duration / easing / property
- 状态动画：duration / easing / iteration
- 页面切换：duration / easing / type

## 6. 响应式规范
- 断点定义（px 值）
- 每个断点的布局变化
- 组件尺寸变化
```

#### 质量标准

- 每个组件必须有精确的 px 值，禁止"大约""适中"等模糊描述
- 每个组件必须列出所有状态（至少 default + 1 种反馈态）
- 文字样式必须精确到：字号 + 字重 + 颜色 + 行高
- 间距必须精确到具体 px 值
- 颜色必须精确到 hex/rgba 值

## 内部记忆结构（用户不可见）

```
.design-doc/
├── README.md              # 项目总目录（设计进度、需求总结）
├── auth/                  # 认证模块
│   ├── _index.md         # 模块总览
│   └── login-regular.md  # 登录页记忆
├── chat/                  # 聊天模块
│   ├── _index.md
│   └── chat-main.md
└── settings/              # 设置模块
    ├── _index.md
    └── settings-main.md
```

### 记忆文档内容

- 模块信息（名称、状态、时间）
- 需求总结（功能、交互、约束）
- 设计方案摘要（布局、组件、细节）
- 设计进度（待完成项）
- 变更记录（历史变更）

**记忆文档不包含完整的HTML/CSS代码，只包含设计摘要和进度。**
