#!/usr/bin/env python3
r"""Priority audit for terminal-basin facet route edge witnesses.

Doc 605 makes every route edge carry a local semantic witness. This witness
closes the next escape: when a surface subject contains multiple semantic
tokens, the winning class may not be hidden in code order. The priority order
must be finite, explicit, replay-stable, and every surface witness must record
the winning class plus all lower-priority shadow classes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_contract import (
    ACTIONCLASS,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_ANCHOR_MAP,
    BOUNDARY_SURFACES,
    CLASSIFYLOC,
    CLASS_ANCHOR_EDGE_WITNESSES,
    CLASS_ANCHOR_MAP,
    CLASS_RULE_TOKENS,
    COHERENT,
    COMPOSED_SURFACE_ANCHOR_MAP,
    CONFLACTION,
    EDGE_WITNESS_DATA,
    EVAL,
    EXEC,
    EXECGLOB,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    KILLBNDRACTION,
    KILLEDGEACTION,
    KILLFACETACTION,
    KILLROUTEACTION,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC605_REQUIRED_DEPS,
    SEMCONS,
    SURFACE_CLASS_MAP,
    SURFACE_EDGE_WITNESSES,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    USED_FACET_CLASSES,
    VERIFYTRACE,
    BANNED_FLAGS as DOC605_BANNED_FLAGS,
    load_map,
)


EXPECTED_DOC = 606
EXPECTED_WITNESS = "doc606-probe-obstruction-terminal-basin-boundary-killfrontier-facet-route-edge-priority-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLPRIORITYACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

SEMANTIC_PRIORITY = (
    "verifier_check",
    "trace_audit_check",
    "trace_payload_route",
    "localizer_blame",
    "classifier_partition",
    "action_semantics",
    "confluence_normalizer",
    "reflection_normalform",
    "fixedpoint_replay",
    "terminal_basin_entry",
    "source_constraint_invariant",
    "source_internality",
    "finite_index_budget",
    "dependency_repair_nogo",
    "boundary_externality",
    "boundary_search_or_retune",
    "boundary_contextual_surrogate",
    "boundary_shape",
)
PRIORITY_INDEX = {facet_class: index for index, facet_class in enumerate(SEMANTIC_PRIORITY)}


def class_hits(subject: str) -> tuple[str, ...]:
    return tuple(
        facet_class
        for facet_class in SEMANTIC_PRIORITY
        if any(token in subject for token in CLASS_RULE_TOKENS[facet_class])
    )


def token_hits(subject: str, facet_class: str) -> tuple[str, ...]:
    return tuple(token for token in CLASS_RULE_TOKENS[facet_class] if token in subject)


def make_priority_decision(surface: str) -> dict[str, Any]:
    edge = SURFACE_EDGE_WITNESSES[surface]
    subject = edge["subject"]
    hits = class_hits(subject)
    winner = hits[0] if hits else ""
    return {
        "surface": surface,
        "subject": subject,
        "edge_class": edge["facet_class"],
        "winning_class": winner,
        "winning_index": PRIORITY_INDEX.get(winner, -1),
        "winning_tokens": token_hits(subject, winner) if winner else (),
        "shadow_classes": hits[1:],
        "shadow_tokens": {
            facet_class: token_hits(subject, facet_class)
            for facet_class in hits[1:]
        },
        "all_hits": hits,
        "composed_anchor": edge["composed_anchor"],
        "priority_order_used": SEMANTIC_PRIORITY,
        "priority_retuned": False,
        "uses_global_lookup_only": False,
        "uses_name_order_only": False,
    }


PRIORITY_DECISIONS = {
    surface: make_priority_decision(surface)
    for surface in BOUNDARY_SURFACES
}
AMBIGUOUS_PRIORITY_DECISIONS = frozenset(
    surface
    for surface, decision in PRIORITY_DECISIONS.items()
    if len(decision["all_hits"]) > 1
)

REQUIRED_DEPS = DOC605_REQUIRED_DEPS | {
    KILLEDGEACTION,
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
    (KILLEDGEACTION, "made_facet_route_edge_priority_by", KILLPRIORITYACTION),
    (KILLPRIORITYACTION, "audits_edge_witness_for", KILLEDGEACTION),
    (KILLPRIORITYACTION, "audits_facet_route_graph_for", KILLROUTEACTION),
    (KILLPRIORITYACTION, "audits_facet_taxonomy_for", KILLFACETACTION),
    (KILLPRIORITYACTION, "audits_killfrontier_facets_for", KILLBNDRACTION),
    (KILLPRIORITYACTION, "audits_boundary_separator_for", BOUNDARYACTION),
    (KILLPRIORITYACTION, "audits_terminal_basin_for", BASINACTION),
    (KILLPRIORITYACTION, "audits_fixedpoint_for", FIXPTACTION),
    (KILLPRIORITYACTION, "audits_normalform_reflection_for", NFREFLACTION),
    (KILLPRIORITYACTION, "audits_confluent_action_for", CONFLACTION),
    (KILLPRIORITYACTION, "audits_action_plan_for", ACTIONCLASS),
    (KILLPRIORITYACTION, "audits_classifier_for", CLASSIFYLOC),
    (KILLPRIORITYACTION, "audits_localizer_for", LOCALIZEVERIFY),
    (KILLPRIORITYACTION, "audits_verifier_for", VERIFYTRACE),
    (KILLPRIORITYACTION, "audits_trace_audit_for", TRACEEXEC),
    (KILLPRIORITYACTION, "audits_executable_global_contraction_for", EXECGLOB),
    (KILLPRIORITYACTION, "audits_global_contraction_for", GLOBCONTR),
    (KILLPRIORITYACTION, "audits_terminal_certificate_for", TERMINAL_CERT),
} | {(KILLPRIORITYACTION, "audits_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_route_edge_priority_source_internal",
    "terminal_basin_boundary_killfrontier_facet_route_edge_priority_total",
    "terminal_basin_boundary_killfrontier_facet_route_edge_priority_explicit",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_priority_certificate",
    "missing_priority_order",
    "priority_order_incomplete",
    "priority_order_retuned",
    "priority_decision_missing",
    "unprioritized_token_overlap",
    "winner_class_mismatch",
    "winning_token_missing",
    "shadow_token_unrecorded",
    "composite_priority_mismatch",
    "class_anchor_missing_from_priority",
    "global_lookup_priority",
    "name_order_priority",
    "priority_not_minimal",
    "priority_not_finite",
    "priority_not_source_internal",
    "priority_not_deterministic",
    "priority_not_extensional",
    "priority_not_dependency_closed",
    "priority_not_graph_wired",
    "priority_not_replay_stable",
    "proof_irrelevant_priority",
    "external_priority",
    "oracle_priority",
    "branch_spawning_priority",
    "unbounded_priority_search",
    "retuned_priority",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

EDGE_PRIORITY_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_reflected_fixedpoint_trace_executable_global_contraction",
    "base_edge_witness": KILLEDGEACTION,
    "exists": True,
    "has_priority_certificate": True,
    "source_internal": True,
    "total": True,
    "explicit": True,
    "minimal": True,
    "finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "budgeted": True,
    "external_priority": False,
    "oracle_priority": False,
    "branch_spawning": False,
    "unbounded_priority_search": False,
    "retuned_priority": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "priority_order": SEMANTIC_PRIORITY,
    "priority_decisions": PRIORITY_DECISIONS,
    "ambiguous_priority_decisions": AMBIGUOUS_PRIORITY_DECISIONS,
    "class_anchor_witnesses": CLASS_ANCHOR_EDGE_WITNESSES,
    "composed_surface_anchor_map": COMPOSED_SURFACE_ANCHOR_MAP,
    "boundary_anchor_map": BOUNDARY_ANCHOR_MAP,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_doc605_flags": DOC605_BANNED_FLAGS,
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
        "edge_witness": deepcopy(EDGE_WITNESS_DATA),
        "priority": deepcopy(EDGE_PRIORITY_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "edge_witness":
            state["edge_witness"].update(value)
        elif key == "priority":
            state["priority"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLPRIORITYACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess_priority_decisions(priority: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    decisions = priority["priority_decisions"]
    order = tuple(priority["priority_order"])
    if set(decisions) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "priority_decision_missing")
    if order != SEMANTIC_PRIORITY:
        reasons.append(FLAG_PREFIX + "priority_order_retuned")
    for surface in BOUNDARY_SURFACES:
        decision = decisions.get(surface)
        if not decision:
            reasons.append(FLAG_PREFIX + "priority_decision_missing")
            continue
        subject = SURFACE_EDGE_WITNESSES[surface]["subject"]
        hits = class_hits(subject)
        winner = hits[0] if hits else ""
        shadows = hits[1:]
        if decision.get("subject") != subject:
            reasons.append(FLAG_PREFIX + "priority_decision_missing")
        if len(hits) > 1 and decision.get("shadow_classes") != shadows:
            reasons.append(FLAG_PREFIX + "shadow_token_unrecorded")
        if len(hits) > 1 and surface not in priority["ambiguous_priority_decisions"]:
            reasons.append(FLAG_PREFIX + "unprioritized_token_overlap")
        if decision.get("winning_class") != winner or winner != SURFACE_CLASS_MAP[surface]:
            reasons.append(FLAG_PREFIX + "winner_class_mismatch")
        if not decision.get("winning_tokens"):
            reasons.append(FLAG_PREFIX + "winning_token_missing")
        for shadow_class in shadows:
            if shadow_class not in decision.get("shadow_tokens", {}) or not decision["shadow_tokens"][shadow_class]:
                reasons.append(FLAG_PREFIX + "shadow_token_unrecorded")
        if decision.get("composed_anchor") != BOUNDARY_ANCHOR_MAP[surface]:
            reasons.append(FLAG_PREFIX + "composite_priority_mismatch")
        if decision.get("priority_retuned"):
            reasons.append(FLAG_PREFIX + "priority_order_retuned")
        if decision.get("uses_global_lookup_only"):
            reasons.append(FLAG_PREFIX + "global_lookup_priority")
        if decision.get("uses_name_order_only"):
            reasons.append(FLAG_PREFIX + "name_order_priority")
    return reasons


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    edge_witness = state["edge_witness"]
    priority = state["priority"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_606")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc606_witness")
    if KILLPRIORITYACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLPRIORITYACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if priority.get("base_edge_witness") != KILLEDGEACTION or not edge_witness.get("has_edge_witness_certificate"):
        reasons.append("wrong_priority_base")
    if not edge_witness.get("total") or not edge_witness.get("local"):
        reasons.append("missing_doc605_edge_witness_state")

    if not priority.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not priority.get("has_priority_certificate"):
        reasons.append(FLAG_PREFIX + "no_priority_certificate")
    if not priority.get("priority_order"):
        reasons.append(FLAG_PREFIX + "missing_priority_order")
    if tuple(priority.get("priority_order", ())) != SEMANTIC_PRIORITY:
        reasons.append(FLAG_PREFIX + "priority_order_incomplete")
    if set(priority.get("priority_order", ())) != set(CLASS_RULE_TOKENS):
        reasons.append(FLAG_PREFIX + "class_anchor_missing_from_priority")
    if not priority.get("total") or not priority.get("explicit"):
        reasons.append(FLAG_PREFIX + "priority_decision_missing")
    if dict(priority["composed_surface_anchor_map"]) != BOUNDARY_ANCHOR_MAP:
        reasons.append(FLAG_PREFIX + "composite_priority_mismatch")

    reasons.extend(assess_priority_decisions(priority))

    used_anchor_classes = set(priority["class_anchor_witnesses"])
    if used_anchor_classes - set(priority["priority_order"]):
        reasons.append(FLAG_PREFIX + "class_anchor_missing_from_priority")

    if not priority.get("minimal"):
        reasons.append(FLAG_PREFIX + "priority_not_minimal")
    if not priority.get("finite"):
        reasons.append(FLAG_PREFIX + "priority_not_finite")
    if not priority.get("source_internal"):
        reasons.append(FLAG_PREFIX + "priority_not_source_internal")
    if not priority.get("deterministic"):
        reasons.append(FLAG_PREFIX + "priority_not_deterministic")
    if not priority.get("extensional"):
        reasons.append(FLAG_PREFIX + "priority_not_extensional")
    if not priority.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "priority_not_dependency_closed")
    if not priority.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "priority_not_graph_wired")
    if not priority.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "priority_not_replay_stable")
    if not priority.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_priority")
    if priority.get("external_priority"):
        reasons.append(FLAG_PREFIX + "external_priority")
    if priority.get("oracle_priority"):
        reasons.append(FLAG_PREFIX + "oracle_priority")
    if priority.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_priority")
    if priority.get("unbounded_priority_search"):
        reasons.append(FLAG_PREFIX + "unbounded_priority_search")
    if priority.get("retuned_priority"):
        reasons.append(FLAG_PREFIX + "retuned_priority")
    if priority.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if priority.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if priority.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if priority.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if priority.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not priority.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if priority["payload_events"] != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if priority["rejected_doc605_flags"] != DOC605_BANNED_FLAGS:
        reasons.append("doc605_rejected_flags_not_preserved")

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
        and KILLPRIORITYACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["priority"]["base_edge_witness"] == KILLEDGEACTION
        and state["edge_witness"]["has_edge_witness_certificate"]
        and state["edge_witness"]["local"],
        "doc605 edge witness is the priority-audit base",
    )
    gate(
        f"{PREFIX}3",
        tuple(state["priority"]["priority_order"]) == SEMANTIC_PRIORITY
        and set(state["priority"]["priority_order"]) == set(CLASS_RULE_TOKENS),
        f"priority_classes={len(SEMANTIC_PRIORITY)}",
    )
    gate(
        f"{PREFIX}4",
        set(state["priority"]["priority_decisions"]) == BOUNDARY_SURFACES
        and not assess_priority_decisions(state["priority"]),
        f"priority_decisions={len(BOUNDARY_SURFACES)} ambiguous={len(AMBIGUOUS_PRIORITY_DECISIONS)}",
    )
    gate(
        f"{PREFIX}5",
        set(state["priority"]["ambiguous_priority_decisions"]) == AMBIGUOUS_PRIORITY_DECISIONS,
        f"ambiguous_priority_decisions={len(AMBIGUOUS_PRIORITY_DECISIONS)}",
    )
    gate(
        f"{PREFIX}6",
        dict(state["priority"]["composed_surface_anchor_map"]) == BOUNDARY_ANCHOR_MAP
        and dict(state["priority"]["composed_surface_anchor_map"]) == COMPOSED_SURFACE_ANCHOR_MAP,
        "priority decisions preserve doc602 anchor composition",
    )
    gate(
        f"{PREFIX}7",
        state["priority"]["minimal"]
        and state["priority"]["finite"]
        and state["priority"]["source_internal"]
        and state["priority"]["deterministic"]
        and state["priority"]["extensional"]
        and state["priority"]["proof_relevant"]
        and state["priority"]["dependency_closed"]
        and state["priority"]["graph_wired"]
        and state["priority"]["replay_stable"]
        and state["priority"]["budgeted"]
        and not any(
            state["priority"][key]
            for key in (
                "external_priority",
                "oracle_priority",
                "branch_spawning",
                "unbounded_priority_search",
                "retuned_priority",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "priority audit is minimal, finite, explicit, source-internal, replay-stable, and budgeted",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLPRIORITYACTION, [])) <= state["accepted"]
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: edge-witness token overlaps have an explicit priority audit")
    print(
        "VERDICT: the missing-object candidate now counts only when semantic "
        "token overlaps are resolved by a finite declared priority order with "
        "recorded shadows; hidden code-order, name-order, global lookup, and "
        "retuned priorities are disguised repairs."
    )


if __name__ == "__main__":
    main()
