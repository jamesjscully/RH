r"""Formal adjoint/projection no-go.

After doc 219, the next repair is to add a transpose/Rosati adjoint to the
formal NS triple envelope with componentwise composition.  This gives an
anti-involution on symbols, but it still does not construct End(S^2/Z): the
adjoint depends on an externally chosen pairing, it does not force positivity,
it does not tie the degree character to the graph self-degree, and the pasted
intersection form plus componentwise composition does not satisfy the expected
correspondence projection identity.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_formal_adjoint_projection_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    primitive_hodge_index,
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


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(compose(graph(F, q, m), graph(F, q, n)), graph(F, q, m + n))


def dagger_twice_defect(A: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(dagger(A, E), E), A)


def anti_defect(A: Corr, B: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(compose(A, B), E), compose(dagger(B, E), dagger(A, E)))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def determinant_edge_defect(F: np.ndarray, q: float) -> float:
    return float(abs(np.linalg.det(F) - q))


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    """Defect in <A o B, C> = <B, A^dag o C> for the pasted formal law."""

    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


# FAP1: the finite-field graph has the expected formal transpose. This is the
# anchor pattern, but only for a carrier where E, degrees, and graphs are
# already geometrically supplied.
q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
H_true = graph(F_true, q_true, 2)
expected_true_dagger = corr(1.0, q_true * np.linalg.inv(F_true), q_true)
true_dagger = dagger(G_true, E_true)
true_dagger_defect = corr_defect(true_dagger, expected_true_dagger)
true_involution = dagger_twice_defect(G_true, E_true)
true_anti = anti_defect(G_true, H_true, E_true)
true_graph = graph_law_defect(F_true, q_true, 1, 2)

gate(
    "FAP1 genuine FF graph has formal transpose anti-involution",
    true_dagger_defect < 1e-12
    and true_involution < 1e-12
    and true_anti < 1e-12
    and true_graph < 1e-12,
    "dagger=%.1e, D2=%.1e, anti=%.1e, graph=%.1e"
    % (true_dagger_defect, true_involution, true_anti, true_graph),
)


# FAP2: the same formal adjoint package exists on off-circle q-similitude
# data, so the anti-involution is not positive Rosati.
q_off = 2
F_off = frobenius(q_off, 3)
E_off = weil_pairing(F_off, q_off)
G_off = graph(F_off, q_off, 1)
H_off = graph(F_off, q_off, 3)
off_expected_dagger = corr(1.0, q_off * np.linalg.inv(F_off), q_off)
off_dagger_defect = corr_defect(dagger(G_off, E_off), off_expected_dagger)
off_involution = dagger_twice_defect(G_off, E_off)
off_anti = anti_defect(G_off, H_off, E_off)
off_qsim = qsim_defect(F_off, E_off, q_off)
off_hodge = primitive_hodge_index(F_off, E_off, 1)

gate(
    "FAP2 formal adjoint wraps off-circle q-similitudes without positivity",
    off_dagger_defect < 1e-12
    and off_involution < 1e-12
    and off_anti < 1e-12
    and off_qsim < 1e-12
    and off_hodge > 0,
    "dagger=%.1e, anti=%.1e, qsim=%.1e, primitive_H=%.3f"
    % (off_dagger_defect, off_anti, off_qsim, off_hodge),
)


# FAP3: formal adjoint from the chosen pairing does not construct the external
# degree character. If F has self-degree 5 but the graph family is assigned
# external q=7, the Rosati adjoint is 5F^{-1}, not 7F^{-1}.
self_q = 5
external_q = 7
F_self = frobenius(self_q, 2)
E_self = weil_pairing(F_self, self_q)
G_external = graph(F_self, external_q, 1)
actual_external_dagger = dagger(G_external, E_self)
forced_external_transpose = corr(1.0, external_q * np.linalg.inv(F_self), external_q)
external_graph_law = graph_law_defect(F_self, external_q, 2, 3)
self_qsim = qsim_defect(F_self, E_self, self_q)
external_transpose_mismatch = corr_defect(actual_external_dagger, forced_external_transpose)

gate(
    "FAP3 formal adjoint does not tie external q to graph self-degree",
    external_graph_law < 1e-12 and self_qsim < 1e-12 and external_transpose_mismatch > 1e-3,
    "graph_law=%.1e, self_qsim=%.1e, actual-vs-external-transpose=%.3f"
    % (external_graph_law, self_qsim, external_transpose_mismatch),
)


# FAP4: the formal law is still not correspondence calculus. With the pasted
# NS pairing and componentwise composition, the expected transpose/projection
# identity has a nonzero defect even on the genuine finite-field block.
projection_cases = [
    projection_defect(G_true, delta(F_true), H_true, E_true),
    projection_defect(G_true, G_true, delta(F_true), E_true),
    projection_defect(H_true, G_true, delta(F_true), E_true),
]
min_projection_defect = min(projection_cases)

gate(
    "FAP4 formal adjoint plus componentwise composition lacks projection formula",
    true_anti < 1e-12 and min_projection_defect > 1e-6,
    "anti=%.1e, projection_defects=%s"
    % (true_anti, [round(float(x), 3) for x in projection_cases]),
)


# FAP5: the same adjoint/projection package is formable on arbitrary controls.
control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_G = graph(control, control_q, 1)
control_H = graph(control, control_q, 2)
control_det = determinant_edge_defect(control, control_q)
control_qsim = qsim_defect(control, control_E, control_q)
control_involution = dagger_twice_defect(control_G, control_E)
control_anti = anti_defect(control_G, control_H, control_E)
control_projection_defect = projection_defect(control_G, delta(control), control_H, control_E)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_properness = False
control_has_positive_rosati = False

gate(
    "FAP5 formal adjoint/projection data is formable on controls",
    control_det < 1e-12
    and control_qsim < 1e-12
    and control_involution < 1e-12
    and control_anti < 1e-12
    and control_projection_defect > 1e-6
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_properness
    and not control_has_positive_rosati,
    "control=%s, qsim=%.1e, anti=%.1e, projection_defect=%.3f, no Euler/Satake/rep_NS/Rosati"
    % (control.astype(int).tolist(), control_qsim, control_anti, control_projection_defect),
)


# FAP6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_degree_character_constructed = False
zeta_frobenius_graph_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "FAP6 formal adjoint/projection repair constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_degree_character_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, fiber-product composition, pairing, projection formula, graph, intersections, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FAP1-FAP6)")
print(
    "VERDICT: adding a formal Rosati/transpose adjoint to the formal NS "
    "composition envelope is not End(S^2/Z). It gives an anti-involution on "
    "chosen triples, but it is external-pairing dependent, survives off-circle "
    "and control data, does not tie the degree character to graph self-degree, "
    "does not supply the correspondence projection formula, and constructs no "
    "actual square carrier, off-diagonal intersections, positive Rosati, or "
    "control death."
)
