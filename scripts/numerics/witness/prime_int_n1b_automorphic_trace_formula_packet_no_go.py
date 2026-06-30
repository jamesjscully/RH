r"""Automorphic / trace-formula packet no-go.

After doc 231, the next repair is to enrich the adelic package with
automorphic spectral data: Hecke action, Satake parameters, Euler product,
functional equation, trace formula, and Rankin-Selberg edge data.  This is
still not construction of End(S^2/Z).  Automorphic packets organize scalar
spectral and local-factor data; they do not by themselves construct the
global square, rep_NS, carrier-native degree maps, proper correspondences,
Frobenius graph, projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_automorphic_trace_formula_packet_no_go
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


def automorphic_packet_profile(rank: int = 2) -> tuple[int, bool, bool, bool, bool, bool, bool]:
    # Toy spectral packet: rank, Hecke action, Satake parameters, Euler
    # product, functional equation, trace formula, and Rankin-Selberg edge.
    return (rank, True, True, True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# ATF1: identical abstract automorphic packet profiles do not determine the
# finite-field count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = automorphic_packet_profile(2)
profile_other = automorphic_packet_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "ATF1 automorphic packet profile does not determine count anchor",
    profile_true == profile_other == (2, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# ATF2: Hecke/Satake packet data does not construct NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "ATF2 Hecke/Satake data does not construct NS degree slots",
    profile_true == automorphic_packet_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same automorphic profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# ATF3: a scalar trace formula at one test function is not graph composition.
# The first trace/count agrees after a trace-zero perturbation, but the second
# trace/count changes because no carrier-native graph law has been built.
trace_zero_perturbation = np.array([[0.0, 1.0], [0.0, 0.0]])
F_scalar_only = F_true + trace_zero_perturbation
same_first_trace = np.trace(F_scalar_only) == np.trace(F_true)
count1_true = point_count(F_true, q_true, 1)
count1_scalar_only = point_count(F_scalar_only, q_true, 1)
count2_true = point_count(F_true, q_true, 2)
count2_scalar_only = point_count(F_scalar_only, q_true, 2)

gate(
    "ATF3 scalar trace formula data is not carrier graph composition",
    same_first_trace
    and count1_true == count1_scalar_only == 7.0
    and count2_true == 63.0
    and count2_scalar_only == 61.0,
    "same first trace/count %.1f; second count changes %.1f -> %.1f without graph law"
    % (count1_true, count2_true, count2_scalar_only),
)


# ATF4: Rankin-Selberg/product edge data does not impose individual radius
# split or Frobenius/Rosati compatibility.
q_pair = 9.0
sqrt_q = np.sqrt(q_pair)
r = float(np.exp(0.4))
moduli = [r * sqrt_q, sqrt_q / r, sqrt_q / r, r * sqrt_q]
pair_products = [moduli[0] * moduli[1], moduli[2] * moduli[3]]
det_product = float(np.prod(moduli))
even_split = all(abs(m - sqrt_q) < 1e-9 for m in moduli)
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
off_metric_defect = normalized_metric_defect(F_off, 2.0, np.eye(2))

gate(
    "ATF4 Rankin-Selberg edge does not impose radius split or Rosati",
    all(abs(pp - q_pair) < 1e-9 for pp in pair_products)
    and abs(det_product - q_pair**2) < 1e-9
    and not even_split
    and off_metric_defect > 1.0,
    "edge pair_products=%s, det=%.1f, moduli=%s, Rosati_defect=%.3f"
    % (
        [round(float(pp), 6) for pp in pair_products],
        det_product,
        [round(float(m), 6) for m in moduli],
        off_metric_defect,
    ),
)


# ATF5: finite automorphic/trace-formula windows admit ghost summands.  A
# 5-cycle ghost has zero traces in powers 1..4 and trace 5 in power 5.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "ATF5 finite trace-formula windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; ghost rank=%d; count_5 gap=%.1f"
    % (window, ghost.shape[0], count_5_gap),
)


# ATF6: the same formal spectral-packet schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = automorphic_packet_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_actual_automorphic_realization = False
control_has_rep_ns = False
control_has_square = False
control_has_proper_correspondences = False
control_has_positive_rosati = False

gate(
    "ATF6 formal automorphic packet schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_actual_automorphic_realization
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_proper_correspondences
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no automorphic realization/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# ATF7: construction audit.
zeta_automorphic_moduli_carrier_constructed = False
zeta_trace_formula_geometric_side_constructed = False
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
    "ATF7 automorphic trace-formula packet constructs no End(S^2/Z) square package",
    not zeta_automorphic_moduli_carrier_constructed
    and not zeta_trace_formula_geometric_side_constructed
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
    "no automorphic moduli carrier, geometric trace side, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (ATF1-ATF7)")
print(
    "VERDICT: automorphic/trace-formula packet data is not End(S^2/Z). "
    "It does not determine the square carrier, degree slots, graph "
    "composition, individual radii, Rosati, ghost exclusion, control death, "
    "rep_NS, or proper correspondences."
)
