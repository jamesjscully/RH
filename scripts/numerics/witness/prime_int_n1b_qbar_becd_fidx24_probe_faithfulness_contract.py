r"""Probe-faithfulness contract for admissible source-square probes.

Doc 539 pins natural source-defined probe functors. This witness prevents
their naturality from becoming quotient naturality: the six probe functors
must be jointly faithful on the source-square morphism skeleton.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_faithfulness_contract
"""

from __future__ import annotations

from copy import deepcopy
from itertools import combinations
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the probe-faithfulness witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 540
EXPECTED_WITNESS = "doc540-probe-faithfulness"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

COMPOSITION_LAWS = {
    "dependency_then_budget": (
        "dependency_closure_morphism",
        "budget_closure_morphism",
        "composite_dependency_budget_morphism",
    ),
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
        PROBE_FAITH,
    },
}


def _probe_functors() -> dict[str, dict[str, Any]]:
    return {
        probe: {
            "domain": ADM_CAT,
            "certificate": PROBE_FAITH,
            "targets": set(targets),
            "morphism_images": {
                morphism: f"{probe}:{morphism}" for morphism in SOURCE_MORPHISMS
            },
        }
        for probe, targets in PROBE_TARGETS.items()
    }


REQUIRED_FLAGS = (
    "probe_faithfulness_certificate_actual",
    "jointly_faithful_on_source_morphisms",
    "reflects_identities",
    "reflects_composition",
    "reflects_terminal_arrow",
    "reflects_dependency_morphisms",
    "reflects_handoff_morphisms",
    "source_before_points",
    "inside_exact_24_budget",
    "no_point_graph_sample_basis_or_quotient",
)

BANNED_FLAGS = (
    "nonfaithful_probe_family",
    "morphism_quotient_probe",
    "automorphism_mask_probe",
    "isomorphism_collapse_probe",
    "identity_blind_probe",
    "composition_blind_probe",
    "terminal_arrow_blind_probe",
    "dependency_morphism_blind_probe",
    "handoff_morphism_blind_probe",
    "point_graph_morphism_shadow",
    "finite_morphism_sample_probe",
    "basis_row_morphism_probe",
    "missing_probe_faithfulness_certificate",
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


def faithfulness_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "functors": _probe_functors(),
        "composition_laws": set(COMPOSITION_LAWS),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def joint_image(functors: dict[str, dict[str, Any]], morphism: str) -> tuple[str, ...]:
    return tuple(
        str(functors[probe].get("morphism_images", {}).get(morphism))
        for probe in sorted(PROBE_TARGETS)
    )


def duplicate_morphism_pairs(functors: dict[str, dict[str, Any]]) -> list[tuple[str, str]]:
    duplicates: list[tuple[str, str]] = []
    for left, right in combinations(sorted(SOURCE_MORPHISMS), 2):
        if joint_image(functors, left) == joint_image(functors, right):
            duplicates.append((left, right))
    return duplicates


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    assignments = dict(state["assignments"])
    functors = state["functors"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_540")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc540_witness_missing")
    if PROBE_FAITH not in accepted:
        out.append("probe_faithfulness_missing_from_current")
    if PROBE_FAITH not in assignments:
        out.append("probe_faithfulness_unassigned")
    if assignments.get(PROBE_FAITH) != "coh_finite_limit_cut":
        out.append(f"probe_faithfulness_bad_charge:{assignments.get(PROBE_FAITH)}")
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
        if functor.get("certificate") != PROBE_FAITH:
            out.append(f"probe_functor_bad_certificate:{probe}")
        targets = set(functor.get("targets", set()))
        if not required_targets <= targets:
            missing = required_targets - targets
            out.append(f"probe_functor_targets_missing:{probe}->{','.join(sorted(missing))}")
        if targets - accepted:
            out.append(f"probe_functor_targets_not_current:{probe}->{','.join(sorted(targets - accepted))}")
        morphism_images = functor.get("morphism_images", {})
        missing_morphisms = SOURCE_MORPHISMS - set(morphism_images)
        if missing_morphisms:
            out.append(f"probe_functor_morphisms_missing:{probe}->{','.join(sorted(missing_morphisms))}")

    duplicates = duplicate_morphism_pairs(functors)
    if duplicates:
        rendered = ",".join(f"{left}={right}" for left, right in duplicates)
        out.append("probe_family_not_jointly_faithful:" + rendered)

    if "id_source_square" not in SOURCE_MORPHISMS:
        out.append("identity_morphism_missing")
    for law, (left, right, composite) in COMPOSITION_LAWS.items():
        if law not in state["composition_laws"]:
            out.append(f"composition_law_missing:{law}")
        for morphism in (left, right, composite):
            if morphism not in SOURCE_MORPHISMS:
                out.append(f"composition_law_unknown_morphism:{law}:{morphism}")

    requires = state["requires"]
    for req in (
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
        if req not in requires.get(PROBE_FAITH, []):
            out.append(f"probe_faithfulness_requires_missing:{req}")
    if PROBE_FAITH not in requires.get(PROBE_NAT, []):
        out.append("probe_naturality_not_required_to_be_faithful")

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("probe_faithfulness_loses_source_before_points")
    if graph_bridge.get("direction") != "realizes_later":
        out.append("probe_faithfulness_uses_graph_side_bridge")

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
live = faithfulness_state(MAP)

gate(
    f"{PREFIX}1 doc 540 probe-faithfulness layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s morphisms=%d"
    % (live["frontier"].get("current_doc"), live["frontier"].get("current_witness"), len(SOURCE_MORPHISMS)),
)

nonfaithful = variant(
    live,
    flags={"jointly_faithful_on_source_morphisms": False},
    banned={"nonfaithful_probe_family": True},
)
for functor in nonfaithful["functors"].values():
    functor["morphism_images"]["terminal_arrow"] = functor["morphism_images"]["source_square_morphism"]

gate(
    f"{PREFIX}2 rejects nonfaithful probe families",
    not accepts(nonfaithful)
    and "nonfaithful_probe_family" in reasons(nonfaithful)
    and any(reason.startswith("probe_family_not_jointly_faithful:") for reason in reasons(nonfaithful)),
    ",".join(reasons(nonfaithful)),
)

quotient_mask = variant(
    live,
    flags={"jointly_faithful_on_source_morphisms": False, "no_point_graph_sample_basis_or_quotient": False},
    banned={"morphism_quotient_probe": True, "automorphism_mask_probe": True},
)
for functor in quotient_mask["functors"].values():
    functor["morphism_images"]["dd4_image_handoff_morphism"] = functor["morphism_images"][
        "graph_later_realization_morphism"
    ]

gate(
    f"{PREFIX}3 rejects morphism quotients and automorphism masks",
    not accepts(quotient_mask)
    and {"morphism_quotient_probe", "automorphism_mask_probe"} <= set(reasons(quotient_mask)),
    ",".join(reasons(quotient_mask)),
)

iso_collapse = variant(
    live,
    flags={"jointly_faithful_on_source_morphisms": False},
    banned={"isomorphism_collapse_probe": True},
)
for functor in iso_collapse["functors"].values():
    functor["morphism_images"]["source_square_morphism"] = functor["morphism_images"]["id_source_square"]

gate(
    f"{PREFIX}4 rejects isomorphism collapses",
    not accepts(iso_collapse)
    and "isomorphism_collapse_probe" in reasons(iso_collapse)
    and any(reason.startswith("probe_family_not_jointly_faithful:") for reason in reasons(iso_collapse)),
    ",".join(reasons(iso_collapse)),
)

id_comp_blind = variant(
    live,
    flags={"reflects_identities": False, "reflects_composition": False},
    banned={"identity_blind_probe": True, "composition_blind_probe": True},
)
for functor in id_comp_blind["functors"].values():
    del functor["morphism_images"]["id_source_square"]
id_comp_blind["composition_laws"].remove("dependency_then_budget")

gate(
    f"{PREFIX}5 rejects identity- or composition-blind probes",
    not accepts(id_comp_blind)
    and {"identity_blind_probe", "composition_blind_probe"} <= set(reasons(id_comp_blind)),
    ",".join(reasons(id_comp_blind)),
)

terminal_blind = variant(
    live,
    flags={"reflects_terminal_arrow": False},
    banned={"terminal_arrow_blind_probe": True},
)
for functor in terminal_blind["functors"].values():
    del functor["morphism_images"]["terminal_arrow"]

gate(
    f"{PREFIX}6 rejects terminal-arrow-blind probes",
    not accepts(terminal_blind)
    and "terminal_arrow_blind_probe" in reasons(terminal_blind)
    and any(reason.startswith("probe_functor_morphisms_missing:") for reason in reasons(terminal_blind)),
    ",".join(reasons(terminal_blind)),
)

dependency_handoff_blind = variant(
    live,
    flags={"reflects_dependency_morphisms": False, "reflects_handoff_morphisms": False},
    banned={"dependency_morphism_blind_probe": True, "handoff_morphism_blind_probe": True},
)
for functor in dependency_handoff_blind["functors"].values():
    functor["morphism_images"].pop("dependency_closure_morphism")
    functor["morphism_images"].pop("dd4_image_handoff_morphism")
    functor["morphism_images"].pop("graph_later_realization_morphism")

gate(
    f"{PREFIX}7 rejects dependency- or handoff-morphism-blind probes",
    not accepts(dependency_handoff_blind)
    and {"dependency_morphism_blind_probe", "handoff_morphism_blind_probe"}
    <= set(reasons(dependency_handoff_blind)),
    ",".join(reasons(dependency_handoff_blind)),
)

point_graph_sample_basis = variant(
    live,
    flags={"source_before_points": False, "inside_exact_24_budget": False, "no_point_graph_sample_basis_or_quotient": False},
    banned={
        "point_graph_morphism_shadow": True,
        "finite_morphism_sample_probe": True,
        "basis_row_morphism_probe": True,
    },
)
point_graph_sample_basis["bridges"]["graph_realization_bridge"]["direction"] = "graph_side_morphism_shadow"
point_graph_sample_basis["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False
for functor in point_graph_sample_basis["functors"].values():
    functor["morphism_images"]["budget_closure_morphism"] = "finite_sample_row"
    functor["morphism_images"]["inhabitance_certificate_morphism"] = "basis_row"

gate(
    f"{PREFIX}8 rejects point/graph shadows, finite samples, or basis morphism probes",
    not accepts(point_graph_sample_basis)
    and {
        "point_graph_morphism_shadow",
        "finite_morphism_sample_probe",
        "basis_row_morphism_probe",
    }
    <= set(reasons(point_graph_sample_basis)),
    ",".join(reasons(point_graph_sample_basis)),
)

missing_cert = variant(
    live,
    flags={"probe_faithfulness_certificate_actual": False},
    banned={"missing_probe_faithfulness_certificate": True},
)
missing_cert["accepted"].remove(PROBE_FAITH)
del missing_cert["assignments"][PROBE_FAITH]
missing_cert["functors"]["budget_closure_probe"]["targets"].remove(PROBE_FAITH)

gate(
    f"{PREFIX}9 rejects missing probe-faithfulness certificates",
    not accepts(missing_cert)
    and "missing_probe_faithfulness_certificate" in reasons(missing_cert)
    and "probe_faithfulness_missing_from_current" in reasons(missing_cert),
    ",".join(reasons(missing_cert)),
)

variants = [
    nonfaithful,
    quotient_mask,
    iso_collapse,
    id_comp_blind,
    terminal_blind,
    dependency_handoff_blind,
    point_graph_sample_basis,
    missing_cert,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only jointly faithful natural source-probe functors pass",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "nonfaithful_probe_family",
        "morphism_quotient_probe",
        "automorphism_mask_probe",
        "isomorphism_collapse_probe",
        "identity_blind_probe",
        "composition_blind_probe",
        "terminal_arrow_blind_probe",
        "dependency_morphism_blind_probe",
        "handoff_morphism_blind_probe",
        "point_graph_morphism_shadow",
        "finite_morphism_sample_probe",
        "basis_row_morphism_probe",
        "missing_probe_faithfulness_certificate",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: admissible source probes are jointly faithful")
print(
    "VERDICT: natural admissible probes count only if their product reflects "
    "the source-square morphism skeleton. Nonfaithful families, morphism "
    "quotients, automorphism masks, isomorphism collapses, identity/"
    "composition/terminal/dependency/handoff blindness, point/graph shadows, "
    "finite morphism samples, basis-row tests, and missing faithfulness "
    "certificates do not construct the missing object."
)
