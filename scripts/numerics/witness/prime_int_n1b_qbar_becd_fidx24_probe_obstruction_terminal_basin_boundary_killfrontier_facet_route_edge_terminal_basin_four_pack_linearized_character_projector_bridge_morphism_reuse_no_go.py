#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack linearized character-projector reuse.

Doc 649 kills quotient/descent support reuse. The next categorical repair is
linearized: instead of selecting a subset of vertices, pass to the vector space
on the four-pack and use an automorphism character, orientation, trace, or
central group-algebra projector to split external_basin/oracle_basin.

This witness checks the exact S4 permutation representation on the four-pack.
The commutant consists of matrices with one diagonal value and one off-diagonal
value. Its idempotents have ranks 0, 1, 3, and 4. The target-pair coordinate
projector has rank 2 but is not S4-equivariant, while character-central
projectors give only the all-ones line, the standard complement, zero, or the
identity. Linearization of the current symmetry therefore does not provide the
missing rank-two selector.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_linearized_character_projector_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from fractions import Fraction
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
    EXTERNAL_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKLINCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
BASIS = tuple(sorted(FOUR_PACK))
INDEX = {surface: index for index, surface in enumerate(BASIS)}

Matrix = tuple[tuple[Fraction, ...], ...]

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def zero_matrix() -> Matrix:
    return tuple(tuple(Fraction(0) for _ in BASIS) for _ in BASIS)


def identity_matrix() -> Matrix:
    return tuple(
        tuple(Fraction(1 if row == col else 0) for col in range(len(BASIS)))
        for row in range(len(BASIS))
    )


def all_ones_matrix() -> Matrix:
    return tuple(tuple(Fraction(1) for _ in BASIS) for _ in BASIS)


def central_commutant_matrix(diagonal: Fraction, off_diagonal: Fraction) -> Matrix:
    return tuple(
        tuple(diagonal if row == col else off_diagonal for col in range(len(BASIS)))
        for row in range(len(BASIS))
    )


def target_pair_projector() -> Matrix:
    return tuple(
        tuple(
            Fraction(1 if row == col and BASIS[row] in LEFT_TARGETS else 0)
            for col in range(len(BASIS))
        )
        for row in range(len(BASIS))
    )


def permutation_matrix(perm_map: dict[str, str]) -> Matrix:
    size = len(BASIS)
    rows = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for source in BASIS:
        rows[INDEX[perm_map[source]]][INDEX[source]] = Fraction(1)
    return tuple(tuple(row) for row in rows)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(sum(left[row][mid] * right[mid][col] for mid in range(size)) for col in range(size))
        for row in range(size)
    )


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scalar_mul(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def matadd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def trace(matrix: Matrix) -> Fraction:
    return sum(matrix[index][index] for index in range(len(matrix)))


def rank(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
    pivot_row = 0
    for col in range(col_count):
        pivot = next((row for row in range(pivot_row, row_count) if rows[row][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not rows[row][col]:
                continue
            factor = rows[row][col]
            rows[row] = [
                current - factor * pivot_value_row
                for current, pivot_value_row in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def commutes_with_all(matrix: Matrix) -> bool:
    return all(
        matmul(permutation_matrix(perm_map), matrix) == matmul(matrix, permutation_matrix(perm_map))
        for perm_map in graph_preserving_permutations()
    )


def is_idempotent(matrix: Matrix) -> bool:
    return matmul(matrix, matrix) == matrix


def central_idempotents_in_permutation_module() -> tuple[Matrix, ...]:
    # End_{S4}(Q^4) is generated by I and J for the transitive four-point action.
    return (
        zero_matrix(),
        scalar_mul(Fraction(1, 4), all_ones_matrix()),
        matsub(identity_matrix(), scalar_mul(Fraction(1, 4), all_ones_matrix())),
        identity_matrix(),
    )


def central_idempotent_ranks() -> tuple[int, ...]:
    return tuple(sorted(rank(projector) for projector in central_idempotents_in_permutation_module()))


def diagonal_profiles() -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(projector[index][index] for index in range(len(BASIS)))
        for projector in central_idempotents_in_permutation_module()
    )


def target_pair_projector_orbit_size() -> int:
    target = target_pair_projector()
    return len(
        {
            matmul(matmul(permutation_matrix(perm_map), target), transpose(permutation_matrix(perm_map)))
            for perm_map in graph_preserving_permutations()
        }
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix)))


def sign_of_permutation(perm_map: dict[str, str]) -> int:
    perm = [INDEX[perm_map[surface]] for surface in BASIS]
    inversions = sum(1 for left in range(len(perm)) for right in range(left + 1, len(perm)) if perm[left] > perm[right])
    return -1 if inversions % 2 else 1


def character_projector(character: str) -> Matrix:
    total = zero_matrix()
    for perm_map in graph_preserving_permutations():
        coefficient = Fraction(1, 24)
        if character == "sign":
            coefficient *= sign_of_permutation(perm_map)
        elif character != "trivial":
            raise ValueError(character)
        total = matadd(total, scalar_mul(coefficient, permutation_matrix(perm_map)))
    return total


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    target = target_pair_projector()
    central_projectors = central_idempotents_in_permutation_module()
    trivial_projector = character_projector("trivial")
    sign_projector = character_projector("sign")

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
        and len(graph_preserving_permutations()) == 24,
        "current non-attachment structure gives the full S4 permutation representation on the four-pack",
    )
    gate(
        f"{PREFIX}5",
        all(commutes_with_all(projector) and is_idempotent(projector) for projector in central_projectors)
        and central_idempotent_ranks() == (0, 1, 3, 4),
        f"central_idempotent_ranks={central_idempotent_ranks()}",
    )
    gate(
        f"{PREFIX}6",
        rank(target) == 2
        and is_idempotent(target)
        and not commutes_with_all(target)
        and target_pair_projector_orbit_size() == 6,
        f"target_rank={rank(target)} target_orbit_size={target_pair_projector_orbit_size()}",
    )
    gate(
        f"{PREFIX}7",
        trivial_projector == scalar_mul(Fraction(1, 4), all_ones_matrix())
        and sign_projector == zero_matrix()
        and rank(trivial_projector) == 1
        and rank(sign_projector) == 0,
        "trivial character gives the all-ones line; sign/orientation projector is zero in the four-point permutation module",
    )
    gate(
        f"{PREFIX}8",
        all(len(set(profile)) == 1 for profile in diagonal_profiles())
        and all(trace(projector) in {0, 1, 3, 4} for projector in central_projectors),
        f"diagonal_profiles={diagonal_profiles()}",
    )
    gate(
        f"{PREFIX}9",
        central_idempotent_ranks() == (0, 1, 3, 4)
        and rank(target) == 2
        and not commutes_with_all(target)
        and sign_projector == zero_matrix(),
        "linearized character/central projector reuse cannot supply the target-pair projector",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack linearized character-projector reuse fails"
    )
    print(
        "VERDICT: linearizing the current S4 action gives only rank 0, 1, 3, "
        "and 4 central idempotents. The rank-two target projector is not "
        "equivariant, and the sign/orientation projector is zero."
    )


if __name__ == "__main__":
    main()
