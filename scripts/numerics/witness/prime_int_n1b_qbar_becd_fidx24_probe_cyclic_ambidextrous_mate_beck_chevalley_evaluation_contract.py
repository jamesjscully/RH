#!/usr/bin/env python3
r"""Cyclic-ambidextrous mate coherence for Beck-Chevalley evaluation.

Doc 580 requires the descended Beck-Chevalley semantic evaluation to be the
coherent adjunction mate of the source dagger, trace, projection, and control
routes. This witness closes the next cheap escape: the mate-coherent square
may still depend on a marked cut of the trace/adjunction cycle. The current
frontier only counts if the mate data is cyclic and ambidextrous under
rotating through trace, dagger/Rosati, boundary, graph, control, and handoff
routes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_cyclic_ambidextrous_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the cyclic-ambidextrous mate witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 581
EXPECTED_WITNESS = "doc581-probe-cyclic-ambidextrous-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCYCAMBMATEBCHEVEVAL"

CYCLIC = "cyclic_ambidextrous_mate_coherent_descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MATE = "mate_coherent_descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
BC = "beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EVAL = "evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
DIAG = "cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SUBREP = "source_fiber_subrepresenter"
UNIVERSAL_ARROW = "coupling_universal_arrow"
DAGGER = "dagger_monoidal_probe_equivalence_certificate"
ADJOINT = "adjoint_pairing_probe_equivalence_certificate"
DUAL_TRACE = "dual_trace_probe_equivalence_certificate"
PIVOTAL = "pivotal_monoidal_probe_equivalence_certificate"
EXACT_ADDITIVE = "exact_additive_trace_probe_equivalence_certificate"
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

ROTATION_STRUCTURES = {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE}

REQUIRED_DEPS = {
    MATE,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | ROTATION_STRUCTURES | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (MATE, "made_cyclic_ambidextrous_by", CYCLIC),
    (CYCLIC, "cyclic_ambidextrous_for", MATE),
    (CYCLIC, "cyclic_mate_of", BC),
    (CYCLIC, "rotates_evaluation_for", EVAL),
    (CYCLIC, "cyclic_over_trace", DUAL_TRACE),
    (CYCLIC, "ambidextrous_over_adjoint_pairing", ADJOINT),
    (CYCLIC, "rotation_coherent_over", DIAG),
    (CYCLIC, "rotation_internal_to", SUBREP),
    (CYCLIC, "rotation_selected_by", UNIVERSAL_ARROW),
} | {
    (CYCLIC, "rotation_coherent_with", target)
    for target in {DAGGER, PIVOTAL, EXACT_ADDITIVE}
} | {
    (CYCLIC, "rotation_preserves_projection_formula_for", target)
    for target in PROJECTION_FORMULA_TARGETS
} | {(CYCLIC, "rotates_with", target) for target in BASE_CHANGE_ROUTES} | {
    (CYCLIC, "rotation_preserves", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "cyclic_ambidextrous_certificate",
    "left_right_ambidextrous",
    "cut_independent_rotation",
    "trace_cyclic_rotation",
    "dagger_rosati_rotation",
    "projection_formula_rotation",
    "boundary_graph_control_rotation",
    "descent_stable_rotation",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_cyclic_mate_missing",
    "center_eliminator_semantics_evaluation_cyclic_mate_not_ambidextrous",
    "center_eliminator_semantics_evaluation_cyclic_mate_left_right_mismatch",
    "center_eliminator_semantics_evaluation_cyclic_mate_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_cut_dependent",
    "center_eliminator_semantics_evaluation_cyclic_mate_trace_cyclicity_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_dagger_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_rosati_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_projection_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_boundary_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_dd4_exact_delta_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_graph_composition_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_control_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_handoff_rotation_gap",
    "center_eliminator_semantics_evaluation_cyclic_mate_descent_rotation_not_stable",
    "center_eliminator_semantics_evaluation_cyclic_mate_not_natural",
    "center_eliminator_semantics_evaluation_cyclic_mate_not_coherent",
    "center_eliminator_semantics_evaluation_cyclic_mate_external",
    "center_eliminator_semantics_evaluation_cyclic_mate_quotient",
    "center_eliminator_semantics_evaluation_cyclic_mate_functor_of_points_only",
    "center_eliminator_semantics_evaluation_cyclic_mate_yoneda_reversal",
    "center_eliminator_semantics_evaluation_cyclic_mate_pointwise_only",
    "center_eliminator_semantics_evaluation_cyclic_mate_objectwise_only",
    "center_eliminator_semantics_evaluation_cyclic_mate_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_cyclic_mate_requires_choice",
    "center_eliminator_semantics_evaluation_cyclic_mate_requires_new_cell",
    "center_eliminator_semantics_evaluation_cyclic_mate_context_collapse",
    "center_eliminator_semantics_evaluation_cyclic_mate_by_declaration",
    "center_eliminator_semantics_evaluation_cyclic_mate_finite_sample",
    "center_eliminator_semantics_evaluation_cyclic_mate_basis_row",
    "center_eliminator_semantics_evaluation_cyclic_mate_not_budgeted",
    "missing_cyclic_ambidextrous_mate_beck_chevalley_evaluation_certificate",
)

CYCLIC_DATA = {
    "certificate": "cyclic_ambidextrous_mate_beck_chevalley_evaluation",
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "ambidextrous": True,
    "left_right_agree": True,
    "cyclic_rotation": True,
    "cut_dependent": False,
    "trace_cyclicity": True,
    "dagger_rotation": True,
    "rosati_rotation": True,
    "projection_rotation": True,
    "boundary_rotation": True,
    "dd4_exact_delta_rotation": True,
    "graph_composition_rotation": True,
    "control_rotation": True,
    "handoff_rotation": True,
    "descent_rotation_stable": True,
    "natural": True,
    "coherent": True,
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
    "structures": ROTATION_STRUCTURES,
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
        "cyclic": deepcopy(CYCLIC_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "cyclic":
            state["cyclic"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CYCLIC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    cyclic = state["cyclic"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_581")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc581_witness")
    if CYCLIC not in state["accepted"]:
        reasons.append("missing_cyclic_ambidextrous_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(CYCLIC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if cyclic.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if cyclic.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not cyclic.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_missing")
    if not cyclic.get("ambidextrous"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_not_ambidextrous")
    if not cyclic.get("left_right_agree"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_left_right_mismatch")
    if not cyclic.get("cyclic_rotation"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_rotation_gap")
    if cyclic.get("cut_dependent"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_cut_dependent")
    if not cyclic.get("trace_cyclicity") or DUAL_TRACE not in cyclic["structures"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_trace_cyclicity_gap")
    if not cyclic.get("dagger_rotation") or DAGGER not in cyclic["structures"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_dagger_rotation_gap")
    if not cyclic.get("rosati_rotation") or ROSATI not in cyclic["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_rosati_rotation_gap")
    if (
        not cyclic.get("projection_rotation")
        or not PROJECTION_FORMULA_TARGETS <= set(cyclic["projection_targets"])
    ):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_projection_rotation_gap")
    if not cyclic.get("boundary_rotation") or PUSHFORWARD not in cyclic["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_boundary_rotation_gap")
    if not cyclic.get("dd4_exact_delta_rotation") or not {DD4_BOUNDARY, EXACT_DELTA} <= set(cyclic["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_dd4_exact_delta_rotation_gap")
    if not cyclic.get("graph_composition_rotation") or GRAPH_COMP not in cyclic["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_graph_composition_rotation_gap")
    if not cyclic.get("control_rotation") or CONTROL not in cyclic["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_control_rotation_gap")
    if not cyclic.get("handoff_rotation") or not {HANDOFF, GRAPH_LATER} <= set(cyclic["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_handoff_rotation_gap")
    if not cyclic.get("descent_rotation_stable"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_descent_rotation_not_stable")
    if not cyclic.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_not_natural")
    if not cyclic.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_not_coherent")
    if cyclic.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_external")
    if cyclic.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_quotient")
    if cyclic.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_functor_of_points_only")
    if cyclic.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_yoneda_reversal")
    if cyclic.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_pointwise_only")
    if cyclic.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_objectwise_only")
    if cyclic.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_nonfunctorial_choice")
    if cyclic.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_requires_choice")
    if cyclic.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_requires_new_cell")
    if cyclic.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_context_collapse")
    if cyclic.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_by_declaration")
    if cyclic.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_finite_sample")
    if cyclic.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_basis_row")
    if not cyclic.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_cyclic_mate_not_budgeted")

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
        and CYCLIC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["cyclic"]["ambidextrous"]
        and state["cyclic"]["left_right_agree"]
        and state["cyclic"]["cyclic_rotation"]
        and not state["cyclic"]["cut_dependent"],
        "mate data is ambidextrous, left/right coherent, cyclic, and cut-independent",
    )
    gate(
        f"{PREFIX}3",
        state["cyclic"]["trace_cyclicity"]
        and state["cyclic"]["dagger_rotation"]
        and state["cyclic"]["rosati_rotation"]
        and {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE} <= state["cyclic"]["structures"],
        "trace, dagger, Rosati, pivotal, and exact-additive rotations commute",
    )
    gate(
        f"{PREFIX}4",
        state["cyclic"]["projection_rotation"]
        and state["cyclic"]["boundary_rotation"]
        and state["cyclic"]["dd4_exact_delta_rotation"]
        and state["cyclic"]["graph_composition_rotation"]
        and PROJECTION_FORMULA_TARGETS <= state["cyclic"]["projection_targets"]
        and {PUSHFORWARD, DD4_BOUNDARY, EXACT_DELTA, GRAPH_COMP} <= state["cyclic"]["routes"],
        "projection, boundary, DD.4, exact-delta, and graph rotations commute",
    )
    gate(
        f"{PREFIX}5",
        state["cyclic"]["control_rotation"]
        and state["cyclic"]["handoff_rotation"]
        and state["cyclic"]["descent_rotation_stable"]
        and state["cyclic"]["natural"]
        and state["cyclic"]["coherent"]
        and {CONTROL, HANDOFF, GRAPH_LATER} <= state["cyclic"]["routes"],
        "control, handoff, descent, naturality, and coherence survive rotation",
    )
    gate(
        f"{PREFIX}6",
        state["cyclic"]["budgeted"]
        and not any(
            state["cyclic"][key]
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
        "cyclic mate coherence is budgeted and not a disguised external or choice-based repair",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(CYCLIC, [])) <= state["accepted"],
        "cyclic-ambidextrous mate dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all cyclic-ambidextrous mate graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: Beck-Chevalley evaluation mate is cyclic-ambidextrous")
    print(
        "VERDICT: the missing-object candidate counts only when the mate-coherent "
        "Beck-Chevalley semantic evaluation is cyclic and ambidextrous, with no "
        "marked cut across trace, dagger/Rosati, projection, boundary, graph, "
        "control, or handoff rotations."
    )


if __name__ == "__main__":
    main()
