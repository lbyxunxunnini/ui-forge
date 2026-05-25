#!/usr/bin/env bash
#
# validate_release.sh — 发布前 gate 检查
#
# 用法: bash scripts/validate_release.sh [项目根目录]
#
# 检查项:
#   1. doctor.sh 全部通过
#   2. route_golden_tests 全部通过
#   3. metadata 模块
#   4. guardrails 模块
#   5. session 模块
#   6. gates 模块
#   7. output_protocol 模块
#   8. 无未提交的 git 变更 (可选)
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
echo "[1/8] Running doctor..."
if bash scripts/doctor.sh "$ROOT" > /dev/null 2>&1; then
    ok "doctor.sh passed"
else
    fail "doctor.sh failed (run 'bash scripts/doctor.sh' for details)"
fi

# --- 2. Route golden tests ---
echo ""
echo "[2/8] Running route golden tests..."
if python3 scripts/route_golden_tests.py > /dev/null 2>&1; then
    ok "route_golden_tests.py passed"
else
    fail "route_golden_tests.py failed (run 'python3 scripts/route_golden_tests.py --verbose')"
fi

# --- 3. Metadata ---
echo ""
echo "[3/8] Metadata"

if bash scripts/check_metadata.sh "$ROOT" > /dev/null 2>&1; then
    ok "metadata contract"
else
    fail "metadata contract failed"
fi

# --- 4. Guardrails ---
echo ""
echo "[4/8] Guardrails"

if bash scripts/check_guardrails.sh "$ROOT" > /dev/null 2>&1; then
    ok "guardrails contract"
else
    fail "guardrails contract failed"
fi

# --- 5. Session ---
echo ""
echo "[5/8] Session"

if bash scripts/check_session.sh "$ROOT" > /dev/null 2>&1; then
    ok "session contract"
else
    fail "session contract failed"
fi

# --- 6. Gates ---
echo ""
echo "[6/8] Gates"

if bash scripts/check_gates.sh "$ROOT" > /dev/null 2>&1; then
    ok "gate contract"
else
    fail "gate contract failed"
fi

# --- 7. Output protocol ---
echo ""
echo "[7/8] Output protocol"

if bash scripts/check_output_protocol.sh "$ROOT" > /dev/null 2>&1; then
    ok "output protocol"
else
    fail "output protocol failed"
fi

# --- 8. Git status ---
echo ""
echo "[8/8] Git status"

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
