#!/usr/bin/env python3
r"""No-go for negation-normalized role-payload morphism reuse.

Doc 617 kills action-normalized role-payload reuse. The remaining singleton
residual not_source_internal naturally suggests treating not as a morphism
rather than as payload data.

This witness tests both leading-not deletion and all-not deletion on the
doc-610 payloads. Neither normalization creates reused evidence for
not_source_internal; it remains a singleton normalized payload. No reused
normalized payload group is class-pure.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_negation_normalized_role_payload_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Callable

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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNEGATIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

PayloadNormalizer = Callable[[tuple[str, ...]], tuple[str, ...]]

failures: list[str] = []


def event_role(surface: str) -> str:
    return SOURCE_EVENTS[surface]["event_kind"]


def payload(surface: str) -> tuple[str, ...]:
    return tuple(SOURCE_EVENTS[surface]["segments"])


def leading_not_deleted(segments: tuple[str, ...]) -> tuple[str, ...]:
    if segments and segments[0] == "not":
        return segments[1:]
    return segments


def all_not_deleted(segments: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(segment for segment in segments if segment != "not")


def payload_groups(normalizer: PayloadNormalizer) -> dict[tuple[str, ...], tuple[str, ...]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for surface in BOUNDARY_SURFACES:
        groups[normalizer(payload(surface))].append(surface)
    return {key: tuple(sorted(value)) for key, value in groups.items()}


LEADING_NOT_GROUPS = payload_groups(leading_not_deleted)
ALL_NOT_GROUPS = payload_groups(all_not_deleted)


def multi_groups(groups: dict[tuple[str, ...], tuple[str, ...]]) -> dict[tuple[str, ...], tuple[str, ...]]:
    return {key: value for key, value in groups.items() if len(value) >= 2}


def role_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(event_role(surface) for surface in surfaces)


def class_profile(surfaces: tuple[str, ...]) -> Counter[str]:
    return Counter(CLASS_OF[surface] for surface in surfaces)


def variant_summary(groups: dict[tuple[str, ...], tuple[str, ...]]) -> dict[str, Any]:
    multi = multi_groups(groups)
    return {
        "multi_group_count": len(multi),
        "class_pure_multi_group_count": sum(1 for surfaces in multi.values() if len(class_profile(surfaces)) == 1),
        "source_internal_key": next(key for key, surfaces in groups.items() if SOURCE_INTERNAL_SURFACE in surfaces),
        "source_internal_group": groups[next(key for key, surfaces in groups.items() if SOURCE_INTERNAL_SURFACE in surfaces)],
    }


LEADING_SUMMARY = variant_summary(LEADING_NOT_GROUPS)
ALL_SUMMARY = variant_summary(ALL_NOT_GROUPS)
SOURCE_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "source" in payload(surface))
)
NOT_SEGMENT_SURFACES = tuple(
    sorted(surface for surface in BOUNDARY_SURFACES if "not" in payload(surface))
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
        IMPOSSIBLE_RESIDUAL_SURFACES == {EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE}
        and IMPOSSIBLE_RESIDUAL_SURFACES <= MISSING_REUSED_CLASS_STATE
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        f"impossible={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}3",
        LEADING_SUMMARY
        == {
            "multi_group_count": 7,
            "class_pure_multi_group_count": 0,
            "source_internal_key": ("source", "internal"),
            "source_internal_group": (SOURCE_INTERNAL_SURFACE,),
        },
        f"leading_summary={LEADING_SUMMARY}",
    )
    gate(
        f"{PREFIX}4",
        ALL_SUMMARY
        == {
            "multi_group_count": 7,
            "class_pure_multi_group_count": 0,
            "source_internal_key": ("source", "internal"),
            "source_internal_group": (SOURCE_INTERNAL_SURFACE,),
        },
        f"all_not_summary={ALL_SUMMARY}",
    )
    gate(
        f"{PREFIX}5",
        role_profile(LEADING_SUMMARY["source_internal_group"]) == Counter({"plain_tail": 1})
        and class_profile(LEADING_SUMMARY["source_internal_group"]) == Counter({"source_internality": 1}),
        "not_source_internal remains a singleton normalized plain-tail payload",
    )
    gate(
        f"{PREFIX}6",
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
        f"{PREFIX}7",
        all(
            len(class_profile(surfaces)) > 1
            for groups in (LEADING_NOT_GROUPS, ALL_NOT_GROUPS)
            for surfaces in multi_groups(groups).values()
        ),
        "no reused negation-normalized payload group is class-pure",
    )
    gate(
        f"{PREFIX}8",
        payload(SOURCE_INTERNAL_SURFACE) == ("not", "source", "internal")
        and leading_not_deleted(payload(SOURCE_INTERNAL_SURFACE)) == ("source", "internal")
        and all_not_deleted(payload(SOURCE_INTERNAL_SURFACE)) == ("source", "internal"),
        "both tested negation normalizations agree on the singleton residual key",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: negation-normalized role-payload reuse fails")
    print(
        "VERDICT: treating not as a morphism does not repair source_internality. "
        "The not_source_internal residual remains singleton after leading-not "
        "and all-not normalization, and all reused normalized groups are mixed-class."
    )


if __name__ == "__main__":
    main()
