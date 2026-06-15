#!/usr/bin/env python3
"""Mutation tests for check_proof_targets.py.

These tests keep the trajectory checker honest. They exercise the failure
modes the checker is meant to catch without mutating repository files.
"""
from __future__ import annotations

import importlib.util
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


def _with_fake_reader(checker, docs: dict[str, str], fn) -> None:
    original = checker._read_text

    def fake_read_text(path: Path) -> str:
        rel = path.relative_to(ROOT).as_posix()
        if rel in docs:
            return docs[rel]
        raise AssertionError(f"unexpected read: {rel}")

    checker._read_text = fake_read_text
    try:
        fn()
    finally:
        checker._read_text = original


def test_keyword_only_shot_fails() -> None:
    checker = _load_checker()
    entry = {
        "doc": 999,
        "path": "research/proof/999-shot.md",
        "target": "TARGET-A",
        "next_target": "TARGET-B",
        "kind": "shot",
        "verdict": "LOCAL_SCHEMA_PASS",
    }
    text = "# 999 - Shot\nTARGET-A\nTARGET-B\nLOCAL_SCHEMA_PASS\ncandidate\n"

    def run() -> None:
        errors: list[str] = []
        checker._check_doc_entry(entry, errors)
        if not any("missing required section" in error for error in errors):
            raise AssertionError(f"keyword-only shot unexpectedly passed: {errors}")

    _with_fake_reader(checker, {entry["path"]: text}, run)


def test_keyword_only_no_go_fails() -> None:
    checker = _load_checker()
    entry = {
        "doc": 998,
        "path": "research/proof/998-no-go.md",
        "target": "TARGET-A",
        "next_target": "TARGET-B",
        "kind": "no-go",
        "verdict": "REJECT_STUB",
    }
    text = (
        "# 998 - No-go\n"
        "TARGET-A\nTARGET-B\nREJECT_STUB\n"
        "`stub` does not satisfy TARGET-A.\n"
    )

    def run() -> None:
        errors: list[str] = []
        checker._check_doc_entry(entry, errors)
        if not any("missing required section" in error for error in errors):
            raise AssertionError(f"keyword-only no-go unexpectedly passed: {errors}")
        if not any("live-route phrase" in error for error in errors):
            raise AssertionError(f"no-go live-route mutation was not caught: {errors}")

    _with_fake_reader(checker, {entry["path"]: text}, run)


def test_broken_chain_fails() -> None:
    checker = _load_checker()
    entries = [
        {"doc": 1, "target": "A", "next_target": "B"},
        {"doc": 2, "target": "C", "next_target": "D"},
    ]
    errors: list[str] = []
    checker._check_chain(entries, "D", errors)
    if not any("broken target chain" in error for error in errors):
        raise AssertionError(f"broken chain was not caught: {errors}")


def main() -> int:
    test_keyword_only_shot_fails()
    test_keyword_only_no_go_fails()
    test_broken_chain_fails()
    print("proof-target-check-tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
