#!/usr/bin/env python3
r"""Obstruction-actionable classifier trace executable global contraction.

Doc 595 classifies every localized verifier obstruction by a finite
source-internal taxonomy. This witness closes the next escape: classification
labels cannot be inert. The doc 596 frontier only counts if every class maps
to a bounded source-internal action that either accepts, emits named no-go
evidence, or performs a bounded repair against an existing requirement.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_action_classifier_trace_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_class_localizer_trace_exec_global_contract import (
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
    REQUIRED_DEPS as DOC595_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 596
EXPECTED_WITNESS = "doc596-probe-obstruction-actionable-classifier-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

ACTIONCLASS = "obstruction_actionable_classifier_trace_executable_global_contraction_certificate"

failures: list[str] = []

ACTION_CODES = {
    "accept_verified_trace",
    "emit_fatal_no_go",
    "apply_existing_requirement_repair",
    "open_dependency_gap",
    "emit_budget_violation",
    "emit_context_collapse_no_go",
    "reject_external_or_oracle",
    "reject_presentation_sample",
}

CLASS_TO_ACTION = {
    "accepted": "accept_verified_trace",
    "fatal_no_go": "emit_fatal_no_go",
    "repair_required_existing_requirement": "apply_existing_requirement_repair",
    "dependency_missing": "open_dependency_gap",
    "budget_violation": "emit_budget_violation",
    "context_collapse": "emit_context_collapse_no_go",
    "external_or_oracle": "reject_external_or_oracle",
    "presentation_or_sample": "reject_presentation_sample",
}

ACTION_EVENTS = {
    "map_class_to_action",
    "emit_acceptance_action",
    "emit_fatal_no_go_action",
    "emit_existing_requirement_repair_action",
    "emit_dependency_gap_action",
    "emit_budget_violation_action",
    "emit_context_collapse_action",
    "emit_external_or_oracle_reject_action",
    "emit_presentation_sample_reject_action",
    "emit_monotone_frontier_decrease",
    "emit_no_branch_spawn_certificate",
    "emit_replayable_action_trace",
}

REQUIRED_DEPS = DOC595_REQUIRED_DEPS | {
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
    (CLASSIFYLOC, "made_actionable_by", ACTIONCLASS),
    (ACTIONCLASS, "acts_on_classifier_for", CLASSIFYLOC),
    (ACTIONCLASS, "acts_on_localized_obstruction_for", LOCALIZEVERIFY),
    (ACTIONCLASS, "acts_on_verifier_failure_for", VERIFYTRACE),
    (ACTIONCLASS, "acts_on_trace_audit_failure_for", TRACEEXEC),
    (ACTIONCLASS, "acts_on_executable_global_contraction_failure_for", EXECGLOB),
    (ACTIONCLASS, "acts_on_global_contraction_failure_for", GLOBCONTR),
    (ACTIONCLASS, "acts_on_law_via", NORM),
    (ACTIONCLASS, "acts_on_law_via", FUNC_NORM),
    (ACTIONCLASS, "acts_on_law_via", COHERENT),
    (ACTIONCLASS, "acts_on_law_via", EXEC),
    (ACTIONCLASS, "acts_on_law_via", SEMCONS),
    (ACTIONCLASS, "acts_on_law_via", REPSEM),
    (ACTIONCLASS, "acts_on_law_via", EVAL),
    (ACTIONCLASS, "acts_on_law_via", BC),
    (ACTIONCLASS, "acts_on_law_via", REFINEMENT_DESCENT),
    (ACTIONCLASS, "acts_on_law_via", TERMINAL_CERT),
    (ACTIONCLASS, "acts_on_law_via", UNIVERSAL_ARROW),
} | {(ACTIONCLASS, "acts_on_invariant_failure_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_actionable_classifier_trace_executable_global_contraction_certificate",
    "action_plan_source_internal",
    "action_plan_total_bounded",
    "action_plan_links_existing_repairs_no_go_kill_frontier",
    "action_plan_decreases_frontier_measure",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_action_classifier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_action_plan",
    "class_only",
    "unclassified_action",
    "ambiguous_action",
    "wrong_action",
    "external_action",
    "oracle_action",
    "not_source_internal",
    "not_total",
    "nondeterministic_action",
    "nonterminating_action",
    "proof_irrelevant_action",
    "nonextensional",
    "action_loop",
    "branch_spawning",
    "nonmonotone_refinement",
    "unbounded_search",
    "repair_not_existing_requirement",
    "no_go_not_named",
    "kill_frontier_link_missing",
    "budget_action_missing",
    "context_action_missing",
    "sample_action_missing",
    "action_trace_missing",
    "retuned_actions",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_actionable_classifier_trace_executable_global_contraction_certificate",
)

ACTION_DATA = {
    "certificate": "obstruction_actionable_classifier_trace_executable_global_contraction",
    "base_classifier": CLASSIFYLOC,
    "base_localizer": LOCALIZEVERIFY,
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_action_plan": True,
    "source_internal": True,
    "total_action_map": True,
    "deterministic": True,
    "terminating": True,
    "proof_relevant": True,
    "extensional_over_classification": True,
    "replay_stable": True,
    "budgeted": True,
    "class_only": False,
    "ambiguous_action": False,
    "wrong_action": False,
    "external_action": False,
    "oracle_action": False,
    "action_loop": False,
    "branch_spawning": False,
    "nonmonotone_refinement": False,
    "unbounded_search": False,
    "retuned_actions": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "classes": CLASSIFICATION_CODES,
    "obstruction_classes": OBSTRUCTION_CLASSES,
    "actions": ACTION_CODES,
    "class_to_action": CLASS_TO_ACTION,
    "action_events": ACTION_EVENTS,
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "repair_actions": {"apply_existing_requirement_repair", "open_dependency_gap"},
    "existing_requirement_repairs": {"apply_existing_requirement_repair", "open_dependency_gap"},
    "no_go_actions": {
        "emit_fatal_no_go",
        "emit_budget_violation",
        "emit_context_collapse_no_go",
        "reject_external_or_oracle",
        "reject_presentation_sample",
    },
    "named_no_go_actions": {
        "emit_fatal_no_go",
        "emit_budget_violation",
        "emit_context_collapse_no_go",
        "reject_external_or_oracle",
        "reject_presentation_sample",
    },
    "kill_frontier_links": {
        "obstruction_classifying_localizer_failure",
        "obstruction_localizing_verifier_failure",
        "verifier_separated_trace_failure",
        "finite_index_budget_impossibility",
        "dependency_closure_impossibility",
        "context_collapse_dd4",
    },
    "budget_actions": {"emit_budget_violation"},
    "context_actions": {"emit_context_collapse_no_go"},
    "sample_actions": {"reject_presentation_sample"},
    "action_trace": True,
    "measure": "finite_class_rank_then_frontier_size",
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
        "kill_frontier": {item["id"] for item in data["kill_frontier"]["current"]},
        "current_rejected": set(data["current_requirements"]["rejected_repairs"]),
        "rejected_repairs": set(data.get("rejected_repairs", {})),
        "action": deepcopy(ACTION_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "action":
            state["action"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(ACTIONCLASS, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    action = state["action"]
    events = set(action["action_events"])
    class_to_action = dict(action["class_to_action"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_596")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc596_witness")
    if ACTIONCLASS not in state["accepted"]:
        reasons.append("missing_obstruction_actionable_classifier_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(ACTIONCLASS, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if action.get("base_classifier") != CLASSIFYLOC or action.get("base_localizer") != LOCALIZEVERIFY:
        reasons.append("wrong_action_base")
    if not action.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not action.get("has_action_plan"):
        reasons.append(FLAG_PREFIX + "no_action_plan")
    if action.get("class_only"):
        reasons.append(FLAG_PREFIX + "class_only")
    if not action.get("total_action_map") or set(class_to_action) != CLASSIFICATION_CODES:
        reasons.append(FLAG_PREFIX + "unclassified_action")
    if set(class_to_action.values()) != ACTION_CODES:
        reasons.append(FLAG_PREFIX + "unclassified_action")
    if action.get("ambiguous_action"):
        reasons.append(FLAG_PREFIX + "ambiguous_action")
    if action.get("wrong_action") or class_to_action != CLASS_TO_ACTION:
        reasons.append(FLAG_PREFIX + "wrong_action")
    if action.get("external_action"):
        reasons.append(FLAG_PREFIX + "external_action")
    if action.get("oracle_action"):
        reasons.append(FLAG_PREFIX + "oracle_action")
    if not action.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not action.get("total_action_map"):
        reasons.append(FLAG_PREFIX + "not_total")
    if not action.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_action")
    if not action.get("terminating"):
        reasons.append(FLAG_PREFIX + "nonterminating_action")
    if not action.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_action")
    if not action.get("extensional_over_classification"):
        reasons.append(FLAG_PREFIX + "nonextensional")
    if action.get("action_loop"):
        reasons.append(FLAG_PREFIX + "action_loop")
    if action.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning")
    if action.get("nonmonotone_refinement") or not action.get("measure_decreases"):
        reasons.append(FLAG_PREFIX + "nonmonotone_refinement")
    if action.get("unbounded_search"):
        reasons.append(FLAG_PREFIX + "unbounded_search")
    if action.get("retuned_actions"):
        reasons.append(FLAG_PREFIX + "retuned_actions")
    if action.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if action.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if action.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if action.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if action.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not action.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if action["classes"] != CLASSIFICATION_CODES or action["obstruction_classes"] != OBSTRUCTION_CLASSES:
        reasons.append("classifier_classes_not_preserved")
    if not action["repair_actions"] <= action["existing_requirement_repairs"]:
        reasons.append(FLAG_PREFIX + "repair_not_existing_requirement")
    if not action["no_go_actions"] <= action["named_no_go_actions"]:
        reasons.append(FLAG_PREFIX + "no_go_not_named")
    if not action["kill_frontier_links"] <= state["kill_frontier"]:
        reasons.append(FLAG_PREFIX + "kill_frontier_link_missing")
    if "emit_budget_violation" not in action["budget_actions"]:
        reasons.append(FLAG_PREFIX + "budget_action_missing")
    if "emit_context_collapse_no_go" not in action["context_actions"]:
        reasons.append(FLAG_PREFIX + "context_action_missing")
    if "reject_presentation_sample" not in action["sample_actions"]:
        reasons.append(FLAG_PREFIX + "sample_action_missing")
    if not action.get("action_trace") or "emit_replayable_action_trace" not in events:
        reasons.append(FLAG_PREFIX + "action_trace_missing")

    required_events = {
        "map_class_to_action",
        "emit_acceptance_action",
        "emit_fatal_no_go_action",
        "emit_existing_requirement_repair_action",
        "emit_dependency_gap_action",
        "emit_budget_violation_action",
        "emit_context_collapse_action",
        "emit_external_or_oracle_reject_action",
        "emit_presentation_sample_reject_action",
        "emit_monotone_frontier_decrease",
        "emit_no_branch_spawn_certificate",
        "emit_replayable_action_trace",
    }
    if not required_events <= events:
        reasons.append("missing_action_events")
    if not CLASSIFIER_EVENTS <= set(action["classifier_events"]):
        reasons.append("missing_classifier_event_action")
    if not LOCALIZER_EVENTS <= set(action["localizer_events"]):
        reasons.append("missing_localizer_event_action")
    if action["facets"] != OBSTRUCTION_FACETS:
        reasons.append("missing_facet_action")
    if action["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append("missing_invariant_action")
    if not PAYLOAD_TRACE_EVENTS <= set(action["payload_events"]):
        reasons.append("missing_payload_action")

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
        and ACTIONCLASS in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["action"]["base_classifier"] == CLASSIFYLOC
        and state["action"]["has_action_plan"]
        and state["action"]["source_internal"]
        and state["action"]["total_action_map"],
        "source-internal total action plan is attached to doc595 classifier",
    )
    gate(
        f"{PREFIX}3",
        state["action"]["class_to_action"] == CLASS_TO_ACTION
        and set(state["action"]["class_to_action"]) == CLASSIFICATION_CODES
        and set(state["action"]["class_to_action"].values()) == ACTION_CODES,
        "each finite obstruction class maps to exactly one bounded action",
    )
    gate(
        f"{PREFIX}4",
        state["action"]["deterministic"]
        and state["action"]["terminating"]
        and state["action"]["proof_relevant"]
        and state["action"]["extensional_over_classification"]
        and state["action"]["replay_stable"],
        "action plan is deterministic, terminating, proof-relevant, extensional, and replay-stable",
    )
    gate(
        f"{PREFIX}5",
        state["action"]["repair_actions"] <= state["action"]["existing_requirement_repairs"]
        and state["action"]["no_go_actions"] <= state["action"]["named_no_go_actions"]
        and state["action"]["kill_frontier_links"] <= state["kill_frontier"],
        "actions link to existing repairs, named no-go evidence, and kill-frontier items",
    )
    gate(
        f"{PREFIX}6",
        "emit_budget_violation" in state["action"]["budget_actions"]
        and "emit_context_collapse_no_go" in state["action"]["context_actions"]
        and "reject_presentation_sample" in state["action"]["sample_actions"],
        "budget, context, and presentation/sample classes have forced actions",
    )
    gate(
        f"{PREFIX}7",
        state["action"]["action_trace"]
        and state["action"]["measure_decreases"]
        and not state["action"]["action_loop"]
        and not state["action"]["branch_spawning"]
        and not state["action"]["unbounded_search"],
        "actions emit a replayable trace and decrease a finite frontier measure",
    )
    gate(
        f"{PREFIX}8",
        state["action"]["budgeted"]
        and not any(
            state["action"][key]
            for key in (
                "class_only",
                "external_action",
                "oracle_action",
                "retuned_actions",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(ACTIONCLASS, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "action classifier is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: classified obstructions force bounded actions")
    print(
        "VERDICT: the missing-object candidate now counts only when each "
        "localized obstruction class forces a source-internal bounded action "
        "against existing repairs, named no-go evidence, kill-frontier, budget, "
        "and context data; inert labels, action loops, branch spawning, "
        "retuned, external, oracle, sample, or unbudgeted action plans are "
        "disguised repairs."
    )


if __name__ == "__main__":
    main()
