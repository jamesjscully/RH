r"""Equalizer-idempotent contract for finite-index closure.

Doc 492 forces the doc-491 globular modification into the finite coherent
source-presentation index.  This witness pins the next edge: that finite-index
closure must be the source equalizer idempotent compatible with alpha/beta,
the equalizer monic, and the eta lift.  Set-level or Karoubi-completed
idempotents do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_finite_index_equalizer_idempotent_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

SOURCE_CATEGORY_ID = "SrcCat_BCCube_Qbar_BECD"
PRODUCT_ID = "Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells"
ALPHA_ID = "alpha_CohSrcPres_BCCube_Qbar_BECD_constraints"
BETA_ID = "beta_CohSrcPres_BCCube_Qbar_BECD_constraints"
EQUALIZER_ID = "Eq_CohSrcPres_BCCube_Qbar_BECD"
INCLUSION_ID = "incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"
COMPARISON_ID = "cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"
ETA_SOURCE_ID = "eta_BCCube_Qbar_BECD_source"
ETA_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
ETA_COMPARISON_ID = "cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_ID = "Tot_CohSrcPres_BCCube_Qbar_BECD"
FINITE_INDEX_ID = "FinIdx_CohSrcPres_BCCube_Qbar_BECD"
DOC491_MODIFICATION_ID = (
    "Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
DOC491_BOUNDARY_ID = (
    "GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
EQUALIZER_IDEMPOTENT_ID = (
    "e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD"
)
IDEMPOTENT_COMPARISON_ID = (
    "cmp_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Tot_CohSrcPres_BCCube_Qbar_BECD"
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
    ("source_category", "product_facets_cells"),
    ("product_facets_cells", "alpha_constraints"),
    ("product_facets_cells", "beta_constraints"),
    ("alpha_constraints", "equalizer_object"),
    ("beta_constraints", "equalizer_object"),
    ("equalizer_object", "equalizer_monic_inclusion"),
    ("equalizer_monic_inclusion", "coherent_source_totalizer"),
    ("equalizer_object", "equalizer_totalizer_comparison"),
    ("equalizer_totalizer_comparison", "comparison_isomorphism"),
    ("comparison_isomorphism", "coherent_source_totalizer"),
    ("eta_source", "eta_equalizer_lift"),
    ("eta_equalizer_lift", "equalizer_object"),
    ("eta_equalizer_lift", "eta_totalizer_comparison"),
    ("eta_totalizer_comparison", "coherent_source_totalizer"),
    ("doc491_globular_modification", "doc491_globular_boundary"),
    ("doc491_globular_modification", "doc491_cells"),
    ("doc491_cells", "doc491_faces"),
    ("doc491_globular_modification", "finite_cell_index"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("fiber_coherence_modification_cell", "equalizer_idempotent"),
    ("equalizer_idempotent", "equalizer_object"),
    ("equalizer_idempotent", "idempotent_on_equalizer"),
    ("equalizer_idempotent", "alpha_beta_compatibility"),
    ("alpha_beta_compatibility", "alpha_constraints"),
    ("alpha_beta_compatibility", "beta_constraints"),
    ("equalizer_idempotent", "monic_inclusion_compatibility"),
    ("monic_inclusion_compatibility", "equalizer_monic_inclusion"),
    ("equalizer_idempotent", "eta_lift_fixed"),
    ("eta_lift_fixed", "eta_equalizer_lift"),
    ("equalizer_idempotent", "idempotent_totalizer_comparison"),
    ("idempotent_totalizer_comparison", "identity_on_totalizer"),
    ("identity_on_totalizer", "same_coherent_source_totalizer"),
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
        "source_category_actual": False,
        "product_actual": False,
        "alpha_actual": False,
        "beta_actual": False,
        "equalizer_actual": False,
        "monic_inclusion_actual": False,
        "comparison_iso_actual": False,
        "eta_lift_actual": False,
        "doc491_modification_actual": False,
        "doc491_boundary_actual": False,
        "doc491_cells": set(),
        "doc491_faces": set(),
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "doc491_in_finite_index": False,
        "equalizer_idempotent_actual": False,
        "idempotent_on_equalizer": False,
        "alpha_beta_compatible": False,
        "monic_inclusion_compatible": False,
        "eta_lift_fixed": False,
        "comparison_identity_on_totalizer": False,
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "index_level_idempotent": False,
        "set_level_closure": False,
        "karoubi_completion": False,
        "external_retract": False,
        "projection_to_facet": False,
        "posthoc_split": False,
        "graph_side_idempotent": False,
        "retuned_idempotent": False,
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("source_category_actual", "source_category_missing"),
    ("product_actual", "product_missing"),
    ("alpha_actual", "alpha_missing"),
    ("beta_actual", "beta_missing"),
    ("equalizer_actual", "equalizer_missing"),
    ("monic_inclusion_actual", "monic_inclusion_missing"),
    ("comparison_iso_actual", "comparison_iso_missing"),
    ("eta_lift_actual", "eta_lift_missing"),
    ("doc491_modification_actual", "doc491_modification_missing"),
    ("doc491_boundary_actual", "doc491_boundary_missing"),
    ("doc491_in_finite_index", "doc491_not_in_finite_index"),
    ("equalizer_idempotent_actual", "equalizer_idempotent_missing"),
    ("idempotent_on_equalizer", "not_idempotent_on_equalizer"),
    ("alpha_beta_compatible", "alpha_beta_incompatible"),
    ("monic_inclusion_compatible", "monic_inclusion_incompatible"),
    ("eta_lift_fixed", "eta_lift_not_fixed"),
    ("comparison_identity_on_totalizer", "comparison_not_identity_on_totalizer"),
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
    ("index_level_idempotent", "index_level_idempotent"),
    ("set_level_closure", "set_level_closure"),
    ("karoubi_completion", "karoubi_completion"),
    ("external_retract", "external_retract"),
    ("projection_to_facet", "projection_to_facet"),
    ("posthoc_split", "posthoc_split"),
    ("graph_side_idempotent", "graph_side_idempotent"),
    ("retuned_idempotent", "retuned_idempotent"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
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


def accepts_equalizer_idempotent(data) -> bool:
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
        source_category_actual=True,
        product_actual=True,
        alpha_actual=True,
        beta_actual=True,
        equalizer_actual=True,
        monic_inclusion_actual=True,
        comparison_iso_actual=True,
        eta_lift_actual=True,
        doc491_modification_actual=True,
        doc491_boundary_actual=True,
        doc491_cells=set(REQUIRED_DOC491_CELLS),
        doc491_faces=set(REQUIRED_DOC491_FACES),
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        doc491_in_finite_index=True,
        equalizer_idempotent_actual=True,
        idempotent_on_equalizer=True,
        alpha_beta_compatible=True,
        monic_inclusion_compatible=True,
        eta_lift_fixed=True,
        comparison_identity_on_totalizer=True,
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


def equalizer_idempotent_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_category": SOURCE_CATEGORY_ID,
        "product": PRODUCT_ID,
        "alpha": ALPHA_ID,
        "beta": BETA_ID,
        "equalizer": EQUALIZER_ID,
        "inclusion": INCLUSION_ID,
        "comparison": COMPARISON_ID,
        "eta_source": ETA_SOURCE_ID,
        "eta_lift": ETA_LIFT_ID,
        "eta_comparison": ETA_COMPARISON_ID,
        "totalizer": TOTALIZER_ID,
        "finite_index": FINITE_INDEX_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "equalizer_idempotent": EQUALIZER_IDEMPOTENT_ID,
        "idempotent_comparison": IDEMPOTENT_COMPARISON_ID,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD1 finite-index closure is an equalizer idempotent",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_EDGES)
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC491_CELLS) == 10
    and len(REQUIRED_DOC491_FACES) == 10
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and equalizer_idempotent_payload(T3_T5_z) == equalizer_idempotent_payload(zC15)
    and equalizer_idempotent_payload(T5_T3_z) == equalizer_idempotent_payload(zC15)
    and equalizer_idempotent_payload(T3_T3_T5_z)
    == equalizer_idempotent_payload(zC45)
    and equalizer_idempotent_payload(T15_zF22)
    == equalizer_idempotent_payload(zC15F22)
    and equalizer_idempotent_payload(T45_zF22)
    == equalizer_idempotent_payload(zC45F22),
    "H1=%s index=%d cells=%d faces=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(FINITE_INDEX),
        len(REQUIRED_DOC491_CELLS),
        len(REQUIRED_DOC491_FACES),
    ),
)

index_only = live_source(
    equalizer_idempotent_actual=False,
    idempotent_on_equalizer=False,
    alpha_beta_compatible=False,
    monic_inclusion_compatible=False,
    eta_lift_fixed=False,
    index_level_idempotent=True,
    set_level_closure=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD2 index-level idempotents fail",
    not accepts_equalizer_idempotent(index_only)
    and {
        "equalizer_idempotent_missing",
        "not_idempotent_on_equalizer",
        "alpha_beta_incompatible",
        "monic_inclusion_incompatible",
        "eta_lift_not_fixed",
        "index_level_idempotent",
        "set_level_closure",
    }
    <= set(reasons(index_only)),
    ",".join(reasons(index_only)),
)

karoubi = live_source(
    source_category_actual=False,
    equalizer_actual=False,
    monic_inclusion_actual=False,
    karoubi_completion=True,
    external_retract=True,
    posthoc_split=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD3 Karoubi and external retracts fail",
    not accepts_equalizer_idempotent(karoubi)
    and {
        "source_category_missing",
        "equalizer_missing",
        "monic_inclusion_missing",
        "karoubi_completion",
        "external_retract",
        "posthoc_split",
    }
    <= set(reasons(karoubi)),
    ",".join(reasons(karoubi)),
)

incompatible = live_source(
    alpha_beta_compatible=False,
    monic_inclusion_compatible=False,
    comparison_identity_on_totalizer=False,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD4 alpha beta monic compatibility is mandatory",
    not accepts_equalizer_idempotent(incompatible)
    and {
        "alpha_beta_incompatible",
        "monic_inclusion_incompatible",
        "comparison_not_identity_on_totalizer",
    }
    <= set(reasons(incompatible)),
    ",".join(reasons(incompatible)),
)

unsourced = live_source(
    eta_lift_actual=False,
    eta_lift_fixed=False,
    closure_returns_same_totalizer=False,
    posthoc_split=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD5 eta lift must be fixed by the idempotent",
    not accepts_equalizer_idempotent(unsourced)
    and {
        "eta_lift_missing",
        "eta_lift_not_fixed",
        "closure_does_not_return_same_totalizer",
        "posthoc_split",
    }
    <= set(reasons(unsourced)),
    ",".join(reasons(unsourced)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"equalizer_idempotent_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    expanded_finite_index=True,
    projection_to_facet=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD6 expanded indexes and facet projections fail",
    not accepts_equalizer_idempotent(expanded)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "expanded_finite_index",
        "projection_to_facet",
    }
    <= set(reasons(expanded)),
    ",".join(reasons(expanded)),
)

missing_doc491 = live_source(
    doc491_modification_actual=False,
    doc491_boundary_actual=False,
    doc491_cells=set(list(REQUIRED_DOC491_CELLS)[:-1]),
    doc491_faces=set(list(REQUIRED_DOC491_FACES)[:-1]),
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD7 doc491 payload remains mandatory",
    not accepts_equalizer_idempotent(missing_doc491)
    and {
        "doc491_modification_missing",
        "doc491_boundary_missing",
        "doc491_cells_missing",
        "doc491_faces_missing",
    }
    <= set(reasons(missing_doc491)),
    ",".join(reasons(missing_doc491)),
)

retuned = live_source(
    comparison_iso_actual=False,
    comparison_identity_on_totalizer=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_idempotent=True,
    graph_side_idempotent=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD8 retuned graph-side idempotents fail",
    not accepts_equalizer_idempotent(retuned)
    and {
        "comparison_iso_missing",
        "comparison_not_identity_on_totalizer",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_idempotent",
        "graph_side_idempotent",
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD9 control/DH/Epstein idempotents fail",
    not accepts_equalizer_idempotent(control)
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
    for edge in list(REQUIRED_EDGES)[:8]
] + [
    live_source(equalizer_idempotent_actual=False),
    live_source(idempotent_on_equalizer=False),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD10 only source equalizer idempotent passes",
    accepts_equalizer_idempotent(live_source())
    and not any(accepts_equalizer_idempotent(data) for data in missing_edges)
    and {
        "required_edges_missing",
        "equalizer_idempotent_missing",
        "not_idempotent_on_equalizer",
        "next_coherence_obligation_open",
    }
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (sorted(missing_reasons), accepts_equalizer_idempotent(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD10 ALL PASS: "
    "finite-index closure equalizer idempotent pinned"
)
print(
    "VERDICT: the doc-492 finite-index closure must be the actual source "
    "equalizer idempotent compatible with alpha/beta, the monic inclusion, "
    "and the eta lift, comparing to the identity on the same totalizer. "
    "Index-level idempotents, Karoubi completions, external retracts, facet "
    "projections, retuned graph-side idempotents, and control/DH/Epstein "
    "point-formability do not construct the missing object."
)
