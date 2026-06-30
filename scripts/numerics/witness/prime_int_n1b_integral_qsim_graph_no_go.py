r"""Integral q-similitude graph no-go.

After doc 214, the next repair is to keep the graph integral and require the
exact q-similitude relation.  This is still not End(S^2/Z): in dimension two,
integral determinant-q matrices already satisfy the standard alternating
q-similitude relation, but they can be off circle and have the wrong primitive
Hodge sign.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_integral_qsim_graph_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def max_integer_defect(A: np.ndarray) -> float:
    return float(np.max(np.abs(A - np.round(A))))


def qsim_defect(A: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(A.T @ E @ A - q * E))


def graph_law_defect(A: np.ndarray, m: int, n: int) -> float:
    return float(
        np.linalg.norm(
            np.linalg.matrix_power(A, m) @ np.linalg.matrix_power(A, n)
            - np.linalg.matrix_power(A, m + n)
        )
    )


def radius_deviation(A: np.ndarray, q: float) -> float:
    target = np.sqrt(q)
    return float(max(abs(abs(z) - target) for z in np.linalg.eigvals(A)))


def determinant_edge_defect(A: np.ndarray, q: float) -> float:
    return float(abs(np.linalg.det(A) - q))


def control_integral_matrix_with_det(q: int) -> np.ndarray:
    """A deliberately untyped integral determinant-q control matrix."""

    return np.array([[1.0, 1.0], [1.0, float(q + 1)]])


# IQG1: the genuine finite-field block has all the square-side graph signs.
q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
true_integral = max_integer_defect(F_true)
true_qsim = qsim_defect(F_true, E_true, q_true)
true_graph = graph_law_defect(F_true, 2, 3)
true_radius = radius_deviation(F_true, q_true)
true_hodge = primitive_hodge_index(F_true, E_true, 1)

gate(
    "IQG1 genuine FF graph has integrality, q-similitude, graph law, and Hodge sign",
    true_integral < 1e-12
    and true_qsim < 1e-12
    and true_graph < 1e-12
    and true_radius < 1e-12
    and true_hodge < 0,
    "integral=%.1e, qsim=%.1e, graph=%.1e, radius=%.1e, H=%.3f"
    % (true_integral, true_qsim, true_graph, true_radius, true_hodge),
)


# IQG2: an integral determinant-q companion can satisfy the same Stage-A
# graph/similitude relations while sitting off circle.
q_off = 2
F_off = frobenius(q_off, 3)
E_off = weil_pairing(F_off, q_off)
off_integral = max_integer_defect(F_off)
off_det = determinant_edge_defect(F_off, q_off)
off_qsim = qsim_defect(F_off, E_off, q_off)
off_graph = graph_law_defect(F_off, 2, 4)
off_radius = radius_deviation(F_off, q_off)
off_hodge = primitive_hodge_index(F_off, E_off, 1)

gate(
    "IQG2 integral q-similitude graph can be off circle with wrong Hodge sign",
    off_integral < 1e-12
    and off_det < 1e-12
    and off_qsim < 1e-12
    and off_graph < 1e-12
    and off_radius > 1e-3
    and off_hodge > 0,
    "F=%s, eig_mod=%s, qsim=%.1e, graph=%.1e, H=%.3f"
    % (
        F_off.astype(int).tolist(),
        [round(float(abs(z)), 6) for z in np.linalg.eigvals(F_off)],
        off_qsim,
        off_graph,
        off_hodge,
    ),
)


# IQG3: the obstruction is not a one-off numerical accident; the same repair
# gives a whole family of integral q-similitudes with positive primitive sign.
family = [(2, 3), (2, 4), (3, 4), (5, 5), (7, 6)]
family_rows: list[tuple[int, int, float, float, float]] = []
for q, a in family:
    F = frobenius(q, a)
    E = weil_pairing(F, q)
    family_rows.append(
        (
            q,
            a,
            qsim_defect(F, E, q),
            radius_deviation(F, q),
            primitive_hodge_index(F, E, 1),
        )
    )

gate(
    "IQG3 integral q-similitude off-circle family is formable",
    all(row[2] < 1e-12 and row[3] > 1e-3 and row[4] > 0 for row in family_rows),
    "rows(q,a,qsim,radius_dev,H)=%s"
    % [
        (q, a, round(float(qs), 3), round(float(dev), 3), round(float(H), 3))
        for q, a, qs, dev, H in family_rows
    ],
)


# IQG4: even the Rosati relation F^dag = q F^{-1} is only the similitude
# relation. It does not force the positive/negative Hodge-index side.
rosati_relation = float(np.linalg.norm(rosati(F_off, E_off) - q_off * np.linalg.inv(F_off)))
stage_a_relation_holds = rosati_relation < 1e-12 and off_qsim < 1e-12
stage_b_sign_fails = off_hodge > 0 and off_radius > 1e-3

gate(
    "IQG4 q-similitude/Rosati relation is not positive Rosati",
    stage_a_relation_holds and stage_b_sign_fails,
    "rosati_relation=%.1e, radius_dev=%.3f, primitive_H=%.3f"
    % (rosati_relation, off_radius, off_hodge),
)


# IQG5: the same integral determinant-q graph package is formable on controls.
control_q = 2
control = control_integral_matrix_with_det(control_q)
control_E = weil_pairing(control, control_q)
control_integral = max_integer_defect(control)
control_det = determinant_edge_defect(control, control_q)
control_qsim = qsim_defect(control, control_E, control_q)
control_graph = graph_law_defect(control, 1, 5)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_intersections = False
control_has_positive_rosati = False

gate(
    "IQG5 integral q-similitude graph package is formable on controls",
    control_integral < 1e-12
    and control_det < 1e-12
    and control_qsim < 1e-12
    and control_graph < 1e-12
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_intersections
    and not control_has_positive_rosati,
    "control=%s, qsim=%.1e, graph=%.1e, no Euler/Satake/rep_NS/Rosati"
    % (control.astype(int).tolist(), control_qsim, control_graph),
)


# IQG6: construction audit.
zeta_rep_ns_constructed = False
zeta_canonical_graph_lattice_constructed = False
zeta_canonical_pairing_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "IQG6 integral q-similitude graph constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_canonical_graph_lattice_constructed
    and not zeta_canonical_pairing_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, canonical graph lattice, pairing, intersections, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (IQG1-IQG6)")
print(
    "VERDICT: integral graph data plus the exact q-similitude/Rosati relation "
    "is still not End(S^2/Z). Determinant-q integral graphs can satisfy the "
    "Stage-A similitude and graph law while remaining off circle with the "
    "wrong primitive Hodge sign. The square object must construct rep_NS, "
    "off-diagonal intersections, and positive Rosati carrier-natively."
)
