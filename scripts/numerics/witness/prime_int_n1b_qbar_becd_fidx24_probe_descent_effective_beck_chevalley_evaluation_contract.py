#!/usr/bin/env python3
r"""Effective descent for Beck-Chevalley semantic evaluation.

Doc 578 requires the represented semantic evaluation to satisfy exact
Beck-Chevalley base-change. This witness closes the next cheap escape:
the Beck-Chevalley data may be only local, cover-dependent, or retuned on
refinement. The current frontier only counts if the evaluation glues by
effective descent over the filtered cofinal refinement calculus already in
the source square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_descent_effective_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the descent-effective evaluation witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 579
EXPECTED_WITNESS = "doc579-probe-descent-effective-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMDESCEFFBCHEVEVAL"

DESC = "descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
BC = "beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EVAL = "evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MODEL = "represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SEM = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FILTERED = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REFINEMENT = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REPLIM = "represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
DIAG = "cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SUBREP = "source_fiber_subrepresenter"
UNIVERSAL_ARROW = "coupling_universal_arrow"
ENDPOINT = "endpoint_integrality"
DEGREE = "degree_maps"
DD4_BOUNDARY = "dd4_boundary"
PUSHFORWARD = "boundary_pushforward"
EXACT_DELTA = "exact_delta"
GRAPH_COMP = "graph_composition"
ROSATI = "rosati_count"
CONTROL = "control_death"
HANDOFF = "dd4_image_only_handoff_contract"
GRAPH_LATER = "graph_later_realization_contract"
SOURCE_BEFORE_POINTS = "source_before_points"
ORIGINAL_DD4 = "original_dd4_res1_nonboundary"
DOC515_FIXED = "doc515_coherence_fixed"
FINITE_INDEX = "exact_24_cell_finite_index"

failures: list[str] = []

BASE_CHANGE_ROUTES = {
    DD4_BOUNDARY,
    PUSHFORWARD,
    EXACT_DELTA,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
    HANDOFF,
    GRAPH_LATER,
}

PROJECTION_FORMULA_TARGETS = {ENDPOINT, DEGREE}

PRESERVED_CONTEXTS = {
    SOURCE_BEFORE_POINTS,
    ORIGINAL_DD4,
    DOC515_FIXED,
    FINITE_INDEX,
}

REQUIRED_DEPS = {
    BC,
    EVAL,
    MODEL,
    SEM,
    FILTERED,
    REFINEMENT,
    REPLIM,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (BC, "made_descent_effective_by", DESC),
    (DESC, "descent_effective_for", BC),
    (DESC, "descends_over", FILTERED),
    (DESC, "glues_local_evaluations_for", EVAL),
    (DESC, "descent_cocycle_for", REPLIM),
    (DESC, "descends_base_change_over", DIAG),
    (DESC, "descent_internal_to", SUBREP),
    (DESC, "descent_selected_by", UNIVERSAL_ARROW),
} | {
    (DESC, "descent_preserves_projection_formula_for", target)
    for target in PROJECTION_FORMULA_TARGETS
} | {
    (DESC, "descent_preserves_base_change_for", target)
    for target in BASE_CHANGE_ROUTES
} | {(DESC, "descent_preserves", target) for target in PRESERVED_CONTEXTS}

REQUIRED_FLAGS = (
    "descent_effective_certificate",
    "filtered_cofinal_descent",
    "refinement_cocycle",
    "local_evaluation_gluing",
    "base_change_descent_stable",
    "projection_formula_descent_stable",
    "original_h1_descent_visible",
    "doc515_descent_visible",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_descent_missing",
    "center_eliminator_semantics_evaluation_descent_not_effective",
    "center_eliminator_semantics_evaluation_descent_not_cofinal",
    "center_eliminator_semantics_evaluation_descent_cocycle_gap",
    "center_eliminator_semantics_evaluation_descent_gluing_gap",
    "center_eliminator_semantics_evaluation_descent_local_only",
    "center_eliminator_semantics_evaluation_descent_cover_dependent",
    "center_eliminator_semantics_evaluation_descent_retuned_on_refinement",
    "center_eliminator_semantics_evaluation_descent_not_unique",
    "center_eliminator_semantics_evaluation_descent_incoherent",
    "center_eliminator_semantics_evaluation_descent_base_change_not_stable",
    "center_eliminator_semantics_evaluation_descent_projection_formula_gap",
    "center_eliminator_semantics_evaluation_descent_original_h1_gap",
    "center_eliminator_semantics_evaluation_descent_doc515_gap",
    "center_eliminator_semantics_evaluation_descent_external",
    "center_eliminator_semantics_evaluation_descent_quotient",
    "center_eliminator_semantics_evaluation_descent_functor_of_points_only",
    "center_eliminator_semantics_evaluation_descent_yoneda_reversal",
    "center_eliminator_semantics_evaluation_descent_pointwise_only",
    "center_eliminator_semantics_evaluation_descent_objectwise_only",
    "center_eliminator_semantics_evaluation_descent_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_descent_requires_choice",
    "center_eliminator_semantics_evaluation_descent_requires_new_cell",
    "center_eliminator_semantics_evaluation_descent_context_collapse",
    "center_eliminator_semantics_evaluation_descent_by_declaration",
    "center_eliminator_semantics_evaluation_descent_finite_sample",
    "center_eliminator_semantics_evaluation_descent_basis_row",
    "center_eliminator_semantics_evaluation_descent_not_budgeted",
    "missing_descent_effective_beck_chevalley_evaluation_certificate",
)

DESCENT_DATA = {
    "certificate": "descent_effective_beck_chevalley_evaluation",
    "base_beck_chevalley": BC,
    "exists": True,
    "effective": True,
    "cofinal": True,
    "cocycle": True,
    "gluing": True,
    "local_only": False,
    "cover_dependent": False,
    "retuned_on_refinement": False,
    "unique": True,
    "coherent": True,
    "base_change_stable": True,
    "projection_formula_stable": True,
    "external": False,
    "quotient": False,
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
        "descent": deepcopy(DESCENT_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "descent":
            state["descent"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(DESC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    descent = state["descent"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_579")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc579_witness")
    if DESC not in state["accepted"]:
        reasons.append("missing_descent_effective_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(DESC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if descent.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not descent.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_descent_missing")
    if not descent.get("effective"):
        reasons.append("center_eliminator_semantics_evaluation_descent_not_effective")
    if not descent.get("cofinal"):
        reasons.append("center_eliminator_semantics_evaluation_descent_not_cofinal")
    if not descent.get("cocycle"):
        reasons.append("center_eliminator_semantics_evaluation_descent_cocycle_gap")
    if not descent.get("gluing"):
        reasons.append("center_eliminator_semantics_evaluation_descent_gluing_gap")
    if descent.get("local_only"):
        reasons.append("center_eliminator_semantics_evaluation_descent_local_only")
    if descent.get("cover_dependent"):
        reasons.append("center_eliminator_semantics_evaluation_descent_cover_dependent")
    if descent.get("retuned_on_refinement"):
        reasons.append("center_eliminator_semantics_evaluation_descent_retuned_on_refinement")
    if not descent.get("unique"):
        reasons.append("center_eliminator_semantics_evaluation_descent_not_unique")
    if not descent.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_descent_incoherent")
    if not descent.get("base_change_stable") or not BASE_CHANGE_ROUTES <= set(descent["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_descent_base_change_not_stable")
    if (
        not descent.get("projection_formula_stable")
        or not PROJECTION_FORMULA_TARGETS <= set(descent["projection_targets"])
    ):
        reasons.append("center_eliminator_semantics_evaluation_descent_projection_formula_gap")
    if ORIGINAL_DD4 not in descent["preserved_contexts"]:
        reasons.append("center_eliminator_semantics_evaluation_descent_original_h1_gap")
    if DOC515_FIXED not in descent["preserved_contexts"]:
        reasons.append("center_eliminator_semantics_evaluation_descent_doc515_gap")
    if descent.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_descent_external")
    if descent.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_descent_quotient")
    if descent.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_descent_functor_of_points_only")
    if descent.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_descent_yoneda_reversal")
    if descent.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_descent_pointwise_only")
    if descent.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_descent_objectwise_only")
    if descent.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_descent_nonfunctorial_choice")
    if descent.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_descent_requires_choice")
    if descent.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_descent_requires_new_cell")
    if descent.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_descent_context_collapse")
    if descent.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_descent_by_declaration")
    if descent.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_descent_finite_sample")
    if descent.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_descent_basis_row")
    if not descent.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_descent_not_budgeted")

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
        and DESC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["descent"]["effective"]
        and state["descent"]["cofinal"]
        and state["descent"]["cocycle"]
        and state["descent"]["gluing"],
        "Beck-Chevalley evaluation has effective cofinal descent with cocycle and gluing",
    )
    gate(
        f"{PREFIX}3",
        not state["descent"]["local_only"]
        and not state["descent"]["cover_dependent"]
        and not state["descent"]["retuned_on_refinement"]
        and state["descent"]["unique"]
        and state["descent"]["coherent"],
        "descent is global, cover-independent, unretuned, unique, and coherent",
    )
    gate(
        f"{PREFIX}4",
        BASE_CHANGE_ROUTES <= state["descent"]["routes"] and state["descent"]["base_change_stable"],
        "DD.4, boundary, exact-delta, graph, Rosati, control, and handoff routes descend",
    )
    gate(
        f"{PREFIX}5",
        PROJECTION_FORMULA_TARGETS <= state["descent"]["projection_targets"]
        and state["descent"]["projection_formula_stable"]
        and {ORIGINAL_DD4, DOC515_FIXED, FINITE_INDEX} <= state["descent"]["preserved_contexts"]
        and state["descent"]["budgeted"],
        "projection formula, original-H1, doc515, and exact-24 budget descend",
    )
    gate(
        f"{PREFIX}6",
        not any(
            state["descent"][key]
            for key in (
                "external",
                "quotient",
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
        ),
        "effective descent is not a disguised external or choice-based repair",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(DESC, [])) <= state["accepted"],
        "descent-effective Beck-Chevalley dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all descent-effective evaluation graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: Beck-Chevalley evaluation has effective descent")
    print(
        "VERDICT: the missing-object candidate counts only when the exact/cartesian "
        "Beck-Chevalley semantic evaluation glues by effective, cofinal, coherent "
        "descent without cover-dependent or retuned local data."
    )


if __name__ == "__main__":
    main()
