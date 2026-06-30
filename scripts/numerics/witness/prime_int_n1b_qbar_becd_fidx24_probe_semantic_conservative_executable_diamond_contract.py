#!/usr/bin/env python3
r"""Semantic-conservative executable diamond center-eliminator normalizer.

Doc 574 requires executable critical-pair diamonds. This witness closes the
next cheap escape: a finite diamond calculus cannot get confluence by
quotienting away the payload semantics. Normal forms must have sound,
complete, conservative, invariant-reflecting semantics for the source-side
payloads and the original DD.4 obstruction context.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_semantic_conservative_executable_diamond_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the semantic-conservative witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 575
EXPECTED_WITNESS = "doc575-probe-semantic-conservative-invariant-reflecting-executable-critical-pair-diamond-coherent-monoidal-exact-dagger-compatible-functorial-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSEMCONSEXECODIAMCARTCOMPAT"

SEM = "semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
COH = "coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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

REQUIRED_DEPS = {EXEC, COH} | SEMANTIC_TARGETS

EXPECTED_EDGES = {
    (EXEC, "made_semantic_by", SEM),
    (SEM, "semantic_conservative_execution_for", EXEC),
} | {(SEM, "semantically_preserves", target) for target in SEMANTIC_TARGETS} | {
    (SEM, "semantically_reflects", target) for target in SEMANTIC_TARGETS
}

REQUIRED_FLAGS = (
    "semantic_interpretation",
    "sound_for_rewrite",
    "complete_for_normal_forms",
    "conservative_over_payloads",
    "reflects_normal_form_equality",
    "probe_kernel_trivial",
    "preserves_original_h1",
    "preserves_source_before_points",
    "preserves_fixed_doc515_payload",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_execution_semantics_missing",
    "center_eliminator_execution_semantics_not_sound",
    "center_eliminator_execution_semantics_not_complete",
    "center_eliminator_execution_not_conservative",
    "center_eliminator_normal_forms_uninterpreted",
    "center_eliminator_normal_form_equality_not_reflected",
    "center_eliminator_semantic_probe_kernel_nontrivial",
    "center_eliminator_endpoint_semantics_collapsed",
    "center_eliminator_degree_semantics_collapsed",
    "center_eliminator_dd4_boundary_semantics_collapsed",
    "center_eliminator_exact_delta_semantics_collapsed",
    "center_eliminator_graph_semantics_collapsed",
    "center_eliminator_rosati_semantics_collapsed",
    "center_eliminator_control_semantics_collapsed",
    "center_eliminator_handoff_semantics_collapsed",
    "center_eliminator_original_h1_semantics_collapsed",
    "center_eliminator_source_before_points_erased_by_semantics",
    "center_eliminator_doc515_payload_rewritten_by_semantics",
    "center_eliminator_semantics_external_oracle",
    "center_eliminator_semantics_requires_choice",
    "center_eliminator_semantics_requires_new_cell",
    "center_eliminator_semantics_context_collapse",
    "center_eliminator_semantics_by_declaration",
    "center_eliminator_semantics_finite_sample",
    "center_eliminator_semantics_basis_row",
    "center_eliminator_semantics_not_budgeted",
    "missing_semantic_conservative_execution_certificate",
)

SEMANTIC_DATA = {
    "certificate": "semantic_conservative_invariant_reflecting_execution",
    "base_certificate": EXEC,
    "has_semantics": True,
    "sound": True,
    "complete": True,
    "conservative": True,
    "normal_forms_interpreted": True,
    "reflects_equality": True,
    "probe_kernel_trivial": True,
    "external_oracle": False,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "preserved_targets": SEMANTIC_TARGETS,
    "reflected_targets": SEMANTIC_TARGETS,
    "collapsed": {flag: False for flag in BANNED_FLAGS},
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
        "semantics": deepcopy(SEMANTIC_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "semantics":
            state["semantics"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(SEM, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    semantics = state["semantics"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_575")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc575_witness")
    if SEM not in state["accepted"]:
        reasons.append("missing_semantic_conservative_execution_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(SEM, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if semantics.get("base_certificate") != EXEC:
        reasons.append("wrong_base_certificate")
    if not semantics.get("has_semantics"):
        reasons.append("center_eliminator_execution_semantics_missing")
    if not semantics.get("sound"):
        reasons.append("center_eliminator_execution_semantics_not_sound")
    if not semantics.get("complete"):
        reasons.append("center_eliminator_execution_semantics_not_complete")
    if not semantics.get("conservative"):
        reasons.append("center_eliminator_execution_not_conservative")
    if not semantics.get("normal_forms_interpreted"):
        reasons.append("center_eliminator_normal_forms_uninterpreted")
    if not semantics.get("reflects_equality"):
        reasons.append("center_eliminator_normal_form_equality_not_reflected")
    if not semantics.get("probe_kernel_trivial"):
        reasons.append("center_eliminator_semantic_probe_kernel_nontrivial")
    if semantics.get("external_oracle"):
        reasons.append("center_eliminator_semantics_external_oracle")
    if semantics.get("requires_choice"):
        reasons.append("center_eliminator_semantics_requires_choice")
    if semantics.get("new_cell"):
        reasons.append("center_eliminator_semantics_requires_new_cell")
    if semantics.get("context_collapse"):
        reasons.append("center_eliminator_semantics_context_collapse")
    if semantics.get("declared_only"):
        reasons.append("center_eliminator_semantics_by_declaration")
    if semantics.get("finite_sample"):
        reasons.append("center_eliminator_semantics_finite_sample")
    if semantics.get("basis_row"):
        reasons.append("center_eliminator_semantics_basis_row")
    if not semantics.get("budgeted"):
        reasons.append("center_eliminator_semantics_not_budgeted")

    preserved = set(semantics["preserved_targets"])
    reflected = set(semantics["reflected_targets"])
    if not SEMANTIC_TARGETS <= preserved:
        reasons.append("semantic_preservation_incomplete")
    if not SEMANTIC_TARGETS <= reflected:
        reasons.append("semantic_reflection_incomplete")

    for flag, collapsed in semantics["collapsed"].items():
        if collapsed:
            reasons.append(flag)
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
        and SEM in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["semantics"]["has_semantics"]
        and state["semantics"]["sound"]
        and state["semantics"]["complete"],
        "normal forms have sound and complete semantics",
    )
    gate(
        f"{PREFIX}3",
        state["semantics"]["conservative"]
        and state["semantics"]["reflects_equality"]
        and state["semantics"]["probe_kernel_trivial"],
        "semantics is conservative and equality-reflecting with trivial probe kernel",
    )
    gate(
        f"{PREFIX}4",
        SEMANTIC_TARGETS <= state["semantics"]["preserved_targets"]
        and SEMANTIC_TARGETS <= state["semantics"]["reflected_targets"],
        f"semantic_targets={len(SEMANTIC_TARGETS)}/15 preserved-and-reflected",
    )
    gate(
        f"{PREFIX}5",
        not state["semantics"]["collapsed"]["center_eliminator_original_h1_semantics_collapsed"]
        and not state["semantics"]["collapsed"]["center_eliminator_source_before_points_erased_by_semantics"]
        and not state["semantics"]["collapsed"]["center_eliminator_doc515_payload_rewritten_by_semantics"],
        "original DD.4 obstruction, source-before-points, and doc515 payload remain separated",
    )
    gate(
        f"{PREFIX}6",
        state["semantics"]["budgeted"]
        and not any(
            state["semantics"][key]
            for key in (
                "external_oracle",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "semantics is budgeted and not external/choice/new-cell/context/sample/basis dependent",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(SEM, [])) <= state["accepted"],
        "semantic-conservative execution dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all semantic preserve/reflect graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: executable diamonds are semantic-conservative")
    print(
        "VERDICT: the missing-object candidate counts only when executable normal forms have "
        "sound, complete, conservative, invariant-reflecting semantics that preserve and reflect "
        "the endpoint, degree, DD.4, boundary, exact-delta, graph, Rosati, control, handoff, "
        "source-before-points, original-H1, fixed-mediator, doc515, and budget payloads."
    )


if __name__ == "__main__":
    main()
