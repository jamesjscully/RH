r"""Formation-level control-death contract for Qbar_BECD.

Doc 320 ties restricted dQ localization to the endpoint pushforwards. This
witness sharpens the remaining control condition: controls must die at carrier
formation. It is not enough to let a control instantiate the square-shaped
package and then fail a later Rosati sign, projection defect, DD.4 boundary,
or finite sample.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_control_formation_death_contract
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []

Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph(F: np.ndarray, q: float, n: int) -> Corr:
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
    return corr_defect(compose(graph(F, q, m), graph(F, q, n)), graph(F, q, m + n))


def dagger_twice_defect(A: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(dagger(A, E), E), A)


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


OBJECT_ENDPOINT_BOUNDARY_COMPAT = {
    "carrier_object",
    "endpoint_maps",
    "dd4_boundary_killing",
    "boundary_endpoint_pushforward_compat",
}
CONTROL_DEATH = {"control_death_at_formation"}


def represented_slots(evidence: set[str]) -> set[str]:
    slots = set(evidence & OBJECT_ENDPOINT_BOUNDARY_COMPAT)
    if CONTROL_DEATH <= evidence:
        slots.add("control_death")
    return slots


def source(**kwargs):
    data = {
        "carrier_native": False,
        "zeta_formation_rule": False,
        "endpoint_integrality_native": False,
        "degree_maps_native": False,
        "dd4_boundary_native": False,
        "boundary_pushforward_compat_native": False,
        "proper_graph_composition_native": False,
        "positive_rosati_native": False,
        "all_atoms_joint_at_formation": False,
        "control_instantiation_impossible_at_formation": False,
        "control_not_built_before_filter": False,
        "finite_field_count_anchor_native": False,
        "graph_degree_anchor_native": False,
        "posthoc_control_filter": False,
        "semantic_zeta_tag": False,
        "finite_sample_filter": False,
        "projection_defect_filter": False,
        "rosati_sign_filter": False,
        "dd4_afterthought_filter": False,
        "external_euler_satake_label": False,
        "declared_control_death": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("zeta_formation_rule", "no_zeta_formation_rule"),
    ("endpoint_integrality_native", "endpoint_integrality_not_native"),
    ("degree_maps_native", "degree_maps_not_native"),
    ("dd4_boundary_native", "dd4_boundary_not_native"),
    ("boundary_pushforward_compat_native", "boundary_pushforward_compat_not_native"),
    ("proper_graph_composition_native", "proper_graph_composition_not_native"),
    ("positive_rosati_native", "positive_rosati_not_native"),
    ("all_atoms_joint_at_formation", "atoms_not_joint_at_formation"),
    (
        "control_instantiation_impossible_at_formation",
        "control_instantiation_not_impossible_at_formation",
    ),
    ("control_not_built_before_filter", "control_built_before_filter"),
    ("finite_field_count_anchor_native", "finite_field_count_anchor_not_native"),
    ("graph_degree_anchor_native", "graph_degree_anchor_not_native"),
)


BANNED = (
    ("posthoc_control_filter", "posthoc_control_filter"),
    ("semantic_zeta_tag", "semantic_zeta_tag"),
    ("finite_sample_filter", "finite_sample_filter"),
    ("projection_defect_filter", "projection_defect_filter"),
    ("rosati_sign_filter", "rosati_sign_filter"),
    ("dd4_afterthought_filter", "dd4_afterthought_filter"),
    ("external_euler_satake_label", "external_euler_satake_label"),
    ("declared_control_death", "declared_control_death"),
    ("control_formable", "control_formable"),
)


def accepts_control_death(data) -> bool:
    return all(data[key] for key, _ in REQUIRED) and not any(
        data[key] for key, _ in BANNED
    )


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    out.extend(label for key, label in BANNED if data[key])
    return out


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        zeta_formation_rule=True,
        endpoint_integrality_native=True,
        degree_maps_native=True,
        dd4_boundary_native=True,
        boundary_pushforward_compat_native=True,
        proper_graph_composition_native=True,
        positive_rosati_native=True,
        all_atoms_joint_at_formation=True,
        control_instantiation_impossible_at_formation=True,
        control_not_built_before_filter=True,
        finite_field_count_anchor_native=True,
        graph_degree_anchor_native=True,
        control_formable=False,
    )
    data.update(kwargs)
    return data


control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_G = graph(control, control_q, 1)
control_H = graph(control, control_q, 2)

control_formal_graph = graph_law_defect(control, control_q, 1, 2)
control_qsim = qsim_defect(control, control_E, control_q)
control_involution = dagger_twice_defect(control_G, control_E)
control_anti = anti_defect(control_G, control_H, control_E)
control_hodge = primitive_hodge_index(control, control_E, 1)

gate(
    "CFD1 controls can instantiate formal graph/adjoint data before any filter",
    control_formal_graph < 1e-12
    and control_qsim < 1e-12
    and control_involution < 1e-12
    and control_anti < 1e-12
    and control_hodge > 0,
    "graph=%.1e qsim=%.1e anti=%.1e primitive_H=%.3f"
    % (control_formal_graph, control_qsim, control_anti, control_hodge),
)


control_D = delta(control)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(control_G, control_D, control_G, control_E)
control_retuned_projection = abs(
    ns_intersection(control_retuned, control_G)
    - projection_sides(control_G, control_D, control_G, control_E)[1]
)

gate(
    "CFD2 projection defects and retunings are downstream filters",
    control_projection == 24.0
    and control_retuned_projection < 1e-12
    and corr_defect(control_retuned, control_G) == 24.0,
    "projection_defect=%.1f retuned_d1=%.1f"
    % (control_projection, control_retuned[0]),
)


prior = set(OBJECT_ENDPOINT_BOUNDARY_COMPAT)
with_control_death = prior | CONTROL_DEATH

gate(
    "CFD3 doc-320 package still needs formation-level control death",
    represented_slots(prior) == OBJECT_ENDPOINT_BOUNDARY_COMPAT
    and represented_slots(with_control_death)
    == OBJECT_ENDPOINT_BOUNDARY_COMPAT | {"control_death"},
    "before=%s after=%s"
    % (
        ",".join(sorted(represented_slots(prior))),
        ",".join(sorted(represented_slots(with_control_death))),
    ),
)


posthoc_filters = [
    live_source(
        control_instantiation_impossible_at_formation=False,
        control_not_built_before_filter=False,
        rosati_sign_filter=True,
        control_formable=True,
    ),
    live_source(
        control_instantiation_impossible_at_formation=False,
        control_not_built_before_filter=False,
        projection_defect_filter=True,
        control_formable=True,
    ),
    live_source(
        control_instantiation_impossible_at_formation=False,
        control_not_built_before_filter=False,
        dd4_afterthought_filter=True,
        control_formable=True,
    ),
]

gate(
    "CFD4 Rosati/projection/DD.4 after-filters are not formation death",
    not any(accepts_control_death(data) for data in posthoc_filters)
    and {
        "control_instantiation_not_impossible_at_formation",
        "control_built_before_filter",
        "rosati_sign_filter",
        "projection_defect_filter",
        "dd4_afterthought_filter",
        "control_formable",
    }
    <= set().union(*(set(reasons(data)) for data in posthoc_filters)),
    "reasons=%s"
    % sorted(set().union(*(set(reasons(data)) for data in posthoc_filters))),
)


semantic_label = live_source(
    zeta_formation_rule=False,
    control_instantiation_impossible_at_formation=False,
    control_not_built_before_filter=False,
    semantic_zeta_tag=True,
    external_euler_satake_label=True,
    control_formable=True,
)

gate(
    "CFD5 semantic zeta/Euler/Satake labels do not kill controls",
    not accepts_control_death(semantic_label)
    and {
        "no_zeta_formation_rule",
        "control_instantiation_not_impossible_at_formation",
        "control_built_before_filter",
        "semantic_zeta_tag",
        "external_euler_satake_label",
        "control_formable",
    }
    <= set(reasons(semantic_label)),
    ",".join(reasons(semantic_label)),
)


finite_sample = live_source(
    all_atoms_joint_at_formation=False,
    control_instantiation_impossible_at_formation=False,
    finite_sample_filter=True,
    control_formable=True,
)

gate(
    "CFD6 finite admission samples are not carrier formation rules",
    not accepts_control_death(finite_sample)
    and {
        "atoms_not_joint_at_formation",
        "control_instantiation_not_impossible_at_formation",
        "finite_sample_filter",
        "control_formable",
    }
    <= set(reasons(finite_sample)),
    ",".join(reasons(finite_sample)),
)


declared_death = live_source(
    control_instantiation_impossible_at_formation=False,
    control_not_built_before_filter=False,
    declared_control_death=True,
)

gate(
    "CFD7 declared control death without formation obstruction is rejected",
    not accepts_control_death(declared_death)
    and {
        "control_instantiation_not_impossible_at_formation",
        "control_built_before_filter",
        "declared_control_death",
    }
    <= set(reasons(declared_death)),
    ",".join(reasons(declared_death)),
)


missing_joint_atoms = [
    live_source(endpoint_integrality_native=False),
    live_source(degree_maps_native=False),
    live_source(dd4_boundary_native=False),
    live_source(boundary_pushforward_compat_native=False),
    live_source(proper_graph_composition_native=False),
    live_source(positive_rosati_native=False),
]

gate(
    "CFD8 endpoint, degree, DD.4, graph, and Rosati atoms must die controls jointly",
    not any(accepts_control_death(data) for data in missing_joint_atoms)
    and {
        "endpoint_integrality_not_native",
        "degree_maps_not_native",
        "dd4_boundary_not_native",
        "boundary_pushforward_compat_not_native",
        "proper_graph_composition_not_native",
        "positive_rosati_not_native",
    }
    <= set().union(*(set(reasons(data)) for data in missing_joint_atoms)),
    "missing=%s"
    % sorted(set().union(*(set(reasons(data)) for data in missing_joint_atoms))),
)


control_lookalike = live_source(carrier_native=False, control_formable=True)

gate(
    "CFD9 complete-looking control package still fails formation death",
    not accepts_control_death(control_lookalike)
    and {"not_carrier_native", "control_formable"} <= set(reasons(control_lookalike)),
    ",".join(reasons(control_lookalike)),
)


live_control_death = live_source()
dead_sources = {
    "posthoc_rosati": posthoc_filters[0],
    "posthoc_projection": posthoc_filters[1],
    "posthoc_dd4": posthoc_filters[2],
    "semantic_label": semantic_label,
    "finite_sample": finite_sample,
    "declared_death": declared_death,
    "control_lookalike": control_lookalike,
}

gate(
    "CFD10 only formation-level control death passes",
    accepts_control_death(live_control_death)
    and not any(accepts_control_death(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_control_death(data) for data in dead_sources.values()),
        accepts_control_death(live_control_death),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCFD1-CFD10 ALL PASS: formation-level control-death contract pinned")
print(
    "VERDICT: controls must be impossible to instantiate at carrier formation "
    "because endpoint integrality, degree maps, DD.4 boundary, boundary "
    "pushforward compatibility, graph composition, Rosati, and count/degree "
    "anchors are produced jointly. Post-hoc Rosati/projection/DD.4 filters, "
    "semantic zeta labels, finite samples, declared deaths, and complete-looking "
    "control packages do not meet this contract."
)
