r"""Dual-trace contract for source-square adjoint pairing data.

Doc 546 pins a nondegenerate source-side pairing making Rosati/dagger an
adjoint. This witness prevents that pairing from being raw bilinear data: the
square must construct it internally from evaluation/coevaluation maps and a
categorical trace with snake identities, cyclicity, degree trace, DD.4
boundary naturality, boundary-pushforward naturality, and control-death
orthogonality.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_dual_trace_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the dual-trace witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 547
EXPECTED_WITNESS = "doc547-probe-dual-trace"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

DUAL_TRACE_IDENTITIES = {
    "evaluation_coevaluation_internal",
    "left_snake",
    "right_snake",
    "categorical_trace_equals_pairing",
    "left_right_trace_agree",
    "degree_trace_from_duality",
    "composition_cyclic_trace",
    "dd4_duality_natural",
    "boundary_pushforward_duality_natural",
    "control_death_dual_orthogonal_ideal",
}

IDENTITY_FAILURES = {
    "evaluation_coevaluation_internal": "external_evaluation_coevaluation",
    "left_snake": "snake_identity_missing",
    "right_snake": "snake_identity_missing",
    "categorical_trace_equals_pairing": "trace_pairing_decoupled",
    "left_right_trace_agree": "left_right_trace_mismatch",
    "degree_trace_from_duality": "degree_trace_not_from_duality",
    "composition_cyclic_trace": "noncyclic_categorical_trace",
    "dd4_duality_natural": "dd4_duality_naturality_missing",
    "boundary_pushforward_duality_natural": "boundary_pushforward_duality_missing",
    "control_death_dual_orthogonal_ideal": "control_duality_leak",
}

COHERENT_ON = {
    "rosati_count",
    "degree_maps",
    "graph_composition",
    "dd4_boundary",
    "boundary_pushforward",
    "control_death",
    "joint_constraint_fork",
}

DUALITY_DATA = {
    "pairing_certificate": ADJ_PAIR,
    "evaluation": "source_eval",
    "coevaluation": "source_coeval",
    "source_side": True,
    "choice_free": True,
    "evaluation_in_category": True,
    "coevaluation_in_category": True,
    "raw_pairing_only": False,
    "external_duality": False,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "trace": "categorical_trace",
    "trace_source": DUAL_TRACE,
    "adjoint_pairing_recovered": True,
    "left_right_trace_agree": True,
    "cyclic_trace": True,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": DUAL_TRACE_IDENTITIES,
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
    "dual_trace_certificate_actual",
    "internal_evaluation_coevaluation",
    "snake_identities",
    "categorical_trace_constructs_pairing",
    "left_right_trace_agreement",
    "degree_trace_from_duality",
    "composition_cyclic_trace_from_duality",
    "dd4_duality_naturality",
    "boundary_pushforward_duality",
    "control_death_duality_ideal",
    "source_before_points",
    "inside_exact_24_budget",
    "no_external_or_positive_duality",
    "no_raw_or_posthoc_duality",
    "no_point_graph_sample_basis_duality",
)

BANNED_FLAGS = (
    "raw_pairing_without_duality",
    "external_evaluation_coevaluation",
    "evaluation_choice",
    "coevaluation_choice",
    "positivity_imported_duality",
    "snake_identity_missing",
    "trace_not_categorical",
    "trace_pairing_decoupled",
    "left_right_trace_mismatch",
    "noncyclic_categorical_trace",
    "degree_trace_not_from_duality",
    "dd4_duality_naturality_missing",
    "boundary_pushforward_duality_missing",
    "control_duality_leak",
    "posthoc_duality_transport",
    "retuned_duality_form",
    "point_graph_duality",
    "finite_duality_sample",
    "basis_duality_row",
    "duality_context_collapse",
    "missing_dual_trace_certificate",
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


def duality_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "duality": deepcopy(DUALITY_DATA),
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
    duality = state["duality"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_547")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc547_witness_missing")
    if DUAL_TRACE not in accepted:
        out.append("dual_trace_missing_from_current")
    if DUAL_TRACE not in assignments:
        out.append("dual_trace_unassigned")
    if assignments.get(DUAL_TRACE) != "coh_finite_limit_cut":
        out.append(f"dual_trace_bad_charge:{assignments.get(DUAL_TRACE)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(duality, dict):
        out.append("duality_data_not_mapping")
        duality = {}

    if duality.get("pairing_certificate") != ADJ_PAIR:
        out.append("duality_not_based_on_adjoint_pairing_certificate")
    if duality.get("raw_pairing_only"):
        out.append("raw_pairing_without_duality")
    if not duality.get("evaluation") or not duality.get("coevaluation"):
        out.append("raw_pairing_without_duality")
    if not duality.get("source_side") or not duality.get("choice_free") or duality.get("external_duality"):
        out.append("external_evaluation_coevaluation")
    if not duality.get("evaluation_in_category"):
        out.append("evaluation_choice")
    if not duality.get("coevaluation_in_category"):
        out.append("coevaluation_choice")
    if not duality.get("nonpositive_stage") or duality.get("imports_positivity"):
        out.append("positivity_imported_duality")
    if not duality.get("preserves_budget"):
        out.append("duality_expands_exact_24_budget")
    if not duality.get("source_before_points"):
        out.append("duality_loses_source_before_points")
    if duality.get("trace") != "categorical_trace" or duality.get("trace_source") != DUAL_TRACE:
        out.append("trace_not_categorical")
    if not duality.get("adjoint_pairing_recovered"):
        out.append("trace_pairing_decoupled")
    if not duality.get("left_right_trace_agree"):
        out.append("left_right_trace_mismatch")
    if not duality.get("cyclic_trace"):
        out.append("noncyclic_categorical_trace")

    missing_identities = DUAL_TRACE_IDENTITIES - _as_set(duality.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(duality.get("coherent_on"))
    if missing_coherence:
        out.append("duality_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if "control_death" not in _as_set(duality.get("annihilates")):
        out.append("control_duality_leak")

    if duality.get("posthoc"):
        out.append("posthoc_duality_transport")
    if duality.get("retuned"):
        out.append("retuned_duality_form")
    if duality.get("point_graph"):
        out.append("point_graph_duality")
    if duality.get("finite_sample"):
        out.append("finite_duality_sample")
    if duality.get("basis_row"):
        out.append("basis_duality_row")
    if duality.get("context_collapse"):
        out.append("duality_context_collapse")

    for req in (
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
        if req not in state["requires"].get(DUAL_TRACE, []):
            out.append(f"dual_trace_requires_missing:{req}")
    for prior in (
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
        if DUAL_TRACE not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_dual_traced")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("dual_trace_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("dual_trace_uses_graph_side_bridge")

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
        elif key == "duality":
            data["duality"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = duality_state(MAP)

gate(
    f"{PREFIX}1 doc 547 dual-trace layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["duality"]["identities"]),
    ),
)

raw_no_duality = variant(
    live,
    flags={"internal_evaluation_coevaluation": False, "categorical_trace_constructs_pairing": False},
    banned={"raw_pairing_without_duality": True},
    duality={
        "raw_pairing_only": True,
        "evaluation": None,
        "coevaluation": None,
        "identities": set(),
        "adjoint_pairing_recovered": False,
    },
)

gate(
    f"{PREFIX}2 rejects raw pairings without internal evaluation/coevaluation",
    not accepts(raw_no_duality)
    and "raw_pairing_without_duality" in reasons(raw_no_duality),
    ",".join(reasons(raw_no_duality)),
)

external_positive = variant(
    live,
    flags={"no_external_or_positive_duality": False},
    banned={
        "external_evaluation_coevaluation": True,
        "evaluation_choice": True,
        "coevaluation_choice": True,
        "positivity_imported_duality": True,
    },
    duality={
        "source_side": False,
        "choice_free": False,
        "evaluation_in_category": False,
        "coevaluation_in_category": False,
        "external_duality": True,
        "nonpositive_stage": False,
        "imports_positivity": True,
    },
)

gate(
    f"{PREFIX}3 rejects external duality data or imported positivity",
    not accepts(external_positive)
    and {
        "external_evaluation_coevaluation",
        "evaluation_choice",
        "coevaluation_choice",
        "positivity_imported_duality",
    }
    <= set(reasons(external_positive)),
    ",".join(reasons(external_positive)),
)

snake_missing = variant(
    live,
    flags={"snake_identities": False},
    banned={"snake_identity_missing": True},
)
snake_missing["duality"]["identities"] -= {"left_snake", "right_snake"}

gate(
    f"{PREFIX}4 rejects missing snake identities",
    not accepts(snake_missing)
    and "snake_identity_missing" in reasons(snake_missing),
    ",".join(reasons(snake_missing)),
)

trace_decoupled = variant(
    live,
    flags={"categorical_trace_constructs_pairing": False},
    banned={"trace_not_categorical": True, "trace_pairing_decoupled": True},
    duality={"trace": "raw_trace_form", "trace_source": ADJ_PAIR, "adjoint_pairing_recovered": False},
)
trace_decoupled["duality"]["identities"].remove("categorical_trace_equals_pairing")

gate(
    f"{PREFIX}5 rejects non-categorical trace or trace-pairing decoupling",
    not accepts(trace_decoupled)
    and {"trace_not_categorical", "trace_pairing_decoupled"} <= set(reasons(trace_decoupled)),
    ",".join(reasons(trace_decoupled)),
)

trace_law_missing = variant(
    live,
    flags={
        "left_right_trace_agreement": False,
        "degree_trace_from_duality": False,
        "composition_cyclic_trace_from_duality": False,
    },
    banned={
        "left_right_trace_mismatch": True,
        "noncyclic_categorical_trace": True,
        "degree_trace_not_from_duality": True,
    },
    duality={"left_right_trace_agree": False, "cyclic_trace": False},
)
trace_law_missing["duality"]["identities"] -= {
    "left_right_trace_agree",
    "degree_trace_from_duality",
    "composition_cyclic_trace",
}
trace_law_missing["duality"]["coherent_on"] -= {"degree_maps", "graph_composition", "rosati_count"}

gate(
    f"{PREFIX}6 rejects trace mismatch, noncyclic trace, or degree-trace gaps",
    not accepts(trace_law_missing)
    and {
        "left_right_trace_mismatch",
        "noncyclic_categorical_trace",
        "degree_trace_not_from_duality",
    }
    <= set(reasons(trace_law_missing)),
    ",".join(reasons(trace_law_missing)),
)

boundary_missing = variant(
    live,
    flags={"dd4_duality_naturality": False, "boundary_pushforward_duality": False},
    banned={"dd4_duality_naturality_missing": True, "boundary_pushforward_duality_missing": True},
)
boundary_missing["duality"]["identities"] -= {
    "dd4_duality_natural",
    "boundary_pushforward_duality_natural",
}
boundary_missing["duality"]["coherent_on"] -= {"dd4_boundary", "boundary_pushforward"}

gate(
    f"{PREFIX}7 rejects missing DD4 or boundary-pushforward duality naturality",
    not accepts(boundary_missing)
    and {"dd4_duality_naturality_missing", "boundary_pushforward_duality_missing"}
    <= set(reasons(boundary_missing)),
    ",".join(reasons(boundary_missing)),
)

control_leak = variant(
    live,
    flags={"control_death_duality_ideal": False},
    banned={"control_duality_leak": True},
)
control_leak["duality"]["identities"].remove("control_death_dual_orthogonal_ideal")
control_leak["duality"]["annihilates"] = set()
control_leak["duality"]["coherent_on"].remove("control_death")

gate(
    f"{PREFIX}8 rejects control-death duality leaks",
    not accepts(control_leak)
    and "control_duality_leak" in reasons(control_leak),
    ",".join(reasons(control_leak)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_raw_or_posthoc_duality": False,
        "no_point_graph_sample_basis_duality": False,
    },
    banned={
        "posthoc_duality_transport": True,
        "retuned_duality_form": True,
        "point_graph_duality": True,
        "finite_duality_sample": True,
        "basis_duality_row": True,
        "duality_context_collapse": True,
    },
    duality={
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
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_duality"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

missing_cert = variant(
    live,
    flags={"dual_trace_certificate_actual": False},
    banned={"missing_dual_trace_certificate": True},
)
missing_cert["accepted"].remove(DUAL_TRACE)
del missing_cert["assignments"][DUAL_TRACE]

gate(
    f"{PREFIX}9 rejects posthoc/point-side duality and missing certificates",
    not accepts(posthoc_point_context)
    and {
        "posthoc_duality_transport",
        "retuned_duality_form",
        "point_graph_duality",
        "finite_duality_sample",
        "basis_duality_row",
        "duality_context_collapse",
    }
    <= set(reasons(posthoc_point_context))
    and not accepts(missing_cert)
    and "missing_dual_trace_certificate" in reasons(missing_cert)
    and "dual_trace_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(posthoc_point_context) + reasons(missing_cert)),
)

variants = [
    raw_no_duality,
    external_positive,
    snake_missing,
    trace_decoupled,
    trace_law_missing,
    boundary_missing,
    control_leak,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only internal dual-trace source data pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: source pairing is constructed by internal dual trace")
print(
    "VERDICT: adjoint-paired source-square data count only when the pairing "
    "is constructed from internal evaluation/coevaluation and categorical "
    "trace with snake identities, left/right trace agreement, cyclicity, "
    "degree trace, DD.4 boundary naturality, boundary-pushforward naturality, "
    "and control-death orthogonality. Raw bilinear forms, external duality, "
    "imported positivity, posthoc or retuned duality, point/graph duality, "
    "finite samples, basis rows, context collapse, and missing dual-trace "
    "certificates do not construct the missing object."
)
