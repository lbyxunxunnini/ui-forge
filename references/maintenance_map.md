# Maintenance Map

`ui-forge` 的维护优先看“改动落在哪个维护面”，不要只改一个文件。

## 1. 阶段门禁

当你修改以下任一内容时，至少同步检查这些文件：

- 阶段顺序、放行条件、回退规则
- 需求确认与是否允许进入下一阶段
- 结束条件与是否允许退出

最小同步集合：

- `SKILL.md`
- `references/shared_workflow_gates/requirement_confirmation.md`
- `references/shared_workflow_gates/role_gate_matrix.md`
- `references/core_contracts.yaml`

## 2. Session / Runtime 状态

当你新增“当前任务必须记住什么”时，先改 session 主表，再改运行时提示。

最小同步集合：

- `references/core_contracts.yaml`
- `references/task_runtime_prompt.md`
- `SKILL.md`

重点字段：

- `goal_state`
- `scope_state`
- `acceptance_state`
- `constraints_state`
- `current_work_unit`
- `work_unit_state`
- `verification_state`
- `scope_risk`
- `plan_conflict_state`
- `mode_lock`
- `exit_permission`

## 3. 角色边界

当你修改需求分析师、UI设计师、视觉审查师的权限边界时，必须保持“谁能做 / 谁不能做 / 违规后怎么处理”一致。

最小同步集合：

- `references/roles/requirement_analyst.md`
- `references/roles/ui_designer.md`
- `references/roles/visual_reviewer.md`
- `references/core_contracts.yaml`
- `references/task_runtime_prompt.md`

## 4. 自动模式豁免

当你允许 `uif-a` 更少提问时，先确认这是不是低风险默认值，而不是产品方向决策。

最小同步集合：

- `references/autonomous_mode.md`
- `references/input_incomplete_handling.md`
- `references/core_contracts.yaml`
- `SKILL.md`

## 5. 发布校验

当你新增合同、门禁、运行时字段或关键协议时，必须同步发布校验，否则规则只写在文档里，无法执法。

最小同步集合：

- `scripts/doctor.sh`
- `scripts/validate_release.sh`
- `scripts/check_metadata.sh`
- `scripts/check_guardrails.sh`
- `scripts/check_session.sh`
- `scripts/check_gates.sh`
- `scripts/check_output_protocol.sh`

## 6. 建议维护顺序

1. 先改 `references/core_contracts.yaml`
2. 再改 `SKILL.md` 与相关 reference
3. 再改角色卡
4. 最后补发布校验与 README 导航

如果只改某个子文档而不改主表，后续大概率再次分叉。
