#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack exterior/pair character-projector reuse.

Doc 650 kills character projectors on the linearized four-pack vertex space.
The next representation-theoretic repair is to pass to pair space, or
equivalently the exterior-square/pair-basis representation. This is dangerous
because the S4 action on the six two-element subsets has a genuine rank-two
central summand.

This witness checks that the rank-two central summand is not the target pair.
The target pair is one basis vector among the six pair-basis elements, while
the rank-two central projector is uniform on all six pair diagonals. Thus the
rank coincidence is representation-theoretic noise, not a carrier-native
selector for external_basin/oracle_basin.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_exterior_pair_character_projector_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from fractions import Fraction
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
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_linearized_character_projector_bridge_morphism_reuse_no_go import (
    Matrix,
    identity_matrix,
    is_idempotent,
    matadd,
    matmul,
    rank,
    scalar_mul,
    trace,
    zero_matrix,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    FOUR_PACK_BAD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_unital_path_idempotent_bridge_morphism_reuse_no_go import (
    all_four_pack_rows_and_columns_equal,
    all_nonattachment_skeletons_equal,
    graph_preserving_permutations,
    target_pair_orbit,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKEXTPAIRCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
PAIR_BASIS = tuple(frozenset(pair) for pair in combinations(sorted(FOUR_PACK), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIR_BASIS)}
TARGET_PAIR_BASIS_VECTOR = LEFT_TARGETS

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def pair_identity_matrix() -> Matrix:
    size = len(PAIR_BASIS)
    return tuple(
        tuple(Fraction(1 if row == col else 0) for col in range(size))
        for row in range(size)
    )


def pair_zero_matrix() -> Matrix:
    size = len(PAIR_BASIS)
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def all_ones_pair_matrix() -> Matrix:
    size = len(PAIR_BASIS)
    return tuple(tuple(Fraction(1) for _ in range(size)) for _ in range(size))


def disjoint_pair_matrix() -> Matrix:
    rows = []
    for left in PAIR_BASIS:
        rows.append(
            tuple(Fraction(1 if left.isdisjoint(right) else 0) for right in PAIR_BASIS)
        )
    return tuple(rows)


def target_pair_coordinate_projector() -> Matrix:
    target_index = PAIR_INDEX[TARGET_PAIR_BASIS_VECTOR]
    size = len(PAIR_BASIS)
    return tuple(
        tuple(Fraction(1 if row == col == target_index else 0) for col in range(size))
        for row in range(size)
    )


def pair_permutation_matrix(perm_map: dict[str, str]) -> Matrix:
    size = len(PAIR_BASIS)
    rows = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for source_pair in PAIR_BASIS:
        image_pair = frozenset(perm_map[surface] for surface in source_pair)
        rows[PAIR_INDEX[image_pair]][PAIR_INDEX[source_pair]] = Fraction(1)
    return tuple(tuple(row) for row in rows)


def commutes_with_all_pair_permutations(matrix: Matrix) -> bool:
    return all(
        matmul(pair_permutation_matrix(perm_map), matrix)
        == matmul(matrix, pair_permutation_matrix(perm_map))
        for perm_map in graph_preserving_permutations()
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix)))


def target_pair_projector_orbit_size() -> int:
    target = target_pair_coordinate_projector()
    return len(
        {
            matmul(matmul(pair_permutation_matrix(perm_map), target), transpose(pair_permutation_matrix(perm_map)))
            for perm_map in graph_preserving_permutations()
        }
    )


def rank_two_pair_projector() -> Matrix:
    # S4 on two-subsets is the Johnson J(4,2) scheme. The disjoint-pair matrix
    # has +1 eigenspace of rank 3; removing the all-ones line gives the
    # rank-two central summand.
    plus_disjoint = scalar_mul(Fraction(1, 2), matadd(pair_identity_matrix(), disjoint_pair_matrix()))
    all_ones_line = scalar_mul(Fraction(1, 6), all_ones_pair_matrix())
    return tuple(
        tuple(plus_disjoint[row][col] - all_ones_line[row][col] for col in range(len(PAIR_BASIS)))
        for row in range(len(PAIR_BASIS))
    )


def rank_three_pair_projector() -> Matrix:
    return scalar_mul(Fraction(1, 2), tuple(
        tuple(pair_identity_matrix()[row][col] - disjoint_pair_matrix()[row][col] for col in range(len(PAIR_BASIS)))
        for row in range(len(PAIR_BASIS))
    ))


def rank_one_pair_projector() -> Matrix:
    return scalar_mul(Fraction(1, 6), all_ones_pair_matrix())


def central_pair_projectors() -> tuple[Matrix, ...]:
    p1 = rank_one_pair_projector()
    p2 = rank_two_pair_projector()
    p3 = rank_three_pair_projector()
    return (
        pair_zero_matrix(),
        p1,
        p2,
        p3,
        matadd(p1, p2),
        matadd(p1, p3),
        matadd(p2, p3),
        pair_identity_matrix(),
    )


def central_pair_projector_ranks() -> tuple[int, ...]:
    return tuple(sorted(rank(projector) for projector in central_pair_projectors()))


def diagonal_profile(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(matrix[index][index] for index in range(len(PAIR_BASIS)))


def pair_names(pair: frozenset[str]) -> tuple[str, ...]:
    return tuple(sorted(surface.rsplit("_nf_", 1)[-1] for surface in pair))


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    target = target_pair_coordinate_projector()
    rank_two = rank_two_pair_projector()

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
        f"four_pack={neighbor_names(FOUR_PACK)} target_pair={pair_names(TARGET_PAIR_BASIS_VECTOR)}",
    )
    gate(
        f"{PREFIX}4",
        all_four_pack_rows_and_columns_equal()
        and all_nonattachment_skeletons_equal()
        and len(graph_preserving_permutations()) == 24
        and len(PAIR_BASIS) == 6
        and target_pair_orbit() == frozenset(PAIR_BASIS),
        "current non-attachment structure gives the transitive S4 action on six two-subsets",
    )
    gate(
        f"{PREFIX}5",
        all(commutes_with_all_pair_permutations(projector) and is_idempotent(projector) for projector in central_pair_projectors())
        and central_pair_projector_ranks() == (0, 1, 2, 3, 3, 4, 5, 6),
        f"central_pair_projector_ranks={central_pair_projector_ranks()}",
    )
    gate(
        f"{PREFIX}6",
        rank(rank_two) == 2
        and is_idempotent(rank_two)
        and commutes_with_all_pair_permutations(rank_two)
        and diagonal_profile(rank_two) == tuple(Fraction(1, 3) for _ in PAIR_BASIS),
        f"rank_two_diagonal={diagonal_profile(rank_two)} trace={trace(rank_two)}",
    )
    gate(
        f"{PREFIX}7",
        rank(target) == 1
        and is_idempotent(target)
        and not commutes_with_all_pair_permutations(target)
        and target_pair_projector_orbit_size() == 6,
        f"target_coordinate_rank={rank(target)} target_projector_orbit={target_pair_projector_orbit_size()}",
    )
    gate(
        f"{PREFIX}8",
        rank_two != target
        and all(value == Fraction(1, 3) for value in diagonal_profile(rank_two))
        and diagonal_profile(target).count(Fraction(1)) == 1,
        "the rank-two central pair-space summand is uniform on all pair-basis elements, not the target-pair coordinate",
    )
    gate(
        f"{PREFIX}9",
        rank(rank_two) == 2
        and commutes_with_all_pair_permutations(rank_two)
        and rank(target) == 1
        and not commutes_with_all_pair_permutations(target),
        "exterior/pair character-projector reuse confuses a rank-two irrep with the target pair",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack exterior pair character-projector reuse fails"
    )
    print(
        "VERDICT: pair/exterior-square linearization contains a canonical "
        "rank-two summand, but it is uniform across all six two-subsets. "
        "The actual target pair is a non-equivariant coordinate choice."
    )


if __name__ == "__main__":
    main()
