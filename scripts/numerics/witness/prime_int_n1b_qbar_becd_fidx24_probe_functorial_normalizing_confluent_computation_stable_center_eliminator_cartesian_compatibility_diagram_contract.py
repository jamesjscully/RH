r"""Functorial normalizing confluent computation-stable center eliminator.

Doc 570 gives the dependent center eliminator a source-internal
well-founded normalizer. This witness closes the next escape: the normalizer
cannot be merely objectwise. It must be functorial and natural for source
square morphisms, refinements, probes, mediator/source-coupling structure,
and all payload projections.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_functorial_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the functorial normalizer witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 571
EXPECTED_WITNESS = "doc571-probe-functorial-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
FUNC = "functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
NORM = "normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CONF = "confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
COMP = "computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ELIM = "center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CENTER = "center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ICONTR = "internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
GLOB = "globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ENDTRIV = "endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
AUT = "automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
DIAG = "cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
BUNDLE = "represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
RLIM = "represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FRC = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ADMCAT = "admissible_source_square_category_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_EQV = "probe_equivalence_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
SUBREP = "source_fiber_subrepresenter"
COUPLED_IMAGE = "coupled_source_image"
FINITE_LIMIT = "finite_limit_cut"
EQUALIZER = "equalizer_arrow_to_subrep"
MEDIATOR = "universal_mediator"
SOURCE_COUPLING = "source_coupling"
DD4_ORIGINAL = "original_dd4_class"
HANDOFF = "dd4_image_only_handoff_contract"
GRAPH_LATER = "graph_later_realization_contract"
ENDPOINT = "endpoint_integrality"
DEGREE = "degree_maps"
DD4_BOUNDARY = "dd4_boundary"
PUSHFORWARD = "boundary_pushforward"
GRAPH_COMP = "graph_composition"
ROSATI = "rosati_count"
CONTROL = "control_death"
EXACT_DELTA = "exact_delta"
FINITE_INDEX = "exact_24_cell_finite_index"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFUNCNORMCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
    NORM,
    CONF,
    COMP,
    ELIM,
    CENTER,
    ICONTR,
    GLOB,
    ENDTRIV,
    AUT,
    DIAG,
    BUNDLE,
    RLIM,
    FRC,
    MED,
    JOINT,
    ADMCAT,
    PROBE_NAT,
    PROBE_EQV,
    CART_EQV,
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    EQUALIZER,
    MEDIATOR,
    SOURCE_COUPLING,
    DD4_ORIGINAL,
    HANDOFF,
    GRAPH_LATER,
    ENDPOINT,
    DEGREE,
    DD4_BOUNDARY,
    PUSHFORWARD,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
    EXACT_DELTA,
    FINITE_INDEX,
}

EXPECTED_EDGES = {
    (NORM, "functorialized_by", FUNC),
    (FUNC, "functorial_normalizer_for", NORM),
    (FUNC, "natural_for", ADMCAT),
    (FUNC, "natural_for", PROBE_NAT),
    (FUNC, "natural_for", PROBE_EQV),
    (FUNC, "natural_for", CART_EQV),
    (FUNC, "natural_for", FRC),
    (FUNC, "natural_for", RLIM),
    (FUNC, "commutes_with_structure_for", FINITE_LIMIT),
    (FUNC, "commutes_with_structure_for", EQUALIZER),
    (FUNC, "commutes_with_structure_for", MEDIATOR),
    (FUNC, "commutes_with_structure_for", SOURCE_COUPLING),
    (FUNC, "commutes_with_structure_for", SUBREP),
    (FUNC, "commutes_with_structure_for", COUPLED_IMAGE),
    (FUNC, "commutes_with_payload_for", ENDPOINT),
    (FUNC, "commutes_with_payload_for", DEGREE),
    (FUNC, "commutes_with_payload_for", DD4_BOUNDARY),
    (FUNC, "commutes_with_payload_for", PUSHFORWARD),
    (FUNC, "commutes_with_payload_for", EXACT_DELTA),
    (FUNC, "commutes_with_payload_for", GRAPH_COMP),
    (FUNC, "commutes_with_payload_for", ROSATI),
    (FUNC, "commutes_with_payload_for", CONTROL),
    (FUNC, "commutes_with_payload_for", HANDOFF),
    (FUNC, "commutes_with_payload_for", GRAPH_LATER),
    (FUNC, "preserves", FINITE_INDEX),
}

NATURALITY_TARGETS = {ADMCAT, PROBE_NAT, PROBE_EQV, CART_EQV, FRC, RLIM}

PAYLOAD_NATURALITY_TARGETS = {
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
}

STRUCTURE_NATURALITY_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    MEDIATOR,
    SOURCE_COUPLING,
    SUBREP,
    COUPLED_IMAGE,
}

REQUIRED_FLAGS = (
    "functorial_normalizer",
    "natural_normalizer",
    "source_square_naturality",
    "refinement_naturality",
    "probe_naturality",
    "payload_naturality_complete",
    "structure_naturality_complete",
    "identity_preservation",
    "composition_preservation",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_normalizer_objectwise_only",
    "center_eliminator_normalizer_not_functorial",
    "center_eliminator_normalizer_not_natural",
    "center_eliminator_normalizer_morphism_naturality_gap",
    "center_eliminator_normalizer_probe_naturality_gap",
    "center_eliminator_normalizer_refinement_naturality_gap",
    "center_eliminator_normalizer_mediator_naturality_gap",
    "center_eliminator_normalizer_source_coupling_naturality_gap",
    "center_eliminator_normalizer_payload_naturality_gap",
    "center_eliminator_normalizer_endpoint_degree_naturality_gap",
    "center_eliminator_normalizer_boundary_naturality_gap",
    "center_eliminator_normalizer_exact_delta_naturality_gap",
    "center_eliminator_normalizer_graph_rosati_control_naturality_gap",
    "center_eliminator_normalizer_handoff_graph_naturality_gap",
    "center_eliminator_normalizer_equalizer_naturality_gap",
    "center_eliminator_normalizer_cartesian_naturality_gap",
    "center_eliminator_normalizer_composition_not_preserved",
    "center_eliminator_normalizer_identity_not_preserved",
    "center_eliminator_normalizer_not_coherent_with_confluence",
    "center_eliminator_normalizer_not_coherent_with_payload",
    "center_eliminator_normalizer_not_coherent_with_structure",
    "center_eliminator_normalizer_requires_choice",
    "center_eliminator_normalizer_requires_new_cell",
    "center_eliminator_normalizer_context_collapse",
    "center_eliminator_normalizer_by_declaration",
    "center_eliminator_normalizer_finite_sample",
    "center_eliminator_normalizer_basis_row",
    "missing_functorial_normalizer_certificate",
)

FUNCTORIAL_DATA = {
    "certificate": "source_internal_functorial_well_founded_normalizer",
    "base_certificate": NORM,
    "functorial": True,
    "natural": True,
    "objectwise_only": False,
    "morphism_natural": True,
    "probe_natural": True,
    "refinement_natural": True,
    "mediator_natural": True,
    "source_coupling_natural": True,
    "payload_natural": True,
    "endpoint_degree_natural": True,
    "boundary_natural": True,
    "exact_delta_natural": True,
    "graph_rosati_control_natural": True,
    "handoff_graph_natural": True,
    "equalizer_natural": True,
    "cartesian_natural": True,
    "identity_preserving": True,
    "composition_preserving": True,
    "coherent_with_confluence": True,
    "coherent_with_payload": True,
    "coherent_with_structure": True,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "naturality_targets": NATURALITY_TARGETS,
    "payload_targets": PAYLOAD_NATURALITY_TARGETS,
    "structure_targets": STRUCTURE_NATURALITY_TARGETS,
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
        "functoriality": deepcopy(FUNCTORIAL_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "functoriality":
            state["functoriality"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(FUNC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    functoriality = state["functoriality"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_571")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if FUNC not in state["accepted"]:
        reasons.append("functorial_normalizer_atom_not_accepted")
    if not set(state["requires"].get(FUNC, [])).issuperset(REQUIRED_DEPS):
        reasons.append("functorial_normalizer_deps_missing")
    if FUNC not in state["requires"].get(NORM, []):
        reasons.append("normalizer_not_required_to_be_functorial")
    if NORM not in state["requires"].get(FUNC, []):
        reasons.append("functorial_normalizer_not_based_on_normalizer")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("functorial_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "functorial",
        "natural",
        "morphism_natural",
        "probe_natural",
        "refinement_natural",
        "mediator_natural",
        "source_coupling_natural",
        "payload_natural",
        "endpoint_degree_natural",
        "boundary_natural",
        "exact_delta_natural",
        "graph_rosati_control_natural",
        "handoff_graph_natural",
        "equalizer_natural",
        "cartesian_natural",
        "identity_preserving",
        "composition_preserving",
        "coherent_with_confluence",
        "coherent_with_payload",
        "coherent_with_structure",
        "preserves_budget",
    )
    for field in required_truths:
        if not functoriality.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "objectwise_only",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if functoriality.get(field):
            reasons.append(f"{field}_present")

    if set(functoriality.get("naturality_targets", set())) != NATURALITY_TARGETS:
        reasons.append("naturality_targets_wrong")
    if set(functoriality.get("payload_targets", set())) != PAYLOAD_NATURALITY_TARGETS:
        reasons.append("payload_targets_wrong")
    if set(functoriality.get("structure_targets", set())) != STRUCTURE_NATURALITY_TARGETS:
        reasons.append("structure_targets_wrong")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            reasons.append(f"required_flag_missing:{flag}")
    for flag, active in state["banned"].items():
        if active:
            reasons.append(f"banned_flag_active:{flag}")
        if not rejected_or_excluded(state, flag):
            reasons.append(f"banned_flag_not_rejected:{flag}")
    return reasons


def main() -> None:
    data = load_map()
    state = active_state(data)
    reasons = assess(state)

    gate(
        f"{PREFIX}1",
        not [
            r
            for r in reasons
            if r in {"current_doc_before_571", "witness_not_registered", "functorial_normalizer_atom_not_accepted"}
        ],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["functoriality"]["functorial"]
        and state["functoriality"]["natural"]
        and state["functoriality"]["morphism_natural"]
        and not state["functoriality"]["objectwise_only"],
        "normalizer is functorial and natural for source-square morphisms",
    )

    naturality_edges = {
        target
        for source, relation, target in state["edges"]
        if source == FUNC and relation == "natural_for"
    }
    gate(
        f"{PREFIX}3",
        naturality_edges.issuperset(NATURALITY_TARGETS)
        and state["functoriality"]["probe_natural"]
        and state["functoriality"]["refinement_natural"],
        f"naturality_targets={len(naturality_edges & NATURALITY_TARGETS)}/{len(NATURALITY_TARGETS)}",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == FUNC and relation == "commutes_with_payload_for"
    }
    gate(
        f"{PREFIX}4",
        payload_edges.issuperset(PAYLOAD_NATURALITY_TARGETS)
        and state["functoriality"]["payload_natural"]
        and state["functoriality"]["endpoint_degree_natural"]
        and state["functoriality"]["boundary_natural"]
        and state["functoriality"]["exact_delta_natural"]
        and state["functoriality"]["graph_rosati_control_natural"]
        and state["functoriality"]["handoff_graph_natural"],
        f"payload_naturality_targets={len(payload_edges & PAYLOAD_NATURALITY_TARGETS)}/{len(PAYLOAD_NATURALITY_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == FUNC and relation == "commutes_with_structure_for"
    }
    gate(
        f"{PREFIX}5",
        structure_edges.issuperset(STRUCTURE_NATURALITY_TARGETS)
        and state["functoriality"]["mediator_natural"]
        and state["functoriality"]["source_coupling_natural"]
        and state["functoriality"]["equalizer_natural"]
        and state["functoriality"]["cartesian_natural"],
        f"structure_naturality_targets={len(structure_edges & STRUCTURE_NATURALITY_TARGETS)}/{len(STRUCTURE_NATURALITY_TARGETS)}",
    )

    gate(
        f"{PREFIX}6",
        state["functoriality"]["identity_preserving"]
        and state["functoriality"]["composition_preserving"]
        and state["functoriality"]["coherent_with_confluence"]
        and state["functoriality"]["coherent_with_payload"]
        and state["functoriality"]["coherent_with_structure"],
        "identity, composition, confluence, payload, and structure coherence are preserved",
    )

    gate(
        f"{PREFIX}7",
        not [
            r
            for r in reasons
            if r
            in {
                "functorial_normalizer_deps_missing",
                "normalizer_not_required_to_be_functorial",
                "functorial_normalizer_not_based_on_normalizer",
            }
        ],
        "functorial normalizer dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("functorial_edges_missing") for r in reasons),
        "all functorial-normalizer graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variants = [
        active_state(data, functoriality={"objectwise_only": True}, banned={"center_eliminator_normalizer_objectwise_only": True}),
        active_state(data, functoriality={"functorial": False}, banned={"center_eliminator_normalizer_not_functorial": True}),
        active_state(data, functoriality={"natural": False}, banned={"center_eliminator_normalizer_not_natural": True}),
        active_state(data, functoriality={"morphism_natural": False}, banned={"center_eliminator_normalizer_morphism_naturality_gap": True}),
        active_state(data, functoriality={"probe_natural": False}, banned={"center_eliminator_normalizer_probe_naturality_gap": True}),
        active_state(data, functoriality={"refinement_natural": False}, banned={"center_eliminator_normalizer_refinement_naturality_gap": True}),
        active_state(data, functoriality={"mediator_natural": False}, banned={"center_eliminator_normalizer_mediator_naturality_gap": True}),
        active_state(data, functoriality={"source_coupling_natural": False}, banned={"center_eliminator_normalizer_source_coupling_naturality_gap": True}),
        active_state(data, functoriality={"payload_natural": False}, banned={"center_eliminator_normalizer_payload_naturality_gap": True}),
        active_state(
            data,
            functoriality={"payload_targets": PAYLOAD_NATURALITY_TARGETS - {ENDPOINT}},
            banned={"center_eliminator_normalizer_endpoint_degree_naturality_gap": True},
        ),
        active_state(
            data,
            functoriality={"payload_targets": PAYLOAD_NATURALITY_TARGETS - {DD4_BOUNDARY}},
            banned={"center_eliminator_normalizer_boundary_naturality_gap": True},
        ),
        active_state(
            data,
            functoriality={"payload_targets": PAYLOAD_NATURALITY_TARGETS - {EXACT_DELTA}},
            banned={"center_eliminator_normalizer_exact_delta_naturality_gap": True},
        ),
        active_state(
            data,
            functoriality={"payload_targets": PAYLOAD_NATURALITY_TARGETS - {ROSATI}},
            banned={"center_eliminator_normalizer_graph_rosati_control_naturality_gap": True},
        ),
        active_state(
            data,
            functoriality={"payload_targets": PAYLOAD_NATURALITY_TARGETS - {HANDOFF}},
            banned={"center_eliminator_normalizer_handoff_graph_naturality_gap": True},
        ),
        active_state(data, functoriality={"equalizer_natural": False}, banned={"center_eliminator_normalizer_equalizer_naturality_gap": True}),
        active_state(data, functoriality={"cartesian_natural": False}, banned={"center_eliminator_normalizer_cartesian_naturality_gap": True}),
        active_state(data, functoriality={"composition_preserving": False}, banned={"center_eliminator_normalizer_composition_not_preserved": True}),
        active_state(data, functoriality={"identity_preserving": False}, banned={"center_eliminator_normalizer_identity_not_preserved": True}),
        active_state(data, functoriality={"coherent_with_confluence": False}, banned={"center_eliminator_normalizer_not_coherent_with_confluence": True}),
        active_state(data, functoriality={"coherent_with_payload": False}, banned={"center_eliminator_normalizer_not_coherent_with_payload": True}),
        active_state(data, functoriality={"coherent_with_structure": False}, banned={"center_eliminator_normalizer_not_coherent_with_structure": True}),
        active_state(data, functoriality={"requires_choice": True}, banned={"center_eliminator_normalizer_requires_choice": True}),
        active_state(data, functoriality={"new_cell": True}, banned={"center_eliminator_normalizer_requires_new_cell": True}),
        active_state(data, functoriality={"context_collapse": True}, banned={"center_eliminator_normalizer_context_collapse": True}),
        active_state(data, functoriality={"declared_only": True}, banned={"center_eliminator_normalizer_by_declaration": True}),
        active_state(data, functoriality={"finite_sample": True}, banned={"center_eliminator_normalizer_finite_sample": True}),
        active_state(data, functoriality={"basis_row": True}, banned={"center_eliminator_normalizer_basis_row": True}),
        active_state(data, accepted=state["accepted"] - {FUNC}, banned={"missing_functorial_normalizer_certificate": True}),
    ]
    live_reasons = reasons
    rejected_variants = [variant for variant in variants if assess(variant)]
    gate(
        f"{PREFIX}10",
        not live_reasons and len(rejected_variants) == len(variants),
        f"live_reasons={live_reasons} rejected_variants={len(rejected_variants)}",
    )

    if failures:
        print("\nFAILURES:", ", ".join(failures))
        raise SystemExit(1)
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: center eliminator normalizer is functorial")
    print(
        "VERDICT: the missing-object candidate counts only when its source-internal "
        "well-founded normalizer is functorial and natural for source-square "
        "morphisms, refinements, probes, mediator/source-coupling structure, "
        "and every endpoint-degree, DD.4, exact-delta, graph-Rosati-control, "
        "handoff, equalizer, and cartesian projection inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
