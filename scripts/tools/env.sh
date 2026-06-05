#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WHIPPLESCRIPT_REPO="${WHIPPLESCRIPT_REPO:-"$ROOT/../whipplescript"}"
LOFT_REPO="${LOFT_REPO:-"$ROOT/../loft"}"
WHIP_STORE="${WHIP_STORE:-"$ROOT/.whipplescript/research.sqlite"}"

WHIP_BIN="${WHIP_BIN:-whip}"
LOFT_BIN="${LOFT_BIN:-loft}"

run_whip() {
  if command -v "$WHIP_BIN" >/dev/null 2>&1; then
    "$WHIP_BIN" "$@"
  else
    cargo run --manifest-path "$WHIPPLESCRIPT_REPO/Cargo.toml" -p whipplescript -- "$@"
  fi
}

run_loft() {
  if command -v "$LOFT_BIN" >/dev/null 2>&1; then
    "$LOFT_BIN" "$@"
  else
    cargo run --manifest-path "$LOFT_REPO/Cargo.toml" -- "$@"
  fi
}
