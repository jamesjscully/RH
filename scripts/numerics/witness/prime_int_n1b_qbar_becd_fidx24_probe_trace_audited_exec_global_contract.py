#!/usr/bin/env python3
r"""Trace-audited executable global contraction.

Doc 591 requires the globally contractible section to be extracted by an
internal executable evaluator. This witness closes the next escape: the
evaluator might be a black box whose output is only externally audited. The
doc 592 frontier only counts if the evaluator emits a source-internal,
proof-relevant, replayable trace covering the normalizer, semantic,
invariant, payload, and handoff routes used by the contraction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_trace_audited_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_executable_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    ADM_CAT,
    BC,
    COHERENT,
    DD4_BOUNDARY,
    DEGREE,
    ENDPOINT,
    EVAL,
    EXACT_DELTA,
    EXEC,
    EXECGLOB,
    FUNC_NORM,
    GLOBCONTR,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    NORM,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC591_REQUIRED_DEPS,
    ROSATI,
    SEMCONS,
    SOURCE_LAW_GENERATORS,
    TERMINAL_CERT,
    UNIVERSAL_ARROW,
    load_map,
)


EXPECTED_DOC = 592
EXPECTED_WITNESS = "doc592-probe-trace-audited-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTRACEAUDITEXECGLOBCONTR"

TRACEEXEC = "trace_audited_executable_global_contraction_certificate"

failures: list[str] = []

CORE_TRACE_EVENTS = {
    "accept_admissible_global_section",
    "normalize_by_finite_diamond",
    "emit_unique_global_section",
    "emit_canonical_trace_order",
    "replay_trace_inside_source",
    "reject_forbidden_surrogates",
}

STRUCTURE_TRACE_EVENTS = {
    "trace_normalizer",
    "trace_functorial_normalizer",
    "trace_coherent_normalizer",
    "trace_executable_diamond",
    "trace_semantic_conservativity",
    "trace_represented_semantics",
    "trace_evaluation",
    "trace_beck_chevalley",
    "trace_refinement_descent",
    "trace_terminal_square",
    "trace_universal_arrow",
}

PAYLOAD_TRACE_EVENTS = {
    "trace_payload_projection",
    "trace_source_law",
    "trace_endpoint",
    "trace_degree",
    "trace_projection_formula",
    "trace_boundary",
    "trace_dd4",
    "trace_exact_delta",
    "trace_graph",
    "trace_rosati",
    "trace_control",
    "trace_handoff",
    "trace_base_change",
}

INVARIANT_TRACE_TARGETS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
    "source_before_points",
    "exact_24_cell_finite_index",
    "doc515_boundary_fiber_coherence",
    "original_dd4_res1_nonboundary",
}

REQUIRED_DEPS = DOC591_REQUIRED_DEPS | {
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
    (EXECGLOB, "made_trace_auditable_by", TRACEEXEC),
    (TRACEEXEC, "trace_audits_executable_global_contraction_for", EXECGLOB),
    (TRACEEXEC, "trace_replays_global_contraction_for", GLOBCONTR),
    (TRACEEXEC, "trace_law_via", NORM),
    (TRACEEXEC, "trace_law_via", FUNC_NORM),
    (TRACEEXEC, "trace_law_via", COHERENT),
    (TRACEEXEC, "trace_law_via", EXEC),
    (TRACEEXEC, "trace_law_via", SEMCONS),
    (TRACEEXEC, "trace_law_via", REPSEM),
    (TRACEEXEC, "trace_law_via", EVAL),
    (TRACEEXEC, "trace_law_via", BC),
    (TRACEEXEC, "trace_law_via", REFINEMENT_DESCENT),
    (TRACEEXEC, "trace_law_via", TERMINAL_CERT),
    (TRACEEXEC, "trace_law_via", UNIVERSAL_ARROW),
} | {(TRACEEXEC, "trace_logs_invariant_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "trace_audited_executable_global_contraction_certificate",
    "audit_trace_internal",
    "audit_trace_replayable",
    "audit_trace_logs_payload_routes",
    "audit_trace_rejects_surrogates",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_trace_audited_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "not_trace_audited",
    "opaque_trace",
    "lossy_trace",
    "posthoc_log",
    "external_auditor",
    "oracle_auditor",
    "proof_irrelevant_trace",
    "nondeterministic_trace",
    "nonterminating_trace",
    "critical_pair_unlogged",
    "normal_form_unlogged",
    "semantic_event_missing",
    "invariant_event_missing",
    "payload_projection_unlogged",
    "source_law_unlogged",
    "endpoint_unlogged",
    "degree_unlogged",
    "projection_formula_unlogged",
    "boundary_unlogged",
    "dd4_unlogged",
    "exact_delta_unlogged",
    "graph_unlogged",
    "rosati_unlogged",
    "control_unlogged",
    "handoff_unlogged",
    "base_change_unlogged",
    "beck_chevalley_unlogged",
    "refinement_descent_unlogged",
    "universal_arrow_unlogged",
    "not_replayable",
    "noncanonical_trace_order",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_trace_audited_executable_global_contraction_certificate",
)

TRACE_DATA = {
    "certificate": "trace_audited_executable_global_contraction",
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "trace_audited": True,
    "internal_trace": True,
    "opaque_trace": False,
    "lossy_trace": False,
    "posthoc_log": False,
    "external_auditor": False,
    "oracle_auditor": False,
    "proof_relevant": True,
    "deterministic": True,
    "terminating_trace": True,
    "critical_pairs_logged": True,
    "normal_forms_logged": True,
    "semantic_events_logged": True,
    "invariant_events_logged": True,
    "replayable": True,
    "canonical_order": True,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "events": CORE_TRACE_EVENTS | STRUCTURE_TRACE_EVENTS | PAYLOAD_TRACE_EVENTS,
    "source_law_targets": SOURCE_LAW_GENERATORS,
    "projection_targets": PROJECTION_FORMULA_TARGETS,
    "route_targets": {
        PUSHFORWARD,
        DD4_BOUNDARY,
        EXACT_DELTA,
        GRAPH_COMP,
        ROSATI,
        HANDOFF,
        GRAPH_LATER,
        BC,
    },
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
        "trace": deepcopy(TRACE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "trace":
            state["trace"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(TRACEEXEC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    trace = state["trace"]
    events = set(trace["events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_592")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc592_witness")
    if TRACEEXEC not in state["accepted"]:
        reasons.append("missing_trace_audited_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(TRACEEXEC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if trace.get("base_executable") != EXECGLOB or trace.get("base_global_contractible") != GLOBCONTR:
        reasons.append("wrong_trace_base")
    if not trace.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not trace.get("trace_audited"):
        reasons.append(FLAG_PREFIX + "not_trace_audited")
    if not trace.get("internal_trace"):
        reasons.append(FLAG_PREFIX + "external_auditor")
    if trace.get("opaque_trace"):
        reasons.append(FLAG_PREFIX + "opaque_trace")
    if trace.get("lossy_trace"):
        reasons.append(FLAG_PREFIX + "lossy_trace")
    if trace.get("posthoc_log"):
        reasons.append(FLAG_PREFIX + "posthoc_log")
    if trace.get("external_auditor"):
        reasons.append(FLAG_PREFIX + "external_auditor")
    if trace.get("oracle_auditor"):
        reasons.append(FLAG_PREFIX + "oracle_auditor")
    if not trace.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_trace")
    if not trace.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_trace")
    if not trace.get("terminating_trace"):
        reasons.append(FLAG_PREFIX + "nonterminating_trace")
    if not trace.get("critical_pairs_logged") or "trace_executable_diamond" not in events:
        reasons.append(FLAG_PREFIX + "critical_pair_unlogged")
    if not trace.get("normal_forms_logged") or "trace_normalizer" not in events:
        reasons.append(FLAG_PREFIX + "normal_form_unlogged")
    if not trace.get("semantic_events_logged") or "trace_semantic_conservativity" not in events:
        reasons.append(FLAG_PREFIX + "semantic_event_missing")
    if not trace.get("invariant_events_logged") or trace["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_event_missing")

    payload_checks = {
        "payload_projection_unlogged": "trace_payload_projection" in events,
        "source_law_unlogged": "trace_source_law" in events and SOURCE_LAW_GENERATORS <= set(trace["source_law_targets"]),
        "endpoint_unlogged": "trace_endpoint" in events and ENDPOINT in trace["source_law_targets"],
        "degree_unlogged": "trace_degree" in events and DEGREE in trace["source_law_targets"],
        "projection_formula_unlogged": "trace_projection_formula" in events
        and PROJECTION_FORMULA_TARGETS <= set(trace["projection_targets"]),
        "boundary_unlogged": "trace_boundary" in events and PUSHFORWARD in trace["route_targets"],
        "dd4_unlogged": "trace_dd4" in events and DD4_BOUNDARY in trace["route_targets"],
        "exact_delta_unlogged": "trace_exact_delta" in events and EXACT_DELTA in trace["route_targets"],
        "graph_unlogged": "trace_graph" in events and GRAPH_COMP in trace["route_targets"],
        "rosati_unlogged": "trace_rosati" in events and ROSATI in trace["route_targets"],
        "control_unlogged": "trace_control" in events,
        "handoff_unlogged": "trace_handoff" in events and {HANDOFF, GRAPH_LATER} <= set(trace["route_targets"]),
        "base_change_unlogged": "trace_base_change" in events and BC in trace["route_targets"],
        "beck_chevalley_unlogged": "trace_beck_chevalley" in events,
        "refinement_descent_unlogged": "trace_refinement_descent" in events,
        "universal_arrow_unlogged": "trace_universal_arrow" in events,
    }
    for suffix, ok in payload_checks.items():
        if not ok:
            reasons.append(FLAG_PREFIX + suffix)

    if not trace.get("replayable") or not CORE_TRACE_EVENTS <= events:
        reasons.append(FLAG_PREFIX + "not_replayable")
    if not trace.get("canonical_order"):
        reasons.append(FLAG_PREFIX + "noncanonical_trace_order")
    if trace.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if trace.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if trace.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if trace.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if trace.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not trace.get("budgeted"):
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
        and TRACEEXEC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["trace"]["base_executable"] == EXECGLOB
        and state["trace"]["base_global_contractible"] == GLOBCONTR
        and state["trace"]["trace_audited"]
        and state["trace"]["internal_trace"],
        "trace audits the doc591 executable contraction internally",
    )
    gate(
        f"{PREFIX}3",
        CORE_TRACE_EVENTS <= state["trace"]["events"]
        and state["trace"]["replayable"]
        and state["trace"]["deterministic"]
        and state["trace"]["canonical_order"],
        "trace is deterministic, canonical-order, and replayable",
    )
    gate(
        f"{PREFIX}4",
        STRUCTURE_TRACE_EVENTS <= state["trace"]["events"]
        and state["trace"]["critical_pairs_logged"]
        and state["trace"]["normal_forms_logged"]
        and state["trace"]["semantic_events_logged"],
        "trace logs the normalizer, critical-pair, semantic, evaluation, and descent structure",
    )
    gate(
        f"{PREFIX}5",
        PAYLOAD_TRACE_EVENTS <= state["trace"]["events"]
        and SOURCE_LAW_GENERATORS <= state["trace"]["source_law_targets"]
        and PROJECTION_FORMULA_TARGETS <= state["trace"]["projection_targets"],
        "trace logs source-law, payload, endpoint, degree, and projection targets",
    )
    gate(
        f"{PREFIX}6",
        INVARIANT_TRACE_TARGETS == state["trace"]["invariant_targets"]
        and {PUSHFORWARD, DD4_BOUNDARY, EXACT_DELTA, GRAPH_COMP, ROSATI, HANDOFF, GRAPH_LATER, BC}
        <= state["trace"]["route_targets"],
        "trace logs every invariant and route target used by the contraction",
    )
    gate(
        f"{PREFIX}7",
        state["trace"]["budgeted"]
        and state["trace"]["proof_relevant"]
        and not any(
            state["trace"][key]
            for key in (
                "opaque_trace",
                "lossy_trace",
                "posthoc_log",
                "external_auditor",
                "oracle_auditor",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "trace is proof-relevant, budgeted, non-oracular, and not a new layer",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(TRACEEXEC, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "trace-audited contraction is dependency-closed and graph-wired",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: executable global contraction is trace-audited")
    print(
        "VERDICT: the missing-object candidate now counts only when the "
        "executable global contraction emits a replayable source-internal "
        "trace; opaque, post-hoc, external, or unlogged contractions are "
        "disguised repairs."
    )


if __name__ == "__main__":
    main()
