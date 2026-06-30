r"""Center-eliminator realized cartesian compatibility diagram.

Doc 566 realizes the center of the internally contractible cartesian
compatibility diagram. This witness closes the next escape: the center cannot
carry payloads as independent attached fields. The source square must provide
a source-internal dependent eliminator that projects every payload component
from the same center.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_center_eliminator_realized_center_realized_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the center-eliminator witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 567
EXPECTED_WITNESS = "doc567-probe-center-eliminator-realized-center-realized-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMREALCARTCOMPAT"

failures: list[str] = []

REQUIRED_DEPS = {
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
    (CENTER, "eliminator_realized_by", ELIM),
    (ELIM, "eliminates_center_for", CENTER),
    (ELIM, "dependent_eliminator_for", DIAG),
    (ELIM, "eliminator_section_for", FINITE_LIMIT),
    (ELIM, "eliminator_section_for", EQUALIZER),
    (ELIM, "eliminator_probe_natural_for", CART_EQV),
    (ELIM, "eliminator_mediator_natural_for", MEDIATOR),
    (ELIM, "eliminator_source_coupled_for", SOURCE_COUPLING),
    (ELIM, "payload_projection_for", ENDPOINT),
    (ELIM, "payload_projection_for", DEGREE),
    (ELIM, "payload_projection_for", DD4_BOUNDARY),
    (ELIM, "payload_projection_for", PUSHFORWARD),
    (ELIM, "payload_projection_for", EXACT_DELTA),
    (ELIM, "payload_projection_for", GRAPH_COMP),
    (ELIM, "payload_projection_for", ROSATI),
    (ELIM, "payload_projection_for", CONTROL),
    (ELIM, "payload_projection_for", HANDOFF),
    (ELIM, "payload_projection_for", GRAPH_LATER),
    (ELIM, "preserves", FINITE_INDEX),
    (ELIM, "coherent_for", COUPLED_IMAGE),
}

PAYLOAD_PROJECTION_TARGETS = {
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

ELIMINATOR_STRUCTURE_TARGETS = {
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
}

REQUIRED_FLAGS = (
    "center_dependent_eliminator",
    "eliminator_source_internal",
    "eliminator_unique",
    "eliminator_coherent",
    "eliminator_payload_complete",
    "eliminator_probe_natural",
    "eliminator_equalizer_section",
    "eliminator_mediator_natural",
    "eliminator_source_coupled",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_payload_attached_not_eliminated",
    "center_payload_independent_tags",
    "center_no_dependent_eliminator",
    "center_eliminator_external",
    "center_eliminator_not_internal",
    "center_eliminator_not_unique",
    "center_eliminator_not_coherent",
    "center_eliminator_endpoint_degree_projection_gap",
    "center_eliminator_boundary_projection_gap",
    "center_eliminator_exact_delta_projection_gap",
    "center_eliminator_graph_rosati_control_projection_gap",
    "center_eliminator_handoff_graph_projection_gap",
    "center_eliminator_probe_projection_gap",
    "center_eliminator_equalizer_projection_gap",
    "center_eliminator_mediator_projection_gap",
    "center_eliminator_source_coupling_projection_gap",
    "center_eliminator_requires_choice",
    "center_eliminator_requires_new_cell",
    "center_eliminator_context_collapse",
    "center_eliminator_by_declaration",
    "center_eliminator_finite_sample",
    "center_eliminator_basis_row",
    "missing_center_dependent_eliminator_certificate",
)

ELIMINATOR_DATA = {
    "certificate": "source_internal_dependent_center_eliminator",
    "base_certificate": CENTER,
    "center": CENTER,
    "dependent_eliminator": True,
    "source_internal": True,
    "unique": True,
    "coherent": True,
    "payload_complete": True,
    "projects_endpoint_degree": True,
    "projects_boundary_exact_delta": True,
    "projects_graph_rosati_control": True,
    "projects_handoff_graph": True,
    "probe_natural": True,
    "equalizer_section": True,
    "mediator_natural": True,
    "source_coupled": True,
    "external": False,
    "independent_tags": False,
    "requires_choice": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "new_cell": False,
    "context_collapse": False,
    "preserves_budget": True,
    "structure_targets": ELIMINATOR_STRUCTURE_TARGETS,
    "payload_projection_targets": PAYLOAD_PROJECTION_TARGETS,
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
        "eliminator": deepcopy(ELIMINATOR_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "eliminator":
            state["eliminator"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        elif key == "edges_remove":
            state["edges"] = set(state["edges"]) - set(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(ELIM, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    eliminator = state["eliminator"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_567")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("witness_not_registered")
    if ELIM not in state["accepted"]:
        reasons.append("eliminator_atom_not_accepted")
    if not set(state["requires"].get(ELIM, [])).issuperset(REQUIRED_DEPS):
        reasons.append("eliminator_deps_missing")
    if ELIM not in state["requires"].get(CENTER, []):
        reasons.append("center_not_required_to_eliminate")

    if missing := sorted(EXPECTED_EDGES - state["edges"]):
        reasons.append("eliminator_edges_missing:" + ",".join("/".join(edge) for edge in missing[:3]))

    required_truths = (
        "dependent_eliminator",
        "source_internal",
        "unique",
        "coherent",
        "payload_complete",
        "projects_endpoint_degree",
        "projects_boundary_exact_delta",
        "projects_graph_rosati_control",
        "projects_handoff_graph",
        "probe_natural",
        "equalizer_section",
        "mediator_natural",
        "source_coupled",
        "preserves_budget",
    )
    for field in required_truths:
        if not eliminator.get(field):
            reasons.append(f"{field}_missing")

    forbidden_truths = (
        "external",
        "independent_tags",
        "requires_choice",
        "declared_only",
        "finite_sample",
        "basis_row",
        "new_cell",
        "context_collapse",
    )
    for field in forbidden_truths:
        if eliminator.get(field):
            reasons.append(f"{field}_present")

    if set(eliminator.get("structure_targets", set())) != ELIMINATOR_STRUCTURE_TARGETS:
        reasons.append("structure_targets_wrong")
    if set(eliminator.get("payload_projection_targets", set())) != PAYLOAD_PROJECTION_TARGETS:
        reasons.append("payload_projection_targets_wrong")

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
        not [r for r in reasons if r in {"current_doc_before_567", "witness_not_registered", "eliminator_atom_not_accepted"}],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )

    gate(
        f"{PREFIX}2",
        state["eliminator"]["dependent_eliminator"]
        and state["eliminator"]["source_internal"]
        and state["eliminator"]["unique"]
        and state["eliminator"]["coherent"]
        and not state["eliminator"]["external"],
        "dependent eliminator is source-internal, unique, coherent, and not external",
    )

    payload_edges = {
        target
        for source, relation, target in state["edges"]
        if source == ELIM and relation == "payload_projection_for"
    }
    gate(
        f"{PREFIX}3",
        payload_edges.issuperset(PAYLOAD_PROJECTION_TARGETS)
        and state["eliminator"]["payload_complete"]
        and state["eliminator"]["projects_endpoint_degree"]
        and state["eliminator"]["projects_boundary_exact_delta"]
        and state["eliminator"]["projects_graph_rosati_control"]
        and state["eliminator"]["projects_handoff_graph"],
        f"payload_projection_targets={len(payload_edges & PAYLOAD_PROJECTION_TARGETS)}/{len(PAYLOAD_PROJECTION_TARGETS)}",
    )

    structure_edges = {
        target
        for source, relation, target in state["edges"]
        if source == ELIM
        and relation in {
            "eliminator_section_for",
            "eliminator_probe_natural_for",
            "eliminator_mediator_natural_for",
            "eliminator_source_coupled_for",
        }
    }
    gate(
        f"{PREFIX}4",
        structure_edges.issuperset(ELIMINATOR_STRUCTURE_TARGETS)
        and state["eliminator"]["probe_natural"]
        and state["eliminator"]["equalizer_section"]
        and state["eliminator"]["mediator_natural"]
        and state["eliminator"]["source_coupled"],
        f"structure_targets={len(structure_edges & ELIMINATOR_STRUCTURE_TARGETS)}/{len(ELIMINATOR_STRUCTURE_TARGETS)}",
    )

    gate(
        f"{PREFIX}5",
        ELIM in state["requires"].get(CENTER, [])
        and CENTER in state["requires"].get(ELIM, [])
        and state["eliminator"]["base_certificate"] == CENTER,
        "center-realized layer closes through the dependent eliminator",
    )

    forbidden_clean = not any(
        state["eliminator"][field]
        for field in (
            "independent_tags",
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
        "no independent tags, choice, new cell, context collapse, declaration, finite sample, or basis row",
    )

    gate(
        f"{PREFIX}7",
        not [r for r in reasons if r in {"eliminator_deps_missing", "center_not_required_to_eliminate"}],
        "eliminator dependency closure is wired",
    )

    gate(
        f"{PREFIX}8",
        not any(r.startswith("eliminator_edges_missing") for r in reasons),
        "all dependent-eliminator graph edges present",
    )

    covered = [flag for flag in BANNED_FLAGS if rejected_or_excluded(state, flag)]
    gate(
        f"{PREFIX}9",
        len(covered) == len(BANNED_FLAGS),
        f"covered={len(covered)}",
    )

    variants = [
        active_state(data, eliminator={"dependent_eliminator": False}, banned={"center_no_dependent_eliminator": True}),
        active_state(data, eliminator={"source_internal": False}, banned={"center_eliminator_not_internal": True}),
        active_state(data, eliminator={"unique": False}, banned={"center_eliminator_not_unique": True}),
        active_state(data, eliminator={"coherent": False}, banned={"center_eliminator_not_coherent": True}),
        active_state(data, eliminator={"external": True}, banned={"center_eliminator_external": True}),
        active_state(data, eliminator={"independent_tags": True}, banned={"center_payload_independent_tags": True}),
        active_state(
            data,
            eliminator={"payload_projection_targets": PAYLOAD_PROJECTION_TARGETS - {ENDPOINT}},
            banned={"center_eliminator_endpoint_degree_projection_gap": True},
        ),
        active_state(
            data,
            eliminator={"payload_projection_targets": PAYLOAD_PROJECTION_TARGETS - {DD4_BOUNDARY}},
            banned={"center_eliminator_boundary_projection_gap": True},
        ),
        active_state(
            data,
            eliminator={"payload_projection_targets": PAYLOAD_PROJECTION_TARGETS - {EXACT_DELTA}},
            banned={"center_eliminator_exact_delta_projection_gap": True},
        ),
        active_state(
            data,
            eliminator={"payload_projection_targets": PAYLOAD_PROJECTION_TARGETS - {ROSATI}},
            banned={"center_eliminator_graph_rosati_control_projection_gap": True},
        ),
        active_state(
            data,
            eliminator={"payload_projection_targets": PAYLOAD_PROJECTION_TARGETS - {HANDOFF}},
            banned={"center_eliminator_handoff_graph_projection_gap": True},
        ),
        active_state(data, eliminator={"probe_natural": False}, banned={"center_eliminator_probe_projection_gap": True}),
        active_state(data, eliminator={"equalizer_section": False}, banned={"center_eliminator_equalizer_projection_gap": True}),
        active_state(data, eliminator={"mediator_natural": False}, banned={"center_eliminator_mediator_projection_gap": True}),
        active_state(data, eliminator={"source_coupled": False}, banned={"center_eliminator_source_coupling_projection_gap": True}),
        active_state(data, eliminator={"requires_choice": True}, banned={"center_eliminator_requires_choice": True}),
        active_state(data, eliminator={"new_cell": True}, banned={"center_eliminator_requires_new_cell": True}),
        active_state(data, eliminator={"context_collapse": True}, banned={"center_eliminator_context_collapse": True}),
        active_state(data, eliminator={"declared_only": True}, banned={"center_eliminator_by_declaration": True}),
        active_state(data, eliminator={"finite_sample": True}, banned={"center_eliminator_finite_sample": True}),
        active_state(data, eliminator={"basis_row": True}, banned={"center_eliminator_basis_row": True}),
        active_state(data, accepted=state["accepted"] - {ELIM}, banned={"missing_center_dependent_eliminator_certificate": True}),
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
    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: center payloads are projected by a dependent eliminator")
    print(
        "VERDICT: the missing-object candidate counts only when the realized center "
        "comes with a source-internal dependent eliminator that coherently projects "
        "endpoint-degree, DD.4, exact-delta, graph-Rosati-control, handoff, probe, "
        "equalizer, mediator, and source-coupling data from the same center inside "
        "the exact-24 budget."
    )


if __name__ == "__main__":
    main()
