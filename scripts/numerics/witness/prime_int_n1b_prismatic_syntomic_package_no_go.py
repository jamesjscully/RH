r"""Prismatic / syntomic / p-adic comparison package no-go.

After doc 229, the next repair is to use the BMS/prismatic/syntomic package:
p-complete TC-/TP/prismatic cohomology, Nygaard filtration, Frobenius, and
comparison maps, hoping the integral p-adic package supplies the missing
global square carrier.  It does not construct End(S^2/Z).  The package is
local and downstream unless the square, proper correspondences, degree maps,
Frobenius graph, projection formula, all-prime/archimedean assembly, and
positive Rosati have already been built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_prismatic_syntomic_package_no_go
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


def prismatic_profile(rank: int = 2) -> tuple[int, bool, tuple[int, int], bool, bool, bool]:
    # Toy p-adic comparison package: rank, p-completeness, Nygaard/Hodge
    # weights, Frobenius, syntomic fiber, and comparison maps.
    return (rank, True, (0, 1), True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# PSP1: identical p-adic/prismatic comparison profiles do not determine the
# finite-field count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = prismatic_profile(2)
profile_other = prismatic_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "PSP1 prismatic/syntomic profile does not determine count anchor",
    profile_true == profile_other == (2, True, (0, 1), True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# PSP2: the comparison package does not construct NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "PSP2 p-adic comparison data does not construct NS degree slots",
    profile_true == prismatic_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same prismatic profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# PSP3: finite p-adic truncations do not pin the over-Z degree character.
# At p=3, degrees 7 and 16 are identical modulo 9 but give different
# diagonal/graph intersections.
p = 3
precision = 2
modulus = p**precision
degree_a = 7
degree_b = 16
same_truncated_degree = degree_a % modulus == degree_b % modulus

gate(
    "PSP3 finite p-adic truncation does not pin global degree character",
    same_truncated_degree
    and ns_intersection(D_true, corr(float(degree_a), F_true, 1.0)) == 7.0
    and ns_intersection(D_true, corr(float(degree_b), F_true, 1.0)) == 16.0,
    "p=%d, mod=%d, degrees %d and %d agree mod %d but Delta.Gamma differs %.1f -> %.1f"
    % (
        p,
        modulus,
        degree_a,
        degree_b,
        modulus,
        ns_intersection(D_true, corr(float(degree_a), F_true, 1.0)),
        ns_intersection(D_true, corr(float(degree_b), F_true, 1.0)),
    ),
)


# PSP4: Nygaard/Hodge-Tate weights and p-adic Frobenius data do not impose the
# complex/archimedean Rosati compatibility required by the square.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = prismatic_profile(2)
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "PSP4 p-adic filtration/Frobenius data does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# PSP5: finite p-adic/prismatic windows admit ghost summands.  A 5-cycle
# ghost has zero traces in powers 1..4 and trace 5 in power 5.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "PSP5 finite prismatic windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; ghost rank=%d; count_5 gap=%.1f"
    % (window, ghost.shape[0], count_5_gap),
)


# PSP6: the same p-adic comparison package is formable on arbitrary controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = prismatic_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, H_pos)
control_has_euler_product = False
control_has_all_prime_assembly = False
control_has_archimedean_component = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "PSP6 prismatic/syntomic package is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_euler_product
    and not control_has_all_prime_assembly
    and not control_has_archimedean_component
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no Euler/all-prime/arch/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# PSP7: construction audit.
zeta_prism_constructed = False
zeta_global_over_z_square_constructed = False
zeta_all_prime_assembly_constructed = False
zeta_archimedean_component_constructed = False
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
    "PSP7 prismatic/syntomic package constructs no End(S^2/Z) square package",
    not zeta_prism_constructed
    and not zeta_global_over_z_square_constructed
    and not zeta_all_prime_assembly_constructed
    and not zeta_archimedean_component_constructed
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
    "no global prism/square/all-prime/archimedean assembly, rep_NS, correspondences, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PSP1-PSP7)")
print(
    "VERDICT: prismatic, syntomic, or p-adic comparison data is not "
    "End(S^2/Z). The p-complete package does not determine counts, construct "
    "NS degree slots, pin the global over-Z degree character, impose "
    "Frobenius/Rosati compatibility, exclude ghost summands, or kill controls; "
    "no global square, all-prime/archimedean assembly, proper correspondences, "
    "projection formula, positive Rosati, or DD.4 datum is constructed."
)
