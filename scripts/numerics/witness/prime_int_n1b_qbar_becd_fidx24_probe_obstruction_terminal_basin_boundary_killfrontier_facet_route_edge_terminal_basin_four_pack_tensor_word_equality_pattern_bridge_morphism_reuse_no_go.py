#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack tensor-word equality-pattern reuse.

Doc 651 kills exterior/pair character projectors. The next functorial repair
is to use tensor words in the current four-pack representation, then define a
selector by equality pattern, diagonal/off-diagonal relations, symmetric
relations, or finite tensor-word orbit data.

This witness checks the finite word action of the current full S4 symmetry on
the four-pack for word lengths 1 through 4. The orbits are exactly equality
patterns. In particular, the ordered target words
external_basin -> oracle_basin and oracle_basin -> external_basin saturate to
the whole ordered-distinct-pair orbit. Tensor-word functors of the current
action remember only equality pattern, not the target labels.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_tensor_word_equality_pattern_bridge_morphism_reuse_no_go
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
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_BASIN_SURFACE,
    EXTERNAL_SURFACE,
    ORACLE_BASIN_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKTENSORWORDEQPATTERNBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
BASIS = tuple(sorted(FOUR_PACK))
BELL_COUNTS = {1: 1, 2: 2, 3: 5, 4: 15}
ORDERED_TARGET_WORD = (EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE)
REVERSED_TARGET_WORD = (ORACLE_BASIN_SURFACE, EXTERNAL_BASIN_SURFACE)
TARGET_ORDERED_PAIR_SUPPORT = frozenset({ORDERED_TARGET_WORD, REVERSED_TARGET_WORD})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def words(length: int) -> tuple[tuple[str, ...], ...]:
    return tuple(product(BASIS, repeat=length))


def image_word(word: tuple[str, ...], perm_map: dict[str, str]) -> tuple[str, ...]:
    return tuple(perm_map[surface] for surface in word)


def word_orbit(word: tuple[str, ...]) -> frozenset[tuple[str, ...]]:
    return frozenset(image_word(word, perm_map) for perm_map in graph_preserving_permutations())


def equality_pattern(word: tuple[str, ...]) -> tuple[int, ...]:
    seen: dict[str, int] = {}
    pattern: list[int] = []
    for surface in word:
        if surface not in seen:
            seen[surface] = len(seen)
        pattern.append(seen[surface])
    return tuple(pattern)


def equality_pattern_support(pattern: tuple[int, ...]) -> frozenset[tuple[str, ...]]:
    length = len(pattern)
    return frozenset(word for word in words(length) if equality_pattern(word) == pattern)


def orbit_partition(length: int) -> tuple[frozenset[tuple[str, ...]], ...]:
    remaining = set(words(length))
    orbits: list[frozenset[tuple[str, ...]]] = []
    while remaining:
        seed = next(iter(remaining))
        orbit = word_orbit(seed)
        orbits.append(orbit)
        remaining -= orbit
    return tuple(sorted(orbits, key=lambda orbit: (len(orbit), sorted(orbit))))


def pattern_partition(length: int) -> dict[tuple[int, ...], frozenset[tuple[str, ...]]]:
    by_pattern: dict[tuple[int, ...], set[tuple[str, ...]]] = defaultdict(set)
    for word in words(length):
        by_pattern[equality_pattern(word)].add(word)
    return {pattern: frozenset(support) for pattern, support in by_pattern.items()}


def support_saturation(support: frozenset[tuple[str, ...]]) -> frozenset[tuple[str, ...]]:
    saturated: set[tuple[str, ...]] = set()
    for word in support:
        saturated |= set(word_orbit(word))
    return frozenset(saturated)


def ordered_distinct_pairs() -> frozenset[tuple[str, str]]:
    return frozenset((left, right) for left in BASIS for right in BASIS if left != right)


def all_orbits_are_equality_patterns() -> bool:
    for length in BELL_COUNTS:
        orbit_set = set(orbit_partition(length))
        pattern_set = set(pattern_partition(length).values())
        if orbit_set != pattern_set:
            return False
    return True


def orbit_size_profiles() -> dict[int, dict[int, int]]:
    return {
        length: dict(Counter(len(orbit) for orbit in orbit_partition(length)))
        for length in BELL_COUNTS
    }


def target_labels_removed(word: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(surface.rsplit("_nf_", 1)[-1] for surface in word)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

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
        f"four_pack={neighbor_names(FOUR_PACK)} target_word={target_labels_removed(ORDERED_TARGET_WORD)}",
    )
    gate(
        f"{PREFIX}4",
        all_four_pack_rows_and_columns_equal()
        and all_nonattachment_skeletons_equal()
        and len(graph_preserving_permutations()) == 24,
        "current non-attachment structure gives full S4 symmetry before tensor-word functors",
    )
    gate(
        f"{PREFIX}5",
        {length: len(orbit_partition(length)) for length in BELL_COUNTS} == BELL_COUNTS
        and all_orbits_are_equality_patterns(),
        f"orbit_size_profiles={orbit_size_profiles()}",
    )
    gate(
        f"{PREFIX}6",
        word_orbit(ORDERED_TARGET_WORD) == ordered_distinct_pairs()
        and len(word_orbit(ORDERED_TARGET_WORD)) == 12,
        "ordered external->oracle word saturates to the full ordered-distinct-pair orbit",
    )
    gate(
        f"{PREFIX}7",
        support_saturation(TARGET_ORDERED_PAIR_SUPPORT) == ordered_distinct_pairs()
        and support_saturation(TARGET_ORDERED_PAIR_SUPPORT) != TARGET_ORDERED_PAIR_SUPPORT,
        "two ordered target orientations still saturate to all ordered distinct pairs",
    )
    gate(
        f"{PREFIX}8",
        all(
            support_saturation(frozenset({word})) == equality_pattern_support(equality_pattern(word))
            for length in BELL_COUNTS
            for word in words(length)
        ),
        "every length<=4 tensor word saturates exactly to its equality-pattern support",
    )
    gate(
        f"{PREFIX}9",
        all_orbits_are_equality_patterns()
        and support_saturation(TARGET_ORDERED_PAIR_SUPPORT) == ordered_distinct_pairs()
        and len(graph_preserving_permutations()) == 24,
        "tensor-word equality-pattern reuse cannot select external_basin/oracle_basin",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack tensor-word equality-pattern reuse fails"
    )
    print(
        "VERDICT: tensor-word functors of the current S4 action remember "
        "equality patterns only. The external/oracle ordered pair saturates "
        "to all ordered distinct pairs, so the target labels are not recovered."
    )


if __name__ == "__main__":
    main()
