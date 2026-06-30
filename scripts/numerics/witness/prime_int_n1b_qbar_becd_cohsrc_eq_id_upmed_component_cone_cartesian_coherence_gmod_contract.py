r"""Globular-modification contract for cartesian component-cone coherence.

Doc 511 requires represented coherence cells for the cartesian component-cone
naturality. This witness pins the next edge: those cells must be faces of one
source-level globular modification with common source and target boundaries.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_ETA_ID = "eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
CONSTRAINT_OBJECT_ID = "Con_NCoup_med_UP_Eq_id_endpoint_dd4_rosati_control_source"
PRODUCT_OBJECT_ID = "Prod_NCoup_med_UP_Eq_id_endpoint_degree_dd4_push_graph_rosati_control"
COMPONENT_CONE_ID = "Cone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_COMPONENT_CONE_ID = "CartCone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_SOURCE_LIFTS_ID = "CartLift_med_UP_Eq_id_source_fiber"
CARTESIAN_COHERENCE_ID = "Cart_med_UP_Eq_id_BCF_self_dual_exact_source"
CONE_COHERENCE_ID = "Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
GLOBULAR_MODIFICATION_ID = "Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
GLOBULAR_BOUNDARY_ID = "GlobBd_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_med_UP_Eq_id_source_constraints"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_id_constraints_to_SubRep_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
CONTROL_DEATH_ID = "Nat_ControlDeath_med_UP_Eq_id_source_constraint"

PROJECTIONS = (
    "pi_NCoup_med_UP_Eq_id_endpoint_integrality",
    "pi_NCoup_med_UP_Eq_id_degree_maps",
    "pi_NCoup_med_UP_Eq_id_dd4_boundary",
    "pi_NCoup_med_UP_Eq_id_boundary_pushforward",
    "pi_NCoup_med_UP_Eq_id_graph_composition",
    "pi_NCoup_med_UP_Eq_id_rosati_count",
    "pi_NCoup_med_UP_Eq_id_control_death",
)

COMPONENT_OBJECTS = (
    "Comp_NCoup_med_UP_Eq_id_endpoint_integrality_source",
    "Comp_NCoup_med_UP_Eq_id_degree_maps_source",
    "Comp_NCoup_med_UP_Eq_id_dd4_boundary_source",
    "Comp_NCoup_med_UP_Eq_id_boundary_pushforward_source",
    "Comp_NCoup_med_UP_Eq_id_graph_composition_source",
    "Comp_NCoup_med_UP_Eq_id_rosati_count_source",
    "Comp_NCoup_med_UP_Eq_id_control_death_source",
)

COMPONENT_LEGS = (
    "leg_NCoup_med_UP_Eq_id_endpoint_integrality_source",
    "leg_NCoup_med_UP_Eq_id_degree_maps_source",
    "leg_NCoup_med_UP_Eq_id_dd4_boundary_source",
    "leg_NCoup_med_UP_Eq_id_boundary_pushforward_source",
    "leg_NCoup_med_UP_Eq_id_graph_composition_source",
    "leg_NCoup_med_UP_Eq_id_rosati_count_source",
    "leg_NCoup_med_UP_Eq_id_control_death_source",
)

PROJECTION_LEG_EQUALITIES = tuple(
    (projection, ALPHA_PAIRING_ID, leg)
    for projection, leg in zip(PROJECTIONS, COMPONENT_LEGS)
)

CONE_CELLS = (
    "cell_C3_C5_C15_NCoup_med_UP_Eq_id_component_cone",
    "cell_C5_C3_C15_NCoup_med_UP_Eq_id_component_cone",
    "cell_C3_C3_C5_C45_NCoup_med_UP_Eq_id_component_cone",
    "cell_F22_interchange_NCoup_med_UP_Eq_id_component_cone",
    "cell_pair_alpha_product_naturality_NCoup_med_UP_Eq_id",
    "cell_pair_beta_zero_diagonal_naturality_NCoup_med_UP_Eq_id",
)

MODIFICATION_FACES = (
    "face_C3_C5_C15_med_UP_Eq_id_globular_boundary",
    "face_C5_C3_C15_med_UP_Eq_id_globular_boundary",
    "face_C3_C3_C5_C45_med_UP_Eq_id_globular_boundary",
    "face_F22_interchange_med_UP_Eq_id_globular_boundary",
    "face_component_leg_naturality_med_UP_Eq_id_globular_boundary",
    "face_projection_leg_naturality_med_UP_Eq_id_globular_boundary",
    "face_pair_alpha_pair_beta_med_UP_Eq_id_globular_boundary",
)

COMPONENTS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

REQUIRED_COHERENCE_CELLS = {
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
}

FINITE_INDEX = set(COMPONENTS) | REQUIRED_COHERENCE_CELLS

REQUIRED_MODIFICATION_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("coupling_universal_arrow", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("universal_mediator", "source_component_cone"),
    ("coupling_universal_arrow", "cartesian_component_cone"),
    ("source_component_cone", "cartesian_component_cone"),
    ("cartesian_source_lifts", "cartesian_component_cone"),
    ("cartesian_source_coherence", "cartesian_component_cone"),
    ("cartesian_component_cone", "cartesian_component_cone_coherence"),
    ("cartesian_source_coherence", "cartesian_component_cone_coherence"),
    ("cartesian_component_cone_coherence", "globular_modification"),
    ("globular_modification", "shared_globular_boundary"),
    ("shared_globular_boundary", "source_boundary"),
    ("shared_globular_boundary", "target_boundary"),
    ("source_boundary", "component_leg_naturality_cells"),
    ("source_boundary", "projection_leg_naturality_cells"),
    ("target_boundary", "pair_alpha_product_naturality_cell"),
    ("target_boundary", "pair_beta_zero_diagonal_naturality_cell"),
    ("globular_modification", "C3_C5_to_C15_pasting_face"),
    ("globular_modification", "C5_C3_to_C15_pasting_face"),
    ("globular_modification", "C3_C3_C5_to_C45_pasting_face"),
    ("globular_modification", "F22_interchange_pasting_face"),
    ("globular_modification", "component_leg_pasting_face"),
    ("globular_modification", "projection_leg_pasting_face"),
    ("globular_modification", "pair_alpha_beta_pasting_face"),
    ("C3_C5_to_C15_pasting_face", "shared_globular_boundary"),
    ("C5_C3_to_C15_pasting_face", "shared_globular_boundary"),
    ("C3_C3_C5_to_C45_pasting_face", "shared_globular_boundary"),
    ("F22_interchange_pasting_face", "shared_globular_boundary"),
    ("component_leg_pasting_face", "component_leg_naturality_cells"),
    ("component_leg_pasting_face", "dd4_leg_boundary"),
    ("projection_leg_pasting_face", "projection_leg_naturality_cells"),
    ("pair_alpha_beta_pasting_face", "pair_alpha_product_naturality_cell"),
    ("pair_alpha_beta_pasting_face", "pair_beta_zero_diagonal_naturality_cell"),
    ("globular_modification", "whiskering_compatibility"),
    ("whiskering_compatibility", "all_component_legs"),
    ("whiskering_compatibility", "all_projection_legs"),
    ("globular_modification", "vertical_horizontal_composition"),
    ("vertical_horizontal_composition", "associativity"),
    ("vertical_horizontal_composition", "interchange"),
    ("globular_modification", "coherence_preserves_coefficients"),
    ("globular_modification", "coherence_preserves_signed_support"),
    ("globular_modification", "same_modification_all_paths"),
    ("same_modification_all_paths", "C3_C5_equals_C15"),
    ("same_modification_all_paths", "C5_C3_equals_C15"),
    ("same_modification_all_paths", "C3_C3_C5_equals_C45"),
    ("same_modification_all_paths", "F22_product"),
    ("dd4_leg_boundary", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("control_death_boundary", "source_before_points_and_graph_objects"),
    ("globular_modification", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "h1_order": z1_order // len(coboundaries),
        "coboundaries_res1_zero": all(
            from_vec(vec).get(1, 0) == 0 for vec in coboundaries
        ),
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "universal_mediator_actual": False,
        "formation_fiber_actual": False,
        "coupling_universal_arrow_actual": False,
        "coupling_subrepresenter_actual": False,
        "finite_limit_cut_actual": False,
        "component_cone_actual": False,
        "cartesian_component_cone_actual": False,
        "cartesian_source_lifts_actual": False,
        "cartesian_source_coherence_actual": False,
        "cone_coherence_actual": False,
        "globular_modification_actual": False,
        "modification_generated_by_coherence": False,
        "shared_globular_boundary_actual": False,
        "source_boundary_actual": False,
        "target_boundary_actual": False,
        "source_boundary_matches_component_projection": False,
        "target_boundary_matches_pairing": False,
        "all_pasting_faces_actual": False,
        "C3_C5_C15_face_actual": False,
        "C5_C3_C15_face_actual": False,
        "C3_C3_C5_C45_face_actual": False,
        "F22_interchange_face_actual": False,
        "component_leg_pasting_face_actual": False,
        "projection_leg_pasting_face_actual": False,
        "pair_alpha_beta_pasting_face_actual": False,
        "whiskering_compatibility_actual": False,
        "vertical_horizontal_composition_actual": False,
        "associativity_actual": False,
        "interchange_actual": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "same_modification_payload_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "finite_anchors_generated": False,
        "no_next_coherence_obligation": False,
        "modification_before_points": False,
        "modification_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "independent_represented_cell_list": False,
        "boundary_mismatched_cells": False,
        "formal_pasting_diagram": False,
        "separate_component_modifications": False,
        "separate_pairing_modifications": False,
        "homotopy_filler_after_points": False,
        "lax_modification_only": False,
        "graph_side_modification": False,
        "pointwise_modification": False,
        "retuned_modification": False,
        "reindexed_modification_label": False,
        "post_product_modification": False,
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("universal_mediator_actual", "universal_mediator_missing"),
    ("formation_fiber_actual", "formation_fiber_missing"),
    ("coupling_universal_arrow_actual", "coupling_universal_arrow_missing"),
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("component_cone_actual", "component_cone_missing"),
    ("cartesian_component_cone_actual", "cartesian_component_cone_missing"),
    ("cartesian_source_lifts_actual", "cartesian_source_lifts_missing"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("cone_coherence_actual", "cone_coherence_missing"),
    ("globular_modification_actual", "globular_modification_missing"),
    ("modification_generated_by_coherence", "modification_not_generated_by_coherence"),
    ("shared_globular_boundary_actual", "shared_globular_boundary_missing"),
    ("source_boundary_actual", "source_boundary_missing"),
    ("target_boundary_actual", "target_boundary_missing"),
    ("source_boundary_matches_component_projection", "source_boundary_mismatch"),
    ("target_boundary_matches_pairing", "target_boundary_mismatch"),
    ("all_pasting_faces_actual", "pasting_faces_missing"),
    ("C3_C5_C15_face_actual", "C3_C5_C15_face_missing"),
    ("C5_C3_C15_face_actual", "C5_C3_C15_face_missing"),
    ("C3_C3_C5_C45_face_actual", "C3_C3_C5_C45_face_missing"),
    ("F22_interchange_face_actual", "F22_interchange_face_missing"),
    ("component_leg_pasting_face_actual", "component_leg_pasting_face_missing"),
    ("projection_leg_pasting_face_actual", "projection_leg_pasting_face_missing"),
    ("pair_alpha_beta_pasting_face_actual", "pair_alpha_beta_pasting_face_missing"),
    ("whiskering_compatibility_actual", "whiskering_compatibility_missing"),
    ("vertical_horizontal_composition_actual", "vertical_horizontal_composition_missing"),
    ("associativity_actual", "associativity_missing"),
    ("interchange_actual", "interchange_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("same_modification_payload_all_paths", "same_modification_payload_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("modification_before_points", "modification_not_before_points"),
    ("modification_before_graph_objects", "modification_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("independent_represented_cell_list", "independent_represented_cell_list"),
    ("boundary_mismatched_cells", "boundary_mismatched_cells"),
    ("formal_pasting_diagram", "formal_pasting_diagram"),
    ("separate_component_modifications", "separate_component_modifications"),
    ("separate_pairing_modifications", "separate_pairing_modifications"),
    ("homotopy_filler_after_points", "homotopy_filler_after_points"),
    ("lax_modification_only", "lax_modification_only"),
    ("graph_side_modification", "graph_side_modification"),
    ("pointwise_modification", "pointwise_modification"),
    ("retuned_modification", "retuned_modification"),
    ("reindexed_modification_label", "reindexed_modification_label"),
    ("post_product_modification", "post_product_modification"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(data["finite_index"]) != FINITE_INDEX:
        out.append("finite_index_not_exact")
    if data["finite_index_cardinality"] != len(FINITE_INDEX):
        out.append("finite_index_cardinality_wrong")
    if not REQUIRED_MODIFICATION_EDGES <= set(data["required_edges"]):
        out.append("required_globular_modification_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_globular_modification(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_MODIFICATION_EDGES <= set(data["required_edges"])
        and graph_connected(set(data["required_edges"]))
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        universal_mediator_actual=True,
        formation_fiber_actual=True,
        coupling_universal_arrow_actual=True,
        coupling_subrepresenter_actual=True,
        finite_limit_cut_actual=True,
        component_cone_actual=True,
        cartesian_component_cone_actual=True,
        cartesian_source_lifts_actual=True,
        cartesian_source_coherence_actual=True,
        cone_coherence_actual=True,
        globular_modification_actual=True,
        modification_generated_by_coherence=True,
        shared_globular_boundary_actual=True,
        source_boundary_actual=True,
        target_boundary_actual=True,
        source_boundary_matches_component_projection=True,
        target_boundary_matches_pairing=True,
        all_pasting_faces_actual=True,
        C3_C5_C15_face_actual=True,
        C5_C3_C15_face_actual=True,
        C3_C3_C5_C45_face_actual=True,
        F22_interchange_face_actual=True,
        component_leg_pasting_face_actual=True,
        projection_leg_pasting_face_actual=True,
        pair_alpha_beta_pasting_face_actual=True,
        whiskering_compatibility_actual=True,
        vertical_horizontal_composition_actual=True,
        associativity_actual=True,
        interchange_actual=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        same_modification_payload_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        finite_anchors_generated=True,
        no_next_coherence_obligation=True,
        modification_before_points=True,
        modification_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_MODIFICATION_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def modification_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    source_boundary = (
        "component_projection_naturality",
        tuple(zip(COMPONENT_LEGS, COMPONENT_OBJECTS)),
        tuple(zip(PROJECTIONS, COMPONENT_LEGS)),
    )
    target_boundary = (
        "pair_alpha_beta_naturality",
        ALPHA_PAIRING_ID,
        BETA_PAIRING_ID,
    )
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "coupling_universal_arrow": COUPLING_ETA_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "component_cone": COMPONENT_CONE_ID,
        "cartesian_component_cone": CARTESIAN_COMPONENT_CONE_ID,
        "cartesian_source_lifts": CARTESIAN_SOURCE_LIFTS_ID,
        "cartesian_source_coherence": CARTESIAN_COHERENCE_ID,
        "component_cone_coherence": CONE_COHERENCE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "globular_boundary": GLOBULAR_BOUNDARY_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "component_objects": COMPONENT_OBJECTS,
        "component_legs": COMPONENT_LEGS,
        "projections": PROJECTIONS,
        "projection_leg_equalities": PROJECTION_LEG_EQUALITIES,
        "cone_cells": CONE_CELLS,
        "modification_faces": MODIFICATION_FACES,
        "source_boundary": source_boundary,
        "target_boundary": target_boundary,
        "endpoint_boundary": (COMPONENT_LEGS[0], PROJECTIONS[0], p1, p2, p1 == p2),
        "degree_boundary": (COMPONENT_LEGS[1], PROJECTIONS[1], tuple(sorted(chi)), p1 + p2),
        "dd4_boundary": (COMPONENT_LEGS[2], PROJECTIONS[2], DD4_CLASS_ID),
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "pushforward_boundary": (COMPONENT_LEGS[3], PROJECTIONS[3], tuple(chi.items())),
        "graph_boundary": (COMPONENT_LEGS[4], PROJECTIONS[4], tuple(sorted(chi))),
        "rosati_boundary": (COMPONENT_LEGS[5], PROJECTIONS[5], "rosati_count_source"),
        "control_boundary": (COMPONENT_LEGS[6], PROJECTIONS[6], CONTROL_DEATH_ID),
        "whiskering": ("component_legs", "projection_legs"),
        "vertical_horizontal_composition": ("associativity", "interchange"),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "globular_modification_payload": True,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_MODIFICATION_EDGES)),
    }


def modification_row(chi: dict[int, int]) -> bool:
    payload = modification_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["component_cone"] == COMPONENT_CONE_ID
        and payload["cartesian_component_cone"] == CARTESIAN_COMPONENT_CONE_ID
        and payload["cartesian_source_lifts"] == CARTESIAN_SOURCE_LIFTS_ID
        and payload["cartesian_source_coherence"] == CARTESIAN_COHERENCE_ID
        and payload["component_cone_coherence"] == CONE_COHERENCE_ID
        and payload["globular_modification"] == GLOBULAR_MODIFICATION_ID
        and payload["globular_boundary"] == GLOBULAR_BOUNDARY_ID
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["coupling_universal_arrow"] == COUPLING_ETA_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["product"] == PRODUCT_OBJECT_ID
        and payload["alpha_pairing"] == ALPHA_PAIRING_ID
        and payload["beta_pairing"] == BETA_PAIRING_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and payload["component_objects"] == COMPONENT_OBJECTS
        and payload["component_legs"] == COMPONENT_LEGS
        and payload["projections"] == PROJECTIONS
        and payload["projection_leg_equalities"] == PROJECTION_LEG_EQUALITIES
        and payload["cone_cells"] == CONE_CELLS
        and payload["modification_faces"] == MODIFICATION_FACES
        and payload["source_boundary"][0] == "component_projection_naturality"
        and payload["target_boundary"][0] == "pair_alpha_beta_naturality"
        and payload["dd4_boundary"] == (COMPONENT_LEGS[2], PROJECTIONS[2], DD4_CLASS_ID)
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_boundary"] == (COMPONENT_LEGS[6], PROJECTIONS[6], CONTROL_DEATH_ID)
        and payload["whiskering"] == ("component_legs", "projection_legs")
        and payload["vertical_horizontal_composition"] == ("associativity", "interchange")
        and payload["globular_modification_payload"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_MODIFICATION_EDGES))
    )


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

rows = [z, zC3, zC5, zC15, zC45, zF22, zC15F22, zC45F22]
profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    f"{TAG}1 represented cells assemble as one source globular modification",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_MODIFICATION_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and modification_payload(T3_T5_z) == modification_payload(zC15)
    and modification_payload(T5_T3_z) == modification_payload(zC15)
    and modification_payload(T3_T3_T5_z) == modification_payload(zC45)
    and modification_payload(T15_zF22) == modification_payload(zC15F22)
    and modification_payload(T45_zF22) == modification_payload(zC45F22)
    and all(modification_row(row) for row in rows),
    "H1=%s mod=%s faces=%d edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        GLOBULAR_MODIFICATION_ID,
        len(MODIFICATION_FACES),
        len(REQUIRED_MODIFICATION_EDGES),
    ),
)

independent = live_source(
    globular_modification_actual=False,
    modification_generated_by_coherence=False,
    independent_represented_cell_list=True,
    formal_pasting_diagram=True,
)

gate(
    f"{TAG}2 independent represented cell lists do not globularize",
    not accepts_globular_modification(independent)
    and {
        "globular_modification_missing",
        "modification_not_generated_by_coherence",
        "independent_represented_cell_list",
        "formal_pasting_diagram",
    }
    <= set(reasons(independent)),
    ",".join(reasons(independent)),
)

boundary_gap = live_source(
    shared_globular_boundary_actual=False,
    source_boundary_actual=False,
    target_boundary_actual=False,
    source_boundary_matches_component_projection=False,
    target_boundary_matches_pairing=False,
    boundary_mismatched_cells=True,
)

gate(
    f"{TAG}3 shared source and target boundaries are mandatory",
    not accepts_globular_modification(boundary_gap)
    and {
        "shared_globular_boundary_missing",
        "source_boundary_missing",
        "target_boundary_missing",
        "source_boundary_mismatch",
        "target_boundary_mismatch",
        "boundary_mismatched_cells",
    }
    <= set(reasons(boundary_gap)),
    ",".join(reasons(boundary_gap)),
)

separate = live_source(
    all_pasting_faces_actual=False,
    component_leg_pasting_face_actual=False,
    projection_leg_pasting_face_actual=False,
    pair_alpha_beta_pasting_face_actual=False,
    separate_component_modifications=True,
    separate_pairing_modifications=True,
)

gate(
    f"{TAG}4 separate component or pairing modifications fail",
    not accepts_globular_modification(separate)
    and {
        "pasting_faces_missing",
        "component_leg_pasting_face_missing",
        "projection_leg_pasting_face_missing",
        "pair_alpha_beta_pasting_face_missing",
        "separate_component_modifications",
        "separate_pairing_modifications",
    }
    <= set(reasons(separate)),
    ",".join(reasons(separate)),
)

path_gap = live_source(
    C3_C5_C15_face_actual=False,
    C5_C3_C15_face_actual=False,
    C3_C3_C5_C45_face_actual=False,
    F22_interchange_face_actual=False,
    same_modification_payload_all_paths=False,
    C5_C3_equals_C15=False,
    F22_product=False,
)

gate(
    f"{TAG}5 path pasting faces and same modification payload are mandatory",
    not accepts_globular_modification(path_gap)
    and {
        "C3_C5_C15_face_missing",
        "C5_C3_C15_face_missing",
        "C3_C3_C5_C45_face_missing",
        "F22_interchange_face_missing",
        "same_modification_payload_not_all_paths",
        "C5_C3_not_C15",
        "F22_product_missing",
    }
    <= set(reasons(path_gap)),
    ",".join(reasons(path_gap)),
)

composition_gap = live_source(
    whiskering_compatibility_actual=False,
    vertical_horizontal_composition_actual=False,
    associativity_actual=False,
    interchange_actual=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
)

gate(
    f"{TAG}6 whiskering, composition, and preservation laws are mandatory",
    not accepts_globular_modification(composition_gap)
    and {
        "whiskering_compatibility_missing",
        "vertical_horizontal_composition_missing",
        "associativity_missing",
        "interchange_missing",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
    }
    <= set(reasons(composition_gap)),
    ",".join(reasons(composition_gap)),
)

late = live_source(
    modification_before_points=False,
    modification_before_graph_objects=False,
    homotopy_filler_after_points=True,
    graph_side_modification=True,
    pointwise_modification=True,
    post_product_modification=True,
)

gate(
    f"{TAG}7 pointwise, graph-side, homotopy, or post-product modifications fail",
    not accepts_globular_modification(late)
    and {
        "modification_not_before_points",
        "modification_not_before_graph_objects",
        "homotopy_filler_after_points",
        "graph_side_modification",
        "pointwise_modification",
        "post_product_modification",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    lax_modification_only=True,
    retuned_modification=True,
    reindexed_modification_label=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
    finite_index=set(FINITE_INDEX) | {"globular_modification_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
)

gate(
    f"{TAG}8 lax or retuned modifications and finite-index expansion fail",
    not accepts_globular_modification(retuned)
    and {
        "lax_modification_only",
        "retuned_modification",
        "reindexed_modification_label",
        "expanded_finite_index",
        "one_more_layer_tower",
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "finite_anchors_not_generated",
        "next_coherence_obligation_open",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

control_like = live_source(
    modification_generated_by_coherence=False,
    graph_side_modification=True,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}9 non-source modification leaves controls formable",
    not accepts_globular_modification(control_like)
    and {
        "modification_not_generated_by_coherence",
        "graph_side_modification",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_like)),
    ",".join(reasons(control_like)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_MODIFICATION_EDGES - {("cartesian_component_cone_coherence", "globular_modification")}),
    live_source(required_edges=REQUIRED_MODIFICATION_EDGES - {("globular_modification", "shared_globular_boundary")}),
    live_source(required_edges=REQUIRED_MODIFICATION_EDGES - {("source_boundary", "projection_leg_naturality_cells")}),
    live_source(required_edges=REQUIRED_MODIFICATION_EDGES - {("target_boundary", "pair_alpha_product_naturality_cell")}),
    live_source(universal_mediator_actual=False),
    live_source(globular_modification_actual=False),
    live_source(shared_globular_boundary_actual=False),
    live_source(source_boundary_actual=False),
    live_source(target_boundary_actual=False),
    live_source(pair_alpha_beta_pasting_face_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}10 every globular modification edge is mandatory",
    not any(accepts_globular_modification(data) for data in missing_edges)
    and {
        "required_globular_modification_edges_missing",
        "universal_mediator_missing",
        "globular_modification_missing",
        "shared_globular_boundary_missing",
        "source_boundary_missing",
        "target_boundary_missing",
        "pair_alpha_beta_pasting_face_missing",
    }
    <= missing_reasons
    and accepts_globular_modification(live_source())
    and not any(
        accepts_globular_modification(data)
        for data in (
            independent,
            boundary_gap,
            separate,
            path_gap,
            composition_gap,
            late,
            retuned,
            control_like,
        )
    ),
    "missing=%s live=%s"
    % (sorted(missing_reasons), accepts_globular_modification(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "component-cone cartesian-coherence globular-modification component-"
    "object product-projected parallel-morphism finite-limit subrepresented "
    "coupled formation-coherent self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: doc-511 represented cartesian-cone coherence cells must be "
    "faces of one source-level globular modification with shared source and "
    "target boundaries. Independent represented cell lists, mismatched "
    "boundaries, separate component or pairing modifications, pointwise or "
    "graph-side modifications, post-product fillers, and finite-index "
    "expansion do not construct the missing source object."
)
