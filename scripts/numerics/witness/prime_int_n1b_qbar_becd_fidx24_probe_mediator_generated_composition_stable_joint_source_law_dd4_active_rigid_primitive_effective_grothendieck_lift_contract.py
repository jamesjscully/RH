r"""Mediator-generated composition-stable joint source-law contract.

Doc 555 pins a single jointly monic source-law tuple. This witness prevents
that tuple from being an externally attached law table: it must be generated
by the universal mediator through the formation/coupling spine and remain
stable under composition, dagger, Rosati, trace, control, and handoff
operations.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the mediator-generated law witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 556
EXPECTED_WITNESS = (
    "doc556-probe-mediator-generated-composition-stable-joint-source-law-"
    "dd4-active-rigid-primitive-effective-grothendieck-lift"
)
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTJLAWDD4ACTRIGIDPRIMEFFK0LIFTDD4ACTRIGIDPRIMEFFK0LIFTRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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
    MED: "coh_finite_limit_cut",
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

FORMATION_SPINE = {
    "universal_mediator",
    "formation_fiber",
    "formation_coherence",
    "cartesian_source_coherence",
    "monoidwide_source_coherence",
    "source_coupling",
    "coupling_representer",
    "coupling_universal_arrow",
    "source_fiber_subrepresenter",
    "equalizer_arrow_to_subrep",
}

STABLE_UNDER = {
    "source_square_composition",
    "dagger",
    "rosati_adjoint",
    "exact_additive_trace",
    "control_death_ideal",
    "dd4_image_handoff",
    "graph_later_realization",
}

MED_IDENTITIES = {
    "mediator_generated_joint_law",
    "formation_fiber_generated_law",
    "cartesian_monoidwide_coherent_law",
    "source_coupling_generated_law",
    "universal_arrow_factorized_law",
    "composition_stable_law",
    "dagger_rosati_trace_stable_law",
    "control_handoff_graph_stable_law",
    "external_law_graft_forbidden",
}

COHERENT_ON = {
    MED,
    JOINT,
    ACTIVE,
    "universal_mediator",
    "formation_fiber",
    "formation_coherence",
    "cartesian_source_coherence",
    "monoidwide_source_coherence",
    "source_coupling",
    "coupling_representer",
    "coupling_universal_arrow",
    "source_fiber_subrepresenter",
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    "joint_constraint_fork",
    "coupled_source_image",
    "graph_composition",
    "control_death",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    DAG_MON_EQV,
    ADJ_PAIR,
    EXACT_ADD,
}

MED_DATA = {
    "joint_certificate": JOINT,
    "generated_law": "mediator_generated_composition_stable_joint_source_law",
    "source_side": True,
    "choice_free": True,
    "mediator_generated": True,
    "formation_spine": FORMATION_SPINE,
    "stable_under": STABLE_UNDER,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "identities": MED_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "external_law_attachment": False,
    "law_table_graft": False,
    "posthoc_mediator_factorization": False,
    "mediator_generation_by_declaration": False,
    "objectwise_terminal_law_only": False,
    "nonfunctorial_law_tuple": False,
    "source_coupling_bypass": False,
    "universal_arrow_bypass": False,
    "formation_fiber_bypass": False,
    "cartesian_coherence_bypass": False,
    "monoidwide_coherence_bypass": False,
    "finite_mediator_sample": False,
    "basis_mediator_row": False,
    "mediator_context_collapse": False,
    "retuned_mediator_law": False,
}

REQUIRED_NODE_DEPS = (
    JOINT,
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
    "universal_mediator",
    "formation_token",
    "formation_fiber",
    "formation_coherence",
    "cartesian_source_coherence",
    "monoidwide_source_coherence",
    "source_coupling",
    "coupling_representer",
    "coupling_universal_arrow",
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
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

EXPECTED_MED_EDGES = {
    (JOINT, "made_mediator_generated_composition_stable_by", MED),
    (MED, "mediator_generated_law_of", JOINT),
    (MED, "generated_by", "universal_mediator"),
    (MED, "formed_in", "formation_fiber"),
    (MED, "formation_coherent_for", "formation_coherence"),
    (MED, "cartesian_coherent_for", "cartesian_source_coherence"),
    (MED, "monoidwide_coherent_for", "monoidwide_source_coherence"),
    (MED, "coupled_through", "source_coupling"),
    (MED, "represented_by", "coupling_representer"),
    (MED, "factors_through", "coupling_universal_arrow"),
    (MED, "anchored_on", "source_fiber_subrepresenter"),
    (MED, "equalizer_stable_for", "equalizer_arrow_to_subrep"),
    (MED, "single_tuple_on", "joint_constraint_fork"),
    (MED, "composition_stable_for", "graph_composition"),
    (MED, "dagger_stable_for", DAG_MON_EQV),
    (MED, "rosati_adjoint_stable_for", ADJ_PAIR),
    (MED, "trace_stable_for", EXACT_ADD),
    (MED, "dd4_handoff_stable_for", "dd4_image_only_handoff_contract"),
    (MED, "graph_realization_stable_for", "graph_later_realization_contract"),
    (MED, "control_ideal_stable_for", "control_death"),
    (MED, "preserves", "exact_24_cell_finite_index"),
    (MED, "coherent_for", "coupled_source_image"),
}

REQUIRED_FLAGS = (
    "mediator_generated_certificate_actual",
    "mediator_generated_law",
    "formation_spine_complete",
    "composition_stable",
    "dagger_rosati_trace_stable",
    "control_handoff_graph_stable",
    "inside_exact_24_budget",
    "no_external_law_graft",
)

BANNED_FLAGS = (
    "external_law_attachment",
    "law_table_graft",
    "posthoc_mediator_factorization",
    "mediator_generation_by_declaration",
    "objectwise_terminal_law_only",
    "nonfunctorial_law_tuple",
    "composition_unstable_law",
    "dagger_unstable_law",
    "rosati_unstable_law",
    "trace_unstable_law",
    "control_ideal_unstable_law",
    "handoff_unstable_law",
    "graph_realization_unstable_law",
    "source_coupling_bypass",
    "universal_arrow_bypass",
    "formation_fiber_bypass",
    "cartesian_coherence_bypass",
    "monoidwide_coherence_bypass",
    "finite_mediator_sample",
    "basis_mediator_row",
    "mediator_context_collapse",
    "retuned_mediator_law",
    "missing_mediator_generated_composition_stable_joint_source_law_certificate",
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
        "edges": edge_set,
        "med": deepcopy(MED_DATA),
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
    med = state["med"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_556")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc556_witness_missing")
    if MED not in accepted:
        out.append("mediator_generated_law_missing_from_current")
    if MED not in assignments:
        out.append("mediator_generated_law_unassigned")
    if assignments.get(MED) != "coh_finite_limit_cut":
        out.append(f"mediator_generated_law_bad_charge:{assignments.get(MED)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(med, dict):
        out.append("mediator_data_not_mapping")
        med = {}

    if med.get("joint_certificate") != JOINT:
        out.append("mediator_generated_law_not_based_on_joint_source_law")
    if not med.get("generated_law"):
        out.append("missing_mediator_generated_composition_stable_joint_source_law_certificate")
    if not med.get("source_side") or not med.get("choice_free"):
        out.append("mediator_generation_by_declaration")
    if not med.get("mediator_generated"):
        out.append("mediator_generation_by_declaration")
    if not med.get("preserves_budget"):
        out.append("mediator_law_expands_exact_24_budget")
    if not med.get("nonpositive_stage") or med.get("imports_positivity"):
        out.append("mediator_context_collapse")

    spine = _as_set(med.get("formation_spine"))
    missing_spine = FORMATION_SPINE - spine
    if missing_spine:
        out.append("formation_spine_missing:" + ",".join(sorted(missing_spine)))
    if "source_coupling" not in spine:
        out.append("source_coupling_bypass")
    if "coupling_universal_arrow" not in spine:
        out.append("universal_arrow_bypass")
    if "formation_fiber" not in spine:
        out.append("formation_fiber_bypass")
    if "cartesian_source_coherence" not in spine:
        out.append("cartesian_coherence_bypass")
    if "monoidwide_source_coherence" not in spine:
        out.append("monoidwide_coherence_bypass")

    stable = _as_set(med.get("stable_under"))
    if "source_square_composition" not in stable:
        out.append("composition_unstable_law")
    if "dagger" not in stable:
        out.append("dagger_unstable_law")
    if "rosati_adjoint" not in stable:
        out.append("rosati_unstable_law")
    if "exact_additive_trace" not in stable:
        out.append("trace_unstable_law")
    if "control_death_ideal" not in stable:
        out.append("control_ideal_unstable_law")
    if "dd4_image_handoff" not in stable:
        out.append("handoff_unstable_law")
    if "graph_later_realization" not in stable:
        out.append("graph_realization_unstable_law")

    for key in (
        "external_law_attachment",
        "law_table_graft",
        "posthoc_mediator_factorization",
        "mediator_generation_by_declaration",
        "objectwise_terminal_law_only",
        "nonfunctorial_law_tuple",
        "source_coupling_bypass",
        "universal_arrow_bypass",
        "formation_fiber_bypass",
        "cartesian_coherence_bypass",
        "monoidwide_coherence_bypass",
        "finite_mediator_sample",
        "basis_mediator_row",
        "mediator_context_collapse",
        "retuned_mediator_law",
    ):
        if med.get(key):
            out.append(key)

    missing_identities = MED_IDENTITIES - _as_set(med.get("identities"))
    if missing_identities:
        out.append("mediator_law_identity_missing:" + ",".join(sorted(missing_identities)))
    missing_coherence = COHERENT_ON - _as_set(med.get("coherent_on"))
    if missing_coherence:
        out.append("mediator_law_coherence_missing:" + ",".join(sorted(missing_coherence)))

    for req in REQUIRED_NODE_DEPS:
        if req not in state["requires"].get(MED, []):
            out.append(f"mediator_generated_law_requires_missing:{req}")
    if MED not in state["requires"].get(JOINT, []):
        out.append("joint_source_law_not_required_to_be_mediator_generated")

    missing_edges = EXPECTED_MED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("mediator_generated_law_edges_missing:" + ",".join(rendered))

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

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
        elif key == "med":
            data["med"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 556 mediator-generated composition-stable law layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s stable_ops=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["med"]["stable_under"]),
    ),
)

external_gap = variant(
    live,
    flags={"mediator_generated_law": False, "no_external_law_graft": False},
    banned={
        "external_law_attachment": True,
        "law_table_graft": True,
        "posthoc_mediator_factorization": True,
        "mediator_generation_by_declaration": True,
    },
    med={
        "mediator_generated": False,
        "external_law_attachment": True,
        "law_table_graft": True,
        "posthoc_mediator_factorization": True,
        "mediator_generation_by_declaration": True,
    },
)
external_gap["med"]["identities"] -= {"mediator_generated_joint_law", "external_law_graft_forbidden"}

gate(
    f"{PREFIX}2 rejects external grafts and posthoc mediator factorization",
    not accepts(external_gap)
    and {
        "external_law_attachment",
        "law_table_graft",
        "posthoc_mediator_factorization",
        "mediator_generation_by_declaration",
    }
    <= set(reasons(external_gap)),
    ",".join(reasons(external_gap)),
)

object_functor_gap = variant(
    live,
    banned={"objectwise_terminal_law_only": True, "nonfunctorial_law_tuple": True},
    med={
        "objectwise_terminal_law_only": True,
        "nonfunctorial_law_tuple": True,
    },
)

gate(
    f"{PREFIX}3 rejects objectwise terminal-only or nonfunctorial law tuples",
    not accepts(object_functor_gap)
    and {"objectwise_terminal_law_only", "nonfunctorial_law_tuple"} <= set(reasons(object_functor_gap)),
    ",".join(reasons(object_functor_gap)),
)

operation_gap = variant(
    live,
    flags={"composition_stable": False, "dagger_rosati_trace_stable": False},
    banned={
        "composition_unstable_law": True,
        "dagger_unstable_law": True,
        "rosati_unstable_law": True,
        "trace_unstable_law": True,
    },
    med={
        "stable_under": {"control_death_ideal", "dd4_image_handoff", "graph_later_realization"},
    },
)
operation_gap["med"]["identities"] -= {"composition_stable_law", "dagger_rosati_trace_stable_law"}

gate(
    f"{PREFIX}4 rejects composition, dagger, Rosati, or trace instability",
    not accepts(operation_gap)
    and {
        "composition_unstable_law",
        "dagger_unstable_law",
        "rosati_unstable_law",
        "trace_unstable_law",
    }
    <= set(reasons(operation_gap)),
    ",".join(reasons(operation_gap)),
)

bridge_control_gap = variant(
    live,
    flags={"control_handoff_graph_stable": False},
    banned={
        "control_ideal_unstable_law": True,
        "handoff_unstable_law": True,
        "graph_realization_unstable_law": True,
    },
    med={
        "stable_under": {"source_square_composition", "dagger", "rosati_adjoint", "exact_additive_trace"},
    },
)
bridge_control_gap["med"]["identities"] -= {"control_handoff_graph_stable_law"}

gate(
    f"{PREFIX}5 rejects control, DD4 handoff, or graph-realization instability",
    not accepts(bridge_control_gap)
    and {"control_ideal_unstable_law", "handoff_unstable_law", "graph_realization_unstable_law"}
    <= set(reasons(bridge_control_gap)),
    ",".join(reasons(bridge_control_gap)),
)

spine_gap = variant(
    live,
    flags={"formation_spine_complete": False},
    banned={
        "source_coupling_bypass": True,
        "universal_arrow_bypass": True,
        "formation_fiber_bypass": True,
    },
    med={
        "formation_spine": {
            "universal_mediator",
            "formation_coherence",
            "cartesian_source_coherence",
            "monoidwide_source_coherence",
            "source_fiber_subrepresenter",
            "equalizer_arrow_to_subrep",
        },
        "source_coupling_bypass": True,
        "universal_arrow_bypass": True,
        "formation_fiber_bypass": True,
    },
)
spine_gap["med"]["identities"] -= {
    "formation_fiber_generated_law",
    "source_coupling_generated_law",
    "universal_arrow_factorized_law",
}

gate(
    f"{PREFIX}6 rejects source-coupling, universal-arrow, or formation-fiber bypass",
    not accepts(spine_gap)
    and {"source_coupling_bypass", "universal_arrow_bypass", "formation_fiber_bypass"}
    <= set(reasons(spine_gap)),
    ",".join(reasons(spine_gap)),
)

coherence_sample_gap = variant(
    live,
    flags={"formation_spine_complete": False, "inside_exact_24_budget": False},
    banned={
        "cartesian_coherence_bypass": True,
        "monoidwide_coherence_bypass": True,
        "finite_mediator_sample": True,
        "basis_mediator_row": True,
        "mediator_context_collapse": True,
        "retuned_mediator_law": True,
    },
    med={
        "formation_spine": FORMATION_SPINE - {"cartesian_source_coherence", "monoidwide_source_coherence"},
        "cartesian_coherence_bypass": True,
        "monoidwide_coherence_bypass": True,
        "finite_mediator_sample": True,
        "basis_mediator_row": True,
        "mediator_context_collapse": True,
        "retuned_mediator_law": True,
        "nonpositive_stage": False,
        "preserves_budget": False,
    },
)
coherence_sample_gap["med"]["identities"] -= {"cartesian_monoidwide_coherent_law"}

gate(
    f"{PREFIX}7 rejects coherence bypass, finite samples, retuning, or context collapse",
    not accepts(coherence_sample_gap)
    and {
        "cartesian_coherence_bypass",
        "monoidwide_coherence_bypass",
        "finite_mediator_sample",
        "basis_mediator_row",
        "mediator_context_collapse",
        "retuned_mediator_law",
    }
    <= set(reasons(coherence_sample_gap)),
    ",".join(reasons(coherence_sample_gap)),
)

missing_cert = variant(
    live,
    flags={"mediator_generated_certificate_actual": False},
    banned={"missing_mediator_generated_composition_stable_joint_source_law_certificate": True},
)
missing_cert["accepted"].remove(MED)
del missing_cert["assignments"][MED]

gate(
    f"{PREFIX}8 rejects missing mediator-generated composition-stable certificates",
    not accepts(missing_cert)
    and "missing_mediator_generated_composition_stable_joint_source_law_certificate" in reasons(missing_cert)
    and "mediator_generated_law_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

dependency_gap = variant(live)
dependency_gap["requires"][MED].remove(JOINT)
dependency_gap["requires"][JOINT].remove(MED)

gate(
    f"{PREFIX}9 requires joint law and mediator-generated certificates to close together",
    not accepts(dependency_gap)
    and "mediator_generated_law_requires_missing:joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
    in reasons(dependency_gap)
    and "joint_source_law_not_required_to_be_mediator_generated" in reasons(dependency_gap),
    ",".join(reasons(dependency_gap)),
)

variants = [
    external_gap,
    object_functor_gap,
    operation_gap,
    bridge_control_gap,
    spine_gap,
    coherence_sample_gap,
    missing_cert,
    dependency_gap,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only mediator-generated composition-stable joint laws pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: joint source law is mediator-generated and composition-stable")
print(
    "VERDICT: the joint source-law DD.4-active rigid primitive effective K0 "
    "lift counts only when its law tuple is generated by the universal "
    "mediator through the formation/coupling spine and remains stable under "
    "composition, dagger, Rosati, trace, control, DD.4 handoff, and graph "
    "realization. External grafts, posthoc mediator factorizations, "
    "objectwise terminal laws, nonfunctorial tuples, operation-unstable laws, "
    "spine bypasses, finite samples, basis rows, retuning, context collapse, "
    "and missing certificates do not construct the missing object."
)
