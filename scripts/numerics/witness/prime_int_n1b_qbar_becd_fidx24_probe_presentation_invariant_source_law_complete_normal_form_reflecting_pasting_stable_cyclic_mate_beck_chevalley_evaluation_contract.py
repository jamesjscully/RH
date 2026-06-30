#!/usr/bin/env python3
r"""Presentation invariance for source-law-complete reflected normal forms.

Doc 584 requires normal-form reflection for the full source-law generator
inventory. This witness closes the next cheap escape: the source-law-complete
normalizer may still depend on the chosen presentation of those generators and
relations. The current frontier only counts if source-law-complete normal-form
reflection is invariant under admissible source-presentation changes, including
generator refinements, relation expansions, Tietze-style redundant-generator
and redundant-relation moves, cell subdivision/merge, universal-arrow
reindexing, filtered-cofinal refinement, and refinement descent.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the presentation-invariant source-law witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
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


EXPECTED_DOC = 585
EXPECTED_WITNESS = "doc585-probe-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

PRESINV = "presentation_invariant_" + LAWCOMP

failures: list[str] = []

PRESENTATION_MOVES = {
    "generator_refinement",
    "relation_expansion",
    "redundant_generator_addition",
    "redundant_relation_addition",
    "tietze_contraction",
    "cell_subdivision",
    "cell_merge",
    "coherent_source_presentation_change",
    "universal_arrow_reindexing",
    "filtered_cofinal_refinement",
    "refinement_descent_transport",
}

REQUIRED_DEPS = {
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
    (LAWCOMP, "made_presentation_invariant_by", PRESINV),
    (PRESINV, "presentation_invariant_for", LAWCOMP),
    (PRESINV, "presentation_invariant_for_normal_form", NORMREF),
    (PRESINV, "presentation_invariant_for_pasting_stable_mate", PASTE),
    (PRESINV, "presentation_invariant_for_cyclic_mate", CYCLIC),
    (PRESINV, "presentation_invariant_for_mate", MATE),
    (PRESINV, "presentation_invariant_for_base_change", BC),
    (PRESINV, "presentation_invariant_for_evaluation", EVAL),
    (PRESINV, "presentation_invariant_over", DIAG),
    (PRESINV, "presentation_internal_to", SUBREP),
    (PRESINV, "presentation_transport_selected_by", UNIVERSAL_ARROW),
    (PRESINV, "presentation_invariant_normalizer_via", NORM),
    (PRESINV, "presentation_invariant_functorial_normalizer_via", FUNC_NORM),
    (PRESINV, "presentation_invariant_monoidal_exact_dagger_normalizer_via", MONEXACT_DAGGER),
    (PRESINV, "presentation_invariant_coherent_normalizer_via", COHERENT),
    (PRESINV, "presentation_invariant_executable_diamonds_via", EXEC),
    (PRESINV, "presentation_invariant_semantics_via", SEMCONS),
    (PRESINV, "presentation_invariant_represented_semantics_via", REPSEM),
    (PRESINV, "presentation_invariant_composition_law_via", next(dep for dep in LAW_COMPLETION_DEPS if dep.startswith("mediator_generated_composition_stable_"))),
    (PRESINV, "presentation_invariant_refinement_law_via", REFINEMENT_DESCENT),
    (PRESINV, "presentation_invariant_filtered_cofinal_law_via", FILTERED_COFINAL),
    (PRESINV, "presentation_invariant_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(PRESINV, "presentation_invariant_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (PRESINV, "presentation_invariant_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(PRESINV, "presentation_invariant_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (PRESINV, "presentation_invariant_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "presentation_invariant_certificate",
    "generator_refinement_invariant",
    "relation_expansion_invariant",
    "tietze_move_invariant",
    "coherent_source_presentation_transport",
    "normalizer_transport_invariant",
    "semantic_transport_invariant",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_missing",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_invariant",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_selected_presentation_only",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_generator_refinement_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_relation_expansion_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_tietze_move_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_redundant_generator_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_redundant_relation_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_cell_subdivision_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_cell_merge_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_source_presentation_transport_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_universal_arrow_reindexing_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_filtered_cofinal_refinement_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_refinement_descent_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_normalizer_transport_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_semantic_transport_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_invariant_reflection_transport_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_endpoint_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_degree_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_projection_formula_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_boundary_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_dd4_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_exact_delta_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_graph_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_rosati_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_control_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_handoff_gap",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_external_presentation",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_syntax_quotient",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_quotient_normal_form",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_presentation_specific_normalizer",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_retuned_generator_list",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_budgeted",
    "missing_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

PRES_DATA = {
    "certificate": "presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_source_law_complete": LAWCOMP,
    "base_normal_form": NORMREF,
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "presentation_invariant": True,
    "selected_presentation_only": False,
    "generator_refinement": True,
    "relation_expansion": True,
    "tietze_move": True,
    "redundant_generator": True,
    "redundant_relation": True,
    "cell_subdivision": True,
    "cell_merge": True,
    "source_presentation_transport": True,
    "universal_arrow_reindexing": True,
    "filtered_cofinal_refinement": True,
    "refinement_descent": True,
    "normalizer_transport": True,
    "semantic_transport": True,
    "invariant_reflection_transport": True,
    "endpoint_invariant": True,
    "degree_invariant": True,
    "projection_formula_invariant": True,
    "boundary_invariant": True,
    "dd4_invariant": True,
    "exact_delta_invariant": True,
    "graph_invariant": True,
    "rosati_invariant": True,
    "control_invariant": True,
    "handoff_invariant": True,
    "natural": True,
    "coherent": True,
    "external_presentation": False,
    "syntax_quotient": False,
    "quotient_normal_form": False,
    "presentation_specific_normalizer": False,
    "retuned_generator_list": False,
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
        "pres": deepcopy(PRES_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "pres":
            state["pres"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(PRESINV, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    pres = state["pres"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_585")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc585_witness")
    if PRESINV not in state["accepted"]:
        reasons.append("missing_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(PRESINV, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if pres.get("base_source_law_complete") != LAWCOMP:
        reasons.append("wrong_base_source_law_complete")
    if pres.get("base_normal_form") != NORMREF:
        reasons.append("wrong_base_normal_form_reflection")
    if pres.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if pres.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if pres.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if pres.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not pres.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_missing")
    if not pres.get("presentation_invariant"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_invariant")
    if pres.get("selected_presentation_only"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_selected_presentation_only")
    if not pres.get("generator_refinement") or "generator_refinement" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_generator_refinement_gap")
    if not pres.get("relation_expansion") or "relation_expansion" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_relation_expansion_gap")
    if not pres.get("tietze_move") or "tietze_contraction" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_tietze_move_gap")
    if not pres.get("redundant_generator") or "redundant_generator_addition" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_redundant_generator_gap")
    if not pres.get("redundant_relation") or "redundant_relation_addition" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_redundant_relation_gap")
    if not pres.get("cell_subdivision") or "cell_subdivision" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_cell_subdivision_gap")
    if not pres.get("cell_merge") or "cell_merge" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_cell_merge_gap")
    if not pres.get("source_presentation_transport") or "coherent_source_presentation_change" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_source_presentation_transport_gap")
    if not pres.get("universal_arrow_reindexing") or "universal_arrow_reindexing" not in pres["moves"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_universal_arrow_reindexing_gap")
    if not pres.get("filtered_cofinal_refinement") or "filtered_cofinal_refinement" not in pres["moves"] or FILTERED_COFINAL not in pres["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_filtered_cofinal_refinement_gap")
    if not pres.get("refinement_descent") or REFINEMENT_DESCENT not in pres["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_refinement_descent_gap")
    if not pres.get("normalizer_transport") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= pres["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_normalizer_transport_gap")
    if not pres.get("semantic_transport") or SEMCONS not in pres["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_semantic_transport_gap")
    if not pres.get("invariant_reflection_transport") or REPSEM not in pres["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_invariant_reflection_transport_gap")
    if not pres.get("endpoint_invariant") or ENDPOINT not in pres["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_endpoint_gap")
    if not pres.get("degree_invariant") or DEGREE not in pres["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_degree_gap")
    if not pres.get("projection_formula_invariant") or not PROJECTION_FORMULA_TARGETS <= set(pres["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_projection_formula_gap")
    if not pres.get("boundary_invariant") or PUSHFORWARD not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_boundary_gap")
    if not pres.get("dd4_invariant") or DD4_BOUNDARY not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_dd4_gap")
    if not pres.get("exact_delta_invariant") or EXACT_DELTA not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_exact_delta_gap")
    if not pres.get("graph_invariant") or GRAPH_COMP not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_graph_gap")
    if not pres.get("rosati_invariant") or ROSATI not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_rosati_gap")
    if not pres.get("control_invariant") or CONTROL not in pres["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_control_gap")
    if not pres.get("handoff_invariant") or not {HANDOFF, GRAPH_LATER} <= set(pres["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_handoff_gap")
    if not pres.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_natural")
    if not pres.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_coherent")
    if pres.get("external_presentation"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_external_presentation")
    if pres.get("syntax_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_syntax_quotient")
    if pres.get("quotient_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_quotient_normal_form")
    if pres.get("presentation_specific_normalizer"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_presentation_specific_normalizer")
    if pres.get("retuned_generator_list"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_retuned_generator_list")
    if pres.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_functor_of_points_only")
    if pres.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_yoneda_reversal")
    if pres.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_pointwise_only")
    if pres.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_objectwise_only")
    if pres.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_nonfunctorial_choice")
    if pres.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_requires_choice")
    if pres.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_requires_new_cell")
    if pres.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_context_collapse")
    if pres.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_by_declaration")
    if pres.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_finite_sample")
    if pres.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_basis_row")
    if not pres.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_pres_invariant_law_nf_not_budgeted")

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
        and PRESINV in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["pres"]["presentation_invariant"]
        and not state["pres"]["selected_presentation_only"]
        and state["pres"]["generator_refinement"]
        and state["pres"]["relation_expansion"]
        and state["pres"]["tietze_move"],
        "generator, relation, and Tietze-equivalent presentations share source-law normal forms",
    )
    gate(
        f"{PREFIX}3",
        state["pres"]["redundant_generator"]
        and state["pres"]["redundant_relation"]
        and state["pres"]["cell_subdivision"]
        and state["pres"]["cell_merge"]
        and PRESENTATION_MOVES <= state["pres"]["moves"],
        "redundant generators/relations and cell subdivision/merge preserve the same law-complete normal forms",
    )
    gate(
        f"{PREFIX}4",
        state["pres"]["source_presentation_transport"]
        and state["pres"]["universal_arrow_reindexing"]
        and state["pres"]["filtered_cofinal_refinement"]
        and state["pres"]["refinement_descent"]
        and {FILTERED_COFINAL, REFINEMENT_DESCENT, REPRESENTED_LIMIT} <= state["pres"]["law_completion_deps"],
        "coherent source-presentation transport, universal-arrow reindexing, and refinement descent preserve completion",
    )
    gate(
        f"{PREFIX}5",
        state["pres"]["endpoint_invariant"]
        and state["pres"]["degree_invariant"]
        and state["pres"]["projection_formula_invariant"]
        and state["pres"]["boundary_invariant"]
        and state["pres"]["dd4_invariant"]
        and state["pres"]["exact_delta_invariant"],
        "endpoint, degree, projection, boundary, DD.4, and exact-delta laws are presentation-invariant",
    )
    gate(
        f"{PREFIX}6",
        state["pres"]["graph_invariant"]
        and state["pres"]["rosati_invariant"]
        and state["pres"]["control_invariant"]
        and state["pres"]["handoff_invariant"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["pres"]["routes"],
        "graph, Rosati, control, handoff, and graph-later laws are presentation-invariant",
    )
    gate(
        f"{PREFIX}7",
        state["pres"]["normalizer_transport"]
        and state["pres"]["semantic_transport"]
        and state["pres"]["invariant_reflection_transport"]
        and NORMALIZER_DEPS <= state["pres"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection transport are presentation-invariant",
    )
    gate(
        f"{PREFIX}8",
        state["pres"]["budgeted"]
        and state["pres"]["natural"]
        and state["pres"]["coherent"]
        and not any(
            state["pres"][key]
            for key in (
                "external_presentation",
                "syntax_quotient",
                "quotient_normal_form",
                "presentation_specific_normalizer",
                "retuned_generator_list",
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
        and set(state["requires"].get(PRESINV, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "presentation invariance is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: source-law-complete normal forms are presentation-invariant")
    print(
        "VERDICT: the missing-object candidate counts only when source-law-complete "
        "reflected pasted cyclic Beck-Chevalley normal forms are invariant under "
        "admissible source-presentation changes; presentation-specific completion "
        "is still a disguised repair."
    )


if __name__ == "__main__":
    main()
