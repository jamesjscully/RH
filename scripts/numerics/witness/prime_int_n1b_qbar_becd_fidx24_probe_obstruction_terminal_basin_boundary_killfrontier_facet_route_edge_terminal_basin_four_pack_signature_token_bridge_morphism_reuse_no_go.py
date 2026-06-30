#!/usr/bin/env python3
r"""No-go for terminal-basin four-pack signature-token bridge reuse.

Doc 641 reduces the current nonlexical terminal-basin data to the four-pack
external_basin/oracle_basin/noncanonical_basin/retuned_basin. The next repair
is to use the accepted doc610 compositional signatures themselves: external
and oracle appear as reusable primitive signature features.

This witness checks that the split is only attachment-token selection. After
removing external/oracle attachment-token features from the doc610 signatures,
all four surfaces have the same structural signature skeleton. No conjunction
of non-attachment signature features selects external_basin/oracle_basin.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

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
    PRIMITIVE_SUPPORT,
    SOURCE_EVENTS,
    load_map,
    primitive_features,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go import (
    BOUNDARY_EXTERNALITY,
    EXTERNAL_SURFACE,
    NONCANONICAL_BASIN_SURFACE,
    RETUNED_BASIN_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    TWO_SEGMENT_LOW_PROFILE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_profile_tail_product_bridge_morphism_reuse_no_go import (
    block_containing,
    product_blocks,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGTOKENBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
FOUR_PACK = TWO_SEGMENT_LOW_PROFILE
FOUR_PACK_BAD = frozenset({NONCANONICAL_BASIN_SURFACE, RETUNED_BASIN_SURFACE})
ATTACHMENT_SIGNATURE_FEATURES = frozenset(
    {
        ("segment", "external"),
        ("stem", "external"),
        ("segment", "oracle"),
        ("stem", "oracle"),
    }
)
ABSENT_BAD_TOKEN_FEATURES = frozenset(
    {
        ("segment", "noncanonical"),
        ("stem", "noncanonical"),
        ("segment", "retuned"),
        ("stem", "retuned"),
    }
)
COMMON_STRUCTURAL_SIGNATURE = (
    ("boundary", "escape"),
    ("event_kind", "plain_tail"),
    ("segment", "basin"),
    ("stem", "basin"),
    ("suffix", "basin"),
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def normalized_signature(surface: str) -> tuple[tuple[str, ...], ...]:
    return tuple(
        feature
        for feature in COMPOSITIONAL_SIGNATURES[surface]
        if feature not in ATTACHMENT_SIGNATURE_FEATURES
    )


def non_attachment_signature_features() -> tuple[tuple[str, ...], ...]:
    return tuple(
        sorted(
            {
                feature
                for surface in FOUR_PACK
                for feature in COMPOSITIONAL_SIGNATURES[surface]
                if feature not in ATTACHMENT_SIGNATURE_FEATURES
            }
        )
    )


def support_for_conjunction(features: tuple[tuple[str, ...], ...]) -> frozenset[str]:
    required = set(features)
    return frozenset(
        surface for surface in FOUR_PACK if required <= set(COMPOSITIONAL_SIGNATURES[surface])
    )


def non_attachment_conjunction_selectors() -> list[tuple[tuple[str, ...], ...]]:
    selectors: list[tuple[tuple[str, ...], ...]] = []
    features = non_attachment_signature_features()
    for size in range(1, len(features) + 1):
        for combo in combinations(features, size):
            if support_for_conjunction(combo) == LEFT_TARGETS:
                selectors.append(combo)
    return selectors


def attachment_feature_support() -> frozenset[str]:
    return frozenset(
        surface
        for surface in FOUR_PACK
        if set(COMPOSITIONAL_SIGNATURES[surface]) & ATTACHMENT_SIGNATURE_FEATURES
    )


def primitive_token_support(token: str) -> frozenset[str]:
    return frozenset(
        surface
        for surface in FOUR_PACK
        if token in SOURCE_EVENTS[surface]["segments"]
    )


def no_nonbasin_primitive_features(surface: str) -> frozenset[tuple[str, ...]]:
    nonbasin = set(SOURCE_EVENTS[surface]["segments"]) - {"basin"}
    return frozenset(
        feature
        for feature in primitive_features(SOURCE_EVENTS[surface])
        if not any(part in nonbasin for part in feature[1:])
    )


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    normalized = {surface: normalized_signature(surface) for surface in FOUR_PACK}
    no_nonbasin = {
        surface: no_nonbasin_primitive_features(surface) for surface in FOUR_PACK
    }

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
        block_containing(LEFT_TARGETS) == FOUR_PACK
        and FOUR_PACK == LEFT_TARGETS | FOUR_PACK_BAD
        and FOUR_PACK in product_blocks(),
        f"four_pack={sorted(surface.rsplit('_nf_', 1)[-1] for surface in FOUR_PACK)}",
    )
    gate(
        f"{PREFIX}4",
        attachment_feature_support() == LEFT_TARGETS
        and all(
            COMPOSITIONAL_SIGNATURES[surface]
            == tuple(sorted(COMMON_STRUCTURAL_SIGNATURE + tuple(feature for feature in ATTACHMENT_SIGNATURE_FEATURES if feature[1] in SOURCE_EVENTS[surface]["segments"])))
            for surface in LEFT_TARGETS
        ),
        "doc610 signatures split the targets only by external/oracle signature features",
    )
    gate(
        f"{PREFIX}5",
        all(sig == COMMON_STRUCTURAL_SIGNATURE for sig in normalized.values())
        and len(set(normalized.values())) == 1,
        f"normalized_signature={next(iter(set(normalized.values())))}",
    )
    gate(
        f"{PREFIX}6",
        not non_attachment_conjunction_selectors()
        and all(
            support_for_conjunction((feature,)) != LEFT_TARGETS
            for feature in non_attachment_signature_features()
        ),
        "no conjunction of non-attachment signature features selects external_basin/oracle_basin",
    )
    gate(
        f"{PREFIX}7",
        PRIMITIVE_SUPPORT[("segment", "external")] == 4
        and PRIMITIVE_SUPPORT[("segment", "oracle")] == 4
        and all(PRIMITIVE_SUPPORT[feature] == 1 for feature in ABSENT_BAD_TOKEN_FEATURES),
        "external/oracle are globally reused token features while noncanonical/retuned are singleton tokens",
    )
    gate(
        f"{PREFIX}8",
        primitive_token_support("external") | primitive_token_support("oracle") == LEFT_TARGETS
        and primitive_token_support("noncanonical") | primitive_token_support("retuned") == FOUR_PACK_BAD
        and all(features == frozenset(COMMON_STRUCTURAL_SIGNATURE) for features in no_nonbasin.values()),
        "removing non-basin token primitives collapses the whole four-pack",
    )
    gate(
        f"{PREFIX}9",
        attachment_feature_support() == LEFT_TARGETS
        and len(set(normalized.values())) == 1
        and not non_attachment_conjunction_selectors(),
        "four-pack doc610 signature separation is attachment-token selection, not new structure",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin four-pack signature-token reuse fails"
    )
    print(
        "VERDICT: doc610 signatures distinguish external_basin/oracle_basin "
        "inside the four-pack only by external/oracle attachment-token features; "
        "after those are removed, all four surfaces share the same structural skeleton."
    )


if __name__ == "__main__":
    main()
