r"""Categorical closure monoidwide square-layer coherence totalization contract.

Doc 458 requires cartesian coherence to commute with the square layers on the
visible C3/C9/F22 patch. This witness pins the next edge: the same
square-layer coherence must be monoidwide for the carrier-native multiplier
action. A local C3 patch, finite generator table, declared monoid action,
formal pentagon/hexagon, prime-axis label, or late boundary/pushforward/graph
filter does not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_monoidwide_square_layer_coherence_totalization_contract
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
CARTESIAN_LIFTS_ID = "CartLift_BCCube_Qbar_BECD_multiplier_source_fiber"
CARTESIAN_COHERENCE_ID = "Coh_BCCube_Qbar_BECD_cartesian_lifts"
SQUARE_LAYER_COHERENCE_ID = "SLC_BCCube_Qbar_BECD_boundary_pushforward_graph"
MONOIDWIDE_COHERENCE_ID = "MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers"

REQUIRED_MONOID_EDGES = {
    ("represented_source_square", "multiplier_action_functor"),
    ("source_cube_totalization", "multiplier_action_functor"),
    ("universal_arrow", "multiplier_action_functor"),
    ("multiplier_action_functor", "identity_transport"),
    ("multiplier_action_functor", "composition_law"),
    ("composition_law", "C3_C3_equals_C9"),
    ("composition_law", "C3_C5_equals_C15"),
    ("composition_law", "C5_C3_equals_C15"),
    ("composition_law", "C3_C3_C5_equals_C45"),
    ("composition_law", "F22_product_naturality"),
    ("cartesian_coherence", "square_layer_coherence"),
    ("square_layer_coherence", "monoidwide_square_layer_coherence"),
    ("composition_law", "monoidwide_square_layer_coherence"),
    ("monoidwide_square_layer_coherence", "dd4_boundary"),
    ("monoidwide_square_layer_coherence", "endpoint_degree"),
    ("monoidwide_square_layer_coherence", "p1_pushforward"),
    ("monoidwide_square_layer_coherence", "p2_pushforward"),
    ("monoidwide_square_layer_coherence", "graph_composition"),
    ("monoidwide_square_layer_coherence", "rosati"),
    ("monoidwide_square_layer_coherence", "count_degree"),
    ("monoidwide_square_layer_coherence", "control_death"),
    ("dd4_boundary", "endpoint_degree"),
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
    ("identity_transport_actual", "identity_transport_not_actual"),
    ("composition_law_actual", "composition_law_not_actual"),
    ("cartesian_coherence_actual", "cartesian_coherence_missing"),
    ("square_layer_coherence_actual", "square_layer_coherence_missing"),
    ("monoidwide_coherence_actual", "monoidwide_coherence_missing"),
    ("coherence_generated_by_universal_arrow", "coherence_not_generated_by_universal_arrow"),
    ("C3_C3_equals_C9_actual", "C3_C3_equals_C9_not_actual"),
    ("C3_C5_equals_C15_actual", "C3_C5_equals_C15_not_actual"),
    ("C5_C3_equals_C15_actual", "C5_C3_equals_C15_not_actual"),
    ("C3_C3_C5_equals_C45_actual", "C3_C3_C5_equals_C45_not_actual"),
    ("F22_product_naturality_actual", "F22_product_naturality_not_actual"),
    ("dd4_boundary_actual", "dd4_boundary_missing"),
    ("endpoint_degree_maps_actual", "endpoint_degree_maps_missing"),
    ("p1_pushforward_square_actual", "p1_pushforward_square_missing"),
    ("p2_pushforward_square_actual", "p2_pushforward_square_missing"),
    ("graph_composition_actual", "graph_composition_missing"),
    ("rosati_actual", "rosati_missing"),
    ("count_degree_actual", "count_degree_missing"),
    ("control_death_actual", "control_death_missing"),
    ("square_layers_commute_monoidwide", "square_layers_not_monoidwide"),
    ("same_coherence_id_all_multiplier_paths", "same_coherence_id_not_all_multiplier_paths"),
    ("preserves_coefficients_and_support", "does_not_preserve_coefficients_and_support"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("local_C3_patch", "local_C3_patch"),
    ("single_prime_axis_patch", "single_prime_axis_patch"),
    ("finite_generator_table", "finite_generator_table"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("prime_axis_tags", "prime_axis_tags"),
    ("declared_monoid_action", "declared_monoid_action"),
    ("formal_pentagon", "formal_pentagon"),
    ("formal_hexagon", "formal_hexagon"),
    ("degree_equality_only", "degree_equality_only"),
    ("count_equality_only", "count_equality_only"),
    ("support_equality_only", "support_equality_only"),
    ("weighted_zero_only", "weighted_zero_only"),
    ("boundary_after_monoid_filter", "boundary_after_monoid_filter"),
    ("pushforward_after_monoid_filter", "pushforward_after_monoid_filter"),
    ("graph_after_monoid_filter", "graph_after_monoid_filter"),
    ("local_layer_table", "local_layer_table"),
    ("external_choice_of_2cells", "external_choice_of_2cells"),
    ("retuned_multiplier_coherence", "retuned_multiplier_coherence"),
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


def support_union(chars: dict[str, dict[int, int]]) -> tuple[int, ...]:
    keys: set[int] = set()
    for chi in chars.values():
        keys.update(chi)
    return tuple(sorted(keys))


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


def multiplier_degree(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items() if val > 0)


def factor_signature(n: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    d = 2
    while d * d <= n:
        exponent = 0
        while n % d == 0:
            n //= d
            exponent += 1
        if exponent:
            factors.append((d, exponent))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


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
        "cartesian_lifts": CARTESIAN_LIFTS_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "square_layer_coherence": SQUARE_LAYER_COHERENCE_ID,
        "monoidwide_coherence": MONOIDWIDE_COHERENCE_ID,
        "cartesian_lift": "cart_%s" % transport,
        "cartesian_degree": cart_degree,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "weighted_mass": weighted_mass(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "graph_degree": p1,
        "count_degree_value": p1 * p2,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "boundary_defect": int(p1 != p2),
        "layer_chain": (
            DD4_BOUNDARY_LOCALIZATION_ID,
            ENDPOINT_DEGREE_MAPS_ID,
            P1_PUSHFORWARD_ID,
            P2_PUSHFORWARD_ID,
            PROPER_GRAPH_ID,
            ROSATI_LAYER_ID,
            COUNT_DEGREE_ID,
            CONTROL_DEATH_NATURALITY_ID,
        ),
        "control_point": False,
        "dh_point": False,
        "epstein_point": False,
    }


def source(**kwargs):
    data = {key: False for key, _ in REQUIRED}
    data.update(
        {
            "required_edges": set(),
            "local_C3_patch": False,
            "single_prime_axis_patch": False,
            "finite_generator_table": False,
            "external_prime_factorization": False,
            "prime_axis_tags": False,
            "declared_monoid_action": False,
            "formal_pentagon": False,
            "formal_hexagon": False,
            "degree_equality_only": False,
            "count_equality_only": False,
            "support_equality_only": False,
            "weighted_zero_only": False,
            "boundary_after_monoid_filter": False,
            "pushforward_after_monoid_filter": False,
            "graph_after_monoid_filter": False,
            "local_layer_table": False,
            "external_choice_of_2cells": False,
            "retuned_multiplier_coherence": False,
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
    if not REQUIRED_MONOID_EDGES <= set(data["required_edges"]):
        out.append("required_monoidwide_square_layer_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_monoidwide_square_layer(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_MONOID_EDGES <= set(data["required_edges"])
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
        identity_transport_actual=True,
        composition_law_actual=True,
        cartesian_coherence_actual=True,
        square_layer_coherence_actual=True,
        monoidwide_coherence_actual=True,
        coherence_generated_by_universal_arrow=True,
        C3_C3_equals_C9_actual=True,
        C3_C5_equals_C15_actual=True,
        C5_C3_equals_C15_actual=True,
        C3_C3_C5_equals_C45_actual=True,
        F22_product_naturality_actual=True,
        dd4_boundary_actual=True,
        endpoint_degree_maps_actual=True,
        p1_pushforward_square_actual=True,
        p2_pushforward_square_actual=True,
        graph_composition_actual=True,
        rosati_actual=True,
        count_degree_actual=True,
        control_death_actual=True,
        square_layers_commute_monoidwide=True,
        same_coherence_id_all_multiplier_paths=True,
        preserves_coefficients_and_support=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_MONOID_EDGES),
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
chi_C3C3 = convolve_chi(chi_C3, chi_C3)
chi_C3C5 = convolve_chi(chi_C3, chi_C5)
chi_C5C3 = convolve_chi(chi_C5, chi_C3)
chi_C3C3C5 = convolve_chi(chi_C3C3, chi_C5)
chi_C15F22 = convolve_chi(chi_C15, chi_F22)
chi_C45F22 = convolve_chi(chi_C45, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T3_T3_z = convolve_chi(T3_z, chi_C3)
T9_z = convolve_chi(z, chi_C9)
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

all_chars = {item["source"]: dict(item["coefficients"]) for item in rows}
base_graph_degree = rows[0]["graph_degree"]
base_count_degree = rows[0]["count_degree_value"]
c3_degree = multiplier_degree(chi_C3)
c5_degree = multiplier_degree(chi_C5)
c9_degree = multiplier_degree(chi_C9)
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
    "CATMWCSLCQBARBECD1 one square-layer coherence works across independent multipliers",
    max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and chi_C3C3 == chi_C9
    and chi_C3C5 == chi_C5C3 == chi_C15
    and chi_C3C3C5 == chi_C45
    and {item["monoidwide_coherence"] for item in rows} == {MONOIDWIDE_COHERENCE_ID}
    and {item["square_layer_coherence"] for item in rows} == {SQUARE_LAYER_COHERENCE_ID}
    and {item["cartesian_coherence"] for item in rows} == {CARTESIAN_COHERENCE_ID}
    and {item["layer_chain"] for item in rows}
    == {
        (
            DD4_BOUNDARY_LOCALIZATION_ID,
            ENDPOINT_DEGREE_MAPS_ID,
            P1_PUSHFORWARD_ID,
            P2_PUSHFORWARD_ID,
            PROPER_GRAPH_ID,
            ROSATI_LAYER_ID,
            COUNT_DEGREE_ID,
            CONTROL_DEATH_NATURALITY_ID,
        )
    }
    and all(item["endpoint_defect"] == 0 for item in rows)
    and all(item["pushforward_defect"] == 0 for item in rows)
    and all(item["boundary_defect"] == 0 for item in rows)
    and all(item["weighted_mass"] == 0 for item in rows)
    and T3_T3_z == T9_z
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
    and rows[13]["cartesian_degree"] == c45_degree * f22_degree == c45f22_degree
    and rows[13]["graph_degree"] == base_graph_degree * c45f22_degree
    and rows[13]["count_degree_value"] == base_count_degree * c45f22_degree**2
    and support_union(all_chars) == (1, 2, 3, 4, 5, 6, 10, 15, 30, 45, 60, 90, 180),
    "count=%.1e anti=%.1e C15=%s C45F22=%s support=%s"
    % (max(true_count_defects), true_anti, T15_z, z_C45F22, support_union(all_chars)),
)


gate(
    "CATMWCSLCQBARBECD2 graph identities do not supply monoidwide coherence",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and control_retuned[0] == 27.0,
    "true_sig=%s control_sig=%s true_H=%.3f control_H=%.3f proj=%.1f"
    % (true_signature, control_signature, true_hodge, control_hodge, control_projection),
)


local_c3 = live_source(
    monoidwide_coherence_actual=False,
    C3_C5_equals_C15_actual=False,
    C5_C3_equals_C15_actual=False,
    C3_C3_C5_equals_C45_actual=False,
    same_coherence_id_all_multiplier_paths=False,
    local_C3_patch=True,
    single_prime_axis_patch=True,
    finite_generator_table=True,
    control_point_formable=True,
)

gate(
    "CATMWCSLCQBARBECD3 local C3/C9 square-layer patches are not monoidwide",
    not accepts_monoidwide_square_layer(local_c3)
    and {
        "monoidwide_coherence_missing",
        "C3_C5_equals_C15_not_actual",
        "C5_C3_equals_C15_not_actual",
        "C3_C3_C5_equals_C45_not_actual",
        "same_coherence_id_not_all_multiplier_paths",
        "local_C3_patch",
        "single_prime_axis_patch",
        "finite_generator_table",
        "control_point_formable",
    }
    <= set(reasons(local_c3)),
    ",".join(reasons(local_c3)),
)


prime_axis = live_source(
    carrier_native=False,
    multiplier_action_functor_actual=False,
    square_layers_commute_monoidwide=False,
    external_prime_factorization=True,
    prime_axis_tags=True,
    finite_generator_table=True,
)

gate(
    "CATMWCSLCQBARBECD4 prime-axis labels and factorization tables are external",
    factor_signature(180) == ((2, 2), (3, 2), (5, 1))
    and not accepts_monoidwide_square_layer(prime_axis)
    and {
        "not_carrier_native",
        "multiplier_action_functor_not_actual",
        "square_layers_not_monoidwide",
        "external_prime_factorization",
        "prime_axis_tags",
        "finite_generator_table",
    }
    <= set(reasons(prime_axis)),
    ",".join(reasons(prime_axis)),
)


declared = live_source(
    composition_law_actual=False,
    monoidwide_coherence_actual=False,
    coherence_generated_by_universal_arrow=False,
    required_edges=set(),
    declared_monoid_action=True,
    formal_pentagon=True,
    formal_hexagon=True,
)

gate(
    "CATMWCSLCQBARBECD5 declared monoid actions and coherence diagrams are labels",
    not accepts_monoidwide_square_layer(declared)
    and {
        "composition_law_not_actual",
        "monoidwide_coherence_missing",
        "coherence_not_generated_by_universal_arrow",
        "required_monoidwide_square_layer_edges_missing",
        "declared_monoid_action",
        "formal_pentagon",
        "formal_hexagon",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


missing_independent = [
    live_source(C3_C5_equals_C15_actual=False),
    live_source(C5_C3_equals_C15_actual=False),
    live_source(C3_C3_C5_equals_C45_actual=False),
    live_source(F22_product_naturality_actual=False),
    live_source(required_edges=REQUIRED_MONOID_EDGES - {("composition_law", "C3_C5_equals_C15")}),
    live_source(required_edges=REQUIRED_MONOID_EDGES - {("composition_law", "C3_C3_C5_equals_C45")}),
]
missing_independent_reasons = set().union(*(set(reasons(data)) for data in missing_independent))

gate(
    "CATMWCSLCQBARBECD6 independent multiplier paths and F22 naturality are mandatory",
    not any(accepts_monoidwide_square_layer(data) for data in missing_independent)
    and {
        "C3_C5_equals_C15_not_actual",
        "C5_C3_equals_C15_not_actual",
        "C3_C3_C5_equals_C45_not_actual",
        "F22_product_naturality_not_actual",
        "required_monoidwide_square_layer_edges_missing",
    }
    <= missing_independent_reasons,
    "missing=%s" % sorted(missing_independent_reasons),
)


late_filters = live_source(
    square_layers_commute_monoidwide=False,
    dd4_boundary_actual=False,
    p1_pushforward_square_actual=False,
    p2_pushforward_square_actual=False,
    graph_composition_actual=False,
    boundary_after_monoid_filter=True,
    pushforward_after_monoid_filter=True,
    graph_after_monoid_filter=True,
    retuned_multiplier_coherence=True,
)

gate(
    "CATMWCSLCQBARBECD7 late boundary pushforward graph filters are rejected",
    not accepts_monoidwide_square_layer(late_filters)
    and {
        "dd4_boundary_missing",
        "p1_pushforward_square_missing",
        "p2_pushforward_square_missing",
        "graph_composition_missing",
        "square_layers_not_monoidwide",
        "boundary_after_monoid_filter",
        "pushforward_after_monoid_filter",
        "graph_after_monoid_filter",
        "retuned_multiplier_coherence",
    }
    <= set(reasons(late_filters)),
    ",".join(reasons(late_filters)),
)


numeric = live_source(
    monoidwide_coherence_actual=False,
    preserves_coefficients_and_support=False,
    degree_equality_only=True,
    count_equality_only=True,
    support_equality_only=True,
    weighted_zero_only=True,
    local_layer_table=True,
)

gate(
    "CATMWCSLCQBARBECD8 numeric equalities and local layer tables are diagnostics",
    not accepts_monoidwide_square_layer(numeric)
    and {
        "monoidwide_coherence_missing",
        "does_not_preserve_coefficients_and_support",
        "degree_equality_only",
        "count_equality_only",
        "support_equality_only",
        "weighted_zero_only",
        "local_layer_table",
    }
    <= set(reasons(numeric)),
    ",".join(reasons(numeric)),
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
    "CATMWCSLCQBARBECD9 control DH Epstein monoid shadows are rejected",
    not accepts_monoidwide_square_layer(control_shadow)
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


static_monoid = live_source(
    required_edges=REQUIRED_MONOID_EDGES
    - {
        ("composition_law", "C3_C5_equals_C15"),
        ("monoidwide_square_layer_coherence", "dd4_boundary"),
        ("monoidwide_square_layer_coherence", "control_death"),
    },
    monoidwide_coherence_actual=False,
    external_choice_of_2cells=True,
)

live = live_source()
dead_sources = {
    "local_c3": local_c3,
    "prime_axis": prime_axis,
    "declared": declared,
    "late_filters": late_filters,
    "numeric": numeric,
    "control_shadow": control_shadow,
    "static_monoid": static_monoid,
}

gate(
    "CATMWCSLCQBARBECD10 only carrier-native monoidwide square-layer coherence passes",
    not accepts_monoidwide_square_layer(static_monoid)
    and {
        "monoidwide_coherence_missing",
        "required_monoidwide_square_layer_edges_missing",
        "external_choice_of_2cells",
    }
    <= set(reasons(static_monoid))
    and accepts_monoidwide_square_layer(live)
    and REQUIRED_MONOID_EDGES <= live["required_edges"]
    and not any(item["control_point"] for item in rows)
    and not any(item["dh_point"] for item in rows)
    and not any(item["epstein_point"] for item in rows)
    and not any(accepts_monoidwide_square_layer(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_monoidwide_square_layer(data) for data in dead_sources.values()),
        accepts_monoidwide_square_layer(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATMWCSLCQBARBECD1-CATMWCSLCQBARBECD10 ALL PASS: categorical closure "
    "monoidwide square-layer coherence totalization contract pinned"
)
print(
    "VERDICT: the doc458 square-layer-coherent cartesian-coherent "
    "represented-source-fiber source-typed graph-formation-control-death-"
    "natural graph/Rosati/count-natural pushforward-natural endpoint-degree-"
    "natural DD.4-natural multiplier-action source totalization is still "
    "insufficient unless square-layer coherence is monoidwide for the "
    "carrier-native multiplier action. Local C3 patches, finite generator "
    "tables, external prime-axis labels, declared monoid actions, formal "
    "pentagon/hexagon diagrams, late filters, numeric equalities, retuned "
    "coherences, and control/DH/Epstein shadows do not construct the "
    "missing object."
)
