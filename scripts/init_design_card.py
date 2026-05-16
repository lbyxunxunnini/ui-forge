#!/usr/bin/env python3
"""
init_design_card.py — 基于项目快照生成 design card 草案。

用法：
    python scripts/init_design_card.py [项目根目录] [--output 输出路径]

默认扫描当前工作目录，输出到 .ui-forge/projects/<dirname>.design_card_draft.yaml
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

# 复用 project_snapshot
sys.path.insert(0, str(Path(__file__).parent))
from project_snapshot import take_snapshot


def guess_project_name(root: Path) -> str:
    """从目录名或 config 推断项目名。"""
    # 尝试从 design-config.json 读取
    config_path = root / "config" / "design-config.json"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            if "project" in config and "name" in config["project"]:
                return config["project"]["name"]
        except (json.JSONDecodeError, OSError):
            pass

    return root.name.replace("-", " ").replace("_", " ").title()


def guess_project_type(root: Path, snapshot: dict) -> str:
    """推断项目类型。"""
    config = snapshot.get("config", {})
    if "design_config" in config:
        project = config["design_config"].get("project", {})
        ptype = project.get("type", "")
        if ptype:
            # 归一化：mobile -> app
            type_map = {"mobile": "app", "ios": "app", "android": "app", "web": "web", "desktop": "desktop"}
            return type_map.get(ptype, ptype)

    # 从文件名推断
    templates = snapshot.get("templates", [])
    html_files = []
    for subdir in ["design-output", "templates", "demo"]:
        d = root / subdir
        if d.exists():
            html_files.extend(f.name for f in d.rglob("*.html"))

    mobile_keywords = ["login", "home", "profile", "settings", "tabbar", "navigation"]
    web_keywords = ["dashboard", "admin", "panel", "sidebar"]

    mobile_count = sum(1 for f in html_files if any(k in f.lower() for k in mobile_keywords))
    web_count = sum(1 for f in html_files if any(k in f.lower() for k in web_keywords))

    if mobile_count > web_count:
        return "app"
    elif web_count > mobile_count:
        return "web"
    return "app"


def guess_platform(root: Path, snapshot: dict) -> str:
    """推断目标平台。"""
    config = snapshot.get("config", {})
    if "design_config" in config:
        project = config["design_config"].get("project", {})
        platforms = project.get("platform", [])
        if isinstance(platforms, list) and len(platforms) == 1:
            return platforms[0]
        elif isinstance(platforms, list) and len(platforms) > 1:
            return "multi"
        elif isinstance(platforms, str):
            return platforms
    return "ios"


def extract_primary_color(snapshot: dict) -> str:
    """从 tokens 或 CSS 提取主色。"""
    tokens = snapshot.get("extracted", {}).get("tokens")
    if tokens and isinstance(tokens, dict):
        colors = tokens.get("color", tokens.get("colors", {}))
        if isinstance(colors, dict):
            primary = colors.get("primary", "")
            if primary:
                return primary

    # 从 config 读取
    config = snapshot.get("config", {})
    if "design_config" in config:
        token_colors = config["design_config"].get("tokens", {}).get("colors", {})
        primary = token_colors.get("primary", "")
        if primary:
            return primary

    return "#4F46E5"


def extract_secondary_color(snapshot: dict) -> str:
    """从 tokens 或 CSS 提取辅助色。"""
    tokens = snapshot.get("extracted", {}).get("tokens")
    if tokens and isinstance(tokens, dict):
        colors = tokens.get("color", tokens.get("colors", {}))
        if isinstance(colors, dict):
            secondary = colors.get("secondary", "")
            if secondary:
                return secondary

    config = snapshot.get("config", {})
    if "design_config" in config:
        token_colors = config["design_config"].get("tokens", {}).get("colors", {})
        secondary = token_colors.get("secondary", "")
        if secondary:
            return secondary

    return "#7C3AED"


def extract_font_family(snapshot: dict) -> str:
    """从 tokens 或 CSS 提取字体族。"""
    tokens = snapshot.get("extracted", {}).get("tokens")
    if tokens and isinstance(tokens, dict):
        font = tokens.get("font", tokens.get("typography", {}))
        if isinstance(font, dict):
            family = font.get("family", font.get("fontFamily", ""))
            if family:
                return family

    config = snapshot.get("config", {})
    if "design_config" in config:
        typography = config["design_config"].get("tokens", {}).get("typography", {})
        family = typography.get("fontFamily", "")
        if family:
            return family

    fonts = snapshot.get("extracted", {}).get("fonts", [])
    if fonts:
        return fonts[0]

    return "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"


def extract_border_radius(snapshot: dict) -> str:
    """提取圆角值。"""
    config = snapshot.get("config", {})
    if "design_config" in config:
        radii = config["design_config"].get("tokens", {}).get("borderRadius", {})
        if radii:
            return radii.get("sm", radii.get("md", "8px"))
    return "8px"


def extract_spacing(snapshot: dict) -> dict:
    """提取间距系统。"""
    config = snapshot.get("config", {})
    if "design_config" in config:
        spacing = config["design_config"].get("tokens", {}).get("spacing", {})
        if spacing:
            return spacing
    return {"xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "32px"}


def extract_component_rules(snapshot: dict) -> dict:
    """从 components/ 目录推断组件规则。"""
    config = snapshot.get("config", {})
    if "design_config" in config:
        comp_config = config["design_config"].get("components", {})
        if comp_config:
            rules = {}
            if "button" in comp_config:
                btn = comp_config["button"]
                rules["button"] = {
                    "height": btn.get("primary", {}).get("height", "44px"),
                    "border_radius": btn.get("primary", {}).get("borderRadius", "8px"),
                    "variants": list(btn.keys()) if isinstance(btn, dict) else ["primary", "secondary"],
                }
            if "input" in comp_config:
                inp = comp_config["input"]
                rules["input"] = {
                    "height": inp.get("height", "44px"),
                    "border_radius": inp.get("borderRadius", "8px"),
                    "border": inp.get("border", "1px solid #D1D5DB"),
                }
            if "card" in comp_config:
                card = comp_config["card"]
                rules["card"] = {
                    "border_radius": card.get("borderRadius", "12px"),
                    "padding": card.get("padding", "16px"),
                    "shadow": card.get("boxShadow", "0 1px 3px rgba(0,0,0,0.1)"),
                }
            if rules:
                return rules

    return {
        "button": {"height": "44px", "border_radius": "8px", "variants": ["primary", "secondary", "ghost", "danger"]},
        "input": {"height": "44px", "border_radius": "8px", "border": "1px solid #D1D5DB"},
        "card": {"border_radius": "12px", "padding": "16px", "shadow": "0 1px 3px rgba(0,0,0,0.1)"},
    }


def count_pages(snapshot: dict) -> int:
    """统计已设计页面数。"""
    count = 0
    design_output = snapshot.get("design_output", {})
    if design_output.get("exists"):
        count += len(design_output.get("pages", []))
        # 根目录的 HTML 也算
        for f in design_output.get("files", []):
            if f.endswith(".html") and f != "index.html":
                count += 1
            elif f == "index.html":
                count += 1

    design_doc = snapshot.get("design_doc", {})
    if design_doc.get("exists"):
        for module in design_doc.get("modules", []):
            count += len(module.get("pages", []))

    return count


def generate_quick_context(snapshot: dict) -> str:
    """生成快速上下文摘要。"""
    parts = []

    design_output = snapshot.get("design_output", {})
    if design_output.get("exists"):
        files = design_output.get("files", [])
        icons = design_output.get("icons", [])
        components = design_output.get("components", [])
        pages = design_output.get("pages", [])
        parts.append(f"design-output: {len(files)} files, {len(icons)} icons, {len(components)} components, {len(pages)} pages")

    design_doc = snapshot.get("design_doc", {})
    if design_doc.get("exists"):
        modules = design_doc.get("modules", [])
        total_pages = sum(len(m.get("pages", [])) for m in modules)
        parts.append(f"design-doc: {len(modules)} modules, {total_pages} page records")

    page_count = count_pages(snapshot)
    if page_count >= 3:
        parts.append("NOTE: 3+ pages detected, design system rules should be active")

    return "; ".join(parts) if parts else "new project, no existing assets"


def build_card(root: Path, snapshot: dict) -> str:
    """生成 YAML 格式的 design card 草案。"""
    project_name = guess_project_name(root)
    project_type = guess_project_type(root, snapshot)
    platform = guess_platform(root, snapshot)
    primary = extract_primary_color(snapshot)
    secondary = extract_secondary_color(snapshot)
    font = extract_font_family(snapshot)
    radius = extract_border_radius(snapshot)
    spacing = extract_spacing(snapshot)
    comp_rules = extract_component_rules(snapshot)
    quick_context = generate_quick_context(snapshot)

    # YAML 手动生成（避免 pyyaml 依赖）
    lines = []
    lines.append(f"# Design Card Draft — {project_name}")
    lines.append(f"# Generated: {date.today().isoformat()}")
    lines.append("# Review and confirm before use.")
    lines.append("")
    lines.append("project:")
    lines.append(f'  name: "{project_name}"')
    lines.append(f"  type: {project_type}")
    lines.append(f"  platform: {platform}")
    lines.append("")
    lines.append("brand_voice:")
    lines.append('  气质: "现代、简洁、专业"')
    lines.append('  禁用风格: ["过于花哨", "拟物化"]')
    lines.append("")
    lines.append("visual_language:")
    lines.append(f'  primary_color: "{primary}"')
    lines.append(f'  secondary_color: "{secondary}"')
    lines.append('  background: "#FFFFFF"')
    lines.append('  text_primary: "#111827"')
    lines.append('  text_secondary: "#6B7280"')
    lines.append(f'  font_family: "{font}"')
    lines.append(f'  border_radius: "{radius}"')
    lines.append('  shadow: "0 1px 3px rgba(0,0,0,0.1)"')
    lines.append('  density: "comfortable"')
    lines.append("")
    lines.append("layout_rules:")
    lines.append('  grid: "12-column"')
    lines.append("  breakpoints:")
    lines.append('    mobile: "< 640px"')
    lines.append('    tablet: "640px - 1024px"')
    lines.append('    desktop: "> 1024px"')
    lines.append('  max_width: "1280px"')
    lines.append('  信息层级: "标题 > 副标题 > 正文 > 辅助文字"')
    lines.append("")
    lines.append("component_rules:")
    if "button" in comp_rules:
        btn = comp_rules["button"]
        lines.append("  button:")
        lines.append(f'    height: "{btn.get("height", "44px")}"')
        lines.append(f'    border_radius: "{btn.get("border_radius", "8px")}"')
        variants = btn.get("variants", ["primary", "secondary"])
        lines.append(f'    variants: {json.dumps(variants)}')
    if "input" in comp_rules:
        inp = comp_rules["input"]
        lines.append("  input:")
        lines.append(f'    height: "{inp.get("height", "44px")}"')
        lines.append(f'    border_radius: "{inp.get("border_radius", "8px")}"')
        lines.append(f'    border: "{inp.get("border", "1px solid #D1D5DB")}"')
    if "card" in comp_rules:
        card = comp_rules["card"]
        lines.append("  card:")
        lines.append(f'    border_radius: "{card.get("border_radius", "12px")}"')
        lines.append(f'    padding: "{card.get("padding", "16px")}"')
        lines.append(f'    shadow: "{card.get("shadow", "0 1px 3px rgba(0,0,0,0.1)")}"')
    lines.append("  navigation:")
    lines.append('    style: "tab_bar"')
    lines.append("")
    lines.append("interaction_rules:")
    lines.append('  loading: "spinner + skeleton"')
    lines.append('  empty: "illustration + message + action"')
    lines.append('  error: "toast (3s) + inline validation"')
    lines.append('  success: "toast (2s)"')
    lines.append('  disabled: "opacity 0.5, cursor not-allowed"')
    lines.append("")
    lines.append("accessibility:")
    lines.append("  min_contrast_ratio: 4.5")
    lines.append('  min_touch_target: "44px"')
    lines.append("  keyboard_navigation: true")
    lines.append("  screen_reader: true")
    lines.append("")
    lines.append("output_preferences:")
    lines.append('  format: "html_css_svg"')
    lines.append('  tokens_format: "json"')
    lines.append("  responsive: true")
    lines.append("  icon_export: true")
    lines.append("")
    lines.append(f'quick_context: "{quick_context}"')

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate a design card draft from project assets.")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--output", "-o", help="Output file path (default: .ui-forge/projects/<name>.design_card_draft.yaml)")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of file")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    snapshot = take_snapshot(root)
    card_content = build_card(root, snapshot)

    if args.stdout:
        print(card_content)
        return

    if args.output:
        output_path = Path(args.output)
    else:
        card_dir = root / ".ui-forge" / "projects"
        card_dir.mkdir(parents=True, exist_ok=True)
        project_name = guess_project_name(root).lower().replace(" ", "-")
        output_path = card_dir / f"{project_name}.design_card_draft.yaml"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(card_content, encoding="utf-8")
    print(f"Design card draft written to: {output_path}")


if __name__ == "__main__":
    main()
