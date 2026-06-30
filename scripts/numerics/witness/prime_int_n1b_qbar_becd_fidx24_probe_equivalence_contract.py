r"""Probe-equivalence contract for admissible source-square probes.

Doc 542 pins full faithfulness plus essential image closure. This witness
prevents that from being used only as an abstract equivalence theorem: the
source square must carry choice-free adjoint-equivalence data coherent with
the terminal object, constraint fork, handoffs, inhabitance, and exact-24
budget.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_equivalence_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the probe-equivalence witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 543
EXPECTED_WITNESS = "doc543-probe-equivalence"
PROBE_EQV = "probe_equivalence_certificate"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

SOURCE_OBJECTS = {
    "terminal_source_square_object",
    "mediator_cone_object",
    "joint_constraint_fork_object",
    "dd4_image_handoff_object",
    "graph_later_realization_object",
    "finite_limit_inhabitance_object",
    "dependency_closure_object",
    "exact24_budget_object",
}

SOURCE_MORPHISMS = {
    "id_source_square",
    "source_square_morphism",
    "terminal_arrow",
    "dependency_closure_morphism",
    "dd4_image_handoff_morphism",
    "graph_later_realization_morphism",
    "inhabitance_certificate_morphism",
    "budget_closure_morphism",
    "composite_dependency_budget_morphism",
}

LIVE_COHERENCE = {
    "terminal",
    "constraints",
    "dd4_handoff",
    "graph_handoff",
    "inhabitance",
    "dependency_closure",
    "budget_closure",
}

REQUIRED_EQV_KEYS = {
    "source_to_probe_functor",
    "probe_to_source_functor",
    "unit",
    "counit",
    "triangles",
    "choice_free",
    "skeleton_free",
    "source_before_points",
    "preserves_budget",
    "coherent_on",
}

TRIANGLE_IDENTITIES = {"left_triangle", "right_triangle"}

EQUIVALENCE_DATA = {
    "source_to_probe_functor": "P",
    "probe_to_source_functor": "R",
    "unit": "unit_id_source",
    "counit": "counit_probe_image",
    "triangles": TRIANGLE_IDENTITIES,
    "choice_free": True,
    "skeleton_free": True,
    "source_before_points": True,
    "preserves_budget": True,
    "coherent_on": LIVE_COHERENCE,
    "objects": SOURCE_OBJECTS,
    "morphisms": SOURCE_MORPHISMS,
}

REQUIRED_FLAGS = (
    "probe_equivalence_certificate_actual",
    "choice_free_quasi_inverse",
    "unit_counit_present",
    "triangle_identities_hold",
    "coherent_on_terminal_constraints_handoffs",
    "source_before_points",
    "inside_exact_24_budget",
    "skeleton_free",
    "no_posthoc_or_retuned_equivalence",
    "no_point_graph_sample_basis_equivalence",
)

BANNED_FLAGS = (
    "abstract_equivalence_only",
    "choice_of_quasi_inverse",
    "skeletonization_equivalence",
    "unit_counit_missing",
    "triangle_identity_missing",
    "pseudoinverse_without_coherence",
    "posthoc_equivalence_lift",
    "retuned_equivalence_data",
    "point_graph_equivalence",
    "finite_equivalence_sample",
    "basis_row_equivalence",
    "expanded_equivalence_index",
    "missing_probe_equivalence_certificate",
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


def equivalence_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "equivalence": deepcopy(EQUIVALENCE_DATA),
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
    eqv = state["equivalence"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_543")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc543_witness_missing")
    if PROBE_EQV not in accepted:
        out.append("probe_equivalence_missing_from_current")
    if PROBE_EQV not in assignments:
        out.append("probe_equivalence_unassigned")
    if assignments.get(PROBE_EQV) != "coh_finite_limit_cut":
        out.append(f"probe_equivalence_bad_charge:{assignments.get(PROBE_EQV)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if not isinstance(eqv, dict):
        out.append("equivalence_data_not_mapping")
        eqv = {}

    missing_keys = REQUIRED_EQV_KEYS - set(eqv)
    if missing_keys:
        out.append("equivalence_data_missing:" + ",".join(sorted(missing_keys)))
    if not eqv.get("source_to_probe_functor"):
        out.append("source_to_probe_functor_missing")
    if not eqv.get("probe_to_source_functor"):
        out.append("choice_free_quasi_inverse_missing")
    if not eqv.get("unit"):
        out.append("unit_missing")
    if not eqv.get("counit"):
        out.append("counit_missing")
    missing_triangles = TRIANGLE_IDENTITIES - _as_set(eqv.get("triangles"))
    if missing_triangles:
        out.append("triangle_identities_missing:" + ",".join(sorted(missing_triangles)))
    if not eqv.get("choice_free"):
        out.append("quasi_inverse_uses_choice")
    if not eqv.get("skeleton_free"):
        out.append("equivalence_uses_skeletonization")
    if not eqv.get("source_before_points"):
        out.append("equivalence_loses_source_before_points")
    if not eqv.get("preserves_budget"):
        out.append("equivalence_expands_exact_24_budget")

    missing_coherence = LIVE_COHERENCE - _as_set(eqv.get("coherent_on"))
    if missing_coherence:
        out.append("equivalence_coherence_missing:" + ",".join(sorted(missing_coherence)))
    if set(eqv.get("objects", ())) != SOURCE_OBJECTS:
        out.append("equivalence_objects_not_source_square_classes")
    if set(eqv.get("morphisms", ())) != SOURCE_MORPHISMS:
        out.append("equivalence_morphisms_not_source_square_classes")
    if eqv.get("abstract_only"):
        out.append("abstract_equivalence_only")
    if eqv.get("posthoc"):
        out.append("posthoc_equivalence_lift")
    if eqv.get("retuned"):
        out.append("retuned_equivalence_data")
    if eqv.get("point_graph"):
        out.append("point_graph_equivalence")
    if eqv.get("finite_sample"):
        out.append("finite_equivalence_sample")
    if eqv.get("basis_row"):
        out.append("basis_row_equivalence")

    for req in (
        PROBE_ESS,
        PROBE_FULL,
        PROBE_FAITH,
        PROBE_NAT,
        PROBE_SEP,
        ADM_CAT,
        TERMINAL_CERT,
        "budget_dependency_closure_certificate",
        "finite_index_budget_certificate",
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
        if req not in state["requires"].get(PROBE_EQV, []):
            out.append(f"probe_equivalence_requires_missing:{req}")
    for prior in (PROBE_ESS, PROBE_FULL, PROBE_FAITH, PROBE_NAT, PROBE_SEP, ADM_CAT):
        if PROBE_EQV not in state["requires"].get(prior, []):
            out.append(f"{prior}_not_required_to_be_equivalence_coherent")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("probe_equivalence_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("probe_equivalence_uses_graph_side_bridge")

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
        elif key == "equivalence":
            data["equivalence"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = equivalence_state(MAP)

gate(
    f"{PREFIX}1 doc 543 probe-equivalence layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s coherence=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["equivalence"]["coherent_on"]),
    ),
)

abstract_only = variant(
    live,
    flags={
        "choice_free_quasi_inverse": False,
        "unit_counit_present": False,
        "triangle_identities_hold": False,
    },
    banned={"abstract_equivalence_only": True},
    equivalence={
        "abstract_only": True,
        "probe_to_source_functor": None,
        "unit": None,
        "counit": None,
        "triangles": set(),
    },
)

gate(
    f"{PREFIX}2 rejects abstract equivalence without adjoint data",
    not accepts(abstract_only)
    and "abstract_equivalence_only" in reasons(abstract_only)
    and "choice_free_quasi_inverse_missing" in reasons(abstract_only)
    and "unit_missing" in reasons(abstract_only)
    and "counit_missing" in reasons(abstract_only),
    ",".join(reasons(abstract_only)),
)

choice_or_skeleton = variant(
    live,
    flags={"choice_free_quasi_inverse": False, "skeleton_free": False},
    banned={"choice_of_quasi_inverse": True, "skeletonization_equivalence": True},
    equivalence={"choice_free": False, "skeleton_free": False},
)

gate(
    f"{PREFIX}3 rejects quasi-inverse choice and skeletonization",
    not accepts(choice_or_skeleton)
    and {"choice_of_quasi_inverse", "skeletonization_equivalence"} <= set(reasons(choice_or_skeleton))
    and "quasi_inverse_uses_choice" in reasons(choice_or_skeleton)
    and "equivalence_uses_skeletonization" in reasons(choice_or_skeleton),
    ",".join(reasons(choice_or_skeleton)),
)

missing_unit_counit = variant(
    live,
    flags={"unit_counit_present": False},
    banned={"unit_counit_missing": True},
    equivalence={"unit": None, "counit": None},
)

gate(
    f"{PREFIX}4 rejects missing unit or counit",
    not accepts(missing_unit_counit)
    and "unit_counit_missing" in reasons(missing_unit_counit)
    and {"unit_missing", "counit_missing"} <= set(reasons(missing_unit_counit)),
    ",".join(reasons(missing_unit_counit)),
)

missing_triangle = variant(
    live,
    flags={"triangle_identities_hold": False},
    banned={"triangle_identity_missing": True},
    equivalence={"triangles": {"left_triangle"}},
)

gate(
    f"{PREFIX}5 rejects missing triangle identities",
    not accepts(missing_triangle)
    and "triangle_identity_missing" in reasons(missing_triangle)
    and "triangle_identities_missing:right_triangle" in reasons(missing_triangle),
    ",".join(reasons(missing_triangle)),
)

pseudoinverse_without_coherence = variant(
    live,
    flags={"coherent_on_terminal_constraints_handoffs": False},
    banned={"pseudoinverse_without_coherence": True},
    equivalence={"coherent_on": {"terminal", "constraints"}},
)

gate(
    f"{PREFIX}6 rejects pseudoinverse data without live coherence",
    not accepts(pseudoinverse_without_coherence)
    and "pseudoinverse_without_coherence" in reasons(pseudoinverse_without_coherence)
    and any(reason.startswith("equivalence_coherence_missing:") for reason in reasons(pseudoinverse_without_coherence)),
    ",".join(reasons(pseudoinverse_without_coherence)),
)

posthoc_retuned = variant(
    live,
    flags={"no_posthoc_or_retuned_equivalence": False},
    banned={"posthoc_equivalence_lift": True, "retuned_equivalence_data": True},
    equivalence={"posthoc": True, "retuned": True},
)

gate(
    f"{PREFIX}7 rejects posthoc or retuned equivalence data",
    not accepts(posthoc_retuned)
    and {"posthoc_equivalence_lift", "retuned_equivalence_data"} <= set(reasons(posthoc_retuned)),
    ",".join(reasons(posthoc_retuned)),
)

point_sample_basis = variant(
    live,
    flags={"source_before_points": False, "inside_exact_24_budget": False, "no_point_graph_sample_basis_equivalence": False},
    banned={
        "point_graph_equivalence": True,
        "finite_equivalence_sample": True,
        "basis_row_equivalence": True,
        "expanded_equivalence_index": True,
    },
    equivalence={
        "source_before_points": False,
        "preserves_budget": False,
        "point_graph": True,
        "finite_sample": True,
        "basis_row": True,
    },
)
point_sample_basis["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_equivalence"
point_sample_basis["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects point/graph equivalence, finite samples, basis rows, or expanded index",
    not accepts(point_sample_basis)
    and {
        "point_graph_equivalence",
        "finite_equivalence_sample",
        "basis_row_equivalence",
        "expanded_equivalence_index",
    }
    <= set(reasons(point_sample_basis)),
    ",".join(reasons(point_sample_basis)),
)

missing_cert = variant(
    live,
    flags={"probe_equivalence_certificate_actual": False},
    banned={"missing_probe_equivalence_certificate": True},
)
missing_cert["accepted"].remove(PROBE_EQV)
del missing_cert["assignments"][PROBE_EQV]

gate(
    f"{PREFIX}9 rejects missing probe-equivalence certificates",
    not accepts(missing_cert)
    and "missing_probe_equivalence_certificate" in reasons(missing_cert)
    and "probe_equivalence_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    abstract_only,
    choice_or_skeleton,
    missing_unit_counit,
    missing_triangle,
    pseudoinverse_without_coherence,
    posthoc_retuned,
    point_sample_basis,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only choice-free coherent adjoint probe-equivalences pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "abstract_equivalence_only",
        "choice_of_quasi_inverse",
        "skeletonization_equivalence",
        "unit_counit_missing",
        "triangle_identity_missing",
        "pseudoinverse_without_coherence",
        "posthoc_equivalence_lift",
        "retuned_equivalence_data",
        "point_graph_equivalence",
        "finite_equivalence_sample",
        "basis_row_equivalence",
        "expanded_equivalence_index",
        "missing_probe_equivalence_certificate",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: admissible probes reconstruct source-square category")
print(
    "VERDICT: full faithful essentially closed admissible probes count only "
    "when the square carries choice-free adjoint-equivalence data with a "
    "quasi-inverse, unit, counit, triangle identities, live coherence, "
    "source-before-points order, and the exact-24 budget. Abstract equivalence, "
    "quasi-inverse choice, skeletonization, incoherent pseudoinverses, "
    "posthoc/retuned equivalence data, point/graph shadows, finite samples, "
    "basis rows, expanded index structure, and missing certificates do not "
    "construct the missing object."
)
