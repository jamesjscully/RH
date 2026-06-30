#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack automorphism-quotient support reuse.

Doc 648 kills automorphism-invariant central-idempotent reuse. The next
categorical repair is quotient/descent-shaped: pass to the orbit quotient or
homotopy quotient of the current four-pack symmetry, then recover the desired
pair as a quotient-side equalizer, fiber, fixed locus, or saturated subobject.

This witness checks that quotient-side supports pull back to saturated supports
for the full S4 action on the four-pack. Since the four-pack is one orbit, a
descended support intersects it either in nothing or in all four vertices.
The target pair external_basin/oracle_basin is not saturated; its saturation is
the whole four-pack.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_automorphism_quotient_saturated_support_bridge_morphism_reuse_no_go
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
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_automorphism_invariant_central_idempotent_bridge_morphism_reuse_no_go import (
    invariant_four_pack_intersections,
    invariant_vertex_supports,
    orbit_partition_on_four_pack,
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOQUOTSATSUPPORTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def orbit_partition_on_kernel_component() -> tuple[frozenset[str], ...]:
    permutations = graph_preserving_permutations()
    remaining = set(KERNEL_COMPONENT)
    orbits: list[frozenset[str]] = []
    while remaining:
        seed = next(iter(remaining))
        orbit = frozenset(perm_map.get(seed, seed) for perm_map in permutations)
        orbits.append(orbit)
        remaining -= orbit
    return tuple(sorted(orbits, key=lambda orbit: (len(orbit), sorted(orbit))))


def support_saturation(support: frozenset[str]) -> frozenset[str]:
    saturated: set[str] = set()
    for orbit in orbit_partition_on_kernel_component():
        if support & orbit:
            saturated |= set(orbit)
    return frozenset(saturated)


def quotient_saturated_supports() -> tuple[frozenset[str], ...]:
    orbits = orbit_partition_on_kernel_component()
    supports: list[frozenset[str]] = []
    for size in range(len(orbits) + 1):
        for combo in combinations(orbits, size):
            supports.append(frozenset().union(*combo) if combo else frozenset())
    return tuple(sorted(set(supports), key=lambda support: (len(support), sorted(support))))


def quotient_image_orbits(support: frozenset[str]) -> frozenset[frozenset[str]]:
    return frozenset(orbit for orbit in orbit_partition_on_kernel_component() if support & orbit)


def saturated_selector_exists() -> bool:
    return any(support & FOUR_PACK == LEFT_TARGETS for support in quotient_saturated_supports())


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    kernel_orbits = orbit_partition_on_kernel_component()
    saturated_supports = quotient_saturated_supports()

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
        and orbit_partition_on_four_pack() == (FOUR_PACK,),
        "current non-attachment graph/signature data descends through one four-pack orbit",
    )
    gate(
        f"{PREFIX}5",
        len(kernel_orbits) == 7
        and FOUR_PACK in kernel_orbits
        and sum(1 for orbit in kernel_orbits if len(orbit) == 1) == 6,
        f"kernel_orbit_sizes={[len(orbit) for orbit in kernel_orbits]}",
    )
    gate(
        f"{PREFIX}6",
        support_saturation(LEFT_TARGETS) == FOUR_PACK
        and support_saturation(LEFT_TARGETS) != LEFT_TARGETS,
        f"target_saturation={neighbor_names(support_saturation(LEFT_TARGETS))}",
    )
    gate(
        f"{PREFIX}7",
        len(saturated_supports) == 128
        and set(saturated_supports) == set(invariant_vertex_supports())
        and invariant_four_pack_intersections() == frozenset({frozenset(), FOUR_PACK}),
        "quotient-side supports are exactly automorphism-invariant saturated supports",
    )
    gate(
        f"{PREFIX}8",
        not saturated_selector_exists()
        and quotient_image_orbits(LEFT_TARGETS) == quotient_image_orbits(FOUR_PACK),
        "no quotient-side support pulls back to the target pair; target pair and whole four-pack have the same quotient image",
    )
    gate(
        f"{PREFIX}9",
        support_saturation(LEFT_TARGETS) == FOUR_PACK
        and not saturated_selector_exists()
        and len(saturated_supports) == 128,
        "automorphism quotient/descent/equalizer support reuse cannot select external_basin/oracle_basin",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack automorphism-quotient saturated support reuse fails"
    )
    print(
        "VERDICT: quotient/descent support from the current S4 symmetry pulls "
        "back to saturated supports. The target pair saturates to the whole "
        "four-pack, so quotient-side equalizers or fibers cannot recover it."
    )


if __name__ == "__main__":
    main()
