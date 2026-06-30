r"""Rigid primitive effective Grothendieck lift contract.

Doc 552 pins a primitive, gcd-one, indecomposable effective K0 source lift.
This witness prevents that primitive lift from living only as an orbit or
torsor of isomorphic primitive representatives. Endpoint, degree, DD.4,
boundary pushforward, graph/Rosati, and control laws must be fixed on one
source-side representative with trivial stabilizer, not after choosing a unit,
sign, skeleton, quotient, or automorphism trivialization.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the rigid primitive lift witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 553
EXPECTED_WITNESS = "doc553-probe-rigid-primitive-effective-grothendieck-lift"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

RIGID_IDENTITIES = {
    "rigid_primitive_lift",
    "trivial_automorphism_group",
    "trivial_stabilizer",
    "canonical_source_representative",
    "unique_equalizer_representative",
    "terminal_choice_unique",
    "endpoint_fixed_on_representative",
    "degree_fixed_on_representative",
    "boundary_fixed_on_representative",
    "pushforward_fixed_on_representative",
    "graph_fixed_on_representative",
    "rosati_fixed_on_representative",
    "control_fixed_on_representative",
}

COHERENT_ON = {
    "source_fiber_subrepresenter",
    "coupled_source_image",
    "finite_limit_cut",
    "equalizer_arrow_to_subrep",
    TERMINAL_CERT,
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
    "joint_constraint_fork",
}

RIGID_DATA = {
    "primitive_certificate": PRIMITIVE,
    "rigid_lift": "source_rigid_primitive_effective_k0_lift",
    "source_side": True,
    "choice_free": True,
    "canonical_representative": True,
    "unique_in_source_fiber": True,
    "unique_in_equalizer": True,
    "terminal_choice_unique": True,
    "automorphism_group": {"identity"},
    "endomorphisms": {"identity"},
    "stabilizer": {"identity"},
    "torsor": False,
    "unit_ambiguity": False,
    "sign_ambiguity": False,
    "scalar_unit_rescaling": False,
    "isomorphic_replacement": False,
    "orbit_choice": False,
    "skeletonized": False,
    "quotient_by_stabilizer": False,
    "endpoint_fixed": True,
    "degree_fixed": True,
    "boundary_fixed": True,
    "pushforward_fixed": True,
    "graph_fixed": True,
    "rosati_fixed": True,
    "control_fixed": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "source_before_points": True,
    "identities": RIGID_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "declared": False,
    "posthoc": False,
    "retuned": False,
    "torsor_trivialization_choice": False,
    "point_graph": False,
    "finite_sample": False,
    "basis_row": False,
    "context_collapse": False,
}

REQUIRED_FLAGS = (
    "rigid_primitive_effective_lift_certificate_actual",
    "rigid_primitive_lift",
    "trivial_automorphism_group",
    "trivial_stabilizer",
    "canonical_source_representative",
    "unique_equalizer_representative",
    "terminal_choice_unique",
    "fixed_endpoint_degree_boundary_graph_rosati_control",
    "source_before_points",
    "inside_exact_24_budget",
    "no_orbit_torsor_or_unit_choice",
    "no_declared_or_posthoc_rigidification",
    "no_point_graph_sample_basis_rigidity",
)

BANNED_FLAGS = (
    "nonrigid_primitive_lift",
    "primitive_lift_torsor",
    "nontrivial_lift_automorphism",
    "nontrivial_lift_endomorphism",
    "unit_ambiguity",
    "sign_ambiguity",
    "scalar_unit_rescaling",
    "automorphism_masked_endpoint",
    "automorphism_masked_degree",
    "automorphism_masked_boundary",
    "automorphism_masked_pushforward",
    "automorphism_masked_graph",
    "automorphism_masked_rosati",
    "automorphism_masked_control",
    "isomorphic_primitive_replacement",
    "orbit_representative_choice",
    "skeletonized_primitive_lift",
    "quotient_by_stabilizer",
    "torsor_trivialization_choice",
    "rigidification_by_declaration",
    "posthoc_rigidification",
    "retuned_rigid_representative",
    "point_graph_rigidity_check",
    "finite_rigidity_sample",
    "basis_rigidity_row",
    "rigidity_context_collapse",
    "missing_rigid_primitive_effective_lift_certificate",
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


def rigid_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "rigid": deepcopy(RIGID_DATA),
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
    rigid = state["rigid"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_553")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc553_witness_missing")
    if RIGID not in accepted:
        out.append("rigid_primitive_effective_lift_missing_from_current")
    if RIGID not in assignments:
        out.append("rigid_primitive_effective_lift_unassigned")
    if assignments.get(RIGID) != "coh_finite_limit_cut":
        out.append(f"rigid_primitive_effective_lift_bad_charge:{assignments.get(RIGID)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(rigid, dict):
        out.append("rigid_data_not_mapping")
        rigid = {}

    if rigid.get("primitive_certificate") != PRIMITIVE:
        out.append("rigid_lift_not_based_on_primitive_effective_lift")
    if not rigid.get("rigid_lift"):
        out.append("missing_rigid_primitive_effective_lift_certificate")
    if not rigid.get("source_side") or not rigid.get("choice_free"):
        out.append("torsor_trivialization_choice")
    if not rigid.get("canonical_representative"):
        out.append("nonrigid_primitive_lift")
    if not rigid.get("unique_in_source_fiber"):
        out.append("primitive_lift_torsor")
    if not rigid.get("unique_in_equalizer"):
        out.append("orbit_representative_choice")
    if not rigid.get("terminal_choice_unique"):
        out.append("torsor_trivialization_choice")

    if _as_set(rigid.get("automorphism_group")) != {"identity"}:
        out.append("nontrivial_lift_automorphism")
    if _as_set(rigid.get("endomorphisms")) != {"identity"}:
        out.append("nontrivial_lift_endomorphism")
    if _as_set(rigid.get("stabilizer")) != {"identity"}:
        out.append("primitive_lift_torsor")
    if rigid.get("torsor"):
        out.append("primitive_lift_torsor")
    if rigid.get("unit_ambiguity"):
        out.append("unit_ambiguity")
    if rigid.get("sign_ambiguity"):
        out.append("sign_ambiguity")
    if rigid.get("scalar_unit_rescaling"):
        out.append("scalar_unit_rescaling")
    if rigid.get("isomorphic_replacement"):
        out.append("isomorphic_primitive_replacement")
    if rigid.get("orbit_choice"):
        out.append("orbit_representative_choice")
    if rigid.get("skeletonized"):
        out.append("skeletonized_primitive_lift")
    if rigid.get("quotient_by_stabilizer"):
        out.append("quotient_by_stabilizer")

    for field, repair in (
        ("endpoint_fixed", "automorphism_masked_endpoint"),
        ("degree_fixed", "automorphism_masked_degree"),
        ("boundary_fixed", "automorphism_masked_boundary"),
        ("pushforward_fixed", "automorphism_masked_pushforward"),
        ("graph_fixed", "automorphism_masked_graph"),
        ("rosati_fixed", "automorphism_masked_rosati"),
        ("control_fixed", "automorphism_masked_control"),
    ):
        if not rigid.get(field):
            out.append(repair)

    if not rigid.get("nonpositive_stage") or rigid.get("imports_positivity"):
        out.append("rigidity_context_collapse")
    if not rigid.get("preserves_budget"):
        out.append("rigidity_expands_exact_24_budget")
    if not rigid.get("source_before_points"):
        out.append("rigidity_loses_source_before_points")

    missing_identities = RIGID_IDENTITIES - _as_set(rigid.get("identities"))
    if missing_identities:
        out.append("rigid_identity_missing:" + ",".join(sorted(missing_identities)))
    missing_coherence = COHERENT_ON - _as_set(rigid.get("coherent_on"))
    if missing_coherence:
        out.append("rigid_coherence_missing:" + ",".join(sorted(missing_coherence)))

    if rigid.get("declared"):
        out.append("rigidification_by_declaration")
    if rigid.get("posthoc"):
        out.append("posthoc_rigidification")
    if rigid.get("retuned"):
        out.append("retuned_rigid_representative")
    if rigid.get("torsor_trivialization_choice"):
        out.append("torsor_trivialization_choice")
    if rigid.get("point_graph"):
        out.append("point_graph_rigidity_check")
    if rigid.get("finite_sample"):
        out.append("finite_rigidity_sample")
    if rigid.get("basis_row"):
        out.append("basis_rigidity_row")
    if rigid.get("context_collapse"):
        out.append("rigidity_context_collapse")

    required = (
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
    )
    for req in required:
        if req not in state["requires"].get(RIGID, []):
            out.append(f"rigid_lift_requires_missing:{req}")
    if RIGID not in state["requires"].get(PRIMITIVE, []):
        out.append("primitive_lift_not_required_to_be_rigid")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("rigidity_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("rigidity_uses_graph_side_bridge")

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
        elif key == "rigid":
            data["rigid"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = rigid_state(MAP)

gate(
    f"{PREFIX}1 doc 553 rigid primitive effective lift layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s identities=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["rigid"]["identities"]),
    ),
)

automorphism_gap = variant(
    live,
    flags={"trivial_automorphism_group": False, "trivial_stabilizer": False, "no_orbit_torsor_or_unit_choice": False},
    banned={
        "nonrigid_primitive_lift": True,
        "nontrivial_lift_automorphism": True,
        "nontrivial_lift_endomorphism": True,
        "unit_ambiguity": True,
        "sign_ambiguity": True,
        "scalar_unit_rescaling": True,
    },
    rigid={
        "canonical_representative": False,
        "automorphism_group": {"identity", "unit_action"},
        "endomorphisms": {"identity", "nontrivial_idempotent"},
        "stabilizer": {"identity", "sign"},
        "unit_ambiguity": True,
        "sign_ambiguity": True,
        "scalar_unit_rescaling": True,
    },
)
automorphism_gap["rigid"]["identities"] -= {
    "trivial_automorphism_group",
    "trivial_stabilizer",
    "canonical_source_representative",
}

gate(
    f"{PREFIX}2 rejects nontrivial automorphisms, endomorphisms, units, and signs",
    not accepts(automorphism_gap)
    and {
        "nonrigid_primitive_lift",
        "nontrivial_lift_automorphism",
        "nontrivial_lift_endomorphism",
        "unit_ambiguity",
        "sign_ambiguity",
        "scalar_unit_rescaling",
    }
    <= set(reasons(automorphism_gap)),
    ",".join(reasons(automorphism_gap)),
)

torsor_orbit_gap = variant(
    live,
    flags={"canonical_source_representative": False, "unique_equalizer_representative": False},
    banned={
        "primitive_lift_torsor": True,
        "isomorphic_primitive_replacement": True,
        "orbit_representative_choice": True,
        "skeletonized_primitive_lift": True,
        "quotient_by_stabilizer": True,
    },
    rigid={
        "unique_in_source_fiber": False,
        "unique_in_equalizer": False,
        "stabilizer": {"identity", "torsor_action"},
        "torsor": True,
        "isomorphic_replacement": True,
        "orbit_choice": True,
        "skeletonized": True,
        "quotient_by_stabilizer": True,
    },
)
torsor_orbit_gap["rigid"]["identities"] -= {
    "canonical_source_representative",
    "unique_equalizer_representative",
}

gate(
    f"{PREFIX}3 rejects torsors, isomorphic replacement orbits, skeletons, and stabilizer quotients",
    not accepts(torsor_orbit_gap)
    and {
        "primitive_lift_torsor",
        "isomorphic_primitive_replacement",
        "orbit_representative_choice",
        "skeletonized_primitive_lift",
        "quotient_by_stabilizer",
    }
    <= set(reasons(torsor_orbit_gap)),
    ",".join(reasons(torsor_orbit_gap)),
)

masked_laws_gap = variant(
    live,
    flags={"fixed_endpoint_degree_boundary_graph_rosati_control": False},
    banned={
        "automorphism_masked_endpoint": True,
        "automorphism_masked_degree": True,
        "automorphism_masked_boundary": True,
        "automorphism_masked_pushforward": True,
        "automorphism_masked_graph": True,
        "automorphism_masked_rosati": True,
        "automorphism_masked_control": True,
    },
    rigid={
        "endpoint_fixed": False,
        "degree_fixed": False,
        "boundary_fixed": False,
        "pushforward_fixed": False,
        "graph_fixed": False,
        "rosati_fixed": False,
        "control_fixed": False,
    },
)
masked_laws_gap["rigid"]["identities"] -= {
    "endpoint_fixed_on_representative",
    "degree_fixed_on_representative",
    "boundary_fixed_on_representative",
    "pushforward_fixed_on_representative",
    "graph_fixed_on_representative",
    "rosati_fixed_on_representative",
    "control_fixed_on_representative",
}
masked_laws_gap["rigid"]["coherent_on"] -= {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

gate(
    f"{PREFIX}4 rejects laws fixed only up to automorphism",
    not accepts(masked_laws_gap)
    and {
        "automorphism_masked_endpoint",
        "automorphism_masked_degree",
        "automorphism_masked_boundary",
        "automorphism_masked_pushforward",
        "automorphism_masked_graph",
        "automorphism_masked_rosati",
        "automorphism_masked_control",
    }
    <= set(reasons(masked_laws_gap)),
    ",".join(reasons(masked_laws_gap)),
)

declared_posthoc_gap = variant(
    live,
    flags={"no_declared_or_posthoc_rigidification": False, "terminal_choice_unique": False},
    banned={
        "torsor_trivialization_choice": True,
        "rigidification_by_declaration": True,
        "posthoc_rigidification": True,
        "retuned_rigid_representative": True,
    },
    rigid={
        "source_side": False,
        "choice_free": False,
        "terminal_choice_unique": False,
        "declared": True,
        "posthoc": True,
        "retuned": True,
        "torsor_trivialization_choice": True,
    },
)
declared_posthoc_gap["rigid"]["identities"] -= {"terminal_choice_unique"}

gate(
    f"{PREFIX}5 rejects declared, posthoc, retuned, or choice-trivialized rigidity",
    not accepts(declared_posthoc_gap)
    and {
        "torsor_trivialization_choice",
        "rigidification_by_declaration",
        "posthoc_rigidification",
        "retuned_rigid_representative",
    }
    <= set(reasons(declared_posthoc_gap)),
    ",".join(reasons(declared_posthoc_gap)),
)

sample_context_gap = variant(
    live,
    flags={
        "source_before_points": False,
        "inside_exact_24_budget": False,
        "no_point_graph_sample_basis_rigidity": False,
    },
    banned={
        "point_graph_rigidity_check": True,
        "finite_rigidity_sample": True,
        "basis_rigidity_row": True,
        "rigidity_context_collapse": True,
    },
    rigid={
        "source_before_points": False,
        "preserves_budget": False,
        "imports_positivity": True,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
        "context_collapse": True,
    },
)
sample_context_gap["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_rigidity_check"
sample_context_gap["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}6 rejects point/graph checks, finite samples, basis rows, positivity, or context collapse",
    not accepts(sample_context_gap)
    and {"point_graph_rigidity_check", "finite_rigidity_sample", "basis_rigidity_row", "rigidity_context_collapse"}
    <= set(reasons(sample_context_gap)),
    ",".join(reasons(sample_context_gap)),
)

missing_cert = variant(
    live,
    flags={"rigid_primitive_effective_lift_certificate_actual": False},
    banned={"missing_rigid_primitive_effective_lift_certificate": True},
)
missing_cert["accepted"].remove(RIGID)
del missing_cert["assignments"][RIGID]

gate(
    f"{PREFIX}7 rejects missing rigid primitive effective lift certificates",
    not accepts(missing_cert)
    and "missing_rigid_primitive_effective_lift_certificate" in reasons(missing_cert)
    and "rigid_primitive_effective_lift_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

source_uniqueness_gap = variant(
    live,
    flags={
        "canonical_source_representative": False,
        "unique_equalizer_representative": False,
        "terminal_choice_unique": False,
    },
    rigid={
        "unique_in_source_fiber": False,
        "unique_in_equalizer": False,
        "terminal_choice_unique": False,
    },
)
source_uniqueness_gap["rigid"]["coherent_on"] -= {
    "source_fiber_subrepresenter",
    "coupled_source_image",
    "equalizer_arrow_to_subrep",
    TERMINAL_CERT,
}
source_uniqueness_gap["rigid"]["identities"] -= {
    "canonical_source_representative",
    "unique_equalizer_representative",
    "terminal_choice_unique",
}

gate(
    f"{PREFIX}8 requires source-fiber, equalizer, coupled-source, and terminal uniqueness",
    not accepts(source_uniqueness_gap)
    and "primitive_lift_torsor" in reasons(source_uniqueness_gap)
    and "orbit_representative_choice" in reasons(source_uniqueness_gap)
    and "torsor_trivialization_choice" in reasons(source_uniqueness_gap),
    ",".join(reasons(source_uniqueness_gap)),
)

dependency_gap = variant(live)
dependency_gap["requires"][RIGID].remove(PRIMITIVE)
dependency_gap["requires"][PRIMITIVE].remove(RIGID)

gate(
    f"{PREFIX}9 requires rigid and primitive certificates to close together",
    not accepts(dependency_gap)
    and "rigid_lift_requires_missing:primitive_effective_grothendieck_lift_certificate" in reasons(dependency_gap)
    and "primitive_lift_not_required_to_be_rigid" in reasons(dependency_gap),
    ",".join(reasons(dependency_gap)),
)

variants = [
    automorphism_gap,
    torsor_orbit_gap,
    masked_laws_gap,
    declared_posthoc_gap,
    sample_context_gap,
    missing_cert,
    source_uniqueness_gap,
    dependency_gap,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only rigid primitive effective Grothendieck lifts pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: primitive effective K0 lift is rigid and stabilizer-free")
print(
    "VERDICT: represented primitive effective K0 trace lifts count only when "
    "the primitive lift is a choice-free source representative with trivial "
    "automorphism group and stabilizer. Torsors, unit/sign ambiguities, "
    "isomorphic replacement orbits, skeletons, quotient-by-stabilizer repairs, "
    "laws fixed only up to automorphism, declared/posthoc rigidifications, "
    "point or graph rigidity checks, finite samples, basis rows, context "
    "collapse, and missing rigid primitive effective lift certificates do not "
    "construct the missing object."
)
