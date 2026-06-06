"""Angle 1 -- total positivity as the common language of the Hermite junction.

The bet (STRATEGY §3 metric enrichment; state-of-search "Hermite junction"):
  RH  <=>  xi in Laguerre-Polya  <=>  the Jensen sequence {gamma(k)} is a Polya-frequency
  (totally-positive) sequence  <=>  the de Bruijn-Newman flow (Gaussian = strictly-TP,
  variation-diminishing kernel, Schoenberg) realizes the zeros.
So "total positivity" names BOTH the static criterion (the PF cone) and the dynamic flow
(a TP semigroup).  The slack we have studied (super-exponential, degree-by-degree, the
Jensen min-rel-gap / the Hermite discriminant) is the distance to the PF-cone boundary.

THE HYPOTHESIS TESTED HERE (go/no-go): in total-positivity coordinates -- the
Hankel/Toeplitz minor positivity of {gamma(k)} -- are the positivity margins MORE UNIFORM
(e.g. polynomial) than the super-exponential degree-by-degree Jensen slack?  If yes, TP is
the right coordinate and the heat flow the right operator; if the minor margins are just as
bad, the TP framing is decoration and we learn that cheaply.

WHAT WE FOUND (honest, certified where it bites; see research/log/2026-06-05-angle1-...):

  (A) The NAIVE Hankel coordinate is WRONG.  The Hankel matrix det[gamma(i+j)] of the real-xi
      Jensen sequence is NOT positive semidefinite (its minors alternate sign from n=2 on):
      {gamma(k)} is NOT a Hamburger moment sequence.  Hankel/moment positivity characterizes
      "moments of a positive measure", a DIFFERENT condition from real-rootedness / LP
      membership.  So "Hankel determinants of {gamma(k)}" -- the obvious first guess -- is not
      even a true property of RH-satisfying xi.  (certified: the n=2 Hankel minor is < 0.)

  (B) The CORRECT TP coordinate is the Aissen-Schoenberg-Whitney (ASW) one: a polynomial with
      positive coefficients is hyperbolic (all real, all-negative roots) <=> the Toeplitz
      matrix of its coefficient sequence is totally nonnegative (TNN).  For each Jensen
      polynomial J_{d,n}, coeffs c_j = C(d,j) gamma(n+j); hyperbolicity <=> coeff-Toeplitz TNN.
      This IS a genuine RH margin: a contiguous minor goes negative exactly when a root pair
      goes complex (validated below).

  (C) The valid ASW margin (smallest strictly-positive contiguous Toeplitz minor) decays
      SUPER-EXPONENTIALLY in degree -- AS BAD AS, in fact faster than, the Jensen min-rel-gap.
      So the TP coordinate is NOT more uniform.  => NO-GO.

  (D) A SEDUCTIVE-BUT-INVALID near-miss (the §8 trap, stress-tested and rejected): the
      condition number sigma_min/sigma_max of the coeff-Toeplitz matrix decays only ~0.05/deg
      (10x more uniform than the gap's ~0.51/deg) -- but it FAILS the validity test: as two
      roots merge to the discriminant boundary it does NOT go to 0 (stays ~0.89, even rises as
      the poly goes non-hyperbolic).  It does not detect the PF-cone boundary, so its uniform
      decay is irrelevant decoration.  Likewise the s-th-root normalization of any minor is a
      massive artificial compressor (turns the discriminant's slope 61 -> 0.17) and is rejected.

  (E) Heat flow: the dBN flow H_t multiplies coeff c_j by Hermite-heat factors; the smallest
      positive Toeplitz minor moves monotonically under the flow but the margin stays
      super-exponentially small -- the variation-diminishing structure does not give a cleaner
      handle on the minors than on the Jensen polynomials.

VERDICT: NO-GO.  Total positivity is the correct LANGUAGE (it unifies the static PF criterion,
the ASW Toeplitz form, and the dBN TP semigroup), but it is NOT a fresher COORDINATE: the valid
TP margin is the same super-exponential slack wearing different clothes.  The slow-decaying TP
quantities are all invalid (don't vanish at the boundary).  This matches the metric-Arakelov
finding (the slack is the height of the discriminant variety, super-exp small) -- TP coordinates
do not change the height.

Run:  python3 -m scripts.numerics.witness.totally_positive
"""
from __future__ import annotations

from math import comb, factorial, log

import numpy as np
from flint import acb, acb_mat, ctx

from .xi_jensen import (_Phi, is_hyperbolic, jensen_poly_rescaled,
                        jensen_sequence, min_rel_gap)


# --------------------------------------------------------------------------- #
# certified Jensen sequence (acb balls, for rigorous small determinants)
# --------------------------------------------------------------------------- #
def jensen_sequence_acb(K, U=4.0, prec=260):
    """gamma(0..K) as certified acb balls (same integrand as xi_jensen, kept as acb)."""
    old = ctx.prec
    ctx.prec = prec
    out = []
    for k in range(K + 1):
        M = acb.integral(lambda u, _o: _Phi(u) * u ** (2 * k), acb(0), acb(U))
        fac = acb(1)
        for j in range(2, 2 * k + 1):
            fac *= j
        out.append((2 * M / fac).real)
    ctx.prec = old
    return out


# --------------------------------------------------------------------------- #
# (A) Hankel / Hamburger-moment positivity  -- the WRONG coordinate
# --------------------------------------------------------------------------- #
def hankel(seq, n, shift=0):
    return [[seq[i + j + shift] for j in range(n)] for i in range(n)]


def hankel_det_acb(seq_acb, n, shift=0):
    """Certified det[gamma(i+j+shift)]_{n x n} as an acb ball."""
    return acb_mat(hankel(seq_acb, n, shift)).det()


def hankel_first_negative(seq_acb, nmax=6):
    """First n (>=2) at which the Hankel minor is certifiably < 0 (=> {gamma} is NOT a
    Hamburger moment sequence => the Hankel/moment coordinate is the wrong TP coordinate)."""
    for n in range(2, nmax + 1):
        d = hankel_det_acb(seq_acb, n).real
        if d < 0:  # acb '<' : rigorous (true only if the whole enclosure is < 0)
            return n, d
    return None, None


# --------------------------------------------------------------------------- #
# (B,C) ASW Toeplitz total-positivity  -- the CORRECT coordinate
# --------------------------------------------------------------------------- #
def coeff_toeplitz(c):
    """Banded Toeplitz T[i,j] = c[i-j] (0 outside the band) of a coeff sequence c_0..c_d.
    ASW: a real polynomial with positive coeffs is hyperbolic (all roots real, negative)
    iff this Toeplitz matrix is totally nonnegative."""
    d = len(c) - 1
    N = d + 1
    M = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            m = i - j
            M[i, j] = c[m] if 0 <= m <= d else 0.0
    return M


def asw_min_pos_minor(c, tol_pos=1e-13, tol_neg=1e-10):
    """Smallest strictly-positive contiguous (Fekete) minor of the coeff Toeplitz matrix,
    Hadamard-normalized (det / prod row-norms, in (-1,1]) so it is scale-invariant.  This is
    the VALID ASW total-positivity margin: a negative such minor appears exactly when the
    polynomial loses hyperbolicity.  Returns (min_positive_minor, any_negative_minor)."""
    M = coeff_toeplitz(c)
    N = M.shape[0]
    mp = np.inf
    neg = False
    for s in range(2, N + 1):
        for r0 in range(N - s + 1):
            for c0 in range(N - s + 1):
                sub = M[r0:r0 + s, c0:c0 + s]
                det = np.linalg.det(sub)
                gscale = np.prod([np.linalg.norm(sub[i]) for i in range(s)])
                v = det / gscale if gscale > 0 else 0.0
                if v < -tol_neg:
                    neg = True
                if v > tol_pos:
                    mp = min(mp, v)
    return mp, neg


def asw_min_minor_order(c, s, tol_pos=1e-13):
    """Smallest strictly-positive contiguous minor of FIXED order s of the coeff Toeplitz
    matrix (Hadamard-normalized).  s=2 = the Turan / log-concavity minors (the lowest-order
    valid TP test); larger s = higher Newton inequalities.  Fixed order makes the
    degree-by-degree decay comparison with the root gap fair (no minor-order inflation)."""
    M = coeff_toeplitz(c)
    N = M.shape[0]
    mp = np.inf
    for r0 in range(N - s + 1):
        for c0 in range(N - s + 1):
            sub = M[r0:r0 + s, c0:c0 + s]
            det = np.linalg.det(sub)
            gscale = np.prod([np.linalg.norm(sub[i]) for i in range(s)])
            v = det / gscale if gscale > 0 else 0.0
            if v > tol_pos:
                mp = min(mp, v)
    return mp


def toeplitz_sigma_ratio(c):
    """sigma_min / sigma_max of the coeff Toeplitz matrix -- the INVALID near-miss condition
    number (slow, uniform decay, but does NOT detect the discriminant boundary; see validity
    test).  Kept to document the §8 trap."""
    sv = np.linalg.svd(coeff_toeplitz(c), compute_uv=False)
    return sv.min() / sv.max()


def jensen_coeffs_balanced(g, d, n):
    """Coeff sequence c_j = C(d,j) gamma(n+j), rescaled to O(1) by the two-end geometric
    factor (preserves hyperbolicity and TNN: c_j -> s c_j with s>0)."""
    c = np.array([comb(d, j) * g[n + j] for j in range(d + 1)], dtype=float)
    return c / (c[0] * c[-1]) ** 0.5


# --------------------------------------------------------------------------- #
# heat flow on the coefficient Toeplitz minors  (E)
# --------------------------------------------------------------------------- #
def _d2(c):
    nn = len(c)
    return (np.array([c[k + 2] * (k + 2) * (k + 1) for k in range(nn - 2)])
            if nn > 2 else np.array([0.0]))


def heat_flow(coeffs, t):
    """H_t = e^{-t D^2} p (ascending coeffs); the dBN Gaussian / TP semigroup."""
    c = np.array(coeffs, float)
    res = c.copy()
    d = c.copy()
    j = 1
    while len(d) > 2:
        d = _d2(d)
        pad = np.zeros(len(c))
        pad[:len(d)] = d
        res = res + ((-t) ** j / factorial(j)) * pad
        j += 1
    return res


# --------------------------------------------------------------------------- #
# validity test:  does each margin vanish at the discriminant boundary?
# --------------------------------------------------------------------------- #
def boundary_family(g, d, n, ts):
    """Build polys p_t from J_{d,n}'s roots by merging its two closest roots: t>0 separated,
    t=0 merged (on the discriminant variety), t<0 split into a complex pair.  Yields
    (t, ascending-balanced-coeffs, hyperbolic?)."""
    c0 = jensen_coeffs_balanced(g, d, n)
    r = np.sort(np.roots(c0[::-1]).real)
    i = int(np.argmin(np.diff(r)))
    mid = 0.5 * (r[i] + r[i + 1])
    span = r[-1] - r[0]
    for t in ts:
        rr = r.copy().astype(complex)
        if t >= 0:
            rr[i] = mid - 0.5 * t * (r[i + 1] - r[i])
            rr[i + 1] = mid + 0.5 * t * (r[i + 1] - r[i])
        else:
            rr[i] = mid + 1j * abs(t) * span
            rr[i + 1] = mid - 1j * abs(t) * span
        p = np.poly(rr).real
        asc = p[::-1].copy()
        asc = asc / (abs(asc[0]) * abs(asc[-1])) ** 0.5
        yield t, asc, is_hyperbolic(asc)


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #
def summary(K=20):
    print(__doc__.split("Run:")[0])
    print("=" * 78)

    g = jensen_sequence(K)
    g_acb = jensen_sequence_acb(min(K, 8))  # certified; only need small n for (A)

    # (A) Hankel = wrong coordinate (certified)
    print("\n(A) Naive Hankel/moment coordinate -- CERTIFIED WRONG")
    print("    det[gamma(i+j)]_{n x n} (acb balls); first certifiably-negative minor:")
    nbad, dbad = hankel_first_negative(g_acb, nmax=6)
    for n in range(1, 5):
        dd = hankel_det_acb(g_acb, n).real
        print(f"      n={n}: Hankel det = {dd}")
    if nbad:
        print(f"    => Hankel minor < 0 at n={nbad} (certified): {{gamma(k)}} is NOT a Hamburger")
        print("       moment sequence.  Hankel/moment positivity is the WRONG TP coordinate.")

    # (B/validity) the ASW margin DOES detect the boundary; the sigma-ratio does NOT
    print("\n(B) ASW Toeplitz coordinate -- validity test (push J_{5,0} to the discriminant):")
    print("    t>0 separated, t=0 merged (on variety), t<0 complex pair.")
    print("    t       | min-rel-gap | ASW min-pos-minor | neg-minor? | sigma-ratio | hyp")
    for t, asc, hyp in boundary_family(g, 5, 0, [0.5, 0.05, 0.0, -0.1]):
        mp, neg = asw_min_pos_minor(list(asc))
        sr = toeplitz_sigma_ratio(list(asc))
        mg = min_rel_gap(asc) if hyp else None
        mgs = f"{mg:.3e}" if mg is not None else "  n/a  "
        print(f"    {t:+.2f}   | {mgs}  | {mp:.4e}       | {str(neg):5s}      | {sr:.4f}      | {hyp}")
    print("    => ASW min-pos-minor -> 0 and a NEGATIVE minor appears exactly at hyperbolicity")
    print("       loss (VALID margin).  sigma-ratio stays ~0.9 and RISES (INVALID -- the §8 trap).")

    # (C) decay rates: valid TP margin vs gap, normalization-free
    print("\n(C) Decay in degree (n=0), the go/no-go:")
    print("    d | ASW min-pos-minor | min-rel-gap | sigma-ratio(INVALID)")
    ds, asw, gap, sig = [], [], [], []
    for d in range(2, 9):
        c = jensen_coeffs_balanced(g, d, 0)
        mp, _ = asw_min_pos_minor(list(c))
        mg = min_rel_gap(jensen_poly_rescaled(g, d, 0))
        sr = toeplitz_sigma_ratio(list(c))
        ds.append(d); asw.append(mp); gap.append(mg); sig.append(sr)
        print(f"    {d:2d} |   {mp:.4e}      | {mg:.4e}  | {sr:.4f}")
    # rates over the float-trustworthy range d<=6 (minors hit float noise ~1e-12 after)
    rng = [i for i, d in enumerate(ds) if d <= 6]
    da = np.array([ds[i] for i in rng])
    sa = np.polyfit(da, [log(asw[i]) for i in rng], 1)[0]
    sg = np.polyfit(da, [log(gap[i]) for i in rng], 1)[0]
    ss = np.polyfit(np.array(ds, float), [log(sig[i]) for i in range(len(ds))], 1)[0]
    print(f"\n    log-slope /degree (d<=6, float-trustworthy):")
    print(f"      ASW min-pos-minor (VALID TP)   : {sa:+.3f}   <- super-exp (minor-order grows with d)")
    print(f"      min-rel-gap       (known slack): {sg:+.3f}")
    print(f"      sigma-ratio       (INVALID)    : {ss:+.3f}   <- 'uniform' but does not detect boundary")

    # (C') the FAIR comparison: fixed-order minors (no minor-order inflation)
    print("\n(C') Fixed-order TP minors vs the gap (the fair, decisive comparison):")
    print("     d | 2x2 (Turan/log-concave) | 3x3 minor   | min-rel-gap")
    ds2, m2, m3 = [], [], []
    for d in range(3, 11):
        c = list(jensen_coeffs_balanced(g, d, 0))
        a2 = asw_min_minor_order(c, 2)
        a3 = asw_min_minor_order(c, 3)
        mg = min_rel_gap(jensen_poly_rescaled(g, d, 0))
        ds2.append(d); m2.append(a2); m3.append(a3)
        print(f"     {d:2d} |   {a2:.4e}          | {a3:.4e} | {mg:.4e}")
    s2 = np.polyfit(np.array(ds2, float), [log(x) for x in m2], 1)[0]
    s3 = np.polyfit(np.array(ds2[:5], float), [log(x) for x in m3[:5]], 1)[0]
    sgall = np.polyfit(np.array(ds2, float),
                       [log(min_rel_gap(jensen_poly_rescaled(g, d, 0))) for d in ds2], 1)[0]
    print(f"     2x2 (lowest-order VALID TP) log-slope: {s2:+.3f}/deg")
    print(f"     3x3                         log-slope: {s3:+.3f}/deg (already super-exp)")
    print(f"     min-rel-gap                 log-slope: {sgall:+.3f}/deg")
    print("     => the 2x2 TP minor decays at the SAME rate as the gap; 3x3+ are WORSE.")
    print("        No order of TP minor beats the gap.  TP is not a fresher coordinate.")

    # (E) heat flow on the minor margin
    print("\n(E) Heat flow (dBN TP semigroup) on the ASW minor margin (J_{6,0}):")
    print("    t        | ASW min-pos-minor | hyperbolic")
    c6 = list(jensen_coeffs_balanced(g, 6, 0))
    for t in [0.0, 1e-4, 5e-4, 1e-3, -1e-4]:
        ct = heat_flow(c6, t)
        ct = ct / (abs(ct[0]) * abs(ct[-1])) ** 0.5
        mp, neg = asw_min_pos_minor(list(ct))
        print(f"    {t:+.1e} | {mp:.4e}       | {is_hyperbolic(ct)}")
    print("    => the minor margin moves monotonically but stays super-exp small -- the")
    print("       variation-diminishing flow gives no cleaner handle on the minors.")

    print("\n" + "=" * 78)
    print("VERDICT: NO-GO.  TP is the correct LANGUAGE (unifies PF criterion + ASW form + dBN")
    print("  TP semigroup) but NOT a fresher COORDINATE.  The naive Hankel coordinate is")
    print("  certifiably wrong (not a moment sequence); the valid ASW Toeplitz margin is the")
    print("  same super-exponential slack; the only uniform-looking TP quantity (sigma-ratio)")
    print("  is invalid (does not vanish at the PF-cone boundary).  TP does not change the")
    print("  height of the discriminant variety.  The §8 backpressure rejected the near-miss.")
    return {
        "hankel_wrong_at_n": nbad,
        "rate_asw": sa,
        "rate_gap": sg,
        "rate_sigma_invalid": ss,
    }


if __name__ == "__main__":
    summary()
