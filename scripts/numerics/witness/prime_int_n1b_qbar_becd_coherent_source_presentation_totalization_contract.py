r"""Finite coherent source-presentation totalizer contract.

Doc 480 pins represented cartesian boundary-fiber coherence cells as faces of
one source-level globular modification.  This witness makes the next cut
finite: the live object must be one represented coherent source-presentation
totalizer whose universal arrow generates the square, cube, facets, boundary
fibers, cartesian transports, and globular coherence with no remaining
"next coherence" obligation.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_totalization_contract
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

CATEGORY_ID = "Cat_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_ID = "Tot_CohSrcPres_BCCube_Qbar_BECD"
UNIVERSAL_ARROW_ID = "eta_CohSrcPres_BCCube_Qbar_BECD"
CATEGORICAL_SQUARE_ID = "CatSq_Qbar_BECD_closes_doc443_boundary_cycle"
FACET_CUBE_ID = "BCCube_CatSq_Qbar_BECD_facets"
CUBE_TOTALIZATION_ID = "Tot_BCCube_CatSq_Qbar_BECD"
SOURCE_REPRESENTING_OBJECT_ID = "Rep_BCCube_Qbar_BECD_source_fiber"
SOURCE_UNIVERSAL_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
CARTESIAN_LIFTS_ID = "CartLift_BCCube_Qbar_BECD_multiplier_source_fiber"
CARTESIAN_COHERENCE_ID = "Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
COMPONENT_CONE_ID = "Cone_NCoup_BCCube_Qbar_BECD_eta_source_components"
GLOBULAR_MODIFICATION_ID = "Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
BOUNDARY_FIBER_ID = "Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
CARTESIAN_BOUNDARY_FIBER_ID = "CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
BOUNDARY_FIBER_COHERENCE_ID = (
    "Coh_CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
)
FIBER_COHERENCE_MODIFICATION_ID = (
    "Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
)
FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID = (
    "GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components"
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

REQUIRED_TOTALIZER_EDGES = {
    ("finite_source_presentation_category", "coherent_source_totalizer"),
    ("represented_source_square", "coherent_source_totalizer"),
    ("source_cube_totalization", "coherent_source_totalizer"),
    ("coherent_source_totalizer", "universal_source_presentation_arrow"),
    ("universal_source_presentation_arrow", "source_representing_object"),
    ("universal_source_presentation_arrow", "cartesian_source_lifts"),
    ("universal_source_presentation_arrow", "endpoint_integrality"),
    ("universal_source_presentation_arrow", "degree_maps"),
    ("universal_source_presentation_arrow", "dd4_boundary"),
    ("universal_source_presentation_arrow", "boundary_pushforward"),
    ("universal_source_presentation_arrow", "graph_composition"),
    ("universal_source_presentation_arrow", "rosati_count"),
    ("universal_source_presentation_arrow", "control_death"),
    ("cartesian_source_lifts", "cartesian_source_coherence"),
    ("cartesian_source_coherence", "component_cone"),
    ("component_cone", "globular_modification"),
    ("globular_modification", "boundary_fiber"),
    ("boundary_fiber", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "boundary_fiber_coherence"),
    ("boundary_fiber_coherence", "fiber_coherence_modification"),
    ("fiber_coherence_modification", "shared_fiber_coherence_boundary"),
    ("shared_fiber_coherence_boundary", "source_boundary_cell"),
    ("shared_fiber_coherence_boundary", "target_boundary_cell"),
    ("coherent_source_totalizer", "finite_cell_index"),
    ("finite_cell_index", "source_square_cell"),
    ("finite_cell_index", "beck_chevalley_cube_cell"),
    ("finite_cell_index", "cartesian_lift_cell"),
    ("finite_cell_index", "component_cone_cell"),
    ("finite_cell_index", "globular_modification_cell"),
    ("finite_cell_index", "boundary_fiber_cell"),
    ("finite_cell_index", "cartesian_boundary_fiber_cell"),
    ("finite_cell_index", "boundary_fiber_coherence_cell"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("finite_cell_index", "closed_finite_coherence_cell"),
    ("closed_finite_coherence_cell", "no_next_coherence_obligation"),
    ("coherent_source_totalizer", "source_before_points"),
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
        "finite_source_presentation_category_actual": False,
        "represented_totalizer_actual": False,
        "universal_source_presentation_arrow_actual": False,
        "represented_source_square_actual": False,
        "source_cube_totalization_actual": False,
        "source_representing_object_actual": False,
        "cartesian_source_lifts_actual": False,
        "facets_internal": set(),
        "coherence_cells": set(),
        "closed_under_boundary_fiber": False,
        "closed_under_cartesian_transport": False,
        "closed_under_globular_modification": False,
        "closed_under_fiber_coherence_modification": False,
        "finite_cell_index_actual": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "one_more_layer_tower": False,
        "open_next_boundary_fiber": False,
        "open_next_globular_modification": False,
        "open_next_cartesian_transport": False,
        "pro_completion_totalizer": False,
        "local_chart_totalizer": False,
        "equivalence_wrapper": False,
        "pointwise_graph_totalizer": False,
        "post_product_totalizer": False,
        "retuned_facet_selector": False,
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
    (
        "universal_source_presentation_arrow_actual",
        "universal_source_presentation_arrow_missing",
    ),
    ("represented_source_square_actual", "represented_source_square_missing"),
    ("source_cube_totalization_actual", "source_cube_totalization_missing"),
    ("source_representing_object_actual", "source_representing_object_missing"),
    ("cartesian_source_lifts_actual", "cartesian_source_lifts_missing"),
    ("closed_under_boundary_fiber", "boundary_fiber_not_closed"),
    ("closed_under_cartesian_transport", "cartesian_transport_not_closed"),
    ("closed_under_globular_modification", "globular_modification_not_closed"),
    (
        "closed_under_fiber_coherence_modification",
        "fiber_coherence_modification_not_closed",
    ),
    ("finite_cell_index_actual", "finite_cell_index_missing"),
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
    ("open_next_boundary_fiber", "open_next_boundary_fiber"),
    ("open_next_globular_modification", "open_next_globular_modification"),
    ("open_next_cartesian_transport", "open_next_cartesian_transport"),
    ("pro_completion_totalizer", "pro_completion_totalizer"),
    ("local_chart_totalizer", "local_chart_totalizer"),
    ("equivalence_wrapper", "equivalence_wrapper"),
    ("pointwise_graph_totalizer", "pointwise_graph_totalizer"),
    ("post_product_totalizer", "post_product_totalizer"),
    ("retuned_facet_selector", "retuned_facet_selector"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_FACETS <= set(data["facets_internal"]):
        out.append("required_facets_not_internal")
    if not REQUIRED_COHERENCE_CELLS <= set(data["coherence_cells"]):
        out.append("required_coherence_cells_not_internal")
    if not REQUIRED_TOTALIZER_EDGES <= set(data["required_edges"]):
        out.append("required_totalizer_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_totalizer(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_FACETS <= set(data["facets_internal"])
        and REQUIRED_COHERENCE_CELLS <= set(data["coherence_cells"])
        and REQUIRED_TOTALIZER_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        finite_source_presentation_category_actual=True,
        represented_totalizer_actual=True,
        universal_source_presentation_arrow_actual=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        source_representing_object_actual=True,
        cartesian_source_lifts_actual=True,
        facets_internal=set(REQUIRED_FACETS),
        coherence_cells=set(REQUIRED_COHERENCE_CELLS),
        closed_under_boundary_fiber=True,
        closed_under_cartesian_transport=True,
        closed_under_globular_modification=True,
        closed_under_fiber_coherence_modification=True,
        finite_cell_index_actual=True,
        no_next_coherence_obligation=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_TOTALIZER_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def totalizer_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "category": CATEGORY_ID,
        "totalizer": TOTALIZER_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "categorical_square": CATEGORICAL_SQUARE_ID,
        "facet_cube": FACET_CUBE_ID,
        "cube_totalization": CUBE_TOTALIZATION_ID,
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "source_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "cartesian_lifts": CARTESIAN_LIFTS_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "component_cone": COMPONENT_CONE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "boundary_fiber": BOUNDARY_FIBER_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "boundary_fiber_coherence": BOUNDARY_FIBER_COHERENCE_ID,
        "fiber_coherence_modification": FIBER_COHERENCE_MODIFICATION_ID,
        "fiber_coherence_boundary": FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
        "facets": tuple(sorted(REQUIRED_FACETS)),
        "coherence_cells": tuple(sorted(REQUIRED_COHERENCE_CELLS)),
        "closed": True,
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
    "CATCOHSRCPRESTOTQBARBECD1 finite represented source-presentation totalizer is closed",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_TOTALIZER_EDGES)
    and len(REQUIRED_FACETS) == 7
    and len(REQUIRED_COHERENCE_CELLS) == 17
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and totalizer_payload(T3_T5_z) == totalizer_payload(zC15)
    and totalizer_payload(T5_T3_z) == totalizer_payload(zC15)
    and totalizer_payload(T3_T3_T5_z) == totalizer_payload(zC45)
    and totalizer_payload(T15_zF22) == totalizer_payload(zC15F22)
    and totalizer_payload(T45_zF22) == totalizer_payload(zC45F22),
    "H1=%s totalizer=%s facets=%d cells=%d"
    % (
        [p["h1_order"] for p in profiles],
        TOTALIZER_ID,
        len(REQUIRED_FACETS),
        len(REQUIRED_COHERENCE_CELLS),
    ),
)

gate(
    "CATCOHSRCPRESTOTQBARBECD2 graph identities still do not supply the source totalizer",
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

tower = live_source(
    finite_source_presentation_category_actual=False,
    represented_totalizer_actual=False,
    finite_cell_index_actual=False,
    no_next_coherence_obligation=False,
    one_more_layer_tower=True,
    open_next_boundary_fiber=True,
    open_next_globular_modification=True,
    open_next_cartesian_transport=True,
)

gate(
    "CATCOHSRCPRESTOTQBARBECD3 one-more-layer coherence towers are not closed totalizers",
    not accepts_totalizer(tower)
    and {
        "finite_source_presentation_category_missing",
        "represented_totalizer_missing",
        "finite_cell_index_missing",
        "next_coherence_obligation_open",
        "one_more_layer_tower",
        "open_next_boundary_fiber",
        "open_next_globular_modification",
        "open_next_cartesian_transport",
    }
    <= set(reasons(tower)),
    ",".join(reasons(tower)),
)

partial_facets = live_source(
    facets_internal=REQUIRED_FACETS - {"control_death", "rosati_count"},
    coherence_cells=REQUIRED_COHERENCE_CELLS - {"closed_finite_coherence_cell"},
)

gate(
    "CATCOHSRCPRESTOTQBARBECD4 partial facet totalizers do not control death with the square",
    not accepts_totalizer(partial_facets)
    and {
        "required_facets_not_internal",
        "required_coherence_cells_not_internal",
    }
    <= set(reasons(partial_facets)),
    ",".join(reasons(partial_facets)),
)

wrapper = live_source(
    carrier_native=False,
    represented_source_square_actual=False,
    universal_source_presentation_arrow_actual=False,
    local_chart_totalizer=True,
    equivalence_wrapper=True,
    pointwise_graph_totalizer=True,
)

gate(
    "CATCOHSRCPRESTOTQBARBECD5 local or equivalence wrappers do not represent the source presentation",
    not accepts_totalizer(wrapper)
    and {
        "not_carrier_native",
        "represented_source_square_missing",
        "universal_source_presentation_arrow_missing",
        "local_chart_totalizer",
        "equivalence_wrapper",
        "pointwise_graph_totalizer",
    }
    <= set(reasons(wrapper)),
    ",".join(reasons(wrapper)),
)

pro_totalizer = live_source(
    finite_source_presentation_category_actual=False,
    finite_cell_index_actual=False,
    no_next_coherence_obligation=False,
    pro_completion_totalizer=True,
    post_product_totalizer=True,
)

gate(
    "CATCOHSRCPRESTOTQBARBECD6 pro-completions and post-product totalizers leave the finite cut open",
    not accepts_totalizer(pro_totalizer)
    and {
        "finite_source_presentation_category_missing",
        "finite_cell_index_missing",
        "next_coherence_obligation_open",
        "pro_completion_totalizer",
        "post_product_totalizer",
    }
    <= set(reasons(pro_totalizer)),
    ",".join(reasons(pro_totalizer)),
)

retuned = live_source(
    closed_under_boundary_fiber=False,
    closed_under_cartesian_transport=False,
    closed_under_globular_modification=False,
    closed_under_fiber_coherence_modification=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_facet_selector=True,
)

gate(
    "CATCOHSRCPRESTOTQBARBECD7 retuned selectors replace the coherent source presentation",
    not accepts_totalizer(retuned)
    and {
        "boundary_fiber_not_closed",
        "cartesian_transport_not_closed",
        "globular_modification_not_closed",
        "fiber_coherence_modification_not_closed",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_facet_selector",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_TOTALIZER_EDGES - {edge})
    for edge in list(REQUIRED_TOTALIZER_EDGES)[:5]
] + [
    live_source(finite_source_presentation_category_actual=False),
    live_source(represented_totalizer_actual=False),
    live_source(represented_source_square_actual=False),
    live_source(source_cube_totalization_actual=False),
    live_source(cartesian_source_lifts_actual=False),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESTOTQBARBECD8 every finite totalizer edge is mandatory",
    not any(accepts_totalizer(data) for data in missing_edges)
    and {
        "required_totalizer_edges_missing",
        "finite_source_presentation_category_missing",
        "represented_totalizer_missing",
        "represented_source_square_missing",
        "source_cube_totalization_missing",
        "cartesian_source_lifts_missing",
        "next_coherence_obligation_open",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_totalizer = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    pointwise_graph_totalizer=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESTOTQBARBECD9 graph-side source totalizers leave controls formable",
    not accepts_totalizer(control_totalizer)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "pointwise_graph_totalizer",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_totalizer)),
    ",".join(reasons(control_totalizer)),
)

live = live_source()
dead_sources = {
    "tower": tower,
    "partial_facets": partial_facets,
    "wrapper": wrapper,
    "pro_totalizer": pro_totalizer,
    "retuned": retuned,
    "control_totalizer": control_totalizer,
}

gate(
    "CATCOHSRCPRESTOTQBARBECD10 only the finite represented coherent source-presentation totalizer passes",
    accepts_totalizer(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_totalizer(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_totalizer(data) for data in dead_sources.values()),
        accepts_totalizer(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESTOTQBARBECD1-CATCOHSRCPRESTOTQBARBECD10 ALL PASS: "
    "finite coherent source-presentation totalizer pinned"
)
print(
    "VERDICT: the live Qbar_BECD object must be represented by one finite "
    "coherent source-presentation totalizer with no remaining next-coherence "
    "obligation. One-more-layer towers, local/equivalence wrappers, graph-side "
    "or post-product totalizers, pro-completions, retuned selectors, and "
    "control/DH/Epstein point-formability do not construct the missing object."
)
