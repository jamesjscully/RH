#!/usr/bin/env python3
r"""No-go for repairing doc614 by existing primitive-conjunction morphisms.

Doc 614 kills total surface-reused class-state repair: two residual classes
have global boundary-surface support one. The surviving categorical idea is to
drop surface-state reuse and ask for morphism-level reuse instead.

This witness tests the strongest version available from existing doc-610 data:
a morphism skeleton is any nonempty conjunction of existing reusable
source-event primitive features whose support contains the residual surface and
has size at least two. For the two singleton-class residuals, every such reused
skeleton is mixed-class. Therefore existing primitive-conjunction morphism
reuse cannot select the residual class without an extra selector, synthetic
support, class merge, or label/anchor change.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_existing_primitive_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    ALL_SURFACES,
    CLASS_OF,
    FEATURE_SUPPORT_SURFACES,
    MISSING_REUSED_CLASS_STATE,
    REUSE_THRESHOLD,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    COMPOSITIONAL_SIGNATURES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEXISTPRIMORMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

Feature = tuple[str, ...]
Schema = tuple[Feature, ...]

GENERIC_KINDS = frozenset({"boundary", "event_kind", "namespace"})
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
PROFILES = ("all_features", "non_generic", "segmental")

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

EXPECTED_EXTERNAL_NONGENERIC_SUPPORT = frozenset(
    {
        "entry_boundary:action:reject_external_or_oracle",
        "entry_boundary:class:external_or_oracle",
        "entry_boundary:obstruction:external_or_oracle",
    }
)
EXPECTED_SOURCE_NONGENERIC_SUPPORT = frozenset(
    {
        "entry_boundary:invariant:source_before_points",
        "entry_boundary:payload:trace_source_law",
        SOURCE_INTERNAL_SURFACE,
    }
)

failures: list[str] = []


def profile_features(surface: str, profile: str) -> tuple[Feature, ...]:
    features = COMPOSITIONAL_SIGNATURES[surface]
    if profile == "all_features":
        return tuple(features)
    if profile == "non_generic":
        return tuple(feature for feature in features if feature[0] not in GENERIC_KINDS)
    if profile == "segmental":
        return tuple(feature for feature in features if feature[0] in SEGMENTAL_KINDS)
    raise ValueError(profile)


def schema_support(schema: Schema) -> frozenset[str]:
    support = ALL_SURFACES
    for feature in schema:
        support &= FEATURE_SUPPORT_SURFACES[feature]
    return support


def class_profile(surfaces: frozenset[str]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def reused_schemas(surface: str, profile: str) -> tuple[tuple[Schema, frozenset[str], Counter[str]], ...]:
    features = profile_features(surface, profile)
    schemas: list[tuple[Schema, frozenset[str], Counter[str]]] = []
    for size in range(1, len(features) + 1):
        for schema in combinations(features, size):
            support = schema_support(schema)
            if len(support) >= REUSE_THRESHOLD:
                schemas.append((schema, support, class_profile(support)))
    return tuple(schemas)


def best_support_sets(surface: str, profile: str) -> frozenset[frozenset[str]]:
    schemas = reused_schemas(surface, profile)
    min_class_count = min(len(classes) for _, _, classes in schemas)
    min_support_size = min(
        len(support)
        for _, support, classes in schemas
        if len(classes) == min_class_count
    )
    return frozenset(
        support
        for _, support, classes in schemas
        if len(classes) == min_class_count and len(support) == min_support_size
    )


def summary(surface: str, profile: str) -> dict[str, Any]:
    schemas = reused_schemas(surface, profile)
    class_pure = tuple((schema, support, classes) for schema, support, classes in schemas if len(classes) == 1)
    return {
        "feature_count": len(profile_features(surface, profile)),
        "reused_schema_count": len(schemas),
        "class_pure_schema_count": len(class_pure),
        "min_support_size": min((len(support) for _, support, _ in schemas), default=None),
        "min_class_count": min((len(classes) for _, _, classes in schemas), default=None),
    }


SUMMARIES = {
    surface: {profile: summary(surface, profile) for profile in PROFILES}
    for surface in sorted(IMPOSSIBLE_RESIDUAL_SURFACES)
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
        IMPOSSIBLE_RESIDUAL_SURFACES == {EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE}
        and IMPOSSIBLE_RESIDUAL_SURFACES <= MISSING_REUSED_CLASS_STATE
        and CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        f"impossible={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}3",
        all(
            SUMMARIES[surface][profile]["reused_schema_count"] > 0
            and SUMMARIES[surface][profile]["class_pure_schema_count"] == 0
            for surface in IMPOSSIBLE_RESIDUAL_SURFACES
            for profile in PROFILES
        ),
        "every reused existing primitive-conjunction skeleton containing a singleton residual is mixed-class",
    )
    gate(
        f"{PREFIX}4",
        SUMMARIES[EXTERNAL_SURFACE]["all_features"]
        == {
            "feature_count": 16,
            "reused_schema_count": 16407,
            "class_pure_schema_count": 0,
            "min_support_size": 2,
            "min_class_count": 2,
        },
        f"external_all={SUMMARIES[EXTERNAL_SURFACE]['all_features']}",
    )
    gate(
        f"{PREFIX}5",
        SUMMARIES[EXTERNAL_SURFACE]["non_generic"]
        == {
            "feature_count": 13,
            "reused_schema_count": 8191,
            "class_pure_schema_count": 0,
            "min_support_size": 3,
            "min_class_count": 3,
        }
        and SUMMARIES[EXTERNAL_SURFACE]["segmental"] == SUMMARIES[EXTERNAL_SURFACE]["non_generic"],
        f"external_non_generic={SUMMARIES[EXTERNAL_SURFACE]['non_generic']}",
    )
    gate(
        f"{PREFIX}6",
        SUMMARIES[SOURCE_INTERNAL_SURFACE]["all_features"]
        == {
            "feature_count": 6,
            "reused_schema_count": 18,
            "class_pure_schema_count": 0,
            "min_support_size": 3,
            "min_class_count": 3,
        },
        f"source_all={SUMMARIES[SOURCE_INTERNAL_SURFACE]['all_features']}",
    )
    gate(
        f"{PREFIX}7",
        SUMMARIES[SOURCE_INTERNAL_SURFACE]["non_generic"]
        == {
            "feature_count": 4,
            "reused_schema_count": 6,
            "class_pure_schema_count": 0,
            "min_support_size": 3,
            "min_class_count": 3,
        }
        and SUMMARIES[SOURCE_INTERNAL_SURFACE]["segmental"] == SUMMARIES[SOURCE_INTERNAL_SURFACE]["non_generic"],
        f"source_non_generic={SUMMARIES[SOURCE_INTERNAL_SURFACE]['non_generic']}",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EXTERNAL_NONGENERIC_SUPPORT in best_support_sets(EXTERNAL_SURFACE, "non_generic")
        and EXPECTED_SOURCE_NONGENERIC_SUPPORT in best_support_sets(SOURCE_INTERNAL_SURFACE, "non_generic"),
        "best non-generic morphism skeletons already mix the target singleton class with other classes",
    )
    gate(
        f"{PREFIX}9",
        all(
            len(class_profile(support)) > 1
            for surface in IMPOSSIBLE_RESIDUAL_SURFACES
            for profile in PROFILES
            for _, support, _ in reused_schemas(surface, profile)
        ),
        "existing primitive morphism reuse needs an extra selector, synthetic support, class merge, or label change",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: existing primitive morphism reuse fails")
    print(
        "VERDICT: morphism-level reuse generated from existing doc610 primitive "
        "feature conjunctions cannot repair the singleton residual classes. "
        "Every reused skeleton containing either singleton residual is mixed-class."
    )


if __name__ == "__main__":
    main()
