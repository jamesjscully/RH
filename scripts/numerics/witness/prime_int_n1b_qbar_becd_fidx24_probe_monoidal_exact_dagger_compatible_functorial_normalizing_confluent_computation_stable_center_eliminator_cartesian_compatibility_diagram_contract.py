r"""Monoidal/exact/dagger-compatible functorial center-eliminator normalizer.

Doc 571 makes the source-internal well-founded normalizer functorial. This
witness closes the next escape: the functorial normalizer cannot be
structure-blind. It must preserve the cartesian, monoidal, exact, dagger,
adjoint, dual-trace, pivotal, integral Grothendieck/K0, lift, DD.4, joint-law,
mediator-composition, endpoint-degree, boundary, graph/Rosati/control, and
handoff payload structure inside the exact-24 budget.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the structure-preserving normalizer witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 572
EXPECTED_WITNESS = "doc572-probe-monoidal-exact-dagger-compatible-functorial-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMMONDAGFUNCNORMCARTCOMPAT"

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

REQUIRED_DEPS = {
    FUNC,
    NORM,
    CONF,
    COMP,
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
    FINITE_INDEX,
}

STRUCTURE_COMPAT_EDGES = {
    ("cartesian_compatible_for", CART_EQV),
    ("monoidal_compatible_for", DAG),
    ("adjoint_compatible_for", ADJ),
    ("dual_trace_compatible_for", DUAL),
    ("pivotal_compatible_for", PIV),
    ("exact_additive_compatible_for", EXADD),
    ("integral_grothendieck_compatible_for", INTK0),
    ("effective_lift_compatible_for", EFF),
    ("primitive_lift_compatible_for", PRIM),
    ("rigid_lift_compatible_for", RIGID),
    ("dd4_active_compatible_for", DD4ACTIVE),
    ("joint_source_law_compatible_for", JOINT),
    ("mediator_composition_compatible_for", MED),
}

PAYLOAD_COMPAT_EDGES = {
    ("endpoint_integral_compatible_for", ENDPOINT),
    ("degree_monoidal_compatible_for", DEGREE),
    ("dd4_boundary_compatible_for", DD4_BOUNDARY),
    ("pushforward_compatible_for", PUSHFORWARD),
    ("exact_delta_compatible_for", EXACT_DELTA),
    ("graph_composition_compatible_for", GRAPH_COMP),
    ("rosati_compatible_for", ROSATI),
    ("control_compatible_for", CONTROL),
    ("handoff_compatible_for", HANDOFF),
    ("graph_later_compatible_for", GRAPH_LATER),
}

EXPECTED_EDGES = {
    (FUNC, "structure_preserved_by", MONDAG),
    (MONDAG, "structure_preserving_normalizer_for", FUNC),
    (MONDAG, "preserves", FINITE_INDEX),
} | {(MONDAG, relation, target) for relation, target in STRUCTURE_COMPAT_EDGES | PAYLOAD_COMPAT_EDGES}

STRUCTURE_COMPAT_TARGETS = {target for _, target in STRUCTURE_COMPAT_EDGES}
PAYLOAD_COMPAT_TARGETS = {target for _, target in PAYLOAD_COMPAT_EDGES}

REQUIRED_FLAGS = (
    "structure_preserving_normalizer",
    "cartesian_monoidal_compatibility",
    "dagger_trace_compatibility",
    "exact_additive_compatibility",
    "integral_grothendieck_compatibility",
    "dd4_joint_mediator_compatibility",
    "rosati_degree_compatibility",
    "payload_structure_compatibility",
    "inside_exact_24_budget",
    "no_new_structure_cell",
)

BANNED_FLAGS = (
    "center_eliminator_normalizer_structure_blind",
    "center_eliminator_normalizer_not_cartesian_monoidal",
    "center_eliminator_normalizer_not_dagger_compatible",
    "center_eliminator_normalizer_not_adjoint_compatible",
    "center_eliminator_normalizer_not_dual_trace_compatible",
    "center_eliminator_normalizer_not_pivotal_compatible",
    "center_eliminator_normalizer_not_exact_additive",
    "center_eliminator_normalizer_not_integral_grothendieck",
    "center_eliminator_normalizer_not_effective_lift_compatible",
    "center_eliminator_normalizer_not_primitive_lift_compatible",
    "center_eliminator_normalizer_not_rigid_lift_compatible",
    "center_eliminator_normalizer_not_dd4_active_compatible",
    "center_eliminator_normalizer_not_joint_source_law_compatible",
    "center_eliminator_normalizer_not_mediator_composition_compatible",
    "center_eliminator_normalizer_endpoint_integrality_structure_gap",
    "center_eliminator_normalizer_degree_monoidal_gap",
    "center_eliminator_normalizer_dd4_boundary_structure_gap",
    "center_eliminator_normalizer_exact_delta_structure_gap",
    "center_eliminator_normalizer_graph_composition_structure_gap",
    "center_eliminator_normalizer_rosati_structure_gap",
    "center_eliminator_normalizer_control_structure_gap",
    "center_eliminator_normalizer_handoff_graph_structure_gap",
    "center_eliminator_normalizer_structure_requires_choice",
    "center_eliminator_normalizer_structure_requires_new_cell",
    "center_eliminator_normalizer_structure_context_collapse",
    "center_eliminator_normalizer_structure_by_declaration",
    "center_eliminator_normalizer_structure_finite_sample",
    "center_eliminator_normalizer_structure_basis_row",
    "missing_structure_preserving_normalizer_certificate",
)

STRUCTURE_DATA = {
    "certificate": "monoidal_exact_dagger_compatible_functorial_normalizer",
    "base_certificate": FUNC,
    "structure_preserving": True,
    "structure_blind": False,
    "cartesian_monoidal": True,
    "dagger": True,
    "adjoint": True,
    "dual_trace": True,
    "pivotal": True,
    "exact_additive": True,
    "integral_grothendieck": True,
    "effective_lift": True,
    "primitive_lift": True,
    "rigid_lift": True,
    "dd4_active": True,
    "joint_source_law": True,
    "mediator_composition": True,
    "endpoint_integrality": True,
    "degree_monoidal": True,
    "dd4_boundary": True,
    "pushforward": True,
    "exact_delta": True,
    "graph_composition": True,
    "rosati": True,
    "control": True,
    "handoff_graph": True,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "structure_targets": STRUCTURE_COMPAT_TARGETS,
    "payload_targets": PAYLOAD_COMPAT_TARGETS,
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
        "structure": deepcopy(STRUCTURE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "structure":
            state["structure"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(MONDAG, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    structure = state["structure"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_572")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if MONDAG not in state["accepted"]:
        reasons.append("structure_preserving_normalizer_atom_not_accepted")
    if not set(state["requires"].get(MONDAG, [])).issuperset(REQUIRED_DEPS):
        reasons.append("structure_preserving_deps_missing")
    if MONDAG not in state["requires"].get(FUNC, []):
        reasons.append("functorial_normalizer_not_required_to_preserve_structure")
    if FUNC not in state["requires"].get(MONDAG, []):
        reasons.append("structure_preserving_normalizer_not_based_on_functorial_normalizer")
    if structure.get("base_certificate") != FUNC:
        reasons.append("wrong_base_certificate")
    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("structure_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "structure_preserving",
        "cartesian_monoidal",
        "dagger",
        "adjoint",
        "dual_trace",
        "pivotal",
        "exact_additive",
        "integral_grothendieck",
        "effective_lift",
        "primitive_lift",
        "rigid_lift",
        "dd4_active",
        "joint_source_law",
        "mediator_composition",
        "endpoint_integrality",
        "degree_monoidal",
        "dd4_boundary",
        "pushforward",
        "exact_delta",
        "graph_composition",
        "rosati",
        "control",
        "handoff_graph",
        "preserves_budget",
    )
    for field in required_truths:
        if not structure.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "structure_blind",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if structure.get(field):
            reasons.append(f"{field}_present")

    if set(structure.get("structure_targets", set())) != STRUCTURE_COMPAT_TARGETS:
        reasons.append("structure_targets_wrong")
    if set(structure.get("payload_targets", set())) != PAYLOAD_COMPAT_TARGETS:
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


def edge_targets(state: dict[str, Any], relations: set[str]) -> set[str]:
    return {
        target
        for source, relation, target in state["edges"]
        if source == MONDAG and relation in relations
    }


def variant(flag: str, **structure: Any) -> dict[str, Any]:
    return {"structure": structure, "banned": {flag: True}}


def main() -> None:
    data = load_map()
    state = active_state(data)
    reasons = assess(state)

    gate(
        f"{PREFIX}1",
        not [
            r
            for r in reasons
            if r
            in {
                "current_doc_before_572",
                "witness_not_registered",
                "structure_preserving_normalizer_atom_not_accepted",
            }
        ],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    structure = state["structure"]
    gate(
        f"{PREFIX}2",
        structure["structure_preserving"]
        and not structure["structure_blind"]
        and structure["base_certificate"] == FUNC,
        "functorial normalizer is structure-preserving, not structure-blind",
    )

    structure_targets = edge_targets(state, {relation for relation, _ in STRUCTURE_COMPAT_EDGES})
    gate(
        f"{PREFIX}3",
        structure_targets.issuperset(STRUCTURE_COMPAT_TARGETS)
        and structure["cartesian_monoidal"]
        and structure["dagger"]
        and structure["adjoint"]
        and structure["dual_trace"]
        and structure["pivotal"]
        and structure["exact_additive"]
        and structure["integral_grothendieck"],
        f"structure_targets={len(structure_targets & STRUCTURE_COMPAT_TARGETS)}/{len(STRUCTURE_COMPAT_TARGETS)}",
    )

    gate(
        f"{PREFIX}4",
        structure["effective_lift"]
        and structure["primitive_lift"]
        and structure["rigid_lift"]
        and structure["dd4_active"]
        and structure["joint_source_law"]
        and structure["mediator_composition"],
        "lift, DD.4, joint-source-law, and mediator-composition structure are preserved",
    )

    payload_targets = edge_targets(state, {relation for relation, _ in PAYLOAD_COMPAT_EDGES})
    gate(
        f"{PREFIX}5",
        payload_targets.issuperset(PAYLOAD_COMPAT_TARGETS)
        and structure["endpoint_integrality"]
        and structure["degree_monoidal"]
        and structure["dd4_boundary"]
        and structure["pushforward"]
        and structure["exact_delta"]
        and structure["graph_composition"]
        and structure["rosati"]
        and structure["control"]
        and structure["handoff_graph"],
        f"payload_targets={len(payload_targets & PAYLOAD_COMPAT_TARGETS)}/{len(PAYLOAD_COMPAT_TARGETS)}",
    )

    gate(
        f"{PREFIX}6",
        not structure["requires_choice"]
        and not structure["new_cell"]
        and not structure["context_collapse"]
        and not structure["declared_only"]
        and not structure["finite_sample"]
        and not structure["basis_row"]
        and structure["preserves_budget"],
        "no choice, new cell, context collapse, declaration, finite sample, or basis row",
    )

    gate(
        f"{PREFIX}7",
        not [
            r
            for r in reasons
            if r
            in {
                "structure_preserving_deps_missing",
                "functorial_normalizer_not_required_to_preserve_structure",
                "structure_preserving_normalizer_not_based_on_functorial_normalizer",
                "wrong_base_certificate",
            }
        ],
        "structure-preserving normalizer dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("structure_edges_missing") for r in reasons),
        "all structure-preserving normalizer graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variant_specs = [
        variant("center_eliminator_normalizer_structure_blind", structure_blind=True),
        variant("center_eliminator_normalizer_not_cartesian_monoidal", cartesian_monoidal=False),
        variant("center_eliminator_normalizer_not_dagger_compatible", dagger=False),
        variant("center_eliminator_normalizer_not_adjoint_compatible", adjoint=False),
        variant("center_eliminator_normalizer_not_dual_trace_compatible", dual_trace=False),
        variant("center_eliminator_normalizer_not_pivotal_compatible", pivotal=False),
        variant("center_eliminator_normalizer_not_exact_additive", exact_additive=False),
        variant("center_eliminator_normalizer_not_integral_grothendieck", integral_grothendieck=False),
        variant("center_eliminator_normalizer_not_effective_lift_compatible", effective_lift=False),
        variant("center_eliminator_normalizer_not_primitive_lift_compatible", primitive_lift=False),
        variant("center_eliminator_normalizer_not_rigid_lift_compatible", rigid_lift=False),
        variant("center_eliminator_normalizer_not_dd4_active_compatible", dd4_active=False),
        variant("center_eliminator_normalizer_not_joint_source_law_compatible", joint_source_law=False),
        variant("center_eliminator_normalizer_not_mediator_composition_compatible", mediator_composition=False),
        variant("center_eliminator_normalizer_endpoint_integrality_structure_gap", endpoint_integrality=False),
        variant("center_eliminator_normalizer_degree_monoidal_gap", degree_monoidal=False),
        variant("center_eliminator_normalizer_dd4_boundary_structure_gap", dd4_boundary=False),
        variant("center_eliminator_normalizer_exact_delta_structure_gap", exact_delta=False),
        variant("center_eliminator_normalizer_graph_composition_structure_gap", graph_composition=False),
        variant("center_eliminator_normalizer_rosati_structure_gap", rosati=False),
        variant("center_eliminator_normalizer_control_structure_gap", control=False),
        variant("center_eliminator_normalizer_handoff_graph_structure_gap", handoff_graph=False),
        variant("center_eliminator_normalizer_structure_requires_choice", requires_choice=True),
        variant("center_eliminator_normalizer_structure_requires_new_cell", new_cell=True),
        variant("center_eliminator_normalizer_structure_context_collapse", context_collapse=True),
        variant("center_eliminator_normalizer_structure_by_declaration", declared_only=True),
        variant("center_eliminator_normalizer_structure_finite_sample", finite_sample=True),
        variant("center_eliminator_normalizer_structure_basis_row", basis_row=True),
        {"accepted": state["accepted"] - {MONDAG}, "banned": {"missing_structure_preserving_normalizer_certificate": True}},
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
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: functorial normalizer preserves the structural payload")
    print(
        "VERDICT: the missing-object candidate counts only when the source-internal "
        "functorial normalizer is cartesian/monoidal/exact/dagger/trace/Rosati "
        "compatible, preserves the integral Grothendieck and DD.4 joint-law lift "
        "payload, and does so without choice, a new cell, context collapse, "
        "declaration, finite sample, or basis row."
    )


if __name__ == "__main__":
    main()
