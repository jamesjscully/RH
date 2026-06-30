#!/usr/bin/env python3
r"""No-go for semantic-polarity bridge morphism reuse.

Doc 629 kills the direct pair bridge between the two doc614 singleton
residual surfaces. The next plausible bridge is semantic polarity: put
external/oracle and not/source/internal into one noninternality family and
use that family as the missing morphism evidence.

This witness checks the visible doc610 source-event segment algebra. Broad
semantic closures are reused, but they are mixed-class. Exact polarity
closures are class-pure only when they collapse back to singleton residual
lookup, while the exact external_or_oracle closure is the already-killed
action/class/obstruction triple.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_semantic_polarity_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    BOUNDARY_SURFACES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSEMPOLARITYBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

ACTION_VERBS = frozenset({"reject", "emit"})
EXTERNAL_ACTION_SURFACE = "entry_boundary:action:reject_external_or_oracle"
EXTERNAL_CLASS_SURFACE = "entry_boundary:class:external_or_oracle"
PRESENTATION_CLASS_SURFACE = "entry_boundary:class:presentation_or_sample"
EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
PRESENTATION_OBSTRUCTION_SURFACE = "entry_boundary:obstruction:presentation_or_sample"
SOURCE_BEFORE_POINTS_SURFACE = "entry_boundary:invariant:source_before_points"
TRACE_SOURCE_LAW_SURFACE = "entry_boundary:payload:trace_source_law"
BASIN_NOT_ABSORBING_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_basin_not_absorbing"
)
BASIN_NOT_EXTENSIONAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_basin_not_extensional"
)
ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_entry_trace_not_replay_stable"
)
EXTERNAL_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_external_basin"
)
NOT_BUDGETED_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted"
)
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
ORACLE_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_oracle_basin"
)

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
EXTERNAL_ORACLE_SURFACES = (
    EXTERNAL_ACTION_SURFACE,
    EXTERNAL_CLASS_SURFACE,
    EXTERNAL_SURFACE,
    EXTERNAL_BASIN_SURFACE,
    ORACLE_BASIN_SURFACE,
)
NOT_SOURCE_INTERNAL_SURFACES = (
    SOURCE_BEFORE_POINTS_SURFACE,
    TRACE_SOURCE_LAW_SURFACE,
    BASIN_NOT_ABSORBING_SURFACE,
    BASIN_NOT_EXTENSIONAL_SURFACE,
    ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE,
    NOT_BUDGETED_SURFACE,
    SOURCE_INTERNAL_SURFACE,
)
NONINTERNAL_SURFACES = (
    EXTERNAL_ACTION_SURFACE,
    EXTERNAL_CLASS_SURFACE,
    SOURCE_BEFORE_POINTS_SURFACE,
    EXTERNAL_SURFACE,
    TRACE_SOURCE_LAW_SURFACE,
    BASIN_NOT_ABSORBING_SURFACE,
    BASIN_NOT_EXTENSIONAL_SURFACE,
    ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE,
    EXTERNAL_BASIN_SURFACE,
    NOT_BUDGETED_SURFACE,
    SOURCE_INTERNAL_SURFACE,
    ORACLE_BASIN_SURFACE,
)
NORMALIZED_EXTERNAL_OR_ORACLE_SURFACES = (
    EXTERNAL_ACTION_SURFACE,
    EXTERNAL_CLASS_SURFACE,
    EXTERNAL_SURFACE,
)
CONNECTOR_OR_SURFACES = (
    EXTERNAL_ACTION_SURFACE,
    EXTERNAL_CLASS_SURFACE,
    PRESENTATION_CLASS_SURFACE,
    EXTERNAL_SURFACE,
    PRESENTATION_OBSTRUCTION_SURFACE,
    EXTERNAL_BASIN_SURFACE,
    ORACLE_BASIN_SURFACE,
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def raw_segments(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def normalized_segments(surface: str) -> tuple[str, ...]:
    segments = raw_segments(surface)
    if (
        SOURCE_EVENTS[surface]["event_kind"] == "action_namespace"
        and segments
        and segments[0] in ACTION_VERBS
    ):
        return segments[1:]
    return segments


def surfaces_with_any(tokens: set[str], *, normalized: bool = False) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if set(normalized_segments(surface) if normalized else raw_segments(surface)) & tokens
        )
    )


def surfaces_with_all(tokens: set[str], *, normalized: bool = False) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if tokens <= set(normalized_segments(surface) if normalized else raw_segments(surface))
        )
    )


def surfaces_with_exact(
    segments: tuple[str, ...], *, normalized: bool = False
) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if (normalized_segments(surface) if normalized else raw_segments(surface)) == segments
        )
    )


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    external_oracle = surfaces_with_any({"external", "oracle"})
    not_source_internal = surfaces_with_any({"not", "source", "internal"})
    noninternal = surfaces_with_any({"external", "oracle", "not", "source", "internal"})
    normalized_external = surfaces_with_exact(
        ("external", "or", "oracle"), normalized=True
    )
    exact_source_internal = surfaces_with_all({"source", "internal"})
    exact_not_source = surfaces_with_all({"not", "source"})
    exact_not_source_internal = surfaces_with_exact(("not", "source", "internal"))
    connector_or = surfaces_with_any({"external", "or", "oracle"})

    candidate_closures = {
        "external_oracle": external_oracle,
        "not_source_internal": not_source_internal,
        "noninternal": noninternal,
        "normalized_external_or_oracle": normalized_external,
        "exact_source_internal": exact_source_internal,
        "exact_not_source": exact_not_source,
        "exact_not_source_internal": exact_not_source_internal,
        "connector_or": connector_or,
    }
    class_pure_reused = {
        name: surfaces
        for name, surfaces in candidate_closures.items()
        if len(surfaces) >= 2 and len(class_profile(surfaces)) == 1
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
        and {CLASS_OF[surface] for surface in PAIR}
        == {"boundary_externality", "source_internality"},
        f"pair_classes={sorted(CLASS_OF[surface] for surface in PAIR)}",
    )
    gate(
        f"{PREFIX}3",
        external_oracle == EXTERNAL_ORACLE_SURFACES
        and class_profile(external_oracle)
        == Counter(
            {
                "terminal_basin_entry": 2,
                "action_semantics": 1,
                "classifier_partition": 1,
                "boundary_externality": 1,
            }
        ),
        f"external_oracle_profile={dict(class_profile(external_oracle))}",
    )
    gate(
        f"{PREFIX}4",
        not_source_internal == NOT_SOURCE_INTERNAL_SURFACES
        and class_profile(not_source_internal)
        == Counter(
            {
                "terminal_basin_entry": 3,
                "source_constraint_invariant": 1,
                "trace_payload_route": 1,
                "finite_index_budget": 1,
                "source_internality": 1,
            }
        ),
        f"not_source_internal_profile={dict(class_profile(not_source_internal))}",
    )
    gate(
        f"{PREFIX}5",
        noninternal == NONINTERNAL_SURFACES
        and PAIR <= set(noninternal)
        and class_profile(noninternal)
        == Counter(
            {
                "terminal_basin_entry": 5,
                "action_semantics": 1,
                "classifier_partition": 1,
                "source_constraint_invariant": 1,
                "boundary_externality": 1,
                "trace_payload_route": 1,
                "finite_index_budget": 1,
                "source_internality": 1,
            }
        ),
        f"noninternal_profile={dict(class_profile(noninternal))}",
    )
    gate(
        f"{PREFIX}6",
        normalized_external == NORMALIZED_EXTERNAL_OR_ORACLE_SURFACES
        and class_profile(normalized_external)
        == Counter(
            {
                "action_semantics": 1,
                "classifier_partition": 1,
                "boundary_externality": 1,
            }
        ),
        f"normalized_external_profile={dict(class_profile(normalized_external))}",
    )
    gate(
        f"{PREFIX}7",
        exact_source_internal == (SOURCE_INTERNAL_SURFACE,)
        and exact_not_source == (SOURCE_INTERNAL_SURFACE,)
        and exact_not_source_internal == (SOURCE_INTERNAL_SURFACE,)
        and class_profile(exact_not_source_internal) == Counter({"source_internality": 1}),
        "exact source/internal polarity closures are singleton residual lookup",
    )
    gate(
        f"{PREFIX}8",
        connector_or == CONNECTOR_OR_SURFACES
        and class_profile(connector_or)
        == Counter(
            {
                "classifier_partition": 2,
                "terminal_basin_entry": 2,
                "action_semantics": 1,
                "boundary_externality": 1,
                "boundary_contextual_surrogate": 1,
            }
        ),
        f"connector_or_profile={dict(class_profile(connector_or))}",
    )
    gate(
        f"{PREFIX}9",
        not class_pure_reused
        and len(noninternal) >= 2
        and len(class_profile(noninternal)) > 1
        and exact_not_source_internal == (SOURCE_INTERNAL_SURFACE,),
        "no semantic-polarity closure is both reused and class-pure; exact purity is singleton",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: semantic-polarity bridge reuse fails")
    print(
        "VERDICT: semantic polarity supplies no independent bridge morphism. "
        "Broad external/oracle/not/source/internal closures are mixed-class; "
        "exact source/internal closures are singleton lookup; and the exact "
        "external_or_oracle closure is only the mixed action/class/obstruction triple."
    )


if __name__ == "__main__":
    main()
