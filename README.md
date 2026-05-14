# UI Forge

GitHub: [lbyxunxunnini/ui-forge](https://github.com/lbyxunxunnini/ui-forge) · License: [MIT](LICENSE) · Current version: `0.1.2`

UI Forge is a UI design workflow skill for App and Web work. It is meant for tasks that need to move from requirement clarification into structure, visual direction, interaction states, and delivery artifacts such as HTML/CSS/SVG or design tokens.

It is not a replacement for `polanyi-design`. `polanyi-design` is the judgment layer. UI Forge is the execution layer. The split is documented in [references/polanyi_integration.md](references/polanyi_integration.md).

## Use It For

- new page design
- redesign and UI critique
- design system alignment
- interaction spec and frontend handoff
- generating structured design outputs instead of loose suggestions

## What It Does

- routes work into `diagnose`, `design`, or `delivery` mode
- uses question budgets instead of defaulting to long requirement interviews
- separates requirement and UI roles with explicit confirmation gates
- can continue from existing design context instead of restarting from scratch
- produces structured outputs, not only aesthetic commentary

Key workflow references:

- [SKILL.md](SKILL.md)
- [references/question_budget.md](references/question_budget.md)
- [references/evaluation_rubric.md](references/evaluation_rubric.md)
- [references/recipes.md](references/recipes.md)

## Trigger Examples

Typical prompts:

```text
/ui-forge redesign this dashboard and explain why it feels templated
use ui-forge to design an iOS settings page in dark mode
uif- create a web login page and include HTML/CSS output
uid- help me tighten a design system for forms and action bars
```

Backward-compatible triggers still supported:

- `uif-`
- `uid-`
- `/ui-forge`
- `/ui-design`

## Output Modes

`Diagnose`

- critique an existing UI
- identify structure, hierarchy, state, and visual issues
- recommend concrete fixes

`Design`

- clarify requirements
- propose layout, components, and interaction states
- tighten direction before implementation

`Delivery`

- output HTML/CSS/SVG, tokens, and handoff structure
- package the result in a stable format for frontend use

Related references:

- [references/output_structure.md](references/output_structure.md)
- [references/design_tokens.md](references/design_tokens.md)
- [references/design_styles.md](references/design_styles.md)

## Repository Guide

Start here:

- [SKILL.md](SKILL.md): main workflow
- [CHANGELOG.md](CHANGELOG.md): release history
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution guide

Examples and demos:

- [examples/dashboard-critique.md](examples/dashboard-critique.md)
- [examples/login-example.md](examples/login-example.md)
- [demo/index.html](demo/index.html)
- [demo/login-demo.html](demo/login-demo.html)
- [demo/home-demo.html](demo/home-demo.html)

Core references:

- [references/polanyi_integration.md](references/polanyi_integration.md)
- [references/recipes.md](references/recipes.md)
- [references/question_budget.md](references/question_budget.md)
- [references/memory_protocol.md](references/memory_protocol.md)

Assets and templates:

- [templates/login.html](templates/login.html)
- [templates/home.html](templates/home.html)
- [templates/style.css](templates/style.css)
- [components/components.css](components/components.css)
- [config/design-config.json](config/design-config.json)

Validation:

- [tests/test-cases.md](tests/test-cases.md)
- [screenshots/README.md](screenshots/README.md)

## Install

If your tool supports skill repos directly, install from GitHub:

```bash
npx skills add lbyxunxunnini/ui-forge
```

Manual install is also fine. Clone the repo into your tool's skill directory, for example:

```bash
git clone https://github.com/lbyxunxunnini/ui-forge ~/.claude/skills/ui-forge
```

## Version

Current version: `0.1.3`

`0.1.3` aligns description format with flutter-forge/h5-forge (3-line structure), fixes logical contradictions (L1/L2 vs prohibition rules), corrects role names, adds missing reference links, and standardizes "UI设计师" naming across all files.
