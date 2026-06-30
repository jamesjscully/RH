#!/usr/bin/env python3
r"""No-go for using doc610 audit fanout edges as residual morphism evidence.

Doc 621 kills historical stage-lineage diagnostics. The next existing
categorical-looking structure is the accepted doc610 audit fanout: the
compositional-event-signature certificate audits prior layers and invariant
facets.

That fanout is accepted dependency bookkeeping. It has no residual-specific
surface, class, tail, or label endpoint for the doc-614 singleton residuals.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_audit_fanout_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_EDGES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    INVARIANT_TRACE_TARGETS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMAUDITFANOUTMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
RESIDUAL_LABELS = (
    "boundary_externality",
    "source_internality",
    "external_or_oracle",
    "not_source_internal",
    "external",
    "oracle",
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def edge_tuple(edge: dict[str, Any]) -> tuple[str, str, str]:
    return (edge["source"], edge["relation"], edge["target"])


def edge_has_residual_label(edge: dict[str, Any]) -> bool:
    text = f"{edge['source']} {edge['relation']} {edge['target']}"
    return any(label in text for label in RESIDUAL_LABELS)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    edges = data["edges"]
    by_doc610 = [edge for edge in edges if edge.get("introduced_by") == 610]
    incident = [
        edge
        for edge in edges
        if edge["source"] == KILLCOMPEVENTSIGACTION
        or edge["target"] == KILLCOMPEVENTSIGACTION
    ]
    actual_edge_set = {edge_tuple(edge) for edge in by_doc610}
    relation_profile = Counter(edge["relation"] for edge in by_doc610)
    expected_profile = Counter(relation for _, relation, _ in EXPECTED_EDGES)
    invariant_targets = {
        edge["target"]
        for edge in by_doc610
        if edge["relation"] == "audits_invariant_facet_for"
    }
    outgoing = [edge for edge in by_doc610 if edge["source"] == KILLCOMPEVENTSIGACTION]
    incoming = [edge for edge in by_doc610 if edge["target"] == KILLCOMPEVENTSIGACTION]

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
        len(EXPECTED_EDGES) == 31
        and len(by_doc610) == 31
        and actual_edge_set == EXPECTED_EDGES,
        f"expected_edges={len(EXPECTED_EDGES)} doc610_edges={len(by_doc610)}",
    )
    gate(
        f"{PREFIX}4",
        len(incident) == len(by_doc610)
        and set(map(edge_tuple, incident)) == actual_edge_set
        and len(outgoing) == 30
        and len(incoming) == 1,
        f"incident={len(incident)} outgoing={len(outgoing)} incoming={len(incoming)}",
    )
    gate(
        f"{PREFIX}5",
        relation_profile == expected_profile
        and relation_profile["audits_invariant_facet_for"] == 11
        and invariant_targets == set(INVARIANT_TRACE_TARGETS),
        f"relation_profile={dict(sorted(relation_profile.items()))}",
    )
    gate(
        f"{PREFIX}6",
        all(edge["source"] in accepted and edge["target"] in accepted for edge in by_doc610),
        "every doc610 audit-fanout endpoint is an accepted atom/invariant",
    )
    gate(
        f"{PREFIX}7",
        not any(edge_has_residual_label(edge) for edge in by_doc610),
        "doc610 audit fanout has no residual surface/class/tail label endpoint",
    )
    gate(
        f"{PREFIX}8",
        all(not any(label in node for node in accepted) for label in RESIDUAL_LABELS),
        "current accepted nodes contain no residual label/tail node",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: audit-fanout morphism reuse fails")
    print(
        "VERDICT: the doc610 audit fanout is accepted dependency wiring around "
        "the compositional signature certificate. It does not supply a "
        "residual-specific morphism endpoint for boundary_externality or "
        "source_internality."
    )


if __name__ == "__main__":
    main()
