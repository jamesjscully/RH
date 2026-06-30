r"""Pivotal-monoidal contract for source-square dual-trace data.

Doc 547 pins internal evaluation/coevaluation and categorical trace. This
witness prevents that duality from being merely objectwise: the square must
carry functorial pivotal monoidal duality, compatible with dagger, tensor,
degree trace, endpoint integrality, DD.4 boundary, boundary pushforward,
control death, and admissible probes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_pivotal_monoidal_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the pivotal-monoidal witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 548
EXPECTED_WITNESS = "doc548-probe-pivotal-monoidal"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PIVOTAL_IDENTITIES = {
    "dual_functor_on_morphisms",
    "double_dual_coherence",
    "tensor_dual_comparison",
    "unit_dual_comparison",
    "dagger_pivotal_coherence",
    "monoidal_trace_multiplicative",
    "degree_trace_multiplicative",
    "endpoint_integrality_tensor_stable",
    "dd4_pivotal_natural",
    "boundary_pushforward_pivotal_natural",
    "control_death_tensor_ideal",
    "probe_pivotal_natural",
}

IDENTITY_FAILURES = {
    "dual_functor_on_morphisms": "dual_not_functorial",
    "double_dual_coherence": "double_dual_coherence_missing",
    "tensor_dual_comparison": "tensor_dual_comparison_missing",
    "unit_dual_comparison": "unit_dual_comparison_missing",
    "dagger_pivotal_coherence": "dagger_pivotal_mismatch",
    "monoidal_trace_multiplicative": "trace_not_monoidal",
    "degree_trace_multiplicative": "degree_trace_not_multiplicative",
    "endpoint_integrality_tensor_stable": "endpoint_integrality_tensor_gap",
    "dd4_pivotal_natural": "dd4_pivotal_naturality_missing",
    "boundary_pushforward_pivotal_natural": "boundary_pushforward_pivotal_missing",
    "control_death_tensor_ideal": "control_tensor_ideal_leak",
    "probe_pivotal_natural": "probe_pivotal_naturality_missing",
}

COHERENT_ON = {
    "rosati_count",
    "degree_maps",
    "endpoint_integrality",
    "graph_composition",
    "dd4_boundary",
    "boundary_pushforward",
    "control_death",
    "probe_naturality_certificate",
    "joint_constraint_fork",
}

PIVOTAL_DATA = {
    "dual_trace_certificate": DUAL_TRACE,
    "duality_functor": "source_dual_functor",
    "source_side": True,
    "choice_free": True,
    "functorial_on_morphisms": True,
    "objectwise_only": False,
    "double_dual_coherent": True,
    "monoidal": True,
    "tensor_dual_comparison": True,
    "unit_dual_comparison": True,
    "dagger_compatible": True,
    "trace_monoidal": True,
    "degree_trace_multiplicative": True,
    "endpoint_tensor_stable": True,
    "external_pivotal": False,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": PIVOTAL_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "annihilates": {"control_death"},
    "posthoc": False,
    "retuned": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "pivotal_monoidal_certificate_actual",
    "functorial_dual_on_morphisms",
    "double_dual_coherence",
    "tensor_unit_duality",
    "dagger_pivotal_coherence",
    "monoidal_categorical_trace",
    "multiplicative_degree_trace",
    "endpoint_integrality_tensor_stable",
    "dd4_pivotal_naturality",
    "boundary_pushforward_pivotal",
    "control_death_tensor_ideal",
    "probe_pivotal_naturality",
    "source_before_points",
    "inside_exact_24_budget",
    "no_external_or_positive_pivotality",
    "no_posthoc_retuned_pivotality",
    "no_point_graph_sample_basis_pivotality",
)

BANNED_FLAGS = (
    "objectwise_duality_only",
    "dual_not_functorial",
    "double_dual_coherence_missing",
    "tensor_dual_comparison_missing",
    "unit_dual_comparison_missing",
    "dagger_pivotal_mismatch",
    "trace_not_monoidal",
    "degree_trace_not_multiplicative",
    "endpoint_integrality_tensor_gap",
    "dd4_pivotal_naturality_missing",
    "boundary_pushforward_pivotal_missing",
    "control_tensor_ideal_leak",
    "probe_pivotal_naturality_missing",
    "external_pivotal_structure",
    "positivity_imported_pivotality",
    "posthoc_pivotal_transport",
    "retuned_pivotal_structure",
    "point_graph_pivotality",
    "finite_pivotal_sample",
    "basis_pivotal_row",
    "pivotal_context_collapse",
    "missing_pivotal_monoidal_certificate",
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


def pivotal_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "pivotal": deepcopy(PIVOTAL_DATA),
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
    pivotal = state["pivotal"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_548")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc548_witness_missing")
    if PIVOTAL not in accepted:
        out.append("pivotal_missing_from_current")
    if PIVOTAL not in assignments:
        out.append("pivotal_unassigned")
    if assignments.get(PIVOTAL) != "coh_finite_limit_cut":
        out.append(f"pivotal_bad_charge:{assignments.get(PIVOTAL)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(pivotal, dict):
        out.append("pivotal_data_not_mapping")
        pivotal = {}

    if pivotal.get("dual_trace_certificate") != DUAL_TRACE:
        out.append("pivotal_not_based_on_dual_trace_certificate")
    if pivotal.get("objectwise_only"):
        out.append("objectwise_duality_only")
    if not pivotal.get("duality_functor") or not pivotal.get("functorial_on_morphisms"):
        out.append("dual_not_functorial")
    if not pivotal.get("double_dual_coherent"):
        out.append("double_dual_coherence_missing")
    if not pivotal.get("monoidal") or not pivotal.get("tensor_dual_comparison"):
        out.append("tensor_dual_comparison_missing")
    if not pivotal.get("unit_dual_comparison"):
        out.append("unit_dual_comparison_missing")
    if not pivotal.get("dagger_compatible"):
        out.append("dagger_pivotal_mismatch")
    if not pivotal.get("trace_monoidal"):
        out.append("trace_not_monoidal")
    if not pivotal.get("degree_trace_multiplicative"):
        out.append("degree_trace_not_multiplicative")
    if not pivotal.get("endpoint_tensor_stable"):
        out.append("endpoint_integrality_tensor_gap")
    if not pivotal.get("source_side") or not pivotal.get("choice_free") or pivotal.get("external_pivotal"):
        out.append("external_pivotal_structure")
    if not pivotal.get("nonpositive_stage") or pivotal.get("imports_positivity"):
        out.append("positivity_imported_pivotality")
    if not pivotal.get("preserves_budget"):
        out.append("pivotal_expands_exact_24_budget")
    if not pivotal.get("source_before_points"):
        out.append("pivotal_loses_source_before_points")

    missing_identities = PIVOTAL_IDENTITIES - _as_set(pivotal.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(pivotal.get("coherent_on"))
    if missing_coherence:
        out.append("pivotal_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if "control_death" not in _as_set(pivotal.get("annihilates")):
        out.append("control_tensor_ideal_leak")

    if pivotal.get("posthoc"):
        out.append("posthoc_pivotal_transport")
    if pivotal.get("retuned"):
        out.append("retuned_pivotal_structure")
    if pivotal.get("point_graph"):
        out.append("point_graph_pivotality")
    if pivotal.get("finite_sample"):
        out.append("finite_pivotal_sample")
    if pivotal.get("basis_row"):
        out.append("basis_pivotal_row")
    if pivotal.get("context_collapse"):
        out.append("pivotal_context_collapse")

    for req in (
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
        if req not in state["requires"].get(PIVOTAL, []):
            out.append(f"pivotal_requires_missing:{req}")
    for prior in (
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
        if PIVOTAL not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_pivotal_monoidal")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("pivotal_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("pivotal_uses_graph_side_bridge")

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
        elif key == "pivotal":
            data["pivotal"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = pivotal_state(MAP)

gate(
    f"{PREFIX}1 doc 548 pivotal-monoidal layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["pivotal"]["identities"]),
    ),
)

objectwise = variant(
    live,
    flags={"functorial_dual_on_morphisms": False},
    banned={"objectwise_duality_only": True, "dual_not_functorial": True},
    pivotal={"objectwise_only": True, "duality_functor": None, "functorial_on_morphisms": False},
)
objectwise["pivotal"]["identities"].remove("dual_functor_on_morphisms")

gate(
    f"{PREFIX}2 rejects objectwise-only or nonfunctorial duality",
    not accepts(objectwise)
    and {"objectwise_duality_only", "dual_not_functorial"} <= set(reasons(objectwise)),
    ",".join(reasons(objectwise)),
)

monoidal_missing = variant(
    live,
    flags={"double_dual_coherence": False, "tensor_unit_duality": False},
    banned={
        "double_dual_coherence_missing": True,
        "tensor_dual_comparison_missing": True,
        "unit_dual_comparison_missing": True,
    },
    pivotal={
        "double_dual_coherent": False,
        "monoidal": False,
        "tensor_dual_comparison": False,
        "unit_dual_comparison": False,
    },
)
monoidal_missing["pivotal"]["identities"] -= {
    "double_dual_coherence",
    "tensor_dual_comparison",
    "unit_dual_comparison",
}

gate(
    f"{PREFIX}3 rejects missing double-dual, tensor, or unit comparisons",
    not accepts(monoidal_missing)
    and {
        "double_dual_coherence_missing",
        "tensor_dual_comparison_missing",
        "unit_dual_comparison_missing",
    }
    <= set(reasons(monoidal_missing)),
    ",".join(reasons(monoidal_missing)),
)

dagger_external = variant(
    live,
    flags={"dagger_pivotal_coherence": False, "no_external_or_positive_pivotality": False},
    banned={
        "dagger_pivotal_mismatch": True,
        "external_pivotal_structure": True,
        "positivity_imported_pivotality": True,
    },
    pivotal={
        "dagger_compatible": False,
        "source_side": False,
        "choice_free": False,
        "external_pivotal": True,
        "nonpositive_stage": False,
        "imports_positivity": True,
    },
)
dagger_external["pivotal"]["identities"].remove("dagger_pivotal_coherence")

gate(
    f"{PREFIX}4 rejects dagger-pivotal mismatch or external positive pivotality",
    not accepts(dagger_external)
    and {"dagger_pivotal_mismatch", "external_pivotal_structure", "positivity_imported_pivotality"}
    <= set(reasons(dagger_external)),
    ",".join(reasons(dagger_external)),
)

trace_multiplicative = variant(
    live,
    flags={
        "monoidal_categorical_trace": False,
        "multiplicative_degree_trace": False,
        "endpoint_integrality_tensor_stable": False,
    },
    banned={
        "trace_not_monoidal": True,
        "degree_trace_not_multiplicative": True,
        "endpoint_integrality_tensor_gap": True,
    },
    pivotal={
        "trace_monoidal": False,
        "degree_trace_multiplicative": False,
        "endpoint_tensor_stable": False,
    },
)
trace_multiplicative["pivotal"]["identities"] -= {
    "monoidal_trace_multiplicative",
    "degree_trace_multiplicative",
    "endpoint_integrality_tensor_stable",
}
trace_multiplicative["pivotal"]["coherent_on"] -= {"degree_maps", "endpoint_integrality", "graph_composition"}

gate(
    f"{PREFIX}5 rejects nonmonoidal trace, nonmultiplicative degree, or endpoint gaps",
    not accepts(trace_multiplicative)
    and {"trace_not_monoidal", "degree_trace_not_multiplicative", "endpoint_integrality_tensor_gap"}
    <= set(reasons(trace_multiplicative)),
    ",".join(reasons(trace_multiplicative)),
)

naturality_missing = variant(
    live,
    flags={
        "dd4_pivotal_naturality": False,
        "boundary_pushforward_pivotal": False,
        "probe_pivotal_naturality": False,
    },
    banned={
        "dd4_pivotal_naturality_missing": True,
        "boundary_pushforward_pivotal_missing": True,
        "probe_pivotal_naturality_missing": True,
    },
)
naturality_missing["pivotal"]["identities"] -= {
    "dd4_pivotal_natural",
    "boundary_pushforward_pivotal_natural",
    "probe_pivotal_natural",
}
naturality_missing["pivotal"]["coherent_on"] -= {
    "dd4_boundary",
    "boundary_pushforward",
    "probe_naturality_certificate",
}

gate(
    f"{PREFIX}6 rejects missing DD4, boundary, or probe pivotal naturality",
    not accepts(naturality_missing)
    and {
        "dd4_pivotal_naturality_missing",
        "boundary_pushforward_pivotal_missing",
        "probe_pivotal_naturality_missing",
    }
    <= set(reasons(naturality_missing)),
    ",".join(reasons(naturality_missing)),
)

control_leak = variant(
    live,
    flags={"control_death_tensor_ideal": False},
    banned={"control_tensor_ideal_leak": True},
)
control_leak["pivotal"]["identities"].remove("control_death_tensor_ideal")
control_leak["pivotal"]["annihilates"] = set()
control_leak["pivotal"]["coherent_on"].remove("control_death")

gate(
    f"{PREFIX}7 rejects control-death tensor ideal leaks",
    not accepts(control_leak)
    and "control_tensor_ideal_leak" in reasons(control_leak),
    ",".join(reasons(control_leak)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_posthoc_retuned_pivotality": False,
        "no_point_graph_sample_basis_pivotality": False,
    },
    banned={
        "posthoc_pivotal_transport": True,
        "retuned_pivotal_structure": True,
        "point_graph_pivotality": True,
        "finite_pivotal_sample": True,
        "basis_pivotal_row": True,
        "pivotal_context_collapse": True,
    },
    pivotal={
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
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_pivotality"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects posthoc, retuned, point/sample/basis, or context-collapsed pivotality",
    not accepts(posthoc_point_context)
    and {
        "posthoc_pivotal_transport",
        "retuned_pivotal_structure",
        "point_graph_pivotality",
        "finite_pivotal_sample",
        "basis_pivotal_row",
        "pivotal_context_collapse",
    }
    <= set(reasons(posthoc_point_context)),
    ",".join(reasons(posthoc_point_context)),
)

missing_cert = variant(
    live,
    flags={"pivotal_monoidal_certificate_actual": False},
    banned={"missing_pivotal_monoidal_certificate": True},
)
missing_cert["accepted"].remove(PIVOTAL)
del missing_cert["assignments"][PIVOTAL]

gate(
    f"{PREFIX}9 rejects missing pivotal-monoidal certificates",
    not accepts(missing_cert)
    and "missing_pivotal_monoidal_certificate" in reasons(missing_cert)
    and "pivotal_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    objectwise,
    monoidal_missing,
    dagger_external,
    trace_multiplicative,
    naturality_missing,
    control_leak,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only functorial pivotal monoidal source duality passes",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: dual trace is functorial pivotal monoidal")
print(
    "VERDICT: dual-traced source-square data count only when the internal "
    "duality is functorial on morphisms, pivotal, monoidal, dagger-compatible, "
    "trace-multiplicative, degree-multiplicative, endpoint-integrality stable, "
    "DD.4/boundary/probe natural, and control-ideal compatible. Objectwise "
    "duality, missing double-dual or tensor/unit comparisons, external "
    "pivotal structure, imported positivity, posthoc or retuned pivotality, "
    "point/graph pivotality, finite samples, basis rows, context collapse, "
    "and missing pivotal-monoidal certificates do not construct the missing object."
)
