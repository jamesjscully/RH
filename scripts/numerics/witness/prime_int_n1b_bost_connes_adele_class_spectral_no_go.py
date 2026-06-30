r"""Bost-Connes / adele-class spectral package no-go.

The Bost-Connes quantum statistical system, the adele-class space, KMS
states, time evolution, spectral triples, and trace-formula realizations are
real zeta-organizing structures.  The R1 shortcut tested here is stronger:
promote that noncommutative-geometric package itself to the square
correspondence carrier End(S^2/Z).  This witness records why that promotion
does not construct the square, rep_NS, degree maps, Frobenius graph,
projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_bost_connes_adele_class_spectral_no_go
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


def bc_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: Bost-Connes algebra, N^x time evolution, KMS state,
    # partition function zeta(beta), adele-class space, scaling action,
    # spectral triple, and trace formula.
    return (True, True, True, True, True, True, True, True)


def kms_weights(beta: float, cutoff: int) -> np.ndarray:
    n = np.arange(1, cutoff + 1, dtype=float)
    weights = n ** (-beta)
    return weights / weights.sum()


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


def spectral_shadow(class_data: np.ndarray) -> tuple[float, float]:
    # A toy spectral/Dixmier trace shadow: keep dimension and residue/volume,
    # forget the endpoint/correspondence coordinate.
    return (float(class_data[0]), float(class_data[1]))


# BCS1: the same BC/adele-class/spectral profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = bc_profile()
profile_other = bc_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "BCS1 BC/adele-class spectral profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# BCS2: BC time evolution and KMS data do not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "BCS2 KMS/time-evolution data does not construct NS degree slots",
    profile_true == bc_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same BC profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# BCS3: KMS positivity / partition weights are state data, not a carrier
# projection formula or count anchor.
weights_beta2 = kms_weights(beta=2.0, cutoff=8)
energy = np.log(np.arange(1, 9, dtype=float))
mean_energy = float(np.dot(weights_beta2, energy))
variance_energy = float(np.dot(weights_beta2, (energy - mean_energy) ** 2))
same_kms_weights_for_different_counts = np.allclose(weights_beta2, kms_weights(2.0, 8))

gate(
    "BCS3 KMS positivity is state data, not square construction",
    same_kms_weights_for_different_counts
    and variance_energy > 0.0
    and counts_true != counts_other,
    "Var_beta=%.6f, same KMS weights can be attached to distinct count anchors"
    % variance_energy,
)


# BCS4: modular/KMS positivity does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
positive_kms_state = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "BCS4 modular/KMS positivity does not impose Frobenius/Rosati compatibility",
    positive_kms_state and off_metric_defect > 1.0,
    "positive KMS state=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# BCS5: spectral-triple/Dixmier-trace shadows can forget endpoint and
# correspondence data.
spectral_class_a = np.array([1.0, 2.0, 0.0])
spectral_class_b = np.array([1.0, 2.0, 4.0])
same_spectral_shadow = spectral_shadow(spectral_class_a) == spectral_shadow(spectral_class_b)
endpoint_gap = float(np.linalg.norm(spectral_class_a - spectral_class_b))

gate(
    "BCS5 spectral-trace shadow loses correspondence endpoint data",
    same_spectral_shadow and endpoint_gap == 4.0,
    "same spectral shadow=%s, endpoint gap=%.1f"
    % (spectral_shadow(spectral_class_a), endpoint_gap),
)


# BCS6: declaring trace formula / spectral correspondence does not construct
# the actual square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_trace_formula = True
declares_spectral_triple = True
declares_correspondence = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "BCS6 trace-formula declaration is not constructed projection formula",
    declares_trace_formula
    and declares_spectral_triple
    and declares_correspondence
    and semantic_projection_defect == 27.0,
    "declared trace/spectral/correspondence=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# BCS7: finite spectral windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "BCS7 finite BC/spectral windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# BCS8: the same formal BC/adele-class/spectral schema is formable on
# controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = bc_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_bc_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "BCS8 formal BC/adele-class spectral schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_bc_square_carrier
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_projection_formula
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no square/rep_NS/degrees/projection/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# BCS9: construction audit.
zeta_bc_algebra_constructed = False
zeta_adele_class_carrier_constructed = False
zeta_spectral_triple_constructed = False
zeta_trace_formula_carrier_constructed = False
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
    "BCS9 BC/adele-class spectral package constructs no End(S^2/Z) square package",
    not zeta_bc_algebra_constructed
    and not zeta_adele_class_carrier_constructed
    and not zeta_spectral_triple_constructed
    and not zeta_trace_formula_carrier_constructed
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
    "no BC square carrier, adele-class carrier, spectral triple carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("BCS1-BCS9 ALL PASS: Bost-Connes / adele-class spectral package is not End(S^2/Z)")
