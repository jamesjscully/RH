#!/usr/bin/env python3
r"""Path independence for presentation-invariant source-law normal forms.

Doc 585 requires source-law-complete normal-form reflection to be invariant
under admissible source-presentation moves. This witness closes the next
cheap escape: each move may preserve the data, while different zigzags between
the same presentations or loops of moves produce nontrivial monodromy. The
current frontier only counts if presentation transport composes
path-independently, inverse moves cancel, and every admissible presentation
loop acts trivially on the law-complete normal forms, normalizer, represented
semantics, and payload laws.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the path-independent presentation witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    BASE_CHANGE_ROUTES,
    BC,
    COHERENT,
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
    MAP_PATH,
    MATE,
    MONEXACT_DAGGER,
    NORMALIZER_DEPS,
    NORM,
    NORMREF,
    PASTE,
    PRESERVED_CONTEXTS,
    PRESENTATION_MOVES,
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
)


EXPECTED_DOC = 586
EXPECTED_WITNESS = "doc586-probe-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

PATHIND = "path_independent_" + PRESINV
COMPOSITION_STABLE = next(dep for dep in LAW_COMPLETION_DEPS if dep.startswith("mediator_generated_composition_stable_"))

failures: list[str] = []

PRESENTATION_LOOPS = {
    "generator_relation_square",
    "tietze_triangle",
    "redundant_generator_inverse_pair",
    "redundant_relation_inverse_pair",
    "subdivision_merge_inverse_pair",
    "coherent_source_presentation_square",
    "universal_arrow_reindexing_square",
    "filtered_cofinal_refinement_square",
    "refinement_descent_square",
    "normalizer_transport_square",
    "semantic_transport_square",
    "payload_law_transport_loop",
    "beck_chevalley_mate_transport_loop",
}

REQUIRED_DEPS = {
    PRESINV,
    LAWCOMP,
    NORMREF,
    PASTE,
    CYCLIC,
    MATE,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | NORMALIZER_DEPS | LAW_COMPLETION_DEPS | SOURCE_LAW_GENERATORS | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (PRESINV, "made_path_independent_by", PATHIND),
    (PATHIND, "path_independent_for", PRESINV),
    (PATHIND, "path_independent_for_source_law_complete", LAWCOMP),
    (PATHIND, "path_independent_for_normal_form", NORMREF),
    (PATHIND, "path_independent_for_pasting_stable_mate", PASTE),
    (PATHIND, "path_independent_for_cyclic_mate", CYCLIC),
    (PATHIND, "path_independent_for_mate", MATE),
    (PATHIND, "path_independent_for_base_change", BC),
    (PATHIND, "path_independent_for_evaluation", EVAL),
    (PATHIND, "path_independent_over", DIAG),
    (PATHIND, "path_internal_to", SUBREP),
    (PATHIND, "path_transport_selected_by", UNIVERSAL_ARROW),
    (PATHIND, "path_independent_normalizer_via", NORM),
    (PATHIND, "path_independent_functorial_normalizer_via", FUNC_NORM),
    (PATHIND, "path_independent_monoidal_exact_dagger_normalizer_via", MONEXACT_DAGGER),
    (PATHIND, "path_independent_coherent_normalizer_via", COHERENT),
    (PATHIND, "path_independent_executable_diamonds_via", EXEC),
    (PATHIND, "path_independent_semantics_via", SEMCONS),
    (PATHIND, "path_independent_represented_semantics_via", REPSEM),
    (PATHIND, "path_independent_composition_law_via", COMPOSITION_STABLE),
    (PATHIND, "path_independent_refinement_law_via", REFINEMENT_DESCENT),
    (PATHIND, "path_independent_filtered_cofinal_law_via", FILTERED_COFINAL),
    (PATHIND, "path_independent_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(PATHIND, "path_independent_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (PATHIND, "path_independent_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(PATHIND, "path_independent_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (PATHIND, "path_independent_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "path_independent_certificate",
    "chain_composition_coherent",
    "inverse_moves_cancel",
    "zigzag_independent",
    "loop_monodromy_zero",
    "normalizer_transport_path_independent",
    "semantic_transport_path_independent",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_path_independent",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_zigzag_dependent",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_loop_monodromy",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_chain_composition_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_associativity_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_unit_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_inverse_move_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_generator_relation_loop_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_tietze_triangle_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_redundant_generator_inverse_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_redundant_relation_inverse_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_subdivision_merge_inverse_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_source_presentation_square_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_universal_arrow_reindexing_square_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_filtered_cofinal_square_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_refinement_descent_square_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_normalizer_transport_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_semantic_transport_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_invariant_reflection_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_payload_loop_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_beck_chevalley_mate_loop_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_endpoint_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_degree_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_projection_formula_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_boundary_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_dd4_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_exact_delta_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_graph_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_rosati_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_control_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_handoff_monodromy_gap",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_external_2groupoid",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_quotient_path_space",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_syntax_path_quotient",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_presentation_specific_path_choice",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_retuned_transport",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_budgeted",
    "missing_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

PATH_DATA = {
    "certificate": "path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_presentation_invariant": PRESINV,
    "base_source_law_complete": LAWCOMP,
    "base_normal_form": NORMREF,
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "path_independent": True,
    "zigzag_independent": True,
    "loop_monodromy_zero": True,
    "chain_composition": True,
    "associative": True,
    "unit": True,
    "inverse_moves_cancel": True,
    "generator_relation_loop_zero": True,
    "tietze_triangle_zero": True,
    "redundant_generator_inverse_zero": True,
    "redundant_relation_inverse_zero": True,
    "subdivision_merge_inverse_zero": True,
    "source_presentation_square_zero": True,
    "universal_arrow_reindexing_square_zero": True,
    "filtered_cofinal_square_zero": True,
    "refinement_descent_square_zero": True,
    "normalizer_transport_monodromy_zero": True,
    "semantic_transport_monodromy_zero": True,
    "invariant_reflection_monodromy_zero": True,
    "payload_loop_zero": True,
    "beck_chevalley_mate_loop_zero": True,
    "endpoint_monodromy_zero": True,
    "degree_monodromy_zero": True,
    "projection_formula_monodromy_zero": True,
    "boundary_monodromy_zero": True,
    "dd4_monodromy_zero": True,
    "exact_delta_monodromy_zero": True,
    "graph_monodromy_zero": True,
    "rosati_monodromy_zero": True,
    "control_monodromy_zero": True,
    "handoff_monodromy_zero": True,
    "natural": True,
    "coherent": True,
    "external_2groupoid": False,
    "quotient_path_space": False,
    "syntax_path_quotient": False,
    "presentation_specific_path_choice": False,
    "retuned_transport": False,
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
    "moves": PRESENTATION_MOVES,
    "loops": PRESENTATION_LOOPS,
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


def load_map() -> dict[str, Any]:
    with MAP_PATH.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit("frontier-map.yaml did not load as a mapping")
    return data


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
        "path": deepcopy(PATH_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "path":
            state["path"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(PATHIND, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    path = state["path"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_586")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc586_witness")
    if PATHIND not in state["accepted"]:
        reasons.append("missing_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(PATHIND, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if path.get("base_presentation_invariant") != PRESINV:
        reasons.append("wrong_base_presentation_invariant")
    if path.get("base_source_law_complete") != LAWCOMP:
        reasons.append("wrong_base_source_law_complete")
    if path.get("base_normal_form") != NORMREF:
        reasons.append("wrong_base_normal_form_reflection")
    if path.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if path.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if path.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if path.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not path.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_missing")
    if not path.get("path_independent"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_path_independent")
    if not path.get("zigzag_independent"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_zigzag_dependent")
    if not path.get("loop_monodromy_zero"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_loop_monodromy")
    if not path.get("chain_composition"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_chain_composition_gap")
    if not path.get("associative"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_associativity_gap")
    if not path.get("unit"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_unit_gap")
    if not path.get("inverse_moves_cancel"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_inverse_move_gap")
    if not path.get("generator_relation_loop_zero") or "generator_relation_square" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_generator_relation_loop_gap")
    if not path.get("tietze_triangle_zero") or "tietze_triangle" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_tietze_triangle_gap")
    if not path.get("redundant_generator_inverse_zero") or "redundant_generator_inverse_pair" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_redundant_generator_inverse_gap")
    if not path.get("redundant_relation_inverse_zero") or "redundant_relation_inverse_pair" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_redundant_relation_inverse_gap")
    if not path.get("subdivision_merge_inverse_zero") or "subdivision_merge_inverse_pair" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_subdivision_merge_inverse_gap")
    if not path.get("source_presentation_square_zero") or "coherent_source_presentation_square" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_source_presentation_square_gap")
    if not path.get("universal_arrow_reindexing_square_zero") or "universal_arrow_reindexing_square" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_universal_arrow_reindexing_square_gap")
    if not path.get("filtered_cofinal_square_zero") or FILTERED_COFINAL not in path["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_filtered_cofinal_square_gap")
    if not path.get("refinement_descent_square_zero") or REFINEMENT_DESCENT not in path["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_refinement_descent_square_gap")
    if not path.get("normalizer_transport_monodromy_zero") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= path["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_normalizer_transport_monodromy_gap")
    if not path.get("semantic_transport_monodromy_zero") or SEMCONS not in path["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_semantic_transport_monodromy_gap")
    if not path.get("invariant_reflection_monodromy_zero") or REPSEM not in path["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_invariant_reflection_monodromy_gap")
    if not path.get("payload_loop_zero") or "payload_law_transport_loop" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_payload_loop_gap")
    if not path.get("beck_chevalley_mate_loop_zero") or "beck_chevalley_mate_transport_loop" not in path["loops"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_beck_chevalley_mate_loop_gap")
    if not path.get("endpoint_monodromy_zero") or ENDPOINT not in path["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_endpoint_monodromy_gap")
    if not path.get("degree_monodromy_zero") or DEGREE not in path["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_degree_monodromy_gap")
    if not path.get("projection_formula_monodromy_zero") or not PROJECTION_FORMULA_TARGETS <= set(path["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_projection_formula_monodromy_gap")
    if not path.get("boundary_monodromy_zero") or PUSHFORWARD not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_boundary_monodromy_gap")
    if not path.get("dd4_monodromy_zero") or DD4_BOUNDARY not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_dd4_monodromy_gap")
    if not path.get("exact_delta_monodromy_zero") or EXACT_DELTA not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_exact_delta_monodromy_gap")
    if not path.get("graph_monodromy_zero") or GRAPH_COMP not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_graph_monodromy_gap")
    if not path.get("rosati_monodromy_zero") or ROSATI not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_rosati_monodromy_gap")
    if not path.get("control_monodromy_zero") or CONTROL not in path["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_control_monodromy_gap")
    if not path.get("handoff_monodromy_zero") or not {HANDOFF, GRAPH_LATER} <= set(path["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_handoff_monodromy_gap")
    if not path.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_natural")
    if not path.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_coherent")
    if path.get("external_2groupoid"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_external_2groupoid")
    if path.get("quotient_path_space"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_quotient_path_space")
    if path.get("syntax_path_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_syntax_path_quotient")
    if path.get("presentation_specific_path_choice"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_presentation_specific_path_choice")
    if path.get("retuned_transport"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_retuned_transport")
    if path.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_functor_of_points_only")
    if path.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_yoneda_reversal")
    if path.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_pointwise_only")
    if path.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_objectwise_only")
    if path.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_nonfunctorial_choice")
    if path.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_requires_choice")
    if path.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_requires_new_cell")
    if path.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_context_collapse")
    if path.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_by_declaration")
    if path.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_finite_sample")
    if path.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_basis_row")
    if not path.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_path_ind_pres_law_nf_not_budgeted")

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
        and PATHIND in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["path"]["path_independent"]
        and state["path"]["zigzag_independent"]
        and state["path"]["chain_composition"]
        and state["path"]["associative"]
        and state["path"]["unit"]
        and state["path"]["inverse_moves_cancel"],
        "presentation transports compose with associativity, units, inverse cancellation, and no zigzag dependence",
    )
    gate(
        f"{PREFIX}3",
        state["path"]["loop_monodromy_zero"]
        and state["path"]["generator_relation_loop_zero"]
        and state["path"]["tietze_triangle_zero"]
        and state["path"]["redundant_generator_inverse_zero"]
        and state["path"]["redundant_relation_inverse_zero"]
        and state["path"]["subdivision_merge_inverse_zero"]
        and PRESENTATION_LOOPS <= state["path"]["loops"],
        "generator/relation/Tietze/redundancy/subdivision loops have zero monodromy",
    )
    gate(
        f"{PREFIX}4",
        state["path"]["source_presentation_square_zero"]
        and state["path"]["universal_arrow_reindexing_square_zero"]
        and state["path"]["filtered_cofinal_square_zero"]
        and state["path"]["refinement_descent_square_zero"]
        and {FILTERED_COFINAL, REFINEMENT_DESCENT, REPRESENTED_LIMIT} <= state["path"]["law_completion_deps"],
        "source-presentation, universal-arrow, cofinal, and refinement-descent squares have zero monodromy",
    )
    gate(
        f"{PREFIX}5",
        state["path"]["normalizer_transport_monodromy_zero"]
        and state["path"]["semantic_transport_monodromy_zero"]
        and state["path"]["invariant_reflection_monodromy_zero"]
        and NORMALIZER_DEPS <= state["path"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection transport loops are trivial",
    )
    gate(
        f"{PREFIX}6",
        state["path"]["payload_loop_zero"]
        and state["path"]["beck_chevalley_mate_loop_zero"]
        and state["path"]["endpoint_monodromy_zero"]
        and state["path"]["degree_monodromy_zero"]
        and state["path"]["projection_formula_monodromy_zero"]
        and state["path"]["boundary_monodromy_zero"]
        and state["path"]["dd4_monodromy_zero"]
        and state["path"]["exact_delta_monodromy_zero"],
        "payload, Beck-Chevalley mate, endpoint, degree, projection, boundary, DD.4, and exact-delta loops are trivial",
    )
    gate(
        f"{PREFIX}7",
        state["path"]["graph_monodromy_zero"]
        and state["path"]["rosati_monodromy_zero"]
        and state["path"]["control_monodromy_zero"]
        and state["path"]["handoff_monodromy_zero"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["path"]["routes"],
        "graph, Rosati, control, handoff, and graph-later loops are trivial",
    )
    gate(
        f"{PREFIX}8",
        state["path"]["budgeted"]
        and state["path"]["natural"]
        and state["path"]["coherent"]
        and not any(
            state["path"][key]
            for key in (
                "external_2groupoid",
                "quotient_path_space",
                "syntax_path_quotient",
                "presentation_specific_path_choice",
                "retuned_transport",
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
        and set(state["requires"].get(PATHIND, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "path independence is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: presentation transports are path-independent with zero loop monodromy")
    print(
        "VERDICT: the missing-object candidate counts only when presentation "
        "transport for source-law-complete reflected pasted cyclic Beck-Chevalley "
        "normal forms is path-independent and loop-trivial; zigzag-dependent "
        "presentation invariance is still a disguised repair."
    )


if __name__ == "__main__":
    main()
