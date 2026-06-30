#!/usr/bin/env python3
r"""Normal-form reflection for the pasting-stable cyclic Beck-Chevalley mate.

Doc 582 requires the cyclic-ambidextrous Beck-Chevalley mate to paste as an
internal source-square calculus. This witness closes the next cheap escape:
the pasting calculus may still be a diagrammatic proof object whose
composites are not reflected by the already accepted finite executable
normal forms. The current frontier only counts if every pasted cyclic mate
composite reduces to the same source-internal normal form through the
existing terminating critical-pair diamond normalizer and its conservative
represented semantics.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the normal-form reflecting cyclic mate witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    BASE_CHANGE_ROUTES,
    BC,
    CONTROL,
    CYCLIC,
    DD4_BOUNDARY,
    DIAG,
    EVAL,
    EXACT_DELTA,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    MAP_PATH,
    MATE,
    PASTE,
    PRESERVED_CONTEXTS,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    ROSATI,
    SUBREP,
    UNIVERSAL_ARROW,
)


EXPECTED_DOC = 583
EXPECTED_WITNESS = "doc583-probe-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNFREFLPASTECYCMATEBCHEVEVAL"

NORMREF = "normal_form_reflecting_" + PASTE
NORM = "normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FUNC_NORM = "functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MONEXACT_DAGGER = "monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
COHERENT = "coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SEMCONS = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REPSEM = "represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"

failures: list[str] = []

NORMALIZER_DEPS = {NORM, FUNC_NORM, MONEXACT_DAGGER, COHERENT, EXEC, SEMCONS, REPSEM}
REQUIRED_DEPS = {
    PASTE,
    CYCLIC,
    MATE,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | NORMALIZER_DEPS | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (PASTE, "made_normal_form_reflecting_by", NORMREF),
    (NORMREF, "normal_form_reflecting_for", PASTE),
    (NORMREF, "reflects_cyclic_mate_of", CYCLIC),
    (NORMREF, "reflects_mate_of", MATE),
    (NORMREF, "reflects_base_change_for", BC),
    (NORMREF, "reflects_evaluation_for", EVAL),
    (NORMREF, "normal_form_coherent_over", DIAG),
    (NORMREF, "normal_form_internal_to", SUBREP),
    (NORMREF, "normal_form_selected_by", UNIVERSAL_ARROW),
    (NORMREF, "normalizes_via", NORM),
    (NORMREF, "functorial_normalizes_via", FUNC_NORM),
    (NORMREF, "monoidal_exact_dagger_normal_form_for", MONEXACT_DAGGER),
    (NORMREF, "coherent_normal_form_for", COHERENT),
    (NORMREF, "executable_diamonds_via", EXEC),
    (NORMREF, "semantically_reflects_via", SEMCONS),
    (NORMREF, "represented_semantics_via", REPSEM),
} | {
    (NORMREF, "normal_form_preserves_projection_formula_for", target)
    for target in PROJECTION_FORMULA_TARGETS
} | {(NORMREF, "normal_form_reflects_route", target) for target in BASE_CHANGE_ROUTES} | {
    (NORMREF, "normal_form_preserves", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "normal_form_reflecting_certificate",
    "pasted_composites_normalize",
    "vertical_horizontal_same_normal_form",
    "interchange_same_normal_form",
    "unit_associator_unitor_same_normal_form",
    "trace_sliding_same_normal_form",
    "critical_pair_diamond_normalizer",
    "semantic_conservative_reflection",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_nf_mate_missing",
    "center_eliminator_semantics_evaluation_nf_mate_not_reflected",
    "center_eliminator_semantics_evaluation_nf_mate_normal_form_gap",
    "center_eliminator_semantics_evaluation_nf_mate_composite_gap",
    "center_eliminator_semantics_evaluation_nf_mate_vertical_gap",
    "center_eliminator_semantics_evaluation_nf_mate_horizontal_gap",
    "center_eliminator_semantics_evaluation_nf_mate_interchange_gap",
    "center_eliminator_semantics_evaluation_nf_mate_unit_gap",
    "center_eliminator_semantics_evaluation_nf_mate_associator_unitor_gap",
    "center_eliminator_semantics_evaluation_nf_mate_trace_sliding_gap",
    "center_eliminator_semantics_evaluation_nf_mate_critical_pair_gap",
    "center_eliminator_semantics_evaluation_nf_mate_confluence_gap",
    "center_eliminator_semantics_evaluation_nf_mate_termination_gap",
    "center_eliminator_semantics_evaluation_nf_mate_semantic_reflection_gap",
    "center_eliminator_semantics_evaluation_nf_mate_invariant_reflection_gap",
    "center_eliminator_semantics_evaluation_nf_mate_projection_formula_gap",
    "center_eliminator_semantics_evaluation_nf_mate_boundary_gap",
    "center_eliminator_semantics_evaluation_nf_mate_dd4_exact_delta_gap",
    "center_eliminator_semantics_evaluation_nf_mate_graph_gap",
    "center_eliminator_semantics_evaluation_nf_mate_rosati_gap",
    "center_eliminator_semantics_evaluation_nf_mate_control_gap",
    "center_eliminator_semantics_evaluation_nf_mate_handoff_gap",
    "center_eliminator_semantics_evaluation_nf_mate_descent_not_stable",
    "center_eliminator_semantics_evaluation_nf_mate_not_natural",
    "center_eliminator_semantics_evaluation_nf_mate_not_coherent",
    "center_eliminator_semantics_evaluation_nf_mate_external_rewrite",
    "center_eliminator_semantics_evaluation_nf_mate_quotient_normal_form",
    "center_eliminator_semantics_evaluation_nf_mate_functor_of_points_only",
    "center_eliminator_semantics_evaluation_nf_mate_yoneda_reversal",
    "center_eliminator_semantics_evaluation_nf_mate_pointwise_only",
    "center_eliminator_semantics_evaluation_nf_mate_objectwise_only",
    "center_eliminator_semantics_evaluation_nf_mate_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_nf_mate_requires_choice",
    "center_eliminator_semantics_evaluation_nf_mate_requires_new_cell",
    "center_eliminator_semantics_evaluation_nf_mate_context_collapse",
    "center_eliminator_semantics_evaluation_nf_mate_by_declaration",
    "center_eliminator_semantics_evaluation_nf_mate_finite_sample",
    "center_eliminator_semantics_evaluation_nf_mate_basis_row",
    "center_eliminator_semantics_evaluation_nf_mate_not_budgeted",
    "missing_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

NF_DATA = {
    "certificate": "normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "normal_form_reflecting": True,
    "pasted_composites_normalize": True,
    "vertical_normal_form": True,
    "horizontal_normal_form": True,
    "interchange_normal_form": True,
    "unit_normal_form": True,
    "associator_unitor_normal_form": True,
    "trace_sliding_normal_form": True,
    "critical_pair_diamonds": True,
    "confluent": True,
    "terminating": True,
    "semantic_reflection": True,
    "invariant_reflection": True,
    "projection_formula_normal_form": True,
    "boundary_normal_form": True,
    "dd4_exact_delta_normal_form": True,
    "graph_normal_form": True,
    "rosati_normal_form": True,
    "control_normal_form": True,
    "handoff_normal_form": True,
    "descent_normal_form_stable": True,
    "natural": True,
    "coherent": True,
    "external_rewrite": False,
    "quotient_normal_form": False,
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
    "normalizer_deps": NORMALIZER_DEPS,
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
        "nf": deepcopy(NF_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "nf":
            state["nf"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(NORMREF, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    nf = state["nf"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_583")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc583_witness")
    if NORMREF not in state["accepted"]:
        reasons.append("missing_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(NORMREF, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if nf.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if nf.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if nf.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if nf.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not nf.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_missing")
    if not nf.get("normal_form_reflecting"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_not_reflected")
    if not nf.get("pasted_composites_normalize"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_composite_gap")
    if not nf.get("vertical_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_vertical_gap")
    if not nf.get("horizontal_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_horizontal_gap")
    if not nf.get("interchange_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_interchange_gap")
    if not nf.get("unit_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_unit_gap")
    if not nf.get("associator_unitor_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_associator_unitor_gap")
    if not nf.get("trace_sliding_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_trace_sliding_gap")
    if not nf.get("critical_pair_diamonds") or EXEC not in nf["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_critical_pair_gap")
    if not nf.get("confluent") or NORM not in nf["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_confluence_gap")
    if not nf.get("terminating") or FUNC_NORM not in nf["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_termination_gap")
    if not nf.get("semantic_reflection") or SEMCONS not in nf["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_semantic_reflection_gap")
    if not nf.get("invariant_reflection") or REPSEM not in nf["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_invariant_reflection_gap")
    if not nf.get("projection_formula_normal_form") or not PROJECTION_FORMULA_TARGETS <= set(nf["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_projection_formula_gap")
    if not nf.get("boundary_normal_form") or PUSHFORWARD not in nf["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_boundary_gap")
    if not nf.get("dd4_exact_delta_normal_form") or not {DD4_BOUNDARY, EXACT_DELTA} <= set(nf["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_dd4_exact_delta_gap")
    if not nf.get("graph_normal_form") or GRAPH_COMP not in nf["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_graph_gap")
    if not nf.get("rosati_normal_form") or ROSATI not in nf["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_rosati_gap")
    if not nf.get("control_normal_form") or CONTROL not in nf["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_control_gap")
    if not nf.get("handoff_normal_form") or not {HANDOFF, GRAPH_LATER} <= set(nf["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_handoff_gap")
    if not nf.get("descent_normal_form_stable"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_descent_not_stable")
    if not nf.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_not_natural")
    if not nf.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_not_coherent")
    if nf.get("external_rewrite"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_external_rewrite")
    if nf.get("quotient_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_quotient_normal_form")
    if nf.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_functor_of_points_only")
    if nf.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_yoneda_reversal")
    if nf.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_pointwise_only")
    if nf.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_objectwise_only")
    if nf.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_nonfunctorial_choice")
    if nf.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_requires_choice")
    if nf.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_requires_new_cell")
    if nf.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_context_collapse")
    if nf.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_by_declaration")
    if nf.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_finite_sample")
    if nf.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_basis_row")
    if not nf.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_not_budgeted")

    if not (
        nf.get("normal_form_reflecting")
        and nf.get("pasted_composites_normalize")
        and nf.get("vertical_normal_form")
        and nf.get("horizontal_normal_form")
    ):
        reasons.append("center_eliminator_semantics_evaluation_nf_mate_normal_form_gap")

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
        and NORMREF in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["nf"]["normal_form_reflecting"]
        and state["nf"]["pasted_composites_normalize"]
        and state["nf"]["vertical_normal_form"]
        and state["nf"]["horizontal_normal_form"],
        "pasted vertical and horizontal composites reduce to source-internal normal forms",
    )
    gate(
        f"{PREFIX}3",
        state["nf"]["interchange_normal_form"]
        and state["nf"]["unit_normal_form"]
        and state["nf"]["associator_unitor_normal_form"]
        and state["nf"]["trace_sliding_normal_form"],
        "interchange, unit, associator/unitor, and trace-sliding laws share normal forms",
    )
    gate(
        f"{PREFIX}4",
        state["nf"]["critical_pair_diamonds"]
        and state["nf"]["confluent"]
        and state["nf"]["terminating"]
        and {NORM, FUNC_NORM, COHERENT, EXEC} <= state["nf"]["normalizer_deps"],
        "existing finite diamond normalizer proves the pasted mate equalities",
    )
    gate(
        f"{PREFIX}5",
        state["nf"]["semantic_reflection"]
        and state["nf"]["invariant_reflection"]
        and {SEMCONS, REPSEM} <= state["nf"]["normalizer_deps"],
        "represented semantics conservatively reflects pasted normal-form equality",
    )
    gate(
        f"{PREFIX}6",
        state["nf"]["projection_formula_normal_form"]
        and state["nf"]["boundary_normal_form"]
        and state["nf"]["dd4_exact_delta_normal_form"]
        and state["nf"]["graph_normal_form"]
        and state["nf"]["rosati_normal_form"]
        and state["nf"]["control_normal_form"]
        and state["nf"]["handoff_normal_form"]
        and PROJECTION_FORMULA_TARGETS <= state["nf"]["projection_targets"]
        and {PUSHFORWARD, DD4_BOUNDARY, EXACT_DELTA, GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["nf"]["routes"],
        "projection, boundary, DD.4, graph, Rosati, control, and handoff routes normalize",
    )
    gate(
        f"{PREFIX}7",
        state["nf"]["budgeted"]
        and state["nf"]["descent_normal_form_stable"]
        and state["nf"]["natural"]
        and state["nf"]["coherent"]
        and not any(
            state["nf"][key]
            for key in (
                "external_rewrite",
                "quotient_normal_form",
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
        "normal-form reflection is descent-stable, budgeted, natural, coherent, and not a disguised repair",
    )
    gate(
        f"{PREFIX}8",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(NORMREF, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "normal-form reflecting pasted mate dependency closure and graph edges are wired",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: pasted cyclic mate equalities are reflected by normal forms")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "pasting-stable cyclic Beck-Chevalley mate is reflected by the existing "
        "finite executable normalizer and conservative represented semantics; "
        "diagrammatic pasting that does not normalize is only decoration."
    )


if __name__ == "__main__":
    main()
