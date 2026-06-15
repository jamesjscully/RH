#!/usr/bin/env python3
"""Discipline checker for the proof track (disciplined-narrowing regime).

This is not a proof checker. It enforces the operating discipline restored
in the 2026-06-14 reset (see research/proof/129):

  1. The no-go bank docs declared in target-ledger.json all exist and carry
     a proper '# N - ' title. The no-go theorems are the program's primary
     product; this keeps the bank from silently rotting.
  2. The dead PFV2 construction-naming lineage is QUARANTINED: the banned
     token and the long-hyphenated "regress signature" (Cor 129.2) may
     appear only in the allowlisted autopsy doc, nowhere else under
     research/proof/. This is the anti-futility guard that stops the
     project from drifting back into the deleted regress.
  3. The navigation docs (HANDOFF/TODO/README) exist and agree on the
     restored front by carrying the discipline marker string.

Run from repo root:

    python3 scripts/automation/check_proof_targets.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "research/proof/target-ledger.json"
PROOF_DIR = ROOT / "research/proof"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise AssertionError(f"missing file: {path}")


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def _check_nogo_bank(ledger: dict, errors: list[str]) -> None:
    for entry in ledger.get("nogo_bank", []):
        rel = entry["path"]
        text = _read_text(ROOT / rel)
        doc = entry["doc"]
        _require(
            bool(re.search(rf"^# {doc} - ", text, re.MULTILINE)),
            f"{rel}: missing '# {doc} -' title",
            errors,
        )


def _check_nav_agreement(ledger: dict, errors: list[str]) -> None:
    marker = ledger["discipline_marker"]
    for rel in ledger.get("nav_docs", []):
        text = _read_text(ROOT / rel)
        _require(
            marker in text,
            f"{rel}: missing discipline marker {marker!r} (nav docs must "
            f"agree on the restored front)",
            errors,
        )


def _check_quarantine(ledger: dict, errors: list[str]) -> None:
    """The dead lineage may live only in the allowlisted autopsy doc."""
    banned = ledger["banned_lineage"]
    signature = re.compile(ledger["regress_signature"])
    allow = {(ROOT / p).resolve() for p in ledger.get("quarantine_allowlist", [])}

    for path in sorted(PROOF_DIR.glob("*.md")):
        if path.resolve() in allow:
            continue
        text = _read_text(path)
        rel = path.relative_to(ROOT)
        _require(
            banned not in text,
            f"{rel}: banned lineage token {banned!r} reappeared outside the "
            f"quarantine doc (see research/proof/129)",
            errors,
        )
        m = signature.search(text)
        if m is not None:
            errors.append(
                f"{rel}: construction-naming regress signature {m.group(0)!r} "
                f"reappeared (Cor 129.2: refactor into a witness or an "
                f"impossibility theorem)"
            )


def main() -> int:
    ledger = json.loads(_read_text(LEDGER))
    errors: list[str] = []

    # The autopsy doc itself must exist and be titled.
    autopsy = ledger["autopsy_doc"]
    _require(
        bool(re.search(r"^# 129 - ", _read_text(ROOT / autopsy), re.MULTILINE)),
        f"{autopsy}: missing '# 129 -' title",
        errors,
    )

    _check_nogo_bank(ledger, errors)
    _check_nav_agreement(ledger, errors)
    _check_quarantine(ledger, errors)

    if errors:
        print("proof-target-check: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    n = len(ledger.get("nogo_bank", []))
    print(
        f"proof-target-check: OK ({n} no-go theorems banked, "
        f"regime={ledger['regime']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
