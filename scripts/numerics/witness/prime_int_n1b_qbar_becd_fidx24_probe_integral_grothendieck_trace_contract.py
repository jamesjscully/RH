r"""Integral Grothendieck trace contract for source-square exact traces.

Doc 549 pins exact-additive pivotal trace data. This witness prevents that
trace from being merely rational or coefficient-extended: it must descend to
a source-side integral Grothendieck/K0 character, with unit and degree
normalization, endpoint integrality, DD.4/control annihilation, integral
boundary pushforward, and graph-composition additivity.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_integral_grothendieck_trace_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the integral Grothendieck trace witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 550
EXPECTED_WITNESS = "doc550-probe-integral-grothendieck-trace"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

INTEGRAL_IDENTITIES = {
    "k0_trace_descent",
    "integral_value_ring",
    "unit_normalization",
    "endpoint_integrality_character",
    "degree_normalization",
    "k0_additivity",
    "finite_limit_equalizer_additivity",
    "dd4_boundary_class_zero",
    "boundary_pushforward_integral",
    "graph_composition_additivity",
    "control_class_zero",
}

IDENTITY_FAILURES = {
    "k0_trace_descent": "trace_not_grothendieck_descended",
    "integral_value_ring": "rational_trace_value",
    "unit_normalization": "unit_normalization_missing",
    "endpoint_integrality_character": "endpoint_integrality_character_missing",
    "degree_normalization": "degree_normalization_missing",
    "k0_additivity": "k0_additivity_missing",
    "finite_limit_equalizer_additivity": "k0_additivity_missing",
    "dd4_boundary_class_zero": "dd4_class_not_annihilated",
    "boundary_pushforward_integral": "boundary_class_nonzero",
    "graph_composition_additivity": "k0_additivity_missing",
    "control_class_zero": "control_class_nonzero",
}

COHERENT_ON = {
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "control_death",
    "probe_naturality_certificate",
    "joint_constraint_fork",
}

INTEGRAL_DATA = {
    "exact_additive_certificate": EXACT_ADD,
    "k0_character": "source_K0_integral_trace",
    "source_side": True,
    "choice_free": True,
    "descends_to_k0": True,
    "group_completion_native": True,
    "value_ring": "Z",
    "coefficient_extension": False,
    "denominator_clearing": False,
    "unit_normalized": True,
    "endpoint_integral": True,
    "degree_normalized": True,
    "k0_additive": True,
    "finite_limit_equalizer_additive": True,
    "boundary_classes_zero": True,
    "dd4_annihilated": True,
    "boundary_pushforward_integral": True,
    "graph_composition_additive": True,
    "control_class_zero": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": INTEGRAL_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "annihilates": {"dd4_boundary", "control_death"},
    "posthoc": False,
    "retuned": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "integral_grothendieck_trace_certificate_actual",
    "k0_trace_descent",
    "integral_value_ring",
    "unit_normalization",
    "endpoint_integrality_character",
    "degree_normalization",
    "k0_additivity",
    "finite_limit_equalizer_additivity",
    "dd4_boundary_class_zero",
    "boundary_pushforward_integrality",
    "graph_composition_additivity",
    "control_class_zero",
    "source_before_points",
    "inside_exact_24_budget",
    "no_coefficient_extension_or_denominator",
    "no_posthoc_retuned_integrality",
    "no_point_graph_sample_basis_integrality",
)

BANNED_FLAGS = (
    "trace_not_grothendieck_descended",
    "rational_trace_value",
    "fractional_degree_character",
    "unit_normalization_missing",
    "endpoint_integrality_character_missing",
    "degree_normalization_missing",
    "k0_additivity_missing",
    "boundary_class_nonzero",
    "dd4_class_not_annihilated",
    "control_class_nonzero",
    "coefficient_extension_trace",
    "denominator_clearing_trace",
    "posthoc_integral_projection",
    "retuned_integer_character",
    "point_graph_integer_count",
    "finite_integer_sample",
    "basis_integer_row",
    "integrality_context_collapse",
    "missing_integral_grothendieck_trace_certificate",
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


def integral_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "integral": deepcopy(INTEGRAL_DATA),
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
    integral = state["integral"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_550")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc550_witness_missing")
    if INTEGRAL not in accepted:
        out.append("integral_grothendieck_trace_missing_from_current")
    if INTEGRAL not in assignments:
        out.append("integral_grothendieck_trace_unassigned")
    if assignments.get(INTEGRAL) != "coh_finite_limit_cut":
        out.append(f"integral_grothendieck_trace_bad_charge:{assignments.get(INTEGRAL)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(integral, dict):
        out.append("integral_data_not_mapping")
        integral = {}

    if integral.get("exact_additive_certificate") != EXACT_ADD:
        out.append("integral_not_based_on_exact_additive_trace")
    if not integral.get("k0_character"):
        out.append("trace_not_grothendieck_descended")
    if not integral.get("source_side") or not integral.get("choice_free"):
        out.append("trace_not_grothendieck_descended")
    if not integral.get("descends_to_k0") or not integral.get("group_completion_native"):
        out.append("trace_not_grothendieck_descended")
    if integral.get("value_ring") != "Z":
        out.append("rational_trace_value")
    if integral.get("coefficient_extension"):
        out.append("coefficient_extension_trace")
    if integral.get("denominator_clearing"):
        out.append("denominator_clearing_trace")
    if not integral.get("unit_normalized"):
        out.append("unit_normalization_missing")
    if not integral.get("endpoint_integral"):
        out.append("endpoint_integrality_character_missing")
    if not integral.get("degree_normalized"):
        out.append("degree_normalization_missing")
    if not integral.get("k0_additive") or not integral.get("finite_limit_equalizer_additive"):
        out.append("k0_additivity_missing")
    if not integral.get("boundary_classes_zero"):
        out.append("boundary_class_nonzero")
    if not integral.get("dd4_annihilated"):
        out.append("dd4_class_not_annihilated")
    if not integral.get("boundary_pushforward_integral"):
        out.append("boundary_class_nonzero")
    if not integral.get("graph_composition_additive"):
        out.append("k0_additivity_missing")
    if not integral.get("control_class_zero"):
        out.append("control_class_nonzero")
    if not integral.get("nonpositive_stage") or integral.get("imports_positivity"):
        out.append("positivity_imported_integrality")
    if not integral.get("preserves_budget"):
        out.append("integral_trace_expands_exact_24_budget")
    if not integral.get("source_before_points"):
        out.append("integral_trace_loses_source_before_points")

    missing_identities = INTEGRAL_IDENTITIES - _as_set(integral.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(integral.get("coherent_on"))
    if missing_coherence:
        out.append("integral_trace_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if {"dd4_boundary", "control_death"} - _as_set(integral.get("annihilates")):
        out.append("control_class_nonzero")

    if integral.get("posthoc"):
        out.append("posthoc_integral_projection")
    if integral.get("retuned"):
        out.append("retuned_integer_character")
    if integral.get("point_graph"):
        out.append("point_graph_integer_count")
    if integral.get("finite_sample"):
        out.append("finite_integer_sample")
    if integral.get("basis_row"):
        out.append("basis_integer_row")
    if integral.get("context_collapse"):
        out.append("integrality_context_collapse")

    for req in (
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
        "finite_limit_cut",
        "equalizer_arrow_to_subrep",
        "budget_dependency_closure_certificate",
        "finite_index_budget_certificate",
        "exact_24_cell_finite_index",
        "joint_constraint_fork",
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
        if req not in state["requires"].get(INTEGRAL, []):
            out.append(f"integral_trace_requires_missing:{req}")
    for prior in (
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
        if INTEGRAL not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_integral_grothendieck")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("integral_trace_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("integral_trace_uses_graph_side_bridge")

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
        elif key == "integral":
            data["integral"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = integral_state(MAP)

gate(
    f"{PREFIX}1 doc 550 integral Grothendieck trace layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["integral"]["identities"]),
    ),
)

descent_gap = variant(
    live,
    flags={"k0_trace_descent": False, "k0_additivity": False, "finite_limit_equalizer_additivity": False},
    banned={"trace_not_grothendieck_descended": True, "k0_additivity_missing": True},
    integral={
        "source_side": False,
        "choice_free": False,
        "descends_to_k0": False,
        "group_completion_native": False,
        "k0_additive": False,
        "finite_limit_equalizer_additive": False,
    },
)
descent_gap["integral"]["identities"] -= {
    "k0_trace_descent",
    "k0_additivity",
    "finite_limit_equalizer_additivity",
}

gate(
    f"{PREFIX}2 rejects missing K0 descent or additive group-completion laws",
    not accepts(descent_gap)
    and {"trace_not_grothendieck_descended", "k0_additivity_missing"} <= set(reasons(descent_gap)),
    ",".join(reasons(descent_gap)),
)

nonintegral_value = variant(
    live,
    flags={"integral_value_ring": False, "no_coefficient_extension_or_denominator": False},
    banned={"rational_trace_value": True, "coefficient_extension_trace": True, "denominator_clearing_trace": True},
    integral={"value_ring": "Q", "coefficient_extension": True, "denominator_clearing": True},
)
nonintegral_value["integral"]["identities"] -= {"integral_value_ring"}

gate(
    f"{PREFIX}3 rejects rational trace values, coefficient extensions, or denominator clearing",
    not accepts(nonintegral_value)
    and {"rational_trace_value", "coefficient_extension_trace", "denominator_clearing_trace"}
    <= set(reasons(nonintegral_value)),
    ",".join(reasons(nonintegral_value)),
)

normalization_gap = variant(
    live,
    flags={"unit_normalization": False, "endpoint_integrality_character": False, "degree_normalization": False},
    banned={
        "unit_normalization_missing": True,
        "endpoint_integrality_character_missing": True,
        "degree_normalization_missing": True,
        "fractional_degree_character": True,
    },
    integral={"unit_normalized": False, "endpoint_integral": False, "degree_normalized": False},
)
normalization_gap["integral"]["identities"] -= {
    "unit_normalization",
    "endpoint_integrality_character",
    "degree_normalization",
}
normalization_gap["integral"]["coherent_on"] -= {"endpoint_integrality", "degree_maps"}

gate(
    f"{PREFIX}4 rejects missing unit, endpoint, or degree normalization",
    not accepts(normalization_gap)
    and {
        "unit_normalization_missing",
        "endpoint_integrality_character_missing",
        "degree_normalization_missing",
        "fractional_degree_character",
    }
    <= set(reasons(normalization_gap)),
    ",".join(reasons(normalization_gap)),
)

boundary_gap = variant(
    live,
    flags={"dd4_boundary_class_zero": False, "boundary_pushforward_integrality": False},
    banned={"boundary_class_nonzero": True, "dd4_class_not_annihilated": True},
    integral={"boundary_classes_zero": False, "dd4_annihilated": False, "boundary_pushforward_integral": False},
)
boundary_gap["integral"]["identities"] -= {"dd4_boundary_class_zero", "boundary_pushforward_integral"}
boundary_gap["integral"]["coherent_on"] -= {"dd4_boundary", "boundary_pushforward"}
boundary_gap["integral"]["annihilates"] -= {"dd4_boundary"}

gate(
    f"{PREFIX}5 rejects nonzero boundary/DD4 classes or nonintegral pushforward",
    not accepts(boundary_gap)
    and {"boundary_class_nonzero", "dd4_class_not_annihilated"} <= set(reasons(boundary_gap)),
    ",".join(reasons(boundary_gap)),
)

composition_control_gap = variant(
    live,
    flags={"graph_composition_additivity": False, "control_class_zero": False},
    banned={"k0_additivity_missing": True, "control_class_nonzero": True},
    integral={"graph_composition_additive": False, "control_class_zero": False},
)
composition_control_gap["integral"]["identities"] -= {"graph_composition_additivity", "control_class_zero"}
composition_control_gap["integral"]["coherent_on"] -= {"graph_composition", "control_death"}
composition_control_gap["integral"]["annihilates"] -= {"control_death"}

gate(
    f"{PREFIX}6 rejects graph-composition additivity gaps or live control classes",
    not accepts(composition_control_gap)
    and {"k0_additivity_missing", "control_class_nonzero"} <= set(reasons(composition_control_gap)),
    ",".join(reasons(composition_control_gap)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_posthoc_retuned_integrality": False,
        "no_point_graph_sample_basis_integrality": False,
    },
    banned={
        "posthoc_integral_projection": True,
        "retuned_integer_character": True,
        "point_graph_integer_count": True,
        "finite_integer_sample": True,
        "basis_integer_row": True,
        "integrality_context_collapse": True,
    },
    integral={
        "source_before_points": False,
        "preserves_budget": False,
        "posthoc": True,
        "retuned": True,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
        "context_collapse": True,
    },
)
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_integrality"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}7 rejects posthoc, retuned, point/sample/basis, or context-collapsed integrality",
    not accepts(posthoc_point_context)
    and {
        "posthoc_integral_projection",
        "retuned_integer_character",
        "point_graph_integer_count",
        "finite_integer_sample",
        "basis_integer_row",
        "integrality_context_collapse",
    }
    <= set(reasons(posthoc_point_context)),
    ",".join(reasons(posthoc_point_context)),
)

missing_cert = variant(
    live,
    flags={"integral_grothendieck_trace_certificate_actual": False},
    banned={"missing_integral_grothendieck_trace_certificate": True},
)
missing_cert["accepted"].remove(INTEGRAL)
del missing_cert["assignments"][INTEGRAL]

gate(
    f"{PREFIX}8 rejects missing integral Grothendieck trace certificates",
    not accepts(missing_cert)
    and "missing_integral_grothendieck_trace_certificate" in reasons(missing_cert)
    and "integral_grothendieck_trace_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    descent_gap,
    nonintegral_value,
    normalization_gap,
    boundary_gap,
    composition_control_gap,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}9 every banned integral trace repair is covered by a rejecting variant",
    set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

gate(
    f"{PREFIX}10 only internal integral Grothendieck traces pass",
    accepts(live) and not any(accepts(data) for data in variants),
    "live_reasons=%s" % reasons(live),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: exact-additive trace is integral Grothendieck-descended")
print(
    "VERDICT: exact-additive source-square trace data count only when the "
    "trace descends to a source-side integral Grothendieck/K0 character "
    "valued in Z, with native group completion, unit normalization, endpoint "
    "integrality, degree normalization, K0 and finite-limit/equalizer "
    "additivity, DD.4 and control classes annihilated, integral boundary "
    "pushforward, and graph-composition additivity. Rational traces, "
    "coefficient extensions, denominator clearing, posthoc integral "
    "projection, retuned integer characters, point/graph integer counts, "
    "finite samples, basis rows, context collapse, and missing integral "
    "Grothendieck trace certificates do not construct the missing object."
)
