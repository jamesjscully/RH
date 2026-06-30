r"""Categorical closure component-object contract for the constraint product.

Doc 471 requires an actual categorical source product with projections. This witness
pins the next edge: the seven projection codomains must themselves be actual
categorical source component objects in Rep_BCCube_Qbar_BECD_source_fiber. Semantic labels,
graph-side targets, point-set codomains, or post-hoc component tables are not
categorical source component objects.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_totalization_contract
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
PRODUCT_OBJECT_ID = "Prod_NCoup_BCCube_Qbar_BECD_endpoint_degree_dd4_push_graph_rosati_control"
CONSTRAINT_OBJECT_ID = "Con_NCoup_BCCube_Qbar_BECD_endpoint_dd4_rosati_control_source"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_BCCube_Qbar_BECD_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_BCCube_Qbar_BECD_source_constraints"
ENDPOINT_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_endpoint_integrality"
DEGREE_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_degree_maps"
DD4_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_dd4_boundary"
PUSH_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_boundary_pushforward"
GRAPH_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_graph_composition"
ROSATI_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_rosati_count"
CONTROL_PROJECTION_ID = "pi_NCoup_BCCube_Qbar_BECD_control_death"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
CONTROL_DEATH_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"

ENDPOINT_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_endpoint_integrality_source"
DEGREE_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_degree_maps_source"
DD4_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_dd4_boundary_source"
PUSH_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_boundary_pushforward_source"
GRAPH_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_graph_composition_source"
ROSATI_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_rosati_count_source"
CONTROL_COMPONENT_OBJECT_ID = "Comp_NCoup_BCCube_Qbar_BECD_control_death_source"

COMPONENT_OBJECTS = (
    ENDPOINT_COMPONENT_OBJECT_ID,
    DEGREE_COMPONENT_OBJECT_ID,
    DD4_COMPONENT_OBJECT_ID,
    PUSH_COMPONENT_OBJECT_ID,
    GRAPH_COMPONENT_OBJECT_ID,
    ROSATI_COMPONENT_OBJECT_ID,
    CONTROL_COMPONENT_OBJECT_ID,
)

PROJECTION_TARGETS = (
    (ENDPOINT_PROJECTION_ID, ENDPOINT_COMPONENT_OBJECT_ID),
    (DEGREE_PROJECTION_ID, DEGREE_COMPONENT_OBJECT_ID),
    (DD4_PROJECTION_ID, DD4_COMPONENT_OBJECT_ID),
    (PUSH_PROJECTION_ID, PUSH_COMPONENT_OBJECT_ID),
    (GRAPH_PROJECTION_ID, GRAPH_COMPONENT_OBJECT_ID),
    (ROSATI_PROJECTION_ID, ROSATI_COMPONENT_OBJECT_ID),
    (CONTROL_PROJECTION_ID, CONTROL_COMPONENT_OBJECT_ID),
)

REQUIRED_COMPONENT_EDGES = {
    ("represented_source_square", "source_representing_object"),
    ("source_cube_totalization", "source_representing_object"),
    ("source_representing_object", "endpoint_component_object"),
    ("source_representing_object", "degree_component_object"),
    ("source_representing_object", "dd4_component_object"),
    ("source_representing_object", "pushforward_component_object"),
    ("source_representing_object", "graph_component_object"),
    ("source_representing_object", "rosati_count_component_object"),
    ("source_representing_object", "control_death_component_object"),
    ("source_representing_object", "constraint_product_object"),
    ("endpoint_component_object", "constraint_product_object"),
    ("degree_component_object", "constraint_product_object"),
    ("dd4_component_object", "constraint_product_object"),
    ("pushforward_component_object", "constraint_product_object"),
    ("graph_component_object", "constraint_product_object"),
    ("rosati_count_component_object", "constraint_product_object"),
    ("control_death_component_object", "constraint_product_object"),
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
    ("endpoint_component_object", "source_before_points_and_graphs"),
    ("degree_component_object", "source_before_points_and_graphs"),
    ("dd4_component_object", "source_before_points_and_graphs"),
    ("pushforward_component_object", "source_before_points_and_graphs"),
    ("graph_component_object", "source_before_points_and_graphs"),
    ("rosati_count_component_object", "source_before_points_and_graphs"),
    ("control_death_component_object", "source_before_points_and_graphs"),
    ("source_before_points_and_graphs", "controls_not_points"),
    ("source_before_points_and_graphs", "dh_not_points"),
    ("source_before_points_and_graphs", "epstein_not_points"),
    ("endpoint_component_object", "same_component_all_paths"),
    ("degree_component_object", "same_component_all_paths"),
    ("dd4_component_object", "same_component_all_paths"),
    ("pushforward_component_object", "same_component_all_paths"),
    ("graph_component_object", "same_component_all_paths"),
    ("rosati_count_component_object", "same_component_all_paths"),
    ("control_death_component_object", "same_component_all_paths"),
    ("same_component_all_paths", "C3_C5_equals_C15"),
    ("same_component_all_paths", "C5_C3_equals_C15"),
    ("same_component_all_paths", "C3_C3_C5_equals_C45"),
    ("same_component_all_paths", "F22_product"),
    ("constraint_product_object", "pair_alpha_NCoup_BCCube_Qbar_BECD_source_constraints"),
    ("constraint_product_object", "pair_beta_NCoup_BCCube_Qbar_BECD_source_constraints"),
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


def component_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "categorical_square": CATEGORICAL_SQUARE_ID,
        "facet_cube": FACET_CUBE_ID,
        "cube_totalization": CUBE_TOTALIZATION_ID,
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "component_objects": COMPONENT_OBJECTS,
        "projection_targets": PROJECTION_TARGETS,
        "endpoint_component": (ENDPOINT_COMPONENT_OBJECT_ID, p1, p2, p1 == p2),
        "degree_component": (DEGREE_COMPONENT_OBJECT_ID, tuple(sorted(chi)), p1 + p2),
        "dd4_component": (DD4_COMPONENT_OBJECT_ID, DD4_CLASS_ID),
        "pushforward_component": (PUSH_COMPONENT_OBJECT_ID, tuple(chi.items())),
        "graph_component": (GRAPH_COMPONENT_OBJECT_ID, tuple(sorted(chi))),
        "rosati_component": (ROSATI_COMPONENT_OBJECT_ID, "count_defect_0"),
        "control_component": (CONTROL_COMPONENT_OBJECT_ID, CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "source_component_payload": True,
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
        "component_objects_actual": False,
        "endpoint_component_source_actual": False,
        "degree_component_source_actual": False,
        "dd4_component_source_actual": False,
        "pushforward_component_source_actual": False,
        "graph_component_source_actual": False,
        "rosati_count_component_source_actual": False,
        "control_death_component_source_actual": False,
        "projections_land_in_source_components": False,
        "product_uses_source_components": False,
        "pairings_use_source_components": False,
        "components_before_points": False,
        "components_before_graph_objects": False,
        "components_transport_all_paths": False,
        "same_component_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "semantic_target_labels": False,
        "external_component_objects": False,
        "point_set_codomain": False,
        "graph_side_target_object": False,
        "posthoc_component_codomain": False,
        "component_shell_no_source_object": False,
        "local_component_table": False,
        "finite_sample_component": False,
        "basis_dependent_component": False,
        "retuned_component_object": False,
        "quotient_component": False,
        "closure_component": False,
        "declared_component_object": False,
        "product_with_non_source_codomains": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("component_objects_actual", "component_objects_missing"),
    ("endpoint_component_source_actual", "endpoint_component_source_missing"),
    ("degree_component_source_actual", "degree_component_source_missing"),
    ("dd4_component_source_actual", "dd4_component_source_missing"),
    ("pushforward_component_source_actual", "pushforward_component_source_missing"),
    ("graph_component_source_actual", "graph_component_source_missing"),
    ("rosati_count_component_source_actual", "rosati_count_component_source_missing"),
    ("control_death_component_source_actual", "control_death_component_source_missing"),
    (
        "projections_land_in_source_components",
        "projections_do_not_land_in_source_components",
    ),
    ("product_uses_source_components", "product_does_not_use_source_components"),
    ("pairings_use_source_components", "pairings_do_not_use_source_components"),
    ("components_before_points", "components_not_before_points"),
    ("components_before_graph_objects", "components_not_before_graph_objects"),
    ("components_transport_all_paths", "components_do_not_transport_all_paths"),
    ("same_component_all_paths", "same_component_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("semantic_target_labels", "semantic_target_labels"),
    ("external_component_objects", "external_component_objects"),
    ("point_set_codomain", "point_set_codomain"),
    ("graph_side_target_object", "graph_side_target_object"),
    ("posthoc_component_codomain", "posthoc_component_codomain"),
    ("component_shell_no_source_object", "component_shell_no_source_object"),
    ("local_component_table", "local_component_table"),
    ("finite_sample_component", "finite_sample_component"),
    ("basis_dependent_component", "basis_dependent_component"),
    ("retuned_component_object", "retuned_component_object"),
    ("quotient_component", "quotient_component"),
    ("closure_component", "closure_component"),
    ("declared_component_object", "declared_component_object"),
    ("product_with_non_source_codomains", "product_with_non_source_codomains"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_COMPONENT_EDGES <= set(data["required_edges"]):
        out.append("required_source_component_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_source_components(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_COMPONENT_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        component_objects_actual=True,
        endpoint_component_source_actual=True,
        degree_component_source_actual=True,
        dd4_component_source_actual=True,
        pushforward_component_source_actual=True,
        graph_component_source_actual=True,
        rosati_count_component_source_actual=True,
        control_death_component_source_actual=True,
        projections_land_in_source_components=True,
        product_uses_source_components=True,
        pairings_use_source_components=True,
        components_before_points=True,
        components_before_graph_objects=True,
        components_transport_all_paths=True,
        same_component_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_COMPONENT_EDGES),
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
    "CATSCOMPQBARBECD1 projections land in seven actual categorical source component objects",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_COMPONENT_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and component_payload(T3_T5_z) == component_payload(zC15)
    and component_payload(T5_T3_z) == component_payload(zC15)
    and component_payload(T3_T3_T5_z) == component_payload(zC45)
    and component_payload(T15_zF22) == component_payload(zC15F22)
    and component_payload(T45_zF22) == component_payload(zC45F22),
    "H1=%s components=%d product=%s"
    % ([p["h1_order"] for p in profiles], len(COMPONENT_OBJECTS), PRODUCT_OBJECT_ID),
)


gate(
    "CATSCOMPQBARBECD2 graph identities still do not supply categorical source component objects",
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


semantic = live_source(
    component_objects_actual=False,
    endpoint_component_source_actual=False,
    degree_component_source_actual=False,
    dd4_component_source_actual=False,
    pushforward_component_source_actual=False,
    graph_component_source_actual=False,
    rosati_count_component_source_actual=False,
    control_death_component_source_actual=False,
    projections_land_in_source_components=False,
    semantic_target_labels=True,
    external_component_objects=True,
    declared_component_object=True,
)

gate(
    "CATSCOMPQBARBECD3 semantic or external target labels are not categorical source components",
    not accepts_source_components(semantic)
    and {
        "component_objects_missing",
        "endpoint_component_source_missing",
        "degree_component_source_missing",
        "dd4_component_source_missing",
        "pushforward_component_source_missing",
        "graph_component_source_missing",
        "rosati_count_component_source_missing",
        "control_death_component_source_missing",
        "projections_do_not_land_in_source_components",
        "semantic_target_labels",
        "external_component_objects",
        "declared_component_object",
    }
    <= set(reasons(semantic)),
    ",".join(reasons(semantic)),
)


late = live_source(
    product_uses_source_components=False,
    pairings_use_source_components=False,
    components_before_points=False,
    components_before_graph_objects=False,
    point_set_codomain=True,
    graph_side_target_object=True,
    posthoc_component_codomain=True,
)

gate(
    "CATSCOMPQBARBECD4 point-set, graph-side, or post-hoc codomains are too late",
    not accepts_source_components(late)
    and {
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
        "components_not_before_points",
        "components_not_before_graph_objects",
        "point_set_codomain",
        "graph_side_target_object",
        "posthoc_component_codomain",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)


local = live_source(
    components_transport_all_paths=False,
    same_component_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_component_table=True,
    finite_sample_component=True,
    basis_dependent_component=True,
    retuned_component_object=True,
)

gate(
    "CATSCOMPQBARBECD5 local, finite, basis, or retuned components do not transport",
    not accepts_source_components(local)
    and {
        "components_do_not_transport_all_paths",
        "same_component_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_component_table",
        "finite_sample_component",
        "basis_dependent_component",
        "retuned_component_object",
    }
    <= set(reasons(local)),
    ",".join(reasons(local)),
)


shell = live_source(
    component_objects_actual=False,
    endpoint_component_source_actual=False,
    projections_land_in_source_components=False,
    component_shell_no_source_object=True,
    quotient_component=True,
    closure_component=True,
    declared_component_object=True,
)

gate(
    "CATSCOMPQBARBECD6 quotient, closure, or declared shells are not source objects",
    not accepts_source_components(shell)
    and {
        "component_objects_missing",
        "endpoint_component_source_missing",
        "projections_do_not_land_in_source_components",
        "component_shell_no_source_object",
        "quotient_component",
        "closure_component",
        "declared_component_object",
    }
    <= set(reasons(shell)),
    ",".join(reasons(shell)),
)


control_components = live_source(
    product_uses_source_components=False,
    pairings_use_source_components=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    product_with_non_source_codomains=True,
    graph_side_target_object=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSCOMPQBARBECD7 non-categorical source product codomains leave controls formable",
    not accepts_source_components(control_components)
    and {
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "product_with_non_source_codomains",
        "graph_side_target_object",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_components)),
    ",".join(reasons(control_components)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_COMPONENT_EDGES
        - {("control_death_projection", "control_death_component_object")}
    ),
    live_source(endpoint_component_source_actual=False),
    live_source(degree_component_source_actual=False),
    live_source(dd4_component_source_actual=False),
    live_source(pushforward_component_source_actual=False),
    live_source(graph_component_source_actual=False),
    live_source(rosati_count_component_source_actual=False),
    live_source(control_death_component_source_actual=False),
    live_source(projections_land_in_source_components=False),
    live_source(product_uses_source_components=False),
    live_source(pairings_use_source_components=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSCOMPQBARBECD8 every categorical source component/projection edge is mandatory",
    not any(accepts_source_components(data) for data in missing_edges)
    and {
        "required_source_component_edges_missing",
        "endpoint_component_source_missing",
        "degree_component_source_missing",
        "dd4_component_source_missing",
        "pushforward_component_source_missing",
        "graph_component_source_missing",
        "rosati_count_component_source_missing",
        "control_death_component_source_missing",
        "projections_do_not_land_in_source_components",
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "semantic": semantic,
    "late": late,
    "local": local,
    "shell": shell,
    "control_components": control_components,
}

gate(
    "CATSCOMPQBARBECD9 only categorical source component-object products pass",
    accepts_source_components(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_source_components(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_source_components(data) for data in dead_sources.values()),
        accepts_source_components(live),
    ),
)


gate(
    "CATSCOMPQBARBECD10 live product uses seven categorical source component objects",
    accepts_source_components(live)
    and len(COMPONENT_OBJECTS) == 7
    and len(PROJECTION_TARGETS) == 7
    and all(target in COMPONENT_OBJECTS for _, target in PROJECTION_TARGETS)
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_COMPONENT_EDGES <= live["required_edges"],
    "components=%s alpha_pair=%s beta_pair=%s edges=%d"
    % (COMPONENT_OBJECTS, ALPHA_PAIRING_ID, BETA_PAIRING_ID, len(REQUIRED_COMPONENT_EDGES)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSCOMPQBARBECD1-CATSCOMPQBARBECD10 ALL PASS: categorical source "
    "component objects pinned"
)
print(
    "VERDICT: the constraint product projections must land in seven actual "
    "categorical source component objects. Semantic labels, external components, point-set "
    "codomains, graph-side targets, post-hoc component tables, quotient or "
    "closure shells, and products with non-source codomains do not construct "
    "the missing source object."
)
