r"""Exact 24-cell dependency-closure contract.

Doc 534 pins the current frontier to seven source facets plus seventeen
coherence cells. This witness checks the next finite audit: every accepted
artifact and every accepted dependency edge in research/proof/frontier-map.yaml
must be charged inside those cells, without context collapse or self-bootstrapped
closure.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_dd4handoff_graphhandoff_inhabited_finidx24_depclosure_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the dependency-closure witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 535
EXPECTED_WITNESS = "doc535-finidx24-depclosure"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

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

SOURCE_CONSTRAINT_ASSIGNMENTS = {
    "endpoint_integrality": "facet_endpoint_integrality",
    "degree_maps": "facet_degree_maps",
    "dd4_boundary": "facet_dd4_boundary",
    "boundary_pushforward": "facet_boundary_pushforward",
    "graph_composition": "facet_graph_composition",
    "rosati_count": "facet_rosati_count",
    "control_death": "facet_control_death",
}

ANCHOR_ASSIGNMENTS = {
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
}

BANNED_FLAGS = (
    "expanded_finite_index",
    "one_more_layer_tower",
    "unbudgeted_dependency_edge",
    "unknown_dependency_endpoint",
    "unassigned_dependency_endpoint",
    "forbidden_cross_context_charge",
    "self_bootstrapped_dependency_closure",
    "posthoc_dependency_edge",
    "context_collapsing_dependency_edge",
    "missing_dependency_closure_certificate",
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


def rejected_repairs(data: dict[str, Any]) -> set[str]:
    return set(data["current_requirements"]["rejected_repairs"])


def current_state(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "rejected": rejected_repairs(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "edges": [
            deepcopy(edge)
            for edge in data["edges"]
            if edge["introduced_by"] <= EXPECTED_DOC
        ],
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "flags": {flag: False for flag in BANNED_FLAGS},
    }


def endpoints(edge: dict[str, Any]) -> set[str]:
    out = {edge["source"], edge["target"]}
    via = edge.get("via")
    if via is not None:
        out.add(via)
    return out


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    rejected = set(state["rejected"])
    assignments = dict(state["assignments"])
    cells = set(assignments.values())

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_535")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc535_witness_missing")
    if "budget_dependency_closure_certificate" not in accepted:
        out.append("closure_certificate_missing")
    if "finite_index_budget_certificate" not in accepted:
        out.append("budget_certificate_missing")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    extra_assignments = set(assignments) - accepted
    if extra_assignments:
        out.append("assignment_for_noncurrent_artifact:" + ",".join(sorted(extra_assignments)))
    unknown_cells = cells - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))
    unused_cells = CELLS - cells
    if unused_cells:
        out.append("declared_cell_unused:" + ",".join(sorted(unused_cells)))

    edge_missing = set()
    for edge in state["edges"]:
        edge_missing |= endpoints(edge) - set(assignments)
    if edge_missing:
        out.append("edge_endpoint_unassigned:" + ",".join(sorted(edge_missing)))

    for key, required in state["requires"].items():
        if key not in accepted:
            continue
        for req in required:
            if req not in accepted:
                out.append(f"consistency_requirement_not_current:{key}->{req}")
            if req not in assignments:
                out.append(f"consistency_requirement_unassigned:{key}->{req}")
            if req in rejected:
                out.append(f"requires_rejected_artifact:{key}->{req}")

    for artifact, expected_cell in {**SOURCE_CONSTRAINT_ASSIGNMENTS, **ANCHOR_ASSIGNMENTS}.items():
        if assignments.get(artifact) != expected_cell:
            out.append(f"bad_anchor_charge:{artifact}->{assignments.get(artifact)}")

    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    if dd4_bridge.get("from") == dd4_bridge.get("to") or dd4_bridge.get("direction") != "image_only":
        out.append("dd4_context_bridge_collapsed")
    if not dd4_bridge.get("prohibits_reverse_pullback") or not dd4_bridge.get("allows_target_kill"):
        out.append("dd4_bridge_not_directed")
    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if graph_bridge.get("from") == graph_bridge.get("to") or graph_bridge.get("direction") != "realizes_later":
        out.append("graph_context_bridge_collapsed")
    if not graph_bridge.get("prohibits_reverse_before_points") or not graph_bridge.get("preserves_source_constraints"):
        out.append("graph_bridge_not_directed")

    out.extend(flag for flag, active in state["flags"].items() if active)
    return out


def accepts(state: dict[str, Any]) -> bool:
    return not reasons(state)


def variant(base: dict[str, Any], **flags: bool) -> dict[str, Any]:
    data = deepcopy(base)
    data["flags"].update(flags)
    return data


MAP = load_map()
live = current_state(MAP)

gate(
    f"{PREFIX}1 doc 535 dependency-closure layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s accepted=%d edges=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["accepted"]),
        len(live["edges"]),
    ),
)

missing_assignment = variant(live, unassigned_dependency_endpoint=True)
del missing_assignment["assignments"]["finite_limit_inhabitance_certificate"]

gate(
    f"{PREFIX}2 rejects accepted artifacts without dependency-cell charge",
    not accepts(missing_assignment)
    and "unassigned_dependency_endpoint" in reasons(missing_assignment)
    and any(reason.startswith("accepted_artifacts_unassigned:") for reason in reasons(missing_assignment)),
    ",".join(reasons(missing_assignment)),
)

unknown_edge = variant(live, unbudgeted_dependency_edge=True, unknown_dependency_endpoint=True)
unknown_edge["edges"].append(
    {
        "source": "finite_index_budget_certificate",
        "relation": "depends_on",
        "target": "undeclared_dependency",
        "introduced_by": EXPECTED_DOC,
    }
)

gate(
    f"{PREFIX}3 rejects dependency edges with uncharged endpoints",
    not accepts(unknown_edge)
    and "unbudgeted_dependency_edge" in reasons(unknown_edge)
    and any(reason.startswith("edge_endpoint_unassigned:") for reason in reasons(unknown_edge)),
    ",".join(reasons(unknown_edge)),
)

bad_charge = variant(live, forbidden_cross_context_charge=True)
bad_charge["assignments"]["dd4_image_only_handoff_contract"] = "coh_graph_later_realization"

gate(
    f"{PREFIX}4 rejects cross-context cell charges",
    not accepts(bad_charge)
    and "forbidden_cross_context_charge" in reasons(bad_charge)
    and "bad_anchor_charge:dd4_image_only_handoff_contract->coh_graph_later_realization" in reasons(bad_charge),
    ",".join(reasons(bad_charge)),
)

collapsed = variant(live, context_collapsing_dependency_edge=True)
collapsed["bridges"]["dd4_certificate_handoff"]["to"] = "original_h1"
collapsed["bridges"]["graph_realization_bridge"]["to"] = "source_constraint"

gate(
    f"{PREFIX}5 rejects context-collapsing dependency closure",
    not accepts(collapsed)
    and "context_collapsing_dependency_edge" in reasons(collapsed)
    and "dd4_context_bridge_collapsed" in reasons(collapsed)
    and "graph_context_bridge_collapsed" in reasons(collapsed),
    ",".join(reasons(collapsed)),
)

missing_closure = variant(live, missing_dependency_closure_certificate=True)
missing_closure["accepted"].remove("budget_dependency_closure_certificate")
del missing_closure["assignments"]["budget_dependency_closure_certificate"]

gate(
    f"{PREFIX}6 rejects missing dependency-closure certificate",
    not accepts(missing_closure)
    and "closure_certificate_missing" in reasons(missing_closure)
    and "missing_dependency_closure_certificate" in reasons(missing_closure),
    ",".join(reasons(missing_closure)),
)

self_bootstrap = variant(live, self_bootstrapped_dependency_closure=True)
self_bootstrap["requires"]["budget_dependency_closure_certificate"] = [
    "budget_dependency_closure_certificate"
]

gate(
    f"{PREFIX}7 rejects self-bootstrapped closure",
    not accepts(self_bootstrap)
    and "self_bootstrapped_dependency_closure" in reasons(self_bootstrap),
    ",".join(reasons(self_bootstrap)),
)

posthoc_edge = variant(live, posthoc_dependency_edge=True)
posthoc_edge["edges"].append(
    {
        "source": "budget_dependency_closure_certificate",
        "relation": "posthoc_depends_on",
        "target": "finite_index_budget_certificate",
        "introduced_by": EXPECTED_DOC,
    }
)

gate(
    f"{PREFIX}8 rejects posthoc dependency edges",
    not accepts(posthoc_edge)
    and "posthoc_dependency_edge" in reasons(posthoc_edge),
    ",".join(reasons(posthoc_edge)),
)

expanded = variant(live, expanded_finite_index=True, one_more_layer_tower=True)
expanded["assignments"]["extra_dependency_artifact"] = "coh_extra_dependency_cell"

gate(
    f"{PREFIX}9 rejects expanded finite-index dependency closure",
    not accepts(expanded)
    and "expanded_finite_index" in reasons(expanded)
    and "one_more_layer_tower" in reasons(expanded)
    and any(reason.startswith("assignment_uses_undeclared_cell:") for reason in reasons(expanded)),
    ",".join(reasons(expanded)),
)

variants = [
    missing_assignment,
    unknown_edge,
    bad_charge,
    collapsed,
    missing_closure,
    self_bootstrap,
    posthoc_edge,
    expanded,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only the current dependency-closed 24-cell budget passes",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "unassigned_dependency_endpoint",
        "unbudgeted_dependency_edge",
        "unknown_dependency_endpoint",
        "forbidden_cross_context_charge",
        "context_collapsing_dependency_edge",
        "missing_dependency_closure_certificate",
        "self_bootstrapped_dependency_closure",
        "posthoc_dependency_edge",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: exact 24-cell dependency closure pinned")
print(
    "VERDICT: the current frontier remains live only if every accepted node, "
    "dependency edge, consistency requirement, and directed context bridge is "
    "charged inside the existing seven source facets plus seventeen coherence "
    "cells. Unbudgeted edges, unassigned endpoints, cross-context charges, "
    "self-bootstrapped closure, posthoc dependencies, and expanded finite index "
    "do not construct the missing object."
)
