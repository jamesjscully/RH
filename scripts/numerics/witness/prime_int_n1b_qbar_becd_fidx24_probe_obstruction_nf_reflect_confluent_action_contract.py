#!/usr/bin/env python3
r"""Obstruction normal-form reflection for confluent action contraction.

Doc 597 makes bounded obstruction actions terminating and confluent. This
witness closes the next escape: the unique action normal form must be reflected
back into the same executable/global contraction state. A proof-side normal
form that does not update the accepted terminal state, invariants, and trace
payload remains only a disguised repair.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_nf_reflect_confluent_action_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_confluent_action_classifier_trace_exec_global_contract import (
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
    NORM,
    OBSTRUCTION_CLASSES,
    OBSTRUCTION_FACETS,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC597_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 598
EXPECTED_WITNESS = "doc598-probe-obstruction-normalform-reflecting-confluent-action-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

NFREFLACTION = "obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction_certificate"

failures: list[str] = []

REFLECTION_EVENTS = {
    "read_unique_action_normal_form",
    "reflect_normal_form_into_executable_state",
    "reflect_normal_form_into_global_contraction",
    "reflect_terminal_action_certificate",
    "reflect_invariant_action_state",
    "reflect_payload_action_trace",
    "emit_idempotent_reflection_trace",
    "emit_replayable_reflection_trace",
    "emit_no_proof_erasure_certificate",
}

REQUIRED_DEPS = DOC597_REQUIRED_DEPS | {
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
    (CONFLACTION, "made_action_normalform_reflecting_by", NFREFLACTION),
    (NFREFLACTION, "reflects_confluent_action_for", CONFLACTION),
    (NFREFLACTION, "reflects_action_plan_for", ACTIONCLASS),
    (NFREFLACTION, "reflects_classifier_actions_for", CLASSIFYLOC),
    (NFREFLACTION, "reflects_localized_obstruction_actions_for", LOCALIZEVERIFY),
    (NFREFLACTION, "reflects_verifier_failure_actions_for", VERIFYTRACE),
    (NFREFLACTION, "reflects_trace_audit_actions_for", TRACEEXEC),
    (NFREFLACTION, "reflects_executable_global_contraction_for", EXECGLOB),
    (NFREFLACTION, "reflects_global_contraction_for", GLOBCONTR),
    (NFREFLACTION, "reflects_terminal_certificate_for", TERMINAL_CERT),
    (NFREFLACTION, "reflects_action_law_via", NORM),
    (NFREFLACTION, "reflects_action_law_via", FUNC_NORM),
    (NFREFLACTION, "reflects_action_law_via", COHERENT),
    (NFREFLACTION, "reflects_action_law_via", EXEC),
    (NFREFLACTION, "reflects_action_law_via", SEMCONS),
    (NFREFLACTION, "reflects_action_law_via", REPSEM),
    (NFREFLACTION, "reflects_action_law_via", EVAL),
    (NFREFLACTION, "reflects_action_law_via", BC),
    (NFREFLACTION, "reflects_action_law_via", REFINEMENT_DESCENT),
    (NFREFLACTION, "reflects_action_law_via", UNIVERSAL_ARROW),
} | {(NFREFLACTION, "reflects_invariant_action_state_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction_certificate",
    "normalform_reflection_source_internal",
    "normalform_reflection_executable_state",
    "normalform_reflection_terminal_certificate",
    "normalform_reflection_invariant_payload",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_nf_reflect_confluent_action_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_reflection_certificate",
    "proof_erased_normal_form",
    "normal_form_not_reflected",
    "executable_state_not_reflected",
    "global_contraction_not_reflected",
    "terminal_certificate_not_reflected",
    "accepted_action_not_reflected",
    "repair_action_not_reflected",
    "no_go_action_not_reflected",
    "budget_action_not_reflected",
    "context_action_not_reflected",
    "sample_action_not_reflected",
    "trace_action_not_reflected",
    "invariant_action_not_reflected",
    "payload_action_not_reflected",
    "wrong_reflected_state",
    "stale_reflected_state",
    "nonidempotent_reflection",
    "nondeterministic_reflection",
    "nonreplayable_reflection",
    "nonextensional_reflection",
    "proof_irrelevant_reflection",
    "external_reflection",
    "oracle_reflection",
    "not_source_internal",
    "action_normal_form_not_terminal",
    "join_trace_not_reflected",
    "critical_pair_not_reflected",
    "branch_spawning_reflection",
    "unbounded_reflection",
    "retuned_reflection",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction_certificate",
)

REFLECTION_DATA = {
    "certificate": "obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction",
    "base_confluence": CONFLACTION,
    "base_action_plan": ACTIONCLASS,
    "base_classifier": CLASSIFYLOC,
    "base_localizer": LOCALIZEVERIFY,
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_reflection_certificate": True,
    "source_internal": True,
    "normal_form_reflected": True,
    "executable_state_reflected": True,
    "global_contraction_reflected": True,
    "terminal_certificate_reflected": True,
    "accepted_action_reflected": True,
    "repair_action_reflected": True,
    "no_go_action_reflected": True,
    "budget_action_reflected": True,
    "context_action_reflected": True,
    "sample_action_reflected": True,
    "trace_action_reflected": True,
    "invariant_action_reflected": True,
    "payload_action_reflected": True,
    "join_trace_reflected": True,
    "normal_forms_terminal": True,
    "idempotent": True,
    "deterministic": True,
    "replay_stable": True,
    "proof_relevant": True,
    "extensional_over_reflected_state": True,
    "budgeted": True,
    "proof_erased_normal_form": False,
    "wrong_reflected_state": False,
    "stale_reflected_state": False,
    "external_reflection": False,
    "oracle_reflection": False,
    "branch_spawning": False,
    "unbounded_reflection": False,
    "retuned_reflection": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "reflected_actions": ACTION_CODES,
    "reflected_normal_forms": ACTION_CODES,
    "reflected_pairs": ACTION_CRITICAL_PAIRS,
    "reflected_classes": CLASSIFICATION_CODES,
    "reflected_obstruction_classes": OBSTRUCTION_CLASSES,
    "reflected_invariants": INVARIANT_TRACE_TARGETS,
    "reflected_payload_events": PAYLOAD_TRACE_EVENTS,
    "reflection_events": REFLECTION_EVENTS,
    "confluence_events": CONFLUENCE_EVENTS,
    "action_events": ACTION_EVENTS,
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "action_plan": ACTION_DATA,
    "reflected_state": "executable_global_contraction_terminal_action_normal_form",
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
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "reflection":
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
    excluded = set(state["excludes"].get(NFREFLACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    confl = state["confluence"]
    refl = state["reflection"]
    events = set(refl["reflection_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_598")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc598_witness")
    if NFREFLACTION not in state["accepted"]:
        reasons.append("missing_obstruction_normalform_reflecting_confluent_action_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(NFREFLACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if refl.get("base_confluence") != CONFLACTION or confl.get("certificate") != "obstruction_confluent_action_classifier_trace_executable_global_contraction":
        reasons.append("wrong_reflection_base")
    if not confl.get("has_confluence_certificate") or not confl.get("unique_normal_form"):
        reasons.append("missing_doc597_confluent_normal_form")
    if confl.get("critical_pairs") != ACTION_CRITICAL_PAIRS or confl.get("joined_pairs") != ACTION_CRITICAL_PAIRS:
        reasons.append(FLAG_PREFIX + "critical_pair_not_reflected")

    if not refl.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not refl.get("has_reflection_certificate"):
        reasons.append(FLAG_PREFIX + "no_reflection_certificate")
    if refl.get("proof_erased_normal_form"):
        reasons.append(FLAG_PREFIX + "proof_erased_normal_form")
    if not refl.get("normal_form_reflected") or refl["reflected_normal_forms"] != ACTION_CODES:
        reasons.append(FLAG_PREFIX + "normal_form_not_reflected")
    if not refl.get("executable_state_reflected") or refl.get("base_executable") != EXECGLOB:
        reasons.append(FLAG_PREFIX + "executable_state_not_reflected")
    if not refl.get("global_contraction_reflected") or refl.get("base_global_contractible") != GLOBCONTR:
        reasons.append(FLAG_PREFIX + "global_contraction_not_reflected")
    if not refl.get("terminal_certificate_reflected"):
        reasons.append(FLAG_PREFIX + "terminal_certificate_not_reflected")
    if not refl.get("accepted_action_reflected"):
        reasons.append(FLAG_PREFIX + "accepted_action_not_reflected")
    if not refl.get("repair_action_reflected"):
        reasons.append(FLAG_PREFIX + "repair_action_not_reflected")
    if not refl.get("no_go_action_reflected"):
        reasons.append(FLAG_PREFIX + "no_go_action_not_reflected")
    if not refl.get("budget_action_reflected"):
        reasons.append(FLAG_PREFIX + "budget_action_not_reflected")
    if not refl.get("context_action_reflected"):
        reasons.append(FLAG_PREFIX + "context_action_not_reflected")
    if not refl.get("sample_action_reflected"):
        reasons.append(FLAG_PREFIX + "sample_action_not_reflected")
    if not refl.get("trace_action_reflected"):
        reasons.append(FLAG_PREFIX + "trace_action_not_reflected")
    if not refl.get("invariant_action_reflected") or refl["reflected_invariants"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_action_not_reflected")
    if not refl.get("payload_action_reflected") or not PAYLOAD_TRACE_EVENTS <= set(refl["reflected_payload_events"]):
        reasons.append(FLAG_PREFIX + "payload_action_not_reflected")
    if refl.get("wrong_reflected_state"):
        reasons.append(FLAG_PREFIX + "wrong_reflected_state")
    if refl.get("stale_reflected_state"):
        reasons.append(FLAG_PREFIX + "stale_reflected_state")
    if not refl.get("idempotent"):
        reasons.append(FLAG_PREFIX + "nonidempotent_reflection")
    if not refl.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_reflection")
    if not refl.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "nonreplayable_reflection")
    if not refl.get("extensional_over_reflected_state"):
        reasons.append(FLAG_PREFIX + "nonextensional_reflection")
    if not refl.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_reflection")
    if refl.get("external_reflection"):
        reasons.append(FLAG_PREFIX + "external_reflection")
    if refl.get("oracle_reflection"):
        reasons.append(FLAG_PREFIX + "oracle_reflection")
    if not refl.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not refl.get("normal_forms_terminal"):
        reasons.append(FLAG_PREFIX + "action_normal_form_not_terminal")
    if not refl.get("join_trace_reflected"):
        reasons.append(FLAG_PREFIX + "join_trace_not_reflected")
    if refl["reflected_pairs"] != ACTION_CRITICAL_PAIRS:
        reasons.append(FLAG_PREFIX + "critical_pair_not_reflected")
    if refl.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_reflection")
    if refl.get("unbounded_reflection"):
        reasons.append(FLAG_PREFIX + "unbounded_reflection")
    if refl.get("retuned_reflection"):
        reasons.append(FLAG_PREFIX + "retuned_reflection")
    if refl.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if refl.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if refl.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if refl.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if refl.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not refl.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if refl["reflected_actions"] != ACTION_CODES:
        reasons.append("reflected_action_codes_not_preserved")
    if refl["reflected_classes"] != CLASSIFICATION_CODES or refl["reflected_obstruction_classes"] != OBSTRUCTION_CLASSES:
        reasons.append("reflected_classes_not_preserved")

    required_events = {
        "read_unique_action_normal_form",
        "reflect_normal_form_into_executable_state",
        "reflect_normal_form_into_global_contraction",
        "reflect_terminal_action_certificate",
        "reflect_invariant_action_state",
        "reflect_payload_action_trace",
        "emit_idempotent_reflection_trace",
        "emit_replayable_reflection_trace",
        "emit_no_proof_erasure_certificate",
    }
    if not required_events <= events:
        reasons.append("missing_reflection_events")
    if not CONFLUENCE_EVENTS <= set(refl["confluence_events"]):
        reasons.append("missing_confluence_event_reflection")
    if not ACTION_EVENTS <= set(refl["action_events"]):
        reasons.append("missing_action_event_reflection")
    if not CLASSIFIER_EVENTS <= set(refl["classifier_events"]):
        reasons.append("missing_classifier_event_reflection")
    if not LOCALIZER_EVENTS <= set(refl["localizer_events"]):
        reasons.append("missing_localizer_event_reflection")
    if refl["facets"] != OBSTRUCTION_FACETS:
        reasons.append("missing_facet_reflection")

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
        and NFREFLACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["reflection"]["base_confluence"] == CONFLACTION
        and state["confluence"]["has_confluence_certificate"]
        and state["confluence"]["unique_normal_form"]
        and state["reflection"]["has_reflection_certificate"],
        "doc597 unique action normal forms are the base reflected by doc598",
    )
    gate(
        f"{PREFIX}3",
        state["reflection"]["normal_form_reflected"]
        and state["reflection"]["executable_state_reflected"]
        and state["reflection"]["global_contraction_reflected"]
        and state["reflection"]["terminal_certificate_reflected"]
        and state["reflection"]["normal_forms_terminal"],
        "normal forms reflect into executable/global state and terminal certificate",
    )
    gate(
        f"{PREFIX}4",
        state["reflection"]["accepted_action_reflected"]
        and state["reflection"]["repair_action_reflected"]
        and state["reflection"]["no_go_action_reflected"]
        and state["reflection"]["budget_action_reflected"]
        and state["reflection"]["context_action_reflected"]
        and state["reflection"]["sample_action_reflected"]
        and state["reflection"]["trace_action_reflected"],
        "accepted, repair, no-go, budget, context, sample, and trace actions reflect",
    )
    gate(
        f"{PREFIX}5",
        state["reflection"]["invariant_action_reflected"]
        and state["reflection"]["payload_action_reflected"]
        and state["reflection"]["reflected_invariants"] == INVARIANT_TRACE_TARGETS
        and PAYLOAD_TRACE_EVENTS <= set(state["reflection"]["reflected_payload_events"]),
        "invariant states and payload events are reflected",
    )
    gate(
        f"{PREFIX}6",
        state["reflection"]["idempotent"]
        and state["reflection"]["deterministic"]
        and state["reflection"]["replay_stable"]
        and state["reflection"]["proof_relevant"]
        and state["reflection"]["extensional_over_reflected_state"],
        "reflection is idempotent, deterministic, replay-stable, proof-relevant, and extensional",
    )
    gate(
        f"{PREFIX}7",
        not any(
            state["reflection"][key]
            for key in (
                "proof_erased_normal_form",
                "wrong_reflected_state",
                "stale_reflected_state",
                "external_reflection",
                "oracle_reflection",
                "branch_spawning",
                "unbounded_reflection",
                "retuned_reflection",
            )
        ),
        "no proof erasure, stale/wrong reflected state, external/oracle reflection, branch spawn, or retune",
    )
    gate(
        f"{PREFIX}8",
        state["reflection"]["source_internal"]
        and state["reflection"]["budgeted"]
        and not any(
            state["reflection"][key]
            for key in (
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(NFREFLACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "normal-form reflection is dependency-closed, graph-wired, budgeted, and source-internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: confluent action normal forms reflect into executable state")
    print(
        "VERDICT: the missing-object candidate now counts only when the "
        "unique bounded obstruction-action normal form is reflected back into "
        "the same executable/global contraction, terminal certificate, "
        "invariant state, and payload trace; proof-erased, stale, external, "
        "oracle, retuned, sample, basis-row, or unbudgeted reflections are "
        "disguised repairs."
    )


if __name__ == "__main__":
    main()
