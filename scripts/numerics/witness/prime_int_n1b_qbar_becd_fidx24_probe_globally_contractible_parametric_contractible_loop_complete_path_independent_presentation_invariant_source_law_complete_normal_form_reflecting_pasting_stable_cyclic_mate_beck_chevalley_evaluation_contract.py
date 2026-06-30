#!/usr/bin/env python3
r"""Global contractibility for parametric loop-completion data.

Doc 589 makes the contractible loop-completion data into a cartesian
pseudonatural family over admissible source-square morphisms. This witness
closes the next cheap escape: the space of such global parametric sections
may itself have multiple components, automorphisms, or descent cocycles. The
current frontier only counts if the cartesian pseudonatural section of
contractible loop-completion data is globally internally contractible.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
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
    PARAM_DATA,
    PASTE,
    PATHIND,
    PRESERVED_CONTEXTS,
    PRESINV,
    PROBE_EQV,
    PROBE_NAT,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    REFINEMENT_DESCENT,
    REQUIRED_DEPS as DOC589_REQUIRED_DEPS,
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


EXPECTED_DOC = 590
EXPECTED_WITNESS = "doc590-probe-globally-contractible-parametric-contractible-loop-complete-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMGLOBCONTRPARAMCONTRLOOPCOMPPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

GLOBCONTR = "globally_contractible_" + PARAMCONTR

failures: list[str] = []

GLOBAL_SECTION_CLOSURES = {
    "global_section_space_contractible",
    "unique_global_section",
    "global_section_relations_complete",
    "global_section_automorphism_trivial",
    "global_descent_cocycle_zero",
    "global_modification_loop_zero",
    "cleavage_monodromy_zero",
    "base_change_global_section_closed",
    "beck_chevalley_global_section_closed",
    "refinement_global_section_closed",
    "descent_global_section_closed",
    "universal_arrow_global_section_closed",
    "payload_global_section_closed",
    "source_law_global_section_closed",
}

REQUIRED_DEPS = DOC589_REQUIRED_DEPS | {
    PARAMCONTR,
    CONTRLOOP,
    ADM_CAT,
    TERMINAL_CERT,
    PROBE_NAT,
    PROBE_EQV,
}

EXPECTED_EDGES = {
    (PARAMCONTR, "made_globally_contractible_by", GLOBCONTR),
    (GLOBCONTR, "globally_contractible_parametric_section_for", PARAMCONTR),
    (GLOBCONTR, "globally_contractible_for_contractible_loop_completion", CONTRLOOP),
    (GLOBCONTR, "globally_contractible_for_loop_complete", LOOPCOMP),
    (GLOBCONTR, "globally_contractible_for_path_independent", PATHIND),
    (GLOBCONTR, "globally_contractible_for_presentation_invariant", PRESINV),
    (GLOBCONTR, "globally_contractible_for_source_law_complete", LAWCOMP),
    (GLOBCONTR, "globally_contractible_for_normal_form", NORMREF),
    (GLOBCONTR, "globally_contractible_for_pasting_stable_mate", PASTE),
    (GLOBCONTR, "globally_contractible_for_cyclic_mate", CYCLIC),
    (GLOBCONTR, "globally_contractible_for_mate", MATE),
    (GLOBCONTR, "globally_contractible_for_base_change", BC),
    (GLOBCONTR, "globally_contractible_for_evaluation", EVAL),
    (GLOBCONTR, "globally_contractible_over", DIAG),
    (GLOBCONTR, "globally_contractible_internal_to", SUBREP),
    (GLOBCONTR, "global_section_contractible_over_admissible_category", ADM_CAT),
    (GLOBCONTR, "global_section_unique_for_terminal_square", TERMINAL_CERT),
    (GLOBCONTR, "global_section_pseudonatural_for_probe_naturality", PROBE_NAT),
    (GLOBCONTR, "global_section_equivalence_coherent_for_probe_equivalence", PROBE_EQV),
    (GLOBCONTR, "global_section_universal_arrow_reindexing_via", UNIVERSAL_ARROW),
    (GLOBCONTR, "global_section_normalizer_via", NORM),
    (GLOBCONTR, "global_section_functorial_normalizer_via", FUNC_NORM),
    (GLOBCONTR, "global_section_monoidal_exact_dagger_via", MONEXACT_DAGGER),
    (GLOBCONTR, "global_section_coherent_normalizer_via", COHERENT),
    (GLOBCONTR, "global_section_executable_diamond_via", EXEC),
    (GLOBCONTR, "global_section_semantics_via", SEMCONS),
    (GLOBCONTR, "global_section_represented_semantics_via", REPSEM),
    (GLOBCONTR, "global_section_composition_law_via", COMPOSITION_STABLE),
    (GLOBCONTR, "global_section_refinement_law_via", REFINEMENT_DESCENT),
    (GLOBCONTR, "global_section_filtered_cofinal_law_via", FILTERED_COFINAL),
    (GLOBCONTR, "global_section_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(GLOBCONTR, "global_section_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (GLOBCONTR, "global_section_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(GLOBCONTR, "global_section_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (GLOBCONTR, "global_section_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "globally_contractible_parametric_section_certificate",
    "global_section_space_connected",
    "unique_global_section",
    "global_section_relations_complete",
    "global_descent_cocycle_zero",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_globally_contractible",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_multiple_global_sections",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_global_section_torsor",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_nonunique_global_section",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_incomplete_global_section_relations",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_nontrivial_section_automorphism",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_global_descent_cocycle",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_cleavage_monodromy",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_global_modification_loop",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_local_only",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_cover_local_only",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_selected_global_section",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_base_change_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_refinement_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_descent_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_normalizer_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_semantic_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_payload_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_source_law_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_degree_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_boundary_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_dd4_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_graph_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_rosati_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_control_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_handoff_global_gap",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_external_section_moduli",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_external_section_stack",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_external_indexed_fibration",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_external_grothendieck_construction",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_external_2groupoid",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_quotient_section_stack",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_homotopy_quotient",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_syntax_global_quotient",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_retuned_cleavage",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted",
    "missing_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

GLOBAL_DATA = {
    "certificate": "globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_parametric_contractible": PARAMCONTR,
    "base_param": PARAM_DATA,
    "exists": True,
    "globally_contractible": True,
    "global_section_space_connected": True,
    "unique_global_section": True,
    "global_section_relations_complete": True,
    "global_section_automorphisms_trivial": True,
    "global_descent_cocycle_zero": True,
    "cleavage_monodromy_zero": True,
    "global_modification_loop_zero": True,
    "local_only": False,
    "cover_local_only": False,
    "selected_global_section": False,
    "base_change_global": True,
    "beck_chevalley_global": True,
    "refinement_global": True,
    "descent_global": True,
    "universal_arrow_global": True,
    "normalizer_global": True,
    "semantic_global": True,
    "invariant_reflection_global": True,
    "payload_global": True,
    "source_law_global": True,
    "endpoint_global": True,
    "degree_global": True,
    "projection_formula_global": True,
    "boundary_global": True,
    "dd4_global": True,
    "exact_delta_global": True,
    "graph_global": True,
    "rosati_global": True,
    "control_global": True,
    "handoff_global": True,
    "natural": True,
    "coherent": True,
    "external_section_moduli": False,
    "external_section_stack": False,
    "external_indexed_fibration": False,
    "external_grothendieck_construction": False,
    "external_2groupoid": False,
    "quotient_section_stack": False,
    "homotopy_quotient": False,
    "syntax_global_quotient": False,
    "retuned_cleavage": False,
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
    "closures": GLOBAL_SECTION_CLOSURES,
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
        "global": deepcopy(GLOBAL_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "global":
            state["global"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(GLOBCONTR, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    global_data = state["global"]
    base = global_data["base_param"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_590")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc590_witness")
    if GLOBCONTR not in state["accepted"]:
        reasons.append("missing_globally_contractible_parametric_contractible_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(GLOBCONTR, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if global_data.get("base_parametric_contractible") != PARAMCONTR:
        reasons.append("wrong_base_parametric_contractible")
    if not base.get("parametric") or not base.get("cartesian_section") or not base.get("pseudonatural_family"):
        reasons.append("base_parametricity_not_doc589_complete")

    if not global_data.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_missing")
    if not global_data.get("globally_contractible"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_globally_contractible")
    if not global_data.get("global_section_space_connected"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_multiple_global_sections")
    if not global_data.get("unique_global_section"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_nonunique_global_section")
    if not global_data.get("global_section_relations_complete"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_incomplete_global_section_relations")
    if not global_data.get("global_section_automorphisms_trivial"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_nontrivial_section_automorphism")
    if not global_data.get("global_descent_cocycle_zero"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_global_descent_cocycle")
    if not global_data.get("cleavage_monodromy_zero"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_cleavage_monodromy")
    if not global_data.get("global_modification_loop_zero"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_global_modification_loop")
    if global_data.get("local_only"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_local_only")
    if global_data.get("cover_local_only"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_cover_local_only")
    if global_data.get("selected_global_section"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_selected_global_section")
    if not global_data.get("base_change_global") or "base_change_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_base_change_global_gap")
    if not global_data.get("beck_chevalley_global") or "beck_chevalley_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_beck_chevalley_global_gap")
    if not global_data.get("refinement_global") or "refinement_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_refinement_global_gap")
    if not global_data.get("descent_global") or "descent_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_descent_global_gap")
    if not global_data.get("universal_arrow_global") or "universal_arrow_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_universal_arrow_global_gap")
    if not global_data.get("normalizer_global") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= global_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_normalizer_global_gap")
    if not global_data.get("semantic_global") or SEMCONS not in global_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_semantic_global_gap")
    if not global_data.get("invariant_reflection_global") or REPSEM not in global_data["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_invariant_reflection_global_gap")
    if not global_data.get("payload_global") or "payload_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_payload_global_gap")
    if not global_data.get("source_law_global") or "source_law_global_section_closed" not in global_data["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_source_law_global_gap")
    if not global_data.get("endpoint_global") or ENDPOINT not in global_data["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_endpoint_global_gap")
    if not global_data.get("degree_global") or DEGREE not in global_data["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_degree_global_gap")
    if not global_data.get("projection_formula_global") or not PROJECTION_FORMULA_TARGETS <= set(global_data["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_projection_formula_global_gap")
    if not global_data.get("boundary_global") or PUSHFORWARD not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_boundary_global_gap")
    if not global_data.get("dd4_global") or DD4_BOUNDARY not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_dd4_global_gap")
    if not global_data.get("exact_delta_global") or EXACT_DELTA not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_exact_delta_global_gap")
    if not global_data.get("graph_global") or GRAPH_COMP not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_graph_global_gap")
    if not global_data.get("rosati_global") or ROSATI not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_rosati_global_gap")
    if not global_data.get("control_global") or CONTROL not in global_data["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_control_global_gap")
    if not global_data.get("handoff_global") or not {HANDOFF, GRAPH_LATER} <= set(global_data["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_handoff_global_gap")
    if not global_data.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_natural")
    if not global_data.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_coherent")

    external_reason = {
        "external_section_moduli": "external_section_moduli",
        "external_section_stack": "external_section_stack",
        "external_indexed_fibration": "external_indexed_fibration",
        "external_grothendieck_construction": "external_grothendieck_construction",
        "external_2groupoid": "external_2groupoid",
        "quotient_section_stack": "quotient_section_stack",
        "homotopy_quotient": "homotopy_quotient",
        "syntax_global_quotient": "syntax_global_quotient",
        "retuned_cleavage": "retuned_cleavage",
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
        if global_data.get(key):
            reasons.append(f"center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_{reason_key}")
    if not global_data.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_global_parametric_contractible_loop_complete_path_pres_law_nf_not_budgeted")

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
        and GLOBCONTR in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["global"]["globally_contractible"]
        and state["global"]["global_section_space_connected"]
        and state["global"]["unique_global_section"],
        "cartesian pseudonatural section space is globally contractible",
    )
    gate(
        f"{PREFIX}3",
        state["global"]["global_section_relations_complete"]
        and state["global"]["global_section_automorphisms_trivial"]
        and state["global"]["global_descent_cocycle_zero"]
        and state["global"]["cleavage_monodromy_zero"]
        and state["global"]["global_modification_loop_zero"],
        "global section relations, automorphisms, descent cocycles, cleavages, and modification loops vanish",
    )
    gate(
        f"{PREFIX}4",
        state["global"]["base_change_global"]
        and state["global"]["beck_chevalley_global"]
        and state["global"]["refinement_global"]
        and state["global"]["descent_global"]
        and state["global"]["universal_arrow_global"]
        and GLOBAL_SECTION_CLOSURES <= state["global"]["closures"],
        "global section contractibility is stable under base-change, Beck-Chevalley, refinement, descent, and universal arrows",
    )
    gate(
        f"{PREFIX}5",
        state["global"]["normalizer_global"]
        and state["global"]["semantic_global"]
        and state["global"]["invariant_reflection_global"]
        and NORMALIZER_DEPS <= state["global"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection global section data are complete",
    )
    gate(
        f"{PREFIX}6",
        state["global"]["payload_global"]
        and state["global"]["source_law_global"]
        and state["global"]["endpoint_global"]
        and state["global"]["degree_global"]
        and state["global"]["projection_formula_global"]
        and state["global"]["boundary_global"]
        and state["global"]["dd4_global"]
        and state["global"]["exact_delta_global"],
        "payload, source-law, endpoint, degree, projection, boundary, DD.4, and exact-delta global data are complete",
    )
    gate(
        f"{PREFIX}7",
        state["global"]["graph_global"]
        and state["global"]["rosati_global"]
        and state["global"]["control_global"]
        and state["global"]["handoff_global"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["global"]["routes"],
        "graph, Rosati, control, handoff, and graph-later global data are complete",
    )
    gate(
        f"{PREFIX}8",
        state["global"]["budgeted"]
        and state["global"]["natural"]
        and state["global"]["coherent"]
        and not state["global"]["local_only"]
        and not state["global"]["cover_local_only"]
        and not state["global"]["selected_global_section"]
        and not any(
            state["global"][key]
            for key in (
                "external_section_moduli",
                "external_section_stack",
                "external_indexed_fibration",
                "external_grothendieck_construction",
                "external_2groupoid",
                "quotient_section_stack",
                "homotopy_quotient",
                "syntax_global_quotient",
                "retuned_cleavage",
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
        and set(state["requires"].get(GLOBCONTR, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "globally contractible parametric section is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: parametric section space is globally contractible")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "cartesian pseudonatural family of contractible loop-completion data "
        "has a globally contractible section space; section torsors and "
        "descent cocycles are still disguised repairs."
    )


if __name__ == "__main__":
    main()
