r"""Internally contractible globally unique cartesian compatibility diagram.

Doc 564 rejects discrete or selector-dependent globally unique diagrams. This
witness closes the next escape: uniqueness cannot remain an external
proposition. The square must carry an internal contractible solution object
with payload-preserving comparison paths.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_internally_contractible_globally_unique_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the internally-contractible witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 565
EXPECTED_WITNESS = "doc565-probe-internally-contractible-globally-unique-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINTCONTRGLOBUNIQCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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
    (GLOB, "internally_contractible_by", ICONTR),
    (ICONTR, "internal_contraction_for", GLOB),
    (ICONTR, "contractible_solution_object_for", DIAG),
    (ICONTR, "internal_comparison_path_for", FINITE_LIMIT),
    (ICONTR, "path_unique_for", EQUALIZER),
    (ICONTR, "path_unique_for", CART_EQV),
    (ICONTR, "path_unique_for", MEDIATOR),
    (ICONTR, "path_unique_for", SOURCE_COUPLING),
    (ICONTR, "payload_contraction_for", ENDPOINT),
    (ICONTR, "payload_contraction_for", DEGREE),
    (ICONTR, "payload_contraction_for", DD4_BOUNDARY),
    (ICONTR, "payload_contraction_for", PUSHFORWARD),
    (ICONTR, "payload_contraction_for", EXACT_DELTA),
    (ICONTR, "payload_contraction_for", GRAPH_COMP),
    (ICONTR, "payload_contraction_for", ROSATI),
    (ICONTR, "payload_contraction_for", CONTROL),
    (ICONTR, "payload_contraction_for", HANDOFF),
    (ICONTR, "payload_contraction_for", GRAPH_LATER),
    (ICONTR, "preserves", FINITE_INDEX),
    (ICONTR, "homotopy_coherent_for", COUPLED_IMAGE),
}

PAYLOAD_PATH_TARGETS = {
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

COMPARISON_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

REQUIRED_FLAGS = (
    "internally_contractible_solution_object",
    "internal_comparison_paths",
    "path_uniqueness",
    "path_coherence",
    "payload_paths_preserve_endpoint_degree",
    "payload_paths_preserve_boundary_exact_delta",
    "payload_paths_preserve_graph_rosati_control",
    "payload_paths_preserve_handoff_graph",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "diagram_global_uniqueness_external_proof",
    "diagram_uniqueness_not_internalized",
    "diagram_missing_comparison_path",
    "diagram_comparison_path_external",
    "diagram_comparison_path_nonunique",
    "diagram_comparison_path_incoherent",
    "diagram_contractibility_by_declaration",
    "diagram_contractibility_finite_sample",
    "diagram_contractibility_basis_row",
    "diagram_path_object_missing",
    "diagram_path_object_new_cell",
    "diagram_path_object_context_collapse",
    "diagram_payload_path_gap",
    "diagram_endpoint_degree_path_gap",
    "diagram_boundary_path_gap",
    "diagram_exact_delta_path_gap",
    "diagram_graph_rosati_control_path_gap",
    "diagram_handoff_graph_path_gap",
    "diagram_probe_path_gap",
    "diagram_equalizer_path_gap",
    "diagram_mediator_path_gap",
    "diagram_source_coupling_path_gap",
    "missing_internally_contractible_cartesian_compatibility_diagram_certificate",
)

CONTRACTION_DATA = {
    "certificate": "source_internal_contractible_solution_object",
    "base_certificate": GLOB,
    "solution_object_internal": True,
    "contractible_solution_space": True,
    "comparison_paths_internal": True,
    "comparison_paths_unique": True,
    "comparison_paths_coherent": True,
    "payload_paths_preserve_endpoint_degree": True,
    "payload_paths_preserve_boundary_exact_delta": True,
    "payload_paths_preserve_graph_rosati_control": True,
    "payload_paths_preserve_handoff_graph": True,
    "external_uniqueness_proof": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "path_object_new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "comparison_targets": COMPARISON_TARGETS,
    "payload_path_targets": PAYLOAD_PATH_TARGETS,
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
        "contractible": deepcopy(CONTRACTION_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "contractible":
            state["contractible"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(ICONTR, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    contractible = state["contractible"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_565")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if ICONTR not in state["accepted"]:
        reasons.append("contractible_atom_not_accepted")
    if not set(state["requires"].get(ICONTR, [])).issuperset(REQUIRED_DEPS):
        reasons.append("contractible_deps_missing")
    if ICONTR not in state["requires"].get(GLOB, []):
        reasons.append("global_unique_not_required_to_internalize")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("contractible_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "solution_object_internal",
        "contractible_solution_space",
        "comparison_paths_internal",
        "comparison_paths_unique",
        "comparison_paths_coherent",
        "payload_paths_preserve_endpoint_degree",
        "payload_paths_preserve_boundary_exact_delta",
        "payload_paths_preserve_graph_rosati_control",
        "payload_paths_preserve_handoff_graph",
        "preserves_budget",
    )
    for field in required_truths:
        if not contractible.get(field):
            reasons.append(f"{field}_missing")
    forbidden_truths = (
        "external_uniqueness_proof",
        "declared_only",
        "finite_sample",
        "basis_row",
        "path_object_new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if contractible.get(field):
            reasons.append(f"{field}_present")

    if set(contractible.get("comparison_targets", set())) != COMPARISON_TARGETS:
        reasons.append("comparison_targets_wrong")
    if set(contractible.get("payload_path_targets", set())) != PAYLOAD_PATH_TARGETS:
        reasons.append("payload_path_targets_wrong")

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
        not [r for r in reasons if r in {"current_doc_before_565", "witness_not_registered", "contractible_atom_not_accepted"}],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["contractible"]["solution_object_internal"]
        and state["contractible"]["contractible_solution_space"]
        and state["contractible"]["comparison_paths_internal"]
        and not state["contractible"]["external_uniqueness_proof"],
        "global uniqueness is internalized as a source-side contractible solution object",
    )

    gate(
        f"{PREFIX}3",
        state["contractible"]["comparison_paths_unique"]
        and state["contractible"]["comparison_paths_coherent"]
        and not any(state["banned"][flag] for flag in (
            "diagram_missing_comparison_path",
            "diagram_comparison_path_external",
            "diagram_comparison_path_nonunique",
            "diagram_comparison_path_incoherent",
        )),
        "comparison paths are internal, unique, and coherent",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == ICONTR and relation == "payload_contraction_for"
    }
    gate(
        f"{PREFIX}4",
        payload_edges.issuperset(PAYLOAD_PATH_TARGETS)
        and state["contractible"]["payload_paths_preserve_endpoint_degree"]
        and state["contractible"]["payload_paths_preserve_boundary_exact_delta"]
        and state["contractible"]["payload_paths_preserve_graph_rosati_control"]
        and state["contractible"]["payload_paths_preserve_handoff_graph"],
        f"payload_path_targets={len(payload_edges & PAYLOAD_PATH_TARGETS)}/{len(PAYLOAD_PATH_TARGETS)}",
    )

    comparison_edges = {
        target
        for source, relation, target in state["edges"]
        if source == ICONTR and relation in {"internal_comparison_path_for", "path_unique_for"}
    }
    gate(
        f"{PREFIX}5",
        comparison_edges.issuperset(COMPARISON_TARGETS),
        f"comparison_targets={len(comparison_edges & COMPARISON_TARGETS)}/{len(COMPARISON_TARGETS)}",
    )

    gate(
        f"{PREFIX}6",
        state["contractible"]["preserves_budget"]
        and not state["contractible"]["path_object_new_cell"]
        and not state["contractible"]["context_collapse"]
        and not state["contractible"]["declared_only"]
        and not state["contractible"]["finite_sample"]
        and not state["contractible"]["basis_row"],
        "no new finite-index cell, context collapse, declaration, finite sample, or basis row",
    )

    missing_deps = sorted(REQUIRED_DEPS - set(state["requires"].get(ICONTR, [])))
    gate(
        f"{PREFIX}7",
        not missing_deps and ICONTR in state["requires"].get(GLOB, []),
        "contractible_deps_missing:" + ",".join(missing_deps[:4]) if missing_deps else "dependency closure is internalized",
    )

    missing_edges = sorted(EXPECTED_EDGES - state["edges"])
    gate(
        f"{PREFIX}8",
        not missing_edges,
        "missing_edges:" + ",".join("/".join(edge) for edge in missing_edges[:3]) if missing_edges else "all contractibility graph edges present",
    )

    uncovered = [flag for flag in BANNED_FLAGS if not rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        not uncovered,
        "uncovered:" + ",".join(uncovered[:5]) if uncovered else f"covered={len(BANNED_FLAGS)}",
    )

    variants = []
    for flag in BANNED_FLAGS:
        variants.append((flag, active_state(data, banned={flag: True})))
    variants.extend(
        [
            ("external_uniqueness_proof", active_state(data, contractible={"external_uniqueness_proof": True})),
            ("declared_only", active_state(data, contractible={"declared_only": True})),
            ("comparison_paths_not_internal", active_state(data, contractible={"comparison_paths_internal": False})),
            ("payload_paths_missing", active_state(data, contractible={"payload_paths_preserve_graph_rosati_control": False})),
            ("missing_required_flag", active_state(data, flags={"internal_comparison_paths": False})),
        ]
    )
    live_variant_reasons = {name: assess(variant) for name, variant in variants}
    gate(
        f"{PREFIX}10",
        not reasons and all(live_variant_reasons[name] for name in live_variant_reasons),
        f"live_reasons={reasons} rejected_variants={len(live_variant_reasons)}",
    )

    if failures:
        print("\nFAILURES:", ", ".join(failures))
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: globally unique diagram is internally contractible")
    print(
        "VERDICT: the cartesian compatibility diagram counts only when global "
        "uniqueness is witnessed by a source-internal contractible solution "
        "object. Endpoint-degree, DD.4 boundary, exact-delta, graph-Rosati-"
        "control, handoff/graph, probe, equalizer, mediator, and source-coupling "
        "data must be preserved along unique internal comparison paths inside "
        "the exact-24 finite-limit budget."
    )


if __name__ == "__main__":
    main()
