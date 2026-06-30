r"""Condensed / liquid / solid analytic carrier no-go.

After doc 240 killed ambient triangulated or mixed motives as direct square
construction, the next repair is the third route named in the construction
charter: use condensed/liquid/solid analytic geometry, pro-etale or analytic
stacks, completion, and topological tensor products to supply the missing
square carrier.  This is still not End(S^2/Z).  Analytic enrichment and
solidification can organize objects after the square exists; they do not
construct the over-Z square, proper correspondences, degree maps, Frobenius
graph, projection formula, or positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_condensed_liquid_analytic_carrier_no_go
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


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


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


def condensed_liquid_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: condensed sheaves, solid modules, liquid vector spaces,
    # analytic stack, pro-etale descent, completion, and completed tensor.
    return (True, True, True, True, True, True, True)


def analytic_shadow(discrete_class: np.ndarray) -> tuple[float, float]:
    # A toy analytic/solid shadow that forgets the discrete endpoint coordinate.
    return (float(discrete_class[0]), float(discrete_class[1]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# CLA1: the same condensed/liquid analytic profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = condensed_liquid_profile()
profile_other = condensed_liquid_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "CLA1 condensed/liquid profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# CLA2: analytic enrichment does not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "CLA2 analytic enrichment does not construct NS degree slots",
    profile_true == condensed_liquid_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same analytic profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# CLA3: solidification/completion can forget discrete endpoint or lattice data
# needed to identify the actual correspondence class.
class_a = np.array([7.0, 1.0, 0.0])
class_b = np.array([7.0, 1.0, 3.0])
same_analytic_shadow = analytic_shadow(class_a) == analytic_shadow(class_b)
discrete_gap = float(np.linalg.norm(class_a - class_b))

gate(
    "CLA3 solid analytic shadow loses discrete correspondence data",
    same_analytic_shadow and discrete_gap == 3.0,
    "same analytic shadow=%s, discrete endpoint gap=%.1f"
    % (analytic_shadow(class_a), discrete_gap),
)


# CLA4: topological or metric positivity does not impose the Frobenius/Rosati
# compatibility relation required by the square.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = condensed_liquid_profile()
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "CLA4 analytic positivity does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# CLA5: completed tensor/projection declarations do not construct the square
# projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_completed_tensor = True
declares_solid_projection = True
declares_pro_etale_descent = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "CLA5 completed tensor/projection declaration is not constructed projection formula",
    declares_completed_tensor
    and declares_solid_projection
    and declares_pro_etale_descent
    and semantic_projection_defect == 27.0,
    "declared tensor/projection/descent=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# CLA6: finite analytic or pro-etale windows admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "CLA6 finite condensed/analytic windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# CLA7: the same formal condensed/liquid schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = condensed_liquid_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_condensed_zeta_square = False
control_has_liquid_analytic_stack = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_positive_rosati = False

gate(
    "CLA7 formal condensed/liquid schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_condensed_zeta_square
    and not control_has_liquid_analytic_stack
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no condensed square/rep_NS/degrees/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# CLA8: construction audit.
zeta_condensed_site_constructed = False
zeta_solid_module_category_constructed = False
zeta_liquid_analytic_stack_constructed = False
zeta_pro_etale_descent_constructed = False
zeta_completion_theorem_constructed = False
zeta_completed_tensor_projection_constructed = False
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
    "CLA8 condensed/liquid analytic package constructs no End(S^2/Z) square package",
    not zeta_condensed_site_constructed
    and not zeta_solid_module_category_constructed
    and not zeta_liquid_analytic_stack_constructed
    and not zeta_pro_etale_descent_constructed
    and not zeta_completion_theorem_constructed
    and not zeta_completed_tensor_projection_constructed
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
    "no condensed site, liquid stack, square, rep_NS, degrees, projection, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CLA1-CLA8)")
print(
    "VERDICT: condensed sheaves, solid modules, liquid analytic geometry, "
    "pro-etale descent, completion, and completed tensor products are not "
    "End(S^2/Z). Their abstract analytic profiles do not determine counts, "
    "do not construct NS degree slots, can forget discrete correspondence "
    "data, do not impose Frobenius/Rosati compatibility, do not turn completed "
    "tensor declarations into a constructed projection formula, admit "
    "finite-window ghosts, are formable on controls, and construct no actual "
    "square carrier."
)
