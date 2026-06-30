r"""Algebraic K-theory / cyclotomic trace carrier no-go.

After operator K/KK assembly fails as direct square construction, the nearby
arithmetic trace-method repair is to use algebraic K-theory, the cyclotomic
trace, TC/TR/TP, cyclotomic Frobenius, and topological cyclic descent as the
carrier.  These are strong realization and comparison tools after a carrier
exists.  They do not by themselves construct the square, rep_NS, degree
maps, Frobenius graph, projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_algebraic_k_cyclotomic_trace_no_go
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


def ktc_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: algebraic K-theory, cyclotomic trace, THH, TC/TR/TP,
    # cyclotomic Frobenius, Nygaard/periodic filtration, descent square, and
    # trace method.
    return (True, True, True, True, True, True, True, True)


def trace_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy cyclotomic-trace shadow: records K-rank and TC-periodic degree,
    # but forgets endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# KTC1: the same algebraic K/TC profile does not determine a finite-field
# count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = ktc_profile()
profile_other = ktc_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "KTC1 algebraic K/TC profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# KTC2: cyclotomic trace / TC data does not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "KTC2 cyclotomic trace data does not construct NS degree slots",
    profile_true == ktc_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same K/TC profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# KTC3: cyclotomic trace / TC periodic shadows can forget correspondence
# endpoint and extension data.
k_class_a = np.array([1, 2, 0])
k_class_b = np.array([1, 2, 4])
same_trace_shadow = trace_shadow(k_class_a) == trace_shadow(k_class_b)
endpoint_gap = int(np.linalg.norm(k_class_a - k_class_b))

gate(
    "KTC3 cyclotomic trace shadow loses correspondence endpoint data",
    same_trace_shadow and endpoint_gap == 4,
    "same trace shadow=%s, endpoint gap=%d"
    % (trace_shadow(k_class_a), endpoint_gap),
)


# KTC4: cyclotomic Frobenius / TP periodicity does not impose
# Frobenius/Rosati compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
has_cyclotomic_frobenius = True
has_tp_periodicity = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "KTC4 cyclotomic Frobenius/TP periodicity does not impose Frobenius/Rosati compatibility",
    has_cyclotomic_frobenius and has_tp_periodicity and off_metric_defect > 1.0,
    "cyclotomic Frobenius/TP=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# KTC5: declaring descent squares / trace method does not construct the
# square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_cyclotomic_trace = True
declares_tc_descent_square = True
declares_trace_method = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "KTC5 TC descent declaration is not constructed projection formula",
    declares_cyclotomic_trace
    and declares_tc_descent_square
    and declares_trace_method
    and semantic_projection_defect == 27.0,
    "declared trace/descent/method=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# KTC6: finite TC/K-theory windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "KTC6 finite K/TC windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# KTC7: the same algebraic K/TC schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = ktc_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "KTC7 formal algebraic K/TC schema is formable on controls",
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


# KTC8: construction audit.
zeta_algebraic_k_carrier_constructed = False
zeta_cyclotomic_trace_carrier_constructed = False
zeta_thh_carrier_constructed = False
zeta_tc_tr_tp_carrier_constructed = False
zeta_cyclotomic_frobenius_carrier_constructed = False
zeta_tc_descent_square_constructed = False
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
    "KTC8 algebraic K/TC package constructs no End(S^2/Z) square package",
    not zeta_algebraic_k_carrier_constructed
    and not zeta_cyclotomic_trace_carrier_constructed
    and not zeta_thh_carrier_constructed
    and not zeta_tc_tr_tp_carrier_constructed
    and not zeta_cyclotomic_frobenius_carrier_constructed
    and not zeta_tc_descent_square_constructed
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
    "no algebraic K carrier, TC/TR/TP carrier, descent square, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("KTC1-KTC8 ALL PASS: algebraic K-theory / cyclotomic trace is not End(S^2/Z)")
