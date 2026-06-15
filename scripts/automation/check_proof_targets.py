#!/usr/bin/env python3
"""Validate the proof target ledger against the markdown routing docs.

This is a discipline check, not a proof checker. It makes the current
research trajectory machine-auditable enough to catch the failure mode where
docs are created quickly but HANDOFF/TODO/dispatch records silently drift.

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


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise AssertionError(f"missing file: {path.relative_to(ROOT)}")


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def _contains(text: str, needle: str) -> bool:
    return needle in text


def _has_section(text: str, phrase: str) -> bool:
    return bool(
        re.search(rf"^##+ (?:\d+\. )?.*{re.escape(phrase)}", text, re.MULTILINE)
    )


def _require_sections(
    rel: Path,
    text: str,
    sections: tuple[str, ...],
    errors: list[str],
) -> None:
    for section in sections:
        _require(
            _has_section(text, section),
            f"{rel}: missing required section containing {section!r}",
            errors,
        )


def _check_doc_entry(entry: dict, errors: list[str]) -> None:
    rel = Path(entry["path"])
    path = ROOT / rel
    text = _read_text(path)

    doc = entry["doc"]
    title_re = re.compile(rf"^# {doc} - ", re.MULTILINE)
    _require(bool(title_re.search(text)), f"{rel}: missing '# {doc} -' title", errors)

    for key in ("target", "next_target", "verdict"):
        value = entry[key]
        _require(
            _contains(text, value),
            f"{rel}: missing ledger {key} {value!r}",
            errors,
        )

    kind = entry["kind"]
    if kind == "shot":
        _require_sections(
            rel,
            text,
            (
                "Candidate Record",
                "Gate Run",
                "Current Verdict",
                "Sharpened Theorem Target",
                "Kill Conditions",
            ),
            errors,
        )
        _require(
            f"SHARPEN to {entry['next_target']}" in text,
            f"{rel}: shot entry lacks exact SHARPEN to {entry['next_target']}",
            errors,
        )
        _require(
            "candidate" in text.lower() or "source record" in text.lower(),
            f"{rel}: shot entry lacks candidate/source-record language",
            errors,
        )
    elif kind == "no-go":
        _require_sections(
            rel,
            text,
            (
                "Covered Class",
                "Lemma",
                "Proof",
                "Surviving Escape",
                "Kill Conditions",
            ),
            errors,
        )
        _require(
            f"does not satisfy {entry['target']}" in text,
            f"{rel}: no-go entry lacks exact 'does not satisfy {entry['target']}'",
            errors,
        )
        _require(
            f"still live only through {entry['next_target']}" in text,
            f"{rel}: no-go entry lacks exact live-route phrase for {entry['next_target']}",
            errors,
        )
        _require(
            "does not satisfy" in text or "reject" in text.lower(),
            f"{rel}: no-go entry lacks rejection language",
            errors,
        )
    else:
        errors.append(f"{rel}: unknown kind {kind!r}")


def _check_chain(entries: list[dict], current_target: str, errors: list[str]) -> None:
    docs = [entry["doc"] for entry in entries]
    _require(docs == sorted(docs), f"ledger entries are not sorted: {docs}", errors)
    _require(len(set(docs)) == len(docs), "ledger contains duplicate doc ids", errors)

    for prev, cur in zip(entries, entries[1:]):
        _require(
            prev["next_target"] == cur["target"],
            (
                f"broken target chain: doc {prev['doc']} next_target "
                f"{prev['next_target']!r} != doc {cur['doc']} target {cur['target']!r}"
            ),
            errors,
        )

    if entries:
        _require(
            entries[-1]["next_target"] == current_target,
            (
                f"current_target {current_target!r} does not match final next_target "
                f"{entries[-1]['next_target']!r}"
            ),
            errors,
        )


def _check_active_slots(slots: list[dict], errors: list[str]) -> None:
    for slot in slots:
        rel = Path(slot["path"])
        text = _read_text(ROOT / rel)
        for pattern in slot["patterns"]:
            _require(
                pattern in text,
                f"{rel}: missing active-slot pattern {pattern!r}",
                errors,
            )


def _check_doc_range(ledger: dict, entries: list[dict], errors: list[str]) -> None:
    doc_range = ledger.get("doc_range", {})
    start = doc_range.get("start")
    end = doc_range.get("end")
    if start is None or end is None:
        errors.append("ledger doc_range must contain start and end")
        return

    docs = [entry["doc"] for entry in entries]
    expected = list(range(start, end + 1))
    _require(
        docs == expected,
        f"ledger docs {docs} do not match declared doc_range {expected}",
        errors,
    )


def main() -> int:
    ledger = json.loads(_read_text(LEDGER))
    entries = ledger["entries"]
    errors: list[str] = []

    _check_doc_range(ledger, entries, errors)
    _check_chain(entries, ledger["current_target"], errors)
    for entry in entries:
        _check_doc_entry(entry, errors)
    _check_active_slots(ledger.get("active_slots", []), errors)

    if errors:
        print("proof-target-check: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "proof-target-check: OK "
        f"({len(entries)} docs, current={ledger['current_target']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
