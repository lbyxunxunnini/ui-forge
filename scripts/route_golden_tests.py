#!/usr/bin/env python3
"""
route_golden_tests.py — 验证 prompt 路由到正确的 UI Forge 模式。

用法：
    python scripts/route_golden_tests.py [--verbose]

基于 SKILL.md 中的入口策略和模式路由规则，测试一组 golden prompts
是否会被路由到正确的模式。

退出码：0=全部通过，1=有失败
"""

import argparse
import re
import sys


# --- 路由规则 ---

def detect_entry(prompt: str) -> str:
    """检测入口前缀。"""
    stripped = prompt.strip().lower()
    if stripped.startswith("uif-fast") or stripped.startswith("uif fast"):
        return "fast"
    if stripped.startswith("uif-a") or stripped.startswith("uif a") or stripped.startswith("uif_a"):
        return "autonomous"
    if stripped.startswith("uif-critique") or stripped.startswith("uif critique"):
        return "critique"
    if stripped.startswith("uif-deliver") or stripped.startswith("uif deliver"):
        return "deliver"
    if stripped.startswith("uif-") or stripped.startswith("uif ") or stripped.startswith("uid-"):
        return "standard"
    return "unknown"


def detect_mode(prompt: str, entry: str) -> str:
    """检测应该进入的模式。"""
    # 入口优先
    if entry == "fast":
        return "fast"
    if entry == "critique":
        return "diagnose"
    if entry == "deliver":
        return "deliver"
    if entry == "autonomous":
        return "design"  # auto 模式走完整设计流程

    # 标准入口：基于关键词路由
    lower = prompt.lower()

    # 诊断模式
    diagnose_keywords = ["review", "critique", "what's wrong", "why", "diagnose", "评审", "诊断", "为什么", "看起来像模板"]
    if any(kw in lower for kw in diagnose_keywords):
        return "diagnose"

    # 交付模式
    deliver_keywords = ["output", "html", "css", "svg", "handoff", "交付", "导出", "输出"]
    if any(kw in lower for kw in deliver_keywords):
        return "deliver"

    # 设计系统模式
    design_system_keywords = ["design system", "tokens", "组件库", "设计系统", "收口", "consistency", "一致性"]
    if any(kw in lower for kw in design_system_keywords):
        return "design_system"

    # 快速调整（小改动）
    tweak_keywords = ["change", "fix", "adjust", "tweak", "改", "调", "换", "把", "修改"]
    tweak_patterns = [
        r"改.*颜色", r"颜色.*改",
        r"改.*大小", r"大小.*改",
        r"改.*间距", r"间距.*改",
        r"改.*圆角", r"圆角.*改",
        r"改.*字体", r"字体.*改",
        r"改.*成.*色", r"改成",
        r"change.*color",
        r"change.*font",
        r"change.*size",
        r"fix.*button",
    ]
    is_tweak = any(kw in lower for kw in tweak_keywords)
    has_tweak_pattern = any(re.search(p, lower) for p in tweak_patterns)
    if is_tweak and has_tweak_pattern:
        return "fast"

    # 设计模式（默认）
    design_keywords = ["design", "create", "设计", "创建", "做一个", "新建"]
    if any(kw in lower for kw in design_keywords):
        return "design"

    return "design"  # 默认走设计


def detect_budget(prompt: str) -> str:
    """检测应该使用的提问预算层级。"""
    lower = prompt.lower()

    # L1：小调整
    l1_keywords = ["change", "fix", "adjust", "tweak", "改", "调", "换"]
    if any(kw in lower for kw in l1_keywords) and len(prompt) < 50:
        return "L1"

    # L4：多页面/设计系统
    l4_keywords = ["design system", "组件库", "设计系统", "收口", "多页面", "multi-page", "consistency"]
    if any(kw in lower for kw in l4_keywords):
        return "L4"

    # L3：重设计/复杂/诊断
    l3_keywords = ["redesign", "重设计", "critique", "review", "complex", "复杂", "仪表盘", "dashboard"]
    if any(kw in lower for kw in l3_keywords):
        return "L3"

    # L2：常规单页（默认）
    return "L2"


# --- Golden Test Cases ---

GOLDEN_TESTS = [
    # 标准入口
    {
        "prompt": "uif- design an iOS login page, modern style, gradient background",
        "expected_entry": "standard",
        "expected_mode": "design",
        "expected_budget": "L2",
    },
    {
        "prompt": "uif-设计一个电商APP首页，简约风格，包含底部导航栏",
        "expected_entry": "standard",
        "expected_mode": "design",
        "expected_budget": "L2",
    },
    {
        "prompt": "uif- redesign this dashboard and explain why it feels templated",
        "expected_entry": "standard",
        "expected_mode": "diagnose",
        "expected_budget": "L3",
    },
    {
        "prompt": "uif- tighten a design system for forms and action bars",
        "expected_entry": "standard",
        "expected_mode": "design_system",
        "expected_budget": "L4",
    },
    # 快速入口
    {
        "prompt": "uif-fast change the primary button to #4F46E5",
        "expected_entry": "fast",
        "expected_mode": "fast",
        "expected_budget": "L1",
    },
    {
        "prompt": "uif-fast把主按钮改成蓝色",
        "expected_entry": "fast",
        "expected_mode": "fast",
        "expected_budget": "L1",
    },
    # 自动入口
    {
        "prompt": "uif-a design a dark mode settings page",
        "expected_entry": "autonomous",
        "expected_mode": "design",
        "expected_budget": "L2",
    },
    {
        "prompt": "uif-a设计一个后台仪表盘，数据密集型，深色主题",
        "expected_entry": "autonomous",
        "expected_mode": "design",
        "expected_budget": "L3",
    },
    # 诊断入口
    {
        "prompt": "uif-critique review this dashboard screenshot, focus on information hierarchy",
        "expected_entry": "critique",
        "expected_mode": "diagnose",
        "expected_budget": "L3",
    },
    {
        "prompt": "uif-critique这个页面为什么看起来很普通",
        "expected_entry": "critique",
        "expected_mode": "diagnose",
        "expected_budget": "L3",
    },
    # 交付入口
    {
        "prompt": "uif-deliver output the login page as HTML/CSS/SVG with tokens",
        "expected_entry": "deliver",
        "expected_mode": "deliver",
        "expected_budget": "L2",
    },
    {
        "prompt": "uif-deliver给我导出HTML/CSS/SVG",
        "expected_entry": "deliver",
        "expected_mode": "deliver",
        "expected_budget": "L2",
    },
    # 向后兼容
    {
        "prompt": "uid-设计一个iOS登录页",
        "expected_entry": "standard",
        "expected_mode": "design",
        "expected_budget": "L2",
    },
    # 复杂场景
    {
        "prompt": "uif-我们已经有4个页面了，帮我收口一套可复用的设计系统",
        "expected_entry": "standard",
        "expected_mode": "design_system",
        "expected_budget": "L4",
    },
    {
        "prompt": "uif-重设计这个后台首页，先别出代码，先告诉我为什么它看起来像模板",
        "expected_entry": "standard",
        "expected_mode": "diagnose",
        "expected_budget": "L3",
    },
    # 微调场景
    {
        "prompt": "uif-把登录页的按钮颜色改成蓝色",
        "expected_entry": "standard",
        "expected_mode": "fast",
        "expected_budget": "L1",
    },
    {
        "prompt": "uif- change the font size to 14px",
        "expected_entry": "standard",
        "expected_mode": "fast",
        "expected_budget": "L1",
    },
]


def run_tests(verbose: bool = False) -> tuple[int, int]:
    """运行所有 golden tests，返回 (passed, failed)。"""
    passed = 0
    failed = 0

    for i, test in enumerate(GOLDEN_TESTS, 1):
        prompt = test["prompt"]
        actual_entry = detect_entry(prompt)
        actual_mode = detect_mode(prompt, actual_entry)
        actual_budget = detect_budget(prompt)

        entry_ok = actual_entry == test["expected_entry"]
        mode_ok = actual_mode == test["expected_mode"]
        budget_ok = actual_budget == test["expected_budget"]

        all_ok = entry_ok and mode_ok and budget_ok

        if all_ok:
            passed += 1
            if verbose:
                print(f"  ✅ #{i:02d} [{actual_entry}/{actual_mode}/{actual_budget}] {prompt[:60]}")
        else:
            failed += 1
            print(f"  ❌ #{i:02d} {prompt[:60]}")
            if not entry_ok:
                print(f"       entry: expected={test['expected_entry']}, got={actual_entry}")
            if not mode_ok:
                print(f"       mode:  expected={test['expected_mode']}, got={actual_mode}")
            if not budget_ok:
                print(f"       budget: expected={test['expected_budget']}, got={actual_budget}")

    return passed, failed


def main():
    parser = argparse.ArgumentParser(description="Run UI Forge routing golden tests.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all test results")
    args = parser.parse_args()

    print(f"UI Forge Route Golden Tests ({len(GOLDEN_TESTS)} cases)\n")

    passed, failed = run_tests(verbose=args.verbose)

    print(f"\nResults: {passed} passed, {failed} failed out of {len(GOLDEN_TESTS)}")

    if failed > 0:
        sys.exit(1)
    else:
        print("All routing tests passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
