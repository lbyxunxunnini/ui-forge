#!/usr/bin/env bash
#
# doctor.sh — 一键检查 UI Forge 项目健康状态
#
# 用法: bash scripts/doctor.sh [项目根目录]
#
# 检查项:
#   1. 版本一致性 (VERSION / .skillhub.json / README.md)
#   2. 核心文件存在性
#   3. 脚本可执行性
#   4. 文档链接有效性
#   5. design-output 完整性 (如存在)
#

set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

ERRORS=0
WARNINGS=0

ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
warn() { echo -e "  ${YELLOW}⚠${NC} $1"; WARNINGS=$((WARNINGS + 1)); }
fail() { echo -e "  ${RED}✗${NC} $1"; ERRORS=$((ERRORS + 1)); }

echo "=== UI Forge Doctor ==="
echo ""

# --- 1. 版本一致性 ---
echo "[1/5] Version consistency"

if [ -f VERSION ]; then
    V_VERSION=$(cat VERSION | tr -d '[:space:]')
    ok "VERSION: $V_VERSION"
else
    fail "VERSION file missing"
    V_VERSION=""
fi

if [ -f .skillhub.json ]; then
    V_SKILLHUB=$(python3 -c "import json; print(json.load(open('.skillhub.json'))['version'])" 2>/dev/null || echo "PARSE_ERROR")
    if [ "$V_SKILLHUB" = "$V_VERSION" ]; then
        ok ".skillhub.json: $V_SKILLHUB (matches)"
    elif [ "$V_SKILLHUB" = "PARSE_ERROR" ]; then
        fail ".skillhub.json: parse error"
    else
        fail ".skillhub.json: $V_SKILLHUB (expected $V_VERSION)"
    fi
else
    fail ".skillhub.json missing"
fi

if [ -f README.md ]; then
    V_README=$(grep -oP 'Version:\s*`\K[^`]+' README.md 2>/dev/null || grep -o 'Version: `[^`]*`' README.md | head -1 | sed 's/Version: `//;s/`//' || echo "NOT_FOUND")
    if [ "$V_README" = "$V_VERSION" ]; then
        ok "README.md: $V_README (matches)"
    elif [ "$V_README" = "NOT_FOUND" ]; then
        warn "README.md: version string not found"
    else
        fail "README.md: $V_README (expected $V_VERSION)"
    fi
else
    fail "README.md missing"
fi

# --- 2. 核心文件 ---
echo ""
echo "[2/5] Core files"

CORE_FILES=(
    "SKILL.md"
    "CHANGELOG.md"
    "CONTRIBUTING.md"
    "LICENSE"
    "QUICKSTART.md"
    "CHEATSHEET.md"
)

for f in "${CORE_FILES[@]}"; do
    if [ -f "$f" ]; then
        ok "$f"
    else
        fail "$f missing"
    fi
done

# --- 3. References ---
echo ""
echo "[3/5] References"

REF_FILES=(
    "references/question_budget.md"
    "references/evaluation_rubric.md"
    "references/recipes.md"
    "references/polanyi_integration.md"
    "references/memory_protocol.md"
    "references/design_card_protocol.md"
    "references/output_structure.md"
    "references/design_tokens.md"
    "references/design_styles.md"
    "references/skill_visibility.md"
    "references/roles/requirement_analyst.md"
    "references/roles/ui_designer.md"
    "references/fast_mode.md"
    "references/autonomous_mode.md"
    "references/task_runtime_prompt.md"
    "references/input_incomplete_handling.md"
    "references/animation_effects.md"
    "references/discussion_mechanism.md"
    "references/escalation_mechanism.md"
    "references/release_playbook.md"
    "references/demo_transcript.md"
    "references/shared_workflow_gates/role_gate_matrix.md"
    "references/shared_workflow_gates/requirement_confirmation.md"
)

for f in "${REF_FILES[@]}"; do
    if [ -f "$f" ]; then
        ok "$f"
    else
        fail "$f missing"
    fi
done

# --- 4. Scripts ---
echo ""
echo "[4/5] Scripts"

SCRIPTS=(
    "scripts/project_snapshot.py"
    "scripts/init_design_card.py"
    "scripts/validate_design_card.py"
    "scripts/validate_output.py"
    "scripts/route_golden_tests.py"
    "scripts/doctor.sh"
    "scripts/validate_release.sh"
)

for s in "${SCRIPTS[@]}"; do
    if [ -f "$s" ]; then
        ok "$s"
    else
        fail "$s missing"
    fi
done

# 测试脚本可运行
echo ""
echo "  Testing script execution..."

if python3 scripts/project_snapshot.py > /dev/null 2>&1; then
    ok "project_snapshot.py runs"
else
    fail "project_snapshot.py failed to run"
fi

if python3 scripts/route_golden_tests.py > /dev/null 2>&1; then
    ok "route_golden_tests.py passes"
else
    warn "route_golden_tests.py has failures (run with --verbose)"
fi

# --- 5. Design output (optional) ---
echo ""
echo "[5/5] Design output (if exists)"

if [ -d "design-output" ]; then
    DO_FILES=("index.html" "style.css" "tokens.json" "DESIGN-GUIDE.md" "REQUIREMENTS.md")
    for f in "${DO_FILES[@]}"; do
        if [ -f "design-output/$f" ]; then
            ok "design-output/$f"
        else
            warn "design-output/$f missing"
        fi
    done

    if [ -d "design-output/icons" ]; then
        ICON_COUNT=$(ls -1 design-output/icons/*.svg 2>/dev/null | wc -l | tr -d ' ')
        if [ "$ICON_COUNT" -gt 0 ]; then
            ok "design-output/icons/ ($ICON_COUNT SVGs)"
        else
            warn "design-output/icons/ empty"
        fi
    else
        warn "design-output/icons/ missing"
    fi
else
    warn "design-output/ not found (no deliverables yet)"
fi

# --- Summary ---
echo ""
echo "=== Summary ==="
echo -e "  Errors:   ${RED}$ERRORS${NC}"
echo -e "  Warnings: ${YELLOW}$WARNINGS${NC}"

if [ "$ERRORS" -gt 0 ]; then
    echo ""
    echo -e "${RED}Doctor found $ERRORS error(s). Fix before release.${NC}"
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    echo ""
    echo -e "${YELLOW}Doctor found $WARNINGS warning(s). Review recommended.${NC}"
    exit 0
else
    echo ""
    echo -e "${GREEN}All checks passed.${NC}"
    exit 0
fi
