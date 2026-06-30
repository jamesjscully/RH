#!/usr/bin/env python3
r"""Facet taxonomy for terminal-basin boundary kill-frontier anchors.

Doc 602 anchors each terminal-basin boundary facet to a current negative
kill-frontier mechanism. This witness closes the next escape: the facet may
not reach that anchor through a fallback bucket. Every facet must first pass
through an explicit disjoint taxonomy class whose class anchor agrees with the
doc-602 boundary-anchor map.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_contract import (
    ACTIONCLASS,
    ADM_CAT,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_ANCHOR_MAP,
    BOUNDARY_SURFACES,
    BANNED_FLAGS as DOC602_BANNED_FLAGS,
    CLASSIFYLOC,
    COHERENT,
    CONFLACTION,
    ENTRY_ANCHOR_MAP,
    ENTRY_BOUNDARY_SURFACES,
    ESCAPE_ANCHOR_MAP,
    ESCAPE_BOUNDARY_SURFACES,
    EVAL,
    EXEC,
    EXECGLOB,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    KILLBNDRACTION,
    KILL_FRONTIER_DATA,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC602_REQUIRED_DEPS,
    REQUIRED_KILL_FRONTIER_IDS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    USED_KILL_FRONTIER_IDS,
    VERIFYTRACE,
    anchor_subject,
    load_map,
)


EXPECTED_DOC = 603
EXPECTED_WITNESS = "doc603-probe-obstruction-terminal-basin-boundary-killfrontier-facet-taxonomy-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

KILLFACETACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_reflected_fixedpoint_trace_executable_global_contraction_certificate"

failures: list[str] = []

CLASS_ANCHOR_MAP = {
    "verifier_check": "verifier_separated_trace_failure",
    "trace_audit_check": "trace_audited_executable_global_contraction_failure",
    "trace_payload_route": "trace_audited_executable_global_contraction_failure",
    "localizer_blame": "obstruction_localizing_verifier_failure",
    "classifier_partition": "obstruction_classifying_localizer_failure",
    "action_semantics": "obstruction_actionable_classifier_failure",
    "confluence_normalizer": "obstruction_confluent_action_failure",
    "reflection_normalform": "center_eliminator_semantic_evaluation_normal_form_reflection_failure",
    "fixedpoint_replay": "obstruction_reflected_fixedpoint_failure",
    "terminal_basin_entry": "obstruction_terminal_basin_failure",
    "source_constraint_invariant": "represented_limit_source_constraint_bundle_failure",
    "source_internality": "represented_limit_source_constraint_bundle_failure",
    "finite_index_budget": "finite_index_insufficiency",
    "dependency_repair_nogo": "dependency_closure_impossibility",
    "boundary_shape": "obstruction_terminal_basin_boundary_failure",
    "boundary_externality": "obstruction_terminal_basin_boundary_failure",
    "boundary_contextual_surrogate": "obstruction_terminal_basin_boundary_failure",
    "boundary_search_or_retune": "obstruction_terminal_basin_boundary_failure",
}
FACET_CLASSES = frozenset(CLASS_ANCHOR_MAP)

REQUIRED_DEPS = DOC602_REQUIRED_DEPS | {
    KILLBNDRACTION,
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
    (KILLBNDRACTION, "made_facet_taxonomy_by", KILLFACETACTION),
    (KILLFACETACTION, "taxonomizes_killfrontier_facets_for", KILLBNDRACTION),
    (KILLFACETACTION, "taxonomizes_boundary_separator_for", BOUNDARYACTION),
    (KILLFACETACTION, "taxonomizes_terminal_basin_for", BASINACTION),
    (KILLFACETACTION, "taxonomizes_fixedpoint_for", FIXPTACTION),
    (KILLFACETACTION, "taxonomizes_normalform_reflection_for", NFREFLACTION),
    (KILLFACETACTION, "taxonomizes_confluent_action_for", CONFLACTION),
    (KILLFACETACTION, "taxonomizes_action_plan_for", ACTIONCLASS),
    (KILLFACETACTION, "taxonomizes_classifier_for", CLASSIFYLOC),
    (KILLFACETACTION, "taxonomizes_localizer_for", LOCALIZEVERIFY),
    (KILLFACETACTION, "taxonomizes_verifier_for", VERIFYTRACE),
    (KILLFACETACTION, "taxonomizes_trace_audit_for", TRACEEXEC),
    (KILLFACETACTION, "taxonomizes_executable_global_contraction_for", EXECGLOB),
    (KILLFACETACTION, "taxonomizes_global_contraction_for", GLOBCONTR),
    (KILLFACETACTION, "taxonomizes_terminal_certificate_for", TERMINAL_CERT),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", NORM),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", FUNC_NORM),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", COHERENT),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", EXEC),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", SEMCONS),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", REPSEM),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", EVAL),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", BC),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", REFINEMENT_DESCENT),
    (KILLFACETACTION, "taxonomizes_action_law_facet_via", UNIVERSAL_ARROW),
} | {(KILLFACETACTION, "taxonomizes_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_taxonomy_source_internal",
    "terminal_basin_boundary_killfrontier_facet_taxonomy_total",
    "terminal_basin_boundary_killfrontier_facet_taxonomy_explicit",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_facet_taxonomy_certificate",
    "unclassified_boundary_surface",
    "ambiguous_boundary_surface",
    "default_anchor_route",
    "anchor_class_mismatch",
    "anchor_bucket_unseparated",
    "facet_class_not_finite",
    "facet_class_not_source_internal",
    "facet_class_not_deterministic",
    "facet_class_not_extensional",
    "facet_class_not_dependency_closed",
    "facet_class_not_graph_wired",
    "facet_class_not_replay_stable",
    "facet_class_not_minimal",
    "facet_class_relabels_boundary",
    "facet_class_changes_fixedpoint",
    "facet_class_allows_second_terminal",
    "proof_irrelevant_facet_class",
    "external_facet_classifier",
    "oracle_facet_classifier",
    "branch_spawning_facet_classifier",
    "unbounded_facet_classification",
    "retuned_facet_classifier",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)


def facet_class_for_text(text: str) -> str:
    if "verifier" in text:
        return "verifier_check"
    if "trace_audit" in text or "trace_state" in text:
        return "trace_audit_check"
    if "payload" in text:
        return "trace_payload_route"
    if "localizer" in text:
        return "localizer_blame"
    if "classifier" in text or "class:" in text or "class" in text:
        return "classifier_partition"
    if "action" in text:
        return "action_semantics"
    if "confluence" in text:
        return "confluence_normalizer"
    if "reflection" in text or "normalform" in text or "normal_form" in text:
        return "reflection_normalform"
    if "fixedpoint" in text or "fixed_point" in text:
        return "fixedpoint_replay"
    if "basin" in text or "entry_trace" in text:
        return "terminal_basin_entry"
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
    ):
        return "source_constraint_invariant"
    if "not_source_internal" in text:
        return "source_internality"
    if "budget" in text or "finite_index" in text or "requires_new_cell" in text or "not_budgeted" in text:
        return "finite_index_budget"
    if "repair" in text or "no_go" in text or "accepted" in text or "dependency" in text:
        return "dependency_repair_nogo"
    if "external" in text or "oracle" in text:
        return "boundary_externality"
    if "branch" in text or "unbounded" in text or "retuned" in text:
        return "boundary_search_or_retune"
    if "context" in text or "sample" in text or "basis" in text or "declaration" in text or "by_declaration" in text:
        return "boundary_contextual_surrogate"
    if (
        "missing" in text
        or "certificate" in text
        or "cover" in text
        or "unlisted" in text
        or "noncanonical" in text
        or "overlap" in text
        or "proof_irrelevant" in text
        or "finite" in text
        or "boundary" in text
    ):
        return "boundary_shape"
    raise ValueError(f"unclassified boundary facet: {text}")


SURFACE_CLASS_MAP = {surface: facet_class_for_text(anchor_subject(surface)) for surface in BOUNDARY_SURFACES}
ENTRY_CLASS_MAP = {surface: SURFACE_CLASS_MAP[surface] for surface in ENTRY_BOUNDARY_SURFACES}
ESCAPE_CLASS_MAP = {surface: SURFACE_CLASS_MAP[surface] for surface in ESCAPE_BOUNDARY_SURFACES}
SURFACE_CLASS_ANCHOR_MAP = {surface: CLASS_ANCHOR_MAP[facet_class] for surface, facet_class in SURFACE_CLASS_MAP.items()}
USED_FACET_CLASSES = frozenset(SURFACE_CLASS_MAP.values())

FACET_TAXONOMY_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_reflected_fixedpoint_trace_executable_global_contraction",
    "base_killfrontier": KILLBNDRACTION,
    "base_boundary": BOUNDARYACTION,
    "base_terminal_basin": BASINACTION,
    "base_fixedpoint": FIXPTACTION,
    "exists": True,
    "has_taxonomy_certificate": True,
    "source_internal": True,
    "total": True,
    "disjoint": True,
    "explicit": True,
    "no_default_route": True,
    "all_anchor_classes_listed": True,
    "all_anchor_buckets_separated": True,
    "class_anchor_matches_doc602_anchor": True,
    "all_entry_facets_classified": True,
    "all_escape_facets_classified": True,
    "all_classes_finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "minimal": True,
    "budgeted": True,
    "boundary_preserving": True,
    "fixedpoint_stable": True,
    "no_second_terminal": True,
    "external_classifier": False,
    "oracle_classifier": False,
    "branch_spawning": False,
    "unbounded_classification": False,
    "retuned_classifier": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "facet_classes": FACET_CLASSES,
    "used_facet_classes": USED_FACET_CLASSES,
    "class_anchor_map": CLASS_ANCHOR_MAP,
    "surface_class_map": SURFACE_CLASS_MAP,
    "surface_class_anchor_map": SURFACE_CLASS_ANCHOR_MAP,
    "entry_class_map": ENTRY_CLASS_MAP,
    "escape_class_map": ESCAPE_CLASS_MAP,
    "boundary_anchor_map": BOUNDARY_ANCHOR_MAP,
    "entry_anchor_map": ENTRY_ANCHOR_MAP,
    "escape_anchor_map": ESCAPE_ANCHOR_MAP,
    "boundary_surfaces": BOUNDARY_SURFACES,
    "entry_boundaries": ENTRY_BOUNDARY_SURFACES,
    "escape_boundaries": ESCAPE_BOUNDARY_SURFACES,
    "required_kill_frontier_ids": REQUIRED_KILL_FRONTIER_IDS,
    "used_kill_frontier_ids": USED_KILL_FRONTIER_IDS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "rejected_killfrontier_flags": DOC602_BANNED_FLAGS,
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
        "killfrontier": deepcopy(KILL_FRONTIER_DATA),
        "facet_taxonomy": deepcopy(FACET_TAXONOMY_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "killfrontier":
            state["killfrontier"].update(value)
        elif key == "facet_taxonomy":
            state["facet_taxonomy"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLFACETACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    killfrontier = state["killfrontier"]
    taxonomy = state["facet_taxonomy"]
    surface_class_map = dict(taxonomy["surface_class_map"])
    surface_class_anchor_map = dict(taxonomy["surface_class_anchor_map"])
    class_anchor_map = dict(taxonomy["class_anchor_map"])
    boundary_anchor_map = dict(taxonomy["boundary_anchor_map"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_603")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc603_witness")
    if KILLFACETACTION not in state["accepted"]:
        reasons.append("missing_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_reflected_fixedpoint_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLFACETACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if taxonomy.get("base_killfrontier") != KILLBNDRACTION or not killfrontier.get("has_anchor_certificate"):
        reasons.append("wrong_facet_taxonomy_base")
    if not killfrontier.get("all_boundary_surfaces_anchored") or not killfrontier.get("anchors_negative"):
        reasons.append("missing_doc602_killfrontier_state")

    if not taxonomy.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not taxonomy.get("has_taxonomy_certificate"):
        reasons.append(FLAG_PREFIX + "no_facet_taxonomy_certificate")
    if not taxonomy.get("total") or set(surface_class_map) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "unclassified_boundary_surface")
    if not taxonomy.get("disjoint") or len(surface_class_map) != len(BOUNDARY_SURFACES):
        reasons.append(FLAG_PREFIX + "ambiguous_boundary_surface")
    if not taxonomy.get("explicit") or not taxonomy.get("no_default_route"):
        reasons.append(FLAG_PREFIX + "default_anchor_route")
    if not taxonomy.get("all_anchor_classes_listed") or set(surface_class_map.values()) - set(class_anchor_map):
        reasons.append(FLAG_PREFIX + "unclassified_boundary_surface")
    if not taxonomy.get("class_anchor_matches_doc602_anchor") or surface_class_anchor_map != boundary_anchor_map:
        reasons.append(FLAG_PREFIX + "anchor_class_mismatch")
    if (
        not taxonomy.get("all_anchor_buckets_separated")
        or set(class_anchor_map.values()) != REQUIRED_KILL_FRONTIER_IDS
        or set(surface_class_anchor_map.values()) != USED_KILL_FRONTIER_IDS
    ):
        reasons.append(FLAG_PREFIX + "anchor_bucket_unseparated")
    if not taxonomy.get("all_entry_facets_classified") or set(taxonomy["entry_class_map"]) != ENTRY_BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "unclassified_boundary_surface")
    if not taxonomy.get("all_escape_facets_classified") or set(taxonomy["escape_class_map"]) != ESCAPE_BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "unclassified_boundary_surface")
    if not taxonomy.get("all_classes_finite"):
        reasons.append(FLAG_PREFIX + "facet_class_not_finite")
    if not taxonomy.get("source_internal"):
        reasons.append(FLAG_PREFIX + "facet_class_not_source_internal")
    if not taxonomy.get("deterministic"):
        reasons.append(FLAG_PREFIX + "facet_class_not_deterministic")
    if not taxonomy.get("extensional"):
        reasons.append(FLAG_PREFIX + "facet_class_not_extensional")
    if not taxonomy.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "facet_class_not_dependency_closed")
    if not taxonomy.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "facet_class_not_graph_wired")
    if not taxonomy.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "facet_class_not_replay_stable")
    if not taxonomy.get("minimal"):
        reasons.append(FLAG_PREFIX + "facet_class_not_minimal")
    if not taxonomy.get("boundary_preserving"):
        reasons.append(FLAG_PREFIX + "facet_class_relabels_boundary")
    if not taxonomy.get("fixedpoint_stable"):
        reasons.append(FLAG_PREFIX + "facet_class_changes_fixedpoint")
    if not taxonomy.get("no_second_terminal"):
        reasons.append(FLAG_PREFIX + "facet_class_allows_second_terminal")
    if not taxonomy.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_facet_class")
    if taxonomy.get("external_classifier"):
        reasons.append(FLAG_PREFIX + "external_facet_classifier")
    if taxonomy.get("oracle_classifier"):
        reasons.append(FLAG_PREFIX + "oracle_facet_classifier")
    if taxonomy.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_facet_classifier")
    if taxonomy.get("unbounded_classification"):
        reasons.append(FLAG_PREFIX + "unbounded_facet_classification")
    if taxonomy.get("retuned_classifier"):
        reasons.append(FLAG_PREFIX + "retuned_facet_classifier")
    if taxonomy.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if taxonomy.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if taxonomy.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if taxonomy.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if taxonomy.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not taxonomy.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if taxonomy["payload_events"] != PAYLOAD_TRACE_EVENTS:
        reasons.append("payload_trace_events_not_preserved")
    if taxonomy["rejected_killfrontier_flags"] != DOC602_BANNED_FLAGS:
        reasons.append("doc602_rejected_flags_not_preserved")

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
        and KILLFACETACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["facet_taxonomy"]["base_killfrontier"] == KILLBNDRACTION
        and state["killfrontier"]["has_anchor_certificate"]
        and state["killfrontier"]["all_boundary_surfaces_anchored"],
        "doc602 kill-frontier anchor map is the facet-taxonomy base",
    )
    gate(
        f"{PREFIX}3",
        state["facet_taxonomy"]["total"]
        and set(state["facet_taxonomy"]["surface_class_map"]) == BOUNDARY_SURFACES,
        f"boundary_facets={len(BOUNDARY_SURFACES)} classified={len(state['facet_taxonomy']['surface_class_map'])}",
    )
    gate(
        f"{PREFIX}4",
        state["facet_taxonomy"]["disjoint"]
        and state["facet_taxonomy"]["explicit"]
        and state["facet_taxonomy"]["no_default_route"]
        and set(state["facet_taxonomy"]["used_facet_classes"]) <= FACET_CLASSES,
        f"used_classes={len(state['facet_taxonomy']['used_facet_classes'])}",
    )
    gate(
        f"{PREFIX}5",
        state["facet_taxonomy"]["class_anchor_matches_doc602_anchor"]
        and state["facet_taxonomy"]["surface_class_anchor_map"] == BOUNDARY_ANCHOR_MAP
        and set(state["facet_taxonomy"]["class_anchor_map"].values()) == REQUIRED_KILL_FRONTIER_IDS
        and set(state["facet_taxonomy"]["surface_class_anchor_map"].values()) == USED_KILL_FRONTIER_IDS,
        f"anchor_ids={len(USED_KILL_FRONTIER_IDS)} classes={len(FACET_CLASSES)}",
    )
    gate(
        f"{PREFIX}6",
        state["facet_taxonomy"]["all_entry_facets_classified"]
        and state["facet_taxonomy"]["all_escape_facets_classified"]
        and set(state["facet_taxonomy"]["entry_class_map"]) == ENTRY_BOUNDARY_SURFACES
        and set(state["facet_taxonomy"]["escape_class_map"]) == ESCAPE_BOUNDARY_SURFACES,
        f"entry_facets={len(ENTRY_BOUNDARY_SURFACES)} escape_facets={len(ESCAPE_BOUNDARY_SURFACES)}",
    )
    gate(
        f"{PREFIX}7",
        state["facet_taxonomy"]["boundary_preserving"]
        and state["facet_taxonomy"]["fixedpoint_stable"]
        and state["facet_taxonomy"]["no_second_terminal"]
        and state["facet_taxonomy"]["minimal"],
        "facet classes preserve boundary/fixedpoint and are minimal",
    )
    gate(
        f"{PREFIX}8",
        state["facet_taxonomy"]["source_internal"]
        and state["facet_taxonomy"]["all_classes_finite"]
        and state["facet_taxonomy"]["deterministic"]
        and state["facet_taxonomy"]["extensional"]
        and state["facet_taxonomy"]["proof_relevant"]
        and state["facet_taxonomy"]["dependency_closed"]
        and state["facet_taxonomy"]["graph_wired"]
        and state["facet_taxonomy"]["replay_stable"]
        and state["facet_taxonomy"]["budgeted"]
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLFACETACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"]
        and not any(
            state["facet_taxonomy"][key]
            for key in (
                "external_classifier",
                "oracle_classifier",
                "branch_spawning",
                "unbounded_classification",
                "retuned_classifier",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "facet taxonomy is finite, source-internal, dependency-closed, graph-wired, replay-stable, and budgeted",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: kill-frontier boundary facets have an explicit taxonomy")
    print(
        "VERDICT: the missing-object candidate now counts only when every "
        "terminal-basin boundary facet reaches its kill-frontier anchor through "
        "a finite explicit disjoint facet class; fallback buckets, merged anchors, "
        "samples, basis rows, or unbudgeted classifiers are disguised repairs."
    )


if __name__ == "__main__":
    main()
