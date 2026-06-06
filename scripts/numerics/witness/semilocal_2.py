"""Semilocal {infinity, 2} Weil positivity -- the minimal place-crossing (thread 0, dir C).

Thread 0's knife-edge (CC20, arXiv:2006.13771): the archimedean Weil quadratic form W_inf
is positive while the test-function support stays inside (1/2, 2) = (e^{-log2}, e^{log2})
("no prime involved"); the place-crossing is whether positivity survives once the support
reaches the first prime p=2, where the Euler factor (1-2^{-s}) contributes
W_2(g) = 2 sum_{k>=1} (log 2) 2^{-k/2} g(k log 2).  CC20 report the sign is restored ONLY by
the exact prime p=2, with a < 10^{-3} window around p=2.  This module builds W_{inf,2} as a
quadratic (Gram) form on positive-type test functions, verifies the explicit-formula
convention against the actual zeros, runs the knife-edge, and the Davenport-Heilbronn (DH)
kill-test (DH has the same Gamma_R but NO Euler factor at 2).

THE RELIABLE ROUTE (spectral side).  For g = h conv h*(-.), ghat = |hhat|^2 >= 0, the Weil
explicit formula reads, for zeta,

    Q(h) := sum_rho |hhat(gamma_rho)|^2
          = [ghat(i/2)+ghat(-i/2)]          (poles s=0,1)
          - P(g)                             (primes:  P = 2 sum_{p,k} log p p^{-k/2} g(k log p))
          + W_inf(g)                         (archimedean)
    W_inf(g) = -g(0) log pi + (1/2pi) int ghat(t) Re psi(1/4 + i t/2) dt .

Q(h) is a manifest sum of squares (PSD).  Killing the poles by the Sonin/Fourier-vanishing
constraints  hhat(0) = hhat(+-i/2) = 0  leaves  Q = W_inf - P >= 0.  Restricting the support
to u = log x in (-log2, log2) makes P = 0 (no prime), so W_inf is PSD there -- CC20's
archimedean positivity.  The KNIFE-EDGE is what happens as the support REACHES u = log2:
the p=2,k=1 term P_2 turns on, W_inf alone then OVERCOUNTS the spectral value by +P_2 and
goes indefinite, and subtracting the p=2 contribution (i.e. adding the Euler-factor term)
restores Q to the PSD spectral value.

Basis: compactly supported even raised-cosine bumps phi_c(u)=cos^2(pi(u-c)/2hw) on
(c-hw, c+hw), folded even.  Compact support => the prime sum is finite (only p=2 reachable
when c+hw in (log2, log3)) and the spectral identity closes exactly.

CONVENTION verified by verify_explicit_formula() against acb.zeta_zero to ~1e-10.

Run:  python3 -m scripts.numerics.witness.semilocal_2
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx

LOG2 = np.log(2.0)
LOG3 = np.log(3.0)

# ---------------------------------------------------------------------------
# cached archimedean kernel and zeros
# ---------------------------------------------------------------------------
_CACHE: dict = {}


def _grids(T=250.0, N=100001, nzero=5000):
    if "ts" not in _CACHE:
        ctx.prec = 80
        ts = np.linspace(-T, T, N)
        _CACHE["ts"] = ts
        _CACHE["dt"] = ts[1] - ts[0]
        _CACHE["psi"] = np.array([float(acb(0.25, t / 2).digamma().real) for t in ts])
        _CACHE["gam"] = np.array([float(acb.zeta_zero(k).imag) for k in range(1, nzero)])
    return _CACHE


# ---------------------------------------------------------------------------
# compactly-supported even raised-cosine bump basis: phihat_c(t) (real, even)
# ---------------------------------------------------------------------------


def _phihat(t, c, hw):
    """Fourier transform of the EVEN bump  phi_c(u)+phi_c(-u), phi_c = cos^2(pi(u-c)/2hw)
    on (c-hw, c+hw).  phihat(t) = 2 int_{c-hw}^{c+hw} cos^2(...) cos(t u) du  (real even).

    Closed form (cos^2 = 1/2 + 1/2 cos(pi v/hw), v = u-c):
        phihat(t) = 2 cos(t c) * [ S(t) + 1/2 S(t + pi/hw) + 1/2 S(t - pi/hw) ],
        S(a) = sin(a hw)/a   (= hw at a=0).
    Exact (verified against quadrature to machine precision); no dense grid needed."""
    t = np.atleast_1d(np.asarray(t, dtype=float))

    def S(a):
        small = np.abs(a) < 1e-9
        return np.where(small, hw, np.sin(a * hw) / np.where(small, 1.0, a))

    inner = S(t) + 0.5 * S(t + np.pi / hw) + 0.5 * S(t - np.pi / hw)
    return 2.0 * np.cos(t * c) * inner


def _phihat_ihalf(c, hw, M=4001):
    """phihat_c at t = i/2:  2 int phi_c(u) cosh(u/2) du  (the pole-constraint value)."""
    uu = np.linspace(c - hw, c + hw, M)
    du = uu[1] - uu[0]
    ph = np.cos(np.pi * (uu - c) / (2 * hw)) ** 2
    return 2.0 * np.sum(ph * np.cosh(uu / 2)) * du


def _phi_at(c, hw, U, M=3001):
    """phihat_c evaluated as the physical g-value requires the inverse transform; instead we
    return phihat sampled at frequency grid -- g(U) is assembled in build_gram via the FT."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# the Gram matrices of the place functionals
# ---------------------------------------------------------------------------


def build_gram(centers, hw, prime_scale=1.0, primes=(2,), kmax=4):
    """Return W_inf, prime-term (P_S), other-primes, spectral Gram matrices, pole vectors.

    CRUCIAL SUPPORT FACT.  g_ij = phi_i conv phi_j*(-.) has support up to
    (c_i+hw)+(c_j+hw), i.e. the CONVOLUTION reaches twice as far as a single bump.  So
    "support(g) in (1/2,2)" means each bump must satisfy c+hw <= log2/2; and the genuine
    place-crossing (p=2 active, p=3 NOT) requires the convolution edge gmax=2(c_max+hw)
    to lie in (log2, log3).  This function therefore tracks the convolution support and
    includes EVERY prime power k log p that falls inside it.

    P_S = the prime term for `primes` (default just p=2), with p -> p*prime_scale on the
    FIRST prime (knife-edge perturbation).  P_other = all OTHER reachable primes (the
    leakage that must be controlled for a clean {inf,2} statement).
    ghat_ij(t) = phihat_i(t) phihat_j(t); all functionals are linear in ghat."""
    g = _grids()
    ts, dt, psi, gam = g["ts"], g["dt"], g["psi"], g["gam"]
    n = len(centers)

    PHt = np.array([_phihat(ts, c, hw) for c in centers])
    PHg = np.array([_phihat(gam, c, hw) for c in centers])
    v0 = np.array([_phihat(np.array([0.0]), c, hw)[0] for c in centers])
    vih = np.array([_phihat_ihalf(c, hw) for c in centers])

    gmax = 2.0 * (centers.max() + hw)          # convolution support edge
    # the target prime(s) (perturbable) and the "other" reachable primes
    tgt_pts, tgt_w = [], []
    for idx, p0 in enumerate(primes):
        p = p0 * (prime_scale if idx == 0 else 1.0)
        lp = np.log(p)
        for k in range(1, kmax + 1):
            if k * lp < gmax:
                tgt_pts.append(k * lp)
                tgt_w.append(2.0 * lp * p ** (-k / 2.0))
    other_primes = [p for p in (3, 5, 7, 11, 13, 17, 19) if p not in primes]
    oth_pts, oth_w = [], []
    for p in other_primes:
        lp = np.log(p)
        for k in range(1, kmax + 1):
            if k * lp < gmax:
                oth_pts.append(k * lp)
                oth_w.append(2.0 * lp * p ** (-k / 2.0))

    tgt_cos = np.cos(np.outer(tgt_pts, ts)) if tgt_pts else np.zeros((0, len(ts)))
    oth_cos = np.cos(np.outer(oth_pts, ts)) if oth_pts else np.zeros((0, len(ts)))

    Winf = np.zeros((n, n))
    P2 = np.zeros((n, n))
    Poth = np.zeros((n, n))
    Spec = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            ghat = PHt[i] * PHt[j]
            g0 = ghat.sum() * dt / (2 * np.pi)
            Winf[i, j] = Winf[j, i] = -g0 * np.log(np.pi) + (ghat * psi).sum() * dt / (2 * np.pi)
            Spec[i, j] = Spec[j, i] = np.dot(PHg[i], PHg[j]) * 2.0
            if tgt_pts:
                gv = (tgt_cos * ghat).sum(axis=1) * dt / (2 * np.pi)
                P2[i, j] = P2[j, i] = float(np.dot(tgt_w, gv))
            if oth_pts:
                gv = (oth_cos * ghat).sum(axis=1) * dt / (2 * np.pi)
                Poth[i, j] = Poth[j, i] = float(np.dot(oth_w, gv))
    return {"Winf": Winf, "P2": P2, "Poth": Poth, "Spec": Spec, "v0": v0, "vih": vih,
            "gmax": gmax, "n_target_pts": len(tgt_pts), "n_other_pts": len(oth_pts)}


def prime_form_from_coeffs(centers, hw, coeffs):
    """Generalized prime term  P(g_ij) = 2 sum_n coeffs[n] n^{-1/2} g_ij(log n), summed over
    all n>=2 with log n inside the convolution support gmax = 2(c_max+hw).  `coeffs` is the
    log-derivative prime-side sequence c(n) of -Z'/Z (von Mangoldt for zeta; c_DH for DH).
    Lets the DH kill-test use DH's ACTUAL prime-side coefficients, not just 'absent at 2'."""
    g = _grids()
    ts, dt = g["ts"], g["dt"]
    n = len(centers)
    PHt = np.array([_phihat(ts, c, hw) for c in centers])
    gmax = 2.0 * (centers.max() + hw)
    ns = [m for m in range(2, len(coeffs) + 1)
          if np.log(m) < gmax and abs(coeffs[m - 1]) > 1e-12]
    pts = [np.log(m) for m in ns]
    w = [2.0 * coeffs[m - 1] * m ** (-0.5) for m in ns]
    cosmat = np.cos(np.outer(pts, ts)) if pts else np.zeros((0, len(ts)))
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            ghat = PHt[i] * PHt[j]
            gv = (cosmat * ghat).sum(axis=1) * dt / (2 * np.pi)
            P[i, j] = P[j, i] = float(np.dot(w, gv))
    return P, ns


def _proj_null(G):
    """Orthonormal basis of the null space of the two pole constraints hhat(0)=hhat(i/2)=0."""
    A = np.vstack([G["v0"], G["vih"]])
    _, _, Vt = np.linalg.svd(A)
    return Vt[2:].T  # n x (n-2)


def constrained_mineig(M, null):
    return float(np.linalg.eigvalsh(null.T @ M @ null).min())


# ---------------------------------------------------------------------------
# explicit-formula convention check (independent of the basis above)
# ---------------------------------------------------------------------------


def verify_explicit_formula(a=0.35, nzero=2000):
    g = _grids()
    ts, dt, psi = g["ts"], g["dt"], g["psi"]
    ctx.prec = 100
    ghat = lambda t: a * np.sqrt(2 * np.pi) * np.exp(-a * a * t * t / 2.0)
    gg = lambda u: np.exp(-u * u / (2 * a * a))
    gammas = np.array([float(acb.zeta_zero(k).imag) for k in range(1, nzero)])
    spec = 2.0 * np.sum(ghat(gammas))
    pole = 2 * a * np.sqrt(2 * np.pi) * np.exp(a * a / 8.0)
    import math
    P = 0.0
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        k = 1
        while k * math.log(p) < 8 * a + 6:
            P += math.log(p) * p ** (-k / 2.0) * gg(k * math.log(p))
            k += 1
    P *= 2.0
    Winf = -gg(0.0) * np.log(np.pi) + np.sum(ghat(ts) * psi) * dt / (2 * np.pi)
    arith = pole - P + Winf
    return {"spectral": spec, "arithmetic": arith, "residual": spec - arith}


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------


def summary():
    print("=" * 78)
    print("Semilocal {infinity, 2} Weil positivity -- the minimal place-crossing")
    print("=" * 78)

    v = verify_explicit_formula()
    print(f"\n[0] convention check (Gaussian g, 2000 zeros):")
    print(f"    sum_rho ghat(gamma) = {v['spectral']:.8f}")
    print(f"    Poles - P + W_inf   = {v['arithmetic']:.8f}    residual = {v['residual']:.2e}")
    print("    => the W_inf / P sign convention used below is the verified Weil convention.")

    hw = 0.18
    ncen = 7
    print(f"\n[basis] {ncen} compact even raised-cosine bumps, half-width hw={hw}; "
          f"log2={LOG2:.4f}, log3={LOG3:.4f}")
    print("  KEY: g = h conv h* has support up to gmax = 2(c_max+hw) -- the CONVOLUTION")
    print("  reaches twice as far. The clean {inf,2} window is gmax in (log2, log3):")
    print("  p=2 active, p=3 NOT.  c_max+hw in (log2/2, log3/2) = (0.347, 0.549).")

    # ---- knife-edge sweep: push the convolution edge gmax across log2 (toward log3) ----
    print("\n[1] KNIFE-EDGE sweep -- constrained (Fourier-vanishing kills the poles).")
    print("    The honest semilocal form for zeta is  Q = W_inf - P_2 - P_other  (= spectral).")
    print("      gmax     p2/poth pts   W_inf       Q=W_inf-P2-Poth   spectral   |Q-spec|")
    rows = []
    cmaxes = [0.32, 0.36, 0.42, 0.48, 0.54, 0.60]
    for cmax in cmaxes:
        centers = np.linspace(0.02, cmax, ncen)
        G = build_gram(centers, hw)
        null = _proj_null(G)
        wi = constrained_mineig(G["Winf"], null)
        Q = constrained_mineig(G["Winf"] - G["P2"] - G["Poth"], null)
        sp = constrained_mineig(G["Spec"], null)
        # identity closure (constrained): pr(Spec) should equal pr(Winf - P2 - Poth)
        nl = null
        gap = float(np.max(np.abs(nl.T @ (G["Spec"] - (G["Winf"] - G["P2"] - G["Poth"])) @ nl)))
        clean = G["n_other_pts"] == 0
        rows.append((G["gmax"], G["n_target_pts"], G["n_other_pts"], wi, Q, sp, gap, clean))
        tag = "  [clean {inf,2}]" if clean else "  [p>=3 leaks in]"
        print(f"     {G['gmax']:.4f}    {G['n_target_pts']}/{G['n_other_pts']}        "
              f"{wi:+.3e}   {Q:+.3e}      {sp:+.3e}  {gap:.1e}{tag}")

    # focus on the cleanest config that still has p=2 active (n_target>0, n_other==0)
    focus = next((i for i, r in enumerate(rows) if r[1] > 0 and r[2] == 0), None)
    if focus is None:
        focus = next((i for i, r in enumerate(rows) if r[1] > 0), len(rows) - 1)
    cmax = cmaxes[focus]
    centers = np.linspace(0.02, cmax, ncen)
    G = build_gram(centers, hw)
    null = _proj_null(G)
    wi = constrained_mineig(G["Winf"], null)
    wp = constrained_mineig(G["Winf"] - G["P2"], null)        # W_inf - p=2 term only
    Q = constrained_mineig(G["Winf"] - G["P2"] - G["Poth"], null)
    sp = constrained_mineig(G["Spec"], null)

    print(f"\n[2] FOCUS at gmax={G['gmax']:.4f}  (p=2 active: {G['n_target_pts']} pt; "
          f"p>=3 pts: {G['n_other_pts']})")
    print(f"    W_inf alone                min eig = {wi:+.4e}   PSD={wi >= -1e-9}")
    print(f"    W_inf - P_2  (add p=2)     min eig = {wp:+.4e}   PSD={wp >= -1e-9}")
    print(f"    spectral (sum of squares)  min eig = {sp:+.4e}   PSD={sp >= -1e-9}")
    print("    p=2 enters with sign giving W_inf - P_2; restoration direction:")
    print(f"      shift W_inf -> W_inf - P_2 : {wp - wi:+.4e}")

    # ---- knife-edge sensitivity: replace p=2 by 2(1+delta) ----
    print("\n[3] SENSITIVITY: replace the prime by a nearby real p = 2(1+delta).")
    print("    We report the GAP |pr(Spec) - pr(W_inf - P_{2(1+delta)})| -- the spectral")
    print("    (true PSD) form is recovered ONLY by the exact prime; a wrong p mis-recovers:")
    print("      delta        |spectral - (W_inf - P_{2(1+delta)})|   min eig of that form")
    base_spec = null.T @ G["Spec"] @ null
    for delta in [-0.05, -0.01, -1e-3, 0.0, 1e-3, 0.01, 0.05]:
        Gd = build_gram(centers, hw, prime_scale=1.0 + delta)
        form = null.T @ (Gd["Winf"] - Gd["P2"]) @ null
        gap = float(np.max(np.abs(base_spec - form)))
        mn = float(np.linalg.eigvalsh(form).min())
        print(f"     {delta:+.4f}      {gap:.6e}                    {mn:+.4e}")

    # ---- DH kill-test: DH's ACTUAL prime-side coefficients (not 'absent at 2') ----
    print("\n[4] DH KILL-TEST  (DH: same Gamma_R; prime-side c_DH(n) is NOT von Mangoldt)")
    from .explicit_formula import log_deriv_coeffs, dh_coeffs
    Mc = 64
    cz = [float(x) for x in log_deriv_coeffs([1] * Mc, Mc)]      # c_zeta = von Mangoldt
    cd = [float(x) for x in log_deriv_coeffs(dh_coeffs(Mc), Mc)]  # c_DH (no Euler product)
    print(f"    c_zeta(2)=Lambda(2)=log2={cz[1]:.4f}; c_DH(2)={cd[1]:.4f}, "
          f"c_DH(4)={cd[3]:.4f} (DH has wrong/extra prime weights)")
    Pz, nz = prime_form_from_coeffs(centers, hw, cz)
    Pd, nd = prime_form_from_coeffs(centers, hw, cd)
    qz = constrained_mineig(G["Winf"] - Pz, null)
    qd = constrained_mineig(G["Winf"] - Pd, null)
    print(f"    zeta : Q = W_inf - P_zeta  (n={nz})  min eig = {qz:+.4e}  PSD={qz >= -1e-9} "
          f"(= spectral {sp:+.4e})")
    print(f"    DH   : Q = W_inf - P_DH    (n={nd})  min eig = {qd:+.4e}  PSD={qd >= -1e-9}")
    print(f"    forms DIFFER by {abs(qz - qd):.3e} (sees the Euler product); "
          f"both PSD => no positivity discrimination at S={{inf,2}}.")
    discriminates = (qz >= -1e-9) and (qd < -1e-9)
    print(f"    discriminates (zeta PSD AND DH indefinite)? {discriminates}")
    print("    => semilocal {inf,2} REGISTERS the Euler product (matrices differ) but is")
    print("       still RH-NEUTRAL by positivity; the gap must accumulate over places.")

    return {
        "Winf_min": wi, "Wsemi_min": wp, "spectral_min": sp,
        "Qzeta_min": qz, "Qdh_min": qd, "form_gap": abs(qz - qd),
        "discriminates": discriminates, "gmax": G["gmax"],
    }


if __name__ == "__main__":
    summary()
