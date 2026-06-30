r"""Globular-modification contract for represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport cells.

Doc 429 requires represented coherence cells for the cartesian transport of
the represented boundary fiber for the represented-coherence boundary-fiber
cartesian-transport boundary-fiber cartesian coherence transport globular
modification.
This witness pins the next edge: those cells must be faces of one
source-level globular modification with common source and target boundaries.
Independent represented coherence cells, boundary-mismatched pasting diagrams,
or post-hoc fillers do not assemble the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_scfgbccgbccgbccgbccgbccgbccgbfccgbfccgbfccgbfccgbfccgbfccgbfccgbfccgbfccgbfccg_gmod_contract
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
GLOBULAR_MODIFICATION_ID = (
    f"{mod_chain(41)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(41)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
BOUNDARY_RESTRICTION_ID = (
    f"res_{mod_chain(41)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(41)}_NCoup"
)
BOUNDARY_FIBER_ID = (
    f"Fib_{mod_chain(41)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
BOUNDARY_FIBER_ARROW_ID = (
    f"eta_Fib_{mod_chain(41)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CARTESIAN_BOUNDARY_FIBER_ID = (
    f"CartFib_{mod_chain(43)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CARTESIAN_BOUNDARY_RESTRICTION_ID = (
    f"cart_res_{mod_chain(41)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(41)}_NCoup"
)
CARTESIAN_BOUNDARY_FIBER_COHERENCE_ID = (
    f"Coh_CartFib_{mod_chain(43)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_MODIFICATION_ID = (
    f"{mod_chain(44)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(44)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"

CARTESIAN_FIBER_CELLS = (
    f"cell_C3_C5_C15_{coh_chain(41)}_NCoup_boundary_fiber",
    f"cell_C5_C3_C15_{coh_chain(41)}_NCoup_boundary_fiber",
    f"cell_C3_C3_C5_C45_{coh_chain(41)}_NCoup_boundary_fiber",
    f"cell_F22_interchange_{coh_chain(41)}_NCoup_boundary_fiber",
    f"cell_boundary_restriction_cartesian_naturality_{coh_chain(41)}_NCoup",
    f"cell_boundary_fiber_arrow_cartesian_naturality_{coh_chain(41)}_NCoup",
    f"cell_fixed_globular_boundary_pullback_{coh_chain(41)}_NCoup",
)

FIBER_COHERENCE_MODIFICATION_FACES = (
    f"face_C3_C5_C15_{coh_chain(41)}_boundary_fiber_coherence_globular_boundary",
    f"face_C5_C3_C15_{coh_chain(41)}_boundary_fiber_coherence_globular_boundary",
    f"face_C3_C3_C5_C45_{coh_chain(41)}_boundary_fiber_coherence_globular_boundary",
    f"face_F22_{coh_chain(41)}_boundary_fiber_coherence_globular_boundary",
    f"face_boundary_restriction_{coh_chain(41)}_naturality_globular_boundary",
    f"face_fiber_arrow_{coh_chain(41)}_naturality_globular_boundary",
    f"face_fixed_boundary_component_projection_pair_pasting_{coh_chain(41)}_globular_boundary",
)

REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES = {
    ("source_universal_arrow", "cartesian_source_coherence"),
    ("cartesian_source_coherence", "cartesian_boundary_fiber"),
    ("globular_modification", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "cartesian_boundary_fiber_coherence"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber_coherence"),
    ("fiber_universal_arrow", "cartesian_boundary_fiber_coherence"),
    ("cartesian_boundary_fiber_coherence", "fiber_coherence_globular_modification"),
    ("fiber_coherence_globular_modification", "shared_fiber_coherence_boundary"),
    ("shared_fiber_coherence_boundary", "source_boundary"),
    ("shared_fiber_coherence_boundary", "target_boundary"),
    ("source_boundary", "boundary_restriction_naturality_cell"),
    ("source_boundary", "fiber_arrow_naturality_cell"),
    ("target_boundary", "fixed_globular_boundary_cell"),
    ("target_boundary", "component_boundary_cell"),
    ("target_boundary", "projection_boundary_cell"),
    ("target_boundary", "pair_alpha_beta_boundary_cell"),
    ("target_boundary", "pasting_faces_cell"),
    ("fiber_coherence_globular_modification", "C3_C5_to_C15_pasting_face"),
    ("fiber_coherence_globular_modification", "C5_C3_to_C15_pasting_face"),
    ("fiber_coherence_globular_modification", "C3_C3_C5_to_C45_pasting_face"),
    ("fiber_coherence_globular_modification", "F22_interchange_pasting_face"),
    ("fiber_coherence_globular_modification", "boundary_restriction_pasting_face"),
    ("fiber_coherence_globular_modification", "fiber_arrow_pasting_face"),
    ("fiber_coherence_globular_modification", "fixed_boundary_pasting_face"),
    ("fiber_coherence_globular_modification", "component_projection_pasting_face"),
    ("fiber_coherence_globular_modification", "pair_alpha_beta_pasting_face"),
    ("fiber_coherence_globular_modification", "pasting_faces_pasting_face"),
    ("C3_C5_to_C15_pasting_face", "shared_fiber_coherence_boundary"),
    ("C5_C3_to_C15_pasting_face", "shared_fiber_coherence_boundary"),
    ("C3_C3_C5_to_C45_pasting_face", "shared_fiber_coherence_boundary"),
    ("F22_interchange_pasting_face", "shared_fiber_coherence_boundary"),
    ("boundary_restriction_pasting_face", "boundary_restriction_naturality_cell"),
    ("fiber_arrow_pasting_face", "fiber_arrow_naturality_cell"),
    ("fixed_boundary_pasting_face", "fixed_globular_boundary_cell"),
    ("component_projection_pasting_face", "component_boundary_cell"),
    ("component_projection_pasting_face", "projection_boundary_cell"),
    ("pair_alpha_beta_pasting_face", "pair_alpha_beta_boundary_cell"),
    ("pasting_faces_pasting_face", "pasting_faces_cell"),
    ("fiber_coherence_globular_modification", "whiskering_compatibility"),
    ("whiskering_compatibility", "cartesian_boundary_restriction"),
    ("whiskering_compatibility", "fiber_universal_arrow"),
    ("fiber_coherence_globular_modification", "vertical_horizontal_composition"),
    ("vertical_horizontal_composition", "associativity"),
    ("vertical_horizontal_composition", "interchange"),
    ("fiber_coherence_globular_modification", "coherence_preserves_coefficients"),
    ("fiber_coherence_globular_modification", "coherence_preserves_signed_support"),
    ("fiber_coherence_globular_modification", "same_modification_all_paths"),
    ("same_modification_all_paths", "C3_C5_equals_C15"),
    ("same_modification_all_paths", "C5_C3_equals_C15"),
    ("same_modification_all_paths", "C3_C3_C5_equals_C45"),
    ("same_modification_all_paths", "F22_product"),
    ("fiber_coherence_globular_modification", "source_before_points_and_graphs"),
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


def fiber_coherence_modification_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source": SOURCE_REPRESENTING_OBJECT_ID,
        "source_universal_arrow": SOURCE_UNIVERSAL_ARROW_ID,
        "cartesian_source_coherence": CARTESIAN_COHERENCE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "globular_boundary": GLOBULAR_BOUNDARY_ID,
        "boundary_restriction": BOUNDARY_RESTRICTION_ID,
        "boundary_fiber": BOUNDARY_FIBER_ID,
        "boundary_fiber_arrow": BOUNDARY_FIBER_ARROW_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "cartesian_boundary_restriction": CARTESIAN_BOUNDARY_RESTRICTION_ID,
        "cartesian_boundary_fiber_coherence": CARTESIAN_BOUNDARY_FIBER_COHERENCE_ID,
        "fiber_coherence_globular_modification": FIBER_COHERENCE_MODIFICATION_ID,
        "fiber_coherence_globular_boundary": FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
        "source_boundary": (
            "boundary_restriction_and_fiber_arrow_naturality",
            CARTESIAN_BOUNDARY_RESTRICTION_ID,
            BOUNDARY_FIBER_ARROW_ID,
        ),
        "target_boundary": (
            "fixed_boundary_component_projection_pair_and_pasting_naturality",
            GLOBULAR_BOUNDARY_ID,
            "component_boundary_cell",
            "projection_boundary_cell",
            "pair_alpha_beta_boundary_cell",
            "pasting_faces_cell",
        ),
        "cartesian_fiber_cells": CARTESIAN_FIBER_CELLS,
        "modification_faces": FIBER_COHERENCE_MODIFICATION_FACES,
        "control_death": CONTROL_DEATH_ID,
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "fiber_coherence_modification_payload": True,
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
        "cartesian_boundary_fiber_actual": False,
        "cartesian_boundary_restriction_actual": False,
        "fiber_universal_arrow_actual": False,
        "cartesian_boundary_fiber_coherence_actual": False,
        "coherence_generated_by_cartesian_fiber": False,
        "fiber_coherence_globular_modification_actual": False,
        "modification_generated_by_fiber_coherence": False,
        "shared_fiber_coherence_boundary_actual": False,
        "source_boundary_actual": False,
        "target_boundary_actual": False,
        "boundaries_are_globular": False,
        "boundary_restriction_boundary_matches": False,
        "fiber_arrow_boundary_matches": False,
        "fixed_boundary_in_same_modification": False,
        "component_projection_in_same_modification": False,
        "pair_alpha_beta_in_same_modification": False,
        "pasting_faces_actual": False,
        "whiskering_compatible": False,
        "vertical_horizontal_composition_compatible": False,
        "C3_C5_to_C15_cell_actual": False,
        "C5_C3_to_C15_cell_actual": False,
        "C3_C3_C5_to_C45_cell_actual": False,
        "F22_interchange_cell_actual": False,
        "boundary_restriction_naturality_cell_actual": False,
        "fiber_arrow_naturality_cell_actual": False,
        "fixed_globular_boundary_cell_actual": False,
        "component_boundary_cell_actual": False,
        "projection_boundary_cell_actual": False,
        "pair_alpha_beta_boundary_cell_actual": False,
        "pasting_faces_cell_actual": False,
        "associativity_actual": False,
        "interchange_actual": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "same_modification_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_anchors_generated": False,
        "modification_before_points": False,
        "modification_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "independent_fiber_coherence_cell_list": False,
        "boundary_mismatched_fiber_cells": False,
        "formal_pasting_diagram": False,
        "separate_boundary_restriction_modification": False,
        "separate_fiber_arrow_modification": False,
        "separate_fixed_boundary_modification": False,
        "homotopy_filler_after_points": False,
        "lax_modification_only": False,
        "graph_side_modification": False,
        "pointwise_modification": False,
        "post_product_modification": False,
        "retuned_modification": False,
        "reindexed_modification_label": False,
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
    ("cartesian_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    ("cartesian_boundary_restriction_actual", "cartesian_boundary_restriction_missing"),
    ("fiber_universal_arrow_actual", "fiber_universal_arrow_missing"),
    (
        "cartesian_boundary_fiber_coherence_actual",
        "cartesian_boundary_fiber_coherence_missing",
    ),
    (
        "coherence_generated_by_cartesian_fiber",
        "coherence_not_generated_by_cartesian_fiber",
    ),
    (
        "fiber_coherence_globular_modification_actual",
        "fiber_coherence_globular_modification_missing",
    ),
    (
        "modification_generated_by_fiber_coherence",
        "modification_not_generated_by_fiber_coherence",
    ),
    (
        "shared_fiber_coherence_boundary_actual",
        "shared_fiber_coherence_boundary_missing",
    ),
    ("source_boundary_actual", "source_boundary_missing"),
    ("target_boundary_actual", "target_boundary_missing"),
    ("boundaries_are_globular", "boundaries_not_globular"),
    (
        "boundary_restriction_boundary_matches",
        "boundary_restriction_boundary_mismatch",
    ),
    ("fiber_arrow_boundary_matches", "fiber_arrow_boundary_mismatch"),
    (
        "fixed_boundary_in_same_modification",
        "fixed_boundary_not_same_modification",
    ),
    (
        "component_projection_in_same_modification",
        "component_projection_not_same_modification",
    ),
    (
        "pair_alpha_beta_in_same_modification",
        "pair_alpha_beta_not_same_modification",
    ),
    ("pasting_faces_actual", "pasting_faces_missing"),
    ("whiskering_compatible", "whiskering_not_compatible"),
    (
        "vertical_horizontal_composition_compatible",
        "vertical_horizontal_composition_not_compatible",
    ),
    ("C3_C5_to_C15_cell_actual", "C3_C5_to_C15_cell_missing"),
    ("C5_C3_to_C15_cell_actual", "C5_C3_to_C15_cell_missing"),
    ("C3_C3_C5_to_C45_cell_actual", "C3_C3_C5_to_C45_cell_missing"),
    ("F22_interchange_cell_actual", "F22_interchange_cell_missing"),
    (
        "boundary_restriction_naturality_cell_actual",
        "boundary_restriction_naturality_cell_missing",
    ),
    ("fiber_arrow_naturality_cell_actual", "fiber_arrow_naturality_cell_missing"),
    ("fixed_globular_boundary_cell_actual", "fixed_globular_boundary_cell_missing"),
    ("component_boundary_cell_actual", "component_boundary_cell_missing"),
    ("projection_boundary_cell_actual", "projection_boundary_cell_missing"),
    ("pair_alpha_beta_boundary_cell_actual", "pair_alpha_beta_boundary_cell_missing"),
    ("pasting_faces_cell_actual", "pasting_faces_cell_missing"),
    ("associativity_actual", "associativity_missing"),
    ("interchange_actual", "interchange_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("same_modification_all_paths", "same_modification_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("modification_before_points", "modification_not_before_points"),
    ("modification_before_graph_objects", "modification_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("independent_fiber_coherence_cell_list", "independent_fiber_coherence_cell_list"),
    ("boundary_mismatched_fiber_cells", "boundary_mismatched_fiber_cells"),
    ("formal_pasting_diagram", "formal_pasting_diagram"),
    (
        "separate_boundary_restriction_modification",
        "separate_boundary_restriction_modification",
    ),
    ("separate_fiber_arrow_modification", "separate_fiber_arrow_modification"),
    ("separate_fixed_boundary_modification", "separate_fixed_boundary_modification"),
    ("homotopy_filler_after_points", "homotopy_filler_after_points"),
    ("lax_modification_only", "lax_modification_only"),
    ("graph_side_modification", "graph_side_modification"),
    ("pointwise_modification", "pointwise_modification"),
    ("post_product_modification", "post_product_modification"),
    ("retuned_modification", "retuned_modification"),
    ("reindexed_modification_label", "reindexed_modification_label"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES <= set(data["required_edges"]):
        out.append("required_fiber_coherence_modification_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_fiber_coherence_modification(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber_actual=True,
        source_universal_arrow_actual=True,
        cartesian_source_coherence_actual=True,
        globular_modification_actual=True,
        cartesian_boundary_fiber_actual=True,
        cartesian_boundary_restriction_actual=True,
        fiber_universal_arrow_actual=True,
        cartesian_boundary_fiber_coherence_actual=True,
        coherence_generated_by_cartesian_fiber=True,
        fiber_coherence_globular_modification_actual=True,
        modification_generated_by_fiber_coherence=True,
        shared_fiber_coherence_boundary_actual=True,
        source_boundary_actual=True,
        target_boundary_actual=True,
        boundaries_are_globular=True,
        boundary_restriction_boundary_matches=True,
        fiber_arrow_boundary_matches=True,
        fixed_boundary_in_same_modification=True,
        component_projection_in_same_modification=True,
        pair_alpha_beta_in_same_modification=True,
        pasting_faces_actual=True,
        whiskering_compatible=True,
        vertical_horizontal_composition_compatible=True,
        C3_C5_to_C15_cell_actual=True,
        C5_C3_to_C15_cell_actual=True,
        C3_C3_C5_to_C45_cell_actual=True,
        F22_interchange_cell_actual=True,
        boundary_restriction_naturality_cell_actual=True,
        fiber_arrow_naturality_cell_actual=True,
        fixed_globular_boundary_cell_actual=True,
        component_boundary_cell_actual=True,
        projection_boundary_cell_actual=True,
        pair_alpha_beta_boundary_cell_actual=True,
        pasting_faces_cell_actual=True,
        associativity_actual=True,
        interchange_actual=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        same_modification_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_anchors_generated=True,
        modification_before_points=True,
        modification_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES),
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
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG1 represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport cells assemble into one globular modification",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES)
    and max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and fiber_coherence_modification_payload(T3_T5_z)
    == fiber_coherence_modification_payload(zC15)
    and fiber_coherence_modification_payload(T5_T3_z)
    == fiber_coherence_modification_payload(zC15)
    and fiber_coherence_modification_payload(T3_T3_T5_z)
    == fiber_coherence_modification_payload(zC45)
    and fiber_coherence_modification_payload(T15_zF22)
    == fiber_coherence_modification_payload(zC15F22)
    and fiber_coherence_modification_payload(T45_zF22)
    == fiber_coherence_modification_payload(zC45F22),
    "H1=%s modification=%s faces=%d"
    % (
        [p["h1_order"] for p in profiles],
        FIBER_COHERENCE_MODIFICATION_ID,
        len(FIBER_COHERENCE_MODIFICATION_FACES),
    ),
)


gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG2 graph identities still do not supply a represented cartesian boundary-fiber coherence modification",
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


independent = live_source(
    fiber_coherence_globular_modification_actual=False,
    modification_generated_by_fiber_coherence=False,
    shared_fiber_coherence_boundary_actual=False,
    independent_fiber_coherence_cell_list=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG3 independent represented cartesian boundary-fiber coherence cells are not one modification",
    not accepts_fiber_coherence_modification(independent)
    and {
        "fiber_coherence_globular_modification_missing",
        "modification_not_generated_by_fiber_coherence",
        "shared_fiber_coherence_boundary_missing",
        "independent_fiber_coherence_cell_list",
    }
    <= set(reasons(independent)),
    ",".join(reasons(independent)),
)


boundary_mismatch = live_source(
    source_boundary_actual=False,
    target_boundary_actual=False,
    boundaries_are_globular=False,
    boundary_restriction_boundary_matches=False,
    fiber_arrow_boundary_matches=False,
    boundary_mismatched_fiber_cells=True,
    formal_pasting_diagram=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG4 boundary-mismatched fiber pasting diagrams do not globularize",
    not accepts_fiber_coherence_modification(boundary_mismatch)
    and {
        "source_boundary_missing",
        "target_boundary_missing",
        "boundaries_not_globular",
        "boundary_restriction_boundary_mismatch",
        "fiber_arrow_boundary_mismatch",
        "boundary_mismatched_fiber_cells",
        "formal_pasting_diagram",
    }
    <= set(reasons(boundary_mismatch)),
    ",".join(reasons(boundary_mismatch)),
)


split_modifications = live_source(
    fixed_boundary_in_same_modification=False,
    component_projection_in_same_modification=False,
    pair_alpha_beta_in_same_modification=False,
    pasting_faces_actual=False,
    separate_boundary_restriction_modification=True,
    separate_fiber_arrow_modification=True,
    separate_fixed_boundary_modification=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG5 split boundary-fiber modifications do not bind the fiber",
    not accepts_fiber_coherence_modification(split_modifications)
    and {
        "fixed_boundary_not_same_modification",
        "component_projection_not_same_modification",
        "pair_alpha_beta_not_same_modification",
        "pasting_faces_missing",
        "separate_boundary_restriction_modification",
        "separate_fiber_arrow_modification",
        "separate_fixed_boundary_modification",
    }
    <= set(reasons(split_modifications)),
    ",".join(reasons(split_modifications)),
)


late_fillers = live_source(
    modification_before_points=False,
    modification_before_graph_objects=False,
    homotopy_filler_after_points=True,
    lax_modification_only=True,
    graph_side_modification=True,
    pointwise_modification=True,
    post_product_modification=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG6 homotopy or pointwise cartesian boundary-fiber coherence fillers are too late",
    not accepts_fiber_coherence_modification(late_fillers)
    and {
        "modification_not_before_points",
        "modification_not_before_graph_objects",
        "homotopy_filler_after_points",
        "lax_modification_only",
        "graph_side_modification",
        "pointwise_modification",
        "post_product_modification",
    }
    <= set(reasons(late_fillers)),
    ",".join(reasons(late_fillers)),
)


retuned = live_source(
    whiskering_compatible=False,
    vertical_horizontal_composition_compatible=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    same_modification_all_paths=False,
    retuned_modification=True,
    reindexed_modification_label=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG7 retuned or reindexed cartesian boundary-fiber coherence modifications replace the boundary",
    not accepts_fiber_coherence_modification(retuned)
    and {
        "whiskering_not_compatible",
        "vertical_horizontal_composition_not_compatible",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "same_modification_not_all_paths",
        "retuned_modification",
        "reindexed_modification_label",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)


missing_edges = [
    live_source(
        required_edges=REQUIRED_FIBER_COHERENCE_MODIFICATION_EDGES
        - {("fiber_coherence_globular_modification", "shared_fiber_coherence_boundary")}
    ),
    live_source(fiber_coherence_globular_modification_actual=False),
    live_source(shared_fiber_coherence_boundary_actual=False),
    live_source(source_boundary_actual=False),
    live_source(target_boundary_actual=False),
    live_source(boundaries_are_globular=False),
    live_source(boundary_restriction_boundary_matches=False),
    live_source(fiber_arrow_boundary_matches=False),
    live_source(fixed_boundary_in_same_modification=False),
    live_source(component_projection_in_same_modification=False),
    live_source(pair_alpha_beta_in_same_modification=False),
    live_source(pasting_faces_actual=False),
    live_source(whiskering_compatible=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG8 every represented cartesian boundary-fiber coherence modification edge is mandatory",
    not any(accepts_fiber_coherence_modification(data) for data in missing_edges)
    and {
        "required_fiber_coherence_modification_edges_missing",
        "fiber_coherence_globular_modification_missing",
        "shared_fiber_coherence_boundary_missing",
        "source_boundary_missing",
        "target_boundary_missing",
        "boundaries_not_globular",
        "boundary_restriction_boundary_mismatch",
        "fiber_arrow_boundary_mismatch",
        "fixed_boundary_not_same_modification",
        "component_projection_not_same_modification",
        "pair_alpha_beta_not_same_modification",
        "pasting_faces_missing",
        "whiskering_not_compatible",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


control_modification = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_modification=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG9 graph-side cartesian boundary-fiber coherence modifications leave controls formable",
    not accepts_fiber_coherence_modification(control_modification)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_modification",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_modification)),
    ",".join(reasons(control_modification)),
)


live = live_source()
dead_sources = {
    "independent": independent,
    "boundary_mismatch": boundary_mismatch,
    "split_modifications": split_modifications,
    "late_fillers": late_fillers,
    "retuned": retuned,
    "control_modification": control_modification,
}

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG10 only one source globular represented cartesian boundary-fiber coherence modification passes",
    accepts_fiber_coherence_modification(live)
    and graph_connected(live["required_edges"])
    and not any(
        accepts_fiber_coherence_modification(data) for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_fiber_coherence_modification(data) for data in dead_sources.values()),
        accepts_fiber_coherence_modification(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nSCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG1-SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCGBFCCG10 ALL PASS: represented-coherence "
    "boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport cells globular modification pinned"
)
print(
    "VERDICT: represented-coherence boundary-fiber cartesian-transport "
    "boundary-fiber cartesian coherence transport cells for the cartesian "
    "boundary fiber must assemble as one source-level globular modification "
    "with shared source and target boundaries. "
    "Independent represented coherence cell lists, boundary-mismatched pasting "
    "diagrams, split restriction/arrow/fixed boundary modifications, homotopy "
    "fillers, lax or graph-side modifications, retuned labels, and "
    "post-product modifications do not construct the missing source object."
)
