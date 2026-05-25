# Load Map

按需加载，不要一次读完所有文档。

## 核心入口

- `SKILL.md`：主流程、铁律、阶段门禁
- `references/core_contracts.yaml`：session 字段、gate 名称、角色边界主表
- `references/maintenance_map.md`：改动时最小同步文件集合

## 按问题加载

- 需求收口 / 能否进入下一阶段：
  - `references/shared_workflow_gates/requirement_confirmation.md`
  - `references/roles/requirement_analyst.md`

- 设计展开 / 页面与组件闭环：
  - `references/roles/ui_designer.md`
  - `references/question_budget.md`

- 视觉放行 / 是否可交付：
  - `references/roles/visual_reviewer.md`
  - `references/shared_workflow_gates/role_gate_matrix.md`
  - `references/shared_workflow_gates/visual_quality_gate.md`

- 自动模式 / 是否允许补齐：
  - `references/autonomous_mode.md`
  - `references/input_incomplete_handling.md`

- 运行时输出与状态恢复：
  - `references/task_runtime_prompt.md`

- 发布与自检：
  - `scripts/doctor.sh`
  - `scripts/validate_release.sh`
