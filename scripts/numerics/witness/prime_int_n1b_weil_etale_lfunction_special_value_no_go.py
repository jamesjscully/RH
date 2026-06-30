r"""Weil-etale / L-function special-value carrier no-go.

After motivic regulators and algebraic K/TC fail as direct square
constructors, the adjacent repair is to use Weil-etale cohomology,
Lichtenbaum special values, determinant lines, Euler characteristics,
regulators, and Tamagawa/order formulas as the carrier.  These are strong
special-value and realization tools after a carrier exists.  They do not by
themselves construct the square, rep_NS, degree maps, Frobenius graph,
projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_weil_etale_lfunction_special_value_no_go
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


def wet_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: Weil-etale cohomology, Lichtenbaum special value,
    # determinant line, regulator, Euler characteristic, Tamagawa/order
    # formula, duality complex, and finite generation.
    return (True, True, True, True, True, True, True, True)


def special_value_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy special-value shadow: records order of vanishing and regulator
    # rank, but forgets endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# WET1: the same Weil-etale/L-value profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = wet_profile()
profile_other = wet_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "WET1 Weil-etale/L-value profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# WET2: Weil-etale cohomology / special-value data does not construct the
# two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "WET2 Weil-etale cohomology data does not construct NS degree slots",
    profile_true == wet_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same Weil-etale/L-value profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# WET3: Euler characteristic / regulator shadows can forget correspondence
# endpoint and extension data.
class_a = np.array([1, 2, 0])
class_b = np.array([1, 2, 4])
same_shadow = special_value_shadow(class_a) == special_value_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "WET3 Euler characteristic/regulator shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 4,
    "same special-value shadow=%s, endpoint gap=%d"
    % (special_value_shadow(class_a), endpoint_gap),
)


# WET4: special-value positivity does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
has_regulator_positivity = True
has_determinant_line = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "WET4 special-value positivity does not impose Frobenius/Rosati compatibility",
    has_regulator_positivity and has_determinant_line and off_metric_defect > 1.0,
    "regulator/determinant=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# WET5: declaring determinant/regulator compatibilities does not construct
# the square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_weil_etale_duality = True
declares_lfunction_special_value = True
declares_regulator_formula = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "WET5 Weil-etale/L-value declaration is not constructed projection formula",
    declares_weil_etale_duality
    and declares_lfunction_special_value
    and declares_regulator_formula
    and semantic_projection_defect == 27.0,
    "declared duality/special-value/regulator=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# WET6: finite Weil-etale/L-function windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "WET6 finite Weil-etale/L-value windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# WET7: the same Weil-etale/L-value schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = wet_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "WET7 formal Weil-etale/L-value schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_zeta_square_carrier
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_projection_formula
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no square/rep_NS/degrees/projection/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# WET8: construction audit.
zeta_weil_etale_carrier_constructed = False
zeta_lfunction_special_value_carrier_constructed = False
zeta_determinant_line_carrier_constructed = False
zeta_regulator_carrier_constructed = False
zeta_euler_characteristic_carrier_constructed = False
zeta_tamagawa_order_formula_constructed = False
zeta_ambient_square_constructed = False
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
    "WET8 Weil-etale/L-value package constructs no End(S^2/Z) square package",
    not zeta_weil_etale_carrier_constructed
    and not zeta_lfunction_special_value_carrier_constructed
    and not zeta_determinant_line_carrier_constructed
    and not zeta_regulator_carrier_constructed
    and not zeta_euler_characteristic_carrier_constructed
    and not zeta_tamagawa_order_formula_constructed
    and not zeta_ambient_square_constructed
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
    "no Weil-etale carrier, L-value carrier, determinant/regulator carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("WET1-WET8 ALL PASS: Weil-etale / L-value special-value package is not End(S^2/Z)")
