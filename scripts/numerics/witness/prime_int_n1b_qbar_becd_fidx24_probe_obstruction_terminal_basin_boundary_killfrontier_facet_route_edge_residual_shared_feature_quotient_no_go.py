#!/usr/bin/env python3
r"""No-go for repairing doc612 by shared-feature quotient closure.

Doc 612 leaves 21 residual decisions without a reused class-pure containment
state. This witness tests the next obvious categorical repair: generate a
quotient relation on those 21 residual events by shared doc-610 source
features, then use connected components as the residual class states.

That fails. Including generic features collapses all residual classes into one
component; removing generic features still leaves a mixed 12-event component
and singleton fragments.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_residual_shared_feature_quotient_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    COMPOSITIONAL_SIGNATURES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMRESIDSHAREDFEATQUOTNOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

failures: list[str] = []

RESIDUAL_SURFACES = tuple(sorted(MISSING_REUSED_CLASS_STATE))

PROFILE_EXCLUDED_KINDS = {
    "all_features": frozenset(),
    "no_boundary": frozenset({"boundary"}),
    "no_boundary_event": frozenset({"boundary", "event_kind"}),
    "no_boundary_event_namespace": frozenset({"boundary", "event_kind", "namespace"}),
}

SEGMENTAL_KINDS = frozenset(
    {
        "segment",
        "stem",
        "bigram",
        "stem_bigram",
        "trigram",
        "stem_trigram",
        "suffix",
    }
)


def residual_shared_features(left: str, right: str, profile: str) -> frozenset[tuple[str, ...]]:
    shared = set(COMPOSITIONAL_SIGNATURES[left]) & set(COMPOSITIONAL_SIGNATURES[right])
    if profile == "only_segments_bigrams":
        return frozenset(feature for feature in shared if feature[0] in SEGMENTAL_KINDS)
    excluded = PROFILE_EXCLUDED_KINDS[profile]
    return frozenset(feature for feature in shared if feature[0] not in excluded)


def residual_components(profile: str) -> tuple[tuple[str, ...], ...]:
    adjacency = {surface: set() for surface in RESIDUAL_SURFACES}
    for i, left in enumerate(RESIDUAL_SURFACES):
        for right in RESIDUAL_SURFACES[i + 1 :]:
            if residual_shared_features(left, right, profile):
                adjacency[left].add(right)
                adjacency[right].add(left)

    seen: set[str] = set()
    components: list[tuple[str, ...]] = []
    for surface in RESIDUAL_SURFACES:
        if surface in seen:
            continue
        stack = [surface]
        seen.add(surface)
        component: list[str] = []
        while stack:
            current = stack.pop()
            component.append(current)
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components, key=lambda comp: (-len(comp), comp[0])))


def class_profile(component: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in component)


def component_summary(profile: str) -> dict[str, Any]:
    components = residual_components(profile)
    mixed = tuple(component for component in components if len(class_profile(component)) > 1)
    singleton = tuple(component for component in components if len(component) == 1)
    return {
        "components": components,
        "component_count": len(components),
        "sizes": tuple(sorted((len(component) for component in components), reverse=True)),
        "mixed_count": len(mixed),
        "largest_mixed_size": max((len(component) for component in mixed), default=0),
        "largest_mixed_class_count": max((len(class_profile(component)) for component in mixed), default=0),
        "singleton_count": len(singleton),
        "all_class_pure": not mixed,
        "all_reused": not singleton,
    }


PROFILE_SUMMARIES = {
    profile: component_summary(profile)
    for profile in (
        "all_features",
        "no_boundary",
        "no_boundary_event",
        "no_boundary_event_namespace",
        "only_segments_bigrams",
    )
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


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
        len(RESIDUAL_SURFACES) == 21
        and Counter(CLASS_OF[surface] for surface in RESIDUAL_SURFACES)
        == Counter(
            {
                "dependency_repair_nogo": 4,
                "terminal_basin_entry": 4,
                "boundary_contextual_surrogate": 4,
                "finite_index_budget": 3,
                "boundary_shape": 2,
                "source_constraint_invariant": 1,
                "source_internality": 1,
                "boundary_externality": 1,
                "action_semantics": 1,
            }
        ),
        f"residual={len(RESIDUAL_SURFACES)} classes={len(set(CLASS_OF[s] for s in RESIDUAL_SURFACES))}",
    )
    gate(
        f"{PREFIX}3",
        PROFILE_SUMMARIES["all_features"]["component_count"] == 1
        and PROFILE_SUMMARIES["all_features"]["largest_mixed_class_count"] == 9,
        f"all_features={PROFILE_SUMMARIES['all_features']}",
    )
    gate(
        f"{PREFIX}4",
        PROFILE_SUMMARIES["no_boundary"]["component_count"] == 1
        and PROFILE_SUMMARIES["no_boundary"]["largest_mixed_class_count"] == 9,
        f"no_boundary={PROFILE_SUMMARIES['no_boundary']}",
    )
    gate(
        f"{PREFIX}5",
        PROFILE_SUMMARIES["no_boundary_event"]["component_count"] == 4
        and PROFILE_SUMMARIES["no_boundary_event"]["sizes"] == (18, 1, 1, 1)
        and PROFILE_SUMMARIES["no_boundary_event"]["largest_mixed_class_count"] == 9,
        f"no_boundary_event={PROFILE_SUMMARIES['no_boundary_event']}",
    )
    gate(
        f"{PREFIX}6",
        PROFILE_SUMMARIES["no_boundary_event_namespace"]["component_count"] == 9
        and PROFILE_SUMMARIES["no_boundary_event_namespace"]["sizes"] == (12, 2, 1, 1, 1, 1, 1, 1, 1)
        and PROFILE_SUMMARIES["no_boundary_event_namespace"]["largest_mixed_class_count"] == 7,
        f"no_boundary_event_namespace={PROFILE_SUMMARIES['no_boundary_event_namespace']}",
    )
    gate(
        f"{PREFIX}7",
        PROFILE_SUMMARIES["only_segments_bigrams"]["component_count"] == 9
        and PROFILE_SUMMARIES["only_segments_bigrams"]["sizes"] == (12, 2, 1, 1, 1, 1, 1, 1, 1)
        and PROFILE_SUMMARIES["only_segments_bigrams"]["largest_mixed_class_count"] == 7,
        f"only_segments_bigrams={PROFILE_SUMMARIES['only_segments_bigrams']}",
    )
    gate(
        f"{PREFIX}8",
        all(
            not summary["all_class_pure"] or not summary["all_reused"]
            for summary in PROFILE_SUMMARIES.values()
        )
        and all(summary["mixed_count"] > 0 for summary in PROFILE_SUMMARIES.values()),
        "every tested source-shared quotient either collapses classes or leaves singleton fragments",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: residual shared-feature quotient repair fails")
    print(
        "VERDICT: doc612 residual cases cannot be repaired by quotient closure "
        "generated from existing shared doc610 source features. Such quotients "
        "collapse classes, and after generic features are removed they still "
        "leave mixed components plus singleton fragments."
    )


if __name__ == "__main__":
    main()
