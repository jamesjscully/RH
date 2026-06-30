r"""Categorical closure self-dual exact-source coherence-coupling contract.

Doc 465 requires universal-arrow-generated source-level coherence cells for
the categorical self-dual exact BCF source. This witness pins the next edge:
those cells cannot merely preserve independent exact/DD.4/duality/graph/
control payloads. The same categorical universal arrow must generate one
non-split source-coherence coupling primitive whose dependency graph couples
the exact delta, kernel, coimage, rank-one duality, DD.4 boundary, normal
ratio, endpoint/pushforward, graph/Rosati/count, and source-level control
death before graph objects exist.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_totalization_contract
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
SQUARE_LAYER_MONOIDWIDE_COHERENCE_ID = "MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers"
SOURCE_COHERENCE_ID = "Coh_BCCube_Qbar_BECD_BCF_self_dual_exact_source_formation"
SOURCE_COUPLING_ID = "NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
CARTESIAN_COHERENCE_ID = "Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
SOURCE_MONOIDWIDE_COHERENCE_ID = "MWC_BCCube_Qbar_BECD_BCF_self_dual_exact_source"
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

REQUIRED_COUPLING_EDGES = {
    ("represented_source_square", "source_coherence_coupling_primitive"),
    ("source_cube_totalization", "source_coherence_coupling_primitive"),
    ("universal_arrow", "source_coherence_coupling_primitive"),
    ("source_coherence_coupling_primitive", "self_dual_exact_source_coherence"),
    ("source_coherence_coupling_primitive", "self_dual_exact_source_token"),
    ("source_coherence_coupling_primitive", "self_dual_exact_source_fiber"),
    ("self_dual_exact_source_fiber", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("multiplier_action_functor", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "exact_boundary_delta"),
    ("self_dual_exact_source_coherence", "cartesian_source_coherence"),
    ("self_dual_exact_source_coherence", "monoidwide_source_coherence"),
    ("source_coherence_coupling_primitive", "exact_boundary_delta"),
    ("exact_boundary_delta", "exact_sequence"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("kernel_is_cancellation_image", "coimage_preserves_signed_coefficients"),
    ("coimage_preserves_signed_coefficients", "rank_one_boundary_defect_duality"),
    ("rank_one_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank_one_boundary_defect_duality", "boundary_is_original_dd4_class"),
    ("boundary_is_original_dd4_class", "nonzero_res1"),
    ("boundary_is_original_dd4_class", "normal_ratio_self_dual_boundary"),
    ("normal_ratio_self_dual_boundary", "connecting_map_sends_c_to_zero"),
    ("normal_ratio_self_dual_boundary", "p1_p2_dual_endpoint_pairing"),
    ("p1_p2_dual_endpoint_pairing", "p1_pushforward"),
    ("p1_p2_dual_endpoint_pairing", "p2_pushforward"),
    ("p1_pushforward", "graph_composition"),
    ("p2_pushforward", "graph_composition"),
    ("graph_composition", "rosati"),
    ("graph_composition", "count_degree"),
    ("rosati", "control_death"),
    ("count_degree", "control_death"),
    ("control_death", "source_before_graph_nonpoints"),
    ("source_before_graph_nonpoints", "controls_not_points"),
    ("source_before_graph_nonpoints", "dh_not_points"),
    ("source_before_graph_nonpoints", "epstein_not_points"),
    ("cartesian_source_coherence", "C3_C5_equals_C15_source"),
    ("cartesian_source_coherence", "C5_C3_equals_C15_source"),
    ("monoidwide_source_coherence", "C3_C3_C5_equals_C45_source"),
    ("monoidwide_source_coherence", "F22_product_source"),
    ("source_coherence_coupling_primitive", "monoidwide_certificate_transport"),
    ("monoidwide_certificate_transport", "single_localization_on_dq"),
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
        "boundary_class": DD4_CLASS_ID,
        "res1": 1,
    }


def coupling_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "square": CATEGORICAL_SQUARE_ID,
        "cube": FACET_CUBE_ID,
        "totalization": CUBE_TOTALIZATION_ID,
        "coupling": SOURCE_COUPLING_ID,
        "source_coherence": SOURCE_COHERENCE_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "monoidwide_coherence": SOURCE_MONOIDWIDE_COHERENCE_ID,
        "source_token": SELF_DUAL_TOKEN_ID,
        "source_fiber": SELF_DUAL_FIBER_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "action_functor": MULTIPLIER_ACTION_FUNCTOR_ID,
        "exact_sequence": EXACT_SEQUENCE_ID,
        "exact_delta": EXACT_DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality": duality_payload(chi),
        "twist": TWIST_ID,
        "boundary_certificate": BOUNDARY_CERTIFICATE_ID,
        "localization": LOCALIZATION_SEQUENCE_ID,
        "normal_ratio": NORMAL_RATIO_ID,
        "dd4_boundary_localization": DD4_BOUNDARY_LOCALIZATION_ID,
        "endpoint_degree": ENDPOINT_DEGREE_MAPS_ID,
        "endpoint_pair": (p1, p2),
        "p1_pushforward": P1_PUSHFORWARD_ID,
        "p2_pushforward": P2_PUSHFORWARD_ID,
        "pushforward": PUSHFORWARD_SQUARE_ID,
        "graph_totalization": GRAPH_ROSATI_COUNT_TOTALIZATION_ID,
        "graph": PROPER_GRAPH_ID,
        "rosati": ROSATI_LAYER_ID,
        "count_degree": COUNT_DEGREE_ID,
        "control_death": CONTROL_DEATH_NATURALITY_ID,
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
    }


def graph_connected(edges: set[tuple[str, str]]) -> bool:
    nodes = {node for edge in edges for node in edge}
    if not nodes:
        return False
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
        "square_layer_monoidwide_coherence": SQUARE_LAYER_MONOIDWIDE_COHERENCE_ID,
        "self_dual_source_token": SELF_DUAL_TOKEN_ID,
        "self_dual_source_fiber": SELF_DUAL_FIBER_ID,
        "source_coherence": SOURCE_COHERENCE_ID,
        "source_coupling": SOURCE_COUPLING_ID,
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "monoidwide_coherence": SOURCE_MONOIDWIDE_COHERENCE_ID,
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
        "coupling_payload": coupling_payload(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "endpoint_defect": p1 - p2,
        "pushforward_defect": p1 - p2,
        "source_before_graph": True,
        "controls_points": False,
        "dh_points": False,
        "epstein_points": False,
    }


def coupled_row(item: dict[str, object]) -> bool:
    payload = item["coupling_payload"]
    duality = payload["duality"]
    return (
        item["source_coupling"] == SOURCE_COUPLING_ID
        and item["source_coherence"] == SOURCE_COHERENCE_ID
        and item["square"] == CATEGORICAL_SQUARE_ID
        and item["cube"] == FACET_CUBE_ID
        and item["totalization"] == CUBE_TOTALIZATION_ID
        and item["self_dual_source_token"] == SELF_DUAL_TOKEN_ID
        and item["self_dual_source_fiber"] == SELF_DUAL_FIBER_ID
        and item["universal_arrow"] == UNIVERSAL_ARROW_ID
        and item["signed_zero_fiber"] == SIGNED_ZERO_FIBER_ID
        and item["source_before_graph"]
        and not item["controls_points"]
        and not item["dh_points"]
        and not item["epstein_points"]
        and item["weighted_mass"] == 0
        and item["endpoint_defect"] == 0
        and item["pushforward_defect"] == 0
        and payload["coupling"] == SOURCE_COUPLING_ID
        and payload["square"] == CATEGORICAL_SQUARE_ID
        and payload["cube"] == FACET_CUBE_ID
        and payload["totalization"] == CUBE_TOTALIZATION_ID
        and payload["monoidwide_coherence"] == SOURCE_MONOIDWIDE_COHERENCE_ID
        and payload["exact_delta"] == EXACT_DELTA_ID
        and payload["kernel"] == KERNEL_ID
        and payload["coimage"] == COIMAGE_ID
        and payload["boundary_certificate"] == BOUNDARY_CERTIFICATE_ID
        and payload["control_death"] == CONTROL_DEATH_NATURALITY_ID
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
        "multiplier_action_functor_actual": False,
        "source_token_actual": False,
        "source_fiber_actual": False,
        "represented_source_fiber": False,
        "universal_arrow_actual": False,
        "self_dual_source_token_actual": False,
        "self_dual_source_fiber_actual": False,
        "signed_zero_fiber_actual": False,
        "source_coherence_coupling_actual": False,
        "coupling_generated_by_universal_arrow": False,
        "source_coherence_cells_actual": False,
        "exact_delta_coupled": False,
        "kernel_coimage_coupled": False,
        "rank_one_duality_coupled": False,
        "pinned_twist_coupled": False,
        "original_dd4_coupled": False,
        "normal_ratio_coupled": False,
        "endpoint_pushforward_coupled": False,
        "graph_rosati_count_coupled": False,
        "control_death_coupled": False,
        "source_before_graph_objects": False,
        "non_split_dependency_graph": False,
        "same_coupling_id_all_paths": False,
        "C3_C5_equals_C15_source": False,
        "C5_C3_equals_C15_source": False,
        "C3_C3_C5_equals_C45_source": False,
        "F22_product_source": False,
        "finite_anchors_generated": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "product_of_layer_coherences": False,
        "atomwise_preservation": False,
        "fiber_product_of_contracts": False,
        "pullback_square_only": False,
        "distributive_law_label": False,
        "bicategory_shadow": False,
        "formal_pasting_diagram": False,
        "sequential_layer_pipeline": False,
        "exactness_then_duality": False,
        "local_C3_patch": False,
        "finite_composition_table": False,
        "external_choice_of_coupling": False,
        "retuned_coupling": False,
        "graph_object_coherence": False,
        "graph_predicate_gate": False,
        "late_control_filter": False,
        "semantic_zeta_label": False,
        "declared_coupling": False,
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
    ("multiplier_action_functor_actual", "multiplier_action_functor_missing"),
    ("source_token_actual", "source_token_missing"),
    ("source_fiber_actual", "source_fiber_missing"),
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    ("self_dual_source_token_actual", "self_dual_source_token_missing"),
    ("self_dual_source_fiber_actual", "self_dual_source_fiber_missing"),
    ("signed_zero_fiber_actual", "signed_zero_fiber_missing"),
    ("source_coherence_coupling_actual", "source_coherence_coupling_missing"),
    (
        "coupling_generated_by_universal_arrow",
        "coupling_not_generated_by_universal_arrow",
    ),
    ("source_coherence_cells_actual", "source_coherence_cells_missing"),
    ("exact_delta_coupled", "exact_delta_not_coupled"),
    ("kernel_coimage_coupled", "kernel_coimage_not_coupled"),
    ("rank_one_duality_coupled", "rank_one_duality_not_coupled"),
    ("pinned_twist_coupled", "pinned_twist_not_coupled"),
    ("original_dd4_coupled", "original_dd4_not_coupled"),
    ("normal_ratio_coupled", "normal_ratio_not_coupled"),
    ("endpoint_pushforward_coupled", "endpoint_pushforward_not_coupled"),
    ("graph_rosati_count_coupled", "graph_rosati_count_not_coupled"),
    ("control_death_coupled", "control_death_not_coupled"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("non_split_dependency_graph", "dependency_graph_split"),
    ("same_coupling_id_all_paths", "same_coupling_id_not_all_paths"),
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
    ("product_of_layer_coherences", "product_of_layer_coherences"),
    ("atomwise_preservation", "atomwise_preservation"),
    ("fiber_product_of_contracts", "fiber_product_of_contracts"),
    ("pullback_square_only", "pullback_square_only"),
    ("distributive_law_label", "distributive_law_label"),
    ("bicategory_shadow", "bicategory_shadow"),
    ("formal_pasting_diagram", "formal_pasting_diagram"),
    ("sequential_layer_pipeline", "sequential_layer_pipeline"),
    ("exactness_then_duality", "exactness_then_duality"),
    ("local_C3_patch", "local_C3_patch"),
    ("finite_composition_table", "finite_composition_table"),
    ("external_choice_of_coupling", "external_choice_of_coupling"),
    ("retuned_coupling", "retuned_coupling"),
    ("graph_object_coherence", "graph_object_coherence"),
    ("graph_predicate_gate", "graph_predicate_gate"),
    ("late_control_filter", "late_control_filter"),
    ("semantic_zeta_label", "semantic_zeta_label"),
    ("declared_coupling", "declared_coupling"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_COUPLING_EDGES <= set(data["required_edges"]):
        out.append("required_source_coherence_coupling_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_coherence_coupling(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_COUPLING_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_square_actual=True,
        source_cube_totalization_actual=True,
        multiplier_action_functor_actual=True,
        source_token_actual=True,
        source_fiber_actual=True,
        represented_source_fiber=True,
        universal_arrow_actual=True,
        self_dual_source_token_actual=True,
        self_dual_source_fiber_actual=True,
        signed_zero_fiber_actual=True,
        source_coherence_coupling_actual=True,
        coupling_generated_by_universal_arrow=True,
        source_coherence_cells_actual=True,
        exact_delta_coupled=True,
        kernel_coimage_coupled=True,
        rank_one_duality_coupled=True,
        pinned_twist_coupled=True,
        original_dd4_coupled=True,
        normal_ratio_coupled=True,
        endpoint_pushforward_coupled=True,
        graph_rosati_count_coupled=True,
        control_death_coupled=True,
        source_before_graph_objects=True,
        non_split_dependency_graph=True,
        same_coupling_id_all_paths=True,
        C3_C5_equals_C15_source=True,
        C5_C3_equals_C15_source=True,
        C3_C3_C5_equals_C45_source=True,
        F22_product_source=True,
        finite_anchors_generated=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_COUPLING_EDGES),
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
    "CATSCCGQBARBECD1 one non-split source-coherence coupling carries all layers",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_COUPLING_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and coupling_payload(T3_T5_z) == coupling_payload(zC15)
    and coupling_payload(T5_T3_z) == coupling_payload(zC15)
    and coupling_payload(T3_T3_T5_z) == coupling_payload(zC45)
    and coupling_payload(T15_zF22) == coupling_payload(zC15F22)
    and coupling_payload(T45_zF22) == coupling_payload(zC45F22)
    and all(coupled_row(item) for item in rows)
    and {item["source_coupling"] for item in rows} == {SOURCE_COUPLING_ID},
    "H1=%s coupling=%s rows=%d"
    % ([p["h1_order"] for p in profiles], SOURCE_COUPLING_ID, len(rows)),
)


gate(
    "CATSCCGQBARBECD2 graph identities still do not supply source coupling",
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


product_layers = live_source(
    source_coherence_coupling_actual=False,
    exact_delta_coupled=False,
    rank_one_duality_coupled=False,
    graph_rosati_count_coupled=False,
    control_death_coupled=False,
    non_split_dependency_graph=False,
    product_of_layer_coherences=True,
    atomwise_preservation=True,
    control_point_formable=True,
)

gate(
    "CATSCCGQBARBECD3 product layer coherences are not one coupling primitive",
    not accepts_coherence_coupling(product_layers)
    and {
        "source_coherence_coupling_missing",
        "exact_delta_not_coupled",
        "rank_one_duality_not_coupled",
        "graph_rosati_count_not_coupled",
        "control_death_not_coupled",
        "dependency_graph_split",
        "product_of_layer_coherences",
        "atomwise_preservation",
        "control_point_formable",
    }
    <= set(reasons(product_layers)),
    ",".join(reasons(product_layers)),
)


formal_pasting = live_source(
    coupling_generated_by_universal_arrow=False,
    required_edges=set(),
    fiber_product_of_contracts=True,
    pullback_square_only=True,
    distributive_law_label=True,
    bicategory_shadow=True,
    formal_pasting_diagram=True,
)

gate(
    "CATSCCGQBARBECD4 pullbacks and formal pasting diagrams are labels",
    not accepts_coherence_coupling(formal_pasting)
    and {
        "coupling_not_generated_by_universal_arrow",
        "required_source_coherence_coupling_edges_missing",
        "fiber_product_of_contracts",
        "pullback_square_only",
        "distributive_law_label",
        "bicategory_shadow",
        "formal_pasting_diagram",
    }
    <= set(reasons(formal_pasting)),
    ",".join(reasons(formal_pasting)),
)


sequential_pipeline = live_source(
    exact_delta_coupled=False,
    kernel_coimage_coupled=False,
    rank_one_duality_coupled=False,
    control_death_coupled=False,
    source_before_graph_objects=False,
    sequential_layer_pipeline=True,
    exactness_then_duality=True,
    late_control_filter=True,
    control_point_formable=True,
)

gate(
    "CATSCCGQBARBECD5 sequential exactness-then-duality pipelines are too late",
    not accepts_coherence_coupling(sequential_pipeline)
    and {
        "exact_delta_not_coupled",
        "kernel_coimage_not_coupled",
        "rank_one_duality_not_coupled",
        "control_death_not_coupled",
        "source_not_before_graph_objects",
        "sequential_layer_pipeline",
        "exactness_then_duality",
        "late_control_filter",
        "control_point_formable",
    }
    <= set(reasons(sequential_pipeline)),
    ",".join(reasons(sequential_pipeline)),
)


local_table = live_source(
    same_coupling_id_all_paths=False,
    C5_C3_equals_C15_source=False,
    C3_C3_C5_equals_C45_source=False,
    F22_product_source=False,
    local_C3_patch=True,
    finite_composition_table=True,
)

gate(
    "CATSCCGQBARBECD6 local C3 tables do not couple independent paths",
    not accepts_coherence_coupling(local_table)
    and {
        "same_coupling_id_not_all_paths",
        "C5_C3_source_not_C15",
        "C3_C3_C5_source_not_C45",
        "F22_product_source_missing",
        "local_C3_patch",
        "finite_composition_table",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)


retuned = live_source(
    universal_arrow_actual=False,
    original_dd4_coupled=False,
    normal_ratio_coupled=False,
    endpoint_pushforward_coupled=False,
    external_choice_of_coupling=True,
    retuned_coupling=True,
    semantic_zeta_label=True,
)

gate(
    "CATSCCGQBARBECD7 external or retuned couplings lose the original source",
    not accepts_coherence_coupling(retuned)
    and {
        "universal_arrow_not_actual",
        "original_dd4_not_coupled",
        "normal_ratio_not_coupled",
        "endpoint_pushforward_not_coupled",
        "external_choice_of_coupling",
        "retuned_coupling",
        "semantic_zeta_label",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)


graph_shadow = live_source(
    carrier_native=False,
    graph_rosati_count_coupled=False,
    control_death_coupled=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_object_coherence=True,
    graph_predicate_gate=True,
    declared_coupling=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATSCCGQBARBECD8 declared graph-level couplings leave controls formable",
    not accepts_coherence_coupling(graph_shadow)
    and {
        "not_carrier_native",
        "graph_rosati_count_not_coupled",
        "control_death_not_coupled",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_object_coherence",
        "graph_predicate_gate",
        "declared_coupling",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_shadow)),
    ",".join(reasons(graph_shadow)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_COUPLING_EDGES
        - {("universal_arrow", "source_coherence_coupling_primitive")}
    ),
    live_source(source_coherence_coupling_actual=False),
    live_source(exact_delta_coupled=False),
    live_source(rank_one_duality_coupled=False),
    live_source(control_death_coupled=False),
    live_source(non_split_dependency_graph=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATSCCGQBARBECD9 every source-coupling edge is mandatory",
    not any(accepts_coherence_coupling(data) for data in missing_edges)
    and {
        "required_source_coherence_coupling_edges_missing",
        "source_coherence_coupling_missing",
        "exact_delta_not_coupled",
        "rank_one_duality_not_coupled",
        "control_death_not_coupled",
        "dependency_graph_split",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


live = live_source()
dead_sources = {
    "product_layers": product_layers,
    "formal_pasting": formal_pasting,
    "sequential_pipeline": sequential_pipeline,
    "local_table": local_table,
    "retuned": retuned,
    "graph_shadow": graph_shadow,
}

gate(
    "CATSCCGQBARBECD10 only non-split universal-arrow source coupling passes",
    accepts_coherence_coupling(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_coherence_coupling(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_coherence_coupling(data) for data in dead_sources.values()),
        accepts_coherence_coupling(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATSCCGQBARBECD1-CATSCCGQBARBECD10 ALL PASS: categorical closure "
    "self-dual exact-source coherence coupling totalization contract pinned"
)
print(
    "VERDICT: the categorical represented source square and totalized "
    "Beck-Chevalley cube must carry one non-split universal-arrow-generated "
    "source-coherence coupling primitive tying exact delta, kernel, coimage, "
    "rank-one duality, original DD.4, normal ratio, endpoint/pushforward, "
    "graph/Rosati/count, and control death before graph objects exist. "
    "Product coherences, pullback/pasting labels, sequential layer pipelines, "
    "local tables, retunings, and graph-level couplings do not construct the "
    "missing source object."
)
