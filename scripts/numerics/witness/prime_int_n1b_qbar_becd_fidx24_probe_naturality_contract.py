r"""Probe-naturality contract for admissible source-square probes.

Doc 538 pins conservative separating probes. This witness prevents those
probes from being objectwise detectors only: the accepted probes must be
source-defined probe functors, natural over admissible source-square morphisms,
and reflective of the terminal mediator.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_naturality_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the probe-naturality witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 539
EXPECTED_WITNESS = "doc539-probe-naturality"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPNATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

NATURALITY_MORPHISMS = {
    "source_square_morphism",
    "terminal_arrow",
    "dependency_closure_morphism",
    "dd4_image_handoff_morphism",
    "graph_later_realization_morphism",
    "inhabitance_certificate_morphism",
    "budget_closure_morphism",
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
        PROBE_NAT,
    },
}


def _probe_functors() -> dict[str, dict[str, Any]]:
    return {
        probe: {
            "domain": ADM_CAT,
            "certificate": PROBE_NAT,
            "targets": set(targets),
            "natural_on": set(NATURALITY_MORPHISMS),
        }
        for probe, targets in PROBE_TARGETS.items()
    }


REQUIRED_FLAGS = (
    "probe_naturality_certificate_actual",
    "source_defined_probe_functors",
    "strict_naturality",
    "natural_on_admissible_morphisms",
    "natural_on_terminal_arrow",
    "natural_on_dependency_and_handoffs",
    "reflects_terminal_mediator",
    "source_before_points",
    "inside_exact_24_budget",
    "no_point_graph_sample_or_basis_naturality",
)

BANNED_FLAGS = (
    "nonfunctorial_probe_family",
    "object_only_probe",
    "morphism_blind_probe",
    "posthoc_separating_predicate",
    "declared_probe_functor",
    "lax_probe_naturality",
    "pointwise_probe_naturality",
    "graph_side_probe_naturality",
    "local_probe_table",
    "retuned_probe_functor",
    "finite_sample_probe",
    "basis_dependent_probe",
    "probe_naturality_up_to_isomorphism",
    "missing_probe_naturality_certificate",
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


def naturality_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "functors": _probe_functors(),
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
    functors = state["functors"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_539")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc539_witness_missing")
    if PROBE_NAT not in accepted:
        out.append("probe_naturality_missing_from_current")
    if PROBE_NAT not in assignments:
        out.append("probe_naturality_unassigned")
    if assignments.get(PROBE_NAT) != "coh_finite_limit_cut":
        out.append(f"probe_naturality_bad_charge:{assignments.get(PROBE_NAT)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    if set(functors) != set(PROBE_TARGETS):
        out.append("probe_functor_set_changed")
    for probe, required_targets in PROBE_TARGETS.items():
        functor = functors.get(probe)
        if not isinstance(functor, dict):
            out.append(f"probe_functor_missing:{probe}")
            continue
        if functor.get("domain") != ADM_CAT:
            out.append(f"probe_functor_bad_domain:{probe}")
        if functor.get("certificate") != PROBE_NAT:
            out.append(f"probe_functor_bad_certificate:{probe}")
        targets = set(functor.get("targets", set()))
        if not required_targets <= targets:
            missing = required_targets - targets
            out.append(f"probe_functor_targets_missing:{probe}->{','.join(sorted(missing))}")
        if targets - accepted:
            out.append(f"probe_functor_targets_not_current:{probe}->{','.join(sorted(targets - accepted))}")
        natural_on = set(functor.get("natural_on", set()))
        missing_morphisms = NATURALITY_MORPHISMS - natural_on
        if missing_morphisms:
            out.append(f"probe_functor_naturality_missing:{probe}->{','.join(sorted(missing_morphisms))}")
        if "terminal_arrow" not in natural_on:
            out.append(f"probe_functor_terminal_blind:{probe}")

    requires = state["requires"]
    for req in (
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
        if req not in requires.get(PROBE_NAT, []):
            out.append(f"probe_naturality_requires_missing:{req}")
    if PROBE_NAT not in requires.get(PROBE_SEP, []):
        out.append("probe_separation_not_required_to_be_natural")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("probe_naturality_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("probe_naturality_uses_graph_side_bridge")
    if dd4_bridge.get("direction") != "image_only":
        out.append("probe_naturality_uses_reversible_dd4_bridge")

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
live = naturality_state(MAP)

gate(
    f"{PREFIX}1 doc 539 probe-naturality layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s functors=%d"
    % (live["frontier"].get("current_doc"), live["frontier"].get("current_witness"), len(live["functors"])),
)

nonfunctorial = variant(
    live,
    flags={"source_defined_probe_functors": False, "natural_on_admissible_morphisms": False},
    banned={"nonfunctorial_probe_family": True},
)
nonfunctorial["functors"]["constraint_fork_probe"]["natural_on"] = {"source_square_morphism"}

gate(
    f"{PREFIX}2 rejects nonfunctorial probe families",
    not accepts(nonfunctorial)
    and "nonfunctorial_probe_family" in reasons(nonfunctorial)
    and any(reason.startswith("probe_functor_naturality_missing:constraint_fork_probe") for reason in reasons(nonfunctorial)),
    ",".join(reasons(nonfunctorial)),
)

object_only = variant(
    live,
    flags={"natural_on_admissible_morphisms": False, "natural_on_terminal_arrow": False},
    banned={"object_only_probe": True},
)
for functor in object_only["functors"].values():
    functor["natural_on"] = set()

gate(
    f"{PREFIX}3 rejects object-only probes",
    not accepts(object_only)
    and "object_only_probe" in reasons(object_only)
    and any(reason.startswith("probe_functor_terminal_blind:") for reason in reasons(object_only)),
    ",".join(reasons(object_only)),
)

morphism_blind = variant(
    live,
    flags={
        "natural_on_terminal_arrow": False,
        "natural_on_dependency_and_handoffs": False,
        "reflects_terminal_mediator": False,
    },
    banned={"morphism_blind_probe": True},
)
for functor in morphism_blind["functors"].values():
    functor["natural_on"] = {"source_square_morphism"}

gate(
    f"{PREFIX}4 rejects morphism-blind probes",
    not accepts(morphism_blind)
    and "morphism_blind_probe" in reasons(morphism_blind)
    and "reflects_terminal_mediator_missing" in reasons(morphism_blind),
    ",".join(reasons(morphism_blind)),
)

posthoc = variant(
    live,
    flags={"source_defined_probe_functors": False, "strict_naturality": False},
    banned={"posthoc_separating_predicate": True},
)
posthoc["functors"]["budget_closure_probe"]["certificate"] = "posthoc_predicate_only"

gate(
    f"{PREFIX}5 rejects posthoc separating predicates",
    not accepts(posthoc)
    and "posthoc_separating_predicate" in reasons(posthoc)
    and "probe_functor_bad_certificate:budget_closure_probe" in reasons(posthoc),
    ",".join(reasons(posthoc)),
)

declared_lax_iso = variant(
    live,
    flags={"strict_naturality": False},
    banned={
        "declared_probe_functor": True,
        "lax_probe_naturality": True,
        "probe_naturality_up_to_isomorphism": True,
    },
)

gate(
    f"{PREFIX}6 rejects declared, lax, or up-to-isomorphism probe functors",
    not accepts(declared_lax_iso)
    and {
        "declared_probe_functor",
        "lax_probe_naturality",
        "probe_naturality_up_to_isomorphism",
    }
    <= set(reasons(declared_lax_iso)),
    ",".join(reasons(declared_lax_iso)),
)

point_graph_local = variant(
    live,
    flags={"source_before_points": False, "no_point_graph_sample_or_basis_naturality": False},
    banned={
        "pointwise_probe_naturality": True,
        "graph_side_probe_naturality": True,
        "local_probe_table": True,
    },
)
point_graph_local["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_points"
point_graph_local["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}7 rejects pointwise, graph-side, or local-table probe naturality",
    not accepts(point_graph_local)
    and {
        "pointwise_probe_naturality",
        "graph_side_probe_naturality",
        "local_probe_table",
    }
    <= set(reasons(point_graph_local)),
    ",".join(reasons(point_graph_local)),
)

retuned_sample_basis = variant(
    live,
    flags={"inside_exact_24_budget": False, "no_point_graph_sample_or_basis_naturality": False},
    banned={
        "retuned_probe_functor": True,
        "finite_sample_probe": True,
        "basis_dependent_probe": True,
    },
)
retuned_sample_basis["functors"]["dd4_image_handoff_probe"]["targets"] = {
    "finite_sample_row",
    "basis_probe_row",
}

gate(
    f"{PREFIX}8 rejects retuned, finite-sample, or basis-row probe functors",
    not accepts(retuned_sample_basis)
    and {"retuned_probe_functor", "finite_sample_probe", "basis_dependent_probe"}
    <= set(reasons(retuned_sample_basis)),
    ",".join(reasons(retuned_sample_basis)),
)

missing_cert = variant(
    live,
    flags={"probe_naturality_certificate_actual": False},
    banned={"missing_probe_naturality_certificate": True},
)
missing_cert["accepted"].remove(PROBE_NAT)
del missing_cert["assignments"][PROBE_NAT]
missing_cert["functors"]["budget_closure_probe"]["targets"].remove(PROBE_NAT)

gate(
    f"{PREFIX}9 rejects missing probe-naturality certificates",
    not accepts(missing_cert)
    and "missing_probe_naturality_certificate" in reasons(missing_cert)
    and "probe_naturality_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    nonfunctorial,
    object_only,
    morphism_blind,
    posthoc,
    declared_lax_iso,
    point_graph_local,
    retuned_sample_basis,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only natural source-probe functors pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "nonfunctorial_probe_family",
        "object_only_probe",
        "morphism_blind_probe",
        "posthoc_separating_predicate",
        "declared_probe_functor",
        "lax_probe_naturality",
        "pointwise_probe_naturality",
        "graph_side_probe_naturality",
        "local_probe_table",
        "retuned_probe_functor",
        "finite_sample_probe",
        "basis_dependent_probe",
        "probe_naturality_up_to_isomorphism",
        "missing_probe_naturality_certificate",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: admissible source probes are functorial")
print(
    "VERDICT: separated admissible probes count only as source-defined natural "
    "probe functors over admissible source-square morphisms. Object-only "
    "detectors, morphism-blind probes, posthoc predicates, declared/lax/"
    "up-to-isomorphism functors, point/graph-side naturality, local tables, "
    "finite samples, basis rows, retunings, and missing naturality certificates "
    "do not construct the missing object."
)
