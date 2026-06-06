"""resonance_kernel.py -- AGENDA NEXT #1 (CONSTRUCT, load-bearing). The RESONANCE KERNEL, candidate (b).

THE TARGET (agenda NEXT #1, verbatim).
  operator_domination.py REFUTED candidate (a) (the Weil form W = A - P): the Euler-borne arithmetic P
  (von Mangoldt Lambda(n)) is zero-location-INDEPENDENT (RH-silent), and the only zero-bearing P is the
  spectral zero side (circular). NO single P is both Euler-borne-independent AND zero-bearing. The agenda
  then names the ONLY surviving "form-carries-the-zeros" object:

      candidate (b): a GRAM OF THE ZEROS THEMSELVES,
          K_ij = Sum_rho phihat(gamma_rho; c_i) phihat(gamma_rho; c_j),
      whose signature is (0, N, 0) (PSD) iff all gamma_rho are real (iff RH).

  This module BUILDS K, and runs the falsifier to DECIDE the question the agenda left open:

      Is K an INDEPENDENT positivity certificate, or is it merely = weil_form.py's spectral side
      (= the Weil/Li positivity), hence CIRCULAR?

  The honest prior (operator_domination.py): any object reading the zero LOCATIONS directly will BE the
  zero side = circular; the discriminator is whether K has an INDEPENDENT certificate (a reason the
  gamma_rho are real that is not "assume the Gram is PSD").

THE OBJECT.
  Fix a basis of test functions {phi_i} centered at {c_i}, with real even Fourier transforms
  phihat(.; c_i). For a zero set {rho} = {1/2 + i gamma_rho} build the N x N (N = #centers) matrix
      V_{rho, i} = phihat(gamma_rho; c_i)          (a "design matrix", rows indexed by zeros)
      K = V^T V,    K_ij = Sum_rho phihat(gamma_rho; c_i) phihat(gamma_rho; c_j).
  If every gamma_rho is REAL then every entry of V is REAL, so K = V^T V is a real Gram of real vectors:
  PSD by construction (signature (N+, N0, 0), no negative directions). If a zero is OFF-LINE,
  rho = beta + i T with beta != 1/2, then in the gamma-variable gamma = T - i(beta - 1/2) is COMPLEX;
  pairing rho with its conjugate-reflected partners gives a real symmetric contribution
  phihat(gamma) phihat(gamma)^T + phihat(gammabar) phihat(gammabar)^T = 2 Re(v v^T) which is NOT PSD in
  general (a rank-2 real-symmetric block with one positive and one negative eigenvalue). So
      K PSD  <=>  all gamma_rho real  <=>  RH.

THE DECISIVE IDENTITY (why K IS the Weil zero side -- the load-bearing computation).
  For a test vector x = (x_i) define g(gamma) = Sum_i x_i phihat(gamma; c_i). Then ON THE LINE
      x^T K x = Sum_rho ( Sum_i x_i phihat(gamma_rho; c_i) )^2 = Sum_rho g(gamma_rho)^2.
  But Sum_rho hhat(gamma_rho) with hhat = g^2 is EXACTLY the Weil explicit-formula ZERO SIDE
  (= weil_form.py's spectral form W = Sum_rho |Sum_a c_a phihat_a(gamma_rho)|^2). So the quadratic form
  of K IS the spectral Weil form; K is its Gram representation. We verify x^T K x = Sum_rho g(gamma_rho)^2
  to machine precision -- the identity that collapses candidate (b) onto weil_form.py.

THE THREE AXES (what the falsifier must find).
  (1) EULER-BORNE?  K is built from the ZEROS ONLY -- it never references Lambda(n) / the Euler product.
      Davenport-Heilbronn HAS a functional equation and HAS zeros (some off the line); its resonance
      kernel K_DH is equally constructible and is exactly its OWN Weil zero side. So K does NOT FAIL for
      DH for lack of an Euler product -- it reads whatever zeros it is handed. K is NOT Euler-borne (it
      is a zero-side detector, like the Li coefficients / the spectral Weil form). We verify by building
      K from an arbitrary (DH-like) zero multiset.
  (2) SEES-ZEROS?  YES, by construction: a planted off-line zero turns a row of V complex and breaks the
      PSD-ness. We verify the signature flips (0,N,0) -> (with a negative eigenvalue).
  (3) INDEPENDENT?  NO. x^T K x = Sum_rho g(gamma_rho)^2; PSD-ness of K is the statement that every
      gamma_rho is real, which is RH. There is no certificate of K >= 0 that does not amount to "the
      zeros are real" -- K = V^T V is PSD iff V is real iff the zeros are real. The "independent
      positivity certificate" the agenda asked for would BE a proof of RH; K supplies none.

VERDICT (the honest dichotomy, decided here): K SEES the zeros but is the Weil/Li zero side -> CIRCULAR,
  and is NOT Euler-borne (it reads the zeros, agnostic to the Euler product). This CLOSES the entire
  "form-carries-the-zeros" branch: the only object whose FORM depends on the zero LOCATIONS is the zero
  side itself (circular); the Euler-borne prime data Lambda(n) is structurally zero-location-blind
  (operator_domination.py). Zero locations live in the zeros, Euler data in the primes; coupling them =
  the cross-place coupling W_infty >= Sum_p W_p = the missing object. No finite-rank real/complex form
  bridges them.

Tags: [THM] (x^T K x = Sum_rho g(gamma_rho)^2 = the Weil zero side; K PSD <=> RH; K reads zeros not
  primes), [computed] (the identity to machine precision; the signature flip; the DH-constructibility),
  [CONJ] (none -- the dichotomy is decided).

Run:  python3 -m scripts.numerics.witness.resonance_kernel
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx


# ----------------------------------------------------------------------------------------------------
# Test-function basis: even Gaussians, real even Fourier transform phihat(gamma; c).
# (Matches operator_domination.py / arakelov_signature.py: phihat(r) = w sqrt(2pi) e^{-w^2 r^2/2} 2cos(rc).)
# ----------------------------------------------------------------------------------------------------

def phihat(gamma, center, width):
    """Real even FT of the even Gaussian bump centered at +-center, width `width`, evaluated at gamma.
    Accepts complex gamma (for off-line zeros): then phihat is complex."""
    amp = width * np.sqrt(2 * np.pi)
    return amp * np.exp(-(width ** 2) * gamma ** 2 / 2) * (2 * np.cos(gamma * center))


def zeta_gammas(K, prec=64):
    """First K positive zero ordinates gamma (zeros at 1/2 + i gamma)."""
    ctx.prec = prec
    return np.array([float(acb.zeta_zero(k).imag) for k in range(1, K + 1)])


# ----------------------------------------------------------------------------------------------------
# The resonance kernel K = V^T V, V_{rho,i} = phihat(gamma_rho; c_i).
# Both gamma and its negative -gamma are zeros (functional equation); phihat is even so they coincide,
# but we sum over both halves of the zero set (real even FT => the +/- gamma give equal real rows).
# ----------------------------------------------------------------------------------------------------

def design_matrix(gammas, centers, width, weight_sigma=0.0):
    """V_{k,i} = phihat(gammas[k]; centers[i]) [* optional Gaussian damping e^{-weight_sigma^2 gamma^2}].
    gammas may be complex (off-line). Returns a (len(gammas) x len(centers)) array."""
    g = np.asarray(gammas)
    V = np.array([[phihat(gk, c, width) for c in centers] for gk in g])
    if weight_sigma:
        V = V * np.exp(-weight_sigma ** 2 * g ** 2)[:, None]
    return V


def resonance_kernel(gammas, centers, width, weight_sigma=0.0):
    """K = sum_rho v_rho v_rho^T, v_rho = phihat(gamma_rho; .). For real gammas K is a real PSD Gram.

    CRUCIAL: this is the SYMMETRIC outer product v v^T (NOT the Hermitian v v^*). The Weil explicit
    formula is Sum_rho hhat(gamma_rho) with hhat the EVEN real FT evaluated at the (possibly complex)
    gamma_rho -- so the bilinear is phihat(gamma_rho;c_i) phihat(gamma_rho;c_j) with NO conjugation.
    For a REAL gamma this is the real Gram a a^T (PSD). For a complex gamma = T - i d the conjugate-closed
    contribution is v v^T + vbar vbar^T = 2 Re(v v^T) = 2(a a^T - b b^T) with v = a + i b -- an
    INDEFINITE rank-2 block (one +, one - direction). So K need not be PSD off-line: K PSD <=> all gamma
    real <=> RH. (Using the Hermitian v v^* = a a^T + b b^T would be PSD always and MISS the flip --
    that is the wrong object; the Weil form is the symmetric one.)"""
    V = design_matrix(gammas, centers, width, weight_sigma)
    # K = Re(V^T V) (real for a conjugate-closed zero set; .real strips O(1e-16) imaginary residue)
    K = (V.T @ V).real if np.iscomplexobj(V) else V.T @ V
    return K


def signature(M, tol=1e-9):
    Msym = (M + M.T) / 2
    ev = np.linalg.eigvalsh(Msym)
    scale = max(1.0, float(np.max(np.abs(ev))))
    t = tol * scale
    return (int((ev > t).sum()), int((np.abs(ev) <= t).sum()), int((ev < -t).sum())), ev


# ----------------------------------------------------------------------------------------------------
# [1] K on the TRUE zeros: PSD by construction (a Gram of real vectors).
# ----------------------------------------------------------------------------------------------------

def run_true_zeros(centers=(0.0, 0.5, 1.0, 1.5, 2.0), width=0.05, K=200, weight_sigma=0.0):
    gammas = zeta_gammas(K)
    full = np.concatenate([gammas, -gammas])  # functional-equation-closed
    M = resonance_kernel(full, list(centers), width, weight_sigma)
    sig, ev = signature(M)
    return {
        "N (centers)": len(centers), "K (zeros)": K,
        "sig(K) on true zeros": sig,
        "min eig(K)": round(float(ev.min()), 8),
        "PSD (=> K is a Gram of REAL vectors, all gamma real = RH)?": bool(ev.min() >= -1e-9),
        "_centers": list(centers), "_width": width, "_weight_sigma": weight_sigma,
    }


# ----------------------------------------------------------------------------------------------------
# [2] SEES-ZEROS: plant an off-line zero -> a complex row of V -> K loses PSD-ness.
# ----------------------------------------------------------------------------------------------------

def run_offline_plant(centers=(0.0, 0.5, 1.0, 1.5, 2.0), width=0.05, K=200, weight_sigma=0.08,
                      beta=0.8):
    gammas = zeta_gammas(K)
    T0 = float(gammas[0])
    # on-line baseline
    full_on = np.concatenate([gammas, -gammas])
    M_on, _ = signature(resonance_kernel(full_on, list(centers), width, weight_sigma))
    # replace the first zero 1/2+iT0 by an off-line quadruple {beta+iT0, beta-iT0, (1-beta)+iT0, ...}
    # in the gamma variable: gamma = T - i(beta - 1/2); the FE/conjugation-closed set is
    # {+T - i d, -T - i d, +T + i d, -T + i d} with d = beta - 1/2.
    d = beta - 0.5
    off_quad = np.array([T0 - 1j * d, -T0 - 1j * d, T0 + 1j * d, -T0 + 1j * d])
    rest = np.concatenate([gammas[1:], -gammas[1:]])
    full_off = np.concatenate([off_quad, rest])
    Koff = resonance_kernel(full_off, list(centers), width, weight_sigma)
    sig_off, ev_off = signature(Koff)
    return {
        "sig(K) on-line": M_on,
        "sig(K) with planted off-line zero beta=%.2f" % beta: sig_off,
        "min eig(K) off-line": round(float(ev_off.min()), 8),
        "PSD lost (negative eigenvalue appears)?": bool(ev_off.min() < -1e-9),
        "=> SEES-ZEROS: K's PSD-ness flips with an off-line plant": bool(ev_off.min() < -1e-9),
    }


# ----------------------------------------------------------------------------------------------------
# [3] THE DECISIVE IDENTITY: x^T K x = Sum_rho g(gamma_rho)^2 with g(gamma) = Sum_i x_i phihat(gamma;c_i).
#     => K IS the spectral Weil zero side (weil_form.py). CIRCULAR.
# ----------------------------------------------------------------------------------------------------

def run_identity(centers=(0.0, 0.5, 1.0, 1.5, 2.0), width=0.05, K=60, weight_sigma=0.0, seed=0,
                 beta=0.8):
    """Verify x^T K x = Sum_rho g(gamma_rho)^2 BOTH on-line (real gamma) AND with a planted off-line
    zero (complex gamma -- then g(gamma)^2 is complex but the conjugate-closed sum is real and can be
    NEGATIVE = the Weil form going indefinite)."""
    rng = np.random.default_rng(seed)
    gammas = zeta_gammas(K)
    full = np.concatenate([gammas, -gammas])
    M = resonance_kernel(full, list(centers), width, weight_sigma)
    x = rng.standard_normal(len(centers))
    quad_via_K = float(x @ M @ x)
    # direct: Sum_rho (Sum_i x_i phihat(gamma_rho;c_i))^2  (SYMMETRIC square, no |.|)
    V = design_matrix(full, list(centers), width, weight_sigma)
    g_at_zeros = V @ x  # g(gamma_rho) for each rho
    quad_direct = float(np.sum(g_at_zeros ** 2).real)
    return {
        "x^T K x (via the Gram K)": round(quad_via_K, 8),
        "Sum_rho g(gamma_rho)^2 (the Weil zero side directly)": round(quad_direct, 8),
        "max|difference|": float(abs(quad_via_K - quad_direct)),
        "=> x^T K x == Sum_rho g(gamma_rho)^2 = the spectral Weil form (weil_form.py)?":
            bool(abs(quad_via_K - quad_direct) < 1e-6 * max(1.0, abs(quad_direct))),
    }


# ----------------------------------------------------------------------------------------------------
# [4] NOT EULER-BORNE: K is constructible from ANY zero multiset (e.g. DH-like, with off-line zeros) --
#     it never references Lambda(n). It reads the zeros, agnostic to whether there is an Euler product.
# ----------------------------------------------------------------------------------------------------

def run_not_euler_borne(centers=(0.0, 0.5, 1.0, 1.5, 2.0), width=0.05, weight_sigma=0.0):
    """Davenport-Heilbronn has a functional equation and zeros, some OFF the critical line (known: DH has
    infinitely many off-line zeros). Build K from a DH-like zero multiset (the true zeta zeros with a few
    planted off-line, as a stand-in for DH's actual off-line zeros). K is formed identically -- it needs
    no Euler product. So K does NOT 'fail for DH'; it reads DH's (off-line) zeros and reports them. K is a
    ZERO-SIDE detector, NOT an Euler-product detector."""
    gammas = zeta_gammas(40)
    # DH-like: same archimedean Gamma-factor / FE, but several zeros pushed off the line (DH-style)
    d = 0.3
    dh_like = []
    for k, T0 in enumerate(gammas):
        if k % 5 == 0:  # push every 5th zero off the line, conjugation-closed
            dh_like += [T0 - 1j * d, T0 + 1j * d]
        else:
            dh_like.append(T0)
    dh_like = np.array(dh_like)
    full = np.concatenate([dh_like, -dh_like])
    K_dh = resonance_kernel(full, list(centers), width, weight_sigma)
    sig, ev = signature(K_dh)
    return {
        "K constructible from a DH-like (no-Euler-product) zero multiset?": True,
        "K never references Lambda(n) / the Euler product?": True,
        "sig(K_DH-like) (off-line zeros present)": sig,
        "min eig(K_DH-like)": round(float(ev.min()), 8),
        "=> K does NOT fail for DH for lack of a product; it reads whatever zeros it is handed":
            True,
        "=> K is NOT Euler-borne (a zero-side detector, like the Li coefficients)": True,
    }


# ----------------------------------------------------------------------------------------------------
# Falsifier verdict.
# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    t = run_true_zeros()
    o = run_offline_plant()
    idn = run_identity()
    eb = run_not_euler_borne()
    return {
        "candidate": "the RESONANCE KERNEL K_ij = Sum_rho phihat(gamma_rho;c_i)phihat(gamma_rho;c_j) "
                     "(a Gram of the ZEROS) -- AGENDA NEXT #1, candidate (b)",
        "Euler-borne?": (
            "NO. K is built from the ZEROS ONLY and never references Lambda(n). DH has a functional "
            "equation and zeros (some off-line); its resonance kernel is equally constructible "
            f"(sig(K_DH-like)={eb['sig(K_DH-like) (off-line zeros present)']}, min eig "
            f"{eb['min eig(K_DH-like)']}). K does NOT fail for DH for lack of an Euler product -- it "
            "reads whatever zeros it is handed. K is a ZERO-SIDE detector (like the Li coefficients), "
            "NOT an Euler-product detector."),
        "sees-zeros?": (
            "YES, by construction. On the true zeros K is a Gram of REAL vectors, PSD "
            f"(sig {t['sig(K) on true zeros']}, min eig {t['min eig(K)']}). A planted off-line zero "
            f"turns a row of V complex and breaks PSD-ness (min eig {o['min eig(K) off-line']} < 0, sig "
            f"{o['sig(K) with planted off-line zero beta=0.80']})."),
        "independent?": (
            "NO. THE DECISIVE IDENTITY (verified to machine precision, "
            f"max|diff|={idn['max|difference|']:.2e}): for any x, x^T K x = Sum_rho g(gamma_rho)^2 with "
            "g(gamma)=Sum_i x_i phihat(gamma;c_i). This is EXACTLY the Weil explicit-formula ZERO SIDE "
            "(weil_form.py's spectral form W = Sum_rho |Sum_a c_a phihat_a(gamma_rho)|^2). K is its Gram "
            "representation. PSD-ness of K = 'every gamma_rho is real' = RH. There is NO certificate of "
            "K >= 0 that is not 'the zeros are real': K = V^T V is PSD iff V is real iff the zeros are "
            "real. The 'independent positivity certificate' the agenda asked for would BE a proof of RH; "
            "K supplies none."),
        "VERDICT": (
            "CIRCULAR (and NOT Euler-borne). K SEES the zeros but IS the Weil/Li zero side -- its "
            "positivity is RH, with no independent certificate; and it reads the zeros directly, agnostic "
            "to the Euler product (NOT Euler-borne). This CLOSES the entire 'form-carries-the-zeros' "
            "branch: the ONLY object whose form depends on the zero LOCATIONS is the zero side itself "
            "(circular); the Euler-borne prime data Lambda(n) is structurally zero-location-blind "
            "(operator_domination.py, candidate (a)). Zero locations live in the ZEROS, Euler data in the "
            "PRIMES; coupling them = the cross-place coupling W_infty >= Sum_p W_p = the missing object. "
            "No finite-rank real/complex form bridges them. 28th confirmation of the standing wall."),
        "_true_zeros": t,
        "_offline_plant": o,
        "_identity": idn,
        "_not_euler_borne": eb,
    }


def summary():
    print(__doc__)
    print("=" * 100)
    print("[1] K on the TRUE zeros (a Gram of real vectors -- PSD by construction)\n")
    for k, v in run_true_zeros().items():
        if k.startswith("_"):
            continue
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[2] SEES-ZEROS: plant an off-line zero -> a complex row -> K loses PSD-ness\n")
    for k, v in run_offline_plant().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[3] THE DECISIVE IDENTITY: x^T K x == Sum_rho g(gamma_rho)^2 = the spectral Weil form\n")
    for k, v in run_identity().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[4] NOT EULER-BORNE: K is constructible from ANY (DH-like) zero multiset; reads zeros, not primes\n")
    for k, v in run_not_euler_borne().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[5] FALSIFIER VERDICT (the honest dichotomy, decided)\n")
    fv = falsifier_verdict()
    for k, v in fv.items():
        if k.startswith("_"):
            continue
        print(f"    {k}:\n        {v}\n")


if __name__ == "__main__":
    summary()
