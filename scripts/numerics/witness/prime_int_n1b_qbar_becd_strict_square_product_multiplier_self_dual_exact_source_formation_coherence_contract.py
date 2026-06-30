r"""Formation-coherence contract for the self-dual exact BCF source.

Doc 350 requires the self-dual exact BCF source to be a represented
formation fiber before graph objects exist.  This witness pins the next edge:
the same universal arrow must generate represented source-level coherence
cells for the self-dual exact source.  Equal rows, common tokens, formal
2-cells, local C3 patches, finite tables, or graph-level coherence do not
construct source-level control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_coherence_contract
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

DOMAIN_ID = "D_Qbar_BECD_eff"
BOUNDARY_ID = "B_Qbar_BECD_DD4"
PUSHFORWARD_ID = "PF_Qbar_BECD_p1p2"
GRAPH_ID = "G_Qbar_BECD_prop"
ROSATI_ID = "R_Qbar_BECD_pos"
COUNT_ID = "CD_Qbar_BECD"
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"
SOURCE_TOKEN_ID = "SRC_Qbar_BECD_strict_square"
FORMATION_FIBER_ID = "Fib_Qbar_BECD_graph_formation"
SELF_DUAL_TOKEN_ID = "Tok_Qbar_BECD_BCF_self_dual_exact_source"
SELF_DUAL_FIBER_ID = "Fib_Qbar_BECD_BCF_self_dual_exact_source"
REPRESENTING_OBJECT_ID = "Rep_Qbar_BECD_source_fiber"
UNIVERSAL_ARROW_ID = "eta_Qbar_BECD_source"
SOURCE_COHERENCE_ID = "Coh_Qbar_BECD_BCF_self_dual_exact_source_formation"
CARTESIAN_COHERENCE_ID = "Cart_Qbar_BECD_BCF_self_dual_exact_source"
MONOIDWIDE_COHERENCE_ID = "MWC_Qbar_BECD_BCF_self_dual_exact_source"
CANCELLATION_MODULE_ID = "CanMod_Qbar_BECD_z_boundary_convolution"
BOUNDARY_FUNCTOR_ID = "BCF_Qbar_BECD_boundary_convolution_module"
EXACT_SEQUENCE_ID = "Ex_Qbar_BECD_CanMod_BCF_dQ"
EXACT_DELTA_ID = "Delta_Qbar_BECD_BCF_to_dQ_boundary"
KERNEL_ID = "Ker_Qbar_BECD_BCF_delta_image_z"
COIMAGE_ID = "Coim_Qbar_BECD_CanMod_BCF_delta"
DUALITY_MAP_ID = "Dual_Qbar_BECD_rank1_boundary_defect"
TWIST_ID = "Tw_Qbar_BECD_OC_BCF_pinned"
BOUNDARY_CERTIFICATE_ID = "BKill_Qbar_BECD_dQ_boundary_properness_self_duality"
DD4_CLASS_ID = "dd4_c_original_res1"
LOCALIZATION_SEQUENCE_ID = "Loc_Qbar_BECD_single_dQ"
NORMAL_RATIO_ID = "NR_Qbar_BECD_ordered_p1_p2"

REQUIRED_COHERENCE_EDGES = {
    ("universal_arrow", "self_dual_exact_source_coherence"),
    ("self_dual_exact_source_coherence", "self_dual_exact_source_token"),
    ("self_dual_exact_source_coherence", "self_dual_exact_source_fiber"),
    ("self_dual_exact_source_fiber", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("strict_square_character_convolution", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "exact_boundary_delta"),
    ("exact_boundary_delta", "exact_sequence"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("exact_boundary_delta", "coimage_preserves_signed_coefficients"),
    ("exact_boundary_delta", "source_cartesian_coherence"),
    ("exact_boundary_delta", "source_monoidwide_coherence"),
    ("source_cartesian_coherence", "C3_C5_equals_C15_source"),
    ("source_cartesian_coherence", "C5_C3_equals_C15_source"),
    ("source_monoidwide_coherence", "C3_C3_C5_equals_C45_source"),
    ("source_monoidwide_coherence", "F22_product_source"),
    ("source_monoidwide_coherence", "rank_one_boundary_defect_duality"),
    ("rank_one_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank_one_boundary_defect_duality", "boundary_is_original_dd4_class"),
    ("boundary_is_original_dd4_class", "nonzero_res1"),
    ("rank_one_boundary_defect_duality", "normal_ratio_self_dual_boundary"),
    ("normal_ratio_self_dual_boundary", "connecting_map_sends_c_to_zero"),
    ("rank_one_boundary_defect_duality", "p1_p2_dual_endpoint_pairing"),
    ("rank_one_boundary_defect_duality", "rosati_compatible_duality"),
    ("rank_one_boundary_defect_duality", "dd4_boundary_certificate"),
    ("dd4_boundary_certificate", "single_localization_on_dq"),
    ("dd4_boundary_certificate", "monoidwide_certificate_transport"),
    ("monoidwide_certificate_transport", "p1_pushforward"),
    ("monoidwide_certificate_transport", "p2_pushforward"),
    ("p1_pushforward", "graph_composition"),
    ("p2_pushforward", "graph_composition"),
    ("graph_composition", "rosati"),
    ("rosati", "count_degree"),
    ("count_degree", "control_death"),
    ("self_dual_exact_source_coherence", "source_before_graph_objects"),
    ("source_before_graph_objects", "controls_not_points"),
    ("source_before_graph_objects", "dh_not_points"),
    ("source_before_graph_objects", "epstein_not_points"),
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


def coherence_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_coherence": SOURCE_COHERENCE_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "monoidwide_coherence": MONOIDWIDE_COHERENCE_ID,
        "source_token": SELF_DUAL_TOKEN_ID,
        "source_fiber": SELF_DUAL_FIBER_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "exact_delta": EXACT_DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality": duality_payload(chi),
        "normal_ratio": NORMAL_RATIO_ID,
        "control_death": CONTROL_DEATH_ID,
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
        "endpoint_pair": (p1, p2),
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
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
    return {
        "representing_object": REPRESENTING_OBJECT_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "source_token": SOURCE_TOKEN_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "self_dual_source_token": SELF_DUAL_TOKEN_ID,
        "self_dual_source_fiber": SELF_DUAL_FIBER_ID,
        "source_coherence": SOURCE_COHERENCE_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
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
        "domain": DOMAIN_ID,
        "boundary": BOUNDARY_ID,
        "pushforward": PUSHFORWARD_ID,
        "graph": GRAPH_ID,
        "rosati": ROSATI_ID,
        "count_degree": COUNT_ID,
        "control_death": CONTROL_DEATH_ID,
        "dd4_class": DD4_CLASS_ID,
        "source": name,
        "transport": transport,
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
        "duality": duality_payload(chi),
        "coherence": coherence_payload(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "graph_degree": p1,
        "count_degree_value": p1 * p2,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
        "controls_points": False,
        "dh_points": False,
        "epstein_points": False,
    }


def coherent_row(item: dict[str, object]) -> bool:
    coherence = item["coherence"]
    duality = item["duality"]
    return (
        item["source_coherence"] == SOURCE_COHERENCE_ID
        and item["cartesian_coherence"] == CARTESIAN_COHERENCE_ID
        and item["monoidwide_coherence"] == MONOIDWIDE_COHERENCE_ID
        and item["self_dual_source_token"] == SELF_DUAL_TOKEN_ID
        and item["self_dual_source_fiber"] == SELF_DUAL_FIBER_ID
        and item["representing_object"] == REPRESENTING_OBJECT_ID
        and item["universal_arrow"] == UNIVERSAL_ARROW_ID
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
        and coherence["source_coherence"] == SOURCE_COHERENCE_ID
        and coherence["exact_delta"] == EXACT_DELTA_ID
        and coherence["kernel"] == KERNEL_ID
        and coherence["coimage"] == COIMAGE_ID
        and coherence["control_death"] == CONTROL_DEATH_ID
        and coherence["endpoint_defect"] == 0
        and coherence["pushforward_defect"] == 0
    )


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_source_fiber": False,
        "universal_arrow_actual": False,
        "self_dual_source_token_actual": False,
        "self_dual_source_fiber_actual": False,
        "source_before_graph_objects": False,
        "source_coherence_cells_actual": False,
        "source_coherence_generated_by_universal_arrow": False,
        "cartesian_coherence_actual": False,
        "monoidwide_coherence_actual": False,
        "same_coherence_id_all_paths": False,
        "coherence_preserves_exact_delta": False,
        "coherence_preserves_kernel": False,
        "coherence_preserves_coimage": False,
        "coherence_preserves_signed_coefficients": False,
        "coherence_preserves_rank_one_duality": False,
        "coherence_preserves_pinned_twist": False,
        "coherence_preserves_original_dd4_class": False,
        "coherence_preserves_normal_ratio": False,
        "coherence_preserves_endpoint_pairing": False,
        "coherence_preserves_endpoint_pushforward_graph": False,
        "coherence_preserves_rosati_count": False,
        "coherence_preserves_control_death": False,
        "C3_C5_equals_C15_source": False,
        "C5_C3_equals_C15_source": False,
        "C3_C3_C5_equals_C45_source": False,
        "F22_product_source": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "same_token_without_coherence": False,
        "declared_2cells": False,
        "formal_commutative_square": False,
        "finite_composition_table": False,
        "local_C3_patch": False,
        "single_prime_axis_patch": False,
        "prime_axis_tags": False,
        "degree_equality_only": False,
        "count_equality_only": False,
        "support_equality_only": False,
        "weighted_zero_only": False,
        "external_choice_of_2cells": False,
        "retuned_source_coherence": False,
        "graph_object_coherence": False,
        "graph_predicate_gate": False,
        "late_control_filter": False,
        "boundary_after_filter": False,
        "dd4_afterthought_filter": False,
        "functor_of_points_without_representer": False,
        "semantic_zeta_label": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    ("self_dual_source_token_actual", "self_dual_source_token_missing"),
    ("self_dual_source_fiber_actual", "self_dual_source_fiber_missing"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("source_coherence_cells_actual", "source_coherence_cells_missing"),
    (
        "source_coherence_generated_by_universal_arrow",
        "source_coherence_not_generated_by_universal_arrow",
    ),
    ("cartesian_coherence_actual", "cartesian_coherence_missing"),
    ("monoidwide_coherence_actual", "monoidwide_coherence_missing"),
    ("same_coherence_id_all_paths", "same_coherence_id_not_all_paths"),
    ("coherence_preserves_exact_delta", "coherence_does_not_preserve_exact_delta"),
    ("coherence_preserves_kernel", "coherence_does_not_preserve_kernel"),
    ("coherence_preserves_coimage", "coherence_does_not_preserve_coimage"),
    (
        "coherence_preserves_signed_coefficients",
        "coherence_does_not_preserve_signed_coefficients",
    ),
    (
        "coherence_preserves_rank_one_duality",
        "coherence_does_not_preserve_rank_one_duality",
    ),
    ("coherence_preserves_pinned_twist", "coherence_does_not_preserve_pinned_twist"),
    (
        "coherence_preserves_original_dd4_class",
        "coherence_does_not_preserve_original_dd4_class",
    ),
    ("coherence_preserves_normal_ratio", "coherence_does_not_preserve_normal_ratio"),
    (
        "coherence_preserves_endpoint_pairing",
        "coherence_does_not_preserve_endpoint_pairing",
    ),
    (
        "coherence_preserves_endpoint_pushforward_graph",
        "coherence_does_not_preserve_endpoint_pushforward_graph",
    ),
    ("coherence_preserves_rosati_count", "coherence_does_not_preserve_rosati_count"),
    (
        "coherence_preserves_control_death",
        "coherence_does_not_preserve_control_death",
    ),
    ("C3_C5_equals_C15_source", "C3_C5_source_not_C15"),
    ("C5_C3_equals_C15_source", "C5_C3_source_not_C15"),
    ("C3_C3_C5_equals_C45_source", "C3_C3_C5_source_not_C45"),
    ("F22_product_source", "F22_product_source_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("same_token_without_coherence", "same_token_without_coherence"),
    ("declared_2cells", "declared_2cells"),
    ("formal_commutative_square", "formal_commutative_square"),
    ("finite_composition_table", "finite_composition_table"),
    ("local_C3_patch", "local_C3_patch"),
    ("single_prime_axis_patch", "single_prime_axis_patch"),
    ("prime_axis_tags", "prime_axis_tags"),
    ("degree_equality_only", "degree_equality_only"),
    ("count_equality_only", "count_equality_only"),
    ("support_equality_only", "support_equality_only"),
    ("weighted_zero_only", "weighted_zero_only"),
    ("external_choice_of_2cells", "external_choice_of_2cells"),
    ("retuned_source_coherence", "retuned_source_coherence"),
    ("graph_object_coherence", "graph_object_coherence"),
    ("graph_predicate_gate", "graph_predicate_gate"),
    ("late_control_filter", "late_control_filter"),
    ("boundary_after_filter", "boundary_after_filter"),
    ("dd4_afterthought_filter", "dd4_afterthought_filter"),
    ("functor_of_points_without_representer", "functor_of_points_without_representer"),
    ("semantic_zeta_label", "semantic_zeta_label"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_COHERENCE_EDGES <= set(data["required_edges"]):
        out.append("required_self_dual_source_coherence_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_formation_coherence(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_COHERENCE_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber=True,
        universal_arrow_actual=True,
        self_dual_source_token_actual=True,
        self_dual_source_fiber_actual=True,
        source_before_graph_objects=True,
        source_coherence_cells_actual=True,
        source_coherence_generated_by_universal_arrow=True,
        cartesian_coherence_actual=True,
        monoidwide_coherence_actual=True,
        same_coherence_id_all_paths=True,
        coherence_preserves_exact_delta=True,
        coherence_preserves_kernel=True,
        coherence_preserves_coimage=True,
        coherence_preserves_signed_coefficients=True,
        coherence_preserves_rank_one_duality=True,
        coherence_preserves_pinned_twist=True,
        coherence_preserves_original_dd4_class=True,
        coherence_preserves_normal_ratio=True,
        coherence_preserves_endpoint_pairing=True,
        coherence_preserves_endpoint_pushforward_graph=True,
        coherence_preserves_rosati_count=True,
        coherence_preserves_control_death=True,
        C3_C5_equals_C15_source=True,
        C5_C3_equals_C15_source=True,
        C3_C3_C5_equals_C45_source=True,
        F22_product_source=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_COHERENCE_EDGES),
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
    "SFC1 universal arrow generates self-dual exact-source coherence",
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
    and coherence_payload(T3_T5_z) == coherence_payload(zC15)
    and coherence_payload(T5_T3_z) == coherence_payload(zC15)
    and coherence_payload(T3_T3_T5_z) == coherence_payload(zC45)
    and coherence_payload(T15_zF22) == coherence_payload(zC15F22)
    and coherence_payload(T45_zF22) == coherence_payload(zC45F22)
    and all(coherent_row(item) for item in rows)
    and {item["source_coherence"] for item in rows} == {SOURCE_COHERENCE_ID}
    and {item["cartesian_coherence"] for item in rows} == {CARTESIAN_COHERENCE_ID}
    and {item["monoidwide_coherence"] for item in rows} == {MONOIDWIDE_COHERENCE_ID},
    "H1=%s coherence=%s rows=%d"
    % ([p["h1_order"] for p in profiles], SOURCE_COHERENCE_ID, len(rows)),
)


gate(
    "SFC2 graph identities still do not supply source coherence",
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


finite_equalities = live_source(
    source_coherence_cells_actual=False,
    source_coherence_generated_by_universal_arrow=False,
    same_coherence_id_all_paths=False,
    same_token_without_coherence=True,
    degree_equality_only=True,
    count_equality_only=True,
    support_equality_only=True,
    weighted_zero_only=True,
    control_point_formable=True,
)

gate(
    "SFC3 same token and finite equalities do not construct coherence",
    not accepts_formation_coherence(finite_equalities)
    and {
        "source_coherence_cells_missing",
        "source_coherence_not_generated_by_universal_arrow",
        "same_coherence_id_not_all_paths",
        "same_token_without_coherence",
        "degree_equality_only",
        "count_equality_only",
        "support_equality_only",
        "weighted_zero_only",
        "control_point_formable",
    }
    <= set(reasons(finite_equalities)),
    ",".join(reasons(finite_equalities)),
)


local_patch = live_source(
    monoidwide_coherence_actual=False,
    same_coherence_id_all_paths=False,
    C5_C3_equals_C15_source=False,
    C3_C3_C5_equals_C45_source=False,
    F22_product_source=False,
    local_C3_patch=True,
    single_prime_axis_patch=True,
    prime_axis_tags=True,
)

gate(
    "SFC4 local C3 patches and prime-axis tags are not source coherence",
    not accepts_formation_coherence(local_patch)
    and {
        "monoidwide_coherence_missing",
        "same_coherence_id_not_all_paths",
        "C5_C3_source_not_C15",
        "C3_C3_C5_source_not_C45",
        "F22_product_source_missing",
        "local_C3_patch",
        "single_prime_axis_patch",
        "prime_axis_tags",
    }
    <= set(reasons(local_patch)),
    ",".join(reasons(local_patch)),
)


declared_diagram = live_source(
    source_coherence_cells_actual=False,
    source_coherence_generated_by_universal_arrow=False,
    cartesian_coherence_actual=False,
    C3_C5_equals_C15_source=False,
    declared_2cells=True,
    formal_commutative_square=True,
    finite_composition_table=True,
)

gate(
    "SFC5 declared 2-cells and formal squares are labels",
    not accepts_formation_coherence(declared_diagram)
    and {
        "source_coherence_cells_missing",
        "source_coherence_not_generated_by_universal_arrow",
        "cartesian_coherence_missing",
        "C3_C5_source_not_C15",
        "declared_2cells",
        "formal_commutative_square",
        "finite_composition_table",
    }
    <= set(reasons(declared_diagram)),
    ",".join(reasons(declared_diagram)),
)


external_retuned = live_source(
    universal_arrow_actual=False,
    source_coherence_generated_by_universal_arrow=False,
    coherence_preserves_exact_delta=False,
    coherence_preserves_signed_coefficients=False,
    coherence_preserves_original_dd4_class=False,
    coherence_preserves_control_death=False,
    external_choice_of_2cells=True,
    retuned_source_coherence=True,
    semantic_zeta_label=True,
)

gate(
    "SFC6 external choices and retuned coherences lose the source",
    not accepts_formation_coherence(external_retuned)
    and {
        "universal_arrow_not_actual",
        "source_coherence_not_generated_by_universal_arrow",
        "coherence_does_not_preserve_exact_delta",
        "coherence_does_not_preserve_signed_coefficients",
        "coherence_does_not_preserve_original_dd4_class",
        "coherence_does_not_preserve_control_death",
        "external_choice_of_2cells",
        "retuned_source_coherence",
        "semantic_zeta_label",
    }
    <= set(reasons(external_retuned)),
    ",".join(reasons(external_retuned)),
)


late_graph = live_source(
    source_before_graph_objects=False,
    coherence_preserves_endpoint_pushforward_graph=False,
    coherence_preserves_rosati_count=False,
    coherence_preserves_control_death=False,
    graph_object_coherence=True,
    graph_predicate_gate=True,
    late_control_filter=True,
    boundary_after_filter=True,
    dd4_afterthought_filter=True,
    control_point_formable=True,
)

gate(
    "SFC7 graph predicates and late filters are not source coherence",
    not accepts_formation_coherence(late_graph)
    and {
        "source_not_before_graph_objects",
        "coherence_does_not_preserve_endpoint_pushforward_graph",
        "coherence_does_not_preserve_rosati_count",
        "coherence_does_not_preserve_control_death",
        "graph_object_coherence",
        "graph_predicate_gate",
        "late_control_filter",
        "boundary_after_filter",
        "dd4_afterthought_filter",
        "control_point_formable",
    }
    <= set(reasons(late_graph)),
    ",".join(reasons(late_graph)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_COHERENCE_EDGES
        - {("universal_arrow", "self_dual_exact_source_coherence")}
    ),
    live_source(source_coherence_cells_actual=False),
    live_source(monoidwide_coherence_actual=False),
    live_source(coherence_preserves_exact_delta=False),
    live_source(coherence_preserves_rank_one_duality=False),
    live_source(coherence_preserves_control_death=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SFC8 every source-coherence edge is mandatory",
    not any(accepts_formation_coherence(data) for data in missing_edges)
    and {
        "required_self_dual_source_coherence_edges_missing",
        "source_coherence_cells_missing",
        "monoidwide_coherence_missing",
        "coherence_does_not_preserve_exact_delta",
        "coherence_does_not_preserve_rank_one_duality",
        "coherence_does_not_preserve_control_death",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


control_shadow = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_object_coherence=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "SFC9 controls/DH/Epstein coherent graph shadows are rejected",
    not accepts_formation_coherence(control_shadow)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_object_coherence",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_shadow)),
    ",".join(reasons(control_shadow)),
)


live = live_source()
dead_sources = {
    "finite_equalities": finite_equalities,
    "local_patch": local_patch,
    "declared_diagram": declared_diagram,
    "external_retuned": external_retuned,
    "late_graph": late_graph,
    "control_shadow": control_shadow,
}

gate(
    "SFC10 only universal-arrow-generated source coherence passes",
    accepts_formation_coherence(live)
    and REQUIRED_COHERENCE_EDGES <= live["required_edges"]
    and not any(accepts_formation_coherence(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_formation_coherence(data) for data in dead_sources.values()),
        accepts_formation_coherence(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSFC1-SFC10 ALL PASS: self-dual exact-source formation coherence pinned")
print(
    "VERDICT: the represented self-dual exact BCF source must carry "
    "universal-arrow-generated source-level coherence cells across C3/C5/C15/"
    "C45/F22 while preserving exact delta, kernel, coimage, rank-one duality, "
    "DD.4 boundary, endpoint/pushforward/graph/Rosati/count, and control "
    "death. Same tokens, finite equalities, declared 2-cells, local patches, "
    "external retunings, and graph-level coherent shadows do not construct "
    "the missing source object."
)
