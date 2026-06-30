#!/usr/bin/env python3
r"""No-go for terminal-basin quotient-graph invariant bridge reuse.

Doc 636 kills failure-complement filtering. The next escape is graph-internal:
use degree or centrality in the kernel quotient graph to separate the four
target endpoints from the six bad terminal-basin labels.

This witness checks the directed kernel-pair graph and its undirected quotient
component. Standard graph profiles do not select the target endpoints. The
left target endpoints share their full graph profile with four bad labels, and
the highest-centrality profile is occupied by bad labels.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import combinations
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BAD_BASIN_SURFACES,
    BOUNDARY_EXTERNALITY,
    EXTERNAL_BASIN_SURFACE,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    NO_BASIN_CERTIFICATE_SURFACE,
    ORACLE_BASIN_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    TARGET_ENDPOINTS,
    UNBOUNDED_BASIN_SEARCH_SURFACE,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_failure_complement_bridge_morphism_reuse_no_go import (
    FAILURE_TOKENS,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINQUOTGRAPHINVBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
LEFT_TARGETS = frozenset({EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE})
HIGH_CENTRALITY_BAD = frozenset({NO_BASIN_CERTIFICATE_SURFACE, UNBOUNDED_BASIN_SEARCH_SURFACE})
PROFILE_LOW = (4, 4, 8, 4, 2, 14)
PROFILE_MID = (8, 8, 16, 8, 2, 10)
PROFILE_HIGH_BAD = (9, 9, 18, 9, 1, 9)
EXPECTED_PROFILE_COUNTS = Counter({PROFILE_LOW: 6, PROFILE_MID: 2, PROFILE_HIGH_BAD: 2})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def undirected_adjacency(pairs: tuple[tuple[str, str], ...]) -> dict[str, set[str]]:
    adjacency: dict[str, set[str]] = defaultdict(set)
    for left, right in pairs:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return dict(adjacency)


def distances_from(start: str, adjacency: dict[str, set[str]]) -> dict[str, int]:
    distances = {start: 0}
    queue: deque[str] = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in adjacency[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances


def graph_profiles() -> dict[str, tuple[int, int, int, int, int, int]]:
    pairs = kernel_pairs()
    out_degree = Counter(left for left, _right in pairs)
    in_degree = Counter(right for _left, right in pairs)
    adjacency = undirected_adjacency(pairs)
    profiles: dict[str, tuple[int, int, int, int, int, int]] = {}
    for surface in sorted(KERNEL_COMPONENT):
        distances = distances_from(surface, adjacency)
        profiles[surface] = (
            out_degree[surface],
            in_degree[surface],
            out_degree[surface] + in_degree[surface],
            len(adjacency[surface]),
            max(distances.values()),
            sum(distances.values()),
        )
    return profiles


def profile_supports() -> dict[tuple[int, int, int, int, int, int], frozenset[str]]:
    supports: dict[tuple[int, int, int, int, int, int], set[str]] = defaultdict(set)
    for surface, profile in graph_profiles().items():
        supports[profile].add(surface)
    return {profile: frozenset(surfaces) for profile, surfaces in supports.items()}


def invariant_value_supports(index: int) -> dict[int, frozenset[str]]:
    supports: dict[int, set[str]] = defaultdict(set)
    for surface, profile in graph_profiles().items():
        supports[profile[index]].add(surface)
    return {value: frozenset(surfaces) for value, surfaces in supports.items()}


def any_profile_union_selects_target() -> bool:
    supports = tuple(profile_supports().values())
    for size in range(1, len(supports) + 1):
        for combo in combinations(supports, size):
            if frozenset().union(*combo) == TARGET_ENDPOINTS:
                return True
    return False


def any_single_invariant_value_selects_target() -> bool:
    return any(
        support == TARGET_ENDPOINTS
        for index in range(6)
        for support in invariant_value_supports(index).values()
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    pairs = kernel_pairs()
    profiles = graph_profiles()
    supports = profile_supports()
    low_support = supports[PROFILE_LOW]
    mid_support = supports[PROFILE_MID]
    high_bad_support = supports[PROFILE_HIGH_BAD]

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
        and len(KERNEL_COMPONENT) == 10
        and Counter(profiles.values()) == EXPECTED_PROFILE_COUNTS,
        f"profile_counts={dict(Counter(profiles.values()))}",
    )
    gate(
        f"{PREFIX}4",
        LEFT_TARGETS <= low_support
        and len(low_support & BAD_BASIN_SURFACES) == 4
        and len(low_support) == 6,
        "external_basin/oracle_basin share their graph profile with four bad labels",
    )
    gate(
        f"{PREFIX}5",
        mid_support <= TARGET_ENDPOINTS
        and len(mid_support) == 2
        and mid_support != TARGET_ENDPOINTS,
        "the only target-pure graph profile selects only the two not-side endpoints",
    )
    gate(
        f"{PREFIX}6",
        high_bad_support == HIGH_CENTRALITY_BAD
        and all(set(SOURCE_EVENTS[surface]["segments"]) & FAILURE_TOKENS for surface in high_bad_support),
        "highest-centrality profile is occupied by bad labels",
    )
    gate(
        f"{PREFIX}7",
        not any_single_invariant_value_selects_target()
        and not any_profile_union_selects_target(),
        "no single graph invariant value or union of full graph profiles selects all target endpoints",
    )
    gate(
        f"{PREFIX}8",
        invariant_value_supports(2)[8] == low_support
        and invariant_value_supports(2)[16] == mid_support
        and invariant_value_supports(2)[18] == high_bad_support,
        "total-degree partition is low mixed, middle partial-target, high bad",
    )
    gate(
        f"{PREFIX}9",
        LEFT_TARGETS <= low_support
        and len(low_support & BAD_BASIN_SURFACES) == 4
        and high_bad_support <= BAD_BASIN_SURFACES
        and not any_single_invariant_value_selects_target(),
        "kernel graph invariants do not supply the missing positive separator",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin quotient graph invariants fail")
    print(
        "VERDICT: graph degree/centrality does not separate the target endpoints. "
        "The left targets share a profile with bad labels, and the highest "
        "centrality profile is bad."
    )


if __name__ == "__main__":
    main()
