# 登录页设计示例

## 用户输入

```
uif-设计一个iOS登录页，现代风格，渐变背景，包含微信登录
```

## 需求分析师输出

```
[ui-forge] 需求分析师：
- 需求理解：设计一个iOS平台的登录页面
- 平台：iOS应用
- 页面类型：登录页
- 设计风格：现代风格
- 功能需求：
  1. 手机号输入
  2. 密码输入
  3. 登录按钮
  4. 微信登录
  5. 注册入口
- 设计约束：
  1. 渐变背景
  2. 遵循iOS设计规范
  3. 支持深色模式
- 关键点：
  1. 渐变背景色值
  2. 微信登录图标样式
  3. 注册入口位置
- 待确认：
  1. 是否需要Apple登录？
  2. 登录成功后跳转页面？
- 建议：
  1. 推荐添加Apple登录，符合iOS规范
  2. 登录成功后跳转到首页
```

## 用户确认

```
需要Apple登录，登录成功后跳转到首页
```

## 需求分析师更新

```
[ui-forge] 需求分析师：需求收口完成
- 平台：iOS
- 页面：登录页
- 风格：现代风格
- 功能：手机号登录、密码输入、微信登录、Apple登录、注册入口
- 设计约束：渐变背景、遵循iOS规范、支持深色模式
- 确认状态：已确认
- 交接给：UI设计师
```

## UI设计师输出

```
[ui-forge] UI设计师：
- 设计方向：现代风格iOS登录页
- 风格选择：现代风格（渐变背景、卡片布局、圆角设计）
- 布局设计：
  ┌─────────────────────────────────────┐
  │           Logo + 应用名称            │
  │           应用标语                   │
  │                                     │
  │           ┌─────────────────────┐   │
  │           │ 请输入手机号         │   │
  │           └─────────────────────┘   │
  │           ┌─────────────────────┐   │
  │           │ 请输入密码           │   │
  │           └─────────────────────┘   │
  │           ┌─────────────────────┐   │
  │           │       登录          │   │
  │           └─────────────────────┘   │
  │                                     │
  │           ─── 其他登录方式 ───       │
  │                                     │
  │           ┌─────┐   ┌─────┐        │
  │           │微信 │   │Apple│        │
  │           └─────┘   └─────┘        │
  │                                     │
  │           还没有账号？立即注册       │
  └─────────────────────────────────────┘
- 组件设计：
  1. 输入框组件（手机号、密码）
  2. 按钮组件（登录按钮）
  3. 社交登录按钮（微信、Apple）
  4. 文字链接（注册入口）
- 细节设计：
  1. 颜色：渐变背景 #667eea → #764ba2
  2. 字体：SF Pro Display
  3. 间距：MD 16px
  4. 圆角：14px
  5. 阴影：中等阴影
- 交互设计：
  1. 输入框聚焦：边框变色
  2. 按钮悬停：上移2px
  3. 按钮点击：缩放动画
- 响应式设计：
  1. 移动端：全屏显示
  2. 平板：居中显示，最大宽度480px
  3. 桌面：居中显示，最大宽度420px
- 确认状态：待确认
```

## 用户确认

```
确认设计
```

## 输出文件

### index.html

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登录</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="style-modern">
    <div class="login-container">
        <div class="logo-section">
            <div class="logo"></div>
            <h1 class="app-name">MyApp</h1>
            <p class="app-slogan">让生活更简单</p>
        </div>

        <form class="login-form">
            <div class="input-group">
                <input type="tel" placeholder="请输入手机号" class="input-field">
            </div>
            <div class="input-group">
                <input type="password" placeholder="请输入密码" class="input-field">
            </div>
            <button type="submit" class="login-btn">登录</button>
        </form>

        <div class="divider"><span>其他登录方式</span></div>

        <div class="social-login">
            <button class="social-btn wechat">微信</button>
            <button class="social-btn apple">Apple</button>
        </div>

        <div class="register-section">
            <span>还没有账号？</span><a href="#">立即注册</a>
        </div>
    </div>
</body>
</html>
```

### style.css

```css
/* 样式文件见 templates/style.css */
```
