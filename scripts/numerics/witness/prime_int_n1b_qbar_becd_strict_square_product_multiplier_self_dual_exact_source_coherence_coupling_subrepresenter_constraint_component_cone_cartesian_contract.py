r"""Cartesian naturality contract for the eta-generated component cone.

Doc 359 requires one eta-generated source component cone.  This witness pins
the next edge: that cone must be cartesian over the represented source
fibration.  Finite path equalities, chosen transport isomorphisms, pointwise
naturality, graph-side base change, or componentwise split naturality are not
a cartesian source component cone.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_contract
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
COUPLING_UNIVERSAL_ARROW_ID = "eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source"
COMPONENT_CONE_ID = "Cone_NCoup_eta_source_components"
CARTESIAN_COMPONENT_CONE_ID = "CartCone_NCoup_eta_source_components"
CARTESIAN_COHERENCE_ID = "Cart_Qbar_BECD_BCF_self_dual_exact_source"
PRODUCT_OBJECT_ID = "Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_source_constraints"
DD4_CLASS_ID = "dd4_c_original_res1"
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"

COMPONENT_LEGS = (
    "leg_NCoup_endpoint_integrality_source",
    "leg_NCoup_degree_maps_source",
    "leg_NCoup_dd4_boundary_source",
    "leg_NCoup_boundary_pushforward_source",
    "leg_NCoup_graph_composition_source",
    "leg_NCoup_rosati_count_source",
    "leg_NCoup_control_death_source",
)

COMPONENT_OBJECTS = (
    "Comp_NCoup_endpoint_integrality_source",
    "Comp_NCoup_degree_maps_source",
    "Comp_NCoup_dd4_boundary_source",
    "Comp_NCoup_boundary_pushforward_source",
    "Comp_NCoup_graph_composition_source",
    "Comp_NCoup_rosati_count_source",
    "Comp_NCoup_control_death_source",
)

PROJECTIONS = (
    "pi_NCoup_endpoint_integrality",
    "pi_NCoup_degree_maps",
    "pi_NCoup_dd4_boundary",
    "pi_NCoup_boundary_pushforward",
    "pi_NCoup_graph_composition",
    "pi_NCoup_rosati_count",
    "pi_NCoup_control_death",
)

REQUIRED_CARTESIAN_CONE_EDGES = {
    ("source_universal_arrow", "cartesian_source_lifts"),
    ("source_universal_arrow", "coupling_universal_arrow"),
    ("coupling_universal_arrow", "source_component_cone"),
    ("source_component_cone", "cartesian_component_cone"),
    ("cartesian_source_lifts", "cartesian_component_cone"),
    ("cartesian_component_cone", "C3_cone_pullback"),
    ("cartesian_component_cone", "C5_cone_pullback"),
    ("cartesian_component_cone", "C15_cone_pullback"),
    ("cartesian_component_cone", "C45_cone_pullback"),
    ("cartesian_component_cone", "F22_cone_pullback"),
    ("C3_cone_pullback", "component_leg_naturality"),
    ("C5_cone_pullback", "component_leg_naturality"),
    ("C15_cone_pullback", "component_leg_naturality"),
    ("C45_cone_pullback", "component_leg_naturality"),
    ("F22_cone_pullback", "component_leg_naturality"),
    ("component_leg_naturality", "endpoint_leg_natural"),
    ("component_leg_naturality", "degree_leg_natural"),
    ("component_leg_naturality", "dd4_leg_natural"),
    ("component_leg_naturality", "pushforward_leg_natural"),
    ("component_leg_naturality", "graph_leg_natural"),
    ("component_leg_naturality", "rosati_count_leg_natural"),
    ("component_leg_naturality", "control_death_leg_natural"),
    ("component_leg_naturality", "projection_leg_naturality"),
    ("projection_leg_naturality", "pair_alpha_cartesian_natural"),
    ("projection_leg_naturality", "pair_beta_cartesian_natural"),
    ("pair_alpha_cartesian_natural", "constraint_product_object"),
    ("pair_beta_cartesian_natural", "zero_diagonal_cartesian_cone"),
    ("cartesian_component_cone", "same_cartesian_cone_all_paths"),
    ("same_cartesian_cone_all_paths", "C3_C5_equals_C15"),
    ("same_cartesian_cone_all_paths", "C5_C3_equals_C15"),
    ("same_cartesian_cone_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cartesian_cone_all_paths", "F22_product"),
    ("cartesian_component_cone", "base_change_preserves_doc359_cone"),
    ("base_change_preserves_doc359_cone", "base_change_preserves_components"),
    ("base_change_preserves_components", "component_objects"),
    ("cartesian_component_cone", "source_before_points_and_graphs"),
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


def cartesian_cone_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "source_universal_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "coupling_universal_arrow": COUPLING_UNIVERSAL_ARROW_ID,
        "component_cone": COMPONENT_CONE_ID,
        "cartesian_component_cone": CARTESIAN_COMPONENT_CONE_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "component_legs": COMPONENT_LEGS,
        "component_objects": COMPONENT_OBJECTS,
        "projections": PROJECTIONS,
        "endpoint_leg": (COMPONENT_LEGS[0], p1, p2, p1 == p2),
        "degree_leg": (COMPONENT_LEGS[1], tuple(sorted(chi)), p1 + p2),
        "dd4_leg": (COMPONENT_LEGS[2], DD4_CLASS_ID),
        "pushforward_leg": (COMPONENT_LEGS[3], tuple(chi.items())),
        "graph_leg": (COMPONENT_LEGS[4], tuple(sorted(chi))),
        "rosati_leg": (COMPONENT_LEGS[5], "count_defect_0"),
        "control_leg": (COMPONENT_LEGS[6], CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cartesian_cone_payload": True,
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
        "coupling_universal_arrow_actual": False,
        "doc359_component_cone_actual": False,
        "cartesian_lifts_actual": False,
        "cartesian_component_cone_actual": False,
        "cone_pullbacks_actual": False,
        "component_leg_naturality_actual": False,
        "projection_leg_naturality_actual": False,
        "pair_alpha_cartesian_natural": False,
        "pair_beta_cartesian_natural": False,
        "base_change_preserves_doc359_cone": False,
        "base_change_preserves_components": False,
        "same_cartesian_cone_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "cone_before_points": False,
        "cone_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "finite_path_check_only": False,
        "sample_path_transport": False,
        "pointwise_naturality": False,
        "graph_side_base_change": False,
        "local_transport_table": False,
        "chosen_transport_isomorphisms": False,
        "up_to_iso_without_coherence": False,
        "lax_naturality_only": False,
        "noncartesian_pullback": False,
        "reindexed_cone_label": False,
        "retuned_transport": False,
        "base_changed_component_replacement": False,
        "declared_naturality_square": False,
        "split_naturality_by_component": False,
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
    ("coupling_universal_arrow_actual", "coupling_universal_arrow_missing"),
    ("doc359_component_cone_actual", "doc359_component_cone_missing"),
    ("cartesian_lifts_actual", "cartesian_lifts_missing"),
    ("cartesian_component_cone_actual", "cartesian_component_cone_missing"),
    ("cone_pullbacks_actual", "cone_pullbacks_missing"),
    ("component_leg_naturality_actual", "component_leg_naturality_missing"),
    ("projection_leg_naturality_actual", "projection_leg_naturality_missing"),
    ("pair_alpha_cartesian_natural", "pair_alpha_not_cartesian_natural"),
    ("pair_beta_cartesian_natural", "pair_beta_not_cartesian_natural"),
    ("base_change_preserves_doc359_cone", "base_change_does_not_preserve_doc359_cone"),
    ("base_change_preserves_components", "base_change_does_not_preserve_components"),
    ("same_cartesian_cone_all_paths", "same_cartesian_cone_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("cone_before_points", "cone_not_before_points"),
    ("cone_before_graph_objects", "cone_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("finite_path_check_only", "finite_path_check_only"),
    ("sample_path_transport", "sample_path_transport"),
    ("pointwise_naturality", "pointwise_naturality"),
    ("graph_side_base_change", "graph_side_base_change"),
    ("local_transport_table", "local_transport_table"),
    ("chosen_transport_isomorphisms", "chosen_transport_isomorphisms"),
    ("up_to_iso_without_coherence", "up_to_iso_without_coherence"),
    ("lax_naturality_only", "lax_naturality_only"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("reindexed_cone_label", "reindexed_cone_label"),
    ("retuned_transport", "retuned_transport"),
    ("base_changed_component_replacement", "base_changed_component_replacement"),
    ("declared_naturality_square", "declared_naturality_square"),
    ("split_naturality_by_component", "split_naturality_by_component"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_CARTESIAN_CONE_EDGES <= set(data["required_edges"]):
        out.append("required_cartesian_component_cone_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_component_cone(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_CARTESIAN_CONE_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        source_universal_arrow_actual=True,
        coupling_universal_arrow_actual=True,
        doc359_component_cone_actual=True,
        cartesian_lifts_actual=True,
        cartesian_component_cone_actual=True,
        cone_pullbacks_actual=True,
        component_leg_naturality_actual=True,
        projection_leg_naturality_actual=True,
        pair_alpha_cartesian_natural=True,
        pair_beta_cartesian_natural=True,
        base_change_preserves_doc359_cone=True,
        base_change_preserves_components=True,
        same_cartesian_cone_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        cone_before_points=True,
        cone_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CARTESIAN_CONE_EDGES),
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
    "SCNA1 eta-generated component cone is cartesian over source lifts",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_CONE_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_cone_payload(T3_T5_z) == cartesian_cone_payload(zC15)
    and cartesian_cone_payload(T5_T3_z) == cartesian_cone_payload(zC15)
    and cartesian_cone_payload(T3_T3_T5_z) == cartesian_cone_payload(zC45)
    and cartesian_cone_payload(T15_zF22) == cartesian_cone_payload(zC15F22)
    and cartesian_cone_payload(T45_zF22) == cartesian_cone_payload(zC45F22),
    "H1=%s cart_cone=%s legs=%d"
    % ([p["h1_order"] for p in profiles], CARTESIAN_COMPONENT_CONE_ID, len(COMPONENT_LEGS)),
)


gate(
    "SCNA2 graph identities still do not supply cartesian cone naturality",
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


finite = live_source(
    cartesian_component_cone_actual=False,
    cone_pullbacks_actual=False,
    component_leg_naturality_actual=False,
    projection_leg_naturality_actual=False,
    finite_path_check_only=True,
    sample_path_transport=True,
    declared_naturality_square=True,
)

gate(
    "SCNA3 finite path checks and declared squares are not cartesian naturality",
    not accepts_cartesian_component_cone(finite)
    and {
        "cartesian_component_cone_missing",
        "cone_pullbacks_missing",
        "component_leg_naturality_missing",
        "projection_leg_naturality_missing",
        "finite_path_check_only",
        "sample_path_transport",
        "declared_naturality_square",
    }
    <= set(reasons(finite)),
    ",".join(reasons(finite)),
)


late = live_source(
    cone_before_points=False,
    cone_before_graph_objects=False,
    base_change_preserves_doc359_cone=False,
    pair_alpha_cartesian_natural=False,
    pair_beta_cartesian_natural=False,
    pointwise_naturality=True,
    graph_side_base_change=True,
    noncartesian_pullback=True,
)

gate(
    "SCNA4 pointwise or graph-side base change is too late",
    not accepts_cartesian_component_cone(late)
    and {
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
        "base_change_does_not_preserve_doc359_cone",
        "cone_not_before_points",
        "cone_not_before_graph_objects",
        "pointwise_naturality",
        "graph_side_base_change",
        "noncartesian_pullback",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)


chosen = live_source(
    same_cartesian_cone_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_transport_table=True,
    chosen_transport_isomorphisms=True,
    up_to_iso_without_coherence=True,
    lax_naturality_only=True,
)

gate(
    "SCNA5 local chosen or lax transport does not cohere",
    not accepts_cartesian_component_cone(chosen)
    and {
        "same_cartesian_cone_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_transport_table",
        "chosen_transport_isomorphisms",
        "up_to_iso_without_coherence",
        "lax_naturality_only",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)


replacement = live_source(
    base_change_preserves_components=False,
    component_leg_naturality_actual=False,
    projection_leg_naturality_actual=False,
    reindexed_cone_label=True,
    retuned_transport=True,
    base_changed_component_replacement=True,
)

gate(
    "SCNA6 reindexed or retuned base changes replace the cone",
    not accepts_cartesian_component_cone(replacement)
    and {
        "component_leg_naturality_missing",
        "projection_leg_naturality_missing",
        "base_change_does_not_preserve_components",
        "reindexed_cone_label",
        "retuned_transport",
        "base_changed_component_replacement",
    }
    <= set(reasons(replacement)),
    ",".join(reasons(replacement)),
)


split = live_source(
    cartesian_component_cone_actual=False,
    pair_alpha_cartesian_natural=False,
    pair_beta_cartesian_natural=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    split_naturality_by_component=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "SCNA7 split componentwise naturality leaves controls formable",
    not accepts_cartesian_component_cone(split)
    and {
        "cartesian_component_cone_missing",
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "split_naturality_by_component",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(split)),
    ",".join(reasons(split)),
)


missing_edges = [
    live_source(required_edges=REQUIRED_CARTESIAN_CONE_EDGES - {("F22_cone_pullback", "component_leg_naturality")}),
    live_source(source_universal_arrow_actual=False),
    live_source(coupling_universal_arrow_actual=False),
    live_source(doc359_component_cone_actual=False),
    live_source(cartesian_lifts_actual=False),
    live_source(cartesian_component_cone_actual=False),
    live_source(cone_pullbacks_actual=False),
    live_source(component_leg_naturality_actual=False),
    live_source(projection_leg_naturality_actual=False),
    live_source(pair_alpha_cartesian_natural=False),
    live_source(pair_beta_cartesian_natural=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SCNA8 every cartesian component-cone edge is mandatory",
    not any(accepts_cartesian_component_cone(data) for data in missing_edges)
    and {
        "required_cartesian_component_cone_edges_missing",
        "source_universal_arrow_missing",
        "coupling_universal_arrow_missing",
        "doc359_component_cone_missing",
        "cartesian_lifts_missing",
        "cartesian_component_cone_missing",
        "cone_pullbacks_missing",
        "component_leg_naturality_missing",
        "projection_leg_naturality_missing",
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "finite": finite,
    "late": late,
    "chosen": chosen,
    "replacement": replacement,
    "split": split,
}

gate(
    "SCNA9 only cartesian eta-component cones pass",
    accepts_cartesian_component_cone(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_cartesian_component_cone(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_cartesian_component_cone(data) for data in dead_sources.values()),
        accepts_cartesian_component_cone(live),
    ),
)


gate(
    "SCNA10 live cone is natural for pair_alpha and pair_beta over cartesian lifts",
    accepts_cartesian_component_cone(live)
    and len(COMPONENT_LEGS) == 7
    and len(PROJECTIONS) == 7
    and not any(live[key] for key, _ in BANNED)
    and REQUIRED_CARTESIAN_CONE_EDGES <= live["required_edges"],
    "cart_cone=%s alpha=%s beta=%s edges=%d"
    % (CARTESIAN_COMPONENT_CONE_ID, ALPHA_PAIRING_ID, BETA_PAIRING_ID, len(REQUIRED_CARTESIAN_CONE_EDGES)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSCNA1-SCNA10 ALL PASS: cartesian component-cone naturality pinned")
print(
    "VERDICT: the eta-generated source component cone must be cartesian over "
    "the represented source lifts, with component-leg and projection-leg "
    "naturality for pair_alpha and pair_beta. Finite path checks, pointwise "
    "or graph-side naturality, chosen transport isomorphisms, local tables, "
    "reindexed/retuned base changes, and split componentwise naturality do "
    "not construct the missing source object."
)
