#!/usr/bin/env python3
r"""No-go for boundary-transducer bridge morphism reuse.

Docs 629 and 630 kill direct residual-pair selection and semantic-polarity
closure. The next plausible repair is a boundary transducer: use the entry /
escape boundary axis, the obstruction / plain-tail event axis, or the
terminal-basin escape prefix as the bridge between the two doc614 singleton
residuals.

This witness checks that the visible boundary axes are broad mixed-class
partitions, while terminal-basin segment support does not contain the residual
pair. A boundary transducer therefore still needs independent proof-relevant
morphism evidence.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_boundary_transducer_bridge_morphism_reuse_no_go
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYTRANSDUCERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
MISSING_TERMINAL_CERTIFICATE_SURFACE = (
    "escape_boundary:missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate"
)
ESCAPE_CENTER_PREFIX = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"
)

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})

ENTRY_KIND_PROFILE = Counter(
    {
        "trace_payload_route": 13,
        "source_constraint_invariant": 11,
        "classifier_partition": 9,
        "action_semantics": 9,
        "dependency_repair_nogo": 6,
        "boundary_contextual_surrogate": 4,
        "finite_index_budget": 2,
        "trace_audit_check": 2,
        "fixedpoint_replay": 1,
        "verifier_check": 1,
        "confluence_normalizer": 1,
        "reflection_normalform": 1,
        "boundary_externality": 1,
        "localizer_blame": 1,
    }
)
ESCAPE_KIND_PROFILE = Counter(
    {
        "terminal_basin_entry": 17,
        "boundary_contextual_surrogate": 6,
        "fixedpoint_replay": 3,
        "finite_index_budget": 3,
        "boundary_shape": 2,
        "action_semantics": 2,
        "dependency_repair_nogo": 2,
        "classifier_partition": 1,
        "reflection_normalform": 1,
        "source_constraint_invariant": 1,
        "confluence_normalizer": 1,
        "source_internality": 1,
        "localizer_blame": 1,
        "trace_audit_check": 1,
        "verifier_check": 1,
        "trace_payload_route": 1,
    }
)
OBSTRUCTION_EVENT_PROFILE = Counter(
    {
        "dependency_repair_nogo": 3,
        "boundary_contextual_surrogate": 2,
        "finite_index_budget": 1,
        "boundary_externality": 1,
    }
)
PLAIN_TAIL_EVENT_PROFILE = Counter(
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
BASIN_SEGMENT_PROFILE = Counter({"terminal_basin_entry": 10, "action_semantics": 1})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def by_boundary_kind(kind: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if SOURCE_EVENTS[surface]["boundary_kind"] == kind
        )
    )


def by_event_kind(kind: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface for surface in BOUNDARY_SURFACES if SOURCE_EVENTS[surface]["event_kind"] == kind
        )
    )


def by_segment(tokens: set[str]) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in BOUNDARY_SURFACES
            if set(SOURCE_EVENTS[surface]["segments"]) & tokens
        )
    )


def by_prefix(prefix: str) -> tuple[str, ...]:
    return tuple(sorted(surface for surface in BOUNDARY_SURFACES if surface.startswith(prefix)))


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    entry_kind = by_boundary_kind("entry")
    escape_kind = by_boundary_kind("escape")
    obstruction_event = by_event_kind("obstruction_namespace")
    plain_tail_event = by_event_kind("plain_tail")
    escape_center = by_prefix(ESCAPE_CENTER_PREFIX)
    basin_segment = by_segment({"basin"})
    terminal_obstruction_segment = by_segment({"terminal", "obstruction"})

    candidate_closures = {
        "entry_kind": entry_kind,
        "escape_kind": escape_kind,
        "obstruction_event": obstruction_event,
        "plain_tail_event": plain_tail_event,
        "escape_center": escape_center,
        "basin_segment": basin_segment,
        "terminal_obstruction_segment": terminal_obstruction_segment,
    }
    class_pure_reused_pair_closures = {
        name: surfaces
        for name, surfaces in candidate_closures.items()
        if PAIR <= set(surfaces) and len(surfaces) >= 2 and len(class_profile(surfaces)) == 1
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
        len(entry_kind) == 62
        and len(escape_kind) == 44
        and class_profile(entry_kind) == ENTRY_KIND_PROFILE
        and class_profile(escape_kind) == ESCAPE_KIND_PROFILE
        and EXTERNAL_SURFACE in entry_kind
        and SOURCE_INTERNAL_SURFACE in escape_kind,
        "entry and escape boundary-kind closures are broad mixed-class partitions",
    )
    gate(
        f"{PREFIX}4",
        len(obstruction_event) == 7
        and len(plain_tail_event) == 37
        and class_profile(obstruction_event) == OBSTRUCTION_EVENT_PROFILE
        and class_profile(plain_tail_event) == PLAIN_TAIL_EVENT_PROFILE
        and EXTERNAL_SURFACE in obstruction_event
        and SOURCE_INTERNAL_SURFACE in plain_tail_event,
        "obstruction_namespace and plain_tail event closures are mixed-class",
    )
    gate(
        f"{PREFIX}5",
        all(SOURCE_EVENTS[surface]["boundary_kind"] == "entry" for surface in obstruction_event)
        and SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]["boundary_kind"] == "escape"
        and SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]["event_kind"] == "plain_tail",
        "the external obstruction event has no visible escape-event counterpart",
    )
    gate(
        f"{PREFIX}6",
        len(escape_center) == 43
        and SOURCE_INTERNAL_SURFACE in escape_center
        and EXTERNAL_SURFACE not in escape_center
        and class_profile(escape_center) == ESCAPE_CENTER_PROFILE,
        "the escape terminal-basin prefix is reused but mixed-class",
    )
    gate(
        f"{PREFIX}7",
        len(basin_segment) == 11
        and class_profile(basin_segment) == BASIN_SEGMENT_PROFILE
        and SOURCE_INTERNAL_SURFACE not in basin_segment
        and EXTERNAL_SURFACE not in basin_segment,
        "basin segment support is mostly terminal-basin class but misses the residual pair",
    )
    gate(
        f"{PREFIX}8",
        terminal_obstruction_segment == (MISSING_TERMINAL_CERTIFICATE_SURFACE,)
        and class_profile(terminal_obstruction_segment) == Counter({"action_semantics": 1}),
        "terminal/obstruction segment evidence is a singleton certificate action",
    )
    gate(
        f"{PREFIX}9",
        not class_pure_reused_pair_closures
        and SOURCE_EVENTS[EXTERNAL_SURFACE]["boundary_kind"] == "entry"
        and SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]["boundary_kind"] == "escape"
        and SOURCE_EVENTS[EXTERNAL_SURFACE]["event_kind"] == "obstruction_namespace"
        and SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]["event_kind"] == "plain_tail",
        "no visible boundary transducer closure is reused, class-pure, and pair-containing",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: boundary-transducer bridge reuse fails")
    print(
        "VERDICT: entry/escape and obstruction/plain-tail axes are mixed-class, "
        "the escape terminal-basin prefix is mixed-class, and basin/terminal "
        "segments do not contain the residual pair. A boundary transducer "
        "needs independent morphism evidence."
    )


if __name__ == "__main__":
    main()
