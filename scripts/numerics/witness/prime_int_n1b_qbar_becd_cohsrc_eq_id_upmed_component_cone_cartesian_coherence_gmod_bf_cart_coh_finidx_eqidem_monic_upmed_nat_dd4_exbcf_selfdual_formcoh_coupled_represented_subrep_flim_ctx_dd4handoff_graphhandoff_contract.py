r"""Graph/Rosati later-realization handoff contract.

Doc 531 pins the DD.4 certificate handoff as a directed image-only object.
This witness pins the other doc-530 bridge: graph/Rosati/count data must be
source-side constraints before graph objects and point semantics exist, with
only a later realization image in the graph_realization context.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_dd4handoff_graphhandoff_contract
"""

from __future__ import annotations


failures: list[str] = []

PREGRAPH_PAYLOAD_ID = "PreGraphRosatiPayload_Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_constraints"
GRAPH_IMAGE_ID = "GraphImg_Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_under_graph_realization_bridge"
GRAPH_HANDOFF_CONTRACT_ID = "LaterGraphRealization_Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_graph_rosati_count"
GRAPH_BRIDGE_ID = "graph_realization_bridge"
JOINT_FORK_ID = "Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_endpoint_dd4_rosati_control_NCoup"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
CONTEXT_SEPARATION_ID = "CtxSep_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
DD4_HANDOFF_CONTRACT_ID = "ImgOnlyHandoff_dd4_c_original_res1_Qbar_BECD"

CONTEXTS = {
    "source_constraint",
    "graph_realization",
    "source_prepoint",
    "finite_limit",
    "certificate_image",
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

GRAPH_PAYLOAD_CONSTRAINTS = {
    "graph_composition",
    "rosati_count",
}

REQUIRED_DEPENDENCIES = {
    PREGRAPH_PAYLOAD_ID,
    GRAPH_IMAGE_ID,
    GRAPH_HANDOFF_CONTRACT_ID,
    JOINT_FORK_ID,
    FINITE_LIMIT_CUT_ID,
    CONTEXT_SEPARATION_ID,
    DD4_HANDOFF_CONTRACT_ID,
}

REQUIRED = (
    ("source_fork_actual", "source_fork_missing"),
    ("source_context_source_constraint", "source_not_source_constraint"),
    ("pregraph_payload_actual", "pregraph_payload_missing"),
    ("payload_context_source_constraint", "payload_not_source_constraint"),
    ("payload_has_graph_composition", "payload_missing_graph_composition"),
    ("payload_has_rosati_count", "payload_missing_rosati_count"),
    ("payload_has_all_source_constraints", "payload_missing_source_constraints"),
    ("source_constraints_pregraph", "source_constraints_not_pregraph"),
    ("source_before_points", "source_not_before_points"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("graph_image_actual", "graph_image_missing"),
    ("image_context_graph_realization", "image_not_graph_realization"),
    ("image_has_source_payload", "image_not_tied_to_payload"),
    ("image_has_bridge_id", "image_not_tied_to_bridge"),
    ("bridge_actual", "graph_bridge_missing"),
    ("bridge_later_only", "graph_bridge_not_later_only"),
    ("bridge_directed", "graph_bridge_not_directed"),
    ("bridge_not_reversible_before_points", "graph_bridge_reversible_before_points"),
    ("bridge_not_prerequisite", "graph_object_prerequisite"),
    ("bridge_not_pullback_source", "graph_pullback_before_source_fork"),
    ("bridge_not_retuned", "graph_bridge_retuned"),
    ("bridge_not_posthoc", "graph_bridge_posthoc"),
    ("bridge_keeps_finite_index", "graph_bridge_expands_finite_index"),
    ("bridge_coupled_to_finite_limit", "graph_bridge_not_coupled_to_finite_limit"),
    ("bridge_compatible_context_separation", "graph_bridge_ignores_context_separation"),
    ("bridge_compatible_dd4_handoff", "graph_bridge_ignores_dd4_handoff"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("graph_context_collapse", "graph_context_collapse"),
    ("source_constraint_is_graph_realization", "source_constraint_is_graph_realization"),
    ("graph_object_required_before_source_fork", "graph_object_required_before_source_fork"),
    ("graph_bridge_reversible_before_points", "graph_bridge_reversible_before_points"),
    ("graph_pullback_before_source_fork", "graph_pullback_before_source_fork"),
    ("point_semantics_graph_admission", "point_semantics_graph_admission"),
    ("control_points_admitted", "control_points_admitted"),
    ("retuned_graph_realization_image", "retuned_graph_realization_image"),
    ("base_changed_graph_realization_image", "base_changed_graph_realization_image"),
    ("posthoc_graph_realization", "posthoc_graph_realization"),
    ("missing_graph_realization_image", "missing_graph_realization_image"),
    ("missing_pregraph_payload", "missing_pregraph_payload"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("local_row_table", "local_row_table"),
    ("finite_index_expansion", "finite_index_expansion"),
    ("one_more_layer_tower", "one_more_layer_tower"),
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def handoff(**kwargs):
    data = {
        "source_fork_actual": False,
        "source_context_source_constraint": False,
        "pregraph_payload_actual": False,
        "payload_context_source_constraint": False,
        "payload_has_graph_composition": False,
        "payload_has_rosati_count": False,
        "payload_has_all_source_constraints": False,
        "source_constraints_pregraph": False,
        "source_before_points": False,
        "source_before_graph_objects": False,
        "graph_image_actual": False,
        "image_context_graph_realization": False,
        "image_has_source_payload": False,
        "image_has_bridge_id": False,
        "bridge_actual": False,
        "bridge_later_only": False,
        "bridge_directed": False,
        "bridge_not_reversible_before_points": False,
        "bridge_not_prerequisite": False,
        "bridge_not_pullback_source": False,
        "bridge_not_retuned": False,
        "bridge_not_posthoc": False,
        "bridge_keeps_finite_index": False,
        "bridge_coupled_to_finite_limit": False,
        "bridge_compatible_context_separation": False,
        "bridge_compatible_dd4_handoff": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "contexts": set(),
        "source_fork": None,
        "source_context": None,
        "pregraph_payload": None,
        "payload_context": None,
        "payload_constraints": set(),
        "graph_image": None,
        "image_context": None,
        "bridge_id": None,
        "dependencies": set(),
        "finite_index_cells": 0,
        "graph_context_collapse": False,
        "source_constraint_is_graph_realization": False,
        "graph_object_required_before_source_fork": False,
        "graph_bridge_reversible_before_points": False,
        "graph_pullback_before_source_fork": False,
        "point_semantics_graph_admission": False,
        "control_points_admitted": False,
        "retuned_graph_realization_image": False,
        "base_changed_graph_realization_image": False,
        "posthoc_graph_realization": False,
        "missing_graph_realization_image": False,
        "missing_pregraph_payload": False,
        "graph_object_classifier": False,
        "local_row_table": False,
        "finite_index_expansion": False,
        "one_more_layer_tower": False,
    }
    data.update(kwargs)
    return data


def live_handoff(**kwargs):
    data = handoff(
        source_fork_actual=True,
        source_context_source_constraint=True,
        pregraph_payload_actual=True,
        payload_context_source_constraint=True,
        payload_has_graph_composition=True,
        payload_has_rosati_count=True,
        payload_has_all_source_constraints=True,
        source_constraints_pregraph=True,
        source_before_points=True,
        source_before_graph_objects=True,
        graph_image_actual=True,
        image_context_graph_realization=True,
        image_has_source_payload=True,
        image_has_bridge_id=True,
        bridge_actual=True,
        bridge_later_only=True,
        bridge_directed=True,
        bridge_not_reversible_before_points=True,
        bridge_not_prerequisite=True,
        bridge_not_pullback_source=True,
        bridge_not_retuned=True,
        bridge_not_posthoc=True,
        bridge_keeps_finite_index=True,
        bridge_coupled_to_finite_limit=True,
        bridge_compatible_context_separation=True,
        bridge_compatible_dd4_handoff=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        contexts=set(CONTEXTS),
        source_fork=JOINT_FORK_ID,
        source_context="source_constraint",
        pregraph_payload=PREGRAPH_PAYLOAD_ID,
        payload_context="source_constraint",
        payload_constraints=set(SOURCE_CONSTRAINTS),
        graph_image=GRAPH_IMAGE_ID,
        image_context="graph_realization",
        bridge_id=GRAPH_BRIDGE_ID,
        dependencies=set(REQUIRED_DEPENDENCIES),
        finite_index_cells=24,
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not CONTEXTS <= set(data["contexts"]):
        out.append("declared_contexts_missing")
    if data["source_fork"] != JOINT_FORK_ID:
        out.append("source_fork_not_joint_constraint_fork")
    if data["source_context"] != "source_constraint":
        out.append("source_context_not_source_constraint")
    if data["pregraph_payload"] != PREGRAPH_PAYLOAD_ID:
        out.append("pregraph_payload_not_named")
    if data["payload_context"] != "source_constraint":
        out.append("payload_context_not_source_constraint")
    if not SOURCE_CONSTRAINTS <= set(data["payload_constraints"]):
        out.append("source_constraints_missing_from_payload")
    if not GRAPH_PAYLOAD_CONSTRAINTS <= set(data["payload_constraints"]):
        out.append("graph_rosati_missing_from_payload")
    if data["graph_image"] != GRAPH_IMAGE_ID:
        out.append("graph_image_not_named")
    if data["image_context"] != "graph_realization":
        out.append("image_context_not_graph_realization")
    if data["bridge_id"] != GRAPH_BRIDGE_ID:
        out.append("bridge_id_not_graph_realization_bridge")
    if data["payload_context"] == data["image_context"]:
        out.append("payload_and_graph_contexts_collapsed")
    if not REQUIRED_DEPENDENCIES <= set(data["dependencies"]):
        out.append("graph_handoff_dependencies_missing")
    if data["finite_index_cells"] != 24:
        out.append("finite_index_not_exact_24")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_graph_handoff(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and not any(data[key] for key, _ in BANNED)
        and CONTEXTS <= set(data["contexts"])
        and data["source_fork"] == JOINT_FORK_ID
        and data["source_context"] == "source_constraint"
        and data["pregraph_payload"] == PREGRAPH_PAYLOAD_ID
        and data["payload_context"] == "source_constraint"
        and SOURCE_CONSTRAINTS <= set(data["payload_constraints"])
        and GRAPH_PAYLOAD_CONSTRAINTS <= set(data["payload_constraints"])
        and data["graph_image"] == GRAPH_IMAGE_ID
        and data["image_context"] == "graph_realization"
        and data["bridge_id"] == GRAPH_BRIDGE_ID
        and data["payload_context"] != data["image_context"]
        and REQUIRED_DEPENDENCIES <= set(data["dependencies"])
        and data["finite_index_cells"] == 24
    )


live = live_handoff()

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1 graph later-realization handoff is coherent",
    accepts_graph_handoff(live)
    and len(SOURCE_CONSTRAINTS) == 7
    and GRAPH_PAYLOAD_CONSTRAINTS <= SOURCE_CONSTRAINTS
    and GRAPH_HANDOFF_CONTRACT_ID,
    "constraints=%d graph_payload=%s" % (len(SOURCE_CONSTRAINTS), sorted(GRAPH_PAYLOAD_CONSTRAINTS)),
)

context_collapse = live_handoff(
    image_context="source_constraint",
    image_context_graph_realization=False,
    bridge_later_only=False,
    graph_context_collapse=True,
    source_constraint_is_graph_realization=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2 rejects source-constraint/graph-realization context collapse",
    not accepts_graph_handoff(context_collapse)
    and {
        "image_not_graph_realization",
        "graph_bridge_not_later_only",
        "image_context_not_graph_realization",
        "payload_and_graph_contexts_collapsed",
        "graph_context_collapse",
        "source_constraint_is_graph_realization",
    }
    <= set(reasons(context_collapse)),
    ",".join(reasons(context_collapse)),
)

graph_first = live_handoff(
    source_before_graph_objects=False,
    bridge_not_prerequisite=False,
    graph_object_required_before_source_fork=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3 rejects graph objects as prerequisites for the source fork",
    not accepts_graph_handoff(graph_first)
    and {
        "source_not_before_graph_objects",
        "graph_object_prerequisite",
        "graph_object_required_before_source_fork",
    }
    <= set(reasons(graph_first)),
    ",".join(reasons(graph_first)),
)

reversible = live_handoff(
    bridge_directed=False,
    bridge_not_reversible_before_points=False,
    bridge_not_pullback_source=False,
    graph_bridge_reversible_before_points=True,
    graph_pullback_before_source_fork=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4 rejects reverse graph pullback before points",
    not accepts_graph_handoff(reversible)
    and {
        "graph_bridge_not_directed",
        "graph_bridge_reversible_before_points",
        "graph_pullback_before_source_fork",
    }
    <= set(reasons(reversible)),
    ",".join(reasons(reversible)),
)

points = live_handoff(
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    point_semantics_graph_admission=True,
    control_points_admitted=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5 rejects point semantics and control/DH/Epstein points",
    not accepts_graph_handoff(points)
    and {
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "point_semantics_graph_admission",
        "control_points_admitted",
    }
    <= set(reasons(points)),
    ",".join(reasons(points)),
)

retuned = live_handoff(
    graph_image="GraphImg_retuned_after_base_change",
    image_has_source_payload=False,
    bridge_not_retuned=False,
    bridge_not_posthoc=False,
    retuned_graph_realization_image=True,
    base_changed_graph_realization_image=True,
    posthoc_graph_realization=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6 rejects retuned, base-changed, or posthoc graph images",
    not accepts_graph_handoff(retuned)
    and {
        "image_not_tied_to_payload",
        "graph_bridge_retuned",
        "graph_bridge_posthoc",
        "graph_image_not_named",
        "retuned_graph_realization_image",
        "base_changed_graph_realization_image",
        "posthoc_graph_realization",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing = live_handoff(
    pregraph_payload=None,
    graph_image=None,
    pregraph_payload_actual=False,
    graph_image_actual=False,
    image_has_bridge_id=False,
    missing_pregraph_payload=True,
    missing_graph_realization_image=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7 rejects missing source payload or graph image",
    not accepts_graph_handoff(missing)
    and {
        "pregraph_payload_missing",
        "graph_image_missing",
        "image_not_tied_to_bridge",
        "pregraph_payload_not_named",
        "graph_image_not_named",
        "missing_pregraph_payload",
        "missing_graph_realization_image",
    }
    <= set(reasons(missing)),
    ",".join(reasons(missing)),
)

classifier = live_handoff(
    payload_has_all_source_constraints=False,
    payload_constraints={"graph_composition", "rosati_count"},
    graph_object_classifier=True,
    local_row_table=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8 rejects graph classifiers and local row tables",
    not accepts_graph_handoff(classifier)
    and {
        "payload_missing_source_constraints",
        "source_constraints_missing_from_payload",
        "graph_object_classifier",
        "local_row_table",
    }
    <= set(reasons(classifier)),
    ",".join(reasons(classifier)),
)

index_tower = live_handoff(
    finite_index_cells=25,
    bridge_keeps_finite_index=False,
    finite_index_expansion=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9 rejects finite-index expansion and towers",
    not accepts_graph_handoff(index_tower)
    and {
        "graph_bridge_expands_finite_index",
        "finite_index_not_exact_24",
        "finite_index_expansion",
        "one_more_layer_tower",
    }
    <= set(reasons(index_tower)),
    ",".join(reasons(index_tower)),
)

variants = [
    context_collapse,
    graph_first,
    reversible,
    points,
    retuned,
    missing,
    classifier,
    index_tower,
    live_handoff(bridge_actual=False),
    live_handoff(dependencies={PREGRAPH_PAYLOAD_ID, GRAPH_IMAGE_ID}),
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 only the directed later-realization bridge passes",
    accepts_graph_handoff(live_handoff())
    and not any(accepts_graph_handoff(data) for data in variants)
    and {
        "graph_bridge_missing",
        "graph_context_collapse",
        "graph_object_required_before_source_fork",
        "graph_bridge_reversible_before_points",
        "point_semantics_graph_admission",
        "retuned_graph_realization_image",
        "missing_graph_realization_image",
        "graph_object_classifier",
        "finite_index_expansion",
        "graph_handoff_dependencies_missing",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: graph/Rosati bridge is pinned as a directed later-realization object"
)
print(
    "VERDICT: graph/Rosati/count data remain source constraints carried by a "
    "named pregraph payload. Only a directed later-realization image may live "
    "in graph_realization. Context collapse, graph-object prerequisites, "
    "reverse pullback, point semantics, retuned images, classifiers, row "
    "tables, and finite-index towers do not construct the missing object."
)
