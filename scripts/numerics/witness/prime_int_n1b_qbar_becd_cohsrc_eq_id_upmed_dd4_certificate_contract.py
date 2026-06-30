r"""DD.4-certificate contract for the equalizer-identity mediator.

Doc 496 makes the source finite-limit universal mediator for id_Eq natural
for the multiplier action.  This witness pins the next edge: that same
mediator naturality must carry the original DD.4 boundary certificate and
preserve the nonzero res_1(c)=1 class before the certificate kills it.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_dd4_certificate_contract
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

REQUIRED_DD4_NATURALITY_CELLS = {
    "dd4_cert_nat_C3_med_UP_Eq_id",
    "dd4_cert_nat_C5_med_UP_Eq_id",
    "dd4_cert_nat_C15_med_UP_Eq_id",
    "dd4_cert_nat_C45_med_UP_Eq_id",
    "dd4_cert_nat_F22_med_UP_Eq_id",
}

REQUIRED_DD4_COMPOSITION_CELLS = {
    "dd4_cert_cell_C3_C5_C15_med_UP_Eq_id",
    "dd4_cert_cell_C5_C3_C15_med_UP_Eq_id",
    "dd4_cert_cell_C3_C3_C5_C45_med_UP_Eq_id",
    "dd4_cert_cell_F22_product_med_UP_Eq_id",
}

REQUIRED_CERT_EDGES = {
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
    ("upmed_dd4_naturality", "dd4_original_class"),
    ("dd4_original_class", "dd4_res1_preserved"),
    ("dd4_original_class", "dd4_nonboundary_preserved"),
    ("dd4_res1_preserved", "res1_equals_one_before_certificate"),
    ("dd4_nonboundary_preserved", "not_coboundary_before_certificate"),
    ("upmed_dd4_naturality", "dd4_certificate_naturality_cells"),
    ("dd4_certificate_naturality_cells", "dd4_cert_nat_C3_med_UP_Eq_id"),
    ("dd4_certificate_naturality_cells", "dd4_cert_nat_C5_med_UP_Eq_id"),
    ("dd4_certificate_naturality_cells", "dd4_cert_nat_C15_med_UP_Eq_id"),
    ("dd4_certificate_naturality_cells", "dd4_cert_nat_C45_med_UP_Eq_id"),
    ("dd4_certificate_naturality_cells", "dd4_cert_nat_F22_med_UP_Eq_id"),
    ("upmed_dd4_naturality", "dd4_certificate_composition_cells"),
    ("dd4_certificate_composition_cells", "dd4_cert_cell_C3_C5_C15_med_UP_Eq_id"),
    ("dd4_certificate_composition_cells", "dd4_cert_cell_C5_C3_C15_med_UP_Eq_id"),
    ("dd4_certificate_composition_cells", "dd4_cert_cell_C3_C3_C5_C45_med_UP_Eq_id"),
    ("dd4_certificate_composition_cells", "dd4_cert_cell_F22_product_med_UP_Eq_id"),
    ("old_boundary_certificate", "dQ_localization"),
    ("dQ_localization", "certificate_kills_class"),
    ("old_boundary_certificate", "ordered_normal_ratio"),
    ("ordered_normal_ratio", "self_dual_boundary"),
    ("upmed_dd4_certificate", "same_certificate_on_multiplier_paths"),
    ("same_certificate_on_multiplier_paths", "C3_C5_equals_C15"),
    ("same_certificate_on_multiplier_paths", "C5_C3_equals_C15"),
    ("same_certificate_on_multiplier_paths", "C3_C3_C5_equals_C45"),
    ("same_certificate_on_multiplier_paths", "F22_product_interchange"),
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
        "dd4_class_actual": False,
        "dd4_res1_preserved": False,
        "dd4_nonboundary_preserved": False,
        "old_boundary_certificate_actual": False,
        "dd4_certificate_handoff_actual": False,
        "upmed_dd4_certificate_actual": False,
        "upmed_dd4_naturality_actual": False,
        "certificate_kills_class": False,
        "localization_actual": False,
        "normal_ratio_actual": False,
        "self_dual_boundary_actual": False,
        "same_certificate_on_paths": False,
        "doc491_modification_actual": False,
        "doc491_boundary_actual": False,
        "doc491_cells": set(),
        "doc491_faces": set(),
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "doc491_in_finite_index": False,
        "dd4_naturality_cells": set(),
        "dd4_composition_cells": set(),
        "closure_returns_same_totalizer": False,
        "no_next_coherence_obligation": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "coefficient_only_naturality": False,
        "dd4_label_only": False,
        "posthoc_certificate_handoff": False,
        "local_path_certificates": False,
        "res1_forgetting": False,
        "coboundary_relabel": False,
        "new_certificate_copy": False,
        "boundary_after_mediator": False,
        "external_certificate": False,
        "graph_side_certificate": False,
        "pointwise_certificate": False,
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
    ("dd4_class_actual", "dd4_class_missing"),
    ("dd4_res1_preserved", "dd4_res1_not_preserved"),
    ("dd4_nonboundary_preserved", "dd4_nonboundary_not_preserved"),
    ("old_boundary_certificate_actual", "old_boundary_certificate_missing"),
    ("dd4_certificate_handoff_actual", "dd4_certificate_handoff_missing"),
    ("upmed_dd4_certificate_actual", "upmed_dd4_certificate_missing"),
    ("upmed_dd4_naturality_actual", "upmed_dd4_naturality_missing"),
    ("certificate_kills_class", "certificate_does_not_kill_class"),
    ("localization_actual", "localization_missing"),
    ("normal_ratio_actual", "normal_ratio_missing"),
    ("self_dual_boundary_actual", "self_dual_boundary_missing"),
    ("same_certificate_on_paths", "certificate_not_path_independent"),
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
    ("coefficient_only_naturality", "coefficient_only_naturality"),
    ("dd4_label_only", "dd4_label_only"),
    ("posthoc_certificate_handoff", "posthoc_certificate_handoff"),
    ("local_path_certificates", "local_path_certificates"),
    ("res1_forgetting", "res1_forgetting"),
    ("coboundary_relabel", "coboundary_relabel"),
    ("new_certificate_copy", "new_certificate_copy"),
    ("boundary_after_mediator", "boundary_after_mediator"),
    ("external_certificate", "external_certificate"),
    ("graph_side_certificate", "graph_side_certificate"),
    ("pointwise_certificate", "pointwise_certificate"),
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
    if not REQUIRED_DD4_NATURALITY_CELLS <= set(data["dd4_naturality_cells"]):
        out.append("dd4_naturality_cells_missing")
    if not REQUIRED_DD4_COMPOSITION_CELLS <= set(data["dd4_composition_cells"]):
        out.append("dd4_composition_cells_missing")
    if not REQUIRED_CERT_EDGES <= set(data["required_edges"]):
        out.append("required_cert_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_dd4_certificate(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_DOC491_CELLS <= set(data["doc491_cells"])
        and REQUIRED_DOC491_FACES <= set(data["doc491_faces"])
        and REQUIRED_DD4_NATURALITY_CELLS <= set(data["dd4_naturality_cells"])
        and REQUIRED_DD4_COMPOSITION_CELLS <= set(data["dd4_composition_cells"])
        and REQUIRED_CERT_EDGES <= set(data["required_edges"])
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
        dd4_class_actual=True,
        dd4_res1_preserved=True,
        dd4_nonboundary_preserved=True,
        old_boundary_certificate_actual=True,
        dd4_certificate_handoff_actual=True,
        upmed_dd4_certificate_actual=True,
        upmed_dd4_naturality_actual=True,
        certificate_kills_class=True,
        localization_actual=True,
        normal_ratio_actual=True,
        self_dual_boundary_actual=True,
        same_certificate_on_paths=True,
        doc491_modification_actual=True,
        doc491_boundary_actual=True,
        doc491_cells=set(REQUIRED_DOC491_CELLS),
        doc491_faces=set(REQUIRED_DOC491_FACES),
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        doc491_in_finite_index=True,
        dd4_naturality_cells=set(REQUIRED_DD4_NATURALITY_CELLS),
        dd4_composition_cells=set(REQUIRED_DD4_COMPOSITION_CELLS),
        closure_returns_same_totalizer=True,
        no_next_coherence_obligation=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CERT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def dd4_certificate_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
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
        "localization": LOCALIZATION_ID,
        "normal_ratio": NORMAL_RATIO_ID,
        "finite_index": FINITE_INDEX_ID,
        "doc491_modification": DOC491_MODIFICATION_ID,
        "doc491_boundary": DOC491_BOUNDARY_ID,
        "dd4_naturality_cells": tuple(sorted(REQUIRED_DD4_NATURALITY_CELLS)),
        "dd4_composition_cells": tuple(sorted(REQUIRED_DD4_COMPOSITION_CELLS)),
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "doc491_cells": tuple(sorted(REQUIRED_DOC491_CELLS)),
        "doc491_faces": tuple(sorted(REQUIRED_DOC491_FACES)),
        "endpoint_boundary": (p1, p2, p1 == p2),
        "dd4_obstruction": ("H1=Z/2", "res1=1", "nonboundary_before_certificate"),
        "certificate_effect": "killed_after_single_dQ_localization",
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD1 mediator naturality carries DD4 certificate",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CERT_EDGES)
    and len(FINITE_INDEX) == 24
    and len(REQUIRED_DOC491_CELLS) == 10
    and len(REQUIRED_DOC491_FACES) == 10
    and len(REQUIRED_DD4_NATURALITY_CELLS) == 5
    and len(REQUIRED_DD4_COMPOSITION_CELLS) == 4
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and dd4_certificate_payload(T3_T5_z) == dd4_certificate_payload(zC15)
    and dd4_certificate_payload(T5_T3_z) == dd4_certificate_payload(zC15)
    and dd4_certificate_payload(T3_T3_T5_z) == dd4_certificate_payload(zC45)
    and dd4_certificate_payload(T15_zF22) == dd4_certificate_payload(zC15F22)
    and dd4_certificate_payload(T45_zF22) == dd4_certificate_payload(zC45F22),
    "H1=%s dd4_nat=%d dd4_comp=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(REQUIRED_DD4_NATURALITY_CELLS),
        len(REQUIRED_DD4_COMPOSITION_CELLS),
    ),
)

coeff_only = live_source(
    dd4_class_actual=False,
    dd4_res1_preserved=False,
    dd4_nonboundary_preserved=False,
    upmed_dd4_certificate_actual=False,
    coefficient_only_naturality=True,
    dd4_label_only=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD2 coefficient-only or label-only naturality fails",
    not accepts_dd4_certificate(coeff_only)
    and {
        "dd4_class_missing",
        "dd4_res1_not_preserved",
        "dd4_nonboundary_not_preserved",
        "upmed_dd4_certificate_missing",
        "coefficient_only_naturality",
        "dd4_label_only",
    }
    <= set(reasons(coeff_only)),
    ",".join(reasons(coeff_only)),
)

posthoc = live_source(
    dd4_certificate_handoff_actual=False,
    old_boundary_certificate_actual=False,
    certificate_kills_class=False,
    localization_actual=False,
    posthoc_certificate_handoff=True,
    boundary_after_mediator=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD3 posthoc certificate handoffs fail",
    not accepts_dd4_certificate(posthoc)
    and {
        "old_boundary_certificate_missing",
        "dd4_certificate_handoff_missing",
        "certificate_does_not_kill_class",
        "localization_missing",
        "posthoc_certificate_handoff",
        "boundary_after_mediator",
    }
    <= set(reasons(posthoc)),
    ",".join(reasons(posthoc)),
)

local_certs = live_source(
    upmed_dd4_naturality_actual=False,
    same_certificate_on_paths=False,
    dd4_naturality_cells=set(list(REQUIRED_DD4_NATURALITY_CELLS)[:-1]),
    dd4_composition_cells=set(list(REQUIRED_DD4_COMPOSITION_CELLS)[:-1]),
    local_path_certificates=True,
    new_certificate_copy=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD4 local path certificates fail",
    not accepts_dd4_certificate(local_certs)
    and {
        "upmed_dd4_naturality_missing",
        "certificate_not_path_independent",
        "dd4_naturality_cells_missing",
        "dd4_composition_cells_missing",
        "local_path_certificates",
        "new_certificate_copy",
    }
    <= set(reasons(local_certs)),
    ",".join(reasons(local_certs)),
)

forgot_res1 = live_source(
    dd4_res1_preserved=False,
    dd4_nonboundary_preserved=False,
    certificate_kills_class=False,
    res1_forgetting=True,
    coboundary_relabel=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD5 res1-forgetting and coboundary relabels fail",
    not accepts_dd4_certificate(forgot_res1)
    and {
        "dd4_res1_not_preserved",
        "dd4_nonboundary_not_preserved",
        "certificate_does_not_kill_class",
        "res1_forgetting",
        "coboundary_relabel",
    }
    <= set(reasons(forgot_res1)),
    ",".join(reasons(forgot_res1)),
)

external = live_source(
    carrier_native=False,
    source_before_points=False,
    upmed_dd4_certificate_actual=False,
    external_certificate=True,
    graph_side_certificate=True,
    pointwise_certificate=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD6 external graph or pointwise certificates fail",
    not accepts_dd4_certificate(external)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "upmed_dd4_certificate_missing",
        "external_certificate",
        "graph_side_certificate",
        "pointwise_certificate",
    }
    <= set(reasons(external)),
    ",".join(reasons(external)),
)

expanded = live_source(
    finite_index=set(FINITE_INDEX) | {"upmed_dd4_certificate_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD7 expanded indexes and towers fail",
    not accepts_dd4_certificate(expanded)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded)),
    ",".join(reasons(expanded)),
)

missing_spine = live_source(
    product_actual=False,
    alpha_actual=False,
    beta_actual=False,
    equalizer_actual=False,
    doc491_modification_actual=False,
    doc491_boundary_actual=False,
    doc491_cells=set(list(REQUIRED_DOC491_CELLS)[:-1]),
    doc491_faces=set(list(REQUIRED_DOC491_FACES)[:-1]),
    required_edges=REQUIRED_CERT_EDGES - {("dd4_certificate_handoff", "old_boundary_certificate")},
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD8 finite-limit spine and doc491 payload remain mandatory",
    not accepts_dd4_certificate(missing_spine)
    and {
        "product_missing",
        "alpha_missing",
        "beta_missing",
        "equalizer_missing",
        "doc491_modification_missing",
        "doc491_boundary_missing",
        "doc491_cells_missing",
        "doc491_faces_missing",
        "required_cert_edges_missing",
    }
    <= set(reasons(missing_spine)),
    ",".join(reasons(missing_spine)),
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD9 control/DH/Epstein certificates fail",
    not accepts_dd4_certificate(control)
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
    live_source(required_edges=REQUIRED_CERT_EDGES - {edge})
    for edge in list(REQUIRED_CERT_EDGES)[:8]
] + [
    live_source(dd4_certificate_handoff_actual=False),
    live_source(upmed_dd4_certificate_actual=False),
    live_source(upmed_dd4_naturality_actual=False),
    live_source(same_certificate_on_paths=False),
    live_source(no_next_coherence_obligation=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD10 only DD4-certificate-carrying mediator passes",
    accepts_dd4_certificate(live_source())
    and not any(accepts_dd4_certificate(data) for data in missing_edges)
    and {
        "required_cert_edges_missing",
        "dd4_certificate_handoff_missing",
        "upmed_dd4_certificate_missing",
        "upmed_dd4_naturality_missing",
        "certificate_not_path_independent",
        "next_coherence_obligation_open",
    }
    <= missing_reasons,
    "missing=%s live accepted=%s"
    % (sorted(missing_reasons), accepts_dd4_certificate(live_source())),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD10 ALL PASS: "
    "equalizer identity universal mediator DD4 certificate pinned"
)
print(
    "VERDICT: the doc-496 multiplier-natural universal mediator for id_Eq "
    "must carry the original DD.4 boundary certificate, preserving the "
    "nonzero res_1(c)=1 class before the same certificate kills it. "
    "Coefficient-only naturality, DD.4 labels, posthoc handoffs, local path "
    "certificates, res1-forgetting, external/graph/pointwise certificates, "
    "expanded indexes, and control/DH/Epstein point-formability do not "
    "construct the missing object."
)
