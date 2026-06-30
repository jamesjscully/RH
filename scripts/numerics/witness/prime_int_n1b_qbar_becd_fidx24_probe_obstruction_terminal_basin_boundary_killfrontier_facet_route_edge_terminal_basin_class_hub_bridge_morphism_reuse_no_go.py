#!/usr/bin/env python3
r"""No-go for terminal-basin class-hub bridge morphism reuse.

Doc 632 kills the direct external_basin/oracle_basin mediator path. The next
sharper repair is to promote the whole terminal_basin_entry class to the
middle object: it is the unique common class-neighbor connecting the
boundary_externality residual to the source_internality residual in the
doc610 segment-induced class graph.

This witness records that positive residue, then checks that it still does
not construct a bridge morphism. The external/oracle attachment and the not
attachment are mixed-class; no terminal_basin_entry surface carries both
attachments; and the internal basin connector needs additional selectors.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_class_hub_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINCLASSHUBBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

BOUNDARY_EXTERNALITY = "boundary_externality"
SOURCE_INTERNALITY = "source_internality"
TERMINAL_BASIN_ENTRY = "terminal_basin_entry"

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
BASIN_NOT_ABSORBING_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_basin_not_absorbing"
)
BASIN_NOT_EXTENSIONAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_basin_not_extensional"
)
ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_entry_trace_not_replay_stable"
)

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
EXTERNAL_ORACLE_MEDIATORS = (EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)
NOT_TERMINAL_MEDIATORS = (
    BASIN_NOT_ABSORBING_SURFACE,
    BASIN_NOT_EXTENSIONAL_SURFACE,
    ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE,
)
BASIN_NOT_MEDIATORS = (BASIN_NOT_ABSORBING_SURFACE, BASIN_NOT_EXTENSIONAL_SURFACE)

EXTERNAL_ORACLE_PROFILE = Counter(
    {
        "terminal_basin_entry": 2,
        "action_semantics": 1,
        "classifier_partition": 1,
        "boundary_externality": 1,
    }
)
NOT_PROFILE = Counter(
    {
        "terminal_basin_entry": 3,
        "finite_index_budget": 1,
        "source_internality": 1,
    }
)
BASIN_PROFILE = Counter({"terminal_basin_entry": 10, "action_semantics": 1})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["segments"])


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def by_class(class_name: str) -> tuple[str, ...]:
    return tuple(sorted(surface for surface in BOUNDARY_SURFACES if CLASS_OF[surface] == class_name))


def by_segment(tokens: set[str]) -> tuple[str, ...]:
    return tuple(
        sorted(surface for surface in BOUNDARY_SURFACES if segments(surface) & tokens)
    )


def token_classes() -> dict[str, set[str]]:
    classes: dict[str, set[str]] = defaultdict(set)
    for surface in BOUNDARY_SURFACES:
        for token in SOURCE_EVENTS[surface]["segments"]:
            classes[token].add(CLASS_OF[surface])
    return dict(classes)


def class_adjacency() -> dict[str, set[str]]:
    adjacency: dict[str, set[str]] = defaultdict(set)
    for classes in token_classes().values():
        for left in classes:
            for right in classes:
                if left != right:
                    adjacency[left].add(right)
    return dict(adjacency)


def edge_tokens(left: str, right: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            token
            for token, classes in token_classes().items()
            if left in classes and right in classes
        )
    )


def class_surfaces_with_tokens(class_name: str, tokens: set[str]) -> tuple[str, ...]:
    return tuple(
        sorted(
            surface
            for surface in by_class(class_name)
            if segments(surface) & tokens
        )
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    terminal_class = by_class(TERMINAL_BASIN_ENTRY)
    adjacency = class_adjacency()
    common_neighbors = adjacency[BOUNDARY_EXTERNALITY] & adjacency[SOURCE_INTERNALITY]
    external_oracle = by_segment({"external", "oracle"})
    not_support = by_segment({"not"})
    basin_support = by_segment({"basin"})
    tbe_external_oracle = class_surfaces_with_tokens(
        TERMINAL_BASIN_ENTRY, {"external", "oracle"}
    )
    tbe_not = class_surfaces_with_tokens(TERMINAL_BASIN_ENTRY, {"not"})
    tbe_basin = class_surfaces_with_tokens(TERMINAL_BASIN_ENTRY, {"basin"})
    tbe_basin_not = tuple(
        sorted(surface for surface in terminal_class if {"basin", "not"} <= segments(surface))
    )
    tbe_external_oracle_not = tuple(
        sorted(
            surface
            for surface in terminal_class
            if segments(surface) & {"external", "oracle"} and "not" in segments(surface)
        )
    )
    internal_basin_path_count = len(tbe_external_oracle) * len(tbe_basin_not)

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
        == {BOUNDARY_EXTERNALITY, SOURCE_INTERNALITY},
        f"pair_classes={sorted(CLASS_OF[surface] for surface in PAIR)}",
    )
    gate(
        f"{PREFIX}3",
        common_neighbors == {TERMINAL_BASIN_ENTRY}
        and edge_tokens(BOUNDARY_EXTERNALITY, TERMINAL_BASIN_ENTRY)
        == ("external", "oracle")
        and edge_tokens(TERMINAL_BASIN_ENTRY, SOURCE_INTERNALITY) == ("not",),
        f"common_neighbors={sorted(common_neighbors)}",
    )
    gate(
        f"{PREFIX}4",
        len(terminal_class) == 17
        and class_profile(terminal_class) == Counter({TERMINAL_BASIN_ENTRY: 17})
        and tbe_external_oracle == EXTERNAL_ORACLE_MEDIATORS
        and tbe_not == NOT_TERMINAL_MEDIATORS,
        f"tbe_external_oracle={len(tbe_external_oracle)} tbe_not={len(tbe_not)}",
    )
    gate(
        f"{PREFIX}5",
        not tbe_external_oracle_not
        and set(tbe_external_oracle).isdisjoint(tbe_not)
        and EXTERNAL_SURFACE not in terminal_class
        and SOURCE_INTERNAL_SURFACE not in terminal_class,
        "no terminal_basin_entry surface carries both external/oracle and not attachments",
    )
    gate(
        f"{PREFIX}6",
        len(external_oracle) == 5
        and class_profile(external_oracle) == EXTERNAL_ORACLE_PROFILE
        and EXTERNAL_SURFACE in external_oracle
        and set(tbe_external_oracle) <= set(external_oracle)
        and len(not_support) == 5
        and class_profile(not_support) == NOT_PROFILE
        and SOURCE_INTERNAL_SURFACE in not_support
        and set(tbe_not) <= set(not_support),
        "both external/oracle and not attachment closures are mixed-class",
    )
    gate(
        f"{PREFIX}7",
        len(basin_support) == 11
        and class_profile(basin_support) == BASIN_PROFILE
        and len(tbe_basin) == 10
        and tbe_basin_not == BASIN_NOT_MEDIATORS
        and set(tbe_external_oracle) <= set(tbe_basin)
        and ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE not in tbe_basin,
        "basin gives an internal class connector only after terminal-basin filtering",
    )
    gate(
        f"{PREFIX}8",
        internal_basin_path_count == 4
        and len(tbe_external_oracle) == 2
        and len(tbe_basin_not) == 2
        and len(tbe_not) == 3,
        "the class hub leaves multiple internal mediator choices",
    )
    gate(
        f"{PREFIX}9",
        common_neighbors == {TERMINAL_BASIN_ENTRY}
        and len(class_profile(external_oracle)) > 1
        and len(class_profile(not_support)) > 1
        and len(class_profile(basin_support)) > 1
        and not tbe_external_oracle_not,
        "unique common class neighbor is adjacency evidence, not a constructed bridge morphism",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin class-hub bridge reuse fails")
    print(
        "VERDICT: terminal_basin_entry is the unique common class-neighbor, "
        "but the bridge still needs mixed external/oracle and not attachments, "
        "an internal basin selector, and a choice among mediator paths."
    )


if __name__ == "__main__":
    main()
