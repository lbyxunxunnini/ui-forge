#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

grep -q '\[ui-forge\]' SKILL.md
grep -q 'REQUIREMENTS.md' SKILL.md
grep -q 'DESIGN-GUIDE.md' SKILL.md
grep -q 'routing.json' SKILL.md
grep -q 'consistency-report.md' SKILL.md
grep -q 'SVG Visual Fallback' SKILL.md
grep -q 'visuals/' references/output_structure.md
grep -q 'iPhone 15' references/output_structure.md
grep -q 'iphone-frame' references/output_structure.md
grep -q 'Home Indicator' references/output_structure.md
