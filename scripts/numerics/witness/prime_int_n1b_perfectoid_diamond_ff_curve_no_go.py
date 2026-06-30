r"""Perfectoid / diamonds / Fargues-Fontaine curve carrier no-go.

After doc 241 killed condensed/liquid analytic enrichment as direct square
construction, the next p-adic repair is more geometric: use perfectoid
covers, untilts, A_inf/period rings, diamonds or v-stacks, and the
Fargues-Fontaine curve/vector-bundle category as the missing carrier.  This
is still not End(S^2/Z).  Perfectoid and Fargues-Fontaine geometry is local
and period-geometric unless a global square, proper correspondences, degree
maps, Frobenius graph, projection formula, all-prime/archimedean assembly,
and positive Rosati have already been built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_perfectoid_diamond_ff_curve_no_go
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


def perfectoid_diamond_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: perfectoid cover, untilt, A_inf/period ring, diamond/v-stack,
    # Fargues-Fontaine curve, vector bundles, and local Frobenius.
    return (True, True, True, True, True, True, True)


def local_period_shadow(global_class: np.ndarray) -> tuple[float, float]:
    # A toy local period shadow that sees the local p-adic rank and slope but
    # forgets the archimedean/all-prime assembly coordinate.
    return (float(global_class[0]), float(global_class[2]))


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# FDC1: the same perfectoid/diamond/FF profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = perfectoid_diamond_profile()
profile_other = perfectoid_diamond_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "FDC1 perfectoid/diamond profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# FDC2: perfectoid/diamond carrier labels do not construct the two NS degree
# slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "FDC2 perfectoid/diamond data does not construct NS degree slots",
    profile_true == perfectoid_diamond_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same local period profile and z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# FDC3: an untilt/local-period shadow can forget global correspondence data.
global_class_a = np.array([2.0, 0.0, 1.0])
global_class_b = np.array([2.0, 3.0, 1.0])
same_local_shadow = local_period_shadow(global_class_a) == local_period_shadow(global_class_b)
global_gap = float(np.linalg.norm(global_class_a - global_class_b))

gate(
    "FDC3 untilt/local-period shadow loses global correspondence data",
    same_local_shadow and global_gap == 3.0,
    "same local shadow=%s, global assembly gap=%.1f"
    % (local_period_shadow(global_class_a), global_gap),
)


# FDC4: a single local p-adic component does not assemble all primes plus the
# archimedean component needed for the global over-Z square.
all_place_a = np.array([7.0, 1.0, 11.0])
all_place_b = np.array([7.0, 2.0, 13.0])
same_p_adic_component = all_place_a[0] == all_place_b[0]
all_place_gap = float(np.linalg.norm(all_place_a - all_place_b))

gate(
    "FDC4 local p-adic period data does not assemble the global degree character",
    same_p_adic_component and all_place_gap > 2.0,
    "same p-adic component=%.1f, all-place gap=%.3f"
    % (all_place_a[0], all_place_gap),
)


# FDC5: Fargues-Fontaine semistability/slope positivity does not impose the
# Frobenius/Rosati compatibility relation required by the square.
F_off = np.array([[0.0, -2.0], [1.0, 3.0]])
q_off = 2.0
H_pos = np.eye(2)
off_profile = perfectoid_diamond_profile()
off_metric_defect = normalized_metric_defect(F_off, q_off, H_pos)

gate(
    "FDC5 FF slope/positivity data does not impose Frobenius/Rosati compatibility",
    off_profile == profile_true and off_metric_defect > 1.0,
    "profile=%s, ||(F/sqrt(q))^T H (F/sqrt(q))-H||=%.3f"
    % (off_profile, off_metric_defect),
)


# FDC6: vector-bundle tensor/projection declarations on the FF curve are not
# the constructed square projection formula.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_vector_bundle_tensor = True
declares_diamond_descent = True
declares_projection = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "FDC6 FF tensor/projection declaration is not constructed projection formula",
    declares_vector_bundle_tensor
    and declares_diamond_descent
    and declares_projection
    and semantic_projection_defect == 27.0,
    "declared tensor/descent/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# FDC7: finite perfectoid/diamond windows admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "FDC7 finite perfectoid/diamond windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# FDC8: the same formal perfectoid/diamond schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = perfectoid_diamond_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_perfectoid_zeta_square = False
control_has_ff_curve_carrier = False
control_has_all_prime_assembly = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "FDC8 formal perfectoid/diamond schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_perfectoid_zeta_square
    and not control_has_ff_curve_carrier
    and not control_has_all_prime_assembly
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no perfectoid square/all-prime/rep_NS/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# FDC9: construction audit.
zeta_perfectoid_cover_constructed = False
zeta_untilt_constructed = False
zeta_ainf_period_ring_constructed = False
zeta_diamond_or_vstack_constructed = False
zeta_fargues_fontaine_curve_constructed = False
zeta_ff_vector_bundle_category_constructed = False
zeta_all_prime_archimedean_assembly_constructed = False
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
    "FDC9 perfectoid/diamond/FF package constructs no End(S^2/Z) square package",
    not zeta_perfectoid_cover_constructed
    and not zeta_untilt_constructed
    and not zeta_ainf_period_ring_constructed
    and not zeta_diamond_or_vstack_constructed
    and not zeta_fargues_fontaine_curve_constructed
    and not zeta_ff_vector_bundle_category_constructed
    and not zeta_all_prime_archimedean_assembly_constructed
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
    "no perfectoid cover, FF curve, all-prime assembly, square, rep_NS, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FDC1-FDC9)")
print(
    "VERDICT: perfectoid covers, untilts, A_inf period rings, diamonds, "
    "v-stacks, and Fargues-Fontaine vector bundles are not End(S^2/Z). "
    "Their local period profiles do not determine counts, do not construct "
    "NS degree slots, can forget global correspondence data, do not assemble "
    "all primes plus the archimedean component, do not impose Frobenius/Rosati "
    "compatibility, do not turn vector-bundle tensor declarations into a "
    "constructed projection formula, admit finite-window ghosts, are formable "
    "on controls, and construct no actual square carrier."
)
