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

## 2026-06-11 修复

| Issue ID | 级别 | 状态 | 描述 |
|----------|------|------|------|
| APM-WORKFLOW-004 | P1 | fixed | 视觉审查通过后可能直接进入交付，绕过用户确认。已统一视觉门禁、视觉审查师和交付 Gate：评分通过只进入用户确认，用户确认后才可交付 |
| APM-LOGIC-006 | P1 | fixed | 用户拒绝回答核心信息时可能被 autonomous 推荐方案自动补齐。已改为区分低风险默认值与核心字段，核心字段持续拒答时保持候选未确认，不得完整设计或交付 |
| APM-OUTPUT-001 | P2 | fixed | 用户可见交付清单遗漏 tokens.json 与 REQUIREMENTS.md。已补齐必备文件，并补充 3+ 页面 routing.json / consistency-report.md 条件项 |
| APM-LOGIC-004 | P2 | fixed | 迭代模式视觉审查缺少角色卡级操作定义。已在 visual_reviewer.md 增加迭代对比、变更点和回归检查输出字段 |
| APM-LOGIC-005 | P2 | fixed | 设计系统锁定时机措辞不一致。已统一为第3个页面设计完成并经用户确认后锁定 tokens.json |
| APM-DESIGN-006 | P2 | fixed | 角色输出规则在多处重复定义。已将运行时提示和 SKILL 主文件收敛为引用 skill_visibility.md 的简短硬约束 |
| APM-DESIGN-007 | P2 | fixed | SKILL.md 行数监控。已将 SKILL.md 从 456 行降至 446 行，继续保持在 500 行阈值以内 |

## 2026-06-11 产品评审改进

| Issue ID | 级别 | 状态 | 描述 |
|----------|------|------|------|
| APM-GOV-001 | P2 | fixed | 模型或运行环境不一定具备视觉理解能力，截图/图片/画布不可读时缺少独立降级策略。已新增 Visual Understanding Fallback，并同步 SKILL、输入处理、UI设计师、视觉审查师、视觉门禁和 load map |

## Backlog

暂无。
