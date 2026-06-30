#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack signed exterior-orientation reuse.

Doc 651 kills unsigned pair/exterior character projectors. The next escape is
to use the actual signed exterior square: perhaps orientation in
e_external_basin wedge e_oracle_basin supplies the missing target selector.

This witness checks the exact signed Lambda^2 representation of the current
S4 action on the four-pack. It decomposes into two rank-three central
summands. The trivial and sign/orientation character projectors are zero, and
the target wedge line is a non-equivariant coordinate line with a six-choice
orbit. Thus signed exterior orientation does not construct the missing pair.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signed_exterior_orientation_bridge_morphism_reuse_no_go
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
    is_idempotent,
    matadd,
    matmul,
    rank,
    scalar_mul,
    trace,
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGNEDEXTERIORORIENTATIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
BASIS = tuple(sorted(FOUR_PACK))
INDEX = {surface: index for index, surface in enumerate(BASIS)}
WEDGE_BASIS = tuple(combinations(range(len(BASIS)), 2))
WEDGE_INDEX = {pair: index for index, pair in enumerate(WEDGE_BASIS)}
TARGET_WEDGE_PAIR = tuple(sorted(INDEX[surface] for surface in LEFT_TARGETS))

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def signed_zero_matrix() -> Matrix:
    return tuple(tuple(Fraction(0) for _ in WEDGE_BASIS) for _ in WEDGE_BASIS)


def signed_identity_matrix() -> Matrix:
    return tuple(
        tuple(Fraction(1 if row == col else 0) for col in range(len(WEDGE_BASIS)))
        for row in range(len(WEDGE_BASIS))
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix)))


def sign_of_permutation(perm_map: dict[str, str]) -> int:
    perm = [INDEX[perm_map[surface]] for surface in BASIS]
    inversions = sum(1 for left in range(len(perm)) for right in range(left + 1, len(perm)) if perm[left] > perm[right])
    return -1 if inversions % 2 else 1


def fixed_points(perm_map: dict[str, str]) -> int:
    return sum(1 for surface in BASIS if perm_map[surface] == surface)


def signed_wedge_matrix(perm_map: dict[str, str]) -> Matrix:
    rows = [[Fraction(0) for _ in WEDGE_BASIS] for _ in WEDGE_BASIS]
    for col, (left, right) in enumerate(WEDGE_BASIS):
        image_left = INDEX[perm_map[BASIS[left]]]
        image_right = INDEX[perm_map[BASIS[right]]]
        image_pair = tuple(sorted((image_left, image_right)))
        rows[WEDGE_INDEX[image_pair]][col] = Fraction(1 if image_left < image_right else -1)
    return tuple(tuple(row) for row in rows)


def commutes_with_all_signed_wedge(matrix: Matrix) -> bool:
    return all(
        matmul(signed_wedge_matrix(perm_map), matrix)
        == matmul(matrix, signed_wedge_matrix(perm_map))
        for perm_map in graph_preserving_permutations()
    )


def standard_character(perm_map: dict[str, str]) -> int:
    return fixed_points(perm_map) - 1


def sign_standard_character(perm_map: dict[str, str]) -> int:
    return sign_of_permutation(perm_map) * standard_character(perm_map)


def character_projector(character_name: str) -> Matrix:
    total = signed_zero_matrix()
    for perm_map in graph_preserving_permutations():
        if character_name == "trivial":
            dimension = 1
            character_value = 1
        elif character_name == "sign":
            dimension = 1
            character_value = sign_of_permutation(perm_map)
        elif character_name == "standard":
            dimension = 3
            character_value = standard_character(perm_map)
        elif character_name == "sign_standard":
            dimension = 3
            character_value = sign_standard_character(perm_map)
        else:
            raise ValueError(character_name)
        total = matadd(
            total,
            scalar_mul(
                Fraction(dimension * character_value, 24),
                transpose(signed_wedge_matrix(perm_map)),
            ),
        )
    return total


def target_wedge_line_projector() -> Matrix:
    target_index = WEDGE_INDEX[TARGET_WEDGE_PAIR]
    return tuple(
        tuple(Fraction(1 if row == col == target_index else 0) for col in range(len(WEDGE_BASIS)))
        for row in range(len(WEDGE_BASIS))
    )


def target_wedge_line_orbit_size() -> int:
    target = target_wedge_line_projector()
    return len(
        {
            matmul(matmul(signed_wedge_matrix(perm_map), target), transpose(signed_wedge_matrix(perm_map)))
            for perm_map in graph_preserving_permutations()
        }
    )


def central_signed_wedge_projectors() -> tuple[Matrix, ...]:
    standard = character_projector("standard")
    sign_standard = character_projector("sign_standard")
    return (
        signed_zero_matrix(),
        standard,
        sign_standard,
        signed_identity_matrix(),
    )


def central_signed_wedge_projector_ranks() -> tuple[int, ...]:
    return tuple(sorted(rank(projector) for projector in central_signed_wedge_projectors()))


def diagonal_profile(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(matrix[index][index] for index in range(len(WEDGE_BASIS)))


def wedge_pair_names(pair: tuple[int, int]) -> tuple[str, str]:
    return tuple(BASIS[index].rsplit("_nf_", 1)[-1] for index in pair)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    target = target_wedge_line_projector()
    trivial = character_projector("trivial")
    sign = character_projector("sign")
    standard = character_projector("standard")
    sign_standard = character_projector("sign_standard")

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
        f"four_pack={neighbor_names(FOUR_PACK)} target_wedge={wedge_pair_names(TARGET_WEDGE_PAIR)}",
    )
    gate(
        f"{PREFIX}4",
        all_four_pack_rows_and_columns_equal()
        and all_nonattachment_skeletons_equal()
        and len(graph_preserving_permutations()) == 24
        and target_pair_orbit() == frozenset(frozenset(BASIS[index] for index in pair) for pair in WEDGE_BASIS),
        "current non-attachment structure gives full S4 signed wedge action",
    )
    gate(
        f"{PREFIX}5",
        trivial == signed_zero_matrix()
        and sign == signed_zero_matrix()
        and rank(trivial) == 0
        and rank(sign) == 0,
        "trivial and sign/orientation character projectors vanish in signed Lambda^2(Q^4)",
    )
    gate(
        f"{PREFIX}6",
        all(commutes_with_all_signed_wedge(projector) and is_idempotent(projector) for projector in central_signed_wedge_projectors())
        and matmul(standard, sign_standard) == signed_zero_matrix()
        and central_signed_wedge_projector_ranks() == (0, 3, 3, 6),
        f"central_signed_wedge_ranks={central_signed_wedge_projector_ranks()}",
    )
    gate(
        f"{PREFIX}7",
        diagonal_profile(standard) == tuple(Fraction(1, 2) for _ in WEDGE_BASIS)
        and diagonal_profile(sign_standard) == tuple(Fraction(1, 2) for _ in WEDGE_BASIS)
        and trace(standard) == 3
        and trace(sign_standard) == 3,
        "rank-three signed wedge summands have uniform half diagonal on all wedge basis lines",
    )
    gate(
        f"{PREFIX}8",
        rank(target) == 1
        and is_idempotent(target)
        and not commutes_with_all_signed_wedge(target)
        and target_wedge_line_orbit_size() == 6,
        f"target_wedge_rank={rank(target)} target_wedge_orbit={target_wedge_line_orbit_size()}",
    )
    gate(
        f"{PREFIX}9",
        trivial == signed_zero_matrix()
        and sign == signed_zero_matrix()
        and central_signed_wedge_projector_ranks() == (0, 3, 3, 6)
        and not commutes_with_all_signed_wedge(target),
        "signed exterior orientation reuse cannot select external_basin/oracle_basin",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack signed exterior orientation reuse fails"
    )
    print(
        "VERDICT: the signed exterior square has two rank-three central "
        "summands and no trivial/sign orientation line. The external/oracle "
        "wedge is a non-equivariant coordinate line with a six-choice orbit."
    )


if __name__ == "__main__":
    main()
