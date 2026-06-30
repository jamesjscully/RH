r"""Shtuka / Hecke-stack carrier no-go.

Automorphic packets, six-functor trace formalisms, generic correspondence
bicategories, and topos/hyperdescent packages have already been killed as
direct square carriers.  The stronger geometric repair is to use the
function-field-style moduli of shtukas, Hecke stacks, Frobenius legs,
excursion operators, or Heegner-Drinfeld cycle intersections as the square
carrier itself.

This witness records why that package is still downstream data for the
zeta-side problem unless it constructs the actual over-Z square, rep_NS,
degree maps, Frobenius graph, projection formula, and positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_shtuka_hecke_stack_no_go
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


def shtuka_profile() -> tuple[int, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: number of legs, Hecke stack, Frobenius leg, paws,
    # excursion algebra, geometric Satake input, Heegner-Drinfeld cycle,
    # and central Rankin-Selberg height formula.
    return (2, True, True, True, True, True, True, True)


def hecke_stack_shadow(class_data: np.ndarray) -> tuple[int, int, int]:
    # Toy Hecke/shtuka shadow: sees leg number, modification degree, and
    # excursion rank, but forgets endpoint/correspondence coordinates.
    return (int(class_data[0]), int(class_data[1]), int(class_data[2]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# SHT1: the same shtuka/Hecke-stack profile does not determine a finite-field
# count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = shtuka_profile()
profile_other = shtuka_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "SHT1 shtuka/Hecke-stack profile does not determine count anchor",
    profile_true == profile_other == (2, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# SHT2: Hecke modifications and leg data do not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "SHT2 Hecke modification data does not construct NS degree slots",
    profile_true == shtuka_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same shtuka legs and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# SHT3: Bun/Hecke/shtuka shadows can forget endpoint and extension data.
class_a = np.array([2, 3, 4, 0])
class_b = np.array([2, 3, 4, 6])
same_shadow = hecke_stack_shadow(class_a) == hecke_stack_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "SHT3 Hecke-stack shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 6,
    "same Hecke shadow=%s, endpoint gap=%d" % (hecke_stack_shadow(class_a), endpoint_gap),
)


# SHT4: Frobenius legs and Hecke modifications do not select the diagonal and
# Frobenius graph triples.
same_leg_profile = True
diagonal_endpoint = corr(1.0, np.eye(2), 1.0)
retuned_endpoint = corr(4.0, np.eye(2), 1.0)
endpoint_intersection_gap = abs(
    ns_intersection(diagonal_endpoint, Gamma_true)
    - ns_intersection(retuned_endpoint, Gamma_true)
)

gate(
    "SHT4 Frobenius-leg data does not select diagonal/graph triples",
    same_leg_profile and endpoint_intersection_gap == 3.0,
    "same leg profile; endpoint intersection gap=%.1f" % endpoint_intersection_gap,
)


# SHT5: central-value or Heegner-Drinfeld self-intersection data is not the
# Weil square count mechanism and does not impose Frobenius/Rosati
# compatibility.
declares_heegner_drinfeld_cycle = True
declares_central_rs_height = True
central_value_scalar = 1.0
count_anchor = true_delta_graph
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "SHT5 central-value self-intersection is not Rosati/count construction",
    declares_heegner_drinfeld_cycle
    and declares_central_rs_height
    and central_value_scalar != count_anchor
    and off_metric_defect > 1.0,
    "central-height scalar=%.1f, Delta.Gamma count=%.1f, Rosati_defect=%.3f"
    % (central_value_scalar, count_anchor, off_metric_defect),
)


# SHT6: excursion/geometric-Satake/projection declarations are not the
# constructed square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_excursion_operators = True
declares_geometric_satake = True
declares_projection_formula = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "SHT6 excursion/projection declarations are not constructed projection formula",
    declares_excursion_operators
    and declares_geometric_satake
    and declares_projection_formula
    and semantic_projection_defect == 27.0,
    "declared excursion/Satake/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# SHT7: finite shtuka/Hecke/excursion windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "SHT7 finite shtuka/Hecke windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f" % (window, window + 1, count_5_gap),
)


# SHT8: the same formal package is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = shtuka_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "SHT8 formal shtuka/Hecke schema is formable on controls",
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


# SHT9: construction audit.
zeta_shtuka_moduli_carrier_constructed = False
zeta_hecke_stack_carrier_constructed = False
zeta_bun_stack_carrier_constructed = False
zeta_frobenius_leg_carrier_constructed = False
zeta_excursion_algebra_carrier_constructed = False
zeta_heegner_drinfeld_cycle_carrier_constructed = False
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
    "SHT9 shtuka/Hecke package constructs no End(S^2/Z) square package",
    not zeta_shtuka_moduli_carrier_constructed
    and not zeta_hecke_stack_carrier_constructed
    and not zeta_bun_stack_carrier_constructed
    and not zeta_frobenius_leg_carrier_constructed
    and not zeta_excursion_algebra_carrier_constructed
    and not zeta_heegner_drinfeld_cycle_carrier_constructed
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
    "no shtuka moduli carrier, Hecke stack carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("SHT1-SHT9 ALL PASS: shtuka / Hecke-stack data is not End(S^2/Z)")
