#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack right-target projection reuse.

Doc 643 shows that full four-pack incidence rows are identical. The next
operation-shaped repair grants a favorable projection: delete the high-bad
right neighbors no_basin_certificate/unbounded_basin_search and keep only the
right target nodes basin_not_absorbing/basin_not_extensional. This mimics the
best possible current-data "control death" projection on the right side.

This witness checks that the projection still does not split the four-pack.
Every four-pack surface is bidirectionally incident to both right target
nodes, and every surface is also bidirectionally incident to both high-bad
nodes before projection. Removing the high-bad nodes leaves the whole
four-pack, not external_basin/oracle_basin.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_right_target_projection_bridge_morphism_reuse_no_go
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
    HIGH_CENTRALITY_BAD,
    RIGHT_NEIGHBORS,
    RIGHT_TARGETS,
    complete_bidirectional_between,
    incoming,
    neighbor_names,
    outgoing,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    FOUR_PACK_BAD,
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKRIGHTTARGETPROJBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def projected_out(surface: str, keep: frozenset[str]) -> frozenset[str]:
    return outgoing(surface) & keep


def projected_in(surface: str, keep: frozenset[str]) -> frozenset[str]:
    return incoming(surface) & keep


def support_with_projected_neighbors(keep: frozenset[str], *, direction: str) -> frozenset[str]:
    if direction == "out":
        return frozenset(surface for surface in FOUR_PACK if projected_out(surface, keep) == keep)
    if direction == "in":
        return frozenset(surface for surface in FOUR_PACK if projected_in(surface, keep) == keep)
    if direction == "both":
        return frozenset(
            surface
            for surface in FOUR_PACK
            if projected_out(surface, keep) == keep and projected_in(surface, keep) == keep
        )
    raise ValueError(direction)


def any_right_target_subprojection_selects_targets() -> bool:
    right_targets = tuple(sorted(RIGHT_TARGETS))
    for size in range(1, len(right_targets) + 1):
        for combo in combinations(right_targets, size):
            keep = frozenset(combo)
            if support_with_projected_neighbors(keep, direction="out") == LEFT_TARGETS:
                return True
            if support_with_projected_neighbors(keep, direction="in") == LEFT_TARGETS:
                return True
            if support_with_projected_neighbors(keep, direction="both") == LEFT_TARGETS:
                return True
    return False


def projected_row_profiles(keep: frozenset[str]) -> frozenset[tuple[frozenset[str], frozenset[str]]]:
    return frozenset((projected_out(surface, keep), projected_in(surface, keep)) for surface in FOUR_PACK)


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
        RIGHT_NEIGHBORS == RIGHT_TARGETS | HIGH_CENTRALITY_BAD
        and complete_bidirectional_between(FOUR_PACK, RIGHT_TARGETS)
        and complete_bidirectional_between(FOUR_PACK, HIGH_CENTRALITY_BAD),
        f"right_targets={neighbor_names(RIGHT_TARGETS)} high_bad={neighbor_names(HIGH_CENTRALITY_BAD)}",
    )
    gate(
        f"{PREFIX}5",
        support_with_projected_neighbors(RIGHT_TARGETS, direction="out") == FOUR_PACK
        and support_with_projected_neighbors(RIGHT_TARGETS, direction="in") == FOUR_PACK
        and support_with_projected_neighbors(RIGHT_TARGETS, direction="both") == FOUR_PACK,
        "projecting to right-target neighbors keeps the whole four-pack",
    )
    gate(
        f"{PREFIX}6",
        support_with_projected_neighbors(HIGH_CENTRALITY_BAD, direction="out") == FOUR_PACK
        and support_with_projected_neighbors(HIGH_CENTRALITY_BAD, direction="in") == FOUR_PACK
        and support_with_projected_neighbors(HIGH_CENTRALITY_BAD, direction="both") == FOUR_PACK,
        "projecting to high-bad neighbors also keeps the whole four-pack",
    )
    gate(
        f"{PREFIX}7",
        projected_row_profiles(RIGHT_TARGETS)
        == frozenset({(RIGHT_TARGETS, RIGHT_TARGETS)})
        and projected_row_profiles(HIGH_CENTRALITY_BAD)
        == frozenset({(HIGH_CENTRALITY_BAD, HIGH_CENTRALITY_BAD)}),
        "right-target and high-bad projected row profiles are singleton profiles",
    )
    gate(
        f"{PREFIX}8",
        not any_right_target_subprojection_selects_targets(),
        "no right-target subprojection selects external_basin/oracle_basin",
    )
    gate(
        f"{PREFIX}9",
        support_with_projected_neighbors(RIGHT_TARGETS, direction="both") == FOUR_PACK
        and not any_right_target_subprojection_selects_targets()
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "right-target projection is still whole-four-pack incidence, not the missing separator",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack right-target projection reuse fails"
    )
    print(
        "VERDICT: even after deleting high-bad right neighbors, every four-pack "
        "surface remains bidirectionally incident to both right target nodes; "
        "the projection selects the whole four-pack, not external_basin/oracle_basin."
    )


if __name__ == "__main__":
    main()
