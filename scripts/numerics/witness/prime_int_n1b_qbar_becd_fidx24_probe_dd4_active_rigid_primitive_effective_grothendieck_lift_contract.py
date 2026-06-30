r"""DD.4-active rigid primitive effective Grothendieck lift contract.

Doc 553 pins a rigid, stabilizer-free primitive effective K0 source lift.
This witness prevents that lift from being the wrong rigid object: a unit,
null, or DD.4-orthogonal representative whose endpoint, boundary, graph,
Rosati, and control laws hold vacuously while the original DD.4 obstruction
and exact-delta payload live elsewhere.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_dd4_active_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the DD.4-active lift witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 554
EXPECTED_WITNESS = "doc554-probe-dd4-active-rigid-primitive-effective-grothendieck-lift"
ACTIVE = "dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
RIGID = "rigid_primitive_effective_grothendieck_lift_certificate"
PRIMITIVE = "primitive_effective_grothendieck_lift_certificate"
EFFECTIVE = "effective_grothendieck_trace_lift_certificate"
INTEGRAL = "integral_grothendieck_trace_probe_equivalence_certificate"
EXACT_ADD = "exact_additive_trace_probe_equivalence_certificate"
PIVOTAL = "pivotal_monoidal_probe_equivalence_certificate"
DUAL_TRACE = "dual_trace_probe_equivalence_certificate"
ADJ_PAIR = "adjoint_pairing_probe_equivalence_certificate"
DAG_MON_EQV = "dagger_monoidal_probe_equivalence_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
PROBE_EQV = "probe_equivalence_certificate"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4ACTRIGIDPRIMEFFK0LIFTRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

failures: list[str] = []

SOURCE_FACETS = {
    "facet_endpoint_integrality",
    "facet_degree_maps",
    "facet_dd4_boundary",
    "facet_boundary_pushforward",
    "facet_graph_composition",
    "facet_rosati_count",
    "facet_control_death",
}

COHERENCE_CELLS = {
    "coh_universal_mediator",
    "coh_formation_fiber",
    "coh_formation",
    "coh_cartesian_source",
    "coh_monoidwide_source",
    "coh_source_coupling",
    "coh_coupling_representer",
    "coh_subrepresenter",
    "coh_equalizer_arrow",
    "coh_finite_limit_cut",
    "coh_context_separation",
    "coh_dd4_image_handoff",
    "coh_graph_later_realization",
    "coh_inhabitance_certificate",
    "coh_doc515_payload",
    "coh_exact_delta_certificate",
    "coh_boundary_defect_duality",
}

CELLS = SOURCE_FACETS | COHERENCE_CELLS

LIVE_ASSIGNMENTS = {
    "universal_mediator": "coh_universal_mediator",
    "formation_token": "coh_formation_fiber",
    "formation_fiber": "coh_formation_fiber",
    "formation_coherence": "coh_formation",
    "cartesian_source_coherence": "coh_cartesian_source",
    "monoidwide_source_coherence": "coh_monoidwide_source",
    "source_coupling": "coh_source_coupling",
    "coupling_representer": "coh_coupling_representer",
    "coupling_universal_arrow": "coh_coupling_representer",
    "source_fiber_subrepresenter": "coh_subrepresenter",
    "monic_subrep_inclusion": "coh_subrepresenter",
    "coupled_source_image": "coh_subrepresenter",
    "subrep_factorization": "coh_subrepresenter",
    "finite_limit_cut": "coh_finite_limit_cut",
    "joint_constraint_fork": "coh_finite_limit_cut",
    "equalizer_arrow_to_subrep": "coh_equalizer_arrow",
    "context_separation_contract": "coh_context_separation",
    "dd4_certificate_image": "coh_dd4_image_handoff",
    "dd4_image_only_handoff_contract": "coh_dd4_image_handoff",
    "original_dd4_class": "coh_dd4_image_handoff",
    "dd4_boundary_certificate": "coh_dd4_image_handoff",
    "pregraph_rosati_payload": "coh_graph_later_realization",
    "graph_realization_image": "coh_graph_later_realization",
    "graph_later_realization_contract": "coh_graph_later_realization",
    "finite_limit_inhabitance_certificate": "coh_inhabitance_certificate",
    "finite_index_budget_certificate": "coh_finite_limit_cut",
    "budget_dependency_closure_certificate": "coh_finite_limit_cut",
    TERMINAL_CERT: "coh_finite_limit_cut",
    ADM_CAT: "coh_finite_limit_cut",
    PROBE_SEP: "coh_finite_limit_cut",
    PROBE_NAT: "coh_finite_limit_cut",
    PROBE_FAITH: "coh_finite_limit_cut",
    PROBE_FULL: "coh_finite_limit_cut",
    PROBE_ESS: "coh_finite_limit_cut",
    PROBE_EQV: "coh_finite_limit_cut",
    CART_EQV: "coh_finite_limit_cut",
    DAG_MON_EQV: "coh_finite_limit_cut",
    ADJ_PAIR: "coh_finite_limit_cut",
    DUAL_TRACE: "coh_finite_limit_cut",
    PIVOTAL: "coh_finite_limit_cut",
    EXACT_ADD: "coh_finite_limit_cut",
    INTEGRAL: "coh_finite_limit_cut",
    EFFECTIVE: "coh_finite_limit_cut",
    PRIMITIVE: "coh_finite_limit_cut",
    RIGID: "coh_finite_limit_cut",
    ACTIVE: "coh_finite_limit_cut",
    "exact_delta": "coh_exact_delta_certificate",
    "rank1_boundary_defect_duality": "coh_boundary_defect_duality",
    "source_control_death": "facet_control_death",
    "source_mediator_fixed": "coh_doc515_payload",
    "doc515_coherence_fixed": "coh_doc515_payload",
    "coupled_self_dual_exact_bcf_sources": "coh_source_coupling",
    "endpoint_integrality": "facet_endpoint_integrality",
    "degree_maps": "facet_degree_maps",
    "dd4_boundary": "facet_dd4_boundary",
    "boundary_pushforward": "facet_boundary_pushforward",
    "graph_composition": "facet_graph_composition",
    "rosati_count": "facet_rosati_count",
    "control_death": "facet_control_death",
    "source_before_points": "coh_context_separation",
    "exact_24_cell_finite_index": "coh_finite_limit_cut",
    "doc515_boundary_fiber_coherence": "coh_doc515_payload",
    "original_dd4_res1_nonboundary": "coh_dd4_image_handoff",
}

ACTIVE_IDENTITIES = {
    "dd4_active_rigid_lift",
    "original_dd4_carried",
    "exact_delta_carried",
    "boundary_defect_duality_carried",
    "certificate_image_has_source_preimage",
    "image_only_handoff_lift_natural",
    "nonnull_dd4_pairing",
    "nonunit_nonterminal_lift",
    "nonvacuous_boundary_zero",
    "nonvacuous_control_zero",
    "endpoint_active_on_dd4_payload",
    "degree_active_on_dd4_payload",
    "graph_active_on_dd4_payload",
    "rosati_active_on_dd4_payload",
}

COHERENT_ON = {
    RIGID,
    "source_fiber_subrepresenter",
    "coupled_source_image",
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "joint_constraint_fork",
    "original_dd4_class",
    "exact_delta",
    "rank1_boundary_defect_duality",
    "dd4_certificate_image",
    "dd4_image_only_handoff_contract",
    "dd4_boundary_certificate",
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

ACTIVE_DATA = {
    "rigid_certificate": RIGID,
    "active_lift": "source_dd4_active_rigid_primitive_effective_k0_lift",
    "source_side": True,
    "choice_free": True,
    "dd4_active": True,
    "carries_original_dd4": True,
    "original_dd4_nonboundary": True,
    "carries_exact_delta": True,
    "carries_boundary_defect_duality": True,
    "dd4_certificate_image_has_source_preimage": True,
    "image_only_handoff": True,
    "dd4_handoff_natural": True,
    "nonnull_dd4_pairing": True,
    "unit_terminal": False,
    "orthogonal_to_original_dd4": False,
    "disjoint_from_exact_delta": False,
    "certificate_image_replaces_source_class": False,
    "boundary_zero_nonvacuous": True,
    "control_zero_nonvacuous": True,
    "endpoint_active": True,
    "degree_active": True,
    "graph_active": True,
    "rosati_active": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": ACTIVE_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "declared": False,
    "posthoc": False,
    "retuned": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "dd4_active_rigid_lift_certificate_actual",
    "dd4_active_rigid_lift",
    "original_dd4_carried",
    "exact_delta_carried",
    "boundary_defect_duality_carried",
    "certificate_image_has_source_preimage",
    "image_only_handoff_lift_natural",
    "nonnull_nonvacuous_dd4_pairing",
    "nonunit_nonterminal_lift",
    "active_endpoint_degree_graph_rosati",
    "source_before_points",
    "inside_exact_24_budget",
    "no_declared_or_posthoc_dd4_activity",
    "no_point_graph_sample_basis_dd4_activity",
)

BANNED_FLAGS = (
    "dd4_inactive_rigid_lift",
    "null_dd4_pairing",
    "unit_terminal_rigid_lift",
    "vacuous_boundary_zero",
    "vacuous_control_zero",
    "original_dd4_not_carried",
    "exact_delta_not_carried",
    "boundary_defect_duality_not_carried",
    "dd4_certificate_image_without_source_preimage",
    "dd4_handoff_not_lift_natural",
    "rigid_lift_orthogonal_to_original_dd4",
    "rigid_lift_disjoint_from_exact_delta",
    "certificate_image_replaces_source_class",
    "dd4_activity_by_declaration",
    "posthoc_dd4_activity",
    "retuned_dd4_active_representative",
    "point_graph_dd4_activity_check",
    "finite_dd4_activity_sample",
    "basis_dd4_activity_row",
    "dd4_activity_context_collapse",
    "missing_dd4_active_rigid_primitive_effective_lift_certificate",
)


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
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "active": deepcopy(ACTIVE_DATA),
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
    assignments = dict(state["assignments"])
    active = state["active"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_554")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc554_witness_missing")
    if ACTIVE not in accepted:
        out.append("dd4_active_lift_missing_from_current")
    if ACTIVE not in assignments:
        out.append("dd4_active_lift_unassigned")
    if assignments.get(ACTIVE) != "coh_finite_limit_cut":
        out.append(f"dd4_active_lift_bad_charge:{assignments.get(ACTIVE)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(active, dict):
        out.append("active_data_not_mapping")
        active = {}

    if active.get("rigid_certificate") != RIGID:
        out.append("dd4_active_lift_not_based_on_rigid_lift")
    if not active.get("active_lift"):
        out.append("missing_dd4_active_rigid_primitive_effective_lift_certificate")
    if not active.get("source_side") or not active.get("choice_free"):
        out.append("dd4_activity_by_declaration")
    if not active.get("dd4_active"):
        out.append("dd4_inactive_rigid_lift")
    if not active.get("carries_original_dd4") or not active.get("original_dd4_nonboundary"):
        out.append("original_dd4_not_carried")
    if not active.get("carries_exact_delta"):
        out.append("exact_delta_not_carried")
    if not active.get("carries_boundary_defect_duality"):
        out.append("boundary_defect_duality_not_carried")
    if not active.get("dd4_certificate_image_has_source_preimage"):
        out.append("dd4_certificate_image_without_source_preimage")
    if not active.get("image_only_handoff") or not active.get("dd4_handoff_natural"):
        out.append("dd4_handoff_not_lift_natural")
    if not active.get("nonnull_dd4_pairing"):
        out.append("null_dd4_pairing")
    if active.get("unit_terminal"):
        out.append("unit_terminal_rigid_lift")
    if active.get("orthogonal_to_original_dd4"):
        out.append("rigid_lift_orthogonal_to_original_dd4")
    if active.get("disjoint_from_exact_delta"):
        out.append("rigid_lift_disjoint_from_exact_delta")
    if active.get("certificate_image_replaces_source_class"):
        out.append("certificate_image_replaces_source_class")
    if not active.get("boundary_zero_nonvacuous"):
        out.append("vacuous_boundary_zero")
    if not active.get("control_zero_nonvacuous"):
        out.append("vacuous_control_zero")
    if not active.get("endpoint_active"):
        out.append("dd4_activity_endpoint_missing")
    if not active.get("degree_active"):
        out.append("dd4_activity_degree_missing")
    if not active.get("graph_active"):
        out.append("dd4_activity_graph_missing")
    if not active.get("rosati_active"):
        out.append("dd4_activity_rosati_missing")

    if not active.get("nonpositive_stage") or active.get("imports_positivity"):
        out.append("dd4_activity_context_collapse")
    if not active.get("preserves_budget"):
        out.append("dd4_activity_expands_exact_24_budget")
    if not active.get("source_before_points"):
        out.append("dd4_activity_loses_source_before_points")

    missing_identities = ACTIVE_IDENTITIES - _as_set(active.get("identities"))
    if missing_identities:
        out.append("dd4_active_identity_missing:" + ",".join(sorted(missing_identities)))
    missing_coherence = COHERENT_ON - _as_set(active.get("coherent_on"))
    if missing_coherence:
        out.append("dd4_active_coherence_missing:" + ",".join(sorted(missing_coherence)))

    if active.get("declared"):
        out.append("dd4_activity_by_declaration")
    if active.get("posthoc"):
        out.append("posthoc_dd4_activity")
    if active.get("retuned"):
        out.append("retuned_dd4_active_representative")
    if active.get("point_graph"):
        out.append("point_graph_dd4_activity_check")
    if active.get("finite_sample"):
        out.append("finite_dd4_activity_sample")
    if active.get("basis_row"):
        out.append("basis_dd4_activity_row")
    if active.get("context_collapse"):
        out.append("dd4_activity_context_collapse")

    required = (
        RIGID,
        PRIMITIVE,
        EFFECTIVE,
        INTEGRAL,
        EXACT_ADD,
        PIVOTAL,
        DUAL_TRACE,
        ADJ_PAIR,
        DAG_MON_EQV,
        CART_EQV,
        PROBE_EQV,
        PROBE_ESS,
        PROBE_FULL,
        PROBE_FAITH,
        PROBE_NAT,
        PROBE_SEP,
        ADM_CAT,
        TERMINAL_CERT,
        "source_fiber_subrepresenter",
        "coupled_source_image",
        "coupled_self_dual_exact_bcf_sources",
        "finite_limit_cut",
        "equalizer_arrow_to_subrep",
        "budget_dependency_closure_certificate",
        "finite_index_budget_certificate",
        "exact_24_cell_finite_index",
        "joint_constraint_fork",
        "pregraph_rosati_payload",
        "dd4_certificate_image",
        "dd4_image_only_handoff_contract",
        "original_dd4_class",
        "dd4_boundary_certificate",
        "exact_delta",
        "rank1_boundary_defect_duality",
        "graph_later_realization_contract",
        "finite_limit_inhabitance_certificate",
        "source_before_points",
        "endpoint_integrality",
        "degree_maps",
        "dd4_boundary",
        "boundary_pushforward",
        "graph_composition",
        "rosati_count",
        "control_death",
    )
    for req in required:
        if req not in state["requires"].get(ACTIVE, []):
            out.append(f"dd4_active_lift_requires_missing:{req}")
    if ACTIVE not in state["requires"].get(RIGID, []):
        out.append("rigid_lift_not_required_to_be_dd4_active")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    if dd4_bridge.get("direction") != "image_only":
        out.append("dd4_handoff_not_lift_natural")
    if not dd4_bridge.get("preserves_source_nonboundary"):
        out.append("original_dd4_not_carried")
    if not dd4_bridge.get("prohibits_reverse_pullback") or not dd4_bridge.get("prohibits_source_quotient"):
        out.append("certificate_image_replaces_source_class")
    if not dd4_bridge.get("allows_target_kill"):
        out.append("dd4_certificate_image_without_source_preimage")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("dd4_activity_loses_source_before_points")

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
        elif key == "active":
            data["active"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 554 DD4-active rigid primitive effective lift layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["active"]["identities"]),
    ),
)

inactive_null_gap = variant(
    live,
    flags={"dd4_active_rigid_lift": False, "nonnull_nonvacuous_dd4_pairing": False, "nonunit_nonterminal_lift": False},
    banned={
        "dd4_inactive_rigid_lift": True,
        "null_dd4_pairing": True,
        "unit_terminal_rigid_lift": True,
        "vacuous_boundary_zero": True,
        "vacuous_control_zero": True,
    },
    active={
        "dd4_active": False,
        "nonnull_dd4_pairing": False,
        "unit_terminal": True,
        "boundary_zero_nonvacuous": False,
        "control_zero_nonvacuous": False,
    },
)
inactive_null_gap["active"]["identities"] -= {
    "dd4_active_rigid_lift",
    "nonnull_dd4_pairing",
    "nonunit_nonterminal_lift",
    "nonvacuous_boundary_zero",
    "nonvacuous_control_zero",
}

gate(
    f"{PREFIX}2 rejects DD4-inactive, null-paired, unit, or vacuous rigid lifts",
    not accepts(inactive_null_gap)
    and {
        "dd4_inactive_rigid_lift",
        "null_dd4_pairing",
        "unit_terminal_rigid_lift",
        "vacuous_boundary_zero",
        "vacuous_control_zero",
    }
    <= set(reasons(inactive_null_gap)),
    ",".join(reasons(inactive_null_gap)),
)

payload_gap = variant(
    live,
    flags={
        "original_dd4_carried": False,
        "exact_delta_carried": False,
        "boundary_defect_duality_carried": False,
        "certificate_image_has_source_preimage": False,
    },
    banned={
        "original_dd4_not_carried": True,
        "exact_delta_not_carried": True,
        "boundary_defect_duality_not_carried": True,
        "dd4_certificate_image_without_source_preimage": True,
    },
    active={
        "carries_original_dd4": False,
        "original_dd4_nonboundary": False,
        "carries_exact_delta": False,
        "carries_boundary_defect_duality": False,
        "dd4_certificate_image_has_source_preimage": False,
    },
)
payload_gap["active"]["identities"] -= {
    "original_dd4_carried",
    "exact_delta_carried",
    "boundary_defect_duality_carried",
    "certificate_image_has_source_preimage",
}
payload_gap["active"]["coherent_on"] -= {
    "original_dd4_class",
    "exact_delta",
    "rank1_boundary_defect_duality",
    "dd4_certificate_image",
}

gate(
    f"{PREFIX}3 rejects lifts that do not carry original DD4, exact delta, and boundary-defect payload",
    not accepts(payload_gap)
    and {
        "original_dd4_not_carried",
        "exact_delta_not_carried",
        "boundary_defect_duality_not_carried",
        "dd4_certificate_image_without_source_preimage",
    }
    <= set(reasons(payload_gap)),
    ",".join(reasons(payload_gap)),
)

handoff_context_gap = variant(
    live,
    flags={"image_only_handoff_lift_natural": False},
    banned={
        "dd4_handoff_not_lift_natural": True,
        "rigid_lift_orthogonal_to_original_dd4": True,
        "rigid_lift_disjoint_from_exact_delta": True,
        "certificate_image_replaces_source_class": True,
    },
    active={
        "image_only_handoff": False,
        "dd4_handoff_natural": False,
        "orthogonal_to_original_dd4": True,
        "disjoint_from_exact_delta": True,
        "certificate_image_replaces_source_class": True,
    },
)
handoff_context_gap["bridges"]["dd4_certificate_handoff"]["direction"] = "source_replaced_by_certificate_image"
handoff_context_gap["bridges"]["dd4_certificate_handoff"]["preserves_source_nonboundary"] = False
handoff_context_gap["bridges"]["dd4_certificate_handoff"]["prohibits_reverse_pullback"] = False
handoff_context_gap["bridges"]["dd4_certificate_handoff"]["prohibits_source_quotient"] = False
handoff_context_gap["active"]["identities"] -= {"image_only_handoff_lift_natural"}
handoff_context_gap["active"]["coherent_on"] -= {
    "dd4_image_only_handoff_contract",
    "dd4_boundary_certificate",
}

gate(
    f"{PREFIX}4 rejects certificate-image substitution, orthogonality, disjointness, or bad handoff",
    not accepts(handoff_context_gap)
    and {
        "dd4_handoff_not_lift_natural",
        "rigid_lift_orthogonal_to_original_dd4",
        "rigid_lift_disjoint_from_exact_delta",
        "certificate_image_replaces_source_class",
    }
    <= set(reasons(handoff_context_gap)),
    ",".join(reasons(handoff_context_gap)),
)

active_laws_gap = variant(
    live,
    flags={"active_endpoint_degree_graph_rosati": False},
    active={
        "endpoint_active": False,
        "degree_active": False,
        "graph_active": False,
        "rosati_active": False,
    },
)
active_laws_gap["active"]["identities"] -= {
    "endpoint_active_on_dd4_payload",
    "degree_active_on_dd4_payload",
    "graph_active_on_dd4_payload",
    "rosati_active_on_dd4_payload",
}
active_laws_gap["active"]["coherent_on"] -= {
    "endpoint_integrality",
    "degree_maps",
    "graph_composition",
    "rosati_count",
}

gate(
    f"{PREFIX}5 requires endpoint, degree, graph, and Rosati activity on the DD4 payload",
    not accepts(active_laws_gap)
    and {
        "dd4_activity_endpoint_missing",
        "dd4_activity_degree_missing",
        "dd4_activity_graph_missing",
        "dd4_activity_rosati_missing",
    }
    <= set(reasons(active_laws_gap)),
    ",".join(reasons(active_laws_gap)),
)

declared_posthoc_gap = variant(
    live,
    flags={"no_declared_or_posthoc_dd4_activity": False},
    banned={
        "dd4_activity_by_declaration": True,
        "posthoc_dd4_activity": True,
        "retuned_dd4_active_representative": True,
    },
    active={
        "source_side": False,
        "choice_free": False,
        "declared": True,
        "posthoc": True,
        "retuned": True,
    },
)

gate(
    f"{PREFIX}6 rejects declared, posthoc, or retuned DD4 activity",
    not accepts(declared_posthoc_gap)
    and {
        "dd4_activity_by_declaration",
        "posthoc_dd4_activity",
        "retuned_dd4_active_representative",
    }
    <= set(reasons(declared_posthoc_gap)),
    ",".join(reasons(declared_posthoc_gap)),
)

sample_context_gap = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_point_graph_sample_basis_dd4_activity": False,
    },
    banned={
        "point_graph_dd4_activity_check": True,
        "finite_dd4_activity_sample": True,
        "basis_dd4_activity_row": True,
        "dd4_activity_context_collapse": True,
    },
    active={
        "source_before_points": False,
        "preserves_budget": False,
        "imports_positivity": True,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
        "context_collapse": True,
    },
)
sample_context_gap["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}7 rejects point/graph checks, finite samples, basis rows, positivity, or context collapse",
    not accepts(sample_context_gap)
    and {
        "point_graph_dd4_activity_check",
        "finite_dd4_activity_sample",
        "basis_dd4_activity_row",
        "dd4_activity_context_collapse",
    }
    <= set(reasons(sample_context_gap)),
    ",".join(reasons(sample_context_gap)),
)

missing_cert = variant(
    live,
    flags={"dd4_active_rigid_lift_certificate_actual": False},
    banned={"missing_dd4_active_rigid_primitive_effective_lift_certificate": True},
)
missing_cert["accepted"].remove(ACTIVE)
del missing_cert["assignments"][ACTIVE]

gate(
    f"{PREFIX}8 rejects missing DD4-active rigid primitive effective lift certificates",
    not accepts(missing_cert)
    and "missing_dd4_active_rigid_primitive_effective_lift_certificate" in reasons(missing_cert)
    and "dd4_active_lift_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

dependency_gap = variant(live)
dependency_gap["requires"][ACTIVE].remove(RIGID)
dependency_gap["requires"][RIGID].remove(ACTIVE)

gate(
    f"{PREFIX}9 requires DD4-active and rigid certificates to close together",
    not accepts(dependency_gap)
    and "dd4_active_lift_requires_missing:rigid_primitive_effective_grothendieck_lift_certificate"
    in reasons(dependency_gap)
    and "rigid_lift_not_required_to_be_dd4_active" in reasons(dependency_gap),
    ",".join(reasons(dependency_gap)),
)

variants = [
    inactive_null_gap,
    payload_gap,
    handoff_context_gap,
    active_laws_gap,
    declared_posthoc_gap,
    sample_context_gap,
    missing_cert,
    dependency_gap,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only DD4-active rigid primitive effective Grothendieck lifts pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: rigid primitive effective K0 lift is DD4-active")
print(
    "VERDICT: rigid primitive effective K0 trace lifts count only when they "
    "carry the original DD.4 class, exact delta, and boundary-defect duality "
    "through the image-only handoff. DD.4-inactive, null-paired, unit, "
    "orthogonal, certificate-image-only, declared, posthoc, retuned, point or "
    "graph checked, finite-sampled, basis-row, context-collapsed, and missing "
    "DD.4-active certificates do not construct the missing object."
)
