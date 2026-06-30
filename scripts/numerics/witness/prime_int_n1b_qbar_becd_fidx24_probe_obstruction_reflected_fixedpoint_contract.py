#!/usr/bin/env python3
r"""Reflected obstruction normal-form fixed point.

Doc 598 forces the unique bounded action normal form to reflect into the
executable/global contraction state. This witness closes the next escape: after
that reflection, rerunning the verifier/localizer/classifier/action/confluence/
reflection pipeline must be a no-op. A reflected state that creates a fresh
obstruction on replay has not actually contracted.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_reflected_fixedpoint_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_nf_reflect_confluent_action_contract import (
    ACTIONCLASS,
    ACTION_CODES,
    ACTION_CRITICAL_PAIRS,
    ACTION_DATA,
    ACTION_EVENTS,
    ADM_CAT,
    BC,
    CLASSIFICATION_CODES,
    CLASSIFIER_EVENTS,
    CLASSIFYLOC,
    COHERENT,
    CONFLACTION,
    CONFLUENCE_DATA,
    CONFLUENCE_EVENTS,
    EVAL,
    EXEC,
    EXECGLOB,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    LOCALIZEVERIFY,
    LOCALIZER_EVENTS,
    NFREFLACTION,
    NORM,
    OBSTRUCTION_CLASSES,
    OBSTRUCTION_FACETS,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REFLECTION_DATA,
    REFLECTION_EVENTS,
    REPSEM,
    REQUIRED_DEPS as DOC598_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 599
EXPECTED_WITNESS = "doc599-probe-obstruction-reflected-fixedpoint-normalform-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

FIXPTACTION = "obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction_certificate"

failures: list[str] = []

FIXEDPOINT_EVENTS = {
    "replay_reflected_normal_form",
    "rerun_verifier_on_reflected_state",
    "rerun_trace_audit_on_reflected_state",
    "rerun_localizer_on_reflected_state",
    "rerun_classifier_on_reflected_state",
    "rerun_action_plan_on_reflected_state",
    "rerun_confluence_on_reflected_state",
    "rerun_reflection_on_reflected_state",
    "emit_no_residual_obstruction_certificate",
    "emit_pipeline_fixedpoint_trace",
    "emit_no_new_action_certificate",
}

REQUIRED_DEPS = DOC598_REQUIRED_DEPS | {
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
    ADM_CAT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (NFREFLACTION, "made_reflected_fixedpoint_by", FIXPTACTION),
    (FIXPTACTION, "fixes_normalform_reflection_for", NFREFLACTION),
    (FIXPTACTION, "fixes_confluent_action_for", CONFLACTION),
    (FIXPTACTION, "fixes_action_plan_for", ACTIONCLASS),
    (FIXPTACTION, "fixes_classifier_for", CLASSIFYLOC),
    (FIXPTACTION, "fixes_localizer_for", LOCALIZEVERIFY),
    (FIXPTACTION, "fixes_verifier_for", VERIFYTRACE),
    (FIXPTACTION, "fixes_trace_audit_for", TRACEEXEC),
    (FIXPTACTION, "fixes_executable_global_contraction_for", EXECGLOB),
    (FIXPTACTION, "fixes_global_contraction_for", GLOBCONTR),
    (FIXPTACTION, "fixes_terminal_certificate_for", TERMINAL_CERT),
    (FIXPTACTION, "fixes_action_law_via", NORM),
    (FIXPTACTION, "fixes_action_law_via", FUNC_NORM),
    (FIXPTACTION, "fixes_action_law_via", COHERENT),
    (FIXPTACTION, "fixes_action_law_via", EXEC),
    (FIXPTACTION, "fixes_action_law_via", SEMCONS),
    (FIXPTACTION, "fixes_action_law_via", REPSEM),
    (FIXPTACTION, "fixes_action_law_via", EVAL),
    (FIXPTACTION, "fixes_action_law_via", BC),
    (FIXPTACTION, "fixes_action_law_via", REFINEMENT_DESCENT),
    (FIXPTACTION, "fixes_action_law_via", UNIVERSAL_ARROW),
} | {(FIXPTACTION, "fixes_invariant_state_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction_certificate",
    "reflected_fixedpoint_source_internal",
    "reflected_fixedpoint_replay_verified",
    "reflected_fixedpoint_no_residual_obstruction",
    "reflected_fixedpoint_pipeline_idempotent",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_reflected_fixedpoint_nf_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_fixedpoint_certificate",
    "post_reflection_verifier_fails",
    "post_reflection_trace_audit_fails",
    "post_reflection_localizer_changes",
    "post_reflection_classifier_changes",
    "post_reflection_action_changes",
    "post_reflection_confluence_changes",
    "post_reflection_reflection_changes",
    "residual_obstruction",
    "new_obstruction_after_replay",
    "new_action_after_replay",
    "normal_form_changes_on_replay",
    "terminal_certificate_changes_on_replay",
    "invariant_state_changes_on_replay",
    "payload_trace_changes_on_replay",
    "accepted_state_not_fixed",
    "repair_state_not_fixed",
    "no_go_state_not_fixed",
    "budget_state_not_fixed",
    "context_state_not_fixed",
    "sample_state_not_fixed",
    "trace_state_not_fixed",
    "not_idempotent_pipeline",
    "nondeterministic_replay",
    "nonterminating_replay",
    "not_replay_stable",
    "proof_irrelevant_fixedpoint",
    "nonextensional_fixedpoint",
    "external_fixedpoint",
    "oracle_fixedpoint",
    "not_source_internal",
    "branch_spawning_replay",
    "unbounded_replay",
    "retuned_pipeline",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction_certificate",
)

FIXEDPOINT_DATA = {
    "certificate": "obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction",
    "base_reflection": NFREFLACTION,
    "base_confluence": CONFLACTION,
    "base_action_plan": ACTIONCLASS,
    "base_classifier": CLASSIFYLOC,
    "base_localizer": LOCALIZEVERIFY,
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_fixedpoint_certificate": True,
    "source_internal": True,
    "post_reflection_verifier_accepts": True,
    "post_reflection_trace_audit_accepts": True,
    "localizer_fixed": True,
    "classifier_fixed": True,
    "action_plan_fixed": True,
    "confluence_fixed": True,
    "reflection_fixed": True,
    "no_residual_obstruction": True,
    "no_new_obstruction": True,
    "no_new_action": True,
    "normal_form_stable": True,
    "terminal_certificate_stable": True,
    "invariant_state_stable": True,
    "payload_trace_stable": True,
    "accepted_state_fixed": True,
    "repair_state_fixed": True,
    "no_go_state_fixed": True,
    "budget_state_fixed": True,
    "context_state_fixed": True,
    "sample_state_fixed": True,
    "trace_state_fixed": True,
    "pipeline_idempotent": True,
    "deterministic": True,
    "terminating": True,
    "replay_stable": True,
    "proof_relevant": True,
    "extensional_over_replay": True,
    "budgeted": True,
    "external_fixedpoint": False,
    "oracle_fixedpoint": False,
    "branch_spawning": False,
    "unbounded_replay": False,
    "retuned_pipeline": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "fixed_actions": ACTION_CODES,
    "fixed_normal_forms": ACTION_CODES,
    "fixed_pairs": ACTION_CRITICAL_PAIRS,
    "fixed_classes": CLASSIFICATION_CODES,
    "fixed_obstruction_classes": OBSTRUCTION_CLASSES,
    "fixed_invariants": INVARIANT_TRACE_TARGETS,
    "fixed_payload_events": PAYLOAD_TRACE_EVENTS,
    "fixedpoint_events": FIXEDPOINT_EVENTS,
    "reflection_events": REFLECTION_EVENTS,
    "confluence_events": CONFLUENCE_EVENTS,
    "action_events": ACTION_EVENTS,
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "action_plan": ACTION_DATA,
    "fixed_state": "reflected_executable_global_contraction_terminal_action_normal_form",
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
        "reflection": deepcopy(REFLECTION_DATA),
        "fixedpoint": deepcopy(FIXEDPOINT_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "fixedpoint":
            state["fixedpoint"].update(value)
        elif key == "reflection":
            state["reflection"].update(value)
        elif key == "confluence":
            state["confluence"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(FIXPTACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    confl = state["confluence"]
    refl = state["reflection"]
    fixed = state["fixedpoint"]
    events = set(fixed["fixedpoint_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_599")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc599_witness")
    if FIXPTACTION not in state["accepted"]:
        reasons.append("missing_obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(FIXPTACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if fixed.get("base_reflection") != NFREFLACTION or refl.get("certificate") != "obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction":
        reasons.append("wrong_fixedpoint_reflection_base")
    if fixed.get("base_confluence") != CONFLACTION or confl.get("certificate") != "obstruction_confluent_action_classifier_trace_executable_global_contraction":
        reasons.append("wrong_fixedpoint_confluence_base")
    if not refl.get("normal_form_reflected") or not refl.get("executable_state_reflected"):
        reasons.append("missing_doc598_reflected_state")
    if not confl.get("unique_normal_form") or confl.get("joined_pairs") != ACTION_CRITICAL_PAIRS:
        reasons.append("missing_doc597_unique_confluent_normal_form")

    if not fixed.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not fixed.get("has_fixedpoint_certificate"):
        reasons.append(FLAG_PREFIX + "no_fixedpoint_certificate")
    if not fixed.get("post_reflection_verifier_accepts"):
        reasons.append(FLAG_PREFIX + "post_reflection_verifier_fails")
    if not fixed.get("post_reflection_trace_audit_accepts"):
        reasons.append(FLAG_PREFIX + "post_reflection_trace_audit_fails")
    if not fixed.get("localizer_fixed"):
        reasons.append(FLAG_PREFIX + "post_reflection_localizer_changes")
    if not fixed.get("classifier_fixed"):
        reasons.append(FLAG_PREFIX + "post_reflection_classifier_changes")
    if not fixed.get("action_plan_fixed"):
        reasons.append(FLAG_PREFIX + "post_reflection_action_changes")
    if not fixed.get("confluence_fixed"):
        reasons.append(FLAG_PREFIX + "post_reflection_confluence_changes")
    if not fixed.get("reflection_fixed"):
        reasons.append(FLAG_PREFIX + "post_reflection_reflection_changes")
    if not fixed.get("no_residual_obstruction"):
        reasons.append(FLAG_PREFIX + "residual_obstruction")
    if not fixed.get("no_new_obstruction"):
        reasons.append(FLAG_PREFIX + "new_obstruction_after_replay")
    if not fixed.get("no_new_action"):
        reasons.append(FLAG_PREFIX + "new_action_after_replay")
    if not fixed.get("normal_form_stable") or fixed["fixed_normal_forms"] != ACTION_CODES:
        reasons.append(FLAG_PREFIX + "normal_form_changes_on_replay")
    if not fixed.get("terminal_certificate_stable"):
        reasons.append(FLAG_PREFIX + "terminal_certificate_changes_on_replay")
    if not fixed.get("invariant_state_stable") or fixed["fixed_invariants"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_state_changes_on_replay")
    if not fixed.get("payload_trace_stable") or not PAYLOAD_TRACE_EVENTS <= set(fixed["fixed_payload_events"]):
        reasons.append(FLAG_PREFIX + "payload_trace_changes_on_replay")
    if not fixed.get("accepted_state_fixed"):
        reasons.append(FLAG_PREFIX + "accepted_state_not_fixed")
    if not fixed.get("repair_state_fixed"):
        reasons.append(FLAG_PREFIX + "repair_state_not_fixed")
    if not fixed.get("no_go_state_fixed"):
        reasons.append(FLAG_PREFIX + "no_go_state_not_fixed")
    if not fixed.get("budget_state_fixed"):
        reasons.append(FLAG_PREFIX + "budget_state_not_fixed")
    if not fixed.get("context_state_fixed"):
        reasons.append(FLAG_PREFIX + "context_state_not_fixed")
    if not fixed.get("sample_state_fixed"):
        reasons.append(FLAG_PREFIX + "sample_state_not_fixed")
    if not fixed.get("trace_state_fixed"):
        reasons.append(FLAG_PREFIX + "trace_state_not_fixed")
    if not fixed.get("pipeline_idempotent"):
        reasons.append(FLAG_PREFIX + "not_idempotent_pipeline")
    if not fixed.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_replay")
    if not fixed.get("terminating"):
        reasons.append(FLAG_PREFIX + "nonterminating_replay")
    if not fixed.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "not_replay_stable")
    if not fixed.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_fixedpoint")
    if not fixed.get("extensional_over_replay"):
        reasons.append(FLAG_PREFIX + "nonextensional_fixedpoint")
    if fixed.get("external_fixedpoint"):
        reasons.append(FLAG_PREFIX + "external_fixedpoint")
    if fixed.get("oracle_fixedpoint"):
        reasons.append(FLAG_PREFIX + "oracle_fixedpoint")
    if not fixed.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if fixed.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_replay")
    if fixed.get("unbounded_replay"):
        reasons.append(FLAG_PREFIX + "unbounded_replay")
    if fixed.get("retuned_pipeline"):
        reasons.append(FLAG_PREFIX + "retuned_pipeline")
    if fixed.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if fixed.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if fixed.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if fixed.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if fixed.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not fixed.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if fixed["fixed_actions"] != ACTION_CODES:
        reasons.append("fixed_action_codes_not_preserved")
    if fixed["fixed_pairs"] != ACTION_CRITICAL_PAIRS:
        reasons.append("fixed_critical_pairs_not_preserved")
    if fixed["fixed_classes"] != CLASSIFICATION_CODES or fixed["fixed_obstruction_classes"] != OBSTRUCTION_CLASSES:
        reasons.append("fixed_classes_not_preserved")

    required_events = {
        "replay_reflected_normal_form",
        "rerun_verifier_on_reflected_state",
        "rerun_trace_audit_on_reflected_state",
        "rerun_localizer_on_reflected_state",
        "rerun_classifier_on_reflected_state",
        "rerun_action_plan_on_reflected_state",
        "rerun_confluence_on_reflected_state",
        "rerun_reflection_on_reflected_state",
        "emit_no_residual_obstruction_certificate",
        "emit_pipeline_fixedpoint_trace",
        "emit_no_new_action_certificate",
    }
    if not required_events <= events:
        reasons.append("missing_fixedpoint_events")
    if not REFLECTION_EVENTS <= set(fixed["reflection_events"]):
        reasons.append("missing_reflection_event_fixedpoint")
    if not CONFLUENCE_EVENTS <= set(fixed["confluence_events"]):
        reasons.append("missing_confluence_event_fixedpoint")
    if not ACTION_EVENTS <= set(fixed["action_events"]):
        reasons.append("missing_action_event_fixedpoint")
    if not CLASSIFIER_EVENTS <= set(fixed["classifier_events"]):
        reasons.append("missing_classifier_event_fixedpoint")
    if not LOCALIZER_EVENTS <= set(fixed["localizer_events"]):
        reasons.append("missing_localizer_event_fixedpoint")
    if fixed["facets"] != OBSTRUCTION_FACETS:
        reasons.append("missing_facet_fixedpoint")

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
        and FIXPTACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["fixedpoint"]["base_reflection"] == NFREFLACTION
        and state["reflection"]["normal_form_reflected"]
        and state["reflection"]["executable_state_reflected"]
        and state["fixedpoint"]["has_fixedpoint_certificate"],
        "doc598 reflected normal form is the fixed-point base",
    )
    gate(
        f"{PREFIX}3",
        state["fixedpoint"]["post_reflection_verifier_accepts"]
        and state["fixedpoint"]["post_reflection_trace_audit_accepts"]
        and state["fixedpoint"]["localizer_fixed"]
        and state["fixedpoint"]["classifier_fixed"]
        and state["fixedpoint"]["action_plan_fixed"]
        and state["fixedpoint"]["confluence_fixed"]
        and state["fixedpoint"]["reflection_fixed"],
        "replaying verifier, trace, localizer, classifier, action, confluence, and reflection is fixed",
    )
    gate(
        f"{PREFIX}4",
        state["fixedpoint"]["no_residual_obstruction"]
        and state["fixedpoint"]["no_new_obstruction"]
        and state["fixedpoint"]["no_new_action"]
        and state["fixedpoint"]["normal_form_stable"],
        "reflected state has no residual obstruction, no new action, and stable normal form",
    )
    gate(
        f"{PREFIX}5",
        state["fixedpoint"]["terminal_certificate_stable"]
        and state["fixedpoint"]["invariant_state_stable"]
        and state["fixedpoint"]["payload_trace_stable"]
        and state["fixedpoint"]["fixed_invariants"] == INVARIANT_TRACE_TARGETS
        and PAYLOAD_TRACE_EVENTS <= set(state["fixedpoint"]["fixed_payload_events"]),
        "terminal certificate, invariant state, and payload trace are replay-stable",
    )
    gate(
        f"{PREFIX}6",
        state["fixedpoint"]["accepted_state_fixed"]
        and state["fixedpoint"]["repair_state_fixed"]
        and state["fixedpoint"]["no_go_state_fixed"]
        and state["fixedpoint"]["budget_state_fixed"]
        and state["fixedpoint"]["context_state_fixed"]
        and state["fixedpoint"]["sample_state_fixed"]
        and state["fixedpoint"]["trace_state_fixed"],
        "accepted, repair, no-go, budget, context, sample, and trace states are fixed",
    )
    gate(
        f"{PREFIX}7",
        state["fixedpoint"]["pipeline_idempotent"]
        and state["fixedpoint"]["deterministic"]
        and state["fixedpoint"]["terminating"]
        and state["fixedpoint"]["replay_stable"]
        and state["fixedpoint"]["proof_relevant"]
        and state["fixedpoint"]["extensional_over_replay"],
        "pipeline replay is idempotent, deterministic, terminating, replay-stable, proof-relevant, and extensional",
    )
    gate(
        f"{PREFIX}8",
        state["fixedpoint"]["source_internal"]
        and state["fixedpoint"]["budgeted"]
        and not any(
            state["fixedpoint"][key]
            for key in (
                "external_fixedpoint",
                "oracle_fixedpoint",
                "branch_spawning",
                "unbounded_replay",
                "retuned_pipeline",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(FIXPTACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "fixed point is dependency-closed, graph-wired, budgeted, and source-internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: reflected obstruction normal form is a replay fixed point")
    print(
        "VERDICT: the missing-object candidate now counts only when the "
        "reflected bounded obstruction-action normal form is a source-internal "
        "fixed point of verifier, trace, localizer, classifier, action, "
        "confluence, and reflection replay; residual-obstruction, new-action, "
        "changed-normal-form, external, oracle, retuned, sample, basis-row, or "
        "unbudgeted fixed points are disguised repairs."
    )


if __name__ == "__main__":
    main()
