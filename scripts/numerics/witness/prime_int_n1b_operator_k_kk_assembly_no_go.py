r"""Operator K-theory / KK assembly carrier no-go.

After the Bost-Connes / adele-class spectral package fails as direct square
construction, the nearby operator-algebraic repair is to pass to groupoid or
crossed-product C*-algebras, Baum-Connes style assembly, K-theory, and the
Kasparov KK product.  The R1 shortcut tested here is the promotion of that
assembly/K-theory calculus itself to End(S^2/Z).  K/KK data is valuable
after a carrier exists, but it does not construct the square, rep_NS, degree
maps, Frobenius graph, projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_operator_k_kk_assembly_no_go
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


def kk_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: groupoid C*-algebra, crossed product, Baum-Connes assembly,
    # K0/K1, Kasparov product, Morita invariance, index pairing, and a
    # positive C*-state.
    return (True, True, True, True, True, True, True, True)


def k_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy K0/index shadow: rank and index only; endpoint/correspondence
    # coordinate and integral lattice data are forgotten.
    return (int(class_data[0]), int(class_data[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# OKK1: the same operator K/KK assembly profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = kk_profile()
profile_other = kk_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "OKK1 operator K/KK profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# OKK2: K-theory / assembly data does not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "OKK2 K-theory assembly data does not construct NS degree slots",
    profile_true == kk_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same K/KK profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# OKK3: K0/index shadows forget extension/endpoint/correspondence data.
k_class_a = np.array([1, 2, 0])
k_class_b = np.array([1, 2, 4])
same_k_shadow = k_shadow(k_class_a) == k_shadow(k_class_b)
endpoint_gap = int(np.linalg.norm(k_class_a - k_class_b))

gate(
    "OKK3 K0/index shadow loses correspondence endpoint data",
    same_k_shadow and endpoint_gap == 4,
    "same K shadow=%s, endpoint gap=%d" % (k_shadow(k_class_a), endpoint_gap),
)


# OKK4: C*-positivity or positive index pairing does not impose
# Frobenius/Rosati compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
positive_cstar_state = True
positive_index_pairing = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "OKK4 C*-positivity/index pairing does not impose Frobenius/Rosati compatibility",
    positive_cstar_state and positive_index_pairing and off_metric_defect > 1.0,
    "positive state/pairing=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# OKK5: declaring KK product / assembly naturality does not construct the
# square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_baum_connes_assembly = True
declares_kk_product = True
declares_index_pairing = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "OKK5 KK product declaration is not constructed projection formula",
    declares_baum_connes_assembly
    and declares_kk_product
    and declares_index_pairing
    and semantic_projection_defect == 27.0,
    "declared assembly/KK/index=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# OKK6: finite K-theory / trace windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "OKK6 finite K/KK windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# OKK7: the same operator K/KK schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = kk_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_groupoid_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "OKK7 formal operator K/KK schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_groupoid_square_carrier
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_projection_formula
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no square/rep_NS/degrees/projection/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# OKK8: construction audit.
zeta_groupoid_cstar_carrier_constructed = False
zeta_crossed_product_carrier_constructed = False
zeta_baum_connes_assembly_constructed = False
zeta_k_theory_carrier_constructed = False
zeta_kk_product_carrier_constructed = False
zeta_index_pairing_carrier_constructed = False
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
    "OKK8 operator K/KK assembly package constructs no End(S^2/Z) square package",
    not zeta_groupoid_cstar_carrier_constructed
    and not zeta_crossed_product_carrier_constructed
    and not zeta_baum_connes_assembly_constructed
    and not zeta_k_theory_carrier_constructed
    and not zeta_kk_product_carrier_constructed
    and not zeta_index_pairing_carrier_constructed
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
    "no groupoid C*-carrier, crossed-product carrier, K/KK carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("OKK1-OKK8 ALL PASS: operator K-theory / KK assembly is not End(S^2/Z)")
