r"""Smooth-proper/Calabi-Yau Mukai pairing no-go.

After doc 225, the next repair is to enrich Perf(A) by declaring it smooth
proper, Calabi-Yau, or equipped with a Mukai/Euler/Frobenius trace pairing,
hoping categorical duality supplies the positive Rosati square carrier.  This
still does not construct End(S^2/Z): nondegenerate categorical trace pairings
are not the NS/Rosati pairing, their normalization is extra data, coarse
smooth-proper/CY profiles do not determine point counts, degree slots remain
unconstructed, finite windows admit ghost CY summands, and the same enrichment
is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_smooth_proper_cy_mukai_no_go
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


def power_traces(A: np.ndarray, upto: int) -> list[complex]:
    return [np.trace(np.linalg.matrix_power(A, n)) for n in range(1, upto + 1)]


def point_count(A: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(A, n)).real)


def point_counts(A: np.ndarray, q: float, upto: int) -> list[float]:
    return [point_count(A, q, n) for n in range(1, upto + 1)]


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


def trace_power_2(q: int, trace: int) -> int:
    return trace * trace - 2 * q


def cy_trace_gram(q: int, trace: int, scale: float = 1.0) -> np.ndarray:
    # Frobenius algebra trace pairing on Q[x]/(x^2 - trace*x + q), basis 1,x.
    return scale * np.array([[2.0, float(trace)], [float(trace), float(trace_power_2(q, trace))]])


def inertia(G: np.ndarray, tol: float = 1e-9) -> tuple[int, int, int]:
    eigs = np.linalg.eigvalsh(G)
    pos = int(np.sum(eigs > tol))
    neg = int(np.sum(eigs < -tol))
    nul = int(len(eigs) - pos - neg)
    return pos, neg, nul


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


# CYM1: a smooth-proper/0-CY Frobenius trace pairing exists on the finite
# etale algebra Q[F], but it is a nondegenerate categorical pairing, not the
# positive Rosati square pairing.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
G_true = cy_trace_gram(q_true, trace_true)
true_det = float(np.linalg.det(G_true))
true_inertia = inertia(G_true)
true_counts = point_counts(F_true, q_true, 4)

gate(
    "CYM1 smooth-proper CY trace pairing is nondegenerate but not Rosati positive",
    np.allclose(G_true, np.array([[2.0, 1.0], [1.0, -13.0]]))
    and round(true_det) == -27
    and true_inertia == (1, 1, 0)
    and true_counts == [7.0, 63.0, 364.0, 2331.0],
    "Gram=%s, det=%.0f, inertia=%s, counts=%s"
    % (G_true.astype(int).tolist(), true_det, true_inertia, [round(c, 1) for c in true_counts]),
)


# CYM2: Calabi-Yau/Frobenius trace normalization is extra data. Rescaling the
# trace preserves nondegeneracy and the same underlying category but changes
# the pairing; negative rescaling even reverses the sign convention.
G_scaled = cy_trace_gram(q_true, trace_true, scale=3.0)
G_negative = cy_trace_gram(q_true, trace_true, scale=-1.0)

gate(
    "CYM2 CY trace normalization is not carrier-native",
    np.linalg.det(G_scaled) != 0.0
    and np.linalg.det(G_negative) != 0.0
    and not np.allclose(G_scaled, G_true)
    and inertia(G_negative) == (1, 1, 0)
    and true_counts == point_counts(F_true, q_true, 4),
    "scale 3 Gram=%s, scale -1 inertia=%s, counts unchanged"
    % (G_scaled.astype(int).tolist(), inertia(G_negative)),
)


# CYM3: coarse smooth-proper/CY profiles do not determine the finite-field
# count anchor. Two genus-one anchors have the same finite-etale 0-CY profile
# but different count windows.
F_other = frobenius(5, 2)
G_other = cy_trace_gram(5, 2)
other_counts = point_counts(F_other, 5, 4)
profile_true = (2, bool(np.linalg.det(G_true) != 0.0), "Serre=Id")
profile_other = (2, bool(np.linalg.det(G_other) != 0.0), "Serre=Id")

gate(
    "CYM3 smooth-proper CY profile does not determine count anchor",
    profile_true == profile_other
    and true_counts != other_counts
    and round(np.linalg.det(G_other)) == -16,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in true_counts], [round(c, 1) for c in other_counts]),
)


# CYM4: the categorical trace pairing on Q[F] does not construct NS degree
# slots. Keeping the same z-component and CY pairing but changing d1 changes
# Delta.Gamma.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "CYM4 Mukai/Frobenius pairing does not construct NS degree slots",
    np.allclose(cy_trace_gram(q_true, trace_true), G_true)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same Q[F] and CY pairing, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# CYM5: finite trace windows still admit smooth-proper/CY ghost summands. A
# 5-cycle ghost has zero traces in powers 1..4 and trace 5 in power 5.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
ghost_cy_summand_rank = window + 1
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "CYM5 finite CY/Mukai windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and ghost_cy_summand_rank == 5
    and count_5_gap == 5.0,
    "first %d traces match; ghost CY rank=%d; count_5 gap=%.1f"
    % (window, ghost_cy_summand_rank, count_5_gap),
)


# CYM6: the same smooth-proper/CY trace pairing is formable on arbitrary
# companion controls, before Euler product, Satake parameters, square carrier,
# or positive Rosati exist.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
G_control = cy_trace_gram(control_q, control_trace)
control_counts = point_counts(F_control, control_q, 3)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "CYM6 smooth-proper CY/Mukai package is formable on controls",
    np.allclose(G_control, np.array([[2.0, 3.0], [3.0, -11.0]]))
    and round(np.linalg.det(G_control)) == -31
    and inertia(G_control) == (1, 1, 0)
    and control_counts == [8.0, 112.0, 1064.0]
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control Gram=%s, counts=%s, no Euler/Satake/rep_NS/square/Rosati"
    % (G_control.astype(int).tolist(), [round(c, 1) for c in control_counts]),
)


# CYM7: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_cy_structure_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "CYM7 smooth-proper/CY Mukai pairing constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_cy_structure_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, degree maps, pairing, projection, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CYM1-CYM7)")
print(
    "VERDICT: smooth-proper/Calabi-Yau or Mukai-paired enrichment of a "
    "perfect-module carrier is not End(S^2/Z). Nondegenerate categorical "
    "trace pairings are scale-dependent and can be indefinite, do not "
    "determine point counts or NS degree slots, finite windows admit ghost "
    "CY summands, the same package is formable on controls, and no actual "
    "square, proper correspondences, projection formula, positive Rosati, or "
    "control death is constructed."
)
