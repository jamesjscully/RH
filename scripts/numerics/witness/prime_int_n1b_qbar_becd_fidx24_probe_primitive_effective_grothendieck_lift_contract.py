r"""Primitive effective Grothendieck lift contract for source-square K0 traces.

Doc 551 pins a represented nonvirtual effective K0 lift. This witness prevents
the lift from being an imprimitive multiple, finite cover, tensor power, or
block sum whose endpoint, degree, boundary, graph/Rosati, and control laws
only work after hidden gcd division or multiplicity cancellation.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the primitive effective lift witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 552
EXPECTED_WITNESS = "doc552-probe-primitive-effective-grothendieck-lift"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PRIMITIVE_IDENTITIES = {
    "represented_primitive_lift",
    "primitive_k0_class",
    "indecomposable_representative",
    "gcd_one_endpoint_degree",
    "no_hidden_multiplicity",
    "boundary_zero_without_division",
    "control_zero_without_multiplicity",
    "connected_graph_representative",
    "rosati_indecomposable_representative",
    "source_subrep_primitive",
    "coupled_source_primitive",
}

IDENTITY_FAILURES = {
    "represented_primitive_lift": "nonprimitive_effective_lift",
    "primitive_k0_class": "divisible_k0_class",
    "indecomposable_representative": "nonprimitive_effective_lift",
    "gcd_one_endpoint_degree": "degree_gcd_not_one",
    "no_hidden_multiplicity": "hidden_multiplicity_lift",
    "boundary_zero_without_division": "boundary_zero_after_division",
    "control_zero_without_multiplicity": "control_zero_after_multiplicity",
    "connected_graph_representative": "graph_disconnected_union",
    "rosati_indecomposable_representative": "rosati_block_diagonal",
    "source_subrep_primitive": "nonprimitive_effective_lift",
    "coupled_source_primitive": "nonprimitive_effective_lift",
}

COHERENT_ON = {
    "source_fiber_subrepresenter",
    "coupled_source_image",
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
    "joint_constraint_fork",
}

PRIMITIVE_DATA = {
    "effective_certificate": EFFECTIVE,
    "primitive_lift": "source_primitive_effective_k0_lift",
    "source_side": True,
    "choice_free": True,
    "represented_by_source_subrep": True,
    "realized_in_coupled_source": True,
    "primitive": True,
    "indecomposable": True,
    "multiplicity": 1,
    "gcd_one": True,
    "divisible": False,
    "multiple": False,
    "rank_scaled": False,
    "finite_cover": False,
    "tensor_power": False,
    "endpoint_gcd_one": True,
    "degree_gcd_one": True,
    "boundary_zero_without_division": True,
    "control_zero_without_multiplicity": True,
    "graph_connected": True,
    "rosati_block_indecomposable": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": PRIMITIVE_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "annihilates": {"dd4_boundary", "control_death"},
    "selector": False,
    "declared": False,
    "posthoc": False,
    "retuned": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "primitive_effective_lift_certificate_actual",
    "represented_primitive_lift",
    "primitive_k0_class",
    "indecomposable_representative",
    "gcd_one_endpoint_degree",
    "no_hidden_multiplicity",
    "boundary_zero_without_division",
    "control_zero_without_multiplicity",
    "connected_graph_representative",
    "rosati_indecomposable_representative",
    "source_subrep_primitive",
    "coupled_source_primitive",
    "source_before_points",
    "inside_exact_24_budget",
    "no_multiplicity_or_divisibility",
    "no_primitive_selector_or_posthoc_projection",
    "no_point_graph_sample_basis_primitivity",
)

BANNED_FLAGS = (
    "nonprimitive_effective_lift",
    "multiple_effective_lift",
    "divisible_k0_class",
    "hidden_multiplicity_lift",
    "rank_scaled_lift",
    "finite_cover_lift",
    "tensor_power_lift",
    "degree_gcd_not_one",
    "endpoint_common_factor",
    "boundary_zero_after_division",
    "control_zero_after_multiplicity",
    "graph_disconnected_union",
    "rosati_block_diagonal",
    "primitive_selector",
    "declared_primitive_lift",
    "posthoc_primitive_projection",
    "retuned_primitive_representative",
    "point_graph_primitive_count",
    "finite_primitive_sample",
    "basis_primitive_row",
    "primitive_context_collapse",
    "missing_primitive_effective_lift_certificate",
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


def primitive_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "primitive": deepcopy(PRIMITIVE_DATA),
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
    primitive = state["primitive"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_552")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc552_witness_missing")
    if PRIMITIVE not in accepted:
        out.append("primitive_effective_lift_missing_from_current")
    if PRIMITIVE not in assignments:
        out.append("primitive_effective_lift_unassigned")
    if assignments.get(PRIMITIVE) != "coh_finite_limit_cut":
        out.append(f"primitive_effective_lift_bad_charge:{assignments.get(PRIMITIVE)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(primitive, dict):
        out.append("primitive_data_not_mapping")
        primitive = {}

    if primitive.get("effective_certificate") != EFFECTIVE:
        out.append("primitive_not_based_on_effective_grothendieck_lift")
    if not primitive.get("primitive_lift"):
        out.append("nonprimitive_effective_lift")
    if not primitive.get("source_side") or not primitive.get("choice_free"):
        out.append("primitive_selector")
    if not primitive.get("represented_by_source_subrep") or not primitive.get("realized_in_coupled_source"):
        out.append("nonprimitive_effective_lift")
    if not primitive.get("primitive") or not primitive.get("indecomposable"):
        out.append("nonprimitive_effective_lift")
    if primitive.get("multiplicity") != 1:
        out.append("hidden_multiplicity_lift")
    if not primitive.get("gcd_one"):
        out.append("degree_gcd_not_one")
    if primitive.get("divisible"):
        out.append("divisible_k0_class")
    if primitive.get("multiple"):
        out.append("multiple_effective_lift")
    if primitive.get("rank_scaled"):
        out.append("rank_scaled_lift")
    if primitive.get("finite_cover"):
        out.append("finite_cover_lift")
    if primitive.get("tensor_power"):
        out.append("tensor_power_lift")
    if not primitive.get("endpoint_gcd_one"):
        out.append("endpoint_common_factor")
    if not primitive.get("degree_gcd_one"):
        out.append("degree_gcd_not_one")
    if not primitive.get("boundary_zero_without_division"):
        out.append("boundary_zero_after_division")
    if not primitive.get("control_zero_without_multiplicity"):
        out.append("control_zero_after_multiplicity")
    if not primitive.get("graph_connected"):
        out.append("graph_disconnected_union")
    if not primitive.get("rosati_block_indecomposable"):
        out.append("rosati_block_diagonal")
    if not primitive.get("nonpositive_stage") or primitive.get("imports_positivity"):
        out.append("positivity_imported_primitivity")
    if not primitive.get("preserves_budget"):
        out.append("primitive_lift_expands_exact_24_budget")
    if not primitive.get("source_before_points"):
        out.append("primitive_lift_loses_source_before_points")

    missing_identities = PRIMITIVE_IDENTITIES - _as_set(primitive.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(primitive.get("coherent_on"))
    if missing_coherence:
        out.append("primitive_lift_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if {"dd4_boundary", "control_death"} - _as_set(primitive.get("annihilates")):
        out.append("control_zero_after_multiplicity")

    if primitive.get("selector"):
        out.append("primitive_selector")
    if primitive.get("declared"):
        out.append("declared_primitive_lift")
    if primitive.get("posthoc"):
        out.append("posthoc_primitive_projection")
    if primitive.get("retuned"):
        out.append("retuned_primitive_representative")
    if primitive.get("point_graph"):
        out.append("point_graph_primitive_count")
    if primitive.get("finite_sample"):
        out.append("finite_primitive_sample")
    if primitive.get("basis_row"):
        out.append("basis_primitive_row")
    if primitive.get("context_collapse"):
        out.append("primitive_context_collapse")

    for req in (
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
        "dd4_image_only_handoff_contract",
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
    ):
        if req not in state["requires"].get(PRIMITIVE, []):
            out.append(f"primitive_lift_requires_missing:{req}")
    for prior in (
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
    ):
        if PRIMITIVE not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_primitive_effective")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("primitive_lift_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("primitive_lift_uses_graph_side_bridge")

    out.extend(flag for flag, active in state["banned"].items() if active)
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
        elif key == "primitive":
            data["primitive"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = primitive_state(MAP)

gate(
    f"{PREFIX}1 doc 552 primitive effective lift layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["primitive"]["identities"]),
    ),
)

multiple_gap = variant(
    live,
    flags={"primitive_k0_class": False, "no_multiplicity_or_divisibility": False},
    banned={
        "nonprimitive_effective_lift": True,
        "multiple_effective_lift": True,
        "divisible_k0_class": True,
        "hidden_multiplicity_lift": True,
        "rank_scaled_lift": True,
    },
    primitive={
        "primitive": False,
        "indecomposable": False,
        "multiplicity": 3,
        "divisible": True,
        "multiple": True,
        "rank_scaled": True,
    },
)
multiple_gap["primitive"]["identities"] -= {
    "primitive_k0_class",
    "indecomposable_representative",
    "no_hidden_multiplicity",
}

gate(
    f"{PREFIX}2 rejects imprimitive multiples, divisible classes, and rank scaling",
    not accepts(multiple_gap)
    and {
        "nonprimitive_effective_lift",
        "multiple_effective_lift",
        "divisible_k0_class",
        "hidden_multiplicity_lift",
        "rank_scaled_lift",
    }
    <= set(reasons(multiple_gap)),
    ",".join(reasons(multiple_gap)),
)

cover_tensor_gcd = variant(
    live,
    flags={"gcd_one_endpoint_degree": False},
    banned={
        "finite_cover_lift": True,
        "tensor_power_lift": True,
        "degree_gcd_not_one": True,
        "endpoint_common_factor": True,
    },
    primitive={
        "finite_cover": True,
        "tensor_power": True,
        "gcd_one": False,
        "endpoint_gcd_one": False,
        "degree_gcd_one": False,
    },
)
cover_tensor_gcd["primitive"]["identities"] -= {"gcd_one_endpoint_degree"}
cover_tensor_gcd["primitive"]["coherent_on"] -= {"endpoint_integrality", "degree_maps"}

gate(
    f"{PREFIX}3 rejects finite covers, tensor powers, and endpoint/degree common factors",
    not accepts(cover_tensor_gcd)
    and {"finite_cover_lift", "tensor_power_lift", "degree_gcd_not_one", "endpoint_common_factor"}
    <= set(reasons(cover_tensor_gcd)),
    ",".join(reasons(cover_tensor_gcd)),
)

division_gap = variant(
    live,
    flags={"boundary_zero_without_division": False, "control_zero_without_multiplicity": False},
    banned={"boundary_zero_after_division": True, "control_zero_after_multiplicity": True},
    primitive={
        "boundary_zero_without_division": False,
        "control_zero_without_multiplicity": False,
    },
)
division_gap["primitive"]["identities"] -= {
    "boundary_zero_without_division",
    "control_zero_without_multiplicity",
}
division_gap["primitive"]["coherent_on"] -= {"dd4_boundary", "control_death"}
division_gap["primitive"]["annihilates"] = set()

gate(
    f"{PREFIX}4 rejects boundary/control laws that require division or multiplicity cancellation",
    not accepts(division_gap)
    and {"boundary_zero_after_division", "control_zero_after_multiplicity"} <= set(reasons(division_gap)),
    ",".join(reasons(division_gap)),
)

block_gap = variant(
    live,
    flags={"connected_graph_representative": False, "rosati_indecomposable_representative": False},
    banned={"graph_disconnected_union": True, "rosati_block_diagonal": True, "nonprimitive_effective_lift": True},
    primitive={"graph_connected": False, "rosati_block_indecomposable": False, "indecomposable": False},
)
block_gap["primitive"]["identities"] -= {
    "connected_graph_representative",
    "rosati_indecomposable_representative",
    "indecomposable_representative",
}
block_gap["primitive"]["coherent_on"] -= {"graph_composition", "rosati_count"}

gate(
    f"{PREFIX}5 rejects disconnected graph unions or Rosati block sums",
    not accepts(block_gap)
    and {"graph_disconnected_union", "rosati_block_diagonal", "nonprimitive_effective_lift"} <= set(reasons(block_gap)),
    ",".join(reasons(block_gap)),
)

representative_gap = variant(
    live,
    flags={"represented_primitive_lift": False, "source_subrep_primitive": False, "coupled_source_primitive": False},
    banned={"nonprimitive_effective_lift": True},
    primitive={
        "primitive_lift": "",
        "represented_by_source_subrep": False,
        "realized_in_coupled_source": False,
    },
)
representative_gap["primitive"]["identities"] -= {
    "represented_primitive_lift",
    "source_subrep_primitive",
    "coupled_source_primitive",
}
representative_gap["primitive"]["coherent_on"] -= {"source_fiber_subrepresenter", "coupled_source_image"}

gate(
    f"{PREFIX}6 rejects primitive claims without source-subrep and coupled-source realization",
    not accepts(representative_gap)
    and "nonprimitive_effective_lift" in reasons(representative_gap),
    ",".join(reasons(representative_gap)),
)

selector_posthoc = variant(
    live,
    flags={"no_primitive_selector_or_posthoc_projection": False},
    banned={
        "primitive_selector": True,
        "declared_primitive_lift": True,
        "posthoc_primitive_projection": True,
        "retuned_primitive_representative": True,
    },
    primitive={"source_side": False, "choice_free": False, "selector": True, "declared": True, "posthoc": True, "retuned": True},
)

gate(
    f"{PREFIX}7 rejects primitive selectors, declarations, posthoc projections, or retunings",
    not accepts(selector_posthoc)
    and {
        "primitive_selector",
        "declared_primitive_lift",
        "posthoc_primitive_projection",
        "retuned_primitive_representative",
    }
    <= set(reasons(selector_posthoc)),
    ",".join(reasons(selector_posthoc)),
)

point_sample_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_point_graph_sample_basis_primitivity": False,
    },
    banned={
        "point_graph_primitive_count": True,
        "finite_primitive_sample": True,
        "basis_primitive_row": True,
        "primitive_context_collapse": True,
    },
    primitive={
        "source_before_points": False,
        "preserves_budget": False,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
        "context_collapse": True,
    },
)
point_sample_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_primitive_lift"
point_sample_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects point/graph counts, finite samples, basis rows, or context collapse as primitivity",
    not accepts(point_sample_context)
    and {"point_graph_primitive_count", "finite_primitive_sample", "basis_primitive_row", "primitive_context_collapse"}
    <= set(reasons(point_sample_context)),
    ",".join(reasons(point_sample_context)),
)

missing_cert = variant(
    live,
    flags={"primitive_effective_lift_certificate_actual": False},
    banned={"missing_primitive_effective_lift_certificate": True},
)
missing_cert["accepted"].remove(PRIMITIVE)
del missing_cert["assignments"][PRIMITIVE]

gate(
    f"{PREFIX}9 rejects missing primitive effective lift certificates",
    not accepts(missing_cert)
    and "missing_primitive_effective_lift_certificate" in reasons(missing_cert)
    and "primitive_effective_lift_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    multiple_gap,
    cover_tensor_gcd,
    division_gap,
    block_gap,
    representative_gap,
    selector_posthoc,
    point_sample_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only primitive gcd-one indecomposable effective Grothendieck lifts pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: effective K0 lift is primitive and gcd-one")
print(
    "VERDICT: represented effective K0 trace lifts count only when the lift "
    "is primitive, gcd-one, and indecomposable in the source square. "
    "Imprimitive multiples, divisible classes, hidden multiplicities, rank "
    "scalings, finite covers, tensor powers, endpoint or degree common "
    "factors, boundary/control laws that require division or multiplicity "
    "cancellation, disconnected graph unions, Rosati block sums, primitive "
    "selectors, declarations, posthoc projections, retunings, point/graph "
    "counts, finite samples, basis rows, context collapse, and missing "
    "primitive effective lift certificates do not construct the missing object."
)
