#!/usr/bin/env python3
r"""No-go for using accepted atom/invariant payloads as residual morphism evidence.

Doc 625 kills the full accepted edge graph as residual morphism evidence. The
neighboring possibility is that the accepted atom and invariant records hide the
missing morphism in their ids, contexts, or introduction metadata.

They do not. The accepted node payloads contain no exact doc-614 residual labels
and no broad external/oracle/not/tail tokens. The generic vocabulary that does
occur is source-square infrastructure, especially "source" across nearly every
accepted node, not a residual-specific selector.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_accepted_node_payload_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACCEPTNODEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
EXACT_RESIDUAL_LABELS = (
    "boundary_externality",
    "source_internality",
    "external_or_oracle",
    "not_source_internal",
)
BROAD_RESIDUAL_TOKENS = ("external", "oracle", "not", "tail")
GENERIC_TOKENS = ("source", "internal", "boundary", "class", "obstruction")
EXPECTED_GENERIC_PAYLOAD_COUNTS = {
    "source": 104,
    "internal": 27,
    "boundary": 15,
    "class": 5,
    "obstruction": 15,
}
EXPECTED_CONTEXT_COUNTS = {
    "finite_limit": 76,
    "source_fiber": 10,
    "source_constraint": 10,
    "source_prepoint": 6,
    "certificate_image": 5,
    "finite_index": 3,
    "fixed_doc515_payload": 3,
    "graph_realization": 2,
    "original_h1": 2,
}

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def accepted_payload_entries(data: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    accepted = accepted_nodes(data)
    entries: list[tuple[str, str, dict[str, Any]]] = []
    for name, value in data["atoms"].items():
        if name in accepted:
            entries.append(("atom", name, value))
    for name, value in data["invariants"].items():
        if name in accepted:
            entries.append(("invariant", name, value))
    return entries


def payload_blob(entry: tuple[str, str, dict[str, Any]]) -> str:
    kind, name, value = entry
    return f"{kind} {name} {value}"


def payload_hits(
    entries: list[tuple[str, str, dict[str, Any]]], label: str
) -> list[tuple[str, str, dict[str, Any]]]:
    return [entry for entry in entries if label in payload_blob(entry)]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    entries = accepted_payload_entries(data)
    entry_names = {name for _, name, _ in entries}
    exact_hit_counts = {
        label: len(payload_hits(entries, label)) for label in EXACT_RESIDUAL_LABELS
    }
    broad_hit_counts = {
        label: len(payload_hits(entries, label)) for label in BROAD_RESIDUAL_TOKENS
    }
    generic_counts = {
        token: len(payload_hits(entries, token)) for token in GENERIC_TOKENS
    }
    context_counts = Counter(value["context"] for _, _, value in entries)

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc", 0) >= 610
        and DOC610_WITNESS in data.get("witnesses", {})
        and KILLCOMPEVENTSIGACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc610_witness={DOC610_WITNESS in data.get('witnesses', {})}",
    )
    gate(
        f"{PREFIX}2",
        IMPOSSIBLE_RESIDUAL_SURFACES == {EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE}
        and IMPOSSIBLE_RESIDUAL_SURFACES <= MISSING_REUSED_CLASS_STATE
        and CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        f"impossible={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}3",
        len(entries) == 117
        and sum(kind == "atom" for kind, _, _ in entries) == 106
        and sum(kind == "invariant" for kind, _, _ in entries) == 11
        and entry_names == accepted,
        f"entries={len(entries)} atoms={sum(kind == 'atom' for kind, _, _ in entries)} invariants={sum(kind == 'invariant' for kind, _, _ in entries)}",
    )
    gate(
        f"{PREFIX}4",
        all(not payload_hits(entries, label) for label in EXACT_RESIDUAL_LABELS),
        f"exact_hit_counts={exact_hit_counts}",
    )
    gate(
        f"{PREFIX}5",
        all(not payload_hits(entries, label) for label in BROAD_RESIDUAL_TOKENS),
        f"broad_hit_counts={broad_hit_counts}",
    )
    gate(
        f"{PREFIX}6",
        all(not payload_hits(entries, surface) for surface in IMPOSSIBLE_RESIDUAL_SURFACES),
        "exact residual surface strings do not occur as accepted node payload data",
    )
    gate(
        f"{PREFIX}7",
        generic_counts == EXPECTED_GENERIC_PAYLOAD_COUNTS
        and generic_counts["source"] > 100,
        f"generic_counts={generic_counts}",
    )
    gate(
        f"{PREFIX}8",
        dict(context_counts) == EXPECTED_CONTEXT_COUNTS
        and context_counts["finite_limit"] == 76
        and context_counts["source_constraint"] == 10,
        f"context_counts={dict(context_counts)}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: accepted node payload morphism reuse fails")
    print(
        "VERDICT: accepted atom/invariant payloads contain no residual labels "
        "or broad external/oracle/not/tail tokens. The visible generic "
        "vocabulary is source-square infrastructure, not residual-specific "
        "morphism evidence."
    )


if __name__ == "__main__":
    main()
