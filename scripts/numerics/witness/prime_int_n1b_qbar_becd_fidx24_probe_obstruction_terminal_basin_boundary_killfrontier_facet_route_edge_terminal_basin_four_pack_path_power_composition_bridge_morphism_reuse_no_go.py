#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack path-power composition reuse.

Doc 645 kills linear degree-map readouts of the current incidence table. The
next composition-shaped repair is to iterate that table: perhaps two-step,
three-step, or higher positive-length paths through the terminal-basin kernel
separate external_basin/oracle_basin from noncanonical_basin/retuned_basin.

This witness checks adjacency powers of the current directed kernel graph.
All positive-length path rows and columns tested here are identical on the
four-pack. Since the first rows and columns already agree, multiplying by the
same adjacency matrix cannot create a distinction; any positive-length
adjacency-polynomial readout of the current relation is constant on the
four-pack.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_path_power_composition_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

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
    RIGHT_TARGETS,
    incoming,
    neighbor_names,
    outgoing,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_right_target_projection_bridge_morphism_reuse_no_go import (
    HIGH_CENTRALITY_BAD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    FOUR_PACK_BAD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKPATHPOWERCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
BASIS = tuple(sorted(KERNEL_COMPONENT))
INDEX = {surface: index for index, surface in enumerate(BASIS)}
MAX_POWER = 7
SAMPLE_WEIGHTS = (
    tuple(range(1, len(BASIS) + 1)),
    tuple((-1) ** index * (index + 2) for index in range(len(BASIS))),
    tuple(5 if surface in RIGHT_TARGETS else -3 for surface in BASIS),
)
SAMPLE_POLYNOMIALS = (
    (1, 1, 0, 0, 0, 0, 0),
    (0, 2, -1, 0, 0, 0, 0),
    (3, -1, 0, 2, 0, 0, 1),
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def adjacency_matrix() -> tuple[tuple[int, ...], ...]:
    rows = [[0 for _ in BASIS] for _ in BASIS]
    for left, right in kernel_pairs():
        if left in INDEX and right in INDEX:
            rows[INDEX[left]][INDEX[right]] = 1
    return tuple(tuple(row) for row in rows)


def matmul(left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(sum(left[row][middle] * right[middle][col] for middle in range(size)) for col in range(size))
        for row in range(size)
    )


def matrix_powers(max_power: int) -> dict[int, tuple[tuple[int, ...], ...]]:
    adjacency = adjacency_matrix()
    powers = {1: adjacency}
    current = adjacency
    for power in range(2, max_power + 1):
        current = matmul(current, adjacency)
        powers[power] = current
    return powers


def row_vector(matrix: tuple[tuple[int, ...], ...], surface: str) -> tuple[int, ...]:
    return matrix[INDEX[surface]]


def column_vector(matrix: tuple[tuple[int, ...], ...], surface: str) -> tuple[int, ...]:
    col = INDEX[surface]
    return tuple(row[col] for row in matrix)


def projected_row(matrix: tuple[tuple[int, ...], ...], surface: str, projection: frozenset[str]) -> tuple[int, ...]:
    return tuple(row_vector(matrix, surface)[INDEX[target]] for target in sorted(projection))


def projected_column(matrix: tuple[tuple[int, ...], ...], surface: str, projection: frozenset[str]) -> tuple[int, ...]:
    return tuple(column_vector(matrix, surface)[INDEX[target]] for target in sorted(projection))


def row_profiles(power: int) -> frozenset[tuple[int, ...]]:
    matrix = matrix_powers(MAX_POWER)[power]
    return frozenset(row_vector(matrix, surface) for surface in FOUR_PACK)


def column_profiles(power: int) -> frozenset[tuple[int, ...]]:
    matrix = matrix_powers(MAX_POWER)[power]
    return frozenset(column_vector(matrix, surface) for surface in FOUR_PACK)


def path_total_profiles() -> dict[int, frozenset[tuple[int, int, int]]]:
    profiles: dict[int, frozenset[tuple[int, int, int]]] = {}
    for power, matrix in matrix_powers(MAX_POWER).items():
        profiles[power] = frozenset(
            (
                sum(row_vector(matrix, surface)),
                sum(column_vector(matrix, surface)),
                sum(row_vector(matrix, surface)) - sum(column_vector(matrix, surface)),
            )
            for surface in FOUR_PACK
        )
    return profiles


def projection_profiles(projection: frozenset[str]) -> dict[int, frozenset[tuple[tuple[int, ...], tuple[int, ...]]]]:
    profiles: dict[int, frozenset[tuple[tuple[int, ...], tuple[int, ...]]]] = {}
    for power, matrix in matrix_powers(MAX_POWER).items():
        profiles[power] = frozenset(
            (
                projected_row(matrix, surface, projection),
                projected_column(matrix, surface, projection),
            )
            for surface in FOUR_PACK
        )
    return profiles


def dot(weights: tuple[int, ...], values: tuple[int, ...]) -> int:
    return sum(weight * value for weight, value in zip(weights, values))


def polynomial_vector(surface: str, coefficients: tuple[int, ...], *, direction: str) -> tuple[int, ...]:
    powers = matrix_powers(MAX_POWER)
    values = [0 for _ in BASIS]
    for power, coefficient in enumerate(coefficients, start=1):
        if coefficient == 0:
            continue
        vector = row_vector(powers[power], surface) if direction == "row" else column_vector(powers[power], surface)
        values = [old + coefficient * new for old, new in zip(values, vector)]
    return tuple(values)


def polynomial_readouts_constant() -> bool:
    return all(
        len(
            frozenset(
                dot(weights, polynomial_vector(surface, coefficients, direction=direction))
                for surface in FOUR_PACK
            )
        )
        == 1
        for weights in SAMPLE_WEIGHTS
        for coefficients in SAMPLE_POLYNOMIALS
        for direction in ("row", "column")
    )


def all_power_rows_and_columns_constant() -> bool:
    return all(
        len(row_profiles(power)) == 1 and len(column_profiles(power)) == 1
        for power in range(1, MAX_POWER + 1)
    )


def all_projections_constant() -> bool:
    return all(
        len(profile) == 1
        for profiles in (projection_profiles(RIGHT_TARGETS), projection_profiles(HIGH_CENTRALITY_BAD))
        for profile in profiles.values()
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    path_totals = path_total_profiles()

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
        all(outgoing(surface) == RIGHT_NEIGHBORS and incoming(surface) == RIGHT_NEIGHBORS for surface in FOUR_PACK),
        f"power_one_neighbors={neighbor_names(RIGHT_NEIGHBORS)}",
    )
    gate(
        f"{PREFIX}5",
        all_power_rows_and_columns_constant(),
        f"checked_positive_path_powers=1..{MAX_POWER}",
    )
    gate(
        f"{PREFIX}6",
        all(len(profile) == 1 for profile in path_totals.values()),
        f"path_total_profiles={path_totals}",
    )
    gate(
        f"{PREFIX}7",
        all_projections_constant(),
        "right-target and high-bad projected path-power profiles are singleton profiles",
    )
    gate(
        f"{PREFIX}8",
        polynomial_readouts_constant(),
        f"sample_positive_adjacency_polynomials={SAMPLE_POLYNOMIALS}",
    )
    gate(
        f"{PREFIX}9",
        all_power_rows_and_columns_constant()
        and all_projections_constant()
        and polynomial_readouts_constant()
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "positive-length path-power composition readouts do not split the four-pack",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack path-power composition reuse fails"
    )
    print(
        "VERDICT: iterating the current terminal-basin relation preserves the "
        "four-pack collapse. Positive-length adjacency powers and sample "
        "adjacency-polynomial readouts are constant on external_basin, "
        "oracle_basin, noncanonical_basin, and retuned_basin."
    )


if __name__ == "__main__":
    main()
