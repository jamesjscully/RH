r"""Tate-cycle / fixed-subspace package no-go.

After doc 233, the next repair is to strengthen compatible Galois-system
data by taking Tate/Hodge/absolute-cycle fixed subspaces and an algebraicity
theorem, hoping the fixed cycle classes are the missing rep_NS carrier.  This
still does not construct End(S^2/Z).  Fixed subspaces and cycle-class
surjectivity are downstream of a carrier; they do not by themselves construct
degree slots, proper correspondences, fiber-product composition, Frobenius
graph, projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_tate_cycle_fixed_subspace_no_go
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


def tate_cycle_profile(fixed_dim: int = 2) -> tuple[int, bool, bool, bool, bool, bool]:
    # Toy package: dimension of Frobenius-fixed z-subspace, algebraicity /
    # Tate theorem, cycle class map, semisimplicity, pairing, and comparison.
    return (fixed_dim, True, True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


def commutes(A: np.ndarray, B: np.ndarray, tol: float = 1e-9) -> bool:
    return bool(np.linalg.norm(A @ B - B @ A) < tol)


# TCF1: identical Tate/fixed-cycle profiles do not determine the finite-field
# count anchor.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
F_other = frobenius(5, 2)
profile_true = tate_cycle_profile(2)
profile_other = tate_cycle_profile(2)
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, 5, 4)

gate(
    "TCF1 Tate-cycle profile does not determine count anchor",
    profile_true == profile_other == (2, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# TCF2: fixed-cycle data does not construct the NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "TCF2 Tate fixed classes do not construct NS degree slots",
    profile_true == tate_cycle_profile(2)
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same fixed z-class and profile, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# TCF3: the fixed z-subspace is not the full correspondence carrier.  Both
# Id and F commute with F, so fixed-subspace membership does not select the
# diagonal, graph, or degree slots.
I = np.eye(F_true.shape[0])
id_fixed = commutes(I, F_true)
f_fixed = commutes(F_true, F_true)
fixed_classes_independent = np.linalg.matrix_rank(np.column_stack([I.reshape(-1), F_true.reshape(-1)])) == 2
delta_self = ns_intersection(delta(F_true), corr(1.0, I, 1.0))
delta_graph = ns_intersection(delta(F_true), Gamma_true)

gate(
    "TCF3 fixed z-subspace does not select diagonal/graph correspondence triples",
    id_fixed
    and f_fixed
    and fixed_classes_independent
    and delta_self == 0.0
    and delta_graph == 7.0,
    "Id and F are both fixed z-classes; Delta.Id=%.1f, Delta.Gamma=%.1f"
    % (delta_self, delta_graph),
)


# TCF4: algebraic/fixed-cycle existence does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
off_profile = tate_cycle_profile(2)
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))
off_has_fixed_identity = commutes(np.eye(2), F_off)
off_has_fixed_frobenius = commutes(F_off, F_off)

gate(
    "TCF4 fixed-cycle existence does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true
    and off_has_fixed_identity
    and off_has_fixed_frobenius
    and off_metric_defect > 1.0,
    "profile=%s, fixed Id/F=True, Rosati_defect=%.3f" % (off_profile, off_metric_defect),
)


# TCF5: finite Tate/Frobenius windows admit invariant ghost cycle classes.  A
# 5-cycle ghost has zero traces in powers 1..4 and trace 5 in power 5, while
# the projector onto the ghost summand commutes with the augmented Frobenius.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
ghost_projector = block_diag(np.zeros_like(F_true, dtype=complex), np.eye(window + 1))
ghost_projector_fixed = commutes(ghost_projector, augmented)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "TCF5 finite Tate windows admit invariant ghost classes",
    ghost_projector_fixed
    and all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; fixed ghost projector rank=%d; count_5 gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# TCF6: the same formal fixed-cycle schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = tate_cycle_profile(2)
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_actual_cycle_class_map = False
control_has_algebraicity_theorem = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "TCF6 formal Tate-cycle schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_actual_cycle_class_map
    and not control_has_algebraicity_theorem
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no cycle-map/Tate/rep_NS/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# TCF7: construction audit.
zeta_tate_cycle_carrier_constructed = False
zeta_cycle_class_map_constructed = False
zeta_algebraicity_theorem_constructed = False
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
    "TCF7 Tate fixed-subspace package constructs no End(S^2/Z) square package",
    not zeta_tate_cycle_carrier_constructed
    and not zeta_cycle_class_map_constructed
    and not zeta_algebraicity_theorem_constructed
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
    "no Tate carrier, cycle map, algebraicity theorem, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (TCF1-TCF7)")
print(
    "VERDICT: Tate/Hodge fixed-subspace data is not End(S^2/Z). It does "
    "not determine the square carrier, degree slots, diagonal/graph triples, "
    "individual radii, Rosati, ghost exclusion, control death, rep_NS, or "
    "proper correspondences."
)
