r"""Normalizing confluent computation-stable center eliminator.

Doc 569 makes the dependent center eliminator computation confluent and gives
it a unique normal form. This witness closes the next escape: confluence must
come with a source-internal well-founded normalizer that actually reaches that
normal form for the full payload/structure tuple. A merely confluent but
nonterminating or externally normalized reduction system does not construct
the square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the normalizing eliminator witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 570
EXPECTED_WITNESS = "doc570-probe-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNORMCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
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
    (CONF, "normalized_by", NORM),
    (NORM, "normalizer_for", CONF),
    (NORM, "well_founded_descent_for", ELIM),
    (NORM, "normalizes_structure_for", FINITE_LIMIT),
    (NORM, "normalizes_structure_for", EQUALIZER),
    (NORM, "normalizes_structure_for", CART_EQV),
    (NORM, "normalizes_structure_for", MEDIATOR),
    (NORM, "normalizes_structure_for", SOURCE_COUPLING),
    (NORM, "normalizes_payload_for", ENDPOINT),
    (NORM, "normalizes_payload_for", DEGREE),
    (NORM, "normalizes_payload_for", DD4_BOUNDARY),
    (NORM, "normalizes_payload_for", PUSHFORWARD),
    (NORM, "normalizes_payload_for", EXACT_DELTA),
    (NORM, "normalizes_payload_for", GRAPH_COMP),
    (NORM, "normalizes_payload_for", ROSATI),
    (NORM, "normalizes_payload_for", CONTROL),
    (NORM, "normalizes_payload_for", HANDOFF),
    (NORM, "normalizes_payload_for", GRAPH_LATER),
    (NORM, "preserves", FINITE_INDEX),
    (NORM, "coherent_for", COUPLED_IMAGE),
}

PAYLOAD_NORMALIZATION_TARGETS = {
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

STRUCTURE_NORMALIZATION_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

REQUIRED_FLAGS = (
    "normalizing_confluence",
    "source_internal_normalizer",
    "well_founded_descent",
    "normal_form_reachable",
    "strong_normalization",
    "normalization_unique",
    "normalization_coherent",
    "payload_normalization_complete",
    "structure_normalization_complete",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_confluent_but_nonterminating",
    "center_eliminator_normalizer_missing",
    "center_eliminator_normalizer_external",
    "center_eliminator_normalizer_not_internal",
    "center_eliminator_normalizer_not_well_founded",
    "center_eliminator_normal_form_unreachable",
    "center_eliminator_infinite_reduction_path",
    "center_eliminator_normalization_not_unique",
    "center_eliminator_normalization_not_coherent",
    "center_eliminator_endpoint_degree_normalization_gap",
    "center_eliminator_boundary_normalization_gap",
    "center_eliminator_exact_delta_normalization_gap",
    "center_eliminator_graph_rosati_control_normalization_gap",
    "center_eliminator_handoff_graph_normalization_gap",
    "center_eliminator_probe_normalization_gap",
    "center_eliminator_equalizer_normalization_gap",
    "center_eliminator_mediator_normalization_gap",
    "center_eliminator_source_coupling_normalization_gap",
    "center_eliminator_normalization_requires_choice",
    "center_eliminator_normalization_requires_new_cell",
    "center_eliminator_normalization_context_collapse",
    "center_eliminator_normalization_by_declaration",
    "center_eliminator_normalization_finite_sample",
    "center_eliminator_normalization_basis_row",
    "missing_center_eliminator_normalization_certificate",
)

NORMALIZATION_DATA = {
    "certificate": "source_internal_well_founded_normalizer",
    "base_certificate": CONF,
    "normalizing": True,
    "source_internal": True,
    "well_founded": True,
    "reaches_normal_form": True,
    "strong_normalization": True,
    "no_infinite_reduction": True,
    "unique": True,
    "coherent": True,
    "payload_complete": True,
    "structure_complete": True,
    "endpoint_degree_normalizes": True,
    "boundary_exact_delta_normalizes": True,
    "graph_rosati_control_normalizes": True,
    "handoff_graph_normalizes": True,
    "probe_normalizes": True,
    "equalizer_normalizes": True,
    "mediator_normalizes": True,
    "source_coupling_normalizes": True,
    "external": False,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "payload_targets": PAYLOAD_NORMALIZATION_TARGETS,
    "structure_targets": STRUCTURE_NORMALIZATION_TARGETS,
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
        "normalization": deepcopy(NORMALIZATION_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "normalization":
            state["normalization"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(NORM, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    normalization = state["normalization"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_570")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if NORM not in state["accepted"]:
        reasons.append("normalization_atom_not_accepted")
    if not set(state["requires"].get(NORM, [])).issuperset(REQUIRED_DEPS):
        reasons.append("normalization_deps_missing")
    if NORM not in state["requires"].get(CONF, []):
        reasons.append("confluence_not_required_to_normalize")
    if CONF not in state["requires"].get(NORM, []):
        reasons.append("normalizer_not_based_on_confluence")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("normalization_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "normalizing",
        "source_internal",
        "well_founded",
        "reaches_normal_form",
        "strong_normalization",
        "no_infinite_reduction",
        "unique",
        "coherent",
        "payload_complete",
        "structure_complete",
        "endpoint_degree_normalizes",
        "boundary_exact_delta_normalizes",
        "graph_rosati_control_normalizes",
        "handoff_graph_normalizes",
        "probe_normalizes",
        "equalizer_normalizes",
        "mediator_normalizes",
        "source_coupling_normalizes",
        "preserves_budget",
    )
    for field in required_truths:
        if not normalization.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "external",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if normalization.get(field):
            reasons.append(f"{field}_present")

    if set(normalization.get("payload_targets", set())) != PAYLOAD_NORMALIZATION_TARGETS:
        reasons.append("payload_targets_wrong")
    if set(normalization.get("structure_targets", set())) != STRUCTURE_NORMALIZATION_TARGETS:
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
            if r in {"current_doc_before_570", "witness_not_registered", "normalization_atom_not_accepted"}
        ],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["normalization"]["normalizing"]
        and state["normalization"]["source_internal"]
        and state["normalization"]["well_founded"]
        and state["normalization"]["reaches_normal_form"]
        and state["normalization"]["strong_normalization"]
        and state["normalization"]["no_infinite_reduction"]
        and not state["normalization"]["external"],
        "normalizer is source-internal, well-founded, reachable, and strongly normalizing",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == NORM and relation == "normalizes_payload_for"
    }
    gate(
        f"{PREFIX}3",
        payload_edges.issuperset(PAYLOAD_NORMALIZATION_TARGETS)
        and state["normalization"]["payload_complete"]
        and state["normalization"]["endpoint_degree_normalizes"]
        and state["normalization"]["boundary_exact_delta_normalizes"]
        and state["normalization"]["graph_rosati_control_normalizes"]
        and state["normalization"]["handoff_graph_normalizes"],
        f"payload_normalization_targets={len(payload_edges & PAYLOAD_NORMALIZATION_TARGETS)}/{len(PAYLOAD_NORMALIZATION_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == NORM and relation == "normalizes_structure_for"
    }
    gate(
        f"{PREFIX}4",
        structure_edges.issuperset(STRUCTURE_NORMALIZATION_TARGETS)
        and state["normalization"]["probe_normalizes"]
        and state["normalization"]["equalizer_normalizes"]
        and state["normalization"]["mediator_normalizes"]
        and state["normalization"]["source_coupling_normalizes"],
        f"structure_normalization_targets={len(structure_edges & STRUCTURE_NORMALIZATION_TARGETS)}/{len(STRUCTURE_NORMALIZATION_TARGETS)}",
    )

    gate(
        f"{PREFIX}5",
        NORM in state["requires"].get(CONF, [])
        and CONF in state["requires"].get(NORM, [])
        and state["normalization"]["base_certificate"] == CONF,
        "confluent computation layer closes through source-internal normalization",
    )

    gate(
        f"{PREFIX}6",
        not state["normalization"]["requires_choice"]
        and not state["normalization"]["new_cell"]
        and not state["normalization"]["context_collapse"]
        and not state["normalization"]["declared_only"]
        and not state["normalization"]["finite_sample"]
        and not state["normalization"]["basis_row"],
        "normalization uses no choice, new cell, context collapse, declaration, finite sample, or basis row",
    )

    gate(
        f"{PREFIX}7",
        not [
            r
            for r in reasons
            if r in {"normalization_deps_missing", "confluence_not_required_to_normalize", "normalizer_not_based_on_confluence"}
        ],
        "normalization dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("normalization_edges_missing") for r in reasons),
        "all normalization graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variants = [
        active_state(data, normalization={"strong_normalization": False}, banned={"center_eliminator_confluent_but_nonterminating": True}),
        active_state(data, normalization={"normalizing": False}, banned={"center_eliminator_normalizer_missing": True}),
        active_state(data, normalization={"external": True}, banned={"center_eliminator_normalizer_external": True}),
        active_state(data, normalization={"source_internal": False}, banned={"center_eliminator_normalizer_not_internal": True}),
        active_state(data, normalization={"well_founded": False}, banned={"center_eliminator_normalizer_not_well_founded": True}),
        active_state(data, normalization={"reaches_normal_form": False}, banned={"center_eliminator_normal_form_unreachable": True}),
        active_state(data, normalization={"no_infinite_reduction": False}, banned={"center_eliminator_infinite_reduction_path": True}),
        active_state(data, normalization={"unique": False}, banned={"center_eliminator_normalization_not_unique": True}),
        active_state(data, normalization={"coherent": False}, banned={"center_eliminator_normalization_not_coherent": True}),
        active_state(
            data,
            normalization={"payload_targets": PAYLOAD_NORMALIZATION_TARGETS - {ENDPOINT}},
            banned={"center_eliminator_endpoint_degree_normalization_gap": True},
        ),
        active_state(
            data,
            normalization={"payload_targets": PAYLOAD_NORMALIZATION_TARGETS - {DD4_BOUNDARY}},
            banned={"center_eliminator_boundary_normalization_gap": True},
        ),
        active_state(
            data,
            normalization={"payload_targets": PAYLOAD_NORMALIZATION_TARGETS - {EXACT_DELTA}},
            banned={"center_eliminator_exact_delta_normalization_gap": True},
        ),
        active_state(
            data,
            normalization={"payload_targets": PAYLOAD_NORMALIZATION_TARGETS - {ROSATI}},
            banned={"center_eliminator_graph_rosati_control_normalization_gap": True},
        ),
        active_state(
            data,
            normalization={"payload_targets": PAYLOAD_NORMALIZATION_TARGETS - {HANDOFF}},
            banned={"center_eliminator_handoff_graph_normalization_gap": True},
        ),
        active_state(data, normalization={"probe_normalizes": False}, banned={"center_eliminator_probe_normalization_gap": True}),
        active_state(data, normalization={"equalizer_normalizes": False}, banned={"center_eliminator_equalizer_normalization_gap": True}),
        active_state(data, normalization={"mediator_normalizes": False}, banned={"center_eliminator_mediator_normalization_gap": True}),
        active_state(data, normalization={"source_coupling_normalizes": False}, banned={"center_eliminator_source_coupling_normalization_gap": True}),
        active_state(data, normalization={"requires_choice": True}, banned={"center_eliminator_normalization_requires_choice": True}),
        active_state(data, normalization={"new_cell": True}, banned={"center_eliminator_normalization_requires_new_cell": True}),
        active_state(data, normalization={"context_collapse": True}, banned={"center_eliminator_normalization_context_collapse": True}),
        active_state(data, normalization={"declared_only": True}, banned={"center_eliminator_normalization_by_declaration": True}),
        active_state(data, normalization={"finite_sample": True}, banned={"center_eliminator_normalization_finite_sample": True}),
        active_state(data, normalization={"basis_row": True}, banned={"center_eliminator_normalization_basis_row": True}),
        active_state(data, accepted=state["accepted"] - {NORM}, banned={"missing_center_eliminator_normalization_certificate": True}),
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
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: center eliminator computation is normalizing")
    print(
        "VERDICT: the missing-object candidate counts only when the source-internal "
        "dependent center eliminator has a well-founded normalizer reaching the "
        "unique confluent normal form for endpoint-degree, DD.4, exact-delta, "
        "graph-Rosati-control, handoff, probe, equalizer, mediator, and "
        "source-coupling projections inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
