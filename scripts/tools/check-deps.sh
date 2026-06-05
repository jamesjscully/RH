#!/usr/bin/env bash
set -euo pipefail

source "$(dirname "$0")/env.sh"

test -d "$WHIPPLESCRIPT_REPO"
test -f "$WHIPPLESCRIPT_REPO/Cargo.toml"
test -d "$LOFT_REPO"
test -f "$LOFT_REPO/Cargo.toml"

cargo metadata --manifest-path "$WHIPPLESCRIPT_REPO/Cargo.toml" --no-deps --format-version 1 >/dev/null
cargo metadata --manifest-path "$LOFT_REPO/Cargo.toml" --no-deps --format-version 1 >/dev/null

run_whip doctor >/dev/null
run_loft --help >/dev/null

echo "local tool dependencies ok"
