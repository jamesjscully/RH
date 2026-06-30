#!/usr/bin/env python3
r"""No-go for terminal-basin failure-complement bridge morphism reuse.

Doc 635 shows that quotienting by the escape/plain_tail/basin kernel is too
coarse. The next escape is to remove the explicitly bad basin labels from the
kernel component, leaving the four target endpoints.

This witness checks that the complement does select the target endpoints, but
only as a negative-label filter. The four targets share no positive doc610
compositional feature beyond the same escape/plain_tail/basin kernel shared by
the six excluded surfaces. The only positive exact selector is the disjunction
of branch tokens external/oracle/not, which is exactly the residual attachment
data rather than an internal composition law.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_failure_complement_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    COMPOSITIONAL_SIGNATURES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BAD_BASIN_SURFACES,
    BOUNDARY_EXTERNALITY,
    COMPOSITION_KERNEL,
    EXTERNAL_BASIN_SURFACE,
    EXTERNAL_SURFACE,
    KERNEL_COMPONENT,
    ORACLE_BASIN_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
    TARGET_ENDPOINTS,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFAILCOMPLEMENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
FAILURE_TOKENS = frozenset(
    {
        "branch",
        "spawning",
        "no",
        "certificate",
        "noncanonical",
        "proof",
        "irrelevant",
        "retuned",
        "unbounded",
        "search",
    }
)
BRANCH_ATTACHMENT_TOKENS = frozenset({"external", "oracle", "not"})
STRUCTURAL_FEATURES = frozenset(
    {
        ("boundary", "escape"),
        ("event_kind", "plain_tail"),
        ("segment", "basin"),
        ("stem", "basin"),
        ("suffix", "basin"),
    }
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> set[str]:
    return set(SOURCE_EVENTS[surface]["segments"])


def signatures(surface: str) -> set[tuple[str, ...]]:
    return set(COMPOSITIONAL_SIGNATURES[surface])


def common_signature(surfaces: frozenset[str]) -> tuple[tuple[str, ...], ...]:
    return tuple(sorted(set.intersection(*(signatures(surface) for surface in surfaces))))


def surfaces_with_any_token(tokens: frozenset[str]) -> frozenset[str]:
    return frozenset(
        surface for surface in KERNEL_COMPONENT if segments(surface) & set(tokens)
    )


def feature_support(features: tuple[tuple[str, ...], ...]) -> frozenset[str]:
    feature_set = set(features)
    return frozenset(
        surface for surface in KERNEL_COMPONENT if feature_set <= signatures(surface)
    )


def structural_feature_selectors() -> list[tuple[tuple[str, ...], ...]]:
    selectors: list[tuple[tuple[str, ...], ...]] = []
    structural = tuple(sorted(STRUCTURAL_FEATURES))
    for size in range(1, len(structural) + 1):
        for combo in combinations(structural, size):
            if feature_support(combo) == TARGET_ENDPOINTS:
                selectors.append(combo)
    return selectors


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    failure_complement = frozenset(
        surface for surface in KERNEL_COMPONENT if not (segments(surface) & FAILURE_TOKENS)
    )
    branch_selector = surfaces_with_any_token(BRANCH_ATTACHMENT_TOKENS)
    common_target = common_signature(TARGET_ENDPOINTS)
    common_bad = common_signature(BAD_BASIN_SURFACES)
    common_all = common_signature(KERNEL_COMPONENT)
    structural_selectors = structural_feature_selectors()

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
        len(KERNEL_COMPONENT) == 10
        and len(TARGET_ENDPOINTS) == 4
        and len(BAD_BASIN_SURFACES) == 6
        and TARGET_ENDPOINTS | BAD_BASIN_SURFACES == KERNEL_COMPONENT,
        "kernel component splits into four target endpoints and six bad basin labels",
    )
    gate(
        f"{PREFIX}4",
        failure_complement == TARGET_ENDPOINTS,
        f"failure_complement_size={len(failure_complement)}",
    )
    gate(
        f"{PREFIX}5",
        common_target == COMPOSITION_KERNEL
        and common_bad == COMPOSITION_KERNEL
        and common_all == COMPOSITION_KERNEL,
        f"common_target={common_target}",
    )
    gate(
        f"{PREFIX}6",
        not structural_selectors
        and all(feature_support((feature,)) != TARGET_ENDPOINTS for feature in STRUCTURAL_FEATURES),
        "no conjunction of structural kernel features selects the target endpoints",
    )
    gate(
        f"{PREFIX}7",
        branch_selector == TARGET_ENDPOINTS
        and surfaces_with_any_token(frozenset({"external", "oracle"}))
        == frozenset({EXTERNAL_BASIN_SURFACE, ORACLE_BASIN_SURFACE})
        and len(surfaces_with_any_token(frozenset({"not"}))) == 2,
        "positive exact selection uses only residual attachment tokens external/oracle/not",
    )
    gate(
        f"{PREFIX}8",
        all(segments(surface) & FAILURE_TOKENS for surface in BAD_BASIN_SURFACES)
        and not any(segments(surface) & FAILURE_TOKENS for surface in TARGET_ENDPOINTS),
        "the complement is defined by explicit failure vocabulary",
    )
    gate(
        f"{PREFIX}9",
        failure_complement == TARGET_ENDPOINTS
        and common_target == common_all
        and not structural_selectors
        and branch_selector == TARGET_ENDPOINTS,
        "failure complement is a negative-label selector, not a constructed terminal-basin morphism",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin failure complement reuse fails")
    print(
        "VERDICT: removing explicit failure labels recovers the target endpoints, "
        "but the targets share only the same kernel as the bad surfaces; positive "
        "selection reuses external/oracle/not attachment tokens."
    )


if __name__ == "__main__":
    main()
