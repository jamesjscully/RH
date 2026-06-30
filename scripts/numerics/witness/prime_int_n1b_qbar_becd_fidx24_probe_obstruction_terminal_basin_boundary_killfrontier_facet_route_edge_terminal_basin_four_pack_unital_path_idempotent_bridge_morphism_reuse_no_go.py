#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack unital path-idempotent reuse.

Doc 646 kills positive-length path-power composition reuse. The categorical
escape is to add identities: in the unital path category or Karoubi envelope,
vertex idempotents exist, so perhaps the idempotent sum
e_external_basin + e_oracle_basin is the missing selector.

This witness checks that the current structure does not select that idempotent
sum. All 24 permutations of the four-pack preserve the current terminal-basin
kernel-pair graph when the other vertices are fixed. The target rank-two
idempotent support is therefore one of six indistinguishable rank-two supports.
Selecting it is attachment-token lookup or external choice, not a
carrier-native categorical construction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_unital_path_idempotent_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from itertools import combinations, permutations
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
    RIGHT_NEIGHBORS,
    incoming,
    neighbor_names,
    outgoing,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_path_power_composition_bridge_morphism_reuse_no_go import (
    all_power_rows_and_columns_constant,
    polynomial_readouts_constant,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    COMMON_STRUCTURAL_SIGNATURE,
    FOUR_PACK_BAD,
    normalized_signature,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKUNITALPATHIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def rank_two_idempotent_supports() -> frozenset[frozenset[str]]:
    return frozenset(frozenset(combo) for combo in combinations(FOUR_PACK, 2))


def permuted_pairs(perm_map: dict[str, str]) -> frozenset[tuple[str, str]]:
    def image(surface: str) -> str:
        return perm_map.get(surface, surface)

    return frozenset((image(left), image(right)) for left, right in kernel_pairs())


def graph_preserving_permutations() -> tuple[dict[str, str], ...]:
    surfaces = tuple(sorted(FOUR_PACK))
    pair_set = frozenset(kernel_pairs())
    preserving: list[dict[str, str]] = []
    for permuted in permutations(surfaces):
        perm_map = dict(zip(surfaces, permuted))
        if permuted_pairs(perm_map) == pair_set:
            preserving.append(perm_map)
    return tuple(preserving)


def target_pair_orbit() -> frozenset[frozenset[str]]:
    return frozenset(
        frozenset(perm_map[surface] for surface in LEFT_TARGETS)
        for perm_map in graph_preserving_permutations()
    )


def all_nonattachment_skeletons_equal() -> bool:
    return (
        frozenset(normalized_signature(surface) for surface in FOUR_PACK)
        == frozenset({COMMON_STRUCTURAL_SIGNATURE})
    )


def all_four_pack_rows_and_columns_equal() -> bool:
    return all(
        outgoing(surface) == RIGHT_NEIGHBORS and incoming(surface) == RIGHT_NEIGHBORS
        for surface in FOUR_PACK
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    preserving = graph_preserving_permutations()
    rank_two_supports = rank_two_idempotent_supports()
    orbit = target_pair_orbit()

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
        and all_power_rows_and_columns_constant()
        and polynomial_readouts_constant(),
        "incidence, path-power, and sample positive polynomial readouts are symmetric on the four-pack",
    )
    gate(
        f"{PREFIX}5",
        all_nonattachment_skeletons_equal(),
        "non-attachment doc610 signature skeleton is common on the four-pack",
    )
    gate(
        f"{PREFIX}6",
        len(preserving) == 24,
        f"four_pack_graph_preserving_permutations={len(preserving)}",
    )
    gate(
        f"{PREFIX}7",
        orbit == rank_two_supports and len(orbit) == 6,
        f"target_pair_orbit_size={len(orbit)} rank_two_supports={len(rank_two_supports)}",
    )
    gate(
        f"{PREFIX}8",
        LEFT_TARGETS in rank_two_supports
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "the desired rank-two idempotent support is selected only by external/oracle attachment tokens",
    )
    gate(
        f"{PREFIX}9",
        len(preserving) == 24
        and orbit == rank_two_supports
        and all_nonattachment_skeletons_equal()
        and all_four_pack_rows_and_columns_equal(),
        "unital path idempotents add vertex names but no canonical target-pair selector",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack unital path-idempotent reuse fails"
    )
    print(
        "VERDICT: the unital path/Karoubi move can form vertex idempotent sums, "
        "but current structure makes the target pair one of six symmetric "
        "rank-two choices. Selecting it is external choice or attachment-token lookup."
    )


if __name__ == "__main__":
    main()
