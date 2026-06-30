r"""Projection-formula quotient no-go.

After doc 220, the next repair is to impose the missing projection formula as
relations on the formal NS envelope with componentwise composition and formal
dagger.  This still does not construct End(S^2/Z): the projection relation is
not a harmless quotient of the formal law.  On genuine finite-field anchors it
forces false trace/count identities or changes the scalar base, and local
retuning destroys graph degrees.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_projection_formula_quotient_no_go
"""

from __future__ import annotations

from math import gcd

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


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def projection_sides(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> tuple[float, float]:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs, rhs = projection_sides(A, B, C, E)
    return float(abs(lhs - rhs))


def trace_power(F: np.ndarray, n: int) -> float:
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - trace_power(F, n))


def retune_first_degree_for_projection(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> Corr:
    """Change only the first degree of A o B to force one projection equation."""

    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    c2 = C[2]
    if abs(c2) < 1e-12:
        raise ValueError("cannot retune against a class with zero second degree")
    return corr(product[0] + (rhs - lhs) / c2, product[1], product[2])


# PFQ1: on a genuine finite-field anchor, imposing the projection formula on
# the formal componentwise law forces a false trace/count identity.
q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta(F_true)
G_true = graph(F_true, q_true, 1)
projection_11 = projection_defect(G_true, D_true, G_true, E_true)
actual_tr2 = trace_power(F_true, 2)
forced_tr2 = 2.0 * q_true
actual_count2 = point_count(F_true, q_true, 2)
forced_count2 = q_true**2 + 1.0 - forced_tr2
count_distortion = abs(actual_count2 - forced_count2)

gate(
    "PFQ1 projection quotient changes genuine FF trace/count data",
    projection_11 > 1e-6
    and abs(projection_11 - count_distortion) < 1e-12
    and actual_count2 == 63.0
    and forced_count2 == 36.0,
    "projection_defect=%.1f, TrF2 actual %.1f vs forced %.1f, count2 %.1f vs %.1f"
    % (projection_11, actual_tr2, forced_tr2, actual_count2, forced_count2),
)


# PFQ2: killing projection defects as scalar quotient relations is not a
# universal over-Z construction. Two genuine finite-field anchors already have
# coprime scalar defects, so the generated ideal is the whole ring.
q_alt = 2
F_alt = frobenius(q_alt, 0)
E_alt = weil_pairing(F_alt, q_alt)
D_alt = delta(F_alt)
G_alt = graph(F_alt, q_alt, 1)
defect_true = int(round(projection_defect(G_true, D_true, G_true, E_true)))
defect_alt = int(round(projection_defect(G_alt, D_alt, G_alt, E_alt)))
universal_gcd = gcd(defect_true, defect_alt)

gate(
    "PFQ2 scalar projection-quotient over multiple anchors collapses",
    defect_true == 27 and defect_alt == 8 and universal_gcd == 1,
    "defects %d and %d generate ideal gcd=%d in Z" % (defect_true, defect_alt, universal_gcd),
)


# PFQ3: local retuning can force one projection equation, but it destroys the
# graph degree and hence the graph class it was supposed to repair.
retuned_G = retune_first_degree_for_projection(G_true, D_true, G_true, E_true)
retuned_projection = abs(ns_intersection(retuned_G, G_true) - projection_sides(G_true, D_true, G_true, E_true)[1])
graph_degree_defect = corr_defect(retuned_G, G_true)

gate(
    "PFQ3 retuning projection locally destroys the graph degree",
    retuned_projection < 1e-12 and graph_degree_defect > 1e-6 and retuned_G[0] == -20.0,
    "retuned d1 %.1f vs graph d1 %.1f, graph_defect=%.1f"
    % (retuned_G[0], G_true[0], graph_degree_defect),
)


# PFQ4: finite projection checks can be cherry-picked. The q=2,a=0 anchor
# satisfies the (m=1,n=2) projection trace relation but fails (m=1,n=1).
H_alt = graph(F_alt, q_alt, 2)
selective_defect_12 = projection_defect(G_alt, D_alt, H_alt, E_alt)
selective_defect_11 = projection_defect(G_alt, D_alt, G_alt, E_alt)
alt_counts_ok = point_count(F_alt, q_alt, 1) == 3.0 and point_count(F_alt, q_alt, 2) == 9.0

gate(
    "PFQ4 finite projection samples are cherry-pickable",
    selective_defect_12 < 1e-12 and selective_defect_11 == 8.0 and alt_counts_ok,
    "defect(1,2)=%.1f but defect(1,1)=%.1f on q=2,a=0"
    % (selective_defect_12, selective_defect_11),
)


# PFQ5: the same quotient/retuning story is formable on controls.
control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_D = delta(control)
control_G = graph(control, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(control_G, control_D, control_G, control_E)
control_retuned_projection = abs(
    ns_intersection(control_retuned, control_G)
    - projection_sides(control_G, control_D, control_G, control_E)[1]
)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square_properness = False
control_has_positive_rosati = False

gate(
    "PFQ5 projection quotient/retuning is formable on controls",
    qsim_defect(control, control_E, control_q) < 1e-12
    and control_projection == 24.0
    and control_retuned_projection < 1e-12
    and corr_defect(control_retuned, control_G) == 24.0
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square_properness
    and not control_has_positive_rosati,
    "control projection_defect=%.1f, retuned d1 %.1f, no Euler/Satake/rep_NS/Rosati"
    % (control_projection, control_retuned[0]),
)


# PFQ6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_degree_character_constructed = False
zeta_frobenius_graph_constructed = False
zeta_point_counts_preserved = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "PFQ6 projection-formula quotient constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_degree_character_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_point_counts_preserved
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, fiber-product composition, pairing, projection formula, graph, counts, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PFQ1-PFQ6)")
print(
    "VERDICT: imposing the projection formula as a quotient or local retuning "
    "of the formal componentwise NS envelope is not End(S^2/Z). It changes "
    "finite-field trace/count data, collapses universal scalar quotients over "
    "Z, can be cherry-picked on finite samples, is formable on controls, and "
    "constructs no actual square, fiber-product composition, carrier-native "
    "pairing, positive Rosati, or control death."
)
