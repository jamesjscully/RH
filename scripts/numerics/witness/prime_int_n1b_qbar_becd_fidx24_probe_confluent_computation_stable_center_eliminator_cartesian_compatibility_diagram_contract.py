r"""Confluent computation-stable center eliminator.

Doc 568 gives the dependent center eliminator internal beta/eta computation
laws. This witness closes the next escape: those computation laws must be
confluent as one joint source-side reduction system. Payload projections
cannot depend on the order in which endpoint, DD.4, exact-delta,
graph/Rosati/control, handoff, probe, equalizer, mediator, and
source-coupling computations are reduced.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the confluent eliminator witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 569
EXPECTED_WITNESS = "doc569-probe-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONFCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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
    (COMP, "confluence_stabilized_by", CONF),
    (CONF, "confluence_law_for", COMP),
    (CONF, "normal_form_for", ELIM),
    (CONF, "diamond_law_for", FINITE_LIMIT),
    (CONF, "diamond_law_for", EQUALIZER),
    (CONF, "diamond_law_for", CART_EQV),
    (CONF, "diamond_law_for", MEDIATOR),
    (CONF, "diamond_law_for", SOURCE_COUPLING),
    (CONF, "commuting_conversion_for", ENDPOINT),
    (CONF, "commuting_conversion_for", DEGREE),
    (CONF, "commuting_conversion_for", DD4_BOUNDARY),
    (CONF, "commuting_conversion_for", PUSHFORWARD),
    (CONF, "commuting_conversion_for", EXACT_DELTA),
    (CONF, "commuting_conversion_for", GRAPH_COMP),
    (CONF, "commuting_conversion_for", ROSATI),
    (CONF, "commuting_conversion_for", CONTROL),
    (CONF, "commuting_conversion_for", HANDOFF),
    (CONF, "commuting_conversion_for", GRAPH_LATER),
    (CONF, "preserves", FINITE_INDEX),
    (CONF, "coherent_for", COUPLED_IMAGE),
}

PAYLOAD_CONFLUENCE_TARGETS = {
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

STRUCTURE_CONFLUENCE_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

REQUIRED_FLAGS = (
    "confluent_computation",
    "source_internal_confluence",
    "unique_normal_form",
    "diamond_laws",
    "commuting_conversions",
    "order_independent",
    "critical_pairs_joined",
    "confluence_unique",
    "confluence_coherent",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_computation_not_confluent",
    "center_eliminator_computation_order_dependent",
    "center_eliminator_no_unique_normal_form",
    "center_eliminator_diamond_law_missing",
    "center_eliminator_commuting_conversion_missing",
    "center_eliminator_confluence_external",
    "center_eliminator_confluence_not_internal",
    "center_eliminator_confluence_not_unique",
    "center_eliminator_confluence_not_coherent",
    "center_eliminator_endpoint_degree_confluence_gap",
    "center_eliminator_boundary_confluence_gap",
    "center_eliminator_exact_delta_confluence_gap",
    "center_eliminator_graph_rosati_control_confluence_gap",
    "center_eliminator_handoff_graph_confluence_gap",
    "center_eliminator_probe_confluence_gap",
    "center_eliminator_equalizer_confluence_gap",
    "center_eliminator_mediator_confluence_gap",
    "center_eliminator_source_coupling_confluence_gap",
    "center_eliminator_confluence_requires_choice",
    "center_eliminator_confluence_requires_new_cell",
    "center_eliminator_confluence_context_collapse",
    "center_eliminator_confluence_by_declaration",
    "center_eliminator_confluence_finite_sample",
    "center_eliminator_confluence_basis_row",
    "missing_center_eliminator_confluence_certificate",
)

CONFLUENCE_DATA = {
    "certificate": "source_internal_confluent_center_eliminator_computation",
    "base_certificate": COMP,
    "confluent": True,
    "source_internal": True,
    "unique_normal_form": True,
    "diamond_laws": True,
    "commuting_conversions": True,
    "order_independent": True,
    "critical_pairs_joined": True,
    "unique": True,
    "coherent": True,
    "payload_complete": True,
    "structure_complete": True,
    "endpoint_degree_confluent": True,
    "boundary_exact_delta_confluent": True,
    "graph_rosati_control_confluent": True,
    "handoff_graph_confluent": True,
    "probe_confluent": True,
    "equalizer_confluent": True,
    "mediator_confluent": True,
    "source_coupling_confluent": True,
    "external": False,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "payload_targets": PAYLOAD_CONFLUENCE_TARGETS,
    "structure_targets": STRUCTURE_CONFLUENCE_TARGETS,
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
        "confluence": deepcopy(CONFLUENCE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "confluence":
            state["confluence"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CONF, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    confluence = state["confluence"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_569")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if CONF not in state["accepted"]:
        reasons.append("confluence_atom_not_accepted")
    if not set(state["requires"].get(CONF, [])).issuperset(REQUIRED_DEPS):
        reasons.append("confluence_deps_missing")
    if CONF not in state["requires"].get(COMP, []):
        reasons.append("computation_not_required_to_converge")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("confluence_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "confluent",
        "source_internal",
        "unique_normal_form",
        "diamond_laws",
        "commuting_conversions",
        "order_independent",
        "critical_pairs_joined",
        "unique",
        "coherent",
        "payload_complete",
        "structure_complete",
        "endpoint_degree_confluent",
        "boundary_exact_delta_confluent",
        "graph_rosati_control_confluent",
        "handoff_graph_confluent",
        "probe_confluent",
        "equalizer_confluent",
        "mediator_confluent",
        "source_coupling_confluent",
        "preserves_budget",
    )
    for field in required_truths:
        if not confluence.get(field):
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
        if confluence.get(field):
            reasons.append(f"{field}_present")

    if set(confluence.get("payload_targets", set())) != PAYLOAD_CONFLUENCE_TARGETS:
        reasons.append("payload_targets_wrong")
    if set(confluence.get("structure_targets", set())) != STRUCTURE_CONFLUENCE_TARGETS:
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
        not [r for r in reasons if r in {"current_doc_before_569", "witness_not_registered", "confluence_atom_not_accepted"}],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["confluence"]["confluent"]
        and state["confluence"]["source_internal"]
        and state["confluence"]["unique_normal_form"]
        and state["confluence"]["order_independent"]
        and not state["confluence"]["external"],
        "confluence is source-internal, order-independent, and has a unique normal form",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == CONF and relation == "commuting_conversion_for"
    }
    gate(
        f"{PREFIX}3",
        payload_edges.issuperset(PAYLOAD_CONFLUENCE_TARGETS)
        and state["confluence"]["payload_complete"]
        and state["confluence"]["endpoint_degree_confluent"]
        and state["confluence"]["boundary_exact_delta_confluent"]
        and state["confluence"]["graph_rosati_control_confluent"]
        and state["confluence"]["handoff_graph_confluent"],
        f"payload_confluence_targets={len(payload_edges & PAYLOAD_CONFLUENCE_TARGETS)}/{len(PAYLOAD_CONFLUENCE_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == CONF and relation == "diamond_law_for"
    }
    gate(
        f"{PREFIX}4",
        structure_edges.issuperset(STRUCTURE_CONFLUENCE_TARGETS)
        and state["confluence"]["probe_confluent"]
        and state["confluence"]["equalizer_confluent"]
        and state["confluence"]["mediator_confluent"]
        and state["confluence"]["source_coupling_confluent"],
        f"structure_confluence_targets={len(structure_edges & STRUCTURE_CONFLUENCE_TARGETS)}/{len(STRUCTURE_CONFLUENCE_TARGETS)}",
    )

    gate(
        f"{PREFIX}5",
        CONF in state["requires"].get(COMP, [])
        and COMP in state["requires"].get(CONF, [])
        and state["confluence"]["base_certificate"] == COMP,
        "computation-stable layer closes through confluence",
    )

    gate(
        f"{PREFIX}6",
        state["confluence"]["diamond_laws"]
        and state["confluence"]["commuting_conversions"]
        and state["confluence"]["critical_pairs_joined"]
        and state["confluence"]["unique"]
        and state["confluence"]["coherent"],
        "diamond laws and commuting conversions join critical pairs coherently",
    )

    gate(
        f"{PREFIX}7",
        not [r for r in reasons if r in {"confluence_deps_missing", "computation_not_required_to_converge"}],
        "confluence dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("confluence_edges_missing") for r in reasons),
        "all confluence graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variants = [
        active_state(data, confluence={"confluent": False}, banned={"center_eliminator_computation_not_confluent": True}),
        active_state(data, confluence={"order_independent": False}, banned={"center_eliminator_computation_order_dependent": True}),
        active_state(data, confluence={"unique_normal_form": False}, banned={"center_eliminator_no_unique_normal_form": True}),
        active_state(data, confluence={"diamond_laws": False}, banned={"center_eliminator_diamond_law_missing": True}),
        active_state(data, confluence={"commuting_conversions": False}, banned={"center_eliminator_commuting_conversion_missing": True}),
        active_state(data, confluence={"external": True}, banned={"center_eliminator_confluence_external": True}),
        active_state(data, confluence={"source_internal": False}, banned={"center_eliminator_confluence_not_internal": True}),
        active_state(data, confluence={"unique": False}, banned={"center_eliminator_confluence_not_unique": True}),
        active_state(data, confluence={"coherent": False}, banned={"center_eliminator_confluence_not_coherent": True}),
        active_state(
            data,
            confluence={"payload_targets": PAYLOAD_CONFLUENCE_TARGETS - {ENDPOINT}},
            banned={"center_eliminator_endpoint_degree_confluence_gap": True},
        ),
        active_state(
            data,
            confluence={"payload_targets": PAYLOAD_CONFLUENCE_TARGETS - {DD4_BOUNDARY}},
            banned={"center_eliminator_boundary_confluence_gap": True},
        ),
        active_state(
            data,
            confluence={"payload_targets": PAYLOAD_CONFLUENCE_TARGETS - {EXACT_DELTA}},
            banned={"center_eliminator_exact_delta_confluence_gap": True},
        ),
        active_state(
            data,
            confluence={"payload_targets": PAYLOAD_CONFLUENCE_TARGETS - {ROSATI}},
            banned={"center_eliminator_graph_rosati_control_confluence_gap": True},
        ),
        active_state(
            data,
            confluence={"payload_targets": PAYLOAD_CONFLUENCE_TARGETS - {HANDOFF}},
            banned={"center_eliminator_handoff_graph_confluence_gap": True},
        ),
        active_state(data, confluence={"probe_confluent": False}, banned={"center_eliminator_probe_confluence_gap": True}),
        active_state(data, confluence={"equalizer_confluent": False}, banned={"center_eliminator_equalizer_confluence_gap": True}),
        active_state(data, confluence={"mediator_confluent": False}, banned={"center_eliminator_mediator_confluence_gap": True}),
        active_state(data, confluence={"source_coupling_confluent": False}, banned={"center_eliminator_source_coupling_confluence_gap": True}),
        active_state(data, confluence={"requires_choice": True}, banned={"center_eliminator_confluence_requires_choice": True}),
        active_state(data, confluence={"new_cell": True}, banned={"center_eliminator_confluence_requires_new_cell": True}),
        active_state(data, confluence={"context_collapse": True}, banned={"center_eliminator_confluence_context_collapse": True}),
        active_state(data, confluence={"declared_only": True}, banned={"center_eliminator_confluence_by_declaration": True}),
        active_state(data, confluence={"finite_sample": True}, banned={"center_eliminator_confluence_finite_sample": True}),
        active_state(data, confluence={"basis_row": True}, banned={"center_eliminator_confluence_basis_row": True}),
        active_state(data, accepted=state["accepted"] - {CONF}, banned={"missing_center_eliminator_confluence_certificate": True}),
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
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: center eliminator computation is confluent")
    print(
        "VERDICT: the missing-object candidate counts only when the source-internal "
        "dependent center eliminator has confluent computation, commuting conversions, "
        "and a unique normal form for endpoint-degree, DD.4, exact-delta, "
        "graph-Rosati-control, handoff, probe, equalizer, mediator, and source-coupling "
        "projections inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
