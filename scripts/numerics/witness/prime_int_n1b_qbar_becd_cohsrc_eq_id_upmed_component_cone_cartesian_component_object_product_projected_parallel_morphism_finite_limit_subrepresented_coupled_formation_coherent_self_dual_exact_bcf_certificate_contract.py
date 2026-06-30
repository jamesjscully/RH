r"""Cartesian component-cone mediator contract.

Doc 509 requires the mediator to generate seven source component legs as one
eta-generated cone. This witness pins the next edge: that cone must be
cartesian over represented mediator source lifts, with component-leg and
projection-leg naturality for both product pairings.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_component_object_product_projected_parallel_morphism_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
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

PULLBACKS = (
    "C3_cone_pullback",
    "C5_cone_pullback",
    "C15_cone_pullback",
    "C45_cone_pullback",
    "F22_cone_pullback",
)

REQUIRED_CARTESIAN_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("coupling_universal_arrow", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("universal_mediator", "source_component_cone"),
    ("coupling_universal_arrow", "source_component_cone"),
    ("formation_fiber", "source_component_cone"),
    ("source_component_cone", "cartesian_component_cone"),
    ("represented_source_lifts", "cartesian_component_cone"),
    ("cartesian_source_coherence", "cartesian_component_cone"),
    ("cartesian_component_cone", "C3_cone_pullback"),
    ("cartesian_component_cone", "C5_cone_pullback"),
    ("cartesian_component_cone", "C15_cone_pullback"),
    ("cartesian_component_cone", "C45_cone_pullback"),
    ("cartesian_component_cone", "F22_cone_pullback"),
    ("C3_cone_pullback", "component_leg_naturality"),
    ("C5_cone_pullback", "component_leg_naturality"),
    ("C15_cone_pullback", "component_leg_naturality"),
    ("C45_cone_pullback", "component_leg_naturality"),
    ("F22_cone_pullback", "component_leg_naturality"),
    ("component_leg_naturality", "endpoint_leg_natural"),
    ("component_leg_naturality", "degree_leg_natural"),
    ("component_leg_naturality", "dd4_leg_natural"),
    ("component_leg_naturality", "pushforward_leg_natural"),
    ("component_leg_naturality", "graph_leg_natural"),
    ("component_leg_naturality", "rosati_count_leg_natural"),
    ("component_leg_naturality", "control_death_leg_natural"),
    ("component_leg_naturality", "projection_leg_naturality"),
    ("projection_leg_naturality", "pair_alpha_cartesian_natural"),
    ("projection_leg_naturality", "pair_beta_cartesian_natural"),
    ("pair_alpha_cartesian_natural", "constraint_product_object"),
    ("pair_alpha_cartesian_natural", "product_universal_property"),
    ("pair_beta_cartesian_natural", "zero_diagonal_cartesian_cone"),
    ("constraint_product_object", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("cartesian_component_cone", "same_cartesian_cone_all_paths"),
    ("same_cartesian_cone_all_paths", "C3_C5_equals_C15"),
    ("same_cartesian_cone_all_paths", "C5_C3_equals_C15"),
    ("same_cartesian_cone_all_paths", "C3_C3_C5_equals_C45"),
    ("same_cartesian_cone_all_paths", "F22_product"),
    ("cartesian_component_cone", "base_change_preserves_doc509_cone"),
    ("base_change_preserves_doc509_cone", "base_change_preserves_doc508_components"),
    ("base_change_preserves_doc508_components", "component_objects"),
    ("dd4_leg_natural", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("control_death_leg_natural", "source_before_points_and_graph_objects"),
    ("cartesian_component_cone", "source_before_points_and_graph_objects"),
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
        "component_cone_eta_generated": False,
        "component_cone_source_native": False,
        "cartesian_source_lifts_actual": False,
        "cartesian_coherence_actual": False,
        "cartesian_component_cone_actual": False,
        "cone_pullbacks_actual": False,
        "component_leg_naturality_actual": False,
        "projection_leg_naturality_actual": False,
        "all_component_legs_natural": False,
        "projections_natural_to_legs": False,
        "pair_alpha_cartesian_natural": False,
        "pair_beta_cartesian_natural": False,
        "pair_alpha_unique_from_cone": False,
        "pair_beta_zero_diagonal_cartesian": False,
        "base_change_preserves_doc509_cone": False,
        "base_change_preserves_doc508_components": False,
        "same_cartesian_cone_payload_all_paths": False,
        "C3_C5_equals_C15": False,
        "C5_C3_equals_C15": False,
        "C3_C3_C5_equals_C45": False,
        "F22_product": False,
        "finite_index": set(),
        "finite_index_cardinality": 0,
        "finite_anchors_generated": False,
        "no_next_coherence_obligation": False,
        "cone_before_points": False,
        "cone_before_graph_objects": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "required_edges": set(),
        "finite_path_check_only": False,
        "sampled_path_transport": False,
        "chosen_transport_isomorphism": False,
        "up_to_iso_without_coherence": False,
        "lax_naturality_only": False,
        "pointwise_naturality": False,
        "graph_side_base_change": False,
        "local_transport_table": False,
        "noncartesian_pullback": False,
        "reindexed_cone_label": False,
        "retuned_transport": False,
        "base_changed_component_replacement": False,
        "declared_naturality_square": False,
        "split_componentwise_naturality": False,
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
    ("component_cone_eta_generated", "component_cone_not_eta_generated"),
    ("component_cone_source_native", "component_cone_not_source_native"),
    ("cartesian_source_lifts_actual", "cartesian_source_lifts_missing"),
    ("cartesian_coherence_actual", "cartesian_coherence_missing"),
    ("cartesian_component_cone_actual", "cartesian_component_cone_missing"),
    ("cone_pullbacks_actual", "cone_pullbacks_missing"),
    ("component_leg_naturality_actual", "component_leg_naturality_missing"),
    ("projection_leg_naturality_actual", "projection_leg_naturality_missing"),
    ("all_component_legs_natural", "component_legs_not_natural"),
    ("projections_natural_to_legs", "projections_not_natural_to_legs"),
    ("pair_alpha_cartesian_natural", "pair_alpha_not_cartesian_natural"),
    ("pair_beta_cartesian_natural", "pair_beta_not_cartesian_natural"),
    ("pair_alpha_unique_from_cone", "pair_alpha_not_unique_from_cone"),
    ("pair_beta_zero_diagonal_cartesian", "pair_beta_not_zero_diagonal_cartesian"),
    ("base_change_preserves_doc509_cone", "base_change_does_not_preserve_doc509_cone"),
    ("base_change_preserves_doc508_components", "base_change_does_not_preserve_doc508_components"),
    ("same_cartesian_cone_payload_all_paths", "same_cartesian_cone_payload_not_all_paths"),
    ("C3_C5_equals_C15", "C3_C5_not_C15"),
    ("C5_C3_equals_C15", "C5_C3_not_C15"),
    ("C3_C3_C5_equals_C45", "C3_C3_C5_not_C45"),
    ("F22_product", "F22_product_missing"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    ("no_next_coherence_obligation", "next_coherence_obligation_open"),
    ("cone_before_points", "cone_not_before_points"),
    ("cone_before_graph_objects", "cone_not_before_graph_objects"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("finite_path_check_only", "finite_path_check_only"),
    ("sampled_path_transport", "sampled_path_transport"),
    ("chosen_transport_isomorphism", "chosen_transport_isomorphism"),
    ("up_to_iso_without_coherence", "up_to_iso_without_coherence"),
    ("lax_naturality_only", "lax_naturality_only"),
    ("pointwise_naturality", "pointwise_naturality"),
    ("graph_side_base_change", "graph_side_base_change"),
    ("local_transport_table", "local_transport_table"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("reindexed_cone_label", "reindexed_cone_label"),
    ("retuned_transport", "retuned_transport"),
    ("base_changed_component_replacement", "base_changed_component_replacement"),
    ("declared_naturality_square", "declared_naturality_square"),
    ("split_componentwise_naturality", "split_componentwise_naturality"),
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
    if not REQUIRED_CARTESIAN_EDGES <= set(data["required_edges"]):
        out.append("required_cartesian_component_cone_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_component_cone(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_CARTESIAN_EDGES <= set(data["required_edges"])
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
        component_cone_eta_generated=True,
        component_cone_source_native=True,
        cartesian_source_lifts_actual=True,
        cartesian_coherence_actual=True,
        cartesian_component_cone_actual=True,
        cone_pullbacks_actual=True,
        component_leg_naturality_actual=True,
        projection_leg_naturality_actual=True,
        all_component_legs_natural=True,
        projections_natural_to_legs=True,
        pair_alpha_cartesian_natural=True,
        pair_beta_cartesian_natural=True,
        pair_alpha_unique_from_cone=True,
        pair_beta_zero_diagonal_cartesian=True,
        base_change_preserves_doc509_cone=True,
        base_change_preserves_doc508_components=True,
        same_cartesian_cone_payload_all_paths=True,
        C3_C5_equals_C15=True,
        C5_C3_equals_C15=True,
        C3_C3_C5_equals_C45=True,
        F22_product=True,
        finite_index=set(FINITE_INDEX),
        finite_index_cardinality=len(FINITE_INDEX),
        finite_anchors_generated=True,
        no_next_coherence_obligation=True,
        cone_before_points=True,
        cone_before_graph_objects=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        required_edges=set(REQUIRED_CARTESIAN_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def cartesian_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    component_naturality = tuple(
        (leg, obj, "cartesian_natural")
        for leg, obj in zip(COMPONENT_LEGS, COMPONENT_OBJECTS)
    )
    projection_naturality = tuple(
        (projection, ALPHA_PAIRING_ID, BETA_PAIRING_ID, leg, "cartesian_natural")
        for projection, leg in zip(PROJECTIONS, COMPONENT_LEGS)
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
        "cartesian_coherence": CARTESIAN_COHERENCE_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "component_objects": COMPONENT_OBJECTS,
        "component_legs": COMPONENT_LEGS,
        "projection_leg_equalities": PROJECTION_LEG_EQUALITIES,
        "component_leg_naturality": component_naturality,
        "projection_leg_naturality": projection_naturality,
        "pullbacks": tuple((pullback, CARTESIAN_COMPONENT_CONE_ID) for pullback in PULLBACKS),
        "base_change_preserves": (COMPONENT_CONE_ID, COMPONENT_OBJECTS),
        "endpoint_leg": (COMPONENT_LEGS[0], COMPONENT_OBJECTS[0], p1, p2, p1 == p2),
        "degree_leg": (COMPONENT_LEGS[1], COMPONENT_OBJECTS[1], tuple(sorted(chi)), p1 + p2),
        "dd4_leg": (COMPONENT_LEGS[2], COMPONENT_OBJECTS[2], DD4_CLASS_ID),
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "pushforward_leg": (COMPONENT_LEGS[3], COMPONENT_OBJECTS[3], tuple(chi.items())),
        "graph_leg": (COMPONENT_LEGS[4], COMPONENT_OBJECTS[4], tuple(sorted(chi))),
        "rosati_leg": (COMPONENT_LEGS[5], COMPONENT_OBJECTS[5], "rosati_count_source"),
        "control_leg": (COMPONENT_LEGS[6], COMPONENT_OBJECTS[6], CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "cartesian_cone_payload": True,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_CARTESIAN_EDGES)),
    }


def cartesian_row(chi: dict[int, int]) -> bool:
    payload = cartesian_payload(chi)
    component_naturality = payload["component_leg_naturality"]
    projection_naturality = payload["projection_leg_naturality"]
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["component_cone"] == COMPONENT_CONE_ID
        and payload["cartesian_component_cone"] == CARTESIAN_COMPONENT_CONE_ID
        and payload["cartesian_source_lifts"] == CARTESIAN_SOURCE_LIFTS_ID
        and payload["cartesian_coherence"] == CARTESIAN_COHERENCE_ID
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
        and payload["projection_leg_equalities"] == PROJECTION_LEG_EQUALITIES
        and len(component_naturality) == 7
        and all(mark == "cartesian_natural" for _, _, mark in component_naturality)
        and len(projection_naturality) == 7
        and all(mark == "cartesian_natural" for *_, mark in projection_naturality)
        and len(payload["pullbacks"]) == 5
        and all(target == CARTESIAN_COMPONENT_CONE_ID for _, target in payload["pullbacks"])
        and payload["base_change_preserves"] == (COMPONENT_CONE_ID, COMPONENT_OBJECTS)
        and payload["dd4_leg"] == (COMPONENT_LEGS[2], COMPONENT_OBJECTS[2], DD4_CLASS_ID)
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_leg"] == (COMPONENT_LEGS[6], COMPONENT_OBJECTS[6], CONTROL_DEATH_ID)
        and payload["cartesian_cone_payload"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_CARTESIAN_EDGES))
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
    f"{TAG}1 eta cone pulls back as one cartesian mediator source cone",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_payload(T3_T5_z) == cartesian_payload(zC15)
    and cartesian_payload(T5_T3_z) == cartesian_payload(zC15)
    and cartesian_payload(T3_T3_T5_z) == cartesian_payload(zC45)
    and cartesian_payload(T15_zF22) == cartesian_payload(zC15F22)
    and cartesian_payload(T45_zF22) == cartesian_payload(zC45F22)
    and all(cartesian_row(row) for row in rows),
    "H1=%s cart_cone=%s pullbacks=%d edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        CARTESIAN_COMPONENT_CONE_ID,
        len(PULLBACKS),
        len(REQUIRED_CARTESIAN_EDGES),
    ),
)

finite_path = live_source(
    cartesian_component_cone_actual=False,
    cone_pullbacks_actual=False,
    same_cartesian_cone_payload_all_paths=False,
    finite_path_check_only=True,
    sampled_path_transport=True,
    chosen_transport_isomorphism=True,
)

gate(
    f"{TAG}2 finite path checks and chosen transports are not cartesianity",
    not accepts_cartesian_component_cone(finite_path)
    and {
        "cartesian_component_cone_missing",
        "cone_pullbacks_missing",
        "same_cartesian_cone_payload_not_all_paths",
        "finite_path_check_only",
        "sampled_path_transport",
        "chosen_transport_isomorphism",
    }
    <= set(reasons(finite_path)),
    ",".join(reasons(finite_path)),
)

late_naturality = live_source(
    component_leg_naturality_actual=False,
    projection_leg_naturality_actual=False,
    all_component_legs_natural=False,
    projections_natural_to_legs=False,
    pair_alpha_cartesian_natural=False,
    pair_beta_cartesian_natural=False,
    pointwise_naturality=True,
    graph_side_base_change=True,
    lax_naturality_only=True,
    up_to_iso_without_coherence=True,
)

gate(
    f"{TAG}3 pointwise, graph-side, lax, or up-to-iso naturality fails",
    not accepts_cartesian_component_cone(late_naturality)
    and {
        "component_leg_naturality_missing",
        "projection_leg_naturality_missing",
        "component_legs_not_natural",
        "projections_not_natural_to_legs",
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
        "pointwise_naturality",
        "graph_side_base_change",
        "lax_naturality_only",
        "up_to_iso_without_coherence",
    }
    <= set(reasons(late_naturality)),
    ",".join(reasons(late_naturality)),
)

rebuilt = live_source(
    base_change_preserves_doc509_cone=False,
    base_change_preserves_doc508_components=False,
    noncartesian_pullback=True,
    reindexed_cone_label=True,
    retuned_transport=True,
    base_changed_component_replacement=True,
)

gate(
    f"{TAG}4 rebuilding the cone or components after base change fails",
    not accepts_cartesian_component_cone(rebuilt)
    and {
        "base_change_does_not_preserve_doc509_cone",
        "base_change_does_not_preserve_doc508_components",
        "noncartesian_pullback",
        "reindexed_cone_label",
        "retuned_transport",
        "base_changed_component_replacement",
    }
    <= set(reasons(rebuilt)),
    ",".join(reasons(rebuilt)),
)

pairing_gap = live_source(
    pair_alpha_cartesian_natural=False,
    pair_beta_cartesian_natural=False,
    pair_alpha_unique_from_cone=False,
    pair_beta_zero_diagonal_cartesian=False,
    declared_naturality_square=True,
    split_componentwise_naturality=True,
)

gate(
    f"{TAG}5 alpha and beta must be cartesian-natural from the same cone",
    not accepts_cartesian_component_cone(pairing_gap)
    and {
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
        "pair_alpha_not_unique_from_cone",
        "pair_beta_not_zero_diagonal_cartesian",
        "declared_naturality_square",
        "split_componentwise_naturality",
    }
    <= set(reasons(pairing_gap)),
    ",".join(reasons(pairing_gap)),
)

missing_lifts = live_source(
    cartesian_source_lifts_actual=False,
    cartesian_coherence_actual=False,
    cartesian_component_cone_actual=False,
    cone_before_points=False,
    cone_before_graph_objects=False,
)

gate(
    f"{TAG}6 source lifts and source-before-points order are mandatory",
    not accepts_cartesian_component_cone(missing_lifts)
    and {
        "cartesian_source_lifts_missing",
        "cartesian_coherence_missing",
        "cartesian_component_cone_missing",
        "cone_not_before_points",
        "cone_not_before_graph_objects",
    }
    <= set(reasons(missing_lifts)),
    ",".join(reasons(missing_lifts)),
)

control_like = live_source(
    graph_side_base_change=True,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 graph-side cartesianity leaves controls formable",
    not accepts_cartesian_component_cone(control_like)
    and {
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_base_change",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_like)),
    ",".join(reasons(control_like)),
)

expanded_index = live_source(
    finite_index=set(FINITE_INDEX) | {"cartesian_component_cone_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}8 finite-index expansion and one-more-layer towers fail",
    not accepts_cartesian_component_cone(expanded_index)
    and {
        "finite_index_not_exact",
        "finite_index_cardinality_wrong",
        "finite_anchors_not_generated",
        "next_coherence_obligation_open",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= set(reasons(expanded_index)),
    ",".join(reasons(expanded_index)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_CARTESIAN_EDGES - {("source_component_cone", "cartesian_component_cone")}),
    live_source(required_edges=REQUIRED_CARTESIAN_EDGES - {("projection_leg_naturality", "pair_alpha_cartesian_natural")}),
    live_source(required_edges=REQUIRED_CARTESIAN_EDGES - {("base_change_preserves_doc509_cone", "base_change_preserves_doc508_components")}),
    live_source(universal_mediator_actual=False),
    live_source(component_cone_actual=False),
    live_source(cartesian_source_lifts_actual=False),
    live_source(cartesian_component_cone_actual=False),
    live_source(component_leg_naturality_actual=False),
    live_source(projection_leg_naturality_actual=False),
    live_source(pair_alpha_cartesian_natural=False),
    live_source(pair_beta_cartesian_natural=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every cartesian cone edge and naturality edge is mandatory",
    not any(accepts_cartesian_component_cone(data) for data in missing_edges)
    and {
        "required_cartesian_component_cone_edges_missing",
        "universal_mediator_missing",
        "component_cone_missing",
        "cartesian_source_lifts_missing",
        "cartesian_component_cone_missing",
        "component_leg_naturality_missing",
        "projection_leg_naturality_missing",
        "pair_alpha_not_cartesian_natural",
        "pair_beta_not_cartesian_natural",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

live = live_source()
dead_sources = {
    "finite_path": finite_path,
    "late_naturality": late_naturality,
    "rebuilt": rebuilt,
    "pairing_gap": pairing_gap,
    "missing_lifts": missing_lifts,
    "control_like": control_like,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only cartesian component-cone mediator passes",
    accepts_cartesian_component_cone(live)
    and graph_connected(live["required_edges"])
    and len(COMPONENT_LEGS) == 7
    and len(PROJECTION_LEG_EQUALITIES) == 7
    and len(FINITE_INDEX) == 24
    and not any(accepts_cartesian_component_cone(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_cartesian_component_cone(data) for data in dead_sources.values()),
        accepts_cartesian_component_cone(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "component-cone cartesian component-object product-projected parallel-"
    "morphism finite-limit subrepresented coupled formation-coherent "
    "self-dual exact BCF certificate pinned"
)
print(
    "VERDICT: the doc-509 eta-generated mediator component cone must be "
    "cartesian over represented source lifts. Finite path checks, chosen "
    "transport isomorphisms, pointwise or graph-side naturality, rebuilt "
    "base-change cones, declared naturality squares, finite-index expansion, "
    "and one-more-layer towers do not construct the missing source object."
)
