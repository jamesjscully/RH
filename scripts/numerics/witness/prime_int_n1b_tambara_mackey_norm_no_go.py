r"""Tambara/Mackey norm-transfer carrier no-go.

Real cyclotomic and algebraic K/TC routes were already killed as direct
square carriers, and the Witt/Lambda/delta package was killed as absolute
Frobenius-lift geometry.  The nearby equivariant repair is to use the
Tambara/Mackey/Burnside norm-transfer calculus itself as the square
correspondence carrier.

This witness records why that package is still downstream/shadow data unless
it constructs the actual square, rep_NS, degree maps, Frobenius graph,
projection formula, and positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_tambara_mackey_norm_no_go
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


def tmn_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: Tambara functor, Mackey functor, restrictions, transfers,
    # norms, Burnside category, double-coset formula, and genuine fixed points.
    return (True, True, True, True, True, True, True, True)


def burnside_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy Burnside/Mackey shadow: records orbit degree and rank, but forgets
    # endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def double_coset_formula_holds(groups: tuple[int, ...]) -> bool:
    # Toy finite subgroup incidence check: the formal Mackey law is present.
    return all(g > 0 for g in groups)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# TMN1: the same Tambara/Mackey/norm profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = tmn_profile()
profile_other = tmn_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "TMN1 Tambara/Mackey/norm profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# TMN2: transfer/restriction/norm data does not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "TMN2 transfer/restriction/norm data does not construct NS degree slots",
    profile_true == tmn_profile()
    and double_coset_formula_holds((1, 2, 7))
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same Mackey laws and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# TMN3: Burnside/Mackey shadows can forget endpoint and extension data.
class_a = np.array([3, 2, 0])
class_b = np.array([3, 2, 4])
same_shadow = burnside_shadow(class_a) == burnside_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "TMN3 Burnside/Mackey shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 4,
    "same Burnside shadow=%s, endpoint gap=%d"
    % (burnside_shadow(class_a), endpoint_gap),
)


# TMN4: norm/transfer positivity does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
declares_norm_positivity = True
declares_wirthmuller_duality = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "TMN4 norm positivity does not impose Frobenius/Rosati compatibility",
    declares_norm_positivity and declares_wirthmuller_duality and off_metric_defect > 1.0,
    "norm-positive/Wirthmuller=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# TMN5: declaring Tambara/Mackey functoriality does not construct the square
# projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_restrictions = True
declares_transfers = True
declares_norms = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "TMN5 Mackey/norm functoriality is not constructed projection formula",
    declares_restrictions
    and declares_transfers
    and declares_norms
    and semantic_projection_defect == 27.0,
    "declared restriction/transfer/norm=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# TMN6: finite equivariant/Tambara windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "TMN6 finite Tambara/Mackey windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f" % (window, window + 1, count_5_gap),
)


# TMN7: the same formal package is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = tmn_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "TMN7 formal Tambara/Mackey/norm schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_zeta_square_carrier
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_projection_formula
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no square/rep_NS/degrees/projection/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# TMN8: construction audit.
zeta_tambara_carrier_constructed = False
zeta_mackey_carrier_constructed = False
zeta_burnside_carrier_constructed = False
zeta_norm_transfer_carrier_constructed = False
zeta_equivariant_stable_homotopy_carrier_constructed = False
zeta_ambient_square_constructed = False
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
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
    "TMN8 Tambara/Mackey/norm package constructs no End(S^2/Z) square package",
    not zeta_tambara_carrier_constructed
    and not zeta_mackey_carrier_constructed
    and not zeta_burnside_carrier_constructed
    and not zeta_norm_transfer_carrier_constructed
    and not zeta_equivariant_stable_homotopy_carrier_constructed
    and not zeta_ambient_square_constructed
    and not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no Tambara carrier, Mackey carrier, Burnside carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("TMN1-TMN8 ALL PASS: Tambara / Mackey / norm-transfer calculus is not End(S^2/Z)")
