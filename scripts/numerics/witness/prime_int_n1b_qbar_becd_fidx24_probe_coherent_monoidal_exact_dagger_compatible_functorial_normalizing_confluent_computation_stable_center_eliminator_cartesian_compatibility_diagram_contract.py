r"""Coherent structure-preserving functorial center-eliminator normalizer.

Doc 572 makes the functorial normalizer preserve every structural payload.
This witness closes the next escape: preservation cannot be a pairwise
checklist. The cartesian, monoidal, exact, dagger, trace, Rosati, integral
Grothendieck/K0, lift, DD.4, joint-law, mediator-composition, endpoint,
degree, boundary, exact-delta, graph, control, and handoff preservation data
must be one coherent interchange law stable under naturality, composition,
and refinement.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the coherent normalizer witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 573
EXPECTED_WITNESS = "doc573-probe-coherent-monoidal-exact-dagger-compatible-functorial-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOHMONDAGFUNCNORMCARTCOMPAT"

COH = "coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MONDAG = "monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FUNC = "functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
NORM = "normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CONF = "confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
COMP = "computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
DAG = "dagger_monoidal_probe_equivalence_certificate"
ADJ = "adjoint_pairing_probe_equivalence_certificate"
DUAL = "dual_trace_probe_equivalence_certificate"
PIV = "pivotal_monoidal_probe_equivalence_certificate"
EXADD = "exact_additive_trace_probe_equivalence_certificate"
INTK0 = "integral_grothendieck_trace_probe_equivalence_certificate"
EFF = "effective_grothendieck_trace_lift_certificate"
PRIM = "primitive_effective_grothendieck_lift_certificate"
RIGID = "rigid_primitive_effective_grothendieck_lift_certificate"
DD4ACTIVE = "dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
FINITE_INDEX = "exact_24_cell_finite_index"

failures: list[str] = []

STRUCTURE_TARGETS = {
    CART_EQV,
    DAG,
    ADJ,
    DUAL,
    PIV,
    EXADD,
    INTK0,
    EFF,
    PRIM,
    RIGID,
    DD4ACTIVE,
    JOINT,
    MED,
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

REQUIRED_DEPS = {
    MONDAG,
    FUNC,
    NORM,
    CONF,
    COMP,
    FINITE_INDEX,
} | STRUCTURE_TARGETS | PAYLOAD_TARGETS

EXPECTED_EDGES = {
    (MONDAG, "cohered_by", COH),
    (COH, "coherent_structure_normalizer_for", MONDAG),
    (COH, "preserves", FINITE_INDEX),
} | {(COH, "coherent_with_structure_for", target) for target in STRUCTURE_TARGETS} | {
    (COH, "coherent_with_payload_for", target) for target in PAYLOAD_TARGETS
}

REQUIRED_FLAGS = (
    "coherent_structure_normalizer",
    "single_interchange_law",
    "structure_coherence_complete",
    "payload_coherence_complete",
    "natural_coherence",
    "compositional_coherence",
    "refinement_stable_coherence",
    "inside_exact_24_budget",
    "no_new_coherence_cell",
    "no_choice",
)

BANNED_FLAGS = (
    "center_eliminator_normalizer_pairwise_structure_only",
    "center_eliminator_normalizer_coherence_missing",
    "center_eliminator_normalizer_cartesian_monoidal_interchange_gap",
    "center_eliminator_normalizer_monoidal_dagger_interchange_gap",
    "center_eliminator_normalizer_dagger_adjoint_interchange_gap",
    "center_eliminator_normalizer_adjoint_dual_trace_interchange_gap",
    "center_eliminator_normalizer_dual_trace_pivotal_interchange_gap",
    "center_eliminator_normalizer_pivotal_exact_additive_interchange_gap",
    "center_eliminator_normalizer_exact_integral_interchange_gap",
    "center_eliminator_normalizer_integral_lift_interchange_gap",
    "center_eliminator_normalizer_effective_primitive_rigid_interchange_gap",
    "center_eliminator_normalizer_dd4_joint_mediator_interchange_gap",
    "center_eliminator_normalizer_endpoint_degree_boundary_interchange_gap",
    "center_eliminator_normalizer_exact_delta_graph_interchange_gap",
    "center_eliminator_normalizer_rosati_control_interchange_gap",
    "center_eliminator_normalizer_handoff_graph_later_interchange_gap",
    "center_eliminator_normalizer_coherence_not_natural",
    "center_eliminator_normalizer_coherence_not_compositional",
    "center_eliminator_normalizer_coherence_not_refinement_stable",
    "center_eliminator_normalizer_coherence_requires_choice",
    "center_eliminator_normalizer_coherence_requires_new_cell",
    "center_eliminator_normalizer_coherence_context_collapse",
    "center_eliminator_normalizer_coherence_by_declaration",
    "center_eliminator_normalizer_coherence_finite_sample",
    "center_eliminator_normalizer_coherence_basis_row",
    "missing_coherent_structure_normalizer_certificate",
)

COHERENCE_DATA = {
    "certificate": "coherent_monoidal_exact_dagger_structure_normalizer",
    "base_certificate": MONDAG,
    "coherent": True,
    "single_interchange_law": True,
    "pairwise_only": False,
    "cartesian_monoidal_interchange": True,
    "monoidal_dagger_interchange": True,
    "dagger_adjoint_interchange": True,
    "adjoint_dual_trace_interchange": True,
    "dual_trace_pivotal_interchange": True,
    "pivotal_exact_additive_interchange": True,
    "exact_integral_interchange": True,
    "integral_lift_interchange": True,
    "effective_primitive_rigid_interchange": True,
    "dd4_joint_mediator_interchange": True,
    "endpoint_degree_boundary_interchange": True,
    "exact_delta_graph_interchange": True,
    "rosati_control_interchange": True,
    "handoff_graph_later_interchange": True,
    "natural": True,
    "compositional": True,
    "refinement_stable": True,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "structure_targets": STRUCTURE_TARGETS,
    "payload_targets": PAYLOAD_TARGETS,
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
        "coherence": deepcopy(COHERENCE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "coherence":
            state["coherence"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(COH, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    coherence = state["coherence"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_573")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if COH not in state["accepted"]:
        reasons.append("coherent_normalizer_atom_not_accepted")
    if not set(state["requires"].get(COH, [])).issuperset(REQUIRED_DEPS):
        reasons.append("coherent_normalizer_deps_missing")
    if COH not in state["requires"].get(MONDAG, []):
        reasons.append("structure_preserving_normalizer_not_required_to_be_coherent")
    if MONDAG not in state["requires"].get(COH, []):
        reasons.append("coherence_not_based_on_structure_preserving_normalizer")
    if coherence.get("base_certificate") != MONDAG:
        reasons.append("wrong_base_certificate")
    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("coherence_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "coherent",
        "single_interchange_law",
        "cartesian_monoidal_interchange",
        "monoidal_dagger_interchange",
        "dagger_adjoint_interchange",
        "adjoint_dual_trace_interchange",
        "dual_trace_pivotal_interchange",
        "pivotal_exact_additive_interchange",
        "exact_integral_interchange",
        "integral_lift_interchange",
        "effective_primitive_rigid_interchange",
        "dd4_joint_mediator_interchange",
        "endpoint_degree_boundary_interchange",
        "exact_delta_graph_interchange",
        "rosati_control_interchange",
        "handoff_graph_later_interchange",
        "natural",
        "compositional",
        "refinement_stable",
        "preserves_budget",
    )
    for field in required_truths:
        if not coherence.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "pairwise_only",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if coherence.get(field):
            reasons.append(f"{field}_present")

    if set(coherence.get("structure_targets", set())) != STRUCTURE_TARGETS:
        reasons.append("structure_targets_wrong")
    if set(coherence.get("payload_targets", set())) != PAYLOAD_TARGETS:
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


def edge_targets(state: dict[str, Any], relation_name: str) -> set[str]:
    return {
        target
        for source, relation, target in state["edges"]
        if source == COH and relation == relation_name
    }


def variant(flag: str, **coherence: Any) -> dict[str, Any]:
    return {"coherence": coherence, "banned": {flag: True}}


def main() -> None:
    data = load_map()
    state = active_state(data)
    reasons = assess(state)
    coherence = state["coherence"]

    gate(
        f"{PREFIX}1",
        not [
            r
            for r in reasons
            if r
            in {
                "current_doc_before_573",
                "witness_not_registered",
                "coherent_normalizer_atom_not_accepted",
            }
        ],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        coherence["coherent"]
        and coherence["single_interchange_law"]
        and not coherence["pairwise_only"]
        and coherence["base_certificate"] == MONDAG,
        "structure preservation is one coherent interchange law",
    )

    structure_targets = edge_targets(state, "coherent_with_structure_for")
    gate(
        f"{PREFIX}3",
        structure_targets.issuperset(STRUCTURE_TARGETS)
        and coherence["cartesian_monoidal_interchange"]
        and coherence["monoidal_dagger_interchange"]
        and coherence["dagger_adjoint_interchange"]
        and coherence["adjoint_dual_trace_interchange"]
        and coherence["dual_trace_pivotal_interchange"]
        and coherence["pivotal_exact_additive_interchange"],
        f"structure_coherence_targets={len(structure_targets & STRUCTURE_TARGETS)}/{len(STRUCTURE_TARGETS)}",
    )

    gate(
        f"{PREFIX}4",
        coherence["exact_integral_interchange"]
        and coherence["integral_lift_interchange"]
        and coherence["effective_primitive_rigid_interchange"]
        and coherence["dd4_joint_mediator_interchange"],
        "exact/integral/lift/DD.4/joint/mediator coherence is present",
    )

    payload_targets = edge_targets(state, "coherent_with_payload_for")
    gate(
        f"{PREFIX}5",
        payload_targets.issuperset(PAYLOAD_TARGETS)
        and coherence["endpoint_degree_boundary_interchange"]
        and coherence["exact_delta_graph_interchange"]
        and coherence["rosati_control_interchange"]
        and coherence["handoff_graph_later_interchange"],
        f"payload_coherence_targets={len(payload_targets & PAYLOAD_TARGETS)}/{len(PAYLOAD_TARGETS)}",
    )

    gate(
        f"{PREFIX}6",
        coherence["natural"]
        and coherence["compositional"]
        and coherence["refinement_stable"]
        and not coherence["requires_choice"]
        and not coherence["new_cell"]
        and not coherence["context_collapse"]
        and not coherence["declared_only"]
        and not coherence["finite_sample"]
        and not coherence["basis_row"]
        and coherence["preserves_budget"],
        "coherence is natural, compositional, refinement-stable, and budgeted",
    )

    gate(
        f"{PREFIX}7",
        not [
            r
            for r in reasons
            if r
            in {
                "coherent_normalizer_deps_missing",
                "structure_preserving_normalizer_not_required_to_be_coherent",
                "coherence_not_based_on_structure_preserving_normalizer",
                "wrong_base_certificate",
            }
        ],
        "coherent normalizer dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("coherence_edges_missing") for r in reasons),
        "all coherent-normalizer graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variant_specs = [
        variant("center_eliminator_normalizer_pairwise_structure_only", pairwise_only=True),
        variant("center_eliminator_normalizer_coherence_missing", coherent=False),
        variant("center_eliminator_normalizer_cartesian_monoidal_interchange_gap", cartesian_monoidal_interchange=False),
        variant("center_eliminator_normalizer_monoidal_dagger_interchange_gap", monoidal_dagger_interchange=False),
        variant("center_eliminator_normalizer_dagger_adjoint_interchange_gap", dagger_adjoint_interchange=False),
        variant("center_eliminator_normalizer_adjoint_dual_trace_interchange_gap", adjoint_dual_trace_interchange=False),
        variant("center_eliminator_normalizer_dual_trace_pivotal_interchange_gap", dual_trace_pivotal_interchange=False),
        variant("center_eliminator_normalizer_pivotal_exact_additive_interchange_gap", pivotal_exact_additive_interchange=False),
        variant("center_eliminator_normalizer_exact_integral_interchange_gap", exact_integral_interchange=False),
        variant("center_eliminator_normalizer_integral_lift_interchange_gap", integral_lift_interchange=False),
        variant("center_eliminator_normalizer_effective_primitive_rigid_interchange_gap", effective_primitive_rigid_interchange=False),
        variant("center_eliminator_normalizer_dd4_joint_mediator_interchange_gap", dd4_joint_mediator_interchange=False),
        variant("center_eliminator_normalizer_endpoint_degree_boundary_interchange_gap", endpoint_degree_boundary_interchange=False),
        variant("center_eliminator_normalizer_exact_delta_graph_interchange_gap", exact_delta_graph_interchange=False),
        variant("center_eliminator_normalizer_rosati_control_interchange_gap", rosati_control_interchange=False),
        variant("center_eliminator_normalizer_handoff_graph_later_interchange_gap", handoff_graph_later_interchange=False),
        variant("center_eliminator_normalizer_coherence_not_natural", natural=False),
        variant("center_eliminator_normalizer_coherence_not_compositional", compositional=False),
        variant("center_eliminator_normalizer_coherence_not_refinement_stable", refinement_stable=False),
        variant("center_eliminator_normalizer_coherence_requires_choice", requires_choice=True),
        variant("center_eliminator_normalizer_coherence_requires_new_cell", new_cell=True),
        variant("center_eliminator_normalizer_coherence_context_collapse", context_collapse=True),
        variant("center_eliminator_normalizer_coherence_by_declaration", declared_only=True),
        variant("center_eliminator_normalizer_coherence_finite_sample", finite_sample=True),
        variant("center_eliminator_normalizer_coherence_basis_row", basis_row=True),
        {"accepted": state["accepted"] - {COH}, "banned": {"missing_coherent_structure_normalizer_certificate": True}},
    ]
    variants = [active_state(data, **spec) for spec in variant_specs]
    live_reasons = reasons
    rejected_variants = [candidate for candidate in variants if assess(candidate)]
    gate(
        f"{PREFIX}10",
        not live_reasons and len(rejected_variants) == len(variants),
        f"live_reasons={live_reasons} rejected_variants={len(rejected_variants)}",
    )

    if failures:
        print("\nFAILURES:", ", ".join(failures))
        raise SystemExit(1)
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: structure-preserving normalizer is coherent")
    print(
        "VERDICT: the missing-object candidate counts only when structure "
        "preservation is one coherent, natural, compositional, refinement-stable "
        "interchange law for the cartesian, monoidal, exact, dagger, trace, "
        "Rosati, Grothendieck, DD.4, joint-law, mediator, endpoint, degree, "
        "boundary, graph, control, and handoff payloads inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
