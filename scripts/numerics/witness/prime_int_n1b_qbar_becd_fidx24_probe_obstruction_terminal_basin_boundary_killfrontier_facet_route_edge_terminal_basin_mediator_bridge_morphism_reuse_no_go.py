#!/usr/bin/env python3
r"""No-go for terminal-basin mediator bridge morphism reuse.

Doc 631 shows that broad boundary transducer axes are mixed-class. The next
specific escape is to use the terminal-basin surfaces external_basin and
oracle_basin as mediators: they share external/oracle vocabulary with the
entry residual and live in the escape terminal-basin prefix near the
not_source_internal residual.

This witness checks that the two mediator legs are not proof-relevant reuse.
The external/oracle leg is mixed-class, the escape/plain-tail leg is
mixed-class, and basin segment support misses both residual surfaces.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_mediator_bridge_morphism_reuse_no_go
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINMEDIATORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
EXTERNAL_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_external_basin"
)
ORACLE_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_oracle_basin"
)
ESCAPE_CENTER_PREFIX = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"
)

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
MEDIATORS = (EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)

EXTERNAL_ORACLE_PROFILE = Counter(
    {
        "terminal_basin_entry": 2,
        "action_semantics": 1,
        "classifier_partition": 1,
        "boundary_externality": 1,
    }
)
ESCAPE_CENTER_PROFILE = Counter(
    {
        "terminal_basin_entry": 17,
        "boundary_contextual_surrogate": 6,
        "finite_index_budget": 3,
        "fixedpoint_replay": 3,
        "boundary_shape": 2,
        "dependency_repair_nogo": 2,
        "action_semantics": 1,
        "classifier_partition": 1,
        "confluence_normalizer": 1,
        "source_constraint_invariant": 1,
        "localizer_blame": 1,
        "source_internality": 1,
        "trace_payload_route": 1,
        "reflection_normalform": 1,
        "trace_audit_check": 1,
        "verifier_check": 1,
    }
)
PLAIN_TAIL_PROFILE = Counter(
    {
        "terminal_basin_entry": 13,
        "boundary_contextual_surrogate": 6,
        "dependency_repair_nogo": 3,
        "finite_index_budget": 3,
        "trace_audit_check": 2,
        "fixedpoint_replay": 2,
        "boundary_shape": 1,
        "verifier_check": 1,
        "confluence_normalizer": 1,
        "source_internality": 1,
        "reflection_normalform": 1,
        "localizer_blame": 1,
        "classifier_partition": 1,
        "action_semantics": 1,
    }
)
BASIN_SEGMENT_PROFILE = Counter({"terminal_basin_entry": 10, "action_semantics": 1})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def segments(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["segments"])


def namespaces(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["namespaces"])


def by_segment(tokens: set[str]) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface for surface in BOUNDARY_SURFACES if segments(surface) & tokens
        )
    )


def by_event_kind(kind: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface for surface in BOUNDARY_SURFACES if SOURCE_EVENTS[surface]["event_kind"] == kind
        )
    )


def by_prefix(prefix: str) -> tuple[str, ...]:
    return tuple(sorted(surface for surface in BOUNDARY_SURFACES if surface.startswith(prefix)))


def basin_mediators() -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if "basin" in segments(surface)
            and bool(segments(surface) & {"external", "oracle"})
        )
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    mediators = basin_mediators()
    external_oracle = by_segment({"external", "oracle"})
    escape_center = by_prefix(ESCAPE_CENTER_PREFIX)
    plain_tail = by_event_kind("plain_tail")
    basin_segment = by_segment({"basin"})
    mediator_to_source_shared_segments = set().union(
        *(segments(surface) for surface in mediators)
    ) & segments(SOURCE_INTERNAL_SURFACE)
    mediator_to_source_shared_namespaces = set().union(
        *(namespaces(surface) for surface in mediators)
    ) & namespaces(SOURCE_INTERNAL_SURFACE)

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
        mediators == MEDIATORS
        and class_profile(mediators) == Counter({"terminal_basin_entry": 2})
        and all(SOURCE_EVENTS[surface]["boundary_kind"] == "escape" for surface in mediators)
        and all(SOURCE_EVENTS[surface]["event_kind"] == "plain_tail" for surface in mediators),
        "the only external/oracle basin mediators are two terminal_basin_entry escape tails",
    )
    gate(
        f"{PREFIX}4",
        len(external_oracle) == 5
        and EXTERNAL_SURFACE in external_oracle
        and set(mediators) <= set(external_oracle)
        and SOURCE_INTERNAL_SURFACE not in external_oracle
        and class_profile(external_oracle) == EXTERNAL_ORACLE_PROFILE,
        f"external_oracle_profile={dict(class_profile(external_oracle))}",
    )
    gate(
        f"{PREFIX}5",
        len(escape_center) == 43
        and set(mediators) <= set(escape_center)
        and SOURCE_INTERNAL_SURFACE in escape_center
        and EXTERNAL_SURFACE not in escape_center
        and class_profile(escape_center) == ESCAPE_CENTER_PROFILE,
        "escape-center mediator leg is reused but mixed-class",
    )
    gate(
        f"{PREFIX}6",
        len(plain_tail) == 37
        and set(mediators) <= set(plain_tail)
        and SOURCE_INTERNAL_SURFACE in plain_tail
        and EXTERNAL_SURFACE not in plain_tail
        and class_profile(plain_tail) == PLAIN_TAIL_PROFILE,
        "plain-tail mediator leg is reused but mixed-class",
    )
    gate(
        f"{PREFIX}7",
        len(basin_segment) == 11
        and set(mediators) <= set(basin_segment)
        and EXTERNAL_SURFACE not in basin_segment
        and SOURCE_INTERNAL_SURFACE not in basin_segment
        and class_profile(basin_segment) == BASIN_SEGMENT_PROFILE,
        "basin segment support contains the mediators but misses both residuals",
    )
    gate(
        f"{PREFIX}8",
        not mediator_to_source_shared_segments
        and not mediator_to_source_shared_namespaces
        and class_profile(mediators) == Counter({"terminal_basin_entry": 2})
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        "mediators have no exact segment/namespace bridge to not_source_internal",
    )
    gate(
        f"{PREFIX}9",
        CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality"
        and class_profile(mediators) == Counter({"terminal_basin_entry": 2})
        and len(class_profile(external_oracle)) > 1
        and len(class_profile(escape_center)) > 1
        and len(class_profile(plain_tail)) > 1,
        "the mediator path needs selectors on both legs and crosses three classes",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin mediator bridge reuse fails")
    print(
        "VERDICT: external_basin/oracle_basin are real terminal-basin mediators, "
        "but the external/oracle leg, escape-prefix leg, and plain-tail leg are "
        "mixed-class; basin support itself misses both residuals."
    )


if __name__ == "__main__":
    main()
