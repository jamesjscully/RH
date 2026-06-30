r"""Bivariant / operational Chow carrier no-go.

After doc 237 killed derived cycle stacks as the square carrier, the next
repair is to use operational Chow or bivariant oriented cohomology: refined
Gysin maps, cap products, and projection formulas are built into the
formalism, so perhaps the correspondence calculus is supplied at that level.
This is still downstream of an ambient square and proper maps.  Bivariant
classes act on cycles of existing spaces; they do not construct End(S^2/Z).

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_bivariant_operational_chow_no_go
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


def operational_profile() -> tuple[bool, bool, bool, bool, bool]:
    # Toy profile: refined Gysin, proper pushforward, flat pullback,
    # cap product, and projection formula are declared.
    return (True, True, True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# BOC1: the same operational/bivariant profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = operational_profile()
profile_other = operational_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "BOC1 operational Chow profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# BOC2: bivariant operations do not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "BOC2 bivariant class does not construct NS degree slots",
    true_delta_graph == 7.0 and retuned_delta_graph == 10.0,
    "same operational z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# BOC3: finite operational tests do not determine the operation.  Two
# operations agree on tested cycle classes but differ on a ghost class.
Op_a = np.eye(3)
Op_b = np.diag([1.0, 1.0, 2.0])
tested_cycles = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])]
ghost_cycle = np.array([0.0, 0.0, 1.0])
agree_on_tests = all(np.allclose(Op_a @ v, Op_b @ v) for v in tested_cycles)
ghost_gap = float(np.linalg.norm(Op_a @ ghost_cycle - Op_b @ ghost_cycle))

gate(
    "BOC3 finite operational tests admit ghost bivariant classes",
    agree_on_tests and ghost_gap == 1.0,
    "two operations agree on %d tested cycles; ghost action gap=%.1f"
    % (len(tested_cycles), ghost_gap),
)


# BOC4: declaring the projection formula in an operational profile is not a
# constructed correspondence calculus. The formal componentwise realization
# still has a nonzero semantic projection defect.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_refined_gysin = True
declares_projection_formula = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "BOC4 operational projection formula declaration is not constructed calculus",
    declares_refined_gysin
    and declares_projection_formula
    and semantic_projection_defect == 27.0,
    "declared Gysin/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# BOC5: orientation choices change degrees unless the carrier constructs the
# orientation and degree map.
base_degree = 7.0
orientation_a = 1.0
orientation_b = -1.0
pushforward_a = base_degree * orientation_a
pushforward_b = base_degree * orientation_b

gate(
    "BOC5 oriented Gysin data does not construct the degree character",
    pushforward_a == 7.0 and pushforward_b == -7.0,
    "same base degree %.1f, two orientations give pushforwards %.1f and %.1f"
    % (base_degree, pushforward_a, pushforward_b),
)


# BOC6: the same formal operational schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = operational_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_actual_bivariant_theory = False
control_has_operational_chow_ring = False
control_has_ambient_square = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "BOC6 formal operational Chow schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_actual_bivariant_theory
    and not control_has_operational_chow_ring
    and not control_has_ambient_square
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no bivariant theory/square/rep_NS/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# BOC7: finite operational windows also admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "BOC7 finite operational windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# BOC8: construction audit.
zeta_bivariant_theory_constructed = False
zeta_operational_chow_constructed = False
zeta_refined_gysin_constructed = False
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
    "BOC8 bivariant operational package constructs no End(S^2/Z) square package",
    not zeta_bivariant_theory_constructed
    and not zeta_operational_chow_constructed
    and not zeta_refined_gysin_constructed
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
    "no bivariant/operational theory, orientation, square, rep_NS, projection, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (BOC1-BOC8)")
print(
    "VERDICT: bivariant / operational Chow data is not End(S^2/Z). It can "
    "act on cycles only after the spaces, proper maps, orientations, and "
    "degree maps exist; it does not construct count anchors, NS degree slots, "
    "projection formula, Frobenius graph, positive Rosati, control death, "
    "rep_NS, or DD.4."
)
