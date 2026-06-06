"""oriented_hodge_pairing.py -- AGENDA NEXT #1 (CONSTRUCT, load-bearing).

THE CORRECTED TARGET, after the ENTIRE REAL-form family closed (zero_in_form_pairing.py, DONE top)
and the conjugation-INVARIANT Hermitian form H = A + i.omega closed (complex_structure_pairing.py).

  The agenda's named next axiom: a form on which COMPLEX CONJUGATION acts NON-trivially -- a genuine
  Hodge (p,q) bigrading where H^{p,q} and H^{q,p} are DISTINGUISHED (an oriented (1,0)-form / a
  polarization with a chosen ORIENTATION), NOT the conjugation-INVARIANT Hermitian A + i.omega of
  complex_structure_pairing (that kept inertia real and Sylvester-locked).

  CONCRETE CONSTRUCTION (verbatim from AGENDA NEXT #1). Build the holomorphic (1,0) projector
        P^{1,0} = 1/2 (Id - i J),   P^{0,1} = 1/2 (Id + i J)   (J^2 = -Id, J the complex structure)
  and pair the plant against the ORIENTED SIGNED Hodge weight (NOT the conjugation-symmetric SUM):
        Q(x) = <P^{1,0} x, P^{1,0} x>_A  -  <P^{0,1} x, P^{0,1} x>_A.
  Test whether THAT flips on-line vs off-line. The off-line plant must inject a genuine gamma
  (height/phase), not just the conjugation-symmetric real Weil pair (beta, 1-beta).

------------------------------------------------------------------------------------------------------
THE DECISIVE ALGEBRA (computed here, exact), the honest prior that must be confronted FIRST.

  Write A symmetric (the Hermitian inner product <x,y>_A = x^* A y), J the A-orthogonal complex
  structure (J^2=-Id, J^T A J = A). The signed Hodge weight, as a Hermitian matrix, is
        Q = (P^{1,0})^* A P^{1,0} - (P^{0,1})^* A P^{0,1}.
  Expanding P^{1,0}=1/2(Id - iJ): a short computation (verified to ~1e-15) gives
        Q = -(i/2)(A J - J^T A).
  But A-orthogonality + J^2=-Id give the EXACT identity  J^T A = -A J  (proved in
  complex_structure_pairing.py). Substituting,
        Q = -(i/2)(A J - (-A J)) = -i (A J) = -i.omega,        omega = A J the Kahler 2-form.
  So the ORIENTED signed Hodge weight is Q = -i.omega, a FIXED HERMITIAN matrix (omega real
  antisymmetric => -i.omega Hermitian). THIS IS THE HONEST PRIOR: the "oriented" form is, after the
  A-orthogonality identity, ANOTHER fixed Hermitian background -- the imaginary/Kahler part of the very
  H = A + i.omega that complex_structure_pairing.py already closed. The decisive question is whether
  pairing the plant against -i.omega ESCAPES the Sylvester lock that A + i.omega did not.

  THE WALL, stated exactly. The prime-shift plant T is REAL. For a real T and a Hermitian Q,
        T^T Q T = T^* Q T   is a *-CONGRUENCE,  so inertia(T^T Q T) = inertia(Q) for det T != 0
  by Sylvester's law of inertia for Hermitian forms. So the SIGNED Hodge inertia is locked to
  inertia(Q) = inertia(-i.omega) -- a DH-shared, FE-derived fixed background -- for ANY real plant,
  exactly as for A + i.omega. The "orientation" (sign Hodge weight vs symmetric sum) changes WHICH
  fixed Hermitian matrix (-i.omega vs A) but NOT the Sylvester lock.

  THE STEELMAN the agenda explicitly asks for. To make conjugation act non-trivially the PLANT itself
  must be COMPLEX / holomorphic -- inject a genuine gamma (height/phase), break rho<->rho-bar. We
  therefore ALSO test:
    (S1) a genuinely COMPLEX plant T_c carrying an oriented phase e^{i gamma u} (the (1,0) part only,
         NOT the conjugation-symmetric cos(gamma u)) -- does the signed-Hodge inertia of T_c^* Q T_c
         flip on-line vs off-line? A complex congruence is NOT inertia-preserving, so a flip is POSSIBLE
         in principle; the question is whether the zeta-intrinsic oriented plant produces one.
    (S2) the on-line vs off-line comparison must use plants that differ in gamma/Im, since Q = -i.omega
         and conjugation gamma -> -gamma. We compare an oriented off-line plant (beta=0.6, +gamma) to
         the on-line (beta=0.5, +gamma) AND to its conjugate (beta=0.6, -gamma) to expose whether Q
         distinguishes the two orientations (the whole point of an oriented form).

WHAT THIS MODULE COMPUTES (executable):
  (O1) Build A (chiral archimedean Gram), the A-orthogonal J (J^2=-Id, J^T A J=A) -- reuse the
       certified construction from complex_structure_pairing.
  (O2) Build the oriented signed Hodge form Q two ways and certify they agree: directly from the
       projectors P^{1,0},P^{0,1}, and via the closed form -i.omega. Certify Q = -i.omega (the
       collapse), Q Hermitian, and inertia(Q).
  (O3) THE FALSIFIER. (a) REAL FE-pair plant (beta,1-beta): inertia(T^T Q T) on-line vs off-line --
       Sylvester-locked, expected NO flip. (b) STEELMAN complex oriented plant T_c(beta,+gamma):
       inertia(T_c^* Q T_c) on-line vs off-line vs conjugate-orientation. Plus three axes.

Tags: [THM] (Q = -i.omega exact via J^T A = -A J; real plant => *-congruence => Sylvester-locked),
[computed] (the collapse, the inertiae, the real- and complex-plant flip tests, three axes),
[CONJ] (whether ANY oriented/complex zeta-intrinsic plant escapes the lock).

Run:  python3 -m scripts.numerics.witness.oriented_hodge_pairing
"""
from __future__ import annotations

import numpy as np

from .theta_twisted_pairing import (
    chiral_centers, theta_matrix, archimedean_gram, correspondence_operator,
    plant_in_operator, plant_FE_pair, signature, sym,
)
from .complex_structure_pairing import (
    complex_structure, a_compatible_complex_structure, herm_signature,
)


# ----------------------------------------------------------------------------------------------------
# The oriented Hodge projectors and the SIGNED Hodge weight form.
# ----------------------------------------------------------------------------------------------------

def hodge_projectors(J):
    """P^{1,0} = 1/2(Id - iJ), P^{0,1} = 1/2(Id + iJ). With J^2 = -Id these are the holomorphic /
    antiholomorphic projectors: (P10)^2 = P10, (P01)^2 = P01, P10 P01 = 0, P10 + P01 = Id."""
    k = J.shape[0]
    Id = np.eye(k)
    P10 = 0.5 * (Id - 1j * J)
    P01 = 0.5 * (Id + 1j * J)
    return P10, P01


def signed_hodge_form(A, J):
    """The ORIENTED signed Hodge weight as a Hermitian matrix:
        Q = (P10)^* A P10 - (P01)^* A P01.
    Returns the complex Hermitian Q (the form x |-> x^* Q x is the signed Hodge weight)."""
    P10, P01 = hodge_projectors(J)
    Ac = A.astype(complex)
    Q = P10.conj().T @ Ac @ P10 - P01.conj().T @ Ac @ P01
    return Q


def oriented_plant(T_base, centers, width, beta, gamma, M=60):
    """A genuinely COMPLEX, ORIENTED plant: inject the (1,0) phase e^{i gamma u} (NOT the conjugation-
    symmetric cos(gamma u) of plant_in_operator). This breaks rho<->rho-bar: the conjugate orientation
    is gamma -> -gamma, a DIFFERENT plant. Off-line modulus carried by e^{(beta-1/2)|u|} as usual."""
    k = len(centers)
    dT = np.zeros((k, k), dtype=complex)
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            s = 0.0 + 0.0j
            for n in range(2, M):
                u = np.log(n)
                ov = (np.exp(-(ci - cj - u) ** 2 / (4 * width ** 2))
                      + np.exp(-(ci - cj + u) ** 2 / (4 * width ** 2)))
                s += np.exp(1j * gamma * u) * np.exp((beta - 0.5) * u) * ov / n
            dT[i, j] = s
    return T_base.astype(complex) + dT


def run(base_centers=None, width=0.5, gamma=14.0):
    if base_centers is None:
        base_centers = [np.log(2), np.log(3), np.log(5), np.log(7)]

    centers, theta_perm = chiral_centers(base_centers)
    Theta = theta_matrix(theta_perm)
    k = len(centers)

    A = archimedean_gram(centers, width)
    A_dh = archimedean_gram(centers, width)
    arch_shared = float(np.max(np.abs(A - A_dh)))

    T_z = correspondence_operator("zeta", centers, width)
    T_d = correspondence_operator("dh", centers, width)

    # (O1) build J on the FE-paired even-dim support (reuse certified construction)
    J_block, support = complex_structure(theta_perm)
    m = support
    A_s = A[np.ix_(m, m)]
    Id_s = np.eye(int(np.sum(m)))
    J_s = a_compatible_complex_structure(A_s)

    J2_defect = float(np.linalg.norm(J_s @ J_s + Id_s))
    A_orth_defect = float(np.linalg.norm(J_s.T @ A_s @ J_s - A_s))
    # the exact identity J^T A = -A J (the engine of the collapse)
    JTA_identity = float(np.linalg.norm(J_s.T @ A_s + A_s @ J_s))

    # (O2) the oriented signed Hodge form Q, two ways, and the COLLAPSE Q = -i.omega
    Q = signed_hodge_form(A_s, J_s)
    omega = A_s @ J_s
    Q_closed = -1j * omega
    collapse_defect = float(np.linalg.norm(Q - Q_closed))      # Q = -i.omega ?
    Q_hermitian = float(np.linalg.norm(Q - Q.conj().T))
    sig_Q = herm_signature(Q)
    # contrast: the conjugation-SYMMETRIC sum (what complex_structure_pairing closed)
    P10, P01 = hodge_projectors(J_s)
    Q_sum = P10.conj().T @ A_s.astype(complex) @ P10 + P01.conj().T @ A_s.astype(complex) @ P01
    sum_is_A = float(np.linalg.norm(Q_sum - A_s.astype(complex)))   # the SYM sum = A (conj-invariant)

    # ---- axis 1: Euler-borne ----
    op_diff = float(np.max(np.abs(T_z - T_d)))
    euler_borne = op_diff > 1e-6

    # restrict plants to support
    def restr(Tm):
        return Tm[np.ix_(m, m)]

    # (O3a) REAL FE-pair plant (beta, 1-beta) -- the conjugation-symmetric real Weil pair
    T_on_r = restr(plant_FE_pair(T_z, centers, width, beta=0.5, gamma=gamma))
    T_off_r = restr(plant_FE_pair(T_z, centers, width, beta=0.6, gamma=gamma))
    detT_on = float(abs(np.linalg.det(T_on_r)))

    def herm_pair_real(Tm):
        return Tm.T @ Q @ Tm            # T real => T^T Q T = T^* Q T, a *-congruence

    sig_real_on = herm_signature(herm_pair_real(T_on_r))
    sig_real_off = herm_signature(herm_pair_real(T_off_r))
    real_flips = sig_real_on != sig_real_off

    # (O3b) STEELMAN: genuinely COMPLEX oriented plant T_c(beta, +gamma) and its conjugate (-gamma)
    Tc_on = restr(oriented_plant(T_z, centers, width, beta=0.5, gamma=gamma))
    Tc_off = restr(oriented_plant(T_z, centers, width, beta=0.6, gamma=gamma))
    Tc_off_conj = restr(oriented_plant(T_z, centers, width, beta=0.6, gamma=-gamma))
    detTc_on = float(abs(np.linalg.det(Tc_on)))

    # does the complex plant couple to J (commute)? if it commutes, it cannot move the Hodge inertia
    TcJ_comm = float(np.linalg.norm(Tc_on @ J_s - J_s @ Tc_on))

    def herm_pair_cplx(Tm):
        return Tm.conj().T @ Q @ Tm     # genuine *-congruence by a COMPLEX T -- inertia CAN move

    sig_cplx_on = herm_signature(herm_pair_cplx(Tc_on))
    sig_cplx_off = herm_signature(herm_pair_cplx(Tc_off))
    sig_cplx_off_conj = herm_signature(herm_pair_cplx(Tc_off_conj))
    cplx_flips = sig_cplx_on != sig_cplx_off
    # the ORIENTATION test: does Q distinguish +gamma from -gamma off-line? (the whole point)
    orientation_distinguishes = sig_cplx_off != sig_cplx_off_conj

    sees_zeros = real_flips or cplx_flips or orientation_distinguishes

    # ---- axis 3: independent ----
    # Q = -i.omega = -i.A J is assembled from the DH-shared A and the FE-derived J. Even a complex-plant
    # flip would be the Weil/explicit-formula coupling (the primes coupled to the line), not independent.
    independent = False

    if not euler_borne:
        verdict = "DISPERSING"
    elif not sees_zeros:
        verdict = "RH-SILENT"
    elif not independent:
        verdict = "CIRCULAR"
    else:
        verdict = "FORCING"

    return {
        "support_dim (FE-paired even)": int(np.sum(m)),
        "full_dim (chiral)": k,
        "arch_metric_DH_shared (max|A_z-A_dh|)": arch_shared,
        "--- (O1) complex structure J certified ---": "",
        "||J^2 + Id||": J2_defect,
        "||J^T A J - A|| (A-orthogonal)": A_orth_defect,
        "||J^T A + A J|| (the EXACT identity J^T A=-A J)": JTA_identity,
        "--- (O2) the ORIENTED signed Hodge form Q ---": "",
        "||Q - (-i.omega)||  (THE COLLAPSE: Q = -i.omega)": collapse_defect,
        "||Q - Q^dagger||  (Q Hermitian)": Q_hermitian,
        "inertia(Q) = inertia(-i.omega)": sig_Q,
        "||Q_sum - A||  (conj-SYMMETRIC sum = A, conj-invariant)": sum_is_A,
        "--- axis 1: Euler-borne ---": "",
        "axis1_euler_borne": euler_borne,
        "operator_diff_z_DH": op_diff,
        "--- (O3a) REAL FE-pair plant (Sylvester-locked) ---": "",
        "det T_on (real plant, !=0)": detT_on,
        "signed-Hodge inertia(T^T Q T) on-line  (real plant)": sig_real_on,
        "signed-Hodge inertia(T^T Q T) off-line (real plant)": sig_real_off,
        "  REAL plant flips? (expect NO -- *-congruence)": real_flips,
        "--- (O3b) STEELMAN: COMPLEX oriented plant e^{i gamma u} ---": "",
        "det T_c on (complex plant, !=0)": detTc_on,
        "||[T_c, J]|| (complex plant couples to J?)": TcJ_comm,
        "signed-Hodge inertia(T_c^* Q T_c) on-line": sig_cplx_on,
        "signed-Hodge inertia(T_c^* Q T_c) off-line (+gamma)": sig_cplx_off,
        "signed-Hodge inertia(T_c^* Q T_c) off-line (-gamma, conj)": sig_cplx_off_conj,
        "  COMPLEX plant flips on/off-line?": cplx_flips,
        "  Q distinguishes +gamma vs -gamma (oriented?)": orientation_distinguishes,
        "--- axes 2,3 ---": "",
        "axis2_sees_zeros": sees_zeros,
        "axis3_independent": independent,
        "VERDICT": verdict,
    }


def summary():
    np.set_printoptions(precision=4, suppress=True)
    print("oriented_hodge_pairing.py -- the ORIENTED signed Hodge weight (NEXT #1, corrected target)\n")
    print("Target: a form on which complex conjugation acts NON-trivially -- the SIGNED Hodge weight")
    print("Q(x) = <P10 x,P10 x>_A - <P01 x,P01 x>_A, P10=1/2(Id-iJ), NOT the conjugation-symmetric sum")
    print("(= A) that complex_structure_pairing closed. Test: does Q flip on/off-line, with the off-line")
    print("plant injecting a genuine gamma/phase (oriented), not just the real Weil pair (beta,1-beta)?\n")

    results = {}
    for label, base in [("chiral [l2,l3,l5,l7]", [np.log(2), np.log(3), np.log(5), np.log(7)]),
                        ("chiral [l2,l3,l5]", [np.log(2), np.log(3), np.log(5)]),
                        ("chiral [l2,l3,l5,l7,l11]",
                         [np.log(2), np.log(3), np.log(5), np.log(7), np.log(11)])]:
        v = run(base)
        results[label] = v
        print(f"=== {label} (support dim {v['support_dim (FE-paired even)']}) ===")
        for kk, vv in v.items():
            if kk in ("support_dim (FE-paired even)",):
                continue
            if kk.startswith("---"):
                print(f"  {kk}")
            else:
                print(f"    {kk:54s}: {vv}")
        print()

    print("[interpretation -- the decisive measurement]")
    v = results["chiral [l2,l3,l5,l7]"]
    print(f"  (O2) THE COLLAPSE: ||Q - (-i.omega)|| = "
          f"{v['||Q - (-i.omega)||  (THE COLLAPSE: Q = -i.omega)']:.2e} -- the ORIENTED signed Hodge")
    print(f"       weight IS -i.omega (the Kahler 2-form), a FIXED Hermitian matrix. "
          f"inertia(Q)={v['inertia(Q) = inertia(-i.omega)']}.")
    print(f"       (the conjugation-SYMMETRIC sum = A: ||Q_sum - A||="
          f"{v['||Q_sum - A||  (conj-SYMMETRIC sum = A, conj-invariant)']:.2e}.)")
    print(f"  (O3a) REAL FE-pair plant: signed-Hodge inertia on-line "
          f"{v['signed-Hodge inertia(T^T Q T) on-line  (real plant)']} vs off-line "
          f"{v['signed-Hodge inertia(T^T Q T) off-line (real plant)']}; flips? "
          f"{v['  REAL plant flips? (expect NO -- *-congruence)']}.")
    print(f"  (O3b) STEELMAN complex oriented plant: on-line "
          f"{v['signed-Hodge inertia(T_c^* Q T_c) on-line']} vs off-line(+g) "
          f"{v['signed-Hodge inertia(T_c^* Q T_c) off-line (+gamma)']} vs off-line(-g) "
          f"{v['signed-Hodge inertia(T_c^* Q T_c) off-line (-gamma, conj)']};")
    print(f"        flips on/off? {v['  COMPLEX plant flips on/off-line?']}; "
          f"distinguishes +/-gamma? {v['  Q distinguishes +gamma vs -gamma (oriented?)']}.")
    print(f"  VERDICT: {v['VERDICT']}")


if __name__ == "__main__":
    summary()
