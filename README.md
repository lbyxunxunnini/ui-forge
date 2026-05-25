# UI Forge

GitHub: [lbyxunxunnini/ui-forge](https://github.com/lbyxunxunnini/ui-forge) · License: [MIT](LICENSE) · Version: `v0.2.0`

UI Forge 是面向 App 和 Web 的 UI 设计 **controller**。自动将任务路由到诊断、设计、交付模式，管理提问预算，强制输出完整性，产出结构化的 HTML/CSS/SVG 交付物。

它不是 `polanyi-design` 的替代品。`polanyi-design` 是审美判断层，UI Forge 是执行层。分层说明见 [references/polanyi_integration.md](references/polanyi_integration.md)。

## 入口

| 前缀 | 模式 | 使用场景 |
|------|------|----------|
| `uif-` | 标准 | 常规 UI 任务，自动路由 |
| `uif-fast` | 快速 | 小调整：颜色、间距、字体、图标替换 |
| `uif-a` | 全自动 | 仅自动补齐低风险视觉默认值，核心方向必须确认 |
| `uif-iter` | 迭代 | 已完成项目的版本化迭代优化 |

其他触发：`/ui-forge`、`使用 ui-forge`、`调用 ui-forge`、`按 ui-forge 工作模式处理`。

## 功能

- 将任务自动路由到诊断、设计、交付、快速、全自动或迭代模式
- 用提问预算（L1-L4）替代默认的长流程需求访谈
- 分离需求分析师和 UI 设计师角色，带明确的确认门禁
- 管理项目级设计规则卡（design card），维护长期 UI 规则
- 产出结构化输出，带完整性校验
- 任务完成自动退出（不常驻模式）

## 快速开始

- [QUICKSTART.md](QUICKSTART.md)：3 分钟上手
- [CHEATSHEET.md](CHEATSHEET.md)：常用任务速查

## 核心文档

- [SKILL.md](SKILL.md)：完整工作流规范
- [CHANGELOG.md](CHANGELOG.md)：版本历史
- [CONTRIBUTING.md](CONTRIBUTING.md)：贡献指南

设计工作流：

- [references/question_budget.md](references/question_budget.md)
- [references/evaluation_rubric.md](references/evaluation_rubric.md)
- [references/recipes.md](references/recipes.md)
- [references/design_card_protocol.md](references/design_card_protocol.md)
- [references/fast_mode.md](references/fast_mode.md)
- [references/autonomous_mode.md](references/autonomous_mode.md)
- [references/iteration_mode.md](references/iteration_mode.md)

运维：

- [references/release_playbook.md](references/release_playbook.md)
- [references/demo_transcript.md](references/demo_transcript.md)
- [references/core_contracts.yaml](references/core_contracts.yaml)
- [references/maintenance_map.md](references/maintenance_map.md)
- [references/load_map.md](references/load_map.md)

角色与门禁：

- [references/roles/requirement_analyst.md](references/roles/requirement_analyst.md)
- [references/roles/ui_designer.md](references/roles/ui_designer.md)
- [references/roles/visual_reviewer.md](references/roles/visual_reviewer.md)
- [references/shared_workflow_gates/role_gate_matrix.md](references/shared_workflow_gates/role_gate_matrix.md)
- [references/shared_workflow_gates/visual_quality_gate.md](references/shared_workflow_gates/visual_quality_gate.md)

Polanyi 集成：

- [references/polanyi_integration.md](references/polanyi_integration.md)

## 示例与 Demo

- [examples/dashboard-critique.md](examples/dashboard-critique.md)
- [examples/login-example.md](examples/login-example.md)
- [demo/login-demo.html](demo/login-demo.html)
- [demo/home-demo.html](demo/home-demo.html)

## 脚本

- `scripts/project_snapshot.py` — 扫描项目 UI 资产，输出 JSON 摘要
- `scripts/init_design_card.py` — 从项目资产生成设计规则卡草稿
- `scripts/validate_design_card.py` — 校验设计规则卡字段和格式
- `scripts/validate_output.py` — 检查 design-output 交付物完整性
- `scripts/route_golden_tests.py` — 验证 prompt 路由到正确模式
- `scripts/doctor.sh` — 一键项目健康检查
- `scripts/validate_release.sh` — 发布门禁（doctor + golden tests + metadata / guardrails / session / gates / output protocol）
- `scripts/check_metadata.sh` — 元数据一致性检查
- `scripts/check_guardrails.sh` — 主规则与失控处理检查
- `scripts/check_session.sh` — session 字段与运行时提示检查
- `scripts/check_gates.sh` — 阶段门禁与主表同步检查
- `scripts/check_output_protocol.sh` — 输出协议关键项检查

```bash
python3 scripts/project_snapshot.py                  # 扫描当前项目
python3 scripts/init_design_card.py                  # 生成设计规则卡草稿
python3 scripts/validate_design_card.py <card.yaml>  # 校验设计规则卡
python3 scripts/validate_output.py design-output/    # 检查交付物
python3 scripts/route_golden_tests.py                # 测试路由
bash scripts/doctor.sh                               # 健康检查
bash scripts/validate_release.sh                     # 发布门禁
```

## 资产与模板

- [templates/login.html](templates/login.html)
- [templates/home.html](templates/home.html)
- [templates/style.css](templates/style.css)
- [components/components.css](components/components.css)
- [config/design-config.json](config/design-config.json)

## 安装

```bash
npx skills add lbyxunxunnini/ui-forge
```

或手动克隆：

```bash
git clone https://github.com/lbyxunxunnini/ui-forge ~/.claude/skills/ui-forge
```

## 版本

当前版本：`v0.2.0`

`v0.2.0` task-driver 风格强门禁闭环 + 维护面收敛：新增全局宪法式铁律、Design Task Brief、失控回退和正常结束条件；新增 core_contracts/maintenance_map/load_map 维护主表；三张角色卡、gate matrix、skill visibility 统一为硬合同风格；自动模式收紧为仅允许低风险视觉默认值；发布校验拆分为 metadata / guardrails / session / gates / output protocol 模块；同步清理旧触发词口径与路由测试。

`v0.1.9` 硬门禁体系与角色卡职责收口：SKILL.md 新增 7 条硬门禁（需求确认闸门、提问预算硬约束、视觉评分硬后果、迭代变更锁定、组件库硬门禁、方案决策闭合、禁止偷懒）；视觉质量基线、检查清单、追问模式从 SKILL.md 移入各角色卡，消除跨文件重复；需求分析师预算规则升级为硬约束+auto_assumption；UI设计师新增先查再做、方案确认回显、迭代约束；视觉审查师门禁阈值简化、评分硬约束、降级交付流程。

`v0.1.8` agent-pm 审查修复 + 最佳实践强化：版本号一致性修复、memory_protocol 去重、role_gate_matrix 放行条件对齐、添加 Iron Law 底线规则、添加 Red Flags 自我欺骗预判表、标准流程 digraph 化、description 字段精简为纯触发条件。

`v0.1.7` agent-pm 审查修复 + 迭代模式：默认值分级规则统一、门禁审查轮次区分、一票否决规则补充、SKILL.md 精简至 446 行、触发词精简、新增迭代模式（uif-iter）、routing.json 同步规则、consistency-report.md 提升为必出产物。

`v0.1.6` agent-pm 审查：新增视觉审查师角色（6维度/30分评分）、视觉质量门禁、画廊展示规范、强化输出完整性检查清单、迭代记忆检查点。

`v0.1.5` 脚本可执行权限修复、doctor.sh 参考文档覆盖扩展。

`v0.1.4` agent-pm 审查修复：统一设计系统锁定触发条件为第3页、"不要假装理解"改为模式感知规则、L2/L3 路由补充边界示例、明确讨论升级路径和返回/讨论回合关系、增加用户拒绝提供信息的降级策略、移除跨文件重复规则。

`v0.1.3` 新增模式参考文档：`fast_mode.md`、`autonomous_mode.md`、`release_playbook.md`、`demo_transcript.md`（7 个真实交互示例）。

`v0.1.2` 新增校验和发布工具。`v0.1.1` 新增设计规则卡自动化。`v0.1.0` 为主结构重构版本。
