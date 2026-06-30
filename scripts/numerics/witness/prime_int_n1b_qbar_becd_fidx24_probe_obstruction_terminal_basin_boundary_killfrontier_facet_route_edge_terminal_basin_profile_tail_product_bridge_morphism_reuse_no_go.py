#!/usr/bin/env python3
r"""No-go for terminal-basin graph-profile/tail-shape product reuse.

Docs 637 and 638 kill graph-profile and tail-shape selection separately, and
doc 640 kills raw graph orbit selection. The next disciplined repair is to
combine graph profile with structural tail shape and ask whether the product
partition makes external_basin/oracle_basin canonical.

This witness checks the product partition on the ten-surface terminal-basin
kernel component. The product features refine the low profile, but the left
targets remain in a four-element block with noncanonical_basin and
retuned_basin. No union of product blocks selects either the left target pair
or all four target endpoints.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_profile_tail_product_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations, product
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
    BASIN_NOT_ABSORBING_SURFACE,
    BASIN_NOT_EXTENSIONAL_SURFACE,
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    NO_BASIN_CERTIFICATE_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    TARGET_ENDPOINTS,
    UNBOUNDED_BASIN_SEARCH_SURFACE,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    THREE_SEGMENT_LOW_PROFILE,
    TWO_SEGMENT_LOW_PROFILE,
    shape_features,
    token_support,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go import (
    PROFILE_HIGH_BAD,
    PROFILE_LOW,
    PROFILE_MID,
    graph_profiles,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINPROFILETAILPRODUCTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
RIGHT_TARGET_SINGLETONS = frozenset(
    {frozenset({BASIN_NOT_ABSORBING_SURFACE}), frozenset({BASIN_NOT_EXTENSIONAL_SURFACE})}
)
HIGH_BAD_SINGLETONS = frozenset(
    {frozenset({NO_BASIN_CERTIFICATE_SURFACE}), frozenset({UNBOUNDED_BASIN_SEARCH_SURFACE})}
)
EXPECTED_PRODUCT_BLOCKS = frozenset(
    {
        TWO_SEGMENT_LOW_PROFILE,
        THREE_SEGMENT_LOW_PROFILE,
        frozenset({BASIN_NOT_ABSORBING_SURFACE}),
        frozenset({BASIN_NOT_EXTENSIONAL_SURFACE}),
        frozenset({NO_BASIN_CERTIFICATE_SURFACE}),
        frozenset({UNBOUNDED_BASIN_SEARCH_SURFACE}),
    }
)
EXPECTED_PRODUCT_AUTOS = factorial(4) * factorial(2)
EXPECTED_TWO_SEGMENT_PAIR_COUNT = 6

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def product_key(surface: str) -> tuple[tuple[int, int, int, int, int, int], tuple[tuple[str, str], ...]]:
    return graph_profiles()[surface], tuple(sorted(shape_features(surface)))


def product_blocks() -> frozenset[frozenset[str]]:
    blocks: dict[
        tuple[tuple[int, int, int, int, int, int], tuple[tuple[str, str], ...]],
        set[str],
    ] = defaultdict(set)
    for surface in KERNEL_COMPONENT:
        blocks[product_key(surface)].add(surface)
    return frozenset(frozenset(block) for block in blocks.values())


def union_of_blocks_selects(target: frozenset[str]) -> bool:
    blocks = tuple(product_blocks())
    for size in range(1, len(blocks) + 1):
        for combo in combinations(blocks, size):
            if frozenset().union(*combo) == target:
                return True
    return False


def block_containing(target: frozenset[str]) -> frozenset[str]:
    matches = [block for block in product_blocks() if target <= block]
    if len(matches) != 1:
        raise AssertionError(f"expected one product block containing {target}, got {matches}")
    return matches[0]


def is_automorphism(mapping: dict[str, str]) -> bool:
    edges = frozenset(kernel_pairs())
    return frozenset((mapping[left], mapping[right]) for left, right in edges) == edges


def product_block_preserving_automorphisms() -> list[dict[str, str]]:
    blocks = tuple(sorted((tuple(sorted(block)) for block in product_blocks()), key=lambda block: (len(block), block)))
    domain = tuple(surface for block in blocks for surface in block)
    autos: list[dict[str, str]] = []
    for block_images in product(*(permutations(block) for block in blocks)):
        image = tuple(surface for block in block_images for surface in block)
        mapping = dict(zip(domain, image))
        if is_automorphism(mapping):
            autos.append(mapping)
    return autos


def pair_orbit(pair: frozenset[str], autos: list[dict[str, str]]) -> frozenset[frozenset[str]]:
    left, right = tuple(pair)
    return frozenset(frozenset({auto[left], auto[right]}) for auto in autos)


def all_pairs_in(block: frozenset[str]) -> frozenset[frozenset[str]]:
    return frozenset(frozenset(pair) for pair in combinations(block, 2))


def profile_support(profile: tuple[int, int, int, int, int, int]) -> frozenset[str]:
    profiles = graph_profiles()
    return frozenset(surface for surface, actual in profiles.items() if actual == profile)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    blocks = product_blocks()
    left_block = block_containing(LEFT_TARGETS)
    autos = product_block_preserving_automorphisms()
    left_pair_orbit = pair_orbit(LEFT_TARGETS, autos)

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
        profile_support(PROFILE_LOW) == TWO_SEGMENT_LOW_PROFILE | THREE_SEGMENT_LOW_PROFILE
        and profile_support(PROFILE_MID) == TARGET_ENDPOINTS - LEFT_TARGETS
        and profile_support(PROFILE_HIGH_BAD)
        == frozenset({NO_BASIN_CERTIFICATE_SURFACE, UNBOUNDED_BASIN_SEARCH_SURFACE}),
        "graph profiles split into low mixed, middle right-target, and high bad blocks",
    )
    gate(
        f"{PREFIX}4",
        blocks == EXPECTED_PRODUCT_BLOCKS and len(blocks) == 6,
        f"product_block_sizes={sorted(len(block) for block in blocks)}",
    )
    gate(
        f"{PREFIX}5",
        left_block == TWO_SEGMENT_LOW_PROFILE
        and len(left_block - LEFT_TARGETS) == 2,
        f"left_block={sorted(surface.rsplit('_nf_', 1)[-1] for surface in left_block)}",
    )
    gate(
        f"{PREFIX}6",
        not union_of_blocks_selects(LEFT_TARGETS)
        and not union_of_blocks_selects(TARGET_ENDPOINTS),
        "no union of graph-profile/tail-shape product blocks selects the target endpoints",
    )
    gate(
        f"{PREFIX}7",
        len(autos) == EXPECTED_PRODUCT_AUTOS
        and left_pair_orbit == all_pairs_in(TWO_SEGMENT_LOW_PROFILE)
        and len(left_pair_orbit) == EXPECTED_TWO_SEGMENT_PAIR_COUNT,
        f"product_autos={len(autos)} left_pair_orbit_size={len(left_pair_orbit)}",
    )
    gate(
        f"{PREFIX}8",
        token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS
        and block_containing(token_support(ATTACHMENT_TOKENS)) == TWO_SEGMENT_LOW_PROFILE,
        "external/oracle attachment tokens still cut inside a four-element product block",
    )
    gate(
        f"{PREFIX}9",
        left_block == TWO_SEGMENT_LOW_PROFILE
        and not union_of_blocks_selects(LEFT_TARGETS)
        and left_pair_orbit == all_pairs_in(TWO_SEGMENT_LOW_PROFILE),
        "product of current graph and tail invariants does not construct the missing separator",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin graph-profile/tail-shape product reuse fails"
    )
    print(
        "VERDICT: graph profile plus structural tail shape leaves "
        "external_basin/oracle_basin in a four-element block with "
        "noncanonical_basin/retuned_basin; selecting the target pair still "
        "requires attachment tokens or new structure."
    )


if __name__ == "__main__":
    main()
