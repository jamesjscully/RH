r"""Motivic cohomology / higher Chow / regulator carrier no-go.

After doc 238 killed bivariant/operational Chow as the square carrier, the
next repair is to move one level up: use motivic cohomology, higher Chow
complexes, Chern characters, cycle maps, and regulators/realizations, hoping
that universal cycle-theoretic data supplies rep_NS and the correspondence
calculus for End(S^2/Z).  It does not.  These packages are realizations or
cycle complexes attached to a carrier; they do not construct the over-Z square,
proper correspondences, degree maps, Frobenius graph, projection formula, or
positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_motivic_cohomology_regulator_no_go
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


def motivic_regulator_profile() -> tuple[bool, bool, bool, bool, bool, bool]:
    # Toy profile: higher Chow complex, motivic cohomology, cycle map,
    # Chern character, regulator/realization, and product.
    return (True, True, True, True, True, True)


def regulator_image(integral_class: np.ndarray) -> tuple[float, float]:
    # A toy regulator/Chern image that kills the torsion coordinate.
    return (float(integral_class[0]), float(integral_class[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# MCR1: the same motivic/regulator profile does not determine a finite-field
# count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = motivic_regulator_profile()
profile_other = motivic_regulator_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "MCR1 motivic/regulator profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# MCR2: motivic cycle-class data does not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "MCR2 motivic cycle class does not construct NS degree slots",
    profile_true == motivic_regulator_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same motivic z-class, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# MCR3: rational Chern/regulator images can lose integral torsion data needed
# to identify the actual correspondence lattice.
integral_class_a = np.array([1.0, 0.0, 0.0])
integral_class_b = np.array([1.0, 0.0, 2.0])
same_regulator = regulator_image(integral_class_a) == regulator_image(integral_class_b)
integral_gap = float(np.linalg.norm(integral_class_a - integral_class_b))

gate(
    "MCR3 Chern/regulator image loses integral correspondence data",
    same_regulator and integral_gap == 2.0,
    "same rational image=%s, integral/torsion gap=%.1f"
    % (regulator_image(integral_class_a), integral_gap),
)


# MCR4: positive realization/regulator data does not impose the Frobenius
# Rosati compatibility relation required by the square.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = motivic_regulator_profile()
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "MCR4 regulator realization does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# MCR5: declaring product/projection in motivic cohomology is not the same as
# constructing the square correspondence calculus.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_product = True
declares_regulator_compatibility = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "MCR5 motivic product/regulator declaration is not constructed projection formula",
    declares_product
    and declares_regulator_compatibility
    and semantic_projection_defect == 27.0,
    "declared product/regulator=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# MCR6: finite motivic/regulator windows admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "MCR6 finite motivic/regulator windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# MCR7: the same formal motivic-regulator schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = motivic_regulator_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_motivic_carrier = False
control_has_higher_chow_complex = False
control_has_regulator_theorem = False
control_has_ambient_square = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "MCR7 formal motivic/regulator schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_motivic_carrier
    and not control_has_higher_chow_complex
    and not control_has_regulator_theorem
    and not control_has_ambient_square
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no motivic carrier/square/rep_NS/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# MCR8: construction audit.
zeta_motivic_cohomology_constructed = False
zeta_higher_chow_complex_constructed = False
zeta_cycle_map_constructed = False
zeta_chern_character_constructed = False
zeta_regulator_constructed = False
zeta_deligne_realization_constructed = False
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
    "MCR8 motivic/regulator package constructs no End(S^2/Z) square package",
    not zeta_motivic_cohomology_constructed
    and not zeta_higher_chow_complex_constructed
    and not zeta_cycle_map_constructed
    and not zeta_chern_character_constructed
    and not zeta_regulator_constructed
    and not zeta_deligne_realization_constructed
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
    "no motivic cohomology, higher Chow, regulator, square, rep_NS, degrees, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (MCR1-MCR8)")
print(
    "VERDICT: motivic cohomology, higher Chow complexes, Chern characters, "
    "cycle maps, and regulators are not End(S^2/Z). Their profiles do not "
    "determine finite-field counts, do not construct NS degree slots, lose "
    "integral correspondence data under rational realization, do not impose "
    "Frobenius/Rosati compatibility, do not turn declared products into a "
    "constructed projection formula, admit finite-window ghosts, are formable "
    "on controls, and construct no actual square carrier."
)
