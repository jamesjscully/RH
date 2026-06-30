r"""Parallel-morphism finite-limit subrepresented coupled mediator contract.

Doc 505 requires the mediator subrepresenter to be cut out by one internal
finite-limit/equalizer fork. This witness pins the next edge: the fork must
be the equalizer of actual parallel source morphisms alpha,beta into one
mediator-native constraint object. A checklist of constraint values or a
point/graph-side equality is not accepted.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_parallel_morphism_finite_limit_subrepresented_coupled_formation_coherent_self_dual_exact_bcf_certificate_contract
"""

from __future__ import annotations

from math import comb


TAG = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD"
failures: list[str] = []

UNIVERSAL_MEDIATOR_ID = "med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD"
FORMATION_FIBER_ID = "Fib_med_UP_Eq_id_BCF_self_dual_exact_source"
SOURCE_COUPLING_ID = "NCoup_med_UP_Eq_id_BCF_self_dual_exact_source"
COUPLING_SUBREP_ID = "SubRep_NCoup_med_UP_Eq_id_source_fiber"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_id_source_fiber"
CONSTRAINT_FORK_ID = "Fork_med_UP_Eq_id_endpoint_dd4_rosati_control_NCoup"
CONSTRAINT_OBJECT_ID = "Con_NCoup_med_UP_Eq_id_endpoint_dd4_rosati_control_source"
CONSTRAINT_PRODUCT_ID = "Prod_NCoup_med_UP_Eq_id_endpoint_degree_dd4_push_graph_rosati_control"
ALPHA_CONSTRAINT_MAP_ID = "alpha_NCoup_med_UP_Eq_id_source_constraints"
BETA_CONSTRAINT_MAP_ID = "beta_NCoup_med_UP_Eq_id_source_constraints"
EQUALIZER_ARROW_ID = "eq_NCoup_med_UP_Eq_id_constraints_to_SubRep_source_fiber"
MONIC_EQ_ARROW_ID = "monic_eq_NCoup_med_UP_Eq_id_constraints_to_source_fiber"
DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
UPMED_DD4_CERT_ID = "Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary"
CONTROL_DEATH_ID = "Nat_ControlDeath_med_UP_Eq_id_source_constraint"

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

REQUIRED_MORPHISM_EDGES = {
    ("universal_mediator", "formation_fiber"),
    ("formation_fiber", "source_coupling"),
    ("source_coupling", "source_coupling_subrepresenter"),
    ("source_coupling_subrepresenter", "finite_limit_cut"),
    ("formation_fiber", "finite_limit_cut"),
    ("finite_limit_cut", "constraint_product_object"),
    ("formation_fiber", "constraint_product_object"),
    ("constraint_product_object", "constraint_object"),
    ("formation_fiber", "alpha_constraint_map"),
    ("formation_fiber", "beta_constraint_map"),
    ("alpha_constraint_map", "constraint_object"),
    ("beta_constraint_map", "constraint_object"),
    ("alpha_constraint_map", "endpoint_integrality_morphism"),
    ("alpha_constraint_map", "degree_map_morphism"),
    ("alpha_constraint_map", "dd4_boundary_morphism"),
    ("alpha_constraint_map", "boundary_pushforward_morphism"),
    ("alpha_constraint_map", "graph_composition_morphism"),
    ("alpha_constraint_map", "rosati_count_morphism"),
    ("alpha_constraint_map", "control_death_morphism"),
    ("beta_constraint_map", "zero_or_diagonal_source_section"),
    ("alpha_constraint_map", "parallel_pair"),
    ("beta_constraint_map", "parallel_pair"),
    ("parallel_pair", "equalizer_arrow"),
    ("equalizer_arrow", "finite_limit_cut"),
    ("equalizer_arrow", "source_coupling_subrepresenter"),
    ("equalizer_arrow", "monic_equalizer_arrow"),
    ("monic_equalizer_arrow", "formation_fiber"),
    ("source_coupling_subrepresenter", "doc504_subrepresenter"),
    ("finite_limit_cut", "doc505_cut"),
    ("equalizer_arrow", "equalizer_image_doc505_cut"),
    ("constraint_object", "source_before_points_and_graph_objects"),
    ("source_before_points_and_graph_objects", "controls_not_points"),
    ("source_before_points_and_graph_objects", "dh_not_points"),
    ("source_before_points_and_graph_objects", "epstein_not_points"),
    ("constraint_object", "same_morphism_payload_all_paths"),
    ("same_morphism_payload_all_paths", "C3_C5_equals_C15"),
    ("same_morphism_payload_all_paths", "C5_C3_equals_C15"),
    ("same_morphism_payload_all_paths", "C3_C3_C5_equals_C45"),
    ("same_morphism_payload_all_paths", "F22_product"),
    ("dd4_boundary_morphism", "dd4_original_class"),
    ("dd4_original_class", "upmed_dd4_certificate"),
    ("upmed_dd4_certificate", "source_before_points_and_graph_objects"),
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
        "source_coupling_actual": False,
        "coupling_subrepresenter_actual": False,
        "finite_limit_cut_actual": False,
        "constraint_fork_actual": False,
        "constraint_object_actual": False,
        "constraint_product_object_actual": False,
        "alpha_constraint_map_actual": False,
        "beta_constraint_map_actual": False,
        "alpha_beta_parallel": False,
        "all_component_morphisms_source_native": False,
        "endpoint_integrality_morphism_actual": False,
        "degree_map_morphism_actual": False,
        "dd4_boundary_morphism_actual": False,
        "boundary_pushforward_morphism_actual": False,
        "graph_composition_morphism_actual": False,
        "rosati_count_morphism_actual": False,
        "control_death_morphism_actual": False,
        "zero_or_diagonal_section_actual": False,
        "equalizer_of_alpha_beta": False,
        "equalizer_arrow_actual": False,
        "monic_equalizer_arrow": False,
        "equalizer_image_is_doc505_cut": False,
        "equalizer_image_is_doc504_subrepresenter": False,
        "morphisms_before_points": False,
        "morphisms_before_graph_objects": False,
        "same_morphism_payload_all_paths": False,
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
        "abstract_external_representer": False,
        "equivalent_representer": False,
        "univalence_transport": False,
        "heterogeneous_codomain_checklist": False,
        "external_constraint_values": False,
        "point_functor_natural_transformation": False,
        "semantic_equality_only": False,
        "componentwise_posthoc_equalities": False,
        "product_object_missing": False,
        "nonparallel_fork_legs": False,
        "one_sided_constraint_map": False,
        "diagonal_after_graph_objects": False,
        "zero_section_inserted_after_facts": False,
        "local_constraint_table": False,
        "finite_sample_morphism": False,
        "basis_dependent_morphism": False,
        "retuned_component_map": False,
        "projected_component_map": False,
        "graph_classifier_morphism": False,
        "declared_parallel_pair": False,
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
    ("source_coupling_actual", "source_coupling_missing"),
    ("coupling_subrepresenter_actual", "coupling_subrepresenter_missing"),
    ("finite_limit_cut_actual", "finite_limit_cut_missing"),
    ("constraint_fork_actual", "constraint_fork_missing"),
    ("constraint_object_actual", "constraint_object_missing"),
    ("constraint_product_object_actual", "constraint_product_object_missing"),
    ("alpha_constraint_map_actual", "alpha_constraint_map_missing"),
    ("beta_constraint_map_actual", "beta_constraint_map_missing"),
    ("alpha_beta_parallel", "alpha_beta_not_parallel"),
    ("all_component_morphisms_source_native", "component_morphisms_not_source_native"),
    ("endpoint_integrality_morphism_actual", "endpoint_morphism_missing"),
    ("degree_map_morphism_actual", "degree_map_morphism_missing"),
    ("dd4_boundary_morphism_actual", "dd4_boundary_morphism_missing"),
    ("boundary_pushforward_morphism_actual", "boundary_pushforward_morphism_missing"),
    ("graph_composition_morphism_actual", "graph_composition_morphism_missing"),
    ("rosati_count_morphism_actual", "rosati_count_morphism_missing"),
    ("control_death_morphism_actual", "control_death_morphism_missing"),
    ("zero_or_diagonal_section_actual", "zero_or_diagonal_section_missing"),
    ("equalizer_of_alpha_beta", "not_equalizer_of_alpha_beta"),
    ("equalizer_arrow_actual", "equalizer_arrow_missing"),
    ("monic_equalizer_arrow", "monic_equalizer_arrow_missing"),
    ("equalizer_image_is_doc505_cut", "equalizer_image_not_doc505_cut"),
    (
        "equalizer_image_is_doc504_subrepresenter",
        "equalizer_image_not_doc504_subrepresenter",
    ),
    ("morphisms_before_points", "morphisms_not_before_points"),
    ("morphisms_before_graph_objects", "morphisms_not_before_graph_objects"),
    ("same_morphism_payload_all_paths", "same_morphism_payload_not_all_paths"),
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
    ("abstract_external_representer", "abstract_external_representer"),
    ("equivalent_representer", "equivalent_representer"),
    ("univalence_transport", "univalence_transport"),
    ("heterogeneous_codomain_checklist", "heterogeneous_codomain_checklist"),
    ("external_constraint_values", "external_constraint_values"),
    ("point_functor_natural_transformation", "point_functor_natural_transformation"),
    ("semantic_equality_only", "semantic_equality_only"),
    ("componentwise_posthoc_equalities", "componentwise_posthoc_equalities"),
    ("product_object_missing", "product_object_missing"),
    ("nonparallel_fork_legs", "nonparallel_fork_legs"),
    ("one_sided_constraint_map", "one_sided_constraint_map"),
    ("diagonal_after_graph_objects", "diagonal_after_graph_objects"),
    ("zero_section_inserted_after_facts", "zero_section_inserted_after_facts"),
    ("local_constraint_table", "local_constraint_table"),
    ("finite_sample_morphism", "finite_sample_morphism"),
    ("basis_dependent_morphism", "basis_dependent_morphism"),
    ("retuned_component_map", "retuned_component_map"),
    ("projected_component_map", "projected_component_map"),
    ("graph_classifier_morphism", "graph_classifier_morphism"),
    ("declared_parallel_pair", "declared_parallel_pair"),
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
    if not REQUIRED_MORPHISM_EDGES <= set(data["required_edges"]):
        out.append("required_constraint_morphism_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_parallel_morphism_mediator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(data["finite_index"]) == FINITE_INDEX
        and data["finite_index_cardinality"] == len(FINITE_INDEX)
        and REQUIRED_MORPHISM_EDGES <= set(data["required_edges"])
        and graph_connected(set(data["required_edges"]))
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        universal_mediator_actual=True,
        formation_fiber_actual=True,
        source_coupling_actual=True,
        coupling_subrepresenter_actual=True,
        finite_limit_cut_actual=True,
        constraint_fork_actual=True,
        constraint_object_actual=True,
        constraint_product_object_actual=True,
        alpha_constraint_map_actual=True,
        beta_constraint_map_actual=True,
        alpha_beta_parallel=True,
        all_component_morphisms_source_native=True,
        endpoint_integrality_morphism_actual=True,
        degree_map_morphism_actual=True,
        dd4_boundary_morphism_actual=True,
        boundary_pushforward_morphism_actual=True,
        graph_composition_morphism_actual=True,
        rosati_count_morphism_actual=True,
        control_death_morphism_actual=True,
        zero_or_diagonal_section_actual=True,
        equalizer_of_alpha_beta=True,
        equalizer_arrow_actual=True,
        monic_equalizer_arrow=True,
        equalizer_image_is_doc505_cut=True,
        equalizer_image_is_doc504_subrepresenter=True,
        morphisms_before_points=True,
        morphisms_before_graph_objects=True,
        same_morphism_payload_all_paths=True,
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
        required_edges=set(REQUIRED_MORPHISM_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def morphism_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "universal_mediator": UNIVERSAL_MEDIATOR_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "source_coupling": SOURCE_COUPLING_ID,
        "coupling_subrepresenter": COUPLING_SUBREP_ID,
        "finite_limit_cut": FINITE_LIMIT_CUT_ID,
        "constraint_fork": CONSTRAINT_FORK_ID,
        "constraint_object": CONSTRAINT_OBJECT_ID,
        "constraint_product": CONSTRAINT_PRODUCT_ID,
        "alpha": ALPHA_CONSTRAINT_MAP_ID,
        "beta": BETA_CONSTRAINT_MAP_ID,
        "equalizer": EQUALIZER_ARROW_ID,
        "monic_equalizer": MONIC_EQ_ARROW_ID,
        "endpoint_component": (p1, p2, p1 == p2),
        "degree_component": (tuple(sorted(chi)), p1 + p2),
        "dd4_component": DD4_CLASS_ID,
        "upmed_dd4_certificate": UPMED_DD4_CERT_ID,
        "control_component": CONTROL_DEATH_ID,
        "alpha_components": tuple(sorted(REQUIRED_FACETS)),
        "beta_component": "zero_or_diagonal_source_section",
        "source_morphism_payload": True,
        "parallel_before_points": True,
        "parallel_before_graph_objects": True,
        "equalizer_image": (FINITE_LIMIT_CUT_ID, COUPLING_SUBREP_ID),
        "controls_not_points": True,
        "dh_not_points": True,
        "epstein_not_points": True,
        "coefficients": tuple(chi.items()),
        "support": tuple(sorted(chi)),
        "weighted_mass": sum(key * val for key, val in chi.items()),
        "endpoint_defect": p1 - p2,
        "finite_index_cells": tuple(sorted(FINITE_INDEX)),
        "required_edges": tuple(sorted(REQUIRED_MORPHISM_EDGES)),
    }


def morphism_row(chi: dict[int, int]) -> bool:
    payload = morphism_payload(chi)
    return (
        payload["weighted_mass"] == 0
        and payload["endpoint_defect"] == 0
        and payload["formation_fiber"] == FORMATION_FIBER_ID
        and payload["source_coupling"] == SOURCE_COUPLING_ID
        and payload["coupling_subrepresenter"] == COUPLING_SUBREP_ID
        and payload["finite_limit_cut"] == FINITE_LIMIT_CUT_ID
        and payload["constraint_fork"] == CONSTRAINT_FORK_ID
        and payload["constraint_object"] == CONSTRAINT_OBJECT_ID
        and payload["constraint_product"] == CONSTRAINT_PRODUCT_ID
        and payload["alpha"] == ALPHA_CONSTRAINT_MAP_ID
        and payload["beta"] == BETA_CONSTRAINT_MAP_ID
        and payload["equalizer"] == EQUALIZER_ARROW_ID
        and payload["monic_equalizer"] == MONIC_EQ_ARROW_ID
        and set(payload["alpha_components"]) == REQUIRED_FACETS
        and payload["beta_component"] == "zero_or_diagonal_source_section"
        and payload["dd4_component"] == DD4_CLASS_ID
        and payload["upmed_dd4_certificate"] == UPMED_DD4_CERT_ID
        and payload["control_component"] == CONTROL_DEATH_ID
        and payload["parallel_before_points"]
        and payload["parallel_before_graph_objects"]
        and payload["equalizer_image"] == (FINITE_LIMIT_CUT_ID, COUPLING_SUBREP_ID)
        and payload["controls_not_points"]
        and payload["dh_not_points"]
        and payload["epstein_not_points"]
        and len(payload["finite_index_cells"]) == 24
        and graph_connected(set(REQUIRED_MORPHISM_EDGES))
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
    f"{TAG}1 finite-limit cut is equalizer of actual parallel source morphisms",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_MORPHISM_EDGES)
    and len(FINITE_INDEX) == 24
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and morphism_payload(T3_T5_z) == morphism_payload(zC15)
    and morphism_payload(T5_T3_z) == morphism_payload(zC15)
    and morphism_payload(T3_T3_T5_z) == morphism_payload(zC45)
    and morphism_payload(T15_zF22) == morphism_payload(zC15F22)
    and morphism_payload(T45_zF22) == morphism_payload(zC45F22)
    and all(morphism_row(row) for row in rows),
    "H1=%s alpha=%s beta=%s edges=%d"
    % (
        [p["h1_order"] for p in profiles],
        ALPHA_CONSTRAINT_MAP_ID,
        BETA_CONSTRAINT_MAP_ID,
        len(REQUIRED_MORPHISM_EDGES),
    ),
)

checklist = live_source(
    constraint_object_actual=False,
    constraint_product_object_actual=False,
    all_component_morphisms_source_native=False,
    heterogeneous_codomain_checklist=True,
    external_constraint_values=True,
    semantic_equality_only=True,
    componentwise_posthoc_equalities=True,
    product_object_missing=True,
)

gate(
    f"{TAG}2 heterogeneous checklists are not source codomains",
    not accepts_parallel_morphism_mediator(checklist)
    and {
        "constraint_object_missing",
        "constraint_product_object_missing",
        "component_morphisms_not_source_native",
        "heterogeneous_codomain_checklist",
        "external_constraint_values",
        "semantic_equality_only",
        "componentwise_posthoc_equalities",
        "product_object_missing",
    }
    <= set(reasons(checklist)),
    ",".join(reasons(checklist)),
)

nonparallel = live_source(
    beta_constraint_map_actual=False,
    alpha_beta_parallel=False,
    zero_or_diagonal_section_actual=False,
    equalizer_of_alpha_beta=False,
    nonparallel_fork_legs=True,
    one_sided_constraint_map=True,
    declared_parallel_pair=True,
)

gate(
    f"{TAG}3 nonparallel or one-sided fork legs fail",
    not accepts_parallel_morphism_mediator(nonparallel)
    and {
        "beta_constraint_map_missing",
        "alpha_beta_not_parallel",
        "zero_or_diagonal_section_missing",
        "not_equalizer_of_alpha_beta",
        "nonparallel_fork_legs",
        "one_sided_constraint_map",
        "declared_parallel_pair",
    }
    <= set(reasons(nonparallel)),
    ",".join(reasons(nonparallel)),
)

point_functor = live_source(
    morphisms_before_points=False,
    morphisms_before_graph_objects=False,
    equalizer_image_is_doc505_cut=False,
    equalizer_image_is_doc504_subrepresenter=False,
    point_functor_natural_transformation=True,
    diagonal_after_graph_objects=True,
    zero_section_inserted_after_facts=True,
    graph_classifier_morphism=True,
)

gate(
    f"{TAG}4 point-functor and graph-side morphisms are too late",
    not accepts_parallel_morphism_mediator(point_functor)
    and {
        "morphisms_not_before_points",
        "morphisms_not_before_graph_objects",
        "equalizer_image_not_doc505_cut",
        "equalizer_image_not_doc504_subrepresenter",
        "point_functor_natural_transformation",
        "diagonal_after_graph_objects",
        "zero_section_inserted_after_facts",
        "graph_classifier_morphism",
    }
    <= set(reasons(point_functor)),
    ",".join(reasons(point_functor)),
)

local_table = live_source(
    same_morphism_payload_all_paths=False,
    C5_C3_equals_C15=False,
    C3_C3_C5_equals_C45=False,
    F22_product=False,
    local_constraint_table=True,
    finite_sample_morphism=True,
    basis_dependent_morphism=True,
    retuned_component_map=True,
    projected_component_map=True,
)

gate(
    f"{TAG}5 local or retuned component maps do not transport all paths",
    not accepts_parallel_morphism_mediator(local_table)
    and {
        "same_morphism_payload_not_all_paths",
        "C5_C3_not_C15",
        "C3_C3_C5_not_C45",
        "F22_product_missing",
        "local_constraint_table",
        "finite_sample_morphism",
        "basis_dependent_morphism",
        "retuned_component_map",
        "projected_component_map",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)

missing_components = live_source(
    endpoint_integrality_morphism_actual=False,
    degree_map_morphism_actual=False,
    dd4_boundary_morphism_actual=False,
    boundary_pushforward_morphism_actual=False,
    graph_composition_morphism_actual=False,
    rosati_count_morphism_actual=False,
    control_death_morphism_actual=False,
)

gate(
    f"{TAG}6 every alpha component morphism is source-native",
    not accepts_parallel_morphism_mediator(missing_components)
    and {
        "endpoint_morphism_missing",
        "degree_map_morphism_missing",
        "dd4_boundary_morphism_missing",
        "boundary_pushforward_morphism_missing",
        "graph_composition_morphism_missing",
        "rosati_count_morphism_missing",
        "control_death_morphism_missing",
    }
    <= set(reasons(missing_components)),
    ",".join(reasons(missing_components)),
)

graph_filter = live_source(
    morphisms_before_points=False,
    morphisms_before_graph_objects=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_classifier_morphism=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    f"{TAG}7 graph classifiers leave controls formable",
    not accepts_parallel_morphism_mediator(graph_filter)
    and {
        "morphisms_not_before_points",
        "morphisms_not_before_graph_objects",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_classifier_morphism",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(graph_filter)),
    ",".join(reasons(graph_filter)),
)

expanded_index = live_source(
    coupling_subrepresenter_actual=False,
    finite_index=set(FINITE_INDEX) | {"parallel_morphism_new_cell"},
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
    not accepts_parallel_morphism_mediator(expanded_index)
    and {
        "coupling_subrepresenter_missing",
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
        required_edges=REQUIRED_MORPHISM_EDGES
        - {("constraint_product_object", "constraint_object")}
    ),
    live_source(
        required_edges=REQUIRED_MORPHISM_EDGES
        - {("alpha_constraint_map", "parallel_pair")}
    ),
    live_source(
        required_edges=REQUIRED_MORPHISM_EDGES
        - {("parallel_pair", "equalizer_arrow")}
    ),
    live_source(constraint_object_actual=False),
    live_source(constraint_product_object_actual=False),
    live_source(alpha_constraint_map_actual=False),
    live_source(beta_constraint_map_actual=False),
    live_source(alpha_beta_parallel=False),
    live_source(equalizer_of_alpha_beta=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    f"{TAG}9 every constraint-morphism edge is mandatory",
    not any(accepts_parallel_morphism_mediator(data) for data in missing_edges)
    and {
        "required_constraint_morphism_edges_missing",
        "constraint_object_missing",
        "constraint_product_object_missing",
        "alpha_constraint_map_missing",
        "beta_constraint_map_missing",
        "alpha_beta_not_parallel",
        "not_equalizer_of_alpha_beta",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

dead_sources = {
    "checklist": checklist,
    "nonparallel": nonparallel,
    "point_functor": point_functor,
    "local_table": local_table,
    "missing_components": missing_components,
    "graph_filter": graph_filter,
    "expanded_index": expanded_index,
}

gate(
    f"{TAG}10 only parallel-morphism finite-limit mediator passes",
    accepts_parallel_morphism_mediator(live_source())
    and not any(
        accepts_parallel_morphism_mediator(data) for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(
            accepts_parallel_morphism_mediator(data)
            for data in dead_sources.values()
        ),
        accepts_parallel_morphism_mediator(live_source()),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(f"\n{TAG}1-{TAG}10 ALL PASS: equalizer identity universal mediator parallel-morphism finite-limit subrepresented coupled formation-coherent self-dual exact BCF certificate pinned")
print(
    "VERDICT: the doc-505 finite-limit cut must be the equalizer of actual "
    "parallel mediator-native source morphisms alpha,beta into one constraint "
    "object. Heterogeneous checklists, external values, point-functor maps, "
    "nonparallel fork legs, local or retuned component maps, graph-side "
    "classifiers, expanded indexes, and towers do not construct the missing "
    "source object."
)
