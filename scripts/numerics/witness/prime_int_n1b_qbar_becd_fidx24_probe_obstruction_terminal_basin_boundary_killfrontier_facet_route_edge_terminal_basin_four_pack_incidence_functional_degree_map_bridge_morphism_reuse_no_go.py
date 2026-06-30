#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack incidence-functional degree-map reuse.

Doc 644 kills right-target projection of the current incidence rows. The next
operation-shaped repair is broader: perhaps an endpoint-degree, boundary, or
control-death map is a weighted functional of the existing incidence table.

This witness checks that the relevant row and column vectors are literally
identical on the four-pack. Therefore every linear readout of the current
outgoing rows, incoming columns, total incidence, signed incidence, or
right-target/high-bad projections is constant on external_basin, oracle_basin,
noncanonical_basin, and retuned_basin. Such a functional cannot split the
target pair.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_incidence_functional_degree_map_bridge_morphism_reuse_no_go
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
    projected_row_profiles,
    support_with_projected_neighbors,
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
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCFUNCDEGMAPBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
FULL_BASIS = tuple(sorted(KERNEL_COMPONENT))
RIGHT_BASIS = tuple(sorted(RIGHT_NEIGHBORS))
SAMPLE_WEIGHTS = (
    tuple(range(1, len(RIGHT_BASIS) + 1)),
    tuple((-1) ** i * (i + 2) for i in range(len(RIGHT_BASIS))),
    tuple(3 if neighbor in RIGHT_TARGETS else -5 for neighbor in RIGHT_BASIS),
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def incidence_vector(surface: str, *, direction: str, basis: tuple[str, ...]) -> tuple[int, ...]:
    if direction == "out":
        support = outgoing(surface)
        return tuple(1 if target in support else 0 for target in basis)
    if direction == "in":
        support = incoming(surface)
        return tuple(1 if target in support else 0 for target in basis)
    if direction == "total":
        return tuple(
            (1 if target in outgoing(surface) else 0)
            + (1 if target in incoming(surface) else 0)
            for target in basis
        )
    if direction == "signed":
        return tuple(
            (1 if target in outgoing(surface) else 0)
            - (1 if target in incoming(surface) else 0)
            for target in basis
        )
    raise ValueError(direction)


def vectors(direction: str, basis: tuple[str, ...]) -> frozenset[tuple[int, ...]]:
    return frozenset(incidence_vector(surface, direction=direction, basis=basis) for surface in FOUR_PACK)


def dot(weights: tuple[int, ...], values: tuple[int, ...]) -> int:
    return sum(weight * value for weight, value in zip(weights, values))


def weighted_values(weights: tuple[int, ...], *, direction: str, basis: tuple[str, ...]) -> frozenset[int]:
    return frozenset(
        dot(weights, incidence_vector(surface, direction=direction, basis=basis))
        for surface in FOUR_PACK
    )


def all_sample_weighted_values_constant() -> bool:
    return all(
        len(weighted_values(weights, direction=direction, basis=RIGHT_BASIS)) == 1
        for weights in SAMPLE_WEIGHTS
        for direction in ("out", "in", "total", "signed")
    )


def full_row_values() -> dict[str, tuple[int, ...]]:
    return {
        direction: next(iter(vectors(direction, FULL_BASIS)))
        for direction in ("out", "in", "total", "signed")
    }


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
        f"four_pack={neighbor_names(FOUR_PACK)}",
    )
    gate(
        f"{PREFIX}4",
        all(len(vectors(direction, FULL_BASIS)) == 1 for direction in ("out", "in", "total", "signed")),
        f"full_row_values={full_row_values()}",
    )
    gate(
        f"{PREFIX}5",
        vectors("out", RIGHT_BASIS) == frozenset({tuple(1 for _ in RIGHT_BASIS)})
        and vectors("in", RIGHT_BASIS) == frozenset({tuple(1 for _ in RIGHT_BASIS)})
        and vectors("total", RIGHT_BASIS) == frozenset({tuple(2 for _ in RIGHT_BASIS)})
        and vectors("signed", RIGHT_BASIS) == frozenset({tuple(0 for _ in RIGHT_BASIS)}),
        f"right_basis={neighbor_names(frozenset(RIGHT_BASIS))}",
    )
    gate(
        f"{PREFIX}6",
        projected_row_profiles(RIGHT_TARGETS)
        == frozenset({(RIGHT_TARGETS, RIGHT_TARGETS)})
        and projected_row_profiles(HIGH_CENTRALITY_BAD)
        == frozenset({(HIGH_CENTRALITY_BAD, HIGH_CENTRALITY_BAD)}),
        "right-target and high-bad projections have singleton row profiles",
    )
    gate(
        f"{PREFIX}7",
        support_with_projected_neighbors(RIGHT_TARGETS, direction="both") == FOUR_PACK
        and support_with_projected_neighbors(HIGH_CENTRALITY_BAD, direction="both") == FOUR_PACK,
        "right-target and high-bad projections both keep the whole four-pack",
    )
    gate(
        f"{PREFIX}8",
        all_sample_weighted_values_constant(),
        f"sample_weights={SAMPLE_WEIGHTS}",
    )
    gate(
        f"{PREFIX}9",
        all(len(vectors(direction, FULL_BASIS)) == 1 for direction in ("out", "in", "total", "signed"))
        and all_sample_weighted_values_constant()
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "any current-incidence linear readout is constant on the four-pack",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack incidence-functional degree map reuse fails"
    )
    print(
        "VERDICT: the four-pack has identical incidence vectors. Any weighted "
        "degree, boundary, signed, or projected linear functional of the current "
        "incidence table is constant and cannot select external_basin/oracle_basin."
    )


if __name__ == "__main__":
    main()
