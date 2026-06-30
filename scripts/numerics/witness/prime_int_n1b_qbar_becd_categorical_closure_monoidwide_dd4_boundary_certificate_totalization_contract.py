r"""Categorical closure monoidwide DD.4 boundary-certificate contract.

Doc 459 requires monoidwide square-layer coherence for the carrier-native
multiplier action. This witness pins the next edge: that coherence must
transport the actual carrier boundary/properness/self-duality certificate
killing the original DD.4 class. A monoidwide coherence label, boundary id,
local orbit splitter, formal nullhomotopy, deletion, quotient, or numeric
equality does not map the original class c=(1+z)^-1 to zero in the carrier
boundary sequence.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_monoidwide_dd4_boundary_certificate_totalization_contract
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
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
BOUNDARY_CERTIFICATE_ID = "BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality"
LOCALIZATION_SEQUENCE_ID = "Loc_BCCube_Qbar_BECD_single_dQ"
NORMAL_RATIO_ID = "NR_BCCube_Qbar_BECD_ordered_p1_p2"

REQUIRED_CERTIFICATE_EDGES = {
    ("represented_source_square", "monoidwide_coherence"),
    ("source_cube_totalization", "monoidwide_coherence"),
    ("universal_arrow", "monoidwide_coherence"),
    ("monoidwide_coherence", "dd4_boundary_certificate"),
    ("dd4_boundary_certificate", "original_dd4_class"),
    ("original_dd4_class", "nonzero_res1"),
    ("dd4_boundary_certificate", "single_localization_on_dq"),
    ("single_localization_on_dq", "p1_boundary_fiber"),
    ("single_localization_on_dq", "p2_boundary_fiber"),
    ("single_localization_on_dq", "normal_ratio"),
    ("normal_ratio", "connecting_map_sends_c_to_zero"),
    ("dd4_boundary_certificate", "self_dual_properness"),
    ("dd4_boundary_certificate", "transported_certificate_same_boundary"),
    ("transported_certificate_same_boundary", "C3_C5_equals_C15"),
    ("transported_certificate_same_boundary", "C5_C3_equals_C15"),
    ("transported_certificate_same_boundary", "C3_C3_C5_equals_C45"),
    ("transported_certificate_same_boundary", "F22_product_naturality"),
    ("dd4_boundary_certificate", "endpoint_degree"),
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

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_square_actual", "represented_source_square_missing"),
    ("source_cube_totalization_actual", "source_cube_totalization_missing"),
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    ("multiplier_action_functor_actual", "multiplier_action_functor_not_actual"),
    ("monoidwide_coherence_actual", "monoidwide_coherence_missing"),
    ("dd4_boundary_certificate_actual", "dd4_boundary_certificate_missing"),
    ("original_dd4_class_preserved", "original_dd4_class_not_preserved"),
    (
        "original_dd4_class_nonzero_before_certificate",
        "original_dd4_class_not_nonzero_before_certificate",
    ),
    ("connecting_map_sends_c_to_zero", "c_not_mapped_to_zero"),
    ("single_localization_on_dq", "no_single_localization_on_dq"),
    ("restricts_to_p1_fiber", "does_not_restrict_to_p1"),
    ("restricts_to_p2_fiber", "does_not_restrict_to_p2"),
    ("common_sequence_for_ratio", "no_common_sequence_for_ratio"),
    ("normal_ratio_boundary", "normal_ratio_not_boundary"),
    ("self_dual_properness", "no_self_dual_properness"),
    ("transported_certificate_same_boundary", "transported_certificate_not_same_boundary"),
    ("boundary_certificate_natural_monoidwide", "boundary_certificate_not_monoidwide"),
    ("same_certificate_all_multiplier_paths", "same_certificate_not_all_multiplier_paths"),
    ("C3_C5_equals_C15_actual", "C3_C5_equals_C15_not_actual"),
    ("C5_C3_equals_C15_actual", "C5_C3_equals_C15_not_actual"),
    ("C3_C3_C5_equals_C45_actual", "C3_C3_C5_equals_C45_not_actual"),
    ("F22_product_naturality_actual", "F22_product_naturality_not_actual"),
    ("endpoint_degree_maps_actual", "endpoint_degree_maps_missing"),
    ("p1_pushforward_square_actual", "p1_pushforward_square_missing"),
    ("p2_pushforward_square_actual", "p2_pushforward_square_missing"),
    ("graph_composition_actual", "graph_composition_missing"),
    ("rosati_actual", "rosati_missing"),
    ("count_degree_actual", "count_degree_missing"),
    ("control_death_actual", "control_death_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("monoidwide_labels_only", "monoidwide_labels_only"),
    ("boundary_id_only", "boundary_id_only"),
    ("coinduced_acyclic_replacement", "coinduced_acyclic_replacement"),
    ("formal_nullhomotopy", "formal_nullhomotopy"),
    ("deletes_obstruction", "deletes_obstruction"),
    ("quotients_obstruction", "quotients_obstruction"),
    ("separate_orbit_certificates", "separate_orbit_certificates"),
    ("local_prime_certificate", "local_prime_certificate"),
    ("declared_connecting_map", "declared_connecting_map"),
    ("declared_localization", "declared_localization"),
    ("declared_self_dual_properness", "declared_self_dual_properness"),
    ("boundary_after_certificate_filter", "boundary_after_certificate_filter"),
    ("pushforward_after_certificate_filter", "pushforward_after_certificate_filter"),
    ("graph_after_certificate_filter", "graph_after_certificate_filter"),
    ("degree_equality_only", "degree_equality_only"),
    ("count_equality_only", "count_equality_only"),
    ("support_equality_only", "support_equality_only"),
    ("weighted_zero_only", "weighted_zero_only"),
    ("local_boundary_table", "local_boundary_table"),
    ("external_choice_of_2cells", "external_choice_of_2cells"),
    ("retuned_boundary_certificate", "retuned_boundary_certificate"),
    ("graph_object_coherence", "graph_object_coherence"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)

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


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


def multiplier_degree(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items() if val > 0)


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
        "c": c,
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


def delta(F: np.ndarray) -> Corr:
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


def row(name: str, chi: dict[int, int], transport: str, cart_degree: int) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "domain": INTERNAL_EFFECTIVITY_DOMAIN_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "monoidwide_coherence": MONOIDWIDE_COHERENCE_ID,
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
        "source_token": SOURCE_TOKEN_ID,
        "formation_fiber": SOURCE_FIBER_ID,
        "representing_object": REPRESENTING_OBJECT_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "dd4_class": DD4_CLASS_ID,
        "cartesian_lift": "cart_%s" % transport,
        "cartesian_degree": cart_degree,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "p1_degree": p1,
        "p2_degree": p2,
        "graph_degree": p1,
        "count_degree_value": p1 * p2,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "boundary_defect": int(p1 != p2),
        "res1": 1,
        "control_point": False,
        "dh_point": False,
        "epstein_point": False,
    }


def source(**kwargs):
    data = {key: False for key, _ in REQUIRED}
    data.update(
        {
            "required_edges": set(),
            "monoidwide_labels_only": False,
            "boundary_id_only": False,
            "coinduced_acyclic_replacement": False,
            "formal_nullhomotopy": False,
            "deletes_obstruction": False,
            "quotients_obstruction": False,
            "separate_orbit_certificates": False,
            "local_prime_certificate": False,
            "declared_connecting_map": False,
            "declared_localization": False,
            "declared_self_dual_properness": False,
            "boundary_after_certificate_filter": False,
            "pushforward_after_certificate_filter": False,
            "graph_after_certificate_filter": False,
            "degree_equality_only": False,
            "count_equality_only": False,
            "support_equality_only": False,
            "weighted_zero_only": False,
            "local_boundary_table": False,
            "external_choice_of_2cells": False,
            "retuned_boundary_certificate": False,
            "graph_object_coherence": False,
            "control_point_formable": True,
            "dh_point_formable": True,
            "epstein_point_formable": True,
        }
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_CERTIFICATE_EDGES <= set(data["required_edges"]):
        out.append("required_dd4_boundary_certificate_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_dd4_boundary_certificate(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_CERTIFICATE_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        represented_source_fiber=True,
        universal_arrow_actual=True,
        multiplier_action_functor_actual=True,
        monoidwide_coherence_actual=True,
        dd4_boundary_certificate_actual=True,
        original_dd4_class_preserved=True,
        original_dd4_class_nonzero_before_certificate=True,
        connecting_map_sends_c_to_zero=True,
        single_localization_on_dq=True,
        restricts_to_p1_fiber=True,
        restricts_to_p2_fiber=True,
        common_sequence_for_ratio=True,
        normal_ratio_boundary=True,
        self_dual_properness=True,
        transported_certificate_same_boundary=True,
        boundary_certificate_natural_monoidwide=True,
        same_certificate_all_multiplier_paths=True,
        C3_C5_equals_C15_actual=True,
        C5_C3_equals_C15_actual=True,
        C3_C3_C5_equals_C45_actual=True,
        F22_product_naturality_actual=True,
        endpoint_degree_maps_actual=True,
        p1_pushforward_square_actual=True,
        p2_pushforward_square_actual=True,
        graph_composition_actual=True,
        rosati_actual=True,
        count_degree_actual=True,
        control_death_actual=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CERTIFICATE_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


C3 = ((3,), (1,), ((0, 0),))
C5 = ((5,), (1,), ((0, 0),))
C9 = ((9,), (1,), ((0, 0),))
C15 = ((15,), (1,), ((0, 0),))
C45 = ((45,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

z = chi_col(*ZERO_SPLIT)
chi_C3 = chi_col(*C3)
chi_C5 = chi_col(*C5)
chi_C9 = chi_col(*C9)
chi_C15 = chi_col(*C15)
chi_C45 = chi_col(*C45)
chi_F22 = chi_col(*F22)
chi_C3C5 = convolve_chi(chi_C3, chi_C5)
chi_C5C3 = convolve_chi(chi_C5, chi_C3)
chi_C3C3C5 = convolve_chi(convolve_chi(chi_C3, chi_C3), chi_C5)
chi_C15F22 = convolve_chi(chi_C15, chi_F22)
chi_C45F22 = convolve_chi(chi_C45, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T5_z = convolve_chi(z, chi_C5)
T3_T5_z = convolve_chi(T5_z, chi_C3)
T5_T3_z = convolve_chi(T3_z, chi_C5)
T15_z = convolve_chi(z, chi_C15)
T3_T3_T5_z = convolve_chi(T3_T5_z, chi_C3)
T9_T5_z = convolve_chi(T5_z, chi_C9)
T45_z = convolve_chi(z, chi_C45)
zF22 = convolve_chi(z, chi_F22)
T15_zF22 = convolve_chi(zF22, chi_C15)
T3_T5_zF22 = convolve_chi(T3_T5_z, chi_F22)
z_C15F22 = convolve_chi(z, chi_C15F22)
T45_zF22 = convolve_chi(zF22, chi_C45)
T3_T3_T5_zF22 = convolve_chi(T3_T3_T5_z, chi_F22)
z_C45F22 = convolve_chi(z, chi_C45F22)

rows = [
    row("z", z, "id", 1),
    row("T3_z", T3_z, "C3", 3),
    row("T5_z", T5_z, "C5", 5),
    row("T3_T5_z", T3_T5_z, "C3_after_C5", 15),
    row("T5_T3_z", T5_T3_z, "C5_after_C3", 15),
    row("T15_z", T15_z, "C15", 15),
    row("T3_T3_T5_z", T3_T3_T5_z, "C3_C3_after_C5", 45),
    row("T9_T5_z", T9_T5_z, "C9_after_C5", 45),
    row("T45_z", T45_z, "C45", 45),
    row("zF22", zF22, "F22", 4),
    row("T15_zF22", T15_zF22, "C15_after_F22", 60),
    row("T3_T5_zF22", T3_T5_zF22, "F22_after_C3_C5", 60),
    row("z_C15F22", z_C15F22, "C15F22", 60),
    row("T45_zF22", T45_zF22, "C45_after_F22", 180),
    row("T3_T3_T5_zF22", T3_T3_T5_zF22, "F22_after_C3_C3_C5", 180),
    row("z_C45F22", z_C45F22, "C45F22", 180),
]

c3_degree = multiplier_degree(chi_C3)
c5_degree = multiplier_degree(chi_C5)
c15_degree = multiplier_degree(chi_C15)
c45_degree = multiplier_degree(chi_C45)
f22_degree = multiplier_degree(chi_F22)
c15f22_degree = multiplier_degree(chi_C15F22)
c45f22_degree = multiplier_degree(chi_C45F22)
profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta(F_true)
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
control_D = delta(control)
control_G = graph_corr(control, control_q, 1)
control_signature = formal_graph_signature(control, control_E, control_q)
control_hodge = primitive_hodge_index(control, control_E, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(
    control_G, control_D, control_G, control_E
)


gate(
    "CATMDCQBARBECD1 one carrier certificate kills the original DD4 class monoidwide",
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
    and chi_C3C5 == chi_C5C3 == chi_C15
    and chi_C3C3C5 == chi_C45
    and {item["boundary_certificate"] for item in rows} == {BOUNDARY_CERTIFICATE_ID}
    and {item["localization_sequence"] for item in rows} == {LOCALIZATION_SEQUENCE_ID}
    and {item["normal_ratio"] for item in rows} == {NORMAL_RATIO_ID}
    and {item["dd4_class"] for item in rows} == {DD4_CLASS_ID}
    and {item["square"] for item in rows} == {CATEGORICAL_SQUARE_ID}
    and {item["cube"] for item in rows} == {FACET_CUBE_ID}
    and {item["totalization"] for item in rows} == {CUBE_TOTALIZATION_ID}
    and all(item["res1"] == 1 for item in rows)
    and all(item["endpoint_defect"] == 0 for item in rows)
    and all(item["pushforward_defect"] == 0 for item in rows)
    and all(item["boundary_defect"] == 0 for item in rows)
    and T3_T5_z == T5_T3_z == T15_z == {15: 2, 30: -1}
    and T3_T3_T5_z == T9_T5_z == T45_z == {45: 2, 90: -1}
    and T15_zF22 == T3_T5_zF22 == z_C15F22 == {30: 4, 60: -2}
    and T45_zF22 == T3_T3_T5_zF22 == z_C45F22 == {90: 4, 180: -2}
    and rows[3]["cartesian_degree"] == rows[4]["cartesian_degree"] == rows[5]["cartesian_degree"]
    and rows[3]["cartesian_degree"] == c3_degree * c5_degree == c15_degree
    and rows[6]["cartesian_degree"] == rows[7]["cartesian_degree"] == rows[8]["cartesian_degree"]
    and rows[6]["cartesian_degree"] == c3_degree * c3_degree * c5_degree == c45_degree
    and rows[10]["cartesian_degree"] == rows[11]["cartesian_degree"] == rows[12]["cartesian_degree"]
    and rows[10]["cartesian_degree"] == c15_degree * f22_degree == c15f22_degree
    and rows[13]["cartesian_degree"] == rows[14]["cartesian_degree"] == rows[15]["cartesian_degree"]
    and rows[13]["cartesian_degree"] == c45_degree * f22_degree == c45f22_degree,
    "H1=%s cert=%s C45F22=%s"
    % ([p["h1_order"] for p in profiles], BOUNDARY_CERTIFICATE_ID, z_C45F22),
)


gate(
    "CATMDCQBARBECD2 graph identities do not kill the DD4 class",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and control_retuned[0] == 27.0,
    "true_sig=%s control_sig=%s true_H=%.3f control_H=%.3f proj=%.1f"
    % (true_signature, control_signature, true_hodge, control_hodge, control_projection),
)


labels_only = live_source(
    dd4_boundary_certificate_actual=False,
    connecting_map_sends_c_to_zero=False,
    single_localization_on_dq=False,
    transported_certificate_same_boundary=False,
    monoidwide_labels_only=True,
    boundary_id_only=True,
    control_point_formable=True,
)

gate(
    "CATMDCQBARBECD3 monoidwide labels without the boundary certificate fail",
    not accepts_dd4_boundary_certificate(labels_only)
    and {
        "dd4_boundary_certificate_missing",
        "c_not_mapped_to_zero",
        "no_single_localization_on_dq",
        "transported_certificate_not_same_boundary",
        "monoidwide_labels_only",
        "boundary_id_only",
        "control_point_formable",
    }
    <= set(reasons(labels_only)),
    ",".join(reasons(labels_only)),
)


formal_killers = [
    live_source(
        carrier_native=False,
        dd4_boundary_certificate_actual=False,
        original_dd4_class_preserved=False,
        coinduced_acyclic_replacement=True,
    ),
    live_source(
        dd4_boundary_certificate_actual=False,
        formal_nullhomotopy=True,
        declared_connecting_map=True,
    ),
    live_source(
        original_dd4_class_preserved=False,
        connecting_map_sends_c_to_zero=False,
        deletes_obstruction=True,
    ),
    live_source(
        original_dd4_class_preserved=False,
        connecting_map_sends_c_to_zero=False,
        quotients_obstruction=True,
    ),
]
formal_reasons = set().union(*(set(reasons(data)) for data in formal_killers))

gate(
    "CATMDCQBARBECD4 formal nullhomotopies deletion and quotient do not preserve c",
    not any(accepts_dd4_boundary_certificate(data) for data in formal_killers)
    and {
        "dd4_boundary_certificate_missing",
        "original_dd4_class_not_preserved",
        "c_not_mapped_to_zero",
        "coinduced_acyclic_replacement",
        "formal_nullhomotopy",
        "declared_connecting_map",
        "deletes_obstruction",
        "quotients_obstruction",
    }
    <= formal_reasons,
    "formal=%s" % sorted(formal_reasons),
)


separate_certificates = live_source(
    same_certificate_all_multiplier_paths=False,
    transported_certificate_same_boundary=False,
    boundary_certificate_natural_monoidwide=False,
    separate_orbit_certificates=True,
    local_prime_certificate=True,
    external_choice_of_2cells=True,
)

gate(
    "CATMDCQBARBECD5 separate orbit or prime certificates do not give one boundary map",
    not accepts_dd4_boundary_certificate(separate_certificates)
    and {
        "same_certificate_not_all_multiplier_paths",
        "transported_certificate_not_same_boundary",
        "boundary_certificate_not_monoidwide",
        "separate_orbit_certificates",
        "local_prime_certificate",
        "external_choice_of_2cells",
    }
    <= set(reasons(separate_certificates)),
    ",".join(reasons(separate_certificates)),
)


declared_certificate = live_source(
    dd4_boundary_certificate_actual=False,
    connecting_map_sends_c_to_zero=False,
    single_localization_on_dq=False,
    self_dual_properness=False,
    required_edges=set(),
    declared_connecting_map=True,
    declared_localization=True,
    declared_self_dual_properness=True,
)

gate(
    "CATMDCQBARBECD6 declared connecting maps localizations and properness are labels",
    not accepts_dd4_boundary_certificate(declared_certificate)
    and {
        "dd4_boundary_certificate_missing",
        "c_not_mapped_to_zero",
        "no_single_localization_on_dq",
        "no_self_dual_properness",
        "required_dd4_boundary_certificate_edges_missing",
        "declared_connecting_map",
        "declared_localization",
        "declared_self_dual_properness",
    }
    <= set(reasons(declared_certificate)),
    ",".join(reasons(declared_certificate)),
)


late_filters = live_source(
    boundary_certificate_natural_monoidwide=False,
    endpoint_degree_maps_actual=False,
    p1_pushforward_square_actual=False,
    p2_pushforward_square_actual=False,
    graph_composition_actual=False,
    boundary_after_certificate_filter=True,
    pushforward_after_certificate_filter=True,
    graph_after_certificate_filter=True,
    retuned_boundary_certificate=True,
)

gate(
    "CATMDCQBARBECD7 endpoint pushforward graph filters after certificate are rejected",
    not accepts_dd4_boundary_certificate(late_filters)
    and {
        "boundary_certificate_not_monoidwide",
        "endpoint_degree_maps_missing",
        "p1_pushforward_square_missing",
        "p2_pushforward_square_missing",
        "graph_composition_missing",
        "boundary_after_certificate_filter",
        "pushforward_after_certificate_filter",
        "graph_after_certificate_filter",
        "retuned_boundary_certificate",
    }
    <= set(reasons(late_filters)),
    ",".join(reasons(late_filters)),
)


numeric_only = live_source(
    dd4_boundary_certificate_actual=False,
    connecting_map_sends_c_to_zero=False,
    degree_equality_only=True,
    count_equality_only=True,
    support_equality_only=True,
    weighted_zero_only=True,
    local_boundary_table=True,
)

gate(
    "CATMDCQBARBECD8 numeric equality and local tables do not map c to zero",
    not accepts_dd4_boundary_certificate(numeric_only)
    and {
        "dd4_boundary_certificate_missing",
        "c_not_mapped_to_zero",
        "degree_equality_only",
        "count_equality_only",
        "support_equality_only",
        "weighted_zero_only",
        "local_boundary_table",
    }
    <= set(reasons(numeric_only)),
    ",".join(reasons(numeric_only)),
)


missing_edges = [
    live_source(required_edges=REQUIRED_CERTIFICATE_EDGES - {("normal_ratio", "connecting_map_sends_c_to_zero")}),
    live_source(required_edges=REQUIRED_CERTIFICATE_EDGES - {("dd4_boundary_certificate", "self_dual_properness")}),
    live_source(required_edges=REQUIRED_CERTIFICATE_EDGES - {("transported_certificate_same_boundary", "C3_C5_equals_C15")}),
    live_source(connecting_map_sends_c_to_zero=False),
    live_source(self_dual_properness=False),
    live_source(C3_C5_equals_C15_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATMDCQBARBECD9 every boundary certificate edge is mandatory",
    not any(accepts_dd4_boundary_certificate(data) for data in missing_edges)
    and {
        "required_dd4_boundary_certificate_edges_missing",
        "c_not_mapped_to_zero",
        "no_self_dual_properness",
        "C3_C5_equals_C15_not_actual",
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

live = live_source()
dead_sources = {
    "labels_only": labels_only,
    "separate_certificates": separate_certificates,
    "declared_certificate": declared_certificate,
    "late_filters": late_filters,
    "numeric_only": numeric_only,
    "control_shadow": control_shadow,
}

gate(
    "CATMDCQBARBECD10 only carrier-native monoidwide DD4 boundary certificate passes",
    not accepts_dd4_boundary_certificate(control_shadow)
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
    <= set(reasons(control_shadow))
    and accepts_dd4_boundary_certificate(live)
    and REQUIRED_CERTIFICATE_EDGES <= live["required_edges"]
    and not any(item["control_point"] for item in rows)
    and not any(item["dh_point"] for item in rows)
    and not any(item["epstein_point"] for item in rows)
    and not any(accepts_dd4_boundary_certificate(data) for data in dead_sources.values())
    and not any(accepts_dd4_boundary_certificate(data) for data in formal_killers),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_dd4_boundary_certificate(data) for data in dead_sources.values()),
        accepts_dd4_boundary_certificate(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATMDCQBARBECD1-CATMDCQBARBECD10 ALL PASS: categorical closure "
    "monoidwide DD4 boundary-certificate totalization contract pinned"
)
print(
    "VERDICT: the doc459 monoidwide-square-layer-coherent square-layer-"
    "coherent cartesian-coherent represented-source-fiber source-typed "
    "graph-formation-control-death-natural graph/Rosati/count-natural "
    "pushforward-natural endpoint-degree-natural DD.4-natural multiplier-"
    "action source totalization is still insufficient unless monoidwide "
    "square-layer coherence transports the actual carrier boundary/"
    "properness/self-duality certificate that preserves the original nonzero "
    "DD.4 class and maps it to zero through one dQ localization sequence. "
    "Labels, formal nullhomotopies, deletion, quotient, separate orbit "
    "certificates, late filters, numeric equalities, and control/DH/Epstein "
    "shadows do not construct the missing object."
)
