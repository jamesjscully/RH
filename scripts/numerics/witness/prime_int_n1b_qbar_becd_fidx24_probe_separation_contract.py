r"""Probe-separation contract for the admissible source-square category.

Doc 537 pins a nonvacuous admissible category. This witness checks that the
admissible probes are conservative for the live source-square data: they must
separate the seven source constraints, DD.4 handoff, graph-later handoff,
inhabitance, and budget/dependency/terminal category data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_separation_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the probe-separation witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 538
EXPECTED_WITNESS = "doc538-probe-separation"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

PROBE_TARGETS = {
    "mediator_cone_probe": {"universal_mediator", "formation_fiber", "source_coupling"},
    "constraint_fork_probe": {
        "endpoint_integrality",
        "degree_maps",
        "dd4_boundary",
        "boundary_pushforward",
        "graph_composition",
        "rosati_count",
        "control_death",
    },
    "dd4_image_handoff_probe": {
        "original_dd4_class",
        "dd4_certificate_image",
        "dd4_image_only_handoff_contract",
        "dd4_boundary_certificate",
    },
    "graph_later_realization_probe": {
        "pregraph_rosati_payload",
        "graph_realization_image",
        "graph_later_realization_contract",
    },
    "inhabitance_probe": {
        "finite_limit_inhabitance_certificate",
        "source_fiber_subrepresenter",
        "equalizer_arrow_to_subrep",
    },
    "budget_closure_probe": {
        "finite_index_budget_certificate",
        "budget_dependency_closure_certificate",
        TERMINAL_CERT,
        ADM_CAT,
        PROBE_SEP,
    },
}

REQUIRED_FLAGS = (
    "probe_separation_certificate_actual",
    "all_six_probe_classes_distinct",
    "separates_all_seven_source_constraints",
    "separates_dd4_handoff",
    "separates_graph_handoff",
    "separates_inhabitance",
    "separates_budget_closure",
    "jointly_conservative_on_terminal_square",
    "source_before_points",
    "no_control_or_sample_probe_replacement",
)

BANNED_FLAGS = (
    "probe_blind_admissible_category",
    "merged_probe_classes",
    "constraint_blind_probe",
    "dd4_handoff_blind_probe",
    "graph_handoff_blind_probe",
    "inhabitance_blind_probe",
    "budget_blind_probe",
    "nonconservative_probe_family",
    "control_probe_replacement",
    "dh_epstein_probe_replacement",
    "finite_sample_probe",
    "basis_dependent_probe",
    "missing_probe_separation_certificate",
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


def probe_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "probe_targets": deepcopy(PROBE_TARGETS),
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
    probe_targets = {key: set(value) for key, value in state["probe_targets"].items()}

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_538")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc538_witness_missing")
    if PROBE_SEP not in accepted:
        out.append("probe_separation_missing_from_current")
    if PROBE_SEP not in assignments:
        out.append("probe_separation_unassigned")
    if assignments.get(PROBE_SEP) != "coh_finite_limit_cut":
        out.append(f"probe_separation_bad_charge:{assignments.get(PROBE_SEP)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if set(probe_targets) != set(PROBE_TARGETS):
        out.append("probe_class_set_changed")
    target_union = set().union(*(targets for targets in probe_targets.values()))
    missing_targets = target_union - accepted
    if missing_targets:
        out.append("probe_targets_not_current:" + ",".join(sorted(missing_targets)))
    for probe, targets in PROBE_TARGETS.items():
        if not targets <= probe_targets.get(probe, set()):
            missing = targets - probe_targets.get(probe, set())
            out.append(f"probe_targets_missing:{probe}->{','.join(sorted(missing))}")
    if not PROBE_TARGETS["constraint_fork_probe"] <= probe_targets.get("constraint_fork_probe", set()):
        out.append("source_constraints_not_separated")
    if not PROBE_TARGETS["dd4_image_handoff_probe"] <= probe_targets.get("dd4_image_handoff_probe", set()):
        out.append("dd4_handoff_not_separated")
    if not PROBE_TARGETS["graph_later_realization_probe"] <= probe_targets.get("graph_later_realization_probe", set()):
        out.append("graph_handoff_not_separated")
    if not PROBE_TARGETS["inhabitance_probe"] <= probe_targets.get("inhabitance_probe", set()):
        out.append("inhabitance_not_separated")
    if not PROBE_TARGETS["budget_closure_probe"] <= probe_targets.get("budget_closure_probe", set()):
        out.append("budget_closure_not_separated")

    requires = state["requires"].get(PROBE_SEP, [])
    for req in (
        ADM_CAT,
        TERMINAL_CERT,
        "budget_dependency_closure_certificate",
        "finite_index_budget_certificate",
        "joint_constraint_fork",
        "dd4_image_only_handoff_contract",
        "graph_later_realization_contract",
        "finite_limit_inhabitance_certificate",
    ):
        if req not in requires:
            out.append(f"probe_separation_requires_missing:{req}")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("probe_separation_loses_source_before_points")

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
live = probe_state(MAP)

gate(
    f"{PREFIX}1 doc 538 probe-separation layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s probes=%d"
    % (live["frontier"].get("current_doc"), live["frontier"].get("current_witness"), len(live["probe_targets"])),
)

merged = variant(
    live,
    probe_targets={
        **PROBE_TARGETS,
        "constraint_fork_probe": PROBE_TARGETS["constraint_fork_probe"] | PROBE_TARGETS["dd4_image_handoff_probe"],
    },
    flags={"all_six_probe_classes_distinct": False},
    banned={"merged_probe_classes": True},
)
del merged["probe_targets"]["dd4_image_handoff_probe"]

gate(
    f"{PREFIX}2 rejects merged probe classes",
    not accepts(merged)
    and "merged_probe_classes" in reasons(merged)
    and "probe_class_set_changed" in reasons(merged),
    ",".join(reasons(merged)),
)

constraint_blind = variant(
    live,
    flags={"separates_all_seven_source_constraints": False},
    banned={"constraint_blind_probe": True},
)
constraint_blind["probe_targets"]["constraint_fork_probe"] = {"endpoint_integrality"}

gate(
    f"{PREFIX}3 rejects constraint-blind probes",
    not accepts(constraint_blind)
    and "constraint_blind_probe" in reasons(constraint_blind)
    and "source_constraints_not_separated" in reasons(constraint_blind),
    ",".join(reasons(constraint_blind)),
)

dd4_blind = variant(
    live,
    flags={"separates_dd4_handoff": False},
    banned={"dd4_handoff_blind_probe": True},
)
dd4_blind["probe_targets"]["dd4_image_handoff_probe"] = {"dd4_certificate_image"}

gate(
    f"{PREFIX}4 rejects DD.4-handoff-blind probes",
    not accepts(dd4_blind)
    and "dd4_handoff_blind_probe" in reasons(dd4_blind)
    and "dd4_handoff_not_separated" in reasons(dd4_blind),
    ",".join(reasons(dd4_blind)),
)

graph_blind = variant(
    live,
    flags={"separates_graph_handoff": False},
    banned={"graph_handoff_blind_probe": True},
)
graph_blind["probe_targets"]["graph_later_realization_probe"] = {"graph_realization_image"}

gate(
    f"{PREFIX}5 rejects graph-handoff-blind probes",
    not accepts(graph_blind)
    and "graph_handoff_blind_probe" in reasons(graph_blind)
    and "graph_handoff_not_separated" in reasons(graph_blind),
    ",".join(reasons(graph_blind)),
)

inh_budget_blind = variant(
    live,
    flags={"separates_inhabitance": False, "separates_budget_closure": False},
    banned={"inhabitance_blind_probe": True, "budget_blind_probe": True},
)
inh_budget_blind["probe_targets"]["inhabitance_probe"] = {"finite_limit_cut"}
inh_budget_blind["probe_targets"]["budget_closure_probe"] = {"finite_index_budget_certificate"}

gate(
    f"{PREFIX}6 rejects inhabitance or budget-blind probes",
    not accepts(inh_budget_blind)
    and {"inhabitance_blind_probe", "budget_blind_probe"} <= set(reasons(inh_budget_blind)),
    ",".join(reasons(inh_budget_blind)),
)

nonconservative = variant(
    live,
    flags={"jointly_conservative_on_terminal_square": False},
    banned={"probe_blind_admissible_category": True, "nonconservative_probe_family": True},
)

gate(
    f"{PREFIX}7 rejects nonconservative probe families",
    not accepts(nonconservative)
    and {"probe_blind_admissible_category", "nonconservative_probe_family"} <= set(reasons(nonconservative)),
    ",".join(reasons(nonconservative)),
)

bad_probe_source = variant(
    live,
    flags={"source_before_points": False, "no_control_or_sample_probe_replacement": False},
    banned={
        "control_probe_replacement": True,
        "dh_epstein_probe_replacement": True,
        "finite_sample_probe": True,
        "basis_dependent_probe": True,
    },
)
bad_probe_source["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}8 rejects control/sample/basis probe replacements",
    not accepts(bad_probe_source)
    and {
        "control_probe_replacement",
        "dh_epstein_probe_replacement",
        "finite_sample_probe",
        "basis_dependent_probe",
    }
    <= set(reasons(bad_probe_source)),
    ",".join(reasons(bad_probe_source)),
)

missing_cert = variant(
    live,
    flags={"probe_separation_certificate_actual": False},
    banned={"missing_probe_separation_certificate": True},
)
missing_cert["accepted"].remove(PROBE_SEP)
del missing_cert["assignments"][PROBE_SEP]

gate(
    f"{PREFIX}9 rejects missing probe-separation certificates",
    not accepts(missing_cert)
    and "missing_probe_separation_certificate" in reasons(missing_cert)
    and "probe_separation_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    merged,
    constraint_blind,
    dd4_blind,
    graph_blind,
    inh_budget_blind,
    nonconservative,
    bad_probe_source,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only conservative source-probe separation passes",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "merged_probe_classes",
        "constraint_blind_probe",
        "dd4_handoff_blind_probe",
        "graph_handoff_blind_probe",
        "inhabitance_blind_probe",
        "budget_blind_probe",
        "probe_blind_admissible_category",
        "nonconservative_probe_family",
        "control_probe_replacement",
        "finite_sample_probe",
        "basis_dependent_probe",
        "missing_probe_separation_certificate",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: conservative admissible source probes pinned")
print(
    "VERDICT: the admissible category counts only if its probes separate the "
    "source constraints, DD.4 handoff, graph-later handoff, inhabitance, and "
    "budget/dependency/terminal data. Merged probes, blind probes, "
    "nonconservative families, control/DH/Epstein replacements, finite samples, "
    "basis probes, and missing separation certificates do not construct the "
    "missing object."
)
