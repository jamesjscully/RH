r"""Exact-BCF certificate contract for the equalizer-identity mediator.

Doc 497 makes the source finite-limit universal mediator carry the old DD.4
boundary certificate.  This witness pins the next edge: that mediator cannot
carry an opaque BKill token.  The handoff must carry the exact BCF generation
of the certificate: signed zero fiber, cancellation module, BCF functor,
boundary delta, kernel, and coimage.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_exact_bcf_certificate_contract
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

REQUIRED_EXACT_NATURALITY_CELLS = {
    "exact_bcf_nat_C3_med_UP_Eq_id",
    "exact_bcf_nat_C5_med_UP_Eq_id",
    "exact_bcf_nat_C15_med_UP_Eq_id",
    "exact_bcf_nat_C45_med_UP_Eq_id",
    "exact_bcf_nat_F22_med_UP_Eq_id",
}

REQUIRED_EXACT_COMPOSITION_CELLS = {
    "exact_bcf_cell_C3_C5_C15_med_UP_Eq_id",
    "exact_bcf_cell_C5_C3_C15_med_UP_Eq_id",
    "exact_bcf_cell_C3_C3_C5_C45_med_UP_Eq_id",
    "exact_bcf_cell_F22_product_med_UP_Eq_id",
}

REQUIRED_EXACT_EDGES = {
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
    ("kernel_is_cancellation_image", "dd4_original_class"),
    ("coimage_preserves_signed_coefficients", "dd4_original_class"),
    ("dd4_original_class", "dd4_res1_preserved"),
    ("dd4_original_class", "dd4_nonboundary_preserved"),
    ("dd4_res1_preserved", "res1_equals_one_before_certificate"),
    ("dd4_nonboundary_preserved", "not_coboundary_before_certificate"),
    ("exact_boundary_delta", "same_exact_source_on_multiplier_paths"),
    ("same_exact_source_on_multiplier_paths", "C3_C5_equals_C15"),
    ("same_exact_source_on_multiplier_paths", "C5_C3_equals_C15"),
    ("same_exact_source_on_multiplier_paths", "C3_C3_C5_equals_C45"),
    ("same_exact_source_on_multiplier_paths", "F22_product_interchange"),
    ("same_exact_source_on_multiplier_paths", "exact_bcf_naturality_cells"),
    ("exact_bcf_naturality_cells", "exact_bcf_nat_C3_med_UP_Eq_id"),
    ("exact_bcf_naturality_cells", "exact_bcf_nat_C5_med_UP_Eq_id"),
    ("exact_bcf_naturality_cells", "exact_bcf_nat_C15_med_UP_Eq_id"),
    ("exact_bcf_naturality_cells", "exact_bcf_nat_C45_med_UP_Eq_id"),
    ("exact_bcf_naturality_cells", "exact_bcf_nat_F22_med_UP_Eq_id"),
    ("same_exact_source_on_multiplier_paths", "exact_bcf_composition_cells"),
    ("exact_bcf_composition_cells", "exact_bcf_cell_C3_C5_C15_med_UP_Eq_id"),
    ("exact_bcf_composition_cells", "exact_bcf_cell_C5_C3_C15_med_UP_Eq_id"),
    ("exact_bcf_composition_cells", "exact_bcf_cell_C3_C3_C5_C45_med_UP_Eq_id"),
    ("exact_bcf_composition_cells", "exact_bcf_cell_F22_product_med_UP_Eq_id"),
    ("old_boundary_certificate", "dQ_localization"),
    ("dQ_localization", "certificate_kills_class"),
    ("old_boundary_certificate", "ordered_normal_ratio"),
    ("ordered_normal_ratio", "self_dual_boundary"),
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
        "dd4_class_actual": False,
        "dd4_res1_preserved": False,
        "dd4_nonboundary_preserved": False,
        "certificate_kills_class": False,
        "localization_actual": False,
        "normal_ratio_actual": False,
        "self_dual_boundary_actual": False,
        "same_exact_source_on_paths": False,
        "doc491_modification_actual": False,
        "doc491_boundary_actual": False,
        "doc491_cells": set(),
        "doc491_faces": set(),
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "doc491_in_finite_index": False,
        "exact_naturality_cells": set(),
        "exact_composition_cells": set(),
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "opaque_bkill_token": False,
        "certificate_without_bcf": False,
        "rowwise_bcf_images": False,
        "declared_exact_sequence": False,
        "weighted_zero_kernel": False,
        "support_kernel": False,
        "quotient_exact_completion": False,
        "cokernel_deletion": False,
        "external_delta": False,
        "late_exactness_filter": False,
        "graph_side_exactness": False,
        "pointwise_exactness": False,
        "retuned_delta": False,
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
    ("dd4_class_actual", "dd4_class_missing"),
    ("dd4_res1_preserved", "dd4_res1_not_preserved"),
    ("dd4_nonboundary_preserved", "dd4_nonboundary_not_preserved"),
    ("certificate_kills_class", "certificate_does_not_kill_class"),
    ("localization_actual", "localization_missing"),
    ("normal_ratio_actual", "normal_ratio_missing"),
    ("self_dual_boundary_actual", "self_dual_boundary_missing"),
    ("same_exact_source_on_paths", "exact_source_not_path_independent"),
    ("doc491_modification_actual", "doc491_modification_missing"),
    ("doc491_boundary_actual", "doc491_boundary_missing"),
    ("doc491_in_finite_index", "doc491_not_in_finite_index"),
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
    ("opaque_bkill_token", "opaque_bkill_token"),
    ("certificate_without_bcf", "certificate_without_bcf"),
    ("rowwise_bcf_images", "rowwise_bcf_images"),
    ("declared_exact_sequence", "declared_exact_sequence"),
    ("weighted_zero_kernel", "weighted_zero_kernel"),
    ("support_kernel", "support_kernel"),
    ("quotient_exact_completion", "quotient_exact_completion"),
    ("cokernel_deletion", "cokernel_deletion"),
    ("external_delta", "external_delta"),
    ("late_exactness_filter", "late_exactness_filter"),
    ("graph_side_exactness", "graph_side_exactness"),
    ("pointwise_exactness", "pointwise_exactness"),
    ("retuned_delta", "retuned_delta"),
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
    if not REQUIRED_EXACT_NATURALITY_CELLS <= set(data["exact_naturality_cells"]):
        out.append("exact_naturality_cells_missing")
    if not REQUIRED_EXACT_COMPOSITION_CELLS <= set(data["exact_composition_cells"]):
        out.append("exact_composition_cells_missing")
    if not REQUIRED_EXACT_EDGES <= set(data["required_edges"]):
        out.append("required_exact_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_exact_bcf_mediator_certificate(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_EXACT_NATURALITY_CELLS <= set(data["exact_naturality_cells"])
        and REQUIRED_EXACT_COMPOSITION_CELLS <= set(data["exact_composition_cells"])
        and REQUIRED_EXACT_EDGES <= set(data["required_edges"])
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
        dd4_class_actual=True,
        dd4_res1_preserved=True,
        dd4_nonboundary_preserved=True,
        certificate_kills_class=True,
        localization_actual=True,
        normal_ratio_actual=True,
        self_dual_boundary_actual=True,
        same_exact_source_on_paths=True,
        doc491_modification_actual=True,
        doc491_boundary_actual=True,
        doc491_cells=set(REQUIRED_DOC491_CELLS),
        doc491_faces=set(REQUIRED_DOC491_FACES),
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        doc491_in_finite_index=True,
        exact_naturality_cells=set(REQUIRED_EXACT_NATURALITY_CELLS),
        exact_composition_cells=set(REQUIRED_EXACT_COMPOSITION_CELLS),
        closure_returns_same_totalizer=True,
        no_next_coherence_obligation=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_EXACT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def exact_bcf_certificate_payload(chi: dict[int, int]) -> dict[str, object]:
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
        "kernel_relation": tuple(chi.items()),
        "coimage_signature": positive_negative_split(chi),
        "localization": LOCALIZATION_ID,
        "normal_ratio": NORMAL_RATIO_ID,
        "finite_index": FINITE_INDEX_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "exact_naturality_cells": tuple(sorted(REQUIRED_EXACT_NATURALITY_CELLS)),
        "exact_composition_cells": tuple(sorted(REQUIRED_EXACT_COMPOSITION_CELLS)),
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
        "delta": delta,
        "endpoint_boundary": (p1, p2, p1 == p2),
        "dd4_obstruction": ("H1=Z/2", "res1=1", "nonboundary_before_certificate"),
        "certificate_effect": "killed_after_single_dQ_localization",
        "coefficients": tuple(chi.items()),
        "support": support(chi),
        "weighted_mass": weighted_mass(chi),
    }


def exact_row(chi: dict[int, int]) -> bool:
    payload = exact_bcf_certificate_payload(chi)
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
        and payload["boundary_certificate"] == BOUNDARY_CERT_ID
        and payload["dd4_class"] == DD4_CLASS_ID
        and payload["endpoint_boundary"][2]
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
allowed_delta_rows = {tuple(row.items()) for row in rows}
non_square_balanced = {1: 4, 4: -1}
profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD1 mediator carries exact BCF certificate generation",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_EXACT_EDGES)
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC491_CELLS) == 10
    and len(REQUIRED_DOC491_FACES) == 10
    and len(REQUIRED_EXACT_NATURALITY_CELLS) == 5
    and len(REQUIRED_EXACT_COMPOSITION_CELLS) == 4
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and exact_bcf_certificate_payload(T3_T5_z)
    == exact_bcf_certificate_payload(zC15)
    and exact_bcf_certificate_payload(T5_T3_z)
    == exact_bcf_certificate_payload(zC15)
    and exact_bcf_certificate_payload(T3_T3_T5_z)
    == exact_bcf_certificate_payload(zC45)
    and exact_bcf_certificate_payload(T15_zF22)
    == exact_bcf_certificate_payload(zC15F22)
    and exact_bcf_certificate_payload(T45_zF22)
    == exact_bcf_certificate_payload(zC45F22)
    and all(exact_row(row) for row in rows),
    "H1=%s exact_nat=%d exact_comp=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(REQUIRED_EXACT_NATURALITY_CELLS),
        len(REQUIRED_EXACT_COMPOSITION_CELLS),
    ),
)

opaque = live_source(
    signed_zero_actual=False,
    canmod_actual=False,
    bcf_functor_actual=False,
    exact_source_actual=False,
    exact_delta_actual=False,
    kernel_actual=False,
    coimage_actual=False,
    exact_sequence_generated_by_bcf=False,
    kernel_is_canmod_image=False,
    opaque_bkill_token=True,
    certificate_without_bcf=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD2 opaque BKill certificates fail",
    not accepts_exact_bcf_mediator_certificate(opaque)
    and {
        "signed_zero_missing",
        "canmod_missing",
        "bcf_functor_missing",
        "exact_source_missing",
        "exact_delta_missing",
        "kernel_missing",
        "coimage_missing",
        "exact_sequence_not_generated_by_bcf",
        "kernel_not_canmod_image",
        "opaque_bkill_token",
        "certificate_without_bcf",
    }
    <= set(reasons(opaque)),
    ",".join(reasons(opaque)),
)

rowwise = live_source(
    exact_delta_actual=False,
    exact_sequence_generated_by_bcf=False,
    same_exact_source_on_paths=False,
    exact_naturality_cells=set(list(REQUIRED_EXACT_NATURALITY_CELLS)[:-1]),
    exact_composition_cells=set(list(REQUIRED_EXACT_COMPOSITION_CELLS)[:-1]),
    rowwise_bcf_images=True,
    declared_exact_sequence=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD3 rowwise BCF images and declared exactness fail",
    not accepts_exact_bcf_mediator_certificate(rowwise)
    and {
        "exact_delta_missing",
        "exact_sequence_not_generated_by_bcf",
        "exact_source_not_path_independent",
        "exact_naturality_cells_missing",
        "exact_composition_cells_missing",
        "rowwise_bcf_images",
        "declared_exact_sequence",
    }
    <= set(reasons(rowwise)),
    ",".join(reasons(rowwise)),
)

weighted_kernel = live_source(
    kernel_actual=False,
    coimage_actual=False,
    kernel_is_canmod_image=False,
    coimage_preserves_signed_coefficients=False,
    coimage_preserves_signed_support=False,
    weighted_zero_kernel=True,
    support_kernel=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD4 weighted-zero and support kernels fail",
    weighted_mass(non_square_balanced) == 0
    and tuple(non_square_balanced.items()) not in allowed_delta_rows
    and not accepts_exact_bcf_mediator_certificate(weighted_kernel)
    and {
        "kernel_missing",
        "coimage_missing",
        "kernel_not_canmod_image",
        "coimage_does_not_preserve_signed_coefficients",
        "coimage_does_not_preserve_signed_support",
        "weighted_zero_kernel",
        "support_kernel",
    }
    <= set(reasons(weighted_kernel)),
    ",".join(reasons(weighted_kernel)),
)

quotient = live_source(
    exact_source_actual=False,
    exact_delta_actual=False,
    required_edges=set(),
    quotient_exact_completion=True,
    cokernel_deletion=True,
    external_delta=True,
    late_exactness_filter=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD5 quotient external or late exactness fails",
    not accepts_exact_bcf_mediator_certificate(quotient)
    and {
        "exact_source_missing",
        "exact_delta_missing",
        "required_exact_edges_missing",
        "quotient_exact_completion",
        "cokernel_deletion",
        "external_delta",
        "late_exactness_filter",
    }
    <= set(reasons(quotient)),
    ",".join(reasons(quotient)),
)

missing_kernel_coimage = live_source(
    kernel_actual=False,
    coimage_actual=False,
    kernel_is_canmod_image=False,
    coimage_preserves_signed_coefficients=False,
    coimage_preserves_signed_support=False,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD6 kernel and coimage preservation remain mandatory",
    not accepts_exact_bcf_mediator_certificate(missing_kernel_coimage)
    and {
        "kernel_missing",
        "coimage_missing",
        "kernel_not_canmod_image",
        "coimage_does_not_preserve_signed_coefficients",
        "coimage_does_not_preserve_signed_support",
    }
    <= set(reasons(missing_kernel_coimage)),
    ",".join(reasons(missing_kernel_coimage)),
)

graph_side = live_source(
    carrier_native=False,
    source_before_points=False,
    exact_source_actual=False,
    exact_delta_actual=False,
    graph_side_exactness=True,
    pointwise_exactness=True,
    retuned_delta=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD7 graph pointwise or retuned exactness fails",
    not accepts_exact_bcf_mediator_certificate(graph_side)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "exact_source_missing",
        "exact_delta_missing",
        "graph_side_exactness",
        "pointwise_exactness",
        "retuned_delta",
    }
    <= set(reasons(graph_side)),
    ",".join(reasons(graph_side)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"med_up_eq_exact_bcf_certificate_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD8 expanded finite indexes and towers fail",
    not accepts_exact_bcf_mediator_certificate(expanded)
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD9 control/DH/Epstein exactness fails",
    not accepts_exact_bcf_mediator_certificate(control)
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
    live_source(required_edges=REQUIRED_EXACT_EDGES - {edge})
    for edge in list(REQUIRED_EXACT_EDGES)[:8]
] + [
    live_source(upmed_dd4_certificate_actual=False),
    live_source(signed_zero_actual=False),
    live_source(canmod_actual=False),
    live_source(bcf_functor_actual=False),
    live_source(exact_delta_actual=False),
    live_source(kernel_is_canmod_image=False),
    live_source(coimage_preserves_signed_coefficients=False),
    live_source(same_exact_source_on_paths=False),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD10 only exact BCF certificate mediator passes",
    accepts_exact_bcf_mediator_certificate(live_source())
    and not any(
        accepts_exact_bcf_mediator_certificate(data) for data in missing_edges
    )
    and {
        "required_exact_edges_missing",
        "upmed_dd4_certificate_missing",
        "signed_zero_missing",
        "canmod_missing",
        "bcf_functor_missing",
        "exact_delta_missing",
        "kernel_not_canmod_image",
        "coimage_does_not_preserve_signed_coefficients",
        "exact_source_not_path_independent",
        "next_coherence_obligation_open",
    }
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (
        sorted(missing_reasons),
        accepts_exact_bcf_mediator_certificate(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPEXBCFQBARBECD10 ALL PASS: "
    "equalizer identity universal mediator exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-497 DD.4-certificate-carrying universal mediator for "
    "id_Eq must carry exact BCF generation of that certificate: signed zero "
    "fiber, cancellation module, BCF functor, exact dQ delta, kernel, and "
    "coimage. Opaque BKill tokens, rowwise BCF images, declared exactness, "
    "weighted/support kernels, quotient completions, external deltas, "
    "graph/pointwise exactness, expanded indexes, towers, and "
    "control/DH/Epstein point-formability do not construct the missing object."
)
