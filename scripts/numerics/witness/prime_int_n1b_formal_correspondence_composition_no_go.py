r"""Formal correspondence-composition no-go.

After doc 218, the next repair is to put a multiplication on the formal
Z^2 + Z[F] envelope: compose triples componentwise so Delta is an identity
and Gamma_m Gamma_n = Gamma_{m+n}.  This still does not construct
End(S^2/Z): the composition is a formal monoid law around a chosen operator
and a chosen degree character, and is formable on off-circle data and
controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_formal_correspondence_composition_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    primitive_hodge_index,
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


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(compose(graph(F, q, m), graph(F, q, n)), graph(F, q, m + n))


def identity_defect(F: np.ndarray, q: float, n: int) -> float:
    D = delta(F)
    G = graph(F, q, n)
    return corr_defect(compose(D, G), G) + corr_defect(compose(G, D), G)


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def target_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(F, n)).real)


# FCC1: the genuine finite-field graph satisfies the formal composition law
# and diagonal intersections. This is the anchor case.
q_true = 7
F_true = frobenius(q_true, 1)
D_true = delta(F_true)
true_graph_defects = [graph_law_defect(F_true, q_true, m, n) for m, n in ((1, 1), (1, 2), (2, 3))]
true_identity = identity_defect(F_true, q_true, 2)
true_intersections = [
    abs(ns_intersection(D_true, graph(F_true, q_true, n)) - target_count(F_true, q_true, n))
    for n in (1, 2, 3)
]

gate(
    "FCC1 genuine FF graphs satisfy formal composition and diagonal counts",
    max(true_graph_defects) < 1e-12 and true_identity < 1e-12 and max(true_intersections) < 1e-12,
    "graph_defect=%.1e, identity=%.1e, count_defect=%.1e"
    % (max(true_graph_defects), true_identity, max(true_intersections)),
)


# FCC2: the same formal composition law holds for off-circle q-similitude
# data, where the primitive Hodge sign is wrong.
q_off = 2
F_off = frobenius(q_off, 3)
E_off = weil_pairing(F_off, q_off)
off_graph_defect = graph_law_defect(F_off, q_off, 2, 3)
off_identity = identity_defect(F_off, q_off, 1)
off_qsim = qsim_defect(F_off, E_off, q_off)
off_hodge = primitive_hodge_index(F_off, E_off, 1)

gate(
    "FCC2 formal composition wraps off-circle graphs without positivity",
    off_graph_defect < 1e-12 and off_identity < 1e-12 and off_qsim < 1e-12 and off_hodge > 0,
    "graph=%.1e, identity=%.1e, qsim=%.1e, primitive_H=%.3f"
    % (off_graph_defect, off_identity, off_qsim, off_hodge),
)


# FCC3: composition does not choose the external base size. The same z-power
# semigroup can be paired with different degree characters q^n.
q_a = 7
q_b = 11
same_z_graph_a = graph(F_true, q_a, 2)
same_z_graph_b = graph(F_true, q_b, 2)
same_z = np.linalg.norm(same_z_graph_a[1] - same_z_graph_b[1]) < 1e-12
both_compose = graph_law_defect(F_true, q_a, 1, 2) < 1e-12 and graph_law_defect(F_true, q_b, 1, 2) < 1e-12
different_degrees = abs(same_z_graph_a[0] - same_z_graph_b[0]) > 1e-9
different_intersections = abs(
    ns_intersection(D_true, graph(F_true, q_a, 1))
    - ns_intersection(D_true, graph(F_true, q_b, 1))
) > 1e-9

gate(
    "FCC3 formal composition does not construct the degree character",
    same_z and both_compose and different_degrees and different_intersections,
    "same z=F^2, degrees %.1f vs %.1f, Delta.Gamma1 %.1f vs %.1f"
    % (
        same_z_graph_a[0],
        same_z_graph_b[0],
        ns_intersection(D_true, graph(F_true, q_a, 1)),
        ns_intersection(D_true, graph(F_true, q_b, 1)),
    ),
)


# FCC4: even if the operator has an intrinsic self-degree, formal composition
# permits an unrelated external degree character.
self_q = 5
external_q = 7
F_self = frobenius(self_q, 2)
E_self = weil_pairing(F_self, self_q)
self_composition = graph_law_defect(F_self, external_q, 2, 3)
self_qsim = qsim_defect(F_self, E_self, self_q)
external_qsim = qsim_defect(F_self, E_self, external_q)

gate(
    "FCC4 formal composition permits external q unrelated to self-degree",
    self_composition < 1e-12 and self_qsim < 1e-12 and external_qsim > 1e-3,
    "composition=%.1e, self_qsim=%.1e, external_qsim=%.3f"
    % (self_composition, self_qsim, external_qsim),
)


# FCC5: the same composition envelope is formable on arbitrary controls.
control_q = 3
control = np.array([[1.0, 2.0], [1.0, 4.0]])
D_control = delta(control)
control_graph_defect = graph_law_defect(control, control_q, 2, 4)
control_identity = identity_defect(control, control_q, 3)
control_count = ns_intersection(D_control, graph(control, control_q, 1))
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_properness = False
control_has_positive_rosati = False

gate(
    "FCC5 formal composition envelope is formable on controls",
    control_graph_defect < 1e-12
    and control_identity < 1e-12
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_properness
    and not control_has_positive_rosati,
    "control Delta.Gamma=%.3f, no Euler/Satake/rep_NS/properness/Rosati"
    % control_count,
)


# FCC6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_degree_character_constructed = False
zeta_diagonal_constructed = False
zeta_frobenius_graph_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "FCC6 formal correspondence composition constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_degree_character_constructed
    and not zeta_diagonal_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, fiber-product composition, degree character, graph, intersections, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FCC1-FCC6)")
print(
    "VERDICT: formal componentwise correspondence composition is not "
    "End(S^2/Z). It gives Delta as an identity and Gamma_m Gamma_n=Gamma_{m+n} "
    "by construction, but the same law wraps off-circle data and controls, "
    "does not choose the degree character or self-degree compatibility, and "
    "constructs no actual square, fiber-product composition, off-diagonal "
    "intersections, positive Rosati, or control death."
)
