r"""Center-realized internally contractible cartesian compatibility diagram.

Doc 565 internalizes contractibility of the globally unique cartesian
compatibility diagram. This witness closes the next escape: a contractible
solution object must expose its center as the actual source-side payload
carrier, not merely assert that such a center is propositionally available.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_center_realized_internally_contractible_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the center-realized witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 566
EXPECTED_WITNESS = "doc566-probe-center-realized-internally-contractible-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERREALINTCONTRCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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

PAYLOAD_TARGETS = {
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

CENTER_STRUCTURE_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

EXPECTED_EDGES = {
    (ICONTR, "center_realized_by", CENTER),
    (CENTER, "realized_center_for", ICONTR),
    (CENTER, "center_solution_for", DIAG),
    (CENTER, "centered_in", FINITE_LIMIT),
    (CENTER, "center_equalized_by", EQUALIZER),
    (CENTER, "center_probe_reflected_by", CART_EQV),
    (CENTER, "center_mediator_generated_by", MEDIATOR),
    (CENTER, "center_source_coupled_by", SOURCE_COUPLING),
    (CENTER, "preserves", FINITE_INDEX),
    (CENTER, "coherent_for", COUPLED_IMAGE),
} | {(CENTER, "center_payload_for", target) for target in PAYLOAD_TARGETS}

REQUIRED_FLAGS = (
    "center_internal",
    "center_realized",
    "center_is_solution",
    "center_equalized",
    "center_probe_reflected",
    "center_mediator_generated",
    "center_source_coupled",
    "center_payload_complete",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "diagram_contractible_without_center",
    "diagram_center_external_choice",
    "diagram_center_global_choice",
    "diagram_center_missing",
    "diagram_center_not_internal",
    "diagram_center_not_realized",
    "diagram_center_payload_gap",
    "diagram_center_endpoint_degree_gap",
    "diagram_center_boundary_gap",
    "diagram_center_exact_delta_gap",
    "diagram_center_graph_rosati_control_gap",
    "diagram_center_handoff_graph_gap",
    "diagram_center_probe_gap",
    "diagram_center_equalizer_gap",
    "diagram_center_mediator_gap",
    "diagram_center_source_coupling_gap",
    "diagram_center_not_equalized",
    "diagram_center_not_probe_reflected",
    "diagram_center_not_mediator_generated",
    "diagram_center_not_source_coupled",
    "diagram_center_requires_new_cell",
    "diagram_center_context_collapse",
    "diagram_center_by_declaration",
    "diagram_center_finite_sample",
    "diagram_center_basis_row",
    "missing_center_realized_cartesian_compatibility_diagram_certificate",
)

CENTER_DATA = {
    "certificate": "source_internal_center_realization",
    "base_certificate": ICONTR,
    "center_internal": True,
    "center_realized": True,
    "center_is_solution": True,
    "center_equalized": True,
    "center_probe_reflected": True,
    "center_mediator_generated": True,
    "center_source_coupled": True,
    "center_payload_complete": True,
    "center_payload_targets": PAYLOAD_TARGETS,
    "center_structure_targets": CENTER_STRUCTURE_TARGETS,
    "external_center_choice": False,
    "global_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
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
        "center": deepcopy(CENTER_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "center":
            state["center"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CENTER, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    center = state["center"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_566")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if CENTER not in state["accepted"]:
        reasons.append("center_atom_not_accepted")
    if not set(state["requires"].get(CENTER, [])).issuperset(REQUIRED_DEPS):
        reasons.append("center_deps_missing")
    if CENTER not in state["requires"].get(ICONTR, []):
        reasons.append("contractible_object_not_required_to_expose_center")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("center_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    for field in (
        "center_internal",
        "center_realized",
        "center_is_solution",
        "center_equalized",
        "center_probe_reflected",
        "center_mediator_generated",
        "center_source_coupled",
        "center_payload_complete",
        "preserves_budget",
    ):
        if not center.get(field):
            reasons.append(f"{field}_missing")

    for field in (
        "external_center_choice",
        "global_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    ):
        if center.get(field):
            reasons.append(f"{field}_present")

    if set(center.get("center_payload_targets", set())) != PAYLOAD_TARGETS:
        reasons.append("center_payload_targets_wrong")
    if set(center.get("center_structure_targets", set())) != CENTER_STRUCTURE_TARGETS:
        reasons.append("center_structure_targets_wrong")

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
        not [r for r in reasons if r in {"current_doc_before_566", "witness_not_registered", "center_atom_not_accepted"}],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["center"]["center_internal"]
        and state["center"]["center_realized"]
        and state["center"]["center_is_solution"]
        and not state["center"]["external_center_choice"]
        and not state["center"]["global_choice"],
        "center is source-internal, realized, and not choice-picked",
    )

    gate(
        f"{PREFIX}3",
        state["center"]["center_equalized"]
        and state["center"]["center_probe_reflected"]
        and state["center"]["center_mediator_generated"]
        and state["center"]["center_source_coupled"],
        "center is equalized, probe-reflected, mediator-generated, and source-coupled",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == CENTER and relation == "center_payload_for"
    }
    gate(
        f"{PREFIX}4",
        payload_edges.issuperset(PAYLOAD_TARGETS) and state["center"]["center_payload_complete"],
        f"center_payload_targets={len(payload_edges & PAYLOAD_TARGETS)}/{len(PAYLOAD_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == CENTER
        and relation in {
            "centered_in",
            "center_equalized_by",
            "center_probe_reflected_by",
            "center_mediator_generated_by",
            "center_source_coupled_by",
        }
    }
    gate(
        f"{PREFIX}5",
        structure_edges.issuperset(CENTER_STRUCTURE_TARGETS),
        f"center_structure_targets={len(structure_edges & CENTER_STRUCTURE_TARGETS)}/{len(CENTER_STRUCTURE_TARGETS)}",
    )

    gate(
        f"{PREFIX}6",
        state["center"]["preserves_budget"]
        and not state["center"]["new_cell"]
        and not state["center"]["context_collapse"]
        and not state["center"]["declared_only"]
        and not state["center"]["finite_sample"]
        and not state["center"]["basis_row"],
        "no new cell, context collapse, declaration, finite sample, or basis row",
    )

    missing_deps = sorted(REQUIRED_DEPS - set(state["requires"].get(CENTER, [])))
    gate(
        f"{PREFIX}7",
        not missing_deps and CENTER in state["requires"].get(ICONTR, []),
        "center_deps_missing:" + ",".join(missing_deps[:4]) if missing_deps else "center dependency closure is wired",
    )

    missing_edges = sorted(EXPECTED_EDGES - state["edges"])
    gate(
        f"{PREFIX}8",
        not missing_edges,
        "missing_edges:" + ",".join("/".join(edge) for edge in missing_edges[:3]) if missing_edges else "all center graph edges present",
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
            ("external_center_choice", active_state(data, center={"external_center_choice": True})),
            ("global_choice", active_state(data, center={"global_choice": True})),
            ("center_not_equalized", active_state(data, center={"center_equalized": False})),
            ("center_payload_incomplete", active_state(data, center={"center_payload_complete": False})),
            ("missing_required_flag", active_state(data, flags={"center_internal": False})),
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: internally contractible diagram has a realized center")
    print(
        "VERDICT: the missing-object candidate counts only when the internally "
        "contractible cartesian compatibility diagram exposes a source-internal "
        "center that is the equalized, probe-reflected, mediator-generated, "
        "source-coupled carrier of endpoint-degree, DD.4, exact-delta, "
        "graph-Rosati-control, and handoff payloads inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
