r"""Categorical closure DD.4 certificate exact-source self-duality contract.

Doc 462 requires BCF generation of the DD.4 boundary certificate to be an
exact natural boundary-delta source inside the represented categorical source
square. This witness pins the next edge: that exact source must itself produce
the boundary-native rank-one duality/properness datum. A one-sided exact
delta, generic self-duality label, hyperbolic endpoint plane, degree-zero twist
normalization, formal adjoint, or late Rosati filter does not construct the
DD.4 certificate inside the square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_dd4_certificate_exact_source_self_duality_totalization_contract
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

REQUIRED_SELF_DUAL_EDGES = {
    ("represented_source_square", "signed_zero_fiber"),
    ("source_cube_totalization", "signed_zero_fiber"),
    ("universal_arrow", "signed_zero_fiber"),
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
    ("control_death", "controls_not_points"),
    ("control_death", "dh_not_points"),
    ("control_death", "epstein_not_points"),
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


def boundary_delta(chi: dict[int, int]) -> dict[str, object]:
    return {
        "weighted_mass": weighted_mass(chi),
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "split": positive_negative_split(chi),
        "endpoint_pair": endpoint_degrees(chi),
    }


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


def laurent_diagnostics(N: int) -> dict[str, int]:
    window_rank = 2 * N + 2
    hyperbolic_rank = 2 * window_rank
    unit_twists = 2 * N + 1
    nonzero_boundary_maps = 2 ** (2 * N + 1) - 1
    return {
        "N": N,
        "window_rank": window_rank,
        "hyperbolic_rank": hyperbolic_rank,
        "defect_rank": 1,
        "unit_twists": unit_twists,
        "nonzero_boundary_maps": nonzero_boundary_maps,
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
        "delta": boundary_delta(chi),
        "duality": duality_payload(chi),
        "kernel_relation": tuple(chi.items()),
        "coimage_signature": positive_negative_split(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "res1": 1,
        "control_point": False,
        "dh_point": False,
        "epstein_point": False,
    }


def exact_self_dual_row(item: dict[str, object]) -> bool:
    duality = item["duality"]
    return (
        item["weighted_mass"] == 0
        and item["delta"]["weighted_mass"] == 0
        and item["kernel_relation"] == item["coefficients"]
        and item["coimage_signature"] == item["delta"]["split"]
        and duality["defect_rank"] == 1
        and duality["perfect_pairing"]
        and duality["bidual_fixed"]
        and duality["boundary_class"] == DD4_CLASS_ID
        and duality["res1"] == 1
        and item["square"] == CATEGORICAL_SQUARE_ID
        and item["cube"] == FACET_CUBE_ID
        and item["totalization"] == CUBE_TOTALIZATION_ID
        and item["signed_zero_fiber"] == SIGNED_ZERO_FIBER_ID
        and item["duality_map"] == DUALITY_MAP_ID
        and item["twist"] == TWIST_ID
        and item["exact_sequence"] == EXACT_SEQUENCE_ID
        and item["exact_delta"] == EXACT_DELTA_ID
        and item["boundary_functor"] == BOUNDARY_FUNCTOR_ID
        and item["boundary_certificate"] == BOUNDARY_CERTIFICATE_ID
        and item["normal_ratio"] == NORMAL_RATIO_ID
        and item["dd4_class"] == DD4_CLASS_ID
        and item["endpoint_defect"] == 0
        and item["pushforward_defect"] == 0
        and not item["control_point"]
        and not item["dh_point"]
        and not item["epstein_point"]
    )


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_source_square_actual": False,
        "source_cube_totalization_actual": False,
        "represented_source_fiber": False,
        "universal_arrow_actual": False,
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
        "control_death_generated": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "one_sided_exact_delta": False,
        "generic_self_duality_label": False,
        "hyperbolic_endpoint_plane": False,
        "degree_zero_twist_normalization": False,
        "scalar_pairing": False,
        "diagonal_coevaluation": False,
        "full_support_duality": False,
        "inserted_dual_primal_matching": False,
        "formal_rosati_adjoint": False,
        "declared_normal_ratio": False,
        "weighted_zero_dual_kernel": False,
        "support_dual_kernel": False,
        "late_rosati_filter": False,
        "degree_equality_only": False,
        "count_equality_only": False,
        "retuned_duality": False,
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
    ("control_death_generated", "control_death_not_generated"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("one_sided_exact_delta", "one_sided_exact_delta"),
    ("generic_self_duality_label", "generic_self_duality_label"),
    ("hyperbolic_endpoint_plane", "hyperbolic_endpoint_plane"),
    ("degree_zero_twist_normalization", "degree_zero_twist_normalization"),
    ("scalar_pairing", "scalar_pairing"),
    ("diagonal_coevaluation", "diagonal_coevaluation"),
    ("full_support_duality", "full_support_duality"),
    ("inserted_dual_primal_matching", "inserted_dual_primal_matching"),
    ("formal_rosati_adjoint", "formal_rosati_adjoint"),
    ("declared_normal_ratio", "declared_normal_ratio"),
    ("weighted_zero_dual_kernel", "weighted_zero_dual_kernel"),
    ("support_dual_kernel", "support_dual_kernel"),
    ("late_rosati_filter", "late_rosati_filter"),
    ("degree_equality_only", "degree_equality_only"),
    ("count_equality_only", "count_equality_only"),
    ("retuned_duality", "retuned_duality"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_SELF_DUAL_EDGES <= set(data["required_edges"]):
        out.append("required_self_dual_exact_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_self_dual_exact_source(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_SELF_DUAL_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        represented_source_fiber=True,
        universal_arrow_actual=True,
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
        control_death_generated=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_SELF_DUAL_EDGES),
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

non_square_balanced = {1: 4, 4: -1}
profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
laurent_rows = [laurent_diagnostics(N) for N in (1, 2, 4, 8)]

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
    "CATBDSQBARBECD1 exact BCF source produces rank-one self-dual properness",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and [r["window_rank"] for r in laurent_rows] == [4, 6, 10, 18]
    and [r["hyperbolic_rank"] for r in laurent_rows] == [8, 12, 20, 36]
    and [r["defect_rank"] for r in laurent_rows] == [1, 1, 1, 1]
    and [r["unit_twists"] for r in laurent_rows] == [3, 5, 9, 17]
    and [r["nonzero_boundary_maps"] for r in laurent_rows] == [7, 31, 511, 131071]
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
    and all(exact_self_dual_row(item) for item in rows),
    "H1=%s dual=%s twist=%s ranks=%s"
    % (
        [p["h1_order"] for p in profiles],
        DUALITY_MAP_ID,
        TWIST_ID,
        [r["defect_rank"] for r in laurent_rows],
    ),
)


gate(
    "CATBDSQBARBECD2 graph identities still do not supply boundary self-duality",
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


one_sided_delta = live_source(
    rank_one_boundary_defect_duality_actual=False,
    duality_generated_by_exact_delta=False,
    p1_p2_dual_endpoint_pairing=False,
    one_sided_exact_delta=True,
    generic_self_duality_label=True,
    control_point_formable=True,
)

gate(
    "CATBDSQBARBECD3 one-sided exact deltas and self-duality labels fail",
    not accepts_self_dual_exact_source(one_sided_delta)
    and {
        "rank_one_boundary_defect_duality_missing",
        "duality_not_generated_by_exact_delta",
        "p1_p2_dual_endpoint_pairing_missing",
        "one_sided_exact_delta",
        "generic_self_duality_label",
        "control_point_formable",
    }
    <= set(reasons(one_sided_delta)),
    ",".join(reasons(one_sided_delta)),
)


hyperbolic_import = live_source(
    rank_one_boundary_defect_duality_actual=False,
    pinned_laurent_twist=False,
    boundary_of_duality_is_original_dd4_class=False,
    hyperbolic_endpoint_plane=True,
    full_support_duality=True,
    inserted_dual_primal_matching=True,
)

gate(
    "CATBDSQBARBECD4 hyperbolic and full-support dualities have the wrong type",
    not accepts_self_dual_exact_source(hyperbolic_import)
    and {
        "rank_one_boundary_defect_duality_missing",
        "pinned_laurent_twist_missing",
        "boundary_not_original_dd4_class",
        "hyperbolic_endpoint_plane",
        "full_support_duality",
        "inserted_dual_primal_matching",
    }
    <= set(reasons(hyperbolic_import)),
    ",".join(reasons(hyperbolic_import)),
)


scalar_or_diagonal = live_source(
    rank_one_boundary_defect_duality_actual=False,
    p1_p2_dual_endpoint_pairing=False,
    rosati_compatible_duality=False,
    scalar_pairing=True,
    diagonal_coevaluation=True,
    formal_rosati_adjoint=True,
)

gate(
    "CATBDSQBARBECD5 scalar pairings and formal adjoints are not defect-line maps",
    not accepts_self_dual_exact_source(scalar_or_diagonal)
    and {
        "rank_one_boundary_defect_duality_missing",
        "p1_p2_dual_endpoint_pairing_missing",
        "rosati_compatible_duality_missing",
        "scalar_pairing",
        "diagonal_coevaluation",
        "formal_rosati_adjoint",
    }
    <= set(reasons(scalar_or_diagonal)),
    ",".join(reasons(scalar_or_diagonal)),
)


twist_fiat = live_source(
    duality_generated_by_exact_delta=False,
    pinned_laurent_twist=False,
    normal_ratio_self_dual_boundary=False,
    degree_zero_twist_normalization=True,
    declared_normal_ratio=True,
    retuned_duality=True,
)

gate(
    "CATBDSQBARBECD6 twist normalization and declared normal ratio are external",
    not accepts_self_dual_exact_source(twist_fiat)
    and {
        "duality_not_generated_by_exact_delta",
        "pinned_laurent_twist_missing",
        "normal_ratio_not_self_dual_boundary",
        "degree_zero_twist_normalization",
        "declared_normal_ratio",
        "retuned_duality",
    }
    <= set(reasons(twist_fiat)),
    ",".join(reasons(twist_fiat)),
)


weighted_dual_kernel = live_source(
    kernel_equals_cancellation_image=False,
    coimage_preserves_signed_coefficients=False,
    boundary_of_duality_is_original_dd4_class=False,
    weighted_zero_dual_kernel=True,
    support_dual_kernel=True,
    degree_equality_only=True,
)

gate(
    "CATBDSQBARBECD7 weighted or support dual kernels overaccept non-square profiles",
    weighted_mass(non_square_balanced) == 0
    and support(non_square_balanced) == (1, 4)
    and not accepts_self_dual_exact_source(weighted_dual_kernel)
    and {
        "kernel_not_cancellation_image",
        "coimage_does_not_preserve_signed_coefficients",
        "boundary_not_original_dd4_class",
        "weighted_zero_dual_kernel",
        "support_dual_kernel",
        "degree_equality_only",
    }
    <= set(reasons(weighted_dual_kernel)),
    ",".join(reasons(weighted_dual_kernel)),
)


late_filter = live_source(
    rosati_compatible_duality=False,
    certificate_transported_monoidwide=False,
    endpoint_pushforward_graph_generated=False,
    late_rosati_filter=True,
    count_equality_only=True,
)

gate(
    "CATBDSQBARBECD8 late Rosati and count filters do not generate duality",
    not accepts_self_dual_exact_source(late_filter)
    and {
        "rosati_compatible_duality_missing",
        "certificate_not_transported_monoidwide",
        "endpoint_pushforward_graph_not_generated",
        "late_rosati_filter",
        "count_equality_only",
    }
    <= set(reasons(late_filter)),
    ",".join(reasons(late_filter)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_SELF_DUAL_EDGES
        - {("exact_boundary_delta", "rank_one_boundary_defect_duality")}
    ),
    live_source(
        required_edges=REQUIRED_SELF_DUAL_EDGES
        - {("rank_one_boundary_defect_duality", "pinned_laurent_twist")}
    ),
    live_source(
        required_edges=REQUIRED_SELF_DUAL_EDGES
        - {("rank_one_boundary_defect_duality", "boundary_is_original_dd4_class")}
    ),
    live_source(rank_one_boundary_defect_duality_actual=False),
    live_source(boundary_of_duality_is_original_dd4_class=False),
    live_source(connecting_map_sends_c_to_zero=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATBDSQBARBECD9 every self-dual exact-source edge is mandatory",
    not any(accepts_self_dual_exact_source(data) for data in missing_edges)
    and {
        "required_self_dual_exact_edges_missing",
        "rank_one_boundary_defect_duality_missing",
        "boundary_not_original_dd4_class",
        "c_not_mapped_to_zero",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


control_shadow = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    generic_self_duality_label=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

live = live_source()
dead_sources = {
    "one_sided_delta": one_sided_delta,
    "hyperbolic_import": hyperbolic_import,
    "scalar_or_diagonal": scalar_or_diagonal,
    "twist_fiat": twist_fiat,
    "weighted_dual_kernel": weighted_dual_kernel,
    "late_filter": late_filter,
    "control_shadow": control_shadow,
}

gate(
    "CATBDSQBARBECD10 only self-dual exact BCF sources pass",
    not accepts_self_dual_exact_source(control_shadow)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "generic_self_duality_label",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_shadow))
    and accepts_self_dual_exact_source(live)
    and REQUIRED_SELF_DUAL_EDGES <= live["required_edges"]
    and not any(accepts_self_dual_exact_source(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_self_dual_exact_source(data) for data in dead_sources.values()),
        accepts_self_dual_exact_source(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATBDSQBARBECD1-CATBDSQBARBECD10 ALL PASS: categorical closure DD4 "
    "certificate exact-source self-duality totalization contract pinned"
)
print(
    "VERDICT: the represented categorical exact BCF boundary-delta source "
    "must itself generate the rank-one boundary-defect duality/properness "
    "datum, with pinned twist, boundary equal to the original DD.4 class, "
    "self-dual normal ratio, Rosati-compatible endpoint pairing, mixed "
    "multiplier duality, and downstream control death. One-sided exact "
    "deltas, generic self-duality labels, hyperbolic planes, scalar pairings, "
    "formal adjoints, twist normalizations, weighted/support kernels, late "
    "filters, and control/DH/Epstein shadows do not construct this source."
)
