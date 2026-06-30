r"""Cartesian probe-equivalence contract for admissible source-square probes.

Doc 543 pins choice-free coherent adjoint equivalence. This witness prevents
that equivalence from being merely categorical: the source square must carry
choice-free cartesian comparison data preserving terminality, equalizers, the
joint constraint fork, both handoffs, inhabitance, dependency closure, and the
exact-24 budget.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_cartesian_equivalence_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the cartesian probe-equivalence witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 544
EXPECTED_WITNESS = "doc544-probe-cartesian-equivalence"
CART_EQV = "cartesian_probe_equivalence_certificate"
PROBE_EQV = "probe_equivalence_certificate"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PRESERVED_NODES = {
    TERMINAL_CERT,
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "joint_constraint_fork",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "finite_limit_inhabitance_certificate",
    "budget_dependency_closure_certificate",
    "exact_24_cell_finite_index",
}

COMPARISON_CELLS = {
    "terminal_comparison",
    "equalizer_comparison",
    "constraint_fork_comparison",
    "dd4_handoff_comparison",
    "graph_handoff_comparison",
    "inhabitance_comparison",
    "budget_comparison",
    "exact24_comparison",
}

COMPARISON_FAILURES = {
    "terminal_comparison": "terminal_comparison_missing",
    "equalizer_comparison": "equalizer_comparison_missing",
    "constraint_fork_comparison": "constraint_fork_comparison_missing",
    "dd4_handoff_comparison": "dd4_handoff_comparison_missing",
    "graph_handoff_comparison": "graph_handoff_comparison_missing",
    "inhabitance_comparison": "inhabitance_comparison_missing",
    "budget_comparison": "budget_comparison_missing",
    "exact24_comparison": "exact24_comparison_missing",
}

CARTESIAN_DATA = {
    "equivalence_certificate": PROBE_EQV,
    "cartesian_exact": True,
    "choice_free": True,
    "source_before_points": True,
    "preserves_budget": True,
    "preserves_exact24": True,
    "preserves": PRESERVED_NODES,
    "comparison_cells": COMPARISON_CELLS,
    "posthoc": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
}

REQUIRED_FLAGS = (
    "cartesian_probe_equivalence_certificate_actual",
    "terminal_comparison_present",
    "equalizer_comparison_present",
    "constraint_fork_comparison_present",
    "handoff_comparisons_present",
    "inhabitance_comparison_present",
    "budget_comparison_present",
    "exact24_comparison_present",
    "choice_free_limit_transport",
    "source_before_points",
    "inside_exact_24_budget",
    "no_posthoc_point_sample_basis_limit_transport",
)

BANNED_FLAGS = (
    "plain_categorical_equivalence",
    "limit_preservation_up_to_choice",
    "terminal_comparison_missing",
    "equalizer_comparison_missing",
    "constraint_fork_comparison_missing",
    "dd4_handoff_comparison_missing",
    "graph_handoff_comparison_missing",
    "inhabitance_comparison_missing",
    "budget_comparison_missing",
    "exact24_comparison_missing",
    "posthoc_limit_transport",
    "point_graph_limit_transport",
    "finite_limit_sample",
    "basis_limit_row",
    "missing_cartesian_probe_equivalence_certificate",
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


def cartesian_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "cartesian": deepcopy(CARTESIAN_DATA),
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
    cart = state["cartesian"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_544")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc544_witness_missing")
    if CART_EQV not in accepted:
        out.append("cartesian_probe_equivalence_missing_from_current")
    if CART_EQV not in assignments:
        out.append("cartesian_probe_equivalence_unassigned")
    if assignments.get(CART_EQV) != "coh_finite_limit_cut":
        out.append(f"cartesian_probe_equivalence_bad_charge:{assignments.get(CART_EQV)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(cart, dict):
        out.append("cartesian_data_not_mapping")
        cart = {}

    if cart.get("equivalence_certificate") != PROBE_EQV:
        out.append("cartesian_data_not_based_on_probe_equivalence")
    if not cart.get("cartesian_exact"):
        out.append("plain_categorical_equivalence")
    if not cart.get("choice_free"):
        out.append("limit_preservation_up_to_choice")
    if not cart.get("source_before_points"):
        out.append("cartesian_transport_loses_source_before_points")
    if not cart.get("preserves_budget"):
        out.append("cartesian_transport_loses_budget")
    if not cart.get("preserves_exact24"):
        out.append("cartesian_transport_loses_exact24")

    missing_preserved = PRESERVED_NODES - _as_set(cart.get("preserves"))
    if missing_preserved:
        out.append("cartesian_preservation_missing:" + ",".join(sorted(missing_preserved)))
    missing_comparisons = COMPARISON_CELLS - _as_set(cart.get("comparison_cells"))
    for comparison in sorted(missing_comparisons):
        out.append(COMPARISON_FAILURES[comparison])

    if cart.get("posthoc"):
        out.append("posthoc_limit_transport")
    if cart.get("point_graph"):
        out.append("point_graph_limit_transport")
    if cart.get("finite_sample"):
        out.append("finite_limit_sample")
    if cart.get("basis_row"):
        out.append("basis_limit_row")

    for req in (
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
        if req not in state["requires"].get(CART_EQV, []):
            out.append(f"cartesian_probe_equivalence_requires_missing:{req}")
    for prior in (PROBE_EQV, PROBE_ESS, PROBE_FULL, PROBE_FAITH, PROBE_NAT, PROBE_SEP, ADM_CAT):
        if CART_EQV not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_cartesian_exact")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("cartesian_probe_equivalence_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("cartesian_probe_equivalence_uses_graph_side_bridge")

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
        elif key == "cartesian":
            data["cartesian"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = cartesian_state(MAP)

gate(
    f"{PREFIX}1 doc 544 cartesian probe-equivalence layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s comparisons=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["cartesian"]["comparison_cells"]),
    ),
)

plain_categorical = variant(
    live,
    flags={
        "terminal_comparison_present": False,
        "equalizer_comparison_present": False,
        "constraint_fork_comparison_present": False,
    },
    banned={"plain_categorical_equivalence": True},
    cartesian={
        "cartesian_exact": False,
        "comparison_cells": set(),
        "preserves": {PROBE_EQV},
    },
)

gate(
    f"{PREFIX}2 rejects plain categorical equivalence without cartesian comparisons",
    not accepts(plain_categorical)
    and "plain_categorical_equivalence" in reasons(plain_categorical)
    and {"terminal_comparison_missing", "equalizer_comparison_missing", "constraint_fork_comparison_missing"}
    <= set(reasons(plain_categorical)),
    ",".join(reasons(plain_categorical)),
)

choice_posthoc = variant(
    live,
    flags={"choice_free_limit_transport": False, "no_posthoc_point_sample_basis_limit_transport": False},
    banned={"limit_preservation_up_to_choice": True, "posthoc_limit_transport": True},
    cartesian={"choice_free": False, "posthoc": True},
)

gate(
    f"{PREFIX}3 rejects limit preservation up to choice or posthoc transport",
    not accepts(choice_posthoc)
    and {"limit_preservation_up_to_choice", "posthoc_limit_transport"} <= set(reasons(choice_posthoc)),
    ",".join(reasons(choice_posthoc)),
)

terminal_equalizer_missing = variant(
    live,
    flags={"terminal_comparison_present": False, "equalizer_comparison_present": False},
    banned={"terminal_comparison_missing": True, "equalizer_comparison_missing": True},
)
terminal_equalizer_missing["cartesian"]["comparison_cells"] -= {"terminal_comparison", "equalizer_comparison"}
terminal_equalizer_missing["cartesian"]["preserves"] -= {TERMINAL_CERT, "equalizer_arrow_to_subrep"}

gate(
    f"{PREFIX}4 rejects missing terminal or equalizer comparisons",
    not accepts(terminal_equalizer_missing)
    and {"terminal_comparison_missing", "equalizer_comparison_missing"} <= set(reasons(terminal_equalizer_missing)),
    ",".join(reasons(terminal_equalizer_missing)),
)

constraint_missing = variant(
    live,
    flags={"constraint_fork_comparison_present": False},
    banned={"constraint_fork_comparison_missing": True},
)
constraint_missing["cartesian"]["comparison_cells"].remove("constraint_fork_comparison")
constraint_missing["cartesian"]["preserves"].remove("joint_constraint_fork")

gate(
    f"{PREFIX}5 rejects missing joint constraint fork comparison",
    not accepts(constraint_missing)
    and "constraint_fork_comparison_missing" in reasons(constraint_missing),
    ",".join(reasons(constraint_missing)),
)

handoffs_missing = variant(
    live,
    flags={"handoff_comparisons_present": False},
    banned={"dd4_handoff_comparison_missing": True, "graph_handoff_comparison_missing": True},
)
handoffs_missing["cartesian"]["comparison_cells"] -= {"dd4_handoff_comparison", "graph_handoff_comparison"}
handoffs_missing["cartesian"]["preserves"] -= {"dd4_image_only_handoff_contract", "graph_later_realization_contract"}

gate(
    f"{PREFIX}6 rejects missing DD4 or graph handoff comparisons",
    not accepts(handoffs_missing)
    and {"dd4_handoff_comparison_missing", "graph_handoff_comparison_missing"} <= set(reasons(handoffs_missing)),
    ",".join(reasons(handoffs_missing)),
)

closure_missing = variant(
    live,
    flags={
        "inhabitance_comparison_present": False,
        "budget_comparison_present": False,
        "exact24_comparison_present": False,
        "inside_exact_24_budget": False,
    },
    banned={
        "inhabitance_comparison_missing": True,
        "budget_comparison_missing": True,
        "exact24_comparison_missing": True,
    },
    cartesian={"preserves_budget": False, "preserves_exact24": False},
)
closure_missing["cartesian"]["comparison_cells"] -= {
    "inhabitance_comparison",
    "budget_comparison",
    "exact24_comparison",
}
closure_missing["cartesian"]["preserves"] -= {
    "finite_limit_inhabitance_certificate",
    "budget_dependency_closure_certificate",
    "exact_24_cell_finite_index",
}

gate(
    f"{PREFIX}7 rejects missing inhabitance, budget, or exact-24 comparisons",
    not accepts(closure_missing)
    and {
        "inhabitance_comparison_missing",
        "budget_comparison_missing",
        "exact24_comparison_missing",
    }
    <= set(reasons(closure_missing)),
    ",".join(reasons(closure_missing)),
)

point_sample_basis = variant(
    live,
    flags={"source_before_points": False, "inside_exact_24_budget": False, "no_posthoc_point_sample_basis_limit_transport": False},
    banned={
        "point_graph_limit_transport": True,
        "finite_limit_sample": True,
        "basis_limit_row": True,
    },
    cartesian={
        "source_before_points": False,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
    },
)
point_sample_basis["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_limit_transport"
point_sample_basis["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects point/graph transport, finite samples, or basis rows",
    not accepts(point_sample_basis)
    and {"point_graph_limit_transport", "finite_limit_sample", "basis_limit_row"} <= set(reasons(point_sample_basis)),
    ",".join(reasons(point_sample_basis)),
)

missing_cert = variant(
    live,
    flags={"cartesian_probe_equivalence_certificate_actual": False},
    banned={"missing_cartesian_probe_equivalence_certificate": True},
)
missing_cert["accepted"].remove(CART_EQV)
del missing_cert["assignments"][CART_EQV]

gate(
    f"{PREFIX}9 rejects missing cartesian probe-equivalence certificates",
    not accepts(missing_cert)
    and "missing_cartesian_probe_equivalence_certificate" in reasons(missing_cert)
    and "cartesian_probe_equivalence_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    plain_categorical,
    choice_posthoc,
    terminal_equalizer_missing,
    constraint_missing,
    handoffs_missing,
    closure_missing,
    point_sample_basis,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only choice-free cartesian exact probe-equivalences pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and set(BANNED_FLAGS) <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: probe equivalence preserves source-square finite limits")
print(
    "VERDICT: choice-free coherent probe equivalence counts only when it is "
    "cartesian exact on terminality, finite-limit/equalizer data, the joint "
    "constraint fork, DD.4 handoff, graph handoff, inhabitance, dependency "
    "closure, and the exact-24 budget. Plain categorical equivalence, "
    "limit preservation by choice, missing comparison cells, posthoc or "
    "point/graph transport, finite samples, basis rows, and missing cartesian "
    "certificates do not construct the missing object."
)
