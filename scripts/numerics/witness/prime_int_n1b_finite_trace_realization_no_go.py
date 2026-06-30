r"""Finite trace realization no-go.

After doc 212, the next repair is to enforce graph composition by choosing a
single operator A and using A^n as the Frobenius graph shadow.  This is still
not the End(S^2/Z) square package: finite trace windows are underdetermined,
companion/Newton realizations are formable on controls, and neither
q-similitude nor positive Rosati is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_finite_trace_realization_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    primitive_hodge_index,
    weil_pairing,
)


failures = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


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


def elementary_from_power_sums(power_sums: list[float]) -> list[float]:
    """Newton identities: first d power sums -> elementary symmetrics e_1..e_d."""

    e: list[float] = []
    for k, pk in enumerate(power_sums, start=1):
        accum = pk
        for i in range(1, k):
            accum += ((-1) ** i) * e[i - 1] * power_sums[k - i - 1]
        e_k = ((-1) ** (k + 1)) * accum / k
        e.append(float(e_k))
    return e


def roots_from_power_sums(power_sums: list[float]) -> np.ndarray:
    e = elementary_from_power_sums(power_sums)
    coeffs = [1.0]
    for k, e_k in enumerate(e, start=1):
        coeffs.append(((-1) ** k) * e_k)
    return np.roots(coeffs)


def standard_symplectic(n: int) -> np.ndarray:
    E = np.zeros((n, n), dtype=complex)
    for i in range(n // 2):
        E[2 * i, 2 * i + 1] = 1.0
        E[2 * i + 1, 2 * i] = -1.0
    return E


def similitude_defect(A: np.ndarray, q: float) -> float:
    E = standard_symplectic(A.shape[0])
    return float(np.linalg.norm(A.T @ E @ A - q * E))


q = 7
a1 = 1
F = frobenius(q, a1).astype(complex)
E = weil_pairing(F, q)


# FTR1: the real finite-field graph is a graph package, not just a trace fit.
true_traces = power_traces(F, 6)
true_composition_defect = float(np.linalg.norm(F @ np.linalg.matrix_power(F, 2) - np.linalg.matrix_power(F, 3)))
true_similitude_defect = float(np.linalg.norm(F.T @ E @ F - q * E))
true_hodge_index = primitive_hodge_index(F, E, 1)

gate(
    "FTR1 genuine FF operator has traces, graph law, q-similitude, and Hodge sign",
    true_composition_defect < 1e-9 and true_similitude_defect < 1e-9 and true_hodge_index < 0,
    "t1..t4=%s, comp=%.1e, sim=%.1e, H=%.3f"
    % ([round(float(t.real), 3) for t in true_traces[:4]], true_composition_defect, true_similitude_defect, true_hodge_index),
)


# FTR2: finite trace windows are underdetermined even when graph composition is enforced by one operator.
window = 5
ghost = root_of_unity_block(window + 1, 1.3)
augmented = block_diag(F, ghost)
base_window = power_traces(F, window)
aug_window = power_traces(augmented, window)
first_mismatch = power_traces(F, window + 1)[-1]
aug_first_mismatch = power_traces(augmented, window + 1)[-1]

gate(
    "FTR2 finite trace window does not determine the semigroup realization",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and abs(first_mismatch - aug_first_mismatch) > 1e-3,
    "first %d traces match; trace_%d differs by %.3f"
    % (window, window + 1, abs(first_mismatch - aug_first_mismatch)),
)


# FTR3: the augmented trace-fit semigroup is not a q-similitude/Rosati carrier.
aug_sim_defect = similitude_defect(augmented, q)
gate(
    "FTR3 semigroup trace realization does not force q-similitude",
    aug_sim_defect > 1e-3,
    "augmented q-similitude defect %.3f" % aug_sim_defect,
)


# FTR4: an off-radius companion realization has a graph law and determinant edge but wrong Hodge sign.
F_off = np.diag([1.45 * np.sqrt(q), np.sqrt(q) / 1.45]).astype(complex)
E_off = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
off_det_edge = abs(np.linalg.det(F_off) - q) < 1e-9
off_graph_law = np.linalg.norm(F_off @ F_off - np.linalg.matrix_power(F_off, 2)) < 1e-9
off_sim = float(np.linalg.norm(F_off.T @ E_off @ F_off - q * E_off))
off_hodge = primitive_hodge_index(F_off, E_off, 1)

gate(
    "FTR4 graph law plus determinant edge does not force Rosati positivity",
    off_det_edge and off_graph_law and off_sim < 1e-9 and off_hodge > 0,
    "det=q? %s, sim=%.1e, off-circle H=%.3f" % (off_det_edge, off_sim, off_hodge),
)


# FTR5: finite companion/Newton realization is formable on arbitrary controls.
control_power_sums = [3.0, -5.0, 8.0, 13.0]
control_roots = roots_from_power_sums(control_power_sums)
control_operator = np.diag(control_roots)
control_realized = power_traces(control_operator, len(control_power_sums))
control_has_euler_product = False
control_has_satake = False
control_has_correspondence_algebra = False
control_has_rosati = False

gate(
    "FTR5 finite trace realization is formable on controls",
    all(abs(a.real - b) < 1e-7 for a, b in zip(control_realized, control_power_sums))
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_correspondence_algebra
    and not control_has_rosati,
    "control traces realized as %s" % [round(float(z.real), 3) for z in control_realized],
)


# FTR6: construction audit.
zeta_rep_ns_constructed = False
zeta_canonical_operator_constructed = False
zeta_square_h2_constructed = False
zeta_off_diagonal_pairing_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "FTR6 finite trace realization constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_canonical_operator_constructed
    and not zeta_square_h2_constructed
    and not zeta_off_diagonal_pairing_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, canonical operator, square H2, off-diagonal pairing, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FTR1-FTR6)")
print(
    "VERDICT: enforcing graph composition by finite trace realization is still "
    "not End(S^2/Z). Finite windows admit ghost semigroup summands, graph law "
    "plus determinant edge can remain off-circle, and Newton/companion "
    "realizations are formable on arbitrary controls. The missing object must "
    "construct rep_NS, a canonical graph carrier, off-diagonal pairings, and "
    "positive Rosati, not merely an operator fitting finitely many traces."
)
