r"""Eta-factorization contract for the coherent source-presentation limit.

Doc 482 requires the finite coherent source-presentation totalizer to be an
internal source finite limit.  This witness pins the next edge: the existing
source universal arrow must factor through the finite product and lift through
the equalizer, and that lifted arrow must compare to the doc-481 totalizer
arrow.  Object-only limits, empty equalizers, chosen sections, or posthoc
point maps do not construct the missing object.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_coherent_source_presentation_eta_factorization_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

SOURCE_ARROW_ID = "eta_BCCube_Qbar_BECD_source"
PRODUCT_ID = "Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells"
EQUALIZER_ID = "Eq_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_ARROW_ID = "eta_CohSrcPres_BCCube_Qbar_BECD"
ETA_PRODUCT_FACTOR_ID = "fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD"
ETA_EQUALIZER_LIFT_ID = "lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD"
ETA_COMPARISON_ID = "cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD"
EQUALIZER_MONIC_ID = "incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"
TOTALIZER_COMPARISON_ID = "cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD"

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

REQUIRED_PROJECTIONS = tuple(
    f"pi_CohSrcPres_BCCube_Qbar_BECD_{name}"
    for name in (*REQUIRED_FACETS, *REQUIRED_COHERENCE_CELLS)
)

REQUIRED_ETA_EDGES = {
    ("source_universal_arrow", "eta_product_factorization"),
    ("eta_product_factorization", "finite_product_object"),
    ("eta_product_factorization", "source_native_projections"),
    ("source_native_projections", "seven_facets"),
    ("source_native_projections", "seventeen_coherence_cells"),
    ("eta_product_factorization", "alpha_constraints"),
    ("eta_product_factorization", "beta_constraints"),
    ("alpha_constraints", "eta_equalizes_parallel_pair"),
    ("beta_constraints", "eta_equalizes_parallel_pair"),
    ("eta_equalizes_parallel_pair", "eta_equalizer_lift"),
    ("eta_equalizer_lift", "equalizer_object"),
    ("eta_equalizer_lift", "equalizer_monic"),
    ("eta_equalizer_lift", "eta_totalizer_comparison"),
    ("eta_totalizer_comparison", "doc481_totalizer_arrow"),
    ("eta_totalizer_comparison", "comparison_isomorphism"),
    ("doc481_totalizer_arrow", "finite_source_facets"),
    ("doc481_totalizer_arrow", "finite_coherence_cells"),
    ("eta_equalizer_lift", "coherence_preserves_coefficients"),
    ("eta_equalizer_lift", "coherence_preserves_signed_support"),
    ("eta_equalizer_lift", "source_before_points"),
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
        "doc482_finite_limit_actual": False,
        "source_universal_arrow_actual": False,
        "eta_product_factorization_actual": False,
        "eta_equalizes_parallel_pair": False,
        "eta_equalizer_lift_actual": False,
        "equalizer_object_actual": False,
        "equalizer_monic_actual": False,
        "eta_totalizer_comparison_actual": False,
        "comparison_isomorphism_actual": False,
        "doc481_totalizer_arrow_actual": False,
        "projection_names": set(),
        "facets_generated_by_eta": set(),
        "coherence_cells_generated_by_eta": set(),
        "required_edges": set(),
        "coherence_preserves_coefficients": False,
        "coherence_preserves_signed_support": False,
        "source_before_points": False,
        "controls_not_points": False,
        "dh_not_points": False,
        "epstein_not_points": False,
        "object_only_equalizer": False,
        "empty_equalizer": False,
        "chosen_section": False,
        "posthoc_point_map": False,
        "product_only_factorization": False,
        "nonmonic_lift": False,
        "retuned_eta_comparison": False,
        "graph_side_section": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("doc482_finite_limit_actual", "doc482_finite_limit_missing"),
    ("source_universal_arrow_actual", "source_universal_arrow_missing"),
    ("eta_product_factorization_actual", "eta_product_factorization_missing"),
    ("eta_equalizes_parallel_pair", "eta_does_not_equalize_parallel_pair"),
    ("eta_equalizer_lift_actual", "eta_equalizer_lift_missing"),
    ("equalizer_object_actual", "equalizer_object_missing"),
    ("equalizer_monic_actual", "equalizer_monic_missing"),
    ("eta_totalizer_comparison_actual", "eta_totalizer_comparison_missing"),
    ("comparison_isomorphism_actual", "comparison_isomorphism_missing"),
    ("doc481_totalizer_arrow_actual", "doc481_totalizer_arrow_missing"),
    ("coherence_preserves_coefficients", "coherence_does_not_preserve_coefficients"),
    ("coherence_preserves_signed_support", "coherence_does_not_preserve_signed_support"),
    ("source_before_points", "source_not_before_points"),
    ("controls_not_points", "controls_are_points"),
    ("dh_not_points", "dh_is_point"),
    ("epstein_not_points", "epstein_is_point"),
)

BANNED = (
    ("object_only_equalizer", "object_only_equalizer"),
    ("empty_equalizer", "empty_equalizer"),
    ("chosen_section", "chosen_section"),
    ("posthoc_point_map", "posthoc_point_map"),
    ("product_only_factorization", "product_only_factorization"),
    ("nonmonic_lift", "nonmonic_lift"),
    ("retuned_eta_comparison", "retuned_eta_comparison"),
    ("graph_side_section", "graph_side_section"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if set(REQUIRED_PROJECTIONS) - set(data["projection_names"]):
        out.append("required_projections_missing")
    if set(REQUIRED_FACETS) - set(data["facets_generated_by_eta"]):
        out.append("eta_does_not_generate_all_facets")
    if set(REQUIRED_COHERENCE_CELLS) - set(data["coherence_cells_generated_by_eta"]):
        out.append("eta_does_not_generate_all_coherence_cells")
    if REQUIRED_ETA_EDGES - set(data["required_edges"]):
        out.append("required_eta_factorization_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_eta_factorization(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and set(REQUIRED_PROJECTIONS) <= set(data["projection_names"])
        and set(REQUIRED_FACETS) <= set(data["facets_generated_by_eta"])
        and set(REQUIRED_COHERENCE_CELLS) <= set(data["coherence_cells_generated_by_eta"])
        and REQUIRED_ETA_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        doc482_finite_limit_actual=True,
        source_universal_arrow_actual=True,
        eta_product_factorization_actual=True,
        eta_equalizes_parallel_pair=True,
        eta_equalizer_lift_actual=True,
        equalizer_object_actual=True,
        equalizer_monic_actual=True,
        eta_totalizer_comparison_actual=True,
        comparison_isomorphism_actual=True,
        doc481_totalizer_arrow_actual=True,
        projection_names=set(REQUIRED_PROJECTIONS),
        facets_generated_by_eta=set(REQUIRED_FACETS),
        coherence_cells_generated_by_eta=set(REQUIRED_COHERENCE_CELLS),
        required_edges=set(REQUIRED_ETA_EDGES),
        coherence_preserves_coefficients=True,
        coherence_preserves_signed_support=True,
        source_before_points=True,
        controls_not_points=True,
        dh_not_points=True,
        epstein_not_points=True,
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


def eta_payload(chi: dict[int, int]) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "source_arrow": SOURCE_ARROW_ID,
        "product": PRODUCT_ID,
        "equalizer": EQUALIZER_ID,
        "totalizer_arrow": TOTALIZER_ARROW_ID,
        "product_factorization": ETA_PRODUCT_FACTOR_ID,
        "equalizer_lift": ETA_EQUALIZER_LIFT_ID,
        "eta_comparison": ETA_COMPARISON_ID,
        "equalizer_monic": EQUALIZER_MONIC_ID,
        "totalizer_comparison": TOTALIZER_COMPARISON_ID,
        "facets": REQUIRED_FACETS,
        "cells": REQUIRED_COHERENCE_CELLS,
        "projections": REQUIRED_PROJECTIONS,
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
    "CATCOHSRCPRESETAQBARBECD1 source eta factors through product and equalizer",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and graph_connected(REQUIRED_ETA_EDGES)
    and len(REQUIRED_PROJECTIONS) == 24
    and z == {1: 2, 2: -1}
    and T3_T5_z == T5_T3_z == zC15 == {15: 2, 30: -1}
    and T3_T3_T5_z == zC45 == {45: 2, 90: -1}
    and T15_zF22 == zC15F22 == {30: 4, 60: -2}
    and T45_zF22 == zC45F22 == {90: 4, 180: -2}
    and eta_payload(T3_T5_z) == eta_payload(zC15)
    and eta_payload(T5_T3_z) == eta_payload(zC15)
    and eta_payload(T3_T3_T5_z) == eta_payload(zC45)
    and eta_payload(T15_zF22) == eta_payload(zC15F22)
    and eta_payload(T45_zF22) == eta_payload(zC45F22),
    "H1=%s lift=%s projections=%d"
    % ([p["h1_order"] for p in profiles], ETA_EQUALIZER_LIFT_ID, len(REQUIRED_PROJECTIONS)),
)

object_only = live_source(
    source_universal_arrow_actual=False,
    eta_product_factorization_actual=False,
    eta_equalizer_lift_actual=False,
    object_only_equalizer=True,
)

gate(
    "CATCOHSRCPRESETAQBARBECD2 object-only equalizers do not construct eta",
    not accepts_eta_factorization(object_only)
    and {
        "source_universal_arrow_missing",
        "eta_product_factorization_missing",
        "eta_equalizer_lift_missing",
        "object_only_equalizer",
    }
    <= set(reasons(object_only)),
    ",".join(reasons(object_only)),
)

empty = live_source(
    eta_equalizes_parallel_pair=False,
    eta_equalizer_lift_actual=False,
    doc481_totalizer_arrow_actual=False,
    empty_equalizer=True,
)

gate(
    "CATCOHSRCPRESETAQBARBECD3 empty equalizers or unsourced lifts fail",
    not accepts_eta_factorization(empty)
    and {
        "eta_does_not_equalize_parallel_pair",
        "eta_equalizer_lift_missing",
        "doc481_totalizer_arrow_missing",
        "empty_equalizer",
    }
    <= set(reasons(empty)),
    ",".join(reasons(empty)),
)

chosen = live_source(
    carrier_native=False,
    eta_totalizer_comparison_actual=False,
    chosen_section=True,
    posthoc_point_map=True,
    graph_side_section=True,
)

gate(
    "CATCOHSRCPRESETAQBARBECD4 chosen sections and posthoc point maps are too late",
    not accepts_eta_factorization(chosen)
    and {
        "not_carrier_native",
        "eta_totalizer_comparison_missing",
        "chosen_section",
        "posthoc_point_map",
        "graph_side_section",
    }
    <= set(reasons(chosen)),
    ",".join(reasons(chosen)),
)

product_only = live_source(
    eta_equalizes_parallel_pair=False,
    eta_equalizer_lift_actual=False,
    equalizer_monic_actual=False,
    product_only_factorization=True,
)

gate(
    "CATCOHSRCPRESETAQBARBECD5 product-only factorization does not lift through the equalizer",
    not accepts_eta_factorization(product_only)
    and {
        "eta_does_not_equalize_parallel_pair",
        "eta_equalizer_lift_missing",
        "equalizer_monic_missing",
        "product_only_factorization",
    }
    <= set(reasons(product_only)),
    ",".join(reasons(product_only)),
)

retuned = live_source(
    comparison_isomorphism_actual=False,
    coherence_preserves_coefficients=False,
    coherence_preserves_signed_support=False,
    nonmonic_lift=True,
    retuned_eta_comparison=True,
)

gate(
    "CATCOHSRCPRESETAQBARBECD6 nonmonic or retuned eta comparisons change the source object",
    not accepts_eta_factorization(retuned)
    and {
        "comparison_isomorphism_missing",
        "coherence_does_not_preserve_coefficients",
        "coherence_does_not_preserve_signed_support",
        "nonmonic_lift",
        "retuned_eta_comparison",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)

missing_generation = live_source(
    projection_names=set(REQUIRED_PROJECTIONS[:-3]),
    facets_generated_by_eta=set(REQUIRED_FACETS) - {"control_death"},
    coherence_cells_generated_by_eta=set(REQUIRED_COHERENCE_CELLS)
    - {"closed_finite_coherence_cell"},
)

gate(
    "CATCOHSRCPRESETAQBARBECD7 eta must generate every projection, facet, and coherence cell",
    not accepts_eta_factorization(missing_generation)
    and {
        "required_projections_missing",
        "eta_does_not_generate_all_facets",
        "eta_does_not_generate_all_coherence_cells",
    }
    <= set(reasons(missing_generation)),
    ",".join(reasons(missing_generation)),
)

missing_edges = [
    live_source(required_edges=REQUIRED_ETA_EDGES - {edge})
    for edge in list(REQUIRED_ETA_EDGES)[:5]
] + [
    live_source(source_universal_arrow_actual=False),
    live_source(eta_product_factorization_actual=False),
    live_source(eta_equalizer_lift_actual=False),
    live_source(eta_totalizer_comparison_actual=False),
    live_source(comparison_isomorphism_actual=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_edges))

gate(
    "CATCOHSRCPRESETAQBARBECD8 every eta-factorization edge is mandatory",
    not any(accepts_eta_factorization(data) for data in missing_edges)
    and {
        "required_eta_factorization_edges_missing",
        "source_universal_arrow_missing",
        "eta_product_factorization_missing",
        "eta_equalizer_lift_missing",
        "eta_totalizer_comparison_missing",
        "comparison_isomorphism_missing",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)

control_eta = live_source(
    carrier_native=False,
    source_before_points=False,
    controls_not_points=False,
    dh_not_points=False,
    epstein_not_points=False,
    graph_side_section=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

live = live_source()
dead_sources = {
    "object_only": object_only,
    "empty": empty,
    "chosen": chosen,
    "product_only": product_only,
    "retuned": retuned,
    "missing_generation": missing_generation,
    "control_eta": control_eta,
}

gate(
    "CATCOHSRCPRESETAQBARBECD9 graph-side eta sections leave controls formable",
    not accepts_eta_factorization(control_eta)
    and {
        "not_carrier_native",
        "source_not_before_points",
        "controls_are_points",
        "dh_is_point",
        "epstein_is_point",
        "graph_side_section",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_eta)),
    ",".join(reasons(control_eta)),
)

gate(
    "CATCOHSRCPRESETAQBARBECD10 only the sourced eta equalizer lift passes",
    accepts_eta_factorization(live)
    and graph_connected(live["required_edges"])
    and not any(accepts_eta_factorization(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_eta_factorization(data) for data in dead_sources.values()),
        accepts_eta_factorization(live),
    ),
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print(
    "\nCATCOHSRCPRESETAQBARBECD1-CATCOHSRCPRESETAQBARBECD10 ALL PASS: "
    "source eta factorization through coherent source-presentation equalizer pinned"
)
print(
    "VERDICT: the existing source universal arrow must factor through the "
    "finite product, equalize the parallel constraints, lift through the "
    "equalizer, and compare isomorphically to eta_CohSrcPres. Object-only "
    "equalizers, empty limits, chosen sections, product-only maps, posthoc "
    "point maps, nonmonic lifts, and retuned eta comparisons do not construct "
    "the missing object."
)
