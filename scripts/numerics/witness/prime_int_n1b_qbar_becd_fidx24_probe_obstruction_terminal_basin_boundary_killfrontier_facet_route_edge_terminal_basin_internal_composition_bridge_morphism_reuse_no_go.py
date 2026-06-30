#!/usr/bin/env python3
r"""No-go for terminal-basin internal-composition bridge morphism reuse.

Doc 633 leaves a precise residue: terminal_basin_entry is the unique common
class hub, but the bridge would need an internal terminal-basin composition
law selecting among mediator paths. The natural internal composition kernel is
the shared escape/plain_tail/basin signature between external_basin or
oracle_basin and basin_not_absorbing or basin_not_extensional.

This witness checks that this kernel is not a constructed bridge morphism. It
gives the same signature on all four candidate paths, appears on many other
terminal-basin ordered pairs, and cannot distinguish absorbing from
extensional. Including the third not attachment splits the alleged law by
event kind and removes the basin connector.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_internal_composition_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from typing import Any

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
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASININTCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

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
LEFT_MEDIATORS = (EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)
BASIN_NOT_MEDIATORS = (BASIN_NOT_ABSORBING_SURFACE, BASIN_NOT_EXTENSIONAL_SURFACE)
ALL_NOT_MEDIATORS = (
    BASIN_NOT_ABSORBING_SURFACE,
    BASIN_NOT_EXTENSIONAL_SURFACE,
    ENTRY_TRACE_NOT_REPLAY_STABLE_SURFACE,
)
COMPOSITION_KERNEL = (
    ("boundary", "escape"),
    ("event_kind", "plain_tail"),
    ("segment", "basin"),
    ("stem", "basin"),
)

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


def pair_kernel(left: str, right: str) -> tuple[tuple[str, ...], ...]:
    return tuple(
        sorted(set(COMPOSITIONAL_SIGNATURES[left]) & set(COMPOSITIONAL_SIGNATURES[right]))
    )


def tbe_ordered_pairs_with_kernel(kernel: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, str], ...]:
    terminal_class = by_class(TERMINAL_BASIN_ENTRY)
    return tuple(
        sorted(
            (left, right)
            for left in terminal_class
            for right in terminal_class
            if left != right and pair_kernel(left, right) == kernel
        )
    )


def signature_difference(left: str, right: str) -> tuple[tuple[str, ...], ...]:
    return tuple(sorted(set(COMPOSITIONAL_SIGNATURES[left]) - set(COMPOSITIONAL_SIGNATURES[right])))


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    common_neighbors = class_adjacency()[BOUNDARY_EXTERNALITY] & class_adjacency()[
        SOURCE_INTERNALITY
    ]
    target_paths = tuple(product(LEFT_MEDIATORS, BASIN_NOT_MEDIATORS))
    all_not_paths = tuple(product(LEFT_MEDIATORS, ALL_NOT_MEDIATORS))
    target_path_kernels = Counter(pair_kernel(left, right) for left, right in target_paths)
    all_not_path_kernels = Counter(pair_kernel(left, right) for left, right in all_not_paths)
    tbe_kernel_pairs = tbe_ordered_pairs_with_kernel(COMPOSITION_KERNEL)
    external_oracle = by_segment({"external", "oracle"})
    not_support = by_segment({"not"})

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
        and len(by_class(TERMINAL_BASIN_ENTRY)) == 17,
        f"common_neighbors={sorted(common_neighbors)}",
    )
    gate(
        f"{PREFIX}4",
        target_path_kernels == Counter({COMPOSITION_KERNEL: 4})
        and len(target_paths) == 4,
        f"target_path_kernels={dict(target_path_kernels)}",
    )
    gate(
        f"{PREFIX}5",
        len(tbe_kernel_pairs) == 58
        and set(target_paths) <= set(tbe_kernel_pairs),
        f"tbe_pairs_with_kernel={len(tbe_kernel_pairs)}",
    )
    gate(
        f"{PREFIX}6",
        signature_difference(BASIN_NOT_ABSORBING_SURFACE, BASIN_NOT_EXTENSIONAL_SURFACE)
        == ()
        and signature_difference(BASIN_NOT_EXTENSIONAL_SURFACE, BASIN_NOT_ABSORBING_SURFACE)
        == (),
        "doc610 compositional signatures do not distinguish absorbing from extensional",
    )
    gate(
        f"{PREFIX}7",
        signature_difference(EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)
        == (("segment", "external"), ("stem", "external"))
        and signature_difference(ORACLE_BASIN_SURFACE, EXTERNAL_BASIN_SURFACE)
        == (("segment", "oracle"), ("stem", "oracle"))
        and class_profile(external_oracle) == EXTERNAL_ORACLE_PROFILE,
        "left branch differs only by external/oracle, whose global support is mixed-class",
    )
    gate(
        f"{PREFIX}8",
        all_not_path_kernels
        == Counter({COMPOSITION_KERNEL: 4, (("boundary", "escape"),): 2})
        and class_profile(not_support) == NOT_PROFILE
        and SOURCE_INTERNAL_SURFACE in not_support,
        "including the third not attachment splits the law and loses basin/plain-tail composition",
    )
    gate(
        f"{PREFIX}9",
        target_path_kernels == Counter({COMPOSITION_KERNEL: 4})
        and len(tbe_kernel_pairs) == 58
        and signature_difference(BASIN_NOT_ABSORBING_SURFACE, BASIN_NOT_EXTENSIONAL_SURFACE)
        == ()
        and len(class_profile(external_oracle)) > 1
        and len(class_profile(not_support)) > 1,
        "terminal-basin internal composition kernel is overproduced and non-selective",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin internal composition reuse fails")
    print(
        "VERDICT: the escape/plain_tail/basin kernel is real, but it gives all "
        "four target paths, appears on 58 terminal-basin ordered pairs, and "
        "cannot distinguish absorbing from extensional."
    )


if __name__ == "__main__":
    main()
