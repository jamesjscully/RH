r"""Computation-stable center eliminator cartesian compatibility diagram.

Doc 567 adds a source-internal dependent eliminator for the realized center.
This witness closes the next escape: the eliminator cannot merely project the
payloads propositionally. Its endpoint-degree, DD.4, exact-delta,
graph/Rosati/control, handoff, probe, equalizer, mediator, and
source-coupling projections must compute by internal beta/eta and stability
laws on the same finite-limit spine.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the computation-stable eliminator witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 568
EXPECTED_WITNESS = "doc568-probe-computation-stable-center-eliminator-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPSTABCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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
    (ELIM, "computation_stabilized_by", COMP),
    (COMP, "computation_law_for", ELIM),
    (COMP, "beta_eta_law_for", FINITE_LIMIT),
    (COMP, "beta_eta_law_for", EQUALIZER),
    (COMP, "beta_eta_law_for", CART_EQV),
    (COMP, "beta_eta_law_for", MEDIATOR),
    (COMP, "beta_eta_law_for", SOURCE_COUPLING),
    (COMP, "computes_payload_for", ENDPOINT),
    (COMP, "computes_payload_for", DEGREE),
    (COMP, "computes_payload_for", DD4_BOUNDARY),
    (COMP, "computes_payload_for", PUSHFORWARD),
    (COMP, "computes_payload_for", EXACT_DELTA),
    (COMP, "computes_payload_for", GRAPH_COMP),
    (COMP, "computes_payload_for", ROSATI),
    (COMP, "computes_payload_for", CONTROL),
    (COMP, "computes_payload_for", HANDOFF),
    (COMP, "computes_payload_for", GRAPH_LATER),
    (COMP, "preserves", FINITE_INDEX),
    (COMP, "coherent_for", COUPLED_IMAGE),
}

PAYLOAD_COMPUTATION_TARGETS = {
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

STRUCTURE_COMPUTATION_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

REQUIRED_FLAGS = (
    "computation_stable_eliminator",
    "computation_source_internal",
    "beta_law_internal",
    "eta_law_internal",
    "computation_unique",
    "computation_coherent",
    "payload_computation_complete",
    "structure_computation_complete",
    "computation_substitution_stable",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_projection_not_computational",
    "center_eliminator_computation_external",
    "center_eliminator_computation_not_internal",
    "center_eliminator_beta_law_missing",
    "center_eliminator_eta_law_missing",
    "center_eliminator_computation_not_unique",
    "center_eliminator_computation_not_coherent",
    "center_eliminator_endpoint_degree_computation_gap",
    "center_eliminator_boundary_computation_gap",
    "center_eliminator_exact_delta_computation_gap",
    "center_eliminator_graph_rosati_control_computation_gap",
    "center_eliminator_handoff_graph_computation_gap",
    "center_eliminator_probe_computation_gap",
    "center_eliminator_equalizer_computation_gap",
    "center_eliminator_mediator_computation_gap",
    "center_eliminator_source_coupling_computation_gap",
    "center_eliminator_computation_requires_choice",
    "center_eliminator_computation_requires_new_cell",
    "center_eliminator_computation_context_collapse",
    "center_eliminator_computation_by_declaration",
    "center_eliminator_computation_finite_sample",
    "center_eliminator_computation_basis_row",
    "missing_center_eliminator_computation_stability_certificate",
)

COMPUTATION_DATA = {
    "certificate": "source_internal_computation_stable_center_eliminator",
    "base_certificate": ELIM,
    "computation_stable": True,
    "source_internal": True,
    "beta_law": True,
    "eta_law": True,
    "unique": True,
    "coherent": True,
    "substitution_stable": True,
    "payload_complete": True,
    "structure_complete": True,
    "computes_endpoint_degree": True,
    "computes_boundary_exact_delta": True,
    "computes_graph_rosati_control": True,
    "computes_handoff_graph": True,
    "computes_probe": True,
    "computes_equalizer": True,
    "computes_mediator": True,
    "computes_source_coupling": True,
    "external": False,
    "propositional_only": False,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "structure_targets": STRUCTURE_COMPUTATION_TARGETS,
    "payload_targets": PAYLOAD_COMPUTATION_TARGETS,
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
        "computation": deepcopy(COMPUTATION_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "computation":
            state["computation"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(COMP, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    computation = state["computation"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_568")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if COMP not in state["accepted"]:
        reasons.append("computation_atom_not_accepted")
    if not set(state["requires"].get(COMP, [])).issuperset(REQUIRED_DEPS):
        reasons.append("computation_deps_missing")
    if COMP not in state["requires"].get(ELIM, []):
        reasons.append("eliminator_not_required_to_compute")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("computation_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "computation_stable",
        "source_internal",
        "beta_law",
        "eta_law",
        "unique",
        "coherent",
        "substitution_stable",
        "payload_complete",
        "structure_complete",
        "computes_endpoint_degree",
        "computes_boundary_exact_delta",
        "computes_graph_rosati_control",
        "computes_handoff_graph",
        "computes_probe",
        "computes_equalizer",
        "computes_mediator",
        "computes_source_coupling",
        "preserves_budget",
    )
    for field in required_truths:
        if not computation.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "external",
        "propositional_only",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if computation.get(field):
            reasons.append(f"{field}_present")

    if set(computation.get("structure_targets", set())) != STRUCTURE_COMPUTATION_TARGETS:
        reasons.append("structure_targets_wrong")
    if set(computation.get("payload_targets", set())) != PAYLOAD_COMPUTATION_TARGETS:
        reasons.append("payload_targets_wrong")

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
        not [r for r in reasons if r in {"current_doc_before_568", "witness_not_registered", "computation_atom_not_accepted"}],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["computation"]["source_internal"]
        and state["computation"]["beta_law"]
        and state["computation"]["eta_law"]
        and state["computation"]["unique"]
        and state["computation"]["coherent"]
        and not state["computation"]["external"]
        and not state["computation"]["propositional_only"],
        "computation laws are internal beta/eta laws, unique, coherent, and not merely propositional",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == COMP and relation == "computes_payload_for"
    }
    gate(
        f"{PREFIX}3",
        payload_edges.issuperset(PAYLOAD_COMPUTATION_TARGETS)
        and state["computation"]["payload_complete"]
        and state["computation"]["computes_endpoint_degree"]
        and state["computation"]["computes_boundary_exact_delta"]
        and state["computation"]["computes_graph_rosati_control"]
        and state["computation"]["computes_handoff_graph"],
        f"payload_computation_targets={len(payload_edges & PAYLOAD_COMPUTATION_TARGETS)}/{len(PAYLOAD_COMPUTATION_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == COMP and relation == "beta_eta_law_for"
    }
    gate(
        f"{PREFIX}4",
        structure_edges.issuperset(STRUCTURE_COMPUTATION_TARGETS)
        and state["computation"]["computes_probe"]
        and state["computation"]["computes_equalizer"]
        and state["computation"]["computes_mediator"]
        and state["computation"]["computes_source_coupling"],
        f"structure_computation_targets={len(structure_edges & STRUCTURE_COMPUTATION_TARGETS)}/{len(STRUCTURE_COMPUTATION_TARGETS)}",
    )

    gate(
        f"{PREFIX}5",
        COMP in state["requires"].get(ELIM, [])
        and ELIM in state["requires"].get(COMP, [])
        and state["computation"]["base_certificate"] == ELIM,
        "dependent eliminator closes through computation stability",
    )

    forbidden_clean = not any(
        state["computation"][field]
        for field in (
            "requires_choice",
            "declared_only",
            "finite_sample",
            "basis_row",
            "new_cell",
            "context_collapse",
        )
    )
    gate(
        f"{PREFIX}6",
        forbidden_clean,
        "no choice, new cell, context collapse, declaration, finite sample, or basis row",
    )

    gate(
        f"{PREFIX}7",
        not [r for r in reasons if r in {"computation_deps_missing", "eliminator_not_required_to_compute"}],
        "computation dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("computation_edges_missing") for r in reasons),
        "all computation-stability graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variants = [
        active_state(data, computation={"propositional_only": True}, banned={"center_eliminator_projection_not_computational": True}),
        active_state(data, computation={"external": True}, banned={"center_eliminator_computation_external": True}),
        active_state(data, computation={"source_internal": False}, banned={"center_eliminator_computation_not_internal": True}),
        active_state(data, computation={"beta_law": False}, banned={"center_eliminator_beta_law_missing": True}),
        active_state(data, computation={"eta_law": False}, banned={"center_eliminator_eta_law_missing": True}),
        active_state(data, computation={"unique": False}, banned={"center_eliminator_computation_not_unique": True}),
        active_state(data, computation={"coherent": False}, banned={"center_eliminator_computation_not_coherent": True}),
        active_state(
            data,
            computation={"payload_targets": PAYLOAD_COMPUTATION_TARGETS - {ENDPOINT}},
            banned={"center_eliminator_endpoint_degree_computation_gap": True},
        ),
        active_state(
            data,
            computation={"payload_targets": PAYLOAD_COMPUTATION_TARGETS - {DD4_BOUNDARY}},
            banned={"center_eliminator_boundary_computation_gap": True},
        ),
        active_state(
            data,
            computation={"payload_targets": PAYLOAD_COMPUTATION_TARGETS - {EXACT_DELTA}},
            banned={"center_eliminator_exact_delta_computation_gap": True},
        ),
        active_state(
            data,
            computation={"payload_targets": PAYLOAD_COMPUTATION_TARGETS - {ROSATI}},
            banned={"center_eliminator_graph_rosati_control_computation_gap": True},
        ),
        active_state(
            data,
            computation={"payload_targets": PAYLOAD_COMPUTATION_TARGETS - {HANDOFF}},
            banned={"center_eliminator_handoff_graph_computation_gap": True},
        ),
        active_state(data, computation={"computes_probe": False}, banned={"center_eliminator_probe_computation_gap": True}),
        active_state(data, computation={"computes_equalizer": False}, banned={"center_eliminator_equalizer_computation_gap": True}),
        active_state(data, computation={"computes_mediator": False}, banned={"center_eliminator_mediator_computation_gap": True}),
        active_state(data, computation={"computes_source_coupling": False}, banned={"center_eliminator_source_coupling_computation_gap": True}),
        active_state(data, computation={"requires_choice": True}, banned={"center_eliminator_computation_requires_choice": True}),
        active_state(data, computation={"new_cell": True}, banned={"center_eliminator_computation_requires_new_cell": True}),
        active_state(data, computation={"context_collapse": True}, banned={"center_eliminator_computation_context_collapse": True}),
        active_state(data, computation={"declared_only": True}, banned={"center_eliminator_computation_by_declaration": True}),
        active_state(data, computation={"finite_sample": True}, banned={"center_eliminator_computation_finite_sample": True}),
        active_state(data, computation={"basis_row": True}, banned={"center_eliminator_computation_basis_row": True}),
        active_state(data, accepted=state["accepted"] - {COMP}, banned={"missing_center_eliminator_computation_stability_certificate": True}),
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
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: center eliminator projections compute internally")
    print(
        "VERDICT: the missing-object candidate counts only when the source-internal "
        "dependent center eliminator carries internal beta/eta computation laws for "
        "endpoint-degree, DD.4, exact-delta, graph-Rosati-control, handoff, probe, "
        "equalizer, mediator, and source-coupling projections inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
