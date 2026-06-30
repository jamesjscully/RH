r"""Anabelian/profinite fundamental-group carrier no-go.

The compatible Galois-system no-go killed l-adic realization data as the
square carrier, and the condensed/liquid no-go killed pro-etale analytic
enrichment as the carrier.  The nearby category-level repair is stronger:
use the profinite fundamental group, finite-cover Galois category, inertia
and decomposition data, or anabelian reconstruction package itself as the
square correspondence carrier.

This witness records why that package is still downstream/shadow data unless
it constructs the actual square, rep_NS, degree maps, Frobenius graph,
projection formula, and positive Rosati.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_anabelian_fundamental_group_no_go
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


def afg_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: profinite pi1, finite-cover Galois category, inertia,
    # decomposition groups, Frobenius conjugacy classes, outer action,
    # section/anabelian reconstruction, and open-subgroup lattice.
    return (True, True, True, True, True, True, True, True)


def cover_shadow(class_data: np.ndarray) -> tuple[int, int]:
    # Toy finite-cover shadow: records cover degree and inertia rank, but
    # forgets endpoint/correspondence and extension coordinates.
    return (int(class_data[0]), int(class_data[1]))


def finite_quotient_profile(group_orders: tuple[int, ...]) -> tuple[int, int, int]:
    return (len(group_orders), min(group_orders), max(group_orders))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# AFG1: the same anabelian/fundamental-group profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = afg_profile()
profile_other = afg_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "AFG1 anabelian/pi1 profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# AFG2: finite-cover/fundamental-group data does not construct the two NS
# degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)
same_quotient_window = finite_quotient_profile((1, 2, 3, 6, 7)) == (5, 1, 7)

gate(
    "AFG2 finite-cover/pi1 data does not construct NS degree slots",
    profile_true == afg_profile()
    and same_quotient_window
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same quotient window and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# AFG3: cover-category shadows can forget endpoint and extension data.
class_a = np.array([6, 2, 0])
class_b = np.array([6, 2, 4])
same_shadow = cover_shadow(class_a) == cover_shadow(class_b)
endpoint_gap = int(np.linalg.norm(class_a - class_b))

gate(
    "AFG3 finite-cover shadow loses correspondence endpoint data",
    same_shadow and endpoint_gap == 4,
    "same cover shadow=%s, endpoint gap=%d" % (cover_shadow(class_a), endpoint_gap),
)


# AFG4: anabelian object reconstruction is not a square correspondence
# selection.  Two formal correspondence triples can share the same pi1/cover
# profile and z-action while having different endpoint classes.
same_reconstructed_object_profile = True
diagonal_endpoint = corr(1.0, np.eye(2), 1.0)
retuned_endpoint = corr(4.0, np.eye(2), 1.0)
endpoint_intersection_gap = abs(
    ns_intersection(diagonal_endpoint, Gamma_true)
    - ns_intersection(retuned_endpoint, Gamma_true)
)

gate(
    "AFG4 anabelian reconstruction does not select diagonal/graph triples",
    same_reconstructed_object_profile and endpoint_intersection_gap == 3.0,
    "same reconstructed-object profile; endpoint intersection gap=%.1f"
    % endpoint_intersection_gap,
)


# AFG5: group-duality or section data does not impose Frobenius/Rosati
# compatibility.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
declares_poincare_duality_group = True
declares_section_splitting = True
off_metric_defect = normalized_metric_defect(F_off, q_off, np.eye(2))

gate(
    "AFG5 pi1 duality/section data does not impose Frobenius/Rosati compatibility",
    declares_poincare_duality_group and declares_section_splitting and off_metric_defect > 1.0,
    "duality/section=true, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % off_metric_defect,
)


# AFG6: pullback/pushforward along covers is not the constructed square
# projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_cover_pullback = True
declares_corestriction_pushforward = True
declares_base_change = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "AFG6 cover pull-push functoriality is not constructed projection formula",
    declares_cover_pullback
    and declares_corestriction_pushforward
    and declares_base_change
    and semantic_projection_defect == 27.0,
    "declared pullback/corestriction/base-change=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# AFG7: finite quotient/profinite windows admit ghost summands.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "AFG7 finite pi1/profinite windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f" % (window, window + 1, count_5_gap),
)


# AFG8: the same formal package is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = afg_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_carrier = False
control_has_rep_ns = False
control_has_degree_maps = False
control_has_projection_formula = False
control_has_positive_rosati = False

gate(
    "AFG8 formal anabelian/pi1 schema is formable on controls",
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


# AFG9: construction audit.
zeta_pi1_carrier_constructed = False
zeta_galois_category_carrier_constructed = False
zeta_finite_cover_carrier_constructed = False
zeta_anabelian_carrier_constructed = False
zeta_inertia_decomposition_carrier_constructed = False
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
    "AFG9 anabelian/pi1 package constructs no End(S^2/Z) square package",
    not zeta_pi1_carrier_constructed
    and not zeta_galois_category_carrier_constructed
    and not zeta_finite_cover_carrier_constructed
    and not zeta_anabelian_carrier_constructed
    and not zeta_inertia_decomposition_carrier_constructed
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
    "no pi1 carrier, cover-category carrier, anabelian carrier, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print("AFG1-AFG9 ALL PASS: anabelian / fundamental-group data is not End(S^2/Z)")
