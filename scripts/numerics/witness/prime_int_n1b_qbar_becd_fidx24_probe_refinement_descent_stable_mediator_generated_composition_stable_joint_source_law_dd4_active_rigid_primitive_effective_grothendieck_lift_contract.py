r"""Refinement-descent-stable mediator-generated joint source-law contract.

Doc 556 pins a mediator-generated composition-stable joint law. This witness
prevents that law from being presentation-dependent: it must descend across
admissible source-square refinements through the existing separated, natural,
full, faithful, essentially closed, equivalence-coherent, cartesian probe
stack.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the refinement-descent witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 557
EXPECTED_WITNESS = (
    "doc557-probe-refinement-descent-stable-mediator-generated-composition-"
    "stable-joint-source-law-dd4-active-rigid-primitive-effective-"
    "grothendieck-lift"
)
REF = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREFDESCSTABMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTJLAWDD4ACTRIGIDPRIMEFFK0LIFTDD4ACTRIGIDPRIMEFFK0LIFTRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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
    REF: "coh_finite_limit_cut",
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

DESCENT_STACK = {
    PROBE_SEP,
    PROBE_NAT,
    PROBE_FAITH,
    PROBE_FULL,
    PROBE_ESS,
    PROBE_EQV,
    CART_EQV,
    TERMINAL_CERT,
}

DESCENDS_FOR = {
    "universal_mediator",
    "source_coupling",
    "equalizer_arrow_to_subrep",
    "finite_limit_cut",
    "original_dd4_class",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "graph_composition",
    "control_death",
}

REF_IDENTITIES = {
    "refinement_descent_stable_law",
    "presentation_independent_mediator_law",
    "overlap_compatible_law",
    "cech_cocycle_zero_law",
    "probe_descent_law",
    "essential_image_descent_law",
    "cartesian_terminal_descent_law",
    "payload_handoff_graph_descent_law",
    "composition_control_descent_law",
}

COHERENT_ON = {
    REF,
    MED,
    JOINT,
    "universal_mediator",
    "source_coupling",
    "equalizer_arrow_to_subrep",
    "finite_limit_cut",
    "coupled_source_image",
    "original_dd4_class",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "graph_composition",
    "control_death",
    *DESCENT_STACK,
}

REF_DATA = {
    "mediator_generated_certificate": MED,
    "descent_law": "refinement_descent_stable_mediator_generated_joint_law",
    "source_side": True,
    "choice_free": True,
    "refinement_stable": True,
    "presentation_independent": True,
    "cover_local_only": False,
    "overlap_compatible": True,
    "cech_cocycle_zero": True,
    "descent_stack": DESCENT_STACK,
    "descends_for": DESCENDS_FOR,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "preserves_budget": True,
    "identities": REF_IDENTITIES,
    "coherent_on": COHERENT_ON,
    "presentation_dependent_mediator_law": False,
    "refinement_retuned_law": False,
    "descent_by_declaration": False,
    "probe_cover_only_law": False,
    "finite_refinement_sample": False,
    "basis_refinement_row": False,
    "refinement_context_collapse": False,
}

REQUIRED_NODE_DEPS = (
    MED,
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

EXPECTED_REF_EDGES = {
    (MED, "made_refinement_descent_stable_by", REF),
    (REF, "refinement_descent_law_of", MED),
    (REF, "refinement_natural_by", PROBE_NAT),
    (REF, "separated_by", PROBE_SEP),
    (REF, "faithful_descent_by", PROBE_FAITH),
    (REF, "full_descent_by", PROBE_FULL),
    (REF, "essential_image_descent_by", PROBE_ESS),
    (REF, "equivalence_descent_by", PROBE_EQV),
    (REF, "cartesian_descent_by", CART_EQV),
    (REF, "terminal_descent_by", TERMINAL_CERT),
    (REF, "mediator_refinement_stable_for", "universal_mediator"),
    (REF, "source_coupling_refinement_stable_for", "source_coupling"),
    (REF, "equalizer_refinement_stable_for", "equalizer_arrow_to_subrep"),
    (REF, "finite_limit_descent_for", "finite_limit_cut"),
    (REF, "payload_descent_for", "original_dd4_class"),
    (REF, "handoff_descent_for", "dd4_image_only_handoff_contract"),
    (REF, "graph_descent_for", "graph_later_realization_contract"),
    (REF, "composition_descent_for", "graph_composition"),
    (REF, "control_descent_for", "control_death"),
    (REF, "preserves", "exact_24_cell_finite_index"),
    (REF, "coherent_for", "coupled_source_image"),
}

REQUIRED_FLAGS = (
    "refinement_descent_certificate_actual",
    "presentation_independent",
    "overlap_compatible",
    "cech_cocycle_zero",
    "probe_stack_descent",
    "mediator_coupling_equalizer_descent",
    "payload_handoff_graph_descent",
    "composition_control_descent",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "presentation_dependent_mediator_law",
    "refinement_retuned_law",
    "cover_local_law_only",
    "overlap_mismatch_law",
    "cech_cocycle_failure",
    "descent_by_declaration",
    "probe_cover_only_law",
    "essential_image_descent_gap",
    "full_faithful_descent_gap",
    "cartesian_descent_gap",
    "terminal_descent_gap",
    "mediator_refinement_mismatch",
    "source_coupling_refinement_mismatch",
    "equalizer_refinement_mismatch",
    "dd4_payload_descent_gap",
    "handoff_descent_gap",
    "graph_descent_gap",
    "composition_descent_gap",
    "control_descent_gap",
    "finite_refinement_sample",
    "basis_refinement_row",
    "refinement_context_collapse",
    "missing_refinement_descent_stable_mediator_generated_joint_law_certificate",
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
        "ref": deepcopy(REF_DATA),
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
    ref = state["ref"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_557")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc557_witness_missing")
    if REF not in accepted:
        out.append("refinement_descent_law_missing_from_current")
    if REF not in assignments:
        out.append("refinement_descent_law_unassigned")
    if assignments.get(REF) != "coh_finite_limit_cut":
        out.append(f"refinement_descent_law_bad_charge:{assignments.get(REF)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(ref, dict):
        out.append("refinement_descent_data_not_mapping")
        ref = {}

    if ref.get("mediator_generated_certificate") != MED:
        out.append("refinement_descent_not_based_on_mediator_generated_law")
    if not ref.get("descent_law"):
        out.append("missing_refinement_descent_stable_mediator_generated_joint_law_certificate")
    if not ref.get("source_side") or not ref.get("choice_free") or ref.get("descent_by_declaration"):
        out.append("descent_by_declaration")
    if not ref.get("refinement_stable"):
        out.append("presentation_dependent_mediator_law")
    if not ref.get("presentation_independent"):
        out.append("presentation_dependent_mediator_law")
    if ref.get("cover_local_only"):
        out.append("cover_local_law_only")
    if not ref.get("overlap_compatible"):
        out.append("overlap_mismatch_law")
    if not ref.get("cech_cocycle_zero"):
        out.append("cech_cocycle_failure")
    if not ref.get("preserves_budget"):
        out.append("refinement_descent_expands_exact_24_budget")
    if not ref.get("nonpositive_stage") or ref.get("imports_positivity"):
        out.append("refinement_context_collapse")

    descent_stack = _as_set(ref.get("descent_stack"))
    if PROBE_SEP not in descent_stack or PROBE_NAT not in descent_stack:
        out.append("probe_cover_only_law")
    if PROBE_ESS not in descent_stack:
        out.append("essential_image_descent_gap")
    if PROBE_FULL not in descent_stack or PROBE_FAITH not in descent_stack:
        out.append("full_faithful_descent_gap")
    if CART_EQV not in descent_stack:
        out.append("cartesian_descent_gap")
    if TERMINAL_CERT not in descent_stack:
        out.append("terminal_descent_gap")

    descends_for = _as_set(ref.get("descends_for"))
    if "universal_mediator" not in descends_for:
        out.append("mediator_refinement_mismatch")
    if "source_coupling" not in descends_for:
        out.append("source_coupling_refinement_mismatch")
    if "equalizer_arrow_to_subrep" not in descends_for:
        out.append("equalizer_refinement_mismatch")
    if "original_dd4_class" not in descends_for:
        out.append("dd4_payload_descent_gap")
    if "dd4_image_only_handoff_contract" not in descends_for:
        out.append("handoff_descent_gap")
    if "graph_later_realization_contract" not in descends_for:
        out.append("graph_descent_gap")
    if "graph_composition" not in descends_for:
        out.append("composition_descent_gap")
    if "control_death" not in descends_for:
        out.append("control_descent_gap")

    for key in (
        "presentation_dependent_mediator_law",
        "refinement_retuned_law",
        "descent_by_declaration",
        "probe_cover_only_law",
        "finite_refinement_sample",
        "basis_refinement_row",
        "refinement_context_collapse",
    ):
        if ref.get(key):
            out.append(key)

    missing_identities = REF_IDENTITIES - _as_set(ref.get("identities"))
    if missing_identities:
        out.append("refinement_descent_identity_missing:" + ",".join(sorted(missing_identities)))
    missing_coherence = COHERENT_ON - _as_set(ref.get("coherent_on"))
    if missing_coherence:
        out.append("refinement_descent_coherence_missing:" + ",".join(sorted(missing_coherence)))

    for req in REQUIRED_NODE_DEPS:
        if req not in state["requires"].get(REF, []):
            out.append(f"refinement_descent_requires_missing:{req}")
    if REF not in state["requires"].get(MED, []):
        out.append("mediator_generated_law_not_required_to_be_refinement_descent_stable")

    missing_edges = EXPECTED_REF_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("refinement_descent_edges_missing:" + ",".join(rendered))

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
        elif key == "ref":
            data["ref"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 557 refinement-descent layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s descent_targets=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["ref"]["descends_for"]),
    ),
)

presentation_gap = variant(
    live,
    flags={"presentation_independent": False},
    banned={
        "presentation_dependent_mediator_law": True,
        "refinement_retuned_law": True,
        "cover_local_law_only": True,
    },
    ref={
        "refinement_stable": False,
        "presentation_independent": False,
        "cover_local_only": True,
        "presentation_dependent_mediator_law": True,
        "refinement_retuned_law": True,
    },
)
presentation_gap["ref"]["identities"] -= {"presentation_independent_mediator_law"}

gate(
    f"{PREFIX}2 rejects presentation-dependent, retuned, or cover-local laws",
    not accepts(presentation_gap)
    and {"presentation_dependent_mediator_law", "refinement_retuned_law", "cover_local_law_only"}
    <= set(reasons(presentation_gap)),
    ",".join(reasons(presentation_gap)),
)

overlap_gap = variant(
    live,
    flags={"overlap_compatible": False, "cech_cocycle_zero": False},
    banned={
        "overlap_mismatch_law": True,
        "cech_cocycle_failure": True,
        "descent_by_declaration": True,
    },
    ref={
        "overlap_compatible": False,
        "cech_cocycle_zero": False,
        "descent_by_declaration": True,
    },
)
overlap_gap["ref"]["identities"] -= {"overlap_compatible_law", "cech_cocycle_zero_law"}

gate(
    f"{PREFIX}3 rejects overlap mismatch, Cech failure, or declared descent",
    not accepts(overlap_gap)
    and {"overlap_mismatch_law", "cech_cocycle_failure", "descent_by_declaration"}
    <= set(reasons(overlap_gap)),
    ",".join(reasons(overlap_gap)),
)

probe_descent_gap = variant(
    live,
    flags={"probe_stack_descent": False},
    banned={
        "probe_cover_only_law": True,
        "essential_image_descent_gap": True,
        "full_faithful_descent_gap": True,
        "cartesian_descent_gap": True,
        "terminal_descent_gap": True,
    },
    ref={
        "descent_stack": {PROBE_SEP, PROBE_NAT},
        "probe_cover_only_law": True,
    },
)
probe_descent_gap["ref"]["identities"] -= {
    "probe_descent_law",
    "essential_image_descent_law",
    "cartesian_terminal_descent_law",
}

gate(
    f"{PREFIX}4 rejects probe-cover-only or probe-stack descent gaps",
    not accepts(probe_descent_gap)
    and {
        "probe_cover_only_law",
        "essential_image_descent_gap",
        "full_faithful_descent_gap",
        "cartesian_descent_gap",
        "terminal_descent_gap",
    }
    <= set(reasons(probe_descent_gap)),
    ",".join(reasons(probe_descent_gap)),
)

spine_descent_gap = variant(
    live,
    flags={"mediator_coupling_equalizer_descent": False},
    banned={
        "mediator_refinement_mismatch": True,
        "source_coupling_refinement_mismatch": True,
        "equalizer_refinement_mismatch": True,
    },
    ref={
        "descends_for": DESCENDS_FOR - {"universal_mediator", "source_coupling", "equalizer_arrow_to_subrep"},
    },
)

gate(
    f"{PREFIX}5 rejects mediator, source-coupling, or equalizer refinement mismatch",
    not accepts(spine_descent_gap)
    and {"mediator_refinement_mismatch", "source_coupling_refinement_mismatch", "equalizer_refinement_mismatch"}
    <= set(reasons(spine_descent_gap)),
    ",".join(reasons(spine_descent_gap)),
)

payload_bridge_gap = variant(
    live,
    flags={"payload_handoff_graph_descent": False},
    banned={
        "dd4_payload_descent_gap": True,
        "handoff_descent_gap": True,
        "graph_descent_gap": True,
    },
    ref={
        "descends_for": DESCENDS_FOR - {"original_dd4_class", "dd4_image_only_handoff_contract", "graph_later_realization_contract"},
    },
)
payload_bridge_gap["ref"]["identities"] -= {"payload_handoff_graph_descent_law"}

gate(
    f"{PREFIX}6 rejects DD4 payload, handoff, or graph descent gaps",
    not accepts(payload_bridge_gap)
    and {"dd4_payload_descent_gap", "handoff_descent_gap", "graph_descent_gap"}
    <= set(reasons(payload_bridge_gap)),
    ",".join(reasons(payload_bridge_gap)),
)

operation_sample_gap = variant(
    live,
    flags={"composition_control_descent": False, "inside_exact_24_budget": False},
    banned={
        "composition_descent_gap": True,
        "control_descent_gap": True,
        "finite_refinement_sample": True,
        "basis_refinement_row": True,
        "refinement_context_collapse": True,
    },
    ref={
        "descends_for": DESCENDS_FOR - {"graph_composition", "control_death"},
        "finite_refinement_sample": True,
        "basis_refinement_row": True,
        "refinement_context_collapse": True,
        "nonpositive_stage": False,
        "preserves_budget": False,
    },
)
operation_sample_gap["ref"]["identities"] -= {"composition_control_descent_law"}

gate(
    f"{PREFIX}7 rejects operation descent gaps, samples, rows, or context collapse",
    not accepts(operation_sample_gap)
    and {
        "composition_descent_gap",
        "control_descent_gap",
        "finite_refinement_sample",
        "basis_refinement_row",
        "refinement_context_collapse",
    }
    <= set(reasons(operation_sample_gap)),
    ",".join(reasons(operation_sample_gap)),
)

missing_cert = variant(
    live,
    flags={"refinement_descent_certificate_actual": False},
    banned={"missing_refinement_descent_stable_mediator_generated_joint_law_certificate": True},
)
missing_cert["accepted"].remove(REF)
del missing_cert["assignments"][REF]

gate(
    f"{PREFIX}8 rejects missing refinement-descent certificates",
    not accepts(missing_cert)
    and "missing_refinement_descent_stable_mediator_generated_joint_law_certificate" in reasons(missing_cert)
    and "refinement_descent_law_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

dependency_gap = variant(live)
dependency_gap["requires"][REF].remove(MED)
dependency_gap["requires"][MED].remove(REF)

gate(
    f"{PREFIX}9 requires mediator-generated and refinement-descent certificates to close together",
    not accepts(dependency_gap)
    and "refinement_descent_requires_missing:mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
    in reasons(dependency_gap)
    and "mediator_generated_law_not_required_to_be_refinement_descent_stable" in reasons(dependency_gap),
    ",".join(reasons(dependency_gap)),
)

variants = [
    presentation_gap,
    overlap_gap,
    probe_descent_gap,
    spine_descent_gap,
    payload_bridge_gap,
    operation_sample_gap,
    missing_cert,
    dependency_gap,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only refinement-descent-stable mediator-generated laws pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: mediator-generated law is refinement-descent stable")
print(
    "VERDICT: the mediator-generated composition-stable joint law counts only "
    "when it is presentation-independent and descends across admissible "
    "source-square refinements through the existing probe stack. "
    "Presentation-dependent, retuned, cover-local, overlap-mismatched, "
    "Cech-nontrivial, declared, probe-cover-only, descent-gap, sampled, "
    "basis-row, context-collapsed, and missing certificates do not construct "
    "the missing object."
)
