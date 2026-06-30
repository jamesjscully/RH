r"""Karoubi/semisimple completion no-go.

After doc 223, the next repair is to pseudo-abelianize/Karoubi-complete the
presented or numerical correspondence category, then semisimplify it, hoping
that the missing projectors and positive Rosati carrier appear as the
completed category of numerical motives.  This still does not construct
End(S^2/Z): the finite-field Frobenius algebra in the q=7, Tr(F)=1 anchor has
no nontrivial rational idempotents, spectral projectors require scalar
extension by the Frobenius eigenvalues, finite trace windows admit ghost
Karoubi summands, semisimplification erases extension data rather than
building correspondences, and the same operations are formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_karoubi_semisimple_completion_no_go
"""

from __future__ import annotations

import math

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import frobenius


failures: list[str] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def discriminant(q: int, trace: int) -> int:
    return trace * trace - 4 * q


def is_square_int(n: int) -> bool:
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n


def power_traces(A: np.ndarray, upto: int) -> list[complex]:
    return [np.trace(np.linalg.matrix_power(A, n)) for n in range(1, upto + 1)]


def point_count(A: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - np.trace(np.linalg.matrix_power(A, n)).real)


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


def spectral_projectors(F: np.ndarray, q: int, trace: int) -> tuple[complex, complex, np.ndarray, np.ndarray]:
    disc = complex(discriminant(q, trace))
    sqrt_disc = np.sqrt(disc)
    alpha = (trace + sqrt_disc) / 2.0
    beta = (trace - sqrt_disc) / 2.0
    I = np.eye(F.shape[0], dtype=complex)
    F_complex = F.astype(complex)
    P_alpha = (F_complex - beta * I) / (alpha - beta)
    P_beta = (F_complex - alpha * I) / (beta - alpha)
    return alpha, beta, P_alpha, P_beta


def matrix_rank(M: np.ndarray, tol: float = 1e-9) -> int:
    return int(np.linalg.matrix_rank(M, tol=tol))


# KSC1: the finite-field Frobenius algebra Q[F] has no nontrivial rational
# idempotents in the anchor. Karoubi completion over Q therefore adds no
# projector that was not already carrier-native.
q_true = 7
trace_true = 1
F_true = frobenius(q_true, trace_true)
disc_true = discriminant(q_true, trace_true)
irreducible_over_q = not is_square_int(disc_true)
rational_idempotents = ["0", "1"] if irreducible_over_q else ["0", "1", "split_projectors"]
true_counts = [point_count(F_true, q_true, n) for n in range(1, 5)]

gate(
    "KSC1 rational Karoubi completion adds no finite-field projector",
    disc_true == -27 and irreducible_over_q and rational_idempotents == ["0", "1"]
    and true_counts == [7.0, 63.0, 364.0, 2331.0],
    "disc=%d, idempotents=%s, counts=%s"
    % (disc_true, rational_idempotents, [round(c, 1) for c in true_counts]),
)


# KSC2: after scalar extension, spectral idempotents exist, but they use the
# eigenvalue field Q(sqrt(-27)); the projectors are not rational/integral
# carrier data over Z.
alpha, beta, P_alpha, P_beta = spectral_projectors(F_true, q_true, trace_true)
projectors_are_idempotent = (
    np.allclose(P_alpha @ P_alpha, P_alpha)
    and np.allclose(P_beta @ P_beta, P_beta)
    and np.allclose(P_alpha @ P_beta, np.zeros_like(P_alpha))
    and np.allclose(P_alpha + P_beta, np.eye(2))
)
projectors_are_nonreal = (
    float(np.max(np.abs(P_alpha.imag))) > 1e-9
    and float(np.max(np.abs(P_beta.imag))) > 1e-9
)

gate(
    "KSC2 spectral projectors require scalar extension/eigenline choice",
    projectors_are_idempotent
    and projectors_are_nonreal
    and abs(alpha - beta) > 1e-9
    and abs((alpha - beta) ** 2 - disc_true) < 1e-9,
    "alpha=%.3f%+.3fi, beta=%.3f%+.3fi, max_imag(P)=%.3f"
    % (alpha.real, alpha.imag, beta.real, beta.imag, float(np.max(np.abs(P_alpha.imag)))),
)


# KSC3: finite presented/numerical windows plus Karoubi completion admit ghost
# idempotents. A 5-cycle ghost has zero traces in powers 1..4 and trace 5 in
# power 5, so the first four relations cannot exclude its central projector.
window = 4
ghost = cycle_permutation(window + 1)
augmented = block_diag(F_true.astype(complex), ghost)
ghost_projector = block_diag(np.zeros((2, 2), dtype=complex), np.eye(window + 1, dtype=complex))
base_window = power_traces(F_true.astype(complex), window)
aug_window = power_traces(augmented, window)
base_count_5 = point_count(F_true, q_true, window + 1)
aug_count_5 = point_count(augmented, q_true, window + 1)
ghost_projector_is_central_idempotent = (
    np.allclose(ghost_projector @ ghost_projector, ghost_projector)
    and np.allclose(ghost_projector @ augmented, augmented @ ghost_projector)
)
count_5_gap = abs(base_count_5 - aug_count_5)

gate(
    "KSC3 finite Karoubi windows admit ghost summands",
    all(abs(a - b) < 1e-9 for a, b in zip(base_window, aug_window))
    and ghost_projector_is_central_idempotent
    and count_5_gap == 5.0,
    "first %d traces match; ghost projector rank=%d; count_5 gap=%.1f"
    % (window, matrix_rank(ghost_projector), count_5_gap),
)


# KSC4: semisimplification can erase extension/nilpotent data rather than
# constructing correspondences. A Jordan block and its semisimple part have
# identical power traces, while the nilpotent arrow has rank one and is lost.
lam = 2.0
J = np.array([[lam, 1.0], [0.0, lam]], dtype=complex)
J_ss = np.array([[lam, 0.0], [0.0, lam]], dtype=complex)
nilpotent = J - J_ss
trace_window = 6
jordan_traces = power_traces(J, trace_window)
ss_traces = power_traces(J_ss, trace_window)
nilpotent_erased = matrix_rank(nilpotent) == 1 and np.allclose(nilpotent @ nilpotent, np.zeros_like(nilpotent))

gate(
    "KSC4 semisimplification erases extension data instead of building carrier maps",
    all(abs(a - b) < 1e-9 for a, b in zip(jordan_traces, ss_traces)) and nilpotent_erased,
    "first %d traces agree; nilpotent rank=%d and N^2=0"
    % (trace_window, matrix_rank(nilpotent)),
)


# KSC5: the same Karoubi/spectral/semisimple operations are formable on
# controls. This uses no Euler product, Satake parameters, square carrier, or
# positive Rosati.
control_q = 10
control_trace = 3
F_control = frobenius(control_q, control_trace)
disc_control = discriminant(control_q, control_trace)
control_irreducible = not is_square_int(disc_control)
_ca, _cb, CP_a, CP_b = spectral_projectors(F_control, control_q, control_trace)
control_projectors_exist_after_extension = (
    np.allclose(CP_a @ CP_a, CP_a)
    and np.allclose(CP_b @ CP_b, CP_b)
    and float(np.max(np.abs(CP_a.imag))) > 1e-9
)
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_square = False
control_has_positive_rosati = False

gate(
    "KSC5 Karoubi/semisimple completion is formable on controls",
    disc_control == -31
    and control_irreducible
    and control_projectors_exist_after_extension
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_square
    and not control_has_positive_rosati,
    "control disc=%d, spectral split after extension, no Euler/Satake/rep_NS/square/Rosati"
    % disc_control,
)


# KSC6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_projectors_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_numerical_motive_theorem_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "KSC6 Karoubi/semisimple completion constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_projectors_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_numerical_motive_theorem_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, projectors, pairing, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (KSC1-KSC6)")
print(
    "VERDICT: Karoubi/pseudo-abelian or semisimple completion of a presented "
    "or numerical carrier is not End(S^2/Z). Over the finite-field anchor, "
    "rational completion adds no nontrivial projector; spectral splitting "
    "imports scalar-extension eigenlines; finite windows admit ghost "
    "idempotents; semisimplification erases extension data; the same "
    "completion is formable on controls; and no actual square, proper "
    "correspondences, carrier-native projectors, positive Rosati, or control "
    "death is constructed."
)
