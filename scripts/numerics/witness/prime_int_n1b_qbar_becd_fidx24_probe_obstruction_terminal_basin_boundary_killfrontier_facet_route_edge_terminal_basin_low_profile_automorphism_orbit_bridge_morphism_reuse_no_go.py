#!/usr/bin/env python3
r"""No-go for terminal-basin low-profile automorphism/orbit bridge reuse.

Doc 639 kills valence filtering inside the low graph-profile terminal-basin
component. The next nonlexical repair is symmetry: perhaps external_basin and
oracle_basin form a canonical pair or graph orbit inside the terminal-basin
kernel graph.

This witness checks the directed kernel-pair graph. The six low-profile
vertices have no internal directed edges, identical kernel-neighborhood
fingerprints, and form one full symmetric orbit. Under the full kernel graph
automorphism group, the target pair external_basin/oracle_basin has orbit all
15 two-element subsets of the low-profile component. Selecting that pair is
therefore an external choice, not a graph-internal canonical orbit.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_automorphism_orbit_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial
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
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    TARGET_ENDPOINTS,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    LEFT_TARGETS,
    LOW_PROFILE_COMPONENT,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go import (
    HIGH_CENTRALITY_BAD,
    PROFILE_HIGH_BAD,
    PROFILE_LOW,
    PROFILE_MID,
    graph_profiles,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEAUTORBITBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
RIGHT_TARGETS = TARGET_ENDPOINTS - LEFT_TARGETS
EXPECTED_KERNEL_AUTOMORPHISMS = factorial(6) * factorial(2) * factorial(2)
EXPECTED_LOW_PAIR_COUNT = 15

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def profile_blocks() -> dict[tuple[int, int, int, int, int, int], tuple[str, ...]]:
    profiles = graph_profiles()
    return {
        profile: tuple(sorted(surface for surface, actual in profiles.items() if actual == profile))
        for profile in (PROFILE_LOW, PROFILE_MID, PROFILE_HIGH_BAD)
    }


def low_induced_edges() -> frozenset[tuple[str, str]]:
    pairs = set(kernel_pairs())
    return frozenset(
        (left, right)
        for left, right in pairs
        if left in LOW_PROFILE_COMPONENT and right in LOW_PROFILE_COMPONENT
    )


def is_automorphism(mapping: dict[str, str], edges: frozenset[tuple[str, str]]) -> bool:
    return frozenset((mapping[left], mapping[right]) for left, right in edges) == edges


def low_automorphisms() -> list[dict[str, str]]:
    vertices = tuple(sorted(LOW_PROFILE_COMPONENT))
    edges = low_induced_edges()
    autos: list[dict[str, str]] = []
    for permuted in permutations(vertices):
        mapping = dict(zip(vertices, permuted))
        if is_automorphism(mapping, edges):
            autos.append(mapping)
    return autos


def kernel_automorphisms() -> list[dict[str, str]]:
    blocks = profile_blocks()
    domains = (blocks[PROFILE_LOW], blocks[PROFILE_MID], blocks[PROFILE_HIGH_BAD])
    domain = tuple(surface for block in domains for surface in block)
    edges = frozenset(kernel_pairs())
    autos: list[dict[str, str]] = []
    for low_perm in permutations(domains[0]):
        for mid_perm in permutations(domains[1]):
            for high_perm in permutations(domains[2]):
                image = tuple(low_perm) + tuple(mid_perm) + tuple(high_perm)
                mapping = dict(zip(domain, image))
                if is_automorphism(mapping, edges):
                    autos.append(mapping)
    return autos


def vertex_orbit(surface: str, autos: list[dict[str, str]]) -> frozenset[str]:
    return frozenset(auto[surface] for auto in autos)


def pair_orbit(pair: frozenset[str], autos: list[dict[str, str]]) -> frozenset[frozenset[str]]:
    left, right = tuple(pair)
    return frozenset(frozenset({auto[left], auto[right]}) for auto in autos)


def all_low_pairs() -> frozenset[frozenset[str]]:
    return frozenset(frozenset(pair) for pair in combinations(LOW_PROFILE_COMPONENT, 2))


def neighbor_fingerprint(surface: str) -> tuple[frozenset[str], frozenset[str]]:
    pairs = set(kernel_pairs())
    outgoing = frozenset(right for left, right in pairs if left == surface)
    incoming = frozenset(left for left, right in pairs if right == surface)
    return outgoing, incoming


def low_neighbor_fingerprints() -> frozenset[tuple[frozenset[str], frozenset[str]]]:
    return frozenset(neighbor_fingerprint(surface) for surface in LOW_PROFILE_COMPONENT)


def setwise_stabilizer_count(pair: frozenset[str], autos: list[dict[str, str]]) -> int:
    return sum(1 for auto in autos if frozenset(auto[surface] for surface in pair) == pair)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    blocks = profile_blocks()
    low_autos = low_automorphisms()
    kernel_autos = kernel_automorphisms()
    left_pair_orbit = pair_orbit(LEFT_TARGETS, kernel_autos)
    stabilizer_count = setwise_stabilizer_count(LEFT_TARGETS, kernel_autos)

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
        frozenset(blocks[PROFILE_LOW]) == LOW_PROFILE_COMPONENT
        and frozenset(blocks[PROFILE_MID]) == RIGHT_TARGETS
        and frozenset(blocks[PROFILE_HIGH_BAD]) == HIGH_CENTRALITY_BAD,
        f"profile_block_sizes={[len(blocks[profile]) for profile in (PROFILE_LOW, PROFILE_MID, PROFILE_HIGH_BAD)]}",
    )
    gate(
        f"{PREFIX}4",
        not low_induced_edges()
        and len(low_autos) == factorial(6)
        and vertex_orbit(next(iter(LOW_PROFILE_COMPONENT)), low_autos) == LOW_PROFILE_COMPONENT,
        f"low_edges={len(low_induced_edges())} low_autos={len(low_autos)}",
    )
    gate(
        f"{PREFIX}5",
        len(kernel_autos) == EXPECTED_KERNEL_AUTOMORPHISMS
        and vertex_orbit(next(iter(LOW_PROFILE_COMPONENT)), kernel_autos) == LOW_PROFILE_COMPONENT
        and vertex_orbit(next(iter(RIGHT_TARGETS)), kernel_autos) == RIGHT_TARGETS
        and vertex_orbit(next(iter(HIGH_CENTRALITY_BAD)), kernel_autos) == HIGH_CENTRALITY_BAD,
        f"kernel_autos={len(kernel_autos)}",
    )
    gate(
        f"{PREFIX}6",
        left_pair_orbit == all_low_pairs()
        and len(left_pair_orbit) == EXPECTED_LOW_PAIR_COUNT,
        f"left_pair_orbit_size={len(left_pair_orbit)}",
    )
    gate(
        f"{PREFIX}7",
        stabilizer_count == len(kernel_autos) // EXPECTED_LOW_PAIR_COUNT
        and stabilizer_count == 192,
        f"setwise_stabilizer={stabilizer_count}",
    )
    gate(
        f"{PREFIX}8",
        len(low_neighbor_fingerprints()) == 1,
        "all six low-profile vertices have identical directed kernel-neighborhood fingerprints",
    )
    gate(
        f"{PREFIX}9",
        left_pair_orbit == all_low_pairs()
        and len(low_neighbor_fingerprints()) == 1
        and vertex_orbit(next(iter(LOW_PROFILE_COMPONENT)), kernel_autos) == LOW_PROFILE_COMPONENT,
        "graph symmetry does not make external_basin/oracle_basin a canonical pair",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin low-profile automorphism/orbit reuse fails"
    )
    print(
        "VERDICT: the kernel graph treats the six low-profile basin labels as "
        "one symmetric orbit; the external_basin/oracle_basin pair has orbit all "
        "15 low-profile pairs, so selecting it requires external labels or new structure."
    )


if __name__ == "__main__":
    main()
