#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

test -f references/core_contracts.yaml
test -f references/task_runtime_prompt.md

for key in goal_state scope_state acceptance_state constraints_state current_work_unit work_unit_state verification_state scope_risk plan_conflict_state mode_lock exit_permission; do
    grep -q "$key" references/core_contracts.yaml
    grep -q "$key" references/task_runtime_prompt.md
done
