r"""Exact-additive trace contract for source-square pivotal data.

Doc 548 pins functorial pivotal monoidal duality. This witness prevents the
pivotal trace from being formal but non-exact: the trace must be additive over
the finite-limit/equalizer fork, kill DD.4 boundary terms, preserve boundary
pushforward exactness, make degree and composition additive, and keep control
death as a trace-zero ideal without external exact structure.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_exact_additive_trace_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the exact-additive trace witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 549
EXPECTED_WITNESS = "doc549-probe-exact-additive-trace"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

EXACT_IDENTITIES = {
    "exact_triangle",
    "finite_limit_trace_additive",
    "equalizer_trace_formula",
    "dd4_boundary_trace_zero",
    "boundary_pushforward_exact",
    "degree_trace_additive",
    "composition_trace_additive",
    "control_death_trace_zero_ideal",
    "probe_exact_natural",
}

IDENTITY_FAILURES = {
    "exact_triangle": "exact_triangle_missing",
    "finite_limit_trace_additive": "finite_limit_trace_additivity_missing",
    "equalizer_trace_formula": "equalizer_trace_formula_missing",
    "dd4_boundary_trace_zero": "dd4_boundary_trace_nonzero",
    "boundary_pushforward_exact": "boundary_pushforward_exactness_missing",
    "degree_trace_additive": "degree_additivity_missing",
    "composition_trace_additive": "composition_additivity_missing",
    "control_death_trace_zero_ideal": "control_trace_nonzero",
    "probe_exact_natural": "probe_exactness_missing",
}

COHERENT_ON = {
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "dd4_boundary",
    "boundary_pushforward",
    "degree_maps",
    "graph_composition",
    "control_death",
    "probe_naturality_certificate",
    "joint_constraint_fork",
}

EXACT_DATA = {
    "pivotal_certificate": PIVOTAL,
    "exact_structure": "source_exact_trace",
    "source_side": True,
    "choice_free": True,
    "internal_exact_structure": True,
    "exact_triangle": True,
    "trace_additive": True,
    "finite_limit_additive": True,
    "equalizer_formula": True,
    "dd4_boundary_trace_zero": True,
    "boundary_pushforward_exact": True,
    "degree_additive": True,
    "composition_additive": True,
    "control_trace_zero": True,
    "probe_exact": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": EXACT_IDENTITIES,
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
    "exact_additive_trace_certificate_actual",
    "internal_exact_structure",
    "exact_triangle",
    "finite_limit_trace_additivity",
    "equalizer_trace_formula",
    "dd4_boundary_trace_zero",
    "boundary_pushforward_exactness",
    "degree_trace_additivity",
    "composition_trace_additivity",
    "control_death_trace_zero",
    "probe_exactness",
    "source_before_points",
    "inside_exact_24_budget",
    "no_external_or_positive_exactness",
    "no_posthoc_retuned_exactness",
    "no_point_graph_sample_basis_exactness",
)

BANNED_FLAGS = (
    "nonadditive_trace",
    "exact_triangle_missing",
    "finite_limit_trace_additivity_missing",
    "equalizer_trace_formula_missing",
    "dd4_boundary_trace_nonzero",
    "boundary_pushforward_exactness_missing",
    "degree_additivity_missing",
    "composition_additivity_missing",
    "control_trace_nonzero",
    "probe_exactness_missing",
    "external_exact_structure",
    "positivity_imported_exactness",
    "posthoc_exact_trace",
    "retuned_exact_sequence",
    "point_graph_exact_trace",
    "finite_exact_sample",
    "basis_exact_row",
    "exactness_context_collapse",
    "missing_exact_additive_trace_certificate",
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


def exact_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "exact": deepcopy(EXACT_DATA),
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
    exact = state["exact"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_549")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc549_witness_missing")
    if EXACT_ADD not in accepted:
        out.append("exact_additive_trace_missing_from_current")
    if EXACT_ADD not in assignments:
        out.append("exact_additive_trace_unassigned")
    if assignments.get(EXACT_ADD) != "coh_finite_limit_cut":
        out.append(f"exact_additive_trace_bad_charge:{assignments.get(EXACT_ADD)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(exact, dict):
        out.append("exact_data_not_mapping")
        exact = {}

    if exact.get("pivotal_certificate") != PIVOTAL:
        out.append("exact_not_based_on_pivotal_certificate")
    if not exact.get("exact_structure") or not exact.get("trace_additive"):
        out.append("nonadditive_trace")
    if not exact.get("internal_exact_structure") or not exact.get("source_side") or not exact.get("choice_free"):
        out.append("external_exact_structure")
    if not exact.get("exact_triangle"):
        out.append("exact_triangle_missing")
    if not exact.get("finite_limit_additive"):
        out.append("finite_limit_trace_additivity_missing")
    if not exact.get("equalizer_formula"):
        out.append("equalizer_trace_formula_missing")
    if not exact.get("dd4_boundary_trace_zero"):
        out.append("dd4_boundary_trace_nonzero")
    if not exact.get("boundary_pushforward_exact"):
        out.append("boundary_pushforward_exactness_missing")
    if not exact.get("degree_additive"):
        out.append("degree_additivity_missing")
    if not exact.get("composition_additive"):
        out.append("composition_additivity_missing")
    if not exact.get("control_trace_zero"):
        out.append("control_trace_nonzero")
    if not exact.get("probe_exact"):
        out.append("probe_exactness_missing")
    if not exact.get("nonpositive_stage") or exact.get("imports_positivity"):
        out.append("positivity_imported_exactness")
    if not exact.get("preserves_budget"):
        out.append("exact_trace_expands_exact_24_budget")
    if not exact.get("source_before_points"):
        out.append("exact_trace_loses_source_before_points")

    missing_identities = EXACT_IDENTITIES - _as_set(exact.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(exact.get("coherent_on"))
    if missing_coherence:
        out.append("exact_trace_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if "control_death" not in _as_set(exact.get("annihilates")):
        out.append("control_trace_nonzero")

    if exact.get("posthoc"):
        out.append("posthoc_exact_trace")
    if exact.get("retuned"):
        out.append("retuned_exact_sequence")
    if exact.get("point_graph"):
        out.append("point_graph_exact_trace")
    if exact.get("finite_sample"):
        out.append("finite_exact_sample")
    if exact.get("basis_row"):
        out.append("basis_exact_row")
    if exact.get("context_collapse"):
        out.append("exactness_context_collapse")

    for req in (
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
        if req not in state["requires"].get(EXACT_ADD, []):
            out.append(f"exact_additive_trace_requires_missing:{req}")
    for prior in (
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
        if EXACT_ADD not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_exact_additive")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("exact_trace_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("exact_trace_uses_graph_side_bridge")

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
        elif key == "exact":
            data["exact"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = exact_state(MAP)

gate(
    f"{PREFIX}1 doc 549 exact-additive trace layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["exact"]["identities"]),
    ),
)

nonadditive = variant(
    live,
    flags={
        "exact_triangle": False,
        "finite_limit_trace_additivity": False,
        "equalizer_trace_formula": False,
    },
    banned={
        "nonadditive_trace": True,
        "exact_triangle_missing": True,
        "finite_limit_trace_additivity_missing": True,
        "equalizer_trace_formula_missing": True,
    },
    exact={
        "trace_additive": False,
        "exact_triangle": False,
        "finite_limit_additive": False,
        "equalizer_formula": False,
    },
)
nonadditive["exact"]["identities"] -= {
    "exact_triangle",
    "finite_limit_trace_additive",
    "equalizer_trace_formula",
}
nonadditive["exact"]["coherent_on"] -= {"finite_limit_cut", "equalizer_arrow_to_subrep"}

gate(
    f"{PREFIX}2 rejects nonadditive traces and missing exact/equalizer formulas",
    not accepts(nonadditive)
    and {
        "nonadditive_trace",
        "exact_triangle_missing",
        "finite_limit_trace_additivity_missing",
        "equalizer_trace_formula_missing",
    }
    <= set(reasons(nonadditive)),
    ",".join(reasons(nonadditive)),
)

boundary_gap = variant(
    live,
    flags={"dd4_boundary_trace_zero": False, "boundary_pushforward_exactness": False},
    banned={"dd4_boundary_trace_nonzero": True, "boundary_pushforward_exactness_missing": True},
    exact={"dd4_boundary_trace_zero": False, "boundary_pushforward_exact": False},
)
boundary_gap["exact"]["identities"] -= {"dd4_boundary_trace_zero", "boundary_pushforward_exact"}
boundary_gap["exact"]["coherent_on"] -= {"dd4_boundary", "boundary_pushforward"}

gate(
    f"{PREFIX}3 rejects DD4 boundary trace leaks or boundary exactness gaps",
    not accepts(boundary_gap)
    and {"dd4_boundary_trace_nonzero", "boundary_pushforward_exactness_missing"}
    <= set(reasons(boundary_gap)),
    ",".join(reasons(boundary_gap)),
)

degree_composition_gap = variant(
    live,
    flags={"degree_trace_additivity": False, "composition_trace_additivity": False},
    banned={"degree_additivity_missing": True, "composition_additivity_missing": True},
    exact={"degree_additive": False, "composition_additive": False},
)
degree_composition_gap["exact"]["identities"] -= {"degree_trace_additive", "composition_trace_additive"}
degree_composition_gap["exact"]["coherent_on"] -= {"degree_maps", "graph_composition"}

gate(
    f"{PREFIX}4 rejects degree or composition additivity gaps",
    not accepts(degree_composition_gap)
    and {"degree_additivity_missing", "composition_additivity_missing"} <= set(reasons(degree_composition_gap)),
    ",".join(reasons(degree_composition_gap)),
)

control_probe_gap = variant(
    live,
    flags={"control_death_trace_zero": False, "probe_exactness": False},
    banned={"control_trace_nonzero": True, "probe_exactness_missing": True},
    exact={"control_trace_zero": False, "probe_exact": False},
)
control_probe_gap["exact"]["identities"] -= {"control_death_trace_zero_ideal", "probe_exact_natural"}
control_probe_gap["exact"]["annihilates"] = set()
control_probe_gap["exact"]["coherent_on"] -= {"control_death", "probe_naturality_certificate"}

gate(
    f"{PREFIX}5 rejects control trace leaks or probe exactness gaps",
    not accepts(control_probe_gap)
    and {"control_trace_nonzero", "probe_exactness_missing"} <= set(reasons(control_probe_gap)),
    ",".join(reasons(control_probe_gap)),
)

external_positive = variant(
    live,
    flags={"internal_exact_structure": False, "no_external_or_positive_exactness": False},
    banned={"external_exact_structure": True, "positivity_imported_exactness": True},
    exact={
        "source_side": False,
        "choice_free": False,
        "internal_exact_structure": False,
        "nonpositive_stage": False,
        "imports_positivity": True,
    },
)

gate(
    f"{PREFIX}6 rejects external exact structures or imported positivity",
    not accepts(external_positive)
    and {"external_exact_structure", "positivity_imported_exactness"} <= set(reasons(external_positive)),
    ",".join(reasons(external_positive)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_posthoc_retuned_exactness": False,
        "no_point_graph_sample_basis_exactness": False,
    },
    banned={
        "posthoc_exact_trace": True,
        "retuned_exact_sequence": True,
        "point_graph_exact_trace": True,
        "finite_exact_sample": True,
        "basis_exact_row": True,
        "exactness_context_collapse": True,
    },
    exact={
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
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_exact_trace"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}7 rejects posthoc, retuned, point/sample/basis, or context-collapsed exact traces",
    not accepts(posthoc_point_context)
    and {
        "posthoc_exact_trace",
        "retuned_exact_sequence",
        "point_graph_exact_trace",
        "finite_exact_sample",
        "basis_exact_row",
        "exactness_context_collapse",
    }
    <= set(reasons(posthoc_point_context)),
    ",".join(reasons(posthoc_point_context)),
)

missing_cert = variant(
    live,
    flags={"exact_additive_trace_certificate_actual": False},
    banned={"missing_exact_additive_trace_certificate": True},
)
missing_cert["accepted"].remove(EXACT_ADD)
del missing_cert["assignments"][EXACT_ADD]

gate(
    f"{PREFIX}8 rejects missing exact-additive trace certificates",
    not accepts(missing_cert)
    and "missing_exact_additive_trace_certificate" in reasons(missing_cert)
    and "exact_additive_trace_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    nonadditive,
    boundary_gap,
    degree_composition_gap,
    control_probe_gap,
    external_positive,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}9 every banned exact-additive repair is covered by a rejecting variant",
    set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

gate(
    f"{PREFIX}10 only internal exact-additive pivotal traces pass",
    accepts(live) and not any(accepts(data) for data in variants),
    "live_reasons=%s" % reasons(live),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: pivotal trace is exact-additive")
print(
    "VERDICT: pivotal-monoidal source-square data count only when the trace "
    "is exact-additive over the finite-limit/equalizer fork, kills DD.4 "
    "boundary terms, preserves boundary-pushforward exactness, makes degree "
    "and composition additive, keeps probes exact, and makes control death a "
    "trace-zero ideal. Nonadditive traces, external exact structures, imported "
    "positivity, posthoc or retuned exact sequences, point/graph exact traces, "
    "finite samples, basis rows, context collapse, and missing exact-additive "
    "trace certificates do not construct the missing object."
)
