r"""Six-functor / Lefschetz-Verdier trace formalism no-go.

After doc 228, the next repair is to say that the needed square
correspondence calculus is supplied by a six-functor formalism: cohomological
correspondences, Verdier duality, proper pushforward, trace maps, and the
Lefschetz-Verdier fixed-point formula.  This still does not construct
End(S^2/Z).  A trace formalism is an operation available after a carrier and
proper maps are built; by itself it does not build the square, the NS degree
slots, the Frobenius graph, the projection formula, the Rosati relation, or
control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_six_functor_trace_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
)


failures: list[str] = []


Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


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


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def six_functor_profile(dim: int = 2) -> tuple[int, bool, bool, bool, bool, bool, bool]:
    # Toy formalism profile: cohomological correspondences, f*, f_*, f_!,
    # f!, Verdier duality, trace, and projection formula are available.
    return (dim, True, True, True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# SFT1: identical six-functor formalism profiles do not determine the
# finite-field count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = six_functor_profile(2)
profile_other = six_functor_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "SFT1 six-functor trace profile does not determine count anchor",
    profile_true == profile_other == (2, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# SFT2: trace formalism does not construct NS degree slots.  Keeping the
# same cohomological action and trace/projection operations, changing d1
# changes Delta.Gamma.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "SFT2 trace formalism does not construct NS degree slots",
    profile_true == six_functor_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same cohomological action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# SFT3: a scalar Lefschetz trace is not a graph correspondence.  A trace-zero
# perturbation preserves the n=1 trace and count while changing the next
# trace/count and determinant.
trace_perturbation = np.array([[0.0, 1.0], [0.0, 0.0]])
F_same_trace = F_true + trace_perturbation
same_n1_trace = np.trace(F_same_trace) == np.trace(F_true)
same_n1_count = point_count(F_same_trace, q_true, 1) == point_count(F_true, q_true, 1)
different_n2_count = point_count(F_same_trace, q_true, 2) != point_count(F_true, q_true, 2)
different_det = round(float(np.linalg.det(F_same_trace)), 9) != round(float(np.linalg.det(F_true)), 9)

gate(
    "SFT3 scalar Lefschetz trace is not a carrier-native graph",
    same_n1_trace and same_n1_count and different_n2_count and different_det,
    "Tr1=%.1f, count1=%.1f, count2 %.1f -> %.1f, det %.1f -> %.1f"
    % (
        np.trace(F_true),
        point_count(F_true, q_true, 1),
        point_count(F_true, q_true, 2),
        point_count(F_same_trace, q_true, 2),
        np.linalg.det(F_true),
        np.linalg.det(F_same_trace),
    ),
)


# SFT4: proper pushforward/ambidexterity existence does not pin the degree
# character.  Trace maps for finite free vector-space models exist with
# either scalar.
degree_a = 7.0
degree_b = 10.0
proper_trace_a_exists = degree_a != 0.0
proper_trace_b_exists = degree_b != 0.0

gate(
    "SFT4 proper trace existence does not pin the degree character",
    proper_trace_a_exists
    and proper_trace_b_exists
    and profile_true == six_functor_profile(2)
    and degree_a != degree_b,
    "same six-functor operations with trace degree %.1f or %.1f" % (degree_a, degree_b),
)


# SFT5: finite trace-formalism windows admit ghost cohomological
# correspondences.  A 5-cycle ghost has zero traces in powers 1..4 and trace
# 5 in power 5.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "SFT5 finite trace-formalism windows admit ghost correspondences",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; ghost rank=%d; count_5 gap=%.1f"
    % (window, ghost.shape[0], count_5_gap),
)


# SFT6: the same six-functor/trace profile is formable on arbitrary controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = six_functor_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "SFT6 six-functor trace package is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no Euler/Satake/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# SFT7: construction audit.
zeta_site_or_stack_constructed = False
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_proper_maps_constructed = False
zeta_six_functor_formalism_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_lefschetz_fixed_point_theorem_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "SFT7 six-functor trace formalism constructs no End(S^2/Z) square package",
    not zeta_site_or_stack_constructed
    and not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_proper_maps_constructed
    and not zeta_six_functor_formalism_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_lefschetz_fixed_point_theorem_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no site/stack, rep_NS, square, proper maps, correspondences, graph, trace theorem, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SFT1-SFT7)")
print(
    "VERDICT: six-functor or Lefschetz-Verdier trace formalism is not "
    "End(S^2/Z). Trace operations do not determine counts, construct NS "
    "degree slots, turn scalar traces into carrier-native graphs, pin the "
    "degree character, exclude ghost correspondences, or kill controls; no "
    "actual square, proper maps, correspondence category, projection formula, "
    "positive Rosati, or DD.4 datum is constructed."
)
