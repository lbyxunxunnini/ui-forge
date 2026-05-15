# Demo Transcript

真实对话示例，展示 UI Forge 在不同模式下的交互方式。

---

## Demo 1: 标准设计流程 (uif-)

**用户：** uif-设计一个iOS登录页，现代风格，渐变背景，包含微信登录

**系统：**
```
[ui-forge] controller：路由判定
- 入口：standard
- 模式：design
- 预算：L2（常规单页）
- 设计卡：未检测到，将在设计完成后生成
```

```
[ui-forge] 需求分析师：第1轮追问
- 登录方式的优先级如何排列？
  A. 手机号 + 密码为主，微信为辅（推荐，国内常见）
  B. 微信为主，手机号为辅
  C. 只有手机号 + 密码
  推荐：A（国内APP常用模式，微信作为快捷入口）
```

**用户：** A

```
[ui-forge] 需求分析师：第2轮追问
- 登录成功后跳转到哪里？
  A. 首页（推荐，首次用户需要引导）
  B. 上一个页面（如果是被踢出登录）
  C. 根据用户状态判断
  推荐：A（首次登录走首页，回退登录用 B）
```

**用户：** A

```
[ui-forge] 需求分析师：需求收口完成
- 平台：iOS
- 页面：登录页
- 风格：现代，渐变背景
- 登录方式：手机号+密码（主）+ 微信（辅）
- 跳转：登录成功 → 首页
- 交接给：UI设计师
```

```
[ui-forge] UI设计师：第1步 - 布局
- 方案A：居中卡片布局（推荐，现代风格常用）
- 方案B：全屏渐变 + 底部浮层
- 推荐：方案A（信息聚焦，渐变作为背景）
- 请选择
```

**用户：** A

```
[ui-forge] UI设计师：方案A细节确认
- 渐变方向：左上到右下（135deg）
- 渐变色：#667eea → #764ba2
- 卡片：白色半透明，backdrop-filter 模糊
- 确认？
```

**用户：** 确认

```
[ui-forge] UI设计师：设计方案完成
- 布局：居中卡片
- 组件：Logo、手机号输入框、密码输入框、登录按钮、微信登录按钮、注册链接
- 渐变：135deg #667eea → #764ba2
- 卡片：rgba(255,255,255,0.95), backdrop-filter: blur(20px)
- 确认状态：待确认
```

**用户：** 确认

```
[ui-forge] UI设计师：输出检查通过
- ✅ index.html
- ✅ style.css
- ✅ tokens.json
- ✅ icons/ (8 SVGs)
- ✅ DESIGN-GUIDE.md
- ✅ REQUIREMENTS.md

设计输出：
- 文件位置：design-output/index.html
- 打开方式：在浏览器中直接打开即可预览
```

---

## Demo 2: 快速调整 (uif-fast)

**用户：** uif-fast把主按钮改成#4F46E5

**系统：**
```
[ui-forge] UI设计师：快速调整完成
- 修改项：主按钮背景色
- 变更：#667eea → #4F46E5
- 影响文件：style.css, tokens.json
- 影响检查：无布局/响应式/交互影响
```

（自动退出，无追问）

---

## Demo 3: UI诊断 (uif-critique)

**用户：** uif-critique这个页面为什么看起来很普通

**系统：**
```
[ui-forge] UI设计师：整体诊断
- 核心问题：figure-ground 失效 — 表头、筛选区和主列表同时争抢注意力
- 视觉语言：所有元素使用相同的 surface 和 shadow，没有层级区分
- 信息密度：首屏塞了太多模块，没有呼吸感

结构性修正：
1. 首屏只保留一个主焦点（概览卡片），其余折叠
2. 筛选区压成 48px 工具条，不使用卡片容器
3. 列表标题提升到 28px/600，正文 14px/400，拉开层级
4. 去掉所有卡片的 box-shadow，改用 1px border 分隔

禁止项：
- 不要再叠一层卡片阴影
- 不要用渐变背景
- 不要在首屏放超过 3 个数据模块
```

（不进入交付，自动退出）

---

## Demo 4: 全自动 (uif-a)

**用户：** uif-a设计一个深色模式的设置页面

**系统：**
```
[ui-forge] controller：自动模式启动
- 任务：设置页面设计
- 已明确：深色模式
- 自动假设：
  · 平台：iOS（默认）
  · 布局：列表式设置（iOS 标准）
  · 主色：#4F46E5
  · 背景：#0F172A
  · 文字：#F8FAFC / #94A3B8
```

```
[ui-forge] 需求分析师：需求收口完成（自动模式）
- 页面类型：设置页
- 功能模块：账户信息、通知设置、隐私设置、关于、退出登录
- 自动补齐：每个设置项右侧带箭头指示可点击
```

```
[ui-forge] UI设计师：设计方案
- 布局：顶部导航栏 + 分组列表
- 分组：账户（头像+昵称+ID）、通用（通知/隐私）、其他（关于/退出）
- 列表项：左侧图标 + 标题 + 副标题 + 右侧箭头/开关
- tokens.json 已锁定
- 输出文件...
```

（自动退出）

---

## Demo 5: 交付模式 (uif-deliver)

**用户：** uif-deliver给我导出登录页的HTML/CSS/SVG

**系统：**
```
[ui-forge] UI设计师：交付输出
- 源文件：design-output/login-regular.md（已有设计）
- 导出内容：
  · index.html — 完整页面
  · style.css — 独立样式
  · tokens.json — 设计 token
  · icons/ — 8 个 SVG 图标
  · DESIGN-GUIDE.md — 视觉规范
  · REQUIREMENTS.md — 交互规范
- 输出位置：design-output/
```

（自动退出）

---

## Demo 6: 设计系统收口

**用户：** uif-我们已经有4个页面了，帮我收口一套可复用的设计系统

**系统：**
```
[ui-forge] controller：路由判定
- 入口：standard
- 模式：design_system
- 预算：L4（多页面/设计系统）
```

```
[ui-forge] 需求分析师：第1轮追问
- 收口范围？
  A. 先收口 tokens + 共享组件（推荐，先打好基础）
  B. 直接出完整组件库
  C. 只做 token 规范文档
  推荐：A（先收口 token 和核心组件，后续逐步扩展）
```

**用户：** A

```
[ui-forge] UI设计师：设计系统收口
- Type scale：H1 24px/Bold → caption 12px/Regular
- Spacing scale：4/8/12/16/24/32/48
- Color tokens：primary/secondary/neutral/success/warning/error
- 共享组件：Button（4 variants × 5 states）、Input、Card、Navbar
- 输出：
  · tokens.json（锁定版）
  · components/（组件 HTML）
  · DESIGN-GUIDE.md（系统规范）
```

---

## Demo 7: 记忆恢复

**用户：** uif-继续设计聊天页面

**系统：**
```
[ui-forge] 需求分析师：检测到已有设计
- 模块：chat
- 已有设计：chat-main.md（2026-05-15 创建，现代风格）
- 设计状态：进行中（需求已确认，UI 设计待完成）
- 选项A：重新设计（推荐，从头开始）
- 选项B：继续使用已有设计
- 选项C：查看详情
```

**用户：** B

```
[ui-forge] 需求分析师：恢复上下文
- 已恢复：需求分析已完成
- 进度：UI 设计阶段
- 继续 UI 设计...
```
