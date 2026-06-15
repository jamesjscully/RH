#!/usr/bin/env python3
"""Mutation tests for check_proof_targets.py (disciplined-narrowing regime).

These tests keep the discipline checker honest. They exercise the failure
modes the checker is meant to catch without mutating repository files.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = ROOT / "scripts/automation/check_proof_targets.py"


def _load_checker():
    spec = importlib.util.spec_from_file_location("check_proof_targets", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load check_proof_targets.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_regress_signature_matches_dead_lineage() -> None:
    checker = _load_checker()
    sig = re.compile(r"[A-Z][A-Z0-9]*(-[A-Z0-9]+){5,}")
    dead = "PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE"
    if sig.search(dead) is None:
        raise AssertionError("regress signature failed to match the dead lineage")
    # A short, legitimate hyphenated token must NOT trip the guard.
    if sig.search("OC1-OC4") is not None:
        raise AssertionError("regress signature false-positived on a short token")


def test_missing_nogo_doc_fails() -> None:
    checker = _load_checker()
    ledger = {"nogo_bank": [{"doc": 999, "path": "research/proof/999-nope.md"}]}
    errors: list[str] = []
    try:
        checker._check_nogo_bank(ledger, errors)
    except AssertionError:
        return  # missing-file raises, which is also a valid failure signal
    if not errors:
        raise AssertionError("missing no-go doc was not caught")


def test_nav_missing_marker_fails(tmp_path: Path = None) -> None:
    checker = _load_checker()
    # Point a nav doc read at a string lacking the marker via monkeypatch.
    original = checker._read_text
    ledger = {
        "discipline_marker": "numerics + no-go theorems + sharp narrowing",
        "nav_docs": ["research/proof/FAKE.md"],
    }

    def fake_read(path: Path) -> str:
        return "# nav doc with no marker\n"

    checker._read_text = fake_read
    try:
        errors: list[str] = []
        checker._check_nav_agreement(ledger, errors)
        if not any("discipline marker" in e for e in errors):
            raise AssertionError("missing nav marker was not caught")
    finally:
        checker._read_text = original


def main() -> int:
    test_regress_signature_matches_dead_lineage()
    test_missing_nogo_doc_fails()
    test_nav_missing_marker_fails()
    print("proof-target-check-tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
