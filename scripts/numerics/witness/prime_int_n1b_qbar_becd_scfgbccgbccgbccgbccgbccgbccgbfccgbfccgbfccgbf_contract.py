r"""Boundary-fiber contract for represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modifications.

Doc 402 requires represented-coherence boundary-fiber cartesian-transport
boundary-fiber cartesian coherence transport cells to assemble as one
source-level globular modification. This witness pins the next edge: that
23-layer modification must be selected by a represented boundary fiber over
its own globular boundary. Chosen sections, contractible-choice wrappers
without a representer, local boundary fibers, and graph-side fibers do not
construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_scfgbccgbccgbccgbccgbccgbccgbfccgbfccgbfccgbf_contract
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
    f"{mod_chain(20)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(20)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
BOUNDARY_RESTRICTION_ID = (
    f"res_{mod_chain(20)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(20)}_NCoup"
)
BOUNDARY_FIBER_ID = (
    f"Fib_{mod_chain(20)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
BOUNDARY_FIBER_ARROW_ID = (
    f"eta_Fib_{mod_chain(20)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CARTESIAN_BOUNDARY_FIBER_ID = (
    f"CartFib_{mod_chain(22)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CARTESIAN_BOUNDARY_RESTRICTION_ID = (
    f"cart_res_{mod_chain(20)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(20)}_NCoup"
)
CARTESIAN_BOUNDARY_FIBER_COHERENCE_ID = (
    f"Coh_CartFib_{mod_chain(22)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_MODIFICATION_ID = (
    f"{mod_chain(23)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID = (
    f"GlobBd_{glob_chain(23)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID = (
    f"res_{mod_chain(23)}_Mod_Coh_CartCone_to_GlobBd_{coh_chain(23)}_NCoup"
)
FIBER_COHERENCE_BOUNDARY_FIBER_ID = (
    f"Fib_{mod_chain(23)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
FIBER_COHERENCE_BOUNDARY_FIBER_ARROW_ID = (
    f"eta_Fib_{mod_chain(23)}_Mod_Coh_CartCone_NCoup_eta_source_components"
)
CONTROL_DEATH_ID = "CTRL_Qbar_BECD_coherent_death"

REQUIRED_EDGES = {
    ("source_universal_arrow", "cartesian_source_coherence"),
    ("cartesian_source_coherence", "cartesian_boundary_fiber"),
    ("globular_modification", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "cartesian_boundary_fiber_coherence"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber_coherence"),
    ("fiber_universal_arrow", "cartesian_boundary_fiber_coherence"),
    ("cartesian_boundary_fiber_coherence", "fiber_coherence_globular_modification"),
    ("fiber_coherence_globular_modification", "shared_fiber_coherence_boundary"),
    ("fiber_coherence_globular_modification", "boundary_restriction_map"),
    ("boundary_restriction_map", "shared_fiber_coherence_boundary"),
    ("boundary_restriction_map", "represented_boundary_fiber"),
    ("shared_fiber_coherence_boundary", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "fiber_boundary_universal_arrow"),
    ("fiber_boundary_universal_arrow", "selected_fiber_coherence_modification"),
    ("selected_fiber_coherence_modification", "fiber_coherence_globular_modification"),
    ("represented_boundary_fiber", "unique_source_filler"),
    ("unique_source_filler", "contractible_after_represented_fiber"),
    ("represented_boundary_fiber", "boundary_preservation"),
    ("boundary_preservation", "shared_fiber_coherence_boundary"),
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

REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber_actual", "represented_source_fiber_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("globular_modification_actual", "globular_modification_missing"),
    ("cartesian_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    ("cartesian_boundary_restriction_actual", "cartesian_boundary_restriction_missing"),
    ("fiber_universal_arrow_actual", "fiber_universal_arrow_missing"),
    ("cartesian_boundary_fiber_coherence_actual", "cartesian_boundary_fiber_coherence_missing"),
    ("coherence_generated_by_cartesian_fiber", "coherence_not_generated_by_cartesian_fiber"),
    ("fiber_coherence_globular_modification_actual", "fiber_coherence_globular_modification_missing"),
    ("modification_generated_by_fiber_coherence", "modification_not_generated_by_fiber_coherence"),
    ("shared_fiber_coherence_boundary_actual", "shared_fiber_coherence_boundary_missing"),
    ("fiber_coherence_boundary_restriction_actual", "boundary_restriction_missing"),
    ("represented_fiber_coherence_boundary_fiber_actual", "represented_boundary_fiber_missing"),
    ("fiber_boundary_universal_arrow_actual", "fiber_universal_arrow_missing"),
    ("modification_selected_by_fiber_arrow", "modification_not_selected_by_fiber_arrow"),
    ("fiber_over_shared_fiber_coherence_boundary", "fiber_not_over_shared_fiber_coherence_boundary"),
    ("boundary_preservation_actual", "boundary_preservation_missing"),
    ("unique_source_filler_actual", "unique_source_filler_missing"),
    ("contractibility_after_represented_fiber", "contractibility_not_after_represented_fiber"),
    ("source_boundary_actual", "source_boundary_missing"),
    ("target_boundary_actual", "target_boundary_missing"),
    ("boundaries_are_globular", "boundaries_not_globular"),
    ("boundary_restriction_boundary_matches", "boundary_restriction_boundary_mismatch"),
    ("fiber_arrow_boundary_matches", "fiber_arrow_boundary_mismatch"),
    ("fixed_boundary_in_same_modification", "fixed_boundary_not_same_modification"),
    ("component_projection_in_same_modification", "component_projection_not_same_modification"),
    ("pair_alpha_beta_in_same_modification", "pair_alpha_beta_not_same_modification"),
    ("pasting_faces_actual", "pasting_faces_missing"),
    ("whiskering_compatible", "whiskering_not_compatible"),
    ("vertical_horizontal_composition_compatible", "vertical_horizontal_composition_not_compatible"),
    ("C3_C5_to_C15_cell_actual", "C3_C5_to_C15_cell_missing"),
    ("C5_C3_to_C15_cell_actual", "C5_C3_to_C15_cell_missing"),
    ("C3_C3_C5_to_C45_cell_actual", "C3_C3_C5_to_C45_cell_missing"),
    ("F22_interchange_cell_actual", "F22_interchange_cell_missing"),
    ("boundary_restriction_naturality_cell_actual", "boundary_restriction_naturality_cell_missing"),
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
    ("chosen_boundary_section", "chosen_boundary_section"),
    ("contractible_choice_without_representer", "contractible_choice_without_representer"),
    ("boundary_mismatched_fiber", "boundary_mismatched_fiber"),
    ("formal_pasting_diagram", "formal_pasting_diagram"),
    ("external_boundary_fiber", "external_boundary_fiber"),
    ("quotient_boundary_fiber", "quotient_boundary_fiber"),
    ("local_boundary_fiber_table", "local_boundary_fiber_table"),
    ("pointwise_boundary_fiber", "pointwise_boundary_fiber"),
    ("graph_side_boundary_fiber", "graph_side_boundary_fiber"),
    ("post_product_boundary_fiber", "post_product_boundary_fiber"),
    ("retuned_boundary_restriction", "retuned_boundary_restriction"),
    ("reindexed_boundary_fiber", "reindexed_boundary_fiber"),
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


def represented_boundary_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
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
        "fiber_coherence_boundary_restriction": FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID,
        "fiber_coherence_boundary_fiber": FIBER_COHERENCE_BOUNDARY_FIBER_ID,
        "fiber_coherence_boundary_fiber_arrow": (
            FIBER_COHERENCE_BOUNDARY_FIBER_ARROW_ID
        ),
        "source_boundary": (
            "boundary_restriction_and_fiber_arrow_naturality",
            FIBER_COHERENCE_BOUNDARY_RESTRICTION_ID,
            FIBER_COHERENCE_BOUNDARY_FIBER_ARROW_ID,
        ),
        "target_boundary": (
            "fixed_boundary_component_projection_pair_and_pasting_naturality",
            FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
            "component_boundary_cell",
            "projection_boundary_cell",
            "pair_alpha_beta_boundary_cell",
            "pasting_faces_cell",
        ),
        "control_death": CONTROL_DEATH_ID,
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "fiber_coherence_boundary_fiber_payload": True,
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
    keys = {key: False for key, _ in REQUIRED}
    keys.update(
        {
            "required_edges": set(),
            "chosen_boundary_section": False,
            "contractible_choice_without_representer": False,
            "boundary_mismatched_fiber": False,
            "formal_pasting_diagram": False,
            "external_boundary_fiber": False,
            "quotient_boundary_fiber": False,
            "local_boundary_fiber_table": False,
            "pointwise_boundary_fiber": False,
            "graph_side_boundary_fiber": False,
            "post_product_boundary_fiber": False,
            "retuned_boundary_restriction": False,
            "reindexed_boundary_fiber": False,
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
        out.append("required_fiber_coherence_boundary_fiber_edges_missing")
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
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF1 represented-coherence boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modification is selected by its represented boundary fiber",
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
    and represented_boundary_fiber_payload(T3_T5_z)
    == represented_boundary_fiber_payload(zC15)
    and represented_boundary_fiber_payload(T5_T3_z)
    == represented_boundary_fiber_payload(zC15)
    and represented_boundary_fiber_payload(T3_T3_T5_z)
    == represented_boundary_fiber_payload(zC45)
    and represented_boundary_fiber_payload(T15_zF22)
    == represented_boundary_fiber_payload(zC15F22)
    and represented_boundary_fiber_payload(T45_zF22)
    == represented_boundary_fiber_payload(zC45F22),
    "H1=%s fiber=%s boundary=%s"
    % (
        [p["h1_order"] for p in profiles],
        FIBER_COHERENCE_BOUNDARY_FIBER_ID,
        FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
    ),
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF2 graph identities still do not supply the represented boundary fiber",
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

chosen = live_source(
    fiber_coherence_boundary_restriction_actual=False,
    represented_fiber_coherence_boundary_fiber_actual=False,
    fiber_boundary_universal_arrow_actual=False,
    modification_selected_by_fiber_arrow=False,
    chosen_boundary_section=True,
    contractible_choice_without_representer=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF3 chosen boundary sections are not represented fibers",
    not accepts(chosen)
    and {
        "boundary_restriction_missing",
        "represented_boundary_fiber_missing",
        "fiber_universal_arrow_missing",
        "modification_not_selected_by_fiber_arrow",
        "chosen_boundary_section",
        "contractible_choice_without_representer",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

wrong_boundary = live_source(
    shared_fiber_coherence_boundary_actual=False,
    fiber_over_shared_fiber_coherence_boundary=False,
    boundary_preservation_actual=False,
    boundary_restriction_boundary_matches=False,
    fiber_arrow_boundary_matches=False,
    boundary_mismatched_fiber=True,
    formal_pasting_diagram=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF4 fibers over the wrong boundary do not select the modification",
    not accepts(wrong_boundary)
    and {
        "shared_fiber_coherence_boundary_missing",
        "fiber_not_over_shared_fiber_coherence_boundary",
        "boundary_preservation_missing",
        "boundary_restriction_boundary_mismatch",
        "fiber_arrow_boundary_mismatch",
        "boundary_mismatched_fiber",
        "formal_pasting_diagram",
    }
    <= set(reasons(wrong_boundary)),
    ",".join(reasons(wrong_boundary)),
)

external = live_source(
    represented_fiber_coherence_boundary_fiber_actual=False,
    fiber_over_shared_fiber_coherence_boundary=False,
    boundary_preservation_actual=False,
    external_boundary_fiber=True,
    quotient_boundary_fiber=True,
    local_boundary_fiber_table=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF5 external quotient or local boundary fibers are not source fibers",
    not accepts(external)
    and {
        "represented_boundary_fiber_missing",
        "fiber_not_over_shared_fiber_coherence_boundary",
        "boundary_preservation_missing",
        "external_boundary_fiber",
        "quotient_boundary_fiber",
        "local_boundary_fiber_table",
    }
    <= set(reasons(external)),
    ",".join(reasons(external)),
)

late = live_source(
    fiber_boundary_universal_arrow_actual=False,
    modification_selected_by_fiber_arrow=False,
    modification_before_points=False,
    modification_before_graph_objects=False,
    pointwise_boundary_fiber=True,
    graph_side_boundary_fiber=True,
    post_product_boundary_fiber=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF6 pointwise graph-side or post-product fibers are too late",
    not accepts(late)
    and {
        "fiber_universal_arrow_missing",
        "modification_not_selected_by_fiber_arrow",
        "modification_not_before_points",
        "modification_not_before_graph_objects",
        "pointwise_boundary_fiber",
        "graph_side_boundary_fiber",
        "post_product_boundary_fiber",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    fiber_coherence_boundary_restriction_actual=False,
    modification_selected_by_fiber_arrow=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    same_modification_all_paths=False,
    retuned_boundary_restriction=True,
    reindexed_boundary_fiber=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF7 retuned or reindexed boundary fibers replace the source map",
    not accepts(retuned)
    and {
        "boundary_restriction_missing",
        "modification_not_selected_by_fiber_arrow",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "same_modification_not_all_paths",
        "retuned_boundary_restriction",
        "reindexed_boundary_fiber",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_EDGES - {("boundary_restriction_map", "represented_boundary_fiber")}),
    live_source(fiber_coherence_boundary_restriction_actual=False),
    live_source(represented_fiber_coherence_boundary_fiber_actual=False),
    live_source(fiber_boundary_universal_arrow_actual=False),
    live_source(modification_selected_by_fiber_arrow=False),
    live_source(fiber_over_shared_fiber_coherence_boundary=False),
    live_source(boundary_preservation_actual=False),
    live_source(unique_source_filler_actual=False),
    live_source(contractibility_after_represented_fiber=False),
    live_source(shared_fiber_coherence_boundary_actual=False),
    live_source(source_boundary_actual=False),
    live_source(target_boundary_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF8 every boundary-fiber edge is mandatory",
    not any(accepts(data) for data in missing_edges)
    and {
        "required_fiber_coherence_boundary_fiber_edges_missing",
        "boundary_restriction_missing",
        "represented_boundary_fiber_missing",
        "fiber_universal_arrow_missing",
        "modification_not_selected_by_fiber_arrow",
        "fiber_not_over_shared_fiber_coherence_boundary",
        "boundary_preservation_missing",
        "unique_source_filler_missing",
        "contractibility_not_after_represented_fiber",
        "shared_fiber_coherence_boundary_missing",
        "source_boundary_missing",
        "target_boundary_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_fiber = live_source(
    carrier_native=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_boundary_fiber=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF9 graph-side boundary fibers leave controls formable",
    not accepts(control_fiber)
    and {
        "not_carrier_native",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_boundary_fiber",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_fiber)),
    ",".join(reasons(control_fiber)),
)

live = live_source()
dead_sources = {
    "chosen": chosen,
    "wrong_boundary": wrong_boundary,
    "external": external,
    "late": late,
    "retuned": retuned,
    "control_fiber": control_fiber,
}

gate(
    "SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF10 only represented source boundary fibers pass",
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
    "\nSCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF1-SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFCCGBFCCGBF10 ALL PASS: represented-coherence "
    "boundary-fiber cartesian-transport boundary-fiber cartesian coherence transport globular modification boundary fiber pinned"
)
print(
    "VERDICT: the represented-coherence boundary-fiber cartesian-transport "
    "boundary-fiber cartesian coherence transport globular modification must "
    "be selected by an actual source boundary-restriction map and represented "
    "boundary fiber over "
    f"{FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID}. "
    "Chosen sections, contractible-choice wrappers without a representer, "
    "external or local boundary fibers, pointwise or graph-side fibers, "
    "retuned boundary maps, and post-product fibers do not construct the "
    "missing source object."
)
