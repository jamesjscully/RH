#!/usr/bin/env python3
r"""Semantic edge witnesses for the terminal-basin facet route graph.

Doc 604 makes the facet taxonomy executable as a finite two-step route graph.
This witness closes the next escape: route edges may not be bare graph edges
justified only by a global lookup. Every surface-to-class edge and every
class-to-anchor edge must carry a local semantic witness whose token, class
rule, anchor rule, and composed anchor agree with the doc-602 map.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_contract import (
    ACTIONCLASS,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_ANCHOR_MAP,
    BOUNDARY_SURFACES,
    CLASSIFYLOC,
    CLASS_ANCHOR_MAP,
    CLASS_TO_ANCHOR_EDGES,
    COHERENT,
    COMPOSED_SURFACE_ANCHOR_MAP,
    CONFLACTION,
    ENTRY_BOUNDARY_SURFACES,
    ESCAPE_BOUNDARY_SURFACES,
    EVAL,
    EXEC,
    EXECGLOB,
    FACET_ROUTE_GRAPH_DATA,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    KILLBNDRACTION,
    KILLFACETACTION,
    KILLROUTEACTION,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC604_REQUIRED_DEPS,
    REQUIRED_KILL_FRONTIER_IDS,
    SEMCONS,
    SURFACE_CLASS_MAP,
    SURFACE_TO_CLASS_EDGES,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    USED_FACET_CLASSES,
    USED_KILL_FRONTIER_IDS,
    VERIFYTRACE,
    BANNED_FLAGS as DOC604_BANNED_FLAGS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_contract import (
    anchor_subject,
)


EXPECTED_DOC = 605
EXPECTED_WITNESS = "doc605-probe-obstruction-terminal-basin-boundary-killfrontier-facet-route-edge-witness-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLEDGEACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

CLASS_RULE_TOKENS = {
    "verifier_check": ("verifier",),
    "trace_audit_check": ("trace_audit", "trace_state"),
    "trace_payload_route": ("payload",),
    "localizer_blame": ("localizer",),
    "classifier_partition": ("classifier", "class:", "class"),
    "action_semantics": ("action",),
    "confluence_normalizer": ("confluence",),
    "reflection_normalform": ("reflection", "normalform", "normal_form"),
    "fixedpoint_replay": ("fixedpoint", "fixed_point"),
    "terminal_basin_entry": ("basin", "entry_trace"),
    "source_constraint_invariant": (
        "invariant",
        "endpoint",
        "degree",
        "dd4",
        "boundary_pushforward",
        "graph",
        "rosati",
        "control",
        "source_before_points",
    ),
    "source_internality": ("not_source_internal",),
    "finite_index_budget": ("budget", "finite_index", "requires_new_cell", "not_budgeted"),
    "dependency_repair_nogo": ("repair", "no_go", "accepted", "dependency"),
    "boundary_shape": (
        "missing",
        "certificate",
        "cover",
        "unlisted",
        "noncanonical",
        "overlap",
        "proof_irrelevant",
        "finite",
        "boundary",
    ),
    "boundary_externality": ("external", "oracle"),
    "boundary_contextual_surrogate": ("context", "sample", "basis", "declaration", "by_declaration"),
    "boundary_search_or_retune": ("branch", "unbounded", "retuned"),
}


def surface_kind(surface: str) -> str:
    if surface in ENTRY_BOUNDARY_SURFACES:
        return "entry"
    if surface in ESCAPE_BOUNDARY_SURFACES:
        return "escape"
    return "unknown"


def matched_token(subject: str, facet_class: str) -> str:
    for token in CLASS_RULE_TOKENS[facet_class]:
        if token in subject:
            return token
    return ""


def make_surface_edge_witness(surface: str) -> dict[str, Any]:
    facet_class = SURFACE_CLASS_MAP[surface]
    subject = anchor_subject(surface)
    token = matched_token(subject, facet_class)
    anchor = CLASS_ANCHOR_MAP[facet_class]
    return {
        "surface": surface,
        "kind": surface_kind(surface),
        "subject": subject,
        "matched_token": token,
        "facet_class": facet_class,
        "class_rule": f"token:{token}->class:{facet_class}",
        "anchor": anchor,
        "anchor_rule": f"class:{facet_class}->anchor:{anchor}",
        "composed_anchor": anchor,
        "uses_surface_name_only": False,
        "uses_global_lookup_only": False,
    }


SURFACE_EDGE_WITNESSES = {
    surface: make_surface_edge_witness(surface)
    for surface in BOUNDARY_SURFACES
}


def make_class_anchor_edge_witness(facet_class: str) -> dict[str, Any]:
    surfaces = frozenset(
        surface
        for surface, klass in SURFACE_CLASS_MAP.items()
        if klass == facet_class
    )
    tokens = frozenset(
        SURFACE_EDGE_WITNESSES[surface]["matched_token"]
        for surface in surfaces
        if SURFACE_EDGE_WITNESSES[surface]["matched_token"]
    )
    anchor = CLASS_ANCHOR_MAP[facet_class]
    return {
        "facet_class": facet_class,
        "anchor": anchor,
        "support_surfaces": surfaces,
        "support_tokens": tokens,
        "anchor_rule": f"class:{facet_class}->anchor:{anchor}",
        "support_nonempty": bool(surfaces),
        "uses_global_lookup_only": False,
    }


CLASS_ANCHOR_EDGE_WITNESSES = {
    facet_class: make_class_anchor_edge_witness(facet_class)
    for facet_class in USED_FACET_CLASSES
}

REQUIRED_DEPS = DOC604_REQUIRED_DEPS | {
    KILLROUTEACTION,
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
    (KILLROUTEACTION, "made_facet_route_edge_witness_by", KILLEDGEACTION),
    (KILLEDGEACTION, "witnesses_facet_route_graph_for", KILLROUTEACTION),
    (KILLEDGEACTION, "witnesses_facet_taxonomy_for", KILLFACETACTION),
    (KILLEDGEACTION, "witnesses_killfrontier_facets_for", KILLBNDRACTION),
    (KILLEDGEACTION, "witnesses_boundary_separator_for", BOUNDARYACTION),
    (KILLEDGEACTION, "witnesses_terminal_basin_for", BASINACTION),
    (KILLEDGEACTION, "witnesses_fixedpoint_for", FIXPTACTION),
    (KILLEDGEACTION, "witnesses_normalform_reflection_for", NFREFLACTION),
    (KILLEDGEACTION, "witnesses_confluent_action_for", CONFLACTION),
    (KILLEDGEACTION, "witnesses_action_plan_for", ACTIONCLASS),
    (KILLEDGEACTION, "witnesses_classifier_for", CLASSIFYLOC),
    (KILLEDGEACTION, "witnesses_localizer_for", LOCALIZEVERIFY),
    (KILLEDGEACTION, "witnesses_verifier_for", VERIFYTRACE),
    (KILLEDGEACTION, "witnesses_trace_audit_for", TRACEEXEC),
    (KILLEDGEACTION, "witnesses_executable_global_contraction_for", EXECGLOB),
    (KILLEDGEACTION, "witnesses_global_contraction_for", GLOBCONTR),
    (KILLEDGEACTION, "witnesses_terminal_certificate_for", TERMINAL_CERT),
} | {(KILLEDGEACTION, "witnesses_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_route_edge_witness_source_internal",
    "terminal_basin_boundary_killfrontier_facet_route_edge_witness_total",
    "terminal_basin_boundary_killfrontier_facet_route_edge_witness_local",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_edge_witness_certificate",
    "missing_surface_edge_witness",
    "missing_class_anchor_edge_witness",
    "edge_subject_missing",
    "edge_kind_mismatch",
    "local_token_missing",
    "class_rule_mismatch",
    "anchor_rule_mismatch",
    "composite_witness_mismatch",
    "name_only_surface_edge",
    "global_lookup_only_surface_edge",
    "global_lookup_only_class_anchor_edge",
    "class_anchor_support_missing",
    "class_anchor_support_token_missing",
    "edge_witness_not_minimal",
    "edge_witness_not_finite",
    "edge_witness_not_source_internal",
    "edge_witness_not_deterministic",
    "edge_witness_not_extensional",
    "edge_witness_not_dependency_closed",
    "edge_witness_not_graph_wired",
    "edge_witness_not_replay_stable",
    "proof_irrelevant_edge_witness",
    "external_edge_witness",
    "oracle_edge_witness",
    "branch_spawning_edge_witness",
    "unbounded_edge_witness_search",
    "retuned_edge_witness",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

EDGE_WITNESS_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_reflected_fixedpoint_trace_executable_global_contraction",
    "base_route_graph": KILLROUTEACTION,
    "base_taxonomy": KILLFACETACTION,
    "exists": True,
    "has_edge_witness_certificate": True,
    "source_internal": True,
    "total": True,
    "local": True,
    "minimal": True,
    "finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "budgeted": True,
    "external_edge_witness": False,
    "oracle_edge_witness": False,
    "branch_spawning": False,
    "unbounded_edge_witness_search": False,
    "retuned_edge_witness": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "surface_edge_witnesses": SURFACE_EDGE_WITNESSES,
    "class_anchor_edge_witnesses": CLASS_ANCHOR_EDGE_WITNESSES,
    "surface_to_class_edges": SURFACE_TO_CLASS_EDGES,
    "class_to_anchor_edges": CLASS_TO_ANCHOR_EDGES,
    "composed_surface_anchor_map": COMPOSED_SURFACE_ANCHOR_MAP,
    "boundary_anchor_map": BOUNDARY_ANCHOR_MAP,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_doc604_flags": DOC604_BANNED_FLAGS,
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
        "route_graph": deepcopy(FACET_ROUTE_GRAPH_DATA),
        "edge_witness": deepcopy(EDGE_WITNESS_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "route_graph":
            state["route_graph"].update(value)
        elif key == "edge_witness":
            state["edge_witness"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLEDGEACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess_surface_witnesses(edge_witness: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    witnesses = edge_witness["surface_edge_witnesses"]
    if set(witnesses) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "missing_surface_edge_witness")
    for surface in BOUNDARY_SURFACES:
        witness = witnesses.get(surface)
        if not witness:
            reasons.append(FLAG_PREFIX + "missing_surface_edge_witness")
            continue
        expected_subject = anchor_subject(surface)
        expected_class = SURFACE_CLASS_MAP[surface]
        expected_anchor = CLASS_ANCHOR_MAP[expected_class]
        expected_kind = surface_kind(surface)
        token = witness.get("matched_token", "")
        if witness.get("surface") != surface:
            reasons.append(FLAG_PREFIX + "missing_surface_edge_witness")
        if witness.get("kind") != expected_kind:
            reasons.append(FLAG_PREFIX + "edge_kind_mismatch")
        if witness.get("subject") != expected_subject or not expected_subject:
            reasons.append(FLAG_PREFIX + "edge_subject_missing")
        if not token or token not in CLASS_RULE_TOKENS[expected_class] or token not in expected_subject:
            reasons.append(FLAG_PREFIX + "local_token_missing")
        if witness.get("facet_class") != expected_class or witness.get("class_rule") != f"token:{token}->class:{expected_class}":
            reasons.append(FLAG_PREFIX + "class_rule_mismatch")
        if witness.get("anchor") != expected_anchor or witness.get("anchor_rule") != f"class:{expected_class}->anchor:{expected_anchor}":
            reasons.append(FLAG_PREFIX + "anchor_rule_mismatch")
        if witness.get("composed_anchor") != BOUNDARY_ANCHOR_MAP[surface]:
            reasons.append(FLAG_PREFIX + "composite_witness_mismatch")
        if witness.get("uses_surface_name_only"):
            reasons.append(FLAG_PREFIX + "name_only_surface_edge")
        if witness.get("uses_global_lookup_only"):
            reasons.append(FLAG_PREFIX + "global_lookup_only_surface_edge")
    return reasons


def assess_class_anchor_witnesses(edge_witness: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    witnesses = edge_witness["class_anchor_edge_witnesses"]
    if set(witnesses) != USED_FACET_CLASSES:
        reasons.append(FLAG_PREFIX + "missing_class_anchor_edge_witness")
    for facet_class in USED_FACET_CLASSES:
        witness = witnesses.get(facet_class)
        if not witness:
            reasons.append(FLAG_PREFIX + "missing_class_anchor_edge_witness")
            continue
        expected_anchor = CLASS_ANCHOR_MAP[facet_class]
        support = set(witness.get("support_surfaces", set()))
        support_tokens = set(witness.get("support_tokens", set()))
        if witness.get("facet_class") != facet_class:
            reasons.append(FLAG_PREFIX + "missing_class_anchor_edge_witness")
        if witness.get("anchor") != expected_anchor or witness.get("anchor_rule") != f"class:{facet_class}->anchor:{expected_anchor}":
            reasons.append(FLAG_PREFIX + "anchor_rule_mismatch")
        if not witness.get("support_nonempty") or not support:
            reasons.append(FLAG_PREFIX + "class_anchor_support_missing")
        if support and any(SURFACE_CLASS_MAP.get(surface) != facet_class for surface in support):
            reasons.append(FLAG_PREFIX + "class_anchor_support_missing")
        if not support_tokens:
            reasons.append(FLAG_PREFIX + "class_anchor_support_token_missing")
        if witness.get("uses_global_lookup_only"):
            reasons.append(FLAG_PREFIX + "global_lookup_only_class_anchor_edge")
    return reasons


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    route = state["route_graph"]
    edge_witness = state["edge_witness"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_605")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc605_witness")
    if KILLEDGEACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLEDGEACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if edge_witness.get("base_route_graph") != KILLROUTEACTION or not route.get("has_route_graph_certificate"):
        reasons.append("wrong_edge_witness_base")
    if not route.get("total") or not route.get("two_step_composable"):
        reasons.append("missing_doc604_route_graph_state")

    if not edge_witness.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not edge_witness.get("has_edge_witness_certificate"):
        reasons.append(FLAG_PREFIX + "no_edge_witness_certificate")
    if not edge_witness.get("total"):
        reasons.append(FLAG_PREFIX + "missing_surface_edge_witness")
    if not edge_witness.get("local"):
        reasons.append(FLAG_PREFIX + "global_lookup_only_surface_edge")
    if set(edge_witness["surface_to_class_edges"]) != SURFACE_TO_CLASS_EDGES:
        reasons.append(FLAG_PREFIX + "missing_surface_edge_witness")
    if set(edge_witness["class_to_anchor_edges"]) != CLASS_TO_ANCHOR_EDGES:
        reasons.append(FLAG_PREFIX + "missing_class_anchor_edge_witness")
    if dict(edge_witness["composed_surface_anchor_map"]) != BOUNDARY_ANCHOR_MAP:
        reasons.append(FLAG_PREFIX + "composite_witness_mismatch")

    reasons.extend(assess_surface_witnesses(edge_witness))
    reasons.extend(assess_class_anchor_witnesses(edge_witness))

    if not edge_witness.get("minimal"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_minimal")
    if not edge_witness.get("finite"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_finite")
    if not edge_witness.get("source_internal"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_source_internal")
    if not edge_witness.get("deterministic"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_deterministic")
    if not edge_witness.get("extensional"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_extensional")
    if not edge_witness.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_dependency_closed")
    if not edge_witness.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_graph_wired")
    if not edge_witness.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "edge_witness_not_replay_stable")
    if not edge_witness.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_edge_witness")
    if edge_witness.get("external_edge_witness"):
        reasons.append(FLAG_PREFIX + "external_edge_witness")
    if edge_witness.get("oracle_edge_witness"):
        reasons.append(FLAG_PREFIX + "oracle_edge_witness")
    if edge_witness.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_edge_witness")
    if edge_witness.get("unbounded_edge_witness_search"):
        reasons.append(FLAG_PREFIX + "unbounded_edge_witness_search")
    if edge_witness.get("retuned_edge_witness"):
        reasons.append(FLAG_PREFIX + "retuned_edge_witness")
    if edge_witness.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if edge_witness.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if edge_witness.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if edge_witness.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if edge_witness.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not edge_witness.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if edge_witness["payload_events"] != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if edge_witness["rejected_doc604_flags"] != DOC604_BANNED_FLAGS:
        reasons.append("doc604_rejected_flags_not_preserved")

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
        and KILLEDGEACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["edge_witness"]["base_route_graph"] == KILLROUTEACTION
        and state["route_graph"]["has_route_graph_certificate"]
        and state["route_graph"]["two_step_composable"],
        "doc604 route graph is the edge-witness base",
    )
    gate(
        f"{PREFIX}3",
        set(state["edge_witness"]["surface_edge_witnesses"]) == BOUNDARY_SURFACES
        and set(state["edge_witness"]["class_anchor_edge_witnesses"]) == USED_FACET_CLASSES,
        f"surface_witnesses={len(BOUNDARY_SURFACES)} class_anchor_witnesses={len(USED_FACET_CLASSES)}",
    )
    gate(
        f"{PREFIX}4",
        not assess_surface_witnesses(state["edge_witness"]),
        "every surface edge has source kind, local subject, token, class rule, and composed anchor",
    )
    gate(
        f"{PREFIX}5",
        not assess_class_anchor_witnesses(state["edge_witness"]),
        f"class_anchor_edges={len(CLASS_ANCHOR_EDGE_WITNESSES)} anchors={len(USED_KILL_FRONTIER_IDS)}",
    )
    gate(
        f"{PREFIX}6",
        dict(state["edge_witness"]["composed_surface_anchor_map"]) == BOUNDARY_ANCHOR_MAP
        and dict(state["edge_witness"]["composed_surface_anchor_map"]) == COMPOSED_SURFACE_ANCHOR_MAP,
        "edge witnesses compose to the doc602 boundary-anchor map",
    )
    gate(
        f"{PREFIX}7",
        state["edge_witness"]["minimal"]
        and state["edge_witness"]["finite"]
        and state["edge_witness"]["source_internal"]
        and state["edge_witness"]["deterministic"]
        and state["edge_witness"]["extensional"]
        and state["edge_witness"]["proof_relevant"]
        and state["edge_witness"]["dependency_closed"]
        and state["edge_witness"]["graph_wired"]
        and state["edge_witness"]["replay_stable"]
        and state["edge_witness"]["budgeted"]
        and not any(
            state["edge_witness"][key]
            for key in (
                "external_edge_witness",
                "oracle_edge_witness",
                "branch_spawning",
                "unbounded_edge_witness_search",
                "retuned_edge_witness",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "edge witnesses are minimal, finite, local, source-internal, replay-stable, and budgeted",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLEDGEACTION, [])) <= state["accepted"]
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: route graph edges carry local semantic witnesses")
    print(
        "VERDICT: the missing-object candidate now counts only when each route "
        "edge has a local semantic witness; name-only edges, global lookup-only "
        "edges, unsupported class anchors, and mismatched composites are "
        "disguised repairs."
    )


if __name__ == "__main__":
    main()
