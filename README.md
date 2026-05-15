# UI Forge

GitHub: [lbyxunxunnini/ui-forge](https://github.com/lbyxunxunnini/ui-forge) · License: [MIT](LICENSE) · Version: `v0.1.3`

UI Forge is a UI design **controller** for App and Web work. It routes tasks through diagnose, design, and delivery modes automatically, manages question budgets, enforces output completeness, and produces structured HTML/CSS/SVG deliverables.

It is not a replacement for `polanyi-design`. `polanyi-design` is the judgment layer. UI Forge is the execution layer. The split is documented in [references/polanyi_integration.md](references/polanyi_integration.md).

## Entry Points

| Prefix | Mode | When to use |
|--------|------|-------------|
| `uif-` | Standard | Normal UI tasks, auto-route |
| `uif-fast` | Fast | Small tweaks: color, spacing, font, icon swap |
| `uif-a` | Autonomous | Full auto, fill gaps with assumptions |
| `uif-critique` | Critique | UI diagnosis only, no delivery |
| `uif-deliver` | Deliver | Explicit HTML/CSS/SVG/tokens/REQUIREMENTS |

Backward-compatible: `uid-`, `/ui-forge`, `/ui-design` still work.

## What It Does

- routes work into diagnose, design, deliver, fast, or autonomous mode
- uses question budgets (L1-L4) instead of defaulting to long requirement interviews
- separates requirement and UI roles with explicit confirmation gates
- manages project-level design cards for long-term UI rules
- produces structured outputs with completeness validation
- auto-exits after task completion (no persistent mode)

## Quick Start

- [QUICKSTART.md](QUICKSTART.md): 3-minute setup and usage
- [CHEATSHEET.md](CHEATSHEET.md): common tasks reference

## Core References

- [SKILL.md](SKILL.md): full workflow specification
- [CHANGELOG.md](CHANGELOG.md): release history
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution guide

Design workflow:

- [references/question_budget.md](references/question_budget.md)
- [references/evaluation_rubric.md](references/evaluation_rubric.md)
- [references/recipes.md](references/recipes.md)
- [references/design_card_protocol.md](references/design_card_protocol.md)
- [references/fast_mode.md](references/fast_mode.md)
- [references/autonomous_mode.md](references/autonomous_mode.md)

Operations:

- [references/release_playbook.md](references/release_playbook.md)
- [references/demo_transcript.md](references/demo_transcript.md)

Roles and gates:

- [references/roles/requirement_analyst.md](references/roles/requirement_analyst.md)
- [references/roles/ui_designer.md](references/roles/ui_designer.md)
- [references/shared_workflow_gates/role_gate_matrix.md](references/shared_workflow_gates/role_gate_matrix.md)

Polanyi integration:

- [references/polanyi_integration.md](references/polanyi_integration.md)

## Examples and Demos

- [examples/dashboard-critique.md](examples/dashboard-critique.md)
- [examples/login-example.md](examples/login-example.md)
- [demo/login-demo.html](demo/login-demo.html)
- [demo/home-demo.html](demo/home-demo.html)

## Scripts

- `scripts/project_snapshot.py` — scan project UI assets, output JSON summary
- `scripts/init_design_card.py` — generate design card draft from project assets
- `scripts/validate_design_card.py` — validate design card fields and formats
- `scripts/validate_output.py` — check design-output deliverable completeness
- `scripts/route_golden_tests.py` — verify prompt routing to correct mode
- `scripts/doctor.sh` — one-click project health check
- `scripts/validate_release.sh` — release gate (doctor + golden tests + version + changelog)

```bash
python3 scripts/project_snapshot.py                  # scan current project
python3 scripts/init_design_card.py                  # generate draft card
python3 scripts/validate_design_card.py <card.yaml>  # validate a card
python3 scripts/validate_output.py design-output/    # check deliverables
python3 scripts/route_golden_tests.py                # test routing
bash scripts/doctor.sh                               # health check
bash scripts/validate_release.sh                     # release gate
```

## Assets and Templates

- [templates/login.html](templates/login.html)
- [templates/home.html](templates/home.html)
- [templates/style.css](templates/style.css)
- [components/components.css](components/components.css)
- [config/design-config.json](config/design-config.json)

## Install

```bash
npx skills add lbyxunxunnini/ui-forge
```

Or clone manually:

```bash
git clone https://github.com/lbyxunxunnini/ui-forge ~/.claude/skills/ui-forge
```

## Version

Current: `v0.1.3`

`v0.1.3` adds mode reference docs: `fast_mode.md`, `autonomous_mode.md`, `release_playbook.md`, `demo_transcript.md` (7 real interaction demos).

`v0.1.2` added validation and release tooling. `v0.1.1` added design card automation. `v0.1.0` was the major restructuring.
