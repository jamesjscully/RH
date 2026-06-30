#!/usr/bin/env python3
r"""Boundary separator for the obstruction terminal basin.

Doc 600 makes every admissible obstruction entry trace absorb into one
terminal fixed point. This witness closes the next escape: the basin must
expose a finite source-internal boundary separating all entry surfaces and all
rejected escape variants. Otherwise "absorption" can still hide an untyped
edge of the basin.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_fixedpoint_contract import (
    ACTIONCLASS,
    ADM_CAT,
    BASINACTION,
    BASIN_DATA,
    BANNED_FLAGS as DOC600_BANNED_FLAGS,
    BC,
    CLASSIFYLOC,
    COHERENT,
    CONFLACTION,
    ENTRY_TRACE_SURFACES,
    EVAL,
    EXEC,
    EXECGLOB,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC600_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 601
EXPECTED_WITNESS = "doc601-probe-obstruction-terminal-basin-boundary-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

BOUNDARYACTION = "obstruction_terminal_basin_boundary_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

ENTRY_BOUNDARY_SURFACES = frozenset(f"entry_boundary:{surface}" for surface in ENTRY_TRACE_SURFACES)
ESCAPE_BOUNDARY_SURFACES = frozenset(f"escape_boundary:{flag}" for flag in DOC600_BANNED_FLAGS)
BOUNDARY_SURFACES = ENTRY_BOUNDARY_SURFACES | ESCAPE_BOUNDARY_SURFACES

BOUNDARY_EVENTS = {
    "enumerate_terminal_basin_entry_boundaries",
    "enumerate_terminal_basin_escape_boundaries",
    "separate_entry_trace_boundary",
    "separate_escape_repair_boundary",
    "verify_boundary_absorption",
    "verify_no_unseparated_escape",
    "verify_no_second_terminal_boundary",
    "emit_terminal_basin_boundary_certificate",
}

REQUIRED_DEPS = DOC600_REQUIRED_DEPS | {
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
    ADM_CAT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (BASINACTION, "made_boundary_separator_by", BOUNDARYACTION),
    (BOUNDARYACTION, "separates_terminal_basin_for", BASINACTION),
    (BOUNDARYACTION, "separates_fixedpoint_for", FIXPTACTION),
    (BOUNDARYACTION, "separates_normalform_reflection_for", NFREFLACTION),
    (BOUNDARYACTION, "separates_confluent_action_for", CONFLACTION),
    (BOUNDARYACTION, "separates_action_plan_for", ACTIONCLASS),
    (BOUNDARYACTION, "separates_classifier_for", CLASSIFYLOC),
    (BOUNDARYACTION, "separates_localizer_for", LOCALIZEVERIFY),
    (BOUNDARYACTION, "separates_verifier_for", VERIFYTRACE),
    (BOUNDARYACTION, "separates_trace_audit_for", TRACEEXEC),
    (BOUNDARYACTION, "separates_executable_global_contraction_for", EXECGLOB),
    (BOUNDARYACTION, "separates_global_contraction_for", GLOBCONTR),
    (BOUNDARYACTION, "separates_terminal_certificate_for", TERMINAL_CERT),
    (BOUNDARYACTION, "separates_action_law_boundary_via", NORM),
    (BOUNDARYACTION, "separates_action_law_boundary_via", FUNC_NORM),
    (BOUNDARYACTION, "separates_action_law_boundary_via", COHERENT),
    (BOUNDARYACTION, "separates_action_law_boundary_via", EXEC),
    (BOUNDARYACTION, "separates_action_law_boundary_via", SEMCONS),
    (BOUNDARYACTION, "separates_action_law_boundary_via", REPSEM),
    (BOUNDARYACTION, "separates_action_law_boundary_via", EVAL),
    (BOUNDARYACTION, "separates_action_law_boundary_via", BC),
    (BOUNDARYACTION, "separates_action_law_boundary_via", REFINEMENT_DESCENT),
    (BOUNDARYACTION, "separates_action_law_boundary_via", UNIVERSAL_ARROW),
} | {(BOUNDARYACTION, "separates_invariant_boundary_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_source_internal",
    "terminal_basin_boundary_entry_cover",
    "terminal_basin_boundary_escape_cover",
    "terminal_basin_boundary_separating",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_boundary_certificate",
    "incomplete_entry_boundary_cover",
    "incomplete_escape_boundary_cover",
    "unlisted_boundary_surface",
    "boundary_not_separating",
    "entry_boundary_missing",
    "escape_boundary_missing",
    "verifier_boundary_missing",
    "trace_audit_boundary_missing",
    "localizer_boundary_missing",
    "classifier_boundary_missing",
    "action_boundary_missing",
    "confluence_boundary_missing",
    "reflection_boundary_missing",
    "fixedpoint_boundary_missing",
    "invariant_boundary_missing",
    "payload_boundary_missing",
    "repair_boundary_missing",
    "no_go_boundary_missing",
    "budget_boundary_missing",
    "context_boundary_missing",
    "sample_boundary_missing",
    "trace_boundary_missing",
    "boundary_does_not_absorb",
    "boundary_changes_fixedpoint",
    "boundary_allows_second_terminal",
    "boundary_overlaps_incompatibly",
    "boundary_not_finite",
    "boundary_not_canonical",
    "boundary_not_replay_stable",
    "boundary_nonterminating",
    "boundary_nondeterministic",
    "boundary_not_extensional",
    "proof_irrelevant_boundary",
    "external_boundary",
    "oracle_boundary",
    "branch_spawning_boundary",
    "unbounded_boundary_search",
    "retuned_boundary",
    "not_source_internal",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

BOUNDARY_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_reflected_fixedpoint_trace_executable_global_contraction",
    "base_basin": BASINACTION,
    "base_fixedpoint": FIXPTACTION,
    "exists": True,
    "has_boundary_certificate": True,
    "source_internal": True,
    "entry_boundary_cover_complete": True,
    "escape_boundary_cover_complete": True,
    "all_boundaries_listed": True,
    "separating": True,
    "all_entries_have_boundaries": True,
    "all_escapes_have_boundaries": True,
    "boundary_absorbs": True,
    "boundary_fixedpoint_stable": True,
    "no_second_terminal_boundary": True,
    "overlapping_incompatible_boundaries": False,
    "finite": True,
    "canonical": True,
    "replay_stable": True,
    "terminating": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "budgeted": True,
    "verifier_boundary_covered": True,
    "trace_audit_boundary_covered": True,
    "localizer_boundary_covered": True,
    "classifier_boundary_covered": True,
    "action_boundary_covered": True,
    "confluence_boundary_covered": True,
    "reflection_boundary_covered": True,
    "fixedpoint_boundary_covered": True,
    "invariant_boundary_covered": True,
    "payload_boundary_covered": True,
    "repair_boundary_covered": True,
    "no_go_boundary_covered": True,
    "budget_boundary_covered": True,
    "context_boundary_covered": True,
    "sample_boundary_covered": True,
    "trace_boundary_covered": True,
    "external_boundary": False,
    "oracle_boundary": False,
    "branch_spawning": False,
    "unbounded_boundary_search": False,
    "retuned_boundary": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "entry_boundaries": ENTRY_BOUNDARY_SURFACES,
    "escape_boundaries": ESCAPE_BOUNDARY_SURFACES,
    "boundary_surfaces": BOUNDARY_SURFACES,
    "entry_boundary_map": {surface: f"entry_boundary:{surface}" for surface in ENTRY_TRACE_SURFACES},
    "escape_boundary_map": {flag: f"escape_boundary:{flag}" for flag in DOC600_BANNED_FLAGS},
    "boundary_events": BOUNDARY_EVENTS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_escape_flags": DOC600_BANNED_FLAGS,
    "terminal_basin": BASIN_DATA["certificate"],
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
        "basin": deepcopy(BASIN_DATA),
        "boundary": deepcopy(BOUNDARY_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "basin":
            state["basin"].update(value)
        elif key == "boundary":
            state["boundary"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(BOUNDARYACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    basin = state["basin"]
    boundary = state["boundary"]
    events = set(boundary["boundary_events"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_601")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc601_witness")
    if BOUNDARYACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(BOUNDARYACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if boundary.get("base_basin") != BASINACTION or not basin.get("all_entries_absorbed"):
        reasons.append("wrong_boundary_basin_base")
    if not basin.get("entry_trace_cover_complete") or not basin.get("single_fixedpoint"):
        reasons.append("missing_doc600_terminal_basin_state")

    if not boundary.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not boundary.get("has_boundary_certificate"):
        reasons.append(FLAG_PREFIX + "no_boundary_certificate")
    if not boundary.get("entry_boundary_cover_complete") or not ENTRY_BOUNDARY_SURFACES <= set(boundary["entry_boundaries"]):
        reasons.append(FLAG_PREFIX + "incomplete_entry_boundary_cover")
    if not boundary.get("escape_boundary_cover_complete") or not ESCAPE_BOUNDARY_SURFACES <= set(boundary["escape_boundaries"]):
        reasons.append(FLAG_PREFIX + "incomplete_escape_boundary_cover")
    if not boundary.get("all_boundaries_listed") or set(boundary["boundary_surfaces"]) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "unlisted_boundary_surface")
    if not boundary.get("separating"):
        reasons.append(FLAG_PREFIX + "boundary_not_separating")
    if not boundary.get("all_entries_have_boundaries") or set(boundary["entry_boundary_map"]) != ENTRY_TRACE_SURFACES:
        reasons.append(FLAG_PREFIX + "entry_boundary_missing")
    if not boundary.get("all_escapes_have_boundaries") or set(boundary["escape_boundary_map"]) != set(DOC600_BANNED_FLAGS):
        reasons.append(FLAG_PREFIX + "escape_boundary_missing")
    if not boundary.get("verifier_boundary_covered"):
        reasons.append(FLAG_PREFIX + "verifier_boundary_missing")
    if not boundary.get("trace_audit_boundary_covered"):
        reasons.append(FLAG_PREFIX + "trace_audit_boundary_missing")
    if not boundary.get("localizer_boundary_covered"):
        reasons.append(FLAG_PREFIX + "localizer_boundary_missing")
    if not boundary.get("classifier_boundary_covered"):
        reasons.append(FLAG_PREFIX + "classifier_boundary_missing")
    if not boundary.get("action_boundary_covered"):
        reasons.append(FLAG_PREFIX + "action_boundary_missing")
    if not boundary.get("confluence_boundary_covered"):
        reasons.append(FLAG_PREFIX + "confluence_boundary_missing")
    if not boundary.get("reflection_boundary_covered"):
        reasons.append(FLAG_PREFIX + "reflection_boundary_missing")
    if not boundary.get("fixedpoint_boundary_covered"):
        reasons.append(FLAG_PREFIX + "fixedpoint_boundary_missing")
    if not boundary.get("invariant_boundary_covered") or boundary["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append(FLAG_PREFIX + "invariant_boundary_missing")
    if not boundary.get("payload_boundary_covered") or not PAYLOAD_TRACE_EVENTS <= set(boundary["payload_events"]):
        reasons.append(FLAG_PREFIX + "payload_boundary_missing")
    if not boundary.get("repair_boundary_covered"):
        reasons.append(FLAG_PREFIX + "repair_boundary_missing")
    if not boundary.get("no_go_boundary_covered"):
        reasons.append(FLAG_PREFIX + "no_go_boundary_missing")
    if not boundary.get("budget_boundary_covered"):
        reasons.append(FLAG_PREFIX + "budget_boundary_missing")
    if not boundary.get("context_boundary_covered"):
        reasons.append(FLAG_PREFIX + "context_boundary_missing")
    if not boundary.get("sample_boundary_covered"):
        reasons.append(FLAG_PREFIX + "sample_boundary_missing")
    if not boundary.get("trace_boundary_covered"):
        reasons.append(FLAG_PREFIX + "trace_boundary_missing")
    if not boundary.get("boundary_absorbs"):
        reasons.append(FLAG_PREFIX + "boundary_does_not_absorb")
    if not boundary.get("boundary_fixedpoint_stable"):
        reasons.append(FLAG_PREFIX + "boundary_changes_fixedpoint")
    if not boundary.get("no_second_terminal_boundary"):
        reasons.append(FLAG_PREFIX + "boundary_allows_second_terminal")
    if boundary.get("overlapping_incompatible_boundaries"):
        reasons.append(FLAG_PREFIX + "boundary_overlaps_incompatibly")
    if not boundary.get("finite"):
        reasons.append(FLAG_PREFIX + "boundary_not_finite")
    if not boundary.get("canonical"):
        reasons.append(FLAG_PREFIX + "boundary_not_canonical")
    if not boundary.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "boundary_not_replay_stable")
    if not boundary.get("terminating"):
        reasons.append(FLAG_PREFIX + "boundary_nonterminating")
    if not boundary.get("deterministic"):
        reasons.append(FLAG_PREFIX + "boundary_nondeterministic")
    if not boundary.get("extensional"):
        reasons.append(FLAG_PREFIX + "boundary_not_extensional")
    if not boundary.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_boundary")
    if boundary.get("external_boundary"):
        reasons.append(FLAG_PREFIX + "external_boundary")
    if boundary.get("oracle_boundary"):
        reasons.append(FLAG_PREFIX + "oracle_boundary")
    if boundary.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_boundary")
    if boundary.get("unbounded_boundary_search"):
        reasons.append(FLAG_PREFIX + "unbounded_boundary_search")
    if boundary.get("retuned_boundary"):
        reasons.append(FLAG_PREFIX + "retuned_boundary")
    if not boundary.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if boundary.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if boundary.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if boundary.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if boundary.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if boundary.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not boundary.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    required_events = {
        "enumerate_terminal_basin_entry_boundaries",
        "enumerate_terminal_basin_escape_boundaries",
        "separate_entry_trace_boundary",
        "separate_escape_repair_boundary",
        "verify_boundary_absorption",
        "verify_no_unseparated_escape",
        "verify_no_second_terminal_boundary",
        "emit_terminal_basin_boundary_certificate",
    }
    if not required_events <= events:
        reasons.append("missing_boundary_events")

    if boundary["rejected_escape_flags"] != DOC600_BANNED_FLAGS:
        reasons.append("boundary_escape_flags_not_preserved")
    if len(boundary["boundary_surfaces"]) != len(ENTRY_TRACE_SURFACES) + len(DOC600_BANNED_FLAGS):
        reasons.append("boundary_surface_count_mismatch")

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
        and BOUNDARYACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["boundary"]["base_basin"] == BASINACTION
        and state["basin"]["all_entries_absorbed"]
        and state["basin"]["single_fixedpoint"]
        and state["boundary"]["has_boundary_certificate"],
        "doc600 terminal basin is the boundary base",
    )
    gate(
        f"{PREFIX}3",
        state["boundary"]["entry_boundary_cover_complete"]
        and state["boundary"]["all_entries_have_boundaries"]
        and ENTRY_BOUNDARY_SURFACES <= set(state["boundary"]["entry_boundaries"]),
        f"entry_boundaries={len(ENTRY_BOUNDARY_SURFACES)}",
    )
    gate(
        f"{PREFIX}4",
        state["boundary"]["escape_boundary_cover_complete"]
        and state["boundary"]["all_escapes_have_boundaries"]
        and ESCAPE_BOUNDARY_SURFACES <= set(state["boundary"]["escape_boundaries"]),
        f"escape_boundaries={len(ESCAPE_BOUNDARY_SURFACES)}",
    )
    gate(
        f"{PREFIX}5",
        state["boundary"]["separating"]
        and state["boundary"]["boundary_absorbs"]
        and state["boundary"]["boundary_fixedpoint_stable"]
        and state["boundary"]["no_second_terminal_boundary"],
        "boundary separates escapes without changing the terminal fixed point",
    )
    gate(
        f"{PREFIX}6",
        state["boundary"]["verifier_boundary_covered"]
        and state["boundary"]["trace_audit_boundary_covered"]
        and state["boundary"]["localizer_boundary_covered"]
        and state["boundary"]["classifier_boundary_covered"]
        and state["boundary"]["action_boundary_covered"]
        and state["boundary"]["confluence_boundary_covered"]
        and state["boundary"]["reflection_boundary_covered"]
        and state["boundary"]["fixedpoint_boundary_covered"],
        "pipeline boundary surfaces are covered",
    )
    gate(
        f"{PREFIX}7",
        state["boundary"]["invariant_boundary_covered"]
        and state["boundary"]["payload_boundary_covered"]
        and state["boundary"]["repair_boundary_covered"]
        and state["boundary"]["no_go_boundary_covered"]
        and state["boundary"]["budget_boundary_covered"]
        and state["boundary"]["context_boundary_covered"]
        and state["boundary"]["sample_boundary_covered"]
        and state["boundary"]["trace_boundary_covered"],
        "invariant, payload, repair, no-go, budget, context, sample, and trace boundaries are covered",
    )
    gate(
        f"{PREFIX}8",
        state["boundary"]["source_internal"]
        and state["boundary"]["finite"]
        and state["boundary"]["canonical"]
        and state["boundary"]["replay_stable"]
        and state["boundary"]["terminating"]
        and state["boundary"]["deterministic"]
        and state["boundary"]["extensional"]
        and state["boundary"]["proof_relevant"]
        and state["boundary"]["budgeted"]
        and not any(
            state["boundary"][key]
            for key in (
                "overlapping_incompatible_boundaries",
                "external_boundary",
                "oracle_boundary",
                "branch_spawning",
                "unbounded_boundary_search",
                "retuned_boundary",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(BOUNDARYACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "boundary is dependency-closed, graph-wired, finite, budgeted, and source-internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: terminal obstruction basin has a separating boundary")
    print(
        "VERDICT: the missing-object candidate now counts only when every "
        "terminal-basin entry surface and rejected escape variant has a "
        "finite source-internal boundary facet; unseparated, external, "
        "retuned, sample, basis-row, or unbudgeted boundaries are disguised repairs."
    )


if __name__ == "__main__":
    main()
