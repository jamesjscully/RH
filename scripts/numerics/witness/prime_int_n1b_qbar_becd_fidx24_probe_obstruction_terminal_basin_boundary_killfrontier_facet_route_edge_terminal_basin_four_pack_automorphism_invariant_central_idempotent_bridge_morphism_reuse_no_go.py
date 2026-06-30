#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack invariant central-idempotent reuse.

Doc 647 kills direct unital path/Karoubi idempotent selection: the desired
rank-two support exists, but it is one of six symmetric choices. The next
categorical repair is to recover canonicity by using automorphism-invariant,
central, trace-invariant, or averaged idempotent data from the same current
category.

This witness checks the support-level obstruction. The current four-pack
automorphism group is the full S4 with the other kernel-component vertices
fixed. Any canonical central/idempotent support built from current vertex
idempotents must be invariant under this action. Its intersection with the
four-pack is therefore either empty or the whole four-pack, never
external_basin/oracle_basin. Averaging the target pair over the orbit gives
equal half-weight on all four vertices, not a rank-two selector.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_automorphism_invariant_central_idempotent_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from itertools import combinations
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
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_incidence_row_bridge_morphism_reuse_no_go import (
    FOUR_PACK,
    neighbor_names,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    FOUR_PACK_BAD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_unital_path_idempotent_bridge_morphism_reuse_no_go import (
    all_four_pack_rows_and_columns_equal,
    all_nonattachment_skeletons_equal,
    graph_preserving_permutations,
    rank_two_idempotent_supports,
    target_pair_orbit,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOINVCENTRALIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def powerset(items: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    return tuple(
        frozenset(combo)
        for size in range(len(items) + 1)
        for combo in combinations(items, size)
    )


def image_support(support: frozenset[str], perm_map: dict[str, str]) -> frozenset[str]:
    return frozenset(perm_map.get(surface, surface) for surface in support)


def invariant_vertex_supports() -> tuple[frozenset[str], ...]:
    permutations = graph_preserving_permutations()
    return tuple(
        support
        for support in powerset(tuple(sorted(KERNEL_COMPONENT)))
        if all(image_support(support, perm_map) == support for perm_map in permutations)
    )


def invariant_four_pack_intersections() -> frozenset[frozenset[str]]:
    return frozenset(support & FOUR_PACK for support in invariant_vertex_supports())


def orbit_partition_on_four_pack() -> tuple[frozenset[str], ...]:
    permutations = graph_preserving_permutations()
    remaining = set(FOUR_PACK)
    orbits: list[frozenset[str]] = []
    while remaining:
        seed = next(iter(remaining))
        orbit = frozenset(perm_map[seed] for perm_map in permutations)
        orbits.append(orbit)
        remaining -= orbit
    return tuple(sorted(orbits, key=lambda orbit: sorted(orbit)))


def target_pair_orbit_incidence_counts() -> dict[str, int]:
    counts = {surface: 0 for surface in FOUR_PACK}
    for perm_map in graph_preserving_permutations():
        image = frozenset(perm_map[surface] for surface in LEFT_TARGETS)
        for surface in image:
            counts[surface] += 1
    return counts


def invariant_boolean_selector_exists() -> bool:
    return any(support & FOUR_PACK == LEFT_TARGETS for support in invariant_vertex_supports())


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    preserving = graph_preserving_permutations()
    invariant_supports = invariant_vertex_supports()
    intersections = invariant_four_pack_intersections()
    orbit = target_pair_orbit()
    orbit_counts = target_pair_orbit_incidence_counts()

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
        FOUR_PACK == LEFT_TARGETS | FOUR_PACK_BAD
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        f"four_pack={neighbor_names(FOUR_PACK)}",
    )
    gate(
        f"{PREFIX}4",
        all_four_pack_rows_and_columns_equal()
        and all_nonattachment_skeletons_equal()
        and len(preserving) == 24,
        "current non-attachment graph/signature structure has full S4 symmetry on the four-pack",
    )
    gate(
        f"{PREFIX}5",
        orbit_partition_on_four_pack() == (FOUR_PACK,),
        f"four_pack_orbit_partition={tuple(neighbor_names(orbit) for orbit in orbit_partition_on_four_pack())}",
    )
    gate(
        f"{PREFIX}6",
        intersections == frozenset({frozenset(), FOUR_PACK})
        and len(invariant_supports) == 128,
        f"invariant_supports={len(invariant_supports)} intersections={tuple(neighbor_names(part) for part in intersections)}",
    )
    gate(
        f"{PREFIX}7",
        not invariant_boolean_selector_exists()
        and LEFT_TARGETS not in intersections,
        "no automorphism-invariant vertex-idempotent support intersects the four-pack in external_basin/oracle_basin",
    )
    gate(
        f"{PREFIX}8",
        orbit == rank_two_idempotent_supports()
        and all(count == 12 for count in orbit_counts.values())
        and len(preserving) == 24,
        f"target_pair_orbit_size={len(orbit)} orbit_incidence_counts={orbit_counts}",
    )
    gate(
        f"{PREFIX}9",
        intersections == frozenset({frozenset(), FOUR_PACK})
        and not invariant_boolean_selector_exists()
        and orbit == rank_two_idempotent_supports(),
        "automorphism-invariant/central idempotent reuse cannot canonically select the target pair",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack automorphism-invariant central idempotent reuse fails"
    )
    print(
        "VERDICT: invariant or central support data from the current category "
        "can see none or all of the four-pack, but not external_basin/oracle_basin. "
        "Averaging the target pair spreads equal weight over all four vertices."
    )


if __name__ == "__main__":
    main()
