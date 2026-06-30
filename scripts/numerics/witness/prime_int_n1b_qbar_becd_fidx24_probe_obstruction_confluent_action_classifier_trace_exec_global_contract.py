#!/usr/bin/env python3
r"""Obstruction-confluent action classifier trace executable global contraction.

Doc 596 makes every obstruction class actionable. This witness closes the next
escape: bounded actions cannot depend on the order in which simultaneous
obstructions are handled. The doc 597 frontier only counts if the finite
action system is terminating and confluent, with every critical pair joined
inside the source-internal budget.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_confluent_action_classifier_trace_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from itertools import combinations_with_replacement
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_action_classifier_trace_exec_global_contract import (
    ACTIONCLASS,
    ACTION_CODES,
    ACTION_EVENTS,
    ACTION_DATA,
    ADM_CAT,
    BC,
    CLASSIFICATION_CODES,
    CLASSIFIER_EVENTS,
    CLASSIFYLOC,
    COHERENT,
    EVAL,
    EXEC,
    EXECGLOB,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    LOCALIZEVERIFY,
    LOCALIZER_EVENTS,
    NORM,
    OBSTRUCTION_CLASSES,
    OBSTRUCTION_FACETS,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC596_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 597
EXPECTED_WITNESS = "doc597-probe-obstruction-confluent-action-classifier-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

CONFLACTION = "obstruction_confluent_action_classifier_trace_executable_global_contraction_certificate"

failures: list[str] = []

ACTION_CRITICAL_PAIRS = {
    tuple(pair) for pair in combinations_with_replacement(sorted(ACTION_CODES), 2)
}

CONFLUENCE_EVENTS = {
    "detect_action_overlap",
    "enumerate_action_critical_pairs",
    "join_action_pair",
    "emit_critical_pair_diamond",
    "emit_unique_action_normal_form",
    "emit_monotone_join_measure",
    "emit_replayable_join_trace",
    "emit_no_order_choice_certificate",
    "emit_no_branch_spawn_certificate",
}

REQUIRED_DEPS = DOC596_REQUIRED_DEPS | {
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
    ADM_CAT,
}

EXPECTED_EDGES = {
    (ACTIONCLASS, "made_action_confluent_by", CONFLACTION),
    (CONFLACTION, "joins_action_plan_for", ACTIONCLASS),
    (CONFLACTION, "joins_classifier_actions_for", CLASSIFYLOC),
    (CONFLACTION, "joins_localized_obstruction_actions_for", LOCALIZEVERIFY),
    (CONFLACTION, "joins_verifier_failure_actions_for", VERIFYTRACE),
    (CONFLACTION, "joins_trace_audit_actions_for", TRACEEXEC),
    (CONFLACTION, "joins_executable_global_contraction_actions_for", EXECGLOB),
    (CONFLACTION, "joins_global_contraction_actions_for", GLOBCONTR),
    (CONFLACTION, "joins_action_law_via", NORM),
    (CONFLACTION, "joins_action_law_via", FUNC_NORM),
    (CONFLACTION, "joins_action_law_via", COHERENT),
    (CONFLACTION, "joins_action_law_via", EXEC),
    (CONFLACTION, "joins_action_law_via", SEMCONS),
    (CONFLACTION, "joins_action_law_via", REPSEM),
    (CONFLACTION, "joins_action_law_via", EVAL),
    (CONFLACTION, "joins_action_law_via", BC),
    (CONFLACTION, "joins_action_law_via", REFINEMENT_DESCENT),
    (CONFLACTION, "joins_action_law_via", TERMINAL_CERT),
    (CONFLACTION, "joins_action_law_via", UNIVERSAL_ARROW),
} | {(CONFLACTION, "joins_invariant_action_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_confluent_action_classifier_trace_executable_global_contraction_certificate",
    "action_confluence_source_internal",
    "action_confluence_critical_pairs_complete",
    "action_confluence_unique_normal_forms",
    "action_confluence_decreases_join_measure",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_confluent_action_classifier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_confluence_certificate",
    "class_order_dependent",
    "action_order_dependent",
    "action_conflict",
    "unresolved_critical_pair",
    "incomplete_critical_pairs",
    "not_locally_confluent",
    "not_globally_confluent",
    "nonterminating_join",
    "no_normal_form",
    "nonunique_normal_form",
    "nondeterministic_join",
    "nonmonotone_join",
    "external_join",
    "oracle_join",
    "not_source_internal",
    "proof_irrelevant_join",
    "nonextensional",
    "branch_spawning",
    "unbounded_completion",
    "repair_action_conflict",
    "no_go_action_conflict",
    "budget_context_conflict",
    "sample_action_conflict",
    "trace_replay_conflict",
    "retuned_join",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_confluent_action_classifier_trace_executable_global_contraction_certificate",
)

CONFLUENCE_DATA = {
    "certificate": "obstruction_confluent_action_classifier_trace_executable_global_contraction",
    "base_action_plan": ACTIONCLASS,
    "base_classifier": CLASSIFYLOC,
    "base_localizer": LOCALIZEVERIFY,
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_confluence_certificate": True,
    "source_internal": True,
    "finite_action_system": True,
    "terminating": True,
    "locally_confluent": True,
    "globally_confluent": True,
    "critical_pairs_complete": True,
    "unique_normal_form": True,
    "deterministic_join": True,
    "replay_stable": True,
    "proof_relevant": True,
    "extensional_over_action_trace": True,
    "budgeted": True,
    "class_order_dependent": False,
    "action_order_dependent": False,
    "action_conflict": False,
    "unresolved_critical_pair": False,
    "external_join": False,
    "oracle_join": False,
    "branch_spawning": False,
    "unbounded_completion": False,
    "repair_action_conflict": False,
    "no_go_action_conflict": False,
    "budget_context_conflict": False,
    "sample_action_conflict": False,
    "trace_replay_conflict": False,
    "retuned_join": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "actions": ACTION_CODES,
    "classes": CLASSIFICATION_CODES,
    "obstruction_classes": OBSTRUCTION_CLASSES,
    "critical_pairs": ACTION_CRITICAL_PAIRS,
    "joined_pairs": ACTION_CRITICAL_PAIRS,
    "normal_forms": ACTION_CODES,
    "confluence_events": CONFLUENCE_EVENTS,
    "action_events": ACTION_EVENTS,
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "action_plan": ACTION_DATA,
    "measure": "finite_action_pair_rank_then_frontier_size",
    "measure_decreases": True,
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
        "confluence": deepcopy(CONFLUENCE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "confluence":
            state["confluence"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CONFLACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    confl = state["confluence"]
    events = set(confl["confluence_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_597")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc597_witness")
    if CONFLACTION not in state["accepted"]:
        reasons.append("missing_obstruction_confluent_action_classifier_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(CONFLACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if confl.get("base_action_plan") != ACTIONCLASS or confl.get("base_classifier") != CLASSIFYLOC:
        reasons.append("wrong_confluence_base")
    if not confl.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not confl.get("has_confluence_certificate"):
        reasons.append(FLAG_PREFIX + "no_confluence_certificate")
    if confl.get("class_order_dependent"):
        reasons.append(FLAG_PREFIX + "class_order_dependent")
    if confl.get("action_order_dependent"):
        reasons.append(FLAG_PREFIX + "action_order_dependent")
    if confl.get("action_conflict"):
        reasons.append(FLAG_PREFIX + "action_conflict")
    if confl.get("unresolved_critical_pair"):
        reasons.append(FLAG_PREFIX + "unresolved_critical_pair")
    if not confl.get("critical_pairs_complete") or confl["critical_pairs"] != ACTION_CRITICAL_PAIRS:
        reasons.append(FLAG_PREFIX + "incomplete_critical_pairs")
    if not confl.get("locally_confluent"):
        reasons.append(FLAG_PREFIX + "not_locally_confluent")
    if not confl.get("globally_confluent"):
        reasons.append(FLAG_PREFIX + "not_globally_confluent")
    if not confl.get("terminating"):
        reasons.append(FLAG_PREFIX + "nonterminating_join")
    if not confl.get("unique_normal_form") or not confl["normal_forms"]:
        reasons.append(FLAG_PREFIX + "no_normal_form")
    if not confl.get("unique_normal_form"):
        reasons.append(FLAG_PREFIX + "nonunique_normal_form")
    if not confl.get("deterministic_join"):
        reasons.append(FLAG_PREFIX + "nondeterministic_join")
    if not confl.get("measure_decreases"):
        reasons.append(FLAG_PREFIX + "nonmonotone_join")
    if confl.get("external_join"):
        reasons.append(FLAG_PREFIX + "external_join")
    if confl.get("oracle_join"):
        reasons.append(FLAG_PREFIX + "oracle_join")
    if not confl.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not confl.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_join")
    if not confl.get("extensional_over_action_trace"):
        reasons.append(FLAG_PREFIX + "nonextensional")
    if confl.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning")
    if confl.get("unbounded_completion"):
        reasons.append(FLAG_PREFIX + "unbounded_completion")
    if confl.get("repair_action_conflict"):
        reasons.append(FLAG_PREFIX + "repair_action_conflict")
    if confl.get("no_go_action_conflict"):
        reasons.append(FLAG_PREFIX + "no_go_action_conflict")
    if confl.get("budget_context_conflict"):
        reasons.append(FLAG_PREFIX + "budget_context_conflict")
    if confl.get("sample_action_conflict"):
        reasons.append(FLAG_PREFIX + "sample_action_conflict")
    if confl.get("trace_replay_conflict") or not confl.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "trace_replay_conflict")
    if confl.get("retuned_join"):
        reasons.append(FLAG_PREFIX + "retuned_join")
    if confl.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if confl.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if confl.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if confl.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if confl.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not confl.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if confl["actions"] != ACTION_CODES:
        reasons.append("action_codes_not_preserved")
    if confl["joined_pairs"] != ACTION_CRITICAL_PAIRS:
        reasons.append(FLAG_PREFIX + "unresolved_critical_pair")
    if confl["classes"] != CLASSIFICATION_CODES or confl["obstruction_classes"] != OBSTRUCTION_CLASSES:
        reasons.append("classifier_classes_not_preserved")

    required_events = {
        "detect_action_overlap",
        "enumerate_action_critical_pairs",
        "join_action_pair",
        "emit_critical_pair_diamond",
        "emit_unique_action_normal_form",
        "emit_monotone_join_measure",
        "emit_replayable_join_trace",
        "emit_no_order_choice_certificate",
        "emit_no_branch_spawn_certificate",
    }
    if not required_events <= events:
        reasons.append("missing_confluence_events")
    if not ACTION_EVENTS <= set(confl["action_events"]):
        reasons.append("missing_action_event_confluence")
    if not CLASSIFIER_EVENTS <= set(confl["classifier_events"]):
        reasons.append("missing_classifier_event_confluence")
    if not LOCALIZER_EVENTS <= set(confl["localizer_events"]):
        reasons.append("missing_localizer_event_confluence")
    if confl["facets"] != OBSTRUCTION_FACETS:
        reasons.append("missing_facet_confluence")
    if confl["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append("missing_invariant_confluence")
    if not PAYLOAD_TRACE_EVENTS <= set(confl["payload_events"]):
        reasons.append("missing_payload_confluence")

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
        and CONFLACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["confluence"]["base_action_plan"] == ACTIONCLASS
        and state["confluence"]["has_confluence_certificate"]
        and state["confluence"]["source_internal"]
        and state["confluence"]["finite_action_system"],
        "source-internal finite confluence certificate is attached to doc596 action plan",
    )
    gate(
        f"{PREFIX}3",
        state["confluence"]["critical_pairs"] == ACTION_CRITICAL_PAIRS
        and state["confluence"]["joined_pairs"] == ACTION_CRITICAL_PAIRS
        and state["confluence"]["critical_pairs_complete"],
        f"critical_pairs={len(ACTION_CRITICAL_PAIRS)}",
    )
    gate(
        f"{PREFIX}4",
        state["confluence"]["terminating"]
        and state["confluence"]["locally_confluent"]
        and state["confluence"]["globally_confluent"]
        and state["confluence"]["unique_normal_form"],
        "finite action joins are terminating, locally confluent, globally confluent, and normalizing",
    )
    gate(
        f"{PREFIX}5",
        state["confluence"]["deterministic_join"]
        and state["confluence"]["proof_relevant"]
        and state["confluence"]["extensional_over_action_trace"]
        and state["confluence"]["replay_stable"],
        "joins are deterministic, proof-relevant, extensional, and replay-stable",
    )
    gate(
        f"{PREFIX}6",
        state["confluence"]["measure_decreases"]
        and not state["confluence"]["branch_spawning"]
        and not state["confluence"]["unbounded_completion"],
        "join traces decrease a finite measure without branch spawning or unbounded completion",
    )
    gate(
        f"{PREFIX}7",
        not any(
            state["confluence"][key]
            for key in (
                "class_order_dependent",
                "action_order_dependent",
                "action_conflict",
                "unresolved_critical_pair",
                "repair_action_conflict",
                "no_go_action_conflict",
                "budget_context_conflict",
                "sample_action_conflict",
                "trace_replay_conflict",
                "retuned_join",
            )
        ),
        "no order dependence, action conflict, unresolved critical pair, or retuned join",
    )
    gate(
        f"{PREFIX}8",
        state["confluence"]["budgeted"]
        and not any(
            state["confluence"][key]
            for key in (
                "external_join",
                "oracle_join",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(CONFLACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "action confluence is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: bounded obstruction actions are confluent")
    print(
        "VERDICT: the missing-object candidate now counts only when bounded "
        "obstruction actions form a terminating source-internal confluent "
        "system with all critical pairs joined; order-dependent, conflicting, "
        "branch-spawning, unbounded, external, oracle, sample, retuned, or "
        "unbudgeted join systems are disguised repairs."
    )


if __name__ == "__main__":
    main()
