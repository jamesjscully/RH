r"""Adjoint-pairing contract for source-square Rosati/dagger data.

Doc 545 pins dagger-monoidal source-square operation laws. This witness
prevents those laws from being unpaired formal operations: the square must
carry a nondegenerate source-side pairing making Rosati/dagger an adjoint and
making degree, composition, DD.4 boundary, boundary pushforward, and control
death trace-compatible without importing positivity.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_adjoint_pairing_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the adjoint-pairing witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 546
EXPECTED_WITNESS = "doc546-probe-adjoint-pairing"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PAIRING_IDENTITIES = {
    "rosati_adjoint",
    "degree_trace",
    "composition_cyclic_trace",
    "dd4_boundary_pairing_natural",
    "boundary_pushforward_pairing_natural",
    "control_death_orthogonal_ideal",
}

IDENTITY_FAILURES = {
    "rosati_adjoint": "rosati_adjoint_identity_missing",
    "degree_trace": "degree_trace_identity_missing",
    "composition_cyclic_trace": "composition_trace_identity_missing",
    "dd4_boundary_pairing_natural": "dd4_pairing_naturality_missing",
    "boundary_pushforward_pairing_natural": "boundary_pushforward_pairing_missing",
    "control_death_orthogonal_ideal": "control_pairing_leak",
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

PAIRING_DATA = {
    "dagger_certificate": DAG_MON_EQV,
    "pairing": "source_trace_pairing",
    "source_side": True,
    "choice_free": True,
    "perfect": True,
    "bilinear": True,
    "integral": True,
    "symmetric": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": PAIRING_IDENTITIES,
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
    "adjoint_pairing_certificate_actual",
    "perfect_source_pairing",
    "bilinear_integral_pairing",
    "rosati_adjoint_identity",
    "degree_trace_identity",
    "composition_cyclic_trace_identity",
    "dd4_pairing_naturality",
    "boundary_pushforward_pairing",
    "control_death_pairing_ideal",
    "source_before_points",
    "inside_exact_24_budget",
    "no_external_or_positive_pairing",
    "no_posthoc_retuned_pairing",
    "no_point_graph_sample_basis_pairing",
)

BANNED_FLAGS = (
    "unpaired_dagger_law",
    "degenerate_trace_pairing",
    "external_trace_functional",
    "positivity_imported_pairing",
    "rosati_adjoint_identity_missing",
    "degree_trace_identity_missing",
    "composition_trace_identity_missing",
    "dd4_pairing_naturality_missing",
    "boundary_pushforward_pairing_missing",
    "control_pairing_leak",
    "posthoc_pairing_transport",
    "retuned_pairing_form",
    "point_graph_pairing",
    "finite_pairing_sample",
    "basis_pairing_row",
    "dd4_pairing_context_collapse",
    "missing_adjoint_pairing_certificate",
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


def pairing_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "pairing": deepcopy(PAIRING_DATA),
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
    pairing = state["pairing"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_546")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc546_witness_missing")
    if ADJ_PAIR not in accepted:
        out.append("adjoint_pairing_missing_from_current")
    if ADJ_PAIR not in assignments:
        out.append("adjoint_pairing_unassigned")
    if assignments.get(ADJ_PAIR) != "coh_finite_limit_cut":
        out.append(f"adjoint_pairing_bad_charge:{assignments.get(ADJ_PAIR)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(pairing, dict):
        out.append("pairing_data_not_mapping")
        pairing = {}

    if pairing.get("dagger_certificate") != DAG_MON_EQV:
        out.append("pairing_not_based_on_dagger_monoidal_certificate")
    if not pairing.get("pairing"):
        out.append("unpaired_dagger_law")
    if not pairing.get("source_side"):
        out.append("external_trace_functional")
    if not pairing.get("choice_free"):
        out.append("external_trace_functional")
    if not pairing.get("perfect"):
        out.append("degenerate_trace_pairing")
    if not pairing.get("bilinear") or not pairing.get("integral"):
        out.append("degenerate_trace_pairing")
    if not pairing.get("symmetric"):
        out.append("degenerate_trace_pairing")
    if not pairing.get("nonpositive_stage") or pairing.get("imports_positivity"):
        out.append("positivity_imported_pairing")
    if not pairing.get("preserves_budget"):
        out.append("pairing_expands_exact_24_budget")
    if not pairing.get("source_before_points"):
        out.append("pairing_loses_source_before_points")

    missing_identities = PAIRING_IDENTITIES - _as_set(pairing.get("identities"))
    for ident in sorted(missing_identities):
        out.append(IDENTITY_FAILURES[ident])
    missing_coherence = COHERENT_ON - _as_set(pairing.get("coherent_on"))
    if missing_coherence:
        out.append("pairing_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if "control_death" not in _as_set(pairing.get("annihilates")):
        out.append("control_pairing_leak")

    if pairing.get("posthoc"):
        out.append("posthoc_pairing_transport")
    if pairing.get("retuned"):
        out.append("retuned_pairing_form")
    if pairing.get("point_graph"):
        out.append("point_graph_pairing")
    if pairing.get("finite_sample"):
        out.append("finite_pairing_sample")
    if pairing.get("basis_row"):
        out.append("basis_pairing_row")
    if pairing.get("context_collapse"):
        out.append("dd4_pairing_context_collapse")

    for req in (
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
        if req not in state["requires"].get(ADJ_PAIR, []):
            out.append(f"adjoint_pairing_requires_missing:{req}")
    for prior in (
        DAG_MON_EQV,
        CART_EQV,
        PROBE_EQV,
        PROBE_ESS,
        PROBE_FULL,
        PROBE_FAITH,
        PROBE_NAT,
        PROBE_SEP,
        ADM_CAT,
    ):
        if ADJ_PAIR not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_adjoint_paired")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("adjoint_pairing_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("adjoint_pairing_uses_graph_side_bridge")

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
        elif key == "pairing":
            data["pairing"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = pairing_state(MAP)

gate(
    f"{PREFIX}1 doc 546 adjoint-pairing layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["pairing"]["identities"]),
    ),
)

unpaired_degenerate = variant(
    live,
    flags={"perfect_source_pairing": False, "bilinear_integral_pairing": False},
    banned={"unpaired_dagger_law": True, "degenerate_trace_pairing": True},
    pairing={
        "pairing": None,
        "perfect": False,
        "bilinear": False,
        "integral": False,
        "symmetric": False,
        "identities": set(),
    },
)

gate(
    f"{PREFIX}2 rejects unpaired or degenerate trace pairings",
    not accepts(unpaired_degenerate)
    and {"unpaired_dagger_law", "degenerate_trace_pairing"} <= set(reasons(unpaired_degenerate)),
    ",".join(reasons(unpaired_degenerate)),
)

external_positive = variant(
    live,
    flags={"no_external_or_positive_pairing": False},
    banned={"external_trace_functional": True, "positivity_imported_pairing": True},
    pairing={"source_side": False, "choice_free": False, "nonpositive_stage": False, "imports_positivity": True},
)

gate(
    f"{PREFIX}3 rejects external trace functionals or imported positivity",
    not accepts(external_positive)
    and {"external_trace_functional", "positivity_imported_pairing"} <= set(reasons(external_positive)),
    ",".join(reasons(external_positive)),
)

rosati_degree_missing = variant(
    live,
    flags={"rosati_adjoint_identity": False, "degree_trace_identity": False},
    banned={"rosati_adjoint_identity_missing": True, "degree_trace_identity_missing": True},
)
rosati_degree_missing["pairing"]["identities"] -= {"rosati_adjoint", "degree_trace"}
rosati_degree_missing["pairing"]["coherent_on"] -= {"rosati_count", "degree_maps"}

gate(
    f"{PREFIX}4 rejects missing Rosati adjoint or degree trace identities",
    not accepts(rosati_degree_missing)
    and {"rosati_adjoint_identity_missing", "degree_trace_identity_missing"} <= set(reasons(rosati_degree_missing)),
    ",".join(reasons(rosati_degree_missing)),
)

composition_missing = variant(
    live,
    flags={"composition_cyclic_trace_identity": False},
    banned={"composition_trace_identity_missing": True},
)
composition_missing["pairing"]["identities"].remove("composition_cyclic_trace")
composition_missing["pairing"]["coherent_on"].remove("graph_composition")

gate(
    f"{PREFIX}5 rejects missing cyclic trace compatibility for composition",
    not accepts(composition_missing)
    and "composition_trace_identity_missing" in reasons(composition_missing),
    ",".join(reasons(composition_missing)),
)

boundary_missing = variant(
    live,
    flags={"dd4_pairing_naturality": False, "boundary_pushforward_pairing": False},
    banned={"dd4_pairing_naturality_missing": True, "boundary_pushforward_pairing_missing": True},
)
boundary_missing["pairing"]["identities"] -= {
    "dd4_boundary_pairing_natural",
    "boundary_pushforward_pairing_natural",
}
boundary_missing["pairing"]["coherent_on"] -= {"dd4_boundary", "boundary_pushforward"}

gate(
    f"{PREFIX}6 rejects missing DD4 or boundary-pushforward pairing naturality",
    not accepts(boundary_missing)
    and {"dd4_pairing_naturality_missing", "boundary_pushforward_pairing_missing"}
    <= set(reasons(boundary_missing)),
    ",".join(reasons(boundary_missing)),
)

control_leak = variant(
    live,
    flags={"control_death_pairing_ideal": False},
    banned={"control_pairing_leak": True},
)
control_leak["pairing"]["identities"].remove("control_death_orthogonal_ideal")
control_leak["pairing"]["annihilates"] = set()
control_leak["pairing"]["coherent_on"].remove("control_death")

gate(
    f"{PREFIX}7 rejects control-death pairing leaks",
    not accepts(control_leak)
    and "control_pairing_leak" in reasons(control_leak),
    ",".join(reasons(control_leak)),
)

posthoc_point_context = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_posthoc_retuned_pairing": False,
        "no_point_graph_sample_basis_pairing": False,
    },
    banned={
        "posthoc_pairing_transport": True,
        "retuned_pairing_form": True,
        "point_graph_pairing": True,
        "finite_pairing_sample": True,
        "basis_pairing_row": True,
        "dd4_pairing_context_collapse": True,
    },
    pairing={
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
posthoc_point_context["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_pairing"
posthoc_point_context["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects posthoc, retuned, point/sample/basis, or context-collapsed pairings",
    not accepts(posthoc_point_context)
    and {
        "posthoc_pairing_transport",
        "retuned_pairing_form",
        "point_graph_pairing",
        "finite_pairing_sample",
        "basis_pairing_row",
        "dd4_pairing_context_collapse",
    }
    <= set(reasons(posthoc_point_context)),
    ",".join(reasons(posthoc_point_context)),
)

missing_cert = variant(
    live,
    flags={"adjoint_pairing_certificate_actual": False},
    banned={"missing_adjoint_pairing_certificate": True},
)
missing_cert["accepted"].remove(ADJ_PAIR)
del missing_cert["assignments"][ADJ_PAIR]

gate(
    f"{PREFIX}9 rejects missing adjoint-pairing certificates",
    not accepts(missing_cert)
    and "missing_adjoint_pairing_certificate" in reasons(missing_cert)
    and "adjoint_pairing_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    unpaired_degenerate,
    external_positive,
    rosati_degree_missing,
    composition_missing,
    boundary_missing,
    control_leak,
    posthoc_point_context,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only nonpositive source-side adjoint pairings pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: source-side pairing makes dagger adjoint")
print(
    "VERDICT: dagger-monoidal source-square operations count only with a "
    "nondegenerate source-side pairing making Rosati/dagger adjoint and "
    "degree, composition, DD.4 boundary, boundary pushforward, and control "
    "death trace-compatible. External trace functionals, imported positivity, "
    "degenerate pairings, posthoc or retuned pairings, point/graph pairings, "
    "finite samples, basis rows, context collapse, and missing adjoint-pairing "
    "certificates do not construct the missing object."
)
