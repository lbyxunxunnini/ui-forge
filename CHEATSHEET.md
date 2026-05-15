# UI Forge Cheatsheet

## Entry Points

| Prefix | Mode | When to use |
|--------|------|-------------|
| `uif-` | Standard | Normal UI tasks, auto-route to diagnose/design/deliver |
| `uif-fast` | Fast | Small tweaks: color, spacing, font, icon swap, local fix |
| `uif-a` | Autonomous | Full auto design push, fill gaps with assumptions, only confirm high-risk |
| `uif-critique` | Critique | UI diagnosis only, no delivery by default |
| `uif-deliver` | Deliver | Explicit HTML/CSS/SVG/tokens/REQUIREMENTS output |

Backward-compatible: `uid-`, `/ui-forge`, `/ui-design` still work.

## Common Tasks

### "Design a login page"
```
uif- design an iOS login page, modern style, gradient background, include WeChat login
```

### "Fix this button color"
```
uif-fast change the primary button to #4F46E5
```

### "Review my dashboard"
```
uif-critique review this dashboard screenshot, focus on information hierarchy
```

### "Give me the HTML/CSS"
```
uif-deliver output the login page as HTML/CSS/SVG with tokens and REQUIREMENTS
```

### "Just design it, don't ask me"
```
uif-a design a settings page in dark mode, tech style, make reasonable assumptions
```

### "Redesign this page"
```
uif- redesign this dashboard and explain why it feels templated
```

### "Build a design system"
```
uif- tighten a design system for forms and action bars
```

## Modes (Auto-Selected)

| Mode | Trigger | Output |
|------|---------|--------|
| Diagnose | Existing UI, "review", "critique", "what's wrong" | Structural analysis + fix recommendations |
| Design | New page, "design", "create" | Layout + components + interaction states |
| Deliver | "output", "HTML", "CSS", "handoff" | HTML/CSS/SVG/tokens/REQUIREMENTS |
| Fast | Small tweak with clear target | Direct fix, no interview |
| Design System | 3+ pages, tokens, components | Locked tokens + component library + consistency report |

## Question Budget

| Level | Task | Budget |
|-------|------|--------|
| L1 | Tweak / known fix | 0-2 questions |
| L2 | Standard single page | 2-4 questions |
| L3 | Complex / redesign | 4-7 questions |
| L4 | Multi-page / design system | 6-10 questions (segmented) |

## Design Card

Store long-term project UI rules in `.ui-forge/projects/<project>.design_card.yaml`. Auto-loaded on entry. Covers brand voice, visual language, layout rules, component rules, interaction rules, accessibility, output preferences.

## Output Checklist

Every delivery must include:
- [ ] `index.html` — opens in browser
- [ ] `style.css` — external stylesheet
- [ ] `tokens.json` — design tokens (JSON)
- [ ] `icons/` — all SVG icons
- [ ] `DESIGN-GUIDE.md` — visual spec
- [ ] `REQUIREMENTS.md` — interaction spec

## Relationship with polanyi-design

- `polanyi-design` = judgment layer (aesthetic diagnosis, gestalt, figure-ground)
- `ui-forge` = execution layer (workflow, roles, delivery)
- Route to polanyi when: "feels off", "too template", "no personality", "too flat"
- Absorb from polanyi: structural diagnosis + concrete fixes, not abstract theory
