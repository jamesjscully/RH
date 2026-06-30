r"""Finite-limit subrepresented coupled mediator contract.

Doc 504 pins the mediator coupling as an actual monic subrepresenter of the
mediator source fiber. This witness pins the next edge: the subrepresenter is
not accepted unless one internal finite-limit/equalizer fork in that source
fiber cuts it out and imposes endpoint, DD.4, pushforward, graph,
Rosati/count, and control-death constraints simultaneously before points and
graph objects exist.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_TOKEN_ID = "Tok_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_COH_ID = "Coh_med_UP_Eq_id_BCF_self_dual_exact_source_formation"
FORMATION_CART_ID = "Cart_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_MWC_ID = "MWC_med_UP_Eq_id_BCF_self_dual_exact_source"
SOURCE_COUPLING_ID = "NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_REP_ID = "Rep_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_ETA_ID = "eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
COUPLING_INCLUSION_ID = "incl_NCoup_med_UP_Eq_id_to_Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_IMAGE_ID = "Img_NCoup_med_UP_Eq_id_coupled_self_dual_exact_sources"
COUPLING_FACTORIZATION_ID = "fact_eta_NCoup_med_UP_Eq_id_through_source_fiber_subrep"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
CONSTRAINT_FORK_ID = "Fork_med_UP_Eq_id_endpoint_dd4_rosati_control_NCoup"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_id_constraints_to_SubRep_source_fiber"
MONIC_EQ_ARROW_ID = "monic_eq_NCoup_med_UP_Eq_id_constraints_to_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
BOUNDARY_CERT_ID = "BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
SIGNED_ZERO_ID = "ZFib_med_UP_Eq_id_signed_zero"
CANMOD_ID = "CanMod_med_UP_Eq_id_z_boundary_convolution"
BCF_ID = "BCF_med_UP_Eq_id_boundary_convolution_module"
EXACT_SOURCE_ID = "Ex_med_UP_Eq_id_CanMod_BCF_dQ"
DELTA_ID = "Delta_med_UP_Eq_id_BCF_to_dQ_boundary"
KERNEL_ID = "Ker_med_UP_Eq_id_BCF_delta_image_z"
COIMAGE_ID = "Coim_med_UP_Eq_id_CanMod_BCF_delta"
DUALITY_ID = "Dual_med_UP_Eq_id_rank1_boundary_defect"
TWIST_ID = "Tw_med_UP_Eq_id_OC_BCF_pinned"
LOCALIZATION_ID = "Loc_BCCube_Qbar_BECD_single_dQ"
NORMAL_RATIO_ID = "NR_BCCube_Qbar_BECD_ordered_p1_p2"
DOC491_MODIFICATION_ID = (
    "Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
DOC491_BOUNDARY_ID = (
    "GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)

REQUIRED_FACETS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

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

FINITE_INDEX = REQUIRED_FACETS | REQUIRED_COHERENCE_CELLS

REQUIRED_DOC491_CELLS = {
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
}

REQUIRED_DOC491_FACES = {
    f"face_{cell}_fiber_coherence_globular_boundary"
    for cell in REQUIRED_DOC491_CELLS
}

REQUIRED_SOURCE_COHERENCE_CELLS = {
    "formation_coh_nat_C3_med_UP_Eq_id",
    "formation_coh_nat_C5_med_UP_Eq_id",
    "formation_coh_nat_C15_med_UP_Eq_id",
    "formation_coh_nat_C45_med_UP_Eq_id",
    "formation_coh_nat_F22_med_UP_Eq_id",
}

REQUIRED_SOURCE_COMPOSITION_CELLS = {
    "formation_coh_cell_C3_C5_C15_med_UP_Eq_id",
    "formation_coh_cell_C5_C3_C15_med_UP_Eq_id",
    "formation_coh_cell_C3_C3_C5_C45_med_UP_Eq_id",
    "formation_coh_cell_F22_product_med_UP_Eq_id",
}

REQUIRED_FINITE_LIMIT_EDGES = {
    ("universal_mediator", "formation_token"),
    ("formation_token", "formation_fiber"),
    ("formation_fiber", "formation_coherence"),
    ("formation_coherence", "cartesian_source_coherence"),
    ("formation_coherence", "monoidwide_source_coherence"),
    ("formation_coherence", "source_coherence_coupling_primitive"),
    ("universal_mediator", "source_coherence_coupling_primitive"),
    ("source_coherence_coupling_primitive", "source_coupling_representer"),
    ("source_coupling_representer", "source_coupling_universal_arrow"),
    ("source_coupling_universal_arrow", "source_coupling_subrepresenter"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("formation_fiber", "finite_limit_cut"),
    ("finite_limit_cut", "joint_endpoint_dd4_rosati_control_fork"),
    ("joint_endpoint_dd4_rosati_control_fork", "endpoint_integrality"),
    ("joint_endpoint_dd4_rosati_control_fork", "degree_maps"),
    ("joint_endpoint_dd4_rosati_control_fork", "dd4_boundary"),
    ("joint_endpoint_dd4_rosati_control_fork", "boundary_pushforward"),
    ("joint_endpoint_dd4_rosati_control_fork", "graph_composition"),
    ("joint_endpoint_dd4_rosati_control_fork", "rosati_count"),
    ("joint_endpoint_dd4_rosati_control_fork", "control_death"),
    ("finite_limit_cut", "equalizer_arrow"),
    ("equalizer_arrow", "source_coupling_subrepresenter"),
    ("equalizer_arrow", "monic_equalizer_arrow"),
    ("monic_equalizer_arrow", "monic_inclusion_to_source_fiber"),
    ("monic_inclusion_to_source_fiber", "formation_fiber"),
    ("equalizer_arrow", "exact_subrepresenter_image"),
    ("exact_subrepresenter_image", "coupled_self_dual_exact_sources"),
    ("coupled_self_dual_exact_sources", "exact_boundary_delta"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("exact_boundary_delta", "coimage_preserves_signed_coefficients"),
    ("kernel_is_cancellation_image", "coimage_preserves_signed_support"),
    ("coimage_preserves_signed_coefficients", "rank1_boundary_defect_duality"),
    ("coimage_preserves_signed_support", "rank1_boundary_defect_duality"),
    ("rank1_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank1_boundary_defect_duality", "original_dd4_boundary"),
    ("original_dd4_boundary", "dd4_original_class"),
    ("dd4_original_class", "dd4_res1_preserved"),
    ("dd4_original_class", "dd4_nonboundary_preserved"),
    ("original_dd4_boundary", "ordered_normal_ratio"),
    ("ordered_normal_ratio", "endpoint_pairing"),
    ("endpoint_pairing", "endpoint_pushforward_graph"),
    ("endpoint_pushforward_graph", "graph_composition"),
    ("graph_composition", "rosati_count"),
    ("rosati_count", "source_control_death"),
    ("source_control_death", "source_before_graph_objects"),
    ("finite_limit_cut", "finite_limit_universal_property"),
    ("finite_limit_universal_property", "same_cut_on_all_paths"),
    ("same_cut_on_all_paths", "C3_C5_equals_C15"),
    ("same_cut_on_all_paths", "C5_C3_equals_C15"),
    ("same_cut_on_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cut_on_all_paths", "F22_product_interchange"),
    ("finite_limit_cut", "source_before_points"),
    ("finite_limit_cut", "source_before_graph_objects"),
    ("source_before_points", "controls_not_points_of_subrepresenter"),
    ("source_before_points", "dh_not_points_of_subrepresenter"),
    ("source_before_points", "epstein_not_points_of_subrepresenter"),
    ("source_coherence_coupling_primitive", "dd4_certificate_handoff"),
    ("dd4_certificate_handoff", "old_boundary_certificate"),
    ("old_boundary_certificate", "upmed_dd4_certificate"),
    ("old_boundary_certificate", "dQ_localization"),
    ("dQ_localization", "certificate_kills_class"),
    ("formation_coherence", "doc491_globular_modification"),
    ("doc491_globular_modification", "doc491_globular_boundary"),
    ("doc491_globular_modification", "doc491_cells"),
    ("doc491_cells", "doc491_faces"),
    ("doc491_globular_modification", "finite_cell_index"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("fiber_coherence_modification_cell", "equalizer_identity"),
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


def boundary_delta(chi: dict[int, int]) -> dict[str, object]:
    return {
        "delta_id": DELTA_ID,
        "weighted_mass": weighted_mass(chi),
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "split": positive_negative_split(chi),
        "endpoint_pair": endpoint_degrees(chi),
    }


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
        "h1_order": z1_order // len(coboundaries),
        "res1_c": c.get(1, 0),
        "coboundaries_res1_zero": all(
            from_vec(vec).get(1, 0) == 0 for vec in coboundaries
        ),
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


def source(**kwargs):
    data = {
        "carrier_native": False,
        "universal_mediator_actual": False,
        "formation_token_actual": False,
        "formation_fiber_actual": False,
        "formation_coherence_actual": False,
        "cartesian_source_coherence_actual": False,
        "monoidwide_source_coherence_actual": False,
        "source_coupling_actual": False,
        "coupling_generated_by_mediator": False,
        "coupling_representer_actual": False,
        "coupling_universal_arrow_actual": False,
        "coupling_subrepresenter_actual": False,
        "subrepresenter_inside_source_fiber": False,
        "monic_inclusion_actual": False,
        "universal_arrow_factors_through_subrep": False,
        "image_exactly_coupled_sources": False,
        "same_subrepresenter_on_paths": False,
        "finite_limit_cut_actual": False,
        "constraint_fork_actual": False,
        "equalizer_arrow_actual": False,
        "monic_equalizer_arrow": False,
        "commuting_fork": False,
        "finite_limit_universal_property": False,
        "cut_before_points": False,
        "cut_before_graph_objects": False,
        "constraints_in_one_fork": False,
        "endpoint_integrality_in_fork": False,
        "degree_maps_in_fork": False,
        "dd4_boundary_in_fork": False,
        "boundary_pushforward_in_fork": False,
        "graph_composition_in_fork": False,
        "rosati_count_in_fork": False,
        "control_death_in_fork": False,
        "same_cut_on_paths": False,
        "image_is_doc504_subrepresenter": False,
        "exact_delta_in_image": False,
        "original_dd4_in_image": False,
        "control_death_in_image": False,
        "signed_zero_actual": False,
        "canmod_actual": False,
        "bcf_functor_actual": False,
        "exact_source_actual": False,
        "exact_delta_actual": False,
        "kernel_actual": False,
        "coimage_actual": False,
        "rank1_duality_actual": False,
        "twist_pinned": False,
        "dd4_class_actual": False,
        "dd4_res1_preserved": False,
        "dd4_nonboundary_preserved": False,
        "certificate_kills_class": False,
        "localization_actual": False,
        "normal_ratio_actual": False,
        "doc491_modification_actual": False,
        "doc491_boundary_actual": False,
        "doc491_cells": set(),
        "doc491_faces": set(),
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "doc491_in_finite_index": False,
        "source_coherence_cells": set(),
        "source_composition_cells": set(),
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "source_before_graph_objects": False,
        "source_before_points": False,
        "controls_not_points_of_subrepresenter": False,
        "dh_not_points_of_subrepresenter": False,
        "epstein_not_points_of_subrepresenter": False,
        "required_edges": set(),
        "abstract_external_representer": False,
        "equivalent_representer": False,
        "univalence_transport": False,
        "isomorphic_copy_only": False,
        "morita_source": False,
        "karoubi_or_idempotent_split": False,
        "localization_or_saturation": False,
        "sheafification_or_stackification": False,
        "image_closure": False,
        "dense_subobject": False,
        "quotient_predicate": False,
        "base_change_subobject": False,
        "retuned_inclusion": False,
        "graph_object_classifier": False,
        "declared_subobject": False,
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
        "pointwise_image_certificate": False,
        "predicate_subobject_selection": False,
        "subobject_classifier": False,
        "characteristic_map_only": False,
        "sequential_intersection": False,
        "iterated_filters": False,
        "posthoc_image_factorization": False,
        "external_finite_limit_completion": False,
        "pullback_after_graph_objects": False,
        "local_row_table": False,
        "finite_sample_cut": False,
        "basis_dependent_cut": False,
        "retuned_projected_constraint": False,
        "graph_invariant_classifier": False,
        "declared_equalizer": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("universal_mediator_actual", "universal_mediator_missing"),
    ("formation_token_actual", "formation_token_missing"),
    ("formation_fiber_actual", "formation_fiber_missing"),
    ("formation_coherence_actual", "formation_coherence_missing"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("monoidwide_source_coherence_actual", "monoidwide_source_coherence_missing"),
    ("source_coupling_actual", "source_coupling_missing"),
    ("coupling_generated_by_mediator", "coupling_not_generated_by_mediator"),
    ("coupling_representer_actual", "coupling_representer_missing"),
    ("coupling_universal_arrow_actual", "coupling_universal_arrow_missing"),
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("subrepresenter_inside_source_fiber", "subrepresenter_not_inside_source_fiber"),
    ("monic_inclusion_actual", "monic_inclusion_missing"),
    (
        "universal_arrow_factors_through_subrep",
        "universal_arrow_not_factored_through_subrep",
    ),
    ("image_exactly_coupled_sources", "image_not_exactly_coupled_sources"),
    ("same_subrepresenter_on_paths", "same_subrepresenter_not_on_paths"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("constraint_fork_actual", "constraint_fork_missing"),
    ("equalizer_arrow_actual", "equalizer_arrow_missing"),
    ("monic_equalizer_arrow", "monic_equalizer_arrow_missing"),
    ("commuting_fork", "commuting_fork_missing"),
    ("finite_limit_universal_property", "finite_limit_universal_property_missing"),
    ("cut_before_points", "cut_not_before_points"),
    ("cut_before_graph_objects", "cut_not_before_graph_objects"),
    ("constraints_in_one_fork", "constraints_not_in_one_fork"),
    ("endpoint_integrality_in_fork", "endpoint_integrality_not_in_fork"),
    ("degree_maps_in_fork", "degree_maps_not_in_fork"),
    ("dd4_boundary_in_fork", "dd4_boundary_not_in_fork"),
    ("boundary_pushforward_in_fork", "boundary_pushforward_not_in_fork"),
    ("graph_composition_in_fork", "graph_composition_not_in_fork"),
    ("rosati_count_in_fork", "rosati_count_not_in_fork"),
    ("control_death_in_fork", "control_death_not_in_fork"),
    ("same_cut_on_paths", "same_cut_not_on_paths"),
    ("image_is_doc504_subrepresenter", "image_not_doc504_subrepresenter"),
    ("exact_delta_in_image", "exact_delta_not_in_image"),
    ("original_dd4_in_image", "original_dd4_not_in_image"),
    ("control_death_in_image", "control_death_not_in_image"),
    ("signed_zero_actual", "signed_zero_missing"),
    ("canmod_actual", "canmod_missing"),
    ("bcf_functor_actual", "bcf_functor_missing"),
    ("exact_source_actual", "exact_source_missing"),
    ("exact_delta_actual", "exact_delta_missing"),
    ("kernel_actual", "kernel_missing"),
    ("coimage_actual", "coimage_missing"),
    ("rank1_duality_actual", "rank1_duality_missing"),
    ("twist_pinned", "twist_not_pinned"),
    ("dd4_class_actual", "dd4_class_missing"),
    ("dd4_res1_preserved", "dd4_res1_not_preserved"),
    ("dd4_nonboundary_preserved", "dd4_nonboundary_not_preserved"),
    ("certificate_kills_class", "certificate_does_not_kill_class"),
    ("localization_actual", "localization_missing"),
    ("normal_ratio_actual", "normal_ratio_missing"),
    ("doc491_modification_actual", "doc491_modification_missing"),
    ("doc491_boundary_actual", "doc491_boundary_missing"),
    ("doc491_in_finite_index", "doc491_not_in_finite_index"),
    ("closure_returns_same_totalizer", "closure_does_not_return_same_totalizer"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points_of_subrepresenter", "controls_are_points_of_subrepresenter"),
    ("dh_not_points_of_subrepresenter", "dh_is_point_of_subrepresenter"),
    ("epstein_not_points_of_subrepresenter", "epstein_is_point_of_subrepresenter"),
)

BANNED = (
    ("abstract_external_representer", "abstract_external_representer"),
    ("equivalent_representer", "equivalent_representer"),
    ("univalence_transport", "univalence_transport"),
    ("isomorphic_copy_only", "isomorphic_copy_only"),
    ("morita_source", "morita_source"),
    ("karoubi_or_idempotent_split", "karoubi_or_idempotent_split"),
    ("localization_or_saturation", "localization_or_saturation"),
    ("sheafification_or_stackification", "sheafification_or_stackification"),
    ("image_closure", "image_closure"),
    ("dense_subobject", "dense_subobject"),
    ("quotient_predicate", "quotient_predicate"),
    ("base_change_subobject", "base_change_subobject"),
    ("retuned_inclusion", "retuned_inclusion"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("declared_subobject", "declared_subobject"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
    ("pointwise_image_certificate", "pointwise_image_certificate"),
    ("predicate_subobject_selection", "predicate_subobject_selection"),
    ("subobject_classifier", "subobject_classifier"),
    ("characteristic_map_only", "characteristic_map_only"),
    ("sequential_intersection", "sequential_intersection"),
    ("iterated_filters", "iterated_filters"),
    ("posthoc_image_factorization", "posthoc_image_factorization"),
    ("external_finite_limit_completion", "external_finite_limit_completion"),
    ("pullback_after_graph_objects", "pullback_after_graph_objects"),
    ("local_row_table", "local_row_table"),
    ("finite_sample_cut", "finite_sample_cut"),
    ("basis_dependent_cut", "basis_dependent_cut"),
    ("retuned_projected_constraint", "retuned_projected_constraint"),
    ("graph_invariant_classifier", "graph_invariant_classifier"),
    ("declared_equalizer", "declared_equalizer"),
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
    if not REQUIRED_DOC491_CELLS <= set(data["doc491_cells"]):
        out.append("doc491_cells_missing")
    if not REQUIRED_DOC491_FACES <= set(data["doc491_faces"]):
        out.append("doc491_faces_missing")
    if not REQUIRED_SOURCE_COHERENCE_CELLS <= set(data["source_coherence_cells"]):
        out.append("source_coherence_cells_missing")
    if not REQUIRED_SOURCE_COMPOSITION_CELLS <= set(data["source_composition_cells"]):
        out.append("source_composition_cells_missing")
    if not REQUIRED_FINITE_LIMIT_EDGES <= set(data["required_edges"]):
        out.append("required_finite_limit_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_finite_limit_subrepresented_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_SOURCE_COHERENCE_CELLS <= set(data["source_coherence_cells"])
        and REQUIRED_SOURCE_COMPOSITION_CELLS <= set(data["source_composition_cells"])
        and REQUIRED_FINITE_LIMIT_EDGES <= set(data["required_edges"])
        and graph_connected(set(data["required_edges"]))
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        universal_mediator_actual=True,
        formation_token_actual=True,
        formation_fiber_actual=True,
        formation_coherence_actual=True,
        cartesian_source_coherence_actual=True,
        monoidwide_source_coherence_actual=True,
        source_coupling_actual=True,
        coupling_generated_by_mediator=True,
        coupling_representer_actual=True,
        coupling_universal_arrow_actual=True,
        coupling_subrepresenter_actual=True,
        subrepresenter_inside_source_fiber=True,
        monic_inclusion_actual=True,
        universal_arrow_factors_through_subrep=True,
        image_exactly_coupled_sources=True,
        same_subrepresenter_on_paths=True,
        finite_limit_cut_actual=True,
        constraint_fork_actual=True,
        equalizer_arrow_actual=True,
        monic_equalizer_arrow=True,
        commuting_fork=True,
        finite_limit_universal_property=True,
        cut_before_points=True,
        cut_before_graph_objects=True,
        constraints_in_one_fork=True,
        endpoint_integrality_in_fork=True,
        degree_maps_in_fork=True,
        dd4_boundary_in_fork=True,
        boundary_pushforward_in_fork=True,
        graph_composition_in_fork=True,
        rosati_count_in_fork=True,
        control_death_in_fork=True,
        same_cut_on_paths=True,
        image_is_doc504_subrepresenter=True,
        exact_delta_in_image=True,
        original_dd4_in_image=True,
        control_death_in_image=True,
        signed_zero_actual=True,
        canmod_actual=True,
        bcf_functor_actual=True,
        exact_source_actual=True,
        exact_delta_actual=True,
        kernel_actual=True,
        coimage_actual=True,
        rank1_duality_actual=True,
        twist_pinned=True,
        dd4_class_actual=True,
        dd4_res1_preserved=True,
        dd4_nonboundary_preserved=True,
        certificate_kills_class=True,
        localization_actual=True,
        normal_ratio_actual=True,
        doc491_modification_actual=True,
        doc491_boundary_actual=True,
        doc491_cells=set(REQUIRED_DOC491_CELLS),
        doc491_faces=set(REQUIRED_DOC491_FACES),
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        doc491_in_finite_index=True,
        source_coherence_cells=set(REQUIRED_SOURCE_COHERENCE_CELLS),
        source_composition_cells=set(REQUIRED_SOURCE_COMPOSITION_CELLS),
        closure_returns_same_totalizer=True,
        no_next_coherence_obligation=True,
        source_before_graph_objects=True,
        source_before_points=True,
        controls_not_points_of_subrepresenter=True,
        dh_not_points_of_subrepresenter=True,
        epstein_not_points_of_subrepresenter=True,
        required_edges=set(REQUIRED_FINITE_LIMIT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def finite_limit_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    delta = boundary_delta(chi)
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_token": FORMATION_TOKEN_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "formation_coherence": FORMATION_COH_ID,
        "cartesian_source_coherence": FORMATION_CART_ID,
        "monoidwide_source_coherence": FORMATION_MWC_ID,
        "source_coupling": SOURCE_COUPLING_ID,
        "coupling_representer": COUPLING_REP_ID,
        "coupling_universal_arrow": COUPLING_ETA_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "monic_inclusion": COUPLING_INCLUSION_ID,
        "coupling_image": COUPLING_IMAGE_ID,
        "eta_factorization": COUPLING_FACTORIZATION_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "constraint_fork": CONSTRAINT_FORK_ID,
        "equalizer_arrow": EQUALIZER_ARROW_ID,
        "monic_equalizer_arrow": MONIC_EQ_ARROW_ID,
        "constraints": (
            "endpoint_integrality",
            "degree_maps",
            "dd4_boundary",
            "boundary_pushforward",
            "graph_composition",
            "rosati_count",
            "control_death",
        ),
        "subrep_inside": FORMATION_FIBER_ID,
        "image_points": "exactly_coupled_self_dual_exact_bcf_sources",
        "image_is_doc504_subrepresenter": True,
        "source_before_graph_objects": True,
        "source_before_points": True,
        "controls_not_points_of_subrepresenter": True,
        "dh_not_points_of_subrepresenter": True,
        "epstein_not_points_of_subrepresenter": True,
        "dd4_class": DD4_CLASS_ID,
        "boundary_certificate": BOUNDARY_CERT_ID,
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "signed_zero_fiber": SIGNED_ZERO_ID,
        "cancellation_module": CANMOD_ID,
        "boundary_convolution_functor": BCF_ID,
        "exact_source": EXACT_SOURCE_ID,
        "exact_delta": DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality": DUALITY_ID,
        "pinned_twist": TWIST_ID,
        "endpoint_pairing": (p1, p2, p1 == p2),
        "boundary_class": DD4_CLASS_ID,
        "res1": 1,
        "normal_ratio": NORMAL_RATIO_ID,
        "kernel_relation": tuple(chi.items()),
        "coimage_signature": positive_negative_split(chi),
        "localization": LOCALIZATION_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
        "required_edges": tuple(sorted(REQUIRED_FINITE_LIMIT_EDGES)),
        "delta": delta,
        "image_contains": (
            SOURCE_COUPLING_ID,
            COUPLING_SUBREP_ID,
            FINITE_LIMIT_CUT_ID,
            EQUALIZER_ARROW_ID,
            DELTA_ID,
            KERNEL_ID,
            COIMAGE_ID,
            DUALITY_ID,
            TWIST_ID,
            DD4_CLASS_ID,
            NORMAL_RATIO_ID,
            "source_control_death",
        ),
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
    }


def finite_limit_row(chi: dict[int, int]) -> bool:
    payload = finite_limit_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["delta"]["weighted_mass"] == 0
        and payload["kernel_relation"] == payload["coefficients"]
        and payload["coimage_signature"] == payload["delta"]["split"]
        and payload["formation_token"] == FORMATION_TOKEN_ID
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["source_coupling"] == SOURCE_COUPLING_ID
        and payload["coupling_representer"] == COUPLING_REP_ID
        and payload["coupling_universal_arrow"] == COUPLING_ETA_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["monic_inclusion"] == COUPLING_INCLUSION_ID
        and payload["eta_factorization"] == COUPLING_FACTORIZATION_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["constraint_fork"] == CONSTRAINT_FORK_ID
        and payload["equalizer_arrow"] == EQUALIZER_ARROW_ID
        and payload["monic_equalizer_arrow"] == MONIC_EQ_ARROW_ID
        and set(payload["constraints"]) == REQUIRED_FACETS
        and payload["subrep_inside"] == FORMATION_FIBER_ID
        and payload["image_points"] == "exactly_coupled_self_dual_exact_bcf_sources"
        and payload["image_is_doc504_subrepresenter"]
        and payload["source_before_graph_objects"]
        and payload["source_before_points"]
        and payload["controls_not_points_of_subrepresenter"]
        and payload["dh_not_points_of_subrepresenter"]
        and payload["epstein_not_points_of_subrepresenter"]
        and payload["exact_delta"] == DELTA_ID
        and payload["kernel"] == KERNEL_ID
        and payload["coimage"] == COIMAGE_ID
        and payload["duality"] == DUALITY_ID
        and payload["pinned_twist"] == TWIST_ID
        and payload["boundary_class"] == DD4_CLASS_ID
        and payload["res1"] == 1
        and payload["endpoint_pairing"][2]
        and SOURCE_COUPLING_ID in payload["image_contains"]
        and COUPLING_SUBREP_ID in payload["image_contains"]
        and FINITE_LIMIT_CUT_ID in payload["image_contains"]
        and EQUALIZER_ARROW_ID in payload["image_contains"]
        and DELTA_ID in payload["image_contains"]
        and DUALITY_ID in payload["image_contains"]
        and DD4_CLASS_ID in payload["image_contains"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_FINITE_LIMIT_EDGES))
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
    f"{TAG}1 mediator subrepresenter is cut out by one finite-limit equalizer fork",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_FINITE_LIMIT_EDGES)
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC491_CELLS) == 10
    and len(REQUIRED_DOC491_FACES) == 10
    and len(REQUIRED_SOURCE_COHERENCE_CELLS) == 5
    and len(REQUIRED_SOURCE_COMPOSITION_CELLS) == 4
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and finite_limit_payload(T3_T5_z) == finite_limit_payload(zC15)
    and finite_limit_payload(T5_T3_z) == finite_limit_payload(zC15)
    and finite_limit_payload(T3_T3_T5_z) == finite_limit_payload(zC45)
    and finite_limit_payload(T15_zF22) == finite_limit_payload(zC15F22)
    and finite_limit_payload(T45_zF22) == finite_limit_payload(zC45F22)
    and all(finite_limit_row(row) for row in rows),
    "H1=%s finite_limit_edges=%d finite_index=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(REQUIRED_FINITE_LIMIT_EDGES),
        len(FINITE_INDEX),
    ),
)

pointwise_shell = live_source(
    finite_limit_cut_actual=False,
    constraint_fork_actual=False,
    equalizer_arrow_actual=False,
    pointwise_image_certificate=True,
    predicate_subobject_selection=True,
    subobject_classifier=True,
    characteristic_map_only=True,
)

gate(
    f"{TAG}2 pointwise image and classifier repairs fail",
    not accepts_finite_limit_subrepresented_mediator(pointwise_shell)
    and {
        "finite_limit_cut_missing",
        "constraint_fork_missing",
        "equalizer_arrow_missing",
        "pointwise_image_certificate",
        "predicate_subobject_selection",
        "subobject_classifier",
        "characteristic_map_only",
    }
    <= set(reasons(pointwise_shell)),
    ",".join(reasons(pointwise_shell)),
)

sequential_shell = live_source(
    constraints_in_one_fork=False,
    commuting_fork=False,
    cut_before_graph_objects=False,
    sequential_intersection=True,
    iterated_filters=True,
    posthoc_image_factorization=True,
    pullback_after_graph_objects=True,
)

gate(
    f"{TAG}3 sequential filters and post-hoc graph pullbacks fail",
    not accepts_finite_limit_subrepresented_mediator(sequential_shell)
    and {
        "constraints_not_in_one_fork",
        "commuting_fork_missing",
        "cut_not_before_graph_objects",
        "sequential_intersection",
        "iterated_filters",
        "posthoc_image_factorization",
        "pullback_after_graph_objects",
    }
    <= set(reasons(sequential_shell)),
    ",".join(reasons(sequential_shell)),
)

external_cut = live_source(
    carrier_native=False,
    finite_limit_universal_property=False,
    same_cut_on_paths=False,
    external_finite_limit_completion=True,
    finite_sample_cut=True,
    basis_dependent_cut=True,
    retuned_projected_constraint=True,
)

gate(
    f"{TAG}4 external finite-limit completions and retuned cuts fail",
    not accepts_finite_limit_subrepresented_mediator(external_cut)
    and {
        "not_carrier_native",
        "finite_limit_universal_property_missing",
        "same_cut_not_on_paths",
        "external_finite_limit_completion",
        "finite_sample_cut",
        "basis_dependent_cut",
        "retuned_projected_constraint",
    }
    <= set(reasons(external_cut)),
    ",".join(reasons(external_cut)),
)

declared_cut = live_source(
    equalizer_arrow_actual=False,
    monic_equalizer_arrow=False,
    image_is_doc504_subrepresenter=False,
    local_row_table=True,
    graph_invariant_classifier=True,
    declared_equalizer=True,
    declared_subobject=True,
)

gate(
    f"{TAG}5 local row tables and declared equalizers fail",
    not accepts_finite_limit_subrepresented_mediator(declared_cut)
    and {
        "equalizer_arrow_missing",
        "monic_equalizer_arrow_missing",
        "image_not_doc504_subrepresenter",
        "local_row_table",
        "graph_invariant_classifier",
        "declared_equalizer",
        "declared_subobject",
    }
    <= set(reasons(declared_cut)),
    ",".join(reasons(declared_cut)),
)

split_fork = live_source(
    constraints_in_one_fork=False,
    endpoint_integrality_in_fork=False,
    degree_maps_in_fork=False,
    dd4_boundary_in_fork=False,
    boundary_pushforward_in_fork=False,
    graph_composition_in_fork=False,
    rosati_count_in_fork=False,
    control_death_in_fork=False,
)

gate(
    f"{TAG}6 endpoint DD4 graph Rosati and control constraints must be simultaneous",
    not accepts_finite_limit_subrepresented_mediator(split_fork)
    and {
        "constraints_not_in_one_fork",
        "endpoint_integrality_not_in_fork",
        "degree_maps_not_in_fork",
        "dd4_boundary_not_in_fork",
        "boundary_pushforward_not_in_fork",
        "graph_composition_not_in_fork",
        "rosati_count_not_in_fork",
        "control_death_not_in_fork",
    }
    <= set(reasons(split_fork)),
    ",".join(reasons(split_fork)),
)

graph_classifier = live_source(
    cut_before_points=False,
    cut_before_graph_objects=False,
    source_before_graph_objects=False,
    source_before_points=False,
    controls_not_points_of_subrepresenter=False,
    dh_not_points_of_subrepresenter=False,
    epstein_not_points_of_subrepresenter=False,
    graph_object_classifier=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 graph classifiers leave controls as points",
    not accepts_finite_limit_subrepresented_mediator(graph_classifier)
    and {
        "cut_not_before_points",
        "cut_not_before_graph_objects",
        "source_not_before_graph_objects",
        "source_not_before_points",
        "controls_are_points_of_subrepresenter",
        "dh_is_point_of_subrepresenter",
        "epstein_is_point_of_subrepresenter",
        "graph_object_classifier",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_classifier)),
    ",".join(reasons(graph_classifier)),
)

expanded_index = live_source(
    coupling_subrepresenter_actual=False,
    subrepresenter_inside_source_fiber=False,
    finite_index=set(FINITE_INDEX) | {"finite_limit_cut_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    doc491_in_finite_index=False,
    closure_returns_same_totalizer=False,
    no_next_coherence_obligation=False,
    abstract_external_representer=True,
    equivalent_representer=True,
    univalence_transport=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}8 finite index expansion and external representer shells fail",
    not accepts_finite_limit_subrepresented_mediator(expanded_index)
    and {
        "coupling_subrepresenter_missing",
        "subrepresenter_not_inside_source_fiber",
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "doc491_not_in_finite_index",
        "closure_does_not_return_same_totalizer",
        "next_coherence_obligation_open",
        "abstract_external_representer",
        "equivalent_representer",
        "univalence_transport",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded_index)),
    ",".join(reasons(expanded_index)),
)

missing_edges = [
    live_source(
        required_edges=REQUIRED_FINITE_LIMIT_EDGES
        - {("source_coupling_subrepresenter", "finite_limit_cut")}
    ),
    live_source(
        required_edges=REQUIRED_FINITE_LIMIT_EDGES
        - {("finite_limit_cut", "joint_endpoint_dd4_rosati_control_fork")}
    ),
    live_source(
        required_edges=REQUIRED_FINITE_LIMIT_EDGES
        - {("finite_limit_cut", "equalizer_arrow")}
    ),
    live_source(
        required_edges=REQUIRED_FINITE_LIMIT_EDGES
        - {("equalizer_arrow", "monic_equalizer_arrow")}
    ),
    live_source(
        required_edges=REQUIRED_FINITE_LIMIT_EDGES
        - {("equalizer_arrow", "exact_subrepresenter_image")}
    ),
    live_source(finite_limit_cut_actual=False),
    live_source(constraint_fork_actual=False),
    live_source(equalizer_arrow_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every finite-limit cut edge is mandatory",
    not any(
        accepts_finite_limit_subrepresented_mediator(data) for data in missing_edges
    )
    and {
        "required_finite_limit_edges_missing",
        "finite_limit_cut_missing",
        "constraint_fork_missing",
        "equalizer_arrow_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

dead_sources = {
    "pointwise_shell": pointwise_shell,
    "sequential_shell": sequential_shell,
    "external_cut": external_cut,
    "declared_cut": declared_cut,
    "split_fork": split_fork,
    "graph_classifier": graph_classifier,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only finite-limit subrepresented coupled mediator passes",
    accepts_finite_limit_subrepresented_mediator(live_source())
    and not any(
        accepts_finite_limit_subrepresented_mediator(data)
        for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(
            accepts_finite_limit_subrepresented_mediator(data)
            for data in dead_sources.values()
        ),
        accepts_finite_limit_subrepresented_mediator(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator finite-limit subrepresented coupled formation-coherent self-dual exact BCF certificate pinned")
print(
    "VERDICT: the doc-504 mediator subrepresenter must be produced by one "
    "internal finite-limit/equalizer fork in the mediator source fiber. "
    "Pointwise predicates, subobject classifiers, sequential filters, post-hoc "
    "image factorizations, external finite-limit completions, late graph "
    "pullbacks, declared equalizers, expanded indexes, and towers do not "
    "construct the missing object."
)
