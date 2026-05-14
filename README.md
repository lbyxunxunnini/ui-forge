# UI Forge

GitHub: [lbyxunxunnini/ui-forge](https://github.com/lbyxunxunnini/ui-forge) · License: MIT · 当前版本：0.1.0

UI Forge 是一个面向 App 和 Web 的 UI 设计工作流 skill。它处理的不只是“画个页面”，而是从需求理解、结构收口、视觉判断、交互状态，到 HTML/CSS/SVG 交付的完整链路。

它不是 `polanyi-design` 的替代品。

- `polanyi-design` 更像设计判断引擎，擅长解释为什么一个界面失衡、模板化或缺少主张。
- `ui-forge` 更像设计执行层，擅长把判断推进成页面方案、组件规范、tokens 和交付文件。

如果你只想做设计评审，`polanyi-design` 已经很强。
如果你要把评审继续推进成重设计和可交付产物，`ui-forge` 仍然有必要存在。

## 功能特点

- 智能需求解析 - 自动识别平台、页面类型、设计风格
- 设计诊断 - 从“感觉不对”翻译到结构问题和具体修正
- 多风格支持 - 简约、现代、商务、科技、活泼
- 全平台覆盖 - iOS、Android、Web、桌面端
- 丰富动效 - 基础动画、过渡效果、高级交互
- 响应式设计 - 自动适配手机、平板、桌面
- 完整输出 - HTML/CSS、SVG、设计token、规范文档
- 记忆功能 - 保存设计进度，下次可继续
- UI规范调整 - 大小、间距、颜色、字体等直接调整

## 适用场景

- 新页面设计
- 页面重设计
- UI 评审和诊断
- 设计系统收口
- 交互规格和前端交付

## 使用方式

### 触发方式

- `uif-`
- `/ui-forge`
- `uid-`
- `/ui-design`
- `使用 ui-forge`
- `调用 ui-forge`

### 使用示例

```
uif-设计一个iOS登录页，现代风格，渐变背景
/ui-forge帮我设计一个电商APP首页
使用ui-forge，做一个深色模式的设置页面
调用ui-forge设计一个登录页
uid-重设计这个后台首页，先解释为什么像模板
```

## 工作模式

- 诊断模式：只做设计评审和结构判断
- 设计模式：从需求推进到信息结构、视觉和交互方案
- 交付模式：输出 HTML/CSS/SVG、tokens、图标和设计指南

## Demo 预览

在线预览：打开 `demo/index.html` 即可查看所有 Demo

- **登录页 Demo**：`demo/login-demo.html` - 支持5种风格切换
- **首页 Demo**：`demo/home-demo.html` - 展示完整首页布局

### 截图预览

> 提示：运行 Demo 后可截图保存到 `screenshots/` 目录

| 登录页（现代风格） | 登录页（科技风格） | 首页（现代风格） |
|:---:|:---:|:---:|
| ![登录页-现代](screenshots/login-modern.png) | ![登录页-科技](screenshots/login-tech.png) | ![首页-现代](screenshots/home-modern.png) |

## 项目结构

```
ui-forge/
├── SKILL.md                    # 核心内容
├── references/                 # 参考文档
│   ├── roles/                  # 角色定义
│   │   ├── requirement_analyst.md
│   │   └── ui_designer.md
│   ├── polanyi_integration.md  # 设计判断层接入
│   ├── recipes.md              # 常用任务 recipes
│   ├── evaluation_rubric.md    # 输出评测标准
│   ├── discussion_mechanism.md
│   ├── escalation_mechanism.md
│   ├── memory_protocol.md
│   ├── design_tokens.md
│   ├── output_structure.md
│   ├── design_styles.md
│   ├── animation_effects.md
│   ├── skill_visibility.md
│   ├── task_runtime_prompt.md
│   └── input_incomplete_handling.md
├── templates/                  # 页面模板
│   ├── login.html
│   ├── home.html
│   └── style.css
├── components/                 # 组件库
│   ├── input.html
│   ├── button.html
│   ├── card.html
│   ├── navigation.html
│   └── components.css
├── config/                     # 配置文件
│   └── design-config.json
├── demo/                       # 在线预览
│   ├── index.html              # Demo入口
│   ├── login-demo.html         # 登录页Demo
│   └── home-demo.html          # 首页Demo
├── examples/                   # 示例
│   ├── login-example.md
│   └── dashboard-critique.md
├── tests/                      # 测试用例
│   └── test-cases.md
├── .design-doc/                # 设计文档目录
├── LICENSE                     # MIT许可证
└── CONTRIBUTING.md             # 贡献指南
```

## 核心功能

### 1. 需求分析

- 自动识别平台、页面类型、设计风格
- 追问逻辑漏洞，确保需求完整
- 提供常用选择和推荐选择

### 2. UI设计

- 根据需求生成设计方案
- 追问设计细节，确保质量
- 提供常用选择和推荐选择

### 3. UI规范调整

- 大小调整：字体大小、图标大小、按钮大小
- 间距调整：内边距、外边距、行间距
- 颜色调整：背景色、文字色、边框色
- 字体调整：字体族、字重、字号
- 图标替换：替换图标样式、大小、颜色
- 距离移动：元素位置调整、对齐方式调整

### 4. 记忆功能

- 保存设计进度到.design-doc目录
- 下次进入时读取并恢复上下文
- 按模块分层设计，便于管理

### 5. 持久化模式

- 进入后不退出，直到用户明确要求退出
- 当用户输入与设计不相关的内容时，询问是否退出

## 支持的平台

- iOS应用
- Android应用
- Web网页
- 桌面应用
- 响应式设计

## 支持的页面类型

- 登录/注册页
- 首页/Dashboard
- 个人中心/设置页
- 列表页/详情页
- 搜索页/表单页

## 设计风格

- 简约风格 - 干净、留白、极简
- 现代风格 - 渐变、卡片、圆角
- 商务风格 - 专业、稳重、蓝色系
- 科技风格 - 深色、霓虹、未来感
- 活泼风格 - 彩色、圆润、有趣

## 输出结构

```
/design-output/
├── index.html              # 主页面
├── style.css               # 样式文件
├── tokens.json             # 设计token
├── icons/                  # SVG图标
├── responsive/             # 响应式版本
└── DESIGN-GUIDE.md         # 设计规范文档
```

## 版本

- 当前版本：0.1.0
- 版本说明：`0.1.0` 是首个公开版本，收口了工作流定位、提问预算、需求确认门禁和角色放行矩阵
- 查看更新日志：CHANGELOG.md
