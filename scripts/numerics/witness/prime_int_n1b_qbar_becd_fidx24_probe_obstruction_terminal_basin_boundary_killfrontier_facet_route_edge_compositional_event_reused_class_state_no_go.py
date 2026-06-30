#!/usr/bin/env python3
r"""No-go for factoring doc610 through reused class-pure states.

Doc 611 kills reuse of whole doc-610 signatures. This witness tests the next
categorical salvage: perhaps a doc-610 signature need not be reused as a whole,
provided every decision factors through some reused class-pure intermediate
state, meaning a subset of reusable primitive features whose containment
support has size at least two and is already contained in one class.

That strengthening is not total. Eighty-five decisions admit such a reused
class state; 21 decisions do not.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    ACTION_IN_CONTRACTION_SURFACE,
    AMBIGUOUS_SIGNATURES,
    BOUNDARY_SURFACES,
    COMPOSITIONAL_SIGNATURE_DECISIONS,
    COMPOSITIONAL_SIGNATURES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    REUSABLE_PRIMITIVE_FEATURES,
    SIGNATURE_BUCKETS,
    load_map,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
REUSE_THRESHOLD = 2

failures: list[str] = []

CLASS_OF = {
    surface: COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["winning_class"]
    for surface in BOUNDARY_SURFACES
}

Feature = tuple[str, ...]
ClassState = tuple[Feature, ...]


def feature_support_surfaces() -> dict[Feature, frozenset[str]]:
    support: dict[Feature, set[str]] = defaultdict(set)
    for surface, signature in COMPOSITIONAL_SIGNATURES.items():
        for feature in signature:
            support[feature].add(surface)
    return {feature: frozenset(surfaces) for feature, surfaces in support.items()}


FEATURE_SUPPORT_SURFACES = feature_support_surfaces()
ALL_SURFACES = frozenset(BOUNDARY_SURFACES)


def class_pure(surfaces: frozenset[str]) -> bool:
    return len({CLASS_OF[surface] for surface in surfaces}) == 1


def class_state_support(features: ClassState) -> frozenset[str]:
    support = ALL_SURFACES
    for feature in features:
        support &= FEATURE_SUPPORT_SURFACES[feature]
    return support


def find_reused_class_state(surface: str) -> tuple[ClassState, frozenset[str]] | None:
    features = tuple(
        sorted(
            COMPOSITIONAL_SIGNATURES[surface],
            key=lambda feature: (len(FEATURE_SUPPORT_SURFACES[feature]), str(feature)),
        )
    )

    @lru_cache(maxsize=None)
    def search(index: int, support: frozenset[str]) -> ClassState | None:
        if len(support) >= REUSE_THRESHOLD and class_pure(support):
            return ()
        if index >= len(features) or len(support) < REUSE_THRESHOLD:
            return None

        best = search(index + 1, support)

        feature = features[index]
        next_support = support & FEATURE_SUPPORT_SURFACES[feature]
        if surface in next_support and REUSE_THRESHOLD <= len(next_support) < len(support):
            tail = search(index + 1, next_support)
            if tail is not None:
                candidate = (feature,) + tail
                if best is None or len(candidate) < len(best):
                    best = candidate

        return best

    state = search(0, ALL_SURFACES)
    if state is None:
        return None
    return state, class_state_support(state)


REUSED_CLASS_STATES = {
    surface: find_reused_class_state(surface) for surface in BOUNDARY_SURFACES
}
MISSING_REUSED_CLASS_STATE = {
    surface for surface, state in REUSED_CLASS_STATES.items() if state is None
}
PRESENT_REUSED_CLASS_STATE = {
    surface: state for surface, state in REUSED_CLASS_STATES.items() if state is not None
}
MISSING_CLASS_COUNTS = Counter(CLASS_OF[surface] for surface in MISSING_REUSED_CLASS_STATE)
PRESENT_CLASS_COUNTS = Counter(CLASS_OF[surface] for surface in PRESENT_REUSED_CLASS_STATE)
CLASS_STATE_SIZE_PROFILE = Counter(
    None if state is None else (len(state[0]), len(state[1]))
    for state in REUSED_CLASS_STATES.values()
)


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
        len(COMPOSITIONAL_SIGNATURE_DECISIONS) == 106
        and len(REUSABLE_PRIMITIVE_FEATURES) == 184
        and len(SIGNATURE_BUCKETS) == 98
        and not AMBIGUOUS_SIGNATURES,
        f"decisions={len(COMPOSITIONAL_SIGNATURE_DECISIONS)} primitives={len(REUSABLE_PRIMITIVE_FEATURES)} signatures={len(SIGNATURE_BUCKETS)}",
    )
    gate(
        f"{PREFIX}3",
        len(PRESENT_REUSED_CLASS_STATE) == 85
        and len(MISSING_REUSED_CLASS_STATE) == 21,
        f"present={len(PRESENT_REUSED_CLASS_STATE)} missing={len(MISSING_REUSED_CLASS_STATE)}",
    )
    gate(
        f"{PREFIX}4",
        CLASS_STATE_SIZE_PROFILE
        == Counter(
            {
                None: 21,
                (1, 2): 19,
                (2, 2): 16,
                (1, 8): 16,
                (1, 13): 13,
                (1, 11): 11,
                (1, 6): 6,
                (2, 11): 3,
                (2, 3): 1,
            }
        ),
        f"class_state_size_profile={dict(CLASS_STATE_SIZE_PROFILE)}",
    )
    gate(
        f"{PREFIX}5",
        MISSING_CLASS_COUNTS
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
        f"missing_classes={dict(sorted(MISSING_CLASS_COUNTS.items()))}",
    )
    gate(
        f"{PREFIX}6",
        ACTION_IN_CONTRACTION_SURFACE in MISSING_REUSED_CLASS_STATE
        and CLASS_OF[ACTION_IN_CONTRACTION_SURFACE] == "action_semantics",
        "doc607 hard repair has no reused class-pure containment state",
    )
    gate(
        f"{PREFIX}7",
        all(
            state is not None
            and len(state[1]) >= REUSE_THRESHOLD
            and class_pure(state[1])
            and surface in state[1]
            for surface, state in PRESENT_REUSED_CLASS_STATE.items()
        ),
        "positive residue states are reused, class-pure, and contain their source surface",
    )
    gate(
        f"{PREFIX}8",
        len(MISSING_REUSED_CLASS_STATE) > 0
        and len(MISSING_CLASS_COUNTS) == 9
        and len(PRESENT_CLASS_COUNTS) == 14,
        "reused class-state factorization is useful but not total",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: doc610 fails total reused-class-state factorization")
    print(
        "VERDICT: doc610 has a real positive residue of 85 reused class-pure "
        "states, but 21 decisions cannot factor through any reused class-pure "
        "containment state. The obstruction is residual class-state leakage."
    )


if __name__ == "__main__":
    main()
