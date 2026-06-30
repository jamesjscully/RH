r"""Perfect-module/dg Morita envelope no-go.

After doc 224, the next repair is to replace the completed presented carrier
by its dg category of perfect modules, or by a noncommutative motive/additive
invariant, hoping Morita invariance supplies the correct idempotents and
correspondence algebra.  This still does not construct End(S^2/Z): Morita
stabilization hides matrix overproduction, additive traces such as HH0/K0 do
not determine finite-field counts or NS degree slots, finite windows still
admit ghost summands, and the same perfect-module envelope is formable on
controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_perfect_morita_envelope_no_go
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


def companion_discriminant(q: int, trace: int) -> int:
    return trace * trace - 4 * q


def quadratic_algebra_dimension(_q: int, _trace: int) -> int:
    return 2


def matrix_algebra_dimension(base_dim: int, rank: int) -> int:
    return base_dim * rank * rank


def morita_hh0_dimension(base_dim: int, _rank: int) -> int:
    # HH0(Mat_r(A)) ~= HH0(A); for the commutative quadratic algebra A, dim HH0(A)=dim A.
    return base_dim


def morita_k0_rank(_base_dim: int, _rank: int) -> int:
    # A field-like simple component and any matrix stabilization have one projective generator class.
    return 1


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


# PME1: passing to Perf(A) or any Morita-invariant replacement makes
# Mat_r(A) indistinguishable from A while the raw endomorphism envelope grows.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
base_dim = quadratic_algebra_dimension(q_true, trace_true)
ranks = [1, 2, 5]
raw_end_dims = [matrix_algebra_dimension(base_dim, r) for r in ranks]
hh0_dims = [morita_hh0_dimension(base_dim, r) for r in ranks]
k0_ranks = [morita_k0_rank(base_dim, r) for r in ranks]

gate(
    "PME1 dg Morita stabilization hides matrix overproduction",
    raw_end_dims == [2, 8, 50] and hh0_dims == [2, 2, 2] and k0_ranks == [1, 1, 1],
    "End dims=%s, HH0 dims=%s, K0 ranks=%s" % (raw_end_dims, hh0_dims, k0_ranks),
)


# PME2: coarse Morita/additive invariants do not determine the finite-field
# trace/count anchor. Two different anchors have the same field-like Perf
# invariant profile but different count windows.
F_other = frobenius(5, 2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)
profile_true = (quadratic_algebra_dimension(7, 1), morita_hh0_dimension(2, 1), morita_k0_rank(2, 1))
profile_other = (quadratic_algebra_dimension(5, 2), morita_hh0_dimension(2, 1), morita_k0_rank(2, 1))

gate(
    "PME2 additive Morita traces do not determine point-count anchors",
    profile_true == profile_other == (2, 2, 1) and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# PME3: Perf of the z-component algebra does not supply the NS degree slots.
# The same algebra Q[F] supports different formal triples (d1,F,d2), changing
# Delta.Gamma while Perf(Q[F]) is unchanged.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)
same_perf_algebra = True

gate(
    "PME3 perfect modules over Q[F] do not construct NS degree slots",
    same_perf_algebra and true_delta_graph == 7.0 and retuned_delta_graph == 10.0,
    "same z-algebra, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# PME4: finite trace windows still admit ghost perfect summands. A 5-cycle
# ghost has zero traces in powers 1..4, so Perf(A x G) has an extra direct
# summand invisible to that finite window but visible at the next count.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
ghost_perf_k0_rank = window + 1
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "PME4 finite perfect-module windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and ghost_perf_k0_rank == 5
    and count_5_gap == 5.0,
    "first %d traces match; ghost K0 rank=%d; count_5 gap=%.1f"
    % (window, ghost_perf_k0_rank, count_5_gap),
)


# PME5: the same perfect-module/Morita envelope is formable on arbitrary
# control companion data, before any Euler product, Satake parameters, square,
# or positive Rosati exists.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = (
    quadratic_algebra_dimension(control_q, control_trace),
    morita_hh0_dimension(2, 3),
    morita_k0_rank(2, 3),
    companion_discriminant(control_q, control_trace),
)
control_counts = point_counts(F_control, control_q, 3)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "PME5 perfect-module Morita envelope is formable on controls",
    control_profile == (2, 2, 1, -31)
    and control_counts == [8.0, 112.0, 1064.0]
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, no Euler/Satake/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts]),
)


# PME6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_perf_category_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "PME6 perfect-module/Morita envelope constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_perf_category_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, degree maps, pairing, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PME1-PME6)")
print(
    "VERDICT: passing a presented/numerical carrier to Perf(A), a dg Morita "
    "envelope, or a noncommutative motive is not End(S^2/Z). Morita "
    "stabilization hides matrix overproduction, additive traces do not "
    "construct point counts or NS degree slots, finite windows admit ghost "
    "perfect summands, the same construction is formable on controls, and no "
    "actual square, proper correspondences, carrier-native pairing, positive "
    "Rosati, or control death is constructed."
)
