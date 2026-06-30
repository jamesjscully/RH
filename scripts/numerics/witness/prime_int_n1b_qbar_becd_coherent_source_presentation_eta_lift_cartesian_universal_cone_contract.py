r"""Cartesian universal-cone contract for the coherent source-presentation eta lift.

Doc 484 requires the doc-483 eta lift to form a source-native universal cone
over the actual coherent source-presentation component codomains.  This
witness pins the next edge: that universal cone must be cartesian over the
represented source lifts.  Finite path checks, chosen transport isomorphisms,
pointwise naturality, or graph-side base change do not make the missing
object stable in the source fibration.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_universal_cone_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
ETA_LIFT_CONE_ID = "Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
CARTESIAN_LIFTS_ID = "CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber"
CARTESIAN_ETA_LIFT_CONE_ID = (
    "CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
)
CARTESIAN_UP_ID = "CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD"
CARTESIAN_MEDIATING_NAT_ID = (
    "Nat_med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD_cartesian"
)
UNIVERSAL_CONE_ID = "UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD"
UNIQUE_FACTOR_ID = "uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD"
MEDIATING_ARROW_ID = "med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD"

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

REQUIRED_LEGS = tuple(
    f"leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_{name}" for name in COMPONENT_NAMES
)

REQUIRED_CARTESIAN_LEGS = tuple(
    f"cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_{name}"
    for name in COMPONENT_NAMES
)

REQUIRED_NATURALITY_PATHS = {
    "C3*C5=C15",
    "C5*C3=C15",
    "C3*C3*C5=C45",
    "F22_product",
}

REQUIRED_CARTESIAN_EDGES = {
    ("eta_equalizer_lift", "eta_lift_universal_cone"),
    ("eta_lift_universal_cone", "cartesian_eta_lift_cone"),
    ("cartesian_source_lifts", "cartesian_eta_lift_cone"),
    ("cartesian_eta_lift_cone", "C3_cone_pullback"),
    ("cartesian_eta_lift_cone", "C5_cone_pullback"),
    ("cartesian_eta_lift_cone", "C15_cone_pullback"),
    ("cartesian_eta_lift_cone", "C45_cone_pullback"),
    ("cartesian_eta_lift_cone", "F22_cone_pullback"),
    ("cartesian_eta_lift_cone", "base_change_preserves_universal_cone"),
    ("base_change_preserves_universal_cone", "component_leg_cartesian_naturality"),
    ("base_change_preserves_universal_cone", "mediating_arrow_cartesian_naturality"),
    ("component_leg_cartesian_naturality", "cartesian_component_legs"),
    ("cartesian_component_legs", "actual_source_components"),
    ("component_leg_cartesian_naturality", "component_leg_codomain_equalities"),
    ("mediating_arrow_cartesian_naturality", "cartesian_universal_property"),
    ("cartesian_universal_property", "unique_factorization"),
    ("unique_factorization", "mediating_arrow"),
    ("mediating_arrow", "eta_equalizer_lift"),
    ("cartesian_eta_lift_cone", "same_cartesian_cone_on_multiplier_paths"),
    ("same_cartesian_cone_on_multiplier_paths", "C3*C5=C15"),
    ("same_cartesian_cone_on_multiplier_paths", "C5*C3=C15"),
    ("same_cartesian_cone_on_multiplier_paths", "C3*C3*C5=C45"),
    ("same_cartesian_cone_on_multiplier_paths", "F22_product"),
    ("cartesian_eta_lift_cone", "coherence_preserves_coefficients"),
    ("cartesian_eta_lift_cone", "coherence_preserves_signed_support"),
    ("cartesian_eta_lift_cone", "source_before_points"),
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
        "doc484_universal_cone_actual": False,
        "cartesian_source_lifts_actual": False,
        "cartesian_eta_lift_cone_actual": False,
        "base_change_preserves_universal_cone": False,
        "component_leg_cartesian_naturality": False,
        "mediating_arrow_cartesian_naturality": False,
        "cartesian_universal_property_actual": False,
        "unique_factorization_actual": False,
        "mediating_arrow_actual": False,
        "same_cartesian_cone_all_paths": False,
        "actual_source_components": False,
        "cartesian_component_legs_actual": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "component_names": set(),
        "leg_names": set(),
        "cartesian_leg_names": set(),
        "required_edges": set(),
        "naturality_paths": set(),
        "finite_path_checks": False,
        "sampled_transport": False,
        "pointwise_naturality": False,
        "graph_side_base_change": False,
        "local_transport_table": False,
        "chosen_transport_isomorphism": False,
        "up_to_iso_without_coherence": False,
        "lax_naturality": False,
        "noncartesian_pullback": False,
        "reindexed_cone_labels": False,
        "retuned_transport": False,
        "base_changed_component_replacements": False,
        "declared_naturality_squares": False,
        "split_componentwise_naturality": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc484_universal_cone_actual", "doc484_universal_cone_missing"),
    ("cartesian_source_lifts_actual", "cartesian_source_lifts_missing"),
    ("cartesian_eta_lift_cone_actual", "cartesian_eta_lift_cone_missing"),
    ("base_change_preserves_universal_cone", "base_change_does_not_preserve_universal_cone"),
    ("component_leg_cartesian_naturality", "component_leg_cartesian_naturality_missing"),
    ("mediating_arrow_cartesian_naturality", "mediating_arrow_cartesian_naturality_missing"),
    ("cartesian_universal_property_actual", "cartesian_universal_property_missing"),
    ("unique_factorization_actual", "unique_factorization_missing"),
    ("mediating_arrow_actual", "mediating_arrow_missing"),
    ("same_cartesian_cone_all_paths", "same_cartesian_cone_not_all_paths"),
    ("actual_source_components", "actual_source_components_missing"),
    ("cartesian_component_legs_actual", "cartesian_component_legs_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("finite_path_checks", "finite_path_checks"),
    ("sampled_transport", "sampled_transport"),
    ("pointwise_naturality", "pointwise_naturality"),
    ("graph_side_base_change", "graph_side_base_change"),
    ("local_transport_table", "local_transport_table"),
    ("chosen_transport_isomorphism", "chosen_transport_isomorphism"),
    ("up_to_iso_without_coherence", "up_to_iso_without_coherence"),
    ("lax_naturality", "lax_naturality"),
    ("noncartesian_pullback", "noncartesian_pullback"),
    ("reindexed_cone_labels", "reindexed_cone_labels"),
    ("retuned_transport", "retuned_transport"),
    ("base_changed_component_replacements", "base_changed_component_replacements"),
    ("declared_naturality_squares", "declared_naturality_squares"),
    ("split_componentwise_naturality", "split_componentwise_naturality"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(REQUIRED_COMPONENTS) - set(data["component_names"]):
        out.append("required_source_components_missing")
    if set(REQUIRED_LEGS) - set(data["leg_names"]):
        out.append("required_component_legs_missing")
    if set(REQUIRED_CARTESIAN_LEGS) - set(data["cartesian_leg_names"]):
        out.append("required_cartesian_component_legs_missing")
    if REQUIRED_CARTESIAN_EDGES - set(data["required_edges"]):
        out.append("required_cartesian_universal_cone_edges_missing")
    if REQUIRED_NATURALITY_PATHS - set(data["naturality_paths"]):
        out.append("required_multiplier_paths_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_cartesian_universal_cone(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_COMPONENTS) <= set(data["component_names"])
        and set(REQUIRED_LEGS) <= set(data["leg_names"])
        and set(REQUIRED_CARTESIAN_LEGS) <= set(data["cartesian_leg_names"])
        and REQUIRED_CARTESIAN_EDGES <= set(data["required_edges"])
        and REQUIRED_NATURALITY_PATHS <= set(data["naturality_paths"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc484_universal_cone_actual=True,
        cartesian_source_lifts_actual=True,
        cartesian_eta_lift_cone_actual=True,
        base_change_preserves_universal_cone=True,
        component_leg_cartesian_naturality=True,
        mediating_arrow_cartesian_naturality=True,
        cartesian_universal_property_actual=True,
        unique_factorization_actual=True,
        mediating_arrow_actual=True,
        same_cartesian_cone_all_paths=True,
        actual_source_components=True,
        cartesian_component_legs_actual=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        component_names=set(REQUIRED_COMPONENTS),
        leg_names=set(REQUIRED_LEGS),
        cartesian_leg_names=set(REQUIRED_CARTESIAN_LEGS),
        required_edges=set(REQUIRED_CARTESIAN_EDGES),
        naturality_paths=set(REQUIRED_NATURALITY_PATHS),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def cartesian_cone_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "eta_lift": ETA_EQUALIZER_LIFT_ID,
        "universal_cone": ETA_LIFT_CONE_ID,
        "cartesian_lifts": CARTESIAN_LIFTS_ID,
        "cartesian_cone": CARTESIAN_ETA_LIFT_CONE_ID,
        "cartesian_up": CARTESIAN_UP_ID,
        "cartesian_mediating_naturality": CARTESIAN_MEDIATING_NAT_ID,
        "universal_property": UNIVERSAL_CONE_ID,
        "unique_factor": UNIQUE_FACTOR_ID,
        "mediating_arrow": MEDIATING_ARROW_ID,
        "components": REQUIRED_COMPONENTS,
        "legs": REQUIRED_LEGS,
        "cartesian_legs": REQUIRED_CARTESIAN_LEGS,
        "facets": REQUIRED_FACETS,
        "cells": REQUIRED_COHERENCE_CELLS,
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
    "CATCOHSRCPRESETACARTCONEQBARBECD1 eta-lift universal cone is cartesian over source lifts",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CARTESIAN_EDGES)
    and len(REQUIRED_COMPONENTS) == len(REQUIRED_LEGS) == len(REQUIRED_CARTESIAN_LEGS) == 24
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cartesian_cone_payload(T3_T5_z) == cartesian_cone_payload(zC15)
    and cartesian_cone_payload(T5_T3_z) == cartesian_cone_payload(zC15)
    and cartesian_cone_payload(T3_T3_T5_z) == cartesian_cone_payload(zC45)
    and cartesian_cone_payload(T15_zF22) == cartesian_cone_payload(zC15F22)
    and cartesian_cone_payload(T45_zF22) == cartesian_cone_payload(zC45F22),
    "H1=%s cartesian_legs=%d"
    % ([p["h1_order"] for p in profiles], len(REQUIRED_CARTESIAN_LEGS)),
)

finite = live_source(
    cartesian_eta_lift_cone_actual=False,
    base_change_preserves_universal_cone=False,
    finite_path_checks=True,
    sampled_transport=True,
    declared_naturality_squares=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD2 finite checks and declared squares are not cartesianity",
    not accepts_cartesian_universal_cone(finite)
    and {
        "cartesian_eta_lift_cone_missing",
        "base_change_does_not_preserve_universal_cone",
        "finite_path_checks",
        "sampled_transport",
        "declared_naturality_squares",
    }
    <= set(reasons(finite)),
    ",".join(reasons(finite)),
)

chosen_transport = live_source(
    component_leg_cartesian_naturality=False,
    mediating_arrow_cartesian_naturality=False,
    chosen_transport_isomorphism=True,
    up_to_iso_without_coherence=True,
    noncartesian_pullback=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD3 chosen transport isomorphisms do not give pullbacks",
    not accepts_cartesian_universal_cone(chosen_transport)
    and {
        "component_leg_cartesian_naturality_missing",
        "mediating_arrow_cartesian_naturality_missing",
        "chosen_transport_isomorphism",
        "up_to_iso_without_coherence",
        "noncartesian_pullback",
    }
    <= set(reasons(chosen_transport)),
    ",".join(reasons(chosen_transport)),
)

split = live_source(
    cartesian_component_legs_actual=False,
    mediating_arrow_cartesian_naturality=False,
    split_componentwise_naturality=True,
    lax_naturality=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD4 split leg naturality without mediating-arrow naturality fails",
    not accepts_cartesian_universal_cone(split)
    and {
        "cartesian_component_legs_missing",
        "mediating_arrow_cartesian_naturality_missing",
        "split_componentwise_naturality",
        "lax_naturality",
    }
    <= set(reasons(split)),
    ",".join(reasons(split)),
)

graph_side = live_source(
    carrier_native=False,
    cartesian_source_lifts_actual=False,
    graph_side_base_change=True,
    pointwise_naturality=True,
    local_transport_table=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD5 graph-side base change and pointwise naturality are too late",
    not accepts_cartesian_universal_cone(graph_side)
    and {
        "not_carrier_native",
        "cartesian_source_lifts_missing",
        "graph_side_base_change",
        "pointwise_naturality",
        "local_transport_table",
    }
    <= set(reasons(graph_side)),
    ",".join(reasons(graph_side)),
)

retuned = live_source(
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    same_cartesian_cone_all_paths=False,
    retuned_transport=True,
    reindexed_cone_labels=True,
    base_changed_component_replacements=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD6 retuned transport or base-changed replacements change the cone",
    not accepts_cartesian_universal_cone(retuned)
    and {
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "same_cartesian_cone_not_all_paths",
        "retuned_transport",
        "reindexed_cone_labels",
        "base_changed_component_replacements",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_paths = live_source(
    same_cartesian_cone_all_paths=False,
    naturality_paths=REQUIRED_NATURALITY_PATHS - {"F22_product"},
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD7 cartesian multiplier-path naturality is mandatory",
    not accepts_cartesian_universal_cone(missing_paths)
    and {
        "same_cartesian_cone_not_all_paths",
        "required_multiplier_paths_missing",
    }
    <= set(reasons(missing_paths)),
    ",".join(reasons(missing_paths)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_CARTESIAN_EDGES - {edge})
    for edge in list(REQUIRED_CARTESIAN_EDGES)[:6]
] + [
    live_source(cartesian_leg_names=set(REQUIRED_CARTESIAN_LEGS[:-1])),
    live_source(cartesian_source_lifts_actual=False),
    live_source(cartesian_eta_lift_cone_actual=False),
    live_source(component_leg_cartesian_naturality=False),
    live_source(mediating_arrow_cartesian_naturality=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD8 every cartesian edge and leg is mandatory",
    not any(accepts_cartesian_universal_cone(data) for data in missing_edges)
    and {
        "required_cartesian_universal_cone_edges_missing",
        "required_cartesian_component_legs_missing",
        "cartesian_source_lifts_missing",
        "cartesian_eta_lift_cone_missing",
        "component_leg_cartesian_naturality_missing",
        "mediating_arrow_cartesian_naturality_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_cartesian = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_base_change=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD9 control/DH/Epstein cartesian cones fail",
    not accepts_cartesian_universal_cone(control_cartesian)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_base_change",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_cartesian)),
    ",".join(reasons(control_cartesian)),
)

live = live_source()
dead_sources = {
    "finite": finite,
    "chosen_transport": chosen_transport,
    "split": split,
    "graph_side": graph_side,
    "retuned": retuned,
    "missing_paths": missing_paths,
    "control_cartesian": control_cartesian,
}

gate(
    "CATCOHSRCPRESETACARTCONEQBARBECD10 only the cartesian eta-lift universal cone passes",
    accepts_cartesian_universal_cone(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_cartesian_universal_cone(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_cartesian_universal_cone(data) for data in dead_sources.values()),
        accepts_cartesian_universal_cone(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACARTCONEQBARBECD1-CATCOHSRCPRESETACARTCONEQBARBECD10 ALL PASS: "
    "eta-lift universal cone cartesianity over coherent source-presentation lifts pinned"
)
print(
    "VERDICT: the doc-484 eta-lift universal cone must be cartesian over the "
    "represented coherent source-presentation lifts. Finite path checks, chosen "
    "transport isomorphisms, pointwise naturality, graph-side base change, "
    "split componentwise naturality, retuned transport, base-changed component "
    "replacements, and control/DH/Epstein point-formability do not construct "
    "the missing object."
)
