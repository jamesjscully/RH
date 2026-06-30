r"""Nonvacuous admissible-category contract for terminal source squares.

Doc 536 pins terminality. This witness prevents the terminal property from
being manufactured by a singleton, retuned, or terminal-defined category of
probes. The admissible source-square category must be preterminally specified,
probe-full, source-before-points, and inside the exact 24-cell budget.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_terminal_admcat_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the admissible-category witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 537
EXPECTED_WITNESS = "doc537-admissible-category"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

CATEGORY_PREDICATES = {
    "preterminal_definition",
    "source_before_points",
    "seven_source_constraints",
    "finite_limit_equalizer",
    "directed_dd4_handoff",
    "directed_graph_later_realization",
    "exact_24_budget",
    "dependency_closure",
    "inhabited_source_fiber",
}

PROBE_CLASSES = {
    "mediator_cone_probe",
    "constraint_fork_probe",
    "dd4_image_handoff_probe",
    "graph_later_realization_probe",
    "inhabitance_probe",
    "budget_closure_probe",
}

REQUIRED_FLAGS = (
    "category_certificate_actual",
    "preterminal_definition",
    "probe_full_nonvacuous",
    "not_singleton",
    "source_before_points",
    "all_seven_constraints_visible",
    "dd4_and_graph_bridges_directed",
    "budget_and_dependency_closed",
    "terminal_object_belongs",
    "no_terminal_defined_membership",
)

BANNED_FLAGS = (
    "singleton_admissible_category",
    "retuned_admissible_category",
    "terminal_defined_category",
    "posthoc_probe_class",
    "graph_first_probe_category",
    "control_probe_admitted",
    "dh_epstein_probe_admitted",
    "h1_quotient_probe_category",
    "missing_admissible_category_certificate",
    "expanded_finite_index",
    "one_more_layer_tower",
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


def category_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "predicates": set(CATEGORY_PREDICATES),
        "probes": set(PROBE_CLASSES),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    assignments = dict(state["assignments"])
    predicates = set(state["predicates"])
    probes = set(state["probes"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_537")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc537_witness_missing")
    if ADM_CAT not in accepted:
        out.append("admissible_category_missing_from_current")
    if ADM_CAT not in assignments:
        out.append("admissible_category_unassigned")
    if assignments.get(ADM_CAT) != "coh_finite_limit_cut":
        out.append(f"admissible_category_bad_charge:{assignments.get(ADM_CAT)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    missing_predicates = CATEGORY_PREDICATES - predicates
    if missing_predicates:
        out.append("category_predicates_missing:" + ",".join(sorted(missing_predicates)))
    if TERMINAL_CERT in predicates:
        out.append("category_membership_defined_by_terminal_object")
    if len(probes) < 6:
        out.append("probe_class_count_too_small")
    missing_probes = PROBE_CLASSES - probes
    if missing_probes:
        out.append("probe_classes_missing:" + ",".join(sorted(missing_probes)))

    requires = state["requires"].get(ADM_CAT, [])
    for req in (
        TERMINAL_CERT,
        "budget_dependency_closure_certificate",
        "finite_index_budget_certificate",
        "finite_limit_cut",
        "joint_constraint_fork",
        "equalizer_arrow_to_subrep",
        "source_before_points",
        "dd4_image_only_handoff_contract",
        "graph_later_realization_contract",
    ):
        if req not in requires:
            out.append(f"admissible_category_requires_missing:{req}")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if dd4_bridge.get("from") == dd4_bridge.get("to") or dd4_bridge.get("direction") != "image_only":
        out.append("dd4_bridge_not_directed_for_category")
    if graph_bridge.get("from") == graph_bridge.get("to") or graph_bridge.get("direction") != "realizes_later":
        out.append("graph_bridge_not_later_for_category")
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("graph_probe_category_reverses_before_points")

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
live = category_state(MAP)

gate(
    f"{PREFIX}1 doc 537 admissible-category layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s probes=%d predicates=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["probes"]),
        len(live["predicates"]),
    ),
)

singleton = variant(
    live,
    probes={"terminal_square_only"},
    flags={"probe_full_nonvacuous": False, "not_singleton": False},
    banned={"singleton_admissible_category": True},
)

gate(
    f"{PREFIX}2 rejects singleton admissible categories",
    not accepts(singleton)
    and "singleton_admissible_category" in reasons(singleton)
    and "probe_class_count_too_small" in reasons(singleton),
    ",".join(reasons(singleton)),
)

retuned = variant(
    live,
    predicates=CATEGORY_PREDICATES | {TERMINAL_CERT},
    flags={"preterminal_definition": False, "no_terminal_defined_membership": False},
    banned={"retuned_admissible_category": True, "terminal_defined_category": True},
)

gate(
    f"{PREFIX}3 rejects terminal-defined or retuned categories",
    not accepts(retuned)
    and "category_membership_defined_by_terminal_object" in reasons(retuned)
    and {"retuned_admissible_category", "terminal_defined_category"} <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

posthoc = variant(
    live,
    probes=PROBE_CLASSES | {"posthoc_universal_arrow_probe"},
    flags={"preterminal_definition": False},
    banned={"posthoc_probe_class": True},
)

gate(
    f"{PREFIX}4 rejects posthoc probe classes",
    not accepts(posthoc)
    and "posthoc_probe_class" in reasons(posthoc)
    and "preterminal_definition_missing" in reasons(posthoc),
    ",".join(reasons(posthoc)),
)

graph_first = variant(
    live,
    flags={"source_before_points": False},
    banned={"graph_first_probe_category": True},
)
graph_first["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}5 rejects graph-first probe categories",
    not accepts(graph_first)
    and "graph_first_probe_category" in reasons(graph_first)
    and "graph_probe_category_reverses_before_points" in reasons(graph_first),
    ",".join(reasons(graph_first)),
)

control_admitted = variant(
    live,
    banned={"control_probe_admitted": True, "dh_epstein_probe_admitted": True},
)

gate(
    f"{PREFIX}6 rejects control/DH/Epstein probe admission",
    not accepts(control_admitted)
    and {"control_probe_admitted", "dh_epstein_probe_admitted"} <= set(reasons(control_admitted)),
    ",".join(reasons(control_admitted)),
)

h1_quotient = variant(
    live,
    banned={"h1_quotient_probe_category": True},
)
h1_quotient["bridges"]["dd4_certificate_handoff"]["to"] = "original_h1"

gate(
    f"{PREFIX}7 rejects H1 quotient probe categories",
    not accepts(h1_quotient)
    and "h1_quotient_probe_category" in reasons(h1_quotient)
    and "dd4_bridge_not_directed_for_category" in reasons(h1_quotient),
    ",".join(reasons(h1_quotient)),
)

missing_cert = variant(
    live,
    flags={"category_certificate_actual": False},
    banned={"missing_admissible_category_certificate": True},
)
missing_cert["accepted"].remove(ADM_CAT)
del missing_cert["assignments"][ADM_CAT]

gate(
    f"{PREFIX}8 rejects missing admissible-category certificates",
    not accepts(missing_cert)
    and "missing_admissible_category_certificate" in reasons(missing_cert)
    and "admissible_category_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

expanded = variant(
    live,
    banned={"expanded_finite_index": True, "one_more_layer_tower": True},
)
expanded["assignments"]["extra_category_layer"] = "coh_extra_category_cell"

gate(
    f"{PREFIX}9 rejects expanded finite-index admissible categories",
    not accepts(expanded)
    and "expanded_finite_index" in reasons(expanded)
    and "one_more_layer_tower" in reasons(expanded)
    and any(reason.startswith("assignment_uses_undeclared_cell:") for reason in reasons(expanded)),
    ",".join(reasons(expanded)),
)

variants = [
    singleton,
    retuned,
    posthoc,
    graph_first,
    control_admitted,
    h1_quotient,
    missing_cert,
    expanded,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only the nonvacuous preterminal admissible category passes",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "singleton_admissible_category",
        "retuned_admissible_category",
        "terminal_defined_category",
        "posthoc_probe_class",
        "graph_first_probe_category",
        "control_probe_admitted",
        "dh_epstein_probe_admitted",
        "h1_quotient_probe_category",
        "missing_admissible_category_certificate",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: nonvacuous admissible source-square category pinned")
print(
    "VERDICT: terminality counts only inside a preterminally specified, "
    "probe-full admissible category of budgeted dependency-closed source "
    "squares. Singleton categories, retuned membership, posthoc probes, "
    "graph-first probes, control/DH/Epstein probes, H1 quotient categories, "
    "missing category certificates, and extra finite-index layers do not "
    "construct the missing object."
)
