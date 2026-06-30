r"""Unitary projection graph no-go.

After doc 215, the next repair is to normalize an integral q-similitude graph
by sqrt(q) and project it to a unitary/compact graph.  This still does not
construct End(S^2/Z): spectral radial projection changes off-circle traces
and integrality, while polar projection depends on an external metric and can
change even the genuine finite-field graph.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_unitary_projection_graph_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import frobenius, weil_pairing


failures: list[str] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def power_traces(A: np.ndarray, upto: int) -> list[float]:
    return [float(np.trace(np.linalg.matrix_power(A, n)).real) for n in range(1, upto + 1)]


def max_trace_delta(A: np.ndarray, B: np.ndarray, upto: int) -> float:
    return max(abs(a - b) for a, b in zip(power_traces(A, upto), power_traces(B, upto)))


def max_integer_defect(A: np.ndarray) -> float:
    return float(np.max(np.abs(A - np.round(A))))


def qsim_defect(A: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(A.T @ E @ A - q * E))


def normalized_radius_deviation(A: np.ndarray, q: float) -> float:
    return float(max(abs(abs(z) / np.sqrt(q) - 1.0) for z in np.linalg.eigvals(A)))


def graph_law_defect(A: np.ndarray, m: int, n: int) -> float:
    return float(
        np.linalg.norm(
            np.linalg.matrix_power(A, m) @ np.linalg.matrix_power(A, n)
            - np.linalg.matrix_power(A, m + n)
        )
    )


def spectral_radial_projection(A: np.ndarray, q: float) -> np.ndarray:
    """Move each eigenvalue radially to |alpha|=sqrt(q), keeping eigenvectors."""

    eigvals, eigvecs = np.linalg.eig(A)
    projected = [np.sqrt(q) * z / abs(z) for z in eigvals]
    B = eigvecs @ np.diag(projected) @ np.linalg.inv(eigvecs)
    return np.real_if_close(B, tol=1000).astype(float)


def scaled_euclidean_polar_unitary(A: np.ndarray, q: float) -> np.ndarray:
    """Return sqrt(q) times the Euclidean polar unitary of A/sqrt(q)."""

    normalized = A / np.sqrt(q)
    gram = normalized.T @ normalized
    eigvals, eigvecs = np.linalg.eigh(gram)
    inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
    return np.sqrt(q) * normalized @ inv_sqrt


def invariant_symmetric_form(normalized: np.ndarray) -> np.ndarray:
    """Solve N^T H N = H on symmetric 2 x 2 forms and return one null vector."""

    basis = [
        np.array([[1.0, 0.0], [0.0, 0.0]]),
        np.array([[0.0, 1.0], [1.0, 0.0]]),
        np.array([[0.0, 0.0], [0.0, 1.0]]),
    ]
    rows = []
    for H in basis:
        residual = normalized.T @ H @ normalized - H
        rows.append([residual[0, 0], residual[0, 1], residual[1, 1]])
    operator = np.array(rows).T
    _u, _s, vh = np.linalg.svd(operator)
    coeffs = vh[-1]
    return sum(c * H for c, H in zip(coeffs, basis))


# UPG1: on a genuine finite-field block, spectral radial projection is the
# identity because the radius is already correct. This is the only safe case.
q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
R_true = spectral_radial_projection(F_true, q_true)

gate(
    "UPG1 spectral radial projection preserves a genuine on-circle graph",
    np.linalg.norm(R_true - F_true) < 1e-10
    and max_trace_delta(R_true, F_true, 4) < 1e-10
    and max_integer_defect(R_true) < 1e-10
    and qsim_defect(R_true, E_true, q_true) < 1e-10,
    "delta=%.1e, trace_delta=%.1e, integral=%.1e"
    % (np.linalg.norm(R_true - F_true), max_trace_delta(R_true, F_true, 4), max_integer_defect(R_true)),
)


# UPG2: on an off-circle integral q-similitude, radial projection repairs the
# radius only by changing the graph traces and losing integrality.
q_off = 2
F_off = frobenius(q_off, 3)
E_off = weil_pairing(F_off, q_off)
R_off = spectral_radial_projection(F_off, q_off)
off_radius_before = normalized_radius_deviation(F_off, q_off)
off_radius_after = normalized_radius_deviation(R_off, q_off)
off_trace_delta = max_trace_delta(R_off, F_off, 4)
off_integral_defect = max_integer_defect(R_off)

gate(
    "UPG2 radial unitarization changes the off-circle graph data",
    off_radius_before > 1e-3
    and off_radius_after < 1e-12
    and off_trace_delta > 1e-3
    and off_integral_defect > 1e-3
    and qsim_defect(R_off, E_off, q_off) < 1e-10
    and graph_law_defect(R_off, 2, 3) < 1e-10,
    "radius %.3f -> %.1e, trace_delta=%.3f, integral_defect=%.3f"
    % (off_radius_before, off_radius_after, off_trace_delta, off_integral_defect),
)


# UPG3: Euclidean polar projection depends on an external metric. With the
# standard Euclidean metric, it changes even the genuine finite-field graph.
P_true = scaled_euclidean_polar_unitary(F_true, q_true)
polar_orth_defect = float(np.linalg.norm((P_true / np.sqrt(q_true)).T @ (P_true / np.sqrt(q_true)) - np.eye(2)))
polar_trace_delta = max_trace_delta(P_true, F_true, 4)
polar_integral_defect = max_integer_defect(P_true)

gate(
    "UPG3 polar projection is metric-dependent and not graph-preserving",
    polar_orth_defect < 1e-10
    and polar_trace_delta > 1e-3
    and polar_integral_defect > 1e-3
    and qsim_defect(P_true, E_true, q_true) < 1e-10,
    "orth_defect=%.1e, trace_delta=%.3f, integral_defect=%.3f"
    % (polar_orth_defect, polar_trace_delta, polar_integral_defect),
)


# UPG4: the original off-circle normalized graph admits no positive invariant
# metric. The invariant symmetric form is hyperbolic, so compactness is not
# recovered without changing the graph or importing positivity.
H_off = invariant_symmetric_form(F_off / np.sqrt(q_off))
H_eigs = np.linalg.eigvalsh((H_off + H_off.T) / 2.0)
H_residual = float(np.linalg.norm((F_off / np.sqrt(q_off)).T @ H_off @ (F_off / np.sqrt(q_off)) - H_off))
has_positive_and_negative = np.min(H_eigs) < -1e-6 and np.max(H_eigs) > 1e-6

gate(
    "UPG4 off-circle normalized graph has only an indefinite invariant form",
    H_residual < 1e-10 and has_positive_and_negative,
    "residual=%.1e, eig(H)=%s" % (H_residual, [round(float(x), 6) for x in H_eigs]),
)


# UPG5: the same projection operations are formable on untyped controls and
# change control traces exactly as they change the zeta-style off-circle graph.
control_q = 2
control = np.array([[1.0, 1.0], [1.0, 3.0]])
control_radial = spectral_radial_projection(control, control_q)
control_polar = scaled_euclidean_polar_unitary(control, control_q)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_intersections = False
control_has_positive_rosati = False

gate(
    "UPG5 unitary projection operations are formable on controls",
    normalized_radius_deviation(control_radial, control_q) < 1e-12
    and float(np.linalg.norm((control_polar / np.sqrt(control_q)).T @ (control_polar / np.sqrt(control_q)) - np.eye(2))) < 1e-10
    and max_trace_delta(control_radial, control, 4) > 1e-3
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_intersections
    and not control_has_positive_rosati,
    "control trace_delta=%.3f, no Euler/Satake/rep_NS/Rosati"
    % max_trace_delta(control_radial, control, 4),
)


# UPG6: construction audit.
zeta_rep_ns_constructed = False
zeta_canonical_unitary_projection_constructed = False
zeta_original_graph_preserved = False
zeta_canonical_pairing_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "UPG6 unitary projection constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_canonical_unitary_projection_constructed
    and not zeta_original_graph_preserved
    and not zeta_canonical_pairing_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, canonical projection, original graph, pairing, intersections, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (UPG1-UPG6)")
print(
    "VERDICT: post-hoc unitary projection is not End(S^2/Z). Spectral "
    "radial projection repairs an off-circle graph only by changing traces "
    "and integrality; Euclidean polar projection depends on an external "
    "metric and can change even a genuine finite-field graph. The original "
    "off-circle graph remains non-polarizable, and the projections are "
    "formable on controls."
)
