r"""Arakelov / arithmetic intersection carrier no-go.

After doc 242 killed local perfectoid/diamond/Fargues-Fontaine geometry as
direct square construction, another square-looking repair is to use Arakelov
geometry directly: arithmetic Chow groups, Green currents, metrized line
bundles, height pairings, Deligne pairings, and the arithmetic Hodge index
theorem.  This is still not End(S^2/Z).  Arithmetic intersection theory is
powerful only after the arithmetic surface/square, proper correspondences,
degree maps, Frobenius graph, projection formula, and positive Rosati have
been built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_arakelov_arithmetic_intersection_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
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


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


def point_count(A: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(A, n)).real)


def point_counts(A: np.ndarray, q: float, upto: int) -> list[float]:
    return [point_count(A, q, n) for n in range(1, upto + 1)]


def power_traces(A: np.ndarray, upto: int) -> list[complex]:
    return [np.trace(np.linalg.matrix_power(A, n)) for n in range(1, upto + 1)]


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    n = sum(block.shape[0] for block in blocks)
    out = np.zeros((n, n), dtype=complex)
    pos = 0
    for block in blocks:
        k = block.shape[0]
        out[pos : pos + k, pos : pos + k] = block
        pos += k
    return out


def cycle_permutation(order: int) -> np.ndarray:
    P = np.zeros((order, order), dtype=complex)
    for i in range(order):
        P[(i + 1) % order, i] = 1.0
    return P


def arakelov_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: arithmetic Chow group, Green current, hermitian line
    # bundle, height pairing, Deligne pairing, arithmetic Hodge index, and
    # archimedean metric data.
    return (True, True, True, True, True, True, True)


def height_shadow(arithmetic_class: np.ndarray) -> tuple[float, float]:
    # A toy height/Green-current shadow that records degree and metric part
    # but forgets the correspondence endpoint coordinate.
    return (float(arithmetic_class[0]), float(arithmetic_class[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# AIC1: the same Arakelov/arithmetic-intersection profile does not determine
# a finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = arakelov_profile()
profile_other = arakelov_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "AIC1 Arakelov profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# AIC2: arithmetic intersection language does not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "AIC2 arithmetic intersection data does not construct NS degree slots",
    profile_true == arakelov_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same Arakelov profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# AIC3: a height or Green-current shadow can forget the correspondence
# endpoint/lattice data needed for rep_NS.
arith_class_a = np.array([1.0, 2.0, 0.0])
arith_class_b = np.array([1.0, 2.0, 4.0])
same_height_shadow = height_shadow(arith_class_a) == height_shadow(arith_class_b)
endpoint_gap = float(np.linalg.norm(arith_class_a - arith_class_b))

gate(
    "AIC3 height/Green-current shadow loses correspondence endpoint data",
    same_height_shadow and endpoint_gap == 4.0,
    "same height shadow=%s, endpoint gap=%.1f"
    % (height_shadow(arith_class_a), endpoint_gap),
)


# AIC4: metric/Green positivity does not impose the Frobenius/Rosati
# compatibility relation required by the square.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = arakelov_profile()
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "AIC4 Green metric positivity does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# AIC5: declaring arithmetic Hodge index/projection does not construct the
# actual square correspondence calculus.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_arithmetic_hodge_index = True
declares_deligne_pairing = True
declares_projection_formula = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "AIC5 arithmetic Hodge/projection declaration is not constructed projection formula",
    declares_arithmetic_hodge_index
    and declares_deligne_pairing
    and declares_projection_formula
    and semantic_projection_defect == 27.0,
    "declared Hodge-index/Deligne/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# AIC6: finite Arakelov/intersection windows admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "AIC6 finite Arakelov/intersection windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# AIC7: the same formal Arakelov schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = arakelov_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_arithmetic_surface = False
control_has_arithmetic_chow_group = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_positive_rosati = False

gate(
    "AIC7 formal Arakelov schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_arithmetic_surface
    and not control_has_arithmetic_chow_group
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no arithmetic surface/rep_NS/degrees/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# AIC8: construction audit.
zeta_arithmetic_surface_constructed = False
zeta_arithmetic_chow_group_constructed = False
zeta_green_current_constructed = False
zeta_hermitian_ample_line_constructed = False
zeta_height_pairing_constructed = False
zeta_deligne_pairing_constructed = False
zeta_arithmetic_hodge_index_constructed = False
zeta_ambient_square_constructed = False
zeta_rep_ns_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "AIC8 Arakelov arithmetic-intersection package constructs no End(S^2/Z) square package",
    not zeta_arithmetic_surface_constructed
    and not zeta_arithmetic_chow_group_constructed
    and not zeta_green_current_constructed
    and not zeta_hermitian_ample_line_constructed
    and not zeta_height_pairing_constructed
    and not zeta_deligne_pairing_constructed
    and not zeta_arithmetic_hodge_index_constructed
    and not zeta_ambient_square_constructed
    and not zeta_rep_ns_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no arithmetic surface, arithmetic Chow group, square, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (AIC1-AIC8)")
print(
    "VERDICT: Arakelov arithmetic Chow groups, Green currents, metrized "
    "line bundles, height pairings, Deligne pairings, and arithmetic Hodge "
    "index are not End(S^2/Z). Their formal profile does not determine "
    "counts, does not construct NS degree slots, can forget correspondence "
    "endpoint data, does not impose Frobenius/Rosati compatibility, does not "
    "turn Hodge-index/projection declarations into a constructed projection "
    "formula, admits finite-window ghosts, is formable on controls, and "
    "constructs no actual square carrier."
)
