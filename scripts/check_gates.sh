#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

test -f references/shared_workflow_gates/requirement_confirmation.md
test -f references/shared_workflow_gates/role_gate_matrix.md
test -f references/skill_visibility.md

for gate in core_definition current_work_unit scope_expansion plan_conflict verification_truth mode_exit; do
    grep -q "$gate" references/core_contracts.yaml
done

grep -q 'Design Task Brief' references/shared_workflow_gates/requirement_confirmation.md
grep -q 'current_work_unit' references/shared_workflow_gates/role_gate_matrix.md
grep -q 'exit_permission' references/shared_workflow_gates/role_gate_matrix.md
grep -q '明确禁止' references/shared_workflow_gates/role_gate_matrix.md
grep -q '只要 `exit_permission != true`' references/skill_visibility.md
