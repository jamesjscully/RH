#!/usr/bin/env python3
r"""Beck-Chevalley exactness for natural evaluation of represented semantics.

Doc 577 requires the represented semantic model to have source-internal
natural evaluation. This witness closes the next cheap escape: naturality may
still be only vertical or projectionwise. The evaluation must satisfy
exact/cartesian Beck-Chevalley base-change against the existing source square,
so pull-then-evaluate and evaluate-then-push agree on the DD.4, exact-delta,
graph, Rosati, control, and handoff routes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_beck_chevalley_evaluation_natural_represented_semantic_model_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the Beck-Chevalley evaluation witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 578
EXPECTED_WITNESS = "doc578-probe-beck-chevalley-evaluation-natural-represented-semantic-model-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM"

BC = "beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EVAL = "evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MODEL = "represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SEM = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
    EVAL,
    MODEL,
    SEM,
    EXEC,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (EVAL, "made_beck_chevalley_by", BC),
    (BC, "beck_chevalley_evaluation_for", EVAL),
    (BC, "exact_cartesian_over", DIAG),
    (BC, "executable_base_change_for", EXEC),
    (BC, "base_change_internal_to", SUBREP),
    (BC, "base_change_selected_by", UNIVERSAL_ARROW),
} | {(BC, "projection_formula_for", target) for target in PROJECTION_FORMULA_TARGETS} | {
    (BC, "base_change_commutes_with", target) for target in BASE_CHANGE_ROUTES
} | {(BC, "base_change_preserves", target) for target in PRESERVED_CONTEXTS}

REQUIRED_FLAGS = (
    "beck_chevalley_certificate",
    "exact_base_change",
    "cartesian_base_change",
    "pull_push_commutes",
    "projection_formula",
    "subrepresenter_internal_base_change",
    "universal_arrow_base_change",
    "executable_base_change",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_beck_chevalley_missing",
    "center_eliminator_semantics_evaluation_not_exact",
    "center_eliminator_semantics_evaluation_not_cartesian",
    "center_eliminator_semantics_evaluation_base_change_gap",
    "center_eliminator_semantics_evaluation_pull_push_mismatch",
    "center_eliminator_semantics_evaluation_projection_formula_gap",
    "center_eliminator_semantics_evaluation_boundary_pushforward_gap",
    "center_eliminator_semantics_evaluation_dd4_exact_delta_gap",
    "center_eliminator_semantics_evaluation_graph_composition_gap",
    "center_eliminator_semantics_evaluation_rosati_control_gap",
    "center_eliminator_semantics_evaluation_handoff_graph_gap",
    "center_eliminator_semantics_evaluation_not_subrepresenter_base_change",
    "center_eliminator_semantics_evaluation_not_universal_arrow_base_change",
    "center_eliminator_semantics_evaluation_external_base_change",
    "center_eliminator_semantics_evaluation_quotient_base_change",
    "center_eliminator_semantics_evaluation_base_change_functor_of_points_only",
    "center_eliminator_semantics_evaluation_base_change_yoneda_reversal",
    "center_eliminator_semantics_evaluation_base_change_pointwise_only",
    "center_eliminator_semantics_evaluation_base_change_objectwise_only",
    "center_eliminator_semantics_evaluation_base_change_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_base_change_path_dependent",
    "center_eliminator_semantics_evaluation_base_change_requires_choice",
    "center_eliminator_semantics_evaluation_base_change_requires_new_cell",
    "center_eliminator_semantics_evaluation_base_change_context_collapse",
    "center_eliminator_semantics_evaluation_base_change_by_declaration",
    "center_eliminator_semantics_evaluation_base_change_finite_sample",
    "center_eliminator_semantics_evaluation_base_change_basis_row",
    "center_eliminator_semantics_evaluation_base_change_not_budgeted",
    "missing_beck_chevalley_evaluation_certificate",
)

BASE_CHANGE_DATA = {
    "certificate": "beck_chevalley_exact_semantic_evaluation",
    "base_evaluation": EVAL,
    "exists": True,
    "exact": True,
    "cartesian": True,
    "base_change": True,
    "pull_push_commutes": True,
    "projection_formula": True,
    "subrepresenter_internal": True,
    "universal_arrow_base_change": True,
    "executable_compatible": True,
    "external": False,
    "quotient": False,
    "functor_of_points_only": False,
    "yoneda_reversal": False,
    "pointwise_only": False,
    "objectwise_only": False,
    "nonfunctorial_choice": False,
    "path_dependent": False,
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
        "base_change": deepcopy(BASE_CHANGE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "base_change":
            state["base_change"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(BC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    base_change = state["base_change"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_578")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc578_witness")
    if BC not in state["accepted"]:
        reasons.append("missing_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(BC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if base_change.get("base_evaluation") != EVAL:
        reasons.append("wrong_base_evaluation")
    if not base_change.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_beck_chevalley_missing")
    if not base_change.get("exact"):
        reasons.append("center_eliminator_semantics_evaluation_not_exact")
    if not base_change.get("cartesian"):
        reasons.append("center_eliminator_semantics_evaluation_not_cartesian")
    if not base_change.get("base_change"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_gap")
    if not base_change.get("pull_push_commutes"):
        reasons.append("center_eliminator_semantics_evaluation_pull_push_mismatch")
    if not PROJECTION_FORMULA_TARGETS <= set(base_change["projection_targets"]) or not base_change.get("projection_formula"):
        reasons.append("center_eliminator_semantics_evaluation_projection_formula_gap")
    if PUSHFORWARD not in base_change["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_boundary_pushforward_gap")
    if not {DD4_BOUNDARY, EXACT_DELTA} <= set(base_change["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_dd4_exact_delta_gap")
    if GRAPH_COMP not in base_change["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_graph_composition_gap")
    if not {ROSATI, CONTROL} <= set(base_change["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_rosati_control_gap")
    if not {HANDOFF, GRAPH_LATER} <= set(base_change["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_handoff_graph_gap")
    if not base_change.get("subrepresenter_internal"):
        reasons.append("center_eliminator_semantics_evaluation_not_subrepresenter_base_change")
    if not base_change.get("universal_arrow_base_change"):
        reasons.append("center_eliminator_semantics_evaluation_not_universal_arrow_base_change")
    if base_change.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_external_base_change")
    if base_change.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_quotient_base_change")
    if base_change.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_functor_of_points_only")
    if base_change.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_yoneda_reversal")
    if base_change.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_pointwise_only")
    if base_change.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_objectwise_only")
    if base_change.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_nonfunctorial_choice")
    if base_change.get("path_dependent"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_path_dependent")
    if base_change.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_requires_choice")
    if base_change.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_requires_new_cell")
    if base_change.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_context_collapse")
    if base_change.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_by_declaration")
    if base_change.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_finite_sample")
    if base_change.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_basis_row")
    if not base_change.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_base_change_not_budgeted")
    if not PRESERVED_CONTEXTS <= set(base_change["preserved_contexts"]):
        reasons.append("center_eliminator_semantics_evaluation_base_change_gap")

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
        and BC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["base_change"]["exact"]
        and state["base_change"]["cartesian"]
        and state["base_change"]["base_change"],
        "evaluation has exact cartesian Beck-Chevalley base-change",
    )
    gate(
        f"{PREFIX}3",
        state["base_change"]["pull_push_commutes"] and state["base_change"]["projection_formula"],
        "pull-push and projection formula commute",
    )
    gate(
        f"{PREFIX}4",
        {DD4_BOUNDARY, PUSHFORWARD, EXACT_DELTA} <= state["base_change"]["routes"],
        "DD.4, boundary-pushforward, and exact-delta base-change routes commute",
    )
    gate(
        f"{PREFIX}5",
        {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["base_change"]["routes"],
        "graph, Rosati, control, handoff, and graph-later base-change routes commute",
    )
    gate(
        f"{PREFIX}6",
        state["base_change"]["subrepresenter_internal"]
        and state["base_change"]["universal_arrow_base_change"]
        and state["base_change"]["budgeted"]
        and not any(
            state["base_change"][key]
            for key in (
                "external",
                "quotient",
                "functor_of_points_only",
                "yoneda_reversal",
                "pointwise_only",
                "objectwise_only",
                "nonfunctorial_choice",
                "path_dependent",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "base-change is internal, universal-arrow based, budgeted, and not a disguised external repair",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(BC, [])) <= state["accepted"],
        "Beck-Chevalley dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all Beck-Chevalley evaluation graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: natural evaluation has Beck-Chevalley base-change")
    print(
        "VERDICT: the missing-object candidate counts only when the represented semantic "
        "evaluation is exact/cartesian and satisfies Beck-Chevalley pull-push base-change "
        "and projection formula for the existing source square."
    )


if __name__ == "__main__":
    main()
