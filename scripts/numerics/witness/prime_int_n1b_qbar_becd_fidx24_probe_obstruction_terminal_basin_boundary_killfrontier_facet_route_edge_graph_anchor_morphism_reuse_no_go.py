#!/usr/bin/env python3
r"""No-go for graph-anchor morphism reuse repairing the doc614 singletons.

Docs 617-618 kill action and negation normalizations inside the source-event
payload algebra. The next source of proof-relevant evidence is the existing
doc-605 route graph: surface-to-class edge witnesses and class-to-anchor edge
witnesses.

That graph layer does not repair the doc-614 singleton residuals. The only
class-anchor witnesses with support one are exactly boundary_externality and
source_internality, and both are doc-612 residual singleton classes. Their
surface-edge tokens, external and not_source_internal, are singleton tokens too.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_graph_anchor_morphism_reuse_no_go
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
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_contract import (
    CLASS_ANCHOR_EDGE_WITNESSES,
    SURFACE_EDGE_WITNESSES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMGRAPHANCHORMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)

failures: list[str] = []


def token_supports() -> dict[str, tuple[str, ...]]:
    supports: dict[str, list[str]] = defaultdict(list)
    for surface, witness in SURFACE_EDGE_WITNESSES.items():
        token = witness["matched_token"]
        if token:
            supports[token].append(surface)
    return {token: tuple(sorted(surfaces)) for token, surfaces in supports.items()}


TOKEN_SUPPORTS = token_supports()
SINGLETON_CLASS_ANCHOR_CLASSES = frozenset(
    facet_class
    for facet_class, witness in CLASS_ANCHOR_EDGE_WITNESSES.items()
    if len(witness["support_surfaces"]) == 1
)
SINGLETON_CLASS_ANCHOR_SURFACES = {
    facet_class: tuple(sorted(witness["support_surfaces"]))
    for facet_class, witness in CLASS_ANCHOR_EDGE_WITNESSES.items()
    if len(witness["support_surfaces"]) == 1
}
CLASS_ANCHOR_SUPPORT_PROFILE = Counter(
    len(witness["support_surfaces"]) for witness in CLASS_ANCHOR_EDGE_WITNESSES.values()
)


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    external_witness = SURFACE_EDGE_WITNESSES[EXTERNAL_SURFACE]
    source_internal_witness = SURFACE_EDGE_WITNESSES[SOURCE_INTERNAL_SURFACE]
    external_anchor = CLASS_ANCHOR_EDGE_WITNESSES["boundary_externality"]
    source_internal_anchor = CLASS_ANCHOR_EDGE_WITNESSES["source_internality"]

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
        SINGLETON_CLASS_ANCHOR_CLASSES == frozenset({"boundary_externality", "source_internality"})
        and SINGLETON_CLASS_ANCHOR_SURFACES
        == {
            "boundary_externality": (EXTERNAL_SURFACE,),
            "source_internality": (SOURCE_INTERNAL_SURFACE,),
        },
        f"singleton_class_anchor_surfaces={SINGLETON_CLASS_ANCHOR_SURFACES}",
    )
    gate(
        f"{PREFIX}4",
        CLASS_ANCHOR_SUPPORT_PROFILE
        == Counter({2: 5, 1: 2, 3: 1, 4: 1, 5: 1, 8: 1, 10: 2, 11: 1, 12: 1, 14: 1, 17: 1}),
        f"class_anchor_support_profile={dict(sorted(CLASS_ANCHOR_SUPPORT_PROFILE.items()))}",
    )
    gate(
        f"{PREFIX}5",
        external_witness["matched_token"] == "external"
        and source_internal_witness["matched_token"] == "not_source_internal"
        and TOKEN_SUPPORTS["external"] == (EXTERNAL_SURFACE,)
        and TOKEN_SUPPORTS["not_source_internal"] == (SOURCE_INTERNAL_SURFACE,),
        "singleton residual graph tokens are singleton supports too",
    )
    gate(
        f"{PREFIX}6",
        external_anchor["support_tokens"] == frozenset({"external"})
        and source_internal_anchor["support_tokens"] == frozenset({"not_source_internal"})
        and external_anchor["anchor"] == "obstruction_terminal_basin_boundary_failure"
        and source_internal_anchor["anchor"] == "represented_limit_source_constraint_bundle_failure",
        "class-anchor witnesses route the singleton classes through singleton local tokens",
    )
    gate(
        f"{PREFIX}7",
        CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality"
        and external_witness["facet_class"] == CLASS_OF[EXTERNAL_SURFACE]
        and source_internal_witness["facet_class"] == CLASS_OF[SOURCE_INTERNAL_SURFACE],
        "surface-edge witnesses agree with the doc610 singleton classes",
    )
    gate(
        f"{PREFIX}8",
        not external_witness["uses_surface_name_only"]
        and not external_witness["uses_global_lookup_only"]
        and not source_internal_witness["uses_surface_name_only"]
        and not source_internal_witness["uses_global_lookup_only"]
        and len(external_anchor["support_surfaces"]) == 1
        and len(source_internal_anchor["support_surfaces"]) == 1,
        "the graph witnesses are local, but their reusable support is still singleton",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: graph-anchor morphism reuse fails")
    print(
        "VERDICT: the doc605 route graph does not repair the doc614 singletons. "
        "The only singleton class-anchor supports are boundary_externality and "
        "source_internality, and their local graph tokens are singleton supports."
    )


if __name__ == "__main__":
    main()
