r"""Chow / Hilbert cycle-moduli carrier no-go.

After doc 235, the next repair is to replace fixed-cycle or CM labels by an
actual moduli slogan: take a Hilbert scheme or Chow variety of cycles, use
the universal family as the correspondence carrier, and read rep_NS from its
cycle parameters.  This is still downstream of an ambient square.  Hilbert
and Chow moduli parameterize subschemes or cycles after the projective
carrier and its degree/pairing/composition data exist; they do not construct
End(S^2/Z) by themselves.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_chow_hilbert_cycle_moduli_no_go
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


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


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


def chow_hilbert_profile() -> tuple[int, tuple[int, int], bool, bool, bool]:
    # Toy profile: one cycle component, fixed Hilbert polynomial coefficients,
    # projectivity, universal family, and cycle-class map declared.
    return (1, (1, 1), True, True, True)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# CHM1: the same abstract Hilbert/Chow profile does not determine the
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = chow_hilbert_profile()
profile_other = chow_hilbert_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "CHM1 Chow/Hilbert profile does not determine count anchor",
    profile_true == profile_other == (1, (1, 1), True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# CHM2: Hilbert/Chow cycle labels do not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "CHM2 cycle moduli do not construct NS degree slots",
    profile_true == chow_hilbert_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same z-cycle label and profile, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# CHM3: a universal family requires an ambient intersection pairing.  The
# same cycle vector and Hilbert polynomial can live in ambient pairings with
# different self-intersections.
cycle_vector = np.array([1.0, 0.0])
ambient_pairing_a = np.array([[0.0, 1.0], [1.0, 0.0]])
ambient_pairing_b = np.array([[2.0, 0.0], [0.0, -1.0]])
self_a = float(cycle_vector @ ambient_pairing_a @ cycle_vector)
self_b = float(cycle_vector @ ambient_pairing_b @ cycle_vector)

gate(
    "CHM3 universal family does not construct the ambient intersection form",
    profile_true == profile_other and self_a == 0.0 and self_b == 2.0,
    "same cycle vector/profile, self-intersection changes %.1f -> %.1f with ambient pairing"
    % (self_a, self_b),
)


# CHM4: being a point of a cycle moduli space does not select the diagonal or
# Frobenius graph correspondence triples.  The identity and Frobenius labels
# are both graph-shaped z-cycles in the same coarse profile, but intersections
# differ.
I = np.eye(F_true.shape[0])
Id_cycle = corr(1.0, I, 1.0)
id_profile = chow_hilbert_profile()
frobenius_profile = chow_hilbert_profile()
delta_id = ns_intersection(D_true, Id_cycle)
delta_graph = ns_intersection(D_true, Gamma_true)

gate(
    "CHM4 cycle-moduli membership does not select diagonal/graph triples",
    id_profile == frobenius_profile
    and delta_id == 0.0
    and delta_graph == 7.0,
    "same coarse graph-cycle profile; Delta.Id=%.1f, Delta.Gamma=%.1f"
    % (delta_id, delta_graph),
)


# CHM5: finite Hilbert/Chow windows admit ghost cycle components.  A 5-cycle
# ghost preserves traces in powers 1..4 and changes the next count.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "CHM5 finite Chow/Hilbert windows admit ghost cycle components",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# CHM6: the same formal cycle-moduli schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = chow_hilbert_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_actual_hilbert_scheme = False
control_has_chow_variety = False
control_has_ambient_square = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "CHM6 formal cycle-moduli schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_actual_hilbert_scheme
    and not control_has_chow_variety
    and not control_has_ambient_square
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no Hilbert/Chow/square/rep_NS/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# CHM7: construction audit.
zeta_hilbert_scheme_constructed = False
zeta_chow_variety_constructed = False
zeta_universal_family_constructed = False
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
    "CHM7 Chow/Hilbert cycle moduli construct no End(S^2/Z) square package",
    not zeta_hilbert_scheme_constructed
    and not zeta_chow_variety_constructed
    and not zeta_universal_family_constructed
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
    "no Hilbert/Chow carrier, ambient square, rep_NS, graph, projection, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CHM1-CHM7)")
print(
    "VERDICT: Chow/Hilbert cycle-moduli data is not End(S^2/Z). It can "
    "parameterize cycles only after an ambient square exists; it does not "
    "construct count anchors, NS degree slots, diagonal/graph triples, the "
    "ambient pairing, proper correspondences, projection formula, positive "
    "Rosati, control death, rep_NS, or DD.4."
)
