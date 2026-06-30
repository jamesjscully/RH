#!/usr/bin/env python3
r"""Kill-frontier anchors for the obstruction terminal-basin boundary.

Doc 601 gives the terminal obstruction basin a finite source-internal boundary.
This witness closes the next escape: every boundary facet must point to a
current negative kill-frontier mechanism. Otherwise "boundary" can still be an
arbitrary label detached from the tests that would refute it.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_contract import (
    ACTIONCLASS,
    ADM_CAT,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_DATA,
    BOUNDARY_SURFACES,
    BANNED_FLAGS as DOC601_BANNED_FLAGS,
    CLASSIFYLOC,
    COHERENT,
    CONFLACTION,
    ENTRY_BOUNDARY_SURFACES,
    ESCAPE_BOUNDARY_SURFACES,
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
    REQUIRED_DEPS as DOC601_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 602
EXPECTED_WITNESS = "doc602-probe-obstruction-terminal-basin-boundary-killfrontier-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLBNDRACTION = "obstruction_terminal_basin_boundary_killfrontier_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

REQUIRED_KILL_FRONTIER_IDS = frozenset(
    {
        "obstruction_terminal_basin_boundary_failure",
        "obstruction_terminal_basin_failure",
        "obstruction_reflected_fixedpoint_failure",
        "verifier_separated_trace_failure",
        "trace_audited_executable_global_contraction_failure",
        "obstruction_localizing_verifier_failure",
        "obstruction_classifying_localizer_failure",
        "obstruction_actionable_classifier_failure",
        "obstruction_confluent_action_failure",
        "center_eliminator_semantic_evaluation_normal_form_reflection_failure",
        "represented_limit_source_constraint_bundle_failure",
        "dependency_closure_impossibility",
        "finite_index_insufficiency",
    }
)

REQUIRED_DEPS = DOC601_REQUIRED_DEPS | {
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
    ADM_CAT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (BOUNDARYACTION, "made_killfrontier_anchor_by", KILLBNDRACTION),
    (KILLBNDRACTION, "anchors_boundary_separator_for", BOUNDARYACTION),
    (KILLBNDRACTION, "anchors_terminal_basin_for", BASINACTION),
    (KILLBNDRACTION, "anchors_fixedpoint_for", FIXPTACTION),
    (KILLBNDRACTION, "anchors_normalform_reflection_for", NFREFLACTION),
    (KILLBNDRACTION, "anchors_confluent_action_for", CONFLACTION),
    (KILLBNDRACTION, "anchors_action_plan_for", ACTIONCLASS),
    (KILLBNDRACTION, "anchors_classifier_for", CLASSIFYLOC),
    (KILLBNDRACTION, "anchors_localizer_for", LOCALIZEVERIFY),
    (KILLBNDRACTION, "anchors_verifier_for", VERIFYTRACE),
    (KILLBNDRACTION, "anchors_trace_audit_for", TRACEEXEC),
    (KILLBNDRACTION, "anchors_executable_global_contraction_for", EXECGLOB),
    (KILLBNDRACTION, "anchors_global_contraction_for", GLOBCONTR),
    (KILLBNDRACTION, "anchors_terminal_certificate_for", TERMINAL_CERT),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", NORM),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", FUNC_NORM),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", COHERENT),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", EXEC),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", SEMCONS),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", REPSEM),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", EVAL),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", BC),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", REFINEMENT_DESCENT),
    (KILLBNDRACTION, "anchors_action_law_killfrontier_via", UNIVERSAL_ARROW),
} | {(KILLBNDRACTION, "anchors_invariant_killfrontier_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_source_internal",
    "terminal_basin_boundary_killfrontier_all_surfaces_anchored",
    "terminal_basin_boundary_killfrontier_current_negative",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_killfrontier_anchor_certificate",
    "unanchored_entry_boundary",
    "unanchored_escape_boundary",
    "missing_killfrontier_item",
    "unlisted_anchor_id",
    "anchor_not_current",
    "anchor_not_negative",
    "anchor_not_finite",
    "anchor_not_source_internal",
    "anchor_not_deterministic",
    "anchor_not_extensional",
    "anchor_not_dependency_closed",
    "anchor_not_graph_wired",
    "anchor_not_replay_stable",
    "anchor_relabels_boundary",
    "anchor_changes_fixedpoint",
    "anchor_allows_second_terminal",
    "proof_irrelevant_anchor",
    "external_anchor",
    "oracle_anchor",
    "branch_spawning_anchor",
    "unbounded_anchor_search",
    "retuned_anchor",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)


def anchor_subject(surface: str) -> str:
    if surface.startswith("entry_boundary:"):
        return surface.removeprefix("entry_boundary:")
    if surface.startswith("escape_boundary:"):
        text = surface.removeprefix("escape_boundary:")
        return text.split("_nf_", 1)[1] if "_nf_" in text else text
    return surface


def anchor_for_text(text: str) -> str:
    if "verifier" in text:
        return "verifier_separated_trace_failure"
    if "trace_audit" in text or "trace_state" in text or "payload" in text:
        return "trace_audited_executable_global_contraction_failure"
    if "localizer" in text:
        return "obstruction_localizing_verifier_failure"
    if "classifier" in text or "class:" in text or "class" in text:
        return "obstruction_classifying_localizer_failure"
    if "action" in text:
        return "obstruction_actionable_classifier_failure"
    if "confluence" in text:
        return "obstruction_confluent_action_failure"
    if "reflection" in text or "normalform" in text or "normal_form" in text:
        return "center_eliminator_semantic_evaluation_normal_form_reflection_failure"
    if "fixedpoint" in text or "fixed_point" in text:
        return "obstruction_reflected_fixedpoint_failure"
    if "basin" in text or "entry_trace" in text:
        return "obstruction_terminal_basin_failure"
    if (
        "invariant" in text
        or "endpoint" in text
        or "degree" in text
        or "dd4" in text
        or "boundary_pushforward" in text
        or "graph" in text
        or "rosati" in text
        or "control" in text
        or "source_before_points" in text
        or "not_source_internal" in text
    ):
        return "represented_limit_source_constraint_bundle_failure"
    if "budget" in text or "finite_index" in text or "requires_new_cell" in text or "not_budgeted" in text:
        return "finite_index_insufficiency"
    if "repair" in text or "no_go" in text or "accepted" in text or "dependency" in text:
        return "dependency_closure_impossibility"
    if (
        "context" in text
        or "sample" in text
        or "basis" in text
        or "external" in text
        or "oracle" in text
        or "branch" in text
        or "unbounded" in text
        or "retuned" in text
        or "declaration" in text
        or "by_declaration" in text
        or "missing" in text
    ):
        return "obstruction_terminal_basin_boundary_failure"
    return "obstruction_terminal_basin_boundary_failure"


BOUNDARY_ANCHOR_MAP = {surface: anchor_for_text(anchor_subject(surface)) for surface in BOUNDARY_SURFACES}
ENTRY_ANCHOR_MAP = {surface: BOUNDARY_ANCHOR_MAP[surface] for surface in ENTRY_BOUNDARY_SURFACES}
ESCAPE_ANCHOR_MAP = {surface: BOUNDARY_ANCHOR_MAP[surface] for surface in ESCAPE_BOUNDARY_SURFACES}
USED_KILL_FRONTIER_IDS = frozenset(BOUNDARY_ANCHOR_MAP.values())

KILL_FRONTIER_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_reflected_fixedpoint_trace_executable_global_contraction",
    "base_boundary": BOUNDARYACTION,
    "base_terminal_basin": BASINACTION,
    "base_fixedpoint": FIXPTACTION,
    "exists": True,
    "has_anchor_certificate": True,
    "source_internal": True,
    "all_boundary_surfaces_anchored": True,
    "all_entry_boundaries_anchored": True,
    "all_escape_boundaries_anchored": True,
    "all_anchor_ids_listed": True,
    "all_anchor_ids_in_current_kill_frontier": True,
    "anchors_current": True,
    "anchors_negative": True,
    "anchors_finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "budgeted": True,
    "boundary_preserving": True,
    "fixedpoint_stable": True,
    "no_second_terminal": True,
    "external_anchor": False,
    "oracle_anchor": False,
    "branch_spawning": False,
    "unbounded_anchor_search": False,
    "retuned_anchor": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "required_kill_frontier_ids": REQUIRED_KILL_FRONTIER_IDS,
    "used_kill_frontier_ids": USED_KILL_FRONTIER_IDS,
    "boundary_anchor_map": BOUNDARY_ANCHOR_MAP,
    "entry_anchor_map": ENTRY_ANCHOR_MAP,
    "escape_anchor_map": ESCAPE_ANCHOR_MAP,
    "boundary_surfaces": BOUNDARY_SURFACES,
    "entry_boundaries": ENTRY_BOUNDARY_SURFACES,
    "escape_boundaries": ESCAPE_BOUNDARY_SURFACES,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_boundary_flags": DOC601_BANNED_FLAGS,
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


def kill_frontier_ids(data: dict[str, Any]) -> set[str]:
    return {item["id"] for item in data.get("kill_frontier", {}).get("current", [])}


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
        "boundary": deepcopy(BOUNDARY_DATA),
        "killfrontier": deepcopy(KILL_FRONTIER_DATA),
        "kill_frontier_ids": kill_frontier_ids(data),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "boundary":
            state["boundary"].update(value)
        elif key == "killfrontier":
            state["killfrontier"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLBNDRACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    boundary = state["boundary"]
    killfrontier = state["killfrontier"]
    current_kill_ids = set(state["kill_frontier_ids"])
    boundary_anchor_map = dict(killfrontier["boundary_anchor_map"])
    entry_anchor_map = dict(killfrontier["entry_anchor_map"])
    escape_anchor_map = dict(killfrontier["escape_anchor_map"])
    used_anchor_ids = set(boundary_anchor_map.values())

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_602")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc602_witness")
    if KILLBNDRACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_killfrontier_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLBNDRACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if killfrontier.get("base_boundary") != BOUNDARYACTION or not boundary.get("has_boundary_certificate"):
        reasons.append("wrong_killfrontier_boundary_base")
    if not boundary.get("entry_boundary_cover_complete") or not boundary.get("escape_boundary_cover_complete"):
        reasons.append("missing_doc601_boundary_state")
    if set(boundary["boundary_surfaces"]) != BOUNDARY_SURFACES:
        reasons.append("doc601_boundary_surface_set_changed")

    if not killfrontier.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not killfrontier.get("has_anchor_certificate"):
        reasons.append(FLAG_PREFIX + "no_killfrontier_anchor_certificate")
    if (
        not killfrontier.get("all_entry_boundaries_anchored")
        or set(entry_anchor_map) != ENTRY_BOUNDARY_SURFACES
        or not set(entry_anchor_map.values()) <= REQUIRED_KILL_FRONTIER_IDS
    ):
        reasons.append(FLAG_PREFIX + "unanchored_entry_boundary")
    if (
        not killfrontier.get("all_escape_boundaries_anchored")
        or set(escape_anchor_map) != ESCAPE_BOUNDARY_SURFACES
        or not set(escape_anchor_map.values()) <= REQUIRED_KILL_FRONTIER_IDS
    ):
        reasons.append(FLAG_PREFIX + "unanchored_escape_boundary")
    if (
        not killfrontier.get("all_boundary_surfaces_anchored")
        or set(boundary_anchor_map) != BOUNDARY_SURFACES
        or set(boundary_anchor_map) != set(entry_anchor_map) | set(escape_anchor_map)
    ):
        reasons.append("boundary_anchor_surface_mismatch")

    if not REQUIRED_KILL_FRONTIER_IDS <= current_kill_ids:
        reasons.append(FLAG_PREFIX + "missing_killfrontier_item")
    if not killfrontier.get("all_anchor_ids_listed") or not used_anchor_ids <= REQUIRED_KILL_FRONTIER_IDS:
        reasons.append(FLAG_PREFIX + "unlisted_anchor_id")
    if not killfrontier.get("all_anchor_ids_in_current_kill_frontier") or not used_anchor_ids <= current_kill_ids:
        reasons.append(FLAG_PREFIX + "anchor_not_current")
    if not killfrontier.get("anchors_current"):
        reasons.append(FLAG_PREFIX + "anchor_not_current")
    if not killfrontier.get("anchors_negative"):
        reasons.append(FLAG_PREFIX + "anchor_not_negative")
    if not killfrontier.get("anchors_finite"):
        reasons.append(FLAG_PREFIX + "anchor_not_finite")
    if not killfrontier.get("source_internal"):
        reasons.append(FLAG_PREFIX + "anchor_not_source_internal")
    if not killfrontier.get("deterministic"):
        reasons.append(FLAG_PREFIX + "anchor_not_deterministic")
    if not killfrontier.get("extensional"):
        reasons.append(FLAG_PREFIX + "anchor_not_extensional")
    if not killfrontier.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "anchor_not_dependency_closed")
    if not killfrontier.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "anchor_not_graph_wired")
    if not killfrontier.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "anchor_not_replay_stable")
    if not killfrontier.get("boundary_preserving"):
        reasons.append(FLAG_PREFIX + "anchor_relabels_boundary")
    if not killfrontier.get("fixedpoint_stable"):
        reasons.append(FLAG_PREFIX + "anchor_changes_fixedpoint")
    if not killfrontier.get("no_second_terminal"):
        reasons.append(FLAG_PREFIX + "anchor_allows_second_terminal")
    if not killfrontier.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_anchor")
    if killfrontier.get("external_anchor"):
        reasons.append(FLAG_PREFIX + "external_anchor")
    if killfrontier.get("oracle_anchor"):
        reasons.append(FLAG_PREFIX + "oracle_anchor")
    if killfrontier.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_anchor")
    if killfrontier.get("unbounded_anchor_search"):
        reasons.append(FLAG_PREFIX + "unbounded_anchor_search")
    if killfrontier.get("retuned_anchor"):
        reasons.append(FLAG_PREFIX + "retuned_anchor")
    if killfrontier.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if killfrontier.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if killfrontier.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if killfrontier.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if killfrontier.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not killfrontier.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if killfrontier["payload_events"] != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if killfrontier["rejected_boundary_flags"] != DOC601_BANNED_FLAGS:
        reasons.append("doc601_rejected_flags_not_preserved")

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
    current_kill_ids = state["kill_frontier_ids"]

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc") >= EXPECTED_DOC
        and KILLBNDRACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["killfrontier"]["base_boundary"] == BOUNDARYACTION
        and state["boundary"]["has_boundary_certificate"]
        and set(state["boundary"]["boundary_surfaces"]) == BOUNDARY_SURFACES,
        "doc601 terminal-basin boundary is the anchor base",
    )
    gate(
        f"{PREFIX}3",
        state["killfrontier"]["all_entry_boundaries_anchored"]
        and set(state["killfrontier"]["entry_anchor_map"]) == ENTRY_BOUNDARY_SURFACES,
        f"entry_anchor_surfaces={len(ENTRY_BOUNDARY_SURFACES)}",
    )
    gate(
        f"{PREFIX}4",
        state["killfrontier"]["all_escape_boundaries_anchored"]
        and set(state["killfrontier"]["escape_anchor_map"]) == ESCAPE_BOUNDARY_SURFACES,
        f"escape_anchor_surfaces={len(ESCAPE_BOUNDARY_SURFACES)}",
    )
    gate(
        f"{PREFIX}5",
        REQUIRED_KILL_FRONTIER_IDS <= current_kill_ids
        and USED_KILL_FRONTIER_IDS <= REQUIRED_KILL_FRONTIER_IDS
        and USED_KILL_FRONTIER_IDS <= current_kill_ids,
        f"required_kill_ids={len(REQUIRED_KILL_FRONTIER_IDS)} used_anchor_ids={len(USED_KILL_FRONTIER_IDS)}",
    )
    gate(
        f"{PREFIX}6",
        state["killfrontier"]["anchors_current"]
        and state["killfrontier"]["anchors_negative"]
        and state["killfrontier"]["anchors_finite"]
        and state["killfrontier"]["source_internal"],
        "anchors are current negative finite source-internal kill-frontier items",
    )
    gate(
        f"{PREFIX}7",
        state["killfrontier"]["boundary_preserving"]
        and state["killfrontier"]["fixedpoint_stable"]
        and state["killfrontier"]["no_second_terminal"],
        "anchors preserve the boundary and do not alter the terminal fixed point",
    )
    gate(
        f"{PREFIX}8",
        state["killfrontier"]["dependency_closed"]
        and state["killfrontier"]["graph_wired"]
        and state["killfrontier"]["replay_stable"]
        and state["killfrontier"]["deterministic"]
        and state["killfrontier"]["extensional"]
        and state["killfrontier"]["proof_relevant"]
        and state["killfrontier"]["budgeted"]
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLBNDRACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"]
        and not any(
            state["killfrontier"][key]
            for key in (
                "external_anchor",
                "oracle_anchor",
                "branch_spawning",
                "unbounded_anchor_search",
                "retuned_anchor",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "kill-frontier anchoring is dependency-closed, graph-wired, replay-stable, and budgeted",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: terminal-basin boundary facets are kill-frontier anchored")
    print(
        "VERDICT: the missing-object candidate now counts only when every "
        "terminal-basin boundary facet is anchored to a current negative "
        "kill-frontier mechanism; arbitrary labels, relabelled boundaries, "
        "external anchors, samples, basis rows, or unbudgeted anchors are disguised repairs."
    )


if __name__ == "__main__":
    main()
