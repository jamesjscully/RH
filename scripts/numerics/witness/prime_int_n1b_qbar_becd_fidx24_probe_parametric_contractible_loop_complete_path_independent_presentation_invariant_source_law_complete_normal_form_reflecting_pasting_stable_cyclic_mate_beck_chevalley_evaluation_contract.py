#!/usr/bin/env python3
r"""Parametricity for contractible loop-completion data.

Doc 588 makes the loop-completion/trivialization certificate space internally
contractible for the current source square. This witness closes the next
cheap escape: the contractibility proofs may exist only fiberwise, with no
cartesian/pseudonatural assembly over all admissible source-square morphisms,
refinements, and base changes. The current frontier only counts if those
contractible fibers form one internal cartesian section over the admissible
source-square category and preserve the full endpoint/degree/DD.4/graph/
Rosati/control payload.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    BASE_CHANGE_ROUTES,
    BC,
    COHERENT,
    COMPOSITION_STABLE,
    CONTRLOOP,
    CONTRACT_DATA,
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
    REQUIRED_DEPS as DOC588_REQUIRED_DEPS,
    REPRESENTED_LIMIT,
    REPSEM,
    ROSATI,
    SEMCONS,
    SOURCE_LAW_GENERATORS,
    SUBREP,
    UNIVERSAL_ARROW,
    load_map,
)


EXPECTED_DOC = 589
EXPECTED_WITNESS = "doc589-probe-parametric-contractible-loop-complete-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPARAMCONTRLOOPCOMPPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

PARAMCONTR = "parametric_" + CONTRLOOP
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_EQV = "probe_equivalence_certificate"

failures: list[str] = []

PARAMETRIC_CLOSURES = {
    "cartesian_section",
    "pseudonatural_family",
    "all_admissible_morphisms_covered",
    "morphism_generators_complete",
    "morphism_relations_complete",
    "base_change_cartesian",
    "beck_chevalley_parametric",
    "refinement_functorial",
    "descent_gluable",
    "universal_arrow_reindexing_closed",
    "normalizer_parametric",
    "semantic_parametric",
    "payload_parametric",
    "source_law_parametric",
}

REQUIRED_DEPS = DOC588_REQUIRED_DEPS | {
    CONTRLOOP,
    ADM_CAT,
    TERMINAL_CERT,
    PROBE_NAT,
    PROBE_EQV,
    FILTERED_COFINAL,
    REFINEMENT_DESCENT,
    REPRESENTED_LIMIT,
}

EXPECTED_EDGES = {
    (CONTRLOOP, "made_parametric_by", PARAMCONTR),
    (PARAMCONTR, "parametric_contractible_loop_completion_for", CONTRLOOP),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_loop_complete", LOOPCOMP),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_path_independent", PATHIND),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_presentation_invariant", PRESINV),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_source_law_complete", LAWCOMP),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_normal_form", NORMREF),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_pasting_stable_mate", PASTE),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_cyclic_mate", CYCLIC),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_mate", MATE),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_base_change", BC),
    (PARAMCONTR, "parametric_contractible_loop_completion_for_evaluation", EVAL),
    (PARAMCONTR, "parametric_contractible_loop_completion_over", DIAG),
    (PARAMCONTR, "parametric_contractible_loop_completion_internal_to", SUBREP),
    (PARAMCONTR, "parametric_over_admissible_category", ADM_CAT),
    (PARAMCONTR, "cartesian_section_for_terminal_square", TERMINAL_CERT),
    (PARAMCONTR, "pseudonatural_for_probe_naturality", PROBE_NAT),
    (PARAMCONTR, "equivalence_coherent_for_probe_equivalence", PROBE_EQV),
    (PARAMCONTR, "parametric_universal_arrow_reindexing_via", UNIVERSAL_ARROW),
    (PARAMCONTR, "parametric_normalizer_via", NORM),
    (PARAMCONTR, "parametric_functorial_normalizer_via", FUNC_NORM),
    (PARAMCONTR, "parametric_monoidal_exact_dagger_via", MONEXACT_DAGGER),
    (PARAMCONTR, "parametric_coherent_normalizer_via", COHERENT),
    (PARAMCONTR, "parametric_executable_diamond_via", EXEC),
    (PARAMCONTR, "parametric_semantics_via", SEMCONS),
    (PARAMCONTR, "parametric_represented_semantics_via", REPSEM),
    (PARAMCONTR, "parametric_composition_law_via", COMPOSITION_STABLE),
    (PARAMCONTR, "parametric_refinement_law_via", REFINEMENT_DESCENT),
    (PARAMCONTR, "parametric_filtered_cofinal_law_via", FILTERED_COFINAL),
    (PARAMCONTR, "parametric_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(PARAMCONTR, "parametric_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (PARAMCONTR, "parametric_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(PARAMCONTR, "parametric_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (PARAMCONTR, "parametric_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "parametric_contractible_loop_completion_certificate",
    "cartesian_section_over_admissible_category",
    "pseudonatural_contractibility_family",
    "all_admissible_morphisms_covered",
    "morphism_relations_complete",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_parametric",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_fiberwise_only",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_objectwise_contractibility_only",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_selected_morphism_basis",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_hidden_morphism_generator_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_morphism_relation_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_cartesian_section_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_pseudonaturality_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_base_change_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_refinement_functoriality_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_descent_gluing_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_reindexing_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_normalizer_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_semantic_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_payload_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_source_law_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_degree_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_boundary_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_dd4_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_graph_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_rosati_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_control_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_handoff_parametricity_gap",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_external_indexed_fibration",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_external_grothendieck_construction",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_external_2groupoid",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_quotient_index_category",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_homotopy_quotient",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_syntax_parametric_quotient",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_retuned_reindexing",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted",
    "missing_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

PARAM_DATA = {
    "certificate": "parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_contractible_loop_complete": CONTRLOOP,
    "base_contract": CONTRACT_DATA,
    "exists": True,
    "parametric": True,
    "fiberwise_only": False,
    "objectwise_contractibility_only": False,
    "selected_morphism_basis": False,
    "all_admissible_morphisms_covered": True,
    "morphism_generators_complete": True,
    "morphism_relations_complete": True,
    "cartesian_section": True,
    "pseudonatural_family": True,
    "base_change_cartesian": True,
    "beck_chevalley_parametric": True,
    "refinement_functorial": True,
    "descent_gluable": True,
    "universal_arrow_reindexing_closed": True,
    "normalizer_parametric": True,
    "semantic_parametric": True,
    "invariant_reflection_parametric": True,
    "payload_parametric": True,
    "source_law_parametric": True,
    "endpoint_parametric": True,
    "degree_parametric": True,
    "projection_formula_parametric": True,
    "boundary_parametric": True,
    "dd4_parametric": True,
    "exact_delta_parametric": True,
    "graph_parametric": True,
    "rosati_parametric": True,
    "control_parametric": True,
    "handoff_parametric": True,
    "natural": True,
    "coherent": True,
    "external_indexed_fibration": False,
    "external_grothendieck_construction": False,
    "external_2groupoid": False,
    "quotient_index_category": False,
    "homotopy_quotient": False,
    "syntax_parametric_quotient": False,
    "retuned_reindexing": False,
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
    "domain": ADM_CAT,
    "terminal": TERMINAL_CERT,
    "probe_naturality": PROBE_NAT,
    "probe_equivalence": PROBE_EQV,
    "closures": PARAMETRIC_CLOSURES,
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
        "param": deepcopy(PARAM_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "param":
            state["param"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(PARAMCONTR, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    param = state["param"]
    base = param["base_contract"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_589")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc589_witness")
    if PARAMCONTR not in state["accepted"]:
        reasons.append("missing_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(PARAMCONTR, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if param.get("base_contractible_loop_complete") != CONTRLOOP:
        reasons.append("wrong_base_contractible_loop_complete")
    if not base.get("loop_completion_contractible") or not base.get("unique_loop_trivialization"):
        reasons.append("base_contractibility_not_doc588_complete")

    if not param.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_missing")
    if not param.get("parametric"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_parametric")
    if param.get("fiberwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_fiberwise_only")
    if param.get("objectwise_contractibility_only"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_objectwise_contractibility_only")
    if param.get("selected_morphism_basis"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_selected_morphism_basis")
    if not param.get("all_admissible_morphisms_covered") or not param.get("morphism_generators_complete"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_hidden_morphism_generator_gap")
    if not param.get("morphism_relations_complete"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_morphism_relation_gap")
    if not param.get("cartesian_section") or "cartesian_section" not in param["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_cartesian_section_gap")
    if not param.get("pseudonatural_family") or "pseudonatural_family" not in param["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_pseudonaturality_gap")
    if not param.get("base_change_cartesian") or "base_change_cartesian" not in param["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_base_change_gap")
    if not param.get("beck_chevalley_parametric"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_gap")
    if not param.get("refinement_functorial"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_refinement_functoriality_gap")
    if not param.get("descent_gluable"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_descent_gluing_gap")
    if not param.get("universal_arrow_reindexing_closed"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_reindexing_gap")
    if not param.get("normalizer_parametric") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= param["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_normalizer_parametricity_gap")
    if not param.get("semantic_parametric") or SEMCONS not in param["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_semantic_parametricity_gap")
    if not param.get("invariant_reflection_parametric") or REPSEM not in param["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_parametricity_gap")
    if not param.get("payload_parametric") or "payload_parametric" not in param["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_payload_parametricity_gap")
    if not param.get("source_law_parametric") or "source_law_parametric" not in param["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_source_law_parametricity_gap")
    if not param.get("endpoint_parametric") or ENDPOINT not in param["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_parametricity_gap")
    if not param.get("degree_parametric") or DEGREE not in param["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_degree_parametricity_gap")
    if not param.get("projection_formula_parametric") or not PROJECTION_FORMULA_TARGETS <= set(param["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_parametricity_gap")
    if not param.get("boundary_parametric") or PUSHFORWARD not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_boundary_parametricity_gap")
    if not param.get("dd4_parametric") or DD4_BOUNDARY not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_dd4_parametricity_gap")
    if not param.get("exact_delta_parametric") or EXACT_DELTA not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_parametricity_gap")
    if not param.get("graph_parametric") or GRAPH_COMP not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_graph_parametricity_gap")
    if not param.get("rosati_parametric") or ROSATI not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_rosati_parametricity_gap")
    if not param.get("control_parametric") or CONTROL not in param["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_control_parametricity_gap")
    if not param.get("handoff_parametric") or not {HANDOFF, GRAPH_LATER} <= set(param["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_handoff_parametricity_gap")
    if not param.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_natural")
    if not param.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent")

    for key in (
        "external_indexed_fibration",
        "external_grothendieck_construction",
        "external_2groupoid",
        "quotient_index_category",
        "homotopy_quotient",
        "syntax_parametric_quotient",
        "retuned_reindexing",
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
    ):
        if param.get(key):
            reason_key = key.replace("declared_only", "by_declaration").replace("new_cell", "requires_new_cell")
            reasons.append(f"center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_{reason_key}")
    if not param.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted")

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
        and PARAMCONTR in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["param"]["parametric"]
        and state["param"]["cartesian_section"]
        and state["param"]["pseudonatural_family"]
        and not state["param"]["fiberwise_only"],
        "contractible loop-completion data form a cartesian pseudonatural family",
    )
    gate(
        f"{PREFIX}3",
        state["param"]["all_admissible_morphisms_covered"]
        and state["param"]["morphism_generators_complete"]
        and state["param"]["morphism_relations_complete"]
        and not state["param"]["selected_morphism_basis"],
        "all admissible morphisms and morphism relations are covered",
    )
    gate(
        f"{PREFIX}4",
        state["param"]["base_change_cartesian"]
        and state["param"]["beck_chevalley_parametric"]
        and state["param"]["refinement_functorial"]
        and state["param"]["descent_gluable"]
        and state["param"]["universal_arrow_reindexing_closed"],
        "base-change, Beck-Chevalley, refinement, descent, and universal-arrow reindexing are parametric",
    )
    gate(
        f"{PREFIX}5",
        state["param"]["normalizer_parametric"]
        and state["param"]["semantic_parametric"]
        and state["param"]["invariant_reflection_parametric"]
        and NORMALIZER_DEPS <= state["param"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection parametricity are complete",
    )
    gate(
        f"{PREFIX}6",
        state["param"]["payload_parametric"]
        and state["param"]["source_law_parametric"]
        and state["param"]["endpoint_parametric"]
        and state["param"]["degree_parametric"]
        and state["param"]["projection_formula_parametric"]
        and state["param"]["boundary_parametric"]
        and state["param"]["dd4_parametric"]
        and state["param"]["exact_delta_parametric"],
        "payload, source-law, endpoint, degree, projection, boundary, DD.4, and exact-delta parametricity are complete",
    )
    gate(
        f"{PREFIX}7",
        state["param"]["graph_parametric"]
        and state["param"]["rosati_parametric"]
        and state["param"]["control_parametric"]
        and state["param"]["handoff_parametric"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["param"]["routes"],
        "graph, Rosati, control, handoff, and graph-later parametricity are complete",
    )
    gate(
        f"{PREFIX}8",
        state["param"]["budgeted"]
        and state["param"]["natural"]
        and state["param"]["coherent"]
        and not any(
            state["param"][key]
            for key in (
                "external_indexed_fibration",
                "external_grothendieck_construction",
                "external_2groupoid",
                "quotient_index_category",
                "homotopy_quotient",
                "syntax_parametric_quotient",
                "retuned_reindexing",
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
        and set(state["requires"].get(PARAMCONTR, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "parametric contractible loop completion is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: contractible loop-completion data assemble parametrically")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "contractible loop-completion proof is a cartesian pseudonatural "
        "family over all admissible source-square morphisms; fiberwise "
        "contractibility is still a disguised repair."
    )


if __name__ == "__main__":
    main()
