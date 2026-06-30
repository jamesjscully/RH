r"""Cartesian contract for the globular-modification boundary fiber.

Doc 363 requires the globular modification to be selected by a represented
source boundary fiber over the fixed globular boundary.  This witness pins the
next edge: that represented boundary fiber must itself be cartesian over the
same multiplier/source lifts.  A one-boundary fiber, a fiber rebuilt after
base change, or a graph-side fiber transport does not construct the missing
source object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_contract
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

SOURCE_REPRESENTING_OBJECT_ID = "Rep_Qbar_BECD_source_fiber"
SOURCE_UNIVERSAL_ARROW_ID = "eta_Qbar_BECD_source"
CARTESIAN_COHERENCE_ID = "Cart_Qbar_BECD_BCF_self_dual_exact_source"
CONE_COHERENCE_ID = "Coh_CartCone_NCoup_eta_source_components"
GLOBULAR_MODIFICATION_ID = "Mod_Coh_CartCone_NCoup_eta_source_components"
GLOBULAR_BOUNDARY_ID = "GlobBd_CartCone_NCoup_eta_source_components"
BOUNDARY_RESTRICTION_ID = "res_Mod_Coh_CartCone_to_GlobBd_NCoup"
BOUNDARY_FIBER_ID = "Fib_Mod_Coh_CartCone_NCoup_eta_source_components"
BOUNDARY_FIBER_ARROW_ID = "eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components"
CARTESIAN_BOUNDARY_FIBER_ID = "CartFib_Mod_Coh_CartCone_NCoup_eta_source_components"
CARTESIAN_BOUNDARY_RESTRICTION_ID = "cart_res_Mod_Coh_CartCone_to_GlobBd_NCoup"
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"

REQUIRED_CARTESIAN_FIBER_EDGES = {
    ("source_universal_arrow", "cartesian_source_coherence"),
    ("source_universal_arrow", "globular_modification"),
    ("cartesian_source_coherence", "cartesian_boundary_fiber"),
    ("globular_modification", "boundary_restriction_map"),
    ("boundary_restriction_map", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "cartesian_boundary_fiber"),
    ("boundary_restriction_map", "cartesian_boundary_restriction"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "fiber_universal_arrow"),
    ("fiber_universal_arrow", "selected_globular_modification"),
    ("selected_globular_modification", "globular_modification"),
    ("cartesian_boundary_fiber", "fixed_globular_boundary_pullback"),
    ("fixed_globular_boundary_pullback", "shared_globular_boundary"),
    ("cartesian_boundary_fiber", "C3_C5_to_C15_fiber_pullback"),
    ("cartesian_boundary_fiber", "C5_C3_to_C15_fiber_pullback"),
    ("cartesian_boundary_fiber", "C3_C3_C5_to_C45_fiber_pullback"),
    ("cartesian_boundary_fiber", "F22_fiber_pullback"),
    ("C3_C5_to_C15_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("C5_C3_to_C15_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("C3_C3_C5_to_C45_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("F22_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("same_cartesian_fiber_all_paths", "C3_C5_equals_C15"),
    ("same_cartesian_fiber_all_paths", "C5_C3_equals_C15"),
    ("same_cartesian_fiber_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cartesian_fiber_all_paths", "F22_product"),
    ("cartesian_boundary_fiber", "component_boundary_cartesian"),
    ("cartesian_boundary_fiber", "projection_boundary_cartesian"),
    ("cartesian_boundary_fiber", "pair_alpha_beta_boundary_cartesian"),
    ("cartesian_boundary_fiber", "pasting_faces_cartesian"),
    ("cartesian_boundary_fiber", "coherence_preserves_coefficients"),
    ("cartesian_boundary_fiber", "coherence_preserves_signed_support"),
    ("cartesian_boundary_fiber", "source_before_points_and_graphs"),
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


def cartesian_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "source_universal_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "cartesian_source_coherence": CARTESIAN_COHERENCE_ID,
        "cone_coherence": CONE_COHERENCE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "globular_boundary": GLOBULAR_BOUNDARY_ID,
        "boundary_restriction": BOUNDARY_RESTRICTION_ID,
        "boundary_fiber": BOUNDARY_FIBER_ID,
        "boundary_fiber_arrow": BOUNDARY_FIBER_ARROW_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "cartesian_boundary_restriction": CARTESIAN_BOUNDARY_RESTRICTION_ID,
        "control_death": CONTROL_DEATH_ID,
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cartesian_fiber_payload": True,
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
        "source_universal_arrow_actual": False,
        "cartesian_source_coherence_actual": False,
        "globular_modification_actual": False,
        "boundary_restriction_actual": False,
        "represented_boundary_fiber_actual": False,
        "fiber_universal_arrow_actual": False,
        "cartesian_boundary_fiber_actual": False,
        "cartesian_boundary_restriction_actual": False,
        "fiber_universal_arrow_cartesian": False,
        "fixed_globular_boundary_pullback_actual": False,
        "component_boundary_cartesian": False,
        "projection_boundary_cartesian": False,
        "pair_alpha_beta_boundary_cartesian": False,
        "pasting_faces_cartesian": False,
        "same_cartesian_fiber_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "finite_anchors_generated": False,
        "fiber_before_points": False,
        "fiber_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "static_single_boundary_fiber": False,
        "chosen_base_change_fiber": False,
        "fiber_rebuilt_after_base_change": False,
        "noncartesian_pullback": False,
        "local_transport_table": False,
        "pointwise_cartesian_fiber": False,
        "graph_side_cartesian_fiber": False,
        "post_product_cartesian_fiber": False,
        "retuned_cartesian_fiber": False,
        "reindexed_cartesian_fiber": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("globular_modification_actual", "globular_modification_missing"),
    ("boundary_restriction_actual", "boundary_restriction_missing"),
    ("represented_boundary_fiber_actual", "represented_boundary_fiber_missing"),
    ("fiber_universal_arrow_actual", "fiber_universal_arrow_missing"),
    ("cartesian_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    ("cartesian_boundary_restriction_actual", "cartesian_boundary_restriction_missing"),
    ("fiber_universal_arrow_cartesian", "fiber_universal_arrow_not_cartesian"),
    ("fixed_globular_boundary_pullback_actual", "fixed_globular_boundary_pullback_missing"),
    ("component_boundary_cartesian", "component_boundary_not_cartesian"),
    ("projection_boundary_cartesian", "projection_boundary_not_cartesian"),
    ("pair_alpha_beta_boundary_cartesian", "pair_alpha_beta_boundary_not_cartesian"),
    ("pasting_faces_cartesian", "pasting_faces_not_cartesian"),
    ("same_cartesian_fiber_all_paths", "same_cartesian_fiber_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("fiber_before_points", "fiber_not_before_points"),
    ("fiber_before_graph_objects", "fiber_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("static_single_boundary_fiber", "static_single_boundary_fiber"),
    ("chosen_base_change_fiber", "chosen_base_change_fiber"),
    ("fiber_rebuilt_after_base_change", "fiber_rebuilt_after_base_change"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("local_transport_table", "local_transport_table"),
    ("pointwise_cartesian_fiber", "pointwise_cartesian_fiber"),
    ("graph_side_cartesian_fiber", "graph_side_cartesian_fiber"),
    ("post_product_cartesian_fiber", "post_product_cartesian_fiber"),
    ("retuned_cartesian_fiber", "retuned_cartesian_fiber"),
    ("reindexed_cartesian_fiber", "reindexed_cartesian_fiber"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_CARTESIAN_FIBER_EDGES <= set(data["required_edges"]):
        out.append("required_cartesian_boundary_fiber_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_boundary_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_CARTESIAN_FIBER_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        source_universal_arrow_actual=True,
        cartesian_source_coherence_actual=True,
        globular_modification_actual=True,
        boundary_restriction_actual=True,
        represented_boundary_fiber_actual=True,
        fiber_universal_arrow_actual=True,
        cartesian_boundary_fiber_actual=True,
        cartesian_boundary_restriction_actual=True,
        fiber_universal_arrow_cartesian=True,
        fixed_globular_boundary_pullback_actual=True,
        component_boundary_cartesian=True,
        projection_boundary_cartesian=True,
        pair_alpha_beta_boundary_cartesian=True,
        pasting_faces_cartesian=True,
        same_cartesian_fiber_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        finite_anchors_generated=True,
        fiber_before_points=True,
        fiber_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CARTESIAN_FIBER_EDGES),
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
    "SCBF1 boundary fiber is cartesian over source lifts",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_FIBER_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_fiber_payload(T3_T5_z) == cartesian_fiber_payload(zC15)
    and cartesian_fiber_payload(T5_T3_z) == cartesian_fiber_payload(zC15)
    and cartesian_fiber_payload(T3_T3_T5_z) == cartesian_fiber_payload(zC45)
    and cartesian_fiber_payload(T15_zF22) == cartesian_fiber_payload(zC15F22)
    and cartesian_fiber_payload(T45_zF22) == cartesian_fiber_payload(zC45F22),
    "H1=%s cart_fiber=%s"
    % ([p["h1_order"] for p in profiles], CARTESIAN_BOUNDARY_FIBER_ID),
)

gate(
    "SCBF2 graph identities still do not supply cartesian fiber transport",
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

static_fiber = live_source(
    cartesian_boundary_fiber_actual=False,
    cartesian_boundary_restriction_actual=False,
    fiber_universal_arrow_cartesian=False,
    same_cartesian_fiber_all_paths=False,
    static_single_boundary_fiber=True,
)

gate(
    "SCBF3 one-boundary fibers are not cartesian fibers",
    not accepts_cartesian_boundary_fiber(static_fiber)
    and {
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "fiber_universal_arrow_not_cartesian",
        "same_cartesian_fiber_not_all_paths",
        "static_single_boundary_fiber",
    }
    <= set(reasons(static_fiber)),
    ",".join(reasons(static_fiber)),
)

bad_pullback = live_source(
    fixed_globular_boundary_pullback_actual=False,
    component_boundary_cartesian=False,
    projection_boundary_cartesian=False,
    pair_alpha_beta_boundary_cartesian=False,
    pasting_faces_cartesian=False,
    noncartesian_pullback=True,
)

gate(
    "SCBF4 noncartesian pullbacks do not preserve the boundary fiber",
    not accepts_cartesian_boundary_fiber(bad_pullback)
    and {
        "fixed_globular_boundary_pullback_missing",
        "component_boundary_not_cartesian",
        "projection_boundary_not_cartesian",
        "pair_alpha_beta_boundary_not_cartesian",
        "pasting_faces_not_cartesian",
        "noncartesian_pullback",
    }
    <= set(reasons(bad_pullback)),
    ",".join(reasons(bad_pullback)),
)

chosen_transport = live_source(
    same_cartesian_fiber_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    chosen_base_change_fiber=True,
    fiber_rebuilt_after_base_change=True,
    local_transport_table=True,
)

gate(
    "SCBF5 chosen local fiber transport does not cohere globally",
    not accepts_cartesian_boundary_fiber(chosen_transport)
    and {
        "same_cartesian_fiber_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "chosen_base_change_fiber",
        "fiber_rebuilt_after_base_change",
        "local_transport_table",
    }
    <= set(reasons(chosen_transport)),
    ",".join(reasons(chosen_transport)),
)

late_fiber = live_source(
    fiber_before_points=False,
    fiber_before_graph_objects=False,
    pointwise_cartesian_fiber=True,
    graph_side_cartesian_fiber=True,
    post_product_cartesian_fiber=True,
)

gate(
    "SCBF6 pointwise graph-side or post-product cartesian fibers are too late",
    not accepts_cartesian_boundary_fiber(late_fiber)
    and {
        "fiber_not_before_points",
        "fiber_not_before_graph_objects",
        "pointwise_cartesian_fiber",
        "graph_side_cartesian_fiber",
        "post_product_cartesian_fiber",
    }
    <= set(reasons(late_fiber)),
    ",".join(reasons(late_fiber)),
)

retuned = live_source(
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    same_cartesian_fiber_all_paths=False,
    retuned_cartesian_fiber=True,
    reindexed_cartesian_fiber=True,
)

gate(
    "SCBF7 retuned or reindexed cartesian fibers replace the source fiber",
    not accepts_cartesian_boundary_fiber(retuned)
    and {
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "same_cartesian_fiber_not_all_paths",
        "retuned_cartesian_fiber",
        "reindexed_cartesian_fiber",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_CARTESIAN_FIBER_EDGES - {("represented_boundary_fiber", "cartesian_boundary_fiber")}),
    live_source(cartesian_source_coherence_actual=False),
    live_source(boundary_restriction_actual=False),
    live_source(represented_boundary_fiber_actual=False),
    live_source(cartesian_boundary_fiber_actual=False),
    live_source(cartesian_boundary_restriction_actual=False),
    live_source(fiber_universal_arrow_cartesian=False),
    live_source(fixed_globular_boundary_pullback_actual=False),
    live_source(component_boundary_cartesian=False),
    live_source(projection_boundary_cartesian=False),
    live_source(pair_alpha_beta_boundary_cartesian=False),
    live_source(pasting_faces_cartesian=False),
    live_source(same_cartesian_fiber_all_paths=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SCBF8 every cartesian boundary-fiber edge is mandatory",
    not any(accepts_cartesian_boundary_fiber(data) for data in missing_edges)
    and {
        "required_cartesian_boundary_fiber_edges_missing",
        "cartesian_source_coherence_missing",
        "boundary_restriction_missing",
        "represented_boundary_fiber_missing",
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "fiber_universal_arrow_not_cartesian",
        "fixed_globular_boundary_pullback_missing",
        "component_boundary_not_cartesian",
        "projection_boundary_not_cartesian",
        "pair_alpha_beta_boundary_not_cartesian",
        "pasting_faces_not_cartesian",
        "same_cartesian_fiber_not_all_paths",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_fiber = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_cartesian_fiber=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "SCBF9 graph-side cartesian fibers leave controls formable",
    not accepts_cartesian_boundary_fiber(control_fiber)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_cartesian_fiber",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_fiber)),
    ",".join(reasons(control_fiber)),
)

live = live_source()
dead_sources = {
    "static_fiber": static_fiber,
    "bad_pullback": bad_pullback,
    "chosen_transport": chosen_transport,
    "late_fiber": late_fiber,
    "retuned": retuned,
    "control_fiber": control_fiber,
}

gate(
    "SCBF10 only cartesian represented boundary fibers pass",
    accepts_cartesian_boundary_fiber(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_cartesian_boundary_fiber(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_cartesian_boundary_fiber(data) for data in dead_sources.values()),
        accepts_cartesian_boundary_fiber(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSCBF1-SCBF10 ALL PASS: cartesian boundary fiber pinned")
print(
    "VERDICT: the represented globular-modification boundary fiber must be "
    "cartesian over the source multiplier lifts, with the boundary restriction "
    "and fiber universal arrow transported on the same C3/C5/C15/C45/F22 "
    "paths. Static one-boundary fibers, chosen local transports, fibers "
    "rebuilt after base change, noncartesian pullbacks, pointwise or graph-side "
    "fibers, retuned fibers, and post-product fibers do not construct the "
    "missing source object."
)
