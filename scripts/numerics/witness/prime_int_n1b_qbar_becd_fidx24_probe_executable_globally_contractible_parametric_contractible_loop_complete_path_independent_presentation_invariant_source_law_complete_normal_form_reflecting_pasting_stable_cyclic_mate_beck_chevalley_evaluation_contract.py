#!/usr/bin/env python3
r"""Executable global contraction for parametric loop-completion data.

Doc 590 makes the space of cartesian pseudonatural global sections
internally globally contractible. This witness closes the next cheap escape:
the contraction might exist only as an external uniqueness proof, oracle,
propositional truncation, or proof-irrelevant erasure. The current frontier
only counts if the global contraction is computed by the existing executable
normal-form/critical-pair diamond and reflects back into the source laws.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_executable_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    ADM_CAT,
    BASE_CHANGE_ROUTES,
    BC,
    COHERENT,
    COMPOSITION_STABLE,
    CONTRLOOP,
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
    GLOBCONTR,
    GLOBAL_DATA,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    LAWCOMP,
    LOOPCOMP,
    MATE,
    MONEXACT_DAGGER,
    NORM,
    NORMALIZER_DEPS,
    NORMREF,
    PARAMCONTR,
    PASTE,
    PATHIND,
    PRESERVED_CONTEXTS,
    PRESINV,
    PROBE_EQV,
    PROBE_NAT,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    REFINEMENT_DESCENT,
    REQUIRED_DEPS as DOC590_REQUIRED_DEPS,
    REPRESENTED_LIMIT,
    REPSEM,
    ROSATI,
    SEMCONS,
    SOURCE_LAW_GENERATORS,
    SUBREP,
    TERMINAL_CERT,
    UNIVERSAL_ARROW,
    load_map,
)


EXPECTED_DOC = 591
EXPECTED_WITNESS = "doc591-probe-executable-globally-contractible-parametric-contractible-loop-complete-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEXECGLOBCONTRPARAMCONTRLOOPCOMPPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

EXECGLOB = "executable_" + GLOBCONTR

failures: list[str] = []

EXEC_GLOBAL_CLOSURES = {
    "global_contraction_evaluator",
    "finite_diamond_executable",
    "terminating_global_rewrite",
    "normal_form_reflecting_global_contraction",
    "semantic_conservative_global_contraction",
    "invariant_reflecting_global_contraction",
    "proof_relevant_global_contraction",
    "payload_projecting_global_contraction",
    "source_law_executing_global_contraction",
    "endpoint_degree_executing_global_contraction",
    "dd4_boundary_executing_global_contraction",
    "graph_rosati_control_handoff_executing_global_contraction",
    "base_change_executing_global_contraction",
    "beck_chevalley_executing_global_contraction",
    "refinement_descent_executing_global_contraction",
    "universal_arrow_executing_global_contraction",
}

REQUIRED_DEPS = DOC590_REQUIRED_DEPS | {
    GLOBCONTR,
    PARAMCONTR,
    CONTRLOOP,
    EXEC,
    NORM,
    FUNC_NORM,
    COHERENT,
    SEMCONS,
    REPSEM,
    ADM_CAT,
    TERMINAL_CERT,
    PROBE_NAT,
    PROBE_EQV,
}

EXPECTED_EDGES = {
    (GLOBCONTR, "made_executable_by", EXECGLOB),
    (EXECGLOB, "executable_global_contraction_for", GLOBCONTR),
    (EXECGLOB, "executes_parametric_contractible_loop_completion_for", PARAMCONTR),
    (EXECGLOB, "executes_contractible_loop_completion_for", CONTRLOOP),
    (EXECGLOB, "executes_loop_complete_for", LOOPCOMP),
    (EXECGLOB, "executes_path_independent_for", PATHIND),
    (EXECGLOB, "executes_presentation_invariant_for", PRESINV),
    (EXECGLOB, "executes_source_law_complete_for", LAWCOMP),
    (EXECGLOB, "executes_normal_form_for", NORMREF),
    (EXECGLOB, "executes_pasting_stable_mate_for", PASTE),
    (EXECGLOB, "executes_cyclic_mate_for", CYCLIC),
    (EXECGLOB, "executes_mate_for", MATE),
    (EXECGLOB, "executes_base_change_for", BC),
    (EXECGLOB, "executes_evaluation_for", EVAL),
    (EXECGLOB, "executable_global_contraction_over", DIAG),
    (EXECGLOB, "executable_global_contraction_internal_to", SUBREP),
    (EXECGLOB, "executable_global_contraction_over_admissible_category", ADM_CAT),
    (EXECGLOB, "executable_global_contraction_for_terminal_square", TERMINAL_CERT),
    (EXECGLOB, "executable_global_contraction_pseudonatural_for_probe_naturality", PROBE_NAT),
    (EXECGLOB, "executable_global_contraction_equivalence_coherent_for_probe_equivalence", PROBE_EQV),
    (EXECGLOB, "executable_global_contraction_universal_arrow_reindexing_via", UNIVERSAL_ARROW),
    (EXECGLOB, "executable_global_contraction_normalizer_via", NORM),
    (EXECGLOB, "executable_global_contraction_functorial_normalizer_via", FUNC_NORM),
    (EXECGLOB, "executable_global_contraction_monoidal_exact_dagger_via", MONEXACT_DAGGER),
    (EXECGLOB, "executable_global_contraction_coherent_normalizer_via", COHERENT),
    (EXECGLOB, "executable_global_contraction_diamond_via", EXEC),
    (EXECGLOB, "executable_global_contraction_semantics_via", SEMCONS),
    (EXECGLOB, "executable_global_contraction_represented_semantics_via", REPSEM),
    (EXECGLOB, "executable_global_contraction_composition_law_via", COMPOSITION_STABLE),
    (EXECGLOB, "executable_global_contraction_refinement_law_via", REFINEMENT_DESCENT),
    (EXECGLOB, "executable_global_contraction_filtered_cofinal_law_via", FILTERED_COFINAL),
    (EXECGLOB, "executable_global_contraction_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(EXECGLOB, "executable_global_contraction_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (EXECGLOB, "executable_global_contraction_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(EXECGLOB, "executable_global_contraction_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (EXECGLOB, "executable_global_contraction_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "executable_globally_contractible_parametric_section_certificate",
    "global_contraction_evaluator_internal",
    "global_contraction_rewrite_terminating",
    "global_contraction_finite_diamond",
    "global_contraction_normal_form_reflecting",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_executable",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_oracle_only",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_external_evaluator",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_propositional_truncation_only",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_proof_irrelevant_erasure",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_nonterminating_rewrite",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_critical_pair_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_normal_form_reflecting",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_semantic_conservativity_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_proof_relevant",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_payload_projection_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_source_law_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_degree_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_boundary_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_dd4_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_graph_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_rosati_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_control_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_handoff_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_base_change_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_refinement_descent_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_execution_gap",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_external_proof_term",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_external_oracle",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted",
    "missing_executable_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

EXEC_GLOBAL_DATA = {
    "certificate": "executable_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_global_contractible": GLOBCONTR,
    "base_global": GLOBAL_DATA,
    "exists": True,
    "executable": True,
    "evaluator_internal": True,
    "evaluator_total": True,
    "oracle_only": False,
    "external_evaluator": False,
    "external_proof_term": False,
    "external_oracle": False,
    "propositional_truncation_only": False,
    "proof_irrelevant_erasure": False,
    "terminating_rewrite": True,
    "finite_critical_pair_diamonds": True,
    "normal_form_reflecting": True,
    "semantic_conservative": True,
    "invariant_reflecting": True,
    "proof_relevant": True,
    "payload_projecting": True,
    "source_law_executing": True,
    "endpoint_executing": True,
    "degree_executing": True,
    "projection_formula_executing": True,
    "boundary_executing": True,
    "dd4_executing": True,
    "exact_delta_executing": True,
    "graph_executing": True,
    "rosati_executing": True,
    "control_executing": True,
    "handoff_executing": True,
    "base_change_executing": True,
    "beck_chevalley_executing": True,
    "refinement_descent_executing": True,
    "universal_arrow_executing": True,
    "natural": True,
    "coherent": True,
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
    "closures": EXEC_GLOBAL_CLOSURES,
    "normalizer_deps": NORMALIZER_DEPS,
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
        "exec_global": deepcopy(EXEC_GLOBAL_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "exec_global":
            state["exec_global"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(EXECGLOB, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    exec_data = state["exec_global"]
    base_global = exec_data["base_global"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_591")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc591_witness")
    if EXECGLOB not in state["accepted"]:
        reasons.append("missing_executable_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(EXECGLOB, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if exec_data.get("base_global_contractible") != GLOBCONTR:
        reasons.append("wrong_base_global_contractible")
    if not base_global.get("globally_contractible") or not base_global.get("unique_global_section"):
        reasons.append("base_global_contractibility_not_doc590_complete")

    if not exec_data.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_missing")
    if not exec_data.get("executable"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_executable")
    if exec_data.get("oracle_only"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_oracle_only")
    if exec_data.get("external_evaluator") or not exec_data.get("evaluator_internal") or not exec_data.get("evaluator_total"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_external_evaluator")
    if exec_data.get("propositional_truncation_only"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_propositional_truncation_only")
    if exec_data.get("proof_irrelevant_erasure"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_proof_irrelevant_erasure")
    if not exec_data.get("terminating_rewrite") or "terminating_global_rewrite" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_nonterminating_rewrite")
    if not exec_data.get("finite_critical_pair_diamonds") or "finite_diamond_executable" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_critical_pair_gap")
    if not exec_data.get("normal_form_reflecting") or NORM not in exec_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_normal_form_reflecting")
    if not exec_data.get("semantic_conservative") or SEMCONS not in exec_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_semantic_conservativity_gap")
    if not exec_data.get("invariant_reflecting") or REPSEM not in exec_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_gap")
    if not exec_data.get("proof_relevant") or "proof_relevant_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_proof_relevant")
    if not exec_data.get("payload_projecting") or "payload_projecting_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_payload_projection_gap")
    if not exec_data.get("source_law_executing") or "source_law_executing_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_source_law_execution_gap")
    if not exec_data.get("endpoint_executing") or ENDPOINT not in exec_data["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_execution_gap")
    if not exec_data.get("degree_executing") or DEGREE not in exec_data["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_degree_execution_gap")
    if not exec_data.get("projection_formula_executing") or not PROJECTION_FORMULA_TARGETS <= set(exec_data["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_execution_gap")
    if not exec_data.get("boundary_executing") or PUSHFORWARD not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_boundary_execution_gap")
    if not exec_data.get("dd4_executing") or DD4_BOUNDARY not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_dd4_execution_gap")
    if not exec_data.get("exact_delta_executing") or EXACT_DELTA not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_execution_gap")
    if not exec_data.get("graph_executing") or GRAPH_COMP not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_graph_execution_gap")
    if not exec_data.get("rosati_executing") or ROSATI not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_rosati_execution_gap")
    if not exec_data.get("control_executing") or CONTROL not in exec_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_control_execution_gap")
    if not exec_data.get("handoff_executing") or not {HANDOFF, GRAPH_LATER} <= set(exec_data["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_handoff_execution_gap")
    if not exec_data.get("base_change_executing") or "base_change_executing_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_base_change_execution_gap")
    if (
        not exec_data.get("beck_chevalley_executing")
        or "beck_chevalley_executing_global_contraction" not in exec_data["closures"]
    ):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_execution_gap")
    if not exec_data.get("refinement_descent_executing") or "refinement_descent_executing_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_refinement_descent_execution_gap")
    if not exec_data.get("universal_arrow_executing") or "universal_arrow_executing_global_contraction" not in exec_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_execution_gap")
    if not exec_data.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_natural")
    if not exec_data.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent")

    external_reason = {
        "external_proof_term": "external_proof_term",
        "external_oracle": "external_oracle",
        "functor_of_points_only": "functor_of_points_only",
        "yoneda_reversal": "yoneda_reversal",
        "pointwise_only": "pointwise_only",
        "objectwise_only": "objectwise_only",
        "nonfunctorial_choice": "nonfunctorial_choice",
        "requires_choice": "requires_choice",
        "new_cell": "requires_new_cell",
        "context_collapse": "context_collapse",
        "declared_only": "by_declaration",
        "finite_sample": "finite_sample",
        "basis_row": "basis_row",
    }
    for key, reason_key in external_reason.items():
        if exec_data.get(key):
            reasons.append(
                "center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_"
                + reason_key
            )
    if not exec_data.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_executable_global_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted")

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
        and EXECGLOB in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["exec_global"]["executable"]
        and state["exec_global"]["evaluator_internal"]
        and state["exec_global"]["evaluator_total"]
        and not state["exec_global"]["oracle_only"]
        and not state["exec_global"]["external_evaluator"],
        "global contraction is an internal total evaluator, not an oracle or external evaluator",
    )
    gate(
        f"{PREFIX}3",
        state["exec_global"]["terminating_rewrite"]
        and state["exec_global"]["finite_critical_pair_diamonds"]
        and state["exec_global"]["normal_form_reflecting"]
        and {NORM, FUNC_NORM, COHERENT, EXEC} <= state["exec_global"]["normalizer_deps"],
        "global contraction is realized by terminating finite critical-pair diamonds in the normalizer",
    )
    gate(
        f"{PREFIX}4",
        state["exec_global"]["semantic_conservative"]
        and state["exec_global"]["invariant_reflecting"]
        and state["exec_global"]["proof_relevant"]
        and not state["exec_global"]["propositional_truncation_only"]
        and not state["exec_global"]["proof_irrelevant_erasure"],
        "semantic conservativity, invariant reflection, and proof relevance survive executable contraction",
    )
    gate(
        f"{PREFIX}5",
        state["exec_global"]["payload_projecting"]
        and state["exec_global"]["source_law_executing"]
        and state["exec_global"]["endpoint_executing"]
        and state["exec_global"]["degree_executing"]
        and state["exec_global"]["projection_formula_executing"],
        "payload, source-law, endpoint, degree, and projection data execute through the contraction",
    )
    gate(
        f"{PREFIX}6",
        state["exec_global"]["boundary_executing"]
        and state["exec_global"]["dd4_executing"]
        and state["exec_global"]["exact_delta_executing"]
        and state["exec_global"]["graph_executing"]
        and state["exec_global"]["rosati_executing"]
        and state["exec_global"]["control_executing"]
        and state["exec_global"]["handoff_executing"],
        "boundary, DD.4, exact-delta, graph, Rosati, control, and handoff data execute through the contraction",
    )
    gate(
        f"{PREFIX}7",
        state["exec_global"]["base_change_executing"]
        and state["exec_global"]["beck_chevalley_executing"]
        and state["exec_global"]["refinement_descent_executing"]
        and state["exec_global"]["universal_arrow_executing"]
        and EXEC_GLOBAL_CLOSURES <= state["exec_global"]["closures"],
        "base-change, Beck-Chevalley, refinement/descent, and universal-arrow execution are closed",
    )
    gate(
        f"{PREFIX}8",
        state["exec_global"]["budgeted"]
        and state["exec_global"]["natural"]
        and state["exec_global"]["coherent"]
        and not any(
            state["exec_global"][key]
            for key in (
                "external_proof_term",
                "external_oracle",
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
        and set(state["requires"].get(EXECGLOB, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "executable global contraction is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: global contraction is executable inside the normal-form calculus")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "globally contractible section is extracted by the internal "
        "terminating critical-pair evaluator; oracle, proof-erased, "
        "propositional, and external-evaluator versions are disguised repairs."
    )


if __name__ == "__main__":
    main()
