#!/usr/bin/env bash
#
# validate_release.sh — 发布前 gate 检查
#
# 用法: bash scripts/validate_release.sh [项目根目录]
#
# 检查项:
#   1. doctor.sh 全部通过
#   2. route_golden_tests 全部通过
#   3. 版本号格式正确 (vX.Y.Z)
#   4. CHANGELOG 包含当前版本条目
#   5. SKILL.md frontmatter 存在
#   6. 无未提交的 git 变更 (可选)
#

set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

ERRORS=0

ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
fail() { echo -e "  ${RED}✗${NC} $1"; ERRORS=$((ERRORS + 1)); }
warn() { echo -e "  ${YELLOW}⚠${NC} $1"; }

echo "=== UI Forge Release Validation ==="
echo ""

# --- 1. Doctor ---
echo "[1/6] Running doctor..."
if bash scripts/doctor.sh "$ROOT" > /dev/null 2>&1; then
    ok "doctor.sh passed"
else
    fail "doctor.sh failed (run 'bash scripts/doctor.sh' for details)"
fi

# --- 2. Route golden tests ---
echo ""
echo "[2/6] Running route golden tests..."
if python3 scripts/route_golden_tests.py > /dev/null 2>&1; then
    ok "route_golden_tests.py passed"
else
    fail "route_golden_tests.py failed (run 'python3 scripts/route_golden_tests.py --verbose')"
fi

# --- 3. Version format ---
echo ""
echo "[3/6] Version format"

if [ -f VERSION ]; then
    V=$(cat VERSION | tr -d '[:space:]')
    if [[ "$V" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        ok "VERSION format: $V"
    else
        fail "VERSION format invalid: '$V' (expected vX.Y.Z)"
    fi
else
    fail "VERSION file missing"
fi

# --- 4. CHANGELOG entry ---
echo ""
echo "[4/6] CHANGELOG entry"

if [ -f CHANGELOG.md ]; then
    if grep -q "## \[$V\]" CHANGELOG.md; then
        ok "CHANGELOG contains [$V]"
    else
        fail "CHANGELOG missing [$V] entry"
    fi
else
    fail "CHANGELOG.md missing"
fi

# --- 5. SKILL.md frontmatter ---
echo ""
echo "[5/6] SKILL.md frontmatter"

if [ -f SKILL.md ]; then
    FIRST_LINE=$(head -1 SKILL.md)
    if [ "$FIRST_LINE" = "---" ]; then
        # 检查是否有 name 和 description (macOS compatible)
        HAS_NAME=$(head -10 SKILL.md | grep -c '^name:' || true)
        HAS_DESC=$(head -10 SKILL.md | grep -c '^description:' || true)
        if [ "$HAS_NAME" -gt 0 ] && [ "$HAS_DESC" -gt 0 ]; then
            ok "SKILL.md frontmatter: name + description present"
        else
            fail "SKILL.md frontmatter: missing name or description"
        fi
    else
        fail "SKILL.md: no frontmatter (first line is not ---)"
    fi
else
    fail "SKILL.md missing"
fi

# --- 6. Git status ---
echo ""
echo "[6/6] Git status"

if git rev-parse --git-dir > /dev/null 2>&1; then
    DIRTY=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    if [ "$DIRTY" -eq 0 ]; then
        ok "Working tree clean"
    else
        warn "Working tree has $DIRTY uncommitted change(s)"
    fi
else
    warn "Not a git repository"
fi

# --- Summary ---
echo ""
echo "=== Summary ==="
echo -e "  Errors: ${RED}$ERRORS${NC}"

if [ "$ERRORS" -gt 0 ]; then
    echo ""
    echo -e "${RED}Release validation FAILED. Fix $ERRORS error(s) before releasing.${NC}"
    exit 1
else
    echo ""
    echo -e "${GREEN}Release validation passed. Ready to release.${NC}"
    exit 0
fi
