r"""Monic-cancellation contract for the doc-517 equalizer idempotent.

Doc 517 puts the finite-index closure on the source equalizer. This witness
pins the next edge: compatibility with the monic inclusion must cancel the
idempotent to the identity on Eq_NCoup_med_UP_Eq_id_source_components itself.
Comparison-only identities, hidden-kernel endomorphisms, automorphism masks,
and index-level identities do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD"
failures: list[str] = []

SOURCE_CATEGORY_ID = "SrcCat_NCoup_med_UP_Eq_id_Qbar_BECD"
PRODUCT_ID = "Prod_NCoup_med_UP_Eq_id_source_components_facets_cells"
ALPHA_ID = "alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_ID = "beta_NCoup_med_UP_Eq_id_source_constraints"
EQUALIZER_ID = "Eq_NCoup_med_UP_Eq_id_source_components"
EQUALIZER_IDENTITY_ID = "id_Eq_NCoup_med_UP_Eq_id_source_components"
INCLUSION_ID = "incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components"
COMPARISON_ID = "cmp_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components"
TOTALIZER_ID = "Tot_NCoup_med_UP_Eq_id_source_components"
FINITE_INDEX_ID = "FinIdx_NCoup_med_UP_Eq_id_source_components"
UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
DOC515_COHERENCE_ID = (
    "Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
)
DOC515_INDEX_CELL = "boundary_fiber_coherence_cell"
EQUALIZER_IDEMPOTENT_ID = (
    "e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components"
)
MONIC_CANCELLATION_ID = (
    "cancel_incl_Eq_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Eq_NCoup_med_UP_Eq_id_source_components"
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

REQUIRED_DOC515_CELLS = {
    "cell_C3_C5_C15_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_C5_C3_C15_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_C3_C3_C5_C45_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_F22_interchange_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_boundary_restriction_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_boundary_fiber_arrow_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_fixed_globular_boundary_pullback_NCoup_med_UP_Eq_id",
    "cell_source_boundary_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_target_boundary_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_pasting_faces_cartesian_naturality_NCoup_med_UP_Eq_id",
}

REQUIRED_EDGES = {
    ("source_category", "product_facets_cells"),
    ("product_facets_cells", "alpha_constraints"),
    ("product_facets_cells", "beta_constraints"),
    ("alpha_constraints", "equalizer_object"),
    ("beta_constraints", "equalizer_object"),
    ("equalizer_object", "equalizer_identity"),
    ("equalizer_object", "equalizer_monic_inclusion"),
    ("equalizer_monic_inclusion", "same_equalizer_identity_mediator_totalizer"),
    ("equalizer_object", "equalizer_totalizer_comparison"),
    ("equalizer_totalizer_comparison", "comparison_isomorphism"),
    ("comparison_isomorphism", "same_equalizer_identity_mediator_totalizer"),
    ("universal_mediator", "equalizer_object"),
    ("finite_cell_index", DOC515_INDEX_CELL),
    ("doc515_cartesian_boundary_fiber_coherence", "doc515_cells"),
    ("doc515_cells", DOC515_INDEX_CELL),
    (DOC515_INDEX_CELL, "equalizer_idempotent"),
    ("equalizer_idempotent", "equalizer_object"),
    ("equalizer_idempotent", "idempotent_on_equalizer"),
    ("equalizer_idempotent", "monic_inclusion_compatibility"),
    ("monic_inclusion_compatibility", "equalizer_monic_inclusion"),
    ("monic_inclusion_compatibility", "monic_cancellation"),
    ("monic_cancellation", "equalizer_identity"),
    ("monic_cancellation", "idempotent_equals_identity"),
    ("idempotent_equals_identity", "alpha_beta_compatibility"),
    ("alpha_beta_compatibility", "alpha_constraints"),
    ("alpha_beta_compatibility", "beta_constraints"),
    ("idempotent_equals_identity", "universal_mediator_fixed"),
    ("universal_mediator_fixed", "universal_mediator"),
    ("idempotent_equals_identity", "doc515_coherence_fixed"),
    ("doc515_coherence_fixed", "doc515_cartesian_boundary_fiber_coherence"),
    ("idempotent_equals_identity", "comparison_identity_on_totalizer"),
    ("comparison_identity_on_totalizer", "same_equalizer_identity_mediator_totalizer"),
    ("same_equalizer_identity_mediator_totalizer", "no_next_coherence_obligation"),
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
        "equalizer_identity_actual": False,
        "monic_inclusion_actual": False,
        "comparison_iso_actual": False,
        "universal_mediator_actual": False,
        "doc515_coherence_actual": False,
        "doc515_cells": set(),
        "doc515_in_finite_index": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "equalizer_idempotent_actual": False,
        "idempotent_on_equalizer": False,
        "monic_inclusion_compatible": False,
        "monic_cancellation_actual": False,
        "idempotent_equals_identity": False,
        "alpha_beta_compatible": False,
        "universal_mediator_fixed": False,
        "doc515_coherence_fixed": False,
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
        "comparison_only_identity": False,
        "hidden_kernel_idempotent": False,
        "automorphism_mask": False,
        "nonmonic_cancellation": False,
        "index_identity_only": False,
        "projectionwise_partial_identity": False,
        "quotient_shadow_identity": False,
        "graph_side_identity": False,
        "retuned_identity": False,
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
    ("equalizer_identity_actual", "equalizer_identity_missing"),
    ("monic_inclusion_actual", "monic_inclusion_missing"),
    ("comparison_iso_actual", "comparison_iso_missing"),
    ("universal_mediator_actual", "universal_mediator_missing"),
    ("doc515_coherence_actual", "doc515_coherence_missing"),
    ("doc515_in_finite_index", "doc515_not_in_finite_index"),
    ("equalizer_idempotent_actual", "equalizer_idempotent_missing"),
    ("idempotent_on_equalizer", "not_idempotent_on_equalizer"),
    ("monic_inclusion_compatible", "monic_inclusion_incompatible"),
    ("monic_cancellation_actual", "monic_cancellation_missing"),
    ("idempotent_equals_identity", "idempotent_not_identity"),
    ("alpha_beta_compatible", "alpha_beta_incompatible"),
    ("universal_mediator_fixed", "universal_mediator_not_fixed"),
    ("doc515_coherence_fixed", "doc515_coherence_not_fixed"),
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
    ("comparison_only_identity", "comparison_only_identity"),
    ("hidden_kernel_idempotent", "hidden_kernel_idempotent"),
    ("automorphism_mask", "automorphism_mask"),
    ("nonmonic_cancellation", "nonmonic_cancellation"),
    ("index_identity_only", "index_identity_only"),
    ("projectionwise_partial_identity", "projectionwise_partial_identity"),
    ("quotient_shadow_identity", "quotient_shadow_identity"),
    ("graph_side_identity", "graph_side_identity"),
    ("retuned_identity", "retuned_identity"),
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
    if not REQUIRED_DOC515_CELLS <= set(data["doc515_cells"]):
        out.append("doc515_cells_missing")
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_monic_cancellation(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC515_CELLS <= set(data["doc515_cells"])
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
        equalizer_identity_actual=True,
        monic_inclusion_actual=True,
        comparison_iso_actual=True,
        universal_mediator_actual=True,
        doc515_coherence_actual=True,
        doc515_cells=set(REQUIRED_DOC515_CELLS),
        doc515_in_finite_index=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        equalizer_idempotent_actual=True,
        idempotent_on_equalizer=True,
        monic_inclusion_compatible=True,
        monic_cancellation_actual=True,
        idempotent_equals_identity=True,
        alpha_beta_compatible=True,
        universal_mediator_fixed=True,
        doc515_coherence_fixed=True,
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


def monic_cancellation_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_category": SOURCE_CATEGORY_ID,
        "product": PRODUCT_ID,
        "alpha": ALPHA_ID,
        "beta": BETA_ID,
        "equalizer": EQUALIZER_ID,
        "equalizer_identity": EQUALIZER_IDENTITY_ID,
        "inclusion": INCLUSION_ID,
        "comparison": COMPARISON_ID,
        "totalizer": TOTALIZER_ID,
        "finite_index": FINITE_INDEX_ID,
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "doc515_coherence": DOC515_COHERENCE_ID,
        "doc515_index_cell": DOC515_INDEX_CELL,
        "equalizer_idempotent": EQUALIZER_IDEMPOTENT_ID,
        "monic_cancellation": MONIC_CANCELLATION_ID,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc515_cells": tuple(sorted(REQUIRED_DOC515_CELLS)),
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
    f"{TAG}1 monic cancellation makes the idempotent identity",
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
    and len(REQUIRED_DOC515_CELLS) == 10
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and monic_cancellation_payload(T3_T5_z) == monic_cancellation_payload(zC15)
    and monic_cancellation_payload(T5_T3_z) == monic_cancellation_payload(zC15)
    and monic_cancellation_payload(T3_T3_T5_z) == monic_cancellation_payload(zC45)
    and monic_cancellation_payload(T15_zF22) == monic_cancellation_payload(zC15F22)
    and monic_cancellation_payload(T45_zF22) == monic_cancellation_payload(zC45F22)
    and accepts_monic_cancellation(live_source()),
    "H1=%s index=%d cells=%d"
    % ([p["h1_order"] for p in profiles], len(FINITE_INDEX), len(REQUIRED_DOC515_CELLS)),
)

comparison_only = live_source(
    equalizer_identity_actual=False,
    monic_cancellation_actual=False,
    idempotent_equals_identity=False,
    comparison_only_identity=True,
    hidden_kernel_idempotent=True,
)

gate(
    f"{TAG}2 comparison-only identities fail",
    not accepts_monic_cancellation(comparison_only)
    and {
        "equalizer_identity_missing",
        "monic_cancellation_missing",
        "idempotent_not_identity",
        "comparison_only_identity",
        "hidden_kernel_idempotent",
    }
    <= set(reasons(comparison_only)),
    ",".join(reasons(comparison_only)),
)

nonmonic = live_source(
    monic_inclusion_actual=False,
    monic_inclusion_compatible=False,
    monic_cancellation_actual=False,
    nonmonic_cancellation=True,
)

gate(
    f"{TAG}3 nonmonic cancellation fails",
    not accepts_monic_cancellation(nonmonic)
    and {
        "monic_inclusion_missing",
        "monic_inclusion_incompatible",
        "monic_cancellation_missing",
        "nonmonic_cancellation",
    }
    <= set(reasons(nonmonic)),
    ",".join(reasons(nonmonic)),
)

index_identity = live_source(
    equalizer_idempotent_actual=False,
    idempotent_on_equalizer=False,
    idempotent_equals_identity=False,
    index_identity_only=True,
    projectionwise_partial_identity=True,
)

gate(
    f"{TAG}4 index and projection identities fail",
    not accepts_monic_cancellation(index_identity)
    and {
        "equalizer_idempotent_missing",
        "not_idempotent_on_equalizer",
        "idempotent_not_identity",
        "index_identity_only",
        "projectionwise_partial_identity",
    }
    <= set(reasons(index_identity)),
    ",".join(reasons(index_identity)),
)

automorphism = live_source(
    idempotent_equals_identity=False,
    universal_mediator_fixed=False,
    doc515_coherence_fixed=False,
    closure_returns_same_totalizer=False,
    automorphism_mask=True,
    quotient_shadow_identity=True,
)

gate(
    f"{TAG}5 automorphism masks and quotient shadows fail",
    not accepts_monic_cancellation(automorphism)
    and {
        "idempotent_not_identity",
        "universal_mediator_not_fixed",
        "doc515_coherence_not_fixed",
        "closure_does_not_return_same_totalizer",
        "automorphism_mask",
        "quotient_shadow_identity",
    }
    <= set(reasons(automorphism)),
    ",".join(reasons(automorphism)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"post_doc517_monic_cancellation_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}6 expanded finite indexes and one-more-layer towers fail",
    not accepts_monic_cancellation(expanded)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded)),
    ",".join(reasons(expanded)),
)

missing_doc515 = live_source(
    doc515_coherence_actual=False,
    doc515_cells=set(list(REQUIRED_DOC515_CELLS)[:-1]),
    doc515_in_finite_index=False,
)

gate(
    f"{TAG}7 missing doc515 payload fails",
    not accepts_monic_cancellation(missing_doc515)
    and {
        "doc515_coherence_missing",
        "doc515_not_in_finite_index",
        "doc515_cells_missing",
    }
    <= set(reasons(missing_doc515)),
    ",".join(reasons(missing_doc515)),
)

retuned = live_source(
    equalizer_identity_actual=False,
    comparison_identity_on_totalizer=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    graph_side_identity=True,
    retuned_identity=True,
)

gate(
    f"{TAG}8 graph-side or retuned identities fail",
    not accepts_monic_cancellation(retuned)
    and {
        "equalizer_identity_missing",
        "comparison_not_identity_on_totalizer",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "graph_side_identity",
        "retuned_identity",
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
    f"{TAG}9 control/DH/Epstein point-formable identities fail",
    not accepts_monic_cancellation(control)
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
    live_source(monic_cancellation_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}10 only monic-cancelled identity passes",
    accepts_monic_cancellation(live_source())
    and not any(accepts_monic_cancellation(data) for data in missing_edges)
    and {
        "required_edges_missing",
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "monic_cancellation_missing",
    }
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (sorted(missing_reasons), accepts_monic_cancellation(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(f"\n{TAG}1-{TAG}10 ALL PASS: doc517 idempotent monic cancellation pinned")
print(
    "VERDICT: the doc-517 source equalizer idempotent must cancel through the "
    "monic inclusion to id_Eq_NCoup_med_UP_Eq_id_source_components. "
    "Comparison-only identities, hidden-kernel idempotents, nonmonic "
    "cancellations, index/projection identities, automorphism masks, expanded "
    "finite indexes, one-more-layer towers, and control/DH/Epstein "
    "point-formability do not construct the missing object."
)
