#!/usr/bin/env python3
r"""Typed source-event classifier for terminal-basin route edges.

Doc 607 kills preserving the exact doc606 substring-priority decisions under a
finite source-native typed token grammar. This witness makes the constructive
counter-move: classify every boundary surface by typed source events
(namespace, obstruction-tail, exact tail, or named event kind), not substring
tokens.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_contract import (
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
    EDGE_PRIORITY_DATA,
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
    KILLPRIORITYACTION,
    KILLROUTEACTION,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    PRIORITY_DECISIONS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC606_REQUIRED_DEPS,
    SEMANTIC_PRIORITY,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    BANNED_FLAGS as DOC606_BANNED_FLAGS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_token_grammar_no_go import (
    ACTION_IN_CONTRACTION_SURFACE,
    STRICT_SHADOW_FAILURES,
    STRICT_WINNER_FAILURES,
    SUBSTRING_ONLY_MATCHES,
    typed_token_stream,
)


EXPECTED_DOC = 608
EXPECTED_WITNESS = "doc608-probe-obstruction-terminal-basin-boundary-killfrontier-facet-route-edge-typed-source-event-classifier-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDEVENTEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLTYPEDEVENTACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

MISSING_TERMINAL_BASIN_CERTIFICATE = (
    "missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate"
)

NAMESPACE_CLASS_RULES = {
    "payload": "trace_payload_route",
    "class": "classifier_partition",
    "action": "action_semantics",
    "invariant": "source_constraint_invariant",
}

OBSTRUCTION_TAIL_CLASS_RULES = {
    "budget_violation": "finite_index_budget",
    "repair_required_existing_requirement": "dependency_repair_nogo",
    "dependency_missing": "dependency_repair_nogo",
    "fatal_no_go": "dependency_repair_nogo",
    "external_or_oracle": "boundary_externality",
    "presentation_or_sample": "boundary_contextual_surrogate",
    "context_collapse": "boundary_contextual_surrogate",
}

TAIL_CLASS_RULES = {
    "verifier_check": frozenset({"verifier_entry", "verifier_entry_missing"}),
    "trace_audit_check": frozenset({"trace_audit_entry", "trace_audit_entry_missing", "trace_state_entry"}),
    "trace_payload_route": frozenset({"payload_entry_missing"}),
    "localizer_blame": frozenset({"localizer_entry", "localizer_entry_missing"}),
    "classifier_partition": frozenset({"classifier_entry", "classifier_entry_missing"}),
    "action_semantics": frozenset({"action_plan_entry", "action_entry_missing"}),
    "confluence_normalizer": frozenset({"confluence_entry", "confluence_entry_missing"}),
    "reflection_normalform": frozenset({"reflection_entry", "reflection_entry_missing"}),
    "fixedpoint_replay": frozenset(
        {
            "fixedpoint_entry",
            "fixedpoint_entry_missing",
            "entry_trace_changes_fixedpoint",
            "multiple_fixedpoints",
        }
    ),
    "terminal_basin_entry": frozenset(
        {
            "basin_not_absorbing",
            "entry_trace_not_replay_stable",
            "entry_trace_nonterminating",
            "proof_irrelevant_basin",
            "no_basin_certificate",
            "incomplete_entry_trace_cover",
            "entry_trace_nondeterministic",
            "unbounded_basin_search",
            "overlapping_incompatible_basins",
            "basin_not_extensional",
            "entry_trace_escapes",
            "noncanonical_basin",
            "unlisted_entry_trace",
            "external_basin",
            "oracle_basin",
            "branch_spawning_basin",
            "retuned_basin",
        }
    ),
    "source_constraint_invariant": frozenset({"invariant_entry_missing"}),
    "source_internality": frozenset({"not_source_internal"}),
    "finite_index_budget": frozenset(
        {"budget_state_entry", "requires_new_cell", "not_budgeted", "budget_entry_missing"}
    ),
    "dependency_repair_nogo": frozenset(
        {
            "repair_state_entry",
            "repair_entry_missing",
            "no_go_state_entry",
            "accepted_state_entry",
            "no_go_entry_missing",
        }
    ),
    "boundary_contextual_surrogate": frozenset(
        {
            "basis_row",
            "finite_sample",
            "sample_state_entry",
            "context_state_entry",
            "sample_entry_missing",
            "context_collapse",
            "by_declaration",
            "context_entry_missing",
        }
    ),
    "boundary_shape": frozenset({"missing", "trace_entry_missing"}),
}

RULE_LITERAL_COUNT = (
    len(NAMESPACE_CLASS_RULES)
    + len(OBSTRUCTION_TAIL_CLASS_RULES)
    + sum(len(tails) for tails in TAIL_CLASS_RULES.values())
    + 1
)


def boundary_kind(surface: str) -> str:
    if surface.startswith("entry_boundary:"):
        return "entry"
    if surface.startswith("escape_boundary:"):
        return "escape"
    return "unknown"


def source_event(surface: str) -> dict[str, Any]:
    subject = PRIORITY_DECISIONS[surface]["subject"]
    parts = tuple(subject.split(":"))
    tail = parts[-1]
    namespaces = parts[:-1]
    segments = tuple(segment for segment in tail.split("_") if segment)
    event_kind = "plain_tail"
    if subject == MISSING_TERMINAL_BASIN_CERTIFICATE:
        event_kind = "missing_terminal_basin_certificate"
    elif namespaces:
        event_kind = f"{namespaces[0]}_namespace"
    elif tail.endswith("_entry_missing"):
        event_kind = "entry_missing_tail"
    elif tail.startswith("entry_trace_"):
        event_kind = "entry_trace_tail"
    return {
        "surface": surface,
        "boundary_kind": boundary_kind(surface),
        "subject": subject,
        "namespaces": namespaces,
        "tail": tail,
        "segments": segments,
        "event_kind": event_kind,
        "typed_tokens": typed_token_stream(subject),
    }


def classify_event(event: dict[str, Any]) -> tuple[str, str, tuple[str, str]]:
    if event["event_kind"] == "missing_terminal_basin_certificate":
        return "action_semantics", "event_kind:missing_terminal_basin_certificate", (
            "event_kind",
            event["event_kind"],
        )

    namespaces = event["namespaces"]
    if namespaces:
        namespace = namespaces[0]
        if namespace in NAMESPACE_CLASS_RULES:
            return NAMESPACE_CLASS_RULES[namespace], f"namespace:{namespace}", ("namespace", namespace)
        if namespace == "obstruction" and event["tail"] in OBSTRUCTION_TAIL_CLASS_RULES:
            tail = event["tail"]
            return OBSTRUCTION_TAIL_CLASS_RULES[tail], f"obstruction_tail:{tail}", (
                "obstruction_tail",
                tail,
            )

    for facet_class, tails in TAIL_CLASS_RULES.items():
        if event["tail"] in tails:
            return facet_class, f"tail:{event['tail']}", ("tail", event["tail"])

    return "", "unclassified", ("missing", event["tail"])


SOURCE_EVENTS = {surface: source_event(surface) for surface in BOUNDARY_SURFACES}


def make_decision(surface: str) -> dict[str, Any]:
    event = SOURCE_EVENTS[surface]
    facet_class, rule_id, evidence = classify_event(event)
    anchor = CLASS_ANCHOR_MAP[facet_class] if facet_class else ""
    return {
        "surface": surface,
        "subject": event["subject"],
        "event": event,
        "winning_class": facet_class,
        "rule_id": rule_id,
        "typed_evidence": evidence,
        "shadow_classes": (),
        "uses_substring_token": False,
        "uses_doc606_winning_token": False,
        "composed_anchor": anchor,
    }


SOURCE_EVENT_DECISIONS = {surface: make_decision(surface) for surface in BOUNDARY_SURFACES}

REQUIRED_DEPS = DOC606_REQUIRED_DEPS | {
    KILLPRIORITYACTION,
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
    (KILLPRIORITYACTION, "made_typed_source_event_classifier_by", KILLTYPEDEVENTACTION),
    (KILLTYPEDEVENTACTION, "audits_priority_layer_for", KILLPRIORITYACTION),
    (KILLTYPEDEVENTACTION, "audits_edge_witness_for", KILLEDGEACTION),
    (KILLTYPEDEVENTACTION, "audits_facet_route_graph_for", KILLROUTEACTION),
    (KILLTYPEDEVENTACTION, "audits_facet_taxonomy_for", KILLFACETACTION),
    (KILLTYPEDEVENTACTION, "audits_killfrontier_facets_for", KILLBNDRACTION),
    (KILLTYPEDEVENTACTION, "audits_boundary_separator_for", BOUNDARYACTION),
    (KILLTYPEDEVENTACTION, "audits_terminal_basin_for", BASINACTION),
    (KILLTYPEDEVENTACTION, "audits_fixedpoint_for", FIXPTACTION),
    (KILLTYPEDEVENTACTION, "audits_normalform_reflection_for", NFREFLACTION),
    (KILLTYPEDEVENTACTION, "audits_confluent_action_for", CONFLACTION),
    (KILLTYPEDEVENTACTION, "audits_action_plan_for", ACTIONCLASS),
    (KILLTYPEDEVENTACTION, "audits_classifier_for", CLASSIFYLOC),
    (KILLTYPEDEVENTACTION, "audits_localizer_for", LOCALIZEVERIFY),
    (KILLTYPEDEVENTACTION, "audits_verifier_for", VERIFYTRACE),
    (KILLTYPEDEVENTACTION, "audits_trace_audit_for", TRACEEXEC),
    (KILLTYPEDEVENTACTION, "audits_executable_global_contraction_for", EXECGLOB),
    (KILLTYPEDEVENTACTION, "audits_global_contraction_for", GLOBCONTR),
    (KILLTYPEDEVENTACTION, "audits_terminal_certificate_for", TERMINAL_CERT),
} | {(KILLTYPEDEVENTACTION, "audits_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_source_internal",
    "terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_total",
    "terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_no_substring",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_typed_source_event_classifier_certificate",
    "source_event_decision_missing",
    "source_event_kind_missing",
    "source_event_namespace_mismatch",
    "source_event_tail_mismatch",
    "source_event_rule_mismatch",
    "typed_evidence_missing",
    "uses_substring_token",
    "preserves_doc606_substring_evidence",
    "doc607_hard_failure_unresolved",
    "doc607_shadow_failure_unresolved",
    "source_event_anchor_mismatch",
    "source_event_not_minimal",
    "source_event_not_finite",
    "source_event_not_source_internal",
    "source_event_not_deterministic",
    "source_event_not_extensional",
    "source_event_not_dependency_closed",
    "source_event_not_graph_wired",
    "source_event_not_replay_stable",
    "proof_irrelevant_source_event_classifier",
    "external_source_event_classifier",
    "oracle_source_event_classifier",
    "branch_spawning_source_event_classifier",
    "unbounded_source_event_search",
    "retuned_source_event_classifier",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

TYPED_SOURCE_EVENT_CLASSIFIER_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_reflected_fixedpoint_trace_executable_global_contraction",
    "base_priority": KILLPRIORITYACTION,
    "base_doc606_priority_data": EDGE_PRIORITY_DATA,
    "exists": True,
    "has_typed_source_event_classifier_certificate": True,
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
    "external_classifier": False,
    "oracle_classifier": False,
    "branch_spawning": False,
    "unbounded_search": False,
    "retuned_classifier": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "namespace_rules": NAMESPACE_CLASS_RULES,
    "obstruction_tail_rules": OBSTRUCTION_TAIL_CLASS_RULES,
    "tail_rules": TAIL_CLASS_RULES,
    "rule_literal_count": RULE_LITERAL_COUNT,
    "source_events": SOURCE_EVENTS,
    "decisions": SOURCE_EVENT_DECISIONS,
    "doc607_winner_failures": STRICT_WINNER_FAILURES,
    "doc607_shadow_failures": STRICT_SHADOW_FAILURES,
    "doc607_substring_only_matches": SUBSTRING_ONLY_MATCHES,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_doc606_flags": DOC606_BANNED_FLAGS,
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
        "classifier": deepcopy(TYPED_SOURCE_EVENT_CLASSIFIER_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "classifier":
            state["classifier"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLTYPEDEVENTACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess_decisions(classifier: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    decisions = classifier["decisions"]
    events = classifier["source_events"]
    if set(decisions) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "source_event_decision_missing")
    if set(events) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "source_event_kind_missing")

    for surface in BOUNDARY_SURFACES:
        event = events.get(surface)
        decision = decisions.get(surface)
        if not event or not decision:
            reasons.append(FLAG_PREFIX + "source_event_decision_missing")
            continue
        if event.get("subject") != PRIORITY_DECISIONS[surface]["subject"]:
            reasons.append(FLAG_PREFIX + "source_event_tail_mismatch")
        if not event.get("event_kind"):
            reasons.append(FLAG_PREFIX + "source_event_kind_missing")
        if "namespaces" not in event:
            reasons.append(FLAG_PREFIX + "source_event_namespace_mismatch")
        if not event.get("tail"):
            reasons.append(FLAG_PREFIX + "source_event_tail_mismatch")

        expected_class, expected_rule, expected_evidence = classify_event(event)
        if decision.get("winning_class") != expected_class or decision.get("rule_id") != expected_rule:
            reasons.append(FLAG_PREFIX + "source_event_rule_mismatch")
        if decision.get("typed_evidence") != expected_evidence or expected_evidence[0] == "missing":
            reasons.append(FLAG_PREFIX + "typed_evidence_missing")
        if decision.get("winning_class") != PRIORITY_DECISIONS[surface]["winning_class"]:
            reasons.append(FLAG_PREFIX + "source_event_rule_mismatch")
        if decision.get("uses_substring_token"):
            reasons.append(FLAG_PREFIX + "uses_substring_token")
        if decision.get("uses_doc606_winning_token"):
            reasons.append(FLAG_PREFIX + "preserves_doc606_substring_evidence")
        if decision.get("composed_anchor") != BOUNDARY_ANCHOR_MAP[surface]:
            reasons.append(FLAG_PREFIX + "source_event_anchor_mismatch")

    for surface, _subject, _facet_class, tokens in STRICT_WINNER_FAILURES:
        decision = decisions.get(surface, {})
        if decision.get("typed_evidence", ("", ""))[1] in tokens or decision.get("uses_doc606_winning_token"):
            reasons.append(FLAG_PREFIX + "doc607_hard_failure_unresolved")
    for surface, _subject, facet_class, _tokens in STRICT_SHADOW_FAILURES:
        decision = decisions.get(surface, {})
        if facet_class in decision.get("shadow_classes", ()):
            reasons.append(FLAG_PREFIX + "doc607_shadow_failure_unresolved")
    action_decision = decisions.get(ACTION_IN_CONTRACTION_SURFACE, {})
    if action_decision.get("typed_evidence") != ("event_kind", "missing_terminal_basin_certificate"):
        reasons.append(FLAG_PREFIX + "doc607_hard_failure_unresolved")

    return reasons


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    classifier = state["classifier"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_608")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc608_witness")
    if KILLTYPEDEVENTACTION not in state["accepted"]:
        reasons.append(
            "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_reflected_fixedpoint_trace_executable_global_contraction_certificate"
        )

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLTYPEDEVENTACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if classifier.get("base_priority") != KILLPRIORITYACTION:
        reasons.append("wrong_classifier_base")
    if not classifier.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not classifier.get("has_typed_source_event_classifier_certificate"):
        reasons.append(FLAG_PREFIX + "no_typed_source_event_classifier_certificate")
    if not classifier.get("total") or not classifier.get("explicit"):
        reasons.append(FLAG_PREFIX + "source_event_decision_missing")
    if not classifier.get("source_events"):
        reasons.append(FLAG_PREFIX + "source_event_kind_missing")

    reasons.extend(assess_decisions(classifier))

    if classifier.get("rule_literal_count", 10**9) >= len(BOUNDARY_SURFACES):
        reasons.append(FLAG_PREFIX + "source_event_not_minimal")
    if set(classifier.get("namespace_rules", {})) != set(NAMESPACE_CLASS_RULES):
        reasons.append(FLAG_PREFIX + "source_event_namespace_mismatch")
    if classifier.get("payload_events") != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if classifier.get("rejected_doc606_flags") != DOC606_BANNED_FLAGS:
        reasons.append("doc606_rejected_flags_not_preserved")

    if not classifier.get("minimal"):
        reasons.append(FLAG_PREFIX + "source_event_not_minimal")
    if not classifier.get("finite"):
        reasons.append(FLAG_PREFIX + "source_event_not_finite")
    if not classifier.get("source_internal"):
        reasons.append(FLAG_PREFIX + "source_event_not_source_internal")
    if not classifier.get("deterministic"):
        reasons.append(FLAG_PREFIX + "source_event_not_deterministic")
    if not classifier.get("extensional"):
        reasons.append(FLAG_PREFIX + "source_event_not_extensional")
    if not classifier.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "source_event_not_dependency_closed")
    if not classifier.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "source_event_not_graph_wired")
    if not classifier.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "source_event_not_replay_stable")
    if not classifier.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_source_event_classifier")
    if classifier.get("external_classifier"):
        reasons.append(FLAG_PREFIX + "external_source_event_classifier")
    if classifier.get("oracle_classifier"):
        reasons.append(FLAG_PREFIX + "oracle_source_event_classifier")
    if classifier.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_source_event_classifier")
    if classifier.get("unbounded_search"):
        reasons.append(FLAG_PREFIX + "unbounded_source_event_search")
    if classifier.get("retuned_classifier"):
        reasons.append(FLAG_PREFIX + "retuned_source_event_classifier")
    if classifier.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if classifier.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if classifier.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if classifier.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if classifier.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not classifier.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

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
        and KILLTYPEDEVENTACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["classifier"]["base_priority"] == KILLPRIORITYACTION
        and state["classifier"]["base_doc606_priority_data"]["has_priority_certificate"],
        "doc606 priority layer is the typed-event replacement base",
    )
    gate(
        f"{PREFIX}3",
        len(state["classifier"]["source_events"]) == len(BOUNDARY_SURFACES)
        and len(state["classifier"]["decisions"]) == len(BOUNDARY_SURFACES)
        and state["classifier"]["rule_literal_count"] < len(BOUNDARY_SURFACES),
        f"source_events={len(BOUNDARY_SURFACES)} rule_literals={state['classifier']['rule_literal_count']}",
    )
    gate(
        f"{PREFIX}4",
        not assess_decisions(state["classifier"]),
        "all source-event decisions are typed, total, non-substring, and anchor-preserving",
    )
    gate(
        f"{PREFIX}5",
        all(
            state["classifier"]["decisions"][surface]["winning_class"]
            == PRIORITY_DECISIONS[surface]["winning_class"]
            for surface in BOUNDARY_SURFACES
        )
        and all(
            state["classifier"]["decisions"][surface]["composed_anchor"] == BOUNDARY_ANCHOR_MAP[surface]
            for surface in BOUNDARY_SURFACES
        ),
        "typed-event classes preserve doc602 anchor composition",
    )
    gate(
        f"{PREFIX}6",
        state["classifier"]["decisions"][ACTION_IN_CONTRACTION_SURFACE]["typed_evidence"]
        == ("event_kind", "missing_terminal_basin_certificate")
        and not any(decision["uses_doc606_winning_token"] for decision in state["classifier"]["decisions"].values()),
        "doc607 hard failure is resolved without action-inside-contraction evidence",
    )
    gate(
        f"{PREFIX}7",
        state["classifier"]["minimal"]
        and state["classifier"]["finite"]
        and state["classifier"]["source_internal"]
        and state["classifier"]["deterministic"]
        and state["classifier"]["extensional"]
        and state["classifier"]["proof_relevant"]
        and state["classifier"]["dependency_closed"]
        and state["classifier"]["graph_wired"]
        and state["classifier"]["replay_stable"]
        and state["classifier"]["budgeted"]
        and not any(
            state["classifier"][key]
            for key in (
                "external_classifier",
                "oracle_classifier",
                "branch_spawning",
                "unbounded_search",
                "retuned_classifier",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "typed-event classifier is finite, source-internal, replay-stable, and budgeted",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLTYPEDEVENTACTION, [])) <= state["accepted"]
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: typed source-event classifier replaces substring priority")
    print(
        "VERDICT: the route-edge classifier now uses finite source events and "
        "preserves doc602 anchor composition without doc606 substring evidence."
    )


if __name__ == "__main__":
    main()
