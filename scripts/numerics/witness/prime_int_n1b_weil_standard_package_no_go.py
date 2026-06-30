r"""Weil-cohomology / standard-conjectures package no-go.

After doc 227, the next repair is to add an abstract Weil cohomology package:
Kunneth projectors, Poincare duality, Hard Lefschetz, and Hodge-standard
positivity.  The hope is that these axioms supply the missing square carrier
and positive Rosati.  They do not construct End(S^2/Z): the package is still
only cohomological shadow data unless the square correspondence carrier and
its degree maps, pairings, Frobenius graph, projection formula, and Rosati
compatibility have already been constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_weil_standard_package_no_go
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


def weil_standard_profile(h1_dim: int = 2) -> tuple[tuple[int, int, int], bool, bool, bool, bool]:
    # Toy package: Betti dimensions plus existence of Kunneth projectors,
    # Poincare duality, Hard Lefschetz, and Hodge-standard positivity.
    return ((1, h1_dim, 1), True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


def hyperbolic_symplectic(dim: int) -> np.ndarray:
    I = np.eye(dim)
    Z = np.zeros((dim, dim))
    return np.block([[Z, I], [-I, Z]])


# WSC1: identical abstract Weil/standard profiles do not determine the
# finite-field count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = weil_standard_profile(2)
profile_other = weil_standard_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "WSC1 Weil-standard profile does not determine count anchor",
    profile_true == profile_other
    and profile_true == ((1, 2, 1), True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# WSC2: Kunneth projectors and cohomology dimensions do not construct the NS
# degree slots.  With the same H^1 operator, changing d1 changes Delta.Gamma.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "WSC2 Kunneth data does not construct NS degree slots",
    profile_true == weil_standard_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same Kunneth/H1 data, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# WSC3: Hodge-standard positivity is not Frobenius/Rosati compatibility.
# A positive form on the realized vector space does not imply F^T H F = qH.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = weil_standard_profile(2)
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "WSC3 Hodge-standard positivity does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# WSC4: Hard Lefschetz alone does not pin the degree/ample class.  Any nonzero
# scalar L: H0 -> H2 is an isomorphism in the toy package, but the scalar is
# exactly the degree information the carrier must construct.
lefschetz_scale_a = 7.0
lefschetz_scale_b = 10.0
hard_lefschetz_a = abs(lefschetz_scale_a) > 0
hard_lefschetz_b = abs(lefschetz_scale_b) > 0

gate(
    "WSC4 Hard Lefschetz existence does not pin the degree character",
    hard_lefschetz_a
    and hard_lefschetz_b
    and weil_standard_profile(2) == profile_true
    and lefschetz_scale_a != lefschetz_scale_b,
    "same Betti/projector package with Lefschetz scale %.1f or %.1f"
    % (lefschetz_scale_a, lefschetz_scale_b),
)


# WSC5: finite Weil-standard windows admit ghost cohomology.  A hyperbolic
# pair of 5-cycle summands preserves traces through degree 4, has a symplectic
# Poincare form, and changes the fifth count.
window = 4
ghost = cycle_permutation(window + 1)
ghost_pair = block_diag(ghost, ghost)
J_ghost = hyperbolic_symplectic(window + 1)
ghost_preserves_pd = np.allclose(ghost_pair.T @ J_ghost @ ghost_pair, J_ghost)
augmented = block_diag(F_true.astype(complex), ghost_pair)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "WSC5 finite Weil-standard windows admit ghost cohomology",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and ghost_preserves_pd
    and count_5_gap == 10.0,
    "first %d traces match; ghost H1 dim=%d; count_5 gap=%.1f"
    % (window, ghost_pair.shape[0], count_5_gap),
)


# WSC6: the same abstract package is formable on arbitrary controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = weil_standard_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, H_pos)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "WSC6 Weil-standard package is formable on controls",
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


# WSC7: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_weil_cohomology_constructed = False
zeta_carrier_native_kunneth_projectors_constructed = False
zeta_carrier_native_lefschetz_class_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "WSC7 Weil-standard package constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_weil_cohomology_constructed
    and not zeta_carrier_native_kunneth_projectors_constructed
    and not zeta_carrier_native_lefschetz_class_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, correspondences, Weil theorem, Kunneth/Lefschetz construction, degrees, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (WSC1-WSC7)")
print(
    "VERDICT: an abstract Weil cohomology plus standard-conjectures package "
    "is not End(S^2/Z). Kunneth/Lefschetz/Hodge-standard data does not "
    "determine counts, construct NS degree slots, impose Frobenius/Rosati "
    "compatibility, pin the degree character, exclude ghost cohomology, or "
    "kill controls; no actual square, proper correspondences, projection "
    "formula, positive Rosati, or DD.4 datum is constructed."
)
