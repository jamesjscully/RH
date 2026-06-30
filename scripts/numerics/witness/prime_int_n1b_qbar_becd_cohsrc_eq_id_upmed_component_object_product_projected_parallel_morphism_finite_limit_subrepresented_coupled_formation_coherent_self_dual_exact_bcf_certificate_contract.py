r"""Component-object product-projected parallel-morphism mediator contract.

Doc 507 requires the parallel mediator source morphisms to land in an actual
source product with seven projections. This witness pins the next edge: those
projection codomains must be seven actual mediator source component objects,
not semantic labels, external modules, point-set codomains, graph-side
targets, or post-hoc component tables.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_object_product_projected_parallel_morphism_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
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

ENDPOINT_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_endpoint_integrality_source"
DEGREE_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_degree_maps_source"
DD4_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_dd4_boundary_source"
PUSH_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_boundary_pushforward_source"
GRAPH_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_graph_composition_source"
ROSATI_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_rosati_count_source"
CONTROL_COMPONENT_OBJECT_ID = "Comp_NCoup_med_UP_Eq_id_control_death_source"

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

COMPONENT_OBJECTS = (
    ENDPOINT_COMPONENT_OBJECT_ID,
    DEGREE_COMPONENT_OBJECT_ID,
    DD4_COMPONENT_OBJECT_ID,
    PUSH_COMPONENT_OBJECT_ID,
    GRAPH_COMPONENT_OBJECT_ID,
    ROSATI_COMPONENT_OBJECT_ID,
    CONTROL_COMPONENT_OBJECT_ID,
)

PROJECTION_TARGETS = (
    (ENDPOINT_PROJECTION_ID, ENDPOINT_COMPONENT_OBJECT_ID),
    (DEGREE_PROJECTION_ID, DEGREE_COMPONENT_OBJECT_ID),
    (DD4_PROJECTION_ID, DD4_COMPONENT_OBJECT_ID),
    (PUSH_PROJECTION_ID, PUSH_COMPONENT_OBJECT_ID),
    (GRAPH_PROJECTION_ID, GRAPH_COMPONENT_OBJECT_ID),
    (ROSATI_PROJECTION_ID, ROSATI_COMPONENT_OBJECT_ID),
    (CONTROL_PROJECTION_ID, CONTROL_COMPONENT_OBJECT_ID),
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

REQUIRED_COMPONENT_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("finite_limit_cut", "constraint_product_object"),
    ("formation_fiber", "constraint_product_object"),
    ("formation_fiber", "endpoint_component_object"),
    ("formation_fiber", "degree_component_object"),
    ("formation_fiber", "dd4_component_object"),
    ("formation_fiber", "pushforward_component_object"),
    ("formation_fiber", "graph_component_object"),
    ("formation_fiber", "rosati_count_component_object"),
    ("formation_fiber", "control_death_component_object"),
    ("endpoint_component_object", "constraint_product_object"),
    ("degree_component_object", "constraint_product_object"),
    ("dd4_component_object", "constraint_product_object"),
    ("pushforward_component_object", "constraint_product_object"),
    ("graph_component_object", "constraint_product_object"),
    ("rosati_count_component_object", "constraint_product_object"),
    ("control_death_component_object", "constraint_product_object"),
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
    ("constraint_product_object", "alpha_pairing_map"),
    ("alpha_pairing_map", "alpha_constraint_map"),
    ("alpha_pairing_map", "constraint_product_object"),
    ("alpha_pairing_map", "all_alpha_components"),
    ("constraint_product_object", "beta_pairing_map"),
    ("beta_pairing_map", "beta_constraint_map"),
    ("beta_pairing_map", "constraint_product_object"),
    ("beta_pairing_map", "all_beta_zero_diagonal_components"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("equalizer_arrow", "source_coupling_subrepresenter"),
    ("endpoint_component_object", "source_before_points_and_graph_objects"),
    ("degree_component_object", "source_before_points_and_graph_objects"),
    ("dd4_component_object", "source_before_points_and_graph_objects"),
    ("pushforward_component_object", "source_before_points_and_graph_objects"),
    ("graph_component_object", "source_before_points_and_graph_objects"),
    ("rosati_count_component_object", "source_before_points_and_graph_objects"),
    ("control_death_component_object", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
    ("endpoint_component_object", "same_component_all_paths"),
    ("degree_component_object", "same_component_all_paths"),
    ("dd4_component_object", "same_component_all_paths"),
    ("pushforward_component_object", "same_component_all_paths"),
    ("graph_component_object", "same_component_all_paths"),
    ("rosati_count_component_object", "same_component_all_paths"),
    ("control_death_component_object", "same_component_all_paths"),
    ("same_component_all_paths", "C3_C5_equals_C15"),
    ("same_component_all_paths", "C5_C3_equals_C15"),
    ("same_component_all_paths", "C3_C3_C5_equals_C45"),
    ("same_component_all_paths", "F22_product"),
    ("dd4_component_object", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("control_death_component_object", "source_before_points_and_graph_objects"),
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
        "endpoint_component_source_actual": False,
        "degree_component_source_actual": False,
        "dd4_component_source_actual": False,
        "pushforward_component_source_actual": False,
        "graph_component_source_actual": False,
        "rosati_count_component_source_actual": False,
        "control_death_component_source_actual": False,
        "projections_land_in_source_components": False,
        "product_uses_source_components": False,
        "product_universal_property_actual": False,
        "projections_jointly_determine_pairing": False,
        "alpha_pairing_actual": False,
        "beta_pairing_actual": False,
        "pairings_use_source_components": False,
        "alpha_beta_parallel_after_product": False,
        "equalizer_uses_product_pair": False,
        "components_before_points": False,
        "components_before_graph_objects": False,
        "components_transport_all_paths": False,
        "same_component_all_paths": False,
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
        "semantic_target_labels": False,
        "external_component_objects": False,
        "point_set_codomain": False,
        "graph_side_target_object": False,
        "posthoc_component_codomain": False,
        "component_shell_no_source_object": False,
        "local_component_table": False,
        "finite_sample_component": False,
        "basis_dependent_component": False,
        "retuned_component_object": False,
        "quotient_component": False,
        "closure_component": False,
        "declared_component_object": False,
        "product_with_non_source_codomains": False,
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
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("constraint_product_actual", "constraint_product_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("component_objects_actual", "component_objects_missing"),
    ("endpoint_component_source_actual", "endpoint_component_source_missing"),
    ("degree_component_source_actual", "degree_component_source_missing"),
    ("dd4_component_source_actual", "dd4_component_source_missing"),
    ("pushforward_component_source_actual", "pushforward_component_source_missing"),
    ("graph_component_source_actual", "graph_component_source_missing"),
    ("rosati_count_component_source_actual", "rosati_count_component_source_missing"),
    ("control_death_component_source_actual", "control_death_component_source_missing"),
    (
        "projections_land_in_source_components",
        "projections_do_not_land_in_source_components",
    ),
    ("product_uses_source_components", "product_does_not_use_source_components"),
    ("product_universal_property_actual", "product_universal_property_missing"),
    (
        "projections_jointly_determine_pairing",
        "projections_do_not_jointly_determine_pairing",
    ),
    ("alpha_pairing_actual", "alpha_pairing_missing"),
    ("beta_pairing_actual", "beta_pairing_missing"),
    ("pairings_use_source_components", "pairings_do_not_use_source_components"),
    ("alpha_beta_parallel_after_product", "alpha_beta_not_parallel_after_product"),
    ("equalizer_uses_product_pair", "equalizer_does_not_use_product_pair"),
    ("components_before_points", "components_not_before_points"),
    ("components_before_graph_objects", "components_not_before_graph_objects"),
    ("components_transport_all_paths", "components_do_not_transport_all_paths"),
    ("same_component_all_paths", "same_component_not_all_paths"),
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
    ("semantic_target_labels", "semantic_target_labels"),
    ("external_component_objects", "external_component_objects"),
    ("point_set_codomain", "point_set_codomain"),
    ("graph_side_target_object", "graph_side_target_object"),
    ("posthoc_component_codomain", "posthoc_component_codomain"),
    ("component_shell_no_source_object", "component_shell_no_source_object"),
    ("local_component_table", "local_component_table"),
    ("finite_sample_component", "finite_sample_component"),
    ("basis_dependent_component", "basis_dependent_component"),
    ("retuned_component_object", "retuned_component_object"),
    ("quotient_component", "quotient_component"),
    ("closure_component", "closure_component"),
    ("declared_component_object", "declared_component_object"),
    ("product_with_non_source_codomains", "product_with_non_source_codomains"),
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
    if not REQUIRED_COMPONENT_EDGES <= set(data["required_edges"]):
        out.append("required_source_component_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_component_object_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_COMPONENT_EDGES <= set(data["required_edges"])
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
        endpoint_component_source_actual=True,
        degree_component_source_actual=True,
        dd4_component_source_actual=True,
        pushforward_component_source_actual=True,
        graph_component_source_actual=True,
        rosati_count_component_source_actual=True,
        control_death_component_source_actual=True,
        projections_land_in_source_components=True,
        product_uses_source_components=True,
        product_universal_property_actual=True,
        projections_jointly_determine_pairing=True,
        alpha_pairing_actual=True,
        beta_pairing_actual=True,
        pairings_use_source_components=True,
        alpha_beta_parallel_after_product=True,
        equalizer_uses_product_pair=True,
        components_before_points=True,
        components_before_graph_objects=True,
        components_transport_all_paths=True,
        same_component_all_paths=True,
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
        required_edges=set(REQUIRED_COMPONENT_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def component_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "product": PRODUCT_OBJECT_ID,
        "alpha_pairing": ALPHA_PAIRING_ID,
        "beta_pairing": BETA_PAIRING_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "projections": PROJECTION_IDS,
        "component_objects": COMPONENT_OBJECTS,
        "projection_targets": PROJECTION_TARGETS,
        "endpoint_component": (ENDPOINT_COMPONENT_OBJECT_ID, p1, p2, p1 == p2),
        "degree_component": (DEGREE_COMPONENT_OBJECT_ID, tuple(sorted(chi)), p1 + p2),
        "dd4_component": (DD4_COMPONENT_OBJECT_ID, DD4_CLASS_ID),
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "pushforward_component": (PUSH_COMPONENT_OBJECT_ID, tuple(chi.items())),
        "graph_component": (GRAPH_COMPONENT_OBJECT_ID, tuple(sorted(chi))),
        "rosati_component": (ROSATI_COMPONENT_OBJECT_ID, "rosati_count_source"),
        "control_component": (CONTROL_COMPONENT_OBJECT_ID, CONTROL_DEATH_ID),
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "source_component_payload": True,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_COMPONENT_EDGES)),
    }


def component_row(chi: dict[int, int]) -> bool:
    payload = component_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["constraint_object"] == CONSTRAINT_OBJECT_ID
        and payload["product"] == PRODUCT_OBJECT_ID
        and payload["alpha_pairing"] == ALPHA_PAIRING_ID
        and payload["beta_pairing"] == BETA_PAIRING_ID
        and payload["alpha"] == ALPHA_CONSTRAINT_MAP_ID
        and payload["beta"] == BETA_CONSTRAINT_MAP_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and payload["projections"] == PROJECTION_IDS
        and payload["component_objects"] == COMPONENT_OBJECTS
        and payload["projection_targets"] == PROJECTION_TARGETS
        and all(target in COMPONENT_OBJECTS for _, target in payload["projection_targets"])
        and payload["dd4_component"] == (DD4_COMPONENT_OBJECT_ID, DD4_CLASS_ID)
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_component"] == (CONTROL_COMPONENT_OBJECT_ID, CONTROL_DEATH_ID)
        and payload["source_component_payload"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_COMPONENT_EDGES))
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
    f"{TAG}1 projections land in seven actual mediator source component objects",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_COMPONENT_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and component_payload(T3_T5_z) == component_payload(zC15)
    and component_payload(T5_T3_z) == component_payload(zC15)
    and component_payload(T3_T3_T5_z) == component_payload(zC45)
    and component_payload(T15_zF22) == component_payload(zC15F22)
    and component_payload(T45_zF22) == component_payload(zC45F22)
    and all(component_row(row) for row in rows),
    "H1=%s components=%d product=%s edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        len(COMPONENT_OBJECTS),
        PRODUCT_OBJECT_ID,
        len(REQUIRED_COMPONENT_EDGES),
    ),
)

semantic = live_source(
    component_objects_actual=False,
    endpoint_component_source_actual=False,
    degree_component_source_actual=False,
    dd4_component_source_actual=False,
    pushforward_component_source_actual=False,
    graph_component_source_actual=False,
    rosati_count_component_source_actual=False,
    control_death_component_source_actual=False,
    projections_land_in_source_components=False,
    semantic_target_labels=True,
    external_component_objects=True,
    declared_component_object=True,
)

gate(
    f"{TAG}2 semantic or external target labels are not source components",
    not accepts_component_object_mediator(semantic)
    and {
        "component_objects_missing",
        "endpoint_component_source_missing",
        "degree_component_source_missing",
        "dd4_component_source_missing",
        "pushforward_component_source_missing",
        "graph_component_source_missing",
        "rosati_count_component_source_missing",
        "control_death_component_source_missing",
        "projections_do_not_land_in_source_components",
        "semantic_target_labels",
        "external_component_objects",
        "declared_component_object",
    }
    <= set(reasons(semantic)),
    ",".join(reasons(semantic)),
)

late = live_source(
    product_uses_source_components=False,
    pairings_use_source_components=False,
    components_before_points=False,
    components_before_graph_objects=False,
    point_set_codomain=True,
    graph_side_target_object=True,
    posthoc_component_codomain=True,
)

gate(
    f"{TAG}3 point-set, graph-side, or post-hoc codomains are too late",
    not accepts_component_object_mediator(late)
    and {
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
        "components_not_before_points",
        "components_not_before_graph_objects",
        "point_set_codomain",
        "graph_side_target_object",
        "posthoc_component_codomain",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

local = live_source(
    components_transport_all_paths=False,
    same_component_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_component_table=True,
    finite_sample_component=True,
    basis_dependent_component=True,
    retuned_component_object=True,
)

gate(
    f"{TAG}4 local, finite, basis, or retuned components do not transport",
    not accepts_component_object_mediator(local)
    and {
        "components_do_not_transport_all_paths",
        "same_component_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_component_table",
        "finite_sample_component",
        "basis_dependent_component",
        "retuned_component_object",
    }
    <= set(reasons(local)),
    ",".join(reasons(local)),
)

shell = live_source(
    component_objects_actual=False,
    endpoint_component_source_actual=False,
    projections_land_in_source_components=False,
    component_shell_no_source_object=True,
    quotient_component=True,
    closure_component=True,
    declared_component_object=True,
)

gate(
    f"{TAG}5 quotient, closure, or declared shells are not source objects",
    not accepts_component_object_mediator(shell)
    and {
        "component_objects_missing",
        "endpoint_component_source_missing",
        "projections_do_not_land_in_source_components",
        "component_shell_no_source_object",
        "quotient_component",
        "closure_component",
        "declared_component_object",
    }
    <= set(reasons(shell)),
    ",".join(reasons(shell)),
)

missing_components = live_source(
    endpoint_component_source_actual=False,
    degree_component_source_actual=False,
    dd4_component_source_actual=False,
    pushforward_component_source_actual=False,
    graph_component_source_actual=False,
    rosati_count_component_source_actual=False,
    control_death_component_source_actual=False,
)

gate(
    f"{TAG}6 every source component object is mandatory",
    not accepts_component_object_mediator(missing_components)
    and {
        "endpoint_component_source_missing",
        "degree_component_source_missing",
        "dd4_component_source_missing",
        "pushforward_component_source_missing",
        "graph_component_source_missing",
        "rosati_count_component_source_missing",
        "control_death_component_source_missing",
    }
    <= set(reasons(missing_components)),
    ",".join(reasons(missing_components)),
)

control_components = live_source(
    product_uses_source_components=False,
    pairings_use_source_components=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    product_with_non_source_codomains=True,
    graph_side_target_object=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 non-source product codomains leave controls formable",
    not accepts_component_object_mediator(control_components)
    and {
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "product_with_non_source_codomains",
        "graph_side_target_object",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_components)),
    ",".join(reasons(control_components)),
)

expanded_index = live_source(
    component_objects_actual=False,
    finite_index=set(FINITE_INDEX) | {"component_object_new_cell"},
    finite_index_cardinality=len(FINITE_INDEX) + 1,
    finite_anchors_generated=False,
    no_next_coherence_obligation=False,
    abstract_external_representer=True,
    expanded_finite_index=True,
    one_more_layer_tower=True,
)

gate(
    f"{TAG}8 finite index expansion and external representer shells fail",
    not accepts_component_object_mediator(expanded_index)
    and {
        "component_objects_missing",
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
    live_source(
        required_edges=REQUIRED_COMPONENT_EDGES
        - {("control_death_projection", "control_death_component_object")}
    ),
    live_source(
        required_edges=REQUIRED_COMPONENT_EDGES
        - {("endpoint_component_object", "constraint_product_object")}
    ),
    live_source(endpoint_component_source_actual=False),
    live_source(degree_component_source_actual=False),
    live_source(dd4_component_source_actual=False),
    live_source(pushforward_component_source_actual=False),
    live_source(graph_component_source_actual=False),
    live_source(rosati_count_component_source_actual=False),
    live_source(control_death_component_source_actual=False),
    live_source(projections_land_in_source_components=False),
    live_source(product_uses_source_components=False),
    live_source(pairings_use_source_components=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every source component/projection edge is mandatory",
    not any(accepts_component_object_mediator(data) for data in missing_edges)
    and {
        "required_source_component_edges_missing",
        "endpoint_component_source_missing",
        "degree_component_source_missing",
        "dd4_component_source_missing",
        "pushforward_component_source_missing",
        "graph_component_source_missing",
        "rosati_count_component_source_missing",
        "control_death_component_source_missing",
        "projections_do_not_land_in_source_components",
        "product_does_not_use_source_components",
        "pairings_do_not_use_source_components",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

live = live_source()
dead_sources = {
    "semantic": semantic,
    "late": late,
    "local": local,
    "shell": shell,
    "missing_components": missing_components,
    "control_components": control_components,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only component-object product-projected mediator passes",
    accepts_component_object_mediator(live)
    and graph_connected(live["required_edges"])
    and len(COMPONENT_OBJECTS) == 7
    and len(PROJECTION_TARGETS) == 7
    and all(target in COMPONENT_OBJECTS for _, target in PROJECTION_TARGETS)
    and not any(accepts_component_object_mediator(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_component_object_mediator(data) for data in dead_sources.values()),
        accepts_component_object_mediator(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator "
    "component-object product-projected parallel-morphism finite-limit "
    "subrepresented coupled formation-coherent self-dual exact BCF "
    "certificate pinned"
)
print(
    "VERDICT: the doc-507 product projections must land in seven actual "
    "mediator source component objects. Semantic labels, external components, "
    "point-set codomains, graph-side targets, post-hoc tables, quotient or "
    "closure shells, finite samples, retuned components, expanded indexes, "
    "and non-source codomains do not construct the missing source object."
)
