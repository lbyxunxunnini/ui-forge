# Issue Ledger

## 2026-05-20 审查

| Issue ID | 级别 | 状态 | 描述 |
|----------|------|------|------|
| APM-LOGIC-001 | P1 | fixed | 默认值规则冲突：SKILL.md 允许告知，reference 文件禁止自动补。修复为分级处理（核心需求确认，非核心告知） |
| APM-LOGIC-002 | P1 | fixed | SKILL.md 门禁流程未区分 L1/L2 和 L3/L4 审查轮次。补充了 L 级别审查轮次说明 |
| APM-LOGIC-003 | P1 | fixed | visual_reviewer.md 缺少"单维度一票否决"规则。已补充 |
| APM-DESIGN-001 | P2 | fixed | SKILL.md 655 行超 500 行阈值。精简至 500 行，功能流程不变 |

## 2026-05-21 审查

| Issue ID | 级别 | 状态 | 描述 |
|----------|------|------|------|
| APM-CONSISTENCY-001 | P1 | fixed | VERSION 文件未同步 v0.1.7，doctor.sh 报 2 errors。已更新 VERSION 为 v0.1.7 |
| APM-WORKFLOW-002 | P1 | fixed | memory_protocol.md 体系1段落完整重复。已删除重复段落 |
| APM-WORKFLOW-003 | P1 | fixed | role_gate_matrix.md 放行条件缺少"20-23 分标注需优化项"区分。已补充 |
| APM-LOGIC-004 | P2 | deferred | 迭代模式下视觉审查师"对比新旧版本"缺操作定义（visual_reviewer.md 无迭代规则） |
| APM-LOGIC-005 | P2 | deferred | 设计系统锁定时机 SKILL.md 说"设计完成后"，memory_protocol.md 说"用户确认后"，时序不一致 |
| APM-DESIGN-006 | P2 | deferred | 角色输出规则在 SKILL.md、skill_visibility.md、task_runtime_prompt.md 三处重复定义 |
| APM-DESIGN-007 | P2 | deferred | SKILL.md 447 行接近 500 行阈值，持续关注 |
| APM-BP-008 | P2 | fixed | Description 字段含工作流描述，违反 BP-006。已精简为纯触发条件 |
| APM-BP-009 | P2 | fixed | 缺少 Iron Law 底线规则。已添加 "NO DESIGN OUTPUT WITHOUT COMPLETENESS CHECKLIST PASSING FIRST" |
| APM-BP-010 | P2 | fixed | 缺少 Red Flags 自我欺骗预判表。已添加 6 条 Red Flags |
| APM-BP-011 | P3 | fixed | 流程图未使用 digraph 格式。标准流程已转为 digraph 含判断节点和分支 |

## Backlog

- APM-LOGIC-004: 迭代模式视觉审查缺操作定义
- APM-LOGIC-005: 设计系统锁定时机不一致
- APM-DESIGN-006: 角色输出规则重复定义
- APM-DESIGN-007: SKILL.md 行数监控
