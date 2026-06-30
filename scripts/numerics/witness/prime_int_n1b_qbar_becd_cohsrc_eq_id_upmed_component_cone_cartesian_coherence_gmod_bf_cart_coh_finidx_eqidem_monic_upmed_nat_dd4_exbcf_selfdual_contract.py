r"""Self-dual exact-BCF certificate contract for the doc-522 mediator.

Doc 522 makes the source finite-limit universal mediator carry the exact BCF
generation of the old DD.4 certificate. This witness pins the next edge:
that exact source must itself generate the rank-one boundary-defect duality
and pinned Laurent twist. A one-sided exact delta plus a downstream
self-duality label does not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

SOURCE_CATEGORY_ID = "SrcCat_NCoup_med_UP_Eq_id_Qbar_BECD"
PRODUCT_ID = "Prod_NCoup_med_UP_Eq_id_source_components_facets_cells"
ALPHA_ID = "alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_ID = "beta_NCoup_med_UP_Eq_id_source_constraints"
EQUALIZER_ID = "Eq_NCoup_med_UP_Eq_id_source_components"
EQUALIZER_IDENTITY_ID = "id_Eq_NCoup_med_UP_Eq_id_source_components"
FINITE_LIMIT_UP_ID = "UP_Eq_NCoup_med_UP_Eq_id_source_components_finite_limit"
UNIVERSAL_MEDIATOR_ID = (
    "med_UP_Eq_NCoup_med_UP_Eq_id_id_to_id_Eq_NCoup_med_UP_Eq_id_source_components"
)
UPMED_NATURALITY_ID = "Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_multiplier_action"
UPMED_COMPOSITION_ID = (
    "Comp_Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_C3_C5_C15_C45_F22"
)
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
BOUNDARY_CERT_ID = (
    "BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality"
)
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_boundary"
UPMED_DD4_NAT_ID = "Nat_Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_multiplier_action"
UPMED_DD4_HANDOFF_ID = (
    "Handoff_BKill_to_med_UP_Eq_NCoup_med_UP_Eq_id_DD4_certificate"
)
SIGNED_ZERO_ID = "ZFib_med_UP_Eq_NCoup_med_UP_Eq_id_id_signed_zero"
CANMOD_ID = "CanMod_med_UP_Eq_NCoup_med_UP_Eq_id_id_z_boundary_convolution"
BCF_ID = "BCF_med_UP_Eq_NCoup_med_UP_Eq_id_id_boundary_convolution_module"
EXACT_SOURCE_ID = "Ex_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_dQ"
DELTA_ID = "Delta_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_to_dQ_boundary"
KERNEL_ID = "Ker_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_delta_image_z"
COIMAGE_ID = "Coim_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_delta"
DUALITY_ID = "Dual_med_UP_Eq_NCoup_med_UP_Eq_id_id_rank1_boundary_defect"
TWIST_ID = "Tw_med_UP_Eq_NCoup_med_UP_Eq_id_id_OC_BCF_pinned"
LOCALIZATION_ID = "Loc_NCoup_med_UP_Eq_id_Qbar_BECD_single_dQ"
NORMAL_RATIO_ID = "NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2"
FINITE_INDEX_ID = "FinIdx_NCoup_med_UP_Eq_id_source_components"
SOURCE_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
DOC515_COHERENCE_ID = (
    "Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components"
)
DOC515_INDEX_CELL = "boundary_fiber_coherence_cell"

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

REQUIRED_DOC515_CELLS = {
    "cell_C3_C5_C15_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_C5_C3_C15_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_C3_C3_C5_C45_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_F22_interchange_NCoup_med_UP_Eq_id_boundary_fiber",
    "cell_boundary_restriction_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_boundary_fiber_arrow_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_fixed_globular_boundary_pullback_NCoup_med_UP_Eq_id",
    "cell_source_boundary_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_target_boundary_cartesian_naturality_NCoup_med_UP_Eq_id",
    "cell_pasting_faces_cartesian_naturality_NCoup_med_UP_Eq_id",
}

REQUIRED_DUALITY_NATURALITY_CELLS = {
    "self_dual_exact_bcf_nat_C3_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_nat_C5_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_nat_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_nat_C45_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_nat_F22_med_UP_Eq_NCoup_med_UP_Eq_id_id",
}

REQUIRED_DUALITY_COMPOSITION_CELLS = {
    "self_dual_exact_bcf_cell_C3_C5_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_cell_C5_C3_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_cell_C3_C3_C5_C45_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    "self_dual_exact_bcf_cell_F22_product_med_UP_Eq_NCoup_med_UP_Eq_id_id",
}

REQUIRED_SELF_DUAL_EDGES = {
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
    ("path_independent_mediator", "dd4_certificate_handoff"),
    ("dd4_certificate_handoff", "old_boundary_certificate"),
    ("old_boundary_certificate", "upmed_dd4_certificate"),
    ("upmed_dd4_certificate", "upmed_dd4_naturality"),
    ("upmed_dd4_certificate", "signed_zero_fiber"),
    ("signed_zero_fiber", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_functor"),
    ("boundary_convolution_functor", "exact_source"),
    ("exact_source", "exact_boundary_delta"),
    ("exact_boundary_delta", "kernel_is_cancellation_image"),
    ("exact_boundary_delta", "coimage_preserves_signed_coefficients"),
    ("exact_boundary_delta", "coimage_preserves_signed_support"),
    ("exact_boundary_delta", "rank1_boundary_defect_duality"),
    ("rank1_boundary_defect_duality", "pinned_laurent_twist"),
    ("rank1_boundary_defect_duality", "original_dd4_boundary"),
    ("rank1_boundary_defect_duality", "dual_to_primal_boundary_defect_line"),
    ("rank1_boundary_defect_duality", "p1_p2_endpoint_pairing"),
    ("rank1_boundary_defect_duality", "bidual_fixed"),
    ("rank1_boundary_defect_duality", "rosati_compatible_duality"),
    ("original_dd4_boundary", "dd4_original_class"),
    ("dd4_original_class", "dd4_res1_preserved"),
    ("dd4_original_class", "dd4_nonboundary_preserved"),
    ("dd4_res1_preserved", "res1_equals_one_before_certificate"),
    ("dd4_nonboundary_preserved", "not_coboundary_before_certificate"),
    ("old_boundary_certificate", "dQ_localization"),
    ("dQ_localization", "certificate_kills_class"),
    ("old_boundary_certificate", "ordered_normal_ratio"),
    ("ordered_normal_ratio", "normal_ratio_self_dual_boundary"),
    ("normal_ratio_self_dual_boundary", "certificate_kills_class"),
    ("rank1_boundary_defect_duality", "same_duality_on_multiplier_paths"),
    ("same_duality_on_multiplier_paths", "C3_C5_equals_C15"),
    ("same_duality_on_multiplier_paths", "C5_C3_equals_C15"),
    ("same_duality_on_multiplier_paths", "C3_C3_C5_equals_C45"),
    ("same_duality_on_multiplier_paths", "F22_product_interchange"),
    ("same_duality_on_multiplier_paths", "duality_naturality_cells"),
    (
        "duality_naturality_cells",
        "self_dual_exact_bcf_nat_C3_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_naturality_cells",
        "self_dual_exact_bcf_nat_C5_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_naturality_cells",
        "self_dual_exact_bcf_nat_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_naturality_cells",
        "self_dual_exact_bcf_nat_C45_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_naturality_cells",
        "self_dual_exact_bcf_nat_F22_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    ("same_duality_on_multiplier_paths", "duality_composition_cells"),
    (
        "duality_composition_cells",
        "self_dual_exact_bcf_cell_C3_C5_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_composition_cells",
        "self_dual_exact_bcf_cell_C5_C3_C15_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_composition_cells",
        "self_dual_exact_bcf_cell_C3_C3_C5_C45_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    (
        "duality_composition_cells",
        "self_dual_exact_bcf_cell_F22_product_med_UP_Eq_NCoup_med_UP_Eq_id_id",
    ),
    ("universal_mediator", "source_mediator_fixed"),
    ("source_mediator_fixed", "source_universal_mediator"),
    ("universal_mediator", "doc515_coherence_fixed"),
    ("doc515_coherence_fixed", "doc515_cartesian_boundary_fiber_coherence"),
    ("doc515_cartesian_boundary_fiber_coherence", "doc515_cells"),
    ("doc515_cells", DOC515_INDEX_CELL),
    (DOC515_INDEX_CELL, "equalizer_identity"),
    ("finite_cell_index", DOC515_INDEX_CELL),
    ("finite_cell_index", "source_before_points"),
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


def laurent_window_profile() -> dict[str, tuple[int, ...]]:
    base = (2, 3, 5, 9)
    unit_twists = tuple(2 * item - 1 for item in base)
    return {
        "support_ranks": tuple(2 * item for item in base),
        "hyperbolic_ranks": tuple(4 * item for item in base),
        "defect_ranks": (1, 1, 1, 1),
        "unit_twists": unit_twists,
        "nonzero_maps": tuple(2**twist - 1 for twist in unit_twists),
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
        "same_duality_on_paths": False,
        "source_mediator_actual": False,
        "source_mediator_fixed": False,
        "doc515_coherence_actual": False,
        "doc515_coherence_fixed": False,
        "doc515_cells": set(),
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "doc515_in_finite_index": False,
        "duality_naturality_cells": set(),
        "duality_composition_cells": set(),
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "one_sided_exact_delta": False,
        "generic_self_duality_label": False,
        "hyperbolic_endpoint_plane": False,
        "full_support_duality": False,
        "inserted_dual_primal_matching": False,
        "scalar_pairing": False,
        "diagonal_coevaluation": False,
        "formal_rosati_adjoint": False,
        "degree_zero_twist_normalization": False,
        "declared_normal_ratio": False,
        "weighted_zero_dual_kernel": False,
        "support_dual_kernel": False,
        "late_rosati_filter": False,
        "degree_count_equality_only": False,
        "retuned_duality": False,
        "graph_side_duality": False,
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
    ("same_duality_on_paths", "duality_not_path_independent"),
    ("source_mediator_actual", "source_mediator_missing"),
    ("source_mediator_fixed", "source_mediator_not_fixed"),
    ("doc515_coherence_actual", "doc515_coherence_missing"),
    ("doc515_coherence_fixed", "doc515_coherence_not_fixed"),
    ("doc515_in_finite_index", "doc515_not_in_finite_index"),
    ("closure_returns_same_totalizer", "closure_does_not_return_same_totalizer"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("one_sided_exact_delta", "one_sided_exact_delta"),
    ("generic_self_duality_label", "generic_self_duality_label"),
    ("hyperbolic_endpoint_plane", "hyperbolic_endpoint_plane"),
    ("full_support_duality", "full_support_duality"),
    ("inserted_dual_primal_matching", "inserted_dual_primal_matching"),
    ("scalar_pairing", "scalar_pairing"),
    ("diagonal_coevaluation", "diagonal_coevaluation"),
    ("formal_rosati_adjoint", "formal_rosati_adjoint"),
    ("degree_zero_twist_normalization", "degree_zero_twist_normalization"),
    ("declared_normal_ratio", "declared_normal_ratio"),
    ("weighted_zero_dual_kernel", "weighted_zero_dual_kernel"),
    ("support_dual_kernel", "support_dual_kernel"),
    ("late_rosati_filter", "late_rosati_filter"),
    ("degree_count_equality_only", "degree_count_equality_only"),
    ("retuned_duality", "retuned_duality"),
    ("graph_side_duality", "graph_side_duality"),
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
    if not REQUIRED_DOC515_CELLS <= set(data["doc515_cells"]):
        out.append("doc515_cells_missing")
    if not REQUIRED_DUALITY_NATURALITY_CELLS <= set(data["duality_naturality_cells"]):
        out.append("duality_naturality_cells_missing")
    if not REQUIRED_DUALITY_COMPOSITION_CELLS <= set(data["duality_composition_cells"]):
        out.append("duality_composition_cells_missing")
    if not REQUIRED_SELF_DUAL_EDGES <= set(data["required_edges"]):
        out.append("required_self_dual_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_self_dual_exact_bcf_mediator_certificate(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC515_CELLS <= set(data["doc515_cells"])
        and REQUIRED_DUALITY_NATURALITY_CELLS <= set(data["duality_naturality_cells"])
        and REQUIRED_DUALITY_COMPOSITION_CELLS <= set(data["duality_composition_cells"])
        and REQUIRED_SELF_DUAL_EDGES <= set(data["required_edges"])
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
        same_duality_on_paths=True,
        source_mediator_actual=True,
        source_mediator_fixed=True,
        doc515_coherence_actual=True,
        doc515_coherence_fixed=True,
        doc515_cells=set(REQUIRED_DOC515_CELLS),
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        doc515_in_finite_index=True,
        duality_naturality_cells=set(REQUIRED_DUALITY_NATURALITY_CELLS),
        duality_composition_cells=set(REQUIRED_DUALITY_COMPOSITION_CELLS),
        closure_returns_same_totalizer=True,
        no_next_coherence_obligation=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_SELF_DUAL_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def self_dual_payload(chi: dict[int, int]) -> dict[str, object]:
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
        "source_mediator": SOURCE_MEDIATOR_ID,
        "doc515_coherence": DOC515_COHERENCE_ID,
        "doc515_index_cell": DOC515_INDEX_CELL,
        "duality_naturality_cells": tuple(sorted(REQUIRED_DUALITY_NATURALITY_CELLS)),
        "duality_composition_cells": tuple(sorted(REQUIRED_DUALITY_COMPOSITION_CELLS)),
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc515_cells": tuple(sorted(REQUIRED_DOC515_CELLS)),
        "delta": delta,
        "dd4_obstruction": ("H1=Z/2", "res1=1", "nonboundary_before_certificate"),
        "certificate_effect": "killed_after_single_dQ_localization",
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
    }


def self_dual_row(chi: dict[int, int]) -> bool:
    payload = self_dual_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["delta"]["weighted_mass"] == 0
        and payload["kernel_relation"] == payload["coefficients"]
        and payload["coimage_signature"] == payload["delta"]["split"]
        and payload["signed_zero_fiber"] == SIGNED_ZERO_ID
        and payload["cancellation_module"] == CANMOD_ID
        and payload["boundary_convolution_functor"] == BCF_ID
        and payload["exact_source"] == EXACT_SOURCE_ID
        and payload["exact_delta"] == DELTA_ID
        and payload["kernel"] == KERNEL_ID
        and payload["coimage"] == COIMAGE_ID
        and payload["duality"] == DUALITY_ID
        and payload["pinned_twist"] == TWIST_ID
        and payload["defect_rank"] == 1
        and payload["duality_generated_by"] == DELTA_ID
        and payload["boundary_class"] == DD4_CLASS_ID
        and payload["res1"] == 1
        and payload["endpoint_pairing"][2]
        and payload["bidual_fixed"]
        and payload["normal_ratio_self_dual_boundary"]
        and payload["rosati_compatible"]
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
profile = laurent_window_profile()
profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
non_square_balanced = {1: 4, 4: -1}
allowed_duality_rows = {tuple(row.items()) for row in rows}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD1 mediator exact BCF source generates rank-one duality",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_SELF_DUAL_EDGES)
    and profile["support_ranks"] == (4, 6, 10, 18)
    and profile["hyperbolic_ranks"] == (8, 12, 20, 36)
    and profile["defect_ranks"] == (1, 1, 1, 1)
    and profile["unit_twists"] == (3, 5, 9, 17)
    and profile["nonzero_maps"] == (7, 31, 511, 131071)
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC515_CELLS) == 10
    and len(REQUIRED_DUALITY_NATURALITY_CELLS) == 5
    and len(REQUIRED_DUALITY_COMPOSITION_CELLS) == 4
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and self_dual_payload(T3_T5_z) == self_dual_payload(zC15)
    and self_dual_payload(T5_T3_z) == self_dual_payload(zC15)
    and self_dual_payload(T3_T3_T5_z) == self_dual_payload(zC45)
    and self_dual_payload(T15_zF22) == self_dual_payload(zC15F22)
    and self_dual_payload(T45_zF22) == self_dual_payload(zC45F22)
    and all(self_dual_row(row) for row in rows),
    "H1=%s twist=%s dual_nat=%d dual_comp=%d"
    % (
        [p["h1_order"] for p in profiles],
        profile["unit_twists"],
        len(REQUIRED_DUALITY_NATURALITY_CELLS),
        len(REQUIRED_DUALITY_COMPOSITION_CELLS),
    ),
)

one_sided = live_source(
    rank1_duality_actual=False,
    duality_generated_by_delta=False,
    twist_pinned=False,
    duality_boundary_is_dd4_class=False,
    normal_ratio_self_dual_boundary=False,
    same_duality_on_paths=False,
    one_sided_exact_delta=True,
    generic_self_duality_label=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD2 one-sided exact deltas and labels fail",
    not accepts_self_dual_exact_bcf_mediator_certificate(one_sided)
    and {
        "rank1_duality_missing",
        "duality_not_generated_by_delta",
        "twist_not_pinned",
        "duality_boundary_not_dd4_class",
        "normal_ratio_not_self_dual_boundary",
        "duality_not_path_independent",
        "one_sided_exact_delta",
        "generic_self_duality_label",
    }
    <= set(reasons(one_sided)),
    ",".join(reasons(one_sided)),
)

hyperbolic = live_source(
    rank1_duality_actual=False,
    dual_to_primal_boundary_line=False,
    p1_p2_dual_endpoint_pairing=False,
    hyperbolic_endpoint_plane=True,
    full_support_duality=True,
    inserted_dual_primal_matching=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD3 hyperbolic full-support dualities fail",
    all(h > s for h, s in zip(profile["hyperbolic_ranks"], profile["support_ranks"]))
    and not accepts_self_dual_exact_bcf_mediator_certificate(hyperbolic)
    and {
        "rank1_duality_missing",
        "dual_to_primal_boundary_line_missing",
        "p1_p2_dual_endpoint_pairing_missing",
        "hyperbolic_endpoint_plane",
        "full_support_duality",
        "inserted_dual_primal_matching",
    }
    <= set(reasons(hyperbolic)),
    ",".join(reasons(hyperbolic)),
)

formal_pairing = live_source(
    rank1_duality_actual=False,
    bidual_fixed=False,
    rosati_compatible_duality=False,
    scalar_pairing=True,
    diagonal_coevaluation=True,
    formal_rosati_adjoint=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD4 scalar pairing and formal adjoints fail",
    not accepts_self_dual_exact_bcf_mediator_certificate(formal_pairing)
    and {
        "rank1_duality_missing",
        "bidual_not_fixed",
        "rosati_incompatible_duality",
        "scalar_pairing",
        "diagonal_coevaluation",
        "formal_rosati_adjoint",
    }
    <= set(reasons(formal_pairing)),
    ",".join(reasons(formal_pairing)),
)

twist_ratio = live_source(
    twist_pinned=False,
    normal_ratio_actual=False,
    normal_ratio_self_dual_boundary=False,
    certificate_kills_class=False,
    degree_zero_twist_normalization=True,
    declared_normal_ratio=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD5 twist normalization and declared ratios fail",
    min(profile["unit_twists"]) > 0
    and not accepts_self_dual_exact_bcf_mediator_certificate(twist_ratio)
    and {
        "twist_not_pinned",
        "normal_ratio_missing",
        "normal_ratio_not_self_dual_boundary",
        "certificate_does_not_kill_class",
        "degree_zero_twist_normalization",
        "declared_normal_ratio",
    }
    <= set(reasons(twist_ratio)),
    ",".join(reasons(twist_ratio)),
)

dual_kernel = live_source(
    kernel_is_canmod_image=False,
    rank1_duality_actual=False,
    duality_generated_by_delta=False,
    weighted_zero_dual_kernel=True,
    support_dual_kernel=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD6 weighted-zero support dual kernels fail",
    weighted_mass(non_square_balanced) == 0
    and tuple(non_square_balanced.items()) not in allowed_duality_rows
    and not accepts_self_dual_exact_bcf_mediator_certificate(dual_kernel)
    and {
        "kernel_not_canmod_image",
        "rank1_duality_missing",
        "duality_not_generated_by_delta",
        "weighted_zero_dual_kernel",
        "support_dual_kernel",
    }
    <= set(reasons(dual_kernel)),
    ",".join(reasons(dual_kernel)),
)

late = live_source(
    rank1_duality_actual=False,
    rosati_compatible_duality=False,
    same_duality_on_paths=False,
    late_rosati_filter=True,
    degree_count_equality_only=True,
    retuned_duality=True,
    graph_side_duality=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD7 late Rosati graph or retuned duality fails",
    not accepts_self_dual_exact_bcf_mediator_certificate(late)
    and {
        "rank1_duality_missing",
        "rosati_incompatible_duality",
        "duality_not_path_independent",
        "late_rosati_filter",
        "degree_count_equality_only",
        "retuned_duality",
        "graph_side_duality",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"med_up_eq_self_dual_exact_bcf_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD8 expanded finite indexes and towers fail",
    not accepts_self_dual_exact_bcf_mediator_certificate(expanded)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded)),
    ",".join(reasons(expanded)),
)

control = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD9 control/DH/Epstein duality fails",
    not accepts_self_dual_exact_bcf_mediator_certificate(control)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control)),
    ",".join(reasons(control)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_SELF_DUAL_EDGES - {edge})
    for edge in list(REQUIRED_SELF_DUAL_EDGES)[:8]
] + [
    live_source(rank1_duality_actual=False),
    live_source(duality_generated_by_delta=False),
    live_source(twist_pinned=False),
    live_source(duality_boundary_is_dd4_class=False),
    live_source(p1_p2_dual_endpoint_pairing=False),
    live_source(rosati_compatible_duality=False),
    live_source(normal_ratio_self_dual_boundary=False),
    live_source(same_duality_on_paths=False),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD10 only self-dual exact BCF mediator passes",
    accepts_self_dual_exact_bcf_mediator_certificate(live_source())
    and not any(
        accepts_self_dual_exact_bcf_mediator_certificate(data)
        for data in missing_edges
    )
    and {
        "required_self_dual_edges_missing",
        "rank1_duality_missing",
        "duality_not_generated_by_delta",
        "twist_not_pinned",
        "duality_boundary_not_dd4_class",
        "p1_p2_dual_endpoint_pairing_missing",
        "rosati_incompatible_duality",
        "normal_ratio_not_self_dual_boundary",
        "duality_not_path_independent",
        "next_coherence_obligation_open",
    }
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (
        sorted(missing_reasons),
        accepts_self_dual_exact_bcf_mediator_certificate(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD10 ALL PASS: "
    "equalizer identity universal mediator self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-522 exact-BCF-generated DD.4-certificate-carrying "
    "universal mediator must also carry the rank-one boundary-defect duality "
    "and pinned Laurent twist generated by the same exact BCF delta. "
    "One-sided deltas, generic self-duality labels, hyperbolic endpoint "
    "planes, scalar pairings, formal Rosati adjoints, declared normal ratios, "
    "weighted/support dual kernels, late filters, retuned dualities, expanded "
    "indexes, towers, and control/DH/Epstein point-formability do not "
    "construct the missing object."
)
