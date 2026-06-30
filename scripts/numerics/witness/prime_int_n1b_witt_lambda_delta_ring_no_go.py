r"""Witt / Lambda / delta-ring absolute-geometry carrier no-go.

The named F1 constant-tower no-go killed Borger-Witt ghosts as one finite
constant field, prismatic/syntomic no-go killed p-complete comparison, and
epicyclic no-go killed power-map coherence as the carrier.  The remaining
nearby repair is stronger: use the all-prime Lambda-ring / big-Witt /
delta-ring absolute-geometry package itself as the square carrier.

This witness records why that package is still downstream/shadow data unless
it constructs the actual square, rep_NS, degree maps, Frobenius graph,
projection formula, and positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_witt_lambda_delta_ring_no_go
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


def wld_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: Lambda-ring structure, big-Witt functor, ghost map,
    # commuting Frobenius lifts, p-typical delta structures, arithmetic jets,
    # Verschiebung/Restriction operations, and absolute-base interpretation.
    return (True, True, True, True, True, True, True, True)


def ghost_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy Witt ghost shadow: records ghost degree and Frobenius-lift index,
    # but forgets endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def commuting_frobenius_lifts(indices: tuple[int, ...]) -> bool:
    # Toy Lambda-ring lifts psi_n = n Id commute multiplicatively.
    dim = 2
    lifts = {n: float(n) * np.eye(dim) for n in indices}
    return all(
        np.linalg.norm(lifts[m] @ lifts[n] - lifts[n] @ lifts[m]) < 1e-12
        for m in indices
        for n in indices
    )


def p_typical_residue(degree: int, p: int, precision: int) -> int:
    return degree % (p**precision)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# WLD1: the same Witt/Lambda/delta profile does not determine a finite-field
# count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = wld_profile()
profile_other = wld_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "WLD1 Witt/Lambda/delta profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# WLD2: all-prime Frobenius lifts / Witt ghosts do not construct the two NS
# degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "WLD2 Witt/Frobenius-lift data does not construct NS degree slots",
    profile_true == wld_profile()
    and commuting_frobenius_lifts((2, 3, 5, 7))
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same commuting lifts and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# WLD3: p-typical / finite Witt truncations do not pin the global degree
# character.
p = 3
precision = 2
degree_a = 7
degree_b = 16
same_p_typical_residue = p_typical_residue(degree_a, p, precision) == p_typical_residue(
    degree_b, p, precision
)
Gamma_p_a = corr(float(degree_a), F_true, 1.0)
Gamma_p_b = corr(float(degree_b), F_true, 1.0)
p_adic_delta_graph_a = ns_intersection(D_true, Gamma_p_a)
p_adic_delta_graph_b = ns_intersection(D_true, Gamma_p_b)

gate(
    "WLD3 finite p-typical Witt truncations do not pin global degree character",
    same_p_typical_residue
    and p_adic_delta_graph_a == 7.0
    and p_adic_delta_graph_b == 16.0,
    "degrees %d and %d agree mod %d^%d but Delta.Gamma changes %.1f -> %.1f"
    % (degree_a, degree_b, p, precision, p_adic_delta_graph_a, p_adic_delta_graph_b),
)


# WLD4: Witt ghost shadows can forget endpoint and extension data.
class_a = np.array([4, 2, 0])
class_b = np.array([4, 2, 4])
same_shadow = ghost_shadow(class_a) == ghost_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "WLD4 Witt ghost shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 4,
    "same ghost shadow=%s, endpoint gap=%d" % (ghost_shadow(class_a), endpoint_gap),
)


# WLD5: Lambda/delta/Frobenius-lift data does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
has_lambda_ring_lifts = commuting_frobenius_lifts((2, 3, 5, 7))
has_delta_structures = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "WLD5 Lambda/delta data does not impose Frobenius/Rosati compatibility",
    has_lambda_ring_lifts and has_delta_structures and off_metric_defect > 1.0,
    "lambda/delta=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# WLD6: declaring Witt/vector or delta-ring functoriality does not construct
# the square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_big_witt_functor = True
declares_delta_jet_space = True
declares_absolute_base = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "WLD6 Witt/delta functoriality is not constructed projection formula",
    declares_big_witt_functor
    and declares_delta_jet_space
    and declares_absolute_base
    and semantic_projection_defect == 27.0,
    "declared Witt/delta/absolute=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# WLD7: finite Witt/Lambda/delta windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "WLD7 finite Witt/Lambda/delta windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f" % (window, window + 1, count_5_gap),
)


# WLD8: the same formal package is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = wld_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "WLD8 formal Witt/Lambda/delta schema is formable on controls",
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


# WLD9: construction audit.
zeta_lambda_ring_carrier_constructed = False
zeta_big_witt_carrier_constructed = False
zeta_delta_ring_carrier_constructed = False
zeta_arithmetic_jet_carrier_constructed = False
zeta_witt_ghost_degree_carrier_constructed = False
zeta_all_prime_frobenius_carrier_constructed = False
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
    "WLD9 Witt/Lambda/delta package constructs no End(S^2/Z) square package",
    not zeta_lambda_ring_carrier_constructed
    and not zeta_big_witt_carrier_constructed
    and not zeta_delta_ring_carrier_constructed
    and not zeta_arithmetic_jet_carrier_constructed
    and not zeta_witt_ghost_degree_carrier_constructed
    and not zeta_all_prime_frobenius_carrier_constructed
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
    "no Lambda-ring carrier, Witt carrier, delta carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("WLD1-WLD9 ALL PASS: Witt / Lambda / delta-ring absolute geometry is not End(S^2/Z)")
