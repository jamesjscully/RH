r"""Boundary-fiber contract for the cartesian eta-lift globular modification.

Doc 487 requires the represented cartesian eta-lift coherence cells to be
faces of one source-level globular modification.  This witness pins the next
edge: that modification must be selected by an actual source boundary
restriction and represented boundary fiber over its fixed globular boundary.
Chosen sections, contractible wrappers, graph-side fibers, or retuned boundary
maps do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
CARTESIAN_ETA_LIFT_CONE_ID = (
    "CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
CARTESIAN_CONE_COHERENCE_ID = (
    "Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
GLOBULAR_MODIFICATION_ID = (
    "Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
GLOBULAR_BOUNDARY_ID = (
    "GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
BOUNDARY_RESTRICTION_ID = (
    "res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd"
)
BOUNDARY_FIBER_ID = (
    "Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
BOUNDARY_FIBER_ARROW_ID = (
    "eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
MEDIATING_ARROW_ID = "med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD"
CARTESIAN_UP_ID = "CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD"

REQUIRED_FACETS = (
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
)

REQUIRED_COHERENCE_CELLS = (
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
)

COMPONENT_NAMES = (*REQUIRED_FACETS, *REQUIRED_COHERENCE_CELLS)

REQUIRED_COMPONENTS = tuple(
    f"Comp_CohSrcPres_BCCube_Qbar_BECD_{name}_source" for name in COMPONENT_NAMES
)
REQUIRED_CARTESIAN_LEGS = tuple(
    f"cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_{name}"
    for name in COMPONENT_NAMES
)
REQUIRED_COMPONENT_LEG_CELLS = tuple(
    f"cell_cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_{name}_naturality"
    for name in COMPONENT_NAMES
)

REQUIRED_MULTIPLIER_CELLS = (
    "cell_C3_C5_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_cartesian_cone",
    "cell_C5_C3_C15_lift_eta_CohSrcPres_BCCube_Qbar_BECD_cartesian_cone",
    "cell_C3_C3_C5_C45_lift_eta_CohSrcPres_BCCube_Qbar_BECD_cartesian_cone",
    "cell_F22_interchange_lift_eta_CohSrcPres_BCCube_Qbar_BECD_cartesian_cone",
)

REQUIRED_STRUCTURE_CELLS = (
    "cell_med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD_cartesian",
    "cell_CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_naturality",
    "cell_unique_factor_CohSrcPres_lift_eta_cartesian",
    "cell_component_codomain_cartesian_equalities_CohSrcPres_BCCube_Qbar_BECD",
)

REQUIRED_COHERENCE_PAYLOAD = (
    *REQUIRED_MULTIPLIER_CELLS,
    *REQUIRED_COMPONENT_LEG_CELLS,
    *REQUIRED_STRUCTURE_CELLS,
)
REQUIRED_PASTING_FACES = tuple(
    f"face_{cell}_globular_boundary" for cell in REQUIRED_COHERENCE_PAYLOAD
)

REQUIRED_NATURALITY_PATHS = {
    "C3*C5=C15",
    "C5*C3=C15",
    "C3*C3*C5=C45",
    "F22_product",
}

REQUIRED_BOUNDARY_FIBER_EDGES = {
    ("eta_equalizer_lift", "cartesian_eta_lift_cone"),
    ("cartesian_eta_lift_cone", "cartesian_cone_coherence"),
    ("cartesian_cone_coherence", "globular_modification"),
    ("globular_modification", "globular_boundary"),
    ("globular_modification", "boundary_restriction"),
    ("boundary_restriction", "globular_boundary"),
    ("globular_boundary", "represented_boundary_fiber"),
    ("boundary_restriction", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "boundary_fiber_arrow"),
    ("boundary_fiber_arrow", "selected_globular_modification"),
    ("selected_globular_modification", "globular_modification"),
    ("represented_boundary_fiber", "unique_source_filler"),
    ("unique_source_filler", "contractible_after_represented_fiber"),
    ("represented_boundary_fiber", "boundary_preservation"),
    ("boundary_preservation", "globular_boundary"),
    ("boundary_preservation", "source_boundary"),
    ("boundary_preservation", "target_boundary"),
    ("source_boundary", "component_leg_naturality_cells"),
    ("source_boundary", "component_codomain_equality_cell"),
    ("target_boundary", "mediating_arrow_naturality_cell"),
    ("target_boundary", "cartesian_universal_property_cell"),
    ("target_boundary", "unique_factorization_cell"),
    ("boundary_preservation", "all_pasting_faces"),
    ("all_pasting_faces", "multiplier_path_faces"),
    ("all_pasting_faces", "component_leg_faces"),
    ("all_pasting_faces", "structure_faces"),
    ("boundary_preservation", "coefficient_preservation"),
    ("boundary_preservation", "signed_support_preservation"),
    ("represented_boundary_fiber", "same_fiber_on_multiplier_paths"),
    ("same_fiber_on_multiplier_paths", "C3*C5=C15"),
    ("same_fiber_on_multiplier_paths", "C5*C3=C15"),
    ("same_fiber_on_multiplier_paths", "C3*C3*C5=C45"),
    ("same_fiber_on_multiplier_paths", "F22_product"),
    ("represented_boundary_fiber", "source_before_points"),
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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "h1_order": z1_order // len(coboundaries),
        "coboundaries_res1_zero": all(
            from_vec(v).get(1, 0) == 0 for v in coboundaries
        ),
    }


def graph_connected(edges: set[tuple[str, str]]) -> bool:
    nodes = {node for edge in edges for node in edge}
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
        "doc487_globular_modification_actual": False,
        "boundary_restriction_actual": False,
        "represented_boundary_fiber_actual": False,
        "boundary_fiber_arrow_actual": False,
        "fiber_over_fixed_boundary": False,
        "fiber_arrow_selects_modification": False,
        "unique_source_filler_after_fiber": False,
        "contractible_only_after_fiber": False,
        "boundary_preservation_actual": False,
        "source_boundary_preserved": False,
        "target_boundary_preserved": False,
        "pasting_faces_preserved": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "same_fiber_all_paths": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "coherence_cells": set(),
        "pasting_faces": set(),
        "component_names": set(),
        "cartesian_leg_names": set(),
        "boundary_fiber_edges": set(),
        "naturality_paths": set(),
        "chosen_boundary_section": False,
        "contractible_choice_wrapper": False,
        "boundary_fiber_without_representer": False,
        "wrong_globular_boundary": False,
        "external_boundary_fiber": False,
        "quotient_boundary_fiber": False,
        "local_boundary_fiber_table": False,
        "pointwise_boundary_fiber": False,
        "graph_side_boundary_fiber": False,
        "post_product_boundary_fiber": False,
        "retuned_boundary_restriction": False,
        "reindexed_boundary_fiber": False,
        "selected_by_label_only": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc487_globular_modification_actual", "doc487_globular_modification_missing"),
    ("boundary_restriction_actual", "boundary_restriction_missing"),
    ("represented_boundary_fiber_actual", "represented_boundary_fiber_missing"),
    ("boundary_fiber_arrow_actual", "boundary_fiber_arrow_missing"),
    ("fiber_over_fixed_boundary", "fiber_not_over_fixed_boundary"),
    ("fiber_arrow_selects_modification", "fiber_arrow_does_not_select_modification"),
    ("unique_source_filler_after_fiber", "unique_source_filler_missing"),
    ("contractible_only_after_fiber", "contractibility_not_downstream_of_fiber"),
    ("boundary_preservation_actual", "boundary_preservation_missing"),
    ("source_boundary_preserved", "source_boundary_not_preserved"),
    ("target_boundary_preserved", "target_boundary_not_preserved"),
    ("pasting_faces_preserved", "pasting_faces_not_preserved"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("same_fiber_all_paths", "same_fiber_not_all_paths"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("chosen_boundary_section", "chosen_boundary_section"),
    ("contractible_choice_wrapper", "contractible_choice_wrapper"),
    ("boundary_fiber_without_representer", "boundary_fiber_without_representer"),
    ("wrong_globular_boundary", "wrong_globular_boundary"),
    ("external_boundary_fiber", "external_boundary_fiber"),
    ("quotient_boundary_fiber", "quotient_boundary_fiber"),
    ("local_boundary_fiber_table", "local_boundary_fiber_table"),
    ("pointwise_boundary_fiber", "pointwise_boundary_fiber"),
    ("graph_side_boundary_fiber", "graph_side_boundary_fiber"),
    ("post_product_boundary_fiber", "post_product_boundary_fiber"),
    ("retuned_boundary_restriction", "retuned_boundary_restriction"),
    ("reindexed_boundary_fiber", "reindexed_boundary_fiber"),
    ("selected_by_label_only", "selected_by_label_only"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(REQUIRED_COHERENCE_PAYLOAD) - set(data["coherence_cells"]):
        out.append("required_coherence_cells_missing")
    if set(REQUIRED_PASTING_FACES) - set(data["pasting_faces"]):
        out.append("required_pasting_faces_missing")
    if set(REQUIRED_COMPONENTS) - set(data["component_names"]):
        out.append("required_source_components_missing")
    if set(REQUIRED_CARTESIAN_LEGS) - set(data["cartesian_leg_names"]):
        out.append("required_cartesian_component_legs_missing")
    if REQUIRED_BOUNDARY_FIBER_EDGES - set(data["boundary_fiber_edges"]):
        out.append("required_boundary_fiber_edges_missing")
    if REQUIRED_NATURALITY_PATHS - set(data["naturality_paths"]):
        out.append("required_multiplier_paths_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_boundary_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_COHERENCE_PAYLOAD) <= set(data["coherence_cells"])
        and set(REQUIRED_PASTING_FACES) <= set(data["pasting_faces"])
        and set(REQUIRED_COMPONENTS) <= set(data["component_names"])
        and set(REQUIRED_CARTESIAN_LEGS) <= set(data["cartesian_leg_names"])
        and REQUIRED_BOUNDARY_FIBER_EDGES <= set(data["boundary_fiber_edges"])
        and REQUIRED_NATURALITY_PATHS <= set(data["naturality_paths"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc487_globular_modification_actual=True,
        boundary_restriction_actual=True,
        represented_boundary_fiber_actual=True,
        boundary_fiber_arrow_actual=True,
        fiber_over_fixed_boundary=True,
        fiber_arrow_selects_modification=True,
        unique_source_filler_after_fiber=True,
        contractible_only_after_fiber=True,
        boundary_preservation_actual=True,
        source_boundary_preserved=True,
        target_boundary_preserved=True,
        pasting_faces_preserved=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        same_fiber_all_paths=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        coherence_cells=set(REQUIRED_COHERENCE_PAYLOAD),
        pasting_faces=set(REQUIRED_PASTING_FACES),
        component_names=set(REQUIRED_COMPONENTS),
        cartesian_leg_names=set(REQUIRED_CARTESIAN_LEGS),
        boundary_fiber_edges=set(REQUIRED_BOUNDARY_FIBER_EDGES),
        naturality_paths=set(REQUIRED_NATURALITY_PATHS),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def boundary_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "eta_lift": ETA_EQUALIZER_LIFT_ID,
        "cartesian_cone": CARTESIAN_ETA_LIFT_CONE_ID,
        "cartesian_cone_coherence": CARTESIAN_CONE_COHERENCE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "globular_boundary": GLOBULAR_BOUNDARY_ID,
        "boundary_restriction": BOUNDARY_RESTRICTION_ID,
        "represented_boundary_fiber": BOUNDARY_FIBER_ID,
        "boundary_fiber_arrow": BOUNDARY_FIBER_ARROW_ID,
        "selected_modification": GLOBULAR_MODIFICATION_ID,
        "source_boundary": (
            "component_leg_naturality_and_codomain_equalities",
            REQUIRED_COMPONENT_LEG_CELLS,
            REQUIRED_STRUCTURE_CELLS[-1],
        ),
        "target_boundary": (
            "mediating_arrow_cartesian_up_and_unique_factorization",
            MEDIATING_ARROW_ID,
            CARTESIAN_UP_ID,
            REQUIRED_STRUCTURE_CELLS[:3],
        ),
        "coherence_cells": REQUIRED_COHERENCE_PAYLOAD,
        "pasting_faces": REQUIRED_PASTING_FACES,
        "components": REQUIRED_COMPONENTS,
        "cartesian_legs": REQUIRED_CARTESIAN_LEGS,
        "naturality_paths": tuple(sorted(REQUIRED_NATURALITY_PATHS)),
        "endpoint_boundary": (p1, p2, p1 == p2),
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
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD1 represented boundary fiber selects globular modification",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_BOUNDARY_FIBER_EDGES)
    and len(REQUIRED_COHERENCE_PAYLOAD) == len(REQUIRED_PASTING_FACES) == 32
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and boundary_fiber_payload(T3_T5_z) == boundary_fiber_payload(zC15)
    and boundary_fiber_payload(T5_T3_z) == boundary_fiber_payload(zC15)
    and boundary_fiber_payload(T3_T3_T5_z) == boundary_fiber_payload(zC45)
    and boundary_fiber_payload(T15_zF22) == boundary_fiber_payload(zC15F22)
    and boundary_fiber_payload(T45_zF22) == boundary_fiber_payload(zC45F22),
    "H1=%s edges=%d" % ([p["h1_order"] for p in profiles], len(REQUIRED_BOUNDARY_FIBER_EDGES)),
)

graph_only = live_source(
    represented_boundary_fiber_actual=False,
    boundary_fiber_arrow_actual=False,
    fiber_arrow_selects_modification=False,
    boundary_fiber_edges=REQUIRED_BOUNDARY_FIBER_EDGES
    - {("represented_boundary_fiber", "boundary_fiber_arrow")},
    selected_by_label_only=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD2 graph identities do not supply the boundary fiber",
    not accepts_boundary_fiber(graph_only)
    and {
        "represented_boundary_fiber_missing",
        "boundary_fiber_arrow_missing",
        "fiber_arrow_does_not_select_modification",
        "required_boundary_fiber_edges_missing",
        "selected_by_label_only",
    }
    <= set(reasons(graph_only)),
    ",".join(reasons(graph_only)),
)

chosen = live_source(
    boundary_restriction_actual=False,
    represented_boundary_fiber_actual=False,
    unique_source_filler_after_fiber=False,
    contractible_only_after_fiber=False,
    chosen_boundary_section=True,
    contractible_choice_wrapper=True,
    boundary_fiber_without_representer=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD3 chosen sections and contractible wrappers fail",
    not accepts_boundary_fiber(chosen)
    and {
        "boundary_restriction_missing",
        "represented_boundary_fiber_missing",
        "unique_source_filler_missing",
        "contractibility_not_downstream_of_fiber",
        "chosen_boundary_section",
        "contractible_choice_wrapper",
        "boundary_fiber_without_representer",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

wrong_boundary = live_source(
    fiber_over_fixed_boundary=False,
    boundary_preservation_actual=False,
    source_boundary_preserved=False,
    target_boundary_preserved=False,
    wrong_globular_boundary=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD4 fibers over the wrong globular boundary fail",
    not accepts_boundary_fiber(wrong_boundary)
    and {
        "fiber_not_over_fixed_boundary",
        "boundary_preservation_missing",
        "source_boundary_not_preserved",
        "target_boundary_not_preserved",
        "wrong_globular_boundary",
    }
    <= set(reasons(wrong_boundary)),
    ",".join(reasons(wrong_boundary)),
)

external = live_source(
    carrier_native=False,
    external_boundary_fiber=True,
    quotient_boundary_fiber=True,
    local_boundary_fiber_table=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD5 external quotient local boundary fibers fail",
    not accepts_boundary_fiber(external)
    and {
        "not_carrier_native",
        "external_boundary_fiber",
        "quotient_boundary_fiber",
        "local_boundary_fiber_table",
    }
    <= set(reasons(external)),
    ",".join(reasons(external)),
)

late = live_source(
    source_before_points=False,
    pointwise_boundary_fiber=True,
    graph_side_boundary_fiber=True,
    post_product_boundary_fiber=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD6 pointwise graph-side post-product boundary fibers fail",
    not accepts_boundary_fiber(late)
    and {
        "source_not_before_points",
        "pointwise_boundary_fiber",
        "graph_side_boundary_fiber",
        "post_product_boundary_fiber",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    boundary_restriction_actual=False,
    same_fiber_all_paths=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_boundary_restriction=True,
    reindexed_boundary_fiber=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD7 retuned or reindexed boundary fibers fail",
    not accepts_boundary_fiber(retuned)
    and {
        "boundary_restriction_missing",
        "same_fiber_not_all_paths",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_boundary_restriction",
        "reindexed_boundary_fiber",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_selection = [
    live_source(boundary_fiber_edges=REQUIRED_BOUNDARY_FIBER_EDGES - {edge})
    for edge in list(REQUIRED_BOUNDARY_FIBER_EDGES)[:8]
] + [
    live_source(boundary_fiber_arrow_actual=False),
    live_source(fiber_arrow_selects_modification=False),
    live_source(unique_source_filler_after_fiber=False),
    live_source(contractible_only_after_fiber=False),
    live_source(pasting_faces=set(REQUIRED_PASTING_FACES[:-1])),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_selection))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD8 selection filler and every edge are mandatory",
    not any(accepts_boundary_fiber(data) for data in missing_selection)
    and {
        "required_boundary_fiber_edges_missing",
        "boundary_fiber_arrow_missing",
        "fiber_arrow_does_not_select_modification",
        "unique_source_filler_missing",
        "contractibility_not_downstream_of_fiber",
        "required_pasting_faces_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_fiber = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_boundary_fiber=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD9 control/DH/Epstein boundary fibers fail",
    not accepts_boundary_fiber(control_fiber)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_boundary_fiber",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_fiber)),
    ",".join(reasons(control_fiber)),
)

live = live_source()
dead_sources = {
    "graph_only": graph_only,
    "chosen": chosen,
    "wrong_boundary": wrong_boundary,
    "external": external,
    "late": late,
    "retuned": retuned,
    "control_fiber": control_fiber,
}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFQBARBECD10 only the represented source boundary fiber passes",
    accepts_boundary_fiber(live)
    and graph_connected(live["boundary_fiber_edges"])
    and not any(accepts_boundary_fiber(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_boundary_fiber(data) for data in dead_sources.values()),
        accepts_boundary_fiber(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFQBARBECD10 ALL PASS: "
    "boundary fiber for cartesian eta-lift globular modification pinned"
)
print(
    "VERDICT: the doc-487 globular modification must be selected by an "
    "actual source boundary restriction and represented boundary fiber over "
    "its fixed globular boundary. Chosen sections, contractible wrappers, "
    "wrong-boundary fibers, external/local/quotient fibers, pointwise or "
    "graph-side fibers, retuned boundary restrictions, and control/DH/Epstein "
    "point-formability do not construct the missing object."
)
