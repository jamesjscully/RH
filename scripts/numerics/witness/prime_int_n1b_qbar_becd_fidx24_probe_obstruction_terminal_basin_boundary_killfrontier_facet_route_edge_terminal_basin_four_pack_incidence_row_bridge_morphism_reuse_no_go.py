#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack incidence-row bridge reuse.

Doc 642 kills doc610 signature-token reuse inside the remaining four-pack.
The next operation-shaped repair is to use the current terminal-basin kernel
incidence rows as a proxy for composition: perhaps external_basin/oracle_basin
compose differently with the right-side terminal-basin nodes than
noncanonical_basin/retuned_basin do.

This witness checks the directed kernel-pair incidence rows and columns. All
four surfaces have identical outgoing and incoming neighbors: the two right
target nodes basin_not_absorbing/basin_not_extensional and the two high-bad
nodes no_basin_certificate/unbounded_basin_search. There are no internal
four-pack edges. Thus current incidence/composition-neighborhood data cannot
split the target pair from the bad pair.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_incidence_row_bridge_morphism_reuse_no_go
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
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go import (
    FOUR_PACK,
    FOUR_PACK_BAD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    TARGET_ENDPOINTS,
    kernel_pairs,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    token_support,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go import (
    HIGH_CENTRALITY_BAD,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCIDENCEROWBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
RIGHT_TARGETS = TARGET_ENDPOINTS - LEFT_TARGETS
RIGHT_NEIGHBORS = RIGHT_TARGETS | HIGH_CENTRALITY_BAD

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def outgoing(surface: str) -> frozenset[str]:
    return frozenset(right for left, right in kernel_pairs() if left == surface)


def incoming(surface: str) -> frozenset[str]:
    return frozenset(left for left, right in kernel_pairs() if right == surface)


def internal_edges() -> frozenset[tuple[str, str]]:
    return frozenset(
        (left, right)
        for left, right in kernel_pairs()
        if left in FOUR_PACK and right in FOUR_PACK
    )


def four_pack_row_support(neighbor_subset: frozenset[str], *, direction: str) -> frozenset[str]:
    if direction == "out":
        return frozenset(surface for surface in FOUR_PACK if neighbor_subset <= outgoing(surface))
    if direction == "in":
        return frozenset(surface for surface in FOUR_PACK if neighbor_subset <= incoming(surface))
    raise ValueError(direction)


def any_neighbor_selector_selects_targets() -> bool:
    neighbors = tuple(sorted(RIGHT_NEIGHBORS))
    for size in range(1, len(neighbors) + 1):
        for combo in combinations(neighbors, size):
            required = frozenset(combo)
            if four_pack_row_support(required, direction="out") == LEFT_TARGETS:
                return True
            if four_pack_row_support(required, direction="in") == LEFT_TARGETS:
                return True
    return False


def pair_incidence_signature(left: str, right: str) -> tuple[bool, bool, int, int]:
    left_out = outgoing(left)
    right_out = outgoing(right)
    left_in = incoming(left)
    right_in = incoming(right)
    return (
        (left, right) in kernel_pairs(),
        (right, left) in kernel_pairs(),
        len(left_out & right_out),
        len(left_in & right_in),
    )


def all_pair_incidence_signatures() -> frozenset[tuple[bool, bool, int, int]]:
    return frozenset(pair_incidence_signature(left, right) for left, right in combinations(FOUR_PACK, 2))


def complete_bidirectional_between(lefts: frozenset[str], rights: frozenset[str]) -> bool:
    pairs = set(kernel_pairs())
    return all((left, right) in pairs and (right, left) in pairs for left in lefts for right in rights)


def neighbor_names(surfaces: frozenset[str]) -> tuple[str, ...]:
    return tuple(sorted(surface.rsplit("_nf_", 1)[-1] for surface in surfaces))


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    outgoing_rows = {surface: outgoing(surface) for surface in FOUR_PACK}
    incoming_rows = {surface: incoming(surface) for surface in FOUR_PACK}

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
        all(row == RIGHT_NEIGHBORS for row in outgoing_rows.values())
        and len(set(outgoing_rows.values())) == 1,
        f"outgoing={neighbor_names(next(iter(outgoing_rows.values())))}",
    )
    gate(
        f"{PREFIX}5",
        all(row == RIGHT_NEIGHBORS for row in incoming_rows.values())
        and len(set(incoming_rows.values())) == 1,
        f"incoming={neighbor_names(next(iter(incoming_rows.values())))}",
    )
    gate(
        f"{PREFIX}6",
        not internal_edges()
        and complete_bidirectional_between(FOUR_PACK, RIGHT_NEIGHBORS),
        f"internal_edges={len(internal_edges())} right_neighbors={neighbor_names(RIGHT_NEIGHBORS)}",
    )
    gate(
        f"{PREFIX}7",
        not any_neighbor_selector_selects_targets(),
        "no outgoing/incoming neighbor-subset selector inside the four-pack selects external_basin/oracle_basin",
    )
    gate(
        f"{PREFIX}8",
        all_pair_incidence_signatures() == frozenset({(False, False, 4, 4)}),
        f"pair_incidence_signatures={all_pair_incidence_signatures()}",
    )
    gate(
        f"{PREFIX}9",
        not internal_edges()
        and len(set(outgoing_rows.values())) == 1
        and len(set(incoming_rows.values())) == 1
        and not any_neighbor_selector_selects_targets(),
        "current incidence/composition rows do not split the four-pack",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack incidence-row reuse fails"
    )
    print(
        "VERDICT: every four-pack surface has the same incoming and outgoing "
        "kernel neighbors, with no internal edges; the current incidence rows "
        "cannot separate external_basin/oracle_basin from noncanonical_basin/retuned_basin."
    )


if __name__ == "__main__":
    main()
