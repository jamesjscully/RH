r"""Exact 24-cell finite-index budget contract.

Doc 533 pins an internal non-control inhabitance certificate for the
finite-limit source fiber. This witness addresses the remaining finite-index
kill route: all current live artifacts must be charged to the existing seven
source facets plus seventeen coherence cells, with no hidden extra cell,
retuned cell, point/control cell, or one-more-layer tower.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_dd4handoff_graphhandoff_inhabited_finidx24_contract
"""

from __future__ import annotations


failures: list[str] = []

FINIDX_CERT_ID = "FinIdx24Budget_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_current_frontier"
INHABITANCE_CERT_ID = "InhCert_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_nonempty_source_fiber"
DD4_HANDOFF_CONTRACT_ID = "ImgOnlyHandoff_dd4_c_original_res1_Qbar_BECD"
GRAPH_HANDOFF_CONTRACT_ID = "LaterGraphRealization_Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_graph_rosati_count"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
JOINT_FORK_ID = "Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_endpoint_dd4_rosati_control_NCoup"

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

REQUIRED_ARTIFACTS = {
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
    "monic_subrep_inclusion",
    "coupled_source_image",
    "subrep_factorization",
    "finite_limit_cut",
    "joint_constraint_fork",
    "equalizer_arrow_to_subrep",
    "context_separation_contract",
    "dd4_certificate_image",
    "dd4_image_only_handoff_contract",
    "pregraph_rosati_payload",
    "graph_realization_image",
    "graph_later_realization_contract",
    "finite_limit_inhabitance_certificate",
    "exact_delta",
    "rank1_boundary_defect_duality",
    "original_dd4_class",
    "dd4_boundary_certificate",
    "source_control_death",
    "source_mediator_fixed",
    "doc515_coherence_fixed",
    "coupled_self_dual_exact_bcf_sources",
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
    "source_before_points",
    "exact_24_cell_finite_index",
    "doc515_boundary_fiber_coherence",
    "original_dd4_res1_nonboundary",
}

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

REQUIRED_DEPENDENCIES = {
    FINIDX_CERT_ID,
    INHABITANCE_CERT_ID,
    DD4_HANDOFF_CONTRACT_ID,
    GRAPH_HANDOFF_CONTRACT_ID,
    FINITE_LIMIT_CUT_ID,
    JOINT_FORK_ID,
}

REQUIRED = (
    ("budget_certificate_actual", "budget_certificate_missing"),
    ("source_facets_exactly_seven", "source_facets_not_exactly_seven"),
    ("coherence_cells_exactly_seventeen", "coherence_cells_not_exactly_seventeen"),
    ("total_cells_exactly_twenty_four", "total_cells_not_exactly_twenty_four"),
    ("all_required_artifacts_assigned", "required_artifacts_unassigned"),
    ("all_assignments_use_declared_cells", "assignment_uses_undeclared_cell"),
    ("all_live_cells_used", "declared_cell_unused"),
    ("dd4_handoff_charged_existing_cell", "dd4_handoff_needs_new_cell"),
    ("graph_handoff_charged_existing_cell", "graph_handoff_needs_new_cell"),
    ("inhabitance_charged_existing_cell", "inhabitance_needs_new_cell"),
    ("source_constraints_charged_to_facets", "source_constraints_not_facets"),
    ("doc515_charged_existing_cell", "doc515_payload_needs_new_cell"),
    ("no_extra_cell", "extra_cell_opened"),
    ("no_tower", "one_more_layer_tower"),
    ("no_retuned_cell_labels", "retuned_cell_labels"),
    ("no_point_cell", "point_cell_admitted"),
    ("no_control_point_cell", "control_point_cell_admitted"),
    ("no_graph_object_cell", "graph_object_cell_admitted"),
    ("compatible_with_inhabitance", "inhabitance_not_budgeted"),
    ("compatible_with_dd4_handoff", "dd4_handoff_not_budgeted"),
    ("compatible_with_graph_handoff", "graph_handoff_not_budgeted"),
)

BANNED = (
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
    ("unassigned_live_artifact", "unassigned_live_artifact"),
    ("undeclared_cell_assignment", "undeclared_cell_assignment"),
    ("retuned_cell_labels", "retuned_cell_labels"),
    ("posthoc_cell_split", "posthoc_cell_split"),
    ("point_cell_admitted", "point_cell_admitted"),
    ("control_point_cell_admitted", "control_point_cell_admitted"),
    ("graph_object_cell_admitted", "graph_object_cell_admitted"),
    ("local_row_cell", "local_row_cell"),
    ("finite_sample_cell", "finite_sample_cell"),
    ("basis_dependent_cell", "basis_dependent_cell"),
    ("missing_budget_certificate", "missing_budget_certificate"),
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def budget(**kwargs):
    data = {
        "budget_certificate_actual": False,
        "source_facets_exactly_seven": False,
        "coherence_cells_exactly_seventeen": False,
        "total_cells_exactly_twenty_four": False,
        "all_required_artifacts_assigned": False,
        "all_assignments_use_declared_cells": False,
        "all_live_cells_used": False,
        "dd4_handoff_charged_existing_cell": False,
        "graph_handoff_charged_existing_cell": False,
        "inhabitance_charged_existing_cell": False,
        "source_constraints_charged_to_facets": False,
        "doc515_charged_existing_cell": False,
        "no_extra_cell": False,
        "no_tower": False,
        "no_retuned_cell_labels": False,
        "no_point_cell": False,
        "no_control_point_cell": False,
        "no_graph_object_cell": False,
        "compatible_with_inhabitance": False,
        "compatible_with_dd4_handoff": False,
        "compatible_with_graph_handoff": False,
        "certificate": None,
        "source_facets": set(),
        "coherence_cells": set(),
        "assignments": {},
        "dependencies": set(),
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
        "unassigned_live_artifact": False,
        "undeclared_cell_assignment": False,
        "retuned_cell_labels": False,
        "posthoc_cell_split": False,
        "point_cell_admitted": False,
        "control_point_cell_admitted": False,
        "graph_object_cell_admitted": False,
        "local_row_cell": False,
        "finite_sample_cell": False,
        "basis_dependent_cell": False,
        "missing_budget_certificate": False,
    }
    data.update(kwargs)
    return data


def live_budget(**kwargs):
    data = budget(
        budget_certificate_actual=True,
        source_facets_exactly_seven=True,
        coherence_cells_exactly_seventeen=True,
        total_cells_exactly_twenty_four=True,
        all_required_artifacts_assigned=True,
        all_assignments_use_declared_cells=True,
        all_live_cells_used=True,
        dd4_handoff_charged_existing_cell=True,
        graph_handoff_charged_existing_cell=True,
        inhabitance_charged_existing_cell=True,
        source_constraints_charged_to_facets=True,
        doc515_charged_existing_cell=True,
        no_extra_cell=True,
        no_tower=True,
        no_retuned_cell_labels=True,
        no_point_cell=True,
        no_control_point_cell=True,
        no_graph_object_cell=True,
        compatible_with_inhabitance=True,
        compatible_with_dd4_handoff=True,
        compatible_with_graph_handoff=True,
        certificate=FINIDX_CERT_ID,
        source_facets=set(SOURCE_FACETS),
        coherence_cells=set(COHERENCE_CELLS),
        assignments=dict(LIVE_ASSIGNMENTS),
        dependencies=set(REQUIRED_DEPENDENCIES),
    )
    data.update(kwargs)
    return data


def budget_reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    cells = set(data["source_facets"]) | set(data["coherence_cells"])
    assignments = dict(data["assignments"])
    if data["certificate"] != FINIDX_CERT_ID:
        out.append("certificate_not_named_finidx24_budget")
    if len(data["source_facets"]) != 7:
        out.append("source_facet_count_bad")
    if len(data["coherence_cells"]) != 17:
        out.append("coherence_cell_count_bad")
    if len(cells) != 24:
        out.append("total_cell_count_bad")
    missing = REQUIRED_ARTIFACTS - set(assignments)
    if missing:
        out.append("missing_assignments:" + ",".join(sorted(missing)))
    unknown_cells = {cell for cell in assignments.values() if cell not in cells}
    if unknown_cells:
        out.append("unknown_cells:" + ",".join(sorted(unknown_cells)))
    unused_cells = cells - set(assignments.values())
    if unused_cells:
        out.append("unused_cells:" + ",".join(sorted(unused_cells)))
    if not REQUIRED_DEPENDENCIES <= set(data["dependencies"]):
        out.append("finite_index_dependencies_missing")
    source_constraint_cells = {
        assignments.get("endpoint_integrality"),
        assignments.get("degree_maps"),
        assignments.get("dd4_boundary"),
        assignments.get("boundary_pushforward"),
        assignments.get("graph_composition"),
        assignments.get("rosati_count"),
        assignments.get("control_death"),
    }
    if not source_constraint_cells <= set(data["source_facets"]):
        out.append("source_constraints_not_all_on_facets")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_budget(data) -> bool:
    cells = set(data["source_facets"]) | set(data["coherence_cells"])
    assignments = dict(data["assignments"])
    return (
        all(data[key] for key, _ in REQUIRED)
        and not any(data[key] for key, _ in BANNED)
        and data["certificate"] == FINIDX_CERT_ID
        and len(data["source_facets"]) == 7
        and len(data["coherence_cells"]) == 17
        and len(cells) == 24
        and REQUIRED_ARTIFACTS <= set(assignments)
        and set(assignments.values()) <= cells
        and cells <= set(assignments.values())
        and REQUIRED_DEPENDENCIES <= set(data["dependencies"])
        and {
            assignments.get("endpoint_integrality"),
            assignments.get("degree_maps"),
            assignments.get("dd4_boundary"),
            assignments.get("boundary_pushforward"),
            assignments.get("graph_composition"),
            assignments.get("rosati_count"),
            assignments.get("control_death"),
        }
        <= set(data["source_facets"])
    )


live = live_budget()

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1 exact 24-cell budget is coherent",
    accepts_budget(live)
    and len(SOURCE_FACETS) == 7
    and len(COHERENCE_CELLS) == 17
    and len(CELLS) == 24,
    "facets=%d coherence=%d artifacts=%d" % (len(SOURCE_FACETS), len(COHERENCE_CELLS), len(REQUIRED_ARTIFACTS)),
)

expanded = live_budget(
    coherence_cells=COHERENCE_CELLS | {"coh_extra_handoff_cell"},
    coherence_cells_exactly_seventeen=False,
    total_cells_exactly_twenty_four=False,
    no_extra_cell=False,
    expanded_finite_index=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2 rejects opening a 25th finite-index cell",
    not accepts_budget(expanded)
    and {
        "coherence_cells_not_exactly_seventeen",
        "total_cells_not_exactly_twenty_four",
        "extra_cell_opened",
        "coherence_cell_count_bad",
        "total_cell_count_bad",
        "expanded_finite_index",
    }
    <= set(budget_reasons(expanded)),
    ",".join(budget_reasons(expanded)),
)

tower = live_budget(
    no_tower=False,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3 rejects one-more-layer towers",
    not accepts_budget(tower)
    and {"one_more_layer_tower"} <= set(budget_reasons(tower)),
    ",".join(budget_reasons(tower)),
)

missing_assignment_map = dict(LIVE_ASSIGNMENTS)
del missing_assignment_map["finite_limit_inhabitance_certificate"]
missing_assignment = live_budget(
    assignments=missing_assignment_map,
    all_required_artifacts_assigned=False,
    inhabitance_charged_existing_cell=False,
    compatible_with_inhabitance=False,
    unassigned_live_artifact=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4 rejects unassigned live artifacts",
    not accepts_budget(missing_assignment)
    and {
        "required_artifacts_unassigned",
        "inhabitance_needs_new_cell",
        "inhabitance_not_budgeted",
        "unassigned_live_artifact",
    }
    <= set(budget_reasons(missing_assignment))
    and "missing_assignments:finite_limit_inhabitance_certificate" in budget_reasons(missing_assignment),
    ",".join(budget_reasons(missing_assignment)),
)

bad_cell_map = dict(LIVE_ASSIGNMENTS)
bad_cell_map["graph_later_realization_contract"] = "coh_undeclared_graph_cell"
bad_cell = live_budget(
    assignments=bad_cell_map,
    all_assignments_use_declared_cells=False,
    graph_handoff_charged_existing_cell=False,
    compatible_with_graph_handoff=False,
    undeclared_cell_assignment=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5 rejects undeclared cell assignments",
    not accepts_budget(bad_cell)
    and {
        "assignment_uses_undeclared_cell",
        "graph_handoff_needs_new_cell",
        "graph_handoff_not_budgeted",
        "undeclared_cell_assignment",
    }
    <= set(budget_reasons(bad_cell))
    and "unknown_cells:coh_undeclared_graph_cell" in budget_reasons(bad_cell),
    ",".join(budget_reasons(bad_cell)),
)

retuned = live_budget(
    no_retuned_cell_labels=False,
    retuned_cell_labels=True,
    posthoc_cell_split=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6 rejects retuned labels and posthoc cell splits",
    not accepts_budget(retuned)
    and {"retuned_cell_labels", "posthoc_cell_split"} <= set(budget_reasons(retuned)),
    ",".join(budget_reasons(retuned)),
)

point_cell = live_budget(
    no_point_cell=False,
    no_control_point_cell=False,
    no_graph_object_cell=False,
    point_cell_admitted=True,
    control_point_cell_admitted=True,
    graph_object_cell_admitted=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7 rejects point/control/graph-object cells",
    not accepts_budget(point_cell)
    and {
        "point_cell_admitted",
        "control_point_cell_admitted",
        "graph_object_cell_admitted",
    }
    <= set(budget_reasons(point_cell)),
    ",".join(budget_reasons(point_cell)),
)

source_bad_map = dict(LIVE_ASSIGNMENTS)
source_bad_map["control_death"] = "coh_inhabitance_certificate"
source_bad = live_budget(
    assignments=source_bad_map,
    source_constraints_charged_to_facets=False,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8 requires all seven source constraints to charge source facets",
    not accepts_budget(source_bad)
    and {
        "source_constraints_not_facets",
        "source_constraints_not_all_on_facets",
    }
    <= set(budget_reasons(source_bad)),
    ",".join(budget_reasons(source_bad)),
)

local_sample = live_budget(
    local_row_cell=True,
    finite_sample_cell=True,
    basis_dependent_cell=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9 rejects local-row finite-sample basis cells",
    not accepts_budget(local_sample)
    and {"local_row_cell", "finite_sample_cell", "basis_dependent_cell"} <= set(budget_reasons(local_sample)),
    ",".join(budget_reasons(local_sample)),
)

missing_cert = live_budget(
    certificate=None,
    budget_certificate_actual=False,
    missing_budget_certificate=True,
)

variants = [
    expanded,
    tower,
    missing_assignment,
    bad_cell,
    retuned,
    point_cell,
    source_bad,
    local_sample,
    missing_cert,
    live_budget(dependencies={FINIDX_CERT_ID}),
]
variant_reasons = set().union(*(set(budget_reasons(data)) for data in variants))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 only the exact 24-cell budget passes",
    accepts_budget(live_budget())
    and not any(accepts_budget(data) for data in variants)
    and {
        "expanded_finite_index",
        "one_more_layer_tower",
        "unassigned_live_artifact",
        "undeclared_cell_assignment",
        "retuned_cell_labels",
        "point_cell_admitted",
        "source_constraints_not_all_on_facets",
        "local_row_cell",
        "missing_budget_certificate",
        "finite_index_dependencies_missing",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: exact 24-cell finite-index budget certificate pinned"
)
print(
    "VERDICT: the current frontier remains live only if every load-bearing "
    "artifact is charged to seven source facets plus seventeen coherence cells. "
    "Extra cells, towers, unassigned artifacts, undeclared or retuned cells, "
    "point/control/graph-object cells, local finite samples, and basis cells do "
    "not construct the missing object."
)
