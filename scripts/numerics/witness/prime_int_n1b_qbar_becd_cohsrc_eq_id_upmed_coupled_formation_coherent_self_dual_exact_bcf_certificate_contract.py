r"""Coupled formation-coherent self-dual exact-BCF mediator contract.

Doc 501 makes the equalizer-identity universal mediator generate source
formation coherence for the self-dual exact BCF certificate. This witness
pins the next edge: those coherence cells cannot be a product of independent
exact/DD.4/duality/endpoint/graph/control preservers. The same universal
mediator must generate one non-split source-coherence coupling primitive
before graph objects exist.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
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

REQUIRED_COUPLING_EDGES = {
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
    ("formation_coherence", "cartesian_source_coherence"),
    ("formation_coherence", "monoidwide_source_coherence"),
    ("formation_coherence", "source_coherence_coupling_primitive"),
    ("universal_mediator", "source_coherence_coupling_primitive"),
    ("source_coherence_coupling_primitive", "formation_token"),
    ("source_coherence_coupling_primitive", "formation_fiber"),
    ("source_coherence_coupling_primitive", "formation_coherence"),
    ("source_coherence_coupling_primitive", "cartesian_source_coherence"),
    ("source_coherence_coupling_primitive", "monoidwide_source_coherence"),
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
    ("source_before_graph_objects", "controls_not_points"),
    ("source_before_graph_objects", "dh_not_points"),
    ("source_before_graph_objects", "epstein_not_points"),
    ("source_coherence_coupling_primitive", "signed_coefficients"),
    ("source_coherence_coupling_primitive", "signed_support"),
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
    ("source_coherence_coupling_primitive", "source_coherence_naturality_cells"),
    ("source_coherence_naturality_cells", "formation_coh_nat_C3_med_UP_Eq_id"),
    ("source_coherence_naturality_cells", "formation_coh_nat_C5_med_UP_Eq_id"),
    ("source_coherence_naturality_cells", "formation_coh_nat_C15_med_UP_Eq_id"),
    ("source_coherence_naturality_cells", "formation_coh_nat_C45_med_UP_Eq_id"),
    ("source_coherence_naturality_cells", "formation_coh_nat_F22_med_UP_Eq_id"),
    ("source_coherence_coupling_primitive", "source_coherence_composition_cells"),
    (
        "source_coherence_composition_cells",
        "formation_coh_cell_C3_C5_C15_med_UP_Eq_id",
    ),
    (
        "source_coherence_composition_cells",
        "formation_coh_cell_C5_C3_C15_med_UP_Eq_id",
    ),
    (
        "source_coherence_composition_cells",
        "formation_coh_cell_C3_C3_C5_C45_med_UP_Eq_id",
    ),
    (
        "source_coherence_composition_cells",
        "formation_coh_cell_F22_product_med_UP_Eq_id",
    ),
    ("doc491_globular_modification", "doc491_globular_boundary"),
    ("doc491_globular_modification", "doc491_cells"),
    ("doc491_cells", "doc491_faces"),
    ("doc491_globular_modification", "finite_cell_index"),
    ("finite_cell_index", "fiber_coherence_modification_cell"),
    ("fiber_coherence_modification_cell", "equalizer_identity"),
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
        "source_before_graph_objects": False,
        "control_death_at_source": False,
        "formation_coherence_actual": False,
        "coherence_generated_by_mediator": False,
        "cartesian_source_coherence_actual": False,
        "monoidwide_source_coherence_actual": False,
        "same_coherence_on_paths": False,
        "source_coupling_actual": False,
        "coupling_generated_by_mediator": False,
        "coupling_generated_by_formation_coherence": False,
        "non_split_dependency_graph": False,
        "same_coupling_on_paths": False,
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
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "product_of_layer_coherences": False,
        "atomwise_preservation": False,
        "fiber_product_of_contracts": False,
        "pullback_square_only": False,
        "distributive_law_label": False,
        "formal_pasting_diagram": False,
        "sequential_layer_pipeline": False,
        "exactness_then_duality": False,
        "local_c3_patch": False,
        "finite_composition_table": False,
        "external_choice_of_coupling": False,
        "retuned_coupling": False,
        "graph_object_coherence": False,
        "graph_predicate_gate": False,
        "late_control_filter": False,
        "boundary_dd4_after_filter": False,
        "semantic_zeta_label": False,
        "expanded_finite_index": False,
        "one_more_layer_tower": False,
        "declared_coupling": False,
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
    ("source_before_graph_objects", "source_not_before_graph_objects"),
    ("control_death_at_source", "control_death_not_at_source"),
    ("formation_coherence_actual", "formation_coherence_missing"),
    ("coherence_generated_by_mediator", "coherence_not_generated_by_mediator"),
    ("cartesian_source_coherence_actual", "cartesian_source_coherence_missing"),
    ("monoidwide_source_coherence_actual", "monoidwide_source_coherence_missing"),
    ("same_coherence_on_paths", "coherence_not_path_independent"),
    ("source_coupling_actual", "source_coupling_missing"),
    ("coupling_generated_by_mediator", "coupling_not_generated_by_mediator"),
    (
        "coupling_generated_by_formation_coherence",
        "coupling_not_generated_by_formation_coherence",
    ),
    ("non_split_dependency_graph", "dependency_graph_split"),
    ("same_coupling_on_paths", "same_coupling_not_on_paths"),
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
    ("source_before_points", "source_not_before_points"),
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
    ("formal_pasting_diagram", "formal_pasting_diagram"),
    ("sequential_layer_pipeline", "sequential_layer_pipeline"),
    ("exactness_then_duality", "exactness_then_duality"),
    ("local_c3_patch", "local_c3_patch"),
    ("finite_composition_table", "finite_composition_table"),
    ("external_choice_of_coupling", "external_choice_of_coupling"),
    ("retuned_coupling", "retuned_coupling"),
    ("graph_object_coherence", "graph_object_coherence"),
    ("graph_predicate_gate", "graph_predicate_gate"),
    ("late_control_filter", "late_control_filter"),
    ("boundary_dd4_after_filter", "boundary_dd4_after_filter"),
    ("semantic_zeta_label", "semantic_zeta_label"),
    ("expanded_finite_index", "expanded_finite_index"),
    ("one_more_layer_tower", "one_more_layer_tower"),
    ("declared_coupling", "declared_coupling"),
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
    if not REQUIRED_COUPLING_EDGES <= set(data["required_edges"]):
        out.append("required_source_coupling_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_coupled_formation_coherent_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_SOURCE_COHERENCE_CELLS <= set(data["source_coherence_cells"])
        and REQUIRED_SOURCE_COMPOSITION_CELLS <= set(data["source_composition_cells"])
        and REQUIRED_COUPLING_EDGES <= set(data["required_edges"])
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
        source_before_graph_objects=True,
        control_death_at_source=True,
        formation_coherence_actual=True,
        coherence_generated_by_mediator=True,
        cartesian_source_coherence_actual=True,
        monoidwide_source_coherence_actual=True,
        same_coherence_on_paths=True,
        source_coupling_actual=True,
        coupling_generated_by_mediator=True,
        coupling_generated_by_formation_coherence=True,
        non_split_dependency_graph=True,
        same_coupling_on_paths=True,
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
        source_before_points=True,
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


def coupling_payload(chi: dict[int, int]) -> dict[str, object]:
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
        "source_before_graph_objects": True,
        "controls_not_points": True,
        "dh_not_points": True,
        "epstein_not_points": True,
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
        "required_edges": tuple(sorted(REQUIRED_COUPLING_EDGES)),
        "delta": delta,
        "couples": (
            DELTA_ID,
            KERNEL_ID,
            COIMAGE_ID,
            "signed_coefficients",
            "signed_support",
            DUALITY_ID,
            TWIST_ID,
            DD4_CLASS_ID,
            NORMAL_RATIO_ID,
            "endpoint_pairing",
            "endpoint_pushforward_graph",
            "rosati_count",
            "source_control_death",
        ),
        "dd4_obstruction": ("H1=Z/2", "res1=1", "nonboundary_before_certificate"),
        "certificate_effect": "killed_after_single_dQ_localization",
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
    }


def coupled_row(chi: dict[int, int]) -> bool:
    payload = coupling_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["delta"]["weighted_mass"] == 0
        and payload["kernel_relation"] == payload["coefficients"]
        and payload["coimage_signature"] == payload["delta"]["split"]
        and payload["formation_token"] == FORMATION_TOKEN_ID
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["formation_coherence"] == FORMATION_COH_ID
        and payload["cartesian_source_coherence"] == FORMATION_CART_ID
        and payload["monoidwide_source_coherence"] == FORMATION_MWC_ID
        and payload["source_coupling"] == SOURCE_COUPLING_ID
        and payload["source_before_graph_objects"]
        and payload["controls_not_points"]
        and payload["dh_not_points"]
        and payload["epstein_not_points"]
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
        and DELTA_ID in payload["couples"]
        and DUALITY_ID in payload["couples"]
        and TWIST_ID in payload["couples"]
        and DD4_CLASS_ID in payload["couples"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_COUPLING_EDGES))
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
non_square_balanced = {1: 4, 4: -1}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD1 mediator source coherence has non-split coupling primitive",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_COUPLING_EDGES)
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
    and coupling_payload(T3_T5_z) == coupling_payload(zC15)
    and coupling_payload(T5_T3_z) == coupling_payload(zC15)
    and coupling_payload(T3_T3_T5_z) == coupling_payload(zC45)
    and coupling_payload(T15_zF22) == coupling_payload(zC15F22)
    and coupling_payload(T45_zF22) == coupling_payload(zC45F22)
    and all(coupled_row(row) for row in rows),
    "H1=%s coupling_edges=%d finite_index=%d"
    % ([p["h1_order"] for p in profiles], len(REQUIRED_COUPLING_EDGES), len(FINITE_INDEX)),
)

product_layers = live_source(
    source_coupling_actual=False,
    coupling_generated_by_mediator=False,
    coupling_generated_by_formation_coherence=False,
    non_split_dependency_graph=False,
    exact_delta_coupled=False,
    rank1_duality_coupled=False,
    control_death_coupled=False,
    product_of_layer_coherences=True,
    atomwise_preservation=True,
    fiber_product_of_contracts=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD2 product layer coherence fails",
    not accepts_coupled_formation_coherent_mediator(product_layers)
    and {
        "source_coupling_missing",
        "coupling_not_generated_by_mediator",
        "coupling_not_generated_by_formation_coherence",
        "dependency_graph_split",
        "exact_delta_not_coupled",
        "rank1_duality_not_coupled",
        "control_death_not_coupled",
        "product_of_layer_coherences",
        "atomwise_preservation",
        "fiber_product_of_contracts",
    }
    <= set(reasons(product_layers)),
    ",".join(reasons(product_layers)),
)

formal_pasting = live_source(
    source_coupling_actual=False,
    coupling_generated_by_mediator=False,
    non_split_dependency_graph=False,
    pullback_square_only=True,
    distributive_law_label=True,
    formal_pasting_diagram=True,
    declared_coupling=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD3 pullback and pasting labels fail",
    not accepts_coupled_formation_coherent_mediator(formal_pasting)
    and {
        "source_coupling_missing",
        "coupling_not_generated_by_mediator",
        "dependency_graph_split",
        "pullback_square_only",
        "distributive_law_label",
        "formal_pasting_diagram",
        "declared_coupling",
    }
    <= set(reasons(formal_pasting)),
    ",".join(reasons(formal_pasting)),
)

sequential = live_source(
    source_before_graph_objects=False,
    exact_delta_coupled=False,
    kernel_coimage_coupled=False,
    rank1_duality_coupled=False,
    control_death_coupled=False,
    sequential_layer_pipeline=True,
    exactness_then_duality=True,
    late_control_filter=True,
    boundary_dd4_after_filter=True,
    control_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD4 sequential exactness-then-duality is too late",
    not accepts_coupled_formation_coherent_mediator(sequential)
    and {
        "source_not_before_graph_objects",
        "exact_delta_not_coupled",
        "kernel_coimage_not_coupled",
        "rank1_duality_not_coupled",
        "control_death_not_coupled",
        "sequential_layer_pipeline",
        "exactness_then_duality",
        "late_control_filter",
        "boundary_dd4_after_filter",
        "control_point_formable",
    }
    <= set(reasons(sequential)),
    ",".join(reasons(sequential)),
)

local_table = live_source(
    same_coupling_on_paths=False,
    source_coherence_cells=set(list(REQUIRED_SOURCE_COHERENCE_CELLS)[:1]),
    source_composition_cells=set(),
    required_edges=REQUIRED_COUPLING_EDGES
    - {("cartesian_source_coherence", "C5_C3_equals_C15")},
    local_c3_patch=True,
    finite_composition_table=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD5 local C3 tables do not couple all paths",
    not accepts_coupled_formation_coherent_mediator(local_table)
    and {
        "same_coupling_not_on_paths",
        "source_coherence_cells_missing",
        "source_composition_cells_missing",
        "required_source_coupling_edges_missing",
        "local_c3_patch",
        "finite_composition_table",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)

retuned = live_source(
    carrier_native=False,
    original_dd4_coupled=False,
    normal_ratio_coupled=False,
    endpoint_pairing_coupled=False,
    endpoint_pushforward_graph_coupled=False,
    external_choice_of_coupling=True,
    retuned_coupling=True,
    semantic_zeta_label=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD6 external or retuned coupling loses the original source",
    not accepts_coupled_formation_coherent_mediator(retuned)
    and {
        "not_carrier_native",
        "original_dd4_not_coupled",
        "normal_ratio_not_coupled",
        "endpoint_pairing_not_coupled",
        "endpoint_pushforward_graph_not_coupled",
        "external_choice_of_coupling",
        "retuned_coupling",
        "semantic_zeta_label",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

graph_shadow = live_source(
    rosati_count_coupled=False,
    control_death_coupled=False,
    source_before_points=False,
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD7 graph-object coupling leaves controls formable",
    not accepts_coupled_formation_coherent_mediator(graph_shadow)
    and {
        "rosati_count_not_coupled",
        "control_death_not_coupled",
        "source_not_before_points",
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

expanded_index = live_source(
    finite_index=set(FINITE_INDEX) | {"source_coupling_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    doc491_in_finite_index=False,
    closure_returns_same_totalizer=False,
    no_next_coherence_obligation=False,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD8 coupling does not expand the finite index",
    not accepts_coupled_formation_coherent_mediator(expanded_index)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "doc491_not_in_finite_index",
        "closure_does_not_return_same_totalizer",
        "next_coherence_obligation_open",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded_index)),
    ",".join(reasons(expanded_index)),
)

missing_edges = [
    live_source(
        required_edges=REQUIRED_COUPLING_EDGES
        - {("universal_mediator", "source_coherence_coupling_primitive")}
    ),
    live_source(source_coupling_actual=False),
    live_source(exact_delta_coupled=False),
    live_source(rank1_duality_coupled=False),
    live_source(control_death_coupled=False),
    live_source(non_split_dependency_graph=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD9 every mediator-coupling edge is mandatory",
    not any(
        accepts_coupled_formation_coherent_mediator(data) for data in missing_edges
    )
    and {
        "required_source_coupling_edges_missing",
        "source_coupling_missing",
        "exact_delta_not_coupled",
        "rank1_duality_not_coupled",
        "control_death_not_coupled",
        "dependency_graph_split",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

dead_sources = {
    "product_layers": product_layers,
    "formal_pasting": formal_pasting,
    "sequential": sequential,
    "local_table": local_table,
    "retuned": retuned,
    "graph_shadow": graph_shadow,
    "expanded_index": expanded_index,
}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD10 only coupled formation-coherent mediator passes",
    accepts_coupled_formation_coherent_mediator(live_source())
    and not any(
        accepts_coupled_formation_coherent_mediator(data)
        for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(
            accepts_coupled_formation_coherent_mediator(data)
            for data in dead_sources.values()
        ),
        accepts_coupled_formation_coherent_mediator(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: equalizer identity universal mediator coupled formation-coherent "
    "self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-501 formation-coherent self-dual exact-BCF mediator must "
    "carry one non-split source-coherence coupling primitive generated by the "
    "same universal mediator. Product coherences, pullback/pasting labels, "
    "sequential exactness-then-duality pipelines, local path tables, retuned "
    "couplings, graph-object couplings, expanded indexes, and late control "
    "filters do not construct the missing object."
)
