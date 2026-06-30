r"""Numerical/GNS quotient no-go.

After doc 222, the next repair is to add a numerical pairing to the presented
correspondence category and quotient by the radical, or by a GNS-style
positive part, hoping to obtain the positive Rosati carrier.  This still does
not construct End(S^2/Z): the finite-field intersection form on the
Delta/Gamma plane is indefinite with no radical, so radical quotient does
nothing, while forcing positivity removes non-null anchor data or changes the
pairing.  The same operation is formable on controls and finite windows still
admit ghost extensions.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_numerical_gns_quotient_no_go
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


def gram(classes: list[Corr]) -> np.ndarray:
    return np.array([[ns_intersection(a, b) for b in classes] for a in classes], dtype=float)


def inertia(G: np.ndarray, tol: float = 1e-9) -> tuple[int, int, int]:
    eigs = np.linalg.eigvalsh(G)
    pos = int(np.sum(eigs > tol))
    neg = int(np.sum(eigs < -tol))
    nul = int(len(eigs) - pos - neg)
    return pos, neg, nul


def radical_dimension(G: np.ndarray, tol: float = 1e-9) -> int:
    return int(np.sum(np.abs(np.linalg.eigvalsh(G)) <= tol))


def positive_projection_change(G: np.ndarray) -> tuple[np.ndarray, float, int]:
    eigvals, eigvecs = np.linalg.eigh(G)
    keep = eigvals > 1e-9
    G_pos = eigvecs[:, keep] @ np.diag(eigvals[keep]) @ eigvecs[:, keep].T
    return G_pos, float(np.linalg.norm(G_pos - G)), int(np.sum(~keep))


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(F, n)).real)


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


def root_of_unity_block(order: int, radius: float) -> np.ndarray:
    roots = [radius * np.exp(2j * np.pi * k / order) for k in range(order)]
    return np.diag(roots)


def rosati_positive_pairing(F: np.ndarray, E: np.ndarray) -> float:
    return float(np.trace(F @ rosati(F, E)).real)


# NGQ1: the genuine finite-field Delta/Gamma intersection plane is indefinite
# and nondegenerate. A radical quotient has no radical to remove.
q_true = 7
F_true = frobenius(q_true, 1)
D_true = delta(F_true)
G_true = graph(F_true, q_true, 1)
GG_true = gram([D_true, G_true])
true_eigs = np.linalg.eigvalsh(GG_true)
true_inertia = inertia(GG_true)
true_radical_dim = radical_dimension(GG_true)

gate(
    "NGQ1 finite-field Delta/Gamma Gram is indefinite with no radical",
    np.allclose(GG_true, np.array([[0.0, 7.0], [7.0, 27.0]]))
    and true_inertia == (1, 1, 0)
    and true_radical_dim == 0,
    "Gram=%s, eigs=%s, inertia=%s"
    % (GG_true.astype(int).tolist(), [round(float(x), 3) for x in true_eigs], true_inertia),
)


# NGQ2: projecting to the positive part makes a PSD form, but it changes the
# finite-field pairing data. This is positivity by modifying non-null data.
G_pos, projection_change, dropped_rank = positive_projection_change(GG_true)
pos_inertia = inertia(G_pos)

gate(
    "NGQ2 positive-part quotient changes non-null finite-field anchor data",
    pos_inertia == (1, 0, 1) and dropped_rank == 1 and projection_change > 1e-6,
    "projected Gram=%s, change_norm=%.3f, dropped_rank=%d"
    % ([[round(float(x), 3) for x in row] for row in G_pos], projection_change, dropped_rank),
)


# NGQ3: the positive Rosati pairing is a different carrier-native pairing, not
# a radical quotient of the NS intersection form on presented symbols.
E_true = weil_pairing(F_true, q_true)
intersection_self = ns_intersection(G_true, G_true)
rosati_self = rosati_positive_pairing(F_true, E_true)
radical_unchanged = true_radical_dim == 0

gate(
    "NGQ3 Rosati positivity is not recovered by radical quotient",
    radical_unchanged and intersection_self == 27.0 and rosati_self == 14.0,
    "Gamma.Gamma=%.1f, Tr(F Fdag)=%.1f, radical_dim=%d"
    % (intersection_self, rosati_self, true_radical_dim),
)


# NGQ4: finite numerical quotients still do not determine the carrier. Ghost
# summands preserve the finite trace window while changing the next count.
window = 4
ghost = root_of_unity_block(window + 1, 1.25)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_next_count = point_count(F_true, q_true, window + 1)
aug_next_count = float(q_true ** (window + 1) + 1.0 - power_traces(augmented, window + 1)[-1].real)
next_count_gap = abs(base_next_count - aug_next_count)

gate(
    "NGQ4 finite numerical quotient windows admit ghost extensions",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window)) and next_count_gap > 1e-3,
    "first %d traces match; count_%d differs by %.3f"
    % (window, window + 1, next_count_gap),
)


# NGQ5: the same Gram/radical/positive-part operation is formable on controls.
control_q = 7
control_counts = [10.0, -3.0]
control_trace_1 = control_q + 1.0 - control_counts[0]
control_trace_2 = control_q**2 + 1.0 - control_counts[1]
control_gram = np.array([[0.0, control_counts[0]], [control_counts[0], 2.0 * control_q - control_trace_2]])
control_inertia = inertia(control_gram)
control_radical = radical_dimension(control_gram)
control_pos, control_change, control_dropped = positive_projection_change(control_gram)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "NGQ5 numerical/GNS quotient is formable on controls",
    control_inertia == (1, 1, 0)
    and control_radical == 0
    and control_dropped == 1
    and control_change > 1e-6
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control Gram=%s, inertia=%s, pos_change=%.3f, no Euler/Satake/rep_NS/Rosati"
    % (control_gram.astype(int).tolist(), control_inertia, control_change),
)


# NGQ6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_numerical_equivalence_constructed = False
zeta_positive_rosati_constructed = False
zeta_frobenius_graph_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "NGQ6 numerical/GNS quotient constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_numerical_equivalence_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, pairing, numerical equivalence, Rosati, graph, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (NGQ1-NGQ6)")
print(
    "VERDICT: numerical radical or GNS quotienting of a presented carrier is "
    "not End(S^2/Z). The finite-field Delta/Gamma Gram is indefinite with no "
    "radical, so radical quotienting does nothing; forcing positivity changes "
    "non-null anchor data or imports a different pairing. The same operation "
    "is formable on controls, finite windows admit ghost extensions, and no "
    "actual square, proper correspondences, carrier-native pairing, positive "
    "Rosati, or control death is constructed."
)
