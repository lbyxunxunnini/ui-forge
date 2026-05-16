#!/usr/bin/env python3
"""
project_snapshot.py — 扫描当前项目 UI 资产，输出结构化摘要。

用法：
    python scripts/project_snapshot.py [项目根目录]

默认扫描当前工作目录。输出 JSON 到 stdout。
"""

import json
import os
import re
import sys
from pathlib import Path


def scan_design_output(root: Path) -> dict:
    """扫描 design-output/ 目录。"""
    output_dir = root / "design-output"
    if not output_dir.exists():
        return {"exists": False}

    result = {"exists": True, "files": [], "icons": [], "components": []}

    for f in sorted(output_dir.iterdir()):
        if f.is_file():
            result["files"].append(f.name)
        elif f.name == "icons" and f.is_dir():
            result["icons"] = [i.name for i in sorted(f.iterdir()) if i.suffix == ".svg"]
        elif f.name == "components" and f.is_dir():
            result["components"] = [c.name for c in sorted(f.iterdir()) if c.suffix == ".html"]

    # 扫描 pages/ 子目录
    pages_dir = output_dir / "pages"
    if pages_dir.exists():
        result["pages"] = [p.name for p in sorted(pages_dir.iterdir()) if p.suffix == ".html"]

    return result


def scan_design_doc(root: Path) -> dict:
    """扫描 .design-doc/ 目录。"""
    doc_dir = root / ".design-doc"
    if not doc_dir.exists():
        return {"exists": False}

    result = {"exists": True, "modules": []}

    for item in sorted(doc_dir.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            module = {"name": item.name, "pages": []}
            index_file = item / "_index.md"
            if index_file.exists():
                module["has_index"] = True
            for f in sorted(item.iterdir()):
                if f.suffix == ".md" and f.name != "_index.md":
                    module["pages"].append(f.name)
            result["modules"].append(module)

    return result


def scan_templates(root: Path) -> list:
    """扫描 templates/ 目录。"""
    templates_dir = root / "templates"
    if not templates_dir.exists():
        return []
    return [f.name for f in sorted(templates_dir.iterdir()) if f.is_file()]


def scan_components(root: Path) -> list:
    """扫描 components/ 目录。"""
    comp_dir = root / "components"
    if not comp_dir.exists():
        return []
    return [f.name for f in sorted(comp_dir.iterdir()) if f.is_file()]


def scan_config(root: Path) -> dict:
    """扫描 config/ 目录。"""
    config_dir = root / "config"
    if not config_dir.exists():
        return {"exists": False}

    result = {"exists": True, "files": []}
    for f in sorted(config_dir.iterdir()):
        if f.is_file():
            result["files"].append(f.name)

    # 尝试读取 design-config.json
    design_config = config_dir / "design-config.json"
    if design_config.exists():
        try:
            with open(design_config, "r", encoding="utf-8") as fh:
                result["design_config"] = json.load(fh)
        except json.JSONDecodeError:
            result["design_config_error"] = "invalid JSON"

    return result


def scan_design_card(root: Path) -> dict:
    """扫描 .ui-forge/projects/ 下的设计规则卡。"""
    card_dir = root / ".ui-forge" / "projects"
    if not card_dir.exists():
        return {"exists": False}

    result = {"exists": True, "cards": []}
    for f in sorted(card_dir.iterdir()):
        if f.suffix in (".yaml", ".yml"):
            result["cards"].append(f.name)

    return result


def scan_screenshots(root: Path) -> list:
    """扫描 screenshots/ 目录。"""
    ss_dir = root / "screenshots"
    if not ss_dir.exists():
        return []
    return [f.name for f in sorted(ss_dir.iterdir()) if f.is_file()]


def scan_demo(root: Path) -> list:
    """扫描 demo/ 目录。"""
    demo_dir = root / "demo"
    if not demo_dir.exists():
        return []
    return [f.name for f in sorted(demo_dir.iterdir()) if f.is_file()]


def extract_colors_from_css(root: Path) -> list:
    """从 CSS 文件中提取颜色值。"""
    colors = set()
    css_files = []

    design_output = root / "design-output"
    if design_output.exists():
        for f in design_output.rglob("*.css"):
            css_files.append(f)

    templates = root / "templates"
    if templates.exists():
        for f in templates.rglob("*.css"):
            css_files.append(f)

    components = root / "components"
    if components.exists():
        for f in components.rglob("*.css"):
            css_files.append(f)

    hex_pattern = re.compile(r"#[0-9a-fA-F]{3,8}\b")
    rgb_pattern = re.compile(r"rgba?\([^)]+\)")

    for css_file in css_files:
        try:
            content = css_file.read_text(encoding="utf-8")
            colors.update(hex_pattern.findall(content))
            colors.update(rgb_pattern.findall(content))
        except (UnicodeDecodeError, OSError):
            pass

    return sorted(colors)


def extract_fonts_from_css(root: Path) -> list:
    """从 CSS 文件中提取字体族。"""
    fonts = set()
    css_files = []

    for subdir in ["design-output", "templates", "components"]:
        d = root / subdir
        if d.exists():
            for f in d.rglob("*.css"):
                css_files.append(f)

    font_pattern = re.compile(r"font-family:\s*([^;]+)", re.IGNORECASE)

    for css_file in css_files:
        try:
            content = css_file.read_text(encoding="utf-8")
            for match in font_pattern.finditer(content):
                fonts.add(match.group(1).strip())
        except (UnicodeDecodeError, OSError):
            pass

    return sorted(fonts)


def extract_tokens(root: Path) -> dict | None:
    """读取 tokens.json（如果存在）。"""
    tokens_path = root / "design-output" / "tokens.json"
    if tokens_path.exists():
        try:
            with open(tokens_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {"error": "invalid JSON"}
    return None


def take_snapshot(root: Path) -> dict:
    """生成完整项目快照。"""
    return {
        "project_root": str(root),
        "design_output": scan_design_output(root),
        "design_doc": scan_design_doc(root),
        "design_card": scan_design_card(root),
        "templates": scan_templates(root),
        "components": scan_components(root),
        "config": scan_config(root),
        "screenshots": scan_screenshots(root),
        "demo": scan_demo(root),
        "extracted": {
            "colors": extract_colors_from_css(root),
            "fonts": extract_fonts_from_css(root),
            "tokens": extract_tokens(root),
        },
    }


def main():
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()
    else:
        root = Path.cwd()

    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    snapshot = take_snapshot(root)
    print(json.dumps(snapshot, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
