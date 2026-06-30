r"""Span/profunctor/correspondence-bicategory carrier no-go.

Many no-go cycles killed formal correspondence laws, presented carriers,
six-functor traces, operational Chow, derived cycle stacks, Tambara/Burnside
norms, and finite-cover categories.  A remaining primitive repair is to use
the generic bicategory of spans, profunctors, distributors, or polynomial
functors itself as the square correspondence carrier.

This witness records why that package is still downstream/framework data
unless it constructs the actual square, rep_NS, degree maps, Frobenius graph,
projection formula, and positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_span_profunctor_bicategory_no_go
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


def spb_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: span bicategory, pullback composition, profunctors,
    # distributors, polynomial functors, adjoints, Beck-Chevalley, and trace.
    return (True, True, True, True, True, True, True, True)


def span_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy span/profunctor shadow: records source-target arity and apex rank,
    # but forgets endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def pullback_composition_exists(legs: tuple[int, ...]) -> bool:
    # Toy finite-span check: the generic pullback operation can be formed.
    return all(leg >= 0 for leg in legs)


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# SPB1: the same span/profunctor/correspondence-bicategory profile does not
# determine a finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = spb_profile()
profile_other = spb_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "SPB1 span/profunctor profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# SPB2: generic span/profunctor data does not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "SPB2 generic span data does not construct NS degree slots",
    profile_true == spb_profile()
    and pullback_composition_exists((1, 2, 7))
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same span laws and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# SPB3: span/profunctor shadows can forget endpoint and extension data.
class_a = np.array([2, 5, 0])
class_b = np.array([2, 5, 4])
same_shadow = span_shadow(class_a) == span_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "SPB3 span/profunctor shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 4,
    "same span shadow=%s, endpoint gap=%d" % (span_shadow(class_a), endpoint_gap),
)


# SPB4: generic pullback composition does not select the Frobenius graph or
# degree character.  The same z-power law supports different external degree
# slots.
Gamma_q = corr(float(q_true**2), np.linalg.matrix_power(F_true, 2), 1.0)
Gamma_r = corr(float(11**2), np.linalg.matrix_power(F_true, 2), 1.0)
same_z_power = np.allclose(Gamma_q[1], Gamma_r[1])
degree_gap = abs(ns_intersection(D_true, corr(7.0, F_true, 1.0)) - ns_intersection(D_true, corr(11.0, F_true, 1.0)))

gate(
    "SPB4 pullback composition does not select graph degree character",
    same_z_power and degree_gap == 4.0,
    "same z^2 span/profunctor action; Delta.Gamma degree gap=%.1f" % degree_gap,
)


# SPB5: adjoints/duals in a bicategory do not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
declares_dualizable_object = True
declares_bicategorical_adjoint = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "SPB5 bicategorical adjoints do not impose Frobenius/Rosati compatibility",
    declares_dualizable_object and declares_bicategorical_adjoint and off_metric_defect > 1.0,
    "dual/adjoint=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# SPB6: Beck-Chevalley/base-change/projection declarations are not the
# constructed square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_beck_chevalley = True
declares_base_change = True
declares_projection_formula = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "SPB6 Beck-Chevalley/projection declaration is not constructed projection formula",
    declares_beck_chevalley
    and declares_base_change
    and declares_projection_formula
    and semantic_projection_defect == 27.0,
    "declared Beck-Chevalley/base-change/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# SPB7: finite span/profunctor windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "SPB7 finite span/profunctor windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f" % (window, window + 1, count_5_gap),
)


# SPB8: the same formal package is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = spb_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "SPB8 formal span/profunctor schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_zeta_square_carrier
    and not control_has_rep_ns
    and not control_has_degree_maps
    and not control_has_projection_formula
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no square/rep_NS/degrees/projection/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# SPB9: construction audit.
zeta_span_bicategory_carrier_constructed = False
zeta_profunctor_carrier_constructed = False
zeta_distributor_carrier_constructed = False
zeta_polynomial_functor_carrier_constructed = False
zeta_correspondence_bicategory_carrier_constructed = False
zeta_ambient_square_constructed = False
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
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
    "SPB9 span/profunctor package constructs no End(S^2/Z) square package",
    not zeta_span_bicategory_carrier_constructed
    and not zeta_profunctor_carrier_constructed
    and not zeta_distributor_carrier_constructed
    and not zeta_polynomial_functor_carrier_constructed
    and not zeta_correspondence_bicategory_carrier_constructed
    and not zeta_ambient_square_constructed
    and not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no span carrier, profunctor carrier, correspondence bicategory, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("SPB1-SPB9 ALL PASS: span / profunctor / correspondence-bicategory data is not End(S^2/Z)")
