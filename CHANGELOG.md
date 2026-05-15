# Changelog

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

### Added

- Entry points: `uif-fast` (quick tweaks), `uif-a` (autonomous), `uif-critique` (diagnosis only), `uif-deliver` (explicit output)
- Design card protocol: `.ui-forge/projects/<project>.design_card.yaml` for long-term project UI rules
- Project isolation: forbid reading other projects' design memory or outputs
- QUICKSTART.md: 3-minute setup guide
- CHEATSHEET.md: common tasks reference
- Controller role: internal routing, budget, escalation management
- UX designer and delivery engineer as internal roles (auto-dispatched, not shown to user)
- Task-scoped sessions: auto-exit after task completion

### Changed

- **Removed persistent mode**: skill no longer stays active across turns; one task = one session
- SKILL.md rewritten as controller specification instead of process document
- README.md restructured around 5 entry points
- Version scheme switched to `v` prefix (v0.1.0), isolating from pre-restructuring history
- Role system expanded: 2 visible roles (requirement analyst, UI designer) + 4 internal roles (controller, UX designer, delivery engineer, verification engineer)

### Fixed

- Version inconsistency: README showed 0.1.2 while VERSION/.skillhub showed 0.1.3
- Conflicting rules: persistent mode vs task-scoped behavior

---

## Pre-v0.1.0 History

<details>
<summary>Internal iterations (0.1.0 - 0.1.3)</summary>

### [0.1.3] - 2026-05-15

格式对齐与逻辑修复

- Description 精简为 3 行，与 flutter-forge/h5-forge 格式统一
- 修复"禁止只给一个方案"与 L1/L2 规则的矛盾
- 统一全项目"UI设计师"命名

### [0.1.2] - 2026-05-14

触发机制修复

- 重写 SKILL.md frontmatter description
- 精简 SKILL.md

### [0.1.1] - 2026-05-14

- 重写公开 README
- 补齐可点击链接
- 统一版本元数据

### [0.1.0] - 2026-05-14

- 新增 polanyi_integration.md、recipes.md、evaluation_rubric.md
- 新增在线预览 Demo
- 项目正式收口为 ui-forge

</details>
