# Changelog

## [v0.2.0] - 2026-05-25

Task-driver 风格硬合同化 + 维护面收敛。

### Added

- `references/core_contracts.yaml` — 集中记录 global constitution、session 核心字段、gate 名称、角色边界、维护面分组
- `references/maintenance_map.md` — 维护导航，明确改阶段门禁、session 字段、角色边界、自动模式豁免、发布校验时的最小同步文件集合
- `references/load_map.md` — 核心入口与按问题加载导航
- `scripts/check_metadata.sh` / `check_guardrails.sh` / `check_session.sh` / `check_gates.sh` / `check_output_protocol.sh` — 发布校验模块

### Changed

- `SKILL.md` — 新增全局宪法式铁律、Design Task Brief、阶段放行条件、范围控制、失控处理、正常结束条件
- `SKILL.md` — `uif-a` 主流程改为“仅自动补齐低风险视觉默认值”，诊断流程标题去除旧专用触发词
- `references/task_runtime_prompt.md` — 增加 session 状态主表与交接前置条件
- `references/roles/requirement_analyst.md` — 改为“仅允许 / 明确禁止 / 违规后强制动作”的硬合同
- `references/roles/ui_designer.md` — 改为当前工作单元驱动的硬合同
- `references/roles/visual_reviewer.md` — 改为独立门禁硬合同
- `references/shared_workflow_gates/role_gate_matrix.md` — 改为 gate 合同风格，补 current_work_unit / exit_permission 约束
- `references/skill_visibility.md` — 改为输出可见性合同，禁止用完成话术掩盖阶段未闭合
- `QUICKSTART.md` / `CHEATSHEET.md` / `references/demo_transcript.md` — 移除旧触发词口径，统一为当前入口策略
- `scripts/route_golden_tests.py` — 删除旧入口兼容测试，统一为当前模式路由
- `scripts/doctor.sh` — 新增 core contracts 检查
- `scripts/validate_release.sh` — 从单体检查切为 metadata / guardrails / session / gates / output protocol 模块
- `README.md` — 新增维护入口与校验脚本导航

## [v0.1.9] - 2026-05-23

硬门禁体系与角色卡职责收口。

### Added

- SKILL.md：硬门禁 14-20 条（需求→设计阶段闸门、提问预算硬约束、视觉评分硬后果、迭代变更锁定、组件库硬门禁、方案决策闭合、禁止偷懒）
- references/roles/ui_designer.md：新增"先查再做"规则（设计前必须读取 design card、tokens.json、已输出页面、recipes.md）
- references/roles/ui_designer.md：新增方案确认回显机制（用户选择方案后回显要点，确认后锁定为设计基线）
- references/roles/ui_designer.md：新增迭代模式约束（迭代范围锁定为用户明确提出的变更项，禁止"顺便优化"）
- references/roles/visual_reviewer.md：新增降级交付流程（2轮修改后仍<20分的标准化通知格式）

### Changed

- SKILL.md：视觉质量基线从 SKILL.md 移入 ui_designer.md 和 visual_reviewer.md，消除跨文件重复
- SKILL.md：输出完整性检查清单精简为引用 ui_designer.md
- SKILL.md：追问模式精简为引用各角色卡，删除与角色卡重复的通用追问规则
- SKILL.md：角色体系补充"对外不展示全部角色，只在需要时出现"
- references/roles/requirement_analyst.md：预算规则从"够用即停"升级为硬约束（达到上限后 auto_assumption 填充，禁止继续追问）
- references/roles/requirement_analyst.md：自主决策范围细化定义（小变动/中等变动/巨大变动的具体标准）
- references/roles/requirement_analyst.md：向UI设计师交接格式从"需求收口完成"改为"需求确认单"（含功能清单、需求边界、异常处理方案，待用户确认后放行）
- references/roles/visual_reviewer.md：门禁阈值从百分比制简化为分数制（≥20放行/15-19返回/<15重设计）
- references/roles/visual_reviewer.md：硬约束强化（逐维度打分+扣分理由、最多2轮修改、2轮后<20降级交付）

## [v0.1.8] - 2026-05-21

Agent-pm 审查修复 + 最佳实践强化。

### Fixed

- `VERSION` 文件同步为 v0.1.7（此前落后于 .skillhub.json，doctor.sh 报 2 errors）
- `references/memory_protocol.md`：删除体系1段落的完整重复
- `references/shared_workflow_gates/role_gate_matrix.md`：放行条件补充"20-23 分标注需优化项"，与 SKILL.md 对齐

### Added

- SKILL.md：Iron Law 底线规则 — `NO DESIGN OUTPUT WITHOUT COMPLETENESS CHECKLIST PASSING FIRST`
- SKILL.md：Red Flags 自我欺骗预判表（6 条），覆盖跳过流程、省略检查、虚高评分等常见 rationalization
- SKILL.md：标准流程从 ASCII 转为 digraph 格式，含判断节点和 yes/no 分支

### Changed

- SKILL.md：frontmatter description 精简为纯触发条件，删除"手动触发后由 skill 内部决定执行路径"等工作流描述（BP-006）

## [v0.1.7] - 2026-05-21

Agent-pm 审查修复 + 迭代模式 + 触发词精简 + SKILL.md 精简。

### Added

- `references/iteration_mode.md` — 迭代模式：已完成项目的版本化迭代优化，完整流程+版本号确认+CHANGELOG/UI-CHANGELOG 变更追踪，文档同步更新规则（P0）
- `references/issue-ledger.md` — 问题台账，记录审查 issue 状态

### Changed

- SKILL.md：新增迭代流程（uif-iter），入口表和模式路由新增迭代模式
- SKILL.md：触发词精简——删除 `uif-critique`、`uif-deliver`、`uid-`、`/ui-design`
- SKILL.md：交付物展示规范 ASCII 图移到 output_structure.md，示例引用 QUICKSTART.md
- SKILL.md：consistency-report.md 从子清单提升到文件完整性主清单
- SKILL.md：routing.json 新增同步更新规则（后续新增页面必须同步更新路由表）
- SKILL.md：默认值规则统一为分级处理（核心需求必须确认，非核心默认值可告知）
- SKILL.md：视觉质量门禁流程补充 L 级别审查轮次（L1/L2 1轮，L3/L4 1-2轮）
- README.md：入口表同步更新，新增迭代模式，删除已移除触发词
- references/input_incomplete_handling.md：默认值规则同步为分级处理
- references/skill_visibility.md：默认值规则同步为分级处理
- references/roles/visual_reviewer.md：门禁规则补充"单维度一票否决"
- references/roles/ui_designer.md：路由表规则补充同步更新说明
- references/output_structure.md：新增画廊展示规范（从 SKILL.md 移入）
- .skillhub.json：版本号更新，描述同步删除已移除触发词

## [v0.1.6] - 2026-05-20

Agent-pm 审查：视觉质量门禁与交付物展示规范强化。

### Added

- `references/roles/visual_reviewer.md` — 视觉审查师角色卡：6维度/30分评分体系（视觉丰富度/信息层次/组件精致度/色彩节奏/功能闭环/文稿精度），门禁阈值（≥24放行/15-23返回/<15重设计），Polanyi调用规则，修改轮次限制
- `references/shared_workflow_gates/visual_quality_gate.md` — 视觉质量门禁：触发条件、评分维度权重、单维度一票否决规则、与交付阶段的关系
- SKILL.md：新增视觉质量基线（丰富度/层次/精致度/色彩 4维度检查清单）
- SKILL.md：新增画廊展示规范（所有页面平铺展示、模块分组、手机mockup、待实现占位）
- SKILL.md：强化输出完整性检查清单（+功能闭环检查、+组件完整性检查、+记忆结构检查）
- SKILL.md：角色体系新增视觉审查师（UI设计师和交付工程师之间的质量审查节点）
- references/evaluation_rubric.md：新增评分示例和视觉质量附加评估（6维度/30分）
- references/output_structure.md：新增DESIGN-GUIDE.md详细模板（逐元素标注要求）
- references/roles/ui_designer.md：新增视觉质量基线要求（丰富度/层次/精致度/色彩）
- references/memory_protocol.md：新增迭代记忆检查点（设计决策锁定、变更影响追踪、迭代一致性验证）

### Changed

- SKILL.md：交付物展示规范从iframe手机切换改为画廊平铺布局
- SKILL.md：核心流程新增视觉审查师评分步骤
- references/shared_workflow_gates/role_gate_matrix.md：新增视觉审查师门禁，交付阶段门禁更新为"视觉质量门禁通过后才允许进入"
- README.md：新增视觉审查师和视觉质量门禁的链接

## [v0.1.5] - 2026-05-17

脚本可执行权限修复与 doctor.sh 覆盖扩展。

### Fixed

- scripts/ 全部脚本添加可执行权限（chmod +x）
- doctor.sh REF_FILES 从 12 项扩展到 23 项，覆盖全部 references 文档
- doctor.sh SCRIPTS 数组新增 validate_release.sh

## [v0.1.4] - 2026-05-17

Agent-pm 审查：规则一致性与模式感知行为修复。

### Fixed

- SKILL.md："不要假装理解"改为模式感知规则（标准模式追问、fast 模式升级确认、autonomous 模式标注假设）
- SKILL.md：L2/L3 路由边界补充具体示例（登录页→L2、仪表盘→L3、电商首页→L3、设计系统→L4）
- SKILL.md：快速模式触发条件引用 fast_mode.md
- SKILL.md：设计系统锁定触发条件统一为第3页（此前多处不一致为"第1页"）
- SKILL.md：组件库抽取触发条件统一为"跨会话累计3个页面"
- SKILL.md：移除重复规则（"禁止只问视觉细节"、"每轮只问1个问题"、"任务完成即退出"）
- SKILL.md：引用列表补充 skill_visibility.md
- autonomous_mode.md：示例不再自动补齐交互决策（原"toast 提示"改为视觉参数）
- discussion_mechanism.md：4轮上限后增加升级路径（UI设计师可标注风险但必须执行）
- escalation_mechanism.md：明确返回机制（2次）与讨论回合（4轮）独立计数
- input_incomplete_handling.md：增加用户拒绝提供信息时的降级策略（切换到 autonomous 模式）
- fast_mode.md：增加最小输出集（style.css + tokens.json，不需要 REQUIREMENTS.md）
- requirement_analyst.md：同步模式感知的"不要假装理解"规则
- ui_designer.md：同步设计系统锁定触发条件和组件库抽取触发条件
- memory_protocol.md：同步设计系统锁定触发条件和组件库抽取触发条件

## [v0.1.3] - 2026-05-15

Mode reference documentation.

### Added

- `references/fast_mode.md` — fast mode rules, trigger conditions, adjustment types, fallback protocol
- `references/autonomous_mode.md` — auto mode rules, auto_assumption mechanism, high-risk confirmation triggers, default values
- `references/release_playbook.md` — version rules, release checklist, release steps, hotfix flow, doc sync checks
- `references/demo_transcript.md` — 7 real interaction demos: standard design, fast tweak, critique, autonomous, delivery, design system, memory recovery

### Changed

- SKILL.md: added fast_mode.md and autonomous_mode.md to references section
- README.md: added mode docs and operations docs to core references

## [v0.1.2] - 2026-05-15

Validation and release tooling.

### Added

- `scripts/validate_output.py` — check design-output deliverable completeness (index.html, style.css, tokens.json, icons, REQUIREMENTS.md, responsive breakpoints, validation states)
- `scripts/route_golden_tests.py` — 17 golden test cases verifying prompt routing to correct mode (standard/fast/autonomous/critique/deliver) and budget (L1-L4)
- `scripts/doctor.sh` — one-click health check: version consistency, core files, references, scripts, design output
- `scripts/validate_release.sh` — release gate: doctor + golden tests + version format + CHANGELOG entry + SKILL.md frontmatter + git status

### Fixed

- macOS sed compatibility in release validation
- Chinese tweak routing: "把...改成..." patterns now correctly route to fast mode

## [v0.1.1] - 2026-05-15

Design card automation scripts.

### Added

- `scripts/project_snapshot.py` — scan project UI assets (design-output, .design-doc, templates, components, config, screenshots, colors, fonts, tokens)
- `scripts/init_design_card.py` — generate design card draft from project assets, auto-detect project type/platform/colors/fonts/components
- `scripts/validate_design_card.py` — validate design card fields (required sections, hex colors, CSS units, accessibility ratios, enum values)

### Changed

- `project.type` normalization: "mobile"/"ios"/"android" → "app" in design card generation

## [v0.1.0] - 2026-05-15

Major restructuring: from design process document to UI design controller.
