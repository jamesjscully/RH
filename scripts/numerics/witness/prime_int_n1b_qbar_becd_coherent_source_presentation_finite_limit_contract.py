r"""Finite-limit realization contract for the coherent source presentation.

Doc 481 requires a finite represented coherent source-presentation totalizer.
This witness pins the next edge: that totalizer must be realized as an
internal finite-limit/equalizer object in the existing source category.  A
declared totalizer, free presentation category, syntax quotient, external
limit, or post-hoc graph-side equalizer does not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_finite_limit_contract
"""

from __future__ import annotations

from math import comb

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []

SOURCE_CATEGORY_ID = "SrcCat_BCCube_Qbar_BECD"
TOTALIZER_ID = "Tot_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_ARROW_ID = "eta_CohSrcPres_BCCube_Qbar_BECD"
FINITE_PRODUCT_ID = "Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells"
ALPHA_ID = "alpha_CohSrcPres_BCCube_Qbar_BECD_constraints"
BETA_ID = "beta_CohSrcPres_BCCube_Qbar_BECD_constraints"
EQUALIZER_ID = "Eq_CohSrcPres_BCCube_Qbar_BECD"
EQUALIZER_MONIC_ID = "incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"
COMPARISON_ID = "cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"

REQUIRED_FACETS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

REQUIRED_COHERENCE_CELLS = (
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
)

REQUIRED_PROJECTIONS = tuple(
    f"pi_CohSrcPres_BCCube_Qbar_BECD_{name}"
    for name in (*REQUIRED_FACETS, *REQUIRED_COHERENCE_CELLS)
)

REQUIRED_LIMIT_EDGES = {
    ("existing_source_category", "finite_product_object"),
    ("finite_product_object", "source_native_projections"),
    ("source_native_projections", "seven_facets"),
    ("source_native_projections", "seventeen_coherence_cells"),
    ("finite_product_object", "alpha_constraints"),
    ("finite_product_object", "beta_constraints"),
    ("alpha_constraints", "equalizer_object"),
    ("beta_constraints", "equalizer_object"),
    ("equalizer_object", "equalizer_monic"),
    ("equalizer_monic", "coherent_source_totalizer"),
    ("equalizer_object", "comparison_to_totalizer"),
    ("comparison_to_totalizer", "comparison_isomorphism"),
    ("comparison_isomorphism", "universal_source_presentation_arrow"),
    ("universal_source_presentation_arrow", "finite_source_facets"),
    ("universal_source_presentation_arrow", "finite_coherence_cells"),
    ("finite_source_facets", "endpoint_integrality"),
    ("finite_source_facets", "degree_maps"),
    ("finite_source_facets", "dd4_boundary"),
    ("finite_source_facets", "boundary_pushforward"),
    ("finite_source_facets", "graph_composition"),
    ("finite_source_facets", "rosati_count"),
    ("finite_source_facets", "control_death"),
    ("finite_coherence_cells", "closed_finite_coherence_cell"),
    ("closed_finite_coherence_cell", "no_next_coherence_obligation"),
    ("equalizer_object", "coherence_preserves_coefficients"),
    ("equalizer_object", "coherence_preserves_signed_support"),
    ("equalizer_object", "source_before_points"),
    ("source_before_points", "controls_not_points"),
    ("source_before_points", "dh_not_points"),
    ("source_before_points", "epstein_not_points"),
}

Corr = tuple[float, np.ndarray, float]


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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "h1_order": z1_order // len(coboundaries),
        "coboundaries_res1_zero": all(
            from_vec(v).get(1, 0) == 0 for v in coboundaries
        ),
    }


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta_corr(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph_corr(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(
        compose(graph_corr(F, q, m), graph_corr(F, q, n)),
        graph_corr(F, q, m + n),
    )


def anti_defect(A: Corr, B: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(compose(A, B), E), compose(dagger(B, E), dagger(A, E)))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def projection_sides(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> tuple[float, float]:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs, rhs = projection_sides(A, B, C, E)
    return abs(lhs - rhs)


def retune_first_degree_for_projection(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> Corr:
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    return corr(product[0] + (rhs - lhs) / C[2], product[1], product[2])


def trace_power(F: np.ndarray, n: int) -> float:
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - trace_power(F, n))


def formal_graph_signature(F: np.ndarray, E: np.ndarray, q: float) -> tuple[bool, bool, bool]:
    G = graph_corr(F, q, 1)
    H = graph_corr(F, q, 2)
    return (
        graph_law_defect(F, q, 1, 2) < 1e-12,
        qsim_defect(F, E, q) < 1e-12,
        anti_defect(G, H, E) < 1e-12,
    )


def graph_connected(edges: set[tuple[str, str]]) -> bool:
    nodes = {node for edge in edges for node in edge}
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
        "doc481_totalizer_actual": False,
        "finite_limit_in_existing_source": False,
        "finite_product_object_actual": False,
        "source_native_projections_actual": False,
        "parallel_constraint_maps_actual": False,
        "equalizer_object_actual": False,
        "equalizer_monic_actual": False,
        "comparison_to_totalizer_actual": False,
        "comparison_isomorphism_actual": False,
        "universal_property_actual": False,
        "facets_internal": set(),
        "coherence_cells_internal": set(),
        "projection_names": set(),
        "required_edges": set(),
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "declared_totalizer": False,
        "free_presentation_category": False,
        "syntax_only_limit": False,
        "external_limit": False,
        "posthoc_equalizer": False,
        "graph_side_limit": False,
        "pointwise_limit": False,
        "pro_limit": False,
        "retuned_comparison": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc481_totalizer_actual", "doc481_totalizer_missing"),
    ("finite_limit_in_existing_source", "finite_limit_not_in_existing_source"),
    ("finite_product_object_actual", "finite_product_object_missing"),
    ("source_native_projections_actual", "source_native_projections_missing"),
    ("parallel_constraint_maps_actual", "parallel_constraint_maps_missing"),
    ("equalizer_object_actual", "equalizer_object_missing"),
    ("equalizer_monic_actual", "equalizer_monic_missing"),
    ("comparison_to_totalizer_actual", "comparison_to_totalizer_missing"),
    ("comparison_isomorphism_actual", "comparison_isomorphism_missing"),
    ("universal_property_actual", "universal_property_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("declared_totalizer", "declared_totalizer"),
    ("free_presentation_category", "free_presentation_category"),
    ("syntax_only_limit", "syntax_only_limit"),
    ("external_limit", "external_limit"),
    ("posthoc_equalizer", "posthoc_equalizer"),
    ("graph_side_limit", "graph_side_limit"),
    ("pointwise_limit", "pointwise_limit"),
    ("pro_limit", "pro_limit"),
    ("retuned_comparison", "retuned_comparison"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(REQUIRED_FACETS) - set(data["facets_internal"]):
        out.append("required_facets_not_internal")
    if set(REQUIRED_COHERENCE_CELLS) - set(data["coherence_cells_internal"]):
        out.append("required_coherence_cells_not_internal")
    if set(REQUIRED_PROJECTIONS) - set(data["projection_names"]):
        out.append("required_projections_missing")
    if REQUIRED_LIMIT_EDGES - set(data["required_edges"]):
        out.append("required_limit_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_finite_limit(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_FACETS) <= set(data["facets_internal"])
        and set(REQUIRED_COHERENCE_CELLS) <= set(data["coherence_cells_internal"])
        and set(REQUIRED_PROJECTIONS) <= set(data["projection_names"])
        and REQUIRED_LIMIT_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc481_totalizer_actual=True,
        finite_limit_in_existing_source=True,
        finite_product_object_actual=True,
        source_native_projections_actual=True,
        parallel_constraint_maps_actual=True,
        equalizer_object_actual=True,
        equalizer_monic_actual=True,
        comparison_to_totalizer_actual=True,
        comparison_isomorphism_actual=True,
        universal_property_actual=True,
        facets_internal=set(REQUIRED_FACETS),
        coherence_cells_internal=set(REQUIRED_COHERENCE_CELLS),
        projection_names=set(REQUIRED_PROJECTIONS),
        required_edges=set(REQUIRED_LIMIT_EDGES),
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def finite_limit_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_category": SOURCE_CATEGORY_ID,
        "totalizer": TOTALIZER_ID,
        "totalizer_arrow": TOTALIZER_ARROW_ID,
        "product": FINITE_PRODUCT_ID,
        "alpha": ALPHA_ID,
        "beta": BETA_ID,
        "equalizer": EQUALIZER_ID,
        "monic": EQUALIZER_MONIC_ID,
        "comparison": COMPARISON_ID,
        "facets": REQUIRED_FACETS,
        "cells": REQUIRED_COHERENCE_CELLS,
        "projections": REQUIRED_PROJECTIONS,
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

q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta_corr(F_true)
G_true = graph_corr(F_true, q_true, 1)
H_true = graph_corr(F_true, q_true, 2)
true_signature = formal_graph_signature(F_true, E_true, q_true)
true_hodge = primitive_hodge_index(F_true, E_true, 1)
true_count_defects = [
    abs(ns_intersection(D_true, graph_corr(F_true, q_true, n)) - point_count(F_true, q_true, n))
    for n in (1, 2, 3)
]
true_anti = anti_defect(G_true, H_true, E_true)

control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_D = delta_corr(control)
control_G = graph_corr(control, control_q, 1)
control_signature = formal_graph_signature(control, control_E, control_q)
control_hodge = primitive_hodge_index(control, control_E, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(
    control_G, control_D, control_G, control_E
)

gate(
    "CATCOHSRCPRESLIMQBARBECD1 finite source-presentation totalizer is an internal equalizer",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_LIMIT_EDGES)
    and len(REQUIRED_FACETS) == 7
    and len(REQUIRED_COHERENCE_CELLS) == 17
    and len(REQUIRED_PROJECTIONS) == 24
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and finite_limit_payload(T3_T5_z) == finite_limit_payload(zC15)
    and finite_limit_payload(T5_T3_z) == finite_limit_payload(zC15)
    and finite_limit_payload(T3_T3_T5_z) == finite_limit_payload(zC45)
    and finite_limit_payload(T15_zF22) == finite_limit_payload(zC15F22)
    and finite_limit_payload(T45_zF22) == finite_limit_payload(zC45F22),
    "H1=%s equalizer=%s projections=%d"
    % ([p["h1_order"] for p in profiles], EQUALIZER_ID, len(REQUIRED_PROJECTIONS)),
)

gate(
    "CATCOHSRCPRESLIMQBARBECD2 graph identities still do not supply the finite limit",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and control_retuned[0] == 27.0,
    "true_sig=%s control_sig=%s true_H=%.3f control_H=%.3f proj=%.1f retuned_d1=%.1f"
    % (
        true_signature,
        control_signature,
        true_hodge,
        control_hodge,
        control_projection,
        control_retuned[0],
    ),
)

declared = live_source(
    finite_limit_in_existing_source=False,
    finite_product_object_actual=False,
    parallel_constraint_maps_actual=False,
    equalizer_object_actual=False,
    declared_totalizer=True,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD3 declared totalizers without source limits fail",
    not accepts_finite_limit(declared)
    and {
        "finite_limit_not_in_existing_source",
        "finite_product_object_missing",
        "parallel_constraint_maps_missing",
        "equalizer_object_missing",
        "declared_totalizer",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)

free_syntax = live_source(
    carrier_native=False,
    source_native_projections_actual=False,
    free_presentation_category=True,
    syntax_only_limit=True,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD4 free presentation or syntax limits are external",
    not accepts_finite_limit(free_syntax)
    and {
        "not_carrier_native",
        "source_native_projections_missing",
        "free_presentation_category",
        "syntax_only_limit",
    }
    <= set(reasons(free_syntax)),
    ",".join(reasons(free_syntax)),
)

missing_product = live_source(
    facets_internal=set(REQUIRED_FACETS) - {"control_death"},
    coherence_cells_internal=set(REQUIRED_COHERENCE_CELLS) - {"closed_finite_coherence_cell"},
    projection_names=set(REQUIRED_PROJECTIONS[:-2]),
    finite_product_object_actual=False,
    source_native_projections_actual=False,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD5 product and all source-native projections are mandatory",
    not accepts_finite_limit(missing_product)
    and {
        "finite_product_object_missing",
        "source_native_projections_missing",
        "required_facets_not_internal",
        "required_coherence_cells_not_internal",
        "required_projections_missing",
    }
    <= set(reasons(missing_product)),
    ",".join(reasons(missing_product)),
)

missing_equalizer = live_source(
    equalizer_object_actual=False,
    equalizer_monic_actual=False,
    comparison_to_totalizer_actual=False,
    comparison_isomorphism_actual=False,
    universal_property_actual=False,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD6 equalizer, monic, comparison, and universal property are mandatory",
    not accepts_finite_limit(missing_equalizer)
    and {
        "equalizer_object_missing",
        "equalizer_monic_missing",
        "comparison_to_totalizer_missing",
        "comparison_isomorphism_missing",
        "universal_property_missing",
    }
    <= set(reasons(missing_equalizer)),
    ",".join(reasons(missing_equalizer)),
)

external = live_source(
    finite_limit_in_existing_source=False,
    external_limit=True,
    posthoc_equalizer=True,
    graph_side_limit=True,
    pointwise_limit=True,
    pro_limit=True,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD7 external or posthoc limits do not realize the source totalizer",
    not accepts_finite_limit(external)
    and {
        "finite_limit_not_in_existing_source",
        "external_limit",
        "posthoc_equalizer",
        "graph_side_limit",
        "pointwise_limit",
        "pro_limit",
    }
    <= set(reasons(external)),
    ",".join(reasons(external)),
)

retuned = live_source(
    comparison_isomorphism_actual=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_comparison=True,
)

gate(
    "CATCOHSRCPRESLIMQBARBECD8 retuned comparisons change the finite-limit object",
    not accepts_finite_limit(retuned)
    and {
        "comparison_isomorphism_missing",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_comparison",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_LIMIT_EDGES - {edge})
    for edge in list(REQUIRED_LIMIT_EDGES)[:5]
] + [
    live_source(finite_limit_in_existing_source=False),
    live_source(finite_product_object_actual=False),
    live_source(parallel_constraint_maps_actual=False),
    live_source(equalizer_object_actual=False),
    live_source(comparison_isomorphism_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESLIMQBARBECD9 every finite-limit edge is mandatory",
    not any(accepts_finite_limit(data) for data in missing_edges)
    and {
        "required_limit_edges_missing",
        "finite_limit_not_in_existing_source",
        "finite_product_object_missing",
        "parallel_constraint_maps_missing",
        "equalizer_object_missing",
        "comparison_isomorphism_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_limit = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_limit=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

live = live_source()
dead_sources = {
    "declared": declared,
    "free_syntax": free_syntax,
    "missing_product": missing_product,
    "missing_equalizer": missing_equalizer,
    "external": external,
    "retuned": retuned,
    "control_limit": control_limit,
}

gate(
    "CATCOHSRCPRESLIMQBARBECD10 only the internal finite-limit realization passes",
    accepts_finite_limit(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_finite_limit(data) for data in dead_sources.values())
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_limit",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_limit)),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_finite_limit(data) for data in dead_sources.values()),
        accepts_finite_limit(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESLIMQBARBECD1-CATCOHSRCPRESLIMQBARBECD10 ALL PASS: "
    "coherent source-presentation finite-limit realization pinned"
)
print(
    "VERDICT: the finite coherent source-presentation totalizer must be "
    "realized as an internal source finite limit: product, source-native "
    "projections, parallel constraints, equalizer, monic inclusion, and "
    "comparison isomorphism. Declared/free/syntax/external/posthoc/graph-side "
    "limits and retuned comparisons do not construct the missing object."
)
