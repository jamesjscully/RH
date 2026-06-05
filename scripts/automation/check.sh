#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/scripts/tools/env.sh"

cd "$ROOT"

lake build RH
run_whip --store "$WHIP_STORE" check workflows/research-program.whip
run_loft doctor >/dev/null

echo "automation check passed"
