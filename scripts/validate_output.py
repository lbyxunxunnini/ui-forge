#!/usr/bin/env python3
"""
validate_output.py — 检查 design-output/ 交付物完整性。

用法：
    python scripts/validate_output.py [design-output目录] [--strict]

校验项：
    - index.html 存在且非空
    - style.css 存在且非空
    - tokens.json 存在且为合法 JSON
    - icons/ 目录存在且含 SVG 文件
    - DESIGN-GUIDE.md 存在
    - REQUIREMENTS.md 存在
    - HTML 中每个 <svg> 都有对应 .svg 导出文件
    - visuals/ 中的 SVG 视觉资产包含 viewBox，建议包含 title/desc
    - SVG fallback 模式下避免外链非 SVG 图片
    - App/iOS 画廊包含 iPhone 15 真机外壳、安全区和系统区域类名
    - HTML 包含响应式断点
    - HTML 包含输入验证状态 CSS

退出码：0=通过，1=有错误，2=有警告（strict 下为 1）
"""

import argparse
import json
import re
import sys
from pathlib import Path


class Issue:
    def __init__(self, path: str, message: str, level: str = "error"):
        self.path = path
        self.message = message
        self.level = level

    def __str__(self):
        tag = "ERROR" if self.level == "error" else "WARN "
        return f"  [{tag}] {self.path}: {self.message}"


def check_file_exists(directory: Path, filename: str, required: bool = True) -> list[Issue]:
    """检查文件是否存在且非空。"""
    issues = []
    filepath = directory / filename
    if not filepath.exists():
        level = "error" if required else "warning"
        issues.append(Issue(filename, "file missing", level))
    elif filepath.stat().st_size == 0:
        level = "error" if required else "warning"
        issues.append(Issue(filename, "file is empty", level))
    return issues


def check_tokens_json(directory: Path) -> list[Issue]:
    """检查 tokens.json 格式。"""
    issues = []
    tokens_path = directory / "tokens.json"
    if not tokens_path.exists():
        issues.append(Issue("tokens.json", "file missing", "error"))
        return issues

    try:
        content = tokens_path.read_text(encoding="utf-8")
        data = json.loads(content)
        if not isinstance(data, dict):
            issues.append(Issue("tokens.json", "root should be an object", "error"))
        elif len(data) == 0:
            issues.append(Issue("tokens.json", "object is empty", "warning"))
    except json.JSONDecodeError as e:
        issues.append(Issue("tokens.json", f"invalid JSON: {e}", "error"))
    except UnicodeDecodeError:
        issues.append(Issue("tokens.json", "encoding error (expected UTF-8)", "error"))

    return issues


def check_icons(directory: Path) -> list[Issue]:
    """检查 icons/ 目录。"""
    issues = []
    icons_dir = directory / "icons"
    if not icons_dir.exists():
        issues.append(Issue("icons/", "directory missing", "error"))
        return issues

    svg_files = list(icons_dir.glob("*.svg"))
    if len(svg_files) == 0:
        issues.append(Issue("icons/", "no SVG files found", "error"))
    else:
        # 检查每个 SVG 文件是否非空
        for svg in svg_files:
            if svg.stat().st_size == 0:
                issues.append(Issue(f"icons/{svg.name}", "SVG file is empty", "error"))

    return issues


def check_html_svg_export(directory: Path) -> list[Issue]:
    """检查 HTML 中的 <svg> 是否都有对应导出文件。"""
    issues = []
    html_files = list(directory.glob("*.html")) + list((directory / "pages").glob("*.html")) if (directory / "pages").exists() else list(directory.glob("*.html"))

    icons_dir = directory / "icons"
    exported_icons = set()
    if icons_dir.exists():
        exported_icons = {f.stem for f in icons_dir.glob("*.svg")}

    svg_pattern = re.compile(r'<svg[^>]*(?:class|id)="([^"]*)"', re.IGNORECASE)
    svg_any = re.compile(r"<svg\b", re.IGNORECASE)

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            issues.append(Issue(html_file.name, "cannot read file", "error"))
            continue

        svg_count = len(svg_any.findall(content))
        if svg_count > 0 and len(exported_icons) == 0:
            issues.append(Issue(html_file.name, f"contains {svg_count} <svg> but icons/ has no exported SVGs", "error"))
        elif svg_count > 0:
            # 尝试匹配 class/id 到导出文件
            matches = svg_pattern.findall(content)
            for match in matches:
                # 尝试常见命名转换
                candidates = [match, match.replace("-icon", "").replace("Icon", "")]
                if not any(c in exported_icons for c in candidates):
                    issues.append(Issue(
                        f"{html_file.name} <svg class=\"{match}\">",
                        f"no matching SVG in icons/ (exported: {', '.join(sorted(exported_icons)[:5])}{'...' if len(exported_icons) > 5 else ''})",
                        "warning"
                    ))

    return issues


def uses_svg_fallback(directory: Path) -> bool:
    """检查交付物是否声明使用 SVG Visual Fallback。"""
    guide_path = directory / "DESIGN-GUIDE.md"
    if not guide_path.exists():
        return False

    try:
        content = guide_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False

    return "SVG Visual Fallback" in content or "SVG视觉" in content or "纯 SVG" in content


def check_visuals(directory: Path) -> list[Issue]:
    """检查 SVG 视觉资产目录。"""
    issues = []
    visuals_dir = directory / "visuals"
    fallback_active = uses_svg_fallback(directory)

    if not visuals_dir.exists():
        if fallback_active:
            issues.append(Issue("visuals/", "SVG fallback declared but visuals/ directory missing", "warning"))
        return issues

    svg_files = list(visuals_dir.glob("*.svg"))
    if len(svg_files) == 0:
        issues.append(Issue("visuals/", "directory exists but no SVG visual assets found", "warning"))
        return issues

    for svg_file in svg_files:
        try:
            content = svg_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            issues.append(Issue(f"visuals/{svg_file.name}", "cannot read SVG file", "error"))
            continue

        if "<svg" not in content:
            issues.append(Issue(f"visuals/{svg_file.name}", "missing <svg> root", "error"))
        if "viewBox" not in content:
            issues.append(Issue(f"visuals/{svg_file.name}", "missing viewBox", "error"))
        if "<title" not in content and "<desc" not in content:
            issues.append(Issue(f"visuals/{svg_file.name}", "missing <title> or <desc> for accessibility", "warning"))

    return issues


def check_svg_fallback_external_images(directory: Path) -> list[Issue]:
    """SVG fallback 模式下检查外链非 SVG 图片风险。"""
    issues = []
    if not uses_svg_fallback(directory):
        return issues

    html_files = list(directory.glob("*.html"))
    pages_dir = directory / "pages"
    if pages_dir.exists():
        html_files.extend(pages_dir.glob("*.html"))

    image_pattern = re.compile(r'<img[^>]+src="([^"]+)"', re.IGNORECASE)
    css_url_pattern = re.compile(r"url\(['\"]?([^'\"\)]+)['\"]?\)", re.IGNORECASE)

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        for match in image_pattern.finditer(content):
            src = match.group(1)
            if not (src.endswith(".svg") or src.startswith("data:image/svg+xml")):
                issues.append(Issue(html_file.name, f"SVG fallback declared but non-SVG <img> used: {src}", "warning"))

        for match in css_url_pattern.finditer(content):
            src = match.group(1)
            if src.startswith("data:"):
                continue
            if re.search(r"\.(png|jpe?g|webp|gif|avif)(\?|#|$)", src, re.IGNORECASE):
                issues.append(Issue(html_file.name, f"SVG fallback declared but bitmap url() used: {src}", "warning"))

    style_css = directory / "style.css"
    if style_css.exists():
        try:
            css_content = style_css.read_text(encoding="utf-8")
            for match in css_url_pattern.finditer(css_content):
                src = match.group(1)
                if src.startswith("data:"):
                    continue
                if re.search(r"\.(png|jpe?g|webp|gif|avif)(\?|#|$)", src, re.IGNORECASE):
                    issues.append(Issue("style.css", f"SVG fallback declared but bitmap url() used: {src}", "warning"))
        except (UnicodeDecodeError, OSError):
            pass

    return issues


def check_responsive(directory: Path) -> list[Issue]:
    """检查 HTML 是否包含响应式断点。"""
    issues = []
    html_files = list(directory.glob("*.html"))

    media_pattern = re.compile(r"@media\s*\(", re.IGNORECASE)

    for html_file in html_files:
        # 同时检查 HTML 和关联 CSS
        try:
            html_content = html_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        # 检查内联样式中的 @media
        media_matches = media_pattern.findall(html_content)

        # 检查引用的 CSS 文件
        css_link_pattern = re.compile(r'<link[^>]+href="([^"]*\.css)"', re.IGNORECASE)
        for css_match in css_link_pattern.finditer(html_content):
            css_path = directory / css_match.group(1)
            if css_path.exists():
                try:
                    css_content = css_path.read_text(encoding="utf-8")
                    media_matches.extend(media_pattern.findall(css_content))
                except (UnicodeDecodeError, OSError):
                    pass

        # 也检查 style.css
        style_css = directory / "style.css"
        if style_css.exists():
            try:
                css_content = style_css.read_text(encoding="utf-8")
                media_matches.extend(media_pattern.findall(css_content))
            except (UnicodeDecodeError, OSError):
                pass

        if len(media_matches) < 2:
            issues.append(Issue(html_file.name, f"only {len(media_matches)} @media query(s) found, expected at least 2 breakpoints", "warning"))

    return issues


def check_validation_states(directory: Path) -> list[Issue]:
    """检查 CSS 是否包含输入验证状态样式。"""
    issues = []

    css_contents = []
    # 收集所有 CSS 内容
    style_css = directory / "style.css"
    if style_css.exists():
        try:
            css_contents.append(style_css.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, OSError):
            pass

    # 也检查 HTML 中的 <style>
    for html_file in directory.glob("*.html"):
        try:
            content = html_file.read_text(encoding="utf-8")
            style_blocks = re.findall(r"<style[^>]*>(.*?)</style>", content, re.DOTALL | re.IGNORECASE)
            css_contents.extend(style_blocks)
        except (UnicodeDecodeError, OSError):
            pass

    all_css = "\n".join(css_contents)

    # 检查错误/成功状态样式
    error_indicators = ["error", "invalid", "danger", "red", "#ef4444", "#f44", "border-color.*red"]
    success_indicators = ["success", "valid", "green", "#22c55e", "#0f0", "border-color.*green"]

    has_error = any(re.search(indicator, all_css, re.IGNORECASE) for indicator in error_indicators)
    has_success = any(re.search(indicator, all_css, re.IGNORECASE) for indicator in success_indicators)

    if not has_error:
        issues.append(Issue("CSS", "no error/validation state styles found (error border, invalid state, etc.)", "warning"))
    if not has_success:
        issues.append(Issue("CSS", "no success state styles found (success border, valid state, etc.)", "warning"))

    return issues


def check_device_frame(directory: Path) -> list[Issue]:
    """检查 App/iOS 画廊是否包含 iPhone 15 外壳和安全区结构。"""
    issues = []
    index_path = directory / "index.html"
    style_path = directory / "style.css"

    if not index_path.exists():
        return issues

    try:
        index_content = index_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        issues.append(Issue("index.html", "cannot read file for device frame validation", "warning"))
        return issues

    css_content = ""
    if style_path.exists():
        try:
            css_content = style_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            pass

    combined = f"{index_content}\n{css_content}"
    required_classes = ["iphone-frame", "iphone-screen", "dynamic-island", "status-bar", "home-indicator"]
    for class_name in required_classes:
        if class_name not in combined:
            issues.append(Issue("index.html", f"missing iPhone gallery class: .{class_name}", "warning"))

    required_values = {
        "393px": "iPhone 15 screen width",
        "852px": "iPhone 15 screen height",
        "59px": "top safe/status area",
        "34px": "bottom safe area",
    }
    for value, meaning in required_values.items():
        if value not in combined:
            issues.append(Issue("style.css", f"missing {meaning} value ({value})", "warning"))

    if "overflow-y" not in combined or "auto" not in combined:
        issues.append(Issue("style.css", "missing scrollable page rule: overflow-y: auto", "warning"))

    return issues


def check_requirements(directory: Path) -> list[Issue]:
    """检查 REQUIREMENTS.md 内容质量。"""
    issues = []
    req_path = directory / "REQUIREMENTS.md"
    if not req_path.exists():
        issues.append(Issue("REQUIREMENTS.md", "file missing", "error"))
        return issues

    try:
        content = req_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        issues.append(Issue("REQUIREMENTS.md", "cannot read file", "error"))
        return issues

    # 检查关键章节
    required_sections = ["组件状态", "交互流程", "API", "异常处理"]
    for section in required_sections:
        if section not in content and section.lower() not in content.lower():
            issues.append(Issue("REQUIREMENTS.md", f"missing section: '{section}'", "warning"))

    if len(content.strip()) < 200:
        issues.append(Issue("REQUIREMENTS.md", "content too short (< 200 chars), may be incomplete", "warning"))

    return issues


def validate_output(directory: Path, strict: bool = False) -> list[Issue]:
    """执行完整输出校验。"""
    issues = []

    if not directory.exists():
        issues.append(Issue(str(directory), "directory does not exist", "error"))
        return issues

    # 文件完整性
    issues.extend(check_file_exists(directory, "index.html", required=True))
    issues.extend(check_file_exists(directory, "style.css", required=True))
    issues.extend(check_tokens_json(directory))
    issues.extend(check_icons(directory))
    issues.extend(check_file_exists(directory, "DESIGN-GUIDE.md", required=False))
    issues.extend(check_requirements(directory))

    # 内容质量
    issues.extend(check_html_svg_export(directory))
    issues.extend(check_visuals(directory))
    issues.extend(check_svg_fallback_external_images(directory))
    issues.extend(check_device_frame(directory))
    issues.extend(check_responsive(directory))
    issues.extend(check_validation_states(directory))

    if strict:
        for issue in issues:
            if issue.level == "warning":
                issue.level = "error"

    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate design output completeness.")
    parser.add_argument("directory", nargs="?", default="design-output", help="Design output directory (default: design-output)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    issues = validate_output(directory, strict=args.strict)

    error_count = sum(1 for i in issues if i.level == "error")
    warning_count = sum(1 for i in issues if i.level == "warning")

    if issues:
        print(f"Output validation: {error_count} errors, {warning_count} warnings\n")
        for issue in issues:
            print(issue)
        print()
        if error_count > 0:
            sys.exit(1)
        elif args.strict and warning_count > 0:
            sys.exit(1)
        sys.exit(0)
    else:
        print("Output validation passed: all deliverables present and complete.")
        sys.exit(0)


if __name__ == "__main__":
    main()
