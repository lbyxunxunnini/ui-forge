# Design Card Protocol

## What Is a Design Card

A design card stores **long-term project UI rules** — the constraints that persist across sessions and pages. It is project-scoped, not task-scoped.

Unlike `.design-doc/` (which tracks design process and progress), a design card captures the **stable rules** that should apply to every page in the project.

## Storage

```
.ui-forge/projects/<project>.design_card.yaml        # active card
.ui-forge/projects/<project>.design_card_draft.yaml   # draft (auto-generated first)
```

**Project isolation**: a design card belongs to one project. Reading another project's card or `.design-doc/` as context for the current project is forbidden.

## When to Create

- First design task in a new project: auto-generate a draft card
- User says "set up design rules" or "create design card": create explicitly
- 3+ pages designed: prompt user to formalize the card

## When to Load

- Every `uif-` entry: check for existing design card and load it
- `uif-fast`: load card to enforce consistency with existing design system
- `uif-a`: load card to fill gaps with project-consistent defaults

## Card Schema

```yaml
# .ui-forge/projects/<project>.design_card.yaml

project:
  name: "My App"
  type: app | web | desktop
  platform: ios | android | web | multi

brand_voice:
 气质: "现代、简洁、专业"
 禁用风格: ["赛博朋克", "拟物化", "过于花哨"]

visual_language:
  primary_color: "#4F46E5"
  secondary_color: "#7C3AED"
  background: "#FFFFFF"
  text_primary: "#111827"
  text_secondary: "#6B7280"
  font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
  border_radius: "8px"
  shadow: "0 1px 3px rgba(0,0,0,0.1)"
  density: "comfortable" | "compact" | "spacious"

layout_rules:
  grid: "12-column"
  breakpoints:
    mobile: "< 640px"
    tablet: "640px - 1024px"
    desktop: "> 1024px"
  max_width: "1280px"
  信息层级: "标题 > 副标题 > 正文 > 辅助文字"

component_rules:
  button:
    height: "44px"
    border_radius: "8px"
    variants: ["primary", "secondary", "ghost", "danger"]
  input:
    height: "44px"
    border_radius: "8px"
    border: "1px solid #D1D5DB"
  card:
    border_radius: "12px"
    padding: "16px"
    shadow: "0 1px 3px rgba(0,0,0,0.1)"
  navigation:
    style: "tab_bar" | "sidebar" | "top_bar"

interaction_rules:
  loading: "spinner + skeleton"
  empty: "illustration + message + action"
  error: "toast (3s) + inline validation"
  success: "toast (2s)"
  disabled: "opacity 0.5, cursor not-allowed"

accessibility:
  min_contrast_ratio: 4.5
  min_touch_target: "44px"
  keyboard_navigation: true
  screen_reader: true

output_preferences:
  format: "html_css_svg"
  tokens_format: "json"
  responsive: true
  icon_export: true

quick_context: ""  # last design scan summary, auto-updated
```

## Auto-Population

On first design task, the system should:

1. Scan existing design assets (if any)
2. Generate a draft card with reasonable defaults
3. Present to user for confirmation
4. Save as active card

## Enforcement

When a design card exists:

- **Colors**: must use card-defined palette; no ad-hoc colors
- **Typography**: must use card-defined scale; no ad-hoc font sizes
- **Spacing**: must use card-defined spacing system
- **Components**: must reference card-defined component rules
- **Interaction states**: must cover card-defined interaction patterns

If a design decision conflicts with the card, flag it:

```
[ui-forge] UI设计师：设计规则冲突
- 冲突项：（具体冲突）
- 卡片规则：（卡片中的定义）
- 当前选择：（当前设计中的选择）
- 选项A：遵循卡片规则
- 选项B：更新卡片规则（影响所有后续页面）
- 请确认
```

## Card Updates

Updates require explicit user confirmation for:

- Brand voice changes
- Color palette changes
- Font family changes
- Layout rule changes

Auto-updates allowed for:

- `quick_context` (last scan summary)
- Adding new component variants (not changing existing ones)
- Adding new breakpoints

## Relationship with Other Layers

| Layer | Scope | Lifetime | Purpose |
|-------|-------|----------|---------|
| Design card | Project | Permanent | Stable UI rules |
| `.design-doc/` | Project | Permanent | Design process memory |
| `design-output/` | Project | Permanent | User-facing deliverables |
| Session | Task | Ephemeral | Current task state |

Design card is the **constraints layer**. `.design-doc/` is the **history layer**. `design-output/` is the **artifact layer**. Session is the **working layer**.
