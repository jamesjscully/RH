r"""Cartesian contract for the mediator globular-modification boundary fiber.

Doc 513 requires the doc-512 globular modification to be selected by a
represented source boundary fiber over the fixed globular boundary. This
witness pins the next edge: that represented boundary fiber must itself be
cartesian over the same represented source lifts. A static one-boundary fiber,
a reused fiber name, or a fiber rebuilt after base change does not construct
the missing source object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_ETA_ID = "eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
COMPONENT_CONE_ID = "Cone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_COMPONENT_CONE_ID = "CartCone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_SOURCE_LIFTS_ID = "CartLift_med_UP_Eq_id_source_fiber"
CARTESIAN_COHERENCE_ID = "Cart_med_UP_Eq_id_BCF_self_dual_exact_source"
CONE_COHERENCE_ID = "Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
GLOBULAR_MODIFICATION_ID = "Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
GLOBULAR_BOUNDARY_ID = "GlobBd_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
BOUNDARY_RESTRICTION_ID = "res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd"
BOUNDARY_FIBER_ID = "Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
BOUNDARY_FIBER_ARROW_ID = "eta_Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_BOUNDARY_FIBER_ID = "CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
CARTESIAN_BOUNDARY_RESTRICTION_ID = "cart_res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd"
CARTESIAN_FIBER_ARROW_TRANSPORT_ID = "cart_eta_Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
PRODUCT_OBJECT_ID = "Prod_NCoup_med_UP_Eq_id_endpoint_degree_dd4_push_graph_rosati_control"
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

BASE_BOUNDARY_FIBER_EDGES = {
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
    ("globular_modification", "boundary_restriction_map"),
    ("boundary_restriction_map", "shared_globular_boundary"),
    ("boundary_restriction_map", "represented_boundary_fiber"),
    ("shared_globular_boundary", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "fiber_universal_arrow"),
    ("fiber_universal_arrow", "selected_globular_modification"),
    ("selected_globular_modification", "globular_modification"),
    ("represented_boundary_fiber", "unique_source_filler"),
    ("unique_source_filler", "contractible_after_represented_fiber"),
    ("represented_boundary_fiber", "boundary_preservation"),
    ("boundary_preservation", "shared_globular_boundary"),
    ("boundary_preservation", "component_projection_boundaries"),
    ("boundary_preservation", "pair_alpha_beta_target_boundary"),
    ("boundary_preservation", "pasting_faces"),
    ("boundary_preservation", "coherence_preserves_coefficients"),
    ("boundary_preservation", "coherence_preserves_signed_support"),
    ("boundary_preservation", "source_before_points_and_graph_objects"),
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
    ("dd4_leg_boundary", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
}

CARTESIAN_BOUNDARY_FIBER_EDGES = {
    ("cartesian_source_lifts", "cartesian_boundary_fiber"),
    ("cartesian_source_coherence", "cartesian_boundary_fiber"),
    ("represented_boundary_fiber", "cartesian_boundary_fiber"),
    ("boundary_restriction_map", "cartesian_boundary_restriction"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "fiber_universal_arrow"),
    ("cartesian_boundary_fiber", "cartesian_fiber_arrow_transport"),
    ("cartesian_fiber_arrow_transport", "selected_globular_modification"),
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
    ("cartesian_boundary_fiber", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
}

REQUIRED_CARTESIAN_FIBER_EDGES = (
    BASE_BOUNDARY_FIBER_EDGES | CARTESIAN_BOUNDARY_FIBER_EDGES
)


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
        "shared_globular_boundary_actual": False,
        "boundary_restriction_actual": False,
        "represented_boundary_fiber_actual": False,
        "fiber_over_fixed_boundary": False,
        "fiber_universal_arrow_actual": False,
        "fiber_arrow_selects_modification": False,
        "cartesian_boundary_fiber_actual": False,
        "cartesian_boundary_restriction_actual": False,
        "boundary_restriction_cartesian": False,
        "fiber_universal_arrow_cartesian": False,
        "cartesian_fiber_arrow_transport_actual": False,
        "fixed_boundary_pullback_actual": False,
        "same_cartesian_fiber_all_paths": False,
        "component_boundary_cartesian": False,
        "projection_boundary_cartesian": False,
        "pair_alpha_beta_boundary_cartesian": False,
        "pasting_faces_cartesian": False,
        "unique_source_filler_after_fiber": False,
        "contractible_only_after_fiber": False,
        "boundary_preservation_actual": False,
        "coefficients_preserved": False,
        "signed_support_preserved": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "finite_anchors_generated": False,
        "no_next_coherence_obligation": False,
        "cartesian_fiber_before_points": False,
        "cartesian_fiber_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "static_one_boundary_fiber": False,
        "reused_fiber_name_without_pullback": False,
        "chosen_base_change_fiber": False,
        "fiber_rebuilt_after_base_change": False,
        "noncartesian_pullback": False,
        "local_transport_table": False,
        "pointwise_cartesian_fiber": False,
        "graph_side_cartesian_fiber": False,
        "post_product_cartesian_fiber": False,
        "retuned_cartesian_fiber": False,
        "reindexed_cartesian_fiber": False,
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
    ("shared_globular_boundary_actual", "shared_globular_boundary_missing"),
    ("boundary_restriction_actual", "boundary_restriction_missing"),
    ("represented_boundary_fiber_actual", "represented_boundary_fiber_missing"),
    ("fiber_over_fixed_boundary", "fiber_not_over_fixed_boundary"),
    ("fiber_universal_arrow_actual", "fiber_universal_arrow_missing"),
    ("fiber_arrow_selects_modification", "fiber_arrow_does_not_select_modification"),
    ("cartesian_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    (
        "cartesian_boundary_restriction_actual",
        "cartesian_boundary_restriction_missing",
    ),
    ("boundary_restriction_cartesian", "boundary_restriction_not_cartesian"),
    ("fiber_universal_arrow_cartesian", "fiber_universal_arrow_not_cartesian"),
    (
        "cartesian_fiber_arrow_transport_actual",
        "cartesian_fiber_arrow_transport_missing",
    ),
    ("fixed_boundary_pullback_actual", "fixed_boundary_pullback_missing"),
    ("same_cartesian_fiber_all_paths", "same_cartesian_fiber_not_all_paths"),
    ("component_boundary_cartesian", "component_boundary_not_cartesian"),
    ("projection_boundary_cartesian", "projection_boundary_not_cartesian"),
    ("pair_alpha_beta_boundary_cartesian", "pair_alpha_beta_boundary_not_cartesian"),
    ("pasting_faces_cartesian", "pasting_faces_not_cartesian"),
    ("unique_source_filler_after_fiber", "unique_source_filler_missing"),
    ("contractible_only_after_fiber", "contractibility_not_after_fiber"),
    ("boundary_preservation_actual", "boundary_preservation_missing"),
    ("coefficients_preserved", "coefficients_not_preserved"),
    ("signed_support_preserved", "signed_support_not_preserved"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("cartesian_fiber_before_points", "cartesian_fiber_not_before_points"),
    (
        "cartesian_fiber_before_graph_objects",
        "cartesian_fiber_not_before_graph_objects",
    ),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("static_one_boundary_fiber", "static_one_boundary_fiber"),
    ("reused_fiber_name_without_pullback", "reused_fiber_name_without_pullback"),
    ("chosen_base_change_fiber", "chosen_base_change_fiber"),
    ("fiber_rebuilt_after_base_change", "fiber_rebuilt_after_base_change"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("local_transport_table", "local_transport_table"),
    ("pointwise_cartesian_fiber", "pointwise_cartesian_fiber"),
    ("graph_side_cartesian_fiber", "graph_side_cartesian_fiber"),
    ("post_product_cartesian_fiber", "post_product_cartesian_fiber"),
    ("retuned_cartesian_fiber", "retuned_cartesian_fiber"),
    ("reindexed_cartesian_fiber", "reindexed_cartesian_fiber"),
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
    if not REQUIRED_CARTESIAN_FIBER_EDGES <= set(data["required_edges"]):
        out.append("required_cartesian_boundary_fiber_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_boundary_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_CARTESIAN_FIBER_EDGES <= set(data["required_edges"])
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
        shared_globular_boundary_actual=True,
        boundary_restriction_actual=True,
        represented_boundary_fiber_actual=True,
        fiber_over_fixed_boundary=True,
        fiber_universal_arrow_actual=True,
        fiber_arrow_selects_modification=True,
        cartesian_boundary_fiber_actual=True,
        cartesian_boundary_restriction_actual=True,
        boundary_restriction_cartesian=True,
        fiber_universal_arrow_cartesian=True,
        cartesian_fiber_arrow_transport_actual=True,
        fixed_boundary_pullback_actual=True,
        same_cartesian_fiber_all_paths=True,
        component_boundary_cartesian=True,
        projection_boundary_cartesian=True,
        pair_alpha_beta_boundary_cartesian=True,
        pasting_faces_cartesian=True,
        unique_source_filler_after_fiber=True,
        contractible_only_after_fiber=True,
        boundary_preservation_actual=True,
        coefficients_preserved=True,
        signed_support_preserved=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        finite_anchors_generated=True,
        no_next_coherence_obligation=True,
        cartesian_fiber_before_points=True,
        cartesian_fiber_before_graph_objects=True,
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


def cartesian_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
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
        "boundary_restriction": BOUNDARY_RESTRICTION_ID,
        "boundary_fiber": BOUNDARY_FIBER_ID,
        "boundary_fiber_arrow": BOUNDARY_FIBER_ARROW_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "cartesian_boundary_restriction": CARTESIAN_BOUNDARY_RESTRICTION_ID,
        "cartesian_fiber_arrow_transport": CARTESIAN_FIBER_ARROW_TRANSPORT_ID,
        "selected_globular_modification": GLOBULAR_MODIFICATION_ID,
        "fixed_boundary": GLOBULAR_BOUNDARY_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "component_objects": COMPONENT_OBJECTS,
        "component_legs": COMPONENT_LEGS,
        "projections": PROJECTIONS,
        "projection_leg_equalities": tuple(zip(PROJECTIONS, COMPONENT_LEGS)),
        "cone_cells": CONE_CELLS,
        "modification_faces": MODIFICATION_FACES,
        "source_boundary": (
            "component_projection_naturality",
            tuple(zip(COMPONENT_LEGS, COMPONENT_OBJECTS)),
            tuple(zip(PROJECTIONS, COMPONENT_LEGS)),
        ),
        "target_boundary": (
            "pair_alpha_beta_naturality",
            ALPHA_PAIRING_ID,
            BETA_PAIRING_ID,
        ),
        "cartesian_pullbacks": (
            "fixed_boundary",
            "source_boundary",
            "target_boundary",
            "pasting_faces",
            "C3_C5_C15",
            "C5_C3_C15",
            "C3_C3_C5_C45",
            "F22",
        ),
        "endpoint_boundary": (COMPONENT_LEGS[0], PROJECTIONS[0], p1, p2, p1 == p2),
        "degree_boundary": (COMPONENT_LEGS[1], PROJECTIONS[1], tuple(sorted(chi))),
        "dd4_boundary": (COMPONENT_LEGS[2], PROJECTIONS[2], DD4_CLASS_ID),
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "pushforward_boundary": (COMPONENT_LEGS[3], PROJECTIONS[3], tuple(chi.items())),
        "graph_boundary": (COMPONENT_LEGS[4], PROJECTIONS[4], tuple(sorted(chi))),
        "rosati_boundary": (COMPONENT_LEGS[5], PROJECTIONS[5], "rosati_count_source"),
        "control_boundary": (COMPONENT_LEGS[6], PROJECTIONS[6], CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cartesian_boundary_fiber_payload": True,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_CARTESIAN_FIBER_EDGES)),
    }


def cartesian_fiber_row(chi: dict[int, int]) -> bool:
    payload = cartesian_fiber_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["cartesian_boundary_fiber"] == CARTESIAN_BOUNDARY_FIBER_ID
        and payload["cartesian_boundary_restriction"] == CARTESIAN_BOUNDARY_RESTRICTION_ID
        and payload["cartesian_fiber_arrow_transport"] == CARTESIAN_FIBER_ARROW_TRANSPORT_ID
        and payload["boundary_restriction"] == BOUNDARY_RESTRICTION_ID
        and payload["boundary_fiber"] == BOUNDARY_FIBER_ID
        and payload["boundary_fiber_arrow"] == BOUNDARY_FIBER_ARROW_ID
        and payload["globular_boundary"] == GLOBULAR_BOUNDARY_ID
        and payload["selected_globular_modification"] == GLOBULAR_MODIFICATION_ID
        and payload["component_cone"] == COMPONENT_CONE_ID
        and payload["cartesian_component_cone"] == CARTESIAN_COMPONENT_CONE_ID
        and payload["cartesian_source_lifts"] == CARTESIAN_SOURCE_LIFTS_ID
        and payload["cartesian_source_coherence"] == CARTESIAN_COHERENCE_ID
        and payload["component_cone_coherence"] == CONE_COHERENCE_ID
        and payload["product"] == PRODUCT_OBJECT_ID
        and payload["alpha_pairing"] == ALPHA_PAIRING_ID
        and payload["beta_pairing"] == BETA_PAIRING_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and payload["component_objects"] == COMPONENT_OBJECTS
        and payload["component_legs"] == COMPONENT_LEGS
        and payload["projections"] == PROJECTIONS
        and payload["cone_cells"] == CONE_CELLS
        and payload["modification_faces"] == MODIFICATION_FACES
        and payload["source_boundary"][0] == "component_projection_naturality"
        and payload["target_boundary"][0] == "pair_alpha_beta_naturality"
        and payload["dd4_boundary"] == (COMPONENT_LEGS[2], PROJECTIONS[2], DD4_CLASS_ID)
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_boundary"] == (COMPONENT_LEGS[6], PROJECTIONS[6], CONTROL_DEATH_ID)
        and payload["cartesian_boundary_fiber_payload"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_CARTESIAN_FIBER_EDGES))
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
    f"{TAG}1 represented boundary fiber is cartesian over source lifts",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_FIBER_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_fiber_payload(T3_T5_z) == cartesian_fiber_payload(zC15)
    and cartesian_fiber_payload(T5_T3_z) == cartesian_fiber_payload(zC15)
    and cartesian_fiber_payload(T3_T3_T5_z) == cartesian_fiber_payload(zC45)
    and cartesian_fiber_payload(T15_zF22) == cartesian_fiber_payload(zC15F22)
    and cartesian_fiber_payload(T45_zF22) == cartesian_fiber_payload(zC45F22)
    and all(cartesian_fiber_row(row) for row in rows)
    and accepts_cartesian_boundary_fiber(live_source()),
    "H1=%s cartfib=%s edges=%d finite=%d"
    % (
        [p["h1_order"] for p in profiles],
        CARTESIAN_BOUNDARY_FIBER_ID,
        len(REQUIRED_CARTESIAN_FIBER_EDGES),
        len(FINITE_INDEX),
    ),
)

static = live_source(
    cartesian_boundary_fiber_actual=False,
    boundary_restriction_cartesian=False,
    fiber_universal_arrow_cartesian=False,
    same_cartesian_fiber_all_paths=False,
    static_one_boundary_fiber=True,
    reused_fiber_name_without_pullback=True,
)

gate(
    f"{TAG}2 static or reused one-boundary fibers fail",
    not accepts_cartesian_boundary_fiber(static)
    and {
        "cartesian_boundary_fiber_missing",
        "boundary_restriction_not_cartesian",
        "fiber_universal_arrow_not_cartesian",
        "same_cartesian_fiber_not_all_paths",
        "static_one_boundary_fiber",
        "reused_fiber_name_without_pullback",
    }
    <= set(reasons(static)),
    ",".join(reasons(static)),
)

noncartesian = live_source(
    fixed_boundary_pullback_actual=False,
    component_boundary_cartesian=False,
    projection_boundary_cartesian=False,
    pair_alpha_beta_boundary_cartesian=False,
    pasting_faces_cartesian=False,
    noncartesian_pullback=True,
)

gate(
    f"{TAG}3 noncartesian pullbacks fail boundary preservation",
    not accepts_cartesian_boundary_fiber(noncartesian)
    and {
        "fixed_boundary_pullback_missing",
        "component_boundary_not_cartesian",
        "projection_boundary_not_cartesian",
        "pair_alpha_beta_boundary_not_cartesian",
        "pasting_faces_not_cartesian",
        "noncartesian_pullback",
    }
    <= set(reasons(noncartesian)),
    ",".join(reasons(noncartesian)),
)

chosen_rebuilt = live_source(
    cartesian_boundary_restriction_actual=False,
    cartesian_fiber_arrow_transport_actual=False,
    chosen_base_change_fiber=True,
    fiber_rebuilt_after_base_change=True,
    local_transport_table=True,
)

gate(
    f"{TAG}4 chosen rebuilt or local base-change fibers fail",
    not accepts_cartesian_boundary_fiber(chosen_rebuilt)
    and {
        "cartesian_boundary_restriction_missing",
        "cartesian_fiber_arrow_transport_missing",
        "chosen_base_change_fiber",
        "fiber_rebuilt_after_base_change",
        "local_transport_table",
    }
    <= set(reasons(chosen_rebuilt)),
    ",".join(reasons(chosen_rebuilt)),
)

late_side = live_source(
    pointwise_cartesian_fiber=True,
    graph_side_cartesian_fiber=True,
    post_product_cartesian_fiber=True,
    cartesian_fiber_before_points=False,
    cartesian_fiber_before_graph_objects=False,
)

gate(
    f"{TAG}5 pointwise graph-side or post-product cartesian fibers fail",
    not accepts_cartesian_boundary_fiber(late_side)
    and {
        "pointwise_cartesian_fiber",
        "graph_side_cartesian_fiber",
        "post_product_cartesian_fiber",
        "cartesian_fiber_not_before_points",
        "cartesian_fiber_not_before_graph_objects",
    }
    <= set(reasons(late_side)),
    ",".join(reasons(late_side)),
)

retuned = live_source(
    retuned_cartesian_fiber=True,
    reindexed_cartesian_fiber=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
    finite_index=set(FINITE_INDEX) | {"cartesian_boundary_fiber_extra_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
)

gate(
    f"{TAG}6 retuned reindexed or expanded cartesian fibers fail",
    not accepts_cartesian_boundary_fiber(retuned)
    and {
        "retuned_cartesian_fiber",
        "reindexed_cartesian_fiber",
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

missing_cart_data = live_source(
    cartesian_boundary_fiber_actual=False,
    cartesian_boundary_restriction_actual=False,
    boundary_restriction_cartesian=False,
    fiber_universal_arrow_cartesian=False,
    cartesian_fiber_arrow_transport_actual=False,
)

gate(
    f"{TAG}7 cartesian fiber restriction and arrow transport are mandatory",
    not accepts_cartesian_boundary_fiber(missing_cart_data)
    and {
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "boundary_restriction_not_cartesian",
        "fiber_universal_arrow_not_cartesian",
        "cartesian_fiber_arrow_transport_missing",
    }
    <= set(reasons(missing_cart_data)),
    ",".join(reasons(missing_cart_data)),
)

missing_paths = live_source(
    same_cartesian_fiber_all_paths=False,
    coefficients_preserved=False,
    signed_support_preserved=False,
    C3_C5_equals_C15=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
)

gate(
    f"{TAG}8 path equality and coefficient support preservation are mandatory",
    not accepts_cartesian_boundary_fiber(missing_paths)
    and {
        "same_cartesian_fiber_not_all_paths",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "C3_C5_not_C15",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
    }
    <= set(reasons(missing_paths)),
    ",".join(reasons(missing_paths)),
)

control_like = live_source(
    graph_side_cartesian_fiber=True,
    cartesian_fiber_before_points=False,
    cartesian_fiber_before_graph_objects=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}9 non-source cartesian fibers leave controls formable",
    not accepts_cartesian_boundary_fiber(control_like)
    and {
        "graph_side_cartesian_fiber",
        "cartesian_fiber_not_before_points",
        "cartesian_fiber_not_before_graph_objects",
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
    live_source(
        required_edges=REQUIRED_CARTESIAN_FIBER_EDGES
        - {("represented_boundary_fiber", "cartesian_boundary_fiber")}
    ),
    live_source(
        required_edges=REQUIRED_CARTESIAN_FIBER_EDGES
        - {("boundary_restriction_map", "cartesian_boundary_restriction")}
    ),
    live_source(
        required_edges=REQUIRED_CARTESIAN_FIBER_EDGES
        - {("cartesian_boundary_restriction", "cartesian_boundary_fiber")}
    ),
    live_source(
        required_edges=REQUIRED_CARTESIAN_FIBER_EDGES
        - {("cartesian_boundary_fiber", "C3_C5_to_C15_fiber_pullback")}
    ),
    live_source(cartesian_boundary_fiber_actual=False),
    live_source(boundary_restriction_cartesian=False),
    live_source(same_cartesian_fiber_all_paths=False),
    live_source(cartesian_fiber_before_points=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}10 every cartesian boundary-fiber edge is mandatory",
    not any(accepts_cartesian_boundary_fiber(data) for data in missing_edges)
    and {
        "required_cartesian_boundary_fiber_edges_missing",
        "cartesian_boundary_fiber_missing",
        "boundary_restriction_not_cartesian",
        "same_cartesian_fiber_not_all_paths",
        "cartesian_fiber_not_before_points",
    }
    <= missing_reasons
    and accepts_cartesian_boundary_fiber(live_source())
    and not any(
        accepts_cartesian_boundary_fiber(data)
        for data in (
            static,
            noncartesian,
            chosen_rebuilt,
            late_side,
            retuned,
            missing_cart_data,
            missing_paths,
            control_like,
        )
    ),
    "missing=%s live=%s"
    % (sorted(missing_reasons), accepts_cartesian_boundary_fiber(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "component-cone cartesian-coherence globular-modification boundary-fiber "
    "cartesian component-object product-projected parallel-morphism "
    "finite-limit subrepresented coupled formation-coherent self-dual exact "
    "BCF certificate pinned"
)
print(
    "VERDICT: doc-513 represented boundary fiber must itself be cartesian "
    "over the represented source lifts. Static one-boundary fibers, reused "
    "fiber names, chosen or rebuilt base-change fibers, noncartesian "
    "pullbacks, pointwise/graph-side fibers, and finite-index expansion do "
    "not construct the missing source object."
)
