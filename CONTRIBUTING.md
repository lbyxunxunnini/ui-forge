# 贡献指南

感谢你对 UI Forge 的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告 Bug

1. 在 Issue 中创建一个 Bug Report
2. 描述问题的详细信息
3. 提供复现步骤
4. 附上截图或日志（如有）

### 提交新功能

1. 在 Issue 中创建一个 Feature Request
2. 描述功能的用途和场景
3. 等待维护者确认后再开始开发

### 提交代码

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建一个 Pull Request

## 开发规范

### 文件结构

```
ui-forge/
├── SKILL.md              # 核心内容（不要轻易修改）
├── references/           # 参考文档
├── templates/            # 页面模板
├── components/           # 组件库
├── config/               # 配置文件
├── examples/             # 示例
└── tests/                # 测试用例
```

### 文档规范

- 使用中文编写文档
- 保持 Markdown 格式清晰
- 代码示例需要可运行

### 测试用例

- 每个新功能需要附带测试用例
- 测试用例放在 `tests/` 目录
- 格式参考 `tests/test-cases.md`

## 提交 Pull Request

### PR 标题

使用清晰的标题描述你的更改，例如：
- `feat: 添加新的设计风格`
- `fix: 修复登录页样式问题`
- `docs: 更新 README 文档`

### PR 描述

请在描述中包含：
1. 更改内容概述
2. 更改原因
3. 测试方法
4. 截图（如适用）

## 代码审查

所有 PR 需要经过维护者审查。审查重点：
- 代码质量
- 文档完整性
- 向后兼容性
- 是否符合项目规范

## 行为准则

- 尊重每一位贡献者
- 接受建设性的批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同理心

## 问题反馈

如有任何问题，请通过 Issue 联系我们。

感谢你的贡献！
