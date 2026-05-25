#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

grep -q '## 铁律' SKILL.md
grep -q '失控处理' SKILL.md
grep -q '正常结束条件' SKILL.md
grep -q 'NO STAGE ADVANCE WITHOUT CONFIRMED GOAL' SKILL.md
grep -q 'Design Task Brief' SKILL.md
grep -q '仅自动补齐低风险视觉默认值' SKILL.md
