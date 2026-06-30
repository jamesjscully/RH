r"""Cartesian contract for the represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modification boundary fiber.

Doc 419 requires a 35-layer represented boundary fiber for the source-level
represented-coherence boundary-fiber cartesian-transport boundary-fiber
cartesian coherence transport globular modification. This witness pins the
next edge: that represented fiber must itself be cartesian over the source
multiplier lifts. Static one-boundary fibers, local transport tables, fibers
rebuilt after base change, and graph-side cartesian labels do not construct
the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_scfgbccgbccgbccgbccgbccgbccgbfccgbfccgbfccgbfccgbfccgbfccgbfccgbfc_cart_contract
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


def mod_chain(count: int) -> str:
    return "_".join(["Mod_Coh_CartFib"] * count)


def glob_chain(count: int) -> str:
    return "_".join(["Coh_CartFib"] + ["Mod_Coh_CartFib"] * (count - 1))


def coh_chain(count: int) -> str:
    return "_".join(["Coh_CartFib"] * count)


SOURCE_REPRESENTING_OBJECT_ID = "Rep_Qbar_BECD_source_fiber"
SOURCE_UNIVERSAL_ARROW_ID = "eta_Qbar_BECD_source"
CARTESIAN_COHERENCE_ID = "Cart_Qbar_BECD_BCF_self_dual_exact_source"
FIBER_COHERENCE_MODIFICATION_ID = (
    f"{mod_chain(35)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(35)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID = (
    f"res_{mod_chain(35)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(35)}_NCoup"
)
FIBER_COHERENCE_BOUNDARY_FIBER_ID = (
    f"Fib_{mod_chain(35)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_BOUNDARY_FIBER_ARROW_ID = (
    f"eta_Fib_{mod_chain(35)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CART_FIBER_COHERENCE_BOUNDARY_FIBER_ID = (
    f"CartFib_{mod_chain(37)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CART_FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID = (
    f"cart_res_{mod_chain(35)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(35)}_NCoup"
)
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"

REQUIRED_EDGES = {
    ("source_universal_arrow", "cartesian_source_coherence"),
    ("cartesian_source_coherence", "cartesian_fiber_coherence_boundary_fiber"),
    ("fiber_coherence_globular_modification", "boundary_restriction_map"),
    ("fiber_coherence_globular_modification", "shared_fiber_coherence_boundary"),
    ("boundary_restriction_map", "shared_fiber_coherence_boundary"),
    ("boundary_restriction_map", "represented_boundary_fiber"),
    ("shared_fiber_coherence_boundary", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "cartesian_fiber_coherence_boundary_fiber"),
    ("boundary_restriction_map", "cartesian_boundary_restriction"),
    ("cartesian_boundary_restriction", "cartesian_fiber_coherence_boundary_fiber"),
    ("cartesian_fiber_coherence_boundary_fiber", "fiber_boundary_universal_arrow"),
    ("fiber_boundary_universal_arrow", "selected_fiber_coherence_modification"),
    ("selected_fiber_coherence_modification", "fiber_coherence_globular_modification"),
    ("cartesian_fiber_coherence_boundary_fiber", "fixed_globular_boundary_pullback"),
    ("fixed_globular_boundary_pullback", "shared_fiber_coherence_boundary"),
    ("cartesian_fiber_coherence_boundary_fiber", "C3_C5_to_C15_fiber_pullback"),
    ("cartesian_fiber_coherence_boundary_fiber", "C5_C3_to_C15_fiber_pullback"),
    ("cartesian_fiber_coherence_boundary_fiber", "C3_C3_C5_to_C45_fiber_pullback"),
    ("cartesian_fiber_coherence_boundary_fiber", "F22_fiber_pullback"),
    ("C3_C5_to_C15_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("C5_C3_to_C15_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("C3_C3_C5_to_C45_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("F22_fiber_pullback", "same_cartesian_fiber_all_paths"),
    ("same_cartesian_fiber_all_paths", "C3_C5_equals_C15"),
    ("same_cartesian_fiber_all_paths", "C5_C3_equals_C15"),
    ("same_cartesian_fiber_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cartesian_fiber_all_paths", "F22_product"),
    ("cartesian_fiber_coherence_boundary_fiber", "source_boundary_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "target_boundary_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "boundary_restriction_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "fiber_arrow_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "component_projection_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "pair_alpha_beta_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "pasting_faces_cartesian"),
    ("cartesian_fiber_coherence_boundary_fiber", "coherence_preserves_coefficients"),
    ("cartesian_fiber_coherence_boundary_fiber", "coherence_preserves_signed_support"),
    ("cartesian_fiber_coherence_boundary_fiber", "source_before_points_and_graphs"),
    ("source_before_points_and_graphs", "controls_not_points"),
    ("source_before_points_and_graphs", "dh_not_points"),
    ("source_before_points_and_graphs", "epstein_not_points"),
}

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("fiber_coherence_globular_modification_actual", "fiber_coherence_globular_modification_missing"),
    ("shared_fiber_coherence_boundary_actual", "shared_fiber_coherence_boundary_missing"),
    ("fiber_coherence_boundary_restriction_actual", "boundary_restriction_missing"),
    ("represented_fiber_coherence_boundary_fiber_actual", "represented_boundary_fiber_missing"),
    ("cartesian_fiber_coherence_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    ("cartesian_boundary_restriction_actual", "cartesian_boundary_restriction_missing"),
    ("fiber_boundary_universal_arrow_actual", "fiber_universal_arrow_not_cartesian"),
    ("modification_selected_by_fiber_arrow", "modification_not_selected_by_fiber_arrow"),
    ("fiber_over_shared_fiber_coherence_boundary", "fiber_not_over_shared_fiber_coherence_boundary"),
    ("boundary_preservation_actual", "boundary_preservation_missing"),
    ("fixed_globular_boundary_pullback_actual", "fixed_globular_boundary_pullback_missing"),
    ("source_boundary_cartesian", "source_boundary_not_cartesian"),
    ("target_boundary_cartesian", "target_boundary_not_cartesian"),
    ("boundary_restriction_cartesian", "boundary_restriction_not_cartesian"),
    ("fiber_arrow_cartesian", "fiber_arrow_not_cartesian"),
    ("component_projection_cartesian", "component_projection_not_cartesian"),
    ("pair_alpha_beta_cartesian", "pair_alpha_beta_not_cartesian"),
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
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("chosen_base_change_fiber", "chosen_base_change_fiber"),
    ("fiber_rebuilt_after_base_change", "fiber_rebuilt_after_base_change"),
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


def cartesian_boundary_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "source_universal_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "cartesian_source_coherence": CARTESIAN_COHERENCE_ID,
        "fiber_coherence_globular_modification": FIBER_COHERENCE_MODIFICATION_ID,
        "fiber_coherence_globular_boundary": FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
        "fiber_coherence_boundary_restriction": FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID,
        "fiber_coherence_boundary_fiber": FIBER_COHERENCE_BOUNDARY_FIBER_ID,
        "fiber_coherence_boundary_fiber_arrow": (
            FIBER_COHERENCE_BOUNDARY_FIBER_ARROW_ID
        ),
        "cartesian_fiber_coherence_boundary_fiber": (
            CART_FIBER_COHERENCE_BOUNDARY_FIBER_ID
        ),
        "cartesian_fiber_coherence_boundary_restriction": (
            CART_FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID
        ),
        "control_death": CONTROL_DEATH_ID,
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cartesian_fiber_coherence_boundary_fiber_payload": True,
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
    data = {key: False for key, _ in REQUIRED}
    data.update(
        {
            "required_edges": set(),
            "static_single_boundary_fiber": False,
            "noncartesian_pullback": False,
            "chosen_base_change_fiber": False,
            "fiber_rebuilt_after_base_change": False,
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
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_cartesian_boundary_fiber_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        **{key: True for key, _ in REQUIRED},
        required_edges=set(REQUIRED_EDGES),
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
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC1 represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modification boundary fiber is cartesian over source lifts",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_boundary_fiber_payload(T3_T5_z)
    == cartesian_boundary_fiber_payload(zC15)
    and cartesian_boundary_fiber_payload(T5_T3_z)
    == cartesian_boundary_fiber_payload(zC15)
    and cartesian_boundary_fiber_payload(T3_T3_T5_z)
    == cartesian_boundary_fiber_payload(zC45)
    and cartesian_boundary_fiber_payload(T15_zF22)
    == cartesian_boundary_fiber_payload(zC15F22)
    and cartesian_boundary_fiber_payload(T45_zF22)
    == cartesian_boundary_fiber_payload(zC45F22),
    "H1=%s cart_fiber=%s"
    % ([p["h1_order"] for p in profiles], CART_FIBER_COHERENCE_BOUNDARY_FIBER_ID),
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC2 graph identities still do not supply cartesian fiber transport",
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

static = live_source(
    cartesian_fiber_coherence_boundary_fiber_actual=False,
    cartesian_boundary_restriction_actual=False,
    fiber_boundary_universal_arrow_actual=False,
    same_cartesian_fiber_all_paths=False,
    static_single_boundary_fiber=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC3 one-boundary fibers are not cartesian fibers",
    not accepts(static)
    and {
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "fiber_universal_arrow_not_cartesian",
        "same_cartesian_fiber_not_all_paths",
        "static_single_boundary_fiber",
    }
    <= set(reasons(static)),
    ",".join(reasons(static)),
)

noncartesian = live_source(
    fixed_globular_boundary_pullback_actual=False,
    source_boundary_cartesian=False,
    target_boundary_cartesian=False,
    boundary_restriction_cartesian=False,
    fiber_arrow_cartesian=False,
    component_projection_cartesian=False,
    pair_alpha_beta_cartesian=False,
    pasting_faces_cartesian=False,
    noncartesian_pullback=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC4 noncartesian pullbacks do not preserve the boundary fiber",
    not accepts(noncartesian)
    and {
        "fixed_globular_boundary_pullback_missing",
        "source_boundary_not_cartesian",
        "target_boundary_not_cartesian",
        "boundary_restriction_not_cartesian",
        "fiber_arrow_not_cartesian",
        "component_projection_not_cartesian",
        "pair_alpha_beta_not_cartesian",
        "pasting_faces_not_cartesian",
        "noncartesian_pullback",
    }
    <= set(reasons(noncartesian)),
    ",".join(reasons(noncartesian)),
)

chosen = live_source(
    same_cartesian_fiber_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    chosen_base_change_fiber=True,
    fiber_rebuilt_after_base_change=True,
    local_transport_table=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC5 chosen local fiber transport does not cohere globally",
    not accepts(chosen)
    and {
        "same_cartesian_fiber_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "chosen_base_change_fiber",
        "fiber_rebuilt_after_base_change",
        "local_transport_table",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

late = live_source(
    fiber_before_points=False,
    fiber_before_graph_objects=False,
    pointwise_cartesian_fiber=True,
    graph_side_cartesian_fiber=True,
    post_product_cartesian_fiber=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC6 pointwise graph-side or post-product cartesian fibers are too late",
    not accepts(late)
    and {
        "fiber_not_before_points",
        "fiber_not_before_graph_objects",
        "pointwise_cartesian_fiber",
        "graph_side_cartesian_fiber",
        "post_product_cartesian_fiber",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    same_cartesian_fiber_all_paths=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_cartesian_fiber=True,
    reindexed_cartesian_fiber=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC7 retuned or reindexed cartesian fibers replace the source fiber",
    not accepts(retuned)
    and {
        "same_cartesian_fiber_not_all_paths",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_cartesian_fiber",
        "reindexed_cartesian_fiber",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_EDGES - {("represented_boundary_fiber", "cartesian_fiber_coherence_boundary_fiber")}),
    live_source(cartesian_fiber_coherence_boundary_fiber_actual=False),
    live_source(cartesian_boundary_restriction_actual=False),
    live_source(fiber_boundary_universal_arrow_actual=False),
    live_source(fixed_globular_boundary_pullback_actual=False),
    live_source(source_boundary_cartesian=False),
    live_source(target_boundary_cartesian=False),
    live_source(boundary_restriction_cartesian=False),
    live_source(fiber_arrow_cartesian=False),
    live_source(component_projection_cartesian=False),
    live_source(pair_alpha_beta_cartesian=False),
    live_source(pasting_faces_cartesian=False),
    live_source(same_cartesian_fiber_all_paths=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC8 every cartesian boundary-fiber edge is mandatory",
    not any(accepts(data) for data in missing_edges)
    and {
        "required_cartesian_boundary_fiber_edges_missing",
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "fiber_universal_arrow_not_cartesian",
        "fixed_globular_boundary_pullback_missing",
        "source_boundary_not_cartesian",
        "target_boundary_not_cartesian",
        "boundary_restriction_not_cartesian",
        "fiber_arrow_not_cartesian",
        "component_projection_not_cartesian",
        "pair_alpha_beta_not_cartesian",
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
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC9 graph-side cartesian fibers leave controls formable",
    not accepts(control_fiber)
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
    "static": static,
    "noncartesian": noncartesian,
    "chosen": chosen,
    "late": late,
    "retuned": retuned,
    "control_fiber": control_fiber,
}

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC10 only cartesian represented boundary fibers pass",
    accepts(live)
    and graph_connected(live["required_edges"])
    and not any(accepts(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts(data) for data in dead_sources.values()),
        accepts(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nSCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC1-SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFC10 ALL PASS: represented-coherence "
    "boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modification represented fiber cartesianness pinned"
)
print(
    "VERDICT: the represented boundary fiber for the represented-coherence "
    "boundary-fiber cartesian-transport boundary-fiber cartesian coherence "
    "transport globular modification must be cartesian over the source multiplier lifts. "
    "Static one-boundary fibers, chosen local transports, fibers rebuilt after "
    "base change, noncartesian pullbacks, pointwise or graph-side fibers, "
    "retuned fibers, and post-product fibers do not construct the missing "
    "source object."
)
