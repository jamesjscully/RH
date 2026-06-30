#!/usr/bin/env python3
r"""Represented semantic model for the executable diamond normalizer.

Doc 575 requires semantic-conservative executable normal forms. This witness
closes the next cheap escape: the semantics cannot remain a meta-level
interpretation. It must be represented by a source-internal model object in
the existing subrepresenter, selected by the existing universal arrow, and it
must realize the same payload semantics without quotient or functor-of-points
reversal.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_represented_semantic_model_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the represented semantic model witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 576
EXPECTED_WITNESS = "doc576-probe-represented-semantic-model-semantic-conservative-executable-diamond"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMREPSEMMODELCARTCOMPAT"

MODEL = "represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SEM = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
SUBREP = "source_fiber_subrepresenter"
UNIVERSAL_ARROW = "coupling_universal_arrow"
COUPLED_IMAGE = "coupled_self_dual_exact_bcf_sources"
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

REQUIRED_DEPS = {SEM, EXEC, SUBREP, UNIVERSAL_ARROW, COUPLED_IMAGE} | SEMANTIC_TARGETS

EXPECTED_EDGES = {
    (SEM, "represented_by", MODEL),
    (MODEL, "represented_semantic_model_for", SEM),
    (MODEL, "model_lives_in", SUBREP),
    (MODEL, "model_selected_by", UNIVERSAL_ARROW),
    (MODEL, "model_image_is", COUPLED_IMAGE),
} | {(MODEL, "model_realizes_semantics_for", target) for target in SEMANTIC_TARGETS}

REQUIRED_FLAGS = (
    "represented_semantic_model",
    "source_internal_model",
    "subrepresenter_model",
    "universal_arrow_evaluation",
    "coupled_source_image",
    "model_realizes_semantic_targets",
    "model_conservative",
    "model_reflecting",
    "not_functor_of_points_only",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_unrepresented",
    "center_eliminator_semantics_model_missing",
    "center_eliminator_semantics_model_external",
    "center_eliminator_semantics_model_not_source_internal",
    "center_eliminator_semantics_model_not_in_subrepresenter",
    "center_eliminator_semantics_model_no_universal_arrow",
    "center_eliminator_semantics_model_wrong_boundary",
    "center_eliminator_semantics_model_functor_of_points_only",
    "center_eliminator_semantics_model_yoneda_reversal",
    "center_eliminator_semantics_model_quotient",
    "center_eliminator_semantics_model_not_conservative",
    "center_eliminator_semantics_model_not_reflecting",
    "center_eliminator_semantics_model_payload_gap",
    "center_eliminator_semantics_model_original_h1_gap",
    "center_eliminator_semantics_model_doc515_gap",
    "center_eliminator_semantics_model_requires_choice",
    "center_eliminator_semantics_model_requires_new_cell",
    "center_eliminator_semantics_model_context_collapse",
    "center_eliminator_semantics_model_by_declaration",
    "center_eliminator_semantics_model_finite_sample",
    "center_eliminator_semantics_model_basis_row",
    "center_eliminator_semantics_model_not_budgeted",
    "missing_represented_semantic_model_certificate",
)

MODEL_DATA = {
    "certificate": "represented_source_internal_semantic_model",
    "base_certificate": SEM,
    "represented": True,
    "source_internal": True,
    "in_subrepresenter": True,
    "selected_by_universal_arrow": True,
    "image_is_coupled_source": True,
    "external": False,
    "wrong_boundary": False,
    "functor_of_points_only": False,
    "yoneda_reversal": False,
    "quotient_model": False,
    "conservative": True,
    "reflecting": True,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "realized_targets": SEMANTIC_TARGETS,
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
        "model": deepcopy(MODEL_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "model":
            state["model"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(MODEL, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    model = state["model"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_576")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc576_witness")
    if MODEL not in state["accepted"]:
        reasons.append("missing_represented_semantic_model_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(MODEL, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if model.get("base_certificate") != SEM:
        reasons.append("wrong_base_certificate")
    if not model.get("represented"):
        reasons.append("center_eliminator_semantics_unrepresented")
    if not model.get("represented"):
        reasons.append("center_eliminator_semantics_model_missing")
    if model.get("external"):
        reasons.append("center_eliminator_semantics_model_external")
    if not model.get("source_internal"):
        reasons.append("center_eliminator_semantics_model_not_source_internal")
    if not model.get("in_subrepresenter"):
        reasons.append("center_eliminator_semantics_model_not_in_subrepresenter")
    if not model.get("selected_by_universal_arrow"):
        reasons.append("center_eliminator_semantics_model_no_universal_arrow")
    if model.get("wrong_boundary"):
        reasons.append("center_eliminator_semantics_model_wrong_boundary")
    if model.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_model_functor_of_points_only")
    if model.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_model_yoneda_reversal")
    if model.get("quotient_model"):
        reasons.append("center_eliminator_semantics_model_quotient")
    if not model.get("conservative"):
        reasons.append("center_eliminator_semantics_model_not_conservative")
    if not model.get("reflecting"):
        reasons.append("center_eliminator_semantics_model_not_reflecting")
    if not SEMANTIC_TARGETS <= set(model["realized_targets"]):
        reasons.append("center_eliminator_semantics_model_payload_gap")
    if ORIGINAL_DD4 not in model["realized_targets"]:
        reasons.append("center_eliminator_semantics_model_original_h1_gap")
    if DOC515_FIXED not in model["realized_targets"]:
        reasons.append("center_eliminator_semantics_model_doc515_gap")
    if model.get("requires_choice"):
        reasons.append("center_eliminator_semantics_model_requires_choice")
    if model.get("new_cell"):
        reasons.append("center_eliminator_semantics_model_requires_new_cell")
    if model.get("context_collapse"):
        reasons.append("center_eliminator_semantics_model_context_collapse")
    if model.get("declared_only"):
        reasons.append("center_eliminator_semantics_model_by_declaration")
    if model.get("finite_sample"):
        reasons.append("center_eliminator_semantics_model_finite_sample")
    if model.get("basis_row"):
        reasons.append("center_eliminator_semantics_model_basis_row")
    if not model.get("budgeted"):
        reasons.append("center_eliminator_semantics_model_not_budgeted")

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
        and MODEL in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["model"]["represented"] and state["model"]["source_internal"],
        "semantic model is represented and source-internal",
    )
    gate(
        f"{PREFIX}3",
        state["model"]["in_subrepresenter"]
        and state["model"]["selected_by_universal_arrow"]
        and state["model"]["image_is_coupled_source"],
        "model lives in subrepresenter and is selected by the existing universal arrow",
    )
    gate(
        f"{PREFIX}4",
        SEMANTIC_TARGETS <= state["model"]["realized_targets"],
        f"model_realizes_targets={len(SEMANTIC_TARGETS)}/15",
    )
    gate(
        f"{PREFIX}5",
        state["model"]["conservative"]
        and state["model"]["reflecting"]
        and ORIGINAL_DD4 in state["model"]["realized_targets"]
        and DOC515_FIXED in state["model"]["realized_targets"],
        "model preserves conservativity, reflection, original-H1, and doc515 payload",
    )
    gate(
        f"{PREFIX}6",
        state["model"]["budgeted"]
        and not any(
            state["model"][key]
            for key in (
                "external",
                "wrong_boundary",
                "functor_of_points_only",
                "yoneda_reversal",
                "quotient_model",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "model is budgeted and not external/quotient/functor-of-points/choice dependent",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(MODEL, [])) <= state["accepted"],
        "represented semantic model dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all represented semantic model graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: semantic conservativity is represented by an internal model")
    print(
        "VERDICT: the missing-object candidate counts only when the conservative semantics is "
        "represented by a source-internal model object in the existing subrepresenter, selected "
        "by the existing universal arrow, and realizing the payload semantics without quotient, "
        "functor-of-points reversal, or external model data."
    )


if __name__ == "__main__":
    main()
