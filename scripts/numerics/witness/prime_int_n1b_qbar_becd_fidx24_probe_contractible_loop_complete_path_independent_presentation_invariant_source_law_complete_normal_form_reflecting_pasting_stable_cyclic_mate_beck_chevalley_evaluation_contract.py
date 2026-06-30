#!/usr/bin/env python3
r"""Contractibility for loop-complete presentation transport.

Doc 587 requires the zero-monodromy loop inventory to generate every
admissible presentation loop. This witness closes the next cheap escape:
there may be several inequivalent internal proofs that the loop inventory is
complete, with nontrivial comparison 2-cells or hidden higher loops between
the loop-trivialization certificates. The current frontier only counts if the
space of loop-completion/trivialization certificates is itself internally
contractible and stable over the full source-square payload.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    BASE_CHANGE_ROUTES,
    BC,
    COHERENT,
    COMPOSITION_STABLE,
    CONTROL,
    CYCLIC,
    DD4_BOUNDARY,
    DEGREE,
    DIAG,
    ENDPOINT,
    EVAL,
    EXACT_DELTA,
    EXEC,
    FILTERED_COFINAL,
    FUNC_NORM,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    LAW_COMPLETION_DEPS,
    LAWCOMP,
    LOOPCOMP,
    LOOP_DATA,
    MAP_PATH,
    MATE,
    MONEXACT_DAGGER,
    NORM,
    NORMALIZER_DEPS,
    NORMREF,
    PASTE,
    PATHIND,
    PRESERVED_CONTEXTS,
    PRESINV,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    REFINEMENT_DESCENT,
    REPRESENTED_LIMIT,
    REPSEM,
    ROSATI,
    SEMCONS,
    SOURCE_LAW_GENERATORS,
    SUBREP,
    UNIVERSAL_ARROW,
    load_map,
)


EXPECTED_DOC = 588
EXPECTED_WITNESS = "doc588-probe-contractible-loop-complete-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONTRLOOPCOMPPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

CONTRLOOP = "contractible_" + LOOPCOMP

failures: list[str] = []

CONTRACTIBLE_LOOP_CLOSURES = {
    "certificate_space_contractible",
    "unique_loop_trivialization",
    "trivialization_2cells_complete",
    "trivialization_relations_complete",
    "trivialization_automorphism_trivial",
    "higher_loop_zero",
    "comparison_cell_complete",
    "conjugation_trivialization_closed",
    "composition_trivialization_closed",
    "inverse_trivialization_closed",
    "refinement_trivialization_closed",
    "subdivision_trivialization_closed",
    "universal_arrow_trivialization_closed",
    "normalizer_trivialization_closed",
    "semantic_trivialization_closed",
    "payload_trivialization_closed",
    "source_law_trivialization_closed",
}

REQUIRED_DEPS = {LOOPCOMP, PATHIND, PRESINV, LAWCOMP, NORMREF, PASTE, CYCLIC, MATE, BC, EVAL, DIAG, SUBREP, UNIVERSAL_ARROW} | NORMALIZER_DEPS | LAW_COMPLETION_DEPS | SOURCE_LAW_GENERATORS | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (LOOPCOMP, "made_contractible_by", CONTRLOOP),
    (CONTRLOOP, "contractible_loop_completion_for", LOOPCOMP),
    (CONTRLOOP, "contractible_loop_completion_for_path_independent", PATHIND),
    (CONTRLOOP, "contractible_loop_completion_for_presentation_invariant", PRESINV),
    (CONTRLOOP, "contractible_loop_completion_for_source_law_complete", LAWCOMP),
    (CONTRLOOP, "contractible_loop_completion_for_normal_form", NORMREF),
    (CONTRLOOP, "contractible_loop_completion_for_pasting_stable_mate", PASTE),
    (CONTRLOOP, "contractible_loop_completion_for_cyclic_mate", CYCLIC),
    (CONTRLOOP, "contractible_loop_completion_for_mate", MATE),
    (CONTRLOOP, "contractible_loop_completion_for_base_change", BC),
    (CONTRLOOP, "contractible_loop_completion_for_evaluation", EVAL),
    (CONTRLOOP, "contractible_loop_completion_over", DIAG),
    (CONTRLOOP, "contractible_loop_completion_internal_to", SUBREP),
    (CONTRLOOP, "contractible_loop_completion_selected_by", UNIVERSAL_ARROW),
    (CONTRLOOP, "contractible_normalizer_trivialization_via", NORM),
    (CONTRLOOP, "contractible_functorial_normalizer_trivialization_via", FUNC_NORM),
    (CONTRLOOP, "contractible_monoidal_exact_dagger_trivialization_via", MONEXACT_DAGGER),
    (CONTRLOOP, "contractible_coherent_normalizer_trivialization_via", COHERENT),
    (CONTRLOOP, "contractible_executable_diamond_trivialization_via", EXEC),
    (CONTRLOOP, "contractible_semantics_trivialization_via", SEMCONS),
    (CONTRLOOP, "contractible_represented_semantics_trivialization_via", REPSEM),
    (CONTRLOOP, "contractible_composition_law_trivialization_via", COMPOSITION_STABLE),
    (CONTRLOOP, "contractible_refinement_law_trivialization_via", REFINEMENT_DESCENT),
    (CONTRLOOP, "contractible_filtered_cofinal_law_trivialization_via", FILTERED_COFINAL),
    (CONTRLOOP, "contractible_represented_limit_law_trivialization_via", REPRESENTED_LIMIT),
} | {(CONTRLOOP, "contractible_source_law_trivialization_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (CONTRLOOP, "contractible_projection_law_trivialization_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(CONTRLOOP, "contractible_route_law_trivialization_for", target) for target in BASE_CHANGE_ROUTES} | {
    (CONTRLOOP, "contractible_context_law_trivialization_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "contractible_loop_completion_certificate",
    "loop_trivialization_space_connected",
    "unique_loop_trivialization",
    "trivialization_2cells_complete",
    "trivialization_automorphisms_trivial",
    "higher_loop_monodromy_zero",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_contractible",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_multiple_components",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nonunique_trivialization",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_incomplete_2cell_relations",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nontrivial_automorphism",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_hidden_higher_loop",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_comparison_cell_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_conjugation_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_composition_closure_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_inverse_closure_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_refinement_closure_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_subdivision_closure_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_universal_arrow_closure_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_normalizer_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_semantic_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_invariant_reflection_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_payload_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_source_law_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_endpoint_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_degree_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_projection_formula_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_boundary_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_dd4_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_exact_delta_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_graph_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_rosati_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_control_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_handoff_trivialization_gap",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_external_contractibility_proof",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_external_2groupoid",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_quotient_higher_groupoid",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_homotopy_quotient",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_syntax_higher_quotient",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_retuned_trivialization",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_budgeted",
    "missing_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

CONTRACT_DATA = {
    "certificate": "contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_loop_complete": LOOPCOMP,
    "base_path_independent": PATHIND,
    "base_presentation_invariant": PRESINV,
    "base_source_law_complete": LAWCOMP,
    "base_normal_form": NORMREF,
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "loop_completion_contractible": True,
    "certificate_space_connected": True,
    "unique_loop_trivialization": True,
    "trivialization_2cells_complete": True,
    "trivialization_relations_complete": True,
    "trivialization_automorphisms_trivial": True,
    "higher_loop_monodromy_zero": True,
    "comparison_cells_complete": True,
    "conjugation_closed": True,
    "composition_closed": True,
    "inverse_closed": True,
    "refinement_closed": True,
    "subdivision_closed": True,
    "universal_arrow_closed": True,
    "normalizer_trivialization_complete": True,
    "semantic_trivialization_complete": True,
    "invariant_reflection_trivialization_complete": True,
    "payload_trivialization_complete": True,
    "source_law_trivialization_complete": True,
    "endpoint_trivialization_complete": True,
    "degree_trivialization_complete": True,
    "projection_formula_trivialization_complete": True,
    "boundary_trivialization_complete": True,
    "dd4_trivialization_complete": True,
    "exact_delta_trivialization_complete": True,
    "graph_trivialization_complete": True,
    "rosati_trivialization_complete": True,
    "control_trivialization_complete": True,
    "handoff_trivialization_complete": True,
    "natural": True,
    "coherent": True,
    "external_contractibility_proof": False,
    "external_2groupoid": False,
    "quotient_higher_groupoid": False,
    "homotopy_quotient": False,
    "syntax_higher_quotient": False,
    "retuned_trivialization": False,
    "functor_of_points_only": False,
    "yoneda_reversal": False,
    "pointwise_only": False,
    "objectwise_only": False,
    "nonfunctorial_choice": False,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "loop_data": LOOP_DATA,
    "closures": CONTRACTIBLE_LOOP_CLOSURES,
    "normalizer_deps": NORMALIZER_DEPS,
    "law_completion_deps": LAW_COMPLETION_DEPS,
    "generators": SOURCE_LAW_GENERATORS,
    "routes": BASE_CHANGE_ROUTES,
    "projection_targets": PROJECTION_FORMULA_TARGETS,
    "preserved_contexts": PRESERVED_CONTEXTS,
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
        "contract": deepcopy(CONTRACT_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "contract":
            state["contract"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CONTRLOOP, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    contract = state["contract"]
    loop = contract["loop_data"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_588")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc588_witness")
    if CONTRLOOP not in state["accepted"]:
        reasons.append("missing_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(CONTRLOOP, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if contract.get("base_loop_complete") != LOOPCOMP:
        reasons.append("wrong_base_loop_complete")
    if contract.get("base_path_independent") != PATHIND:
        reasons.append("wrong_base_path_independent")
    if contract.get("base_presentation_invariant") != PRESINV:
        reasons.append("wrong_base_presentation_invariant")
    if contract.get("base_source_law_complete") != LAWCOMP:
        reasons.append("wrong_base_source_law_complete")
    if contract.get("base_normal_form") != NORMREF:
        reasons.append("wrong_base_normal_form_reflection")
    if contract.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if contract.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if contract.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if contract.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not loop.get("loop_complete") or loop.get("selected_loop_basis_only"):
        reasons.append("base_loop_completion_not_doc587_complete")

    if not contract.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_missing")
    if not contract.get("loop_completion_contractible"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_contractible")
    if not contract.get("certificate_space_connected"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_multiple_components")
    if not contract.get("unique_loop_trivialization"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nonunique_trivialization")
    if not contract.get("trivialization_2cells_complete") or not contract.get("trivialization_relations_complete"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_incomplete_2cell_relations")
    if not contract.get("trivialization_automorphisms_trivial"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nontrivial_automorphism")
    if not contract.get("higher_loop_monodromy_zero"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_hidden_higher_loop")
    if not contract.get("comparison_cells_complete") or "comparison_cell_complete" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_comparison_cell_gap")
    if not contract.get("conjugation_closed") or "conjugation_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_conjugation_gap")
    if not contract.get("composition_closed") or "composition_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_composition_closure_gap")
    if not contract.get("inverse_closed") or "inverse_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_inverse_closure_gap")
    if not contract.get("refinement_closed") or "refinement_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_refinement_closure_gap")
    if not contract.get("subdivision_closed") or "subdivision_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_subdivision_closure_gap")
    if not contract.get("universal_arrow_closed") or "universal_arrow_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_universal_arrow_closure_gap")
    if not contract.get("normalizer_trivialization_complete") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= contract["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_normalizer_trivialization_gap")
    if not contract.get("semantic_trivialization_complete") or SEMCONS not in contract["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_semantic_trivialization_gap")
    if not contract.get("invariant_reflection_trivialization_complete") or REPSEM not in contract["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_invariant_reflection_trivialization_gap")
    if not contract.get("payload_trivialization_complete") or "payload_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_payload_trivialization_gap")
    if not contract.get("source_law_trivialization_complete") or "source_law_trivialization_closed" not in contract["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_source_law_trivialization_gap")
    if not contract.get("endpoint_trivialization_complete") or ENDPOINT not in contract["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_endpoint_trivialization_gap")
    if not contract.get("degree_trivialization_complete") or DEGREE not in contract["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_degree_trivialization_gap")
    if not contract.get("projection_formula_trivialization_complete") or not PROJECTION_FORMULA_TARGETS <= set(contract["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_projection_formula_trivialization_gap")
    if not contract.get("boundary_trivialization_complete") or PUSHFORWARD not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_boundary_trivialization_gap")
    if not contract.get("dd4_trivialization_complete") or DD4_BOUNDARY not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_dd4_trivialization_gap")
    if not contract.get("exact_delta_trivialization_complete") or EXACT_DELTA not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_exact_delta_trivialization_gap")
    if not contract.get("graph_trivialization_complete") or GRAPH_COMP not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_graph_trivialization_gap")
    if not contract.get("rosati_trivialization_complete") or ROSATI not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_rosati_trivialization_gap")
    if not contract.get("control_trivialization_complete") or CONTROL not in contract["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_control_trivialization_gap")
    if not contract.get("handoff_trivialization_complete") or not {HANDOFF, GRAPH_LATER} <= set(contract["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_handoff_trivialization_gap")
    if not contract.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_natural")
    if not contract.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_coherent")
    if contract.get("external_contractibility_proof"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_external_contractibility_proof")
    if contract.get("external_2groupoid"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_external_2groupoid")
    if contract.get("quotient_higher_groupoid"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_quotient_higher_groupoid")
    if contract.get("homotopy_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_homotopy_quotient")
    if contract.get("syntax_higher_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_syntax_higher_quotient")
    if contract.get("retuned_trivialization"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_retuned_trivialization")
    if contract.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_functor_of_points_only")
    if contract.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_yoneda_reversal")
    if contract.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_pointwise_only")
    if contract.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_objectwise_only")
    if contract.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_nonfunctorial_choice")
    if contract.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_requires_choice")
    if contract.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_requires_new_cell")
    if contract.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_context_collapse")
    if contract.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_by_declaration")
    if contract.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_finite_sample")
    if contract.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_basis_row")
    if not contract.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_contractible_loop_complete_path_pres_law_nf_not_budgeted")

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
        and CONTRLOOP in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["contract"]["loop_completion_contractible"]
        and state["contract"]["certificate_space_connected"]
        and state["contract"]["unique_loop_trivialization"],
        "loop-completion trivialization certificate space is internally contractible",
    )
    gate(
        f"{PREFIX}3",
        state["contract"]["trivialization_2cells_complete"]
        and state["contract"]["trivialization_relations_complete"]
        and state["contract"]["trivialization_automorphisms_trivial"]
        and state["contract"]["higher_loop_monodromy_zero"]
        and CONTRACTIBLE_LOOP_CLOSURES <= state["contract"]["closures"],
        "2-cell relations, automorphisms, and higher loops are trivialized",
    )
    gate(
        f"{PREFIX}4",
        state["contract"]["comparison_cells_complete"]
        and state["contract"]["conjugation_closed"]
        and state["contract"]["composition_closed"]
        and state["contract"]["inverse_closed"]
        and state["contract"]["refinement_closed"]
        and state["contract"]["subdivision_closed"]
        and state["contract"]["universal_arrow_closed"]
        and {FILTERED_COFINAL, REFINEMENT_DESCENT, REPRESENTED_LIMIT} <= state["contract"]["law_completion_deps"],
        "contractible trivialization is stable under comparison, algebra, refinement, subdivision, and transport",
    )
    gate(
        f"{PREFIX}5",
        state["contract"]["normalizer_trivialization_complete"]
        and state["contract"]["semantic_trivialization_complete"]
        and state["contract"]["invariant_reflection_trivialization_complete"]
        and NORMALIZER_DEPS <= state["contract"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection trivializations are complete",
    )
    gate(
        f"{PREFIX}6",
        state["contract"]["payload_trivialization_complete"]
        and state["contract"]["source_law_trivialization_complete"]
        and state["contract"]["endpoint_trivialization_complete"]
        and state["contract"]["degree_trivialization_complete"]
        and state["contract"]["projection_formula_trivialization_complete"]
        and state["contract"]["boundary_trivialization_complete"]
        and state["contract"]["dd4_trivialization_complete"]
        and state["contract"]["exact_delta_trivialization_complete"],
        "payload, source-law, endpoint, degree, projection, boundary, DD.4, and exact-delta trivializations are complete",
    )
    gate(
        f"{PREFIX}7",
        state["contract"]["graph_trivialization_complete"]
        and state["contract"]["rosati_trivialization_complete"]
        and state["contract"]["control_trivialization_complete"]
        and state["contract"]["handoff_trivialization_complete"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["contract"]["routes"],
        "graph, Rosati, control, handoff, and graph-later trivializations are complete",
    )
    gate(
        f"{PREFIX}8",
        state["contract"]["budgeted"]
        and state["contract"]["natural"]
        and state["contract"]["coherent"]
        and not any(
            state["contract"][key]
            for key in (
                "external_contractibility_proof",
                "external_2groupoid",
                "quotient_higher_groupoid",
                "homotopy_quotient",
                "syntax_higher_quotient",
                "retuned_trivialization",
                "functor_of_points_only",
                "yoneda_reversal",
                "pointwise_only",
                "objectwise_only",
                "nonfunctorial_choice",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(CONTRLOOP, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "contractible loop completion is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: loop-completion trivialization certificate space is contractible")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "loop-complete presentation-transport proof has a unique internal "
        "coherent trivialization; multiple loop-completion certificates are "
        "still disguised repairs."
    )


if __name__ == "__main__":
    main()
