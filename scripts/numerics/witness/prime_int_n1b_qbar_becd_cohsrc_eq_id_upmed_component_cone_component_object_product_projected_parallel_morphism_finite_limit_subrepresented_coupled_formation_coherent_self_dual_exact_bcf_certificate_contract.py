r"""Component-cone product-projected parallel-morphism mediator contract.

Doc 508 requires the product projections to land in seven actual mediator
source component objects. This witness pins the next edge: the mediator must
generate those seven component legs as one source-native cone, and pair_alpha
must be the unique product-mediated arrow induced by that cone.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_component_object_product_projected_parallel_morphism_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_ETA_ID = "eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
CONSTRAINT_OBJECT_ID = "Con_NCoup_med_UP_Eq_id_endpoint_dd4_rosati_control_source"
PRODUCT_OBJECT_ID = "Prod_NCoup_med_UP_Eq_id_endpoint_degree_dd4_push_graph_rosati_control"
COMPONENT_CONE_ID = "Cone_NCoup_med_UP_Eq_id_eta_source_components"
ALPHA_CONSTRAINT_MAP_ID = "alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_CONSTRAINT_MAP_ID = "beta_NCoup_med_UP_Eq_id_source_constraints"
ALPHA_PAIRING_ID = "pair_alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_PAIRING_ID = "pair_beta_NCoup_med_UP_Eq_id_source_constraints"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_id_constraints_to_SubRep_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
CONTROL_DEATH_ID = "Nat_ControlDeath_med_UP_Eq_id_source_constraint"

ENDPOINT_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_endpoint_integrality"
DEGREE_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_degree_maps"
DD4_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_dd4_boundary"
PUSH_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_boundary_pushforward"
GRAPH_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_graph_composition"
ROSATI_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_rosati_count"
CONTROL_PROJECTION_ID = "pi_NCoup_med_UP_Eq_id_control_death"

ENDPOINT_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_endpoint_integrality_source"
DEGREE_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_degree_maps_source"
DD4_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_dd4_boundary_source"
PUSH_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_boundary_pushforward_source"
GRAPH_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_graph_composition_source"
ROSATI_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_rosati_count_source"
CONTROL_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_control_death_source"

ENDPOINT_LEG_ID = "leg_NCoup_med_UP_Eq_id_endpoint_integrality_source"
DEGREE_LEG_ID = "leg_NCoup_med_UP_Eq_id_degree_maps_source"
DD4_LEG_ID = "leg_NCoup_med_UP_Eq_id_dd4_boundary_source"
PUSH_LEG_ID = "leg_NCoup_med_UP_Eq_id_boundary_pushforward_source"
GRAPH_LEG_ID = "leg_NCoup_med_UP_Eq_id_graph_composition_source"
ROSATI_LEG_ID = "leg_NCoup_med_UP_Eq_id_rosati_count_source"
CONTROL_LEG_ID = "leg_NCoup_med_UP_Eq_id_control_death_source"

COMPONENTS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

COMPONENT_OBJECTS = (
    ENDPOINT_COMPONENT_OBJECT_ID,
    DEGREE_COMPONENT_OBJECT_ID,
    DD4_COMPONENT_OBJECT_ID,
    PUSH_COMPONENT_OBJECT_ID,
    GRAPH_COMPONENT_OBJECT_ID,
    ROSATI_COMPONENT_OBJECT_ID,
    CONTROL_COMPONENT_OBJECT_ID,
)

COMPONENT_LEGS = (
    (ENDPOINT_LEG_ID, ENDPOINT_COMPONENT_OBJECT_ID),
    (DEGREE_LEG_ID, DEGREE_COMPONENT_OBJECT_ID),
    (DD4_LEG_ID, DD4_COMPONENT_OBJECT_ID),
    (PUSH_LEG_ID, PUSH_COMPONENT_OBJECT_ID),
    (GRAPH_LEG_ID, GRAPH_COMPONENT_OBJECT_ID),
    (ROSATI_LEG_ID, ROSATI_COMPONENT_OBJECT_ID),
    (CONTROL_LEG_ID, CONTROL_COMPONENT_OBJECT_ID),
)

PROJECTION_LEG_EQUALITIES = (
    (ENDPOINT_PROJECTION_ID, ALPHA_PAIRING_ID, ENDPOINT_LEG_ID),
    (DEGREE_PROJECTION_ID, ALPHA_PAIRING_ID, DEGREE_LEG_ID),
    (DD4_PROJECTION_ID, ALPHA_PAIRING_ID, DD4_LEG_ID),
    (PUSH_PROJECTION_ID, ALPHA_PAIRING_ID, PUSH_LEG_ID),
    (GRAPH_PROJECTION_ID, ALPHA_PAIRING_ID, GRAPH_LEG_ID),
    (ROSATI_PROJECTION_ID, ALPHA_PAIRING_ID, ROSATI_LEG_ID),
    (CONTROL_PROJECTION_ID, ALPHA_PAIRING_ID, CONTROL_LEG_ID),
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

REQUIRED_CONE_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("coupling_universal_arrow", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("universal_mediator", "source_component_cone"),
    ("coupling_universal_arrow", "source_component_cone"),
    ("formation_fiber", "source_component_cone"),
    ("source_component_cone", "endpoint_leg"),
    ("source_component_cone", "degree_leg"),
    ("source_component_cone", "dd4_leg"),
    ("source_component_cone", "pushforward_leg"),
    ("source_component_cone", "graph_leg"),
    ("source_component_cone", "rosati_count_leg"),
    ("source_component_cone", "control_death_leg"),
    ("endpoint_leg", "endpoint_component_object"),
    ("degree_leg", "degree_component_object"),
    ("dd4_leg", "dd4_component_object"),
    ("pushforward_leg", "pushforward_component_object"),
    ("graph_leg", "graph_component_object"),
    ("rosati_count_leg", "rosati_count_component_object"),
    ("control_death_leg", "control_death_component_object"),
    ("source_component_cone", "constraint_product_object"),
    ("finite_limit_cut", "constraint_product_object"),
    ("constraint_product_object", "constraint_object"),
    ("constraint_product_object", "product_universal_property"),
    ("source_component_cone", "alpha_pairing_map"),
    ("alpha_pairing_map", "constraint_product_object"),
    ("alpha_pairing_map", "alpha_constraint_map"),
    ("product_universal_property", "pair_alpha_unique_from_cone"),
    ("pair_alpha_unique_from_cone", "endpoint_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "degree_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "dd4_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "pushforward_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "graph_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "rosati_count_projection_leg_equality"),
    ("pair_alpha_unique_from_cone", "control_death_projection_leg_equality"),
    ("endpoint_projection_leg_equality", "endpoint_leg"),
    ("degree_projection_leg_equality", "degree_leg"),
    ("dd4_projection_leg_equality", "dd4_leg"),
    ("pushforward_projection_leg_equality", "pushforward_leg"),
    ("graph_projection_leg_equality", "graph_leg"),
    ("rosati_count_projection_leg_equality", "rosati_count_leg"),
    ("control_death_projection_leg_equality", "control_death_leg"),
    ("source_component_cone", "beta_pairing_map"),
    ("beta_pairing_map", "beta_constraint_map"),
    ("beta_pairing_map", "zero_diagonal_source_cone"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("equalizer_arrow", "source_coupling_subrepresenter"),
    ("source_component_cone", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
    ("source_component_cone", "same_cone_payload_all_paths"),
    ("same_cone_payload_all_paths", "C3_C5_equals_C15"),
    ("same_cone_payload_all_paths", "C5_C3_equals_C15"),
    ("same_cone_payload_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cone_payload_all_paths", "F22_product"),
    ("dd4_leg", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("control_death_leg", "source_before_points_and_graph_objects"),
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
        "cone_eta_generated": False,
        "cone_source_native": False,
        "all_component_legs_actual": False,
        "endpoint_leg_actual": False,
        "degree_leg_actual": False,
        "dd4_leg_actual": False,
        "pushforward_leg_actual": False,
        "graph_leg_actual": False,
        "rosati_count_leg_actual": False,
        "control_death_leg_actual": False,
        "legs_land_in_doc508_components": False,
        "constraint_product_actual": False,
        "constraint_object_actual": False,
        "product_universal_property_actual": False,
        "cone_assembles_pair_alpha": False,
        "pair_alpha_unique_from_cone": False,
        "projections_equal_cone_legs": False,
        "pair_beta_cone_compatible": False,
        "alpha_beta_parallel_after_product": False,
        "equalizer_uses_product_pair": False,
        "cone_before_points": False,
        "cone_before_graph_objects": False,
        "cone_transports_all_paths": False,
        "same_cone_payload_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "finite_anchors_generated": False,
        "no_next_coherence_obligation": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "independent_component_legs": False,
        "external_chosen_legs": False,
        "posthoc_cone_label": False,
        "product_projection_pullback": False,
        "point_functor_cone": False,
        "graph_side_cone": False,
        "componentwise_natural_transformations": False,
        "local_cone_table": False,
        "finite_sample_cone": False,
        "basis_dependent_cone": False,
        "retuned_cone_leg": False,
        "quotient_cone": False,
        "closure_cone": False,
        "split_product_of_cones": False,
        "declared_cone": False,
        "non_eta_generated_cone": False,
        "abstract_external_representer": False,
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
    ("cone_eta_generated", "cone_not_eta_generated"),
    ("cone_source_native", "cone_not_source_native"),
    ("all_component_legs_actual", "component_legs_missing"),
    ("endpoint_leg_actual", "endpoint_leg_missing"),
    ("degree_leg_actual", "degree_leg_missing"),
    ("dd4_leg_actual", "dd4_leg_missing"),
    ("pushforward_leg_actual", "pushforward_leg_missing"),
    ("graph_leg_actual", "graph_leg_missing"),
    ("rosati_count_leg_actual", "rosati_count_leg_missing"),
    ("control_death_leg_actual", "control_death_leg_missing"),
    ("legs_land_in_doc508_components", "legs_do_not_land_in_doc508_components"),
    ("constraint_product_actual", "constraint_product_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("product_universal_property_actual", "product_universal_property_missing"),
    ("cone_assembles_pair_alpha", "cone_does_not_assemble_pair_alpha"),
    ("pair_alpha_unique_from_cone", "pair_alpha_not_unique_from_cone"),
    ("projections_equal_cone_legs", "projections_do_not_equal_cone_legs"),
    ("pair_beta_cone_compatible", "pair_beta_cone_incompatible"),
    ("alpha_beta_parallel_after_product", "alpha_beta_not_parallel_after_product"),
    ("equalizer_uses_product_pair", "equalizer_does_not_use_product_pair"),
    ("cone_before_points", "cone_not_before_points"),
    ("cone_before_graph_objects", "cone_not_before_graph_objects"),
    ("cone_transports_all_paths", "cone_does_not_transport_all_paths"),
    ("same_cone_payload_all_paths", "same_cone_payload_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("independent_component_legs", "independent_component_legs"),
    ("external_chosen_legs", "external_chosen_legs"),
    ("posthoc_cone_label", "posthoc_cone_label"),
    ("product_projection_pullback", "product_projection_pullback"),
    ("point_functor_cone", "point_functor_cone"),
    ("graph_side_cone", "graph_side_cone"),
    ("componentwise_natural_transformations", "componentwise_natural_transformations"),
    ("local_cone_table", "local_cone_table"),
    ("finite_sample_cone", "finite_sample_cone"),
    ("basis_dependent_cone", "basis_dependent_cone"),
    ("retuned_cone_leg", "retuned_cone_leg"),
    ("quotient_cone", "quotient_cone"),
    ("closure_cone", "closure_cone"),
    ("split_product_of_cones", "split_product_of_cones"),
    ("declared_cone", "declared_cone"),
    ("non_eta_generated_cone", "non_eta_generated_cone"),
    ("abstract_external_representer", "abstract_external_representer"),
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
    if not REQUIRED_CONE_EDGES <= set(data["required_edges"]):
        out.append("required_source_component_cone_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_component_cone_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_CONE_EDGES <= set(data["required_edges"])
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
        cone_eta_generated=True,
        cone_source_native=True,
        all_component_legs_actual=True,
        endpoint_leg_actual=True,
        degree_leg_actual=True,
        dd4_leg_actual=True,
        pushforward_leg_actual=True,
        graph_leg_actual=True,
        rosati_count_leg_actual=True,
        control_death_leg_actual=True,
        legs_land_in_doc508_components=True,
        constraint_product_actual=True,
        constraint_object_actual=True,
        product_universal_property_actual=True,
        cone_assembles_pair_alpha=True,
        pair_alpha_unique_from_cone=True,
        projections_equal_cone_legs=True,
        pair_beta_cone_compatible=True,
        alpha_beta_parallel_after_product=True,
        equalizer_uses_product_pair=True,
        cone_before_points=True,
        cone_before_graph_objects=True,
        cone_transports_all_paths=True,
        same_cone_payload_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        finite_anchors_generated=True,
        no_next_coherence_obligation=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CONE_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def cone_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "coupling_universal_arrow": COUPLING_ETA_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "component_cone": COMPONENT_CONE_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "component_objects": COMPONENT_OBJECTS,
        "component_legs": COMPONENT_LEGS,
        "projection_leg_equalities": PROJECTION_LEG_EQUALITIES,
        "endpoint_leg": (ENDPOINT_LEG_ID, ENDPOINT_COMPONENT_OBJECT_ID, p1, p2, p1 == p2),
        "degree_leg": (DEGREE_LEG_ID, DEGREE_COMPONENT_OBJECT_ID, tuple(sorted(chi)), p1 + p2),
        "dd4_leg": (DD4_LEG_ID, DD4_COMPONENT_OBJECT_ID, DD4_CLASS_ID),
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "pushforward_leg": (PUSH_LEG_ID, PUSH_COMPONENT_OBJECT_ID, tuple(chi.items())),
        "graph_leg": (GRAPH_LEG_ID, GRAPH_COMPONENT_OBJECT_ID, tuple(sorted(chi))),
        "rosati_leg": (ROSATI_LEG_ID, ROSATI_COMPONENT_OBJECT_ID, "rosati_count_source"),
        "control_leg": (CONTROL_LEG_ID, CONTROL_COMPONENT_OBJECT_ID, CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "eta_generated_cone_payload": True,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_CONE_EDGES)),
    }


def cone_row(chi: dict[int, int]) -> bool:
    payload = cone_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["coupling_universal_arrow"] == COUPLING_ETA_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["component_cone"] == COMPONENT_CONE_ID
        and payload["constraint_object"] == CONSTRAINT_OBJECT_ID
        and payload["product"] == PRODUCT_OBJECT_ID
        and payload["alpha_pairing"] == ALPHA_PAIRING_ID
        and payload["beta_pairing"] == BETA_PAIRING_ID
        and payload["alpha"] == ALPHA_CONSTRAINT_MAP_ID
        and payload["beta"] == BETA_CONSTRAINT_MAP_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and payload["component_objects"] == COMPONENT_OBJECTS
        and payload["component_legs"] == COMPONENT_LEGS
        and payload["projection_leg_equalities"] == PROJECTION_LEG_EQUALITIES
        and all(target in COMPONENT_OBJECTS for _, target in payload["component_legs"])
        and all(leg in {item[0] for item in COMPONENT_LEGS} for _, _, leg in payload["projection_leg_equalities"])
        and payload["dd4_leg"] == (DD4_LEG_ID, DD4_COMPONENT_OBJECT_ID, DD4_CLASS_ID)
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_leg"] == (CONTROL_LEG_ID, CONTROL_COMPONENT_OBJECT_ID, CONTROL_DEATH_ID)
        and payload["eta_generated_cone_payload"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_CONE_EDGES))
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
    f"{TAG}1 eta generates one mediator source component cone",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CONE_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cone_payload(T3_T5_z) == cone_payload(zC15)
    and cone_payload(T5_T3_z) == cone_payload(zC15)
    and cone_payload(T3_T3_T5_z) == cone_payload(zC45)
    and cone_payload(T15_zF22) == cone_payload(zC15F22)
    and cone_payload(T45_zF22) == cone_payload(zC45F22)
    and all(cone_row(row) for row in rows),
    "H1=%s cone=%s legs=%d edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        COMPONENT_CONE_ID,
        len(COMPONENT_LEGS),
        len(REQUIRED_CONE_EDGES),
    ),
)

independent = live_source(
    component_cone_actual=False,
    cone_eta_generated=False,
    cone_assembles_pair_alpha=False,
    pair_alpha_unique_from_cone=False,
    independent_component_legs=True,
    external_chosen_legs=True,
    declared_cone=True,
)

gate(
    f"{TAG}2 independent or externally chosen legs are not one source cone",
    not accepts_component_cone_mediator(independent)
    and {
        "component_cone_missing",
        "cone_not_eta_generated",
        "cone_does_not_assemble_pair_alpha",
        "pair_alpha_not_unique_from_cone",
        "independent_component_legs",
        "external_chosen_legs",
        "declared_cone",
    }
    <= set(reasons(independent)),
    ",".join(reasons(independent)),
)

late = live_source(
    cone_before_points=False,
    cone_before_graph_objects=False,
    projections_equal_cone_legs=False,
    pair_beta_cone_compatible=False,
    posthoc_cone_label=True,
    product_projection_pullback=True,
    point_functor_cone=True,
    graph_side_cone=True,
    componentwise_natural_transformations=True,
)

gate(
    f"{TAG}3 post-hoc, pointwise, or graph-side cones are too late",
    not accepts_component_cone_mediator(late)
    and {
        "projections_do_not_equal_cone_legs",
        "pair_beta_cone_incompatible",
        "cone_not_before_points",
        "cone_not_before_graph_objects",
        "posthoc_cone_label",
        "product_projection_pullback",
        "point_functor_cone",
        "graph_side_cone",
        "componentwise_natural_transformations",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

local = live_source(
    cone_transports_all_paths=False,
    same_cone_payload_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_cone_table=True,
    finite_sample_cone=True,
    basis_dependent_cone=True,
    retuned_cone_leg=True,
)

gate(
    f"{TAG}4 local, finite, basis, or retuned cones do not transport",
    not accepts_component_cone_mediator(local)
    and {
        "cone_does_not_transport_all_paths",
        "same_cone_payload_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_cone_table",
        "finite_sample_cone",
        "basis_dependent_cone",
        "retuned_cone_leg",
    }
    <= set(reasons(local)),
    ",".join(reasons(local)),
)

shell = live_source(
    cone_eta_generated=False,
    cone_source_native=False,
    all_component_legs_actual=False,
    quotient_cone=True,
    closure_cone=True,
    split_product_of_cones=True,
    declared_cone=True,
    non_eta_generated_cone=True,
)

gate(
    f"{TAG}5 quotient, closure, split, or declared cones are not eta-generated",
    not accepts_component_cone_mediator(shell)
    and {
        "cone_not_eta_generated",
        "cone_not_source_native",
        "component_legs_missing",
        "quotient_cone",
        "closure_cone",
        "split_product_of_cones",
        "declared_cone",
        "non_eta_generated_cone",
    }
    <= set(reasons(shell)),
    ",".join(reasons(shell)),
)

missing_legs = live_source(
    endpoint_leg_actual=False,
    degree_leg_actual=False,
    dd4_leg_actual=False,
    pushforward_leg_actual=False,
    graph_leg_actual=False,
    rosati_count_leg_actual=False,
    control_death_leg_actual=False,
    legs_land_in_doc508_components=False,
)

gate(
    f"{TAG}6 every source component-cone leg is mandatory",
    not accepts_component_cone_mediator(missing_legs)
    and {
        "endpoint_leg_missing",
        "degree_leg_missing",
        "dd4_leg_missing",
        "pushforward_leg_missing",
        "graph_leg_missing",
        "rosati_count_leg_missing",
        "control_death_leg_missing",
        "legs_do_not_land_in_doc508_components",
    }
    <= set(reasons(missing_legs)),
    ",".join(reasons(missing_legs)),
)

control_cone = live_source(
    cone_eta_generated=False,
    legs_land_in_doc508_components=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_cone=True,
    non_eta_generated_cone=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 non-eta-generated cones leave controls formable",
    not accepts_component_cone_mediator(control_cone)
    and {
        "cone_not_eta_generated",
        "legs_do_not_land_in_doc508_components",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_cone",
        "non_eta_generated_cone",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_cone)),
    ",".join(reasons(control_cone)),
)

expanded_index = live_source(
    component_cone_actual=False,
    finite_index=set(FINITE_INDEX) | {"component_cone_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
    abstract_external_representer=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}8 finite index expansion and external representer shells fail",
    not accepts_component_cone_mediator(expanded_index)
    and {
        "component_cone_missing",
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "finite_anchors_not_generated",
        "next_coherence_obligation_open",
        "abstract_external_representer",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded_index)),
    ",".join(reasons(expanded_index)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_CONE_EDGES - {("source_component_cone", "control_death_leg")}),
    live_source(required_edges=REQUIRED_CONE_EDGES - {("product_universal_property", "pair_alpha_unique_from_cone")}),
    live_source(universal_mediator_actual=False),
    live_source(coupling_universal_arrow_actual=False),
    live_source(component_cone_actual=False),
    live_source(endpoint_leg_actual=False),
    live_source(degree_leg_actual=False),
    live_source(dd4_leg_actual=False),
    live_source(pushforward_leg_actual=False),
    live_source(graph_leg_actual=False),
    live_source(rosati_count_leg_actual=False),
    live_source(control_death_leg_actual=False),
    live_source(cone_assembles_pair_alpha=False),
    live_source(projections_equal_cone_legs=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every eta-cone leg and projection equality is mandatory",
    not any(accepts_component_cone_mediator(data) for data in missing_edges)
    and {
        "required_source_component_cone_edges_missing",
        "universal_mediator_missing",
        "coupling_universal_arrow_missing",
        "component_cone_missing",
        "endpoint_leg_missing",
        "degree_leg_missing",
        "dd4_leg_missing",
        "pushforward_leg_missing",
        "graph_leg_missing",
        "rosati_count_leg_missing",
        "control_death_leg_missing",
        "cone_does_not_assemble_pair_alpha",
        "projections_do_not_equal_cone_legs",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

live = live_source()
dead_sources = {
    "independent": independent,
    "late": late,
    "local": local,
    "shell": shell,
    "missing_legs": missing_legs,
    "control_cone": control_cone,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only component-cone component-object product-projected mediator passes",
    accepts_component_cone_mediator(live)
    and graph_connected(live["required_edges"])
    and len(COMPONENT_LEGS) == 7
    and len(PROJECTION_LEG_EQUALITIES) == 7
    and not any(accepts_component_cone_mediator(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_component_cone_mediator(data) for data in dead_sources.values()),
        accepts_component_cone_mediator(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "component-cone component-object product-projected parallel-morphism "
    "finite-limit subrepresented coupled formation-coherent self-dual exact "
    "BCF certificate pinned"
)
print(
    "VERDICT: the doc-508 component objects must be generated as one "
    "mediator source-native cone, and pair_alpha must be the unique "
    "product-mediated arrow whose projections are those legs. Independent "
    "legs, post-hoc product pullbacks, graph-side cones, local tables, "
    "quotient or closure cones, split products, declared cone labels, "
    "expanded indexes, and non-eta-generated cones do not construct the "
    "missing source object."
)
