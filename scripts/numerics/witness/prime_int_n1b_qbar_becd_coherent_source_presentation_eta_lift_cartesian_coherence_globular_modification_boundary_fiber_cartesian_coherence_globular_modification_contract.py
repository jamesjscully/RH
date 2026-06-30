r"""Globular-modification contract for cartesian boundary-fiber coherence.

Doc 490 requires represented coherence cells for the cartesian boundary-fiber
transport.  This witness pins the next edge: those cells must be faces of one
source-level globular modification with a shared source and target boundary.
Independent cell lists, boundary-mismatched pasting diagrams, split
modifications, or graph-side fillers do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
CARTESIAN_SOURCE_LIFT_ID = (
    "CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber"
)
BOUNDARY_FIBER_ID = (
    "Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
CARTESIAN_BOUNDARY_FIBER_ID = (
    "CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
CARTESIAN_BOUNDARY_RESTRICTION_ID = (
    "cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd"
)
CARTESIAN_BOUNDARY_FIBER_COHERENCE_ID = (
    "Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
FIBER_COHERENCE_GLOBULAR_MODIFICATION_ID = (
    "Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID = (
    "GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)

REQUIRED_FACETS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

REQUIRED_COHERENCE_CELLS = (
    "source_square_cell",
    "beck_chevalley_cube_cell",
    "cartesian_lift_cell",
    "component_cone_cell",
    "component_projection_pair_cell",
    "globular_modification_cell",
    "boundary_fiber_cell",
    "cartesian_boundary_fiber_cell",
    "boundary_fiber_coherence_cell",
    "fiber_coherence_modification_cell",
    "source_boundary_cell",
    "target_boundary_cell",
    "multiplier_path_cell",
    "coefficient_preservation_cell",
    "signed_support_preservation_cell",
    "source_before_points_cell",
    "closed_finite_coherence_cell",
)

COMPONENT_NAMES = (*REQUIRED_FACETS, *REQUIRED_COHERENCE_CELLS)

REQUIRED_COMPONENTS = tuple(
    f"Comp_CohSrcPres_BCCube_Qbar_BECD_{name}_source" for name in COMPONENT_NAMES
)
REQUIRED_CARTESIAN_LEGS = tuple(
    f"cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_{name}"
    for name in COMPONENT_NAMES
)

REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS = (
    "cell_C3_C5_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_C5_C3_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_C3_C3_C5_C45_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_F22_interchange_lift_eta_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber",
    "cell_boundary_restriction_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_boundary_fiber_arrow_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_fixed_globular_boundary_pullback_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_source_boundary_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_target_boundary_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
    "cell_pasting_faces_cartesian_naturality_lift_eta_CohSrcPres_BCCube_Qbar_BECD",
)

REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES = tuple(
    f"face_{cell}_fiber_coherence_globular_boundary"
    for cell in REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS
)

REQUIRED_NATURALITY_PATHS = {
    "C3*C5=C15",
    "C5*C3=C15",
    "C3*C3*C5=C45",
    "F22_product",
}

REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES = {
    ("eta_equalizer_lift", "cartesian_source_lift"),
    ("cartesian_source_lift", "cartesian_boundary_fiber"),
    ("represented_boundary_fiber", "cartesian_boundary_fiber"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "cartesian_boundary_fiber_coherence"),
    ("cartesian_boundary_fiber_coherence", "fiber_coherence_globular_modification"),
    ("fiber_coherence_globular_modification", "shared_fiber_coherence_boundary"),
    ("shared_fiber_coherence_boundary", "source_boundary"),
    ("shared_fiber_coherence_boundary", "target_boundary"),
    ("source_boundary", "boundary_restriction_naturality_cell"),
    ("source_boundary", "boundary_fiber_arrow_naturality_cell"),
    ("target_boundary", "fixed_globular_boundary_cell"),
    ("target_boundary", "source_boundary_cell"),
    ("target_boundary", "target_boundary_cell"),
    ("target_boundary", "pasting_faces_cell"),
    ("fiber_coherence_globular_modification", "all_fiber_coherence_faces"),
    ("all_fiber_coherence_faces", "shared_fiber_coherence_boundary"),
    ("all_fiber_coherence_faces", "multiplier_path_faces"),
    ("all_fiber_coherence_faces", "structure_faces"),
    ("fiber_coherence_globular_modification", "C3*C5=C15_face"),
    ("fiber_coherence_globular_modification", "C5*C3=C15_face"),
    ("fiber_coherence_globular_modification", "C3*C3*C5=C45_face"),
    ("fiber_coherence_globular_modification", "F22_face"),
    ("fiber_coherence_globular_modification", "whiskering_compatibility"),
    ("whiskering_compatibility", "cartesian_boundary_restriction"),
    ("whiskering_compatibility", "cartesian_boundary_fiber"),
    ("fiber_coherence_globular_modification", "vertical_horizontal_composition"),
    ("vertical_horizontal_composition", "associativity"),
    ("vertical_horizontal_composition", "interchange"),
    ("fiber_coherence_globular_modification", "coefficient_preservation"),
    ("fiber_coherence_globular_modification", "signed_support_preservation"),
    ("fiber_coherence_globular_modification", "same_modification_all_paths"),
    ("same_modification_all_paths", "C3*C5=C15"),
    ("same_modification_all_paths", "C5*C3=C15"),
    ("same_modification_all_paths", "C3*C3*C5=C45"),
    ("same_modification_all_paths", "F22_product"),
    ("fiber_coherence_globular_modification", "source_before_points"),
    ("source_before_points", "controls_not_points"),
    ("source_before_points", "dh_not_points"),
    ("source_before_points", "epstein_not_points"),
}


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


def source(**kwargs):
    data = {
        "carrier_native": False,
        "doc490_coherence_actual": False,
        "globular_modification_actual": False,
        "shared_globular_boundary_actual": False,
        "source_boundary_actual": False,
        "target_boundary_actual": False,
        "source_boundary_matches_naturality": False,
        "target_boundary_matches_structure": False,
        "all_faces_actual": False,
        "whiskering_compatibility_actual": False,
        "vertical_horizontal_composition_actual": False,
        "associativity_actual": False,
        "interchange_actual": False,
        "same_modification_all_paths": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "component_names": set(),
        "cartesian_leg_names": set(),
        "boundary_fiber_coherence_cells": set(),
        "fiber_coherence_faces": set(),
        "globular_edges": set(),
        "naturality_paths": set(),
        "independent_cell_list": False,
        "boundary_mismatched_pasting": False,
        "separate_boundary_restriction_modification": False,
        "separate_fiber_arrow_modification": False,
        "separate_fixed_boundary_modification": False,
        "homotopy_filler_after_points": False,
        "lax_modification": False,
        "pointwise_modification": False,
        "graph_side_modification": False,
        "post_product_modification": False,
        "retuned_modification": False,
        "reindexed_modification_labels": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc490_coherence_actual", "doc490_coherence_missing"),
    ("globular_modification_actual", "globular_modification_missing"),
    ("shared_globular_boundary_actual", "shared_globular_boundary_missing"),
    ("source_boundary_actual", "source_boundary_missing"),
    ("target_boundary_actual", "target_boundary_missing"),
    ("source_boundary_matches_naturality", "source_boundary_mismatch"),
    ("target_boundary_matches_structure", "target_boundary_mismatch"),
    ("all_faces_actual", "all_faces_missing"),
    ("whiskering_compatibility_actual", "whiskering_compatibility_missing"),
    ("vertical_horizontal_composition_actual", "vertical_horizontal_composition_missing"),
    ("associativity_actual", "associativity_missing"),
    ("interchange_actual", "interchange_missing"),
    ("same_modification_all_paths", "same_modification_not_all_paths"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("independent_cell_list", "independent_cell_list"),
    ("boundary_mismatched_pasting", "boundary_mismatched_pasting"),
    ("separate_boundary_restriction_modification", "separate_boundary_restriction_modification"),
    ("separate_fiber_arrow_modification", "separate_fiber_arrow_modification"),
    ("separate_fixed_boundary_modification", "separate_fixed_boundary_modification"),
    ("homotopy_filler_after_points", "homotopy_filler_after_points"),
    ("lax_modification", "lax_modification"),
    ("pointwise_modification", "pointwise_modification"),
    ("graph_side_modification", "graph_side_modification"),
    ("post_product_modification", "post_product_modification"),
    ("retuned_modification", "retuned_modification"),
    ("reindexed_modification_labels", "reindexed_modification_labels"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(REQUIRED_COMPONENTS) - set(data["component_names"]):
        out.append("required_source_components_missing")
    if set(REQUIRED_CARTESIAN_LEGS) - set(data["cartesian_leg_names"]):
        out.append("required_cartesian_component_legs_missing")
    if set(REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS) - set(data["boundary_fiber_coherence_cells"]):
        out.append("required_boundary_fiber_coherence_cells_missing")
    if set(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES) - set(data["fiber_coherence_faces"]):
        out.append("required_fiber_coherence_faces_missing")
    if REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES - set(data["globular_edges"]):
        out.append("required_globular_edges_missing")
    if REQUIRED_NATURALITY_PATHS - set(data["naturality_paths"]):
        out.append("required_multiplier_paths_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_globular_modification(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_COMPONENTS) <= set(data["component_names"])
        and set(REQUIRED_CARTESIAN_LEGS) <= set(data["cartesian_leg_names"])
        and set(REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS)
        <= set(data["boundary_fiber_coherence_cells"])
        and set(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES)
        <= set(data["fiber_coherence_faces"])
        and REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES <= set(data["globular_edges"])
        and REQUIRED_NATURALITY_PATHS <= set(data["naturality_paths"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc490_coherence_actual=True,
        globular_modification_actual=True,
        shared_globular_boundary_actual=True,
        source_boundary_actual=True,
        target_boundary_actual=True,
        source_boundary_matches_naturality=True,
        target_boundary_matches_structure=True,
        all_faces_actual=True,
        whiskering_compatibility_actual=True,
        vertical_horizontal_composition_actual=True,
        associativity_actual=True,
        interchange_actual=True,
        same_modification_all_paths=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        component_names=set(REQUIRED_COMPONENTS),
        cartesian_leg_names=set(REQUIRED_CARTESIAN_LEGS),
        boundary_fiber_coherence_cells=set(REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS),
        fiber_coherence_faces=set(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES),
        globular_edges=set(REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES),
        naturality_paths=set(REQUIRED_NATURALITY_PATHS),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def fiber_coherence_globular_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "eta_lift": ETA_EQUALIZER_LIFT_ID,
        "cartesian_source_lift": CARTESIAN_SOURCE_LIFT_ID,
        "represented_boundary_fiber": BOUNDARY_FIBER_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "cartesian_boundary_restriction": CARTESIAN_BOUNDARY_RESTRICTION_ID,
        "cartesian_boundary_fiber_coherence": CARTESIAN_BOUNDARY_FIBER_COHERENCE_ID,
        "fiber_coherence_globular_modification": FIBER_COHERENCE_GLOBULAR_MODIFICATION_ID,
        "fiber_coherence_globular_boundary": FIBER_COHERENCE_GLOBULAR_BOUNDARY_ID,
        "boundary_fiber_coherence_cells": REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS,
        "fiber_coherence_faces": REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES,
        "components": REQUIRED_COMPONENTS,
        "cartesian_legs": REQUIRED_CARTESIAN_LEGS,
        "naturality_paths": tuple(sorted(REQUIRED_NATURALITY_PATHS)),
        "endpoint_boundary": (p1, p2, p1 == p2),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
    }


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

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD1 coherence cells globularize",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES)
    and len(REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS) == 10
    and len(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES) == 10
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and fiber_coherence_globular_payload(T3_T5_z)
    == fiber_coherence_globular_payload(zC15)
    and fiber_coherence_globular_payload(T5_T3_z)
    == fiber_coherence_globular_payload(zC15)
    and fiber_coherence_globular_payload(T3_T3_T5_z)
    == fiber_coherence_globular_payload(zC45)
    and fiber_coherence_globular_payload(T15_zF22)
    == fiber_coherence_globular_payload(zC15F22)
    and fiber_coherence_globular_payload(T45_zF22)
    == fiber_coherence_globular_payload(zC45F22),
    "H1=%s faces=%d"
    % ([p["h1_order"] for p in profiles], len(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES)),
)

graph_only = live_source(
    globular_modification_actual=False,
    shared_globular_boundary_actual=False,
    globular_edges=REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES
    - {("cartesian_boundary_fiber_coherence", "fiber_coherence_globular_modification")},
    independent_cell_list=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD2 graph identities do not supply the modification",
    not accepts_globular_modification(graph_only)
    and {
        "globular_modification_missing",
        "shared_globular_boundary_missing",
        "required_globular_edges_missing",
        "independent_cell_list",
    }
    <= set(reasons(graph_only)),
    ",".join(reasons(graph_only)),
)

independent = live_source(
    all_faces_actual=False,
    independent_cell_list=True,
    boundary_mismatched_pasting=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD3 independent cell lists fail",
    not accepts_globular_modification(independent)
    and {
        "all_faces_missing",
        "independent_cell_list",
        "boundary_mismatched_pasting",
    }
    <= set(reasons(independent)),
    ",".join(reasons(independent)),
)

boundary_mismatch = live_source(
    source_boundary_actual=False,
    target_boundary_actual=False,
    source_boundary_matches_naturality=False,
    target_boundary_matches_structure=False,
    boundary_mismatched_pasting=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD4 source and target boundaries must match",
    not accepts_globular_modification(boundary_mismatch)
    and {
        "source_boundary_missing",
        "target_boundary_missing",
        "source_boundary_mismatch",
        "target_boundary_mismatch",
        "boundary_mismatched_pasting",
    }
    <= set(reasons(boundary_mismatch)),
    ",".join(reasons(boundary_mismatch)),
)

split = live_source(
    whiskering_compatibility_actual=False,
    vertical_horizontal_composition_actual=False,
    separate_boundary_restriction_modification=True,
    separate_fiber_arrow_modification=True,
    separate_fixed_boundary_modification=True,
    lax_modification=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD5 split modifications fail",
    not accepts_globular_modification(split)
    and {
        "whiskering_compatibility_missing",
        "vertical_horizontal_composition_missing",
        "separate_boundary_restriction_modification",
        "separate_fiber_arrow_modification",
        "separate_fixed_boundary_modification",
        "lax_modification",
    }
    <= set(reasons(split)),
    ",".join(reasons(split)),
)

late = live_source(
    carrier_native=False,
    source_before_points=False,
    pointwise_modification=True,
    graph_side_modification=True,
    post_product_modification=True,
    homotopy_filler_after_points=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD6 late pointwise graph-side fillers fail",
    not accepts_globular_modification(late)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "pointwise_modification",
        "graph_side_modification",
        "post_product_modification",
        "homotopy_filler_after_points",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    associativity_actual=False,
    interchange_actual=False,
    same_modification_all_paths=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_modification=True,
    reindexed_modification_labels=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD7 retuned or reindexed modifications fail",
    not accepts_globular_modification(retuned)
    and {
        "associativity_missing",
        "interchange_missing",
        "same_modification_not_all_paths",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_modification",
        "reindexed_modification_labels",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(globular_edges=REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES - {edge})
    for edge in list(REQUIRED_FIBER_COHERENCE_GLOBULAR_EDGES)[:8]
] + [
    live_source(globular_modification_actual=False),
    live_source(shared_globular_boundary_actual=False),
    live_source(fiber_coherence_faces=set(REQUIRED_BOUNDARY_FIBER_COHERENCE_FACES[:-1])),
    live_source(boundary_fiber_coherence_cells=set(REQUIRED_BOUNDARY_FIBER_COHERENCE_CELLS[:-1])),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD8 every edge face and cell is mandatory",
    not any(accepts_globular_modification(data) for data in missing_edges)
    and {
        "required_globular_edges_missing",
        "globular_modification_missing",
        "shared_globular_boundary_missing",
        "required_fiber_coherence_faces_missing",
        "required_boundary_fiber_coherence_cells_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_mod = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_modification=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD9 control/DH/Epstein modifications fail",
    not accepts_globular_modification(control_mod)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_modification",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_mod)),
    ",".join(reasons(control_mod)),
)

live = live_source()
dead_sources = {
    "graph_only": graph_only,
    "independent": independent,
    "boundary_mismatch": boundary_mismatch,
    "split": split,
    "late": late,
    "retuned": retuned,
    "control_mod": control_mod,
}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD10 only one source globular modification passes",
    accepts_globular_modification(live)
    and graph_connected(live["globular_edges"])
    and not any(accepts_globular_modification(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_globular_modification(data) for data in dead_sources.values()),
        accepts_globular_modification(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMQBARBECD10 ALL PASS: "
    "globular modification for cartesian boundary-fiber coherence pinned"
)
print(
    "VERDICT: the doc-490 represented cartesian boundary-fiber coherence cells "
    "must be faces of one source-level globular modification with shared "
    "source and target boundary. Independent lists, boundary-mismatched "
    "pasting, split modifications, late graph-side fillers, retuned "
    "modifications, and control/DH/Epstein point-formability do not construct "
    "the missing object."
)
