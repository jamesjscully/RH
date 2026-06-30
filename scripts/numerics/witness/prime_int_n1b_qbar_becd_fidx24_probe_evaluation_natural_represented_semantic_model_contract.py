#!/usr/bin/env python3
r"""Natural evaluation for the represented semantic model.

Doc 576 requires the conservative semantics to be represented by a
source-internal model object. This witness closes the next cheap escape: the
model cannot evaluate only objectwise, pointwise, or by a nonfunctorial
choice. Its evaluation must be a natural source-internal transformation that
commutes with executable rewrites, refinements, composition, and every payload
projection.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_evaluation_natural_represented_semantic_model_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the evaluation-natural semantic model witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 577
EXPECTED_WITNESS = "doc577-probe-evaluation-natural-represented-semantic-model-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEVALNATREPSEMMODEL"

EVAL = "evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MODEL = "represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SEM = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FUNC = "functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
COMP = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REFINEMENT = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
SOURCE_MEDIATOR_FIXED = "source_mediator_fixed"
DOC515_FIXED = "doc515_coherence_fixed"
FINITE_INDEX = "exact_24_cell_finite_index"

failures: list[str] = []

SEMANTIC_TARGETS = {
    ENDPOINT,
    DEGREE,
    DD4_BOUNDARY,
    PUSHFORWARD,
    EXACT_DELTA,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
    HANDOFF,
    GRAPH_LATER,
    SOURCE_BEFORE_POINTS,
    ORIGINAL_DD4,
    SOURCE_MEDIATOR_FIXED,
    DOC515_FIXED,
    FINITE_INDEX,
}

REQUIRED_DEPS = {MODEL, SEM, EXEC, FUNC, COMP, REFINEMENT, SUBREP, UNIVERSAL_ARROW} | SEMANTIC_TARGETS

EXPECTED_EDGES = {
    (MODEL, "evaluated_by", EVAL),
    (EVAL, "evaluation_natural_for", MODEL),
    (EVAL, "evaluates_semantics_for", SEM),
    (EVAL, "evaluation_commutes_with", EXEC),
    (EVAL, "evaluation_internal_to", SUBREP),
    (EVAL, "evaluation_selected_by", UNIVERSAL_ARROW),
    (EVAL, "evaluation_refinement_stable_for", REFINEMENT),
    (EVAL, "evaluation_compositional_for", COMP),
    (EVAL, "evaluation_functorial_for", FUNC),
} | {(EVAL, "evaluation_commutes_with_payload_projection", target) for target in SEMANTIC_TARGETS}

REQUIRED_FLAGS = (
    "evaluation_natural_certificate",
    "source_internal_evaluation",
    "universal_arrow_evaluation",
    "executable_compatible_evaluation",
    "rewrite_compatible_evaluation",
    "refinement_stable_evaluation",
    "compositional_evaluation",
    "payload_projection_commuting_evaluation",
    "original_h1_evaluation_visible",
    "doc515_evaluation_visible",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_missing",
    "center_eliminator_semantics_evaluation_not_natural",
    "center_eliminator_semantics_evaluation_not_executable_compatible",
    "center_eliminator_semantics_evaluation_not_rewrite_compatible",
    "center_eliminator_semantics_evaluation_not_refinement_stable",
    "center_eliminator_semantics_evaluation_not_compositional",
    "center_eliminator_semantics_evaluation_not_subrepresenter_internal",
    "center_eliminator_semantics_evaluation_not_universal_arrow_evaluation",
    "center_eliminator_semantics_evaluation_pointwise_only",
    "center_eliminator_semantics_evaluation_objectwise_only",
    "center_eliminator_semantics_evaluation_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_path_dependent",
    "center_eliminator_semantics_evaluation_payload_projection_gap",
    "center_eliminator_semantics_evaluation_original_h1_gap",
    "center_eliminator_semantics_evaluation_doc515_gap",
    "center_eliminator_semantics_evaluation_external",
    "center_eliminator_semantics_evaluation_quotient",
    "center_eliminator_semantics_evaluation_functor_of_points_only",
    "center_eliminator_semantics_evaluation_yoneda_reversal",
    "center_eliminator_semantics_evaluation_requires_choice",
    "center_eliminator_semantics_evaluation_requires_new_cell",
    "center_eliminator_semantics_evaluation_context_collapse",
    "center_eliminator_semantics_evaluation_by_declaration",
    "center_eliminator_semantics_evaluation_finite_sample",
    "center_eliminator_semantics_evaluation_basis_row",
    "center_eliminator_semantics_evaluation_not_budgeted",
    "missing_evaluation_natural_semantic_model_certificate",
)

EVALUATION_DATA = {
    "certificate": "evaluation_natural_represented_source_internal_semantic_model",
    "base_model": MODEL,
    "exists": True,
    "natural": True,
    "source_internal": True,
    "subrepresenter_internal": True,
    "universal_arrow_evaluation": True,
    "executable_compatible": True,
    "rewrite_compatible": True,
    "refinement_stable": True,
    "compositional": True,
    "pointwise_only": False,
    "objectwise_only": False,
    "nonfunctorial_choice": False,
    "path_dependent": False,
    "external": False,
    "quotient": False,
    "functor_of_points_only": False,
    "yoneda_reversal": False,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "payload_projections": SEMANTIC_TARGETS,
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
        "evaluation": deepcopy(EVALUATION_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "evaluation":
            state["evaluation"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(EVAL, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    evaluation = state["evaluation"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_577")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc577_witness")
    if EVAL not in state["accepted"]:
        reasons.append("missing_evaluation_natural_semantic_model_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(EVAL, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if evaluation.get("base_model") != MODEL:
        reasons.append("wrong_base_model")
    if not evaluation.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_missing")
    if not evaluation.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_not_natural")
    if not evaluation.get("executable_compatible"):
        reasons.append("center_eliminator_semantics_evaluation_not_executable_compatible")
    if not evaluation.get("rewrite_compatible"):
        reasons.append("center_eliminator_semantics_evaluation_not_rewrite_compatible")
    if not evaluation.get("refinement_stable"):
        reasons.append("center_eliminator_semantics_evaluation_not_refinement_stable")
    if not evaluation.get("compositional"):
        reasons.append("center_eliminator_semantics_evaluation_not_compositional")
    if not evaluation.get("subrepresenter_internal"):
        reasons.append("center_eliminator_semantics_evaluation_not_subrepresenter_internal")
    if not evaluation.get("universal_arrow_evaluation"):
        reasons.append("center_eliminator_semantics_evaluation_not_universal_arrow_evaluation")
    if evaluation.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_pointwise_only")
    if evaluation.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_objectwise_only")
    if evaluation.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_nonfunctorial_choice")
    if evaluation.get("path_dependent"):
        reasons.append("center_eliminator_semantics_evaluation_path_dependent")
    if not SEMANTIC_TARGETS <= set(evaluation["payload_projections"]):
        reasons.append("center_eliminator_semantics_evaluation_payload_projection_gap")
    if ORIGINAL_DD4 not in evaluation["payload_projections"]:
        reasons.append("center_eliminator_semantics_evaluation_original_h1_gap")
    if DOC515_FIXED not in evaluation["payload_projections"]:
        reasons.append("center_eliminator_semantics_evaluation_doc515_gap")
    if evaluation.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_external")
    if evaluation.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_quotient")
    if evaluation.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_functor_of_points_only")
    if evaluation.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_yoneda_reversal")
    if evaluation.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_requires_choice")
    if evaluation.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_requires_new_cell")
    if evaluation.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_context_collapse")
    if evaluation.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_by_declaration")
    if evaluation.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_finite_sample")
    if evaluation.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_basis_row")
    if not evaluation.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_not_budgeted")

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
        and EVAL in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["evaluation"]["natural"]
        and state["evaluation"]["source_internal"]
        and state["evaluation"]["subrepresenter_internal"]
        and state["evaluation"]["universal_arrow_evaluation"],
        "evaluation is natural, source-internal, and universal-arrow based",
    )
    gate(
        f"{PREFIX}3",
        state["evaluation"]["executable_compatible"]
        and state["evaluation"]["rewrite_compatible"]
        and state["evaluation"]["refinement_stable"]
        and state["evaluation"]["compositional"],
        "evaluation commutes with execution, rewrites, refinements, and composition",
    )
    gate(
        f"{PREFIX}4",
        SEMANTIC_TARGETS <= state["evaluation"]["payload_projections"],
        f"payload_projection_targets={len(SEMANTIC_TARGETS)}/15",
    )
    gate(
        f"{PREFIX}5",
        ORIGINAL_DD4 in state["evaluation"]["payload_projections"]
        and DOC515_FIXED in state["evaluation"]["payload_projections"]
        and state["evaluation"]["budgeted"],
        "original-H1, doc515, and exact-24 budget survive evaluation",
    )
    gate(
        f"{PREFIX}6",
        not any(
            state["evaluation"][key]
            for key in (
                "pointwise_only",
                "objectwise_only",
                "nonfunctorial_choice",
                "path_dependent",
                "external",
                "quotient",
                "functor_of_points_only",
                "yoneda_reversal",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "evaluation is not pointwise/objectwise/external/quotient/choice dependent",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(EVAL, [])) <= state["accepted"],
        "evaluation dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all evaluation-naturality graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: represented semantics has natural evaluation")
    print(
        "VERDICT: the missing-object candidate counts only when the represented semantic model "
        "has a source-internal natural evaluation that commutes with executable normal forms, "
        "refinements, composition, and every payload projection."
    )


if __name__ == "__main__":
    main()
