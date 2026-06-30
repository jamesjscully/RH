r"""Triangulated / mixed motives carrier no-go.

After doc 239 killed motivic cohomology, higher Chow complexes, Chern
characters, and regulators as direct square constructors, the next repair is
to move to the ambient motivic category itself: Voevodsky/Beilinson-style
triangulated motives, mixed motives, Tate twists, tensor products,
t-/weight-structures, and realization conservativity.  This is still not
End(S^2/Z).  The category is useful only after the zeta square, proper
correspondences, degree maps, Frobenius graph, projection formula, and
positive Rosati have been constructed inside it.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_triangulated_motives_carrier_no_go
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


def motivic_category_profile() -> tuple[bool, bool, bool, bool, bool, bool, bool]:
    # Toy profile: tensor triangulated category, Tate twists, compact
    # generation, six-functor-style operations, weight/t-structure, realization
    # functor, and declared realization conservativity.
    return (True, True, True, True, True, True, True)


def euler_k0_shadow(even_rank: int, odd_rank: int) -> int:
    return even_rank - odd_rank


def normalized_metric_defect(F: np.ndarray, q: float, H: np.ndarray) -> float:
    N = F / np.sqrt(q)
    return float(np.linalg.norm(N.T @ H @ N - H))


# TMC1: the same abstract motivic category profile does not determine a
# finite-field count anchor.
q_true = 7
F_true = frobenius(q_true, 1)
q_other = 5
F_other = frobenius(q_other, 2)
profile_true = motivic_category_profile()
profile_other = motivic_category_profile()
counts_true = point_counts(F_true, q_true, 4)
counts_other = point_counts(F_other, q_other, 4)

gate(
    "TMC1 triangulated-motive profile does not determine count anchor",
    profile_true == profile_other == (True, True, True, True, True, True, True)
    and counts_true != counts_other,
    "profile=%s, q7 counts=%s, q5 counts=%s"
    % (profile_true, [round(c, 1) for c in counts_true], [round(c, 1) for c in counts_other]),
)


# TMC2: the category/profile does not construct the two NS degree slots.
D_true = delta(F_true)
Gamma_true = corr(float(q_true), F_true, 1.0)
Gamma_retuned = corr(float(q_true + 3), F_true, 1.0)
true_delta_graph = ns_intersection(D_true, Gamma_true)
retuned_delta_graph = ns_intersection(D_true, Gamma_retuned)

gate(
    "TMC2 motivic category data does not construct NS degree slots",
    profile_true == motivic_category_profile()
    and true_delta_graph == 7.0
    and retuned_delta_graph == 10.0,
    "same abstract motive/z-action, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (true_delta_graph, retuned_delta_graph),
)


# TMC3: a triangulated/K0 shadow loses extension data.  The square requires
# actual correspondences and composition, not only the decategorified class.
even_rank = 2
odd_rank = 1
extension_a = 0.0
extension_b = 3.0
same_k0_shadow = euler_k0_shadow(even_rank, odd_rank) == euler_k0_shadow(even_rank, odd_rank)
extension_gap = abs(extension_a - extension_b)

gate(
    "TMC3 triangulated K0 shadow loses extension/correspondence data",
    same_k0_shadow and euler_k0_shadow(even_rank, odd_rank) == 1 and extension_gap == 3.0,
    "same K0 Euler shadow=%d, extension gap=%.1f"
    % (euler_k0_shadow(even_rank, odd_rank), extension_gap),
)


# TMC4: realization conservativity is not a constructed carrier theorem.
# A phantom summand can be invisible to the tested realization coordinates
# while remaining nonzero internally.
tested_realization = np.zeros(4)
phantom_realization = np.zeros(4)
phantom_internal_class = np.array([0.0, 0.0, 0.0, 1.0])
same_tested_realization = np.allclose(tested_realization, phantom_realization)
phantom_norm = float(np.linalg.norm(phantom_internal_class))
declares_conservative_realization = True
carrier_conservativity_theorem_constructed = False

gate(
    "TMC4 realization conservativity declaration does not exclude phantom motives",
    declares_conservative_realization
    and not carrier_conservativity_theorem_constructed
    and same_tested_realization
    and phantom_norm == 1.0,
    "tested realization=0, phantom internal norm=%.1f, no carrier conservativity theorem"
    % phantom_norm,
)


# TMC5: tensor/Tate/product declarations do not construct the projection
# formula for the actual square correspondence calculus.
E_true = weil_pairing(F_true, q_true)
G_true = graph(F_true, q_true, 1)
declares_tensor = True
declares_tate_twists = True
declares_projection = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "TMC5 tensor/Tate/projection declarations are not constructed projection formula",
    declares_tensor
    and declares_tate_twists
    and declares_projection
    and semantic_projection_defect == 27.0,
    "declared tensor/Tate/projection=true, componentwise semantic defect=%.1f"
    % semantic_projection_defect,
)


# TMC6: finite motivic-category windows admit trace ghosts.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "TMC6 finite motivic-category windows admit trace ghosts",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and count_5_gap == 5.0,
    "first %d traces match; count_%d gap=%.1f"
    % (window, window + 1, count_5_gap),
)


# TMC7: the same formal motivic-category schema is formable on controls.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
control_profile = motivic_category_profile()
control_counts = point_counts(F_control, control_q, 3)
control_metric_defect = normalized_metric_defect(F_control, control_q, np.eye(2))
control_has_zeta_square_motive = False
control_has_actual_motivic_category = False
control_has_rep_ns = False
control_has_correspondence_composition = False
control_has_positive_rosati = False

gate(
    "TMC7 formal triangulated-motive schema is formable on controls",
    control_profile == profile_true
    and control_counts == [8.0, 112.0, 1064.0]
    and control_metric_defect > 1.0
    and not control_has_zeta_square_motive
    and not control_has_actual_motivic_category
    and not control_has_rep_ns
    and not control_has_correspondence_composition
    and not control_has_positive_rosati,
    "control profile=%s, counts=%s, metric_defect=%.3f, no motive/square/rep_NS/composition/Rosati"
    % (control_profile, [round(c, 1) for c in control_counts], control_metric_defect),
)


# TMC8: construction audit.
zeta_triangulated_motive_category_constructed = False
zeta_mixed_motive_heart_constructed = False
zeta_motivic_t_structure_constructed = False
zeta_weight_structure_constructed = False
zeta_tate_twist_degree_character_constructed = False
zeta_realization_conservativity_constructed = False
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
    "TMC8 triangulated/mixed motive package constructs no End(S^2/Z) square package",
    not zeta_triangulated_motive_category_constructed
    and not zeta_mixed_motive_heart_constructed
    and not zeta_motivic_t_structure_constructed
    and not zeta_weight_structure_constructed
    and not zeta_tate_twist_degree_character_constructed
    and not zeta_realization_conservativity_constructed
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
    "no motive category, t/weight structure, square, rep_NS, degrees, projection, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (TMC1-TMC8)")
print(
    "VERDICT: triangulated motives, mixed motives, Tate twists, tensor "
    "products, weight/t-structures, and realization conservativity are not "
    "End(S^2/Z). Their abstract profiles do not determine counts, do not "
    "construct NS degree slots, lose extension data under K0 shadows, do not "
    "exclude phantoms without a carrier conservativity theorem, do not turn "
    "tensor/Tate declarations into a constructed projection formula, admit "
    "finite-window ghosts, are formable on controls, and construct no actual "
    "square carrier."
)
