#!/usr/bin/env python3
r"""No-go for action-normalized role-payload morphism reuse.

Doc 616 kills exact role-payload graph reuse. The next natural normalization
is to let action roles compose with obstruction/class roles by stripping the
action verbs reject and emit from action_namespace payloads.

This creates real action/class/obstruction triples, including the
external_or_oracle triple, but every reused normalized role-payload group is
mixed-class. It also still gives no reused graph for the not_source_internal
singleton residual.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_action_normalized_role_payload_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    BOUNDARY_SURFACES,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

ACTION_VERBS = frozenset({"reject", "emit"})
EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
EXTERNAL_ACTION_SURFACE = "entry_boundary:action:reject_external_or_oracle"
EXTERNAL_CLASS_SURFACE = "entry_boundary:class:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

failures: list[str] = []


def event_role(surface: str) -> str:
    return SOURCE_EVENTS[surface]["event_kind"]


def normalized_payload(surface: str) -> tuple[str, ...]:
    segments = tuple(SOURCE_EVENTS[surface]["segments"])
    if event_role(surface) == "action_namespace" and segments and segments[0] in ACTION_VERBS:
        return segments[1:]
    return segments


def normalized_payload_groups() -> dict[tuple[str, ...], tuple[str, ...]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for surface in BOUNDARY_SURFACES:
        groups[normalized_payload(surface)].append(surface)
    return {key: tuple(sorted(value)) for key, value in groups.items()}


NORMALIZED_PAYLOAD_GROUPS = normalized_payload_groups()
MULTI_NORMALIZED_PAYLOAD_GROUPS = {
    key: value for key, value in NORMALIZED_PAYLOAD_GROUPS.items() if len(value) >= 2
}
NORMALIZED_ROLE_PROFILES = Counter(
    tuple(sorted(Counter(event_role(surface) for surface in surfaces).items()))
    for surfaces in MULTI_NORMALIZED_PAYLOAD_GROUPS.values()
)
NORMALIZED_OBSTRUCTION_NODE_CLASSES = Counter(
    CLASS_OF[surface]
    for surfaces in MULTI_NORMALIZED_PAYLOAD_GROUPS.values()
    for surface in surfaces
    if event_role(surface) == "obstruction_namespace"
)
SOURCE_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "source" in normalized_payload(surface))
)
NOT_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "not" in normalized_payload(surface))
)


def role_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(event_role(surface) for surface in surfaces)


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


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

    external_group = NORMALIZED_PAYLOAD_GROUPS[normalized_payload(EXTERNAL_SURFACE)]
    source_internal_group = NORMALIZED_PAYLOAD_GROUPS[normalized_payload(SOURCE_INTERNAL_SURFACE)]

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
        and IMPOSSIBLE_RESIDUAL_SURFACES <= MISSING_REUSED_CLASS_STATE,
        f"impossible={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}3",
        len(MULTI_NORMALIZED_PAYLOAD_GROUPS) == 7
        and NORMALIZED_ROLE_PROFILES
        == Counter(
            {
                (("class_namespace", 1), ("obstruction_namespace", 1)): 3,
                (
                    ("action_namespace", 1),
                    ("class_namespace", 1),
                    ("obstruction_namespace", 1),
                ): 3,
                (("class_namespace", 1), ("obstruction_namespace", 1), ("plain_tail", 1)): 1,
            }
        ),
        f"multi_normalized_groups={len(MULTI_NORMALIZED_PAYLOAD_GROUPS)} role_profiles={dict(NORMALIZED_ROLE_PROFILES)}",
    )
    gate(
        f"{PREFIX}4",
        all(len(class_profile(surfaces)) > 1 for surfaces in MULTI_NORMALIZED_PAYLOAD_GROUPS.values()),
        "every reused action-normalized role-payload group is mixed-class",
    )
    gate(
        f"{PREFIX}5",
        external_group == (EXTERNAL_ACTION_SURFACE, EXTERNAL_CLASS_SURFACE, EXTERNAL_SURFACE)
        and role_profile(external_group)
        == Counter({"action_namespace": 1, "class_namespace": 1, "obstruction_namespace": 1})
        and class_profile(external_group)
        == Counter({"action_semantics": 1, "classifier_partition": 1, "boundary_externality": 1}),
        f"external_group_roles={dict(role_profile(external_group))} classes={dict(class_profile(external_group))}",
    )
    gate(
        f"{PREFIX}6",
        NORMALIZED_OBSTRUCTION_NODE_CLASSES
        == Counter(
            {
                "dependency_repair_nogo": 3,
                "boundary_contextual_surrogate": 2,
                "boundary_externality": 1,
                "finite_index_budget": 1,
            }
        ),
        f"normalized_obstruction_node_classes={dict(sorted(NORMALIZED_OBSTRUCTION_NODE_CLASSES.items()))}",
    )
    gate(
        f"{PREFIX}7",
        source_internal_group == (SOURCE_INTERNAL_SURFACE,)
        and role_profile(source_internal_group) == Counter({"plain_tail": 1})
        and class_profile(source_internal_group) == Counter({"source_internality": 1}),
        "not_source_internal still has no reused action-normalized payload graph",
    )
    gate(
        f"{PREFIX}8",
        class_profile(SOURCE_SEGMENT_SURFACES)
        == Counter(
            {
                "source_constraint_invariant": 1,
                "trace_payload_route": 1,
                "source_internality": 1,
            }
        )
        and class_profile(NOT_SEGMENT_SURFACES)
        == Counter(
            {
                "terminal_basin_entry": 3,
                "finite_index_budget": 1,
                "source_internality": 1,
            }
        ),
        "source/not segment broadening remains mixed-class",
    )
    gate(
        f"{PREFIX}9",
        CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        "action-normalized role-payload reuse still needs a selector or synthetic evidence",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: action-normalized role-payload reuse fails")
    print(
        "VERDICT: stripping action verbs creates repeated role-payload triples, "
        "including external_or_oracle, but every reused normalized group is "
        "mixed-class and not_source_internal remains singleton."
    )


if __name__ == "__main__":
    main()
