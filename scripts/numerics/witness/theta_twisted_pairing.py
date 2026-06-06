"""theta_twisted_pairing.py -- AGENDA NEXT #1 (CONSTRUCT, load-bearing).

THE SHARPENED TARGET (after hecke_correspondence.py closed the SYMMETRIC self-pairing).
  hecke_correspondence.py established a TWO-PART result on the zeta-intrinsic non-product Hecke
  correspondence T (the explicit-formula prime side AS AN OPERATOR):
    (1) indecomposability ACHIEVED -- T is genuinely non-product (||[T,A]||~30-47 >> 0 while
        ||[Id,A]||=0), and
    (2) BUT its graph SELF-INTERSECTION F = T^T A T is a SYMMETRIC CONGRUENCE of the DH-shared
        archimedean metric A; by SYLVESTER's law of inertia sig(F)=sig(A) for ANY invertible plant,
        so the signature is congruence-locked to the DH-shared A -> RH-SILENT.

  The obstruction was renamed precisely: SYMMETRIC CONGRUENCES PRESERVE INERTIA. The agenda's
  sharpened sub-target (NEXT #1) is therefore a pairing that BREAKS the A-congruence:

      a PHASE-carrying / theta-TWISTED pairing  F_theta := T^T A theta T   (theta = the FE involution)

  whose signature is NOT congruence-locked to A -- i.e. it should retain the off-diagonal/phase info
  that the symmetrization T^T A T throws away. The Sylvester argument does NOT apply to T^T A theta T
  because (a) theta need not be positive-definite and (b) the form need not be symmetric, so inertia is
  not preserved. The QUESTION this module answers: does inserting theta GENUINELY break the
  congruence-lock AND make the (symmetrized) signature DISTINGUISH on-line from off-line (the FE-forced
  Weil pair), where the symmetric self-pairing could not?

------------------------------------------------------------------------------------------------------
THE INVOLUTION theta (the FE).  On the archimedean Mellin model H ~ L^2(Re s = 1/2), the FE involution
is  theta: s |-> 1-s, i.e. t |-> -t in s = 1/2 + i t, i.e. the multiplicative inversion u |-> -u in the
log-scale coordinate u = log(scale).  theta^2 = Id, theta = theta^T (it IS an involution and symmetric).

CRUCIAL HONEST POINT (the trap to avoid).  The SYMMETRIC Gaussian basis used by
hecke_correspondence.py / square_representability.py, g_c(u) = e^{-(u-c)^2/2w^2} + e^{-(u+c)^2/2w^2},
is ALREADY theta-symmetric: g_c(-u) = g_c(u), so theta acts as the IDENTITY on the span and F_theta
collapses back to F = T^T A T (the symmetric congruence, RH-silent). To give theta a chance to act
NON-trivially we MUST use a basis that is NOT theta-symmetric -- a ONE-SIDED (chiral) basis
g_c(u) = e^{-(u-c)^2/2w^2} on which theta: u|->-u genuinely maps g_c to g_{-c} (a DIFFERENT basis
vector). On this basis theta is a real permutation-like involution (a reflection matrix Theta with
Theta^2=Id, Theta != Id) and F_theta = T^T A Theta T can genuinely differ from T^T A T.

------------------------------------------------------------------------------------------------------
WHAT THIS MODULE COMPUTES (executable), and the three decisive tests:

  (D1) Is theta NON-TRIVIAL on the chosen basis?  (||Theta - Id|| > 0).  If trivial, the whole
       construction is the symmetric congruence and is RH-silent by hecke_correspondence.py. We
       therefore use the CHIRAL (one-sided) basis so Theta is a genuine reflection.

  (D2) Does theta BREAK the Sylvester congruence-lock?  Compare sig(sym(T^T A T)) vs sig(sym(T^T A
       Theta T)) -- if theta-twisting changes the signature AWAY from sig(A), the congruence-lock is
       broken (necessary for any RH content). We verify Sylvester directly: sig(T^T A T)=sig(A) on the
       chiral basis too (the symmetric self-pairing is STILL a congruence), and ask whether the
       theta-twist escapes it.

  (D3) THE DECISIVE FALSIFIER (sees-zeros / distinguishes line). Plant the FE-forced Weil pair
       (beta, 1-beta) in T (the genuine off-line plant, signature_forcing.py standard) and ask whether
       the signature of sym(F_theta) FLIPS on-line (beta=1/2) vs off-line (beta=0.6) -- the content
       that the symmetric self-pairing congruence-locked away.

  Plus the full falsify.py three axes (Euler-borne zeta vs DH, sees-zeros via the FE-pair signature
  flip, independent).

THE HONEST PRIOR.  theta-twisting MIGHT still be RH-silent for a DEEPER reason than Sylvester: if
A.Theta is itself effectively a (signed) metric whose inertia is plant-independent, the twisted form is
again congruence-locked, just to a DIFFERENT fixed background. The point of D2/D3 is to MEASURE whether
the twist genuinely opens a line-distinguishing degree of freedom or merely relocates the congruence.
Either outcome is load-bearing: a FLIP would be the first non-congruence-locked self-pairing (chase it);
NO flip names a STRONGER obstruction than Sylvester (the twist relocates but does not escape the
congruence -- the phase the symmetrization throws away is not recoverable by a real theta-twist).

Tags: [THM] (theta = FE involution, theta^2=Id; Sylvester inertia for symmetric congruences;
chiral basis makes Theta != Id), [computed] (Theta nontrivial, the twisted signatures, the FE-pair
flip test, the three axes), [CONJ] (whether ANY real theta-twist can carry the (1,rho-1) phase).

Run:  python3 -m scripts.numerics.witness.theta_twisted_pairing
"""
from __future__ import annotations

import numpy as np
from flint import acb

from .explicit_formula import log_deriv_coeffs, dh_coeffs, von_mangoldt


# ----------------------------------------------------------------------------------------------------
# Archimedean metric A on a CHIRAL (one-sided, NOT theta-symmetric) Gaussian basis g_c(u)=exp(-(u-c)^2/
# 2w^2). The basis centers are placed symmetrically about 0 (c and -c BOTH present) so that theta:
# u|->-u permutes the basis (g_c <-> g_{-c}) as a genuine reflection Theta != Id. The archimedean
# Gamma_R density Re psi(1/4 + i r/2) is the SAME DH-shared factor as hecke_correspondence.py.
# ----------------------------------------------------------------------------------------------------

def _repsi(t: float) -> float:
    """Re psi(1/4 + i t/2) -- the DH-shared archimedean Gamma_R density."""
    return float(acb(0.25, t / 2).digamma().real)


def chiral_centers(base):
    """Make a theta-paired center list: for each c>0 include both +c and -c (so theta permutes them);
    keep a single 0. Returns (centers, theta_index) where theta_index[i]=j means theta(g_i)=g_j."""
    cs = [0.0]
    for c in base:
        if c > 0:
            cs.append(c)
            cs.append(-c)
    # theta: u->-u sends g_c -> g_{-c}; build the permutation
    idx = {}
    for i, c in enumerate(cs):
        # find j with center -c
        for j, d in enumerate(cs):
            if abs(d + c) < 1e-12:
                idx[i] = j
                break
    theta_perm = [idx[i] for i in range(len(cs))]
    return cs, theta_perm


def theta_matrix(theta_perm):
    """The involution Theta as a permutation matrix on the chiral basis (Theta g_i = g_{theta(i)})."""
    k = len(theta_perm)
    Th = np.zeros((k, k))
    for i, j in enumerate(theta_perm):
        Th[j, i] = 1.0
    return Th


def archimedean_gram(centers, width: float, T: float = 200.0, N: int = 40001):
    """A_ij = (1/2pi) int hhat_i(r) hhat_j(r) Re psi(1/4 + i r/2) dr, CHIRAL basis g_c(u)=exp(-(u-c)^2/
    2w^2) (one-sided). Fourier transform hhat(r,c) = w sqrt(2pi) exp(-w^2 r^2/2) exp(-i r c); the
    archimedean density is even in r, so the REAL part of the product gives a cos kernel."""
    ts = np.linspace(-T, T, N)
    dt = ts[1] - ts[0]
    psi = np.array([_repsi(t) for t in ts])

    def hhat_re(r, c):
        return width * np.sqrt(2 * np.pi) * np.exp(-width ** 2 * r ** 2 / 2) * np.cos(r * c)

    def hhat_im(r, c):
        return -width * np.sqrt(2 * np.pi) * np.exp(-width ** 2 * r ** 2 / 2) * np.sin(r * c)

    k = len(centers)
    A = np.zeros((k, k))
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            # Re( hhat_i conj(hhat_j) ) integrated against the even density
            integ = (hhat_re(ts, ci) * hhat_re(ts, cj) + hhat_im(ts, ci) * hhat_im(ts, cj)) * psi
            A[i, j] = np.sum(integ) * dt / (2 * np.pi)
    return A


def _prime_coeffs(kind: str, M: int):
    if kind == "zeta":
        return [float(von_mangoldt(n)) for n in range(1, M + 1)]
    if kind == "dh":
        return [float(x) for x in log_deriv_coeffs(dh_coeffs(M), M)]
    raise ValueError(kind)


def correspondence_operator(kind: str, centers, width: float, M: int = 60):
    """The zeta-intrinsic prime-shift correspondence T on the CHIRAL basis. (T f)(u)=sum c(n)/sqrt n
    (f(u-log n)+f(u+log n))/2; T_ij = overlap of g_i with the shifted g_j (one-sided Gaussians)."""
    cn = _prime_coeffs(kind, M)
    k = len(centers)
    T_mat = np.zeros((k, k))
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            s = 0.0
            for n in range(2, M + 1):
                if cn[n - 1] == 0.0:
                    continue
                u = np.log(n)
                # one-sided Gaussian overlaps: g_i centered ci with g_j shifted by +-log n
                ov = (np.exp(-(ci - cj - u) ** 2 / (4 * width ** 2))
                      + np.exp(-(ci - cj + u) ** 2 / (4 * width ** 2)))
                s += cn[n - 1] * ov / n
            T_mat[i, j] = s
    return T_mat


def plant_in_operator(T_mat, centers, width, rho0, strength=1.0, M=60):
    """Add the off-line resonance term cos(gamma u) e^{(beta-1/2)|u|} to the prime-shift coefficients
    (the SAME plant as hecke_correspondence.py)."""
    beta, gamma = rho0
    k = len(centers)
    dT = np.zeros((k, k))
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            s = 0.0
            for n in range(2, M):
                u = np.log(n)
                ov = (np.exp(-(ci - cj - u) ** 2 / (4 * width ** 2))
                      + np.exp(-(ci - cj + u) ** 2 / (4 * width ** 2)))
                s += strength * np.cos(gamma * u) * np.exp((beta - 0.5) * u) * ov / n
            dT[i, j] = s
    return T_mat + dT


def signature(Mx, tol=1e-9):
    ev = np.linalg.eigvalsh((Mx + Mx.T) / 2)
    pos = int(np.sum(ev > tol))
    neg = int(np.sum(ev < -tol))
    zer = len(ev) - pos - neg
    return (pos, neg, zer)


def sym(Mx):
    return (Mx + Mx.T) / 2


# ----------------------------------------------------------------------------------------------------
# The decisive tests.
# ----------------------------------------------------------------------------------------------------

def plant_FE_pair(T_z, centers, width, beta, gamma=14.0):
    """Plant beta AND its FE partner 1-beta (the genuine off-line Weil pair). For beta=1/2 the two
    coincide (its own FE partner) -- planted twice (degenerate), matching hecke_correspondence.py."""
    return plant_in_operator(
        plant_in_operator(T_z, centers, width, rho0=(beta, gamma)),
        centers, width, rho0=(1 - beta, gamma))


def run(base_centers=None, width=0.5):
    if base_centers is None:
        base_centers = [np.log(2), np.log(3), np.log(5), np.log(7)]

    centers, theta_perm = chiral_centers(base_centers)
    Theta = theta_matrix(theta_perm)
    k = len(centers)
    Id = np.eye(k)

    A = archimedean_gram(centers, width)
    A_dh = archimedean_gram(centers, width)
    arch_shared = float(np.max(np.abs(A - A_dh)))

    T_z = correspondence_operator("zeta", centers, width)
    T_d = correspondence_operator("dh", centers, width)

    # (D1) is theta NON-trivial on this basis?
    theta_nontrivial = float(np.linalg.norm(Theta - Id))
    # sanity: Theta^2 = Id, Theta symmetric (permutation involution)
    theta_is_involution = float(np.linalg.norm(Theta @ Theta - Id))

    # the SYMMETRIC self-pairing (hecke_correspondence.py's object) on the chiral basis
    F_sym = T_z.T @ A @ T_z
    sig_A = signature(A)
    sig_F_sym = signature(F_sym)
    detT = float(np.linalg.det(T_z))
    # Sylvester check: sig(F_sym) should equal sig(A) since T invertible
    sylvester_holds = (sig_F_sym == sig_A) and abs(detT) > 1e-12

    # (D2) the THETA-TWISTED pairing F_theta = T^T A Theta T (NOT symmetric in general). Take its
    # symmetric part for the signature (the Hodge-index/Weil signature lives in the symmetric form).
    F_theta = T_z.T @ A @ Theta @ T_z
    F_theta_sym = sym(F_theta)
    sig_F_theta = signature(F_theta_sym)
    # is the twist NON-symmetric (does it carry an antisymmetric/phase part)?
    antisym_norm = float(np.linalg.norm((F_theta - F_theta.T) / 2))
    twist_breaks_congruence = (sig_F_theta != sig_A)

    # also report the signature of A.Theta itself (the twisted metric) -- if its inertia is plant-
    # independent, the twist merely relocates the congruence to A.Theta
    sig_ATheta = signature(sym(A @ Theta))

    # ---- axis 1: Euler-borne ----
    op_diff = float(np.max(np.abs(T_z - T_d)))
    euler_borne = op_diff > 1e-6

    # ---- (D3) DECISIVE: does sym(F_theta)'s signature FLIP on-line vs off-line (FE-forced pair)? ----
    T_on = plant_FE_pair(T_z, centers, width, beta=0.5)
    T_off = plant_FE_pair(T_z, centers, width, beta=0.6)

    # symmetric self-pairing (the RH-silent baseline)
    sig_sym_on = signature(sym(T_on.T @ A @ T_on))
    sig_sym_off = signature(sym(T_off.T @ A @ T_off))
    sym_flips = sig_sym_on != sig_sym_off

    # theta-twisted pairing (the candidate)
    sig_tw_on = signature(sym(T_on.T @ A @ Theta @ T_on))
    sig_tw_off = signature(sym(T_off.T @ A @ Theta @ T_off))
    twist_flips = sig_tw_on != sig_tw_off

    # also: the scalar twisted self-int (monotone-in-beta control, NOT line content)
    scal_tw_on = float(np.trace(T_on.T @ A @ Theta @ T_on))
    scal_tw_off = float(np.trace(T_off.T @ A @ Theta @ T_off))

    sees_zeros = twist_flips  # the genuine RH content = the SIGNATURE flip with the FE pair

    # ---- axis 3: independent ----
    # F_theta = T^T A Theta T is still assembled ENTIRELY from (T, A, Theta) = the explicit-formula
    # prime side, the DH-shared archimedean metric, and the FE. If its line-positivity is a flip, it is
    # still the Weil/explicit-formula content (the primes coupled to the line via the FE) -> not
    # independent. We set independent=False unless a genuinely new (non-Weil) positivity appears.
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
        "basis_dim (chiral)": k,
        "arch_metric_DH_shared (max|A_z-A_dh|)": arch_shared,
        "--- (D1) is theta nontrivial on the chiral basis? ---": "",
        "||Theta - Id|| (theta nontrivial)": theta_nontrivial,
        "||Theta^2 - Id|| (theta involution)": theta_is_involution,
        "--- baseline: symmetric self-pairing T^T A T (hecke_correspondence.py) ---": "",
        "det T (!=0 => Sylvester applies)": detT,
        "sig(A)": sig_A,
        "sig(T^T A T)": sig_F_sym,
        "SYLVESTER congruence-lock holds (sig(T^TAT)=sig(A))": sylvester_holds,
        "--- (D2) does the theta-twist BREAK the congruence-lock? ---": "",
        "sig(sym(T^T A Theta T))": sig_F_theta,
        "antisymmetric part norm (phase carried)": antisym_norm,
        "twist signature != sig(A) (congruence broken?)": twist_breaks_congruence,
        "sig(sym(A.Theta)) (twisted metric inertia)": sig_ATheta,
        "--- axis 1: Euler-borne ---": "",
        "axis1_euler_borne": euler_borne,
        "operator_diff_z_DH": op_diff,
        "--- (D3) DECISIVE: signature flip with FE-forced Weil pair ---": "",
        "sym self-pairing sig on-line": sig_sym_on,
        "sym self-pairing sig off-line": sig_sym_off,
        "  symmetric pairing flips (RH-silent baseline)": sym_flips,
        "twisted pairing sig on-line": sig_tw_on,
        "twisted pairing sig off-line": sig_tw_off,
        "  TWISTED pairing flips (THE candidate's RH content)": twist_flips,
        "twisted scalar self-int on-line": scal_tw_on,
        "twisted scalar self-int off-line": scal_tw_off,
        "--- axes 2,3 ---": "",
        "axis2_sees_zeros (twist signature flips)": sees_zeros,
        "axis3_independent": independent,
        "VERDICT": verdict,
    }


def summary():
    np.set_printoptions(precision=4, suppress=True)
    print("theta_twisted_pairing.py -- the THETA-TWISTED self-pairing T^T A Theta T (NEXT #1)\n")
    print("Target: break the Sylvester congruence-lock that made hecke_correspondence.py's SYMMETRIC")
    print("self-pairing T^T A T RH-silent. Insert the FE involution theta to carry the phase the")
    print("symmetrization throws away. CRUCIAL: on a theta-SYMMETRIC basis theta=Id (trivial), so we")
    print("use a CHIRAL (one-sided) basis where theta: u->-u is a genuine reflection Theta != Id.\n")

    results = {}
    for label, base in [("chiral [l2,l3,l5,l7]", [np.log(2), np.log(3), np.log(5), np.log(7)]),
                         ("chiral [l2,l3,l5]", [np.log(2), np.log(3), np.log(5)]),
                         ("chiral [l2,l3,l5,l7,l11]",
                          [np.log(2), np.log(3), np.log(5), np.log(7), np.log(11)])]:
        v = run(base)
        results[label] = v
        print(f"=== {label} (dim {v['basis_dim (chiral)']}) ===")
        for kk, vv in v.items():
            if kk in ("basis_dim (chiral)",):
                continue
            if kk.startswith("---"):
                print(f"  {kk}")
            else:
                print(f"    {kk:52s}: {vv}")
        print()

    print("[interpretation -- the decisive measurement]")
    v = results["chiral [l2,l3,l5,l7]"]
    print(f"  (D1) theta is NONTRIVIAL on the chiral basis: ||Theta-Id||={v['||Theta - Id|| (theta nontrivial)']:.3f}")
    print(f"       (involution defect {v['||Theta^2 - Id|| (theta involution)']:.1e}).")
    print(f"  (baseline) Sylvester congruence-lock on the SYMMETRIC pairing holds: "
          f"{v['SYLVESTER congruence-lock holds (sig(T^TAT)=sig(A))']} "
          f"(sig(T^TAT)={v['sig(T^T A T)']} = sig(A)={v['sig(A)']}).")
    print(f"  (D2) theta-twist signature sig(sym(T^TA Theta T))={v['sig(sym(T^T A Theta T))']}; "
          f"breaks congruence-lock (!= sig(A))? {v['twist signature != sig(A) (congruence broken?)']}.")
    twist_flip = v["  TWISTED pairing flips (THE candidate's RH content)"]
    print(f"  (D3) THE FALSIFIER: does sym(F_theta) FLIP on-line vs off-line (FE pair)? {twist_flip}")
    print(f"       (twisted sig on-line {v['twisted pairing sig on-line']} vs off-line "
          f"{v['twisted pairing sig off-line']}).")
    print(f"  VERDICT: {v['VERDICT']}")


if __name__ == "__main__":
    summary()
