#!/usr/bin/env python3
r"""No-go for using the accepted frontier edge graph as residual morphism evidence.

Docs 620-624 kill nearby bookkeeping and metadata sources. The next broader
categorical-looking source is the full accepted edge graph in frontier-map.yaml.

That graph has accepted endpoints and substantial source/internal/boundary/class/
obstruction vocabulary, but none of the doc-614 singleton residual labels, and
none of the broad external/oracle/not/tail tokens. The generic vocabulary is
spread across many documents and relation types, so it is infrastructure rather
than a residual-specific selector.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_accepted_edge_graph_morphism_reuse_no_go
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACCEPTEDGEGRAPHMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

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
EXPECTED_GENERIC_EDGE_COUNTS = {
    "source": 1280,
    "internal": 984,
    "boundary": 414,
    "class": 157,
    "obstruction": 460,
}
EXPECTED_GENERIC_DOC_SPREAD = {
    "source": 72,
    "internal": 44,
    "boundary": 62,
    "class": 21,
    "obstruction": 15,
}
EXPECTED_GENERIC_RELATION_SPREAD = {
    "source": 662,
    "internal": 459,
    "boundary": 195,
    "class": 81,
    "obstruction": 179,
}

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def edge_blob(edge: dict[str, Any]) -> str:
    return f"{edge.get('source', '')} {edge.get('relation', '')} {edge.get('target', '')}"


def edge_hits(edges: list[dict[str, Any]], label: str) -> list[dict[str, Any]]:
    return [edge for edge in edges if label in edge_blob(edge)]


def generic_profile(edges: list[dict[str, Any]], token: str) -> tuple[int, int, int]:
    hits = edge_hits(edges, token)
    docs = Counter(edge.get("introduced_by") for edge in hits)
    relations = Counter(edge.get("relation") for edge in hits)
    return len(hits), len(docs), len(relations)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    edges = data["edges"]
    accepted = accepted_nodes(data)
    missing_endpoints = [
        edge
        for edge in edges
        if edge["source"] not in accepted or edge["target"] not in accepted
    ]

    exact_hit_counts = {
        label: len(edge_hits(edges, label)) for label in EXACT_RESIDUAL_LABELS
    }
    broad_hit_counts = {
        label: len(edge_hits(edges, label)) for label in BROAD_RESIDUAL_TOKENS
    }
    generic_edge_counts = {
        token: generic_profile(edges, token)[0] for token in GENERIC_TOKENS
    }
    generic_doc_spread = {
        token: generic_profile(edges, token)[1] for token in GENERIC_TOKENS
    }
    generic_relation_spread = {
        token: generic_profile(edges, token)[2] for token in GENERIC_TOKENS
    }

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
        len(edges) == 1801
        and len(data["current_requirements"]["atoms"]) == 106
        and len(data["current_requirements"]["invariants"]) == 11
        and len(accepted) == 117
        and not missing_endpoints,
        f"edges={len(edges)} accepted={len(accepted)} missing_endpoints={len(missing_endpoints)}",
    )
    gate(
        f"{PREFIX}4",
        all(not edge_hits(edges, label) for label in EXACT_RESIDUAL_LABELS),
        f"exact_hit_counts={exact_hit_counts}",
    )
    gate(
        f"{PREFIX}5",
        all(not edge_hits(edges, label) for label in BROAD_RESIDUAL_TOKENS),
        f"broad_hit_counts={broad_hit_counts}",
    )
    gate(
        f"{PREFIX}6",
        all(not edge_hits(edges, surface) for surface in IMPOSSIBLE_RESIDUAL_SURFACES),
        "exact residual surface strings do not occur as accepted edge data",
    )
    gate(
        f"{PREFIX}7",
        generic_edge_counts == EXPECTED_GENERIC_EDGE_COUNTS
        and generic_doc_spread == EXPECTED_GENERIC_DOC_SPREAD,
        f"generic_edge_counts={generic_edge_counts} generic_doc_spread={generic_doc_spread}",
    )
    gate(
        f"{PREFIX}8",
        generic_relation_spread == EXPECTED_GENERIC_RELATION_SPREAD
        and min(generic_doc_spread.values()) >= 15
        and min(generic_relation_spread.values()) >= 81,
        f"generic_relation_spread={generic_relation_spread}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: accepted edge graph morphism reuse fails")
    print(
        "VERDICT: the full accepted frontier edge graph has accepted endpoints "
        "but no residual labels or broad external/oracle/not/tail tokens. "
        "The remaining source/internal/boundary/class/obstruction vocabulary "
        "is diffuse infrastructure, not residual-specific morphism evidence."
    )


if __name__ == "__main__":
    main()
