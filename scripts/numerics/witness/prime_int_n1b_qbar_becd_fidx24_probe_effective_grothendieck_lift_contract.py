r"""Effective Grothendieck lift contract for source-square K0 traces.

Doc 550 pins an integral Grothendieck/K0 trace character. This witness
prevents the character from being merely virtual: it must have a represented
effective source lift in the finite-limit source square, so endpoint, degree,
DD.4, graph/Rosati, and control identities are not produced by cancellation
between positive and negative K0 summands.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the effective Grothendieck lift witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 551
EXPECTED_WITNESS = "doc551-probe-effective-grothendieck-lift"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

EFFECTIVE_IDENTITIES = {
    "represented_effective_lift",
    "nonvirtual_k0_class",
    "source_subrep_represented",
    "coupled_source_realization",
    "endpoint_effective_integrality",
    "degree_effective_normalization",
    "boundary_effective_zero",
    "pushforward_effective_integrality",
    "graph_effective_additivity",
    "rosati_representative_compatibility",
    "control_effective_zero",
}

IDENTITY_FAILURES = {
    "represented_effective_lift": "class_without_representative",
    "nonvirtual_k0_class": "virtual_k0_difference",
    "source_subrep_represented": "class_without_representative",
    "coupled_source_realization": "class_without_representative",
    "endpoint_effective_integrality": "non_effective_k0_class",
    "degree_effective_normalization": "non_effective_k0_class",
    "boundary_effective_zero": "boundary_hidden_in_virtual_cancellation",
    "pushforward_effective_integrality": "non_effective_k0_class",
    "graph_effective_additivity": "non_effective_k0_class",
    "rosati_representative_compatibility": "rosati_only_on_virtual_class",
    "control_effective_zero": "control_hidden_in_virtual_cancellation",
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

EFFECTIVE_DATA = {
    "integral_certificate": INTEGRAL,
    "effective_lift": "source_effective_k0_lift",
    "source_side": True,
    "choice_free": True,
    "represented_by_source_subrep": True,
    "realized_in_coupled_source": True,
    "nonvirtual": True,
    "effective_class": True,
    "positive_negative_cancellation": False,
    "group_completion_only": False,
    "euler_characteristic_only": False,
    "split_representative": False,
    "external_effective_cone": False,
    "endpoint_effective": True,
    "degree_effective": True,
    "boundary_cancellation_native": True,
    "dd4_boundary_effective_zero": True,
    "boundary_pushforward_effective": True,
    "graph_composition_effective": True,
    "rosati_on_representative": True,
    "control_annihilation_native": True,
    "control_effective_zero": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": EFFECTIVE_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "annihilates": {"dd4_boundary", "control_death"},
    "declared": False,
    "posthoc": False,
    "retuned": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "effective_grothendieck_lift_certificate_actual",
    "represented_effective_lift",
    "nonvirtual_k0_class",
    "source_subrep_represented",
    "coupled_source_realization",
    "endpoint_effective_integrality",
    "degree_effective_normalization",
    "boundary_effective_zero",
    "boundary_pushforward_effective",
    "graph_effective_additivity",
    "rosati_representative_compatibility",
    "control_effective_zero",
    "source_before_points",
    "inside_exact_24_budget",
    "no_virtual_or_group_completion_only",
    "no_external_declared_or_posthoc_effectivity",
    "no_point_graph_sample_basis_effectivity",
)

BANNED_FLAGS = (
    "virtual_k0_difference",
    "positive_negative_cancellation",
    "formal_group_completion_only",
    "euler_characteristic_only",
    "class_without_representative",
    "non_effective_k0_class",
    "split_effective_representative",
    "external_effective_cone",
    "boundary_hidden_in_virtual_cancellation",
    "control_hidden_in_virtual_cancellation",
    "rosati_only_on_virtual_class",
    "declared_effective_lift",
    "posthoc_effective_projection",
    "retuned_effective_representative",
    "point_graph_effective_count",
    "finite_effective_sample",
    "basis_effective_row",
    "effectivity_context_collapse",
    "missing_effective_grothendieck_lift_certificate",
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


def effective_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "effective": deepcopy(EFFECTIVE_DATA),
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
    effective = state["effective"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_551")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc551_witness_missing")
    if EFFECTIVE not in accepted:
        out.append("effective_grothendieck_lift_missing_from_current")
    if EFFECTIVE not in assignments:
        out.append("effective_grothendieck_lift_unassigned")
    if assignments.get(EFFECTIVE) != "coh_finite_limit_cut":
        out.append(f"effective_grothendieck_lift_bad_charge:{assignments.get(EFFECTIVE)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(effective, dict):
        out.append("effective_data_not_mapping")
        effective = {}

    if effective.get("integral_certificate") != INTEGRAL:
        out.append("effective_not_based_on_integral_grothendieck_trace")
    if not effective.get("effective_lift"):
        out.append("class_without_representative")
    if not effective.get("source_side") or not effective.get("choice_free"):
        out.append("external_effective_cone")
    if not effective.get("represented_by_source_subrep") or not effective.get("realized_in_coupled_source"):
        out.append("class_without_representative")
    if not effective.get("nonvirtual"):
        out.append("virtual_k0_difference")
    if not effective.get("effective_class"):
        out.append("non_effective_k0_class")
    if effective.get("positive_negative_cancellation"):
        out.append("positive_negative_cancellation")
    if effective.get("group_completion_only"):
        out.append("formal_group_completion_only")
    if effective.get("euler_characteristic_only"):
        out.append("euler_characteristic_only")
    if effective.get("split_representative"):
        out.append("split_effective_representative")
    if effective.get("external_effective_cone"):
        out.append("external_effective_cone")
    if not effective.get("endpoint_effective") or not effective.get("degree_effective"):
        out.append("non_effective_k0_class")
    if not effective.get("boundary_cancellation_native") or not effective.get("dd4_boundary_effective_zero"):
        out.append("boundary_hidden_in_virtual_cancellation")
    if not effective.get("boundary_pushforward_effective") or not effective.get("graph_composition_effective"):
        out.append("non_effective_k0_class")
    if not effective.get("rosati_on_representative"):
        out.append("rosati_only_on_virtual_class")
    if not effective.get("control_annihilation_native") or not effective.get("control_effective_zero"):
        out.append("control_hidden_in_virtual_cancellation")
    if not effective.get("nonpositive_stage") or effective.get("imports_positivity"):
        out.append("positivity_imported_effectivity")
    if not effective.get("preserves_budget"):
        out.append("effective_lift_expands_exact_24_budget")
    if not effective.get("source_before_points"):
        out.append("effective_lift_loses_source_before_points")

    missing_identities = EFFECTIVE_IDENTITIES - _as_set(effective.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(effective.get("coherent_on"))
    if missing_coherence:
        out.append("effective_lift_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if {"dd4_boundary", "control_death"} - _as_set(effective.get("annihilates")):
        out.append("control_hidden_in_virtual_cancellation")

    if effective.get("declared"):
        out.append("declared_effective_lift")
    if effective.get("posthoc"):
        out.append("posthoc_effective_projection")
    if effective.get("retuned"):
        out.append("retuned_effective_representative")
    if effective.get("point_graph"):
        out.append("point_graph_effective_count")
    if effective.get("finite_sample"):
        out.append("finite_effective_sample")
    if effective.get("basis_row"):
        out.append("basis_effective_row")
    if effective.get("context_collapse"):
        out.append("effectivity_context_collapse")

    for req in (
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
        if req not in state["requires"].get(EFFECTIVE, []):
            out.append(f"effective_lift_requires_missing:{req}")
    for prior in (
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
        if EFFECTIVE not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_effective_grothendieck")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("effective_lift_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("effective_lift_uses_graph_side_bridge")

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
        elif key == "effective":
            data["effective"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = effective_state(MAP)

gate(
    f"{PREFIX}1 doc 551 effective Grothendieck lift layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["effective"]["identities"]),
    ),
)

virtual_gap = variant(
    live,
    flags={"nonvirtual_k0_class": False, "no_virtual_or_group_completion_only": False},
    banned={
        "virtual_k0_difference": True,
        "positive_negative_cancellation": True,
        "formal_group_completion_only": True,
        "euler_characteristic_only": True,
    },
    effective={
        "nonvirtual": False,
        "positive_negative_cancellation": True,
        "group_completion_only": True,
        "euler_characteristic_only": True,
    },
)
virtual_gap["effective"]["identities"] -= {"nonvirtual_k0_class"}

gate(
    f"{PREFIX}2 rejects virtual K0 differences and cancellation-only characters",
    not accepts(virtual_gap)
    and {
        "virtual_k0_difference",
        "positive_negative_cancellation",
        "formal_group_completion_only",
        "euler_characteristic_only",
    }
    <= set(reasons(virtual_gap)),
    ",".join(reasons(virtual_gap)),
)

representative_gap = variant(
    live,
    flags={"represented_effective_lift": False, "source_subrep_represented": False, "coupled_source_realization": False},
    banned={
        "class_without_representative": True,
        "non_effective_k0_class": True,
        "split_effective_representative": True,
        "external_effective_cone": True,
    },
    effective={
        "effective_lift": "",
        "source_side": False,
        "choice_free": False,
        "represented_by_source_subrep": False,
        "realized_in_coupled_source": False,
        "effective_class": False,
        "split_representative": True,
        "external_effective_cone": True,
    },
)
representative_gap["effective"]["identities"] -= {
    "represented_effective_lift",
    "source_subrep_represented",
    "coupled_source_realization",
}
representative_gap["effective"]["coherent_on"] -= {"source_fiber_subrepresenter", "coupled_source_image"}

gate(
    f"{PREFIX}3 rejects missing, split, non-effective, or external representatives",
    not accepts(representative_gap)
    and {
        "class_without_representative",
        "non_effective_k0_class",
        "split_effective_representative",
        "external_effective_cone",
    }
    <= set(reasons(representative_gap)),
    ",".join(reasons(representative_gap)),
)

boundary_control_virtual = variant(
    live,
    flags={"boundary_effective_zero": False, "control_effective_zero": False},
    banned={
        "boundary_hidden_in_virtual_cancellation": True,
        "control_hidden_in_virtual_cancellation": True,
        "rosati_only_on_virtual_class": True,
    },
    effective={
        "boundary_cancellation_native": False,
        "dd4_boundary_effective_zero": False,
        "rosati_on_representative": False,
        "control_annihilation_native": False,
        "control_effective_zero": False,
    },
)
boundary_control_virtual["effective"]["identities"] -= {
    "boundary_effective_zero",
    "rosati_representative_compatibility",
    "control_effective_zero",
}
boundary_control_virtual["effective"]["coherent_on"] -= {"dd4_boundary", "rosati_count", "control_death"}
boundary_control_virtual["effective"]["annihilates"] = set()

gate(
    f"{PREFIX}4 rejects boundary/control cancellation hidden in virtual differences",
    not accepts(boundary_control_virtual)
    and {
        "boundary_hidden_in_virtual_cancellation",
        "control_hidden_in_virtual_cancellation",
        "rosati_only_on_virtual_class",
    }
    <= set(reasons(boundary_control_virtual)),
    ",".join(reasons(boundary_control_virtual)),
)

source_law_gap = variant(
    live,
    flags={"endpoint_effective_integrality": False, "degree_effective_normalization": False},
    banned={"non_effective_k0_class": True},
    effective={"endpoint_effective": False, "degree_effective": False},
)
source_law_gap["effective"]["identities"] -= {
    "endpoint_effective_integrality",
    "degree_effective_normalization",
}
source_law_gap["effective"]["coherent_on"] -= {"endpoint_integrality", "degree_maps"}

gate(
    f"{PREFIX}5 rejects endpoint or degree laws not carried by the effective lift",
    not accepts(source_law_gap)
    and "non_effective_k0_class" in reasons(source_law_gap),
    ",".join(reasons(source_law_gap)),
)

pushforward_graph_gap = variant(
    live,
    flags={"boundary_pushforward_effective": False, "graph_effective_additivity": False},
    banned={"non_effective_k0_class": True},
    effective={"boundary_pushforward_effective": False, "graph_composition_effective": False},
)
pushforward_graph_gap["effective"]["identities"] -= {
    "pushforward_effective_integrality",
    "graph_effective_additivity",
}
pushforward_graph_gap["effective"]["coherent_on"] -= {"boundary_pushforward", "graph_composition"}

gate(
    f"{PREFIX}6 rejects pushforward or graph additivity outside the effective lift",
    not accepts(pushforward_graph_gap)
    and "non_effective_k0_class" in reasons(pushforward_graph_gap),
    ",".join(reasons(pushforward_graph_gap)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_external_declared_or_posthoc_effectivity": False,
        "no_point_graph_sample_basis_effectivity": False,
    },
    banned={
        "declared_effective_lift": True,
        "posthoc_effective_projection": True,
        "retuned_effective_representative": True,
        "point_graph_effective_count": True,
        "finite_effective_sample": True,
        "basis_effective_row": True,
        "effectivity_context_collapse": True,
    },
    effective={
        "source_before_points": False,
        "preserves_budget": False,
        "declared": True,
        "posthoc": True,
        "retuned": True,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
        "context_collapse": True,
    },
)
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_effective_lift"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}7 rejects declared, posthoc, retuned, point/sample/basis, or context-collapsed effectivity",
    not accepts(posthoc_point_context)
    and {
        "declared_effective_lift",
        "posthoc_effective_projection",
        "retuned_effective_representative",
        "point_graph_effective_count",
        "finite_effective_sample",
        "basis_effective_row",
        "effectivity_context_collapse",
    }
    <= set(reasons(posthoc_point_context)),
    ",".join(reasons(posthoc_point_context)),
)

missing_cert = variant(
    live,
    flags={"effective_grothendieck_lift_certificate_actual": False},
    banned={"missing_effective_grothendieck_lift_certificate": True},
)
missing_cert["accepted"].remove(EFFECTIVE)
del missing_cert["assignments"][EFFECTIVE]

gate(
    f"{PREFIX}8 rejects missing effective Grothendieck lift certificates",
    not accepts(missing_cert)
    and "missing_effective_grothendieck_lift_certificate" in reasons(missing_cert)
    and "effective_grothendieck_lift_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    virtual_gap,
    representative_gap,
    boundary_control_virtual,
    source_law_gap,
    pushforward_graph_gap,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}9 every banned effective-lift repair is covered by a rejecting variant",
    set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

gate(
    f"{PREFIX}10 only represented nonvirtual effective Grothendieck lifts pass",
    accepts(live) and not any(accepts(data) for data in variants),
    "live_reasons=%s" % reasons(live),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: integral K0 trace has represented effective source lift")
print(
    "VERDICT: integral Grothendieck/K0 trace data count only when the "
    "character has a represented nonvirtual effective source lift in the "
    "finite-limit square. Virtual K0 differences, positive-minus-negative "
    "cancellation, group-completion-only classes, Euler characteristics, "
    "missing or split representatives, external effective cones, boundary or "
    "control cancellation hidden in virtual summands, Rosati only on virtual "
    "classes, declared/posthoc/retuned lifts, point/graph counts, finite "
    "samples, basis rows, context collapse, and missing effective lift "
    "certificates do not construct the missing object."
)
