#!/usr/bin/env python3
r"""No-go for terminal-basin low-profile valence-filter bridge reuse.

Doc 638 kills suffix and tail-shape selection inside the low graph-profile
terminal-basin component. The next tempting repair is semantic valence:
external_basin and oracle_basin look like the non-defect basin labels, while
branch_spawning_basin, noncanonical_basin, proof_irrelevant_basin, and
retuned_basin look like defect/failure labels.

This witness checks that the valence filter works only as a lexical
complement. Inside the low-profile component, excluding defect tokens recovers
external_basin and oracle_basin, but that is equivalent in extension to using
the external/oracle attachment tokens. No structural low-profile feature
selects those targets.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_valence_filter_bridge_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
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
    EXTERNAL_SURFACE,
    SOURCE_INTERNALITY,
    SOURCE_INTERNAL_SURFACE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go import (
    ATTACHMENT_TOKENS,
    LEFT_TARGETS,
    LOW_PROFILE_BAD,
    LOW_PROFILE_COMPONENT,
    STRUCTURAL_SHAPE_FEATURES,
    support_for_features,
    token_support,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go import (
    PROFILE_LOW,
    graph_profiles,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEVALENCEFILTERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

PAIR = frozenset({EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE})
DEFECT_TOKENS = frozenset(
    {"branch", "spawning", "noncanonical", "proof", "irrelevant", "retuned"}
)
NEUTRAL_TERMINAL_TOKENS = frozenset({"basin"})
LEXICAL_SELECTOR_TOKENS = ATTACHMENT_TOKENS | DEFECT_TOKENS

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def segments(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def non_basin_tokens(surface: str) -> frozenset[str]:
    return frozenset(segment for segment in segments(surface) if segment != "basin")


def defect_support() -> frozenset[str]:
    return frozenset(
        surface
        for surface in LOW_PROFILE_COMPONENT
        if non_basin_tokens(surface) & DEFECT_TOKENS
    )


def defect_complement() -> frozenset[str]:
    return LOW_PROFILE_COMPONENT - defect_support()


def neutral_terminal_support() -> frozenset[str]:
    return frozenset(
        surface
        for surface in LOW_PROFILE_COMPONENT
        if set(segments(surface)) & set(NEUTRAL_TERMINAL_TOKENS)
    )


def non_basin_token_profile() -> Counter[frozenset[str]]:
    return Counter(non_basin_tokens(surface) for surface in LOW_PROFILE_COMPONENT)


def singleton_non_basin_tokens() -> set[str]:
    return {
        token
        for surface in LOW_PROFILE_COMPONENT
        for token in non_basin_tokens(surface)
    }


def all_exact_token_selectors_for_targets() -> list[frozenset[str]]:
    tokens = sorted(singleton_non_basin_tokens())
    selectors: list[frozenset[str]] = []
    for mask in range(1, 1 << len(tokens)):
        chosen = frozenset(token for index, token in enumerate(tokens) if mask & (1 << index))
        if token_support(chosen) == LEFT_TARGETS:
            selectors.append(chosen)
    return selectors


def structural_single_supports() -> dict[tuple[str, str], frozenset[str]]:
    return {
        feature: support_for_features((feature,)) for feature in STRUCTURAL_SHAPE_FEATURES
    }


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
    exact_selectors = all_exact_token_selectors_for_targets()

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
        and LOW_PROFILE_COMPONENT == LEFT_TARGETS | LOW_PROFILE_BAD
        and len(LOW_PROFILE_COMPONENT) == 6,
        "low graph profile contains exactly two targets and four defect-looking labels",
    )
    gate(
        f"{PREFIX}4",
        defect_support() == LOW_PROFILE_BAD
        and defect_complement() == LEFT_TARGETS,
        f"defect_support_size={len(defect_support())} complement_size={len(defect_complement())}",
    )
    gate(
        f"{PREFIX}5",
        token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS
        and all(selector & ATTACHMENT_TOKENS for selector in exact_selectors),
        f"exact_token_selectors={sorted(tuple(sorted(selector)) for selector in exact_selectors)}",
    )
    gate(
        f"{PREFIX}6",
        neutral_terminal_support() == LOW_PROFILE_COMPONENT
        and all(support != LEFT_TARGETS for support in structural_single_supports().values()),
        "neutral basin and structural shape features do not select the targets",
    )
    gate(
        f"{PREFIX}7",
        non_basin_token_profile()
        == Counter({frozenset({"branch", "spawning"}): 1, frozenset({"external"}): 1,
                    frozenset({"noncanonical"}): 1, frozenset({"oracle"}): 1,
                    frozenset({"proof", "irrelevant"}): 1, frozenset({"retuned"}): 1}),
        f"non_basin_profile={dict(non_basin_token_profile())}",
    )
    gate(
        f"{PREFIX}8",
        singleton_non_basin_tokens() == LEXICAL_SELECTOR_TOKENS
        and not (DEFECT_TOKENS & ATTACHMENT_TOKENS),
        f"tokens={sorted(singleton_non_basin_tokens())}",
    )
    gate(
        f"{PREFIX}9",
        defect_complement() == token_support(ATTACHMENT_TOKENS) == LEFT_TARGETS
        and neutral_terminal_support() == LOW_PROFILE_COMPONENT
        and all(support != LEFT_TARGETS for support in structural_single_supports().values()),
        "valence filtering recovers targets only by lexical complement or attachment-token lookup",
    )

    if failures:
        raise SystemExit(1)

    print(
        f"\n{PREFIX}1-{PREFIX}9 ALL PASS: terminal-basin low-profile valence filter fails"
    )
    print(
        "VERDICT: excluding defect vocabulary recovers external_basin/oracle_basin, "
        "but this is extensionally the same as external/oracle attachment-token "
        "selection; no low-profile structural feature supplies the separator."
    )


if __name__ == "__main__":
    main()
