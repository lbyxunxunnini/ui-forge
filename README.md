# UI Forge

GitHub: [lbyxunxunnini/ui-forge](https://github.com/lbyxunxunnini/ui-forge) · License: [MIT](LICENSE) · Version: `v0.1.4`

UI Forge 是面向 App 和 Web 的 UI 设计 **controller**。自动将任务路由到诊断、设计、交付模式，管理提问预算，强制输出完整性，产出结构化的 HTML/CSS/SVG 交付物。

它不是 `polanyi-design` 的替代品。`polanyi-design` 是审美判断层，UI Forge 是执行层。分层说明见 [references/polanyi_integration.md](references/polanyi_integration.md)。

## 入口

| 前缀 | 模式 | 使用场景 |
|------|------|----------|
| `uif-` | 标准 | 常规 UI 任务，自动路由 |
| `uif-fast` | 快速 | 小调整：颜色、间距、字体、图标替换 |
| `uif-a` | 全自动 | 全自动执行，缺失信息用推荐方案补齐 |
| `uif-critique` | 诊断 | 仅做 UI 诊断，不进入交付 |
| `uif-deliver` | 交付 | 明确要 HTML/CSS/SVG/tokens/REQUIREMENTS 输出 |

向后兼容：`uid-`、`/ui-forge`、`/ui-design` 仍可用。

## 功能

- 将任务自动路由到诊断、设计、交付、快速或全自动模式
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

运维：

- [references/release_playbook.md](references/release_playbook.md)
- [references/demo_transcript.md](references/demo_transcript.md)

角色与门禁：

- [references/roles/requirement_analyst.md](references/roles/requirement_analyst.md)
- [references/roles/ui_designer.md](references/roles/ui_designer.md)
- [references/shared_workflow_gates/role_gate_matrix.md](references/shared_workflow_gates/role_gate_matrix.md)

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
- `scripts/validate_release.sh` — 发布门禁（doctor + golden tests + 版本 + changelog）

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

当前版本：`v0.1.4`

`v0.1.4` agent-pm 审查修复：统一设计系统锁定触发条件为第3页、"不要假装理解"改为模式感知规则、L2/L3 路由补充边界示例、明确讨论升级路径和返回/讨论回合关系、增加用户拒绝提供信息的降级策略、移除跨文件重复规则。

`v0.1.3` 新增模式参考文档：`fast_mode.md`、`autonomous_mode.md`、`release_playbook.md`、`demo_transcript.md`（7 个真实交互示例）。

`v0.1.2` 新增校验和发布工具。`v0.1.1` 新增设计规则卡自动化。`v0.1.0` 为主结构重构版本。
