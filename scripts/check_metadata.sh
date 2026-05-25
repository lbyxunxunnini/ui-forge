#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

test -f VERSION
test -f README.md
test -f CHANGELOG.md
test -f SKILL.md

V=$(tr -d '[:space:]' < VERSION)
[[ "$V" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]
grep -q "Version: \`$V\`" README.md
grep -q "## \[$V\]" CHANGELOG.md
head -1 SKILL.md | grep -q '^---$'
grep -q '^name:' SKILL.md
grep -q '^description:' SKILL.md
! rg -n 'uif-critique|uif-deliver|uid-|/ui-design' README.md QUICKSTART.md CHEATSHEET.md references/demo_transcript.md scripts/route_golden_tests.py > /dev/null
