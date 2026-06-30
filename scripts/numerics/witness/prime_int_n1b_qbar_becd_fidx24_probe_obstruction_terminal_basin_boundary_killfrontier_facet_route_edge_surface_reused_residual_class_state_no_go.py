#!/usr/bin/env python3
r"""No-go for any surface-reused class-state repair of the doc612 residual.

Doc 613 kills quotient closure generated from existing shared doc-610 source
features. This witness checks a broader obstruction: if a residual repair
requires each residual decision to pass through a class-pure state reused by at
least two boundary surfaces, then singleton classes make the repair impossible
independently of which new feature name is added.

Two doc-610 classes have global surface support one, and both are in the
doc-612 residual set: boundary_externality and source_internality.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    BOUNDARY_SURFACES,
    COMPOSITIONAL_SIGNATURE_DECISIONS,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    SOURCE_EVENTS,
    load_map,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSURFREUSEDRESIDCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
REUSE_THRESHOLD = 2

failures: list[str] = []

CLASS_COUNTS = Counter(COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["winning_class"] for surface in BOUNDARY_SURFACES)
SINGLETON_CLASSES = frozenset(class_name for class_name, count in CLASS_COUNTS.items() if count == 1)
SINGLETON_CLASS_COUNTS = {class_name: CLASS_COUNTS[class_name] for class_name in sorted(SINGLETON_CLASSES)}
SINGLETON_CLASS_SURFACES = {
    class_name: tuple(
        surface
        for surface in BOUNDARY_SURFACES
        if COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["winning_class"] == class_name
    )
    for class_name in SINGLETON_CLASSES
}
RESIDUAL_SINGLETON_CLASS_SURFACES = {
    class_name: surfaces
    for class_name, surfaces in SINGLETON_CLASS_SURFACES.items()
    if any(surface in MISSING_REUSED_CLASS_STATE for surface in surfaces)
}


def max_class_pure_surface_support(surface: str) -> int:
    """Maximum support of any class-pure surface state containing surface.

    This is independent of how the state is named: class purity forces the
    support to be a subset of the surface's class.
    """

    return CLASS_COUNTS[CLASS_OF[surface]]


MAX_RESIDUAL_CLASS_PURE_SUPPORT = {
    surface: max_class_pure_surface_support(surface) for surface in MISSING_REUSED_CLASS_STATE
}
IMPOSSIBLE_RESIDUAL_SURFACES = {
    surface
    for surface, support in MAX_RESIDUAL_CLASS_PURE_SUPPORT.items()
    if support < REUSE_THRESHOLD
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
        len(BOUNDARY_SURFACES) == 106
        and len(CLASS_COUNTS) == 17
        and CLASS_COUNTS["boundary_externality"] == 1
        and CLASS_COUNTS["source_internality"] == 1,
        f"classes={len(CLASS_COUNTS)} singleton_counts={SINGLETON_CLASS_COUNTS}",
    )
    gate(
        f"{PREFIX}3",
        SINGLETON_CLASSES == frozenset({"boundary_externality", "source_internality"}),
        f"singleton_classes={sorted(SINGLETON_CLASSES)}",
    )
    gate(
        f"{PREFIX}4",
        set(RESIDUAL_SINGLETON_CLASS_SURFACES) == {"boundary_externality", "source_internality"}
        and all(
            surface in MISSING_REUSED_CLASS_STATE
            for surfaces in RESIDUAL_SINGLETON_CLASS_SURFACES.values()
            for surface in surfaces
        ),
        f"residual_singleton_class_surfaces={RESIDUAL_SINGLETON_CLASS_SURFACES}",
    )
    gate(
        f"{PREFIX}5",
        IMPOSSIBLE_RESIDUAL_SURFACES
        == {
            "entry_boundary:obstruction:external_or_oracle",
            "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal",
        },
        f"impossible_residual_surfaces={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}6",
        all(MAX_RESIDUAL_CLASS_PURE_SUPPORT[surface] == 1 for surface in IMPOSSIBLE_RESIDUAL_SURFACES)
        and all(
            MAX_RESIDUAL_CLASS_PURE_SUPPORT[surface] >= REUSE_THRESHOLD
            for surface in MISSING_REUSED_CLASS_STATE - IMPOSSIBLE_RESIDUAL_SURFACES
        ),
        "only the two global singleton classes fail surface-reused class-state support in principle",
    )
    gate(
        f"{PREFIX}7",
        SOURCE_EVENTS["entry_boundary:obstruction:external_or_oracle"]["event_kind"] == "obstruction_namespace"
        and SOURCE_EVENTS[
            "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
        ]["event_kind"]
        == "plain_tail",
        "the singleton-class obstruction occurs in both obstruction-namespace and plain-tail residual forms",
    )
    gate(
        f"{PREFIX}8",
        len(IMPOSSIBLE_RESIDUAL_SURFACES) == 2
        and len(MISSING_REUSED_CLASS_STATE) == 21,
        "a total surface-reused class-state repair must add synthetic support, merge classes, change labels, or relax reuse",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: surface-reused residual class-state repair is impossible")
    print(
        "VERDICT: no new feature name can make every doc612 residual case "
        "factor through a reused class-pure surface state. The boundary_externality "
        "and source_internality classes have global surface support one."
    )


if __name__ == "__main__":
    main()
