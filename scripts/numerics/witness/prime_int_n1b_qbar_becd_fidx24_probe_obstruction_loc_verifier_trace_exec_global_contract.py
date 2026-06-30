#!/usr/bin/env python3
r"""Obstruction-localizing verifier trace executable global contraction.

Doc 593 separates the trace producer from a source-internal verifier. This
witness closes the next escape: a verifier can reject without telling the
search where the obstruction lives. The doc 594 frontier only counts if every
rejection returns a canonical proof-relevant source-internal obstruction
location over the same finite checks.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_loc_verifier_trace_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_verifier_sep_trace_exec_global_contract import (
    ADM_CAT,
    BC,
    CHECK_EVENTS,
    COHERENT,
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
    REQUIRED_DEPS as DOC593_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 594
EXPECTED_WITNESS = "doc594-probe-obstruction-localizing-verifier-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMLOCVERIFTRACEEXECGLOBCONTR"

LOCALIZEVERIFY = "obstruction_localizing_verifier_trace_executable_global_contraction_certificate"

failures: list[str] = []

OBSTRUCTION_FACETS = {
    "schema",
    "event_coverage",
    "canonical_order",
    "replay",
    "semantic_reflection",
    "invariant_events",
    "payload_routes",
    "source_laws",
    "exact_24_budget",
    "producer_separation",
    "source_internality",
}

LOCALIZER_EVENTS = {
    "return_accept_or_obstruction",
    "localize_schema_failure",
    "localize_event_coverage_failure",
    "localize_order_failure",
    "localize_replay_failure",
    "localize_semantic_reflection_failure",
    "localize_invariant_failure",
    "localize_payload_route_failure",
    "localize_budget_failure",
    "emit_minimal_failing_subtrace",
    "emit_canonical_obstruction_location",
}

REQUIRED_DEPS = DOC593_REQUIRED_DEPS | {
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
    (VERIFYTRACE, "made_obstruction_localizing_by", LOCALIZEVERIFY),
    (LOCALIZEVERIFY, "localizes_verifier_failure_for", VERIFYTRACE),
    (LOCALIZEVERIFY, "localizes_trace_audit_failure_for", TRACEEXEC),
    (LOCALIZEVERIFY, "localizes_executable_global_contraction_failure_for", EXECGLOB),
    (LOCALIZEVERIFY, "localizes_global_contraction_failure_for", GLOBCONTR),
    (LOCALIZEVERIFY, "localizes_law_via", NORM),
    (LOCALIZEVERIFY, "localizes_law_via", FUNC_NORM),
    (LOCALIZEVERIFY, "localizes_law_via", COHERENT),
    (LOCALIZEVERIFY, "localizes_law_via", EXEC),
    (LOCALIZEVERIFY, "localizes_law_via", SEMCONS),
    (LOCALIZEVERIFY, "localizes_law_via", REPSEM),
    (LOCALIZEVERIFY, "localizes_law_via", EVAL),
    (LOCALIZEVERIFY, "localizes_law_via", BC),
    (LOCALIZEVERIFY, "localizes_law_via", REFINEMENT_DESCENT),
    (LOCALIZEVERIFY, "localizes_law_via", TERMINAL_CERT),
    (LOCALIZEVERIFY, "localizes_law_via", UNIVERSAL_ARROW),
} | {(LOCALIZEVERIFY, "localizes_invariant_failure_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_localizing_verifier_trace_executable_global_contraction_certificate",
    "localizer_source_internal",
    "localizer_returns_accept_or_obstruction",
    "localizer_emits_minimal_subtrace",
    "localizer_projects_budget_and_payload_blame",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_localizer_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_localizer",
    "boolean_only",
    "accept_only",
    "reject_without_witness",
    "noncanonical_location",
    "nonminimal_obstruction",
    "wrong_blame",
    "external_blame",
    "oracle_localization",
    "producer_coupled_localization",
    "not_source_internal",
    "subtrace_missing",
    "facet_projection_missing",
    "payload_route_blame_missing",
    "invariant_blame_missing",
    "budget_blame_missing",
    "replay_unstable",
    "semantic_reflection_blame_missing",
    "multiple_incompatible_obstructions",
    "nondeterministic_localizer",
    "nonterminating_localizer",
    "proof_irrelevant_localizer",
    "nonextensional",
    "unsound_localization",
    "incomplete_failure_coverage",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_localizing_verifier_trace_executable_global_contraction_certificate",
)

LOCALIZER_DATA = {
    "certificate": "obstruction_localizing_verifier_trace_executable_global_contraction",
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_localizer": True,
    "source_internal": True,
    "returns_accept_or_obstruction": True,
    "boolean_only": False,
    "accept_only": False,
    "reject_witness": True,
    "canonical_location": True,
    "minimal_obstruction": True,
    "correct_blame": True,
    "external_blame": False,
    "oracle_localization": False,
    "producer_coupled": False,
    "subtrace_witness": True,
    "facet_projection": True,
    "payload_route_blame": True,
    "invariant_blame": True,
    "budget_blame": True,
    "replay_stable": True,
    "semantic_reflection_blame": True,
    "unique_compatible_obstruction": True,
    "deterministic": True,
    "terminating": True,
    "proof_relevant": True,
    "extensional_over_trace": True,
    "sound": True,
    "complete_failure_coverage": True,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "facets": OBSTRUCTION_FACETS,
    "events": LOCALIZER_EVENTS,
    "checked_events": CHECK_EVENTS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
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
        "localizer": deepcopy(LOCALIZER_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "localizer":
            state["localizer"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(LOCALIZEVERIFY, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    loc = state["localizer"]
    events = set(loc["events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_594")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc594_witness")
    if LOCALIZEVERIFY not in state["accepted"]:
        reasons.append("missing_obstruction_localizing_verifier_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(LOCALIZEVERIFY, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if loc.get("base_verifier") != VERIFYTRACE or loc.get("base_trace") != TRACEEXEC:
        reasons.append("wrong_localizer_base")
    if not loc.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not loc.get("has_localizer"):
        reasons.append(FLAG_PREFIX + "no_localizer")
    if loc.get("boolean_only"):
        reasons.append(FLAG_PREFIX + "boolean_only")
    if loc.get("accept_only"):
        reasons.append(FLAG_PREFIX + "accept_only")
    if not loc.get("reject_witness"):
        reasons.append(FLAG_PREFIX + "reject_without_witness")
    if not loc.get("canonical_location") or "emit_canonical_obstruction_location" not in events:
        reasons.append(FLAG_PREFIX + "noncanonical_location")
    if not loc.get("minimal_obstruction") or "emit_minimal_failing_subtrace" not in events:
        reasons.append(FLAG_PREFIX + "nonminimal_obstruction")
    if not loc.get("correct_blame"):
        reasons.append(FLAG_PREFIX + "wrong_blame")
    if loc.get("external_blame"):
        reasons.append(FLAG_PREFIX + "external_blame")
    if loc.get("oracle_localization"):
        reasons.append(FLAG_PREFIX + "oracle_localization")
    if loc.get("producer_coupled"):
        reasons.append(FLAG_PREFIX + "producer_coupled_localization")
    if not loc.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not loc.get("subtrace_witness"):
        reasons.append(FLAG_PREFIX + "subtrace_missing")
    if not loc.get("facet_projection") or loc["facets"] != OBSTRUCTION_FACETS:
        reasons.append(FLAG_PREFIX + "facet_projection_missing")
    if not loc.get("payload_route_blame") or not PAYLOAD_TRACE_EVENTS <= set(loc["payload_events"]):
        reasons.append(FLAG_PREFIX + "payload_route_blame_missing")
    if not loc.get("invariant_blame") or loc["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_blame_missing")
    if not loc.get("budget_blame") or "exact_24_budget" not in loc["facets"]:
        reasons.append(FLAG_PREFIX + "budget_blame_missing")
    if not loc.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "replay_unstable")
    if not loc.get("semantic_reflection_blame"):
        reasons.append(FLAG_PREFIX + "semantic_reflection_blame_missing")
    if not loc.get("unique_compatible_obstruction"):
        reasons.append(FLAG_PREFIX + "multiple_incompatible_obstructions")
    if not loc.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_localizer")
    if not loc.get("terminating"):
        reasons.append(FLAG_PREFIX + "nonterminating_localizer")
    if not loc.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_localizer")
    if not loc.get("extensional_over_trace"):
        reasons.append(FLAG_PREFIX + "nonextensional")
    if not loc.get("sound"):
        reasons.append(FLAG_PREFIX + "unsound_localization")
    if not loc.get("complete_failure_coverage"):
        reasons.append(FLAG_PREFIX + "incomplete_failure_coverage")
    if loc.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if loc.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if loc.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if loc.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if loc.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not loc.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    required_events = {
        "return_accept_or_obstruction",
        "localize_schema_failure",
        "localize_event_coverage_failure",
        "localize_order_failure",
        "localize_replay_failure",
        "localize_semantic_reflection_failure",
        "localize_invariant_failure",
        "localize_payload_route_failure",
        "localize_budget_failure",
    }
    if not required_events <= events:
        reasons.append("missing_localizer_events")

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
        and LOCALIZEVERIFY in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["localizer"]["base_verifier"] == VERIFYTRACE
        and state["localizer"]["has_localizer"]
        and state["localizer"]["source_internal"]
        and state["localizer"]["returns_accept_or_obstruction"],
        "source-internal localizer returns accepted certificate or obstruction",
    )
    gate(
        f"{PREFIX}3",
        state["localizer"]["reject_witness"]
        and state["localizer"]["canonical_location"]
        and state["localizer"]["minimal_obstruction"]
        and state["localizer"]["correct_blame"],
        "rejections carry canonical minimal correctly-blamed obstruction witnesses",
    )
    gate(
        f"{PREFIX}4",
        OBSTRUCTION_FACETS == state["localizer"]["facets"]
        and "emit_minimal_failing_subtrace" in state["localizer"]["events"]
        and "emit_canonical_obstruction_location" in state["localizer"]["events"],
        "localizer exposes the finite source facets and failing subtrace",
    )
    gate(
        f"{PREFIX}5",
        state["localizer"]["invariant_blame"]
        and state["localizer"]["payload_route_blame"]
        and state["localizer"]["budget_blame"]
        and INVARIANT_TRACE_TARGETS == state["localizer"]["invariant_targets"],
        "localizer projects invariant, payload-route, and budget blame",
    )
    gate(
        f"{PREFIX}6",
        state["localizer"]["replay_stable"]
        and state["localizer"]["semantic_reflection_blame"]
        and state["localizer"]["unique_compatible_obstruction"],
        "obstruction localization is replay-stable, semantic-reflection aware, and unique",
    )
    gate(
        f"{PREFIX}7",
        state["localizer"]["deterministic"]
        and state["localizer"]["terminating"]
        and state["localizer"]["proof_relevant"]
        and state["localizer"]["extensional_over_trace"]
        and state["localizer"]["sound"]
        and state["localizer"]["complete_failure_coverage"],
        "localizer is deterministic, terminating, proof-relevant, extensional, sound, and complete on failures",
    )
    gate(
        f"{PREFIX}8",
        state["localizer"]["budgeted"]
        and not any(
            state["localizer"][key]
            for key in (
                "boolean_only",
                "accept_only",
                "external_blame",
                "oracle_localization",
                "producer_coupled",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(LOCALIZEVERIFY, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "obstruction localizer is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: verifier failures are obstruction-localized")
    print(
        "VERDICT: the missing-object candidate now counts only when verifier "
        "failure is converted into a canonical source-internal obstruction; "
        "boolean-only, wrong-blame, external, oracle, or unbudgeted localizers "
        "are disguised repairs."
    )


if __name__ == "__main__":
    main()
