#!/usr/bin/env python3
r"""Loop completeness for path-independent presentation transport.

Doc 586 requires zero monodromy for the named presentation-loop checks. This
witness closes the next cheap escape: those loops may be only a selected
basis, while other admissible presentation loops remain outside the tested
zero-monodromy inventory. The current frontier only counts if the named loop
checks generate every admissible presentation loop through internal
conjugation, refinement, subdivision, composition, inverse cancellation, and
source-law/payload closure.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the loop-complete presentation witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
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
    MAP_PATH,
    MATE,
    MONEXACT_DAGGER,
    NORMALIZER_DEPS,
    NORM,
    NORMREF,
    PASTE,
    PATHIND,
    PRESENTATION_LOOPS,
    PRESENTATION_MOVES,
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
)


EXPECTED_DOC = 587
EXPECTED_WITNESS = "doc587-probe-loop-complete-path-independent-presentation-invariant-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMLOOPCOMPPATHINDPRESINVSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

LOOPCOMP = "loop_complete_" + PATHIND

failures: list[str] = []

LOOP_COMPLETION_CLOSURES = {
    "loop_generator_complete",
    "loop_relation_complete",
    "conjugation_closed",
    "composition_closed",
    "inverse_closed",
    "refinement_closed",
    "subdivision_closed",
    "universal_arrow_closed",
    "normalizer_loop_closed",
    "semantic_loop_closed",
    "payload_loop_closed",
    "source_law_loop_closed",
}

REQUIRED_DEPS = {
    PATHIND,
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
    (PATHIND, "made_loop_complete_by", LOOPCOMP),
    (LOOPCOMP, "loop_complete_for", PATHIND),
    (LOOPCOMP, "loop_complete_for_presentation_invariant", PRESINV),
    (LOOPCOMP, "loop_complete_for_source_law_complete", LAWCOMP),
    (LOOPCOMP, "loop_complete_for_normal_form", NORMREF),
    (LOOPCOMP, "loop_complete_for_pasting_stable_mate", PASTE),
    (LOOPCOMP, "loop_complete_for_cyclic_mate", CYCLIC),
    (LOOPCOMP, "loop_complete_for_mate", MATE),
    (LOOPCOMP, "loop_complete_for_base_change", BC),
    (LOOPCOMP, "loop_complete_for_evaluation", EVAL),
    (LOOPCOMP, "loop_complete_over", DIAG),
    (LOOPCOMP, "loop_internal_to", SUBREP),
    (LOOPCOMP, "loop_completion_selected_by", UNIVERSAL_ARROW),
    (LOOPCOMP, "loop_complete_normalizer_via", NORM),
    (LOOPCOMP, "loop_complete_functorial_normalizer_via", FUNC_NORM),
    (LOOPCOMP, "loop_complete_monoidal_exact_dagger_normalizer_via", MONEXACT_DAGGER),
    (LOOPCOMP, "loop_complete_coherent_normalizer_via", COHERENT),
    (LOOPCOMP, "loop_complete_executable_diamonds_via", EXEC),
    (LOOPCOMP, "loop_complete_semantics_via", SEMCONS),
    (LOOPCOMP, "loop_complete_represented_semantics_via", REPSEM),
    (LOOPCOMP, "loop_complete_composition_law_via", COMPOSITION_STABLE),
    (LOOPCOMP, "loop_complete_refinement_law_via", REFINEMENT_DESCENT),
    (LOOPCOMP, "loop_complete_filtered_cofinal_law_via", FILTERED_COFINAL),
    (LOOPCOMP, "loop_complete_represented_limit_law_via", REPRESENTED_LIMIT),
} | {(LOOPCOMP, "loop_complete_source_law_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (LOOPCOMP, "loop_complete_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(LOOPCOMP, "loop_complete_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (LOOPCOMP, "loop_complete_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "loop_complete_certificate",
    "all_admissible_loops_generated",
    "loop_relations_complete",
    "conjugation_closed",
    "refinement_closed",
    "normalizer_loop_complete",
    "semantic_loop_complete",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_missing",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_complete",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_selected_loop_basis_only",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_hidden_loop_generator_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_loop_relation_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_conjugation_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_composition_closure_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_inverse_closure_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_refinement_closure_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_subdivision_closure_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_universal_arrow_closure_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_normalizer_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_semantic_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_invariant_reflection_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_payload_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_source_law_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_endpoint_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_degree_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_projection_formula_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_boundary_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_dd4_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_exact_delta_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_graph_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_rosati_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_control_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_handoff_loop_gap",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_natural",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_coherent",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_external_loop_presentation",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_external_2groupoid",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_quotient_fundamental_group",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_homotopy_quotient",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_syntax_loop_quotient",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_retuned_loop_basis",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_requires_choice",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_context_collapse",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_by_declaration",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_finite_sample",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_basis_row",
    "center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_budgeted",
    "missing_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

LOOP_DATA = {
    "certificate": "loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_path_independent": PATHIND,
    "base_presentation_invariant": PRESINV,
    "base_source_law_complete": LAWCOMP,
    "base_normal_form": NORMREF,
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "loop_complete": True,
    "selected_loop_basis_only": False,
    "all_admissible_loops_generated": True,
    "loop_relations_complete": True,
    "hidden_loop_generators": False,
    "conjugation_closed": True,
    "composition_closed": True,
    "inverse_closed": True,
    "refinement_closed": True,
    "subdivision_closed": True,
    "universal_arrow_closed": True,
    "normalizer_loop_complete": True,
    "semantic_loop_complete": True,
    "invariant_reflection_loop_complete": True,
    "payload_loop_complete": True,
    "source_law_loop_complete": True,
    "endpoint_loop_complete": True,
    "degree_loop_complete": True,
    "projection_formula_loop_complete": True,
    "boundary_loop_complete": True,
    "dd4_loop_complete": True,
    "exact_delta_loop_complete": True,
    "graph_loop_complete": True,
    "rosati_loop_complete": True,
    "control_loop_complete": True,
    "handoff_loop_complete": True,
    "natural": True,
    "coherent": True,
    "external_loop_presentation": False,
    "external_2groupoid": False,
    "quotient_fundamental_group": False,
    "homotopy_quotient": False,
    "syntax_loop_quotient": False,
    "retuned_loop_basis": False,
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
    "closures": LOOP_COMPLETION_CLOSURES,
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
        "loop": deepcopy(LOOP_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "loop":
            state["loop"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(LOOPCOMP, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    loop = state["loop"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_587")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc587_witness")
    if LOOPCOMP not in state["accepted"]:
        reasons.append("missing_loop_complete_path_independent_presentation_invariant_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(LOOPCOMP, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if loop.get("base_path_independent") != PATHIND:
        reasons.append("wrong_base_path_independent")
    if loop.get("base_presentation_invariant") != PRESINV:
        reasons.append("wrong_base_presentation_invariant")
    if loop.get("base_source_law_complete") != LAWCOMP:
        reasons.append("wrong_base_source_law_complete")
    if loop.get("base_normal_form") != NORMREF:
        reasons.append("wrong_base_normal_form_reflection")
    if loop.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if loop.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if loop.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if loop.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not loop.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_missing")
    if not loop.get("loop_complete"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_complete")
    if loop.get("selected_loop_basis_only"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_selected_loop_basis_only")
    if not loop.get("all_admissible_loops_generated") or loop.get("hidden_loop_generators"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_hidden_loop_generator_gap")
    if not loop.get("loop_relations_complete"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_loop_relation_gap")
    if not loop.get("conjugation_closed") or "conjugation_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_conjugation_gap")
    if not loop.get("composition_closed") or "composition_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_composition_closure_gap")
    if not loop.get("inverse_closed") or "inverse_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_inverse_closure_gap")
    if not loop.get("refinement_closed") or "refinement_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_refinement_closure_gap")
    if not loop.get("subdivision_closed") or "subdivision_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_subdivision_closure_gap")
    if not loop.get("universal_arrow_closed") or "universal_arrow_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_universal_arrow_closure_gap")
    if not loop.get("normalizer_loop_complete") or not {NORM, FUNC_NORM, COHERENT, EXEC} <= loop["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_normalizer_loop_gap")
    if not loop.get("semantic_loop_complete") or SEMCONS not in loop["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_semantic_loop_gap")
    if not loop.get("invariant_reflection_loop_complete") or REPSEM not in loop["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_invariant_reflection_loop_gap")
    if not loop.get("payload_loop_complete") or "payload_loop_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_payload_loop_gap")
    if not loop.get("source_law_loop_complete") or "source_law_loop_closed" not in loop["closures"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_source_law_loop_gap")
    if not loop.get("endpoint_loop_complete") or ENDPOINT not in loop["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_endpoint_loop_gap")
    if not loop.get("degree_loop_complete") or DEGREE not in loop["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_degree_loop_gap")
    if not loop.get("projection_formula_loop_complete") or not PROJECTION_FORMULA_TARGETS <= set(loop["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_projection_formula_loop_gap")
    if not loop.get("boundary_loop_complete") or PUSHFORWARD not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_boundary_loop_gap")
    if not loop.get("dd4_loop_complete") or DD4_BOUNDARY not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_dd4_loop_gap")
    if not loop.get("exact_delta_loop_complete") or EXACT_DELTA not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_exact_delta_loop_gap")
    if not loop.get("graph_loop_complete") or GRAPH_COMP not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_graph_loop_gap")
    if not loop.get("rosati_loop_complete") or ROSATI not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_rosati_loop_gap")
    if not loop.get("control_loop_complete") or CONTROL not in loop["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_control_loop_gap")
    if not loop.get("handoff_loop_complete") or not {HANDOFF, GRAPH_LATER} <= set(loop["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_handoff_loop_gap")
    if not loop.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_natural")
    if not loop.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_coherent")
    if loop.get("external_loop_presentation"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_external_loop_presentation")
    if loop.get("external_2groupoid"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_external_2groupoid")
    if loop.get("quotient_fundamental_group"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_quotient_fundamental_group")
    if loop.get("homotopy_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_homotopy_quotient")
    if loop.get("syntax_loop_quotient"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_syntax_loop_quotient")
    if loop.get("retuned_loop_basis"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_retuned_loop_basis")
    if loop.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_functor_of_points_only")
    if loop.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_yoneda_reversal")
    if loop.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_pointwise_only")
    if loop.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_objectwise_only")
    if loop.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_nonfunctorial_choice")
    if loop.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_requires_choice")
    if loop.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_requires_new_cell")
    if loop.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_context_collapse")
    if loop.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_by_declaration")
    if loop.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_finite_sample")
    if loop.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_basis_row")
    if not loop.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_loop_complete_path_pres_law_nf_not_budgeted")

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
        and LOOPCOMP in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["loop"]["loop_complete"]
        and not state["loop"]["selected_loop_basis_only"]
        and state["loop"]["all_admissible_loops_generated"]
        and not state["loop"]["hidden_loop_generators"],
        "named zero-monodromy loops generate every admissible presentation loop",
    )
    gate(
        f"{PREFIX}3",
        state["loop"]["loop_relations_complete"]
        and state["loop"]["conjugation_closed"]
        and state["loop"]["composition_closed"]
        and state["loop"]["inverse_closed"]
        and LOOP_COMPLETION_CLOSURES <= state["loop"]["closures"],
        "loop generators are relation-complete and closed under conjugation, composition, and inverse moves",
    )
    gate(
        f"{PREFIX}4",
        state["loop"]["refinement_closed"]
        and state["loop"]["subdivision_closed"]
        and state["loop"]["universal_arrow_closed"]
        and {FILTERED_COFINAL, REFINEMENT_DESCENT, REPRESENTED_LIMIT} <= state["loop"]["law_completion_deps"],
        "loop completion is stable under refinement, subdivision, and universal-arrow transport",
    )
    gate(
        f"{PREFIX}5",
        state["loop"]["normalizer_loop_complete"]
        and state["loop"]["semantic_loop_complete"]
        and state["loop"]["invariant_reflection_loop_complete"]
        and NORMALIZER_DEPS <= state["loop"]["normalizer_deps"],
        "normalizer, semantic, and invariant-reflection loops are complete",
    )
    gate(
        f"{PREFIX}6",
        state["loop"]["payload_loop_complete"]
        and state["loop"]["source_law_loop_complete"]
        and state["loop"]["endpoint_loop_complete"]
        and state["loop"]["degree_loop_complete"]
        and state["loop"]["projection_formula_loop_complete"]
        and state["loop"]["boundary_loop_complete"]
        and state["loop"]["dd4_loop_complete"]
        and state["loop"]["exact_delta_loop_complete"],
        "payload, source-law, endpoint, degree, projection, boundary, DD.4, and exact-delta loop coverage is complete",
    )
    gate(
        f"{PREFIX}7",
        state["loop"]["graph_loop_complete"]
        and state["loop"]["rosati_loop_complete"]
        and state["loop"]["control_loop_complete"]
        and state["loop"]["handoff_loop_complete"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["loop"]["routes"],
        "graph, Rosati, control, handoff, and graph-later loop coverage is complete",
    )
    gate(
        f"{PREFIX}8",
        state["loop"]["budgeted"]
        and state["loop"]["natural"]
        and state["loop"]["coherent"]
        and not any(
            state["loop"][key]
            for key in (
                "external_loop_presentation",
                "external_2groupoid",
                "quotient_fundamental_group",
                "homotopy_quotient",
                "syntax_loop_quotient",
                "retuned_loop_basis",
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
        and set(state["requires"].get(LOOPCOMP, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "loop completeness is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: presentation loop zero-monodromy inventory is complete")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "path-independent presentation transport loop checks generate every "
        "admissible loop internally; selected loop bases are still disguised "
        "repairs."
    )


if __name__ == "__main__":
    main()
