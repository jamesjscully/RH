#!/usr/bin/env bash
set -euo pipefail

source "$(dirname "$0")/env.sh"

cargo install --path "$LOFT_REPO" --locked
cargo install --path "$WHIPPLESCRIPT_REPO/crates/whipplescript-cli" --locked

echo "installed loft and whip from local repos"
