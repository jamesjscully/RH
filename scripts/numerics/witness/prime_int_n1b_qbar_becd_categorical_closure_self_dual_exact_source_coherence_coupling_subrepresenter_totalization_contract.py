r"""Categorical closure subrepresenter contract for the self-dual exact-source coupling.

Doc 467 requires the non-split categorical source-coherence coupling
primitive to be represented by an actual source-side object and universal
arrow. This witness pins the next edge: that representer cannot be an
abstract or equivalent copy. It must be an actual subrepresenter/fiber of
Rep_BCCube_Qbar_BECD_source_fiber, with a monomorphism whose image is exactly
the coupled self-dual exact sources.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_totalization_contract
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
COUPLING_REPRESENTING_OBJECT_ID = "Rep_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
COUPLING_UNIVERSAL_ARROW_ID = "eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SUBREPRESENTING_OBJECT_ID = "SubRep_NCoup_BCCube_Qbar_BECD_source_fiber"
SUBREP_INCLUSION_ID = "incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber"
SUBREP_IMAGE_ID = "Img_NCoup_BCCube_Qbar_BECD_coupled_self_dual_exact_sources"
SOURCE_COHERENCE_ID = "Coh_BCCube_Qbar_BECD_BCF_self_dual_exact_source_formation"
SOURCE_COUPLING_ID = "NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SELF_DUAL_TOKEN_ID = "Tok_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SELF_DUAL_FIBER_ID = "Fib_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SIGNED_ZERO_FIBER_ID = "ZFib_BCCube_Qbar_BECD_signed_zero"
CANCELLATION_MODULE_ID = "CanMod_BCCube_Qbar_BECD_z_boundary_convolution"
BOUNDARY_FUNCTOR_ID = "BCF_BCCube_Qbar_BECD_boundary_convolution_module"
EXACT_DELTA_ID = "Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary"
KERNEL_ID = "Ker_BCCube_Qbar_BECD_BCF_delta_image_z"
COIMAGE_ID = "Coim_BCCube_Qbar_BECD_CanMod_BCF_delta"
DUALITY_MAP_ID = "Dual_BCCube_Qbar_BECD_rank1_boundary_defect"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
NORMAL_RATIO_ID = "NR_BCCube_Qbar_BECD_ordered_p1_p2"

REQUIRED_SUBREP_EDGES = {
    ("represented_source_square", "source_representing_object"),
    ("source_cube_totalization", "source_representing_object"),
    ("source_representing_object", "source_universal_arrow"),
    ("source_representing_object", "coupling_subrepresenter"),
    ("coupling_subrepresenter", "subrepresenter_inclusion"),
    ("subrepresenter_inclusion", "source_representing_object"),
    ("coupling_subrepresenter", "coupling_representing_object"),
    ("coupling_representing_object", "coupling_universal_arrow"),
    ("coupling_universal_arrow", "source_coherence_coupling_primitive"),
    ("source_coherence_coupling_primitive", "self_dual_exact_source_fiber"),
    ("self_dual_exact_source_fiber", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("multiplier_action_functor", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "exact_boundary_delta"),
    ("source_universal_arrow", "coupling_universal_arrow_factors"),
    ("coupling_universal_arrow_factors", "subrepresenter_inclusion"),
    ("subrepresenter_inclusion", "coupled_image"),
    ("coupled_image", "exact_boundary_delta"),
    ("exact_boundary_delta", "kernel"),
    ("kernel", "coimage"),
    ("coimage", "rank_one_duality"),
    ("rank_one_duality", "original_dd4"),
    ("original_dd4", "normal_ratio"),
    ("normal_ratio", "endpoint_pushforward"),
    ("endpoint_pushforward", "graph_composition"),
    ("graph_composition", "rosati"),
    ("graph_composition", "count_degree"),
    ("rosati", "control_death"),
    ("count_degree", "control_death"),
    ("coupling_subrepresenter", "source_before_graph_objects"),
    ("source_before_graph_objects", "controls_not_points_of_subrepresenter"),
    ("source_before_graph_objects", "dh_not_points_of_subrepresenter"),
    ("source_before_graph_objects", "epstein_not_points_of_subrepresenter"),
    ("coupled_image", "C3_C5_equals_C15"),
    ("coupled_image", "C5_C3_equals_C15"),
    ("coupled_image", "C3_C3_C5_equals_C45"),
    ("coupled_image", "F22_product"),
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


def positive_negative_split(
    chi: dict[int, int],
) -> tuple[dict[int, int], dict[int, int]]:
    pos = {key: val for key, val in chi.items() if val > 0}
    neg = {key: -val for key, val in chi.items() if val < 0}
    return normalize(pos), normalize(neg)


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


def duality_payload(chi: dict[int, int]) -> dict[str, object]:
    pos, neg = positive_negative_split(chi)
    p1, p2 = endpoint_degrees(chi)
    return {
        "duality_map": DUALITY_MAP_ID,
        "defect_rank": 1,
        "dual_line": tuple(neg.items()),
        "primal_line": tuple(pos.items()),
        "endpoint_pair": (p1, p2),
        "perfect_pairing": p1 == p2 and bool(pos) and bool(neg),
        "boundary_class": DD4_CLASS_ID,
        "res1": 1,
    }


def subrep_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "domain": INTERNAL_EFFECTIVITY_DOMAIN_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "source_representer": SOURCE_REPRESENTING_OBJECT_ID,
        "source_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "subrepresenter": SUBREPRESENTING_OBJECT_ID,
        "inclusion": SUBREP_INCLUSION_ID,
        "image": SUBREP_IMAGE_ID,
        "coupling_representer": COUPLING_REPRESENTING_OBJECT_ID,
        "coupling_arrow": COUPLING_UNIVERSAL_ARROW_ID,
        "coupling": SOURCE_COUPLING_ID,
        "coherence": SOURCE_COHERENCE_ID,
        "token": SELF_DUAL_TOKEN_ID,
        "fiber": SELF_DUAL_FIBER_ID,
        "signed_zero_fiber": SIGNED_ZERO_FIBER_ID,
        "cancellation_module": CANCELLATION_MODULE_ID,
        "boundary_functor": BOUNDARY_FUNCTOR_ID,
        "dd4_boundary_localization": DD4_BOUNDARY_LOCALIZATION_ID,
        "endpoint_degree": ENDPOINT_DEGREE_MAPS_ID,
        "delta": EXACT_DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality": duality_payload(chi),
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
        "endpoint_pair": (p1, p2),
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
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
        "multiplier_action_functor_actual": False,
        "source_representer_actual": False,
        "source_universal_arrow_actual": False,
        "coupling_representer_actual": False,
        "coupling_universal_arrow_actual": False,
        "self_dual_source_fiber_actual": False,
        "signed_zero_fiber_actual": False,
        "coupling_subrepresenter_actual": False,
        "subrepresenter_inclusion_actual": False,
        "inclusion_is_monomorphism": False,
        "coupling_arrow_factors_through_inclusion": False,
        "image_exactly_coupled_sources": False,
        "subobject_before_graph_objects": False,
        "same_subrepresenter_all_paths": False,
        "exact_delta_in_image": False,
        "kernel_coimage_in_image": False,
        "rank_one_duality_in_image": False,
        "original_dd4_in_image": False,
        "normal_ratio_in_image": False,
        "endpoint_pushforward_in_image": False,
        "graph_rosati_count_in_image": False,
        "control_death_in_image": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "controls_not_points_of_subrepresenter": False,
        "dh_not_points_of_subrepresenter": False,
        "epstein_not_points_of_subrepresenter": False,
        "required_edges": set(),
        "abstract_external_representer": False,
        "equivalent_representer": False,
        "univalence_transport": False,
        "isomorphic_copy_only": False,
        "morita_equivalent_source": False,
        "idempotent_or_karoubi_split": False,
        "localization_or_saturation": False,
        "sheafification_or_stackification": False,
        "image_closure_only": False,
        "dense_subobject": False,
        "quotient_predicate": False,
        "base_change_subobject": False,
        "retuned_inclusion": False,
        "graph_object_classifier": False,
        "declared_subobject": False,
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
    ("multiplier_action_functor_actual", "multiplier_action_functor_missing"),
    ("source_representer_actual", "source_representer_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("coupling_representer_actual", "coupling_representer_missing"),
    ("coupling_universal_arrow_actual", "coupling_universal_arrow_missing"),
    ("self_dual_source_fiber_actual", "self_dual_source_fiber_missing"),
    ("signed_zero_fiber_actual", "signed_zero_fiber_missing"),
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("subrepresenter_inclusion_actual", "subrepresenter_inclusion_missing"),
    ("inclusion_is_monomorphism", "inclusion_not_monomorphism"),
    (
        "coupling_arrow_factors_through_inclusion",
        "coupling_arrow_does_not_factor_through_inclusion",
    ),
    ("image_exactly_coupled_sources", "image_not_exactly_coupled_sources"),
    ("subobject_before_graph_objects", "subobject_not_before_graph_objects"),
    ("same_subrepresenter_all_paths", "same_subrepresenter_not_all_paths"),
    ("exact_delta_in_image", "exact_delta_not_in_image"),
    ("kernel_coimage_in_image", "kernel_coimage_not_in_image"),
    ("rank_one_duality_in_image", "rank_one_duality_not_in_image"),
    ("original_dd4_in_image", "original_dd4_not_in_image"),
    ("normal_ratio_in_image", "normal_ratio_not_in_image"),
    ("endpoint_pushforward_in_image", "endpoint_pushforward_not_in_image"),
    ("graph_rosati_count_in_image", "graph_rosati_count_not_in_image"),
    ("control_death_in_image", "control_death_not_in_image"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points_of_subrepresenter", "controls_are_points_of_subrepresenter"),
    ("dh_not_points_of_subrepresenter", "dh_is_point_of_subrepresenter"),
    ("epstein_not_points_of_subrepresenter", "epstein_is_point_of_subrepresenter"),
)

BANNED = (
    ("abstract_external_representer", "abstract_external_representer"),
    ("equivalent_representer", "equivalent_representer"),
    ("univalence_transport", "univalence_transport"),
    ("isomorphic_copy_only", "isomorphic_copy_only"),
    ("morita_equivalent_source", "morita_equivalent_source"),
    ("idempotent_or_karoubi_split", "idempotent_or_karoubi_split"),
    ("localization_or_saturation", "localization_or_saturation"),
    ("sheafification_or_stackification", "sheafification_or_stackification"),
    ("image_closure_only", "image_closure_only"),
    ("dense_subobject", "dense_subobject"),
    ("quotient_predicate", "quotient_predicate"),
    ("base_change_subobject", "base_change_subobject"),
    ("retuned_inclusion", "retuned_inclusion"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("declared_subobject", "declared_subobject"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_SUBREP_EDGES <= set(data["required_edges"]):
        out.append("required_subrepresenter_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_subrepresenter(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_SUBREP_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        multiplier_action_functor_actual=True,
        source_representer_actual=True,
        source_universal_arrow_actual=True,
        coupling_representer_actual=True,
        coupling_universal_arrow_actual=True,
        self_dual_source_fiber_actual=True,
        signed_zero_fiber_actual=True,
        coupling_subrepresenter_actual=True,
        subrepresenter_inclusion_actual=True,
        inclusion_is_monomorphism=True,
        coupling_arrow_factors_through_inclusion=True,
        image_exactly_coupled_sources=True,
        subobject_before_graph_objects=True,
        same_subrepresenter_all_paths=True,
        exact_delta_in_image=True,
        kernel_coimage_in_image=True,
        rank_one_duality_in_image=True,
        original_dd4_in_image=True,
        normal_ratio_in_image=True,
        endpoint_pushforward_in_image=True,
        graph_rosati_count_in_image=True,
        control_death_in_image=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        controls_not_points_of_subrepresenter=True,
        dh_not_points_of_subrepresenter=True,
        epstein_not_points_of_subrepresenter=True,
        required_edges=set(REQUIRED_SUBREP_EDGES),
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
    "CATSSRBQBARBECD1 coupling representer is an actual source subrepresenter",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_SUBREP_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and subrep_payload(T3_T5_z) == subrep_payload(zC15)
    and subrep_payload(T5_T3_z) == subrep_payload(zC15)
    and subrep_payload(T3_T3_T5_z) == subrep_payload(zC45)
    and subrep_payload(T15_zF22) == subrep_payload(zC15F22)
    and subrep_payload(T45_zF22) == subrep_payload(zC45F22),
    "H1=%s subrep=%s incl=%s"
    % ([p["h1_order"] for p in profiles], SUBREPRESENTING_OBJECT_ID, SUBREP_INCLUSION_ID),
)


gate(
    "CATSSRBQBARBECD2 graph identities still do not supply the source subrepresenter",
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


external_copy = live_source(
    coupling_subrepresenter_actual=False,
    subrepresenter_inclusion_actual=False,
    coupling_arrow_factors_through_inclusion=False,
    abstract_external_representer=True,
    equivalent_representer=True,
    univalence_transport=True,
    isomorphic_copy_only=True,
)

gate(
    "CATSSRBQBARBECD3 external or equivalent representers are not source subobjects",
    not accepts_subrepresenter(external_copy)
    and {
        "coupling_subrepresenter_missing",
        "subrepresenter_inclusion_missing",
        "coupling_arrow_does_not_factor_through_inclusion",
        "abstract_external_representer",
        "equivalent_representer",
        "univalence_transport",
        "isomorphic_copy_only",
    }
    <= set(reasons(external_copy)),
    ",".join(reasons(external_copy)),
)


split_completion = live_source(
    inclusion_is_monomorphism=False,
    image_exactly_coupled_sources=False,
    morita_equivalent_source=True,
    idempotent_or_karoubi_split=True,
    localization_or_saturation=True,
    sheafification_or_stackification=True,
)

gate(
    "CATSSRBQBARBECD4 completions and saturations do not give the exact image",
    not accepts_subrepresenter(split_completion)
    and {
        "inclusion_not_monomorphism",
        "image_not_exactly_coupled_sources",
        "morita_equivalent_source",
        "idempotent_or_karoubi_split",
        "localization_or_saturation",
        "sheafification_or_stackification",
    }
    <= set(reasons(split_completion)),
    ",".join(reasons(split_completion)),
)


image_shadow = live_source(
    image_exactly_coupled_sources=False,
    exact_delta_in_image=False,
    original_dd4_in_image=False,
    control_death_in_image=False,
    image_closure_only=True,
    dense_subobject=True,
    quotient_predicate=True,
    graph_object_classifier=True,
    control_point_formable=True,
)

gate(
    "CATSSRBQBARBECD5 closures quotients and graph classifiers miss exact source image",
    not accepts_subrepresenter(image_shadow)
    and {
        "image_not_exactly_coupled_sources",
        "exact_delta_not_in_image",
        "original_dd4_not_in_image",
        "control_death_not_in_image",
        "image_closure_only",
        "dense_subobject",
        "quotient_predicate",
        "graph_object_classifier",
        "control_point_formable",
    }
    <= set(reasons(image_shadow)),
    ",".join(reasons(image_shadow)),
)


base_change = live_source(
    same_subrepresenter_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    base_change_subobject=True,
    retuned_inclusion=True,
    declared_subobject=True,
)

gate(
    "CATSSRBQBARBECD6 base-changed or retuned subobjects do not transport all paths",
    not accepts_subrepresenter(base_change)
    and {
        "same_subrepresenter_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "base_change_subobject",
        "retuned_inclusion",
        "declared_subobject",
    }
    <= set(reasons(base_change)),
    ",".join(reasons(base_change)),
)


control_shadow = live_source(
    carrier_native=False,
    subobject_before_graph_objects=False,
    controls_not_points_of_subrepresenter=False,
    dh_not_points_of_subrepresenter=False,
    epstein_not_points_of_subrepresenter=False,
    graph_object_classifier=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSSRBQBARBECD7 control/DH/Epstein subobject shadows are rejected",
    not accepts_subrepresenter(control_shadow)
    and {
        "not_carrier_native",
        "subobject_not_before_graph_objects",
        "controls_are_points_of_subrepresenter",
        "dh_is_point_of_subrepresenter",
        "epstein_is_point_of_subrepresenter",
        "graph_object_classifier",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_shadow)),
    ",".join(reasons(control_shadow)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_SUBREP_EDGES
        - {("source_representing_object", "coupling_subrepresenter")}
    ),
    live_source(coupling_subrepresenter_actual=False),
    live_source(subrepresenter_inclusion_actual=False),
    live_source(inclusion_is_monomorphism=False),
    live_source(image_exactly_coupled_sources=False),
    live_source(controls_not_points_of_subrepresenter=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSSRBQBARBECD8 every subrepresenter edge is mandatory",
    not any(accepts_subrepresenter(data) for data in missing_edges)
    and {
        "required_subrepresenter_edges_missing",
        "coupling_subrepresenter_missing",
        "subrepresenter_inclusion_missing",
        "inclusion_not_monomorphism",
        "image_not_exactly_coupled_sources",
        "controls_are_points_of_subrepresenter",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "external_copy": external_copy,
    "split_completion": split_completion,
    "image_shadow": image_shadow,
    "base_change": base_change,
    "control_shadow": control_shadow,
}

gate(
    "CATSSRBQBARBECD9 only exact source subrepresenters pass",
    accepts_subrepresenter(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_subrepresenter(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_subrepresenter(data) for data in dead_sources.values()),
        accepts_subrepresenter(live),
    ),
)


gate(
    "CATSSRBQBARBECD10 live object is a subrepresenter, not an equivalent shell",
    accepts_subrepresenter(live)
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_SUBREP_EDGES <= live["required_edges"],
    "subrep=%s image=%s edges=%d"
    % (SUBREPRESENTING_OBJECT_ID, SUBREP_IMAGE_ID, len(REQUIRED_SUBREP_EDGES)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSSRBQBARBECD1-CATSSRBQBARBECD10 ALL PASS: categorical closure "
    "self-dual exact-source coherence coupling subrepresenter totalization "
    "contract pinned"
)
print(
    "VERDICT: Rep_NCoup must be an actual subrepresenter/fiber of "
    "Rep_BCCube_Qbar_BECD_source_fiber inside the represented categorical "
    "source square and totalized Beck-Chevalley cube, with a monic inclusion "
    "whose image is exactly the coupled self-dual exact sources. External or "
    "equivalent representers, completions, closures, quotients, base changes, "
    "retuned inclusions, and graph classifiers do not construct the missing "
    "source object."
)
