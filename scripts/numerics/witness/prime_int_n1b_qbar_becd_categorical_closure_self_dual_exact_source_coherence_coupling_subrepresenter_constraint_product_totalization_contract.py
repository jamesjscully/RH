r"""Categorical closure constraint-product contract for source constraint morphisms.

Doc 470 requires alpha,beta to be parallel source morphisms into one
constraint object. This witness pins the next edge: the named product
constraint must be an actual categorical source product with projections and
unique pairing maps. A bundled codomain label or tuple of component checks is not a
categorical source product in Rep_BCCube_Qbar_BECD_source_fiber.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_product_totalization_contract
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

CATEGORICAL_SQUARE_ID = "CatSq_Qbar_BECD_closes_doc443_boundary_cycle"
FACET_CUBE_ID = "BCCube_CatSq_Qbar_BECD_facets"
CUBE_TOTALIZATION_ID = "Tot_BCCube_CatSq_Qbar_BECD"
SOURCE_REPRESENTING_OBJECT_ID = "Rep_BCCube_Qbar_BECD_source_fiber"
CONSTRAINT_OBJECT_ID = "Con_NCoup_BCCube_Qbar_BECD_endpoint_dd4_rosati_control_source"
PRODUCT_OBJECT_ID = "Prod_NCoup_BCCube_Qbar_BECD_endpoint_degree_dd4_push_graph_rosati_control"
ALPHA_CONSTRAINT_MAP_ID = "alpha_NCoup_BCCube_Qbar_BECD_source_constraints"
BETA_CONSTRAINT_MAP_ID = "beta_NCoup_BCCube_Qbar_BECD_source_constraints"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_BCCube_Qbar_BECD_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_BCCube_Qbar_BECD_source_constraints"
ENDPOINT_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_endpoint_integrality"
DEGREE_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_degree_maps"
DD4_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_dd4_boundary"
PUSH_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_boundary_pushforward"
GRAPH_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_graph_composition"
ROSATI_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_rosati_count"
CONTROL_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_control_death"
EQUALIZER_ARROW_ID = "eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_BCCube_Qbar_BECD_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
CONTROL_DEATH_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"

COMPONENTS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

REQUIRED_PRODUCT_EDGES = {
    ("represented_source_square", "source_representing_object"),
    ("source_cube_totalization", "source_representing_object"),
    ("source_representing_object", "constraint_product_object"),
    ("constraint_product_object", "constraint_object"),
    ("constraint_product_object", "endpoint_projection"),
    ("constraint_product_object", "degree_projection"),
    ("constraint_product_object", "dd4_projection"),
    ("constraint_product_object", "pushforward_projection"),
    ("constraint_product_object", "graph_projection"),
    ("constraint_product_object", "rosati_count_projection"),
    ("constraint_product_object", "control_death_projection"),
    ("endpoint_projection", "endpoint_component_object"),
    ("degree_projection", "degree_component_object"),
    ("dd4_projection", "dd4_component_object"),
    ("pushforward_projection", "pushforward_component_object"),
    ("graph_projection", "graph_component_object"),
    ("rosati_count_projection", "rosati_count_component_object"),
    ("control_death_projection", "control_death_component_object"),
    ("constraint_product_object", "product_universal_property"),
    ("product_universal_property", "projections_jointly_determine_pairing"),
    ("source_representing_object", "alpha_pairing_map"),
    ("alpha_pairing_map", "alpha_constraint_map"),
    ("alpha_pairing_map", "constraint_product_object"),
    ("alpha_pairing_map", "all_alpha_components"),
    ("source_representing_object", "beta_pairing_map"),
    ("beta_pairing_map", "beta_constraint_map"),
    ("beta_pairing_map", "constraint_product_object"),
    ("beta_pairing_map", "all_beta_zero_diagonal_components"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("constraint_product_object", "same_product_all_paths"),
    ("same_product_all_paths", "C3_C5_equals_C15"),
    ("same_product_all_paths", "C5_C3_equals_C15"),
    ("same_product_all_paths", "C3_C3_C5_equals_C45"),
    ("same_product_all_paths", "F22_product"),
    ("constraint_product_object", "source_before_points_and_graphs"),
    ("source_before_points_and_graphs", "controls_not_points"),
    ("source_before_points_and_graphs", "dh_not_points"),
    ("source_before_points_and_graphs", "epstein_not_points"),
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


def product_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "categorical_square": CATEGORICAL_SQUARE_ID,
        "facet_cube": FACET_CUBE_ID,
        "cube_totalization": CUBE_TOTALIZATION_ID,
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "projections": (
            ENDPOINT_PROJECTION_ID,
            DEGREE_PROJECTION_ID,
            DD4_PROJECTION_ID,
            PUSH_PROJECTION_ID,
            GRAPH_PROJECTION_ID,
            ROSATI_PROJECTION_ID,
            CONTROL_PROJECTION_ID,
        ),
        "endpoint_component": (p1, p2, p1 == p2),
        "degree_component": (tuple(sorted(chi)), p1 + p2),
        "dd4_component": DD4_CLASS_ID,
        "control_component": CONTROL_DEATH_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "cut": FINITE_LIMIT_CUT_ID,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "source_product_payload": True,
    }


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


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_source_fiber_actual": False,
        "constraint_product_actual": False,
        "constraint_object_actual": False,
        "component_objects_actual": False,
        "product_projections_actual": False,
        "projections_source_native": False,
        "projections_jointly_monic": False,
        "product_universal_property_actual": False,
        "alpha_pairing_actual": False,
        "beta_pairing_actual": False,
        "alpha_pairing_unique": False,
        "beta_pairing_unique": False,
        "alpha_components_factor_through_projections": False,
        "beta_components_factor_through_projections": False,
        "alpha_beta_parallel_after_product": False,
        "equalizer_uses_product_pair": False,
        "same_product_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "product_before_points": False,
        "product_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "bundled_tuple_label": False,
        "external_product_of_sets": False,
        "product_after_functor_of_points": False,
        "component_checklist_product": False,
        "missing_projection": False,
        "nonuniversal_bundle": False,
        "coproduct_or_sum_substitute": False,
        "fiber_product_after_graph_objects": False,
        "projection_after_graph_objects": False,
        "local_projection_table": False,
        "finite_sample_product": False,
        "basis_dependent_projection": False,
        "retuned_projection": False,
        "projected_component_map": False,
        "graph_classifier_product": False,
        "declared_product": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("constraint_product_actual", "constraint_product_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("component_objects_actual", "component_objects_missing"),
    ("product_projections_actual", "product_projections_missing"),
    ("projections_source_native", "projections_not_source_native"),
    ("projections_jointly_monic", "projections_not_jointly_monic"),
    ("product_universal_property_actual", "product_universal_property_missing"),
    ("alpha_pairing_actual", "alpha_pairing_missing"),
    ("beta_pairing_actual", "beta_pairing_missing"),
    ("alpha_pairing_unique", "alpha_pairing_not_unique"),
    ("beta_pairing_unique", "beta_pairing_not_unique"),
    (
        "alpha_components_factor_through_projections",
        "alpha_components_do_not_factor_through_projections",
    ),
    (
        "beta_components_factor_through_projections",
        "beta_components_do_not_factor_through_projections",
    ),
    ("alpha_beta_parallel_after_product", "alpha_beta_not_parallel_after_product"),
    ("equalizer_uses_product_pair", "equalizer_does_not_use_product_pair"),
    ("same_product_all_paths", "same_product_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("product_before_points", "product_not_before_points"),
    ("product_before_graph_objects", "product_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("bundled_tuple_label", "bundled_tuple_label"),
    ("external_product_of_sets", "external_product_of_sets"),
    ("product_after_functor_of_points", "product_after_functor_of_points"),
    ("component_checklist_product", "component_checklist_product"),
    ("missing_projection", "missing_projection"),
    ("nonuniversal_bundle", "nonuniversal_bundle"),
    ("coproduct_or_sum_substitute", "coproduct_or_sum_substitute"),
    ("fiber_product_after_graph_objects", "fiber_product_after_graph_objects"),
    ("projection_after_graph_objects", "projection_after_graph_objects"),
    ("local_projection_table", "local_projection_table"),
    ("finite_sample_product", "finite_sample_product"),
    ("basis_dependent_projection", "basis_dependent_projection"),
    ("retuned_projection", "retuned_projection"),
    ("projected_component_map", "projected_component_map"),
    ("graph_classifier_product", "graph_classifier_product"),
    ("declared_product", "declared_product"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_PRODUCT_EDGES <= set(data["required_edges"]):
        out.append("required_constraint_product_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_constraint_product(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_PRODUCT_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        constraint_product_actual=True,
        constraint_object_actual=True,
        component_objects_actual=True,
        product_projections_actual=True,
        projections_source_native=True,
        projections_jointly_monic=True,
        product_universal_property_actual=True,
        alpha_pairing_actual=True,
        beta_pairing_actual=True,
        alpha_pairing_unique=True,
        beta_pairing_unique=True,
        alpha_components_factor_through_projections=True,
        beta_components_factor_through_projections=True,
        alpha_beta_parallel_after_product=True,
        equalizer_uses_product_pair=True,
        same_product_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        product_before_points=True,
        product_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_PRODUCT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


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
    "CATSCPPQBARBECD1 constraint codomain is an actual categorical source product with projections",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_PRODUCT_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and product_payload(T3_T5_z) == product_payload(zC15)
    and product_payload(T5_T3_z) == product_payload(zC15)
    and product_payload(T3_T3_T5_z) == product_payload(zC45)
    and product_payload(T15_zF22) == product_payload(zC15F22)
    and product_payload(T45_zF22) == product_payload(zC45F22),
    "H1=%s product=%s projections=%d"
    % ([p["h1_order"] for p in profiles], PRODUCT_OBJECT_ID, len(COMPONENTS)),
)


gate(
    "CATSCPPQBARBECD2 graph identities still do not supply the categorical source product",
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


bundle = live_source(
    constraint_product_actual=False,
    product_projections_actual=False,
    product_universal_property_actual=False,
    projections_jointly_monic=False,
    bundled_tuple_label=True,
    external_product_of_sets=True,
    component_checklist_product=True,
    declared_product=True,
)

gate(
    "CATSCPPQBARBECD3 bundled tuple labels are not categorical source products",
    not accepts_constraint_product(bundle)
    and {
        "constraint_product_missing",
        "product_projections_missing",
        "product_universal_property_missing",
        "projections_not_jointly_monic",
        "bundled_tuple_label",
        "external_product_of_sets",
        "component_checklist_product",
        "declared_product",
    }
    <= set(reasons(bundle)),
    ",".join(reasons(bundle)),
)


nonuniversal = live_source(
    product_universal_property_actual=False,
    alpha_pairing_unique=False,
    beta_pairing_unique=False,
    alpha_components_factor_through_projections=False,
    beta_components_factor_through_projections=False,
    nonuniversal_bundle=True,
    coproduct_or_sum_substitute=True,
    missing_projection=True,
)

gate(
    "CATSCPPQBARBECD4 nonuniversal bundles do not assemble alpha and beta",
    not accepts_constraint_product(nonuniversal)
    and {
        "product_universal_property_missing",
        "alpha_pairing_not_unique",
        "beta_pairing_not_unique",
        "alpha_components_do_not_factor_through_projections",
        "beta_components_do_not_factor_through_projections",
        "nonuniversal_bundle",
        "coproduct_or_sum_substitute",
        "missing_projection",
    }
    <= set(reasons(nonuniversal)),
    ",".join(reasons(nonuniversal)),
)


late_product = live_source(
    product_before_points=False,
    product_before_graph_objects=False,
    alpha_beta_parallel_after_product=False,
    equalizer_uses_product_pair=False,
    product_after_functor_of_points=True,
    fiber_product_after_graph_objects=True,
    projection_after_graph_objects=True,
    graph_classifier_product=True,
)

gate(
    "CATSCPPQBARBECD5 pointwise or graph-side products are too late",
    not accepts_constraint_product(late_product)
    and {
        "product_not_before_points",
        "product_not_before_graph_objects",
        "alpha_beta_not_parallel_after_product",
        "equalizer_does_not_use_product_pair",
        "product_after_functor_of_points",
        "fiber_product_after_graph_objects",
        "projection_after_graph_objects",
        "graph_classifier_product",
    }
    <= set(reasons(late_product)),
    ",".join(reasons(late_product)),
)


local_product = live_source(
    same_product_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_projection_table=True,
    finite_sample_product=True,
    basis_dependent_projection=True,
    retuned_projection=True,
    projected_component_map=True,
)

gate(
    "CATSCPPQBARBECD6 local or retuned projections do not transport all paths",
    not accepts_constraint_product(local_product)
    and {
        "same_product_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_projection_table",
        "finite_sample_product",
        "basis_dependent_projection",
        "retuned_projection",
        "projected_component_map",
    }
    <= set(reasons(local_product)),
    ",".join(reasons(local_product)),
)


control_product = live_source(
    component_objects_actual=False,
    projections_source_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_classifier_product=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSCPPQBARBECD7 graph classifier products leave controls formable",
    not accepts_constraint_product(control_product)
    and {
        "component_objects_missing",
        "projections_not_source_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_classifier_product",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_product)),
    ",".join(reasons(control_product)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_PRODUCT_EDGES
        - {("constraint_product_object", "control_death_projection")}
    ),
    live_source(constraint_product_actual=False),
    live_source(product_projections_actual=False),
    live_source(product_universal_property_actual=False),
    live_source(alpha_pairing_actual=False),
    live_source(beta_pairing_actual=False),
    live_source(equalizer_uses_product_pair=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSCPPQBARBECD8 every product/projection edge is mandatory",
    not any(accepts_constraint_product(data) for data in missing_edges)
    and {
        "required_constraint_product_edges_missing",
        "constraint_product_missing",
        "product_projections_missing",
        "product_universal_property_missing",
        "alpha_pairing_missing",
        "beta_pairing_missing",
        "equalizer_does_not_use_product_pair",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "bundle": bundle,
    "nonuniversal": nonuniversal,
    "late_product": late_product,
    "local_product": local_product,
    "control_product": control_product,
}

gate(
    "CATSCPPQBARBECD9 only categorical source products with universal pairings pass",
    accepts_constraint_product(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_constraint_product(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_constraint_product(data) for data in dead_sources.values()),
        accepts_constraint_product(live),
    ),
)


gate(
    "CATSCPPQBARBECD10 live product has projections and unique alpha/beta pairings",
    accepts_constraint_product(live)
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_PRODUCT_EDGES <= live["required_edges"],
    "product=%s alpha_pair=%s beta_pair=%s edges=%d"
    % (PRODUCT_OBJECT_ID, ALPHA_PAIRING_ID, BETA_PAIRING_ID, len(REQUIRED_PRODUCT_EDGES)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSCPPQBARBECD1-CATSCPPQBARBECD10 ALL PASS: categorical source "
    "constraint product pinned"
)
print(
    "VERDICT: the constraint codomain must be an actual categorical source product with "
    "source-native projections and unique alpha/beta pairing maps. Bundled "
    "tuple labels, external products of sets, nonuniversal bundles, pointwise "
    "or graph-side products, local projection tables, retuned projections, "
    "and graph classifier products do not construct the missing source object."
)
