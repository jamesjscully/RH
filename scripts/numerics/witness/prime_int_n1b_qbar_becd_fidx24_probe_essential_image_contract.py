r"""Probe-essential-image contract for admissible source-square probes.

Doc 541 pins fullness on compatible probe morphism tuples. This witness
prevents the full faithful probe image from having compatible probe-object
tuples that do not lift to source-square objects.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_essential_image_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the probe-essential-image witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 542
EXPECTED_WITNESS = "doc542-probe-essential-image"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PROBE_TARGETS = {
    "mediator_cone_probe",
    "constraint_fork_probe",
    "dd4_image_handoff_probe",
    "graph_later_realization_probe",
    "inhabitance_probe",
    "budget_closure_probe",
}


def _probe_object_tuple(source_object: str) -> tuple[str, ...]:
    return tuple(f"{probe}:{source_object}" for probe in sorted(PROBE_TARGETS))


def _compatible_object_tuples() -> dict[str, dict[str, Any]]:
    return {
        f"object_tuple_{source_object}": {
            "objects": _probe_object_tuple(source_object),
            "expected_source": source_object,
            "lift": source_object,
        }
        for source_object in SOURCE_OBJECTS
    }


REQUIRED_FLAGS = (
    "probe_essential_image_certificate_actual",
    "all_compatible_probe_objects_lift",
    "object_lifts_are_source_objects",
    "essential_on_terminal_constraints_handoffs",
    "unique_object_lifts_by_full_faithfulness",
    "strict_object_descent",
    "source_before_points",
    "inside_exact_24_budget",
    "no_declared_or_posthoc_object_lifts",
    "no_point_graph_sample_basis_objects",
)

BANNED_FLAGS = (
    "nonessential_probe_image",
    "extra_probe_object_tuple",
    "compatible_probe_object_without_source_lift",
    "essential_surjectivity_by_declaration",
    "arbitrary_object_lift_selector",
    "nonunique_object_lift",
    "posthoc_object_lift",
    "retuned_object_lift",
    "lax_object_descent",
    "point_graph_object_shadow",
    "finite_object_sample",
    "basis_row_object_probe",
    "missing_probe_essential_image_certificate",
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


def essential_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "compatible_objects": _compatible_object_tuples(),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def lift_values(entry: dict[str, Any]) -> list[str]:
    lift = entry.get("lift")
    if isinstance(lift, list):
        return [str(item) for item in lift]
    if lift is None:
        return []
    return [str(lift)]


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    assignments = dict(state["assignments"])
    compatible_objects = state["compatible_objects"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_542")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc542_witness_missing")
    if PROBE_ESS not in accepted:
        out.append("probe_essential_image_missing_from_current")
    if PROBE_ESS not in assignments:
        out.append("probe_essential_image_unassigned")
    if assignments.get(PROBE_ESS) != "coh_finite_limit_cut":
        out.append(f"probe_essential_image_bad_charge:{assignments.get(PROBE_ESS)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    expected_tuple_keys = {f"object_tuple_{source_object}" for source_object in SOURCE_OBJECTS}
    missing_tuples = expected_tuple_keys - set(compatible_objects)
    if missing_tuples:
        out.append("compatible_probe_object_tuples_missing:" + ",".join(sorted(missing_tuples)))
    extra_tuples = set(compatible_objects) - expected_tuple_keys
    if extra_tuples:
        out.append("extra_probe_object_tuple:" + ",".join(sorted(extra_tuples)))

    for key, entry in compatible_objects.items():
        if not isinstance(entry, dict):
            out.append(f"probe_object_tuple_not_mapping:{key}")
            continue
        expected = entry.get("expected_source")
        lifts = lift_values(entry)
        if not lifts:
            out.append(f"probe_object_tuple_without_lift:{key}")
            continue
        if len(lifts) != 1:
            out.append(f"probe_object_tuple_nonunique_lift:{key}")
        for lift in lifts:
            if lift not in SOURCE_OBJECTS:
                out.append(f"probe_object_tuple_lift_not_source:{key}->{lift}")
        if len(lifts) == 1 and expected in SOURCE_OBJECTS and lifts[0] != expected:
            out.append(f"probe_object_tuple_retuned_lift:{key}->{lifts[0]}_instead_of_{expected}")
        if entry.get("declared_only"):
            out.append(f"probe_object_tuple_declared_lift:{key}")
        if entry.get("lax"):
            out.append(f"probe_object_tuple_lax_lift:{key}")

    for req in (
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
    ):
        if req not in state["requires"].get(PROBE_ESS, []):
            out.append(f"probe_essential_image_requires_missing:{req}")
    if PROBE_ESS not in state["requires"].get(PROBE_FULL, []):
        out.append("probe_fullness_not_required_to_be_essential")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("probe_essential_image_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("probe_essential_image_uses_graph_side_bridge")

    out.extend(flag for flag, active in state["banned"].items() if active)
    return out


def accepts(state: dict[str, Any]) -> bool:
    return not reasons(state)


def variant(base: dict[str, Any], **kwargs) -> dict[str, Any]:
    data = deepcopy(base)
    for key, value in kwargs.items():
        if key == "flags":
            data["flags"].update(value)
        elif key == "banned":
            data["banned"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = essential_state(MAP)

gate(
    f"{PREFIX}1 doc 542 probe-essential-image layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s objects=%d"
    % (live["frontier"].get("current_doc"), live["frontier"].get("current_witness"), len(live["compatible_objects"])),
)

nonessential = variant(
    live,
    flags={"all_compatible_probe_objects_lift": False},
    banned={"nonessential_probe_image": True, "compatible_probe_object_without_source_lift": True},
)
del nonessential["compatible_objects"]["object_tuple_terminal_source_square_object"]["lift"]

gate(
    f"{PREFIX}2 rejects nonessential probe images",
    not accepts(nonessential)
    and {"nonessential_probe_image", "compatible_probe_object_without_source_lift"} <= set(reasons(nonessential)),
    ",".join(reasons(nonessential)),
)

extra_probe_object = variant(
    live,
    flags={"all_compatible_probe_objects_lift": False},
    banned={"extra_probe_object_tuple": True, "compatible_probe_object_without_source_lift": True},
)
extra_probe_object["compatible_objects"]["object_tuple_extra_probe_object"] = {
    "objects": tuple(f"{probe}:extra_object" for probe in sorted(PROBE_TARGETS)),
    "expected_source": "extra_probe_object",
    "lift": None,
}

gate(
    f"{PREFIX}3 rejects extra probe-object tuples",
    not accepts(extra_probe_object)
    and "extra_probe_object_tuple" in reasons(extra_probe_object)
    and any(reason.startswith("extra_probe_object_tuple:") for reason in reasons(extra_probe_object)),
    ",".join(reasons(extra_probe_object)),
)

declared_selector = variant(
    live,
    flags={"no_declared_or_posthoc_object_lifts": False},
    banned={"essential_surjectivity_by_declaration": True, "arbitrary_object_lift_selector": True},
)
declared_selector["compatible_objects"]["object_tuple_exact24_budget_object"]["declared_only"] = True

gate(
    f"{PREFIX}4 rejects essential surjectivity by declaration or arbitrary object selectors",
    not accepts(declared_selector)
    and {"essential_surjectivity_by_declaration", "arbitrary_object_lift_selector"}
    <= set(reasons(declared_selector))
    and "probe_object_tuple_declared_lift:object_tuple_exact24_budget_object" in reasons(declared_selector),
    ",".join(reasons(declared_selector)),
)

nonunique = variant(
    live,
    flags={"unique_object_lifts_by_full_faithfulness": False},
    banned={"nonunique_object_lift": True},
)
nonunique["compatible_objects"]["object_tuple_mediator_cone_object"]["lift"] = [
    "mediator_cone_object",
    "terminal_source_square_object",
]

gate(
    f"{PREFIX}5 rejects nonunique object lifts",
    not accepts(nonunique)
    and "nonunique_object_lift" in reasons(nonunique)
    and "probe_object_tuple_nonunique_lift:object_tuple_mediator_cone_object" in reasons(nonunique),
    ",".join(reasons(nonunique)),
)

posthoc_retuned = variant(
    live,
    flags={"object_lifts_are_source_objects": False, "no_declared_or_posthoc_object_lifts": False},
    banned={"posthoc_object_lift": True, "retuned_object_lift": True},
)
posthoc_retuned["compatible_objects"]["object_tuple_dd4_image_handoff_object"]["lift"] = "posthoc_retuned_object"

gate(
    f"{PREFIX}6 rejects posthoc or retuned object lifts",
    not accepts(posthoc_retuned)
    and {"posthoc_object_lift", "retuned_object_lift"} <= set(reasons(posthoc_retuned)),
    ",".join(reasons(posthoc_retuned)),
)

lax = variant(
    live,
    flags={"strict_object_descent": False},
    banned={"lax_object_descent": True},
)
lax["compatible_objects"]["object_tuple_dependency_closure_object"]["lax"] = True

gate(
    f"{PREFIX}7 rejects lax object descent",
    not accepts(lax)
    and "lax_object_descent" in reasons(lax)
    and "probe_object_tuple_lax_lift:object_tuple_dependency_closure_object" in reasons(lax),
    ",".join(reasons(lax)),
)

point_graph_sample_basis = variant(
    live,
    flags={"source_before_points": False, "inside_exact_24_budget": False, "no_point_graph_sample_basis_objects": False},
    banned={
        "point_graph_object_shadow": True,
        "finite_object_sample": True,
        "basis_row_object_probe": True,
    },
)
point_graph_sample_basis["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_object_shadow"
point_graph_sample_basis["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False
point_graph_sample_basis["compatible_objects"]["object_tuple_finite_limit_inhabitance_object"]["lift"] = "finite_object_sample"
point_graph_sample_basis["compatible_objects"]["object_tuple_exact24_budget_object"]["lift"] = "basis_row_object"

gate(
    f"{PREFIX}8 rejects point/graph object shadows, finite samples, or basis-row probes",
    not accepts(point_graph_sample_basis)
    and {"point_graph_object_shadow", "finite_object_sample", "basis_row_object_probe"}
    <= set(reasons(point_graph_sample_basis)),
    ",".join(reasons(point_graph_sample_basis)),
)

missing_cert = variant(
    live,
    flags={"probe_essential_image_certificate_actual": False},
    banned={"missing_probe_essential_image_certificate": True},
)
missing_cert["accepted"].remove(PROBE_ESS)
del missing_cert["assignments"][PROBE_ESS]

gate(
    f"{PREFIX}9 rejects missing probe-essential-image certificates",
    not accepts(missing_cert)
    and "missing_probe_essential_image_certificate" in reasons(missing_cert)
    and "probe_essential_image_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    nonessential,
    extra_probe_object,
    declared_selector,
    nonunique,
    posthoc_retuned,
    lax,
    point_graph_sample_basis,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only essentially closed full faithful natural source-probe functors pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "nonessential_probe_image",
        "extra_probe_object_tuple",
        "compatible_probe_object_without_source_lift",
        "essential_surjectivity_by_declaration",
        "arbitrary_object_lift_selector",
        "nonunique_object_lift",
        "posthoc_object_lift",
        "retuned_object_lift",
        "lax_object_descent",
        "point_graph_object_shadow",
        "finite_object_sample",
        "basis_row_object_probe",
        "missing_probe_essential_image_certificate",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: admissible source probes have closed essential image")
print(
    "VERDICT: full faithful natural admissible probes count only if every "
    "compatible probe-object tuple lifts to a source-square object. Nonessential "
    "probe images, extra object tuples, missing/nonunique/declared/posthoc/"
    "retuned/lax object lifts, point/graph shadows, finite samples, basis-row "
    "object probes, and missing essential-image certificates do not construct "
    "the missing object."
)
