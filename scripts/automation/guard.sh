#!/usr/bin/env bash
# Futility guard (STRATEGY.md).  Keeps the tree from drifting back into the deleted
# Nyman-Beurling / forward-convergence / witness apparatus.  Fast, no dependencies.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

fail=0
banned=(
  "scripts/numerics/witness/hardy.py"
  "scripts/numerics/witness/forward_bound.py"
  "scripts/numerics/witness/power_test.py"
  "research-program.md"
  "research/tracker.md"
  "research/forward-theorem.md"
)
for f in "${banned[@]}"; do
  if [ -e "$f" ]; then
    echo "ERROR: '$f' is deleted futility (STRATEGY.md section 2). Do not reintroduce."
    fail=1
  fi
done

# the Lean witness apparatus (forward=RH formalization) must not return
if [ -d "RH" ] || ls ./*.lean >/dev/null 2>&1; then
  echo "ERROR: Lean witness apparatus reappeared (STRATEGY.md section 6: do not formalize ahead of the math)."
  fail=1
fi

[ "$fail" -eq 0 ] && echo "futility-guard: OK"
if [ "$fail" -eq 0 ]; then
  python3 scripts/automation/check_proof_targets.py || fail=1
fi
if [ "$fail" -eq 0 ]; then
  python3 scripts/automation/check_frontier_map.py || fail=1
fi
if [ "$fail" -eq 0 ]; then
  python3 scripts/automation/test_check_proof_targets.py || fail=1
fi

exit "$fail"
