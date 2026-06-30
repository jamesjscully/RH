#!/usr/bin/env python3
"""Validate the proof frontier map.

This is a structural checker, not a proof checker. It keeps
research/proof/frontier-map.yaml from becoming another prose ledger by
requiring its doc, witness, and graph references to resolve.

Run from repo root:

    python3 scripts/automation/check_frontier_map.py
    python3 scripts/automation/check_frontier_map.py --run-current
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "frontier-map-check: FAIL\n"
        "  - PyYAML is required to validate research/proof/frontier-map.yaml"
    ) from exc


ROOT = Path(__file__).resolve().parents[2]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
PROOF_DIR = ROOT / "research/proof"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise AssertionError(f"missing file: {path.relative_to(ROOT)}")


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def _doc_exists(doc: int) -> bool:
    return any(PROOF_DIR.glob(f"{doc}-*.md"))


def _module_for_witness(path: str) -> str:
    rel = Path(path)
    if rel.suffix != ".py":
        raise AssertionError(f"{path}: witness path must end in .py")
    return ".".join(rel.with_suffix("").parts)


def _load_map() -> dict[str, Any]:
    data = yaml.safe_load(_read_text(MAP_PATH))
    if not isinstance(data, dict):
        raise AssertionError("frontier-map.yaml must load as a mapping")
    return data


def _nodes(data: dict[str, Any]) -> set[str]:
    return set(data.get("atoms", {})) | set(data.get("invariants", {}))


def _current_sets(data: dict[str, Any]) -> tuple[set[str], set[str]]:
    current = data.get("current_requirements", {})
    accepted = set(current.get("atoms", [])) | set(current.get("invariants", []))
    rejected = set(current.get("rejected_repairs", []))
    return accepted, rejected


def _check_docs(data: dict[str, Any], errors: list[str]) -> None:
    deltas = data.get("deltas", {})
    _require(isinstance(deltas, dict) and bool(deltas), "deltas must be a nonempty mapping", errors)

    for key, delta in deltas.items():
        if not isinstance(delta, dict):
            errors.append(f"deltas.{key}: must be a mapping")
            continue
        doc = delta.get("doc")
        path = delta.get("path")
        _require(isinstance(doc, int), f"deltas.{key}.doc must be an integer", errors)
        _require(isinstance(path, str), f"deltas.{key}.path must be a string", errors)
        if isinstance(doc, int):
            _require(_doc_exists(doc), f"deltas.{key}: no research/proof/{doc}-*.md doc exists", errors)
        if isinstance(doc, int) and isinstance(path, str):
            full_path = ROOT / path
            text = _read_text(full_path)
            _require(
                text.startswith(f"# {doc} - "),
                f"{path}: title must start with '# {doc} - '",
                errors,
            )


def _check_witnesses(data: dict[str, Any], errors: list[str]) -> None:
    witnesses = data.get("witnesses", {})
    deltas = data.get("deltas", {})
    _require(
        isinstance(witnesses, dict) and bool(witnesses),
        "witnesses must be a nonempty mapping",
        errors,
    )

    for key, witness in witnesses.items():
        if not isinstance(witness, dict):
            errors.append(f"witnesses.{key}: must be a mapping")
            continue
        doc = witness.get("doc")
        path = witness.get("path")
        gate_prefix = witness.get("gate_prefix")
        gates = witness.get("gates")
        _require(isinstance(doc, int), f"witnesses.{key}.doc must be an integer", errors)
        _require(isinstance(path, str), f"witnesses.{key}.path must be a string", errors)
        _require(
            isinstance(gate_prefix, str) and gate_prefix,
            f"witnesses.{key}.gate_prefix must be a nonempty string",
            errors,
        )
        _require(isinstance(gates, int) and gates > 0, f"witnesses.{key}.gates must be positive", errors)
        if isinstance(path, str):
            text = _read_text(ROOT / path)
            if isinstance(gate_prefix, str):
                _require(gate_prefix in text, f"{path}: missing gate prefix {gate_prefix}", errors)

    for delta_key, delta in deltas.items():
        if not isinstance(delta, dict):
            continue
        witness_key = delta.get("witness")
        _require(
            isinstance(witness_key, str) and witness_key in witnesses,
            f"deltas.{delta_key}.witness must name an existing witness",
            errors,
        )
        if isinstance(witness_key, str) and witness_key in witnesses:
            _require(
                witnesses[witness_key].get("doc") == delta.get("doc"),
                f"deltas.{delta_key}.witness doc must match delta doc",
                errors,
            )


def _check_graph(data: dict[str, Any], errors: list[str]) -> None:
    atoms = data.get("atoms", {})
    invariants = data.get("invariants", {})
    edges = data.get("edges", [])
    _require(isinstance(atoms, dict) and bool(atoms), "atoms must be a nonempty mapping", errors)
    _require(isinstance(invariants, dict), "invariants must be a mapping", errors)
    _require(isinstance(edges, list) and bool(edges), "edges must be a nonempty list", errors)

    nodes = set(atoms) | set(invariants)
    docs_to_check: set[int] = set()

    for atom_key, atom in atoms.items():
        if not isinstance(atom, dict):
            errors.append(f"atoms.{atom_key}: must be a mapping")
            continue
        _require(isinstance(atom.get("id"), str) and atom["id"], f"atoms.{atom_key}.id missing", errors)
        doc = atom.get("introduced_by")
        _require(isinstance(doc, int), f"atoms.{atom_key}.introduced_by must be an integer", errors)
        if isinstance(doc, int):
            docs_to_check.add(doc)

    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}]: must be a mapping")
            continue
        for field in ("source", "relation", "target"):
            _require(isinstance(edge.get(field), str) and edge[field], f"edges[{i}].{field} missing", errors)
        for endpoint in ("source", "target", "via"):
            val = edge.get(endpoint)
            if val is not None:
                _require(val in nodes, f"edges[{i}].{endpoint}={val!r} is not a known atom/invariant", errors)
        doc = edge.get("introduced_by")
        _require(isinstance(doc, int), f"edges[{i}].introduced_by must be an integer", errors)
        if isinstance(doc, int):
            docs_to_check.add(doc)

    for key, repair in data.get("rejected_repairs", {}).items():
        if not isinstance(repair, dict):
            errors.append(f"rejected_repairs.{key}: must be a mapping")
            continue
        doc = repair.get("rejected_by")
        _require(isinstance(doc, int), f"rejected_repairs.{key}.rejected_by must be an integer", errors)
        if isinstance(doc, int):
            docs_to_check.add(doc)

    for doc in sorted(docs_to_check):
        _require(_doc_exists(doc), f"introduced/rejected doc {doc} has no research/proof/{doc}-*.md file", errors)


def _check_contexts(data: dict[str, Any], errors: list[str]) -> None:
    contexts = data.get("contexts", {})
    atoms = data.get("atoms", {})
    invariants = data.get("invariants", {})
    bridges = data.get("context_bridges", {})
    claims = data.get("claims", {})
    known_nodes = _nodes(data)

    _require(isinstance(contexts, dict) and bool(contexts), "contexts must be a nonempty mapping", errors)
    for key, entry in {**atoms, **invariants}.items():
        if not isinstance(entry, dict):
            continue
        context = entry.get("context")
        _require(isinstance(context, str), f"{key}: context must be a string", errors)
        if isinstance(context, str):
            _require(context in contexts, f"{key}: unknown context {context!r}", errors)

    _require(isinstance(bridges, dict), "context_bridges must be a mapping", errors)
    for key, bridge in bridges.items():
        if not isinstance(bridge, dict):
            errors.append(f"context_bridges.{key}: must be a mapping")
            continue
        for field in ("from", "to", "direction"):
            _require(
                isinstance(bridge.get(field), str) and bridge[field],
                f"context_bridges.{key}.{field} missing",
                errors,
            )
        for field in ("from", "to"):
            context = bridge.get(field)
            if isinstance(context, str):
                _require(
                    context in contexts,
                    f"context_bridges.{key}.{field}={context!r} is not a declared context",
                    errors,
                )
        doc = bridge.get("introduced_by")
        _require(isinstance(doc, int), f"context_bridges.{key}.introduced_by must be an integer", errors)
        if isinstance(doc, int):
            _require(_doc_exists(doc), f"context bridge {key}: doc {doc} does not exist", errors)

    _require(isinstance(claims, dict), "claims must be a mapping", errors)
    for key, claim in claims.items():
        if not isinstance(claim, dict):
            errors.append(f"claims.{key}: must be a mapping")
            continue
        subject = claim.get("subject")
        context = claim.get("context")
        _require(subject in known_nodes, f"claims.{key}.subject={subject!r} is unknown", errors)
        _require(context in contexts, f"claims.{key}.context={context!r} is unknown", errors)
        _require(
            isinstance(claim.get("predicate"), str) and claim["predicate"],
            f"claims.{key}.predicate missing",
            errors,
        )
        if subject in atoms:
            _require(
                atoms[subject].get("context") == context,
                f"claims.{key}: context {context!r} does not match atom {subject!r}",
                errors,
            )
        if subject in invariants:
            _require(
                invariants[subject].get("context") == context,
                f"claims.{key}: context {context!r} does not match invariant {subject!r}",
                errors,
            )
        bridge = claim.get("bridge")
        if bridge is not None:
            _require(bridge in bridges, f"claims.{key}.bridge={bridge!r} is unknown", errors)


def _check_current_requirements(data: dict[str, Any], errors: list[str]) -> None:
    current = data.get("current_requirements", {})
    atoms = data.get("atoms", {})
    invariants = data.get("invariants", {})
    repairs = data.get("rejected_repairs", {})
    current_doc = data.get("frontier", {}).get("current_doc")
    _require(isinstance(current, dict), "current_requirements must be a mapping", errors)
    _require(isinstance(current_doc, int), "frontier.current_doc must be an integer", errors)

    accepted, rejected = _current_sets(data)
    for key in current.get("atoms", []):
        _require(key in atoms, f"current_requirements.atoms contains unknown atom {key!r}", errors)
        doc = atoms.get(key, {}).get("introduced_by")
        if isinstance(doc, int) and isinstance(current_doc, int):
            _require(doc <= current_doc, f"current atom {key!r} is introduced after current_doc", errors)
    for key in current.get("invariants", []):
        _require(
            key in invariants,
            f"current_requirements.invariants contains unknown invariant {key!r}",
            errors,
        )
    for key in current.get("rejected_repairs", []):
        _require(
            key in repairs,
            f"current_requirements.rejected_repairs contains unknown repair {key!r}",
            errors,
        )
        doc = repairs.get(key, {}).get("rejected_by")
        if isinstance(doc, int) and isinstance(current_doc, int):
            _require(doc <= current_doc, f"current rejected repair {key!r} is rejected after current_doc", errors)

    overlap = accepted & rejected
    _require(not overlap, f"current requirements both accept and reject {sorted(overlap)}", errors)

    for edge_num, edge in enumerate(data.get("edges", [])):
        doc = edge.get("introduced_by")
        if isinstance(doc, int) and isinstance(current_doc, int):
            _require(doc <= current_doc, f"edges[{edge_num}] is introduced after current_doc", errors)


def _check_consistency_rules(data: dict[str, Any], errors: list[str]) -> None:
    rules = data.get("consistency_rules", {})
    claims = data.get("claims", {})
    bridges = data.get("context_bridges", {})
    known = _nodes(data) | set(data.get("rejected_repairs", {}))
    accepted, rejected = _current_sets(data)

    _require(isinstance(rules, dict), "consistency_rules must be a mapping", errors)

    for key, required in rules.get("requires", {}).items():
        _require(key in known, f"consistency_rules.requires.{key}: unknown key", errors)
        _require(isinstance(required, list), f"consistency_rules.requires.{key}: must be a list", errors)
        if key in accepted:
            for req in required:
                _require(req in known, f"consistency_rules.requires.{key}: unknown requirement {req!r}", errors)
                _require(req in accepted, f"current requirement {key!r} is missing required {req!r}", errors)
                _require(req not in rejected, f"current requirement {key!r} requires rejected {req!r}", errors)

    for key, excluded in rules.get("excludes_current", {}).items():
        _require(key in known, f"consistency_rules.excludes_current.{key}: unknown key", errors)
        _require(isinstance(excluded, list), f"consistency_rules.excludes_current.{key}: must be a list", errors)
        if key in accepted:
            for bad in excluded:
                _require(bad in known, f"consistency_rules.excludes_current.{key}: unknown exclusion {bad!r}", errors)
                _require(
                    bad not in accepted,
                    f"current requirement {key!r} conflicts with accepted {bad!r}",
                    errors,
                )

    for i, rule in enumerate(rules.get("context_separation", [])):
        if not isinstance(rule, dict):
            errors.append(f"consistency_rules.context_separation[{i}]: must be a mapping")
            continue
        bridge = rule.get("bridge")
        _require(bridge in bridges, f"context_separation[{i}].bridge={bridge!r} is unknown", errors)
        left_claim = rule.get("left_claim")
        right_claim = rule.get("right_claim")
        if left_claim and right_claim:
            _require(left_claim in claims, f"context_separation[{i}].left_claim is unknown", errors)
            _require(right_claim in claims, f"context_separation[{i}].right_claim is unknown", errors)
            if left_claim in claims and right_claim in claims and rule.get("must_differ"):
                _require(
                    claims[left_claim].get("context") != claims[right_claim].get("context"),
                    f"context_separation[{i}]: claims collapse into the same context",
                    errors,
                )
        forbidden = rule.get("forbidden_context")
        if left_claim and forbidden and left_claim in claims:
            _require(
                claims[left_claim].get("context") != forbidden,
                f"context_separation[{i}]: claim {left_claim!r} is in forbidden context {forbidden!r}",
                errors,
            )


def _check_kill_frontier(data: dict[str, Any], errors: list[str]) -> None:
    kill = data.get("kill_frontier", {})
    _require(isinstance(kill, dict), "kill_frontier must be a mapping", errors)
    current = kill.get("current", [])
    _require(isinstance(current, list) and bool(current), "kill_frontier.current must be a nonempty list", errors)
    seen: set[str] = set()
    for i, entry in enumerate(current):
        if not isinstance(entry, dict):
            errors.append(f"kill_frontier.current[{i}]: must be a mapping")
            continue
        for field in ("id", "target", "would_kill"):
            _require(
                isinstance(entry.get(field), str) and entry[field],
                f"kill_frontier.current[{i}].{field} missing",
                errors,
            )
        ident = entry.get("id")
        if isinstance(ident, str):
            _require(ident not in seen, f"kill_frontier id {ident!r} is duplicated", errors)
            seen.add(ident)


def _check_current(data: dict[str, Any], errors: list[str]) -> None:
    frontier = data.get("frontier", {})
    deltas = data.get("deltas", {})
    witnesses = data.get("witnesses", {})
    _require(isinstance(frontier, dict), "frontier must be a mapping", errors)

    current_doc = frontier.get("current_doc")
    current_delta = frontier.get("current_delta")
    current_witness = frontier.get("current_witness")
    _require(isinstance(current_doc, int), "frontier.current_doc must be an integer", errors)
    _require(isinstance(current_delta, str), "frontier.current_delta must be a string", errors)
    _require(isinstance(current_witness, str), "frontier.current_witness must be a string", errors)
    if isinstance(current_delta, str) and current_delta in deltas:
        _require(
            deltas[current_delta].get("doc") == current_doc,
            "frontier.current_delta doc must match frontier.current_doc",
            errors,
        )
    else:
        errors.append("frontier.current_delta must name an existing delta")
    if isinstance(current_witness, str) and current_witness in witnesses:
        _require(
            witnesses[current_witness].get("doc") == current_doc,
            "frontier.current_witness doc must match frontier.current_doc",
            errors,
        )
    else:
        errors.append("frontier.current_witness must name an existing witness")


def _run_current(data: dict[str, Any], errors: list[str]) -> None:
    current_witness = data["frontier"]["current_witness"]
    witness = data["witnesses"][current_witness]
    module = _module_for_witness(witness["path"])
    proc = subprocess.run(
        [sys.executable, "-m", module],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        errors.append(f"{module}: current witness failed with exit {proc.returncode}\n{proc.stdout}")
        return
    expected = f"{witness['gate_prefix']}1-{witness['gate_prefix']}{witness['gates']} ALL PASS"
    if expected not in proc.stdout:
        errors.append(f"{module}: missing expected pass line {expected!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-current", action="store_true", help="also execute the current witness")
    args = parser.parse_args()

    errors: list[str] = []
    try:
        data = _load_map()
        _require(data.get("schema_version") == 1, "schema_version must be 1", errors)
        _check_docs(data, errors)
        _check_witnesses(data, errors)
        _check_graph(data, errors)
        _check_contexts(data, errors)
        _check_current(data, errors)
        _check_current_requirements(data, errors)
        _check_consistency_rules(data, errors)
        _check_kill_frontier(data, errors)
        if args.run_current and not errors:
            _run_current(data, errors)
    except AssertionError as exc:
        errors.append(str(exc))

    if errors:
        print("frontier-map-check: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    current_doc = data["frontier"]["current_doc"]
    print(
        "frontier-map-check: OK "
        f"(current_doc={current_doc}, atoms={len(data['atoms'])}, edges={len(data['edges'])})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
