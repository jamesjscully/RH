#!/usr/bin/env bash
# Stub guard: fail if vacuous proof scaffolds reappear in the Lean spine.
#
# The corrected architecture forbids "theorems" that prove `True`.  A clean
# `lake build` with zero `sorry`/`axiom` is NOT evidence of progress if the
# statements are `:= True`.  This guard makes that explicit (tracker L2).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

fail=0

# strip line comments before matching so doc-comment prose can't trip the guard
if grep -rn ":= True\b" RH/ | grep -vE '^\S+:[0-9]+:\s*--' | grep -E ':= True\b' ; then
  echo "ERROR: ':= True' proposition stub(s) found -- replace with a real statement."
  fail=1
fi

# vacuous scaffold proofs in the strategy spine
if grep -rn "by trivial" RH/Strategy/ RH/Experiments/ 2>/dev/null ; then
  echo "ERROR: 'by trivial' in Strategy/Experiments -- likely a vacuous scaffold theorem."
  fail=1
fi

# sorries / axioms (belt and suspenders)
if grep -rn "\bsorry\b\|^\s*axiom\b" RH/ ; then
  echo "ERROR: sorry/axiom found in RH/."
  fail=1
fi

if [ "$fail" -eq 0 ]; then
  echo "stub-guard: OK (no := True, no trivial spine theorems, no sorry/axiom)"
fi
exit "$fail"
