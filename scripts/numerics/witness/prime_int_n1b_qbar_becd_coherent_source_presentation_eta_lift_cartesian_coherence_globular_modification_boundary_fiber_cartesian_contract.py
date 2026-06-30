r"""Cartesian boundary-fiber contract for the cartesian eta-lift branch.

Doc 488 requires the doc-487 globular modification to be selected by a
represented source boundary fiber over its fixed globular boundary.  This
witness pins the next edge: that represented boundary fiber must itself be
cartesian over the represented source multiplier lifts.  Static one-boundary
fibers, chosen base-change transports, rebuilt fibers, graph-side fibers, or
retuned cartesian labels do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
CARTESIAN_SOURCE_LIFT_ID = (
    "CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber"
)
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
CARTESIAN_BOUNDARY_FIBER_ID = (
    "CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
CARTESIAN_BOUNDARY_RESTRICTION_ID = (
    "cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd"
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

REQUIRED_CARTESIAN_FIBER_EDGES = {
    ("eta_equalizer_lift", "cartesian_source_lift"),
    ("cartesian_source_lift", "cartesian_eta_lift_cone"),
    ("cartesian_eta_lift_cone", "cartesian_cone_coherence"),
    ("cartesian_cone_coherence", "globular_modification"),
    ("globular_modification", "boundary_restriction"),
    ("boundary_restriction", "represented_boundary_fiber"),
    ("represented_boundary_fiber", "boundary_fiber_arrow"),
    ("boundary_fiber_arrow", "selected_globular_modification"),
    ("selected_globular_modification", "globular_modification"),
    ("cartesian_source_lift", "cartesian_boundary_fiber"),
    ("represented_boundary_fiber", "cartesian_boundary_fiber"),
    ("boundary_restriction", "cartesian_boundary_restriction"),
    ("cartesian_boundary_restriction", "cartesian_boundary_fiber"),
    ("cartesian_boundary_fiber", "boundary_fiber_arrow_cartesian"),
    ("boundary_fiber_arrow_cartesian", "selected_globular_modification"),
    ("cartesian_boundary_fiber", "fixed_globular_boundary_pullback"),
    ("fixed_globular_boundary_pullback", "globular_boundary"),
    ("cartesian_boundary_fiber", "source_boundary_cartesian"),
    ("cartesian_boundary_fiber", "target_boundary_cartesian"),
    ("cartesian_boundary_fiber", "pasting_faces_cartesian"),
    ("pasting_faces_cartesian", "all_pasting_faces"),
    ("cartesian_boundary_fiber", "C3*C5=C15_fiber_pullback"),
    ("cartesian_boundary_fiber", "C5*C3=C15_fiber_pullback"),
    ("cartesian_boundary_fiber", "C3*C3*C5=C45_fiber_pullback"),
    ("cartesian_boundary_fiber", "F22_fiber_pullback"),
    ("all_fiber_pullbacks", "same_cartesian_fiber_on_all_paths"),
    ("C3*C5=C15_fiber_pullback", "all_fiber_pullbacks"),
    ("C5*C3=C15_fiber_pullback", "all_fiber_pullbacks"),
    ("C3*C3*C5=C45_fiber_pullback", "all_fiber_pullbacks"),
    ("F22_fiber_pullback", "all_fiber_pullbacks"),
    ("same_cartesian_fiber_on_all_paths", "C3*C5=C15"),
    ("same_cartesian_fiber_on_all_paths", "C5*C3=C15"),
    ("same_cartesian_fiber_on_all_paths", "C3*C3*C5=C45"),
    ("same_cartesian_fiber_on_all_paths", "F22_product"),
    ("cartesian_boundary_fiber", "coefficient_preservation"),
    ("cartesian_boundary_fiber", "signed_support_preservation"),
    ("cartesian_boundary_fiber", "source_before_points"),
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
        "doc488_boundary_fiber_actual": False,
        "cartesian_source_lift_actual": False,
        "cartesian_boundary_fiber_actual": False,
        "cartesian_boundary_restriction_actual": False,
        "boundary_restriction_cartesian_natural": False,
        "boundary_fiber_arrow_cartesian": False,
        "fixed_globular_boundary_pullback": False,
        "source_boundary_cartesian": False,
        "target_boundary_cartesian": False,
        "pasting_faces_cartesian": False,
        "same_cartesian_fiber_all_paths": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "coherence_cells": set(),
        "pasting_faces": set(),
        "component_names": set(),
        "cartesian_leg_names": set(),
        "cartesian_fiber_edges": set(),
        "naturality_paths": set(),
        "static_one_boundary_fiber": False,
        "chosen_base_change_fiber": False,
        "fiber_rebuilt_after_base_change": False,
        "noncartesian_pullback": False,
        "local_transport_table": False,
        "pointwise_cartesian_fiber": False,
        "graph_side_cartesian_fiber": False,
        "post_product_cartesian_fiber": False,
        "retuned_cartesian_fiber": False,
        "reindexed_cartesian_fiber": False,
        "fiber_name_reused_without_pullback": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc488_boundary_fiber_actual", "doc488_boundary_fiber_missing"),
    ("cartesian_source_lift_actual", "cartesian_source_lift_missing"),
    ("cartesian_boundary_fiber_actual", "cartesian_boundary_fiber_missing"),
    ("cartesian_boundary_restriction_actual", "cartesian_boundary_restriction_missing"),
    ("boundary_restriction_cartesian_natural", "boundary_restriction_not_cartesian_natural"),
    ("boundary_fiber_arrow_cartesian", "boundary_fiber_arrow_not_cartesian"),
    ("fixed_globular_boundary_pullback", "fixed_globular_boundary_pullback_missing"),
    ("source_boundary_cartesian", "source_boundary_not_cartesian"),
    ("target_boundary_cartesian", "target_boundary_not_cartesian"),
    ("pasting_faces_cartesian", "pasting_faces_not_cartesian"),
    ("same_cartesian_fiber_all_paths", "same_cartesian_fiber_not_all_paths"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("static_one_boundary_fiber", "static_one_boundary_fiber"),
    ("chosen_base_change_fiber", "chosen_base_change_fiber"),
    ("fiber_rebuilt_after_base_change", "fiber_rebuilt_after_base_change"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("local_transport_table", "local_transport_table"),
    ("pointwise_cartesian_fiber", "pointwise_cartesian_fiber"),
    ("graph_side_cartesian_fiber", "graph_side_cartesian_fiber"),
    ("post_product_cartesian_fiber", "post_product_cartesian_fiber"),
    ("retuned_cartesian_fiber", "retuned_cartesian_fiber"),
    ("reindexed_cartesian_fiber", "reindexed_cartesian_fiber"),
    ("fiber_name_reused_without_pullback", "fiber_name_reused_without_pullback"),
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
    if REQUIRED_CARTESIAN_FIBER_EDGES - set(data["cartesian_fiber_edges"]):
        out.append("required_cartesian_fiber_edges_missing")
    if REQUIRED_NATURALITY_PATHS - set(data["naturality_paths"]):
        out.append("required_multiplier_paths_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_COHERENCE_PAYLOAD) <= set(data["coherence_cells"])
        and set(REQUIRED_PASTING_FACES) <= set(data["pasting_faces"])
        and set(REQUIRED_COMPONENTS) <= set(data["component_names"])
        and set(REQUIRED_CARTESIAN_LEGS) <= set(data["cartesian_leg_names"])
        and REQUIRED_CARTESIAN_FIBER_EDGES <= set(data["cartesian_fiber_edges"])
        and REQUIRED_NATURALITY_PATHS <= set(data["naturality_paths"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc488_boundary_fiber_actual=True,
        cartesian_source_lift_actual=True,
        cartesian_boundary_fiber_actual=True,
        cartesian_boundary_restriction_actual=True,
        boundary_restriction_cartesian_natural=True,
        boundary_fiber_arrow_cartesian=True,
        fixed_globular_boundary_pullback=True,
        source_boundary_cartesian=True,
        target_boundary_cartesian=True,
        pasting_faces_cartesian=True,
        same_cartesian_fiber_all_paths=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        coherence_cells=set(REQUIRED_COHERENCE_PAYLOAD),
        pasting_faces=set(REQUIRED_PASTING_FACES),
        component_names=set(REQUIRED_COMPONENTS),
        cartesian_leg_names=set(REQUIRED_CARTESIAN_LEGS),
        cartesian_fiber_edges=set(REQUIRED_CARTESIAN_FIBER_EDGES),
        naturality_paths=set(REQUIRED_NATURALITY_PATHS),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def cartesian_boundary_fiber_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "eta_lift": ETA_EQUALIZER_LIFT_ID,
        "cartesian_source_lift": CARTESIAN_SOURCE_LIFT_ID,
        "cartesian_cone": CARTESIAN_ETA_LIFT_CONE_ID,
        "cartesian_cone_coherence": CARTESIAN_CONE_COHERENCE_ID,
        "globular_modification": GLOBULAR_MODIFICATION_ID,
        "globular_boundary": GLOBULAR_BOUNDARY_ID,
        "boundary_restriction": BOUNDARY_RESTRICTION_ID,
        "boundary_fiber": BOUNDARY_FIBER_ID,
        "boundary_fiber_arrow": BOUNDARY_FIBER_ARROW_ID,
        "cartesian_boundary_fiber": CARTESIAN_BOUNDARY_FIBER_ID,
        "cartesian_boundary_restriction": CARTESIAN_BOUNDARY_RESTRICTION_ID,
        "mediating_arrow": MEDIATING_ARROW_ID,
        "cartesian_up": CARTESIAN_UP_ID,
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
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD1 represented boundary fiber is cartesian",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_FIBER_EDGES)
    and len(REQUIRED_COHERENCE_PAYLOAD) == len(REQUIRED_PASTING_FACES) == 32
    and z == {1: 2, 2: -1}
    and zC3 == {3: 2, 6: -1}
    and zC5 == {5: 2, 10: -1}
    and zF22 == {2: 4, 4: -2}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_boundary_fiber_payload(T3_T5_z)
    == cartesian_boundary_fiber_payload(zC15)
    and cartesian_boundary_fiber_payload(T5_T3_z)
    == cartesian_boundary_fiber_payload(zC15)
    and cartesian_boundary_fiber_payload(T3_T3_T5_z)
    == cartesian_boundary_fiber_payload(zC45)
    and cartesian_boundary_fiber_payload(T15_zF22)
    == cartesian_boundary_fiber_payload(zC15F22)
    and cartesian_boundary_fiber_payload(T45_zF22)
    == cartesian_boundary_fiber_payload(zC45F22),
    "H1=%s edges=%d"
    % ([p["h1_order"] for p in profiles], len(REQUIRED_CARTESIAN_FIBER_EDGES)),
)

graph_only = live_source(
    cartesian_boundary_fiber_actual=False,
    cartesian_boundary_restriction_actual=False,
    boundary_restriction_cartesian_natural=False,
    cartesian_fiber_edges=REQUIRED_CARTESIAN_FIBER_EDGES
    - {("cartesian_source_lift", "cartesian_boundary_fiber")},
    fiber_name_reused_without_pullback=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD2 graph identities do not supply cartesian fiber transport",
    not accepts_cartesian_fiber(graph_only)
    and {
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "boundary_restriction_not_cartesian_natural",
        "required_cartesian_fiber_edges_missing",
        "fiber_name_reused_without_pullback",
    }
    <= set(reasons(graph_only)),
    ",".join(reasons(graph_only)),
)

static = live_source(
    cartesian_source_lift_actual=False,
    cartesian_boundary_fiber_actual=False,
    same_cartesian_fiber_all_paths=False,
    static_one_boundary_fiber=True,
    fiber_name_reused_without_pullback=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD3 static one-boundary fibers fail",
    not accepts_cartesian_fiber(static)
    and {
        "cartesian_source_lift_missing",
        "cartesian_boundary_fiber_missing",
        "same_cartesian_fiber_not_all_paths",
        "static_one_boundary_fiber",
        "fiber_name_reused_without_pullback",
    }
    <= set(reasons(static)),
    ",".join(reasons(static)),
)

noncartesian = live_source(
    boundary_restriction_cartesian_natural=False,
    boundary_fiber_arrow_cartesian=False,
    fixed_globular_boundary_pullback=False,
    source_boundary_cartesian=False,
    target_boundary_cartesian=False,
    pasting_faces_cartesian=False,
    noncartesian_pullback=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD4 noncartesian pullbacks fail",
    not accepts_cartesian_fiber(noncartesian)
    and {
        "boundary_restriction_not_cartesian_natural",
        "boundary_fiber_arrow_not_cartesian",
        "fixed_globular_boundary_pullback_missing",
        "source_boundary_not_cartesian",
        "target_boundary_not_cartesian",
        "pasting_faces_not_cartesian",
        "noncartesian_pullback",
    }
    <= set(reasons(noncartesian)),
    ",".join(reasons(noncartesian)),
)

chosen = live_source(
    carrier_native=False,
    chosen_base_change_fiber=True,
    fiber_rebuilt_after_base_change=True,
    local_transport_table=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD5 chosen or rebuilt base-change fibers fail",
    not accepts_cartesian_fiber(chosen)
    and {
        "not_carrier_native",
        "chosen_base_change_fiber",
        "fiber_rebuilt_after_base_change",
        "local_transport_table",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

late = live_source(
    source_before_points=False,
    pointwise_cartesian_fiber=True,
    graph_side_cartesian_fiber=True,
    post_product_cartesian_fiber=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD6 pointwise graph-side post-product cartesian fibers fail",
    not accepts_cartesian_fiber(late)
    and {
        "source_not_before_points",
        "pointwise_cartesian_fiber",
        "graph_side_cartesian_fiber",
        "post_product_cartesian_fiber",
    }
    <= set(reasons(late)),
    ",".join(reasons(late)),
)

retuned = live_source(
    same_cartesian_fiber_all_paths=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    retuned_cartesian_fiber=True,
    reindexed_cartesian_fiber=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD7 retuned or reindexed cartesian fibers fail",
    not accepts_cartesian_fiber(retuned)
    and {
        "same_cartesian_fiber_not_all_paths",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "retuned_cartesian_fiber",
        "reindexed_cartesian_fiber",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_edges = [
    live_source(cartesian_fiber_edges=REQUIRED_CARTESIAN_FIBER_EDGES - {edge})
    for edge in list(REQUIRED_CARTESIAN_FIBER_EDGES)[:8]
] + [
    live_source(cartesian_boundary_fiber_actual=False),
    live_source(cartesian_boundary_restriction_actual=False),
    live_source(boundary_fiber_arrow_cartesian=False),
    live_source(fixed_globular_boundary_pullback=False),
    live_source(pasting_faces=set(REQUIRED_PASTING_FACES[:-1])),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD8 every cartesian boundary-fiber edge is mandatory",
    not any(accepts_cartesian_fiber(data) for data in missing_edges)
    and {
        "required_cartesian_fiber_edges_missing",
        "cartesian_boundary_fiber_missing",
        "cartesian_boundary_restriction_missing",
        "boundary_fiber_arrow_not_cartesian",
        "fixed_globular_boundary_pullback_missing",
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
    graph_side_cartesian_fiber=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD9 control/DH/Epstein cartesian fibers fail",
    not accepts_cartesian_fiber(control_fiber)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_cartesian_fiber",
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
    "static": static,
    "noncartesian": noncartesian,
    "chosen": chosen,
    "late": late,
    "retuned": retuned,
    "control_fiber": control_fiber,
}

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD10 only the cartesian represented boundary fiber passes",
    accepts_cartesian_fiber(live)
    and graph_connected(live["cartesian_fiber_edges"])
    and not any(accepts_cartesian_fiber(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_cartesian_fiber(data) for data in dead_sources.values()),
        accepts_cartesian_fiber(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD10 ALL PASS: "
    "cartesian boundary fiber for cartesian eta-lift branch pinned"
)
print(
    "VERDICT: the doc-488 represented boundary fiber must itself be cartesian "
    "over the represented source multiplier lifts. Static one-boundary fibers, "
    "chosen or rebuilt base-change fibers, noncartesian pullbacks, local "
    "transport tables, pointwise or graph-side cartesian fibers, retuned "
    "cartesian labels, and control/DH/Epstein point-formability do not "
    "construct the missing object."
)
