#!/usr/bin/env python3
r"""No-go for direct residual-pair bridge reuse.

After the frontier-map compartments are exhausted, a tempting repair is to pair
the two doc-614 singleton residuals directly and call that pair the missing
morphism. This witness checks whether that direct bridge is supported by any
existing doc-610 primitive, payload, normalized-payload, or route-token
evidence.

It is not. The two residual surfaces share no reusable primitive feature, no
exact segment, no namespace, no payload group, no action-normalized payload
group, and no route-token support. A bridge supported only by this pair is
therefore a synthetic selector unless it brings independent proof-relevant
morphism evidence.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_residual_pair_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_action_normalized_role_payload_morphism_reuse_no_go import (
    NORMALIZED_PAYLOAD_GROUPS,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    BOUNDARY_SURFACES,
    COMPOSITIONAL_SIGNATURES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_graph_anchor_morphism_reuse_no_go import (
    TOKEN_SUPPORTS,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_role_payload_morphism_reuse_no_go import (
    PAYLOAD_GROUPS,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMRESIDPAIRBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
PAIR_SEGMENT_SUPPORT_PROFILE = {
    "external": Counter(
        {
            "boundary_externality": 1,
            "classifier_partition": 1,
            "action_semantics": 1,
            "terminal_basin_entry": 1,
        }
    ),
    "or": Counter(
        {
            "boundary_externality": 1,
            "boundary_contextual_surrogate": 1,
            "classifier_partition": 2,
            "action_semantics": 1,
        }
    ),
    "oracle": Counter(
        {
            "boundary_externality": 1,
            "classifier_partition": 1,
            "action_semantics": 1,
            "terminal_basin_entry": 1,
        }
    ),
    "not": Counter(
        {
            "terminal_basin_entry": 3,
            "finite_index_budget": 1,
            "source_internality": 1,
        }
    ),
    "source": Counter(
        {
            "source_constraint_invariant": 1,
            "trace_payload_route": 1,
            "source_internality": 1,
        }
    ),
    "internal": Counter({"source_internality": 1}),
}

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["segments"])


def namespaces(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["namespaces"])


def payload_group_contains_pair(groups: dict[tuple[str, ...], tuple[str, ...]]) -> bool:
    return any(PAIR <= set(surfaces) for surfaces in groups.values())


def exact_segment_support_profile() -> dict[str, Counter[str]]:
    tokens = sorted(segments(EXTERNAL_SURFACE) | segments(SOURCE_INTERNAL_SURFACE))
    return {
        token: Counter(
            CLASS_OF[surface]
            for surface in BOUNDARY_SURFACES
            if token in SOURCE_EVENTS[surface]["segments"]
        )
        for token in tokens
    }


def token_support_contains_pair() -> bool:
    return any(PAIR <= set(surfaces) for surfaces in TOKEN_SUPPORTS.values())


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    external_event = SOURCE_EVENTS[EXTERNAL_SURFACE]
    source_internal_event = SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]
    shared_signature = set(COMPOSITIONAL_SIGNATURES[EXTERNAL_SURFACE]) & set(
        COMPOSITIONAL_SIGNATURES[SOURCE_INTERNAL_SURFACE]
    )
    segment_profile = exact_segment_support_profile()

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
        and {CLASS_OF[surface] for surface in PAIR}
        == {"boundary_externality", "source_internality"},
        f"pair_classes={sorted(CLASS_OF[surface] for surface in PAIR)}",
    )
    gate(
        f"{PREFIX}3",
        not shared_signature
        and not (segments(EXTERNAL_SURFACE) & segments(SOURCE_INTERNAL_SURFACE))
        and not (namespaces(EXTERNAL_SURFACE) & namespaces(SOURCE_INTERNAL_SURFACE)),
        f"shared_signature={shared_signature}",
    )
    gate(
        f"{PREFIX}4",
        external_event["boundary_kind"] == "entry"
        and source_internal_event["boundary_kind"] == "escape"
        and external_event["event_kind"] == "obstruction_namespace"
        and source_internal_event["event_kind"] == "plain_tail"
        and external_event["tail"] == "external_or_oracle"
        and source_internal_event["tail"] == "not_source_internal",
        "the proposed bridge crosses boundary kind, event kind, and tail type",
    )
    gate(
        f"{PREFIX}5",
        not payload_group_contains_pair(PAYLOAD_GROUPS)
        and not payload_group_contains_pair(NORMALIZED_PAYLOAD_GROUPS),
        "the residual pair is not an exact or action-normalized payload group",
    )
    gate(
        f"{PREFIX}6",
        not token_support_contains_pair()
        and TOKEN_SUPPORTS["external"] == (EXTERNAL_SURFACE,)
        and TOKEN_SUPPORTS["not_source_internal"] == (SOURCE_INTERNAL_SURFACE,),
        "route-token supports do not contain the residual pair",
    )
    gate(
        f"{PREFIX}7",
        segment_profile == PAIR_SEGMENT_SUPPORT_PROFILE,
        f"segment_profile={{{', '.join(f'{k}: {dict(v)}' for k, v in segment_profile.items())}}}",
    )
    gate(
        f"{PREFIX}8",
        Counter(CLASS_OF[surface] for surface in PAIR)
        == Counter({"boundary_externality": 1, "source_internality": 1})
        and len(PAIR) == 2,
        "a bridge supported only by the residual pair is mixed-class and exact-pair selected",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: direct residual-pair bridge reuse fails")
    print(
        "VERDICT: directly pairing the two doc614 singleton residuals is not "
        "supported by existing primitive, segment, namespace, payload, "
        "normalized-payload, or route-token evidence. It needs independent "
        "morphism evidence rather than pair selection."
    )


if __name__ == "__main__":
    main()
