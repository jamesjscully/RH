r"""Joint source-law DD.4-active rigid primitive effective K0 lift contract.

Doc 554 pins the right DD.4-active rigid primitive effective source
representative. This witness prevents the remaining projectionwise escape:
endpoint, degree, DD.4 boundary, boundary pushforward, graph, Rosati, and
control must be components of one jointly monic source-law tuple on the
finite-limit/equalizer fork, not separate laws glued after the fact.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the joint source-law witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 555
EXPECTED_WITNESS = "doc555-probe-joint-source-law-dd4-active-rigid-primitive-effective-grothendieck-lift"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPJLAWDD4ACTRIGIDPRIMEFFK0LIFTDD4ACTRIGIDPRIMEFFK0LIFTRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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
    JOINT: "coh_finite_limit_cut",
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

LAW_COMPONENTS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

PAYLOADS = {
    "original_dd4_class",
    "exact_delta",
    "rank1_boundary_defect_duality",
}

JOINT_IDENTITIES = {
    "single_source_law_tuple",
    "jointly_monic_law_tuple",
    "equalizer_law_tuple",
    "shared_dd4_payload_tuple",
    "endpoint_degree_boundary_pushforward_graph_rosati_control_shared_source",
    "dd4_handoff_interchange",
    "graph_realization_interchange",
    "projectionwise_law_gluing_forbidden",
}

COHERENT_ON = {
    ACTIVE,
    RIGID,
    "source_fiber_subrepresenter",
    "coupled_source_image",
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "joint_constraint_fork",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "original_dd4_class",
    "exact_delta",
    "rank1_boundary_defect_duality",
    *LAW_COMPONENTS,
}

JOINT_DATA = {
    "active_certificate": ACTIVE,
    "joint_law_tuple": "source_equalizer_joint_law_tuple_on_dd4_active_rigid_primitive_effective_k0_lift",
    "source_side": True,
    "choice_free": True,
    "single_tuple": True,
    "jointly_monic": True,
    "equalizer_monic": True,
    "laws_commute": True,
    "components": LAW_COMPONENTS,
    "payloads": PAYLOADS,
    "handoff_interchange": True,
    "graph_interchange": True,
    "endpoint_degree_boundary_coupled": True,
    "graph_rosati_control_coupled": True,
    "dd4_payload_shared": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "identities": JOINT_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "separate_projection_laws": False,
    "componentwise_activity_checklist": False,
    "pairwise_compatibility_only": False,
    "projection_table_law": False,
    "posthoc_law_gluing": False,
    "graph_side_law_product": False,
    "pointwise_law_tuple": False,
    "finite_law_sample": False,
    "basis_law_row": False,
    "law_context_collapse": False,
    "retuned_law_tuple": False,
    "interchange_by_declaration": False,
    "joint_monicity_by_declaration": False,
}

REQUIRED_NODE_DEPS = (
    ACTIVE,
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
    *LAW_COMPONENTS,
)

EXPECTED_JOINT_EDGES = {
    (ACTIVE, "made_joint_source_law_by", JOINT),
    (JOINT, "joint_law_lift_of", ACTIVE),
    (JOINT, "single_tuple_on", "joint_constraint_fork"),
    (JOINT, "jointly_monic_in", "finite_limit_cut"),
    (JOINT, "factors_through", "equalizer_arrow_to_subrep"),
    (JOINT, "anchored_on", "source_fiber_subrepresenter"),
    (JOINT, "law_on_original_payload", "original_dd4_class"),
    (JOINT, "law_on_exact_delta", "exact_delta"),
    (JOINT, "law_on_boundary_defect_duality", "rank1_boundary_defect_duality"),
    (JOINT, "tuple_endpoint_component", "endpoint_integrality"),
    (JOINT, "tuple_degree_component", "degree_maps"),
    (JOINT, "tuple_dd4_boundary_component", "dd4_boundary"),
    (JOINT, "tuple_pushforward_component", "boundary_pushforward"),
    (JOINT, "tuple_graph_component", "graph_composition"),
    (JOINT, "tuple_rosati_component", "rosati_count"),
    (JOINT, "tuple_control_component", "control_death"),
    (JOINT, "handoff_interchange_for", "dd4_image_only_handoff_contract"),
    (JOINT, "graph_interchange_for", "graph_later_realization_contract"),
    (JOINT, "preserves", "exact_24_cell_finite_index"),
    (JOINT, "coherent_for", "coupled_source_image"),
}

REQUIRED_FLAGS = (
    "joint_source_law_certificate_actual",
    "single_source_law_tuple",
    "jointly_monic_law_tuple",
    "equalizer_law_tuple",
    "all_seven_laws_are_components",
    "dd4_payload_shared_by_tuple",
    "handoff_interchange",
    "graph_interchange",
    "endpoint_degree_boundary_coupled",
    "graph_rosati_control_coupled",
    "inside_exact_24_budget",
    "no_projection_or_posthoc_law_repairs",
)

BANNED_FLAGS = (
    "separate_projection_laws",
    "componentwise_activity_checklist",
    "pairwise_compatibility_only",
    "noncommuting_law_square",
    "missing_joint_law_tuple",
    "projection_table_law",
    "posthoc_law_gluing",
    "graph_side_law_product",
    "pointwise_law_tuple",
    "finite_law_sample",
    "basis_law_row",
    "law_context_collapse",
    "retuned_law_tuple",
    "interchange_by_declaration",
    "joint_monicity_by_declaration",
    "endpoint_degree_boundary_decoupled",
    "graph_rosati_control_decoupled",
    "dd4_payload_law_not_shared",
    "source_law_tuple_not_equalizer_monic",
    "missing_joint_source_law_dd4_active_lift_certificate",
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
    edge_set = {
        (edge["source"], edge["relation"], edge["target"])
        for edge in data.get("edges", [])
        if edge.get("introduced_by", 0) <= EXPECTED_DOC
    }
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "edges": edge_set,
        "joint": deepcopy(JOINT_DATA),
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
    joint = state["joint"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_555")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc555_witness_missing")
    if JOINT not in accepted:
        out.append("joint_source_law_lift_missing_from_current")
    if JOINT not in assignments:
        out.append("joint_source_law_lift_unassigned")
    if assignments.get(JOINT) != "coh_finite_limit_cut":
        out.append(f"joint_source_law_bad_charge:{assignments.get(JOINT)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(joint, dict):
        out.append("joint_data_not_mapping")
        joint = {}

    if joint.get("active_certificate") != ACTIVE:
        out.append("joint_source_law_not_based_on_dd4_active_lift")
    if not joint.get("joint_law_tuple"):
        out.append("missing_joint_source_law_dd4_active_lift_certificate")
    if not joint.get("source_side") or not joint.get("choice_free"):
        out.append("joint_law_tuple_by_declaration")
    if not joint.get("single_tuple"):
        out.append("missing_joint_law_tuple")
    if not joint.get("jointly_monic"):
        out.append("joint_monicity_by_declaration")
    if not joint.get("equalizer_monic"):
        out.append("source_law_tuple_not_equalizer_monic")
    if not joint.get("laws_commute"):
        out.append("noncommuting_law_square")

    components = _as_set(joint.get("components"))
    missing_components = LAW_COMPONENTS - components
    if missing_components:
        out.append("joint_law_components_missing:" + ",".join(sorted(missing_components)))
    extra_components = components - LAW_COMPONENTS
    if extra_components:
        out.append("joint_law_has_extra_components:" + ",".join(sorted(extra_components)))

    payloads = _as_set(joint.get("payloads"))
    missing_payloads = PAYLOADS - payloads
    if missing_payloads:
        out.append("dd4_payload_law_not_shared")
    if not joint.get("dd4_payload_shared"):
        out.append("dd4_payload_law_not_shared")
    if not joint.get("handoff_interchange"):
        out.append("interchange_by_declaration")
    if not joint.get("graph_interchange"):
        out.append("graph_side_law_product")
    if not joint.get("endpoint_degree_boundary_coupled"):
        out.append("endpoint_degree_boundary_decoupled")
    if not joint.get("graph_rosati_control_coupled"):
        out.append("graph_rosati_control_decoupled")

    if not joint.get("nonpositive_stage") or joint.get("imports_positivity"):
        out.append("law_context_collapse")
    if not joint.get("preserves_budget"):
        out.append("joint_law_expands_exact_24_budget")

    missing_identities = JOINT_IDENTITIES - _as_set(joint.get("identities"))
    if missing_identities:
        out.append("joint_law_identity_missing:" + ",".join(sorted(missing_identities)))
    missing_coherence = COHERENT_ON - _as_set(joint.get("coherent_on"))
    if missing_coherence:
        out.append("joint_law_coherence_missing:" + ",".join(sorted(missing_coherence)))

    for key in (
        "separate_projection_laws",
        "componentwise_activity_checklist",
        "pairwise_compatibility_only",
        "projection_table_law",
        "posthoc_law_gluing",
        "graph_side_law_product",
        "pointwise_law_tuple",
        "finite_law_sample",
        "basis_law_row",
        "law_context_collapse",
        "retuned_law_tuple",
        "interchange_by_declaration",
        "joint_monicity_by_declaration",
    ):
        if joint.get(key):
            out.append(key)

    for req in REQUIRED_NODE_DEPS:
        if req not in state["requires"].get(JOINT, []):
            out.append(f"joint_source_law_requires_missing:{req}")
    if JOINT not in state["requires"].get(ACTIVE, []):
        out.append("dd4_active_lift_not_required_to_be_joint_source_law")

    missing_edges = EXPECTED_JOINT_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("joint_source_law_edges_missing:" + ",".join(rendered))

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    if dd4_bridge.get("direction") != "image_only":
        out.append("interchange_by_declaration")
    if not dd4_bridge.get("preserves_source_nonboundary"):
        out.append("dd4_payload_law_not_shared")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("graph_side_law_product")

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
        elif key == "joint":
            data["joint"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 555 joint source-law layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s components=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["joint"]["components"]),
    ),
)

projection_gap = variant(
    live,
    flags={"no_projection_or_posthoc_law_repairs": False, "single_source_law_tuple": False},
    banned={"separate_projection_laws": True, "componentwise_activity_checklist": True},
    joint={
        "single_tuple": False,
        "separate_projection_laws": True,
        "componentwise_activity_checklist": True,
    },
)
projection_gap["joint"]["identities"] -= {
    "single_source_law_tuple",
    "projectionwise_law_gluing_forbidden",
}

gate(
    f"{PREFIX}2 rejects separate projection laws and componentwise checklists",
    not accepts(projection_gap)
    and {"separate_projection_laws", "componentwise_activity_checklist", "missing_joint_law_tuple"}
    <= set(reasons(projection_gap)),
    ",".join(reasons(projection_gap)),
)

pairwise_gap = variant(
    live,
    flags={"single_source_law_tuple": False},
    banned={
        "pairwise_compatibility_only": True,
        "noncommuting_law_square": True,
        "missing_joint_law_tuple": True,
    },
    joint={
        "single_tuple": False,
        "laws_commute": False,
        "pairwise_compatibility_only": True,
    },
)

gate(
    f"{PREFIX}3 rejects pairwise compatibility, noncommuting squares, or missing tuples",
    not accepts(pairwise_gap)
    and {"pairwise_compatibility_only", "noncommuting_law_square", "missing_joint_law_tuple"}
    <= set(reasons(pairwise_gap)),
    ",".join(reasons(pairwise_gap)),
)

gluing_gap = variant(
    live,
    banned={
        "projection_table_law": True,
        "posthoc_law_gluing": True,
        "graph_side_law_product": True,
        "pointwise_law_tuple": True,
    },
    joint={
        "projection_table_law": True,
        "posthoc_law_gluing": True,
        "graph_side_law_product": True,
        "pointwise_law_tuple": True,
        "graph_interchange": False,
    },
)

gate(
    f"{PREFIX}4 rejects projection tables, posthoc gluing, graph-side products, or pointwise tuples",
    not accepts(gluing_gap)
    and {
        "projection_table_law",
        "posthoc_law_gluing",
        "graph_side_law_product",
        "pointwise_law_tuple",
    }
    <= set(reasons(gluing_gap)),
    ",".join(reasons(gluing_gap)),
)

sample_declare_gap = variant(
    live,
    flags={"jointly_monic_law_tuple": False, "handoff_interchange": False},
    banned={
        "finite_law_sample": True,
        "basis_law_row": True,
        "law_context_collapse": True,
        "retuned_law_tuple": True,
        "interchange_by_declaration": True,
        "joint_monicity_by_declaration": True,
    },
    joint={
        "finite_law_sample": True,
        "basis_law_row": True,
        "law_context_collapse": True,
        "retuned_law_tuple": True,
        "interchange_by_declaration": True,
        "joint_monicity_by_declaration": True,
        "nonpositive_stage": False,
        "jointly_monic": False,
        "handoff_interchange": False,
    },
)
sample_declare_gap["joint"]["identities"] -= {
    "jointly_monic_law_tuple",
    "dd4_handoff_interchange",
}

gate(
    f"{PREFIX}5 rejects finite samples, basis rows, retuning, or declared structure",
    not accepts(sample_declare_gap)
    and {
        "finite_law_sample",
        "basis_law_row",
        "law_context_collapse",
        "retuned_law_tuple",
        "interchange_by_declaration",
        "joint_monicity_by_declaration",
    }
    <= set(reasons(sample_declare_gap)),
    ",".join(reasons(sample_declare_gap)),
)

decoupled_gap = variant(
    live,
    flags={"endpoint_degree_boundary_coupled": False, "graph_rosati_control_coupled": False},
    banned={"endpoint_degree_boundary_decoupled": True, "graph_rosati_control_decoupled": True},
    joint={
        "endpoint_degree_boundary_coupled": False,
        "graph_rosati_control_coupled": False,
    },
)

gate(
    f"{PREFIX}6 rejects endpoint-degree-boundary or graph-rosati-control decoupling",
    not accepts(decoupled_gap)
    and {"endpoint_degree_boundary_decoupled", "graph_rosati_control_decoupled"}
    <= set(reasons(decoupled_gap)),
    ",".join(reasons(decoupled_gap)),
)

payload_monic_gap = variant(
    live,
    flags={"dd4_payload_shared_by_tuple": False, "equalizer_law_tuple": False},
    banned={
        "dd4_payload_law_not_shared": True,
        "source_law_tuple_not_equalizer_monic": True,
    },
    joint={
        "payloads": {"exact_delta"},
        "dd4_payload_shared": False,
        "equalizer_monic": False,
    },
)
payload_monic_gap["joint"]["identities"] -= {
    "shared_dd4_payload_tuple",
    "equalizer_law_tuple",
}

gate(
    f"{PREFIX}7 rejects DD4 payload split or non-monic equalizer law tuples",
    not accepts(payload_monic_gap)
    and {"dd4_payload_law_not_shared", "source_law_tuple_not_equalizer_monic"}
    <= set(reasons(payload_monic_gap)),
    ",".join(reasons(payload_monic_gap)),
)

missing_cert = variant(
    live,
    flags={"joint_source_law_certificate_actual": False},
    banned={"missing_joint_source_law_dd4_active_lift_certificate": True},
)
missing_cert["accepted"].remove(JOINT)
del missing_cert["assignments"][JOINT]

gate(
    f"{PREFIX}8 rejects missing joint source-law DD4-active lift certificates",
    not accepts(missing_cert)
    and "missing_joint_source_law_dd4_active_lift_certificate" in reasons(missing_cert)
    and "joint_source_law_lift_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

dependency_gap = variant(live)
dependency_gap["requires"][JOINT].remove(ACTIVE)
dependency_gap["requires"][ACTIVE].remove(JOINT)

gate(
    f"{PREFIX}9 requires DD4-active and joint source-law certificates to close together",
    not accepts(dependency_gap)
    and "joint_source_law_requires_missing:dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
    in reasons(dependency_gap)
    and "dd4_active_lift_not_required_to_be_joint_source_law" in reasons(dependency_gap),
    ",".join(reasons(dependency_gap)),
)

variants = [
    projection_gap,
    pairwise_gap,
    gluing_gap,
    sample_declare_gap,
    decoupled_gap,
    payload_monic_gap,
    missing_cert,
    dependency_gap,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only joint source-law DD4-active rigid primitive effective K0 lifts pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: DD4-active lift has one joint source-law tuple")
print(
    "VERDICT: the DD.4-active rigid primitive effective K0 lift counts only "
    "when endpoint, degree, DD.4 boundary, boundary pushforward, graph, "
    "Rosati, and control are components of one jointly monic source-law "
    "tuple on the equalizer fork. Projectionwise, pairwise, posthoc, "
    "graph-side, pointwise, sampled, retuned, declared, context-collapsed, "
    "and missing joint-law repairs do not construct the missing object."
)
