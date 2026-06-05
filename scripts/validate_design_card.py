#!/usr/bin/env python3
"""
validate_design_card.py — 校验 design card 字段完整性和格式。

用法：
    python scripts/validate_design_card.py <card.yaml> [--strict]

退出码：
    0 = 通过
    1 = 有错误
    2 = 有警告（仅 strict 模式下退出码为 1）
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# --- 必需字段定义 ---

REQUIRED_SECTIONS = [
    "project",
    "brand_voice",
    "visual_language",
    "layout_rules",
    "device_frame_rules",
    "hierarchy_rules",
    "component_rules",
    "interaction_rules",
    "accessibility",
    "output_preferences",
]

REQUIRED_PROJECT_FIELDS = ["name", "type", "platform"]
REQUIRED_VISUAL_FIELDS = ["primary_color", "font_family", "border_radius"]
REQUIRED_LAYOUT_FIELDS = ["breakpoints"]
REQUIRED_DEVICE_FIELDS = ["target_device", "viewport_width", "viewport_height", "page_width", "page_height", "page_overflow_y", "status_bar_height", "bottom_safe_padding"]
REQUIRED_HIERARCHY_FIELDS = ["primary_focal_rule", "focus_chain_required", "squint_test"]
REQUIRED_COMPONENT_FIELDS = ["button", "input"]
REQUIRED_INTERACTION_FIELDS = ["loading", "error", "empty"]
REQUIRED_ACCESSIBILITY_FIELDS = ["min_contrast_ratio", "min_touch_target"]
REQUIRED_OUTPUT_FIELDS = ["format", "tokens_format"]

VALID_PROJECT_TYPES = {"app", "web", "desktop"}
VALID_PLATFORMS = {"ios", "android", "web", "multi"}
VALID_DENSITIES = {"comfortable", "compact", "spacious"}
VALID_NAV_STYLES = {"tab_bar", "sidebar", "top_bar"}

HEX_COLOR_RE = re.compile(r"^#[0-9a-fA-F]{3,8}$")
CSS_UNIT_RE = re.compile(r"^\d+(\.\d+)?(px|rem|em|%)$")


class ValidationError:
    def __init__(self, path: str, message: str, level: str = "error"):
        self.path = path
        self.message = message
        self.level = level  # "error" or "warning"

    def __str__(self):
        tag = "ERROR" if self.level == "error" else "WARN "
        return f"  [{tag}] {self.path}: {self.message}"


def parse_yaml_file(path: Path) -> dict:
    """解析 YAML 文件，回退到简单行解析。"""
    content = path.read_text(encoding="utf-8")

    if yaml:
        try:
            return yaml.safe_load(content) or {}
        except yaml.YAMLError as e:
            print(f"Warning: YAML parse error ({e}), using fallback parser", file=sys.stderr)

    # 简单回退解析：提取 key: value 对
    result = {}
    current_section = None
    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # 顶级 key
        if not line.startswith(" ") and ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val:
                result[key] = val
            else:
                result[key] = {}
                current_section = key
        elif current_section and ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if isinstance(result.get(current_section), dict):
                result[current_section][key] = val

    return result


def validate_hex_color(value: str, path: str) -> list[ValidationError]:
    """校验十六进制颜色格式。"""
    errors = []
    if isinstance(value, str) and not HEX_COLOR_RE.match(value):
        # 允许 rgba() 和其他 CSS 颜色值
        if not value.startswith(("rgb", "hsl", "linear-gradient", "var(")):
            errors.append(ValidationError(path, f"invalid color format: '{value}'"))
    return errors


def validate_css_unit(value: str, path: str) -> list[ValidationError]:
    """校验 CSS 单位格式。"""
    errors = []
    if isinstance(value, str) and not CSS_UNIT_RE.match(value):
        # 允许 0、auto、特殊值
        if value not in ("0", "auto", "none", "inherit", "initial"):
            errors.append(ValidationError(path, f"invalid CSS unit: '{value}' (expected Npx/Nrem/Nem/N%)"))
    return errors


def validate_card(data: dict, strict: bool = False) -> list[ValidationError]:
    """校验 design card 完整性和格式。"""
    errors = []

    # --- 1. 检查必需顶层 section ---
    for section in REQUIRED_SECTIONS:
        if section not in data:
            errors.append(ValidationError(section, f"missing required section", "error"))

    # --- 2. project ---
    project = data.get("project", {})
    if isinstance(project, dict):
        for field in REQUIRED_PROJECT_FIELDS:
            if field not in project:
                errors.append(ValidationError(f"project.{field}", "missing required field", "error"))

        ptype = project.get("type", "")
        if ptype and ptype not in VALID_PROJECT_TYPES:
            errors.append(ValidationError("project.type", f"invalid type '{ptype}', expected one of {VALID_PROJECT_TYPES}", "warning"))

        platform = project.get("platform", "")
        if platform and platform not in VALID_PLATFORMS:
            errors.append(ValidationError("project.platform", f"invalid platform '{platform}', expected one of {VALID_PLATFORMS}", "warning"))

    # --- 3. brand_voice ---
    brand = data.get("brand_voice", {})
    if isinstance(brand, dict):
        if "气质" not in brand and "personality" not in brand:
            errors.append(ValidationError("brand_voice", "missing '气质' or 'personality' field", "warning"))

    # --- 4. visual_language ---
    visual = data.get("visual_language", {})
    if isinstance(visual, dict):
        for field in REQUIRED_VISUAL_FIELDS:
            if field not in visual:
                errors.append(ValidationError(f"visual_language.{field}", "missing required field", "error"))

        if "primary_color" in visual:
            errors.extend(validate_hex_color(visual["primary_color"], "visual_language.primary_color"))
        if "secondary_color" in visual:
            errors.extend(validate_hex_color(visual["secondary_color"], "visual_language.secondary_color"))
        if "border_radius" in visual:
            errors.extend(validate_css_unit(visual["border_radius"], "visual_language.border_radius"))

        density = visual.get("density", "")
        if density and density not in VALID_DENSITIES:
            errors.append(ValidationError("visual_language.density", f"invalid density '{density}', expected one of {VALID_DENSITIES}", "warning"))

    # --- 5. layout_rules ---
    layout = data.get("layout_rules", {})
    if isinstance(layout, dict):
        for field in REQUIRED_LAYOUT_FIELDS:
            if field not in layout:
                errors.append(ValidationError(f"layout_rules.{field}", "missing required field", "error"))

        breakpoints = layout.get("breakpoints", {})
        if isinstance(breakpoints, dict):
            for bp_name in ["mobile", "tablet", "desktop"]:
                if bp_name not in breakpoints:
                    errors.append(ValidationError(f"layout_rules.breakpoints.{bp_name}", f"missing breakpoint '{bp_name}'", "warning"))

    # --- 6. device_frame_rules ---
    device = data.get("device_frame_rules", {})
    if isinstance(device, dict):
        for field in REQUIRED_DEVICE_FIELDS:
            if field not in device:
                errors.append(ValidationError(f"device_frame_rules.{field}", "missing required device frame rule", "error"))

        expected_numbers = {
            "viewport_width": 393,
            "viewport_height": 852,
        }
        for field, expected in expected_numbers.items():
            if field in device:
                try:
                    actual = int(device[field])
                    if actual != expected:
                        errors.append(ValidationError(f"device_frame_rules.{field}", f"expected iPhone 15 value {expected}, got {actual}", "warning"))
                except (ValueError, TypeError):
                    errors.append(ValidationError(f"device_frame_rules.{field}", f"expected integer value {expected}", "error"))

        expected_units = {
            "page_width": "393px",
            "page_height": "852px",
            "status_bar_height": "59px",
            "bottom_safe_padding": "34px",
        }
        for field, expected in expected_units.items():
            if field in device and str(device[field]) != expected:
                errors.append(ValidationError(f"device_frame_rules.{field}", f"expected '{expected}' for iPhone 15", "warning"))

        required_classes = device.get("required_gallery_classes", [])
        if isinstance(required_classes, str):
            required_classes = [c.strip().strip("'\"[]") for c in required_classes.split(",") if c.strip()]
        for class_name in ["iphone-frame", "iphone-screen", "dynamic-island", "status-bar", "home-indicator"]:
            if isinstance(required_classes, list) and class_name not in required_classes:
                errors.append(ValidationError("device_frame_rules.required_gallery_classes", f"missing '{class_name}'", "warning"))

    # --- 7. hierarchy_rules ---
    hierarchy = data.get("hierarchy_rules", {})
    if isinstance(hierarchy, dict):
        for field in REQUIRED_HIERARCHY_FIELDS:
            if field not in hierarchy:
                errors.append(ValidationError(f"hierarchy_rules.{field}", "missing required hierarchy rule", "error"))

        focus_required = hierarchy.get("focus_chain_required")
        if isinstance(focus_required, str) and focus_required.lower() in {"true", "false"}:
            focus_required = focus_required.lower() == "true"
        if focus_required is not None and not isinstance(focus_required, bool):
            errors.append(ValidationError("hierarchy_rules.focus_chain_required", "should be a boolean", "warning"))

        if "squint_test" in hierarchy and not str(hierarchy.get("squint_test", "")).strip():
            errors.append(ValidationError("hierarchy_rules.squint_test", "must describe how visual focus is verified", "error"))

    # --- 8. component_rules ---
    components = data.get("component_rules", {})
    if isinstance(components, dict):
        for field in REQUIRED_COMPONENT_FIELDS:
            if field not in components:
                errors.append(ValidationError(f"component_rules.{field}", "missing required component rule", "error"))

        # 校验 button
        button = components.get("button", {})
        if isinstance(button, dict):
            if "variants" in button and not isinstance(button["variants"], list):
                errors.append(ValidationError("component_rules.button.variants", "should be a list", "error"))

        # 校验 navigation style
        nav = components.get("navigation", {})
        if isinstance(nav, dict):
            style = nav.get("style", "")
            if style and style not in VALID_NAV_STYLES:
                errors.append(ValidationError("component_rules.navigation.style", f"invalid style '{style}'", "warning"))

    # --- 9. interaction_rules ---
    interaction = data.get("interaction_rules", {})
    if isinstance(interaction, dict):
        for field in REQUIRED_INTERACTION_FIELDS:
            if field not in interaction:
                errors.append(ValidationError(f"interaction_rules.{field}", "missing required interaction rule", "warning"))

    # --- 10. accessibility ---
    a11y = data.get("accessibility", {})
    if isinstance(a11y, dict):
        for field in REQUIRED_ACCESSIBILITY_FIELDS:
            if field not in a11y:
                errors.append(ValidationError(f"accessibility.{field}", "missing required field", "error"))

        contrast = a11y.get("min_contrast_ratio")
        if contrast is not None:
            try:
                ratio = float(contrast)
                if ratio < 3.0:
                    errors.append(ValidationError("accessibility.min_contrast_ratio", f"ratio {ratio} is below WCAG minimum (3.0)", "error"))
                elif ratio < 4.5:
                    errors.append(ValidationError("accessibility.min_contrast_ratio", f"ratio {ratio} is below WCAG AA (4.5), consider increasing", "warning"))
            except (ValueError, TypeError):
                errors.append(ValidationError("accessibility.min_contrast_ratio", f"invalid number: '{contrast}'", "error"))

        touch = a11y.get("min_touch_target")
        if touch:
            errors.extend(validate_css_unit(str(touch), "accessibility.min_touch_target"))

    # --- 11. output_preferences ---
    output = data.get("output_preferences", {})
    if isinstance(output, dict):
        for field in REQUIRED_OUTPUT_FIELDS:
            if field not in output:
                errors.append(ValidationError(f"output_preferences.{field}", "missing required field", "warning"))

    # --- 12. quick_context ---
    if "quick_context" not in data:
        errors.append(ValidationError("quick_context", "missing (auto-populated field)", "warning"))

    # --- strict 模式：warnings 也报错 ---
    if strict:
        for err in errors:
            if err.level == "warning":
                err.level = "error"

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate a design card YAML file.")
    parser.add_argument("card", help="Path to the design card YAML file")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    card_path = Path(args.card)
    if not card_path.exists():
        print(f"Error: file not found: {card_path}", file=sys.stderr)
        sys.exit(1)

    data = parse_yaml_file(card_path)
    errors = validate_card(data, strict=args.strict)

    error_count = sum(1 for e in errors if e.level == "error")
    warning_count = sum(1 for e in errors if e.level == "warning")

    if errors:
        print(f"Validation: {error_count} errors, {warning_count} warnings\n")
        for err in errors:
            print(err)
        print()
        if error_count > 0:
            sys.exit(1)
        elif args.strict and warning_count > 0:
            sys.exit(1)
        else:
            sys.exit(0)
    else:
        print("Validation passed: all fields present and well-formed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
