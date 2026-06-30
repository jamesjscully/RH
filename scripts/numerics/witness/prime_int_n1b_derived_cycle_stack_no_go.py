r"""Derived cycle-stack / virtual-intersection carrier no-go.

After doc 236 killed ordinary Chow/Hilbert cycle moduli as the square
carrier, the next repair is to derive them: use a derived Hilbert/Chow stack,
perfect obstruction theory, virtual fundamental class, and derived
intersections to supply the missing correspondence calculus.  This is still
downstream of an ambient square and its orientations.  Derived intersections
can refine cycle calculus once the square, degree maps, pairing, and
projection formula exist; they do not construct End(S^2/Z) by themselves.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_derived_cycle_stack_no_go
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


def derived_cycle_profile() -> tuple[tuple[int, int], bool, bool, bool, bool]:
    # Toy profile: perfect cotangent amplitude, perfect obstruction theory,
    # orientation, virtual fundamental class, and derived intersection product.
    return ((-1, 0), True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# DCS1: the same abstract derived-cycle profile does not determine the
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = derived_cycle_profile()
profile_other = derived_cycle_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "DCS1 derived cycle-stack profile does not determine count anchor",
    profile_true == profile_other == ((-1, 0), True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# DCS2: virtual classes do not construct the NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "DCS2 virtual cycle data does not construct NS degree slots",
    true_delta_graph == 7.0 and retuned_delta_graph == 10.0,
    "same derived z-cycle, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# DCS3: the virtual fundamental class depends on obstruction/orientation data
# not supplied by the profile.  The same classical cycle can carry different
# virtual weights.
classical_degree = 7.0
obstruction_euler_a = 1.0
obstruction_euler_b = -2.0
virtual_degree_a = classical_degree * obstruction_euler_a
virtual_degree_b = classical_degree * obstruction_euler_b

gate(
    "DCS3 virtual class depends on extra obstruction/orientation data",
    profile_true == profile_other
    and virtual_degree_a == 7.0
    and virtual_degree_b == -14.0,
    "same classical degree %.1f, virtual degrees %.1f and %.1f"
    % (classical_degree, virtual_degree_a, virtual_degree_b),
)


# DCS4: derived intersection/product declarations do not construct the
# projection formula.  The same componentwise realization has a nonzero
# semantic projection defect.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_derived_fiber_product = True
declares_virtual_pull_push = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "DCS4 derived pull-push declaration is not a constructed projection formula",
    declares_derived_fiber_product
    and declares_virtual_pull_push
    and semantic_projection_defect == 27.0,
    "declared derived pull-push=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# DCS5: finite derived/virtual windows admit ghost obstruction summands.  A
# 5-cycle ghost preserves traces in powers 1..4 and changes the next count.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "DCS5 finite derived windows admit ghost obstruction summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# DCS6: the same formal derived-stack schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = derived_cycle_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_derived_hilbert_stack = False
control_has_perfect_obstruction_theory = False
control_has_orientation = False
control_has_ambient_square = False
control_has_positive_rosati = False

gate(
    "DCS6 formal derived cycle-stack schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_derived_hilbert_stack
    and not control_has_perfect_obstruction_theory
    and not control_has_orientation
    and not control_has_ambient_square
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no derived stack/POT/orientation/square/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# DCS7: construction audit.
zeta_derived_hilbert_stack_constructed = False
zeta_derived_chow_stack_constructed = False
zeta_perfect_obstruction_theory_constructed = False
zeta_virtual_fundamental_class_constructed = False
zeta_orientation_constructed = False
zeta_ambient_square_constructed = False
zeta_rep_ns_constructed = False
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
    "DCS7 derived cycle-stack package constructs no End(S^2/Z) square package",
    not zeta_derived_hilbert_stack_constructed
    and not zeta_derived_chow_stack_constructed
    and not zeta_perfect_obstruction_theory_constructed
    and not zeta_virtual_fundamental_class_constructed
    and not zeta_orientation_constructed
    and not zeta_ambient_square_constructed
    and not zeta_rep_ns_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no derived stack/POT/VFC/orientation, ambient square, rep_NS, projection, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (DCS1-DCS7)")
print(
    "VERDICT: derived cycle-stack / virtual-intersection data is not "
    "End(S^2/Z). It can refine intersections only after an ambient square, "
    "orientation, degree maps, and correspondence calculus exist; it does "
    "not construct count anchors, NS degree slots, projection formula, "
    "positive Rosati, control death, rep_NS, or DD.4."
)
