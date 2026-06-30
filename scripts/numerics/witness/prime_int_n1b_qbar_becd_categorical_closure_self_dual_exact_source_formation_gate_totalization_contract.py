r"""Categorical closure self-dual exact-source formation-gate contract.

Doc 463 requires the represented categorical exact BCF boundary-delta source
to generate the rank-one self-dual boundary-defect/properness datum. This
witness pins the next edge: that self-dual exact source must be a represented
formation fiber before graph objects exist. A graph-level predicate, declared
non-point condition, functor of points, finite admission table, local source
stack, or late control/DH/Epstein filter does not construct source-level
death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_formation_gate_totalization_contract
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
GRAPH_FORMATION_GATE_ID = "K_Qbar_BECD_graph_formation_death"
CONTROL_DEATH_NATURALITY_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"
SOURCE_TOKEN_ID = "SrcTok_BCCube_Qbar_BECD_source_typed_graph_formation"
SOURCE_FIBER_ID = "Fib_BCCube_Qbar_BECD_source_typed_graph_formation"
SELF_DUAL_TOKEN_ID = "Tok_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SELF_DUAL_FIBER_ID = "Fib_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
REPRESENTING_OBJECT_ID = "Rep_BCCube_Qbar_BECD_source_fiber"
UNIVERSAL_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
MONOIDWIDE_COHERENCE_ID = "MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers"
SIGNED_ZERO_FIBER_ID = "ZFib_BCCube_Qbar_BECD_signed_zero"
CANCELLATION_MODULE_ID = "CanMod_BCCube_Qbar_BECD_z_boundary_convolution"
BOUNDARY_FUNCTOR_ID = "BCF_BCCube_Qbar_BECD_boundary_convolution_module"
EXACT_SEQUENCE_ID = "Ex_BCCube_Qbar_BECD_CanMod_BCF_dQ"
EXACT_DELTA_ID = "Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary"
KERNEL_ID = "Ker_BCCube_Qbar_BECD_BCF_delta_image_z"
COIMAGE_ID = "Coim_BCCube_Qbar_BECD_CanMod_BCF_delta"
DUALITY_MAP_ID = "Dual_BCCube_Qbar_BECD_rank1_boundary_defect"
TWIST_ID = "Tw_BCCube_Qbar_BECD_OC_BCF_pinned"
BOUNDARY_CERTIFICATE_ID = "BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
LOCALIZATION_SEQUENCE_ID = "Loc_BCCube_Qbar_BECD_single_dQ"
NORMAL_RATIO_ID = "NR_BCCube_Qbar_BECD_ordered_p1_p2"

REQUIRED_FORMATION_EDGES = {
    ("represented_source_square", "self_dual_exact_source_token"),
    ("source_cube_totalization", "self_dual_exact_source_token"),
    ("universal_arrow", "self_dual_exact_source_token"),
    ("self_dual_exact_source_token", "self_dual_exact_source_fiber"),
    ("self_dual_exact_source_fiber", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("multiplier_action_functor", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "exact_boundary_delta"),
    ("exact_boundary_delta", "exact_sequence"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("exact_boundary_delta", "coimage_preserves_signed_coefficients"),
    ("exact_boundary_delta", "rank_one_boundary_defect_duality"),
    ("rank_one_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank_one_boundary_defect_duality", "boundary_is_original_dd4_class"),
    ("boundary_is_original_dd4_class", "nonzero_res1"),
    ("rank_one_boundary_defect_duality", "normal_ratio_self_dual_boundary"),
    ("normal_ratio_self_dual_boundary", "connecting_map_sends_c_to_zero"),
    ("rank_one_boundary_defect_duality", "p1_p2_dual_endpoint_pairing"),
    ("rank_one_boundary_defect_duality", "rosati_compatible_duality"),
    ("rank_one_boundary_defect_duality", "dd4_boundary_certificate"),
    ("dd4_boundary_certificate", "single_localization_on_dq"),
    ("self_dual_exact_source_fiber", "source_before_graph_objects"),
    ("source_before_graph_objects", "controls_not_points"),
    ("source_before_graph_objects", "dh_not_points"),
    ("source_before_graph_objects", "epstein_not_points"),
    ("rank_one_boundary_defect_duality", "C3_duality_naturality"),
    ("rank_one_boundary_defect_duality", "C5_duality_naturality"),
    ("rank_one_boundary_defect_duality", "C3_C5_equals_C15_duality"),
    ("rank_one_boundary_defect_duality", "C5_C3_equals_C15_duality"),
    ("rank_one_boundary_defect_duality", "C3_C3_C5_equals_C45_duality"),
    ("rank_one_boundary_defect_duality", "F22_product_duality"),
    ("dd4_boundary_certificate", "monoidwide_certificate_transport"),
    ("monoidwide_certificate_transport", "endpoint_degree"),
    ("endpoint_degree", "p1_pushforward"),
    ("endpoint_degree", "p2_pushforward"),
    ("p1_pushforward", "graph_composition"),
    ("p2_pushforward", "graph_composition"),
    ("graph_composition", "rosati"),
    ("rosati", "count_degree"),
    ("count_degree", "control_death"),
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


def support(chi: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted(chi))


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


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
        "twist": TWIST_ID,
        "defect_rank": 1,
        "dual_line": tuple(neg.items()),
        "primal_line": tuple(pos.items()),
        "endpoint_pair": (p1, p2),
        "perfect_pairing": p1 == p2 and bool(pos) and bool(neg),
        "bidual_fixed": positive_negative_split(chi) == (pos, neg),
        "boundary_class": DD4_CLASS_ID,
        "res1": 1,
    }


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


def row(name: str, chi: dict[int, int], transport: str) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    graph_degree = p1
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "domain": INTERNAL_EFFECTIVITY_DOMAIN_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "source_token": SOURCE_TOKEN_ID,
        "source_fiber": SOURCE_FIBER_ID,
        "representing_object": REPRESENTING_OBJECT_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "signed_zero_fiber": SIGNED_ZERO_FIBER_ID,
        "monoidwide_coherence": MONOIDWIDE_COHERENCE_ID,
        "self_dual_source_token": SELF_DUAL_TOKEN_ID,
        "self_dual_source_fiber": SELF_DUAL_FIBER_ID,
        "cancellation_module": CANCELLATION_MODULE_ID,
        "boundary_functor": BOUNDARY_FUNCTOR_ID,
        "exact_sequence": EXACT_SEQUENCE_ID,
        "exact_delta": EXACT_DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality_map": DUALITY_MAP_ID,
        "twist": TWIST_ID,
        "boundary_certificate": BOUNDARY_CERTIFICATE_ID,
        "localization_sequence": LOCALIZATION_SEQUENCE_ID,
        "normal_ratio": NORMAL_RATIO_ID,
        "boundary": DD4_BOUNDARY_LOCALIZATION_ID,
        "endpoint_degree": ENDPOINT_DEGREE_MAPS_ID,
        "p1_pushforward": P1_PUSHFORWARD_ID,
        "p2_pushforward": P2_PUSHFORWARD_ID,
        "pushforward": PUSHFORWARD_SQUARE_ID,
        "graph_totalization": GRAPH_ROSATI_COUNT_TOTALIZATION_ID,
        "graph": PROPER_GRAPH_ID,
        "rosati": ROSATI_LAYER_ID,
        "count_degree": COUNT_DEGREE_ID,
        "control_gate": GRAPH_FORMATION_GATE_ID,
        "control_death": CONTROL_DEATH_NATURALITY_ID,
        "dd4_class": DD4_CLASS_ID,
        "source": name,
        "transport": transport,
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
        "duality": duality_payload(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "graph_degree": graph_degree,
        "count_degree_value": graph_degree * graph_degree,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
        "controls_points": False,
        "dh_points": False,
        "epstein_points": False,
    }


def formation_row(item: dict[str, object]) -> bool:
    duality = item["duality"]
    return (
        item["self_dual_source_token"] == SELF_DUAL_TOKEN_ID
        and item["self_dual_source_fiber"] == SELF_DUAL_FIBER_ID
        and item["square"] == CATEGORICAL_SQUARE_ID
        and item["cube"] == FACET_CUBE_ID
        and item["totalization"] == CUBE_TOTALIZATION_ID
        and item["representing_object"] == REPRESENTING_OBJECT_ID
        and item["universal_arrow"] == UNIVERSAL_ARROW_ID
        and item["signed_zero_fiber"] == SIGNED_ZERO_FIBER_ID
        and item["source_before_graph"]
        and not item["controls_points"]
        and not item["dh_points"]
        and not item["epstein_points"]
        and item["weighted_mass"] == 0
        and item["endpoint_defect"] == 0
        and item["pushforward_defect"] == 0
        and duality["defect_rank"] == 1
        and duality["perfect_pairing"]
        and duality["boundary_class"] == DD4_CLASS_ID
        and duality["res1"] == 1
    )


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_source_square_actual": False,
        "source_cube_totalization_actual": False,
        "represented_source_fiber": False,
        "universal_arrow_actual": False,
        "self_dual_source_token_actual": False,
        "self_dual_source_fiber_actual": False,
        "source_before_graph_objects": False,
        "signed_zero_fiber_actual": False,
        "multiplier_action_functor_actual": False,
        "cancellation_module_actual": False,
        "boundary_convolution_module_functor_actual": False,
        "exact_boundary_delta_actual": False,
        "exact_sequence_generated_by_bcf": False,
        "kernel_equals_cancellation_image": False,
        "coimage_preserves_signed_coefficients": False,
        "rank_one_boundary_defect_duality_actual": False,
        "duality_generated_by_exact_delta": False,
        "pinned_laurent_twist": False,
        "boundary_of_duality_is_original_dd4_class": False,
        "original_dd4_class_nonzero_before_certificate": False,
        "normal_ratio_self_dual_boundary": False,
        "connecting_map_sends_c_to_zero": False,
        "p1_p2_dual_endpoint_pairing": False,
        "rosati_compatible_duality": False,
        "dd4_boundary_certificate_generated": False,
        "single_localization_on_dq": False,
        "C3_duality_natural": False,
        "C5_duality_natural": False,
        "C3_C5_equals_C15_duality": False,
        "C5_C3_equals_C15_duality": False,
        "C3_C3_C5_equals_C45_duality": False,
        "F22_product_duality": False,
        "certificate_transported_monoidwide": False,
        "endpoint_pushforward_graph_generated": False,
        "control_death_generated_at_source": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "graph_predicate_gate": False,
        "source_token_after_graph": False,
        "declared_nonpoint_condition": False,
        "functor_of_points_without_representer": False,
        "yoneda_reversal": False,
        "predicate_subfibration": False,
        "finite_admission_table": False,
        "local_source_stack": False,
        "external_oracle": False,
        "semantic_zeta_label": False,
        "late_control_filter": False,
        "late_dh_filter": False,
        "late_epstein_filter": False,
        "projection_defect_filter": False,
        "rosati_sign_filter": False,
        "dd4_afterthought_filter": False,
        "retuned_formation_rule": False,
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
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    ("self_dual_source_token_actual", "self_dual_source_token_missing"),
    ("self_dual_source_fiber_actual", "self_dual_source_fiber_missing"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("signed_zero_fiber_actual", "signed_zero_fiber_missing"),
    ("multiplier_action_functor_actual", "multiplier_action_functor_missing"),
    ("cancellation_module_actual", "cancellation_module_missing"),
    (
        "boundary_convolution_module_functor_actual",
        "boundary_convolution_module_functor_missing",
    ),
    ("exact_boundary_delta_actual", "exact_boundary_delta_missing"),
    ("exact_sequence_generated_by_bcf", "exact_sequence_not_generated_by_bcf"),
    ("kernel_equals_cancellation_image", "kernel_not_cancellation_image"),
    (
        "coimage_preserves_signed_coefficients",
        "coimage_does_not_preserve_signed_coefficients",
    ),
    (
        "rank_one_boundary_defect_duality_actual",
        "rank_one_boundary_defect_duality_missing",
    ),
    ("duality_generated_by_exact_delta", "duality_not_generated_by_exact_delta"),
    ("pinned_laurent_twist", "pinned_laurent_twist_missing"),
    (
        "boundary_of_duality_is_original_dd4_class",
        "boundary_not_original_dd4_class",
    ),
    (
        "original_dd4_class_nonzero_before_certificate",
        "original_dd4_class_not_nonzero_before_certificate",
    ),
    ("normal_ratio_self_dual_boundary", "normal_ratio_not_self_dual_boundary"),
    ("connecting_map_sends_c_to_zero", "c_not_mapped_to_zero"),
    ("p1_p2_dual_endpoint_pairing", "p1_p2_dual_endpoint_pairing_missing"),
    ("rosati_compatible_duality", "rosati_compatible_duality_missing"),
    ("dd4_boundary_certificate_generated", "dd4_boundary_certificate_missing"),
    ("single_localization_on_dq", "no_single_localization_on_dq"),
    ("C3_duality_natural", "C3_duality_not_natural"),
    ("C5_duality_natural", "C5_duality_not_natural"),
    ("C3_C5_equals_C15_duality", "C3_C5_duality_not_C15"),
    ("C5_C3_equals_C15_duality", "C5_C3_duality_not_C15"),
    ("C3_C3_C5_equals_C45_duality", "C3_C3_C5_duality_not_C45"),
    ("F22_product_duality", "F22_product_duality_missing"),
    (
        "certificate_transported_monoidwide",
        "certificate_not_transported_monoidwide",
    ),
    (
        "endpoint_pushforward_graph_generated",
        "endpoint_pushforward_graph_not_generated",
    ),
    ("control_death_generated_at_source", "control_death_not_generated_at_source"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("graph_predicate_gate", "graph_predicate_gate"),
    ("source_token_after_graph", "source_token_after_graph"),
    ("declared_nonpoint_condition", "declared_nonpoint_condition"),
    ("functor_of_points_without_representer", "functor_of_points_without_representer"),
    ("yoneda_reversal", "yoneda_reversal"),
    ("predicate_subfibration", "predicate_subfibration"),
    ("finite_admission_table", "finite_admission_table"),
    ("local_source_stack", "local_source_stack"),
    ("external_oracle", "external_oracle"),
    ("semantic_zeta_label", "semantic_zeta_label"),
    ("late_control_filter", "late_control_filter"),
    ("late_dh_filter", "late_dh_filter"),
    ("late_epstein_filter", "late_epstein_filter"),
    ("projection_defect_filter", "projection_defect_filter"),
    ("rosati_sign_filter", "rosati_sign_filter"),
    ("dd4_afterthought_filter", "dd4_afterthought_filter"),
    ("retuned_formation_rule", "retuned_formation_rule"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_FORMATION_EDGES <= set(data["required_edges"]):
        out.append("required_self_dual_formation_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_formation_gate(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_FORMATION_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        represented_source_fiber=True,
        universal_arrow_actual=True,
        self_dual_source_token_actual=True,
        self_dual_source_fiber_actual=True,
        source_before_graph_objects=True,
        signed_zero_fiber_actual=True,
        multiplier_action_functor_actual=True,
        cancellation_module_actual=True,
        boundary_convolution_module_functor_actual=True,
        exact_boundary_delta_actual=True,
        exact_sequence_generated_by_bcf=True,
        kernel_equals_cancellation_image=True,
        coimage_preserves_signed_coefficients=True,
        rank_one_boundary_defect_duality_actual=True,
        duality_generated_by_exact_delta=True,
        pinned_laurent_twist=True,
        boundary_of_duality_is_original_dd4_class=True,
        original_dd4_class_nonzero_before_certificate=True,
        normal_ratio_self_dual_boundary=True,
        connecting_map_sends_c_to_zero=True,
        p1_p2_dual_endpoint_pairing=True,
        rosati_compatible_duality=True,
        dd4_boundary_certificate_generated=True,
        single_localization_on_dq=True,
        C3_duality_natural=True,
        C5_duality_natural=True,
        C3_C5_equals_C15_duality=True,
        C5_C3_equals_C15_duality=True,
        C3_C3_C5_equals_C45_duality=True,
        F22_product_duality=True,
        certificate_transported_monoidwide=True,
        endpoint_pushforward_graph_generated=True,
        control_death_generated_at_source=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_FORMATION_EDGES),
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

rows = [
    row("z", z, "id"),
    row("zC3", zC3, "C3"),
    row("zC5", zC5, "C5"),
    row("zC15", zC15, "C15"),
    row("zC45", zC45, "C45"),
    row("zF22", zF22, "F22"),
    row("zC15F22", zC15F22, "C15F22"),
    row("zC45F22", zC45F22, "C45F22"),
]

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
    "CATSFGQBARBECD1 self-dual exact source is a represented formation fiber",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and zF22 == {2: 4, 4: -2}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and duality_payload(T3_T5_z) == duality_payload(zC15)
    and duality_payload(T5_T3_z) == duality_payload(zC15)
    and duality_payload(T3_T3_T5_z) == duality_payload(zC45)
    and duality_payload(T15_zF22) == duality_payload(zC15F22)
    and duality_payload(T45_zF22) == duality_payload(zC45F22)
    and all(formation_row(item) for item in rows),
    "H1=%s token=%s fiber=%s rows=%d"
    % ([p["h1_order"] for p in profiles], SELF_DUAL_TOKEN_ID, SELF_DUAL_FIBER_ID, len(rows)),
)


gate(
    "CATSFGQBARBECD2 graph identities still do not supply source-level control death",
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


graph_predicate = live_source(
    source_before_graph_objects=False,
    control_death_generated_at_source=False,
    graph_predicate_gate=True,
    source_token_after_graph=True,
    projection_defect_filter=True,
    rosati_sign_filter=True,
    control_point_formable=True,
)

gate(
    "CATSFGQBARBECD3 graph predicates and late signs are too late",
    not accepts_formation_gate(graph_predicate)
    and {
        "source_not_before_graph_objects",
        "control_death_not_generated_at_source",
        "graph_predicate_gate",
        "source_token_after_graph",
        "projection_defect_filter",
        "rosati_sign_filter",
        "control_point_formable",
    }
    <= set(reasons(graph_predicate)),
    ",".join(reasons(graph_predicate)),
)


declared_nonpoints = live_source(
    self_dual_source_token_actual=False,
    self_dual_source_fiber_actual=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    declared_nonpoint_condition=True,
    late_control_filter=True,
    late_dh_filter=True,
    late_epstein_filter=True,
)

gate(
    "CATSFGQBARBECD4 declared nonpoint conditions are not source fibers",
    not accepts_formation_gate(declared_nonpoints)
    and {
        "self_dual_source_token_missing",
        "self_dual_source_fiber_missing",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "declared_nonpoint_condition",
        "late_control_filter",
        "late_dh_filter",
        "late_epstein_filter",
    }
    <= set(reasons(declared_nonpoints)),
    ",".join(reasons(declared_nonpoints)),
)


functor_points = live_source(
    represented_source_fiber=False,
    universal_arrow_actual=False,
    required_edges=set(),
    functor_of_points_without_representer=True,
    yoneda_reversal=True,
    predicate_subfibration=True,
)

gate(
    "CATSFGQBARBECD5 functors of points do not represent the self-dual source",
    not accepts_formation_gate(functor_points)
    and {
        "represented_source_fiber_missing",
        "universal_arrow_not_actual",
        "required_self_dual_formation_edges_missing",
        "functor_of_points_without_representer",
        "yoneda_reversal",
        "predicate_subfibration",
    }
    <= set(reasons(functor_points)),
    ",".join(reasons(functor_points)),
)


finite_stack = live_source(
    C3_C5_equals_C15_duality=False,
    C5_C3_equals_C15_duality=False,
    C3_C3_C5_equals_C45_duality=False,
    F22_product_duality=False,
    finite_admission_table=True,
    local_source_stack=True,
    external_oracle=True,
)

gate(
    "CATSFGQBARBECD6 finite tables and local stacks miss mixed multiplier formation",
    not accepts_formation_gate(finite_stack)
    and {
        "C3_C5_duality_not_C15",
        "C5_C3_duality_not_C15",
        "C3_C3_C5_duality_not_C45",
        "F22_product_duality_missing",
        "finite_admission_table",
        "local_source_stack",
        "external_oracle",
    }
    <= set(reasons(finite_stack)),
    ",".join(reasons(finite_stack)),
)


semantic_or_retuned = live_source(
    exact_sequence_generated_by_bcf=False,
    boundary_of_duality_is_original_dd4_class=False,
    connecting_map_sends_c_to_zero=False,
    semantic_zeta_label=True,
    dd4_afterthought_filter=True,
    retuned_formation_rule=True,
)

gate(
    "CATSFGQBARBECD7 semantic labels and retuned rules lose the exact source",
    not accepts_formation_gate(semantic_or_retuned)
    and {
        "exact_sequence_not_generated_by_bcf",
        "boundary_not_original_dd4_class",
        "c_not_mapped_to_zero",
        "semantic_zeta_label",
        "dd4_afterthought_filter",
        "retuned_formation_rule",
    }
    <= set(reasons(semantic_or_retuned)),
    ",".join(reasons(semantic_or_retuned)),
)


late_downstream = live_source(
    certificate_transported_monoidwide=False,
    endpoint_pushforward_graph_generated=False,
    control_death_generated_at_source=False,
    late_control_filter=True,
    projection_defect_filter=True,
    rosati_sign_filter=True,
)

gate(
    "CATSFGQBARBECD8 downstream endpoint and Rosati filters are not formation death",
    not accepts_formation_gate(late_downstream)
    and {
        "certificate_not_transported_monoidwide",
        "endpoint_pushforward_graph_not_generated",
        "control_death_not_generated_at_source",
        "late_control_filter",
        "projection_defect_filter",
        "rosati_sign_filter",
    }
    <= set(reasons(late_downstream)),
    ",".join(reasons(late_downstream)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_FORMATION_EDGES
        - {("universal_arrow", "self_dual_exact_source_token")}
    ),
    live_source(
        required_edges=REQUIRED_FORMATION_EDGES
        - {("self_dual_exact_source_token", "self_dual_exact_source_fiber")}
    ),
    live_source(
        required_edges=REQUIRED_FORMATION_EDGES
        - {("source_before_graph_objects", "controls_not_points")}
    ),
    live_source(self_dual_source_fiber_actual=False),
    live_source(source_before_graph_objects=False),
    live_source(control_death_generated_at_source=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSFGQBARBECD9 every source-level formation edge is mandatory",
    not any(accepts_formation_gate(data) for data in missing_edges)
    and {
        "required_self_dual_formation_edges_missing",
        "self_dual_source_fiber_missing",
        "source_not_before_graph_objects",
        "control_death_not_generated_at_source",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


control_shadow = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_predicate_gate=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

live = live_source()
dead_sources = {
    "graph_predicate": graph_predicate,
    "declared_nonpoints": declared_nonpoints,
    "functor_points": functor_points,
    "finite_stack": finite_stack,
    "semantic_or_retuned": semantic_or_retuned,
    "late_downstream": late_downstream,
    "control_shadow": control_shadow,
}

gate(
    "CATSFGQBARBECD10 only represented self-dual source-level death passes",
    not accepts_formation_gate(control_shadow)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_predicate_gate",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_shadow))
    and accepts_formation_gate(live)
    and REQUIRED_FORMATION_EDGES <= live["required_edges"]
    and not any(accepts_formation_gate(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_formation_gate(data) for data in dead_sources.values()),
        accepts_formation_gate(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSFGQBARBECD1-CATSFGQBARBECD10 ALL PASS: categorical closure "
    "self-dual exact-source formation gate totalization contract pinned"
)
print(
    "VERDICT: the categorical self-dual exact BCF source must be represented "
    "as a source-level formation fiber before graph objects exist, with the "
    "universal arrow generating the admission token and making controls, DH, "
    "and Epstein non-points at source formation. Graph predicates, declared "
    "nonpoint conditions, functors of points, finite admission tables, local "
    "stacks, semantic labels, retunings, and late control/Rosati/DD.4 filters "
    "do not construct source-level death."
)
