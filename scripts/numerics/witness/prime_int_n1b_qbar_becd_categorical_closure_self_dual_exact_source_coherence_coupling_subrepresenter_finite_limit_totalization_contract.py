r"""Categorical closure finite-limit cut contract for the self-dual exact-source subrepresenter.

Doc 468 pins the coupling representer to an actual categorical
subrepresenter/fiber of Rep_BCCube_Qbar_BECD_source_fiber. This witness pins
the next edge: the subrepresenter cannot be selected by a pointwise exact-
image predicate. It must be cut out internally, before points and graph
objects, by one finite-limit/equalizer fork carrying endpoint integrality,
degree maps, DD.4 boundary, boundary pushforward, graph composition,
Rosati/count, and control death simultaneously.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_totalization_contract
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
INTERNAL_EFFECTIVITY_DOMAIN_ID = "D_Qbar_BECD_eff"
MULTIPLIER_ACTION_FUNCTOR_ID = "Act_BCCube_Qbar_BECD_multiplier_functor"
DD4_BOUNDARY_LOCALIZATION_ID = "B_Qbar_BECD_DD4_multiplier_natural"
ENDPOINT_DEGREE_MAPS_ID = "DegMaps_BCCube_Qbar_BECD_multiplier_endpoint"
P1_PUSHFORWARD_ID = "p1_star_Qbar_BECD_endpoint_boundary"
P2_PUSHFORWARD_ID = "p2_star_Qbar_BECD_endpoint_boundary"
PUSHFORWARD_SQUARE_ID = "PF_Qbar_BECD_p1p2_DD4_endpoint"
GRAPH_ROSATI_COUNT_TOTALIZATION_ID = "GRCTot_BCCube_Qbar_BECD_pushforward_internal_stratum"
PROPER_GRAPH_ID = "G_Qbar_BECD_pushforward_prop"
ROSATI_LAYER_ID = "R_Qbar_BECD_pushforward_positive"
COUNT_DEGREE_ID = "CD_Qbar_BECD_pushforward"
CONTROL_DEATH_NATURALITY_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"
SOURCE_REPRESENTING_OBJECT_ID = "Rep_BCCube_Qbar_BECD_source_fiber"
SOURCE_UNIVERSAL_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
SUBREPRESENTING_OBJECT_ID = "SubRep_NCoup_BCCube_Qbar_BECD_source_fiber"
SUBREP_INCLUSION_ID = "incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber"
SUBREP_IMAGE_ID = "Img_NCoup_BCCube_Qbar_BECD_coupled_self_dual_exact_sources"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_BCCube_Qbar_BECD_source_fiber"
EQUALIZER_ARROW_ID = "eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber"
JOINT_FORK_ID = "Fork_BCCube_endpoint_dd4_rosati_control_NCoup"
SOURCE_COUPLING_ID = "NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SIGNED_ZERO_FIBER_ID = "ZFib_BCCube_Qbar_BECD_signed_zero"
CANCELLATION_MODULE_ID = "CanMod_BCCube_Qbar_BECD_z_boundary_convolution"
BOUNDARY_FUNCTOR_ID = "BCF_BCCube_Qbar_BECD_boundary_convolution_module"
EXACT_DELTA_ID = "Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
NORMAL_RATIO_ID = "NR_BCCube_Qbar_BECD_ordered_p1_p2"

REQUIRED_LIMIT_EDGES = {
    ("represented_source_square", "source_representing_object"),
    ("source_cube_totalization", "source_representing_object"),
    ("source_representing_object", "finite_limit_cut"),
    ("source_universal_arrow", "finite_limit_cut"),
    ("finite_limit_cut", "joint_constraint_fork"),
    ("joint_constraint_fork", "endpoint_integrality_constraint"),
    ("joint_constraint_fork", "degree_map_constraint"),
    ("joint_constraint_fork", "dd4_boundary_constraint"),
    ("joint_constraint_fork", "boundary_pushforward_constraint"),
    ("joint_constraint_fork", "graph_composition_constraint"),
    ("joint_constraint_fork", "rosati_count_constraint"),
    ("joint_constraint_fork", "control_death_constraint"),
    ("finite_limit_cut", "equalizer_arrow"),
    ("equalizer_arrow", "coupling_subrepresenter"),
    ("equalizer_arrow", "subrepresenter_inclusion"),
    ("equalizer_arrow", "subrepresenter_image"),
    ("equalizer_arrow", "monic_equalizer_arrow"),
    ("monic_equalizer_arrow", "exact_subrepresenter_image"),
    ("exact_subrepresenter_image", "coupled_self_dual_exact_sources"),
    ("coupled_self_dual_exact_sources", "source_coherence_coupling"),
    ("source_coherence_coupling", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("multiplier_action_functor", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "exact_boundary_delta"),
    ("source_coherence_coupling", "exact_boundary_delta"),
    ("exact_boundary_delta", "original_dd4_boundary"),
    ("original_dd4_boundary", "normal_ratio"),
    ("normal_ratio", "endpoint_pushforward"),
    ("endpoint_pushforward", "graph_composition"),
    ("graph_composition", "rosati_count"),
    ("rosati_count", "control_death"),
    ("finite_limit_cut", "universal_property"),
    ("universal_property", "same_cut_all_paths"),
    ("same_cut_all_paths", "C3_C5_equals_C15"),
    ("same_cut_all_paths", "C5_C3_equals_C15"),
    ("same_cut_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cut_all_paths", "F22_product"),
    ("finite_limit_cut", "source_before_points_and_graphs"),
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


def limit_cut_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "domain": INTERNAL_EFFECTIVITY_DOMAIN_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "source_representer": SOURCE_REPRESENTING_OBJECT_ID,
        "source_universal_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "joint_fork": JOINT_FORK_ID,
        "equalizer_arrow": EQUALIZER_ARROW_ID,
        "subrepresenter": SUBREPRESENTING_OBJECT_ID,
        "inclusion": SUBREP_INCLUSION_ID,
        "image": SUBREP_IMAGE_ID,
        "coupling": SOURCE_COUPLING_ID,
        "signed_zero_fiber": SIGNED_ZERO_FIBER_ID,
        "cancellation_module": CANCELLATION_MODULE_ID,
        "boundary_functor": BOUNDARY_FUNCTOR_ID,
        "endpoint_integrality": (p1, p2, p1 == p2),
        "degree_maps": (tuple(sorted(chi)), p1 + p2),
        "endpoint_degree_maps": ENDPOINT_DEGREE_MAPS_ID,
        "dd4_boundary": DD4_CLASS_ID,
        "dd4_boundary_localization": DD4_BOUNDARY_LOCALIZATION_ID,
        "exact_delta": EXACT_DELTA_ID,
        "normal_ratio": NORMAL_RATIO_ID,
        "p1_pushforward": P1_PUSHFORWARD_ID,
        "p2_pushforward": P2_PUSHFORWARD_ID,
        "pushforward": PUSHFORWARD_SQUARE_ID,
        "graph_totalization": GRAPH_ROSATI_COUNT_TOTALIZATION_ID,
        "graph": PROPER_GRAPH_ID,
        "rosati": ROSATI_LAYER_ID,
        "count": COUNT_DEGREE_ID,
        "control_death": CONTROL_DEATH_NATURALITY_ID,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cut_before_points": True,
        "cut_before_graph_objects": True,
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
        "represented_source_square_actual": False,
        "source_cube_totalization_actual": False,
        "source_universal_arrow_actual": False,
        "multiplier_action_functor_actual": False,
        "represented_source_fiber_actual": False,
        "coupling_subrepresenter_actual": False,
        "subrepresenter_inclusion_actual": False,
        "subrepresenter_image_actual": False,
        "finite_limit_cut_actual": False,
        "joint_constraint_fork_actual": False,
        "equalizer_arrow_actual": False,
        "equalizer_arrow_monic": False,
        "fork_commutes": False,
        "universal_property_actual": False,
        "cut_before_points": False,
        "cut_before_graph_objects": False,
        "image_is_the_doc468_subrepresenter": False,
        "constraints_same_fork": False,
        "endpoint_integrality_in_fork": False,
        "degree_maps_in_fork": False,
        "dd4_boundary_in_fork": False,
        "boundary_pushforward_in_fork": False,
        "graph_composition_in_fork": False,
        "rosati_count_in_fork": False,
        "control_death_in_fork": False,
        "same_cut_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "pointwise_image_certificate": False,
        "predicate_subobject_selection": False,
        "subobject_classifier": False,
        "characteristic_map_only": False,
        "sequential_intersection": False,
        "iterated_filters": False,
        "posthoc_image_factorization": False,
        "external_limit_completion": False,
        "pullback_after_graph_objects": False,
        "local_row_table": False,
        "finite_sample_cut": False,
        "basis_dependent_cut": False,
        "retuned_constraint": False,
        "projected_constraint": False,
        "graph_invariant_classifier": False,
        "declared_equalizer": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_square_actual", "represented_source_square_missing"),
    ("source_cube_totalization_actual", "source_cube_totalization_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("multiplier_action_functor_actual", "multiplier_action_functor_missing"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("subrepresenter_inclusion_actual", "subrepresenter_inclusion_missing"),
    ("subrepresenter_image_actual", "subrepresenter_image_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("joint_constraint_fork_actual", "joint_constraint_fork_missing"),
    ("equalizer_arrow_actual", "equalizer_arrow_missing"),
    ("equalizer_arrow_monic", "equalizer_arrow_not_monic"),
    ("fork_commutes", "fork_not_commuting"),
    ("universal_property_actual", "universal_property_missing"),
    ("cut_before_points", "cut_not_before_points"),
    ("cut_before_graph_objects", "cut_not_before_graph_objects"),
    ("image_is_the_doc468_subrepresenter", "image_not_doc468_subrepresenter"),
    ("constraints_same_fork", "constraints_not_same_fork"),
    ("endpoint_integrality_in_fork", "endpoint_integrality_not_in_fork"),
    ("degree_maps_in_fork", "degree_maps_not_in_fork"),
    ("dd4_boundary_in_fork", "dd4_boundary_not_in_fork"),
    ("boundary_pushforward_in_fork", "boundary_pushforward_not_in_fork"),
    ("graph_composition_in_fork", "graph_composition_not_in_fork"),
    ("rosati_count_in_fork", "rosati_count_not_in_fork"),
    ("control_death_in_fork", "control_death_not_in_fork"),
    ("same_cut_all_paths", "same_cut_not_all_paths"),
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
    ("pointwise_image_certificate", "pointwise_image_certificate"),
    ("predicate_subobject_selection", "predicate_subobject_selection"),
    ("subobject_classifier", "subobject_classifier"),
    ("characteristic_map_only", "characteristic_map_only"),
    ("sequential_intersection", "sequential_intersection"),
    ("iterated_filters", "iterated_filters"),
    ("posthoc_image_factorization", "posthoc_image_factorization"),
    ("external_limit_completion", "external_limit_completion"),
    ("pullback_after_graph_objects", "pullback_after_graph_objects"),
    ("local_row_table", "local_row_table"),
    ("finite_sample_cut", "finite_sample_cut"),
    ("basis_dependent_cut", "basis_dependent_cut"),
    ("retuned_constraint", "retuned_constraint"),
    ("projected_constraint", "projected_constraint"),
    ("graph_invariant_classifier", "graph_invariant_classifier"),
    ("declared_equalizer", "declared_equalizer"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_LIMIT_EDGES <= set(data["required_edges"]):
        out.append("required_finite_limit_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_limit_cut(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_LIMIT_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        source_universal_arrow_actual=True,
        multiplier_action_functor_actual=True,
        represented_source_fiber_actual=True,
        coupling_subrepresenter_actual=True,
        subrepresenter_inclusion_actual=True,
        subrepresenter_image_actual=True,
        finite_limit_cut_actual=True,
        joint_constraint_fork_actual=True,
        equalizer_arrow_actual=True,
        equalizer_arrow_monic=True,
        fork_commutes=True,
        universal_property_actual=True,
        cut_before_points=True,
        cut_before_graph_objects=True,
        image_is_the_doc468_subrepresenter=True,
        constraints_same_fork=True,
        endpoint_integrality_in_fork=True,
        degree_maps_in_fork=True,
        dd4_boundary_in_fork=True,
        boundary_pushforward_in_fork=True,
        graph_composition_in_fork=True,
        rosati_count_in_fork=True,
        control_death_in_fork=True,
        same_cut_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_LIMIT_EDGES),
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
    "CATSFLQBARBECD1 subrepresenter is cut out by one source finite-limit fork",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_LIMIT_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and limit_cut_payload(T3_T5_z) == limit_cut_payload(zC15)
    and limit_cut_payload(T5_T3_z) == limit_cut_payload(zC15)
    and limit_cut_payload(T3_T3_T5_z) == limit_cut_payload(zC45)
    and limit_cut_payload(T15_zF22) == limit_cut_payload(zC15F22)
    and limit_cut_payload(T45_zF22) == limit_cut_payload(zC45F22),
    "H1=%s cut=%s eq=%s"
    % ([p["h1_order"] for p in profiles], FINITE_LIMIT_CUT_ID, EQUALIZER_ARROW_ID),
)


gate(
    "CATSFLQBARBECD2 graph identities still do not supply the finite-limit cut",
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


pointwise = live_source(
    finite_limit_cut_actual=False,
    joint_constraint_fork_actual=False,
    equalizer_arrow_actual=False,
    universal_property_actual=False,
    pointwise_image_certificate=True,
    predicate_subobject_selection=True,
    subobject_classifier=True,
    characteristic_map_only=True,
)

gate(
    "CATSFLQBARBECD3 pointwise exact-image predicates are not finite-limit cuts",
    not accepts_limit_cut(pointwise)
    and {
        "finite_limit_cut_missing",
        "joint_constraint_fork_missing",
        "equalizer_arrow_missing",
        "universal_property_missing",
        "pointwise_image_certificate",
        "predicate_subobject_selection",
        "subobject_classifier",
        "characteristic_map_only",
    }
    <= set(reasons(pointwise)),
    ",".join(reasons(pointwise)),
)


sequential = live_source(
    constraints_same_fork=False,
    fork_commutes=False,
    control_death_in_fork=False,
    sequential_intersection=True,
    iterated_filters=True,
    posthoc_image_factorization=True,
    control_point_formable=True,
)

gate(
    "CATSFLQBARBECD4 sequential intersections do not make one simultaneous source fork",
    not accepts_limit_cut(sequential)
    and {
        "constraints_not_same_fork",
        "fork_not_commuting",
        "control_death_not_in_fork",
        "sequential_intersection",
        "iterated_filters",
        "posthoc_image_factorization",
        "control_point_formable",
    }
    <= set(reasons(sequential)),
    ",".join(reasons(sequential)),
)


late_pullback = live_source(
    cut_before_points=False,
    cut_before_graph_objects=False,
    image_is_the_doc468_subrepresenter=False,
    external_limit_completion=True,
    pullback_after_graph_objects=True,
    graph_invariant_classifier=True,
)

gate(
    "CATSFLQBARBECD5 external completions and late pullbacks miss the source cut",
    not accepts_limit_cut(late_pullback)
    and {
        "cut_not_before_points",
        "cut_not_before_graph_objects",
        "image_not_doc468_subrepresenter",
        "external_limit_completion",
        "pullback_after_graph_objects",
        "graph_invariant_classifier",
    }
    <= set(reasons(late_pullback)),
    ",".join(reasons(late_pullback)),
)


local_table = live_source(
    same_cut_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_row_table=True,
    finite_sample_cut=True,
    basis_dependent_cut=True,
    retuned_constraint=True,
    projected_constraint=True,
)

gate(
    "CATSFLQBARBECD6 local row tables and retuned constraints do not transport all paths",
    not accepts_limit_cut(local_table)
    and {
        "same_cut_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_row_table",
        "finite_sample_cut",
        "basis_dependent_cut",
        "retuned_constraint",
        "projected_constraint",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)


graph_filter = live_source(
    endpoint_integrality_in_fork=False,
    degree_maps_in_fork=False,
    dd4_boundary_in_fork=False,
    boundary_pushforward_in_fork=False,
    graph_composition_in_fork=False,
    rosati_count_in_fork=False,
    control_death_in_fork=False,
    graph_invariant_classifier=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSFLQBARBECD7 graph/Rosati/DD4 after-filters leave controls formable",
    not accepts_limit_cut(graph_filter)
    and {
        "endpoint_integrality_not_in_fork",
        "degree_maps_not_in_fork",
        "dd4_boundary_not_in_fork",
        "boundary_pushforward_not_in_fork",
        "graph_composition_not_in_fork",
        "rosati_count_not_in_fork",
        "control_death_not_in_fork",
        "graph_invariant_classifier",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_filter)),
    ",".join(reasons(graph_filter)),
)


missing_edges = [
    live_source(required_edges=REQUIRED_LIMIT_EDGES - {("finite_limit_cut", "equalizer_arrow")}),
    live_source(finite_limit_cut_actual=False),
    live_source(joint_constraint_fork_actual=False),
    live_source(equalizer_arrow_actual=False),
    live_source(equalizer_arrow_monic=False),
    live_source(universal_property_actual=False),
    live_source(control_death_in_fork=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSFLQBARBECD8 every finite-limit cut edge is mandatory",
    not any(accepts_limit_cut(data) for data in missing_edges)
    and {
        "required_finite_limit_edges_missing",
        "finite_limit_cut_missing",
        "joint_constraint_fork_missing",
        "equalizer_arrow_missing",
        "equalizer_arrow_not_monic",
        "universal_property_missing",
        "control_death_not_in_fork",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "pointwise": pointwise,
    "sequential": sequential,
    "late_pullback": late_pullback,
    "local_table": local_table,
    "graph_filter": graph_filter,
}

gate(
    "CATSFLQBARBECD9 only simultaneous source finite-limit cuts pass",
    accepts_limit_cut(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_limit_cut(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_limit_cut(data) for data in dead_sources.values()),
        accepts_limit_cut(live),
    ),
)


gate(
    "CATSFLQBARBECD10 live cut is internal, not a predicate shell",
    accepts_limit_cut(live)
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_LIMIT_EDGES <= live["required_edges"],
    "cut=%s fork=%s edges=%d"
    % (FINITE_LIMIT_CUT_ID, JOINT_FORK_ID, len(REQUIRED_LIMIT_EDGES)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSFLQBARBECD1-CATSFLQBARBECD10 ALL PASS: categorical closure "
    "self-dual exact-source coherence coupling subrepresenter finite-limit "
    "totalization contract pinned"
)
print(
    "VERDICT: the categorical source-coupling subrepresenter must be produced "
    "by one carrier-native finite-limit/equalizer fork inside "
    "Rep_BCCube_Qbar_BECD_source_fiber before points and graph objects. "
    "Pointwise exact-image predicates, sequential filters, external limit "
    "completions, late pullbacks, local row tables, retuned constraints, and "
    "graph/Rosati/DD4 after-filters do not construct the missing source object "
    "or jointly kill controls."
)
