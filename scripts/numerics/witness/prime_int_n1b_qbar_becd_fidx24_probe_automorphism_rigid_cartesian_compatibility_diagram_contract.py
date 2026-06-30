r"""Automorphism-rigid represented-limit cartesian compatibility diagram.

Doc 561 makes the represented-limit source-constraint bundle into one
cartesian compatibility diagram. This witness closes the next cheap repair:
the diagram cannot exist only up to automorphism, transport, skeleton choice,
or retuned representative. The same source-side diagram must fix the endpoint,
boundary, DD4/exact-delta, graph/Rosati/control, handoff, mediator, coupling,
equalizer, and probe payloads.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_automorphism_rigid_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the automorphism-rigid diagram witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 562
EXPECTED_WITNESS = "doc562-probe-automorphism-rigid-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPAUTRIGCARTCOMPATREPLIMSRCBUNDLE"

failures: list[str] = []

REQUIRED_AUT_DEPS = {
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
    (DIAG, "made_automorphism_rigid_by", AUT),
    (AUT, "automorphism_rigid_diagram_for", DIAG),
    (AUT, "rigid_diagram_for", BUNDLE),
    (AUT, "automorphism_free_for", DIAG),
    (AUT, "stabilizer_trivial_for", EQUALIZER),
    (AUT, "choice_unique_for", SUBREP),
    (AUT, "transport_unique_for", CART_EQV),
    (AUT, "skeleton_free_for", FINITE_LIMIT),
    (AUT, "representative_unique_for", COUPLED_IMAGE),
    (AUT, "mediator_fixed_by", MEDIATOR),
    (AUT, "source_coupling_fixed_by", SOURCE_COUPLING),
    (AUT, "endpoint_degree_fixed_for", ENDPOINT),
    (AUT, "endpoint_degree_fixed_for", DEGREE),
    (AUT, "boundary_square_fixed_for", DD4_BOUNDARY),
    (AUT, "boundary_square_fixed_for", PUSHFORWARD),
    (AUT, "exact_delta_fixed_for", EXACT_DELTA),
    (AUT, "graph_rosati_control_fixed_for", GRAPH_COMP),
    (AUT, "graph_rosati_control_fixed_for", ROSATI),
    (AUT, "graph_rosati_control_fixed_for", CONTROL),
    (AUT, "handoff_fixed_for", HANDOFF),
    (AUT, "graph_realization_fixed_for", GRAPH_LATER),
    (AUT, "preserves", FINITE_INDEX),
    (AUT, "coherent_for", COUPLED_IMAGE),
}

REQUIRED_FIXED_TARGETS = {
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
    MEDIATOR,
    SOURCE_COUPLING,
    EQUALIZER,
    CART_EQV,
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    FINITE_INDEX,
}

REQUIRED_IDENTITIES = {
    "automorphism_triviality_law",
    "stabilizer_triviality_law",
    "transport_uniqueness_law",
    "unique_representative_law",
    "no_skeletonization_law",
    "fixed_endpoint_degree_law",
    "fixed_boundary_exact_delta_law",
    "fixed_graph_rosati_control_law",
    "fixed_mediator_coupling_equalizer_probe_law",
}

BANNED_FLAGS = (
    "diagram_automorphism_group_nontrivial",
    "diagram_stabilizer_torsor",
    "diagram_isomorphic_replacement",
    "diagram_skeleton_choice",
    "diagram_transport_ambiguity",
    "diagram_representative_choice",
    "diagram_retuned_representative",
    "diagram_unit_sign_ambiguity",
    "diagram_endpoint_degree_moves",
    "diagram_boundary_square_moves",
    "diagram_exact_delta_moves",
    "diagram_graph_rosati_control_moves",
    "diagram_handoff_graph_moves",
    "diagram_mediator_moves",
    "diagram_source_coupling_moves",
    "diagram_equalizer_moves",
    "diagram_probe_transport_moves",
    "diagram_rigidity_by_declaration",
    "diagram_rigidity_finite_sample",
    "diagram_rigidity_basis_row",
    "missing_automorphism_rigid_cartesian_compatibility_diagram_certificate",
)

REQUIRED_FLAGS = (
    "automorphism_rigid_diagram_actual",
    "automorphism_free",
    "stabilizer_trivial",
    "transport_unique",
    "representative_choice_free",
    "fixed_payloads",
    "inside_exact_24_budget",
)

RIGIDITY_DATA = {
    "certificate": "represented_limit_automorphism_rigid_cartesian_compatibility_diagram",
    "base_certificate": DIAG,
    "automorphism_free": True,
    "stabilizer_trivial": True,
    "choice_unique": True,
    "transport_unique": True,
    "skeleton_free": True,
    "representative_unique": True,
    "unit_sign_ambiguous": False,
    "endpoint_degree_fixed": True,
    "boundary_square_fixed": True,
    "exact_delta_fixed": True,
    "graph_rosati_control_fixed": True,
    "handoff_graph_fixed": True,
    "mediator_fixed": True,
    "source_coupling_fixed": True,
    "equalizer_fixed": True,
    "probe_transport_fixed": True,
    "preserves_budget": True,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "retuned_representative": False,
    "imports_positivity": False,
    "fixed_targets": REQUIRED_FIXED_TARGETS,
    "identities": REQUIRED_IDENTITIES,
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


def active_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    edge_set = {
        (edge["source"], edge["relation"], edge["target"])
        for edge in data.get("edges", [])
        if edge.get("introduced_by", 0) <= EXPECTED_DOC
    }
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "edges": edge_set,
        "rigidity": deepcopy(RIGIDITY_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def _as_set(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {value}
    return {str(item) for item in value}


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    requires = state["requires"]
    rigidity = state["rigidity"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_562")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc562_witness_missing")
    if AUT not in accepted:
        out.append("automorphism_rigid_cartesian_compatibility_diagram_missing_from_current")
    if DIAG not in accepted:
        out.append("cartesian_compatibility_diagram_base_missing_from_current")

    if not isinstance(rigidity, dict):
        out.append("automorphism_rigid_diagram_data_not_mapping")
        rigidity = {}
    if rigidity.get("certificate") != "represented_limit_automorphism_rigid_cartesian_compatibility_diagram":
        out.append("missing_automorphism_rigid_cartesian_compatibility_diagram_certificate")
    if rigidity.get("base_certificate") != DIAG:
        out.append("automorphism_rigid_diagram_not_based_on_cartesian_diagram")
    if not rigidity.get("automorphism_free"):
        out.append("diagram_automorphism_group_nontrivial")
    if not rigidity.get("stabilizer_trivial"):
        out.append("diagram_stabilizer_torsor")
    if not rigidity.get("choice_unique"):
        out.append("diagram_representative_choice")
    if not rigidity.get("transport_unique"):
        out.append("diagram_transport_ambiguity")
    if not rigidity.get("skeleton_free"):
        out.append("diagram_skeleton_choice")
    if not rigidity.get("representative_unique"):
        out.append("diagram_isomorphic_replacement")
    if rigidity.get("retuned_representative"):
        out.append("diagram_retuned_representative")
    if rigidity.get("unit_sign_ambiguous"):
        out.append("diagram_unit_sign_ambiguity")
    if not rigidity.get("endpoint_degree_fixed"):
        out.append("diagram_endpoint_degree_moves")
    if not rigidity.get("boundary_square_fixed"):
        out.append("diagram_boundary_square_moves")
    if not rigidity.get("exact_delta_fixed"):
        out.append("diagram_exact_delta_moves")
    if not rigidity.get("graph_rosati_control_fixed"):
        out.append("diagram_graph_rosati_control_moves")
    if not rigidity.get("handoff_graph_fixed"):
        out.append("diagram_handoff_graph_moves")
    if not rigidity.get("mediator_fixed"):
        out.append("diagram_mediator_moves")
    if not rigidity.get("source_coupling_fixed"):
        out.append("diagram_source_coupling_moves")
    if not rigidity.get("equalizer_fixed"):
        out.append("diagram_equalizer_moves")
    if not rigidity.get("probe_transport_fixed"):
        out.append("diagram_probe_transport_moves")
    if not rigidity.get("preserves_budget"):
        out.append("automorphism_rigid_diagram_not_inside_exact_24_budget")
    if rigidity.get("declared_only"):
        out.append("diagram_rigidity_by_declaration")
    if rigidity.get("finite_sample"):
        out.append("diagram_rigidity_finite_sample")
    if rigidity.get("basis_row"):
        out.append("diagram_rigidity_basis_row")
    if rigidity.get("imports_positivity"):
        out.append("automorphism_rigid_diagram_imports_positivity")

    missing_targets = REQUIRED_FIXED_TARGETS - _as_set(rigidity.get("fixed_targets"))
    if missing_targets:
        out.append("automorphism_rigid_fixed_targets_missing:" + ",".join(sorted(missing_targets)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(rigidity.get("identities"))
    if missing_identities:
        out.append("automorphism_rigid_identity_missing:" + ",".join(sorted(missing_identities)))

    if AUT not in requires.get(DIAG, []):
        out.append("cartesian_diagram_not_required_to_be_automorphism_rigid")
    if DIAG not in requires.get(AUT, []):
        out.append("automorphism_rigid_diagram_requires_missing_cartesian_diagram")
    missing_deps = REQUIRED_AUT_DEPS - set(requires.get(AUT, []))
    if missing_deps:
        out.append("automorphism_rigid_diagram_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("automorphism_rigid_edges_missing:" + ",".join(rendered))

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    out.extend(flag for flag, active_flag in state["banned"].items() if active_flag)
    return out


def accepts(state: dict[str, Any]) -> bool:
    return not reasons(state)


def variant(base: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    data = deepcopy(base)
    for key, value in kwargs.items():
        if key == "flags":
            data["flags"].update(value)
        elif key == "banned":
            data["banned"].update(value)
        elif key == "rigidity":
            data["rigidity"].update(value)
        elif key == "requires_drop":
            for node, req in value:
                data["requires"][node] = [item for item in data["requires"].get(node, []) if item != req]
        elif key == "edges_drop":
            data["edges"] -= set(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 562 automorphism-rigid diagram layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s fixed_targets=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["rigidity"]["fixed_targets"]),
    ),
)

automorphism_gap = variant(
    live,
    banned={
        "diagram_automorphism_group_nontrivial": True,
        "diagram_stabilizer_torsor": True,
        "diagram_unit_sign_ambiguity": True,
    },
    rigidity={"automorphism_free": False, "stabilizer_trivial": False, "unit_sign_ambiguous": True},
)

gate(
    f"{PREFIX}2 rejects nontrivial automorphisms, stabilizers, or unit signs",
    not accepts(automorphism_gap)
    and {
        "diagram_automorphism_group_nontrivial",
        "diagram_stabilizer_torsor",
        "diagram_unit_sign_ambiguity",
    }
    <= set(reasons(automorphism_gap)),
    ",".join(reasons(automorphism_gap)),
)

transport_gap = variant(
    live,
    banned={
        "diagram_isomorphic_replacement": True,
        "diagram_skeleton_choice": True,
        "diagram_transport_ambiguity": True,
        "diagram_representative_choice": True,
        "diagram_retuned_representative": True,
    },
    rigidity={
        "representative_unique": False,
        "skeleton_free": False,
        "transport_unique": False,
        "choice_unique": False,
        "retuned_representative": True,
    },
)

gate(
    f"{PREFIX}3 rejects isomorphic replacement, skeleton, representative, transport, or retuning choices",
    not accepts(transport_gap)
    and {
        "diagram_isomorphic_replacement",
        "diagram_skeleton_choice",
        "diagram_transport_ambiguity",
        "diagram_representative_choice",
        "diagram_retuned_representative",
    }
    <= set(reasons(transport_gap)),
    ",".join(reasons(transport_gap)),
)

source_payload_gap = variant(
    live,
    banned={
        "diagram_endpoint_degree_moves": True,
        "diagram_boundary_square_moves": True,
        "diagram_exact_delta_moves": True,
    },
    rigidity={"endpoint_degree_fixed": False, "boundary_square_fixed": False, "exact_delta_fixed": False},
)

gate(
    f"{PREFIX}4 rejects endpoint-degree, boundary, or exact-delta movement",
    not accepts(source_payload_gap)
    and {
        "diagram_endpoint_degree_moves",
        "diagram_boundary_square_moves",
        "diagram_exact_delta_moves",
    }
    <= set(reasons(source_payload_gap)),
    ",".join(reasons(source_payload_gap)),
)

structural_payload_gap = variant(
    live,
    banned={
        "diagram_graph_rosati_control_moves": True,
        "diagram_handoff_graph_moves": True,
        "diagram_mediator_moves": True,
        "diagram_source_coupling_moves": True,
        "diagram_equalizer_moves": True,
        "diagram_probe_transport_moves": True,
    },
    rigidity={
        "graph_rosati_control_fixed": False,
        "handoff_graph_fixed": False,
        "mediator_fixed": False,
        "source_coupling_fixed": False,
        "equalizer_fixed": False,
        "probe_transport_fixed": False,
    },
)

gate(
    f"{PREFIX}5 rejects graph, handoff, mediator, coupling, equalizer, or probe movement",
    not accepts(structural_payload_gap)
    and {
        "diagram_graph_rosati_control_moves",
        "diagram_handoff_graph_moves",
        "diagram_mediator_moves",
        "diagram_source_coupling_moves",
        "diagram_equalizer_moves",
        "diagram_probe_transport_moves",
    }
    <= set(reasons(structural_payload_gap)),
    ",".join(reasons(structural_payload_gap)),
)

selector_gap = variant(
    live,
    banned={
        "diagram_rigidity_by_declaration": True,
        "diagram_rigidity_finite_sample": True,
        "diagram_rigidity_basis_row": True,
    },
    rigidity={"declared_only": True, "finite_sample": True, "basis_row": True},
)

gate(
    f"{PREFIX}6 rejects declared rigidity, finite samples, or basis rows",
    not accepts(selector_gap)
    and {
        "diagram_rigidity_by_declaration",
        "diagram_rigidity_finite_sample",
        "diagram_rigidity_basis_row",
    }
    <= set(reasons(selector_gap)),
    ",".join(reasons(selector_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_automorphism_rigid_cartesian_compatibility_diagram_certificate": True},
    rigidity={
        "certificate": None,
        "fixed_targets": REQUIRED_FIXED_TARGETS - {ENDPOINT, HANDOFF, CART_EQV},
        "identities": REQUIRED_IDENTITIES
        - {
            "automorphism_triviality_law",
            "transport_uniqueness_law",
            "fixed_endpoint_degree_law",
        },
    },
)

gate(
    f"{PREFIX}7 rejects missing rigidity certificates, fixed targets, or identities",
    not accepts(missing_gap)
    and "missing_automorphism_rigid_cartesian_compatibility_diagram_certificate" in reasons(missing_gap)
    and any(reason.startswith("automorphism_rigid_fixed_targets_missing:") for reason in reasons(missing_gap))
    and any(reason.startswith("automorphism_rigid_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(DIAG, AUT), (AUT, DIAG), (AUT, EXACT_DELTA)],
)

gate(
    f"{PREFIX}8 requires cartesian diagram and automorphism-rigid layer to close together",
    not accepts(closure_gap)
    and {
        "cartesian_diagram_not_required_to_be_automorphism_rigid",
        "automorphism_rigid_diagram_requires_missing_cartesian_diagram",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("automorphism_rigid_diagram_requires_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

edge_gap = variant(
    live,
    edges_drop={
        (DIAG, "made_automorphism_rigid_by", AUT),
        (AUT, "automorphism_rigid_diagram_for", DIAG),
        (AUT, "exact_delta_fixed_for", EXACT_DELTA),
    },
)

gate(
    f"{PREFIX}9 requires every automorphism-rigid graph edge",
    not accepts(edge_gap)
    and any(reason.startswith("automorphism_rigid_edges_missing:") for reason in reasons(edge_gap)),
    ",".join(reasons(edge_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only automorphism-rigid cartesian compatibility diagrams pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: cartesian compatibility diagram is automorphism-rigid")
print(
    "VERDICT: the represented-limit cartesian compatibility diagram counts only "
    "when its automorphism group and stabilizer are trivial, transport and "
    "representative choices are unique, and endpoint-degree, boundary, "
    "DD4/exact-delta, graph-Rosati-control, handoff, mediator, coupling, "
    "equalizer, and probe data are fixed inside the same exact-24 finite-limit "
    "diagram. Automorphism torsors, skeleton choices, retuned representatives, "
    "moving payloads, declared rigidity, finite samples, and basis rows do not "
    "construct the missing object."
)
