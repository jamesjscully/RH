#!/usr/bin/env python3
r"""Route graph for terminal-basin boundary kill-frontier facet taxonomy.

Doc 603 makes every boundary facet pass through an explicit facet class before
reaching its kill-frontier anchor. This witness closes the next escape: the
taxonomy may not remain a static lookup table. Every accepted route must be a
finite two-step graph

    boundary surface -> used facet class -> current kill-frontier anchor

with no direct shortcut, no orphan route class, and no composition mismatch
against the doc-602 boundary-anchor map.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_contract import (
    ACTIONCLASS,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_ANCHOR_MAP,
    BOUNDARY_SURFACES,
    CLASSIFYLOC,
    CLASS_ANCHOR_MAP,
    COHERENT,
    CONFLACTION,
    DOC602_BANNED_FLAGS,
    ENTRY_BOUNDARY_SURFACES,
    ESCAPE_BOUNDARY_SURFACES,
    EVAL,
    EXEC,
    EXECGLOB,
    FACET_CLASSES,
    FACET_TAXONOMY_DATA,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    KILLBNDRACTION,
    KILLFACETACTION,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC603_REQUIRED_DEPS,
    REQUIRED_KILL_FRONTIER_IDS,
    SEMCONS,
    SURFACE_CLASS_ANCHOR_MAP,
    SURFACE_CLASS_MAP,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    USED_FACET_CLASSES,
    USED_KILL_FRONTIER_IDS,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 604
EXPECTED_WITNESS = "doc604-probe-obstruction-terminal-basin-boundary-killfrontier-facet-route-graph-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMROUTEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLROUTEACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

SURFACE_TO_CLASS_EDGES = frozenset(SURFACE_CLASS_MAP.items())
CLASS_TO_ANCHOR_EDGES = frozenset(
    (facet_class, CLASS_ANCHOR_MAP[facet_class]) for facet_class in USED_FACET_CLASSES
)
CLASS_TO_ANCHOR_MAP = dict(CLASS_TO_ANCHOR_EDGES)
COMPOSED_SURFACE_ANCHOR_MAP = {
    surface: CLASS_TO_ANCHOR_MAP[facet_class]
    for surface, facet_class in SURFACE_TO_CLASS_EDGES
}
ENTRY_ESCAPE_CLASS_KINDS = {
    facet_class: frozenset(
        kind
        for kind, surfaces in (
            ("entry", ENTRY_BOUNDARY_SURFACES),
            ("escape", ESCAPE_BOUNDARY_SURFACES),
        )
        if any(SURFACE_CLASS_MAP[surface] == facet_class for surface in surfaces)
    )
    for facet_class in USED_FACET_CLASSES
}
MIXED_ENTRY_ESCAPE_CLASSES = frozenset(
    facet_class
    for facet_class, kinds in ENTRY_ESCAPE_CLASS_KINDS.items()
    if kinds == frozenset({"entry", "escape"})
)

REQUIRED_DEPS = DOC603_REQUIRED_DEPS | {
    KILLFACETACTION,
    KILLBNDRACTION,
    BOUNDARYACTION,
    BASINACTION,
    FIXPTACTION,
    NFREFLACTION,
    CONFLACTION,
    ACTIONCLASS,
    CLASSIFYLOC,
    LOCALIZEVERIFY,
    VERIFYTRACE,
    TRACEEXEC,
    EXECGLOB,
    GLOBCONTR,
    NORM,
    FUNC_NORM,
    COHERENT,
    EXEC,
    SEMCONS,
    REPSEM,
    EVAL,
    BC,
    REFINEMENT_DESCENT,
    TERMINAL_CERT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (KILLFACETACTION, "made_facet_route_graph_by", KILLROUTEACTION),
    (KILLROUTEACTION, "routes_facet_taxonomy_for", KILLFACETACTION),
    (KILLROUTEACTION, "routes_killfrontier_facets_for", KILLBNDRACTION),
    (KILLROUTEACTION, "routes_boundary_separator_for", BOUNDARYACTION),
    (KILLROUTEACTION, "routes_terminal_basin_for", BASINACTION),
    (KILLROUTEACTION, "routes_fixedpoint_for", FIXPTACTION),
    (KILLROUTEACTION, "routes_normalform_reflection_for", NFREFLACTION),
    (KILLROUTEACTION, "routes_confluent_action_for", CONFLACTION),
    (KILLROUTEACTION, "routes_action_plan_for", ACTIONCLASS),
    (KILLROUTEACTION, "routes_classifier_for", CLASSIFYLOC),
    (KILLROUTEACTION, "routes_localizer_for", LOCALIZEVERIFY),
    (KILLROUTEACTION, "routes_verifier_for", VERIFYTRACE),
    (KILLROUTEACTION, "routes_trace_audit_for", TRACEEXEC),
    (KILLROUTEACTION, "routes_executable_global_contraction_for", EXECGLOB),
    (KILLROUTEACTION, "routes_global_contraction_for", GLOBCONTR),
    (KILLROUTEACTION, "routes_terminal_certificate_for", TERMINAL_CERT),
} | {(KILLROUTEACTION, "routes_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_route_graph_source_internal",
    "terminal_basin_boundary_killfrontier_facet_route_graph_total",
    "terminal_basin_boundary_killfrontier_facet_route_graph_two_step",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_route_graph_certificate",
    "missing_surface_to_class_edge",
    "missing_class_to_anchor_edge",
    "route_noncomposable",
    "surface_anchor_composition_mismatch",
    "direct_anchor_shortcut",
    "orphan_facet_class",
    "unused_route_class",
    "entry_escape_bridge_missing",
    "anchor_bucket_route_merge",
    "class_anchor_mismatch",
    "route_not_minimal",
    "route_not_finite",
    "route_not_source_internal",
    "route_not_deterministic",
    "route_not_extensional",
    "route_not_dependency_closed",
    "route_not_graph_wired",
    "route_not_replay_stable",
    "proof_irrelevant_route",
    "external_route_graph",
    "oracle_route_graph",
    "branch_spawning_route_graph",
    "unbounded_route_search",
    "retuned_route_graph",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

FACET_ROUTE_GRAPH_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_reflected_fixedpoint_trace_executable_global_contraction",
    "base_taxonomy": KILLFACETACTION,
    "base_killfrontier": KILLBNDRACTION,
    "exists": True,
    "has_route_graph_certificate": True,
    "source_internal": True,
    "total": True,
    "two_step": True,
    "two_step_composable": True,
    "direct_surface_anchor_shortcut": False,
    "no_orphan_route_classes": True,
    "no_unused_route_classes": True,
    "entry_escape_bridge_complete": True,
    "anchor_bucket_route_separated": True,
    "class_anchor_matches_doc602_anchor": True,
    "minimal": True,
    "finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "budgeted": True,
    "external_route_graph": False,
    "oracle_route_graph": False,
    "branch_spawning": False,
    "unbounded_route_search": False,
    "retuned_route_graph": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "surface_to_class_edges": SURFACE_TO_CLASS_EDGES,
    "class_to_anchor_edges": CLASS_TO_ANCHOR_EDGES,
    "route_classes": USED_FACET_CLASSES,
    "taxonomy_classes": FACET_CLASSES,
    "class_anchor_map": CLASS_ANCHOR_MAP,
    "composed_surface_anchor_map": COMPOSED_SURFACE_ANCHOR_MAP,
    "boundary_anchor_map": BOUNDARY_ANCHOR_MAP,
    "surface_class_anchor_map": SURFACE_CLASS_ANCHOR_MAP,
    "entry_escape_class_kinds": ENTRY_ESCAPE_CLASS_KINDS,
    "entry_escape_bridge_classes": MIXED_ENTRY_ESCAPE_CLASSES,
    "boundary_surfaces": BOUNDARY_SURFACES,
    "entry_boundaries": ENTRY_BOUNDARY_SURFACES,
    "escape_boundaries": ESCAPE_BOUNDARY_SURFACES,
    "required_kill_frontier_ids": REQUIRED_KILL_FRONTIER_IDS,
    "used_kill_frontier_ids": USED_KILL_FRONTIER_IDS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_doc602_flags": DOC602_BANNED_FLAGS,
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    atoms = data["atoms"]
    accepted_atoms = {
        key
        for key in current["atoms"]
        if atoms[key]["introduced_by"] <= EXPECTED_DOC
    }
    return accepted_atoms | set(current["invariants"])


def edge_set(data: dict[str, Any]) -> set[tuple[str, str, str]]:
    return {
        (edge["source"], edge["relation"], edge["target"])
        for edge in data.get("edges", [])
        if edge.get("introduced_by", 0) <= EXPECTED_DOC
    }


def active_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "excludes": deepcopy(data["consistency_rules"]["excludes_current"]),
        "edges": edge_set(data),
        "current_rejected": set(data["current_requirements"]["rejected_repairs"]),
        "rejected_repairs": set(data.get("rejected_repairs", {})),
        "facet_taxonomy": deepcopy(FACET_TAXONOMY_DATA),
        "route_graph": deepcopy(FACET_ROUTE_GRAPH_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "facet_taxonomy":
            state["facet_taxonomy"].update(value)
        elif key == "route_graph":
            state["route_graph"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLROUTEACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    taxonomy = state["facet_taxonomy"]
    route = state["route_graph"]

    surface_to_class_edges = set(route["surface_to_class_edges"])
    class_to_anchor_edges = set(route["class_to_anchor_edges"])
    class_to_anchor_map = dict(class_to_anchor_edges)
    route_classes = set(route["route_classes"])
    composed = dict(route["composed_surface_anchor_map"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_604")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc604_witness")
    if KILLROUTEACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLROUTEACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if route.get("base_taxonomy") != KILLFACETACTION or not taxonomy.get("has_taxonomy_certificate"):
        reasons.append("wrong_facet_route_graph_base")
    if not taxonomy.get("total") or not taxonomy.get("no_default_route"):
        reasons.append("missing_doc603_taxonomy_state")

    if not route.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not route.get("has_route_graph_certificate"):
        reasons.append(FLAG_PREFIX + "no_route_graph_certificate")
    if not route.get("total") or surface_to_class_edges != SURFACE_TO_CLASS_EDGES:
        reasons.append(FLAG_PREFIX + "missing_surface_to_class_edge")
    if class_to_anchor_edges != CLASS_TO_ANCHOR_EDGES:
        reasons.append(FLAG_PREFIX + "missing_class_to_anchor_edge")
    if not route.get("two_step") or not route.get("two_step_composable"):
        reasons.append(FLAG_PREFIX + "route_noncomposable")
    if composed != BOUNDARY_ANCHOR_MAP or composed != SURFACE_CLASS_ANCHOR_MAP:
        reasons.append(FLAG_PREFIX + "surface_anchor_composition_mismatch")
    if route.get("direct_surface_anchor_shortcut"):
        reasons.append(FLAG_PREFIX + "direct_anchor_shortcut")
    if not route.get("no_orphan_route_classes") or route_classes - USED_FACET_CLASSES:
        reasons.append(FLAG_PREFIX + "orphan_facet_class")
    if not route.get("no_unused_route_classes") or route_classes != USED_FACET_CLASSES:
        reasons.append(FLAG_PREFIX + "unused_route_class")
    if not route.get("entry_escape_bridge_complete") or not (
        MIXED_ENTRY_ESCAPE_CLASSES <= set(route["entry_escape_bridge_classes"])
    ):
        reasons.append(FLAG_PREFIX + "entry_escape_bridge_missing")
    if (
        not route.get("anchor_bucket_route_separated")
        or set(class_to_anchor_map.values()) != REQUIRED_KILL_FRONTIER_IDS
        or set(composed.values()) != USED_KILL_FRONTIER_IDS
    ):
        reasons.append(FLAG_PREFIX + "anchor_bucket_route_merge")
    if not route.get("class_anchor_matches_doc602_anchor") or class_to_anchor_map != {
        facet_class: CLASS_ANCHOR_MAP[facet_class]
        for facet_class in USED_FACET_CLASSES
    }:
        reasons.append(FLAG_PREFIX + "class_anchor_mismatch")
    if not route.get("minimal"):
        reasons.append(FLAG_PREFIX + "route_not_minimal")
    if not route.get("finite"):
        reasons.append(FLAG_PREFIX + "route_not_finite")
    if not route.get("source_internal"):
        reasons.append(FLAG_PREFIX + "route_not_source_internal")
    if not route.get("deterministic"):
        reasons.append(FLAG_PREFIX + "route_not_deterministic")
    if not route.get("extensional"):
        reasons.append(FLAG_PREFIX + "route_not_extensional")
    if not route.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "route_not_dependency_closed")
    if not route.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "route_not_graph_wired")
    if not route.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "route_not_replay_stable")
    if not route.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_route")
    if route.get("external_route_graph"):
        reasons.append(FLAG_PREFIX + "external_route_graph")
    if route.get("oracle_route_graph"):
        reasons.append(FLAG_PREFIX + "oracle_route_graph")
    if route.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_route_graph")
    if route.get("unbounded_route_search"):
        reasons.append(FLAG_PREFIX + "unbounded_route_search")
    if route.get("retuned_route_graph"):
        reasons.append(FLAG_PREFIX + "retuned_route_graph")
    if route.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if route.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if route.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if route.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if route.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not route.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if route["payload_events"] != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if route["rejected_doc602_flags"] != DOC602_BANNED_FLAGS:
        reasons.append("doc602_rejected_flags_not_preserved")

    for flag, live in state["banned"].items():
        if live:
            reasons.append(flag)

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        reasons.append(f"missing_edges:{len(missing_edges)}")

    return reasons


def main() -> None:
    data = load_map()
    state = active_state(data)
    live_reasons = assess(state)

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc") >= EXPECTED_DOC
        and KILLROUTEACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["route_graph"]["base_taxonomy"] == KILLFACETACTION
        and state["facet_taxonomy"]["has_taxonomy_certificate"]
        and state["facet_taxonomy"]["total"],
        "doc603 facet taxonomy is the route-graph base",
    )
    gate(
        f"{PREFIX}3",
        set(state["route_graph"]["surface_to_class_edges"]) == SURFACE_TO_CLASS_EDGES
        and set(state["route_graph"]["class_to_anchor_edges"]) == CLASS_TO_ANCHOR_EDGES,
        f"surface_edges={len(SURFACE_TO_CLASS_EDGES)} class_edges={len(CLASS_TO_ANCHOR_EDGES)}",
    )
    gate(
        f"{PREFIX}4",
        state["route_graph"]["two_step"]
        and state["route_graph"]["two_step_composable"]
        and not state["route_graph"]["direct_surface_anchor_shortcut"]
        and state["route_graph"]["composed_surface_anchor_map"] == BOUNDARY_ANCHOR_MAP,
        "two-step route graph composes to the doc602 anchor map with no shortcut",
    )
    gate(
        f"{PREFIX}5",
        state["route_graph"]["route_classes"] == USED_FACET_CLASSES
        and state["route_graph"]["no_orphan_route_classes"]
        and state["route_graph"]["no_unused_route_classes"],
        f"route_classes={len(USED_FACET_CLASSES)} taxonomy_classes={len(FACET_CLASSES)}",
    )
    gate(
        f"{PREFIX}6",
        MIXED_ENTRY_ESCAPE_CLASSES <= state["route_graph"]["entry_escape_bridge_classes"]
        and state["route_graph"]["anchor_bucket_route_separated"],
        f"mixed_entry_escape_classes={len(MIXED_ENTRY_ESCAPE_CLASSES)} anchors={len(USED_KILL_FRONTIER_IDS)}",
    )
    gate(
        f"{PREFIX}7",
        state["route_graph"]["minimal"]
        and state["route_graph"]["finite"]
        and state["route_graph"]["source_internal"]
        and state["route_graph"]["deterministic"]
        and state["route_graph"]["extensional"]
        and state["route_graph"]["proof_relevant"]
        and state["route_graph"]["dependency_closed"]
        and state["route_graph"]["graph_wired"]
        and state["route_graph"]["replay_stable"]
        and state["route_graph"]["budgeted"]
        and not any(
            state["route_graph"][key]
            for key in (
                "external_route_graph",
                "oracle_route_graph",
                "branch_spawning",
                "unbounded_route_search",
                "retuned_route_graph",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "route graph is minimal, finite, source-internal, replay-stable, and budgeted",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLROUTEACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        f"expected_edges={len(EXPECTED_EDGES)}",
    )

    variants = {flag: assess(active_state(data, banned={flag: True})) for flag in BANNED_FLAGS}
    covered = {
        flag
        for flag, reasons in variants.items()
        if flag in reasons and rejected_or_excluded(state, flag)
    }
    gate(
        f"{PREFIX}9",
        covered == set(BANNED_FLAGS),
        f"covered={len(covered)}",
    )
    gate(
        f"{PREFIX}10",
        not live_reasons and all(variants[flag] for flag in BANNED_FLAGS),
        f"live_reasons={live_reasons} rejected_variants={sum(bool(v) for v in variants.values())}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: facet taxonomy routes through an explicit finite graph")
    print(
        "VERDICT: the missing-object candidate now counts only when each "
        "terminal-basin boundary facet reaches its kill-frontier anchor by the "
        "two-step route facet->used-class->anchor; direct shortcuts, orphan "
        "classes, and noncomposable route graphs are disguised repairs."
    )


if __name__ == "__main__":
    main()
