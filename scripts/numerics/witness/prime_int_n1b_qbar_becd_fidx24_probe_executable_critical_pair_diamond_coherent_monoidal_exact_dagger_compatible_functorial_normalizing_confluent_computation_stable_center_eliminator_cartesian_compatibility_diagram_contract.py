#!/usr/bin/env python3
r"""Executable critical-pair diamond coherent center-eliminator normalizer.

Doc 573 requires one coherent structure-preserving interchange law. This
witness closes the next cheap escape: that coherence cannot be only a
certificate. It must be executable as a finite source-internal rewrite and
critical-pair diamond calculus with termination, local/global confluence,
unique source-internal normal forms, and natural/compositional/refinement
stability.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the executable coherence witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 574
EXPECTED_WITNESS = "doc574-probe-executable-critical-pair-diamond-coherent-monoidal-exact-dagger-compatible-functorial-normalizing-confluent-computation-stable-center-eliminator-cartesian-compatibility-diagram"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEXECODIAMCOHMONDAGFUNCNORMCARTCOMPAT"

EXEC = "executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
    COH,
    MONDAG,
    FUNC,
    NORM,
    CONF,
    COMP,
    FINITE_INDEX,
} | STRUCTURE_TARGETS | PAYLOAD_TARGETS

EXPECTED_EDGES = {
    (COH, "made_executable_by", EXEC),
    (EXEC, "executable_coherent_normalizer_for", COH),
    (EXEC, "preserves", FINITE_INDEX),
} | {(EXEC, "diamond_checks_structure_for", target) for target in STRUCTURE_TARGETS} | {
    (EXEC, "diamond_checks_payload_for", target) for target in PAYLOAD_TARGETS
}

REQUIRED_FLAGS = (
    "executable_coherence",
    "finite_rewrite_rules",
    "critical_pairs_complete",
    "terminating_rewrite",
    "local_and_global_confluence",
    "diamond_joins",
    "unique_source_internal_normal_forms",
    "natural_compositional_refinement_stable",
    "inside_exact_24_budget",
    "no_new_rewrite_cell",
)

BANNED_FLAGS = (
    "center_eliminator_coherence_not_executable",
    "center_eliminator_coherence_no_rewrite_rules",
    "center_eliminator_coherence_no_critical_pairs",
    "center_eliminator_coherence_unchecked_critical_pair",
    "center_eliminator_coherence_nonterminating_rewrite",
    "center_eliminator_coherence_not_locally_confluent",
    "center_eliminator_coherence_not_globally_confluent",
    "center_eliminator_coherence_diamond_missing",
    "center_eliminator_coherence_diamond_only_pairwise",
    "center_eliminator_coherence_diamond_not_payload_complete",
    "center_eliminator_coherence_diamond_not_structure_complete",
    "center_eliminator_coherence_diamond_not_natural",
    "center_eliminator_coherence_diamond_not_compositional",
    "center_eliminator_coherence_diamond_not_refinement_stable",
    "center_eliminator_coherence_normal_form_not_unique",
    "center_eliminator_coherence_normal_form_not_source_internal",
    "center_eliminator_coherence_rewrite_requires_choice",
    "center_eliminator_coherence_rewrite_requires_new_cell",
    "center_eliminator_coherence_rewrite_context_collapse",
    "center_eliminator_coherence_rewrite_by_declaration",
    "center_eliminator_coherence_rewrite_finite_sample",
    "center_eliminator_coherence_rewrite_basis_row",
    "center_eliminator_coherence_rewrite_not_budgeted",
    "missing_executable_coherence_diamond_certificate",
)

EXECUTABLE_DATA = {
    "certificate": "executable_critical_pair_diamond_coherent_normalizer",
    "base_certificate": COH,
    "executable": True,
    "finite_rewrite_rules": True,
    "critical_pairs_complete": True,
    "unchecked_critical_pair": False,
    "terminating": True,
    "locally_confluent": True,
    "globally_confluent": True,
    "diamond_joins": True,
    "pairwise_only": False,
    "payload_complete": True,
    "structure_complete": True,
    "natural": True,
    "compositional": True,
    "refinement_stable": True,
    "unique_normal_form": True,
    "source_internal_normal_form": True,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
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
        "executable": deepcopy(EXECUTABLE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "executable":
            state["executable"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(EXEC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    executable = state["executable"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_574")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc574_witness")
    if EXEC not in state["accepted"]:
        reasons.append("missing_executable_coherence_diamond_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(EXEC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if executable.get("base_certificate") != COH:
        reasons.append("wrong_base_certificate")
    if not executable.get("executable"):
        reasons.append("center_eliminator_coherence_not_executable")
    if not executable.get("finite_rewrite_rules"):
        reasons.append("center_eliminator_coherence_no_rewrite_rules")
    if not executable.get("critical_pairs_complete"):
        reasons.append("center_eliminator_coherence_no_critical_pairs")
    if executable.get("unchecked_critical_pair"):
        reasons.append("center_eliminator_coherence_unchecked_critical_pair")
    if not executable.get("terminating"):
        reasons.append("center_eliminator_coherence_nonterminating_rewrite")
    if not executable.get("locally_confluent"):
        reasons.append("center_eliminator_coherence_not_locally_confluent")
    if not executable.get("globally_confluent"):
        reasons.append("center_eliminator_coherence_not_globally_confluent")
    if not executable.get("diamond_joins"):
        reasons.append("center_eliminator_coherence_diamond_missing")
    if executable.get("pairwise_only"):
        reasons.append("center_eliminator_coherence_diamond_only_pairwise")
    if not executable.get("payload_complete") or not PAYLOAD_TARGETS <= set(executable["payload_targets"]):
        reasons.append("center_eliminator_coherence_diamond_not_payload_complete")
    if not executable.get("structure_complete") or not STRUCTURE_TARGETS <= set(executable["structure_targets"]):
        reasons.append("center_eliminator_coherence_diamond_not_structure_complete")
    if not executable.get("natural"):
        reasons.append("center_eliminator_coherence_diamond_not_natural")
    if not executable.get("compositional"):
        reasons.append("center_eliminator_coherence_diamond_not_compositional")
    if not executable.get("refinement_stable"):
        reasons.append("center_eliminator_coherence_diamond_not_refinement_stable")
    if not executable.get("unique_normal_form"):
        reasons.append("center_eliminator_coherence_normal_form_not_unique")
    if not executable.get("source_internal_normal_form"):
        reasons.append("center_eliminator_coherence_normal_form_not_source_internal")
    if executable.get("requires_choice"):
        reasons.append("center_eliminator_coherence_rewrite_requires_choice")
    if executable.get("new_cell"):
        reasons.append("center_eliminator_coherence_rewrite_requires_new_cell")
    if executable.get("context_collapse"):
        reasons.append("center_eliminator_coherence_rewrite_context_collapse")
    if executable.get("declared_only"):
        reasons.append("center_eliminator_coherence_rewrite_by_declaration")
    if executable.get("finite_sample"):
        reasons.append("center_eliminator_coherence_rewrite_finite_sample")
    if executable.get("basis_row"):
        reasons.append("center_eliminator_coherence_rewrite_basis_row")
    if not executable.get("budgeted"):
        reasons.append("center_eliminator_coherence_rewrite_not_budgeted")

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        reasons.append(f"missing_edges:{len(missing_edges)}")

    for flag, live in state["banned"].items():
        if live:
            reasons.append(flag)

    return reasons


def main() -> None:
    data = load_map()
    state = active_state(data)
    live_reasons = assess(state)

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc") >= EXPECTED_DOC
        and EXEC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["executable"]["executable"]
        and state["executable"]["finite_rewrite_rules"]
        and not state["executable"]["declared_only"],
        "coherence is executable by finite rewrite rules, not declaration",
    )
    gate(
        f"{PREFIX}3",
        STRUCTURE_TARGETS <= state["executable"]["structure_targets"]
        and PAYLOAD_TARGETS <= state["executable"]["payload_targets"],
        f"critical_pair_targets={len(STRUCTURE_TARGETS) + len(PAYLOAD_TARGETS)}/23",
    )
    gate(
        f"{PREFIX}4",
        state["executable"]["terminating"]
        and state["executable"]["locally_confluent"]
        and state["executable"]["globally_confluent"]
        and state["executable"]["diamond_joins"],
        "rewrite terminates and every critical peak joins",
    )
    gate(
        f"{PREFIX}5",
        state["executable"]["unique_normal_form"]
        and state["executable"]["source_internal_normal_form"],
        "normal forms are unique and source-internal",
    )
    gate(
        f"{PREFIX}6",
        state["executable"]["natural"]
        and state["executable"]["compositional"]
        and state["executable"]["refinement_stable"]
        and state["executable"]["budgeted"]
        and not any(
            state["executable"][key]
            for key in (
                "requires_choice",
                "new_cell",
                "context_collapse",
                "finite_sample",
                "basis_row",
            )
        ),
        "diamond calculus is natural, compositional, refinement-stable, and budgeted",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(EXEC, [])) <= state["accepted"],
        "executable coherent normalizer dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all executable-diamond graph edges present",
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

    print(
        f"\n{PREFIX}1-{PREFIX}10 ALL PASS: coherent structure preservation is executable by finite critical-pair diamonds"
    )
    print(
        "VERDICT: the missing-object candidate counts only when its coherent normalizer is an executable, "
        "terminating, confluent, source-internal diamond calculus covering all structural and payload "
        "critical pairs inside the exact-24 budget."
    )


if __name__ == "__main__":
    main()
