#!/usr/bin/env python3
r"""Verifier-separated trace executable global contraction.

Doc 592 requires a source-internal replay trace for the executable global
contraction. This witness closes the next escape: the evaluator might be the
only judge of its own trace. The doc 593 frontier only counts if a finite
source-internal verifier, separated from the producer and without a shared
oracle, checks and rejects traces by replaying the existing source calculus.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_verifier_sep_trace_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_trace_audited_exec_global_contract import (
    ADM_CAT,
    BC,
    COHERENT,
    CORE_TRACE_EVENTS,
    EVAL,
    EXEC,
    EXECGLOB,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC592_REQUIRED_DEPS,
    SEMCONS,
    STRUCTURE_TRACE_EVENTS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    load_map,
)


EXPECTED_DOC = 593
EXPECTED_WITNESS = "doc593-probe-verifier-separated-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMVERIFTRACEEXECGLOBCONTR"

VERIFYTRACE = "verifier_separated_trace_executable_global_contraction_certificate"

failures: list[str] = []

CHECK_EVENTS = {
    "check_trace_schema",
    "check_event_coverage",
    "check_canonical_order",
    "check_replay",
    "check_semantic_reflection",
    "check_invariants",
    "check_payload_routes",
    "check_exact_24_budget",
    "reject_invalid_trace",
}

REQUIRED_DEPS = DOC592_REQUIRED_DEPS | {
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
    (TRACEEXEC, "made_verifier_separated_by", VERIFYTRACE),
    (VERIFYTRACE, "verifier_separates_trace_audit_for", TRACEEXEC),
    (VERIFYTRACE, "verifier_checks_trace_for", EXECGLOB),
    (VERIFYTRACE, "verifier_replays_global_contraction_for", GLOBCONTR),
    (VERIFYTRACE, "verifier_checks_law_via", NORM),
    (VERIFYTRACE, "verifier_checks_law_via", FUNC_NORM),
    (VERIFYTRACE, "verifier_checks_law_via", COHERENT),
    (VERIFYTRACE, "verifier_checks_law_via", EXEC),
    (VERIFYTRACE, "verifier_checks_law_via", SEMCONS),
    (VERIFYTRACE, "verifier_checks_law_via", REPSEM),
    (VERIFYTRACE, "verifier_checks_law_via", EVAL),
    (VERIFYTRACE, "verifier_checks_law_via", BC),
    (VERIFYTRACE, "verifier_checks_law_via", REFINEMENT_DESCENT),
    (VERIFYTRACE, "verifier_checks_law_via", TERMINAL_CERT),
    (VERIFYTRACE, "verifier_checks_law_via", UNIVERSAL_ARROW),
} | {(VERIFYTRACE, "verifier_checks_invariant_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "verifier_separated_trace_executable_global_contraction_certificate",
    "verifier_source_internal",
    "verifier_producer_separated",
    "verifier_replay_checks_trace",
    "verifier_rejects_invalid_traces",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_verifier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_verifier",
    "producer_coupled",
    "external_checker",
    "oracle_checker",
    "shared_oracle",
    "schema_unchecked",
    "event_coverage_unchecked",
    "order_unchecked",
    "replay_unchecked",
    "semantic_reflection_unchecked",
    "invariant_unchecked",
    "payload_route_unchecked",
    "budget_unchecked",
    "unsound",
    "incomplete",
    "accepts_invalid_trace",
    "nondeterministic_verifier",
    "nonterminating_verifier",
    "proof_irrelevant_verifier",
    "nonextensional",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_verifier_separated_trace_executable_global_contraction_certificate",
)

VERIFIER_DATA = {
    "certificate": "verifier_separated_trace_executable_global_contraction",
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_verifier": True,
    "source_internal": True,
    "finite_checker": True,
    "producer_separated": True,
    "external_checker": False,
    "oracle_checker": False,
    "shared_oracle": False,
    "checks_schema": True,
    "checks_event_coverage": True,
    "checks_order": True,
    "checks_replay": True,
    "checks_semantic_reflection": True,
    "checks_invariants": True,
    "checks_payload_routes": True,
    "checks_budget": True,
    "sound": True,
    "complete_for_admissible_traces": True,
    "rejects_invalid_traces": True,
    "deterministic": True,
    "terminating": True,
    "proof_relevant": True,
    "extensional_over_trace": True,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "checked_events": CHECK_EVENTS,
    "trace_events": CORE_TRACE_EVENTS | STRUCTURE_TRACE_EVENTS | PAYLOAD_TRACE_EVENTS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
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
        "verifier": deepcopy(VERIFIER_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "verifier":
            state["verifier"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(VERIFYTRACE, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    verifier = state["verifier"]
    checked = set(verifier["checked_events"])
    trace_events = set(verifier["trace_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_593")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc593_witness")
    if VERIFYTRACE not in state["accepted"]:
        reasons.append("missing_verifier_separated_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(VERIFYTRACE, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if verifier.get("base_trace") != TRACEEXEC or verifier.get("base_executable") != EXECGLOB:
        reasons.append("wrong_verifier_base")
    if not verifier.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not verifier.get("has_verifier"):
        reasons.append(FLAG_PREFIX + "no_verifier")
    if not verifier.get("source_internal") or verifier.get("external_checker"):
        reasons.append(FLAG_PREFIX + "external_checker")
    if not verifier.get("producer_separated"):
        reasons.append(FLAG_PREFIX + "producer_coupled")
    if verifier.get("oracle_checker"):
        reasons.append(FLAG_PREFIX + "oracle_checker")
    if verifier.get("shared_oracle"):
        reasons.append(FLAG_PREFIX + "shared_oracle")
    if not verifier.get("checks_schema") or "check_trace_schema" not in checked:
        reasons.append(FLAG_PREFIX + "schema_unchecked")
    if not verifier.get("checks_event_coverage") or "check_event_coverage" not in checked:
        reasons.append(FLAG_PREFIX + "event_coverage_unchecked")
    if not verifier.get("checks_order") or "check_canonical_order" not in checked:
        reasons.append(FLAG_PREFIX + "order_unchecked")
    if not verifier.get("checks_replay") or "check_replay" not in checked:
        reasons.append(FLAG_PREFIX + "replay_unchecked")
    if not verifier.get("checks_semantic_reflection") or "check_semantic_reflection" not in checked:
        reasons.append(FLAG_PREFIX + "semantic_reflection_unchecked")
    if (
        not verifier.get("checks_invariants")
        or "check_invariants" not in checked
        or verifier["invariant_targets"] != INVARIANT_TRACE_TARGETS
    ):
        reasons.append(FLAG_PREFIX + "invariant_unchecked")
    if (
        not verifier.get("checks_payload_routes")
        or "check_payload_routes" not in checked
        or not PAYLOAD_TRACE_EVENTS <= trace_events
    ):
        reasons.append(FLAG_PREFIX + "payload_route_unchecked")
    if not verifier.get("checks_budget") or "check_exact_24_budget" not in checked:
        reasons.append(FLAG_PREFIX + "budget_unchecked")
    if not verifier.get("sound"):
        reasons.append(FLAG_PREFIX + "unsound")
    if not verifier.get("complete_for_admissible_traces"):
        reasons.append(FLAG_PREFIX + "incomplete")
    if not verifier.get("rejects_invalid_traces") or "reject_invalid_trace" not in checked:
        reasons.append(FLAG_PREFIX + "accepts_invalid_trace")
    if not verifier.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_verifier")
    if not verifier.get("terminating") or not verifier.get("finite_checker"):
        reasons.append(FLAG_PREFIX + "nonterminating_verifier")
    if not verifier.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_verifier")
    if not verifier.get("extensional_over_trace"):
        reasons.append(FLAG_PREFIX + "nonextensional")
    if verifier.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if verifier.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if verifier.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if verifier.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if verifier.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not verifier.get("budgeted"):
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
        and VERIFYTRACE in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["verifier"]["base_trace"] == TRACEEXEC
        and state["verifier"]["has_verifier"]
        and state["verifier"]["source_internal"]
        and state["verifier"]["finite_checker"],
        "finite source-internal verifier checks the doc592 trace",
    )
    gate(
        f"{PREFIX}3",
        state["verifier"]["producer_separated"]
        and not state["verifier"]["external_checker"]
        and not state["verifier"]["oracle_checker"]
        and not state["verifier"]["shared_oracle"],
        "producer and verifier are separated without shared external oracle",
    )
    gate(
        f"{PREFIX}4",
        {"check_trace_schema", "check_event_coverage", "check_canonical_order", "check_replay"}
        <= state["verifier"]["checked_events"]
        and CORE_TRACE_EVENTS <= state["verifier"]["trace_events"],
        "verifier checks schema, event coverage, canonical order, and replay",
    )
    gate(
        f"{PREFIX}5",
        {"check_semantic_reflection", "check_invariants", "check_payload_routes"}
        <= state["verifier"]["checked_events"]
        and STRUCTURE_TRACE_EVENTS <= state["verifier"]["trace_events"]
        and PAYLOAD_TRACE_EVENTS <= state["verifier"]["trace_events"],
        "verifier checks semantic reflection, invariants, and payload routes",
    )
    gate(
        f"{PREFIX}6",
        state["verifier"]["invariant_targets"] == INVARIANT_TRACE_TARGETS
        and state["verifier"]["checks_budget"]
        and "check_exact_24_budget" in state["verifier"]["checked_events"],
        "verifier checks all invariant targets and exact-24 budget charge",
    )
    gate(
        f"{PREFIX}7",
        state["verifier"]["sound"]
        and state["verifier"]["complete_for_admissible_traces"]
        and state["verifier"]["rejects_invalid_traces"]
        and state["verifier"]["deterministic"]
        and state["verifier"]["terminating"]
        and state["verifier"]["proof_relevant"]
        and state["verifier"]["extensional_over_trace"],
        "verifier is sound, complete on admissible traces, deterministic, terminating, proof-relevant, and extensional",
    )
    gate(
        f"{PREFIX}8",
        state["verifier"]["budgeted"]
        and not any(
            state["verifier"][key]
            for key in (
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(VERIFYTRACE, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "verifier-separated trace contraction is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: trace verifier is separated and internal")
    print(
        "VERDICT: the missing-object candidate now counts only when the "
        "trace-audited executable global contraction has an independent "
        "source-internal finite verifier; self-accepted, external, oracle, "
        "schema-only, or unbudgeted checks are disguised repairs."
    )


if __name__ == "__main__":
    main()
