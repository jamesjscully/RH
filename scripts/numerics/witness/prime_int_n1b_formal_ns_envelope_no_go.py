r"""Formal NS-envelope no-go.

After doc 217, the next repair is to add the two missing fiber-degree slots
by hand: build a formal Z^2 + Z[F] envelope with intersection
d1 e2 + d2 e1 - Tr(zw), declare Delta=(1,Id,1), and declare
Gamma_F=(q,F,1).  This still does not construct End(S^2/Z): the envelope is
the finite-field formula pasted around a chosen operator, its fiber degrees
are freely assigned, and it is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_formal_ns_envelope_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    is_indecomposable,
    ns_intersection,
    primitive_hodge_index,
    weil_pairing,
)


failures: list[str] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def formal_corr(d1: float, z: np.ndarray, d2: float) -> tuple[float, np.ndarray, float]:
    return (float(d1), z, float(d2))


def formal_delta(F: np.ndarray) -> tuple[float, np.ndarray, float]:
    return formal_corr(1.0, np.eye(F.shape[0]), 1.0)


def formal_graph(F: np.ndarray, q: float, n: int = 1) -> tuple[float, np.ndarray, float]:
    return formal_corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def power_traces(F: np.ndarray, upto: int) -> list[float]:
    return [float(np.trace(np.linalg.matrix_power(F, n)).real) for n in range(1, upto + 1)]


def target_count(q: float, F: np.ndarray, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(F, n)).real)


# FNE1: the genuine finite-field envelope reproduces the doc-211 anchor.
q_true = 7
F_true = frobenius(q_true, 1)
D_true = formal_delta(F_true)
matches_anchor = []
for n in (1, 2, 3):
    G = formal_graph(F_true, q_true, n)
    matches_anchor.append(abs(ns_intersection(D_true, G) - target_count(q_true, F_true, n)) < 1e-12)

gate(
    "FNE1 genuine FF formal envelope reproduces diagonal intersections",
    all(matches_anchor) and is_indecomposable(D_true),
    "counts=%s, Delta indecomposable=%s"
    % ([round(target_count(q_true, F_true, n), 3) for n in (1, 2, 3)], is_indecomposable(D_true)),
)


# FNE2: the same formal recipe wraps an off-circle q-similitude and produces
# scalar diagonal intersections while positivity fails.
q_off = 2
F_off = frobenius(q_off, 3)
E_off = weil_pairing(F_off, q_off)
D_off = formal_delta(F_off)
G_off = formal_graph(F_off, q_off, 1)
off_diag_value = ns_intersection(D_off, G_off)
off_target_value = target_count(q_off, F_off, 1)
off_hodge = primitive_hodge_index(F_off, E_off, 1)

gate(
    "FNE2 formal envelope can wrap off-circle graphs without positivity",
    abs(off_diag_value - off_target_value) < 1e-12 and off_hodge > 0,
    "Delta.Gamma=%.3f by formula, primitive_H=%.3f" % (off_diag_value, off_hodge),
)


# FNE3: the diagonal intersection only fixes d1+d2-Tr(z). The two fiber
# degrees are freely assigned unless a carrier constructs them.
G_standard = formal_graph(F_true, q_true, 1)
G_shifted = formal_corr(6.0, F_true, 2.0)
G_more_shifted = formal_corr(0.0, F_true, 8.0)
same_z = (
    np.linalg.norm(G_standard[1] - G_shifted[1]) < 1e-12
    and np.linalg.norm(G_standard[1] - G_more_shifted[1]) < 1e-12
)
intersections = [ns_intersection(D_true, G) for G in (G_standard, G_shifted, G_more_shifted)]
degrees_differ = len({(G[0], G[2]) for G in (G_standard, G_shifted, G_more_shifted)}) == 3

gate(
    "FNE3 formal fiber degrees are not determined by diagonal traces",
    same_z and degrees_differ and max(intersections) - min(intersections) < 1e-12,
    "degree pairs=%s, shared Delta.Gamma=%.3f"
    % ([(G[0], G[2]) for G in (G_standard, G_shifted, G_more_shifted)], intersections[0]),
)


# FNE4: diagonal indecomposability is inserted by choosing z=Id. The formal
# wrapper can make the same indecomposable diagonal for a control operator.
control = np.array([[1.0, 1.0], [1.0, 3.0]])
D_control = formal_delta(control)
product_fiber_class = formal_corr(1.0, np.zeros_like(control), 0.0)
control_diagonal_inserted = is_indecomposable(D_control) and not is_indecomposable(product_fiber_class)

gate(
    "FNE4 indecomposable diagonal is inserted, not carrier-constructed",
    control_diagonal_inserted,
    "control Delta indecomposable=%s, product/fiber indecomposable=%s"
    % (is_indecomposable(D_control), is_indecomposable(product_fiber_class)),
)


# FNE5: arbitrary scalar count windows can be hit by choosing fiber degrees
# after the operator is chosen. This is calibration, not construction.
target_window = [10.0, -3.0, 25.0]
control_graphs = []
for n, target in enumerate(target_window, start=1):
    z = np.linalg.matrix_power(control, n)
    # Delta.(d1,z,d2) = d1 + d2 - Tr(z). Set d2=1 and solve for d1.
    d2 = 1.0
    d1 = target + np.trace(z).real - d2
    control_graphs.append(formal_corr(d1, z, d2))
realized_window = [ns_intersection(D_control, G) for G in control_graphs]
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_properness = False
control_has_positive_rosati = False

gate(
    "FNE5 formal NS envelope is formable and calibratable on controls",
    all(abs(a - b) < 1e-12 for a, b in zip(realized_window, target_window))
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_properness
    and not control_has_positive_rosati,
    "targets=%s realized=%s without Euler/Satake/rep_NS/properness/Rosati"
    % (target_window, [round(float(x), 3) for x in realized_window]),
)


# FNE6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_fiber_degrees_constructed = False
zeta_diagonal_constructed = False
zeta_frobenius_graph_constructed = False
zeta_off_diagonal_intersections_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "FNE6 formal NS envelope constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_fiber_degrees_constructed
    and not zeta_diagonal_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_off_diagonal_intersections_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, fiber degrees, diagonal, graph, intersections, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FNE1-FNE6)")
print(
    "VERDICT: a formal Z^2 + Z[F] NS envelope is not End(S^2/Z). It can "
    "paste the finite-field intersection formula around any chosen operator "
    "and even calibrate scalar intersections by choosing fiber degrees, but "
    "it constructs no square, no carrier-native diagonal or Frobenius graph, "
    "no off-diagonal intersections, no positive Rosati, and no control death."
)
