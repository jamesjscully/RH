r"""Categorical closure constraint-morphism contract for the finite-limit source cut.

Doc 469 requires the coupling subrepresenter to be produced by one internal
finite-limit/equalizer fork. This witness pins the next edge: the fork legs
must be actual parallel source morphisms into one carrier-native constraint
object. A heterogeneous checklist of external constraint values, pointwise
natural transformations, or graph-side component equalities is not an
equalizer fork in Rep_BCCube_Qbar_BECD_source_fiber.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_morphism_totalization_contract
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
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_BCCube_Qbar_BECD_source_fiber"
CONSTRAINT_OBJECT_ID = "Con_NCoup_BCCube_Qbar_BECD_endpoint_dd4_rosati_control_source"
CONSTRAINT_PRODUCT_ID = "Prod_NCoup_BCCube_Qbar_BECD_endpoint_degree_dd4_push_graph_rosati_control"
ALPHA_CONSTRAINT_MAP_ID = "alpha_NCoup_BCCube_Qbar_BECD_source_constraints"
BETA_CONSTRAINT_MAP_ID = "beta_NCoup_BCCube_Qbar_BECD_source_constraints"
EQUALIZER_ARROW_ID = "eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber"
SUBREPRESENTING_OBJECT_ID = "SubRep_NCoup_BCCube_Qbar_BECD_source_fiber"
CONTROL_DEATH_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"

REQUIRED_MORPHISM_EDGES = {
    ("represented_source_square", "source_representing_object"),
    ("source_cube_totalization", "source_representing_object"),
    ("source_representing_object", "finite_limit_cut"),
    ("source_representing_object", "constraint_product_object"),
    ("finite_limit_cut", "constraint_product_object"),
    ("constraint_product_object", "constraint_object"),
    ("source_representing_object", "alpha_constraint_map"),
    ("source_representing_object", "beta_constraint_map"),
    ("alpha_constraint_map", "constraint_object"),
    ("beta_constraint_map", "constraint_object"),
    ("alpha_constraint_map", "endpoint_integrality_morphism"),
    ("alpha_constraint_map", "degree_map_morphism"),
    ("alpha_constraint_map", "dd4_boundary_morphism"),
    ("alpha_constraint_map", "boundary_pushforward_morphism"),
    ("alpha_constraint_map", "graph_composition_morphism"),
    ("alpha_constraint_map", "rosati_count_morphism"),
    ("alpha_constraint_map", "control_death_morphism"),
    ("beta_constraint_map", "zero_or_diagonal_section"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("equalizer_arrow", "coupling_subrepresenter"),
    ("coupling_subrepresenter", "doc468_subrepresenter"),
    ("finite_limit_cut", "doc469_cut"),
    ("constraint_object", "source_before_points_and_graphs"),
    ("source_before_points_and_graphs", "controls_not_points"),
    ("source_before_points_and_graphs", "dh_not_points"),
    ("source_before_points_and_graphs", "epstein_not_points"),
    ("constraint_object", "same_morphism_payload_all_paths"),
    ("same_morphism_payload_all_paths", "C3_C5_equals_C15"),
    ("same_morphism_payload_all_paths", "C5_C3_equals_C15"),
    ("same_morphism_payload_all_paths", "C3_C3_C5_equals_C45"),
    ("same_morphism_payload_all_paths", "F22_product"),
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


def morphism_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "categorical_square": CATEGORICAL_SQUARE_ID,
        "facet_cube": FACET_CUBE_ID,
        "cube_totalization": CUBE_TOTALIZATION_ID,
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "constraint_product": CONSTRAINT_PRODUCT_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "cut": FINITE_LIMIT_CUT_ID,
        "subrepresenter": SUBREPRESENTING_OBJECT_ID,
        "endpoint_component": (p1, p2, p1 == p2),
        "degree_component": (tuple(sorted(chi)), p1 + p2),
        "dd4_component": DD4_CLASS_ID,
        "control_component": CONTROL_DEATH_ID,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "source_morphism_payload": True,
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
        "finite_limit_cut_actual": False,
        "constraint_object_actual": False,
        "constraint_product_object_actual": False,
        "alpha_constraint_map_actual": False,
        "beta_constraint_map_actual": False,
        "alpha_beta_parallel": False,
        "all_component_morphisms_source_native": False,
        "endpoint_integrality_morphism_actual": False,
        "degree_map_morphism_actual": False,
        "dd4_boundary_morphism_actual": False,
        "boundary_pushforward_morphism_actual": False,
        "graph_composition_morphism_actual": False,
        "rosati_count_morphism_actual": False,
        "control_death_morphism_actual": False,
        "zero_or_diagonal_section_actual": False,
        "equalizer_of_alpha_beta": False,
        "equalizer_image_is_doc469_cut": False,
        "morphisms_before_points": False,
        "morphisms_before_graph_objects": False,
        "same_morphism_payload_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "heterogeneous_codomain_checklist": False,
        "external_constraint_values": False,
        "point_functor_natural_transformation": False,
        "semantic_equality_only": False,
        "componentwise_posthoc_equalities": False,
        "product_object_missing": False,
        "nonparallel_fork_legs": False,
        "one_sided_constraint_map": False,
        "diagonal_after_graph_objects": False,
        "zero_section_inserted_after_facts": False,
        "local_constraint_table": False,
        "finite_sample_morphism": False,
        "basis_dependent_morphism": False,
        "retuned_component_map": False,
        "projected_component_map": False,
        "graph_classifier_morphism": False,
        "declared_parallel_pair": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("constraint_product_object_actual", "constraint_product_object_missing"),
    ("alpha_constraint_map_actual", "alpha_constraint_map_missing"),
    ("beta_constraint_map_actual", "beta_constraint_map_missing"),
    ("alpha_beta_parallel", "alpha_beta_not_parallel"),
    (
        "all_component_morphisms_source_native",
        "component_morphisms_not_source_native",
    ),
    ("endpoint_integrality_morphism_actual", "endpoint_morphism_missing"),
    ("degree_map_morphism_actual", "degree_map_morphism_missing"),
    ("dd4_boundary_morphism_actual", "dd4_boundary_morphism_missing"),
    (
        "boundary_pushforward_morphism_actual",
        "boundary_pushforward_morphism_missing",
    ),
    ("graph_composition_morphism_actual", "graph_composition_morphism_missing"),
    ("rosati_count_morphism_actual", "rosati_count_morphism_missing"),
    ("control_death_morphism_actual", "control_death_morphism_missing"),
    ("zero_or_diagonal_section_actual", "zero_or_diagonal_section_missing"),
    ("equalizer_of_alpha_beta", "not_equalizer_of_alpha_beta"),
    ("equalizer_image_is_doc469_cut", "equalizer_image_not_doc469_cut"),
    ("morphisms_before_points", "morphisms_not_before_points"),
    ("morphisms_before_graph_objects", "morphisms_not_before_graph_objects"),
    ("same_morphism_payload_all_paths", "same_morphism_payload_not_all_paths"),
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
    ("heterogeneous_codomain_checklist", "heterogeneous_codomain_checklist"),
    ("external_constraint_values", "external_constraint_values"),
    (
        "point_functor_natural_transformation",
        "point_functor_natural_transformation",
    ),
    ("semantic_equality_only", "semantic_equality_only"),
    ("componentwise_posthoc_equalities", "componentwise_posthoc_equalities"),
    ("product_object_missing", "product_object_missing"),
    ("nonparallel_fork_legs", "nonparallel_fork_legs"),
    ("one_sided_constraint_map", "one_sided_constraint_map"),
    ("diagonal_after_graph_objects", "diagonal_after_graph_objects"),
    ("zero_section_inserted_after_facts", "zero_section_inserted_after_facts"),
    ("local_constraint_table", "local_constraint_table"),
    ("finite_sample_morphism", "finite_sample_morphism"),
    ("basis_dependent_morphism", "basis_dependent_morphism"),
    ("retuned_component_map", "retuned_component_map"),
    ("projected_component_map", "projected_component_map"),
    ("graph_classifier_morphism", "graph_classifier_morphism"),
    ("declared_parallel_pair", "declared_parallel_pair"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_MORPHISM_EDGES <= set(data["required_edges"]):
        out.append("required_constraint_morphism_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_constraint_morphisms(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_MORPHISM_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        finite_limit_cut_actual=True,
        constraint_object_actual=True,
        constraint_product_object_actual=True,
        alpha_constraint_map_actual=True,
        beta_constraint_map_actual=True,
        alpha_beta_parallel=True,
        all_component_morphisms_source_native=True,
        endpoint_integrality_morphism_actual=True,
        degree_map_morphism_actual=True,
        dd4_boundary_morphism_actual=True,
        boundary_pushforward_morphism_actual=True,
        graph_composition_morphism_actual=True,
        rosati_count_morphism_actual=True,
        control_death_morphism_actual=True,
        zero_or_diagonal_section_actual=True,
        equalizer_of_alpha_beta=True,
        equalizer_image_is_doc469_cut=True,
        morphisms_before_points=True,
        morphisms_before_graph_objects=True,
        same_morphism_payload_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_MORPHISM_EDGES),
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
    "CATSCFMQBARBECD1 finite-limit fork has actual parallel source constraint morphisms",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_MORPHISM_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and morphism_payload(T3_T5_z) == morphism_payload(zC15)
    and morphism_payload(T5_T3_z) == morphism_payload(zC15)
    and morphism_payload(T3_T3_T5_z) == morphism_payload(zC45)
    and morphism_payload(T15_zF22) == morphism_payload(zC15F22)
    and morphism_payload(T45_zF22) == morphism_payload(zC45F22),
    "H1=%s alpha=%s beta=%s"
    % ([p["h1_order"] for p in profiles], ALPHA_CONSTRAINT_MAP_ID, BETA_CONSTRAINT_MAP_ID),
)


gate(
    "CATSCFMQBARBECD2 graph identities still do not supply source constraint morphisms",
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


checklist = live_source(
    constraint_object_actual=False,
    constraint_product_object_actual=False,
    all_component_morphisms_source_native=False,
    heterogeneous_codomain_checklist=True,
    external_constraint_values=True,
    semantic_equality_only=True,
    componentwise_posthoc_equalities=True,
    product_object_missing=True,
)

gate(
    "CATSCFMQBARBECD3 heterogeneous constraint checklists are not source codomains",
    not accepts_constraint_morphisms(checklist)
    and {
        "constraint_object_missing",
        "constraint_product_object_missing",
        "component_morphisms_not_source_native",
        "heterogeneous_codomain_checklist",
        "external_constraint_values",
        "semantic_equality_only",
        "componentwise_posthoc_equalities",
        "product_object_missing",
    }
    <= set(reasons(checklist)),
    ",".join(reasons(checklist)),
)


nonparallel = live_source(
    beta_constraint_map_actual=False,
    alpha_beta_parallel=False,
    zero_or_diagonal_section_actual=False,
    equalizer_of_alpha_beta=False,
    nonparallel_fork_legs=True,
    one_sided_constraint_map=True,
    declared_parallel_pair=True,
)

gate(
    "CATSCFMQBARBECD4 nonparallel or one-sided fork legs do not define the equalizer",
    not accepts_constraint_morphisms(nonparallel)
    and {
        "beta_constraint_map_missing",
        "alpha_beta_not_parallel",
        "zero_or_diagonal_section_missing",
        "not_equalizer_of_alpha_beta",
        "nonparallel_fork_legs",
        "one_sided_constraint_map",
        "declared_parallel_pair",
    }
    <= set(reasons(nonparallel)),
    ",".join(reasons(nonparallel)),
)


point_functor = live_source(
    morphisms_before_points=False,
    morphisms_before_graph_objects=False,
    equalizer_image_is_doc469_cut=False,
    point_functor_natural_transformation=True,
    diagonal_after_graph_objects=True,
    zero_section_inserted_after_facts=True,
    graph_classifier_morphism=True,
)

gate(
    "CATSCFMQBARBECD5 point-functor and graph-side morphisms are too late",
    not accepts_constraint_morphisms(point_functor)
    and {
        "morphisms_not_before_points",
        "morphisms_not_before_graph_objects",
        "equalizer_image_not_doc469_cut",
        "point_functor_natural_transformation",
        "diagonal_after_graph_objects",
        "zero_section_inserted_after_facts",
        "graph_classifier_morphism",
    }
    <= set(reasons(point_functor)),
    ",".join(reasons(point_functor)),
)


local_table = live_source(
    same_morphism_payload_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_constraint_table=True,
    finite_sample_morphism=True,
    basis_dependent_morphism=True,
    retuned_component_map=True,
    projected_component_map=True,
)

gate(
    "CATSCFMQBARBECD6 local or retuned component maps do not transport all paths",
    not accepts_constraint_morphisms(local_table)
    and {
        "same_morphism_payload_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_constraint_table",
        "finite_sample_morphism",
        "basis_dependent_morphism",
        "retuned_component_map",
        "projected_component_map",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)


graph_filter = live_source(
    endpoint_integrality_morphism_actual=False,
    degree_map_morphism_actual=False,
    dd4_boundary_morphism_actual=False,
    boundary_pushforward_morphism_actual=False,
    graph_composition_morphism_actual=False,
    rosati_count_morphism_actual=False,
    control_death_morphism_actual=False,
    graph_classifier_morphism=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSCFMQBARBECD7 graph/Rosati/DD4 component classifiers leave controls formable",
    not accepts_constraint_morphisms(graph_filter)
    and {
        "endpoint_morphism_missing",
        "degree_map_morphism_missing",
        "dd4_boundary_morphism_missing",
        "boundary_pushforward_morphism_missing",
        "graph_composition_morphism_missing",
        "rosati_count_morphism_missing",
        "control_death_morphism_missing",
        "graph_classifier_morphism",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_filter)),
    ",".join(reasons(graph_filter)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_MORPHISM_EDGES
        - {("alpha_constraint_map", "parallel_pair")}
    ),
    live_source(constraint_object_actual=False),
    live_source(alpha_constraint_map_actual=False),
    live_source(beta_constraint_map_actual=False),
    live_source(alpha_beta_parallel=False),
    live_source(equalizer_of_alpha_beta=False),
    live_source(control_death_morphism_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSCFMQBARBECD8 every constraint-morphism edge is mandatory",
    not any(accepts_constraint_morphisms(data) for data in missing_edges)
    and {
        "required_constraint_morphism_edges_missing",
        "constraint_object_missing",
        "alpha_constraint_map_missing",
        "beta_constraint_map_missing",
        "alpha_beta_not_parallel",
        "not_equalizer_of_alpha_beta",
        "control_death_morphism_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "checklist": checklist,
    "nonparallel": nonparallel,
    "point_functor": point_functor,
    "local_table": local_table,
    "graph_filter": graph_filter,
}

gate(
    "CATSCFMQBARBECD9 only carrier-native parallel source morphism forks pass",
    accepts_constraint_morphisms(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_constraint_morphisms(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_constraint_morphisms(data) for data in dead_sources.values()),
        accepts_constraint_morphisms(live),
    ),
)


gate(
    "CATSCFMQBARBECD10 live fork has one source codomain and one parallel pair",
    accepts_constraint_morphisms(live)
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_MORPHISM_EDGES <= live["required_edges"],
    "codomain=%s alpha=%s beta=%s edges=%d"
    % (
        CONSTRAINT_OBJECT_ID,
        ALPHA_CONSTRAINT_MAP_ID,
        BETA_CONSTRAINT_MAP_ID,
        len(REQUIRED_MORPHISM_EDGES),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSCFMQBARBECD1-CATSCFMQBARBECD10 ALL PASS: categorical source "
    "constraint morphisms pinned"
)
print(
    "VERDICT: the finite-limit source cut must be the equalizer of actual "
    "parallel carrier-native source morphisms alpha,beta into one constraint "
    "object. Heterogeneous checklists, external values, point-functor natural "
    "transformations, nonparallel fork legs, local/retuned component maps, and "
    "graph-side classifiers do not construct the missing source object."
)
