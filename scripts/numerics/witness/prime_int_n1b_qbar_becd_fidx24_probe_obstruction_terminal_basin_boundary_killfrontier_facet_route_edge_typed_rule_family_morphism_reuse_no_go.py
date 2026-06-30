#!/usr/bin/env python3
r"""No-go for using typed rule families as residual morphism evidence.

Doc 609 kills promotion of doc608 exact rule ids to a fully reused grammar:
the residual rules are singleton exact tail/obstruction-tail rules. A nearby
repair is to move one level up and treat the typed classifier's rule family
itself as the reusable morphism evidence.

That fails for the doc-614 singleton residuals. The exact residual rule ids are
singleton, while their reusable families are mixed-class:

    obstruction_tail -> boundary_externality plus three other classes;
    tail             -> source_internality plus fourteen other classes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_rule_family_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_contract import (
    EXPECTED_WITNESS as DOC608_WITNESS,
    KILLTYPEDEVENTACTION,
    RULE_LITERAL_COUNT,
    SOURCE_EVENT_DECISIONS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_reuse_no_go import (
    REUSED_RULES,
    SINGLETON_RULES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDRULEFAMILYMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

EXPECTED_OBSTRUCTION_TAIL_PROFILE = Counter(
    {
        "dependency_repair_nogo": 3,
        "boundary_contextual_surrogate": 2,
        "finite_index_budget": 1,
        "boundary_externality": 1,
    }
)
EXPECTED_TAIL_PROFILE = Counter(
    {
        "terminal_basin_entry": 17,
        "boundary_contextual_surrogate": 8,
        "dependency_repair_nogo": 5,
        "fixedpoint_replay": 4,
        "finite_index_budget": 4,
        "trace_audit_check": 3,
        "confluence_normalizer": 2,
        "verifier_check": 2,
        "localizer_blame": 2,
        "boundary_shape": 2,
        "reflection_normalform": 2,
        "action_semantics": 2,
        "classifier_partition": 2,
        "trace_payload_route": 1,
        "source_constraint_invariant": 1,
        "source_internality": 1,
    }
)

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def rule_family(rule_id: str) -> str:
    return rule_id.split(":", 1)[0]


def rule_supports() -> dict[str, tuple[str, ...]]:
    by_rule: dict[str, list[str]] = defaultdict(list)
    for surface, decision in SOURCE_EVENT_DECISIONS.items():
        by_rule[decision["rule_id"]].append(surface)
    return {rule: tuple(surfaces) for rule, surfaces in by_rule.items()}


def family_supports() -> dict[str, tuple[str, ...]]:
    by_family: dict[str, list[str]] = defaultdict(list)
    for surface, decision in SOURCE_EVENT_DECISIONS.items():
        by_family[rule_family(decision["rule_id"])].append(surface)
    return {family: tuple(surfaces) for family, surfaces in by_family.items()}


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(SOURCE_EVENT_DECISIONS[surface]["winning_class"] for surface in surfaces)


def reused_class_pure_families() -> dict[str, Counter[str]]:
    return {
        family: class_profile(surfaces)
        for family, surfaces in FAMILY_SUPPORTS.items()
        if len(surfaces) >= 2 and len(class_profile(surfaces)) == 1
    }


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


RULE_SUPPORTS = rule_supports()
FAMILY_SUPPORTS = family_supports()
REUSED_CLASS_PURE_FAMILIES = reused_class_pure_families()


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    external_decision = SOURCE_EVENT_DECISIONS[EXTERNAL_SURFACE]
    source_internal_decision = SOURCE_EVENT_DECISIONS[SOURCE_INTERNAL_SURFACE]
    external_rule = external_decision["rule_id"]
    source_internal_rule = source_internal_decision["rule_id"]
    external_family = rule_family(external_rule)
    source_internal_family = rule_family(source_internal_rule)
    external_family_profile = class_profile(FAMILY_SUPPORTS[external_family])
    source_internal_family_profile = class_profile(FAMILY_SUPPORTS[source_internal_family])

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc", 0) >= 610
        and DOC608_WITNESS in data.get("witnesses", {})
        and DOC610_WITNESS in data.get("witnesses", {})
        and KILLTYPEDEVENTACTION in accepted
        and KILLCOMPEVENTSIGACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc608={DOC608_WITNESS in data.get('witnesses', {})} doc610={DOC610_WITNESS in data.get('witnesses', {})}",
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
        len(SOURCE_EVENT_DECISIONS) == 106
        and RULE_LITERAL_COUNT == 70
        and len(RULE_SUPPORTS) == 70
        and set(FAMILY_SUPPORTS) == {"event_kind", "namespace", "obstruction_tail", "tail"},
        f"decisions={len(SOURCE_EVENT_DECISIONS)} rules={len(RULE_SUPPORTS)} families={sorted(FAMILY_SUPPORTS)}",
    )
    gate(
        f"{PREFIX}4",
        len(REUSED_RULES) == 4
        and all(rule.startswith("namespace:") for rule in REUSED_RULES)
        and external_rule in SINGLETON_RULES
        and source_internal_rule in SINGLETON_RULES
        and RULE_SUPPORTS[external_rule] == (EXTERNAL_SURFACE,)
        and RULE_SUPPORTS[source_internal_rule] == (SOURCE_INTERNAL_SURFACE,),
        f"external_rule={external_rule} source_rule={source_internal_rule} reused_rules={sorted(REUSED_RULES)}",
    )
    gate(
        f"{PREFIX}5",
        external_family == "obstruction_tail"
        and len(FAMILY_SUPPORTS[external_family]) == 7
        and external_family_profile == EXPECTED_OBSTRUCTION_TAIL_PROFILE,
        f"obstruction_tail_profile={dict(sorted(external_family_profile.items()))}",
    )
    gate(
        f"{PREFIX}6",
        source_internal_family == "tail"
        and len(FAMILY_SUPPORTS[source_internal_family]) == 58
        and source_internal_family_profile == EXPECTED_TAIL_PROFILE,
        f"tail_profile={dict(sorted(source_internal_family_profile.items()))}",
    )
    gate(
        f"{PREFIX}7",
        external_family_profile["boundary_externality"] == 1
        and len(external_family_profile) == 4
        and source_internal_family_profile["source_internality"] == 1
        and len(source_internal_family_profile) == 16,
        "both residual rule families are reused but mixed-class",
    )
    gate(
        f"{PREFIX}8",
        not REUSED_CLASS_PURE_FAMILIES
        and all(
            family not in REUSED_CLASS_PURE_FAMILIES
            for family in (external_family, source_internal_family)
        ),
        f"reused_class_pure_families={REUSED_CLASS_PURE_FAMILIES}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: typed rule-family morphism reuse fails")
    print(
        "VERDICT: moving from singleton typed rule ids to their reusable rule "
        "families does not repair the doc614 residuals. The relevant families "
        "are reused, but mixed-class, so selecting boundary_externality or "
        "source_internality still requires the forbidden selector."
    )


if __name__ == "__main__":
    main()
