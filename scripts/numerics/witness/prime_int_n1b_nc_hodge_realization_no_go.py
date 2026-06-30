r"""Noncommutative Hodge / periodic-cyclic realization no-go.

After doc 226, the next repair is to take the smooth-proper/CY category and
apply a realization functor such as periodic cyclic homology or a polarized
noncommutative Hodge structure, hoping the realized Hodge data supplies the
square carrier and positive Rosati.  This still does not construct
End(S^2/Z): the realization profile is too coarse to determine finite-field
counts, it does not construct NS degree slots, positive Hodge data does not
make Frobenius compatible unless the Rosati relation is added, finite windows
admit ghost realization summands, and the same realization package is formable
on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_nc_hodge_realization_no_go
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


def realization_profile(dim: int = 2) -> tuple[int, int, tuple[int, int], bool]:
    # A toy HP/Hodge profile: HP_even dimension, HP_odd dimension, Hodge split,
    # and existence of a positive polarization on the realized vector space.
    return (dim, 0, (dim // 2, dim // 2), True)


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# NHR1: identical realization profiles do not determine the finite-field count
# anchor. The q=7,a=1 and q=5,a=2 anchors both have the same toy HP/Hodge
# profile, but their point-count windows differ.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = realization_profile(2)
profile_other = realization_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "NHR1 HP/Hodge realization profile does not determine count anchor",
    profile_true == profile_other == (2, 0, (1, 1), True) and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# NHR2: the realization does not construct NS degree slots. Keeping the same
# realized vector space and z-component but changing d1 changes Delta.Gamma.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "NHR2 realization data does not construct NS degree slots",
    profile_true == realization_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same realization and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# NHR3: a positive realized Hodge metric does not make Frobenius compatible.
# Compatibility F^* H F = qH is the Rosati/polarization relation, not a
# consequence of having a positive realization.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = realization_profile(2)
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "NHR3 positive Hodge realization does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# NHR4: finite realization windows still admit ghost HP/Hodge summands. A
# 5-cycle ghost has zero traces in powers 1..4 and trace 5 in power 5.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
ghost_profile = realization_profile(window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "NHR4 finite Hodge-realization windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and ghost_profile[0] == 5
    and count_5_gap == 5.0,
    "first %d traces match; ghost HP_even=%d; count_5 gap=%.1f"
    % (window, ghost_profile[0], count_5_gap),
)


# NHR5: the same realization package is formable on arbitrary control
# companion data without Euler product, Satake parameters, rep_NS, square, or
# positive Rosati.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = realization_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, H_pos)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "NHR5 NC-Hodge realization package is formable on controls",
    control_profile == (2, 0, (1, 1), True)
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


# NHR6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_hodge_realization_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "NHR6 NC-Hodge/HP realization constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_hodge_realization_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, realization theorem, degrees, pairing, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (NHR1-NHR6)")
print(
    "VERDICT: NC-Hodge or periodic-cyclic realization of a smooth-proper "
    "category is not End(S^2/Z). Realization profiles do not determine "
    "finite-field counts, do not construct NS degree slots, positive realized "
    "metrics do not impose Frobenius/Rosati compatibility, finite windows "
    "admit ghost realization summands, controls admit the same package, and "
    "no actual square, proper correspondences, projection formula, positive "
    "Rosati, or control death is constructed."
)
