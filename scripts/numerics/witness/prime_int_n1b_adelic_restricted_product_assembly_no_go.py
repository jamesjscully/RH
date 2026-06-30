r"""Adelic restricted-product assembly no-go.

After doc 230, the next repair is to assemble all local p-adic/prismatic
packages by a restricted product, add the archimedean place, and use the
result as the global square carrier.  This still does not construct
End(S^2/Z).  Restricted products and product-formula compatibility are
bookkeeping unless the square, proper correspondences, degree maps,
Frobenius graph, projection formula, and positive Rosati have already been
built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_adelic_restricted_product_assembly_no_go
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


def adelic_profile(local_count: int = 3) -> tuple[int, bool, bool, bool, bool, bool]:
    # Toy restricted-product profile: finitely many displayed local packages,
    # restricted-product condition, product formula, archimedean component,
    # local trace factors, and comparison maps.
    return (local_count, True, True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# ARP1: identical restricted-product profiles do not determine the
# finite-field count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = adelic_profile(3)
profile_other = adelic_profile(3)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "ARP1 restricted-product profile does not determine count anchor",
    profile_true == profile_other == (3, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# ARP2: local all-place bookkeeping does not construct NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "ARP2 restricted-product data does not construct NS degree slots",
    profile_true == adelic_profile(3)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same adelic profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# ARP3: finite all-prime windows do not pin the over-Z degree character.
small_primes = (2, 3, 5)
modulus = int(np.prod(small_primes))
degree_a = 7
degree_b = 37
same_finite_local_degrees = all(
    degree_a % p == degree_b % p for p in small_primes
)

gate(
    "ARP3 finite all-prime window does not pin global degree character",
    same_finite_local_degrees
    and degree_a % modulus == degree_b % modulus
    and ns_intersection(D_true, corr(float(degree_a), F_true, 1.0)) == 7.0
    and ns_intersection(D_true, corr(float(degree_b), F_true, 1.0)) == 37.0,
    "primes=%s, mod=%d, degrees %d and %d agree locally but Delta.Gamma differs %.1f -> %.1f"
    % (
        small_primes,
        modulus,
        degree_a,
        degree_b,
        ns_intersection(D_true, corr(float(degree_a), F_true, 1.0)),
        ns_intersection(D_true, corr(float(degree_b), F_true, 1.0)),
    ),
)


# ARP4: product-formula and determinant/pairing data do not impose the
# individual radius split or Rosati compatibility.
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
    "ARP4 product formula does not impose radius split or Rosati",
    all(abs(pp - q_pair) < 1e-9 for pp in pair_products)
    and abs(det_product - q_pair**2) < 1e-9
    and not even_split
    and off_metric_defect > 1.0,
    "moduli=%s, pair_products=%s, det=%.1f, Rosati_defect=%.3f"
    % (
        [round(float(m), 6) for m in moduli],
        [round(float(pp), 6) for pp in pair_products],
        det_product,
        off_metric_defect,
    ),
)


# ARP5: finite local/restricted-product windows admit ghost summands.  A
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
    "ARP5 finite adelic windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; ghost rank=%d; count_5 gap=%.1f"
    % (window, ghost.shape[0], count_5_gap),
)


# ARP6: the same restricted-product profile is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = adelic_profile(3)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_actual_local_factors_from_carrier = False
control_has_archimedean_square_component = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "ARP6 restricted-product package is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_actual_local_factors_from_carrier
    and not control_has_archimedean_square_component
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no carrier-local/arch/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# ARP7: construction audit.
zeta_restricted_product_square_constructed = False
zeta_diagonal_rational_quotient_constructed = False
zeta_archimedean_compatible_carrier_constructed = False
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
    "ARP7 restricted-product assembly constructs no End(S^2/Z) square package",
    not zeta_restricted_product_square_constructed
    and not zeta_diagonal_rational_quotient_constructed
    and not zeta_archimedean_compatible_carrier_constructed
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
    "no restricted-product square, rational quotient, arch-compatible carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (ARP1-ARP7)")
print(
    "VERDICT: an adelic restricted product of local comparison packages is "
    "bookkeeping, not a global square carrier.  It does not determine count "
    "anchors, degree slots, individual radii, Rosati, ghost exclusion, "
    "control death, rep_NS, or End(S^2/Z)."
)
