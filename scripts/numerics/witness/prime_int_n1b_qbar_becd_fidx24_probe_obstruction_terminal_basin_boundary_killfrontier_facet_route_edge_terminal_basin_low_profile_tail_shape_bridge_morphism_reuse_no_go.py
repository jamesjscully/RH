#!/usr/bin/env python3
r"""No-go for terminal-basin low-profile tail-shape bridge reuse.

Doc 637 leaves a smaller pressure point: external_basin and oracle_basin share
their kernel-graph profile with four bad basin labels. The next obvious
positive selector is tail shape: suffix basin, two-segment tails, or other
shape data inside that low-profile class.

This witness checks that suffix and arity do not separate the two target
left endpoints from bad labels. The only exact selector is again the
external/oracle attachment token pair.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go
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
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    BRANCH_SPAWNING_BASIN_SURFACE,
    EXTERNAL_BASIN_SURFACE,
    EXTERNAL_SURFACE,
    NONCANONICAL_BASIN_SURFACE,
    ORACLE_BASIN_SURFACE,
    PROOF_IRRELEVANT_BASIN_SURFACE,
    RETUNED_BASIN_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go import (
    LEFT_TARGETS,
    PROFILE_LOW,
    graph_profiles,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILETAILSHAPEBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
LOW_PROFILE_BAD = frozenset(
    {
        BRANCH_SPAWNING_BASIN_SURFACE,
        NONCANONICAL_BASIN_SURFACE,
        PROOF_IRRELEVANT_BASIN_SURFACE,
        RETUNED_BASIN_SURFACE,
    }
)
LOW_PROFILE_COMPONENT = frozenset(LEFT_TARGETS | LOW_PROFILE_BAD)
TWO_SEGMENT_LOW_PROFILE = frozenset(
    {
        EXTERNAL_BASIN_SURFACE,
        ORACLE_BASIN_SURFACE,
        NONCANONICAL_BASIN_SURFACE,
        RETUNED_BASIN_SURFACE,
    }
)
THREE_SEGMENT_LOW_PROFILE = frozenset(
    {BRANCH_SPAWNING_BASIN_SURFACE, PROOF_IRRELEVANT_BASIN_SURFACE}
)
ATTACHMENT_TOKENS = frozenset({"external", "oracle"})
STRUCTURAL_SHAPE_FEATURES = frozenset(
    {
        ("suffix", "basin"),
        ("tail_length", "2"),
        ("tail_length", "3"),
        ("event_kind", "plain_tail"),
        ("boundary", "escape"),
        ("segment", "basin"),
    }
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def shape_features(surface: str) -> frozenset[tuple[str, str]]:
    event = SOURCE_EVENTS[surface]
    features = {
        ("boundary", event["boundary_kind"]),
        ("event_kind", event["event_kind"]),
        ("tail_length", str(len(event["segments"]))),
    }
    if event["segments"]:
        features.add(("suffix", event["segments"][-1]))
    for segment in event["segments"]:
        if segment == "basin":
            features.add(("segment", "basin"))
    return frozenset(features)


def support_for_features(features: tuple[tuple[str, str], ...]) -> frozenset[str]:
    required = set(features)
    return frozenset(
        surface for surface in LOW_PROFILE_COMPONENT if required <= shape_features(surface)
    )


def structural_shape_selectors() -> list[tuple[tuple[str, str], ...]]:
    selectors: list[tuple[tuple[str, str], ...]] = []
    features = tuple(sorted(STRUCTURAL_SHAPE_FEATURES))
    for size in range(1, len(features) + 1):
        for combo in combinations(features, size):
            if support_for_features(combo) == LEFT_TARGETS:
                selectors.append(combo)
    return selectors


def token_support(tokens: frozenset[str]) -> frozenset[str]:
    return frozenset(
        surface for surface in LOW_PROFILE_COMPONENT if set(segments(surface)) & set(tokens)
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    profiles = graph_profiles()
    low_profile = frozenset(
        surface for surface, profile in profiles.items() if profile == PROFILE_LOW
    )
    shape_profile = Counter(tuple(sorted(shape_features(surface))) for surface in low_profile)

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
        low_profile == LOW_PROFILE_COMPONENT
        and LEFT_TARGETS <= low_profile
        and LOW_PROFILE_BAD <= low_profile
        and len(low_profile) == 6,
        "low graph profile contains two targets and four bad labels",
    )
    gate(
        f"{PREFIX}4",
        support_for_features((("suffix", "basin"),)) == LOW_PROFILE_COMPONENT
        and support_for_features((("segment", "basin"),)) == LOW_PROFILE_COMPONENT,
        "suffix/segment basin selects the whole low-profile component",
    )
    gate(
        f"{PREFIX}5",
        support_for_features((("tail_length", "2"),)) == TWO_SEGMENT_LOW_PROFILE
        and support_for_features((("tail_length", "3"),)) == THREE_SEGMENT_LOW_PROFILE,
        "tail arity leaves target endpoints mixed with noncanonical/retuned bad labels",
    )
    gate(
        f"{PREFIX}6",
        not structural_shape_selectors()
        and all(support_for_features((feature,)) != LEFT_TARGETS for feature in STRUCTURAL_SHAPE_FEATURES),
        "no structural tail-shape feature conjunction selects external_basin/oracle_basin",
    )
    gate(
        f"{PREFIX}7",
        token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "the only exact positive selector is external/oracle attachment tokens",
    )
    gate(
        f"{PREFIX}8",
        shape_profile
        == Counter(
            {
                tuple(sorted(shape_features(EXTERNAL_BASIN_SURFACE))): 4,
                tuple(sorted(shape_features(BRANCH_SPAWNING_BASIN_SURFACE))): 2,
            }
        ),
        f"shape_profile={dict(shape_profile)}",
    )
    gate(
        f"{PREFIX}9",
        low_profile == LOW_PROFILE_COMPONENT
        and not structural_shape_selectors()
        and token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS,
        "low-profile tail shape does not supply the missing positive separator",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin low-profile tail shape fails")
    print(
        "VERDICT: suffix and tail arity do not separate external_basin/oracle_basin "
        "from low-profile bad labels; only external/oracle attachment tokens do."
    )


if __name__ == "__main__":
    main()
