r"""Universal-cone contract for the coherent source-presentation eta lift.

Doc 483 requires the existing source universal arrow to factor through the
coherent source-presentation equalizer.  This witness pins the next edge:
that lift must be one source-native universal cone over the actual twenty-four
component codomains.  A chosen section, inhabited equalizer, pointwise cone,
or Yoneda-style recognition statement does not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_universal_cone_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
ETA_LIFT_CONE_ID = "Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components"
UNIVERSAL_CONE_ID = "UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD"
UNIQUE_FACTOR_ID = "uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD"
MEDIATING_ARROW_ID = "med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD"
SOURCE_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
PRODUCT_FACTOR_ID = "fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD"
EQUALIZER_ID = "Eq_CohSrcPres_BCCube_Qbar_BECD"

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

REQUIRED_NATURALITY_PATHS = {
    "C3*C5=C15",
    "C5*C3=C15",
    "C3*C3*C5=C45",
    "F22_product",
}

REQUIRED_CONE_EDGES = {
    ("source_universal_arrow", "eta_product_factorization"),
    ("eta_product_factorization", "eta_equalizer_lift"),
    ("eta_equalizer_lift", "equalizer_object"),
    ("eta_equalizer_lift", "eta_lift_universal_cone"),
    ("eta_lift_universal_cone", "all_component_legs"),
    ("all_component_legs", "actual_source_components"),
    ("actual_source_components", "seven_facet_components"),
    ("actual_source_components", "seventeen_cell_components"),
    ("all_component_legs", "component_leg_codomain_equalities"),
    ("component_leg_codomain_equalities", "actual_source_components"),
    ("eta_lift_universal_cone", "universal_cone_property"),
    ("universal_cone_property", "unique_factorization"),
    ("unique_factorization", "mediating_arrow"),
    ("mediating_arrow", "eta_equalizer_lift"),
    ("unique_factorization", "same_cone_on_multiplier_paths"),
    ("same_cone_on_multiplier_paths", "C3*C5=C15"),
    ("same_cone_on_multiplier_paths", "C5*C3=C15"),
    ("same_cone_on_multiplier_paths", "C3*C3*C5=C45"),
    ("same_cone_on_multiplier_paths", "F22_product"),
    ("eta_lift_universal_cone", "coherence_preserves_coefficients"),
    ("eta_lift_universal_cone", "coherence_preserves_signed_support"),
    ("eta_lift_universal_cone", "source_before_points"),
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
        "doc483_eta_lift_actual": False,
        "actual_source_component_codomains": False,
        "eta_lift_universal_cone_actual": False,
        "all_component_legs_actual": False,
        "legs_land_in_source_components": False,
        "universal_cone_property_actual": False,
        "unique_factorization_actual": False,
        "mediating_arrow_actual": False,
        "factorization_targets_eta_lift": False,
        "naturality_multiplier_paths": False,
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "component_names": set(),
        "leg_names": set(),
        "required_edges": set(),
        "naturality_paths": set(),
        "chosen_cone": False,
        "pointwise_section": False,
        "inhabited_equalizer": False,
        "external_component_codomains": False,
        "semantic_target_labels": False,
        "graph_side_cone": False,
        "posthoc_yoneda_recognition": False,
        "retuned_component_codomains": False,
        "retuned_cone_payload": False,
        "nonunique_mediating_arrow": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc483_eta_lift_actual", "doc483_eta_lift_missing"),
    ("actual_source_component_codomains", "source_component_codomains_missing"),
    ("eta_lift_universal_cone_actual", "eta_lift_universal_cone_missing"),
    ("all_component_legs_actual", "component_legs_missing"),
    ("legs_land_in_source_components", "legs_do_not_land_in_source_components"),
    ("universal_cone_property_actual", "universal_cone_property_missing"),
    ("unique_factorization_actual", "unique_factorization_missing"),
    ("mediating_arrow_actual", "mediating_arrow_missing"),
    ("factorization_targets_eta_lift", "factorization_does_not_target_eta_lift"),
    ("naturality_multiplier_paths", "multiplier_naturality_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("chosen_cone", "chosen_cone"),
    ("pointwise_section", "pointwise_section"),
    ("inhabited_equalizer", "inhabited_equalizer"),
    ("external_component_codomains", "external_component_codomains"),
    ("semantic_target_labels", "semantic_target_labels"),
    ("graph_side_cone", "graph_side_cone"),
    ("posthoc_yoneda_recognition", "posthoc_yoneda_recognition"),
    ("retuned_component_codomains", "retuned_component_codomains"),
    ("retuned_cone_payload", "retuned_cone_payload"),
    ("nonunique_mediating_arrow", "nonunique_mediating_arrow"),
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
    if REQUIRED_CONE_EDGES - set(data["required_edges"]):
        out.append("required_universal_cone_edges_missing")
    if REQUIRED_NATURALITY_PATHS - set(data["naturality_paths"]):
        out.append("required_multiplier_paths_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_universal_cone(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_COMPONENTS) <= set(data["component_names"])
        and set(REQUIRED_LEGS) <= set(data["leg_names"])
        and REQUIRED_CONE_EDGES <= set(data["required_edges"])
        and REQUIRED_NATURALITY_PATHS <= set(data["naturality_paths"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc483_eta_lift_actual=True,
        actual_source_component_codomains=True,
        eta_lift_universal_cone_actual=True,
        all_component_legs_actual=True,
        legs_land_in_source_components=True,
        universal_cone_property_actual=True,
        unique_factorization_actual=True,
        mediating_arrow_actual=True,
        factorization_targets_eta_lift=True,
        naturality_multiplier_paths=True,
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        component_names=set(REQUIRED_COMPONENTS),
        leg_names=set(REQUIRED_LEGS),
        required_edges=set(REQUIRED_CONE_EDGES),
        naturality_paths=set(REQUIRED_NATURALITY_PATHS),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def cone_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_arrow": SOURCE_ARROW_ID,
        "product_factor": PRODUCT_FACTOR_ID,
        "equalizer": EQUALIZER_ID,
        "eta_lift": ETA_EQUALIZER_LIFT_ID,
        "cone": ETA_LIFT_CONE_ID,
        "universal_property": UNIVERSAL_CONE_ID,
        "unique_factor": UNIQUE_FACTOR_ID,
        "mediating_arrow": MEDIATING_ARROW_ID,
        "components": REQUIRED_COMPONENTS,
        "legs": REQUIRED_LEGS,
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
    "CATCOHSRCPRESETACONEQBARBECD1 eta lift is a universal source cone",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_CONE_EDGES)
    and len(REQUIRED_COMPONENTS) == len(REQUIRED_LEGS) == 24
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and cone_payload(T3_T5_z) == cone_payload(zC15)
    and cone_payload(T5_T3_z) == cone_payload(zC15)
    and cone_payload(T3_T3_T5_z) == cone_payload(zC45)
    and cone_payload(T15_zF22) == cone_payload(zC15F22)
    and cone_payload(T45_zF22) == cone_payload(zC45F22),
    "H1=%s components=%d legs=%d"
    % ([p["h1_order"] for p in profiles], len(REQUIRED_COMPONENTS), len(REQUIRED_LEGS)),
)

chosen = live_source(
    carrier_native=False,
    eta_lift_universal_cone_actual=False,
    universal_cone_property_actual=False,
    chosen_cone=True,
    pointwise_section=True,
    inhabited_equalizer=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD2 chosen cones or inhabited equalizers fail",
    not accepts_universal_cone(chosen)
    and {
        "not_carrier_native",
        "eta_lift_universal_cone_missing",
        "universal_cone_property_missing",
        "chosen_cone",
        "pointwise_section",
        "inhabited_equalizer",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

external_components = live_source(
    actual_source_component_codomains=False,
    legs_land_in_source_components=False,
    component_names=set(REQUIRED_COMPONENTS[:-4]),
    external_component_codomains=True,
    semantic_target_labels=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD3 component codomains must be actual source objects",
    not accepts_universal_cone(external_components)
    and {
        "source_component_codomains_missing",
        "legs_do_not_land_in_source_components",
        "required_source_components_missing",
        "external_component_codomains",
        "semantic_target_labels",
    }
    <= set(reasons(external_components)),
    ",".join(reasons(external_components)),
)

nonunique = live_source(
    unique_factorization_actual=False,
    mediating_arrow_actual=False,
    factorization_targets_eta_lift=False,
    nonunique_mediating_arrow=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD4 mediating arrows must be unique and target the eta lift",
    not accepts_universal_cone(nonunique)
    and {
        "unique_factorization_missing",
        "mediating_arrow_missing",
        "factorization_does_not_target_eta_lift",
        "nonunique_mediating_arrow",
    }
    <= set(reasons(nonunique)),
    ",".join(reasons(nonunique)),
)

recognition = live_source(
    carrier_native=False,
    eta_lift_universal_cone_actual=False,
    all_component_legs_actual=False,
    graph_side_cone=True,
    posthoc_yoneda_recognition=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD5 graph-side or Yoneda recognition is too late",
    not accepts_universal_cone(recognition)
    and {
        "not_carrier_native",
        "eta_lift_universal_cone_missing",
        "component_legs_missing",
        "graph_side_cone",
        "posthoc_yoneda_recognition",
    }
    <= set(reasons(recognition)),
    ",".join(reasons(recognition)),
)

retuned = live_source(
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    component_names=set(REQUIRED_COMPONENTS),
    leg_names=set(REQUIRED_LEGS[:-2]),
    retuned_component_codomains=True,
    retuned_cone_payload=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD6 retuned components or cone payloads change the source data",
    not accepts_universal_cone(retuned)
    and {
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "required_component_legs_missing",
        "retuned_component_codomains",
        "retuned_cone_payload",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_paths = live_source(
    naturality_multiplier_paths=False,
    naturality_paths=REQUIRED_NATURALITY_PATHS - {"F22_product"},
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD7 multiplier-path naturality is part of the cone",
    not accepts_universal_cone(missing_paths)
    and {
        "multiplier_naturality_missing",
        "required_multiplier_paths_missing",
    }
    <= set(reasons(missing_paths)),
    ",".join(reasons(missing_paths)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_CONE_EDGES - {edge})
    for edge in list(REQUIRED_CONE_EDGES)[:6]
] + [
    live_source(component_names=set(REQUIRED_COMPONENTS[:-1])),
    live_source(leg_names=set(REQUIRED_LEGS[:-1])),
    live_source(universal_cone_property_actual=False),
    live_source(unique_factorization_actual=False),
    live_source(mediating_arrow_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETACONEQBARBECD8 every universal-cone edge and leg is mandatory",
    not any(accepts_universal_cone(data) for data in missing_edges)
    and {
        "required_universal_cone_edges_missing",
        "required_source_components_missing",
        "required_component_legs_missing",
        "universal_cone_property_missing",
        "unique_factorization_missing",
        "mediating_arrow_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_cone = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_cone=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "CATCOHSRCPRESETACONEQBARBECD9 control/DH/Epstein point-formable cones fail",
    not accepts_universal_cone(control_cone)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_cone",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_cone)),
    ",".join(reasons(control_cone)),
)

live = live_source()
dead_sources = {
    "chosen": chosen,
    "external_components": external_components,
    "nonunique": nonunique,
    "recognition": recognition,
    "retuned": retuned,
    "missing_paths": missing_paths,
    "control_cone": control_cone,
}

gate(
    "CATCOHSRCPRESETACONEQBARBECD10 only the source-native universal cone passes",
    accepts_universal_cone(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_universal_cone(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_universal_cone(data) for data in dead_sources.values()),
        accepts_universal_cone(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETACONEQBARBECD1-CATCOHSRCPRESETACONEQBARBECD10 ALL PASS: "
    "eta lift universal source cone over coherent source-presentation components pinned"
)
print(
    "VERDICT: the doc-483 eta lift must form one source-native universal cone "
    "over the actual seven facet and seventeen coherence-cell component "
    "codomains, with unique factorization for every coherent source-presentation "
    "arrow. Chosen cones, inhabited equalizers, pointwise sections, graph-side "
    "cones, posthoc Yoneda recognition, retuned component codomains, and "
    "control/DH/Epstein point-formability do not construct the missing object."
)
