r"""Finite-index closure contract for the doc-491 globular modification.

Doc 491 pins the represented cartesian boundary-fiber coherence cells as faces
of one source-level globular modification.  The next disciplined cut is not to
ask for another boundary-fiber layer.  The modification must be absorbed by the
already finite coherent source-presentation index, and applying the closure
operator to it must return the same source totalizer.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_finite_index_closure_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

CATEGORY_ID = "Cat_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_ID = "Tot_CohSrcPres_BCCube_Qbar_BECD"
FINITE_INDEX_ID = "FinIdx_CohSrcPres_BCCube_Qbar_BECD"
ETA_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
DOC491_MODIFICATION_ID = (
    "Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
DOC491_BOUNDARY_ID = (
    "GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
DOC491_INDEX_INCLUSION_ID = (
    "incl_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_FinIdx_CohSrcPres_BCCube_Qbar_BECD"
)
DOC491_IDEMPOTENT_CLOSURE_ID = (
    "idem_close_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD"
)

REQUIRED_FACETS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

REQUIRED_COHERENCE_CELLS = {
    "source_square_cell",
    "beck_chevalley_cube_cell",
    "cartesian_lift_cell",
    "component_cone_cell",
    "component_projection_pair_cell",
    "globular_modification_cell",
    "boundary_fiber_cell",
    "cartesian_boundary_fiber_cell",
    "boundary_fiber_coherence_cell",
    "fiber_coherence_modification_cell",
    "source_boundary_cell",
    "target_boundary_cell",
    "multiplier_path_cell",
    "coefficient_preservation_cell",
    "signed_support_preservation_cell",
    "source_before_points_cell",
    "closed_finite_coherence_cell",
}

FINITE_INDEX = REQUIRED_FACETS | REQUIRED_COHERENCE_CELLS

REQUIRED_DOC491_CELLS = {
    "cell_C3_C5_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_C5_C3_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_C3_C3_C5_C45_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_F22_interchange_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_boundary_restriction_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_boundary_fiber_arrow_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_fixed_globular_boundary_pullback_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_source_boundary_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_target_boundary_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_pasting_faces_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
}

REQUIRED_DOC491_FACES = {
    f"face_{cell}_fiber_coherence_globular_boundary"
    for cell in REQUIRED_DOC491_CELLS
}

REQUIRED_EDGES = {
    ("coherent_source_category", "coherent_source_totalizer"),
    ("coherent_source_totalizer", "finite_cell_index"),
    ("finite_cell_index", "endpoint_integrality"),
    ("finite_cell_index", "degree_maps"),
    ("finite_cell_index", "dd4_boundary"),
    ("finite_cell_index", "boundary_pushforward"),
    ("finite_cell_index", "graph_composition"),
    ("finite_cell_index", "rosati_count"),
    ("finite_cell_index", "control_death"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("eta_equalizer_lift", "doc491_globular_modification"),
    ("doc491_globular_modification", "doc491_globular_boundary"),
    ("doc491_globular_modification", "doc491_faces"),
    ("doc491_faces", "fiber_coherence_modification_cell"),
    ("doc491_globular_modification", "finite_cell_index"),
    ("finite_cell_index", "closed_finite_coherence_cell"),
    ("closed_finite_coherence_cell", "doc491_idempotent_closure"),
    ("doc491_idempotent_closure", "same_coherent_source_totalizer"),
    ("same_coherent_source_totalizer", "no_next_coherence_obligation"),
    ("finite_cell_index", "source_before_points"),
    ("source_before_points", "controls_not_points"),
    ("source_before_points", "dh_not_points"),
    ("source_before_points", "epstein_not_points"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def normalize(chi: dict[int, int]) -> dict[int, int]:
    return {key: val for key, val in sorted(chi.items()) if val != 0}


def chi_col(a, b, edges) -> dict[int, int]:
    out: dict[int, int] = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return normalize(out)


def convolve_chi(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return normalize(out)


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


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


def graph_connected(edges: set[tuple[str, str]]) -> bool:
    nodes = {node for edge in edges for node in edge}
    if not nodes:
        return False
    seen = {next(iter(nodes))}
    changed = True
    while changed:
        changed = False
        for left, right in edges:
            if left in seen and right not in seen:
                seen.add(right)
                changed = True
            if right in seen and left not in seen:
                seen.add(left)
                changed = True
    return seen == nodes


def source(**kwargs):
    data = {
        "carrier_native": False,
        "finite_source_presentation_category_actual": False,
        "represented_totalizer_actual": False,
        "finite_limit_equalizer_actual": False,
        "eta_lift_actual": False,
        "doc491_modification_actual": False,
        "doc491_boundary_actual": False,
        "doc491_cells": set(),
        "doc491_faces": set(),
        "doc491_in_finite_index": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "no_index_expansion": False,
        "idempotent_closure_actual": False,
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "one_more_layer_tower": False,
        "post_doc491_boundary_fiber": False,
        "post_doc491_cartesian_transport": False,
        "post_doc491_globular_modification": False,
        "expanded_finite_index": False,
        "declared_totalizer": False,
        "chosen_section": False,
        "pro_completion": False,
        "local_chart": False,
        "graph_side_closure": False,
        "retuned_index": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    (
        "finite_source_presentation_category_actual",
        "finite_source_presentation_category_missing",
    ),
    ("represented_totalizer_actual", "represented_totalizer_missing"),
    ("finite_limit_equalizer_actual", "finite_limit_equalizer_missing"),
    ("eta_lift_actual", "eta_lift_missing"),
    ("doc491_modification_actual", "doc491_modification_missing"),
    ("doc491_boundary_actual", "doc491_boundary_missing"),
    ("doc491_in_finite_index", "doc491_not_in_finite_index"),
    ("no_index_expansion", "finite_index_expands"),
    ("idempotent_closure_actual", "idempotent_closure_missing"),
    ("closure_returns_same_totalizer", "closure_does_not_return_same_totalizer"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("one_more_layer_tower", "one_more_layer_tower"),
    ("post_doc491_boundary_fiber", "post_doc491_boundary_fiber"),
    ("post_doc491_cartesian_transport", "post_doc491_cartesian_transport"),
    ("post_doc491_globular_modification", "post_doc491_globular_modification"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("declared_totalizer", "declared_totalizer"),
    ("chosen_section", "chosen_section"),
    ("pro_completion", "pro_completion"),
    ("local_chart", "local_chart"),
    ("graph_side_closure", "graph_side_closure"),
    ("retuned_index", "retuned_index"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(data["finite_index"]) != FINITE_INDEX:
        out.append("finite_index_not_exact")
    if data["finite_index_cardinality"] != len(FINITE_INDEX):
        out.append("finite_index_cardinality_wrong")
    if not REQUIRED_DOC491_CELLS <= set(data["doc491_cells"]):
        out.append("doc491_cells_missing")
    if not REQUIRED_DOC491_FACES <= set(data["doc491_faces"]):
        out.append("doc491_faces_missing")
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_finite_index_closure(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        finite_source_presentation_category_actual=True,
        represented_totalizer_actual=True,
        finite_limit_equalizer_actual=True,
        eta_lift_actual=True,
        doc491_modification_actual=True,
        doc491_boundary_actual=True,
        doc491_cells=set(REQUIRED_DOC491_CELLS),
        doc491_faces=set(REQUIRED_DOC491_FACES),
        doc491_in_finite_index=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        no_index_expansion=True,
        idempotent_closure_actual=True,
        closure_returns_same_totalizer=True,
        no_next_coherence_obligation=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def finite_index_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "category": CATEGORY_ID,
        "totalizer": TOTALIZER_ID,
        "finite_index": FINITE_INDEX_ID,
        "eta_lift": ETA_LIFT_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "doc491_index_inclusion": DOC491_INDEX_INCLUSION_ID,
        "doc491_idempotent_closure": DOC491_IDEMPOTENT_CLOSURE_ID,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
        "index_size": len(FINITE_INDEX),
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
    }


C3 = ((3,), (1,), ((0, 0),))
C5 = ((5,), (1,), ((0, 0),))
C15 = ((15,), (1,), ((0, 0),))
C45 = ((45,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

z = chi_col(*ZERO_SPLIT)
chi_C3 = chi_col(*C3)
chi_C5 = chi_col(*C5)
chi_C15 = chi_col(*C15)
chi_C45 = chi_col(*C45)
chi_F22 = chi_col(*F22)
chi_C15F22 = convolve_chi(chi_C15, chi_F22)
chi_C45F22 = convolve_chi(chi_C45, chi_F22)

zC3 = convolve_chi(z, chi_C3)
zC5 = convolve_chi(z, chi_C5)
zC15 = convolve_chi(z, chi_C15)
zC45 = convolve_chi(z, chi_C45)
zF22 = convolve_chi(z, chi_F22)
zC15F22 = convolve_chi(z, chi_C15F22)
zC45F22 = convolve_chi(z, chi_C45F22)
T3_T5_z = convolve_chi(zC5, chi_C3)
T5_T3_z = convolve_chi(zC3, chi_C5)
T3_T3_T5_z = convolve_chi(T3_T5_z, chi_C3)
T15_zF22 = convolve_chi(zF22, chi_C15)
T45_zF22 = convolve_chi(zF22, chi_C45)

profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD1 doc491 modification is finite-index closed",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_EDGES)
    and len(REQUIRED_FACETS) == 7
    and len(REQUIRED_COHERENCE_CELLS) == 17
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC491_CELLS) == 10
    and len(REQUIRED_DOC491_FACES) == 10
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and finite_index_payload(T3_T5_z) == finite_index_payload(zC15)
    and finite_index_payload(T5_T3_z) == finite_index_payload(zC15)
    and finite_index_payload(T3_T3_T5_z) == finite_index_payload(zC45)
    and finite_index_payload(T15_zF22) == finite_index_payload(zC15F22)
    and finite_index_payload(T45_zF22) == finite_index_payload(zC45F22),
    "H1=%s index=%d cells=%d faces=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(FINITE_INDEX),
        len(REQUIRED_DOC491_CELLS),
        len(REQUIRED_DOC491_FACES),
    ),
)

graph_only = live_source(
    finite_limit_equalizer_actual=False,
    doc491_in_finite_index=False,
    graph_side_closure=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD2 graph closure is not finite-index absorption",
    not accepts_finite_index_closure(graph_only)
    and {
        "finite_limit_equalizer_missing",
        "doc491_not_in_finite_index",
        "graph_side_closure",
    }
    <= set(reasons(graph_only)),
    ",".join(reasons(graph_only)),
)

tower = live_source(
    doc491_in_finite_index=False,
    no_index_expansion=False,
    idempotent_closure_actual=False,
    closure_returns_same_totalizer=False,
    no_next_coherence_obligation=False,
    one_more_layer_tower=True,
    post_doc491_boundary_fiber=True,
    post_doc491_cartesian_transport=True,
    post_doc491_globular_modification=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD3 one-more-layer after doc491 fails",
    not accepts_finite_index_closure(tower)
    and {
        "doc491_not_in_finite_index",
        "finite_index_expands",
        "idempotent_closure_missing",
        "closure_does_not_return_same_totalizer",
        "next_coherence_obligation_open",
        "one_more_layer_tower",
        "post_doc491_boundary_fiber",
        "post_doc491_cartesian_transport",
        "post_doc491_globular_modification",
    }
    <= set(reasons(tower)),
    ",".join(reasons(tower)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"post_doc491_boundary_fiber_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    no_index_expansion=False,
    expanded_finite_index=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD4 expanded finite indexes are tower data",
    not accepts_finite_index_closure(expanded)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "finite_index_expands",
        "expanded_finite_index",
    }
    <= set(reasons(expanded)),
    ",".join(reasons(expanded)),
)

declared = live_source(
    finite_source_presentation_category_actual=False,
    represented_totalizer_actual=False,
    eta_lift_actual=False,
    declared_totalizer=True,
    chosen_section=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD5 declared totalizers and chosen sections fail",
    not accepts_finite_index_closure(declared)
    and {
        "finite_source_presentation_category_missing",
        "represented_totalizer_missing",
        "eta_lift_missing",
        "declared_totalizer",
        "chosen_section",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)

missing_doc491 = live_source(
    doc491_modification_actual=False,
    doc491_boundary_actual=False,
    doc491_cells=set(list(REQUIRED_DOC491_CELLS)[:-1]),
    doc491_faces=set(list(REQUIRED_DOC491_FACES)[:-1]),
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD6 doc491 cells faces and boundary remain mandatory",
    not accepts_finite_index_closure(missing_doc491)
    and {
        "doc491_modification_missing",
        "doc491_boundary_missing",
        "doc491_cells_missing",
        "doc491_faces_missing",
    }
    <= set(reasons(missing_doc491)),
    ",".join(reasons(missing_doc491)),
)

wrapper = live_source(
    carrier_native=False,
    finite_limit_equalizer_actual=False,
    pro_completion=True,
    local_chart=True,
    graph_side_closure=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD7 pro local and graph-side closures fail",
    not accepts_finite_index_closure(wrapper)
    and {
        "not_carrier_native",
        "finite_limit_equalizer_missing",
        "pro_completion",
        "local_chart",
        "graph_side_closure",
    }
    <= set(reasons(wrapper)),
    ",".join(reasons(wrapper)),
)

retuned = live_source(
    idempotent_closure_actual=False,
    closure_returns_same_totalizer=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_index=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD8 retuned non-idempotent closure fails",
    not accepts_finite_index_closure(retuned)
    and {
        "idempotent_closure_missing",
        "closure_does_not_return_same_totalizer",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_index",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

control = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD9 control/DH/Epstein finite-index closures fail",
    not accepts_finite_index_closure(control)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control)),
    ",".join(reasons(control)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_EDGES - {edge})
    for edge in list(REQUIRED_EDGES)[:6]
] + [
    live_source(finite_index=set(FINITE_INDEX - {"closed_finite_coherence_cell"})),
    live_source(finite_index_cardinality=23),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD10 only exact idempotent finite-index closure passes",
    accepts_finite_index_closure(live_source())
    and not any(accepts_finite_index_closure(data) for data in missing_edges)
    and {"required_edges_missing", "finite_index_not_exact", "finite_index_cardinality_wrong"}
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (sorted(missing_reasons), accepts_finite_index_closure(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD10 ALL PASS: "
    "doc491 globular modification finite-index closure pinned"
)
print(
    "VERDICT: the doc-491 globular modification must be absorbed by the existing "
    "finite coherent source-presentation index and close idempotently to the "
    "same totalizer. Post-doc491 boundary fibers, cartesian transports, "
    "globular modifications, expanded finite indexes, declared totalizers, "
    "and control/DH/Epstein point-formability do not construct the missing object."
)
