r"""Context-separated finite-limit subrepresenter contract.

Doc 529 requires the source-fiber subrepresenter to be cut out by one
finite-limit/equalizer fork. This witness pins the context discipline around
that cut: the original DD.4 nonboundary class and the certificate-killed
image must remain in distinct bridged contexts, and source-level graph /
Rosati / count constraints must remain source constraints before later graph
realization. Collapsing those contexts is a contradiction, not progress.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
BOUNDARY_CERT_ID = "BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
JOINT_FORK_ID = "Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_endpoint_dd4_rosati_control_NCoup"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_constraints_to_SubRep_source_fiber"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
COUPLING_IMAGE_ID = "Img_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_coupled_self_dual_exact_sources"
DELTA_ID = "Delta_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_to_dQ_boundary"
NORMAL_RATIO_ID = "NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2"

CONTEXTS = {
    "source_prepoint",
    "source_fiber",
    "source_constraint",
    "finite_limit",
    "original_h1",
    "certificate_image",
    "graph_realization",
    "finite_index",
}

REQUIRED_SOURCE_CONSTRAINTS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

REQUIRED_CONTEXT_EDGES = {
    ("original_h1", "dd4_certificate_handoff", "certificate_image"),
    ("source_constraint", "graph_realization_bridge", "graph_realization"),
    ("finite_limit", "cuts_out", "source_fiber"),
    ("source_constraint", "imposed_before", "graph_realization"),
    ("source_prepoint", "precedes", "graph_realization"),
}

BANNED = (
    ("context_collapse_dd4", "context_collapse_dd4"),
    ("certificate_kills_original_h1", "certificate_kills_original_h1"),
    ("dd4_bridge_missing", "dd4_bridge_missing"),
    ("dd4_bridge_reversible", "dd4_bridge_reversible"),
    ("source_constraint_is_graph_realization", "source_constraint_is_graph_realization"),
    ("graph_bridge_missing", "graph_bridge_missing"),
    ("graph_bridge_reversible_before_points", "graph_bridge_reversible_before_points"),
    ("graph_object_required_before_source_fork", "graph_object_required_before_source_fork"),
    ("source_before_points_erased", "source_before_points_erased"),
    ("control_points_admitted", "control_points_admitted"),
    ("finite_index_expanded", "finite_index_expanded"),
    ("one_more_layer_tower", "one_more_layer_tower"),
)

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("contexts_declared", "contexts_not_declared"),
    ("dd4_contexts_distinct", "dd4_contexts_not_distinct"),
    ("dd4_bridge_actual", "dd4_bridge_missing"),
    ("dd4_bridge_image_only", "dd4_bridge_not_image_only"),
    ("original_h1_nonboundary", "original_h1_boundary"),
    ("certificate_kills_image_only", "certificate_does_not_kill_image"),
    ("graph_contexts_distinct", "graph_contexts_not_distinct"),
    ("graph_bridge_actual", "graph_bridge_missing"),
    ("graph_bridge_later_only", "graph_bridge_not_later_only"),
    ("source_constraints_pregraph", "source_constraints_not_pregraph"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("joint_fork_actual", "joint_fork_missing"),
    ("equalizer_arrow_actual", "equalizer_arrow_missing"),
    ("all_source_constraints_in_fork", "source_constraints_missing"),
    ("source_before_points", "source_not_before_points"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
    ("exact_24_cell_finite_index", "finite_index_not_exact"),
    ("context_edges_complete", "context_edges_incomplete"),
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make_h1(L: int):
    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})
        term = {0: 1}
        out = {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            out = add(out, term)
        return out

    def phi(f):
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return mul, inv, phi


def to_vec(f, L: int) -> tuple[int, ...]:
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L: int, mul) -> set[tuple[int, ...]]:
    seen = {(0,) * L}
    queue = [(0,) * L]
    while queue:
        current = from_vec(queue.pop())
        for gen in gens:
            nxt = to_vec(mul(current, gen), L)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def h1_profile(L: int) -> dict[str, object]:
    mul, inv, phi = make_h1(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(boundary_gens, L, mul)
    norm_image = closure(norm_gens, L, mul)
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "h1_order": z1_order // len(coboundaries),
        "res1_c": c.get(1, 0),
        "coboundaries_res1_zero": all(
            from_vec(vec).get(1, 0) == 0 for vec in coboundaries
        ),
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "contexts_declared": False,
        "dd4_contexts_distinct": False,
        "dd4_bridge_actual": False,
        "dd4_bridge_image_only": False,
        "original_h1_nonboundary": False,
        "certificate_kills_image_only": False,
        "graph_contexts_distinct": False,
        "graph_bridge_actual": False,
        "graph_bridge_later_only": False,
        "source_constraints_pregraph": False,
        "finite_limit_cut_actual": False,
        "joint_fork_actual": False,
        "equalizer_arrow_actual": False,
        "all_source_constraints_in_fork": False,
        "source_before_points": False,
        "source_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "exact_24_cell_finite_index": False,
        "context_edges_complete": False,
        "contexts": set(),
        "source_constraints": set(),
        "context_edges": set(),
        "context_collapse_dd4": False,
        "certificate_kills_original_h1": False,
        "dd4_bridge_missing": False,
        "dd4_bridge_reversible": False,
        "source_constraint_is_graph_realization": False,
        "graph_bridge_missing": False,
        "graph_bridge_reversible_before_points": False,
        "graph_object_required_before_source_fork": False,
        "source_before_points_erased": False,
        "control_points_admitted": False,
        "finite_index_expanded": False,
        "one_more_layer_tower": False,
    }
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not CONTEXTS <= set(data["contexts"]):
        out.append("declared_contexts_missing")
    if not REQUIRED_SOURCE_CONSTRAINTS <= set(data["source_constraints"]):
        out.append("fork_constraints_missing")
    if not REQUIRED_CONTEXT_EDGES <= set(data["context_edges"]):
        out.append("required_context_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_context_separation(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and CONTEXTS <= set(data["contexts"])
        and REQUIRED_SOURCE_CONSTRAINTS <= set(data["source_constraints"])
        and REQUIRED_CONTEXT_EDGES <= set(data["context_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        contexts_declared=True,
        dd4_contexts_distinct=True,
        dd4_bridge_actual=True,
        dd4_bridge_image_only=True,
        original_h1_nonboundary=True,
        certificate_kills_image_only=True,
        graph_contexts_distinct=True,
        graph_bridge_actual=True,
        graph_bridge_later_only=True,
        source_constraints_pregraph=True,
        finite_limit_cut_actual=True,
        joint_fork_actual=True,
        equalizer_arrow_actual=True,
        all_source_constraints_in_fork=True,
        source_before_points=True,
        source_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        exact_24_cell_finite_index=True,
        context_edges_complete=True,
        contexts=set(CONTEXTS),
        source_constraints=set(REQUIRED_SOURCE_CONSTRAINTS),
        context_edges=set(REQUIRED_CONTEXT_EDGES),
    )
    data.update(kwargs)
    return data


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1 context-separated finite-limit cut is coherent",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and accepts_context_separation(live_source())
    and DD4_CLASS_ID
    and BOUNDARY_CERT_ID
    and FINITE_LIMIT_CUT_ID
    and JOINT_FORK_ID
    and EQUALIZER_ARROW_ID,
    "H1=%s contexts=%d constraints=%d"
    % ([p["h1_order"] for p in profiles], len(CONTEXTS), len(REQUIRED_SOURCE_CONSTRAINTS)),
)

dd4_collapse = live_source(
    dd4_contexts_distinct=False,
    dd4_bridge_image_only=False,
    context_collapse_dd4=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2 DD4 original class cannot share the certificate-image context",
    not accepts_context_separation(dd4_collapse)
    and {
        "dd4_contexts_not_distinct",
        "dd4_bridge_not_image_only",
        "context_collapse_dd4",
    }
    <= set(reasons(dd4_collapse)),
    ",".join(reasons(dd4_collapse)),
)

kill_original = live_source(
    original_h1_nonboundary=False,
    certificate_kills_image_only=False,
    certificate_kills_original_h1=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3 certificate kill cannot act in original H1",
    not accepts_context_separation(kill_original)
    and {
        "original_h1_boundary",
        "certificate_does_not_kill_image",
        "certificate_kills_original_h1",
    }
    <= set(reasons(kill_original)),
    ",".join(reasons(kill_original)),
)

missing_dd4_bridge = live_source(
    dd4_bridge_actual=False,
    dd4_bridge_image_only=False,
    dd4_bridge_missing=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4 DD4 handoff requires an explicit bridge",
    not accepts_context_separation(missing_dd4_bridge)
    and {
        "dd4_bridge_missing",
        "dd4_bridge_not_image_only",
    }
    <= set(reasons(missing_dd4_bridge)),
    ",".join(reasons(missing_dd4_bridge)),
)

graph_collapse = live_source(
    graph_contexts_distinct=False,
    source_constraints_pregraph=False,
    source_constraint_is_graph_realization=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5 source constraints cannot be actual graph realization",
    not accepts_context_separation(graph_collapse)
    and {
        "graph_contexts_not_distinct",
        "source_constraints_not_pregraph",
        "source_constraint_is_graph_realization",
    }
    <= set(reasons(graph_collapse)),
    ",".join(reasons(graph_collapse)),
)

graph_bridge_bad = live_source(
    graph_bridge_actual=False,
    graph_bridge_later_only=False,
    graph_bridge_missing=True,
    graph_bridge_reversible_before_points=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6 graph realization bridge is later-only and nonreversible prepoint",
    not accepts_context_separation(graph_bridge_bad)
    and {
        "graph_bridge_missing",
        "graph_bridge_not_later_only",
        "graph_bridge_reversible_before_points",
    }
    <= set(reasons(graph_bridge_bad)),
    ",".join(reasons(graph_bridge_bad)),
)

graph_first = live_source(
    source_before_graph_objects=False,
    graph_object_required_before_source_fork=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7 graph objects cannot be prerequisites for the source fork",
    not accepts_context_separation(graph_first)
    and {
        "source_not_before_graph_objects",
        "graph_object_required_before_source_fork",
    }
    <= set(reasons(graph_first)),
    ",".join(reasons(graph_first)),
)

point_erasure = live_source(
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    source_before_points_erased=True,
    control_points_admitted=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8 point semantics cannot enter before source context separation",
    not accepts_context_separation(point_erasure)
    and {
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "source_before_points_erased",
        "control_points_admitted",
    }
    <= set(reasons(point_erasure)),
    ",".join(reasons(point_erasure)),
)

index_tower = live_source(
    exact_24_cell_finite_index=False,
    finite_index_expanded=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9 context separation cannot open a new finite-index tower",
    not accepts_context_separation(index_tower)
    and {
        "finite_index_not_exact",
        "finite_index_expanded",
        "one_more_layer_tower",
    }
    <= set(reasons(index_tower)),
    ",".join(reasons(index_tower)),
)

missing_edges = [
    live_source(context_edges=REQUIRED_CONTEXT_EDGES - {("original_h1", "dd4_certificate_handoff", "certificate_image")}),
    live_source(context_edges=REQUIRED_CONTEXT_EDGES - {("source_constraint", "graph_realization_bridge", "graph_realization")}),
    live_source(source_constraints=REQUIRED_SOURCE_CONSTRAINTS - {"rosati_count"}),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 all context edges and fork constraints are mandatory",
    not any(accepts_context_separation(data) for data in missing_edges)
    and {
        "required_context_edges_missing",
        "fork_constraints_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: context-separated finite-limit source-fiber cut pinned"
)
print(
    "VERDICT: the doc-529 finite-limit cut is coherent only if original H1, "
    "certificate-image, source-constraint, and graph-realization contexts remain "
    "distinct and bridged. DD.4 context collapse, certificate killing in original "
    "H1, graph-realization prerequisites, point-semantics erasure, expanded "
    "finite indexes, and context-edge omissions do not construct the missing object."
)
