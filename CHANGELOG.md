# Changelog

## [0.1.2] - 2026-05-14

触发机制修复

- 重写 SKILL.md frontmatter description：加入硬触发关键词变体（`uif -`/`uif `/`uid -`）、强制调用规则、防误判规则
- 精简 SKILL.md：删除正文重复的触发列表（硬触发、语义触发、示例表达）

## [0.1.1] - 2026-05-14

### Changed

- 重写公开 README，删除重复说明和失效展示内容
- 为仓库内关键文档、示例、Demo 和资源补齐可点击链接
- 统一公开版本元数据到 `0.1.1`

## [0.1.0] - 2026-05-14

### Added

- 新增 `polanyi_integration.md`，明确 UI Forge 与 `polanyi-design` 的分工和接入方式
- 新增 `recipes.md`，收口重设计、后台、登录流、设计系统和评审模式的常用流程
- 新增 `evaluation_rubric.md`，用于对比普通 UI prompt 与 UI Forge 的输出质量
- 新增在线预览 Demo（登录页、首页）
- 新增 LICENSE、CONTRIBUTING 和截图目录规范

### Changed

- 项目正式从 `ui-design` / `ui-design-skill` 收口为 `ui-forge`
- 兼容旧触发词 `uid-` 和 `/ui-design`
- 更新 README 和 skill 描述，明确本项目是设计工作流层而不是单纯审美判断层
- 合并此前未发布的 1.x 内部迭代记录，统一收口为首个公开版本 `0.1.0`
