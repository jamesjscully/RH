#!/usr/bin/env python3
r"""No-go for role-payload graph reuse repairing the doc614 singleton residuals.

Doc 615 kills morphism reuse generated from existing primitive conjunctions.
The next plausible proof-relevant reuse is a role-payload graph: repeated
payloads with typed source roles such as obstruction/class or
source/invariant/trace.

That also fails for the doc-614 singleton residuals. The external_or_oracle
residual lies in a real repeated obstruction/class payload pattern, but the
obstruction nodes in that pattern span four classes. The not_source_internal
residual has no reused exact-payload role graph; the broader source/not segment
supports are mixed-class.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_role_payload_morphism_reuse_no_go
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
EXTERNAL_CLASS_SURFACE = "entry_boundary:class:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

failures: list[str] = []


def payload(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def event_role(surface: str) -> str:
    return SOURCE_EVENTS[surface]["event_kind"]


def payload_groups() -> dict[tuple[str, ...], tuple[str, ...]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for surface in BOUNDARY_SURFACES:
        groups[payload(surface)].append(surface)
    return {key: tuple(sorted(value)) for key, value in groups.items()}


PAYLOAD_GROUPS = payload_groups()
MULTI_PAYLOAD_GROUPS = {
    key: value for key, value in PAYLOAD_GROUPS.items() if len(value) >= 2
}
OBSTRUCTION_CLASS_PAYLOADS = {
    key: value
    for key, value in MULTI_PAYLOAD_GROUPS.items()
    if {"obstruction_namespace", "class_namespace"} <= {event_role(surface) for surface in value}
}
OBSTRUCTION_NODE_CLASSES = Counter(
    CLASS_OF[surface]
    for surfaces in OBSTRUCTION_CLASS_PAYLOADS.values()
    for surface in surfaces
    if event_role(surface) == "obstruction_namespace"
)

SOURCE_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "source" in payload(surface))
)
NOT_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "not" in payload(surface))
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

    external_group = PAYLOAD_GROUPS[payload(EXTERNAL_SURFACE)]
    source_internal_group = PAYLOAD_GROUPS[payload(SOURCE_INTERNAL_SURFACE)]

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
        len(MULTI_PAYLOAD_GROUPS) == 7
        and len(OBSTRUCTION_CLASS_PAYLOADS) == 7,
        f"multi_payload_groups={len(MULTI_PAYLOAD_GROUPS)} obstruction_class_payloads={len(OBSTRUCTION_CLASS_PAYLOADS)}",
    )
    gate(
        f"{PREFIX}4",
        OBSTRUCTION_NODE_CLASSES
        == Counter(
            {
                "dependency_repair_nogo": 3,
                "boundary_contextual_surrogate": 2,
                "boundary_externality": 1,
                "finite_index_budget": 1,
            }
        ),
        f"obstruction_node_classes={dict(sorted(OBSTRUCTION_NODE_CLASSES.items()))}",
    )
    gate(
        f"{PREFIX}5",
        external_group == (EXTERNAL_CLASS_SURFACE, EXTERNAL_SURFACE)
        and role_profile(external_group)
        == Counter({"class_namespace": 1, "obstruction_namespace": 1})
        and class_profile(external_group)
        == Counter({"classifier_partition": 1, "boundary_externality": 1}),
        f"external_group_roles={dict(role_profile(external_group))} classes={dict(class_profile(external_group))}",
    )
    gate(
        f"{PREFIX}6",
        source_internal_group == (SOURCE_INTERNAL_SURFACE,)
        and role_profile(source_internal_group) == Counter({"plain_tail": 1})
        and class_profile(source_internal_group) == Counter({"source_internality": 1}),
        "not_source_internal has no reused exact-payload role graph",
    )
    gate(
        f"{PREFIX}7",
        role_profile(SOURCE_SEGMENT_SURFACES)
        == Counter({"invariant_namespace": 1, "payload_namespace": 1, "plain_tail": 1})
        and class_profile(SOURCE_SEGMENT_SURFACES)
        == Counter(
            {
                "source_constraint_invariant": 1,
                "trace_payload_route": 1,
                "source_internality": 1,
            }
        ),
        f"source_segment_roles={dict(role_profile(SOURCE_SEGMENT_SURFACES))} classes={dict(class_profile(SOURCE_SEGMENT_SURFACES))}",
    )
    gate(
        f"{PREFIX}8",
        len(NOT_SEGMENT_SURFACES) == 5
        and role_profile(NOT_SEGMENT_SURFACES)
        == Counter({"plain_tail": 4, "entry_trace_tail": 1})
        and class_profile(NOT_SEGMENT_SURFACES)
        == Counter(
            {
                "terminal_basin_entry": 3,
                "finite_index_budget": 1,
                "source_internality": 1,
            }
        ),
        f"not_segment_roles={dict(role_profile(NOT_SEGMENT_SURFACES))} classes={dict(class_profile(NOT_SEGMENT_SURFACES))}",
    )
    gate(
        f"{PREFIX}9",
        CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        "role-payload reuse either stays mixed-class or becomes exact-payload singleton selection",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: role-payload morphism reuse fails")
    print(
        "VERDICT: repeated role-payload graphs do not repair the doc614 "
        "singleton residuals. The external obstruction/class graph is reused "
        "but class-mixed, while not_source_internal has no reused exact-payload graph."
    )


if __name__ == "__main__":
    main()
