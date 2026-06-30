r"""Finite-limit source-fiber inhabitance contract.

Docs 531-532 type the DD.4 and graph/Rosati handoff bridges. This witness
addresses the next live kill route: the simultaneous finite-limit source fork
must have a nonempty source-fiber certificate that is internal to the
subrepresenter, not a point, not a control/DH/Epstein artifact, and not a
finite sample or local row table.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_dd4handoff_graphhandoff_inhabited_contract
"""

from __future__ import annotations


failures: list[str] = []

INHABITANCE_CERT_ID = "InhCert_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_nonempty_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
JOINT_FORK_ID = "Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_endpoint_dd4_rosati_control_NCoup"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_constraints_to_SubRep_source_fiber"
SOURCE_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
DD4_HANDOFF_CONTRACT_ID = "ImgOnlyHandoff_dd4_c_original_res1_Qbar_BECD"
GRAPH_HANDOFF_CONTRACT_ID = "LaterGraphRealization_Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_graph_rosati_count"
CONTEXT_SEPARATION_ID = "CtxSep_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"

CONTEXTS = {
    "source_fiber",
    "finite_limit",
    "source_constraint",
    "source_prepoint",
    "certificate_image",
    "graph_realization",
}

SOURCE_CONSTRAINTS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

REQUIRED_DEPENDENCIES = {
    INHABITANCE_CERT_ID,
    FINITE_LIMIT_CUT_ID,
    JOINT_FORK_ID,
    EQUALIZER_ARROW_ID,
    SOURCE_SUBREP_ID,
    DD4_HANDOFF_CONTRACT_ID,
    GRAPH_HANDOFF_CONTRACT_ID,
    CONTEXT_SEPARATION_ID,
}

REQUIRED = (
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("source_subrep_actual", "source_subrep_missing"),
    ("equalizer_arrow_actual", "equalizer_arrow_missing"),
    ("joint_fork_actual", "joint_fork_missing"),
    ("inhabitance_certificate_actual", "inhabitance_certificate_missing"),
    ("certificate_context_source_fiber", "certificate_not_source_fiber"),
    ("certificate_lands_in_subrep", "certificate_not_in_subrep"),
    ("certificate_factors_through_equalizer", "certificate_not_equalizer_factored"),
    ("certificate_tied_to_joint_fork", "certificate_not_tied_to_joint_fork"),
    ("certificate_carries_all_constraints", "certificate_missing_constraints"),
    ("certificate_nonempty", "source_fiber_empty"),
    ("certificate_noncontrol", "source_fiber_control_only"),
    ("certificate_not_point_semantics", "certificate_is_point_semantics"),
    ("certificate_not_control_point", "certificate_is_control_point"),
    ("certificate_not_dh_point", "certificate_is_dh_point"),
    ("certificate_not_epstein_point", "certificate_is_epstein_point"),
    ("source_before_points", "source_not_before_points"),
    ("dd4_handoff_compatible", "dd4_handoff_not_compatible"),
    ("graph_handoff_compatible", "graph_handoff_not_compatible"),
    ("context_separation_compatible", "context_separation_not_compatible"),
    ("exact_24_finite_index", "finite_index_not_exact_24"),
    ("not_local_row_table", "local_row_table"),
    ("not_finite_sample", "finite_sample_cut"),
    ("not_basis_dependent", "basis_dependent_cut"),
    ("not_retuned", "retuned_inhabitance_certificate"),
    ("not_posthoc", "posthoc_inhabitance_certificate"),
    ("not_external_choice", "external_choice_inhabitant"),
)

BANNED = (
    ("empty_source_fiber", "empty_source_fiber"),
    ("control_only_source_fiber", "control_only_source_fiber"),
    ("dh_point_inhabitant", "dh_point_inhabitant"),
    ("epstein_point_inhabitant", "epstein_point_inhabitant"),
    ("point_semantics_inhabitant", "point_semantics_inhabitant"),
    ("graph_object_inhabitant", "graph_object_inhabitant"),
    ("local_row_table", "local_row_table"),
    ("finite_sample_cut", "finite_sample_cut"),
    ("basis_dependent_cut", "basis_dependent_cut"),
    ("retuned_inhabitance_certificate", "retuned_inhabitance_certificate"),
    ("posthoc_inhabitance_certificate", "posthoc_inhabitance_certificate"),
    ("external_choice_inhabitant", "external_choice_inhabitant"),
    ("missing_inhabitance_certificate", "missing_inhabitance_certificate"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def source(**kwargs):
    data = {
        "finite_limit_cut_actual": False,
        "source_subrep_actual": False,
        "equalizer_arrow_actual": False,
        "joint_fork_actual": False,
        "inhabitance_certificate_actual": False,
        "certificate_context_source_fiber": False,
        "certificate_lands_in_subrep": False,
        "certificate_factors_through_equalizer": False,
        "certificate_tied_to_joint_fork": False,
        "certificate_carries_all_constraints": False,
        "certificate_nonempty": False,
        "certificate_noncontrol": False,
        "certificate_not_point_semantics": False,
        "certificate_not_control_point": False,
        "certificate_not_dh_point": False,
        "certificate_not_epstein_point": False,
        "source_before_points": False,
        "dd4_handoff_compatible": False,
        "graph_handoff_compatible": False,
        "context_separation_compatible": False,
        "exact_24_finite_index": False,
        "not_local_row_table": False,
        "not_finite_sample": False,
        "not_basis_dependent": False,
        "not_retuned": False,
        "not_posthoc": False,
        "not_external_choice": False,
        "contexts": set(),
        "certificate": None,
        "certificate_context": None,
        "finite_limit_cut": None,
        "source_subrep": None,
        "equalizer_arrow": None,
        "joint_fork": None,
        "constraint_payload": set(),
        "dependencies": set(),
        "internal_rank_lower_bound": 0,
        "finite_index_cells": 0,
        "empty_source_fiber": False,
        "control_only_source_fiber": False,
        "dh_point_inhabitant": False,
        "epstein_point_inhabitant": False,
        "point_semantics_inhabitant": False,
        "graph_object_inhabitant": False,
        "local_row_table": False,
        "finite_sample_cut": False,
        "basis_dependent_cut": False,
        "retuned_inhabitance_certificate": False,
        "posthoc_inhabitance_certificate": False,
        "external_choice_inhabitant": False,
        "missing_inhabitance_certificate": False,
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
    }
    data.update(kwargs)
    return data


def live_source(**kwargs):
    data = source(
        finite_limit_cut_actual=True,
        source_subrep_actual=True,
        equalizer_arrow_actual=True,
        joint_fork_actual=True,
        inhabitance_certificate_actual=True,
        certificate_context_source_fiber=True,
        certificate_lands_in_subrep=True,
        certificate_factors_through_equalizer=True,
        certificate_tied_to_joint_fork=True,
        certificate_carries_all_constraints=True,
        certificate_nonempty=True,
        certificate_noncontrol=True,
        certificate_not_point_semantics=True,
        certificate_not_control_point=True,
        certificate_not_dh_point=True,
        certificate_not_epstein_point=True,
        source_before_points=True,
        dd4_handoff_compatible=True,
        graph_handoff_compatible=True,
        context_separation_compatible=True,
        exact_24_finite_index=True,
        not_local_row_table=True,
        not_finite_sample=True,
        not_basis_dependent=True,
        not_retuned=True,
        not_posthoc=True,
        not_external_choice=True,
        contexts=set(CONTEXTS),
        certificate=INHABITANCE_CERT_ID,
        certificate_context="source_fiber",
        finite_limit_cut=FINITE_LIMIT_CUT_ID,
        source_subrep=SOURCE_SUBREP_ID,
        equalizer_arrow=EQUALIZER_ARROW_ID,
        joint_fork=JOINT_FORK_ID,
        constraint_payload=set(SOURCE_CONSTRAINTS),
        dependencies=set(REQUIRED_DEPENDENCIES),
        internal_rank_lower_bound=1,
        finite_index_cells=24,
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not CONTEXTS <= set(data["contexts"]):
        out.append("declared_contexts_missing")
    if data["certificate"] != INHABITANCE_CERT_ID:
        out.append("certificate_not_named_inhabitance_cert")
    if data["certificate_context"] != "source_fiber":
        out.append("certificate_context_not_source_fiber")
    if data["finite_limit_cut"] != FINITE_LIMIT_CUT_ID:
        out.append("finite_limit_cut_not_named")
    if data["source_subrep"] != SOURCE_SUBREP_ID:
        out.append("source_subrep_not_named")
    if data["equalizer_arrow"] != EQUALIZER_ARROW_ID:
        out.append("equalizer_arrow_not_named")
    if data["joint_fork"] != JOINT_FORK_ID:
        out.append("joint_fork_not_named")
    if not SOURCE_CONSTRAINTS <= set(data["constraint_payload"]):
        out.append("source_constraints_missing")
    if not REQUIRED_DEPENDENCIES <= set(data["dependencies"]):
        out.append("inhabitance_dependencies_missing")
    if data["internal_rank_lower_bound"] < 1:
        out.append("internal_rank_lower_bound_zero")
    if data["finite_index_cells"] != 24:
        out.append("finite_index_not_exact_24")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_inhabitance(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and not any(data[key] for key, _ in BANNED)
        and CONTEXTS <= set(data["contexts"])
        and data["certificate"] == INHABITANCE_CERT_ID
        and data["certificate_context"] == "source_fiber"
        and data["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and data["source_subrep"] == SOURCE_SUBREP_ID
        and data["equalizer_arrow"] == EQUALIZER_ARROW_ID
        and data["joint_fork"] == JOINT_FORK_ID
        and SOURCE_CONSTRAINTS <= set(data["constraint_payload"])
        and REQUIRED_DEPENDENCIES <= set(data["dependencies"])
        and data["internal_rank_lower_bound"] >= 1
        and data["finite_index_cells"] == 24
    )


live = live_source()

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1 finite-limit source-fiber inhabitance is coherent",
    accepts_inhabitance(live)
    and len(SOURCE_CONSTRAINTS) == 7
    and live["internal_rank_lower_bound"] == 1,
    "constraints=%d rank_lb=%d" % (len(SOURCE_CONSTRAINTS), live["internal_rank_lower_bound"]),
)

empty = live_source(
    certificate_nonempty=False,
    internal_rank_lower_bound=0,
    empty_source_fiber=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2 rejects empty source fiber",
    not accepts_inhabitance(empty)
    and {
        "source_fiber_empty",
        "internal_rank_lower_bound_zero",
        "empty_source_fiber",
    }
    <= set(reasons(empty)),
    ",".join(reasons(empty)),
)

control_only = live_source(
    certificate_noncontrol=False,
    certificate_not_control_point=False,
    certificate_not_dh_point=False,
    certificate_not_epstein_point=False,
    control_only_source_fiber=True,
    dh_point_inhabitant=True,
    epstein_point_inhabitant=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3 rejects control-only and DH/Epstein inhabitants",
    not accepts_inhabitance(control_only)
    and {
        "source_fiber_control_only",
        "certificate_is_control_point",
        "certificate_is_dh_point",
        "certificate_is_epstein_point",
        "control_only_source_fiber",
        "dh_point_inhabitant",
        "epstein_point_inhabitant",
    }
    <= set(reasons(control_only)),
    ",".join(reasons(control_only)),
)

point_semantics = live_source(
    certificate_not_point_semantics=False,
    source_before_points=False,
    point_semantics_inhabitant=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4 rejects point-semantics inhabitance",
    not accepts_inhabitance(point_semantics)
    and {
        "certificate_is_point_semantics",
        "source_not_before_points",
        "point_semantics_inhabitant",
    }
    <= set(reasons(point_semantics)),
    ",".join(reasons(point_semantics)),
)

missing_factorization = live_source(
    equalizer_arrow_actual=False,
    certificate_factors_through_equalizer=False,
    certificate_tied_to_joint_fork=False,
    dependencies={INHABITANCE_CERT_ID, FINITE_LIMIT_CUT_ID, SOURCE_SUBREP_ID},
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5 requires equalizer and joint-fork factorization",
    not accepts_inhabitance(missing_factorization)
    and {
        "equalizer_arrow_missing",
        "certificate_not_equalizer_factored",
        "certificate_not_tied_to_joint_fork",
        "inhabitance_dependencies_missing",
    }
    <= set(reasons(missing_factorization)),
    ",".join(reasons(missing_factorization)),
)

local_sample = live_source(
    not_local_row_table=False,
    not_finite_sample=False,
    not_basis_dependent=False,
    local_row_table=True,
    finite_sample_cut=True,
    basis_dependent_cut=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6 rejects local rows, finite samples, and basis cuts",
    not accepts_inhabitance(local_sample)
    and {
        "local_row_table",
        "finite_sample_cut",
        "basis_dependent_cut",
    }
    <= set(reasons(local_sample)),
    ",".join(reasons(local_sample)),
)

retuned = live_source(
    certificate="InhCert_retuned_after_base_change",
    not_retuned=False,
    not_posthoc=False,
    not_external_choice=False,
    retuned_inhabitance_certificate=True,
    posthoc_inhabitance_certificate=True,
    external_choice_inhabitant=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7 rejects retuned, posthoc, or external-choice inhabitance",
    not accepts_inhabitance(retuned)
    and {
        "certificate_not_named_inhabitance_cert",
        "retuned_inhabitance_certificate",
        "posthoc_inhabitance_certificate",
        "external_choice_inhabitant",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

graph_object = live_source(
    graph_handoff_compatible=False,
    certificate_context="graph_realization",
    certificate_context_source_fiber=False,
    graph_object_inhabitant=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8 rejects graph-object inhabitants before source fiber",
    not accepts_inhabitance(graph_object)
    and {
        "certificate_not_source_fiber",
        "certificate_context_not_source_fiber",
        "graph_handoff_not_compatible",
        "graph_object_inhabitant",
    }
    <= set(reasons(graph_object)),
    ",".join(reasons(graph_object)),
)

index_tower = live_source(
    exact_24_finite_index=False,
    finite_index_cells=25,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9 rejects finite-index expansion and towers",
    not accepts_inhabitance(index_tower)
    and {
        "finite_index_not_exact_24",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(index_tower)),
    ",".join(reasons(index_tower)),
)

missing_cert = live_source(
    certificate=None,
    inhabitance_certificate_actual=False,
    certificate_lands_in_subrep=False,
    missing_inhabitance_certificate=True,
)

variants = [
    empty,
    control_only,
    point_semantics,
    missing_factorization,
    local_sample,
    retuned,
    graph_object,
    index_tower,
    missing_cert,
    live_source(constraint_payload={"endpoint_integrality"}),
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 only the internal non-control inhabitance certificate passes",
    accepts_inhabitance(live_source())
    and not any(accepts_inhabitance(data) for data in variants)
    and {
        "empty_source_fiber",
        "control_only_source_fiber",
        "point_semantics_inhabitant",
        "equalizer_arrow_missing",
        "local_row_table",
        "retuned_inhabitance_certificate",
        "graph_object_inhabitant",
        "expanded_finite_index",
        "missing_inhabitance_certificate",
        "source_constraints_missing",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: finite-limit source-fiber inhabitance certificate pinned"
)
print(
    "VERDICT: the simultaneous finite-limit fork remains live only with an "
    "internal source-fiber inhabitance certificate that factors through the "
    "equalizer and joint fork, carries all seven constraints, and is not a "
    "point, control/DH/Epstein artifact, finite sample, local row, graph "
    "object, retuned certificate, or finite-index tower."
)
