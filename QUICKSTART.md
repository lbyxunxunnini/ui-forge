# Quick Start

## 30-Second Setup

If your tool supports skill repos:
```bash
npx skills add lbyxunxunnini/ui-forge
```

Or clone manually:
```bash
git clone https://github.com/lbyxunxunnini/ui-forge ~/.claude/skills/ui-forge
```

## 3-Minute Usage

### 1. Standard Design Task

```
uif- design a modern login page for iOS
```

UI Forge auto-routes to the right mode (diagnose/design/deliver) and asks questions based on complexity. Answer each question, get your design.

### 2. Quick Fix

```
uif-fast change the button border radius to 8px
```

No interview. Direct fix. Done.

### 3. Full Auto

```
uif-a design a dark mode settings page
```

Makes reasonable assumptions. Only asks for high-risk decisions. Outputs complete design.

### 4. Just Critique

```
uif-critique what's wrong with this dashboard?
```

Diagnosis and recommendations only. No HTML/CSS unless you ask for it.

### 5. Explicit Delivery

```
uif-deliver give me the HTML/CSS/SVG for the login page
```

Outputs complete handoff package: HTML, CSS, tokens, icons, REQUIREMENTS.

## What You Get

Every delivery includes:
- `index.html` — open in browser to preview
- `style.css` — standalone stylesheet
- `tokens.json` — design tokens
- `icons/` — all SVG icons
- `DESIGN-GUIDE.md` — visual specification
- `REQUIREMENTS.md` — interaction specification for code generation

## Project Design Card

For multi-page projects, create a design card to lock in project-wide rules:

```bash
# Auto-generated on first design, or create manually
.ui-forge/projects/<project>.design_card.yaml
```

Stores: brand voice, visual language, layout rules, component rules, accessibility requirements.

## Learn More

- [CHEATSHEET.md](CHEATSHEET.md) — common tasks reference
- [SKILL.md](SKILL.md) — full workflow specification
- [CHANGELOG.md](CHANGELOG.md) — version history
