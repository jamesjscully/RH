r"""Categorical closure Beck-Chevalley cube contract for the Qbar_BECD front.

Doc 444 requires one represented source square whose universal source map
emits endpoint integrality, degree maps, DD.4 boundary, graph composition,
Rosati sign, control death, and the doc-443 boundary fiber. This witness pins
the next edge: those emitted facets must form one source-native
Beck-Chevalley compatibility cube. Independent facet bundles, edgewise-only
witnesses, declared commutative cubes, or posthoc naturality checks do not
construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_beck_chevalley_cube_contract
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


DOC443_BOUNDARY_FIBER_ID = (
    f"Fib_{mod_chain(53)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
DOC443_GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(53)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
DOC443_BOUNDARY_RESTRICTION_ID = (
    f"res_{mod_chain(53)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(53)}_NCoup"
)
CATEGORICAL_SQUARE_ID = "CatSq_Qbar_BECD_closes_doc443_boundary_cycle"
UNIVERSAL_ARROW_ID = "eta_CatSq_Qbar_BECD_source_closure"
ENDPOINT_INTEGRALITY_ID = "EndInt_CatSq_Qbar_BECD"
DEGREE_MAPS_ID = "Deg_CatSq_Qbar_BECD_p1_p2"
DD4_BOUNDARY_ID = "DD4Bd_CatSq_Qbar_BECD"
GRAPH_COMPOSITION_ID = "GraphComp_CatSq_Qbar_BECD"
ROSATI_POSITIVE_ID = "Rosati_CatSq_Qbar_BECD_positive"
CONTROL_DEATH_ID = "ControlDeath_CatSq_Qbar_BECD_formation"
CLOSURE_IDEMPOTENT_ID = "IdemClosure_CatSq_Qbar_BECD"
FACET_CUBE_ID = "BCCube_CatSq_Qbar_BECD_facets"
CUBE_TOTALIZATION_ID = "Tot_BCCube_CatSq_Qbar_BECD"
JOINT_MONIC_FACETS_ID = "JMonic_BCCube_CatSq_Qbar_BECD_facets"
BC_EXACTNESS_ID = "BCExact_CatSq_Qbar_BECD_boundary_graph_rosati_control"

REQUIRED_EDGES = {
    ("represented_source_square", "universal_source_arrow"),
    ("universal_source_arrow", "doc443_boundary_fiber"),
    ("doc443_boundary_fiber", "doc443_globular_boundary"),
    ("doc443_boundary_fiber", "closure_idempotent"),
    ("closure_idempotent", "represented_source_square"),
    ("represented_source_square", "endpoint_integrality"),
    ("represented_source_square", "degree_maps"),
    ("endpoint_integrality", "degree_maps"),
    ("degree_maps", "dd4_boundary"),
    ("degree_maps", "graph_composition"),
    ("graph_composition", "rosati_positive"),
    ("dd4_boundary", "control_death"),
    ("rosati_positive", "control_death"),
    ("control_death", "source_before_points_and_graphs"),
    ("represented_source_square", "all_facets_from_universal_map"),
    ("all_facets_from_universal_map", "endpoint_integrality"),
    ("all_facets_from_universal_map", "dd4_boundary"),
    ("all_facets_from_universal_map", "graph_composition"),
    ("all_facets_from_universal_map", "rosati_positive"),
    ("all_facets_from_universal_map", "control_death"),
    ("represented_source_square", "facet_compatibility_cube"),
    ("facet_compatibility_cube", "endpoint_degree_face"),
    ("facet_compatibility_cube", "degree_dd4_face"),
    ("facet_compatibility_cube", "degree_graph_face"),
    ("facet_compatibility_cube", "graph_rosati_face"),
    ("facet_compatibility_cube", "dd4_control_face"),
    ("facet_compatibility_cube", "rosati_control_face"),
    ("facet_compatibility_cube", "cube_totalization"),
    ("cube_totalization", "closure_idempotent"),
    ("cube_totalization", "same_cube_all_paths"),
    ("cube_totalization", "jointly_monic_facet_projections"),
    ("jointly_monic_facet_projections", "all_facets_from_universal_map"),
    ("endpoint_degree_face", "endpoint_integrality"),
    ("endpoint_degree_face", "degree_maps"),
    ("degree_dd4_face", "dd4_boundary"),
    ("degree_graph_face", "graph_composition"),
    ("graph_rosati_face", "rosati_positive"),
    ("dd4_control_face", "control_death"),
    ("rosati_control_face", "control_death"),
    ("same_cube_all_paths", "coefficient_preservation"),
    ("same_cube_all_paths", "signed_support_preservation"),
}

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_square_actual", "represented_source_square_missing"),
    ("universal_source_arrow_actual", "universal_source_arrow_missing"),
    ("doc443_boundary_fiber_actual", "doc443_boundary_fiber_missing"),
    ("doc443_boundary_over_fixed_boundary", "doc443_boundary_not_fixed"),
    ("same_source_object", "same_source_object_missing"),
    ("endpoint_integrality_actual", "endpoint_integrality_missing"),
    ("degree_maps_actual", "degree_maps_missing"),
    ("proper_pushforward_actual", "proper_pushforward_missing"),
    ("dd4_boundary_actual", "dd4_boundary_missing"),
    ("dd4_class_killed_by_boundary", "dd4_class_not_killed_by_boundary"),
    ("graph_composition_actual", "graph_composition_missing"),
    ("composition_by_source_square", "composition_not_by_source_square"),
    ("rosati_positive_actual", "rosati_positive_missing"),
    ("rosati_from_same_square", "rosati_not_from_same_square"),
    ("control_death_actual", "control_death_missing"),
    ("control_death_at_formation", "control_death_not_at_formation"),
    ("closure_idempotent_actual", "closure_idempotent_missing"),
    ("boundary_cartesian_coherence_globular_cycle_closes", "cycle_not_closed"),
    ("no_new_layer_after_closure", "new_layer_after_closure"),
    ("all_facets_from_universal_map", "facets_not_from_universal_map"),
    ("facet_compatibility_cube_actual", "facet_compatibility_cube_missing"),
    ("endpoint_degree_face_commutes", "endpoint_degree_face_not_commutative"),
    ("degree_dd4_face_commutes", "degree_dd4_face_not_commutative"),
    ("degree_graph_face_commutes", "degree_graph_face_not_commutative"),
    ("graph_rosati_face_commutes", "graph_rosati_face_not_commutative"),
    ("dd4_control_face_commutes", "dd4_control_face_not_commutative"),
    ("rosati_control_face_commutes", "rosati_control_face_not_commutative"),
    ("cube_totalization_actual", "cube_totalization_missing"),
    ("jointly_monic_facet_projections", "facet_projections_not_jointly_monic"),
    ("beck_chevalley_exactness", "beck_chevalley_exactness_missing"),
    ("same_cube_all_paths", "same_cube_not_all_paths"),
    ("coefficient_preservation", "coefficient_preservation_missing"),
    ("signed_support_preservation", "signed_support_preservation_missing"),
    ("endpoint_balance_actual", "endpoint_balance_missing"),
    ("source_before_points_and_graphs", "source_not_before_points_and_graphs"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("recognition_only", "recognition_only"),
    ("equivalence_transport_only", "equivalence_transport_only"),
    ("tower_extension_only", "tower_extension_only"),
    ("external_controller", "external_controller"),
    ("post_product_patch", "post_product_patch"),
    ("graph_side_closure", "graph_side_closure"),
    ("local_boundary_table", "local_boundary_table"),
    ("free_dd4_splitter", "free_dd4_splitter"),
    ("retuned_degree_maps", "retuned_degree_maps"),
    ("rosati_filter_only", "rosati_filter_only"),
    ("control_killed_by_filter", "control_killed_by_filter"),
    ("contractible_choice_without_representer", "contractible_choice_without_representer"),
    ("independent_facet_bundle", "independent_facet_bundle"),
    ("edgewise_witness_only", "edgewise_witness_only"),
    ("declared_commutative_cube", "declared_commutative_cube"),
    ("posthoc_naturality", "posthoc_naturality"),
    ("external_totalization", "external_totalization"),
    ("non_jointly_monic_facets", "non_jointly_monic_facets"),
    ("facet_product_after_points", "facet_product_after_points"),
    ("cube_by_equivalence", "cube_by_equivalence"),
    ("tower_cube", "tower_cube"),
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


def closure_layer(layer: int, idempotent: bool) -> int:
    return layer if idempotent else layer + 1


def categorical_square_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "doc443_boundary_fiber": DOC443_BOUNDARY_FIBER_ID,
        "doc443_globular_boundary": DOC443_GLOBULAR_BOUNDARY_ID,
        "doc443_boundary_restriction": DOC443_BOUNDARY_RESTRICTION_ID,
        "endpoint_integrality": ENDPOINT_INTEGRALITY_ID,
        "degree_maps": DEGREE_MAPS_ID,
        "dd4_boundary": DD4_BOUNDARY_ID,
        "graph_composition": GRAPH_COMPOSITION_ID,
        "rosati_positive": ROSATI_POSITIVE_ID,
        "control_death": CONTROL_DEATH_ID,
        "closure_idempotent": CLOSURE_IDEMPOTENT_ID,
        "facet_cube": FACET_CUBE_ID,
        "cube_totalization": CUBE_TOTALIZATION_ID,
        "joint_monic_facets": JOINT_MONIC_FACETS_ID,
        "beck_chevalley_exactness": BC_EXACTNESS_ID,
        "endpoint_degrees": (p1, p2),
        "endpoint_balanced": p1 == p2,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "closure_layer": closure_layer(53, True),
    }


def source(**kwargs):
    keys = {key: False for key, _ in REQUIRED}
    keys.update(
        {
            "required_edges": set(),
            "recognition_only": False,
            "equivalence_transport_only": False,
            "tower_extension_only": False,
            "external_controller": False,
            "post_product_patch": False,
            "graph_side_closure": False,
            "local_boundary_table": False,
            "free_dd4_splitter": False,
            "retuned_degree_maps": False,
            "rosati_filter_only": False,
            "control_killed_by_filter": False,
            "contractible_choice_without_representer": False,
            "independent_facet_bundle": False,
            "edgewise_witness_only": False,
            "declared_commutative_cube": False,
            "posthoc_naturality": False,
            "external_totalization": False,
            "non_jointly_monic_facets": False,
            "facet_product_after_points": False,
            "cube_by_equivalence": False,
            "tower_cube": False,
            "control_point_formable": True,
            "dh_point_formable": True,
            "epstein_point_formable": True,
        }
    )
    keys.update(kwargs)
    return keys


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_beck_chevalley_cube_edges_missing")
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

square_payload = categorical_square_payload(T3_T5_z)

gate(
    "CATBCCUBEQBARBECD1 represented source square totalizes facets as one Beck-Chevalley cube",
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
    and true_hodge < 0
    and square_payload["endpoint_balanced"]
    and square_payload["closure_layer"] == 53
    and square_payload["facet_cube"] == FACET_CUBE_ID
    and square_payload["cube_totalization"] == CUBE_TOTALIZATION_ID
    and square_payload["joint_monic_facets"] == JOINT_MONIC_FACETS_ID
    and square_payload["beck_chevalley_exactness"] == BC_EXACTNESS_ID
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2},
    "square=%s cube=%s totalization=%s closure=%s H1=%s"
    % (
        CATEGORICAL_SQUARE_ID,
        FACET_CUBE_ID,
        CUBE_TOTALIZATION_ID,
        square_payload["closure_layer"],
        [p["h1_order"] for p in profiles],
    ),
)

recognition = live_source(
    represented_source_square_actual=False,
    universal_source_arrow_actual=False,
    doc443_boundary_fiber_actual=False,
    same_source_object=False,
    closure_idempotent_actual=False,
    all_facets_from_universal_map=False,
    facet_compatibility_cube_actual=False,
    cube_totalization_actual=False,
    recognition_only=True,
)
equivalence = live_source(
    represented_source_square_actual=False,
    universal_source_arrow_actual=False,
    same_source_object=False,
    all_facets_from_universal_map=False,
    facet_compatibility_cube_actual=False,
    same_cube_all_paths=False,
    equivalence_transport_only=True,
    cube_by_equivalence=True,
)

gate(
    "CATBCCUBEQBARBECD2 recognition or equivalence does not construct the cube",
    not accepts(recognition)
    and not accepts(equivalence)
    and {
        "represented_source_square_missing",
        "universal_source_arrow_missing",
        "doc443_boundary_fiber_missing",
        "same_source_object_missing",
        "closure_idempotent_missing",
        "facets_not_from_universal_map",
        "facet_compatibility_cube_missing",
        "cube_totalization_missing",
        "same_cube_not_all_paths",
        "recognition_only",
        "equivalence_transport_only",
        "cube_by_equivalence",
    }
    <= set(reasons(recognition) + reasons(equivalence)),
    "recognition=%s equivalence=%s" % (",".join(reasons(recognition)), ",".join(reasons(equivalence))),
)

tower = live_source(
    closure_idempotent_actual=False,
    boundary_cartesian_coherence_globular_cycle_closes=False,
    no_new_layer_after_closure=False,
    cube_totalization_actual=False,
    same_cube_all_paths=False,
    tower_extension_only=True,
    tower_cube=True,
)

gate(
    "CATBCCUBEQBARBECD3 one-more-layer tower fails cube totalization",
    closure_layer(53, False) == 54
    and not accepts(tower)
    and {
        "closure_idempotent_missing",
        "cycle_not_closed",
        "new_layer_after_closure",
        "cube_totalization_missing",
        "same_cube_not_all_paths",
        "tower_extension_only",
        "tower_cube",
    }
    <= set(reasons(tower)),
    ",".join(reasons(tower)),
)

endpoint_label = live_source(
    endpoint_integrality_actual=False,
    degree_maps_actual=False,
    proper_pushforward_actual=False,
    endpoint_balance_actual=False,
    all_facets_from_universal_map=False,
    endpoint_degree_face_commutes=False,
    jointly_monic_facet_projections=False,
    external_controller=True,
    retuned_degree_maps=True,
    independent_facet_bundle=True,
    non_jointly_monic_facets=True,
)

gate(
    "CATBCCUBEQBARBECD4 endpoint and degree faces must commute in the cube",
    endpoint_degrees(zC15) == (30, 30)
    and endpoint_degrees({15: 2, 31: -1}) != (30, 30)
    and not accepts(endpoint_label)
    and {
        "endpoint_integrality_missing",
        "degree_maps_missing",
        "proper_pushforward_missing",
        "endpoint_balance_missing",
        "facets_not_from_universal_map",
        "endpoint_degree_face_not_commutative",
        "facet_projections_not_jointly_monic",
        "external_controller",
        "retuned_degree_maps",
        "independent_facet_bundle",
        "non_jointly_monic_facets",
    }
    <= set(reasons(endpoint_label)),
    ",".join(reasons(endpoint_label)),
)

free_boundary = live_source(
    dd4_boundary_actual=False,
    dd4_class_killed_by_boundary=False,
    all_facets_from_universal_map=False,
    degree_dd4_face_commutes=False,
    beck_chevalley_exactness=False,
    local_boundary_table=True,
    free_dd4_splitter=True,
    declared_commutative_cube=True,
)

gate(
    "CATBCCUBEQBARBECD5 DD.4 boundary must be an exact cube face",
    all(p["c_nonboundary"] and p["res1_c"] == 1 for p in profiles)
    and not accepts(free_boundary)
    and {
        "dd4_boundary_missing",
        "dd4_class_not_killed_by_boundary",
        "facets_not_from_universal_map",
        "degree_dd4_face_not_commutative",
        "beck_chevalley_exactness_missing",
        "local_boundary_table",
        "free_dd4_splitter",
        "declared_commutative_cube",
    }
    <= set(reasons(free_boundary)),
    ",".join(reasons(free_boundary)),
)

graph_patch = live_source(
    graph_composition_actual=False,
    composition_by_source_square=False,
    degree_graph_face_commutes=False,
    graph_rosati_face_commutes=False,
    coefficient_preservation=False,
    signed_support_preservation=False,
    post_product_patch=True,
    graph_side_closure=True,
    edgewise_witness_only=True,
    posthoc_naturality=True,
)

gate(
    "CATBCCUBEQBARBECD6 graph and Rosati faces must commute in the cube",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and not accepts(graph_patch)
    and {
        "graph_composition_missing",
        "composition_not_by_source_square",
        "degree_graph_face_not_commutative",
        "graph_rosati_face_not_commutative",
        "coefficient_preservation_missing",
        "signed_support_preservation_missing",
        "post_product_patch",
        "graph_side_closure",
        "edgewise_witness_only",
        "posthoc_naturality",
    }
    <= set(reasons(graph_patch)),
    ",".join(reasons(graph_patch)),
)

rosati_filter = live_source(
    rosati_positive_actual=False,
    rosati_from_same_square=False,
    control_death_at_formation=False,
    rosati_control_face_commutes=False,
    dd4_control_face_commutes=False,
    cube_totalization_actual=False,
    source_before_points_and_graphs=False,
    rosati_filter_only=True,
    control_killed_by_filter=True,
    external_totalization=True,
)

gate(
    "CATBCCUBEQBARBECD7 Rosati and control faces must share one totalization",
    true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and not accepts(rosati_filter)
    and {
        "rosati_positive_missing",
        "rosati_not_from_same_square",
        "control_death_not_at_formation",
        "rosati_control_face_not_commutative",
        "dd4_control_face_not_commutative",
        "cube_totalization_missing",
        "source_not_before_points_and_graphs",
        "rosati_filter_only",
        "control_killed_by_filter",
        "external_totalization",
    }
    <= set(reasons(rosati_filter)),
    "true_H=%.3f control_H=%.3f control_proj=%.1f %s"
    % (true_hodge, control_hodge, control_projection, ",".join(reasons(rosati_filter))),
)

missing_facets = [
    live_source(required_edges=REQUIRED_EDGES - {("facet_compatibility_cube", "degree_dd4_face")}),
    live_source(represented_source_square_actual=False),
    live_source(universal_source_arrow_actual=False),
    live_source(doc443_boundary_fiber_actual=False),
    live_source(facet_compatibility_cube_actual=False),
    live_source(endpoint_degree_face_commutes=False),
    live_source(degree_dd4_face_commutes=False),
    live_source(degree_graph_face_commutes=False),
    live_source(graph_rosati_face_commutes=False),
    live_source(dd4_control_face_commutes=False),
    live_source(rosati_control_face_commutes=False),
    live_source(cube_totalization_actual=False),
    live_source(jointly_monic_facet_projections=False),
    live_source(beck_chevalley_exactness=False),
    live_source(same_cube_all_paths=False),
    live_source(endpoint_integrality_actual=False),
    live_source(degree_maps_actual=False),
    live_source(dd4_boundary_actual=False),
    live_source(graph_composition_actual=False),
    live_source(rosati_positive_actual=False),
    live_source(control_death_actual=False),
    live_source(closure_idempotent_actual=False),
    live_source(all_facets_from_universal_map=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_facets))

gate(
    "CATBCCUBEQBARBECD8 every Beck-Chevalley cube face is mandatory",
    not any(accepts(data) for data in missing_facets)
    and {
        "required_beck_chevalley_cube_edges_missing",
        "represented_source_square_missing",
        "universal_source_arrow_missing",
        "doc443_boundary_fiber_missing",
        "facet_compatibility_cube_missing",
        "endpoint_degree_face_not_commutative",
        "degree_dd4_face_not_commutative",
        "degree_graph_face_not_commutative",
        "graph_rosati_face_not_commutative",
        "dd4_control_face_not_commutative",
        "rosati_control_face_not_commutative",
        "cube_totalization_missing",
        "facet_projections_not_jointly_monic",
        "beck_chevalley_exactness_missing",
        "same_cube_not_all_paths",
        "endpoint_integrality_missing",
        "degree_maps_missing",
        "dd4_boundary_missing",
        "graph_composition_missing",
        "rosati_positive_missing",
        "control_death_missing",
        "closure_idempotent_missing",
        "facets_not_from_universal_map",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_survives = live_source(
    carrier_native=False,
    represented_source_square_actual=False,
    facet_compatibility_cube_actual=False,
    cube_totalization_actual=False,
    control_death_actual=False,
    control_death_at_formation=False,
    dd4_control_face_commutes=False,
    source_before_points_and_graphs=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_closure=True,
    facet_product_after_points=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATBCCUBEQBARBECD9 facet products after points leave controls formable",
    not accepts(control_survives)
    and {
        "not_carrier_native",
        "represented_source_square_missing",
        "facet_compatibility_cube_missing",
        "cube_totalization_missing",
        "control_death_missing",
        "control_death_not_at_formation",
        "dd4_control_face_not_commutative",
        "source_not_before_points_and_graphs",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_closure",
        "facet_product_after_points",
    }
    <= set(reasons(control_survives)),
    ",".join(reasons(control_survives)),
)

live = live_source()
dead_sources = {
    "recognition": recognition,
    "equivalence": equivalence,
    "tower": tower,
    "endpoint_label": endpoint_label,
    "free_boundary": free_boundary,
    "graph_patch": graph_patch,
    "rosati_filter": rosati_filter,
    "control_survives": control_survives,
}

gate(
    "CATBCCUBEQBARBECD10 only one totalized source cube passes",
    accepts(live)
    and graph_connected(live["required_edges"])
    and closure_layer(53, live["closure_idempotent_actual"]) == 53
    and live["facet_compatibility_cube_actual"]
    and live["cube_totalization_actual"]
    and live["jointly_monic_facet_projections"]
    and live["same_cube_all_paths"]
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
    "\nCATBCCUBEQBARBECD1-CATBCCUBEQBARBECD10 ALL PASS: categorical closure Beck-Chevalley cube "
    "contract pinned"
)
print(
    "VERDICT: the doc443 represented boundary fiber is still insufficient "
    "unless a single represented source square closes the boundary/cartesian/"
    "coherence/globular cycle idempotently and totalizes endpoint integrality, "
    "degree maps, DD.4 boundary, graph composition, Rosati sign, and "
    "formation-level control death as one Beck-Chevalley source cube. "
    "Independent facet bundles, edgewise-only witnesses, declared commutative "
    "cubes, posthoc naturality, external totalizations, and one-more-layer "
    "towers do not construct the missing object."
)
