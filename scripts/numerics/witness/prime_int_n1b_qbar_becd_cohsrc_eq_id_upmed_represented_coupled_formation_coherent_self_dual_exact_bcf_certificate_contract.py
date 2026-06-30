r"""Represented coupled formation-coherent self-dual exact-BCF mediator contract.

Doc 502 requires one non-split source-coherence coupling primitive generated
by the equalizer-identity universal mediator. This witness pins the next
edge: the coupling graph is not itself the source object. The coupling must
be represented by an actual mediator-side source object and universal arrow
whose points are exactly the coupled self-dual exact BCF sources.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_represented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

SOURCE_CATEGORY_ID = "SrcCat_BCCube_Qbar_BECD"
PRODUCT_ID = "Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells"
ALPHA_ID = "alpha_CohSrcPres_BCCube_Qbar_BECD_constraints"
BETA_ID = "beta_CohSrcPres_BCCube_Qbar_BECD_constraints"
EQUALIZER_ID = "Eq_CohSrcPres_BCCube_Qbar_BECD"
EQUALIZER_IDENTITY_ID = "id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FINITE_LIMIT_UP_ID = "UP_Eq_CohSrcPres_BCCube_Qbar_BECD_finite_limit"
UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
UPMED_NATURALITY_ID = "Nat_med_UP_Eq_CohSrcPres_id_multiplier_action"
UPMED_COMPOSITION_ID = "Comp_Nat_med_UP_Eq_CohSrcPres_id_C3_C5_C15_C45_F22"
FORMATION_TOKEN_ID = "Tok_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_COH_ID = "Coh_med_UP_Eq_id_BCF_self_dual_exact_source_formation"
FORMATION_CART_ID = "Cart_med_UP_Eq_id_BCF_self_dual_exact_source"
FORMATION_MWC_ID = "MWC_med_UP_Eq_id_BCF_self_dual_exact_source"
SOURCE_COUPLING_ID = "NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_REP_ID = "Rep_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_ETA_ID = "eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
BOUNDARY_CERT_ID = "BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
UPMED_DD4_NAT_ID = "Nat_Cert_med_UP_Eq_CohSrcPres_id_DD4_multiplier_action"
UPMED_DD4_HANDOFF_ID = "Handoff_BKill_to_med_UP_Eq_id_DD4_certificate"
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
FINITE_INDEX_ID = "FinIdx_CohSrcPres_BCCube_Qbar_BECD"
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

REQUIRED_REPRESENTABILITY_EDGES = {
    ("source_category", "product_facets_cells"),
    ("product_facets_cells", "alpha_constraints"),
    ("product_facets_cells", "beta_constraints"),
    ("alpha_constraints", "equalizer_object"),
    ("beta_constraints", "equalizer_object"),
    ("equalizer_object", "finite_limit_universal_property"),
    ("finite_limit_universal_property", "universal_mediator"),
    ("universal_mediator", "equalizer_identity"),
    ("universal_mediator", "upmed_multiplier_naturality"),
    ("upmed_multiplier_naturality", "upmed_composition_coherence"),
    ("upmed_composition_coherence", "path_independent_mediator"),
    ("path_independent_mediator", "formation_token"),
    ("universal_mediator", "formation_token"),
    ("formation_token", "formation_fiber"),
    ("formation_fiber", "formation_coherence"),
    ("formation_coherence", "source_coherence_coupling_primitive"),
    ("universal_mediator", "source_coherence_coupling_primitive"),
    ("universal_mediator", "source_coupling_representing_object"),
    ("formation_coherence", "source_coupling_representing_object"),
    ("source_coherence_coupling_primitive", "source_coupling_representing_object"),
    ("source_coupling_representing_object", "source_coupling_universal_arrow"),
    ("source_coupling_universal_arrow", "source_coherence_coupling_primitive"),
    ("source_coupling_universal_arrow", "represented_coupled_source_points"),
    ("represented_coupled_source_points", "formation_token"),
    ("represented_coupled_source_points", "formation_fiber"),
    ("represented_coupled_source_points", "formation_coherence"),
    ("represented_coupled_source_points", "cartesian_source_coherence"),
    ("represented_coupled_source_points", "monoidwide_source_coherence"),
    ("source_coherence_coupling_primitive", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_functor"),
    ("boundary_convolution_functor", "exact_source"),
    ("exact_source", "exact_boundary_delta"),
    ("source_coherence_coupling_primitive", "exact_boundary_delta"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("exact_boundary_delta", "coimage_preserves_signed_coefficients"),
    ("kernel_is_cancellation_image", "coimage_preserves_signed_support"),
    ("coimage_preserves_signed_coefficients", "rank1_boundary_defect_duality"),
    ("coimage_preserves_signed_support", "rank1_boundary_defect_duality"),
    ("rank1_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank1_boundary_defect_duality", "original_dd4_boundary"),
    ("rank1_boundary_defect_duality", "endpoint_pairing"),
    ("rank1_boundary_defect_duality", "rosati_compatible_duality"),
    ("original_dd4_boundary", "dd4_original_class"),
    ("dd4_original_class", "dd4_res1_preserved"),
    ("dd4_original_class", "dd4_nonboundary_preserved"),
    ("original_dd4_boundary", "ordered_normal_ratio"),
    ("ordered_normal_ratio", "normal_ratio_self_dual_boundary"),
    ("normal_ratio_self_dual_boundary", "endpoint_pairing"),
    ("endpoint_pairing", "endpoint_pushforward_graph"),
    ("endpoint_pushforward_graph", "rosati_count"),
    ("rosati_count", "source_control_death"),
    ("source_control_death", "source_before_graph_objects"),
    ("source_coupling_representing_object", "source_before_graph_objects"),
    ("source_before_graph_objects", "controls_not_points_of_representer"),
    ("source_before_graph_objects", "dh_not_points_of_representer"),
    ("source_before_graph_objects", "epstein_not_points_of_representer"),
    ("source_coherence_coupling_primitive", "dd4_certificate_handoff"),
    ("dd4_certificate_handoff", "old_boundary_certificate"),
    ("old_boundary_certificate", "upmed_dd4_certificate"),
    ("upmed_dd4_certificate", "upmed_dd4_naturality"),
    ("old_boundary_certificate", "dQ_localization"),
    ("dQ_localization", "certificate_kills_class"),
    ("cartesian_source_coherence", "C3_C5_equals_C15"),
    ("cartesian_source_coherence", "C5_C3_equals_C15"),
    ("monoidwide_source_coherence", "C3_C3_C5_equals_C45"),
    ("monoidwide_source_coherence", "F22_product_interchange"),
    ("doc491_globular_modification", "doc491_globular_boundary"),
    ("doc491_globular_modification", "doc491_cells"),
    ("doc491_cells", "doc491_faces"),
    ("doc491_globular_modification", "finite_cell_index"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("fiber_coherence_modification_cell", "equalizer_identity"),
    ("finite_cell_index", "source_before_points"),
    ("source_before_points", "controls_not_points_of_representer"),
    ("source_before_points", "dh_not_points_of_representer"),
    ("source_before_points", "epstein_not_points_of_representer"),
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
        "source_category_actual": False,
        "product_actual": False,
        "alpha_actual": False,
        "beta_actual": False,
        "equalizer_actual": False,
        "universal_mediator_actual": False,
        "multiplier_naturality_actual": False,
        "path_independent_mediator": False,
        "formation_token_actual": False,
        "formation_fiber_actual": False,
        "formation_generated_by_mediator": False,
        "formation_coherence_actual": False,
        "coherence_generated_by_mediator": False,
        "cartesian_source_coherence_actual": False,
        "monoidwide_source_coherence_actual": False,
        "source_coupling_actual": False,
        "coupling_generated_by_mediator": False,
        "coupling_generated_by_formation_coherence": False,
        "non_split_dependency_graph": False,
        "same_coupling_on_paths": False,
        "coupling_representer_actual": False,
        "coupling_universal_arrow_actual": False,
        "coupling_functor_represented": False,
        "coupling_generated_by_representer": False,
        "representer_points_exactly_coupled_sources": False,
        "exact_delta_coupled": False,
        "kernel_coimage_coupled": False,
        "signed_coefficients_coupled": False,
        "signed_support_coupled": False,
        "rank1_duality_coupled": False,
        "pinned_twist_coupled": False,
        "original_dd4_coupled": False,
        "normal_ratio_coupled": False,
        "endpoint_pairing_coupled": False,
        "endpoint_pushforward_graph_coupled": False,
        "rosati_count_coupled": False,
        "control_death_coupled": False,
        "dd4_certificate_handoff_actual": False,
        "old_boundary_certificate_actual": False,
        "upmed_dd4_certificate_actual": False,
        "upmed_dd4_naturality_actual": False,
        "signed_zero_actual": False,
        "canmod_actual": False,
        "bcf_functor_actual": False,
        "exact_source_actual": False,
        "exact_delta_actual": False,
        "kernel_actual": False,
        "coimage_actual": False,
        "exact_sequence_generated_by_bcf": False,
        "kernel_is_canmod_image": False,
        "coimage_preserves_signed_coefficients": False,
        "coimage_preserves_signed_support": False,
        "rank1_duality_actual": False,
        "duality_generated_by_delta": False,
        "twist_pinned": False,
        "duality_boundary_is_dd4_class": False,
        "dual_to_primal_boundary_line": False,
        "p1_p2_dual_endpoint_pairing": False,
        "bidual_fixed": False,
        "rosati_compatible_duality": False,
        "normal_ratio_self_dual_boundary": False,
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
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "controls_not_points_of_representer": False,
        "dh_not_points_of_representer": False,
        "epstein_not_points_of_representer": False,
        "required_edges": set(),
        "connected_dependency_graph_only": False,
        "nerve_or_segal_completion": False,
        "functor_of_points_without_representer": False,
        "yoneda_reversal": False,
        "grothendieck_or_category_of_elements": False,
        "formal_universal_property": False,
        "limit_cone_or_comma_label": False,
        "free_operad_completion": False,
        "collage_or_proarrow_equipment": False,
        "codescent_or_descent_label": False,
        "rezk_completion": False,
        "local_representer_table": False,
        "external_choice_representer": False,
        "retuned_representer": False,
        "product_or_pullback_representer": False,
        "graph_object_classifier": False,
        "semantic_zeta_label": False,
        "declared_representer": False,
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
    ("source_category_actual", "source_category_missing"),
    ("product_actual", "product_missing"),
    ("alpha_actual", "alpha_missing"),
    ("beta_actual", "beta_missing"),
    ("equalizer_actual", "equalizer_missing"),
    ("universal_mediator_actual", "universal_mediator_missing"),
    ("multiplier_naturality_actual", "multiplier_naturality_missing"),
    ("path_independent_mediator", "mediator_not_path_independent"),
    ("formation_token_actual", "formation_token_missing"),
    ("formation_fiber_actual", "formation_fiber_missing"),
    ("formation_generated_by_mediator", "formation_not_generated_by_mediator"),
    ("formation_coherence_actual", "formation_coherence_missing"),
    ("coherence_generated_by_mediator", "coherence_not_generated_by_mediator"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("monoidwide_source_coherence_actual", "monoidwide_source_coherence_missing"),
    ("source_coupling_actual", "source_coupling_missing"),
    ("coupling_generated_by_mediator", "coupling_not_generated_by_mediator"),
    (
        "coupling_generated_by_formation_coherence",
        "coupling_not_generated_by_formation_coherence",
    ),
    ("non_split_dependency_graph", "dependency_graph_split"),
    ("same_coupling_on_paths", "same_coupling_not_on_paths"),
    ("coupling_representer_actual", "coupling_representer_missing"),
    ("coupling_universal_arrow_actual", "coupling_universal_arrow_missing"),
    ("coupling_functor_represented", "coupling_functor_not_represented"),
    ("coupling_generated_by_representer", "coupling_not_generated_by_representer"),
    (
        "representer_points_exactly_coupled_sources",
        "representer_points_not_exactly_coupled_sources",
    ),
    ("exact_delta_coupled", "exact_delta_not_coupled"),
    ("kernel_coimage_coupled", "kernel_coimage_not_coupled"),
    ("signed_coefficients_coupled", "signed_coefficients_not_coupled"),
    ("signed_support_coupled", "signed_support_not_coupled"),
    ("rank1_duality_coupled", "rank1_duality_not_coupled"),
    ("pinned_twist_coupled", "pinned_twist_not_coupled"),
    ("original_dd4_coupled", "original_dd4_not_coupled"),
    ("normal_ratio_coupled", "normal_ratio_not_coupled"),
    ("endpoint_pairing_coupled", "endpoint_pairing_not_coupled"),
    (
        "endpoint_pushforward_graph_coupled",
        "endpoint_pushforward_graph_not_coupled",
    ),
    ("rosati_count_coupled", "rosati_count_not_coupled"),
    ("control_death_coupled", "control_death_not_coupled"),
    ("dd4_certificate_handoff_actual", "dd4_certificate_handoff_missing"),
    ("old_boundary_certificate_actual", "old_boundary_certificate_missing"),
    ("upmed_dd4_certificate_actual", "upmed_dd4_certificate_missing"),
    ("upmed_dd4_naturality_actual", "upmed_dd4_naturality_missing"),
    ("signed_zero_actual", "signed_zero_missing"),
    ("canmod_actual", "canmod_missing"),
    ("bcf_functor_actual", "bcf_functor_missing"),
    ("exact_source_actual", "exact_source_missing"),
    ("exact_delta_actual", "exact_delta_missing"),
    ("kernel_actual", "kernel_missing"),
    ("coimage_actual", "coimage_missing"),
    ("exact_sequence_generated_by_bcf", "exact_sequence_not_generated_by_bcf"),
    ("kernel_is_canmod_image", "kernel_not_canmod_image"),
    (
        "coimage_preserves_signed_coefficients",
        "coimage_does_not_preserve_signed_coefficients",
    ),
    ("coimage_preserves_signed_support", "coimage_does_not_preserve_signed_support"),
    ("rank1_duality_actual", "rank1_duality_missing"),
    ("duality_generated_by_delta", "duality_not_generated_by_delta"),
    ("twist_pinned", "twist_not_pinned"),
    ("duality_boundary_is_dd4_class", "duality_boundary_not_dd4_class"),
    ("dual_to_primal_boundary_line", "dual_to_primal_boundary_line_missing"),
    ("p1_p2_dual_endpoint_pairing", "p1_p2_dual_endpoint_pairing_missing"),
    ("bidual_fixed", "bidual_not_fixed"),
    ("rosati_compatible_duality", "rosati_incompatible_duality"),
    ("normal_ratio_self_dual_boundary", "normal_ratio_not_self_dual_boundary"),
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
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
    ("controls_not_points_of_representer", "controls_are_points_of_representer"),
    ("dh_not_points_of_representer", "dh_is_point_of_representer"),
    ("epstein_not_points_of_representer", "epstein_is_point_of_representer"),
)

BANNED = (
    ("connected_dependency_graph_only", "connected_dependency_graph_only"),
    ("nerve_or_segal_completion", "nerve_or_segal_completion"),
    ("functor_of_points_without_representer", "functor_of_points_without_representer"),
    ("yoneda_reversal", "yoneda_reversal"),
    (
        "grothendieck_or_category_of_elements",
        "grothendieck_or_category_of_elements",
    ),
    ("formal_universal_property", "formal_universal_property"),
    ("limit_cone_or_comma_label", "limit_cone_or_comma_label"),
    ("free_operad_completion", "free_operad_completion"),
    ("collage_or_proarrow_equipment", "collage_or_proarrow_equipment"),
    ("codescent_or_descent_label", "codescent_or_descent_label"),
    ("rezk_completion", "rezk_completion"),
    ("local_representer_table", "local_representer_table"),
    ("external_choice_representer", "external_choice_representer"),
    ("retuned_representer", "retuned_representer"),
    ("product_or_pullback_representer", "product_or_pullback_representer"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("semantic_zeta_label", "semantic_zeta_label"),
    ("declared_representer", "declared_representer"),
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
    if not REQUIRED_DOC491_CELLS <= set(data["doc491_cells"]):
        out.append("doc491_cells_missing")
    if not REQUIRED_DOC491_FACES <= set(data["doc491_faces"]):
        out.append("doc491_faces_missing")
    if not REQUIRED_SOURCE_COHERENCE_CELLS <= set(data["source_coherence_cells"]):
        out.append("source_coherence_cells_missing")
    if not REQUIRED_SOURCE_COMPOSITION_CELLS <= set(data["source_composition_cells"]):
        out.append("source_composition_cells_missing")
    if not REQUIRED_REPRESENTABILITY_EDGES <= set(data["required_edges"]):
        out.append("required_coupling_representability_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_represented_coupled_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_SOURCE_COHERENCE_CELLS <= set(data["source_coherence_cells"])
        and REQUIRED_SOURCE_COMPOSITION_CELLS <= set(data["source_composition_cells"])
        and REQUIRED_REPRESENTABILITY_EDGES <= set(data["required_edges"])
        and graph_connected(set(data["required_edges"]))
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        source_category_actual=True,
        product_actual=True,
        alpha_actual=True,
        beta_actual=True,
        equalizer_actual=True,
        universal_mediator_actual=True,
        multiplier_naturality_actual=True,
        path_independent_mediator=True,
        formation_token_actual=True,
        formation_fiber_actual=True,
        formation_generated_by_mediator=True,
        formation_coherence_actual=True,
        coherence_generated_by_mediator=True,
        cartesian_source_coherence_actual=True,
        monoidwide_source_coherence_actual=True,
        source_coupling_actual=True,
        coupling_generated_by_mediator=True,
        coupling_generated_by_formation_coherence=True,
        non_split_dependency_graph=True,
        same_coupling_on_paths=True,
        coupling_representer_actual=True,
        coupling_universal_arrow_actual=True,
        coupling_functor_represented=True,
        coupling_generated_by_representer=True,
        representer_points_exactly_coupled_sources=True,
        exact_delta_coupled=True,
        kernel_coimage_coupled=True,
        signed_coefficients_coupled=True,
        signed_support_coupled=True,
        rank1_duality_coupled=True,
        pinned_twist_coupled=True,
        original_dd4_coupled=True,
        normal_ratio_coupled=True,
        endpoint_pairing_coupled=True,
        endpoint_pushforward_graph_coupled=True,
        rosati_count_coupled=True,
        control_death_coupled=True,
        dd4_certificate_handoff_actual=True,
        old_boundary_certificate_actual=True,
        upmed_dd4_certificate_actual=True,
        upmed_dd4_naturality_actual=True,
        signed_zero_actual=True,
        canmod_actual=True,
        bcf_functor_actual=True,
        exact_source_actual=True,
        exact_delta_actual=True,
        kernel_actual=True,
        coimage_actual=True,
        exact_sequence_generated_by_bcf=True,
        kernel_is_canmod_image=True,
        coimage_preserves_signed_coefficients=True,
        coimage_preserves_signed_support=True,
        rank1_duality_actual=True,
        duality_generated_by_delta=True,
        twist_pinned=True,
        duality_boundary_is_dd4_class=True,
        dual_to_primal_boundary_line=True,
        p1_p2_dual_endpoint_pairing=True,
        bidual_fixed=True,
        rosati_compatible_duality=True,
        normal_ratio_self_dual_boundary=True,
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
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        controls_not_points_of_representer=True,
        dh_not_points_of_representer=True,
        epstein_not_points_of_representer=True,
        required_edges=set(REQUIRED_REPRESENTABILITY_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def representability_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    delta = boundary_delta(chi)
    return {
        "source_category": SOURCE_CATEGORY_ID,
        "product": PRODUCT_ID,
        "alpha": ALPHA_ID,
        "beta": BETA_ID,
        "equalizer": EQUALIZER_ID,
        "equalizer_identity": EQUALIZER_IDENTITY_ID,
        "finite_limit_up": FINITE_LIMIT_UP_ID,
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "upmed_naturality": UPMED_NATURALITY_ID,
        "upmed_composition": UPMED_COMPOSITION_ID,
        "formation_token": FORMATION_TOKEN_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "formation_coherence": FORMATION_COH_ID,
        "cartesian_source_coherence": FORMATION_CART_ID,
        "monoidwide_source_coherence": FORMATION_MWC_ID,
        "source_coupling": SOURCE_COUPLING_ID,
        "coupling_representer": COUPLING_REP_ID,
        "coupling_universal_arrow": COUPLING_ETA_ID,
        "representer_points": "exactly_coupled_self_dual_exact_bcf_sources",
        "source_before_graph_objects": True,
        "controls_not_points": True,
        "dh_not_points": True,
        "epstein_not_points": True,
        "controls_not_points_of_representer": True,
        "dh_not_points_of_representer": True,
        "epstein_not_points_of_representer": True,
        "dd4_class": DD4_CLASS_ID,
        "boundary_certificate": BOUNDARY_CERT_ID,
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "upmed_dd4_naturality": UPMED_DD4_NAT_ID,
        "upmed_dd4_handoff": UPMED_DD4_HANDOFF_ID,
        "signed_zero_fiber": SIGNED_ZERO_ID,
        "cancellation_module": CANMOD_ID,
        "boundary_convolution_functor": BCF_ID,
        "exact_source": EXACT_SOURCE_ID,
        "exact_delta": DELTA_ID,
        "kernel": KERNEL_ID,
        "coimage": COIMAGE_ID,
        "duality": DUALITY_ID,
        "pinned_twist": TWIST_ID,
        "defect_rank": 1,
        "duality_generated_by": DELTA_ID,
        "duality_direction": ("dual_boundary_defect_line", "primal_boundary_defect_line"),
        "endpoint_pairing": (p1, p2, p1 == p2),
        "bidual_fixed": True,
        "boundary_class": DD4_CLASS_ID,
        "res1": 1,
        "normal_ratio": NORMAL_RATIO_ID,
        "normal_ratio_self_dual_boundary": True,
        "rosati_compatible": True,
        "kernel_relation": tuple(chi.items()),
        "coimage_signature": positive_negative_split(chi),
        "localization": LOCALIZATION_ID,
        "finite_index": FINITE_INDEX_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "source_coherence_cells": tuple(sorted(REQUIRED_SOURCE_COHERENCE_CELLS)),
        "source_composition_cells": tuple(sorted(REQUIRED_SOURCE_COMPOSITION_CELLS)),
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
        "required_edges": tuple(sorted(REQUIRED_REPRESENTABILITY_EDGES)),
        "delta": delta,
        "represents": (
            SOURCE_COUPLING_ID,
            DELTA_ID,
            KERNEL_ID,
            COIMAGE_ID,
            DUALITY_ID,
            TWIST_ID,
            DD4_CLASS_ID,
            NORMAL_RATIO_ID,
            "endpoint_pairing",
            "endpoint_pushforward_graph",
            "rosati_count",
            "source_control_death",
        ),
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
    }


def represented_row(chi: dict[int, int]) -> bool:
    payload = representability_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["delta"]["weighted_mass"] == 0
        and payload["kernel_relation"] == payload["coefficients"]
        and payload["coimage_signature"] == payload["delta"]["split"]
        and payload["formation_token"] == FORMATION_TOKEN_ID
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["formation_coherence"] == FORMATION_COH_ID
        and payload["source_coupling"] == SOURCE_COUPLING_ID
        and payload["coupling_representer"] == COUPLING_REP_ID
        and payload["coupling_universal_arrow"] == COUPLING_ETA_ID
        and payload["representer_points"] == "exactly_coupled_self_dual_exact_bcf_sources"
        and payload["source_before_graph_objects"]
        and payload["controls_not_points_of_representer"]
        and payload["dh_not_points_of_representer"]
        and payload["epstein_not_points_of_representer"]
        and payload["exact_delta"] == DELTA_ID
        and payload["kernel"] == KERNEL_ID
        and payload["coimage"] == COIMAGE_ID
        and payload["duality"] == DUALITY_ID
        and payload["pinned_twist"] == TWIST_ID
        and payload["boundary_class"] == DD4_CLASS_ID
        and payload["res1"] == 1
        and payload["endpoint_pairing"][2]
        and payload["normal_ratio_self_dual_boundary"]
        and payload["rosati_compatible"]
        and SOURCE_COUPLING_ID in payload["represents"]
        and DELTA_ID in payload["represents"]
        and DUALITY_ID in payload["represents"]
        and DD4_CLASS_ID in payload["represents"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_REPRESENTABILITY_EDGES))
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD1 mediator coupling has source representer",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_REPRESENTABILITY_EDGES)
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
    and representability_payload(T3_T5_z) == representability_payload(zC15)
    and representability_payload(T5_T3_z) == representability_payload(zC15)
    and representability_payload(T3_T3_T5_z) == representability_payload(zC45)
    and representability_payload(T15_zF22) == representability_payload(zC15F22)
    and representability_payload(T45_zF22) == representability_payload(zC45F22)
    and all(represented_row(row) for row in rows),
    "H1=%s rep_edges=%d finite_index=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(REQUIRED_REPRESENTABILITY_EDGES),
        len(FINITE_INDEX),
    ),
)

graph_only = live_source(
    coupling_representer_actual=False,
    coupling_universal_arrow_actual=False,
    coupling_functor_represented=False,
    coupling_generated_by_representer=False,
    representer_points_exactly_coupled_sources=False,
    connected_dependency_graph_only=True,
    nerve_or_segal_completion=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD2 connected graphs and nerves fail",
    not accepts_represented_coupled_mediator(graph_only)
    and {
        "coupling_representer_missing",
        "coupling_universal_arrow_missing",
        "coupling_functor_not_represented",
        "coupling_not_generated_by_representer",
        "representer_points_not_exactly_coupled_sources",
        "connected_dependency_graph_only",
        "nerve_or_segal_completion",
    }
    <= set(reasons(graph_only)),
    ",".join(reasons(graph_only)),
)

points_wrapper = live_source(
    coupling_representer_actual=False,
    coupling_functor_represented=False,
    functor_of_points_without_representer=True,
    yoneda_reversal=True,
    grothendieck_or_category_of_elements=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD3 point wrappers without representer fail",
    not accepts_represented_coupled_mediator(points_wrapper)
    and {
        "coupling_representer_missing",
        "coupling_functor_not_represented",
        "functor_of_points_without_representer",
        "yoneda_reversal",
        "grothendieck_or_category_of_elements",
    }
    <= set(reasons(points_wrapper)),
    ",".join(reasons(points_wrapper)),
)

formal_up = live_source(
    coupling_representer_actual=False,
    coupling_universal_arrow_actual=False,
    formal_universal_property=True,
    limit_cone_or_comma_label=True,
    declared_representer=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD4 formal universal-property labels fail",
    not accepts_represented_coupled_mediator(formal_up)
    and {
        "coupling_representer_missing",
        "coupling_universal_arrow_missing",
        "formal_universal_property",
        "limit_cone_or_comma_label",
        "declared_representer",
    }
    <= set(reasons(formal_up)),
    ",".join(reasons(formal_up)),
)

free_completion = live_source(
    coupling_generated_by_representer=False,
    free_operad_completion=True,
    collage_or_proarrow_equipment=True,
    codescent_or_descent_label=True,
    rezk_completion=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD5 free completions and descent labels fail",
    not accepts_represented_coupled_mediator(free_completion)
    and {
        "coupling_not_generated_by_representer",
        "free_operad_completion",
        "collage_or_proarrow_equipment",
        "codescent_or_descent_label",
        "rezk_completion",
    }
    <= set(reasons(free_completion)),
    ",".join(reasons(free_completion)),
)

local_external = live_source(
    carrier_native=False,
    same_coupling_on_paths=False,
    exact_delta_coupled=False,
    original_dd4_coupled=False,
    local_representer_table=True,
    external_choice_representer=True,
    retuned_representer=True,
    product_or_pullback_representer=True,
    semantic_zeta_label=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD6 local or retuned representers fail",
    not accepts_represented_coupled_mediator(local_external)
    and {
        "not_carrier_native",
        "same_coupling_not_on_paths",
        "exact_delta_not_coupled",
        "original_dd4_not_coupled",
        "local_representer_table",
        "external_choice_representer",
        "retuned_representer",
        "product_or_pullback_representer",
        "semantic_zeta_label",
    }
    <= set(reasons(local_external)),
    ",".join(reasons(local_external)),
)

graph_classifier = live_source(
    source_before_graph_objects=False,
    source_before_points=False,
    controls_not_points_of_representer=False,
    dh_not_points_of_representer=False,
    epstein_not_points_of_representer=False,
    graph_object_classifier=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD7 graph classifiers leave controls as points",
    not accepts_represented_coupled_mediator(graph_classifier)
    and {
        "source_not_before_graph_objects",
        "source_not_before_points",
        "controls_are_points_of_representer",
        "dh_is_point_of_representer",
        "epstein_is_point_of_representer",
        "graph_object_classifier",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_classifier)),
    ",".join(reasons(graph_classifier)),
)

wrong_points = live_source(
    representer_points_exactly_coupled_sources=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    controls_not_points_of_representer=False,
    dh_not_points_of_representer=False,
    epstein_not_points_of_representer=False,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD8 representer points must be exact",
    not accepts_represented_coupled_mediator(wrong_points)
    and {
        "representer_points_not_exactly_coupled_sources",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "controls_are_points_of_representer",
        "dh_is_point_of_representer",
        "epstein_is_point_of_representer",
    }
    <= set(reasons(wrong_points)),
    ",".join(reasons(wrong_points)),
)

missing_edges = [
    live_source(
        required_edges=REQUIRED_REPRESENTABILITY_EDGES
        - {("universal_mediator", "source_coupling_representing_object")}
    ),
    live_source(coupling_representer_actual=False),
    live_source(coupling_universal_arrow_actual=False),
    live_source(coupling_functor_represented=False),
    live_source(coupling_generated_by_representer=False),
    live_source(representer_points_exactly_coupled_sources=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD9 every representability edge is mandatory",
    not any(accepts_represented_coupled_mediator(data) for data in missing_edges)
    and {
        "required_coupling_representability_edges_missing",
        "coupling_representer_missing",
        "coupling_universal_arrow_missing",
        "coupling_functor_not_represented",
        "coupling_not_generated_by_representer",
        "representer_points_not_exactly_coupled_sources",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

expanded_index = live_source(
    finite_index=set(FINITE_INDEX) | {"coupling_representer_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    doc491_in_finite_index=False,
    closure_returns_same_totalizer=False,
    no_next_coherence_obligation=False,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

dead_sources = {
    "graph_only": graph_only,
    "points_wrapper": points_wrapper,
    "formal_up": formal_up,
    "free_completion": free_completion,
    "local_external": local_external,
    "graph_classifier": graph_classifier,
    "wrong_points": wrong_points,
    "expanded_index": expanded_index,
}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD10 only represented coupled mediator passes",
    accepts_represented_coupled_mediator(live_source())
    and not accepts_represented_coupled_mediator(expanded_index)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "doc491_not_in_finite_index",
        "closure_does_not_return_same_totalizer",
        "next_coherence_obligation_open",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded_index))
    and not any(
        accepts_represented_coupled_mediator(data) for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(
            accepts_represented_coupled_mediator(data)
            for data in dead_sources.values()
        ),
        accepts_represented_coupled_mediator(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: equalizer identity universal mediator represented coupled "
    "formation-coherent self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-502 mediator coupling must be represented by an actual "
    "source-side object and universal arrow generated by the same equalizer-"
    "identity mediator, with points exactly the coupled self-dual exact BCF "
    "sources and controls/DH/Epstein non-points. Connected graphs, nerves, "
    "functors of points, formal universal properties, completions, local or "
    "retuned representers, graph classifiers, declared representers, expanded "
    "indexes, and towers do not construct the missing object."
)
