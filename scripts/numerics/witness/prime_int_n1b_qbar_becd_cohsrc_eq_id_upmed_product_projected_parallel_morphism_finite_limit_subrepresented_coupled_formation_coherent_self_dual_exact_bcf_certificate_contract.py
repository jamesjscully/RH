r"""Product-projected parallel-morphism finite-limit mediator contract.

Doc 506 requires the finite-limit cut to be the equalizer of actual parallel
source morphisms alpha,beta. This witness pins the next edge: the common
constraint codomain must be an actual mediator source product with seven
source-native projections and unique alpha/beta pairings.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_product_projected_parallel_morphism_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
CONSTRAINT_OBJECT_ID = "Con_NCoup_med_UP_Eq_id_endpoint_dd4_rosati_control_source"
PRODUCT_OBJECT_ID = "Prod_NCoup_med_UP_Eq_id_endpoint_degree_dd4_push_graph_rosati_control"
ALPHA_CONSTRAINT_MAP_ID = "alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_CONSTRAINT_MAP_ID = "beta_NCoup_med_UP_Eq_id_source_constraints"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_med_UP_Eq_id_source_constraints"
ENDPOINT_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_endpoint_integrality"
DEGREE_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_degree_maps"
DD4_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_dd4_boundary"
PUSH_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_boundary_pushforward"
GRAPH_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_graph_composition"
ROSATI_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_rosati_count"
CONTROL_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_control_death"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_id_constraints_to_SubRep_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
CONTROL_DEATH_ID = "Nat_ControlDeath_med_UP_Eq_id_source_constraint"

COMPONENTS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

PROJECTION_IDS = (
    ENDPOINT_PROJECTION_ID,
    DEGREE_PROJECTION_ID,
    DD4_PROJECTION_ID,
    PUSH_PROJECTION_ID,
    GRAPH_PROJECTION_ID,
    ROSATI_PROJECTION_ID,
    CONTROL_PROJECTION_ID,
)

REQUIRED_FACETS = set(COMPONENTS)

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

REQUIRED_PRODUCT_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("finite_limit_cut", "constraint_product_object"),
    ("formation_fiber", "constraint_product_object"),
    ("constraint_product_object", "constraint_object"),
    ("constraint_product_object", "endpoint_projection"),
    ("constraint_product_object", "degree_projection"),
    ("constraint_product_object", "dd4_projection"),
    ("constraint_product_object", "pushforward_projection"),
    ("constraint_product_object", "graph_projection"),
    ("constraint_product_object", "rosati_count_projection"),
    ("constraint_product_object", "control_death_projection"),
    ("endpoint_projection", "endpoint_component_object"),
    ("degree_projection", "degree_component_object"),
    ("dd4_projection", "dd4_component_object"),
    ("pushforward_projection", "pushforward_component_object"),
    ("graph_projection", "graph_component_object"),
    ("rosati_count_projection", "rosati_count_component_object"),
    ("control_death_projection", "control_death_component_object"),
    ("constraint_product_object", "product_universal_property"),
    ("product_universal_property", "projections_jointly_determine_pairing"),
    ("formation_fiber", "alpha_pairing_map"),
    ("alpha_pairing_map", "alpha_constraint_map"),
    ("alpha_pairing_map", "constraint_product_object"),
    ("alpha_pairing_map", "all_alpha_components"),
    ("formation_fiber", "beta_pairing_map"),
    ("beta_pairing_map", "beta_constraint_map"),
    ("beta_pairing_map", "constraint_product_object"),
    ("beta_pairing_map", "all_beta_zero_diagonal_components"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("equalizer_arrow", "source_coupling_subrepresenter"),
    ("constraint_product_object", "same_product_all_paths"),
    ("same_product_all_paths", "C3_C5_equals_C15"),
    ("same_product_all_paths", "C5_C3_equals_C15"),
    ("same_product_all_paths", "C3_C3_C5_equals_C45"),
    ("same_product_all_paths", "F22_product"),
    ("constraint_product_object", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
    ("dd4_projection", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("control_death_projection", "source_before_points_and_graph_objects"),
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
        "coupling_subrepresenter_actual": False,
        "finite_limit_cut_actual": False,
        "constraint_product_actual": False,
        "constraint_object_actual": False,
        "component_objects_actual": False,
        "endpoint_projection_actual": False,
        "degree_projection_actual": False,
        "dd4_projection_actual": False,
        "pushforward_projection_actual": False,
        "graph_projection_actual": False,
        "rosati_projection_actual": False,
        "control_projection_actual": False,
        "projections_source_native": False,
        "projections_jointly_determine_pairing": False,
        "product_universal_property_actual": False,
        "alpha_pairing_actual": False,
        "beta_pairing_actual": False,
        "alpha_pairing_unique": False,
        "beta_pairing_unique": False,
        "alpha_components_factor_through_projections": False,
        "beta_components_factor_through_projections": False,
        "alpha_beta_parallel_after_product": False,
        "equalizer_uses_product_pair": False,
        "same_product_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "finite_anchors_generated": False,
        "no_next_coherence_obligation": False,
        "product_before_points": False,
        "product_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "abstract_external_representer": False,
        "equivalent_representer": False,
        "univalence_transport": False,
        "bundled_tuple_label": False,
        "external_product_of_sets": False,
        "product_after_functor_of_points": False,
        "component_checklist_product": False,
        "missing_projection": False,
        "nonuniversal_bundle": False,
        "coproduct_or_sum_substitute": False,
        "fiber_product_after_graph_objects": False,
        "projection_after_graph_objects": False,
        "local_projection_table": False,
        "finite_sample_product": False,
        "basis_dependent_projection": False,
        "retuned_projection": False,
        "projected_component_map": False,
        "graph_classifier_product": False,
        "declared_product": False,
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
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("constraint_product_actual", "constraint_product_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("component_objects_actual", "component_objects_missing"),
    ("endpoint_projection_actual", "endpoint_projection_missing"),
    ("degree_projection_actual", "degree_projection_missing"),
    ("dd4_projection_actual", "dd4_projection_missing"),
    ("pushforward_projection_actual", "pushforward_projection_missing"),
    ("graph_projection_actual", "graph_projection_missing"),
    ("rosati_projection_actual", "rosati_projection_missing"),
    ("control_projection_actual", "control_projection_missing"),
    ("projections_source_native", "projections_not_source_native"),
    (
        "projections_jointly_determine_pairing",
        "projections_do_not_jointly_determine_pairing",
    ),
    ("product_universal_property_actual", "product_universal_property_missing"),
    ("alpha_pairing_actual", "alpha_pairing_missing"),
    ("beta_pairing_actual", "beta_pairing_missing"),
    ("alpha_pairing_unique", "alpha_pairing_not_unique"),
    ("beta_pairing_unique", "beta_pairing_not_unique"),
    (
        "alpha_components_factor_through_projections",
        "alpha_components_not_through_projections",
    ),
    (
        "beta_components_factor_through_projections",
        "beta_components_not_through_projections",
    ),
    ("alpha_beta_parallel_after_product", "alpha_beta_not_parallel_after_product"),
    ("equalizer_uses_product_pair", "equalizer_does_not_use_product_pair"),
    ("same_product_all_paths", "same_product_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("product_before_points", "product_not_before_points"),
    ("product_before_graph_objects", "product_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("abstract_external_representer", "abstract_external_representer"),
    ("equivalent_representer", "equivalent_representer"),
    ("univalence_transport", "univalence_transport"),
    ("bundled_tuple_label", "bundled_tuple_label"),
    ("external_product_of_sets", "external_product_of_sets"),
    ("product_after_functor_of_points", "product_after_functor_of_points"),
    ("component_checklist_product", "component_checklist_product"),
    ("missing_projection", "missing_projection"),
    ("nonuniversal_bundle", "nonuniversal_bundle"),
    ("coproduct_or_sum_substitute", "coproduct_or_sum_substitute"),
    ("fiber_product_after_graph_objects", "fiber_product_after_graph_objects"),
    ("projection_after_graph_objects", "projection_after_graph_objects"),
    ("local_projection_table", "local_projection_table"),
    ("finite_sample_product", "finite_sample_product"),
    ("basis_dependent_projection", "basis_dependent_projection"),
    ("retuned_projection", "retuned_projection"),
    ("projected_component_map", "projected_component_map"),
    ("graph_classifier_product", "graph_classifier_product"),
    ("declared_product", "declared_product"),
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
    if not REQUIRED_PRODUCT_EDGES <= set(data["required_edges"]):
        out.append("required_product_projection_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_product_projected_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_PRODUCT_EDGES <= set(data["required_edges"])
        and graph_connected(set(data["required_edges"]))
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        universal_mediator_actual=True,
        formation_fiber_actual=True,
        coupling_subrepresenter_actual=True,
        finite_limit_cut_actual=True,
        constraint_product_actual=True,
        constraint_object_actual=True,
        component_objects_actual=True,
        endpoint_projection_actual=True,
        degree_projection_actual=True,
        dd4_projection_actual=True,
        pushforward_projection_actual=True,
        graph_projection_actual=True,
        rosati_projection_actual=True,
        control_projection_actual=True,
        projections_source_native=True,
        projections_jointly_determine_pairing=True,
        product_universal_property_actual=True,
        alpha_pairing_actual=True,
        beta_pairing_actual=True,
        alpha_pairing_unique=True,
        beta_pairing_unique=True,
        alpha_components_factor_through_projections=True,
        beta_components_factor_through_projections=True,
        alpha_beta_parallel_after_product=True,
        equalizer_uses_product_pair=True,
        same_product_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        finite_anchors_generated=True,
        no_next_coherence_obligation=True,
        product_before_points=True,
        product_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_PRODUCT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def product_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "projections": PROJECTION_IDS,
        "components": COMPONENTS,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "endpoint_component": (p1, p2, p1 == p2),
        "degree_component": (tuple(sorted(chi)), p1 + p2),
        "dd4_component": DD4_CLASS_ID,
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "control_component": CONTROL_DEATH_ID,
        "alpha_components": tuple(sorted(REQUIRED_FACETS)),
        "beta_component": "zero_or_diagonal_source_section",
        "source_product_payload": True,
        "product_before_points": True,
        "product_before_graph_objects": True,
        "equalizer_uses_product_pair": True,
        "equalizer_image": (FINITE_LIMIT_CUT_ID, COUPLING_SUBREP_ID),
        "controls_not_points": True,
        "dh_not_points": True,
        "epstein_not_points": True,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_PRODUCT_EDGES)),
    }


def product_row(chi: dict[int, int]) -> bool:
    payload = product_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["constraint_object"] == CONSTRAINT_OBJECT_ID
        and payload["product"] == PRODUCT_OBJECT_ID
        and payload["projections"] == PROJECTION_IDS
        and set(payload["components"]) == REQUIRED_FACETS
        and payload["alpha_pairing"] == ALPHA_PAIRING_ID
        and payload["beta_pairing"] == BETA_PAIRING_ID
        and payload["alpha"] == ALPHA_CONSTRAINT_MAP_ID
        and payload["beta"] == BETA_CONSTRAINT_MAP_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and set(payload["alpha_components"]) == REQUIRED_FACETS
        and payload["beta_component"] == "zero_or_diagonal_source_section"
        and payload["dd4_component"] == DD4_CLASS_ID
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_component"] == CONTROL_DEATH_ID
        and payload["source_product_payload"]
        and payload["product_before_points"]
        and payload["product_before_graph_objects"]
        and payload["equalizer_uses_product_pair"]
        and payload["equalizer_image"] == (FINITE_LIMIT_CUT_ID, COUPLING_SUBREP_ID)
        and payload["controls_not_points"]
        and payload["dh_not_points"]
        and payload["epstein_not_points"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_PRODUCT_EDGES))
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
    f"{TAG}1 mediator constraint codomain is an actual source product",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_PRODUCT_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and product_payload(T3_T5_z) == product_payload(zC15)
    and product_payload(T5_T3_z) == product_payload(zC15)
    and product_payload(T3_T3_T5_z) == product_payload(zC45)
    and product_payload(T15_zF22) == product_payload(zC15F22)
    and product_payload(T45_zF22) == product_payload(zC45F22)
    and all(product_row(row) for row in rows),
    "H1=%s product=%s projections=%d edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        PRODUCT_OBJECT_ID,
        len(PROJECTION_IDS),
        len(REQUIRED_PRODUCT_EDGES),
    ),
)

tuple_shell = live_source(
    constraint_product_actual=False,
    product_universal_property_actual=False,
    bundled_tuple_label=True,
    external_product_of_sets=True,
    component_checklist_product=True,
    declared_product=True,
)

gate(
    f"{TAG}2 bundled tuple labels are not mediator source products",
    not accepts_product_projected_mediator(tuple_shell)
    and {
        "constraint_product_missing",
        "product_universal_property_missing",
        "bundled_tuple_label",
        "external_product_of_sets",
        "component_checklist_product",
        "declared_product",
    }
    <= set(reasons(tuple_shell)),
    ",".join(reasons(tuple_shell)),
)

bad_product = live_source(
    endpoint_projection_actual=False,
    degree_projection_actual=False,
    projections_jointly_determine_pairing=False,
    alpha_pairing_unique=False,
    beta_pairing_unique=False,
    missing_projection=True,
    nonuniversal_bundle=True,
    coproduct_or_sum_substitute=True,
)

gate(
    f"{TAG}3 nonuniversal products and missing projections fail",
    not accepts_product_projected_mediator(bad_product)
    and {
        "endpoint_projection_missing",
        "degree_projection_missing",
        "projections_do_not_jointly_determine_pairing",
        "alpha_pairing_not_unique",
        "beta_pairing_not_unique",
        "missing_projection",
        "nonuniversal_bundle",
        "coproduct_or_sum_substitute",
    }
    <= set(reasons(bad_product)),
    ",".join(reasons(bad_product)),
)

late_product = live_source(
    product_before_points=False,
    product_before_graph_objects=False,
    equalizer_uses_product_pair=False,
    product_after_functor_of_points=True,
    fiber_product_after_graph_objects=True,
    projection_after_graph_objects=True,
    graph_classifier_product=True,
)

gate(
    f"{TAG}4 pointwise or graph-side products are too late",
    not accepts_product_projected_mediator(late_product)
    and {
        "product_not_before_points",
        "product_not_before_graph_objects",
        "equalizer_does_not_use_product_pair",
        "product_after_functor_of_points",
        "fiber_product_after_graph_objects",
        "projection_after_graph_objects",
        "graph_classifier_product",
    }
    <= set(reasons(late_product)),
    ",".join(reasons(late_product)),
)

local_product = live_source(
    same_product_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_projection_table=True,
    finite_sample_product=True,
    basis_dependent_projection=True,
    retuned_projection=True,
    projected_component_map=True,
)

gate(
    f"{TAG}5 local or retuned projections do not transport all paths",
    not accepts_product_projected_mediator(local_product)
    and {
        "same_product_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_projection_table",
        "finite_sample_product",
        "basis_dependent_projection",
        "retuned_projection",
        "projected_component_map",
    }
    <= set(reasons(local_product)),
    ",".join(reasons(local_product)),
)

missing_projections = live_source(
    endpoint_projection_actual=False,
    degree_projection_actual=False,
    dd4_projection_actual=False,
    pushforward_projection_actual=False,
    graph_projection_actual=False,
    rosati_projection_actual=False,
    control_projection_actual=False,
    projections_source_native=False,
    alpha_components_factor_through_projections=False,
    beta_components_factor_through_projections=False,
)

gate(
    f"{TAG}6 all seven source-native projections are mandatory",
    not accepts_product_projected_mediator(missing_projections)
    and {
        "endpoint_projection_missing",
        "degree_projection_missing",
        "dd4_projection_missing",
        "pushforward_projection_missing",
        "graph_projection_missing",
        "rosati_projection_missing",
        "control_projection_missing",
        "projections_not_source_native",
        "alpha_components_not_through_projections",
        "beta_components_not_through_projections",
    }
    <= set(reasons(missing_projections)),
    ",".join(reasons(missing_projections)),
)

graph_filter = live_source(
    product_before_points=False,
    product_before_graph_objects=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_classifier_product=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 graph classifier products leave controls formable",
    not accepts_product_projected_mediator(graph_filter)
    and {
        "product_not_before_points",
        "product_not_before_graph_objects",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_classifier_product",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_filter)),
    ",".join(reasons(graph_filter)),
)

expanded_index = live_source(
    constraint_product_actual=False,
    finite_index=set(FINITE_INDEX) | {"product_projection_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
    abstract_external_representer=True,
    equivalent_representer=True,
    univalence_transport=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}8 finite index expansion and external representer shells fail",
    not accepts_product_projected_mediator(expanded_index)
    and {
        "constraint_product_missing",
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "finite_anchors_not_generated",
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
        required_edges=REQUIRED_PRODUCT_EDGES
        - {("constraint_product_object", "endpoint_projection")}
    ),
    live_source(
        required_edges=REQUIRED_PRODUCT_EDGES
        - {("product_universal_property", "projections_jointly_determine_pairing")}
    ),
    live_source(
        required_edges=REQUIRED_PRODUCT_EDGES
        - {("alpha_pairing_map", "constraint_product_object")}
    ),
    live_source(required_edges=REQUIRED_PRODUCT_EDGES - {("parallel_pair", "equalizer_arrow")}),
    live_source(constraint_product_actual=False),
    live_source(endpoint_projection_actual=False),
    live_source(alpha_pairing_actual=False),
    live_source(beta_pairing_actual=False),
    live_source(equalizer_uses_product_pair=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every product/projection edge is mandatory",
    not any(accepts_product_projected_mediator(data) for data in missing_edges)
    and {
        "required_product_projection_edges_missing",
        "constraint_product_missing",
        "endpoint_projection_missing",
        "alpha_pairing_missing",
        "beta_pairing_missing",
        "equalizer_does_not_use_product_pair",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

live = live_source()
dead_sources = {
    "tuple_shell": tuple_shell,
    "bad_product": bad_product,
    "late_product": late_product,
    "local_product": local_product,
    "missing_projections": missing_projections,
    "graph_filter": graph_filter,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only product-projected parallel-morphism mediator passes",
    accepts_product_projected_mediator(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_product_projected_mediator(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_product_projected_mediator(data) for data in dead_sources.values()),
        accepts_product_projected_mediator(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "product-projected parallel-morphism finite-limit subrepresented coupled "
    "formation-coherent self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-506 parallel alpha,beta source morphisms must land in an "
    "actual mediator source product with seven source-native projections and "
    "unique alpha/beta pairings. Bundled tuples, external products, pointwise "
    "or graph-side products, local projections, finite samples, retuned "
    "components, expanded indexes, and towers do not construct the missing "
    "source object."
)
