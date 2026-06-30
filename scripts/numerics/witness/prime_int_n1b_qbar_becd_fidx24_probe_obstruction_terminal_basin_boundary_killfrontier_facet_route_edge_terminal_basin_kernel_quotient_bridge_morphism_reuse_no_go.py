#!/usr/bin/env python3
r"""No-go for terminal-basin kernel-quotient bridge morphism reuse.

Doc 634 kills the visible escape/plain_tail/basin kernel as a selective
composition law. The next escape is quotienting: perhaps all paths with that
kernel represent the same morphism, so the four target mediator paths become
one proof-relevant bridge.

This witness checks that the quotient is too coarse. The kernel-equivalence
component containing the target mediators also contains retuned, noncanonical,
proof-irrelevant, unbounded, no-certificate, and branch-spawning basin
surfaces. Quotienting by the visible kernel erases exactly the terminal-basin
distinctions the proof needs.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINKERNELQUOTIENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

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
BRANCH_SPAWNING_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_branch_spawning_basin"
)
NO_BASIN_CERTIFICATE_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_no_basin_certificate"
)
NONCANONICAL_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_noncanonical_basin"
)
PROOF_IRRELEVANT_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_proof_irrelevant_basin"
)
RETUNED_BASIN_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_retuned_basin"
)
UNBOUNDED_BASIN_SEARCH_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_unbounded_basin_search"
)

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
LEFT_MEDIATORS = (EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)
RIGHT_MEDIATORS = (BASIN_NOT_ABSORBING_SURFACE, BASIN_NOT_EXTENSIONAL_SURFACE)
TARGET_ENDPOINTS = frozenset(
    {
        EXTERNAL_BASIN_SURFACE,
        ORACLE_BASIN_SURFACE,
        BASIN_NOT_ABSORBING_SURFACE,
        BASIN_NOT_EXTENSIONAL_SURFACE,
    }
)
BAD_BASIN_SURFACES = frozenset(
    {
        BRANCH_SPAWNING_BASIN_SURFACE,
        NO_BASIN_CERTIFICATE_SURFACE,
        NONCANONICAL_BASIN_SURFACE,
        PROOF_IRRELEVANT_BASIN_SURFACE,
        RETUNED_BASIN_SURFACE,
        UNBOUNDED_BASIN_SEARCH_SURFACE,
    }
)
KERNEL_COMPONENT = frozenset(TARGET_ENDPOINTS | BAD_BASIN_SURFACES)
COMPOSITION_KERNEL = (
    ("boundary", "escape"),
    ("event_kind", "plain_tail"),
    ("segment", "basin"),
    ("stem", "basin"),
)
KERNEL_DEGREE_PROFILE = Counter({8: 6, 16: 2, 18: 2})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def by_class(class_name: str) -> tuple[str, ...]:
    return tuple(sorted(surface for surface in BOUNDARY_SURFACES if CLASS_OF[surface] == class_name))


def pair_kernel(left: str, right: str) -> tuple[tuple[str, ...], ...]:
    return tuple(
        sorted(set(COMPOSITIONAL_SIGNATURES[left]) & set(COMPOSITIONAL_SIGNATURES[right]))
    )


def kernel_pairs() -> tuple[tuple[str, str], ...]:
    terminal_class = by_class(TERMINAL_BASIN_ENTRY)
    return tuple(
        sorted(
            (left, right)
            for left in terminal_class
            for right in terminal_class
            if left != right and pair_kernel(left, right) == COMPOSITION_KERNEL
        )
    )


def kernel_components(pairs: tuple[tuple[str, str], ...]) -> tuple[frozenset[str], ...]:
    adjacency: dict[str, set[str]] = {}
    for left, right in pairs:
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)

    seen: set[str] = set()
    components: list[frozenset[str]] = []
    for node in sorted(adjacency):
        if node in seen:
            continue
        stack = [node]
        seen.add(node)
        component: set[str] = set()
        while stack:
            current = stack.pop()
            component.add(current)
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        components.append(frozenset(component))
    return tuple(sorted(components, key=lambda component: (len(component), sorted(component))))


def endpoint_degrees(pairs: tuple[tuple[str, str], ...]) -> Counter[int]:
    left_degrees = Counter(left for left, _right in pairs)
    right_degrees = Counter(right for _left, right in pairs)
    return Counter(left_degrees[surface] + right_degrees[surface] for surface in KERNEL_COMPONENT)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    pairs = kernel_pairs()
    components = kernel_components(pairs)
    target_pairs = frozenset(product(LEFT_MEDIATORS, RIGHT_MEDIATORS))
    pair_set = frozenset(pairs)

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
        len(pairs) == 58
        and target_pairs <= pair_set
        and len(pair_set - target_pairs) == 54,
        f"kernel_pairs={len(pairs)} non_target={len(pair_set - target_pairs)}",
    )
    gate(
        f"{PREFIX}4",
        components == (KERNEL_COMPONENT,),
        f"component_sizes={[len(component) for component in components]}",
    )
    gate(
        f"{PREFIX}5",
        TARGET_ENDPOINTS <= components[0]
        and BAD_BASIN_SURFACES <= components[0]
        and len(BAD_BASIN_SURFACES) == 6,
        "target endpoints share the quotient component with six non-proof-relevant basin labels",
    )
    gate(
        f"{PREFIX}6",
        endpoint_degrees(pairs) == KERNEL_DEGREE_PROFILE,
        f"degree_profile={dict(endpoint_degrees(pairs))}",
    )
    gate(
        f"{PREFIX}7",
        all(CLASS_OF[surface] == TERMINAL_BASIN_ENTRY for surface in components[0])
        and all(SOURCE_EVENTS[surface]["event_kind"] == "plain_tail" for surface in components[0])
        and all("basin" in segments(surface) for surface in components[0]),
        "the quotient component is class-pure only because it erases basin distinctions",
    )
    gate(
        f"{PREFIX}8",
        {
            "retuned",
            "noncanonical",
            "unbounded",
            "proof",
            "irrelevant",
            "no",
            "certificate",
            "branch",
            "spawning",
        }
        <= {token for surface in BAD_BASIN_SURFACES for token in segments(surface)},
        "kernel quotient imports explicit selector/failure vocabulary",
    )
    gate(
        f"{PREFIX}9",
        len(pairs) == 58
        and components == (KERNEL_COMPONENT,)
        and TARGET_ENDPOINTS < components[0]
        and BAD_BASIN_SURFACES <= components[0],
        "kernel quotient collapses terminal-basin failure labels instead of constructing the bridge",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin kernel quotient reuse fails")
    print(
        "VERDICT: quotienting by the escape/plain_tail/basin kernel identifies "
        "the target mediators with retuned, noncanonical, proof-irrelevant, "
        "unbounded, no-certificate, and branch-spawning basin surfaces."
    )


if __name__ == "__main__":
    main()
