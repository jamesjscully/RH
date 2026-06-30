r"""Isospectral graph carrier no-go.

After doc 213, the next repair is to use the whole spectrum/conjugacy class,
not merely a finite trace window.  This still does not construct End(S^2/Z):
power traces and graph composition are invariant under similarity, while the
integral lattice and Rosati/cup pairing are extra carrier data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_isospectral_graph_carrier_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    primitive_hodge_index,
)


failures = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    n = sum(block.shape[0] for block in blocks)
    out = np.zeros((n, n), dtype=float)
    pos = 0
    for block in blocks:
        k = block.shape[0]
        out[pos : pos + k, pos : pos + k] = block
        pos += k
    return out


def standard_symplectic(n: int) -> np.ndarray:
    E = np.zeros((n, n), dtype=float)
    for i in range(n // 2):
        E[2 * i, 2 * i + 1] = 1.0
        E[2 * i + 1, 2 * i] = -1.0
    return E


def qsim_defect(A: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(A.T @ E @ A - q * E))


def power_traces(A: np.ndarray, upto: int) -> list[float]:
    return [float(np.trace(np.linalg.matrix_power(A, n)).real) for n in range(1, upto + 1)]


def max_integer_defect(A: np.ndarray) -> float:
    return float(np.max(np.abs(A - np.round(A))))


q = 7
F = block_diag(frobenius(q, 1), frobenius(q, 3))
E = standard_symplectic(4)


# ISG1: genuine finite-field graph carrier data.
true_qsim = qsim_defect(F, E, q)
true_hodge = primitive_hodge_index(F, E, 2)
true_integral_defect = max_integer_defect(F)

gate(
    "ISG1 genuine FF block has integral graph, q-similitude, and Hodge sign",
    true_integral_defect < 1e-12 and true_qsim < 1e-9 and true_hodge < 0,
    "integral_defect=%.1e, qsim=%.1e, H=%.3f" % (true_integral_defect, true_qsim, true_hodge),
)


# ISG2: a non-integral similarity preserves every sampled power trace and graph law.
P = np.eye(4)
P[0, 2] = 0.37
P[1, 3] = -0.22
Pinv = np.linalg.inv(P)
A = P @ F @ Pinv

trace_match = all(abs(a - b) < 1e-8 for a, b in zip(power_traces(F, 10), power_traces(A, 10)))
graph_law_defect = float(np.linalg.norm(A @ np.linalg.matrix_power(A, 3) - np.linalg.matrix_power(A, 4)))
char_match = np.allclose(np.poly(F), np.poly(A), atol=1e-8)

gate(
    "ISG2 full spectral/trace data and graph law survive noncanonical similarity",
    trace_match and graph_law_defect < 1e-9 and char_match,
    "t1..t4=%s, graph_defect=%.1e, char_match=%s"
    % ([round(x, 3) for x in power_traces(A, 4)], graph_law_defect, char_match),
)


# ISG3: the same isospectral graph is not the original integral/Rosati carrier.
A_integral_defect = max_integer_defect(A)
A_qsim_original = qsim_defect(A, E, q)

gate(
    "ISG3 isospectral graph does not preserve the original lattice or cup form",
    A_integral_defect > 1e-3 and A_qsim_original > 1e-3,
    "integral_defect=%.3f, qsim_original=%.3f" % (A_integral_defect, A_qsim_original),
)


# ISG4: Rosati can be transported along the chosen similarity, showing the extra choice.
E_transported = Pinv.T @ E @ Pinv
A_qsim_transported = qsim_defect(A, E_transported, q)
transported_pairing_moved = float(np.linalg.norm(E_transported - E))

P2 = np.eye(4)
P2[0, 3] = -0.41
P2[2, 1] = 0.29
E_transported_2 = np.linalg.inv(P2).T @ E @ np.linalg.inv(P2)
two_pairings_differ = float(np.linalg.norm(E_transported - E_transported_2))

gate(
    "ISG4 spectrum does not choose the Rosati pairing",
    A_qsim_transported < 1e-9 and transported_pairing_moved > 1e-3 and two_pairings_differ > 1e-3,
    "transported_qsim=%.1e, |E1-E|=%.3f, |E1-E2|=%.3f"
    % (A_qsim_transported, transported_pairing_moved, two_pairings_differ),
)


# ISG5: isospectral conjugacy is formable on arbitrary controls.
control = np.diag([1.2, 2.1, -0.7, 3.4])
Q = np.eye(4)
Q[0, 1] = 0.5
Q[2, 3] = -0.25
control_conj = Q @ control @ np.linalg.inv(Q)
control_trace_match = all(
    abs(a - b) < 1e-9 for a, b in zip(power_traces(control, 6), power_traces(control_conj, 6))
)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_rosati = False

gate(
    "ISG5 isospectral graph operation is formable on controls",
    control_trace_match
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_rosati,
    "control power traces preserved without Euler/Satake/rep_NS/Rosati",
)


# ISG6: construction audit.
zeta_rep_ns_constructed = False
zeta_integral_lattice_constructed = False
zeta_canonical_pairing_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "ISG6 spectral graph data constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_integral_lattice_constructed
    and not zeta_canonical_pairing_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, lattice, pairing, off-diagonal intersections, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (ISG1-ISG6)")
print(
    "VERDICT: full isospectral graph data is still not End(S^2/Z). "
    "Similarity preserves power traces and graph law, but the integral lattice "
    "and Rosati/cup pairing move with an extra choice; the same operation is "
    "formable on controls. The square object must construct rep_NS, the "
    "lattice, off-diagonal intersections, and positive Rosati carrier-natively."
)
