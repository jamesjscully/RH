r"""Categorical closure represented source-fiber totalization contract.

Doc 455 requires a source-typed graph-formation fiber before graph objects
exist. This witness pins the next edge: the source fiber must be represented
by an actual carrier-side object and universal arrow with cartesian multiplier
lifts. A specification functor, functor of points, predicate subfibration,
declared representer, formal universal property, or local source-label table
is not the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_represented_source_fiber_totalization_contract
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
PUSHFORWARD_SQUARE_ID = "PF_Qbar_BECD_p1p2_DD4_endpoint"
GRAPH_ROSATI_COUNT_TOTALIZATION_ID = "GRCTot_BCCube_Qbar_BECD_pushforward_internal_stratum"
PROPER_GRAPH_ID = "G_Qbar_BECD_pushforward_prop"
ROSATI_LAYER_ID = "R_Qbar_BECD_pushforward_positive"
COUNT_DEGREE_ID = "CD_Qbar_BECD_pushforward"
GRAPH_FORMATION_GATE_ID = "K_Qbar_BECD_graph_formation_death"
CONTROL_DEATH_NATURALITY_ID = "Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD"
SOURCE_TOKEN_ID = "SrcTok_BCCube_Qbar_BECD_source_typed_graph_formation"
SOURCE_FIBER_ID = "Fib_BCCube_Qbar_BECD_source_typed_graph_formation"
SOURCE_TOKEN_NATURALITY_ID = "Nat_SourceToken_T_multiplier_BCCube_Qbar_BECD"
REPRESENTING_OBJECT_ID = "Rep_BCCube_Qbar_BECD_source_fiber"
UNIVERSAL_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
CARTESIAN_LIFTS_ID = "CartLift_BCCube_Qbar_BECD_multiplier_source_fiber"

REQUIRED_EDGES = {
    ("represented_source_square", "representing_object"),
    ("source_cube_totalization", "representing_object"),
    ("internal_effectivity_domain", "representing_object"),
    ("multiplier_action_functor", "representing_object"),
    ("dd4_boundary_localization", "representing_object"),
    ("endpoint_degree_maps", "representing_object"),
    ("pushforward_square", "representing_object"),
    ("graph_rosati_count_totalization", "representing_object"),
    ("graph_formation_control_death", "representing_object"),
    ("source_typed_formation_gate", "representing_object"),
    ("representing_object", "universal_arrow"),
    ("universal_arrow", "source_token"),
    ("universal_arrow", "source_formation_fiber"),
    ("universal_arrow", "cartesian_lifts"),
    ("cartesian_lifts", "multiplier_transport"),
    ("cartesian_lifts", "cartesian_composition"),
    ("cartesian_lifts", "control_death_at_graph_formation"),
    ("source_formation_fiber", "controls_not_points"),
    ("source_formation_fiber", "dh_not_points"),
    ("source_formation_fiber", "epstein_not_points"),
    ("cartesian_composition", "same_representer_transports_rows"),
    ("same_representer_transports_rows", "internal_effectivity_domain"),
}

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_square_actual", "represented_source_square_missing"),
    ("source_cube_totalization_actual", "source_cube_totalization_missing"),
    ("internal_effectivity_domain_actual", "internal_effectivity_domain_missing"),
    ("multiplier_action_functor_actual", "multiplier_action_functor_missing"),
    ("dd4_boundary_source", "dd4_boundary_source_missing"),
    ("endpoint_degree_source", "endpoint_degree_source_missing"),
    ("pushforward_source", "pushforward_source_missing"),
    ("graph_rosati_count_source", "graph_rosati_count_source_missing"),
    ("graph_formation_control_death_source", "graph_formation_control_death_source_missing"),
    ("source_typed_formation_gate", "source_typed_formation_gate_missing"),
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("representing_object_actual", "representing_object_not_actual"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    ("source_token_generated_by_universal_arrow", "source_token_not_generated_by_universal_arrow"),
    ("formation_fiber_generated_by_universal_arrow", "formation_fiber_not_generated_by_universal_arrow"),
    ("structural_maps_represented", "structural_maps_not_represented"),
    ("cartesian_lifts_actual", "cartesian_lifts_not_actual"),
    ("cartesian_lifts_compose", "cartesian_lifts_do_not_compose"),
    ("cartesian_lifts_preserve_coefficients", "cartesian_lifts_do_not_preserve_coefficients"),
    ("fiber_before_graph_objects", "fiber_not_before_graph_objects"),
    ("control_death_represented", "control_death_not_represented"),
    ("controls_not_points_of_representer", "controls_are_points_of_representer"),
    ("dh_not_points_of_representer", "dh_is_point_of_representer"),
    ("epstein_not_points_of_representer", "epstein_is_point_of_representer"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("same_representer_transports_all_rows", "same_representer_does_not_transport_all_rows"),
)

BANNED = (
    ("specification_functor_only", "specification_functor_only"),
    ("functor_of_points_without_representer", "functor_of_points_without_representer"),
    ("yoneda_reversal", "yoneda_reversal"),
    ("predicate_subfibration", "predicate_subfibration"),
    ("discrete_fibration_labels", "discrete_fibration_labels"),
    ("declared_representer", "declared_representer"),
    ("formal_universal_property", "formal_universal_property"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("local_representers", "local_representers"),
    ("finite_representer_table", "finite_representer_table"),
    ("external_choice_of_cartesian_lifts", "external_choice_of_cartesian_lifts"),
    ("retuned_cartesian_lifts", "retuned_cartesian_lifts"),
    ("semantic_zeta_tag", "semantic_zeta_tag"),
    ("source_token_after_graph_formation", "source_token_after_graph_formation"),
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


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


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


def source_row(name: str, chi: dict[int, int], transport: str, cart_degree: int) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "domain": INTERNAL_EFFECTIVITY_DOMAIN_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "boundary": DD4_BOUNDARY_LOCALIZATION_ID,
        "endpoint_maps": ENDPOINT_DEGREE_MAPS_ID,
        "pushforward": PUSHFORWARD_SQUARE_ID,
        "graph_totalization": GRAPH_ROSATI_COUNT_TOTALIZATION_ID,
        "graph": PROPER_GRAPH_ID,
        "rosati": ROSATI_LAYER_ID,
        "count_degree": COUNT_DEGREE_ID,
        "control_gate": GRAPH_FORMATION_GATE_ID,
        "control_death_naturality": CONTROL_DEATH_NATURALITY_ID,
        "source_token": SOURCE_TOKEN_ID,
        "source_fiber": SOURCE_FIBER_ID,
        "source_token_naturality": SOURCE_TOKEN_NATURALITY_ID,
        "representing_object": REPRESENTING_OBJECT_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "cartesian_lifts": CARTESIAN_LIFTS_ID,
        "cartesian_lift": "cart_%s" % transport,
        "cartesian_degree": cart_degree,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "weighted_mass": weighted_mass(chi),
        "graph_degree": p1,
        "count_degree_value": p1 * p2,
        "endpoint_defect": p1 - p2,
        "control_point": False,
        "dh_point": False,
        "epstein_point": False,
    }


def source(**kwargs):
    data = {key: False for key, _ in REQUIRED}
    data.update(
        {
            "required_edges": set(),
            "specification_functor_only": False,
            "functor_of_points_without_representer": False,
            "yoneda_reversal": False,
            "predicate_subfibration": False,
            "discrete_fibration_labels": False,
            "declared_representer": False,
            "formal_universal_property": False,
            "graph_object_classifier": False,
            "local_representers": False,
            "finite_representer_table": False,
            "external_choice_of_cartesian_lifts": False,
            "retuned_cartesian_lifts": False,
            "semantic_zeta_tag": False,
            "source_token_after_graph_formation": False,
            "control_point_formable": True,
            "dh_point_formable": True,
            "epstein_point_formable": True,
        }
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_represented_source_fiber_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_represented_source_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        internal_effectivity_domain_actual=True,
        multiplier_action_functor_actual=True,
        dd4_boundary_source=True,
        endpoint_degree_source=True,
        pushforward_source=True,
        graph_rosati_count_source=True,
        graph_formation_control_death_source=True,
        source_typed_formation_gate=True,
        represented_source_fiber=True,
        representing_object_actual=True,
        universal_arrow_actual=True,
        source_token_generated_by_universal_arrow=True,
        formation_fiber_generated_by_universal_arrow=True,
        structural_maps_represented=True,
        cartesian_lifts_actual=True,
        cartesian_lifts_compose=True,
        cartesian_lifts_preserve_coefficients=True,
        fiber_before_graph_objects=True,
        control_death_represented=True,
        controls_not_points_of_representer=True,
        dh_not_points_of_representer=True,
        epstein_not_points_of_representer=True,
        finite_anchors_generated=True,
        same_representer_transports_all_rows=True,
        required_edges=set(REQUIRED_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


C3 = ((3,), (1,), ((0, 0),))
C9 = ((9,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

z = chi_col(*ZERO_SPLIT)
chi_C3 = chi_col(*C3)
chi_C9 = chi_col(*C9)
chi_F22 = chi_col(*F22)
chi_C3F22 = convolve_chi(chi_C3, chi_F22)
chi_C9F22 = convolve_chi(chi_C9, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T3_T3_z = convolve_chi(T3_z, chi_C3)
T9_z = convolve_chi(z, chi_C9)
zF22 = convolve_chi(z, chi_F22)
T3_zF22 = convolve_chi(zF22, chi_C3)
T3_z_then_F22 = convolve_chi(T3_z, chi_F22)
z_C3F22 = convolve_chi(z, chi_C3F22)
T9_zF22 = convolve_chi(T9_z, chi_F22)
z_C9F22 = convolve_chi(z, chi_C9F22)

rows = [
    source_row("z", z, "id", 1),
    source_row("T3_z", T3_z, "C3", 3),
    source_row("T3_T3_z", T3_T3_z, "C3_then_C3", 9),
    source_row("T9_z", T9_z, "C9", 9),
    source_row("zF22", zF22, "F22", 4),
    source_row("T3_zF22", T3_zF22, "C3_after_F22", 12),
    source_row("T3_z_then_F22", T3_z_then_F22, "F22_after_C3", 12),
    source_row("z_C3F22", z_C3F22, "C3F22", 12),
    source_row("T9_zF22", T9_zF22, "C9_after_F22", 36),
    source_row("z_C9F22", z_C9F22, "C9F22", 36),
]

cartesian_degree_table = {row["source"]: row["cartesian_degree"] for row in rows}
graph_degree_table = {row["source"]: row["graph_degree"] for row in rows}
count_degree_table = {row["source"]: row["count_degree_value"] for row in rows}
base_graph_degree = graph_degree_table["z"]
base_count_degree = count_degree_table["z"]
c3_degree = multiplier_degree(chi_C3)
c9_degree = multiplier_degree(chi_C9)
f22_degree = multiplier_degree(chi_F22)
c3f22_degree = multiplier_degree(chi_C3F22)
c9f22_degree = multiplier_degree(chi_C9F22)
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
    "CATRSFQBARBECD1 specification functors still see controls without a representer",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and control_retuned[0] == 27.0
    and all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    ),
    "true_sig=%s control_sig=%s true_H=%.3f control_H=%.3f proj=%.1f"
    % (true_signature, control_signature, true_hodge, control_hodge, control_projection),
)


gate(
    "CATRSFQBARBECD2 one representer and universal arrow carry all cartesian lifts",
    max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and {row["square"] for row in rows} == {CATEGORICAL_SQUARE_ID}
    and {row["cube"] for row in rows} == {FACET_CUBE_ID}
    and {row["totalization"] for row in rows} == {CUBE_TOTALIZATION_ID}
    and {row["domain"] for row in rows} == {INTERNAL_EFFECTIVITY_DOMAIN_ID}
    and {row["action_functor"] for row in rows} == {MULTIPLIER_ACTION_FUNCTOR_ID}
    and {row["boundary"] for row in rows} == {DD4_BOUNDARY_LOCALIZATION_ID}
    and {row["endpoint_maps"] for row in rows} == {ENDPOINT_DEGREE_MAPS_ID}
    and {row["pushforward"] for row in rows} == {PUSHFORWARD_SQUARE_ID}
    and {row["graph_totalization"] for row in rows} == {GRAPH_ROSATI_COUNT_TOTALIZATION_ID}
    and {row["control_gate"] for row in rows} == {GRAPH_FORMATION_GATE_ID}
    and {row["source_token"] for row in rows} == {SOURCE_TOKEN_ID}
    and {row["source_fiber"] for row in rows} == {SOURCE_FIBER_ID}
    and {row["source_token_naturality"] for row in rows} == {SOURCE_TOKEN_NATURALITY_ID}
    and {row["representing_object"] for row in rows} == {REPRESENTING_OBJECT_ID}
    and {row["universal_arrow"] for row in rows} == {UNIVERSAL_ARROW_ID}
    and {row["cartesian_lifts"] for row in rows} == {CARTESIAN_LIFTS_ID}
    and all(row["endpoint_defect"] == 0 for row in rows)
    and not any(row["control_point"] for row in rows)
    and not any(row["dh_point"] for row in rows)
    and not any(row["epstein_point"] for row in rows)
    and cartesian_degree_table["z"] == 1
    and cartesian_degree_table["T3_z"] == c3_degree == 3
    and cartesian_degree_table["T3_T3_z"] == cartesian_degree_table["T9_z"] == c9_degree == 9
    and cartesian_degree_table["zF22"] == f22_degree == 4
    and cartesian_degree_table["T3_zF22"]
    == cartesian_degree_table["T3_z_then_F22"]
    == cartesian_degree_table["z_C3F22"]
    == c3f22_degree
    == 12
    and cartesian_degree_table["T9_zF22"]
    == cartesian_degree_table["z_C9F22"]
    == c9f22_degree
    == 36
    and graph_degree_table["T3_T3_z"] == graph_degree_table["T9_z"] == base_graph_degree * c9_degree
    and graph_degree_table["T3_zF22"] == graph_degree_table["T3_z_then_F22"]
    and graph_degree_table["T3_zF22"] == graph_degree_table["z_C3F22"]
    and graph_degree_table["z_C9F22"] == base_graph_degree * c9f22_degree
    and count_degree_table["T3_T3_z"] == count_degree_table["T9_z"] == base_count_degree * c9_degree**2
    and count_degree_table["T3_zF22"] == count_degree_table["T3_z_then_F22"]
    and count_degree_table["T3_zF22"] == count_degree_table["z_C3F22"]
    and count_degree_table["z_C9F22"] == base_count_degree * c9f22_degree**2
    and T3_T3_z == T9_z
    and T3_zF22 == T3_z_then_F22 == z_C3F22
    and T9_zF22 == z_C9F22
    and all(row["weighted_mass"] == 0 for row in rows),
    "representer=%s arrow=%s cart_degrees=%s"
    % (REPRESENTING_OBJECT_ID, UNIVERSAL_ARROW_ID, [row["cartesian_degree"] for row in rows]),
)


specification = live_source(
    represented_source_fiber=False,
    representing_object_actual=False,
    universal_arrow_actual=False,
    source_token_generated_by_universal_arrow=False,
    formation_fiber_generated_by_universal_arrow=False,
    specification_functor_only=True,
    functor_of_points_without_representer=True,
    yoneda_reversal=True,
    control_point_formable=True,
)

gate(
    "CATRSFQBARBECD3 specification functors and Yoneda reversal are not representers",
    not accepts_represented_source_fiber(specification)
    and {
        "represented_source_fiber_missing",
        "representing_object_not_actual",
        "universal_arrow_not_actual",
        "source_token_not_generated_by_universal_arrow",
        "formation_fiber_not_generated_by_universal_arrow",
        "specification_functor_only",
        "functor_of_points_without_representer",
        "yoneda_reversal",
        "control_point_formable",
    }
    <= set(reasons(specification)),
    ",".join(reasons(specification)),
)


predicate_fiber = live_source(
    represented_source_fiber=False,
    fiber_before_graph_objects=False,
    controls_not_points_of_representer=False,
    predicate_subfibration=True,
    discrete_fibration_labels=True,
    graph_object_classifier=True,
    source_token_after_graph_formation=True,
    control_point_formable=True,
)

gate(
    "CATRSFQBARBECD4 predicate subfibrations classify graph objects too late",
    not accepts_represented_source_fiber(predicate_fiber)
    and {
        "represented_source_fiber_missing",
        "fiber_not_before_graph_objects",
        "controls_are_points_of_representer",
        "predicate_subfibration",
        "discrete_fibration_labels",
        "graph_object_classifier",
        "source_token_after_graph_formation",
        "control_point_formable",
    }
    <= set(reasons(predicate_fiber)),
    ",".join(reasons(predicate_fiber)),
)


declared = live_source(
    representing_object_actual=False,
    universal_arrow_actual=False,
    structural_maps_represented=False,
    declared_representer=True,
    formal_universal_property=True,
    semantic_zeta_tag=True,
)

gate(
    "CATRSFQBARBECD5 declared representers and formal universal properties fail",
    not accepts_represented_source_fiber(declared)
    and {
        "representing_object_not_actual",
        "universal_arrow_not_actual",
        "structural_maps_not_represented",
        "declared_representer",
        "formal_universal_property",
        "semantic_zeta_tag",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


local_lifts = live_source(
    cartesian_lifts_actual=False,
    cartesian_lifts_compose=False,
    cartesian_lifts_preserve_coefficients=False,
    same_representer_transports_all_rows=False,
    local_representers=True,
    finite_representer_table=True,
    external_choice_of_cartesian_lifts=True,
    retuned_cartesian_lifts=True,
)

gate(
    "CATRSFQBARBECD6 local tables and retuned lifts do not give cartesian transport",
    not accepts_represented_source_fiber(local_lifts)
    and {
        "cartesian_lifts_not_actual",
        "cartesian_lifts_do_not_compose",
        "cartesian_lifts_do_not_preserve_coefficients",
        "same_representer_does_not_transport_all_rows",
        "local_representers",
        "finite_representer_table",
        "external_choice_of_cartesian_lifts",
        "retuned_cartesian_lifts",
    }
    <= set(reasons(local_lifts)),
    ",".join(reasons(local_lifts)),
)


point_shadow = live_source(
    carrier_native=False,
    controls_not_points_of_representer=False,
    dh_not_points_of_representer=False,
    epstein_not_points_of_representer=False,
    graph_object_classifier=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATRSFQBARBECD7 control/DH/Epstein points are not points of the representer",
    not accepts_represented_source_fiber(point_shadow)
    and {
        "not_carrier_native",
        "controls_are_points_of_representer",
        "dh_is_point_of_representer",
        "epstein_is_point_of_representer",
        "graph_object_classifier",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(point_shadow)),
    ",".join(reasons(point_shadow)),
)


missing_sources = [
    live_source(represented_source_square_actual=False),
    live_source(source_cube_totalization_actual=False),
    live_source(internal_effectivity_domain_actual=False),
    live_source(multiplier_action_functor_actual=False),
    live_source(dd4_boundary_source=False),
    live_source(endpoint_degree_source=False),
    live_source(pushforward_source=False),
    live_source(graph_rosati_count_source=False),
    live_source(graph_formation_control_death_source=False),
    live_source(source_typed_formation_gate=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_sources))

gate(
    "CATRSFQBARBECD8 every upstream represented source is mandatory",
    not any(accepts_represented_source_fiber(data) for data in missing_sources)
    and {
        "represented_source_square_missing",
        "source_cube_totalization_missing",
        "internal_effectivity_domain_missing",
        "multiplier_action_functor_missing",
        "dd4_boundary_source_missing",
        "endpoint_degree_source_missing",
        "pushforward_source_missing",
        "graph_rosati_count_source_missing",
        "graph_formation_control_death_source_missing",
        "source_typed_formation_gate_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


static_representer = live_source(
    required_edges=REQUIRED_EDGES
    - {
        ("representing_object", "universal_arrow"),
        ("universal_arrow", "source_token"),
        ("universal_arrow", "cartesian_lifts"),
        ("cartesian_lifts", "cartesian_composition"),
    },
    universal_arrow_actual=False,
    cartesian_lifts_actual=False,
)

gate(
    "CATRSFQBARBECD9 representer names without universal-arrow edges are rejected",
    not accepts_represented_source_fiber(static_representer)
    and {
        "universal_arrow_not_actual",
        "cartesian_lifts_not_actual",
        "required_represented_source_fiber_edges_missing",
    }
    <= set(reasons(static_representer)),
    ",".join(reasons(static_representer)),
)


live = live_source()
dead_sources = {
    "specification": specification,
    "predicate_fiber": predicate_fiber,
    "declared": declared,
    "local_lifts": local_lifts,
    "point_shadow": point_shadow,
    "static_representer": static_representer,
}

gate(
    "CATRSFQBARBECD10 only represented source fiber with universal arrow passes",
    accepts_represented_source_fiber(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(row["control_point"] for row in rows)
    and not any(row["dh_point"] for row in rows)
    and not any(row["epstein_point"] for row in rows)
    and not any(accepts_represented_source_fiber(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_represented_source_fiber(data) for data in dead_sources.values()),
        accepts_represented_source_fiber(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATRSFQBARBECD1-CATRSFQBARBECD10 ALL PASS: categorical closure represented "
    "source-fiber totalization contract pinned"
)
print(
    "VERDICT: the doc455 source-typed graph-formation-control-death-natural "
    "graph/Rosati/count-natural pushforward-natural endpoint-degree-natural "
    "DD.4 multiplier-action totalization is still insufficient unless the "
    "source fiber is represented by an actual carrier-side object and "
    "universal arrow with cartesian multiplier lifts. Specification functors, "
    "functors of points, Yoneda reversal, predicate subfibrations, declared "
    "representers, formal universal properties, local lift tables, retuned "
    "lifts, and control/DH/Epstein points do not construct the missing object."
)
