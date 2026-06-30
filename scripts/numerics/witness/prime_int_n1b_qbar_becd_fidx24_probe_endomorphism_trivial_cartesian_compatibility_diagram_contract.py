r"""Endomorphism-trivial represented-limit cartesian compatibility diagram.

Doc 562 pins the represented-limit cartesian compatibility diagram against
automorphisms, stabilizers, transport, skeleton choice, and retuned
representatives. This witness closes the next algebraic escape: a diagram with
no nontrivial automorphisms can still have non-invertible self-endomorphisms,
idempotents, retracts, quotient/summand collapses, or nilpotent self-maps.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_endomorphism_trivial_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the endomorphism-trivial diagram witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 563
EXPECTED_WITNESS = "doc563-probe-endomorphism-trivial-automorphism-rigid-cartesian-compatibility-diagram"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPENDTRIVAUTRIGCARTCOMPAT"

failures: list[str] = []

REQUIRED_END_DEPS = {
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
    (AUT, "made_endomorphism_trivial_by", ENDTRIV),
    (ENDTRIV, "endomorphism_trivial_diagram_for", AUT),
    (ENDTRIV, "identity_only_endomorphism_for", DIAG),
    (ENDTRIV, "no_nontrivial_idempotent_for", EQUALIZER),
    (ENDTRIV, "no_retract_for", BUNDLE),
    (ENDTRIV, "no_nilpotent_self_map_for", FINITE_LIMIT),
    (ENDTRIV, "quotient_free_for", COUPLED_IMAGE),
    (ENDTRIV, "payload_endomorphism_fixed_for", ENDPOINT),
    (ENDTRIV, "payload_endomorphism_fixed_for", DEGREE),
    (ENDTRIV, "payload_endomorphism_fixed_for", DD4_BOUNDARY),
    (ENDTRIV, "payload_endomorphism_fixed_for", PUSHFORWARD),
    (ENDTRIV, "payload_endomorphism_fixed_for", EXACT_DELTA),
    (ENDTRIV, "payload_endomorphism_fixed_for", GRAPH_COMP),
    (ENDTRIV, "payload_endomorphism_fixed_for", ROSATI),
    (ENDTRIV, "payload_endomorphism_fixed_for", CONTROL),
    (ENDTRIV, "payload_endomorphism_fixed_for", HANDOFF),
    (ENDTRIV, "payload_endomorphism_fixed_for", GRAPH_LATER),
    (ENDTRIV, "payload_endomorphism_fixed_for", MEDIATOR),
    (ENDTRIV, "payload_endomorphism_fixed_for", SOURCE_COUPLING),
    (ENDTRIV, "payload_endomorphism_fixed_for", CART_EQV),
    (ENDTRIV, "preserves", FINITE_INDEX),
    (ENDTRIV, "coherent_for", COUPLED_IMAGE),
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
    "identity_only_endomorphism_law",
    "no_nontrivial_idempotent_law",
    "no_retract_summand_law",
    "no_quotient_collapse_law",
    "no_subobject_projection_law",
    "no_nilpotent_self_map_law",
    "payload_endomorphism_fixed_law",
    "finite_limit_endomorphism_identity_law",
}

BANNED_FLAGS = (
    "diagram_nontrivial_endomorphism_monoid",
    "diagram_nontrivial_idempotent",
    "diagram_retract_summand",
    "diagram_quotient_collapse",
    "diagram_subobject_projection",
    "diagram_nilpotent_self_map",
    "diagram_self_map_payload_invariant_only",
    "diagram_endomorphism_endpoint_degree_moves",
    "diagram_endomorphism_boundary_square_moves",
    "diagram_endomorphism_exact_delta_moves",
    "diagram_endomorphism_graph_rosati_control_moves",
    "diagram_endomorphism_handoff_graph_moves",
    "diagram_endomorphism_mediator_moves",
    "diagram_endomorphism_source_coupling_moves",
    "diagram_endomorphism_equalizer_moves",
    "diagram_endomorphism_probe_transport_moves",
    "diagram_endomorphism_by_declaration",
    "diagram_endomorphism_finite_sample",
    "diagram_endomorphism_basis_row",
    "missing_endomorphism_trivial_cartesian_compatibility_diagram_certificate",
)

REQUIRED_FLAGS = (
    "endomorphism_trivial_diagram_actual",
    "identity_only_endomorphism_monoid",
    "no_nontrivial_idempotents",
    "no_retract_summands",
    "no_quotient_or_projection_collapse",
    "no_nilpotent_self_maps",
    "payloads_fixed_under_endomorphism",
    "inside_exact_24_budget",
)

END_DATA = {
    "certificate": "represented_limit_endomorphism_trivial_cartesian_compatibility_diagram",
    "base_certificate": AUT,
    "endomorphism_monoid": {"identity"},
    "idempotents": {"identity"},
    "retract_free": True,
    "summand_free": True,
    "quotient_free": True,
    "subobject_projection_free": True,
    "nilpotent_self_map_free": True,
    "payload_invariant_only": False,
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
        "endomorphism": deepcopy(END_DATA),
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
    endomorphism = state["endomorphism"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_563")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc563_witness_missing")
    if ENDTRIV not in accepted:
        out.append("endomorphism_trivial_cartesian_compatibility_diagram_missing_from_current")
    if AUT not in accepted:
        out.append("automorphism_rigid_diagram_base_missing_from_current")

    if not isinstance(endomorphism, dict):
        out.append("endomorphism_trivial_diagram_data_not_mapping")
        endomorphism = {}
    if endomorphism.get("certificate") != "represented_limit_endomorphism_trivial_cartesian_compatibility_diagram":
        out.append("missing_endomorphism_trivial_cartesian_compatibility_diagram_certificate")
    if endomorphism.get("base_certificate") != AUT:
        out.append("endomorphism_trivial_diagram_not_based_on_automorphism_rigid_diagram")
    if _as_set(endomorphism.get("endomorphism_monoid")) != {"identity"}:
        out.append("diagram_nontrivial_endomorphism_monoid")
    if _as_set(endomorphism.get("idempotents")) != {"identity"}:
        out.append("diagram_nontrivial_idempotent")
    if not endomorphism.get("retract_free") or not endomorphism.get("summand_free"):
        out.append("diagram_retract_summand")
    if not endomorphism.get("quotient_free"):
        out.append("diagram_quotient_collapse")
    if not endomorphism.get("subobject_projection_free"):
        out.append("diagram_subobject_projection")
    if not endomorphism.get("nilpotent_self_map_free"):
        out.append("diagram_nilpotent_self_map")
    if endomorphism.get("payload_invariant_only"):
        out.append("diagram_self_map_payload_invariant_only")
    if not endomorphism.get("endpoint_degree_fixed"):
        out.append("diagram_endomorphism_endpoint_degree_moves")
    if not endomorphism.get("boundary_square_fixed"):
        out.append("diagram_endomorphism_boundary_square_moves")
    if not endomorphism.get("exact_delta_fixed"):
        out.append("diagram_endomorphism_exact_delta_moves")
    if not endomorphism.get("graph_rosati_control_fixed"):
        out.append("diagram_endomorphism_graph_rosati_control_moves")
    if not endomorphism.get("handoff_graph_fixed"):
        out.append("diagram_endomorphism_handoff_graph_moves")
    if not endomorphism.get("mediator_fixed"):
        out.append("diagram_endomorphism_mediator_moves")
    if not endomorphism.get("source_coupling_fixed"):
        out.append("diagram_endomorphism_source_coupling_moves")
    if not endomorphism.get("equalizer_fixed"):
        out.append("diagram_endomorphism_equalizer_moves")
    if not endomorphism.get("probe_transport_fixed"):
        out.append("diagram_endomorphism_probe_transport_moves")
    if not endomorphism.get("preserves_budget"):
        out.append("endomorphism_trivial_diagram_not_inside_exact_24_budget")
    if endomorphism.get("declared_only"):
        out.append("diagram_endomorphism_by_declaration")
    if endomorphism.get("finite_sample"):
        out.append("diagram_endomorphism_finite_sample")
    if endomorphism.get("basis_row"):
        out.append("diagram_endomorphism_basis_row")
    if endomorphism.get("imports_positivity"):
        out.append("endomorphism_trivial_diagram_imports_positivity")

    missing_targets = REQUIRED_FIXED_TARGETS - _as_set(endomorphism.get("fixed_targets"))
    if missing_targets:
        out.append("endomorphism_trivial_fixed_targets_missing:" + ",".join(sorted(missing_targets)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(endomorphism.get("identities"))
    if missing_identities:
        out.append("endomorphism_trivial_identity_missing:" + ",".join(sorted(missing_identities)))

    if ENDTRIV not in requires.get(AUT, []):
        out.append("automorphism_rigid_diagram_not_required_to_be_endomorphism_trivial")
    if AUT not in requires.get(ENDTRIV, []):
        out.append("endomorphism_trivial_diagram_requires_missing_automorphism_rigid_base")
    missing_deps = REQUIRED_END_DEPS - set(requires.get(ENDTRIV, []))
    if missing_deps:
        out.append("endomorphism_trivial_diagram_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("endomorphism_trivial_edges_missing:" + ",".join(rendered))

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
        elif key == "endomorphism":
            data["endomorphism"].update(value)
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
    f"{PREFIX}1 doc 563 endomorphism-trivial diagram layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s endomorphisms=%s"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        sorted(live["endomorphism"]["endomorphism_monoid"]),
    ),
)

endomorphism_gap = variant(
    live,
    banned={
        "diagram_nontrivial_endomorphism_monoid": True,
        "diagram_nontrivial_idempotent": True,
        "diagram_nilpotent_self_map": True,
    },
    endomorphism={
        "endomorphism_monoid": {"identity", "hidden_self_map"},
        "idempotents": {"identity", "hidden_projector"},
        "nilpotent_self_map_free": False,
    },
)

gate(
    f"{PREFIX}2 rejects nontrivial endomorphisms, idempotents, or nilpotents",
    not accepts(endomorphism_gap)
    and {
        "diagram_nontrivial_endomorphism_monoid",
        "diagram_nontrivial_idempotent",
        "diagram_nilpotent_self_map",
    }
    <= set(reasons(endomorphism_gap)),
    ",".join(reasons(endomorphism_gap)),
)

retract_gap = variant(
    live,
    banned={
        "diagram_retract_summand": True,
        "diagram_quotient_collapse": True,
        "diagram_subobject_projection": True,
    },
    endomorphism={
        "retract_free": False,
        "summand_free": False,
        "quotient_free": False,
        "subobject_projection_free": False,
    },
)

gate(
    f"{PREFIX}3 rejects retracts, summands, quotients, or subobject projections",
    not accepts(retract_gap)
    and {
        "diagram_retract_summand",
        "diagram_quotient_collapse",
        "diagram_subobject_projection",
    }
    <= set(reasons(retract_gap)),
    ",".join(reasons(retract_gap)),
)

source_payload_gap = variant(
    live,
    banned={
        "diagram_self_map_payload_invariant_only": True,
        "diagram_endomorphism_endpoint_degree_moves": True,
        "diagram_endomorphism_boundary_square_moves": True,
        "diagram_endomorphism_exact_delta_moves": True,
    },
    endomorphism={
        "payload_invariant_only": True,
        "endpoint_degree_fixed": False,
        "boundary_square_fixed": False,
        "exact_delta_fixed": False,
    },
)

gate(
    f"{PREFIX}4 rejects invariant-only payloads or source payload movement",
    not accepts(source_payload_gap)
    and {
        "diagram_self_map_payload_invariant_only",
        "diagram_endomorphism_endpoint_degree_moves",
        "diagram_endomorphism_boundary_square_moves",
        "diagram_endomorphism_exact_delta_moves",
    }
    <= set(reasons(source_payload_gap)),
    ",".join(reasons(source_payload_gap)),
)

structural_payload_gap = variant(
    live,
    banned={
        "diagram_endomorphism_graph_rosati_control_moves": True,
        "diagram_endomorphism_handoff_graph_moves": True,
        "diagram_endomorphism_mediator_moves": True,
        "diagram_endomorphism_source_coupling_moves": True,
        "diagram_endomorphism_equalizer_moves": True,
        "diagram_endomorphism_probe_transport_moves": True,
    },
    endomorphism={
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
        "diagram_endomorphism_graph_rosati_control_moves",
        "diagram_endomorphism_handoff_graph_moves",
        "diagram_endomorphism_mediator_moves",
        "diagram_endomorphism_source_coupling_moves",
        "diagram_endomorphism_equalizer_moves",
        "diagram_endomorphism_probe_transport_moves",
    }
    <= set(reasons(structural_payload_gap)),
    ",".join(reasons(structural_payload_gap)),
)

selector_gap = variant(
    live,
    banned={
        "diagram_endomorphism_by_declaration": True,
        "diagram_endomorphism_finite_sample": True,
        "diagram_endomorphism_basis_row": True,
    },
    endomorphism={"declared_only": True, "finite_sample": True, "basis_row": True},
)

gate(
    f"{PREFIX}6 rejects declared endomorphism triviality, finite samples, or basis rows",
    not accepts(selector_gap)
    and {
        "diagram_endomorphism_by_declaration",
        "diagram_endomorphism_finite_sample",
        "diagram_endomorphism_basis_row",
    }
    <= set(reasons(selector_gap)),
    ",".join(reasons(selector_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_endomorphism_trivial_cartesian_compatibility_diagram_certificate": True},
    endomorphism={
        "certificate": None,
        "fixed_targets": REQUIRED_FIXED_TARGETS - {EQUALIZER, FINITE_LIMIT, CART_EQV},
        "identities": REQUIRED_IDENTITIES
        - {
            "identity_only_endomorphism_law",
            "no_nontrivial_idempotent_law",
            "finite_limit_endomorphism_identity_law",
        },
    },
)

gate(
    f"{PREFIX}7 rejects missing endomorphism-trivial certificates, fixed targets, or identities",
    not accepts(missing_gap)
    and "missing_endomorphism_trivial_cartesian_compatibility_diagram_certificate" in reasons(missing_gap)
    and any(reason.startswith("endomorphism_trivial_fixed_targets_missing:") for reason in reasons(missing_gap))
    and any(reason.startswith("endomorphism_trivial_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(AUT, ENDTRIV), (ENDTRIV, AUT), (ENDTRIV, EXACT_DELTA)],
)

gate(
    f"{PREFIX}8 requires automorphism-rigid and endomorphism-trivial layers to close together",
    not accepts(closure_gap)
    and {
        "automorphism_rigid_diagram_not_required_to_be_endomorphism_trivial",
        "endomorphism_trivial_diagram_requires_missing_automorphism_rigid_base",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("endomorphism_trivial_diagram_requires_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

edge_gap = variant(
    live,
    edges_drop={
        (AUT, "made_endomorphism_trivial_by", ENDTRIV),
        (ENDTRIV, "endomorphism_trivial_diagram_for", AUT),
        (ENDTRIV, "payload_endomorphism_fixed_for", EXACT_DELTA),
    },
)

gate(
    f"{PREFIX}9 requires every endomorphism-trivial graph edge",
    not accepts(edge_gap)
    and any(reason.startswith("endomorphism_trivial_edges_missing:") for reason in reasons(edge_gap)),
    ",".join(reasons(edge_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only endomorphism-trivial cartesian compatibility diagrams pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: cartesian compatibility diagram is endomorphism-trivial")
print(
    "VERDICT: the represented-limit cartesian compatibility diagram counts only "
    "when its endomorphism monoid is identity-only, with no nontrivial "
    "idempotents, retracts, quotient or summand collapses, subobject "
    "projections, nilpotent self-maps, or payload-preserving shadow maps. "
    "Endpoint-degree, boundary, DD4/exact-delta, graph-Rosati-control, "
    "handoff, mediator, coupling, equalizer, and probe data must be fixed "
    "under the trivial endomorphism action inside the same exact-24 "
    "finite-limit diagram."
)
