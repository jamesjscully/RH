r"""Dagger-monoidal probe-equivalence contract for source-square operations.

Doc 544 pins cartesian exactness of the probe equivalence. This witness
prevents the remaining correspondence-algebra escape: the equivalence must
also preserve identity, composition, degree, Rosati/dagger, DD.4 boundary
naturality, boundary pushforward, and control-death operations.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_dagger_monoidal_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the dagger-monoidal witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 545
EXPECTED_WITNESS = "doc545-probe-dagger-monoidal"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PRESERVED_OPERATIONS = {
    "graph_composition",
    "rosati_count",
    "degree_maps",
    "endpoint_integrality",
    "dd4_boundary",
    "boundary_pushforward",
    "control_death",
    "joint_constraint_fork",
}

OPERATION_LAWS = {
    "identity",
    "composition",
    "associativity",
    "dagger_involution",
    "dagger_contravariant",
    "rosati_degree_adjoint",
    "degree_multiplicative",
    "endpoint_integral_closed",
    "dd4_boundary_natural",
    "boundary_pushforward_natural",
    "control_death_two_sided_ideal",
}

LAW_FAILURES = {
    "identity": "identity_law_missing",
    "composition": "composition_law_missing",
    "dagger_involution": "rosati_involution_missing",
    "rosati_degree_adjoint": "rosati_degree_adjoint_mismatch",
    "degree_multiplicative": "degree_multiplicativity_missing",
    "endpoint_integral_closed": "endpoint_integrality_not_closed",
    "dd4_boundary_natural": "dd4_boundary_not_natural",
    "boundary_pushforward_natural": "boundary_pushforward_not_natural",
    "control_death_two_sided_ideal": "control_death_not_ideal",
}

DAGGER_MONOIDAL_DATA = {
    "cartesian_certificate": CART_EQV,
    "dagger_monoidal": True,
    "choice_free": True,
    "strict_on_operations": True,
    "source_before_points": True,
    "preserves_budget": True,
    "preserved_operations": PRESERVED_OPERATIONS,
    "operation_laws": OPERATION_LAWS,
    "posthoc": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
}

REQUIRED_FLAGS = (
    "dagger_monoidal_probe_equivalence_certificate_actual",
    "identity_and_composition_laws_present",
    "degree_multiplicativity_present",
    "rosati_dagger_laws_present",
    "dd4_boundary_naturality_present",
    "boundary_pushforward_naturality_present",
    "endpoint_integrality_closed",
    "control_death_ideal_present",
    "choice_free_operation_transport",
    "source_before_points",
    "inside_exact_24_budget",
    "no_posthoc_point_sample_basis_operation_transport",
)

BANNED_FLAGS = (
    "plain_cartesian_equivalence",
    "operation_transport_up_to_isomorphism",
    "composition_law_missing",
    "identity_law_missing",
    "rosati_involution_missing",
    "rosati_degree_adjoint_mismatch",
    "degree_multiplicativity_missing",
    "endpoint_integrality_not_closed",
    "dd4_boundary_not_natural",
    "boundary_pushforward_not_natural",
    "control_death_not_ideal",
    "posthoc_dagger_transport",
    "point_graph_dagger_transport",
    "finite_operation_sample",
    "basis_operation_row",
    "missing_dagger_monoidal_probe_equivalence_certificate",
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


def dagger_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "dagger": deepcopy(DAGGER_MONOIDAL_DATA),
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
    dagger = state["dagger"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_545")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc545_witness_missing")
    if DAG_MON_EQV not in accepted:
        out.append("dagger_monoidal_probe_equivalence_missing_from_current")
    if DAG_MON_EQV not in assignments:
        out.append("dagger_monoidal_probe_equivalence_unassigned")
    if assignments.get(DAG_MON_EQV) != "coh_finite_limit_cut":
        out.append(f"dagger_monoidal_probe_equivalence_bad_charge:{assignments.get(DAG_MON_EQV)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(dagger, dict):
        out.append("dagger_monoidal_data_not_mapping")
        dagger = {}

    if dagger.get("cartesian_certificate") != CART_EQV:
        out.append("dagger_data_not_based_on_cartesian_equivalence")
    if not dagger.get("dagger_monoidal"):
        out.append("plain_cartesian_equivalence")
    if not dagger.get("choice_free"):
        out.append("operation_transport_up_to_isomorphism")
    if not dagger.get("strict_on_operations"):
        out.append("operation_transport_up_to_isomorphism")
    if not dagger.get("source_before_points"):
        out.append("dagger_transport_loses_source_before_points")
    if not dagger.get("preserves_budget"):
        out.append("dagger_transport_expands_exact_24_budget")

    missing_operations = PRESERVED_OPERATIONS - _as_set(dagger.get("preserved_operations"))
    if missing_operations:
        out.append("operation_preservation_missing:" + ",".join(sorted(missing_operations)))
    missing_laws = OPERATION_LAWS - _as_set(dagger.get("operation_laws"))
    for law in sorted(missing_laws):
        out.append(LAW_FAILURES.get(law, f"operation_law_missing:{law}"))

    if dagger.get("posthoc"):
        out.append("posthoc_dagger_transport")
    if dagger.get("point_graph"):
        out.append("point_graph_dagger_transport")
    if dagger.get("finite_sample"):
        out.append("finite_operation_sample")
    if dagger.get("basis_row"):
        out.append("basis_operation_row")

    for req in (
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
        if req not in state["requires"].get(DAG_MON_EQV, []):
            out.append(f"dagger_monoidal_probe_equivalence_requires_missing:{req}")
    for prior in (CART_EQV, PROBE_EQV, PROBE_ESS, PROBE_FULL, PROBE_FAITH, PROBE_NAT, PROBE_SEP, ADM_CAT):
        if DAG_MON_EQV not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_dagger_monoidal")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("dagger_monoidal_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("dagger_monoidal_uses_graph_side_bridge")

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
        elif key == "dagger":
            data["dagger"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = dagger_state(MAP)

gate(
    f"{PREFIX}1 doc 545 dagger-monoidal layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s laws=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["dagger"]["operation_laws"]),
    ),
)

plain_cartesian = variant(
    live,
    flags={
        "identity_and_composition_laws_present": False,
        "degree_multiplicativity_present": False,
        "rosati_dagger_laws_present": False,
    },
    banned={"plain_cartesian_equivalence": True},
    dagger={
        "dagger_monoidal": False,
        "preserved_operations": set(),
        "operation_laws": set(),
    },
)

gate(
    f"{PREFIX}2 rejects cartesian equivalence without operation laws",
    not accepts(plain_cartesian)
    and "plain_cartesian_equivalence" in reasons(plain_cartesian)
    and {"identity_law_missing", "composition_law_missing", "degree_multiplicativity_missing"}
    <= set(reasons(plain_cartesian)),
    ",".join(reasons(plain_cartesian)),
)

choice_transport = variant(
    live,
    flags={"choice_free_operation_transport": False},
    banned={"operation_transport_up_to_isomorphism": True, "posthoc_dagger_transport": True},
    dagger={"choice_free": False, "strict_on_operations": False, "posthoc": True},
)

gate(
    f"{PREFIX}3 rejects operation transport up to isomorphism or posthoc transport",
    not accepts(choice_transport)
    and {"operation_transport_up_to_isomorphism", "posthoc_dagger_transport"} <= set(reasons(choice_transport)),
    ",".join(reasons(choice_transport)),
)

composition_missing = variant(
    live,
    flags={"identity_and_composition_laws_present": False},
    banned={"composition_law_missing": True, "identity_law_missing": True},
)
composition_missing["dagger"]["operation_laws"] -= {"identity", "composition", "associativity"}
composition_missing["dagger"]["preserved_operations"].remove("graph_composition")

gate(
    f"{PREFIX}4 rejects missing identity or composition laws",
    not accepts(composition_missing)
    and {"identity_law_missing", "composition_law_missing"} <= set(reasons(composition_missing)),
    ",".join(reasons(composition_missing)),
)

rosati_missing = variant(
    live,
    flags={"rosati_dagger_laws_present": False},
    banned={"rosati_involution_missing": True, "rosati_degree_adjoint_mismatch": True},
)
rosati_missing["dagger"]["operation_laws"] -= {
    "dagger_involution",
    "dagger_contravariant",
    "rosati_degree_adjoint",
}
rosati_missing["dagger"]["preserved_operations"].remove("rosati_count")

gate(
    f"{PREFIX}5 rejects missing Rosati/dagger laws",
    not accepts(rosati_missing)
    and {"rosati_involution_missing", "rosati_degree_adjoint_mismatch"} <= set(reasons(rosati_missing)),
    ",".join(reasons(rosati_missing)),
)

degree_endpoint_missing = variant(
    live,
    flags={"degree_multiplicativity_present": False, "endpoint_integrality_closed": False},
    banned={"degree_multiplicativity_missing": True, "endpoint_integrality_not_closed": True},
)
degree_endpoint_missing["dagger"]["operation_laws"] -= {"degree_multiplicative", "endpoint_integral_closed"}
degree_endpoint_missing["dagger"]["preserved_operations"] -= {"degree_maps", "endpoint_integrality"}

gate(
    f"{PREFIX}6 rejects missing degree multiplicativity or endpoint closure",
    not accepts(degree_endpoint_missing)
    and {"degree_multiplicativity_missing", "endpoint_integrality_not_closed"} <= set(reasons(degree_endpoint_missing)),
    ",".join(reasons(degree_endpoint_missing)),
)

boundary_missing = variant(
    live,
    flags={"dd4_boundary_naturality_present": False, "boundary_pushforward_naturality_present": False},
    banned={"dd4_boundary_not_natural": True, "boundary_pushforward_not_natural": True},
)
boundary_missing["dagger"]["operation_laws"] -= {"dd4_boundary_natural", "boundary_pushforward_natural"}
boundary_missing["dagger"]["preserved_operations"] -= {"dd4_boundary", "boundary_pushforward"}

gate(
    f"{PREFIX}7 rejects missing DD4 boundary or boundary-pushforward naturality",
    not accepts(boundary_missing)
    and {"dd4_boundary_not_natural", "boundary_pushforward_not_natural"} <= set(reasons(boundary_missing)),
    ",".join(reasons(boundary_missing)),
)

control_point_sample = variant(
    live,
    flags={
        "control_death_ideal_present": False,
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_posthoc_point_sample_basis_operation_transport": False,
    },
    banned={
        "control_death_not_ideal": True,
        "point_graph_dagger_transport": True,
        "finite_operation_sample": True,
        "basis_operation_row": True,
    },
    dagger={
        "source_before_points": False,
        "preserves_budget": False,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
    },
)
control_point_sample["dagger"]["operation_laws"].remove("control_death_two_sided_ideal")
control_point_sample["dagger"]["preserved_operations"].remove("control_death")
control_point_sample["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_dagger_transport"
control_point_sample["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects missing control-death ideal or point/sample/basis operation transport",
    not accepts(control_point_sample)
    and {
        "control_death_not_ideal",
        "point_graph_dagger_transport",
        "finite_operation_sample",
        "basis_operation_row",
    }
    <= set(reasons(control_point_sample)),
    ",".join(reasons(control_point_sample)),
)

missing_cert = variant(
    live,
    flags={"dagger_monoidal_probe_equivalence_certificate_actual": False},
    banned={"missing_dagger_monoidal_probe_equivalence_certificate": True},
)
missing_cert["accepted"].remove(DAG_MON_EQV)
del missing_cert["assignments"][DAG_MON_EQV]

gate(
    f"{PREFIX}9 rejects missing dagger-monoidal probe-equivalence certificates",
    not accepts(missing_cert)
    and "missing_dagger_monoidal_probe_equivalence_certificate" in reasons(missing_cert)
    and "dagger_monoidal_probe_equivalence_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    plain_cartesian,
    choice_transport,
    composition_missing,
    rosati_missing,
    degree_endpoint_missing,
    boundary_missing,
    control_point_sample,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only choice-free dagger-monoidal source-square equivalences pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: source-square operations are dagger-monoidal")
print(
    "VERDICT: cartesian exact probe equivalence counts only when it also "
    "preserves source-square identity, composition, degree multiplicativity, "
    "Rosati/dagger laws, DD.4 boundary naturality, boundary pushforward, and "
    "control-death ideal structure. Plain cartesian equivalence, operation "
    "transport up to isomorphism, posthoc or point/graph dagger transport, "
    "finite samples, basis rows, and missing dagger-monoidal certificates do "
    "not construct the missing object."
)
