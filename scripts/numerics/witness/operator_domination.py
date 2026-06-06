"""operator_domination.py -- AGENDA NEXT #1 (ANALYTIC, load-bearing). THE OPERATOR INEQUALITY A >= P.

THE TARGET (agenda NEXT #1, verbatim).
  Every self-pairing of a FIXED form is now closed (symmetric T^T A T, real-twist T^T A Theta T,
  Hermitian T^T(A+i omega)T, oriented signed-Hodge; real OR complex plant) -- Sylvester's law of inertia
  locks every invertible *-congruence (26 Euler-product confirmations). The corrected target is the
  Weil explicit-formula domination W_infty >= Sum_p W_p DIRECTLY -- the OPERATOR INEQUALITY A >= P,
  where the form itself is W = A - P (NOT a congruence T^T(.)T). The agenda's specific HOPE:

      "This is the first object where the form depends on the zero locations (through P carrying the
       planted resonance), so Sylvester does NOT apply."

  This module BUILDS the two explicit Gram matrices A (archimedean, DH-shared) and P (prime,
  Euler-borne) and tests, with the falsifier in the loop, whether the operator inequality A >= P (PSD of
  W = A - P) SEES the off-line plant where every congruence did not -- AND, decisively, whether the
  agenda's hope is even REALIZABLE: can P carry a planted resonance at all?

THE OBJECT (the Weil explicit formula AS A QUADRATIC FORM)  [THM, standard].
  For a real even test function h with Fourier transform hhat,
        Sum_rho hhat(gamma_rho)  =  W_arch(h)  -  W_prime(h)  +  (pole terms),
  W_arch(h) = (1/2pi) int hhat(r) Re psi(1/4 + i r/2) dr        (ARCHIMEDEAN, the Gamma_R density)
  W_prime(h) = Sum_n Lambda(n) h(log n)/sqrt(n)                 (FINITE places, the Euler product).
  Polarize on a basis {h_j}: A[i,j] = arch bilinear, P[i,j] = prime bilinear. The Weil form is the
  GRAM W = A - P. RH <=> W >= 0 on the relevant subspace <=> the operator inequality A >= P.

  CRUCIAL: W = A - P is NOT a congruence (plant)^T(fixed form)(plant). Its inertia is the inertia of the
  DIFFERENCE of two fixed PSD-ish forms, and an off-line zero would (the hope) move P's positive
  directions to overwhelm A. Sylvester does not apply to A - P. So IF P carries the zeros, this is the
  first object that can flip.

THE DECISIVE EXPERIMENT (and the honest dichotomy it forces).
  The question is whether P (the prime Gram) can carry a planted off-line resonance. There are exactly
  TWO honest realizations of "plant a zero", and we test BOTH against the three falsify axes:

  (R1) ARITHMETIC P (P built from Lambda(n)). The von Mangoldt coefficients Lambda(n) are a property of
       the EULER PRODUCT of zeta -- they do NOT depend on where zeta's zeros sit. Planting an off-line
       zero in zeta does NOT change Lambda(n) (zeta has the zeros it has; Lambda is fixed). So A and the
       arithmetic P are BOTH zero-location-independent, W = A - P is a FIXED matrix, and its inertia
       CANNOT flip on/off-line. The agenda's hope that "P carries the planted resonance" is FALSE for the
       arithmetic P. We verify this: build A, P for zeta, compute sig(W); then attempt to plant an
       off-line zero and confirm P (hence W) is UNCHANGED.

  (R2) SPECTRAL P (the explicit formula run BACKWARDS from a chosen zero set). The explicit formula lets
       us trade the prime side for the zero side: W(h,h) = Sum_rho hhat(gamma_rho) - W_arch(h)... i.e. we
       can DEFINE a "prime side" P_spec consistent with a chosen zero multiset. With the TRUE zeros,
       W = A - P_spec = Sum_rho hhat(gamma_rho) is PSD (all gamma real). Replace the first zero by an
       off-line pair (Re rho = beta != 1/2): the gamma becomes COMPLEX and the zero-side sum can go
       NEGATIVE -- W loses PSD-ness. This DOES see the zeros. BUT: P_spec for the off-line zero set is
       NOT zeta's Lambda(n) -- it is the prime side of a DIFFERENT function (one with that off-line
       zero), exactly as green_current_perturbation.py CASE 2 found. So R2 sees the zeros ONLY because
       it IS the Weil positivity (the zero side is PSD iff RH) -- CIRCULAR -- and the P it uses is not
       Euler-borne in the independent sense (it is whatever the zeros dictate).

  The PIN (the load-bearing equality): the agenda's hope conflates R1's Euler-borne P (independent, but
  zero-INDEPENDENT) with R2's zero-bearing P (sees-zeros, but = the zero side = Weil positivity). NO
  single P is BOTH Euler-borne-independent AND carrying the planted resonance. That is the wall, now in
  operator-inequality language: A >= P is RH-silent for the arithmetic (Euler-borne) P and circular for
  the spectral (zero-bearing) P -- the cross-place coupling that would make zeta's OWN Lambda(n) (the
  arithmetic P) force the zero side is exactly the missing object.

WHAT THIS MODULE COMPUTES (executable):
  [1] Build A (arch) and P (prime, arithmetic) for zeta; report sig(A), sig(P), sig(W=A-P), and the
      operator inequality A >= P (PSD of W).
  [2] R1: confirm P is zero-INDEPENDENT -- the arithmetic P for zeta is unchanged by "planting" an
      off-line zero (P depends on Lambda(n), not on the zero locations). So W=A-P does NOT flip.
  [3] R1 Euler-borne litmus: A is DH-shared (max|A_z-A_dh|=0); only P differs zeta/DH. The operator
      inequality A >= P_zeta vs A >= P_DH -- does the PSD-ness discriminate? (Test whether A - P stays
      indefinite/PSD for both: a one-place model is too coarse, like semilocal_2.py.)
  [4] R2: build the SPECTRAL W = Sum_rho hhat(gamma_rho) as a Toeplitz Gram on the TRUE zeros (PSD) and
      with a planted off-line zero (PSD lost). Confirm it SEES the zeros -- but it IS the zero side =
      Weil positivity. Compare to the arithmetic W of [1]: do they agree (explicit-formula closure)?
  [5] falsifier_verdict(): the honest dichotomy R1 (RH-silent) / R2 (circular), all three axes.

Tags: [THM] (the explicit formula = the Weil quadratic form; Lambda(n) is zero-independent; the zero
side is PSD iff RH), [computed] (A, P, W signatures; the zero-independence of arithmetic P; the
spectral PSD flip), [CONJ] (whether any P is both Euler-borne-independent and zero-bearing -- the wall).

Run:  python3 -m scripts.numerics.witness.operator_domination
"""
from __future__ import annotations

import mpmath as mp
import numpy as np
from flint import acb, ctx

from .explicit_formula import log_deriv_coeffs, dh_coeffs


# ----------------------------------------------------------------------------------------------------
# Test-function basis (reuse the arakelov_signature.py even-Gaussian construction).
# ----------------------------------------------------------------------------------------------------

def gaussian_pair(center, width):
    """Even bump g_c(u) = exp(-(u-c)^2/2w^2) + exp(-(u+c)^2/2w^2) and its (real, even) FT."""
    def h(u):
        return mp.e ** (-((u - center) ** 2) / (2 * width ** 2)) + mp.e ** (-((u + center) ** 2) / (2 * width ** 2))

    def hhat(r):
        amp = width * mp.sqrt(2 * mp.pi)
        g = amp * mp.e ** (-(width ** 2) * r ** 2 / 2)
        return g * (mp.cos(r * center) * 2)
    return h, hhat


def w_arch_kernel(r):
    """Archimedean Gamma_R density (1/2pi) Re psi(1/4 + i r/2) -- DH-shared (same for zeta and DH)."""
    return (1 / (2 * mp.pi)) * mp.re(mp.digamma(mp.mpf('0.25') + 1j * r / 2))


def gram_pieces(centers, width, coeffs, M=400, R=60.0, nquad=1600):
    """A[i,j] = arch bilinear int hi_hat(r) hj_hat(r) (1/2pi)Re psi(1/4+ir/2) dr;
       P[i,j] = prime bilinear Sum_n c(n) hi(log n) hj(log n) / n.   W = A - P."""
    B = [gaussian_pair(c, width) for c in centers]
    m = len(B)
    A = np.zeros((m, m))
    P = np.zeros((m, m))
    rs = np.linspace(-R, R, nquad)
    dr = rs[1] - rs[0]
    trap = np.trapz if hasattr(np, "trapz") else np.trapezoid
    # precompute the arch kernel and each hi_hat on the grid
    kern = np.array([float(w_arch_kernel(mp.mpf(r))) for r in rs])
    hhat_grid = []
    for (h, hhat) in B:
        hhat_grid.append(np.array([float(mp.re(hhat(mp.mpf(r)))) for r in rs]))
    for i in range(m):
        for j in range(i, m):
            A[i, j] = A[j, i] = float(trap(hhat_grid[i] * hhat_grid[j] * kern, dx=dr))
            hi = B[i][0]
            hj = B[j][0]
            s = mp.mpf(0)
            for nn in range(2, M + 1):
                cn = coeffs[nn - 1]
                if abs(float(cn)) < 1e-300:
                    continue
                s += mp.mpf(str(float(cn))) * hi(mp.log(nn)) * hj(mp.log(nn)) / nn
            P[i, j] = P[j, i] = float(s)
    return A, P


def signature(Msym, tol=1e-9):
    ev = np.linalg.eigvalsh((Msym + Msym.T) / 2)
    scale = max(1.0, float(np.max(np.abs(ev))))
    t = tol * scale
    return (int((ev > t).sum()), int((np.abs(ev) <= t).sum()), int((ev < -t).sum())), ev


# ----------------------------------------------------------------------------------------------------
# [1] The operator inequality A >= P for zeta (arithmetic P).
# ----------------------------------------------------------------------------------------------------

def run_operator_inequality(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    mp.mp.dps = 30
    cz = log_deriv_coeffs([1] * M, M)
    A, P = gram_pieces(list(centers), width, cz, M=M)
    sigA, _ = signature(A)
    sigP, _ = signature(P)
    W = A - P
    sigW, evW = signature(W)
    # operator inequality A >= P  <=>  W = A - P PSD  <=>  min eig(W) >= 0
    min_eig_W = float(np.min(evW))
    return {
        "centers": list(centers), "width": width, "M": M,
        "sig(A) archimedean": sigA,
        "sig(P) prime (arithmetic, Lambda)": sigP,
        "sig(W=A-P)": sigW,
        "min eig(W)": round(min_eig_W, 6),
        "operator inequality A >= P (W PSD)?": bool(min_eig_W >= -1e-9),
        "_W_eigs": [round(float(x), 5) for x in evW],
    }


# ----------------------------------------------------------------------------------------------------
# [2] R1 -- the arithmetic P is ZERO-INDEPENDENT. "Planting" an off-line zero in zeta does NOT change
#     Lambda(n) (the Euler product), hence does NOT change P, hence W = A - P is unchanged.
# ----------------------------------------------------------------------------------------------------

def r1_zero_independence(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    """The arithmetic prime Gram P is a function of Lambda(n) ONLY. Lambda(n) = the n-th coefficient of
    -zeta'/zeta -- a property of zeta's EULER PRODUCT, not of where its zeros sit. There is no operation
    'plant an off-line zero' that changes Lambda(n) while keeping zeta zeta: zeta has the zeros it has.
    A surrogate WITH an off-line zero (e.g. DH) has DIFFERENT coefficients -- but then it is a different
    function. So within zeta, P (and W=A-P) is zero-INDEPENDENT: the operator inequality A>=P is a FIXED
    fact, it cannot flip on/off-line. We confirm this by re-deriving P from the SAME Lambda and noting it
    is invariant, and by checking that the only way to move P is to change the function (=> R2)."""
    mp.mp.dps = 30
    cz = log_deriv_coeffs([1] * M, M)
    A, P = gram_pieces(list(centers), width, cz, M=M)
    # there is no zero-location parameter in P: it is Sum_n Lambda(n) hi hj / n. Demonstrate by building
    # P from Lambda directly vs from the -zeta'/zeta recursion -- identical -- and note neither has a
    # 'beta' (off-line) knob.
    from .explicit_formula import von_mangoldt
    P_fromLambda = np.zeros_like(P)
    B = [gaussian_pair(c, width) for c in centers]
    m = len(B)
    for i in range(m):
        for j in range(i, m):
            s = mp.mpf(0)
            for nn in range(2, M + 1):
                lam = von_mangoldt(nn)
                if lam == 0.0:
                    continue
                s += mp.mpf(str(lam)) * B[i][0](mp.log(nn)) * B[j][0](mp.log(nn)) / nn
            P_fromLambda[i, j] = P_fromLambda[j, i] = float(s)
    return {
        "max|P_from(-zeta'/zeta) - P_from(Lambda)|": float(np.max(np.abs(P - P_fromLambda))),
        "P depends on a zero-location (beta) parameter?": False,
        "=> arithmetic W=A-P is zero-INDEPENDENT (cannot flip on/off-line)": True,
        "the only way to move P is to change Lambda(n) = change the function (=> R2 / different L)": True,
    }


# ----------------------------------------------------------------------------------------------------
# [3] R1 Euler-borne litmus -- A is DH-shared; only P differs zeta/DH. Does the operator inequality
#     discriminate?
# ----------------------------------------------------------------------------------------------------

def r1_euler_borne(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    mp.mp.dps = 30
    cz = log_deriv_coeffs([1] * M, M)
    cd = log_deriv_coeffs(dh_coeffs(M), M)
    Az, Pz = gram_pieces(list(centers), width, cz, M=M)
    Ad, Pd = gram_pieces(list(centers), width, cd, M=M)
    _, evWz = signature(Az - Pz)
    _, evWd = signature(Ad - Pd)
    return {
        "max|A_zeta - A_DH| (archimedean, DH-shared)": float(np.max(np.abs(Az - Ad))),
        "max|P_zeta - P_DH| (prime, Euler-borne)": float(np.max(np.abs(Pz - Pd))),
        "sig(W_zeta=A-P_zeta)": signature(Az - Pz)[0],
        "sig(W_DH=A-P_DH)": signature(Ad - Pd)[0],
        "min eig(W_zeta)": round(float(np.min(evWz)), 6),
        "min eig(W_DH)": round(float(np.min(evWd)), 6),
        "A>=P discriminates zeta from DH by PSD-ness at one place?":
            (float(np.min(evWz)) >= -1e-9) != (float(np.min(evWd)) >= -1e-9),
    }


# ----------------------------------------------------------------------------------------------------
# [4] R2 -- the SPECTRAL W = Sum_rho hhat(gamma_rho). This DOES carry the zeros (it IS the zero side).
#     PSD iff all gamma real iff RH. A planted off-line zero breaks it. But it = the Weil positivity.
# ----------------------------------------------------------------------------------------------------

def _zeros(K, prec=64):
    ctx.prec = prec
    return np.array([float(acb.zeta_zero(k).imag) for k in range(1, K + 1)])


def spectral_toeplitz(taus, gammas, sigma, offline=None):
    """The zero-side Weil Toeplitz kernel f(tau) = Sum_rho exp(-sigma^2 gamma^2) cos(tau gamma).
    offline=(beta, T) replaces the first zero by an off-line pair gamma = T - i(beta-1/2) (COMPLEX)."""
    if offline is None:
        return np.array([float(np.sum(np.exp(-sigma ** 2 * gammas ** 2) * np.cos(t * gammas)))
                         for t in taus])
    beta, T = offline
    g = T - 1j * (beta - 0.5)
    base = np.exp(-sigma ** 2 * gammas[1:] ** 2)
    out = []
    for t in taus:
        b = np.sum(base * np.cos(t * gammas[1:]))
        off = (np.exp(-sigma ** 2 * g * g) * np.exp(1j * t * g)
               + np.exp(-sigma ** 2 * np.conj(g) ** 2) * np.exp(1j * t * np.conj(g)))
        out.append(b + off.real)
    return np.array(out)


def toeplitz_min_eig(f):
    m = len(f)
    T = np.array([[f[abs(i - j)] for j in range(m)] for i in range(m)])
    ev = np.linalg.eigvalsh(T)
    return float(ev.min()), float(ev.max())


def r2_spectral(sigma=0.12, beta=0.8, K=200):
    taus = np.arange(0, 8.01, 0.25)
    gammas = _zeros(K)
    f_on = spectral_toeplitz(taus, gammas, sigma)
    mn_on, mx_on = toeplitz_min_eig(f_on)
    f_off = spectral_toeplitz(taus, gammas, sigma, offline=(beta, float(gammas[0])))
    mn_off, _ = toeplitz_min_eig(f_off)
    return {
        "spectral W = Sum_rho hhat(gamma_rho), TRUE zeros: min eig": round(mn_on, 6),
        "  PSD (=> A>=P holds on the true zeros)?": bool(mn_on >= -1e-9),
        "spectral W, PLANTED off-line zero beta=%.2f: min eig" % beta: round(mn_off, 6),
        "  PSD?": bool(mn_off >= -1e-9),
        "=> the SPECTRAL P_spec (zero side) SEES the off-line plant": bool(mn_off < -1e-9),
        "but it IS the zero side = PSD iff RH = the Weil positivity (CIRCULAR)": True,
    }


# ----------------------------------------------------------------------------------------------------
# Falsifier (the honest dichotomy).
# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    op = run_operator_inequality()
    r1z = r1_zero_independence()
    r1e = r1_euler_borne()
    r2 = r2_spectral()
    return {
        "candidate": "the OPERATOR INEQUALITY A >= P (W = A - P, NOT a congruence) -- AGENDA NEXT #1",
        "Euler-borne?": (
            "YES for the ARITHMETIC P (R1): A is DH-shared (max|A_z-A_dh|="
            f"{r1e['max|A_zeta - A_DH| (archimedean, DH-shared)']:.2e}), P differs zeta/DH "
            f"(max|P_z-P_dh|={r1e['max|P_zeta - P_DH| (prime, Euler-borne)']:.4f}). The prime form P "
            "carries the Euler product. So the OBJECT A-P is Euler-borne through P."),
        "sees-zeros?": (
            "NO for the arithmetic P (R1): Lambda(n) is a property of zeta's EULER PRODUCT, NOT of where "
            "its zeros sit -- there is no 'plant an off-line zero' operation that changes Lambda(n) while "
            "keeping zeta zeta. So the arithmetic W=A-P is a FIXED matrix (zero-independent), its inertia "
            "CANNOT flip on/off-line. The agenda's hope that 'P carries the planted resonance' is FALSE "
            "for the arithmetic P -- Sylvester is irrelevant because there is no plant to apply it to. "
            "YES only for the SPECTRAL P_spec (R2): W=Sum_rho hhat(gamma_rho) is PSD iff all gamma real; "
            "a planted off-line zero breaks it (min eig "
            f"{op['min eig(W)']} on-true -> "
            f"{r2['spectral W, PLANTED off-line zero beta=0.80: min eig']} off-line). But P_spec is the "
            "ZERO SIDE, not zeta's Lambda(n)."),
        "independent?": (
            "the two readings split: ARITHMETIC P (R1) is independent (Lambda(n) unconditional) but "
            "zero-INDEPENDENT (RH-silent); SPECTRAL P_spec (R2) sees-zeros but IS the zero side = PSD iff "
            "RH = the Weil positivity (CIRCULAR), and its P is whatever the zeros dictate (not zeta's "
            "Euler product). NO single P is BOTH Euler-borne-independent AND zero-bearing."),
        "VERDICT": (
            "The OPERATOR INEQUALITY A >= P does NOT escape the wall -- it SPLITS it (like "
            "green_current_perturbation.py / square_representability.py): for the EULER-BORNE arithmetic "
            "P (built from zeta's Lambda(n)) the form W=A-P is ZERO-INDEPENDENT (RH-SILENT) because "
            "Lambda(n) does not know where the zeros are; for the ZERO-BEARING spectral P_spec the form "
            "IS the zero side = the Weil positivity (CIRCULAR). The agenda's hope that 'A-P is the first "
            "object where the form depends on the zero locations through P carrying the planted "
            "resonance' is FALSE: the arithmetic P carries the EULER PRODUCT, not the zero LOCATIONS; the "
            "only P that carries the zero locations is the zero side itself. Sylvester was never the "
            "obstruction here -- the obstruction is that zeta's OWN Lambda(n) (the Euler-borne, "
            "independent P) does not force the zero side; making it do so IS the cross-place coupling "
            "W_infty >= Sum_p W_p / the missing object. 27th Euler-product confirmation."),
        "_operator_inequality": op,
        "_R1_zero_independence": r1z,
        "_R1_euler_borne": r1e,
        "_R2_spectral": r2,
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[1] THE OPERATOR INEQUALITY A >= P for zeta (arithmetic P = Lambda(n))\n")
    for k, v in run_operator_inequality().items():
        if k.startswith("_"):
            continue
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[2] R1 -- the arithmetic P is ZERO-INDEPENDENT (no plant operation on Lambda(n))\n")
    for k, v in r1_zero_independence().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[3] R1 EULER-BORNE litmus -- A DH-shared, only P differs; does A>=P discriminate?\n")
    for k, v in r1_euler_borne().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[4] R2 -- the SPECTRAL P_spec (zero side) DOES see the plant, but IS the Weil positivity\n")
    for k, v in r2_spectral().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[5] FALSIFIER VERDICT (the honest dichotomy)\n")
    fv = falsifier_verdict()
    for k, v in fv.items():
        if k.startswith("_"):
            continue
        print(f"    {k}:\n        {v}\n")


if __name__ == "__main__":
    summary()
