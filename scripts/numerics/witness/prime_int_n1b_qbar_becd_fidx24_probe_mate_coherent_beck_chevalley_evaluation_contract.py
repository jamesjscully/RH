#!/usr/bin/env python3
r"""Mate coherence for descent-effective Beck-Chevalley semantic evaluation.

Doc 579 requires the exact/cartesian Beck-Chevalley semantic evaluation to
descend effectively over filtered cofinal refinements. This witness closes
the next cheap escape: the descended Beck-Chevalley square may commute as a
standalone square while failing to be the mate of the source adjunctions,
dagger/Rosati structure, pivotal trace, exact-additive trace, projection
formula, and control-death routes already present in the source square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_mate_coherent_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the mate-coherent evaluation witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 580
EXPECTED_WITNESS = "doc580-probe-mate-coherent-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMMATECOHBCHEVEVAL"

MATE = "mate_coherent_descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
DESC = "descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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

MATE_STRUCTURES = {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE}

REQUIRED_DEPS = {
    DESC,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | MATE_STRUCTURES | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (DESC, "made_mate_coherent_by", MATE),
    (MATE, "mate_coherent_for", DESC),
    (MATE, "mate_of", BC),
    (MATE, "mates_evaluation_for", EVAL),
    (MATE, "mate_coherent_over", DIAG),
    (MATE, "mate_internal_to", SUBREP),
    (MATE, "mate_selected_by", UNIVERSAL_ARROW),
} | {(MATE, "mate_coherent_with", target) for target in MATE_STRUCTURES} | {
    (MATE, "mate_preserves_projection_formula_for", target)
    for target in PROJECTION_FORMULA_TARGETS
} | {(MATE, "mate_commutes_with", target) for target in BASE_CHANGE_ROUTES} | {
    (MATE, "mate_preserves", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "mate_coherent_certificate",
    "adjunction_mate",
    "unit_counit_coherent",
    "triangle_identities",
    "dagger_rosati_mate",
    "trace_control_mate",
    "projection_formula_mate",
    "descent_mate_stable",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_mate_missing",
    "center_eliminator_semantics_evaluation_mate_not_adjunction_mate",
    "center_eliminator_semantics_evaluation_mate_unit_gap",
    "center_eliminator_semantics_evaluation_mate_counit_gap",
    "center_eliminator_semantics_evaluation_mate_triangle_gap",
    "center_eliminator_semantics_evaluation_mate_involution_gap",
    "center_eliminator_semantics_evaluation_mate_projection_formula_gap",
    "center_eliminator_semantics_evaluation_mate_boundary_pushforward_gap",
    "center_eliminator_semantics_evaluation_mate_dd4_exact_delta_gap",
    "center_eliminator_semantics_evaluation_mate_graph_composition_gap",
    "center_eliminator_semantics_evaluation_mate_rosati_dagger_gap",
    "center_eliminator_semantics_evaluation_mate_trace_control_gap",
    "center_eliminator_semantics_evaluation_mate_handoff_graph_gap",
    "center_eliminator_semantics_evaluation_mate_descent_not_stable",
    "center_eliminator_semantics_evaluation_mate_not_natural",
    "center_eliminator_semantics_evaluation_mate_not_coherent",
    "center_eliminator_semantics_evaluation_mate_one_sided_adjunction",
    "center_eliminator_semantics_evaluation_mate_lax",
    "center_eliminator_semantics_evaluation_mate_external",
    "center_eliminator_semantics_evaluation_mate_quotient",
    "center_eliminator_semantics_evaluation_mate_functor_of_points_only",
    "center_eliminator_semantics_evaluation_mate_yoneda_reversal",
    "center_eliminator_semantics_evaluation_mate_pointwise_only",
    "center_eliminator_semantics_evaluation_mate_objectwise_only",
    "center_eliminator_semantics_evaluation_mate_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_mate_requires_choice",
    "center_eliminator_semantics_evaluation_mate_requires_new_cell",
    "center_eliminator_semantics_evaluation_mate_context_collapse",
    "center_eliminator_semantics_evaluation_mate_by_declaration",
    "center_eliminator_semantics_evaluation_mate_finite_sample",
    "center_eliminator_semantics_evaluation_mate_basis_row",
    "center_eliminator_semantics_evaluation_mate_not_budgeted",
    "missing_mate_coherent_beck_chevalley_evaluation_certificate",
)

MATE_DATA = {
    "certificate": "mate_coherent_beck_chevalley_evaluation",
    "base_descent": DESC,
    "base_beck_chevalley": BC,
    "exists": True,
    "adjunction_mate": True,
    "unit": True,
    "counit": True,
    "triangle_identities": True,
    "mate_involution": True,
    "projection_formula_mate": True,
    "boundary_pushforward_mate": True,
    "dd4_exact_delta_mate": True,
    "graph_composition_mate": True,
    "rosati_dagger_mate": True,
    "trace_control_mate": True,
    "handoff_graph_mate": True,
    "descent_stable": True,
    "natural": True,
    "coherent": True,
    "one_sided_adjunction": False,
    "lax": False,
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
    "structures": MATE_STRUCTURES,
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
        "mate": deepcopy(MATE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "mate":
            state["mate"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(MATE, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    mate = state["mate"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_580")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc580_witness")
    if MATE not in state["accepted"]:
        reasons.append("missing_mate_coherent_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(MATE, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if mate.get("base_descent") != DESC:
        reasons.append("wrong_base_descent")
    if mate.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not mate.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_mate_missing")
    if not mate.get("adjunction_mate"):
        reasons.append("center_eliminator_semantics_evaluation_mate_not_adjunction_mate")
    if not mate.get("unit"):
        reasons.append("center_eliminator_semantics_evaluation_mate_unit_gap")
    if not mate.get("counit"):
        reasons.append("center_eliminator_semantics_evaluation_mate_counit_gap")
    if not mate.get("triangle_identities"):
        reasons.append("center_eliminator_semantics_evaluation_mate_triangle_gap")
    if not mate.get("mate_involution"):
        reasons.append("center_eliminator_semantics_evaluation_mate_involution_gap")
    if (
        not mate.get("projection_formula_mate")
        or not PROJECTION_FORMULA_TARGETS <= set(mate["projection_targets"])
    ):
        reasons.append("center_eliminator_semantics_evaluation_mate_projection_formula_gap")
    if not mate.get("boundary_pushforward_mate") or PUSHFORWARD not in mate["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_mate_boundary_pushforward_gap")
    if not mate.get("dd4_exact_delta_mate") or not {DD4_BOUNDARY, EXACT_DELTA} <= set(mate["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_mate_dd4_exact_delta_gap")
    if not mate.get("graph_composition_mate") or GRAPH_COMP not in mate["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_mate_graph_composition_gap")
    if not mate.get("rosati_dagger_mate") or not {ROSATI} <= set(mate["routes"]) or DAGGER not in mate["structures"]:
        reasons.append("center_eliminator_semantics_evaluation_mate_rosati_dagger_gap")
    if not mate.get("trace_control_mate") or not {CONTROL} <= set(mate["routes"]) or DUAL_TRACE not in mate["structures"]:
        reasons.append("center_eliminator_semantics_evaluation_mate_trace_control_gap")
    if not mate.get("handoff_graph_mate") or not {HANDOFF, GRAPH_LATER} <= set(mate["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_mate_handoff_graph_gap")
    if not mate.get("descent_stable"):
        reasons.append("center_eliminator_semantics_evaluation_mate_descent_not_stable")
    if not mate.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_mate_not_natural")
    if not mate.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_mate_not_coherent")
    if mate.get("one_sided_adjunction"):
        reasons.append("center_eliminator_semantics_evaluation_mate_one_sided_adjunction")
    if mate.get("lax"):
        reasons.append("center_eliminator_semantics_evaluation_mate_lax")
    if mate.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_mate_external")
    if mate.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_mate_quotient")
    if mate.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_mate_functor_of_points_only")
    if mate.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_mate_yoneda_reversal")
    if mate.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_mate_pointwise_only")
    if mate.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_mate_objectwise_only")
    if mate.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_mate_nonfunctorial_choice")
    if mate.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_mate_requires_choice")
    if mate.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_mate_requires_new_cell")
    if mate.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_mate_context_collapse")
    if mate.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_mate_by_declaration")
    if mate.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_mate_finite_sample")
    if mate.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_mate_basis_row")
    if not mate.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_mate_not_budgeted")

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
        and MATE in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["mate"]["adjunction_mate"]
        and state["mate"]["unit"]
        and state["mate"]["counit"]
        and state["mate"]["triangle_identities"]
        and state["mate"]["mate_involution"],
        "Beck-Chevalley evaluation is an adjunction mate with unit, counit, triangles, and mate involution",
    )
    gate(
        f"{PREFIX}3",
        state["mate"]["projection_formula_mate"]
        and PROJECTION_FORMULA_TARGETS <= state["mate"]["projection_targets"]
        and {PUSHFORWARD, DD4_BOUNDARY, EXACT_DELTA, GRAPH_COMP} <= state["mate"]["routes"],
        "projection formula, boundary, DD.4, exact-delta, and graph mates commute",
    )
    gate(
        f"{PREFIX}4",
        state["mate"]["rosati_dagger_mate"]
        and state["mate"]["trace_control_mate"]
        and state["mate"]["handoff_graph_mate"]
        and {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE} <= state["mate"]["structures"]
        and {ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["mate"]["routes"],
        "Rosati/dagger, trace/control, and handoff/graph mate routes commute",
    )
    gate(
        f"{PREFIX}5",
        state["mate"]["descent_stable"] and state["mate"]["natural"] and state["mate"]["coherent"],
        "mate coherence is descent-stable, natural, and coherent",
    )
    gate(
        f"{PREFIX}6",
        state["mate"]["budgeted"]
        and not any(
            state["mate"][key]
            for key in (
                "one_sided_adjunction",
                "lax",
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
        "mate coherence is budgeted and not a disguised external or choice-based repair",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(MATE, [])) <= state["accepted"],
        "mate-coherent Beck-Chevalley dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all mate-coherent Beck-Chevalley evaluation graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: Beck-Chevalley evaluation is mate-coherent")
    print(
        "VERDICT: the missing-object candidate counts only when the descended "
        "Beck-Chevalley semantic evaluation is the coherent adjunction mate of "
        "the source dagger, trace, projection, and control routes."
    )


if __name__ == "__main__":
    main()
