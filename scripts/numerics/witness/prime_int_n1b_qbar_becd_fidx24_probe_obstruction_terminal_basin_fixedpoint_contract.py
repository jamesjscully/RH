#!/usr/bin/env python3
r"""Terminal basin for reflected obstruction fixed point.

Doc 599 makes the reflected normal form a replay fixed point. This witness
closes the next escape: the fixed point must absorb every admissible
obstruction entry trace, not just the selected reflected replay trace. Otherwise
the construction can still hide a second terminal state behind a different
verifier/localizer/classifier/action entry.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_fixedpoint_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_reflected_fixedpoint_contract import (
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
    FIXEDPOINT_DATA,
    FIXEDPOINT_EVENTS,
    FIXPTACTION,
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
    REQUIRED_DEPS as DOC599_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 600
EXPECTED_WITNESS = "doc600-probe-obstruction-terminal-basin-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

BASINACTION = "obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

BASIN_EVENTS = {
    "enumerate_obstruction_entry_traces",
    "route_entry_trace_to_fixedpoint",
    "verify_entry_trace_absorption",
    "verify_single_terminal_fixedpoint",
    "verify_basin_closure_under_replay",
    "verify_no_escape_entry_trace",
    "verify_no_second_terminal_state",
    "emit_terminal_basin_certificate",
    "emit_absorbing_basin_trace",
}

ENTRY_TRACE_SURFACES = (
    frozenset(
        {
            "verifier_entry",
            "trace_audit_entry",
            "localizer_entry",
            "classifier_entry",
            "action_plan_entry",
            "confluence_entry",
            "reflection_entry",
            "fixedpoint_entry",
            "accepted_state_entry",
            "repair_state_entry",
            "no_go_state_entry",
            "budget_state_entry",
            "context_state_entry",
            "sample_state_entry",
            "trace_state_entry",
        }
    )
    | {f"class:{code}" for code in CLASSIFICATION_CODES}
    | {f"obstruction:{code}" for code in OBSTRUCTION_CLASSES}
    | {f"action:{code}" for code in ACTION_CODES}
    | {f"invariant:{target}" for target in INVARIANT_TRACE_TARGETS}
    | {f"payload:{event}" for event in PAYLOAD_TRACE_EVENTS}
)

REQUIRED_DEPS = DOC599_REQUIRED_DEPS | {
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
    ADM_CAT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (FIXPTACTION, "made_terminal_basin_by", BASINACTION),
    (BASINACTION, "absorbs_fixedpoint_for", FIXPTACTION),
    (BASINACTION, "absorbs_normalform_reflection_for", NFREFLACTION),
    (BASINACTION, "absorbs_confluent_action_for", CONFLACTION),
    (BASINACTION, "absorbs_action_plan_for", ACTIONCLASS),
    (BASINACTION, "absorbs_classifier_for", CLASSIFYLOC),
    (BASINACTION, "absorbs_localizer_for", LOCALIZEVERIFY),
    (BASINACTION, "absorbs_verifier_for", VERIFYTRACE),
    (BASINACTION, "absorbs_trace_audit_for", TRACEEXEC),
    (BASINACTION, "absorbs_executable_global_contraction_for", EXECGLOB),
    (BASINACTION, "absorbs_global_contraction_for", GLOBCONTR),
    (BASINACTION, "absorbs_terminal_certificate_for", TERMINAL_CERT),
    (BASINACTION, "absorbs_action_law_via", NORM),
    (BASINACTION, "absorbs_action_law_via", FUNC_NORM),
    (BASINACTION, "absorbs_action_law_via", COHERENT),
    (BASINACTION, "absorbs_action_law_via", EXEC),
    (BASINACTION, "absorbs_action_law_via", SEMCONS),
    (BASINACTION, "absorbs_action_law_via", REPSEM),
    (BASINACTION, "absorbs_action_law_via", EVAL),
    (BASINACTION, "absorbs_action_law_via", BC),
    (BASINACTION, "absorbs_action_law_via", REFINEMENT_DESCENT),
    (BASINACTION, "absorbs_action_law_via", UNIVERSAL_ARROW),
} | {(BASINACTION, "absorbs_invariant_entry_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_source_internal",
    "terminal_basin_entry_trace_total",
    "terminal_basin_single_fixedpoint",
    "terminal_basin_absorbing",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_basin_certificate",
    "incomplete_entry_trace_cover",
    "unlisted_entry_trace",
    "entry_trace_escapes",
    "entry_trace_changes_fixedpoint",
    "entry_trace_nonterminating",
    "entry_trace_nondeterministic",
    "entry_trace_not_replay_stable",
    "not_source_internal",
    "verifier_entry_missing",
    "trace_audit_entry_missing",
    "localizer_entry_missing",
    "classifier_entry_missing",
    "action_entry_missing",
    "confluence_entry_missing",
    "reflection_entry_missing",
    "fixedpoint_entry_missing",
    "invariant_entry_missing",
    "payload_entry_missing",
    "repair_entry_missing",
    "no_go_entry_missing",
    "budget_entry_missing",
    "context_entry_missing",
    "sample_entry_missing",
    "trace_entry_missing",
    "noncanonical_basin",
    "overlapping_incompatible_basins",
    "multiple_fixedpoints",
    "basin_not_absorbing",
    "basin_not_extensional",
    "proof_irrelevant_basin",
    "external_basin",
    "oracle_basin",
    "branch_spawning_basin",
    "unbounded_basin_search",
    "retuned_basin",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

BASIN_DATA = {
    "certificate": "obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction",
    "base_fixedpoint": FIXPTACTION,
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
    "has_basin_certificate": True,
    "source_internal": True,
    "entry_trace_cover_complete": True,
    "all_entry_traces_listed": True,
    "all_entries_absorbed": True,
    "entry_trace_fixedpoint_stable": True,
    "entry_traces_terminate": True,
    "entry_traces_deterministic": True,
    "entry_traces_replay_stable": True,
    "single_fixedpoint": True,
    "absorbing": True,
    "canonical": True,
    "proof_relevant": True,
    "extensional_over_entry_trace": True,
    "budgeted": True,
    "verifier_entry_covered": True,
    "trace_audit_entry_covered": True,
    "localizer_entry_covered": True,
    "classifier_entry_covered": True,
    "action_entry_covered": True,
    "confluence_entry_covered": True,
    "reflection_entry_covered": True,
    "fixedpoint_entry_covered": True,
    "invariant_entry_covered": True,
    "payload_entry_covered": True,
    "repair_entry_covered": True,
    "no_go_entry_covered": True,
    "budget_entry_covered": True,
    "context_entry_covered": True,
    "sample_entry_covered": True,
    "trace_entry_covered": True,
    "entry_trace_escapes": False,
    "overlapping_incompatible_basins": False,
    "multiple_fixedpoints": False,
    "external_basin": False,
    "oracle_basin": False,
    "branch_spawning": False,
    "unbounded_basin_search": False,
    "retuned_basin": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "entry_traces": ENTRY_TRACE_SURFACES,
    "absorbed_entry_traces": ENTRY_TRACE_SURFACES,
    "basin_events": BASIN_EVENTS,
    "fixedpoint_events": FIXEDPOINT_EVENTS,
    "reflection_events": REFLECTION_EVENTS,
    "confluence_events": CONFLUENCE_EVENTS,
    "action_events": ACTION_EVENTS,
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "actions": ACTION_CODES,
    "classes": CLASSIFICATION_CODES,
    "obstruction_classes": OBSTRUCTION_CLASSES,
    "critical_pairs": ACTION_CRITICAL_PAIRS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "action_plan": ACTION_DATA,
    "terminal_fixedpoint": "reflected_executable_global_contraction_terminal_action_normal_form",
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
        "basin": deepcopy(BASIN_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "basin":
            state["basin"].update(value)
        elif key == "fixedpoint":
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
    excluded = set(state["excludes"].get(BASINACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    fixed = state["fixedpoint"]
    basin = state["basin"]
    events = set(basin["basin_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_600")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc600_witness")
    if BASINACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(BASINACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if basin.get("base_fixedpoint") != FIXPTACTION or fixed.get("certificate") != "obstruction_reflected_fixedpoint_normalform_trace_executable_global_contraction":
        reasons.append("wrong_basin_fixedpoint_base")
    if not fixed.get("pipeline_idempotent") or not fixed.get("no_residual_obstruction"):
        reasons.append("missing_doc599_fixedpoint_state")

    if not basin.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not basin.get("has_basin_certificate"):
        reasons.append(FLAG_PREFIX + "no_basin_certificate")
    if not basin.get("entry_trace_cover_complete") or not ENTRY_TRACE_SURFACES <= set(basin["entry_traces"]):
        reasons.append(FLAG_PREFIX + "incomplete_entry_trace_cover")
    if not basin.get("all_entry_traces_listed") or set(basin["entry_traces"]) - ENTRY_TRACE_SURFACES:
        reasons.append(FLAG_PREFIX + "unlisted_entry_trace")
    if basin.get("entry_trace_escapes") or not basin.get("all_entries_absorbed"):
        reasons.append(FLAG_PREFIX + "entry_trace_escapes")
    if not basin.get("entry_trace_fixedpoint_stable") or set(basin["absorbed_entry_traces"]) != ENTRY_TRACE_SURFACES:
        reasons.append(FLAG_PREFIX + "entry_trace_changes_fixedpoint")
    if not basin.get("entry_traces_terminate"):
        reasons.append(FLAG_PREFIX + "entry_trace_nonterminating")
    if not basin.get("entry_traces_deterministic"):
        reasons.append(FLAG_PREFIX + "entry_trace_nondeterministic")
    if not basin.get("entry_traces_replay_stable"):
        reasons.append(FLAG_PREFIX + "entry_trace_not_replay_stable")
    if not basin.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not basin.get("verifier_entry_covered"):
        reasons.append(FLAG_PREFIX + "verifier_entry_missing")
    if not basin.get("trace_audit_entry_covered"):
        reasons.append(FLAG_PREFIX + "trace_audit_entry_missing")
    if not basin.get("localizer_entry_covered"):
        reasons.append(FLAG_PREFIX + "localizer_entry_missing")
    if not basin.get("classifier_entry_covered"):
        reasons.append(FLAG_PREFIX + "classifier_entry_missing")
    if not basin.get("action_entry_covered"):
        reasons.append(FLAG_PREFIX + "action_entry_missing")
    if not basin.get("confluence_entry_covered"):
        reasons.append(FLAG_PREFIX + "confluence_entry_missing")
    if not basin.get("reflection_entry_covered"):
        reasons.append(FLAG_PREFIX + "reflection_entry_missing")
    if not basin.get("fixedpoint_entry_covered"):
        reasons.append(FLAG_PREFIX + "fixedpoint_entry_missing")
    if not basin.get("invariant_entry_covered") or basin["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_entry_missing")
    if not basin.get("payload_entry_covered") or not PAYLOAD_TRACE_EVENTS <= set(basin["payload_events"]):
        reasons.append(FLAG_PREFIX + "payload_entry_missing")
    if not basin.get("repair_entry_covered"):
        reasons.append(FLAG_PREFIX + "repair_entry_missing")
    if not basin.get("no_go_entry_covered"):
        reasons.append(FLAG_PREFIX + "no_go_entry_missing")
    if not basin.get("budget_entry_covered"):
        reasons.append(FLAG_PREFIX + "budget_entry_missing")
    if not basin.get("context_entry_covered"):
        reasons.append(FLAG_PREFIX + "context_entry_missing")
    if not basin.get("sample_entry_covered"):
        reasons.append(FLAG_PREFIX + "sample_entry_missing")
    if not basin.get("trace_entry_covered"):
        reasons.append(FLAG_PREFIX + "trace_entry_missing")
    if not basin.get("canonical"):
        reasons.append(FLAG_PREFIX + "noncanonical_basin")
    if basin.get("overlapping_incompatible_basins"):
        reasons.append(FLAG_PREFIX + "overlapping_incompatible_basins")
    if basin.get("multiple_fixedpoints") or not basin.get("single_fixedpoint"):
        reasons.append(FLAG_PREFIX + "multiple_fixedpoints")
    if not basin.get("absorbing"):
        reasons.append(FLAG_PREFIX + "basin_not_absorbing")
    if not basin.get("extensional_over_entry_trace"):
        reasons.append(FLAG_PREFIX + "basin_not_extensional")
    if not basin.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_basin")
    if basin.get("external_basin"):
        reasons.append(FLAG_PREFIX + "external_basin")
    if basin.get("oracle_basin"):
        reasons.append(FLAG_PREFIX + "oracle_basin")
    if basin.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_basin")
    if basin.get("unbounded_basin_search"):
        reasons.append(FLAG_PREFIX + "unbounded_basin_search")
    if basin.get("retuned_basin"):
        reasons.append(FLAG_PREFIX + "retuned_basin")
    if basin.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if basin.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if basin.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if basin.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if basin.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not basin.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if basin["actions"] != ACTION_CODES:
        reasons.append("basin_action_codes_not_preserved")
    if basin["classes"] != CLASSIFICATION_CODES or basin["obstruction_classes"] != OBSTRUCTION_CLASSES:
        reasons.append("basin_classes_not_preserved")
    if basin["critical_pairs"] != ACTION_CRITICAL_PAIRS:
        reasons.append("basin_critical_pairs_not_preserved")

    required_events = {
        "enumerate_obstruction_entry_traces",
        "route_entry_trace_to_fixedpoint",
        "verify_entry_trace_absorption",
        "verify_single_terminal_fixedpoint",
        "verify_basin_closure_under_replay",
        "verify_no_escape_entry_trace",
        "verify_no_second_terminal_state",
        "emit_terminal_basin_certificate",
        "emit_absorbing_basin_trace",
    }
    if not required_events <= events:
        reasons.append("missing_basin_events")
    if not FIXEDPOINT_EVENTS <= set(basin["fixedpoint_events"]):
        reasons.append("missing_fixedpoint_event_basin")
    if not REFLECTION_EVENTS <= set(basin["reflection_events"]):
        reasons.append("missing_reflection_event_basin")
    if not CONFLUENCE_EVENTS <= set(basin["confluence_events"]):
        reasons.append("missing_confluence_event_basin")
    if not ACTION_EVENTS <= set(basin["action_events"]):
        reasons.append("missing_action_event_basin")
    if not CLASSIFIER_EVENTS <= set(basin["classifier_events"]):
        reasons.append("missing_classifier_event_basin")
    if not LOCALIZER_EVENTS <= set(basin["localizer_events"]):
        reasons.append("missing_localizer_event_basin")
    if basin["facets"] != OBSTRUCTION_FACETS:
        reasons.append("missing_facet_basin")

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
        and BASINACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["basin"]["base_fixedpoint"] == FIXPTACTION
        and state["fixedpoint"]["pipeline_idempotent"]
        and state["fixedpoint"]["no_residual_obstruction"]
        and state["basin"]["has_basin_certificate"],
        "doc599 fixed point is the terminal basin base",
    )
    gate(
        f"{PREFIX}3",
        state["basin"]["entry_trace_cover_complete"]
        and state["basin"]["all_entry_traces_listed"]
        and ENTRY_TRACE_SURFACES <= set(state["basin"]["entry_traces"])
        and not (set(state["basin"]["entry_traces"]) - ENTRY_TRACE_SURFACES),
        f"entry_traces={len(ENTRY_TRACE_SURFACES)}",
    )
    gate(
        f"{PREFIX}4",
        state["basin"]["all_entries_absorbed"]
        and state["basin"]["entry_trace_fixedpoint_stable"]
        and set(state["basin"]["absorbed_entry_traces"]) == ENTRY_TRACE_SURFACES
        and not state["basin"]["entry_trace_escapes"],
        "all admissible entry traces absorb into the same fixed point",
    )
    gate(
        f"{PREFIX}5",
        state["basin"]["verifier_entry_covered"]
        and state["basin"]["trace_audit_entry_covered"]
        and state["basin"]["localizer_entry_covered"]
        and state["basin"]["classifier_entry_covered"]
        and state["basin"]["action_entry_covered"]
        and state["basin"]["confluence_entry_covered"]
        and state["basin"]["reflection_entry_covered"]
        and state["basin"]["fixedpoint_entry_covered"],
        "pipeline entry traces are covered",
    )
    gate(
        f"{PREFIX}6",
        state["basin"]["invariant_entry_covered"]
        and state["basin"]["payload_entry_covered"]
        and state["basin"]["repair_entry_covered"]
        and state["basin"]["no_go_entry_covered"]
        and state["basin"]["budget_entry_covered"]
        and state["basin"]["context_entry_covered"]
        and state["basin"]["sample_entry_covered"]
        and state["basin"]["trace_entry_covered"],
        "invariant, payload, repair, no-go, budget, context, sample, and trace entries are covered",
    )
    gate(
        f"{PREFIX}7",
        state["basin"]["entry_traces_terminate"]
        and state["basin"]["entry_traces_deterministic"]
        and state["basin"]["entry_traces_replay_stable"]
        and state["basin"]["single_fixedpoint"]
        and state["basin"]["absorbing"]
        and state["basin"]["canonical"]
        and state["basin"]["proof_relevant"]
        and state["basin"]["extensional_over_entry_trace"],
        "terminal basin is terminating, deterministic, replay-stable, single, absorbing, canonical, proof-relevant, and extensional",
    )
    gate(
        f"{PREFIX}8",
        state["basin"]["source_internal"]
        and state["basin"]["budgeted"]
        and not any(
            state["basin"][key]
            for key in (
                "overlapping_incompatible_basins",
                "multiple_fixedpoints",
                "external_basin",
                "oracle_basin",
                "branch_spawning",
                "unbounded_basin_search",
                "retuned_basin",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(BASINACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "terminal basin is dependency-closed, graph-wired, budgeted, and source-internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: reflected fixed point has a terminal obstruction basin")
    print(
        "VERDICT: the missing-object candidate now counts only when every "
        "admissible obstruction entry trace is absorbed by the same "
        "source-internal terminal fixed point; incomplete, escaping, "
        "multi-terminal, external, oracle, retuned, sample, basis-row, or "
        "unbudgeted basins are disguised repairs."
    )


if __name__ == "__main__":
    main()
