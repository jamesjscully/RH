r"""Represented source-fiber contract for the strict-square multiplier action.

Doc 341 requires a source-typed graph-formation fiber.  This witness pins the
next categorical edge: the source fiber must be represented by an actual
carrier-side object and universal arrow with cartesian multiplier lifts.  A
specification functor, predicate fibration, declared representer, or local
table of source labels is not the source fiber.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_represented_source_fiber_contract
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"
BOUNDARY_ID = "B_Qbar_BECD_DD4"
PUSHFORWARD_ID = "PF_Qbar_BECD_p1p2"
GRAPH_ID = "G_Qbar_BECD_prop"
ROSATI_ID = "R_Qbar_BECD_pos"
COUNT_ID = "CD_Qbar_BECD"
SOURCE_TOKEN_ID = "SRC_Qbar_BECD_strict_square"
FORMATION_FIBER_ID = "Fib_Qbar_BECD_graph_formation"
REPRESENTING_OBJECT_ID = "Rep_Qbar_BECD_source_fiber"
UNIVERSAL_ARROW_ID = "eta_Qbar_BECD_source"

REQUIRED_EDGES = {
    ("internal_effectivity_domain", "representing_object"),
    ("multiplier_action", "representing_object"),
    ("dd4_boundary", "representing_object"),
    ("endpoint_degree", "representing_object"),
    ("pushforward_square", "representing_object"),
    ("graph_rosati_count", "representing_object"),
    ("representing_object", "universal_arrow"),
    ("universal_arrow", "source_token"),
    ("source_token", "formation_fiber"),
    ("universal_arrow", "cartesian_lifts"),
    ("cartesian_lifts", "multiplier_transport"),
    ("cartesian_lifts", "control_death"),
    ("formation_fiber", "controls_not_points"),
    ("formation_fiber", "dh_not_points"),
    ("formation_fiber", "epstein_not_points"),
}

Corr = tuple[float, np.ndarray, float]


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


def support(chi: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted(chi))


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


def multiplier_degree(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items() if val > 0)


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph_corr(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(
        compose(graph_corr(F, q, m), graph_corr(F, q, n)),
        graph_corr(F, q, m + n),
    )


def anti_defect(A: Corr, B: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(compose(A, B), E), compose(dagger(B, E), dagger(A, E)))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def projection_sides(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> tuple[float, float]:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs, rhs = projection_sides(A, B, C, E)
    return abs(lhs - rhs)


def retune_first_degree_for_projection(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> Corr:
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    return corr(product[0] + (rhs - lhs) / C[2], product[1], product[2])


def trace_power(F: np.ndarray, n: int) -> float:
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - trace_power(F, n))


def formal_graph_signature(F: np.ndarray, E: np.ndarray, q: float) -> tuple[bool, bool, bool]:
    G = graph_corr(F, q, 1)
    H = graph_corr(F, q, 2)
    return (
        graph_law_defect(F, q, 1, 2) < 1e-12,
        qsim_defect(F, E, q) < 1e-12,
        anti_defect(G, H, E) < 1e-12,
    )


def source_row(name: str, chi: dict[int, int], transport: str, cart_degree: int) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "domain": DOMAIN_ID,
        "boundary": BOUNDARY_ID,
        "pushforward": PUSHFORWARD_ID,
        "graph": GRAPH_ID,
        "rosati": ROSATI_ID,
        "count_degree": COUNT_ID,
        "source_token": SOURCE_TOKEN_ID,
        "formation_fiber": FORMATION_FIBER_ID,
        "representing_object": REPRESENTING_OBJECT_ID,
        "universal_arrow": UNIVERSAL_ARROW_ID,
        "cartesian_lift": "cart_%s" % transport,
        "cartesian_degree": cart_degree,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "graph_degree": p1,
        "count_degree_value": p1 * p2,
        "endpoint_defect": p1 - p2,
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_source_fiber": False,
        "representing_object_actual": False,
        "universal_arrow_actual": False,
        "source_token_generated_by_universal_arrow": False,
        "formation_fiber_actual": False,
        "structural_maps_represented": False,
        "cartesian_lifts_actual": False,
        "cartesian_lifts_compose": False,
        "cartesian_lifts_preserve_coefficients": False,
        "fiber_before_graph_objects": False,
        "control_death_represented": False,
        "controls_not_points_of_representer": False,
        "dh_not_points_of_representer": False,
        "epstein_not_points_of_representer": False,
        "finite_anchors_generated": False,
        "same_representer_transports_all_rows": False,
        "required_edges": set(),
        "specification_functor_only": False,
        "functor_of_points_without_representer": False,
        "yoneda_reversal": False,
        "predicate_subfibration": False,
        "discrete_fibration_labels": False,
        "declared_representer": False,
        "formal_universal_property": False,
        "graph_object_classifier": False,
        "local_representers": False,
        "finite_representer_table": False,
        "external_choice_of_cartesian_lifts": False,
        "retuned_cartesian_lifts": False,
        "semantic_zeta_tag": False,
        "control_point_formable": True,
        "dh_point_formable": True,
        "epstein_point_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_source_fiber", "represented_source_fiber_missing"),
    ("representing_object_actual", "representing_object_not_actual"),
    ("universal_arrow_actual", "universal_arrow_not_actual"),
    (
        "source_token_generated_by_universal_arrow",
        "source_token_not_generated_by_universal_arrow",
    ),
    ("formation_fiber_actual", "formation_fiber_not_actual"),
    ("structural_maps_represented", "structural_maps_not_represented"),
    ("cartesian_lifts_actual", "cartesian_lifts_not_actual"),
    ("cartesian_lifts_compose", "cartesian_lifts_do_not_compose"),
    (
        "cartesian_lifts_preserve_coefficients",
        "cartesian_lifts_do_not_preserve_coefficients",
    ),
    ("fiber_before_graph_objects", "fiber_not_before_graph_objects"),
    ("control_death_represented", "control_death_not_represented"),
    ("controls_not_points_of_representer", "controls_are_points_of_representer"),
    ("dh_not_points_of_representer", "dh_is_point_of_representer"),
    ("epstein_not_points_of_representer", "epstein_is_point_of_representer"),
    ("finite_anchors_generated", "finite_anchors_not_generated"),
    (
        "same_representer_transports_all_rows",
        "same_representer_does_not_transport_all_rows",
    ),
)

BANNED = (
    ("specification_functor_only", "specification_functor_only"),
    (
        "functor_of_points_without_representer",
        "functor_of_points_without_representer",
    ),
    ("yoneda_reversal", "yoneda_reversal"),
    ("predicate_subfibration", "predicate_subfibration"),
    ("discrete_fibration_labels", "discrete_fibration_labels"),
    ("declared_representer", "declared_representer"),
    ("formal_universal_property", "formal_universal_property"),
    ("graph_object_classifier", "graph_object_classifier"),
    ("local_representers", "local_representers"),
    ("finite_representer_table", "finite_representer_table"),
    ("external_choice_of_cartesian_lifts", "external_choice_of_cartesian_lifts"),
    ("retuned_cartesian_lifts", "retuned_cartesian_lifts"),
    ("semantic_zeta_tag", "semantic_zeta_tag"),
    ("control_point_formable", "control_point_formable"),
    ("dh_point_formable", "dh_point_formable"),
    ("epstein_point_formable", "epstein_point_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_represented_source_fiber_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_represented_source_fiber(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_source_fiber=True,
        representing_object_actual=True,
        universal_arrow_actual=True,
        source_token_generated_by_universal_arrow=True,
        formation_fiber_actual=True,
        structural_maps_represented=True,
        cartesian_lifts_actual=True,
        cartesian_lifts_compose=True,
        cartesian_lifts_preserve_coefficients=True,
        fiber_before_graph_objects=True,
        control_death_represented=True,
        controls_not_points_of_representer=True,
        dh_not_points_of_representer=True,
        epstein_not_points_of_representer=True,
        finite_anchors_generated=True,
        same_representer_transports_all_rows=True,
        required_edges=set(REQUIRED_EDGES),
        control_point_formable=False,
        dh_point_formable=False,
        epstein_point_formable=False,
    )
    data.update(kwargs)
    return data


C3 = ((3,), (1,), ((0, 0),))
C9 = ((9,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

z = chi_col(*ZERO_SPLIT)
chi_C3 = chi_col(*C3)
chi_C9 = chi_col(*C9)
chi_F22 = chi_col(*F22)
chi_C3F22 = convolve_chi(chi_C3, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T3_T3_z = convolve_chi(T3_z, chi_C3)
T9_z = convolve_chi(z, chi_C9)
zF22 = convolve_chi(z, chi_F22)
T3_zF22 = convolve_chi(zF22, chi_C3)
T3_z_then_F22 = convolve_chi(T3_z, chi_F22)
z_C3F22 = convolve_chi(z, chi_C3F22)

rows = [
    source_row("z", z, "id", 1),
    source_row("T3_z", T3_z, "C3", 3),
    source_row("T3_T3_z", T3_T3_z, "C3_then_C3", 9),
    source_row("T9_z", T9_z, "C9", 9),
    source_row("zF22", zF22, "F22", 4),
    source_row("T3_zF22", T3_zF22, "C3_after_F22", 12),
    source_row("T3_z_then_F22", T3_z_then_F22, "F22_after_C3", 12),
    source_row("z_C3F22", z_C3F22, "C3F22", 12),
]

base_graph_degree = rows[0]["graph_degree"]
base_count_degree = rows[0]["count_degree_value"]
c3_degree = multiplier_degree(chi_C3)
c9_degree = multiplier_degree(chi_C9)
f22_degree = multiplier_degree(chi_F22)
c3f22_degree = multiplier_degree(chi_C3F22)

q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta(F_true)
G_true = graph_corr(F_true, q_true, 1)
H_true = graph_corr(F_true, q_true, 2)
true_signature = formal_graph_signature(F_true, E_true, q_true)
true_hodge = primitive_hodge_index(F_true, E_true, 1)
true_count_defects = [
    abs(ns_intersection(D_true, graph_corr(F_true, q_true, n)) - point_count(F_true, q_true, n))
    for n in (1, 2, 3)
]
true_anti = anti_defect(G_true, H_true, E_true)

control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_D = delta(control)
control_G = graph_corr(control, control_q, 1)
control_H = graph_corr(control, control_q, 2)
control_signature = formal_graph_signature(control, control_E, control_q)
control_hodge = primitive_hodge_index(control, control_E, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(
    control_G, control_D, control_G, control_E
)


gate(
    "RSF1 specification functors see controls unless a representer excludes them",
    true_signature == (True, True, True)
    and control_signature == true_signature
    and true_hodge < 0
    and control_hodge > 0
    and control_projection == 24.0
    and control_retuned[0] == 27.0,
    "true_sig=%s control_sig=%s true_H=%.3f control_H=%.3f proj=%.1f retuned_d1=%.1f"
    % (
        true_signature,
        control_signature,
        true_hodge,
        control_hodge,
        control_projection,
        control_retuned[0],
    ),
)


gate(
    "RSF2 one representer carries cartesian multiplier lifts",
    max(true_count_defects) < 1e-12
    and true_anti < 1e-12
    and {row["representing_object"] for row in rows} == {REPRESENTING_OBJECT_ID}
    and {row["universal_arrow"] for row in rows} == {UNIVERSAL_ARROW_ID}
    and {row["source_token"] for row in rows} == {SOURCE_TOKEN_ID}
    and {row["formation_fiber"] for row in rows} == {FORMATION_FIBER_ID}
    and all(row["endpoint_defect"] == 0 for row in rows)
    and rows[1]["graph_degree"] == base_graph_degree * c3_degree
    and rows[2]["graph_degree"] == rows[3]["graph_degree"]
    and rows[2]["cartesian_degree"] == c3_degree * c3_degree == c9_degree
    and rows[4]["graph_degree"] == base_graph_degree * f22_degree
    and rows[5]["graph_degree"] == rows[6]["graph_degree"] == rows[7]["graph_degree"]
    and rows[5]["cartesian_degree"] == c3_degree * f22_degree == c3f22_degree
    and rows[1]["count_degree_value"] == base_count_degree * c3_degree**2
    and rows[3]["count_degree_value"] == base_count_degree * c9_degree**2
    and rows[4]["count_degree_value"] == base_count_degree * f22_degree**2
    and rows[5]["count_degree_value"] == base_count_degree * c3f22_degree**2,
    "count=%.1e anti=%.1e rows=%s" % (max(true_count_defects), true_anti, rows),
)


spec_functor = live_source(
    represented_source_fiber=False,
    representing_object_actual=False,
    universal_arrow_actual=False,
    source_token_generated_by_universal_arrow=False,
    specification_functor_only=True,
    functor_of_points_without_representer=True,
    yoneda_reversal=True,
    control_point_formable=True,
)

gate(
    "RSF3 specification functors and Yoneda reversal are not representers",
    not accepts_represented_source_fiber(spec_functor)
    and {
        "represented_source_fiber_missing",
        "representing_object_not_actual",
        "universal_arrow_not_actual",
        "source_token_not_generated_by_universal_arrow",
        "specification_functor_only",
        "functor_of_points_without_representer",
        "yoneda_reversal",
        "control_point_formable",
    }
    <= set(reasons(spec_functor)),
    ",".join(reasons(spec_functor)),
)


predicate_fibration = live_source(
    represented_source_fiber=False,
    formation_fiber_actual=False,
    fiber_before_graph_objects=False,
    predicate_subfibration=True,
    discrete_fibration_labels=True,
    graph_object_classifier=True,
    control_point_formable=True,
)

gate(
    "RSF4 predicate subfibrations are graph-object classifiers",
    not accepts_represented_source_fiber(predicate_fibration)
    and {
        "represented_source_fiber_missing",
        "formation_fiber_not_actual",
        "fiber_not_before_graph_objects",
        "predicate_subfibration",
        "discrete_fibration_labels",
        "graph_object_classifier",
        "control_point_formable",
    }
    <= set(reasons(predicate_fibration)),
    ",".join(reasons(predicate_fibration)),
)


declared_representer = live_source(
    representing_object_actual=False,
    universal_arrow_actual=False,
    structural_maps_represented=False,
    declared_representer=True,
    formal_universal_property=True,
    semantic_zeta_tag=True,
)

gate(
    "RSF5 declared representers and formal universal properties are labels",
    not accepts_represented_source_fiber(declared_representer)
    and {
        "representing_object_not_actual",
        "universal_arrow_not_actual",
        "structural_maps_not_represented",
        "declared_representer",
        "formal_universal_property",
        "semantic_zeta_tag",
    }
    <= set(reasons(declared_representer)),
    ",".join(reasons(declared_representer)),
)


local_lifts = live_source(
    same_representer_transports_all_rows=False,
    cartesian_lifts_actual=False,
    cartesian_lifts_compose=False,
    local_representers=True,
    finite_representer_table=True,
    external_choice_of_cartesian_lifts=True,
    retuned_cartesian_lifts=True,
)

gate(
    "RSF6 local representers and chosen lifts do not compose",
    not accepts_represented_source_fiber(local_lifts)
    and {
        "same_representer_does_not_transport_all_rows",
        "cartesian_lifts_not_actual",
        "cartesian_lifts_do_not_compose",
        "local_representers",
        "finite_representer_table",
        "external_choice_of_cartesian_lifts",
        "retuned_cartesian_lifts",
    }
    <= set(reasons(local_lifts)),
    ",".join(reasons(local_lifts)),
)


control_points = live_source(
    carrier_native=False,
    controls_not_points_of_representer=False,
    dh_not_points_of_representer=False,
    epstein_not_points_of_representer=False,
    specification_functor_only=True,
    control_point_formable=True,
    dh_point_formable=True,
    epstein_point_formable=True,
)

gate(
    "RSF7 control/DH/Epstein points mean the source fiber is not represented",
    not accepts_represented_source_fiber(control_points)
    and {
        "not_carrier_native",
        "controls_are_points_of_representer",
        "dh_is_point_of_representer",
        "epstein_is_point_of_representer",
        "specification_functor_only",
        "control_point_formable",
        "dh_point_formable",
        "epstein_point_formable",
    }
    <= set(reasons(control_points)),
    ",".join(reasons(control_points)),
)


missing_sources = [
    live_source(structural_maps_represented=False),
    live_source(source_token_generated_by_universal_arrow=False),
    live_source(cartesian_lifts_preserve_coefficients=False),
    live_source(control_death_represented=False),
    live_source(finite_anchors_generated=False),
]
missing_reasons = set().union(*(set(reasons(data)) for data in missing_sources))

gate(
    "RSF8 represented source fiber needs every upstream represented source",
    not any(accepts_represented_source_fiber(data) for data in missing_sources)
    and {
        "structural_maps_not_represented",
        "source_token_not_generated_by_universal_arrow",
        "cartesian_lifts_do_not_preserve_coefficients",
        "control_death_not_represented",
        "finite_anchors_not_generated",
    }
    <= missing_reasons,
    "missing=%s" % sorted(missing_reasons),
)


static_representer = live_source(
    required_edges=REQUIRED_EDGES
    - {
        ("representing_object", "universal_arrow"),
        ("universal_arrow", "source_token"),
        ("universal_arrow", "cartesian_lifts"),
    },
    universal_arrow_actual=False,
    cartesian_lifts_actual=False,
    cartesian_lifts_compose=False,
)

gate(
    "RSF9 representer names without universal-arrow edges are rejected",
    not accepts_represented_source_fiber(static_representer)
    and {
        "universal_arrow_not_actual",
        "cartesian_lifts_not_actual",
        "cartesian_lifts_do_not_compose",
        "required_represented_source_fiber_edges_missing",
    }
    <= set(reasons(static_representer)),
    ",".join(reasons(static_representer)),
)


live = live_source()
dead_sources = {
    "spec_functor": spec_functor,
    "predicate_fibration": predicate_fibration,
    "declared_representer": declared_representer,
    "local_lifts": local_lifts,
    "control_points": control_points,
    "static_representer": static_representer,
}

gate(
    "RSF10 only represented source fiber with universal arrow passes",
    accepts_represented_source_fiber(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_represented_source_fiber(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_represented_source_fiber(data) for data in dead_sources.values()),
        accepts_represented_source_fiber(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nRSF1-RSF10 ALL PASS: represented source-fiber contract pinned")
print(
    "VERDICT: the source-typed graph-formation fiber must be represented by "
    "an actual carrier-side object and universal arrow with cartesian "
    "multiplier lifts. Specification functors, Yoneda reversal, predicate "
    "subfibrations, declared representers, local tables, chosen/retuned "
    "cartesian lifts, and control/DH/Epstein points do not construct it."
)
