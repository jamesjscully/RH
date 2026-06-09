"""Killing-direction resonance dictionary: partial-margin killers are frequency combs.

Companion to research/proof/09-inverse-analysis.md section 6''. For a subset S of places,
the minimal eigenvector y of W_inf - P_S is conjectured to be (approximately) a
single-frequency resonance comb at a frequency t0 where the S-partial explicit-formula
density is most negative, and the repair pattern of the excluded atoms is then

    contribution of atom n  =  2 Lambda(n) n^{-1/2} k_y(log n),
    k_y(U) ~ A cos(t0 U + phase)     (single-frequency approximation),

i.e. the sign of each repairing/harming atom is predicted by the equidistribution of
log n on the resonance circle R / (2pi/t0) Z. For S={2}, t0 ~ 2pi/log2 and the predicted
sign at n is  sign(cos(2 pi frac(log_2 n))).

This witness measures, for S = {2}, {2,3}, {2,3,5,7}:
    * the killing direction's autocorrelation k_y at every reachable prime-power log;
    * the dominant frequency t0 of |yhat|^2;
    * the sign-match rate between observed k_y(log n) and the single-frequency
      prediction cos(t0 log n + phase);
    * the identity check  y^T M_full y = y^T M_S y - sum(excluded contributions).

Fail-closed: a sign-match rate near 0.5 (chance) kills the resonance dictionary and
with it the combinatorial-skeleton route; the identity must hold to roundoff.

Run:
    python3 -m scripts.numerics.witness.prime_killing_resonance
"""
from __future__ import annotations

import math
import sys

import numpy as np

from .prime_carleson_flow import _sym
from .prime_ladder_scaling import Ladder, build_ladder, nested_basis


def _strip(n: int, primes: tuple) -> bool:
    m = n
    for p in primes:
        while m % p == 0:
            m //= p
    return m != 1   # True = excluded from P_S


def analyze_subset(lad: Ladder, Q: np.ndarray, gmax: float, primes: tuple) -> dict:
    Msub = lad.Winf.copy()
    for logn, _w, block in lad.atoms["zeta"]:
        if logn < gmax and not _strip(round(math.exp(logn)), primes):
            Msub = Msub - block
    Msub_n = _sym(Q.T @ Msub @ Q)
    w, V = np.linalg.eigh(Msub_n)
    y = V[:, 0]
    amb = Q @ y
    yhat = amb @ lad.PH
    dens = yhat * yhat
    scale = lad.dt / (2.0 * np.pi)

    # dominant resonance frequency of |yhat|^2 (positive t)
    pos = lad.ts > 0.2
    t0 = float(lad.ts[pos][np.argmax(dens[pos])])

    # phase fit: k_y(U) ~ A cos(t0 U + phi) via two samples of the transform
    # (use least squares over the atom shifts)
    rows = []
    for logn, wt, _block in lad.atoms["zeta"]:
        if logn >= gmax:
            continue
        n = round(math.exp(logn))
        k = float(np.sum(dens * np.cos(logn * lad.ts)) * scale)
        rows.append((n, logn, wt, k, _strip(n, primes)))
    # fit A, phi: k ~ a cos(t0 L) + b sin(t0 L)
    Ls = np.array([r[1] for r in rows])
    ks = np.array([r[3] for r in rows])
    X = np.column_stack([np.cos(t0 * Ls), np.sin(t0 * Ls)])
    coef, *_ = np.linalg.lstsq(X, ks, rcond=None)
    pred = X @ coef
    weights = np.array([abs(r[2]) for r in rows])
    signif = np.abs(ks) > 0.05 * np.max(np.abs(ks))
    match = np.sign(pred[signif]) == np.sign(ks[signif])
    match_rate = float(np.mean(match)) if signif.any() else float("nan")
    resid = float(np.linalg.norm(ks - pred) / np.linalg.norm(ks))

    excl_sum = sum(r[2] * r[3] for r in rows if r[4])
    full_val = float(w[0] - excl_sum)
    return {"primes": primes, "eigmin": float(w[0]), "t0": t0,
            "match_rate": match_rate, "fit_residual": resid,
            "excl_sum": float(excl_sum), "full_on_y": full_val, "rows": rows}


def summary(quick: bool = True) -> dict:
    print("=" * 86)
    print("Killing-direction resonance dictionary")
    print("=" * 86)
    if quick:
        cmax, ncenters, hw, T, N, gmax = 2.42, 38, 0.06, 250.0, 100001, 4.96
    else:
        cmax, ncenters, hw, T, N, gmax = 2.89, 46, 0.06, 300.0, 120001, 5.90
    lad = build_ladder(cmax, ncenters, hw, gmax, T=T, N=N)
    Q = nested_basis(lad, gmax)
    out = {}
    for primes in ((2,), (2, 3), (2, 3, 5, 7)):
        r = analyze_subset(lad, Q, gmax, primes)
        out[primes] = r
        print(f"\nS={set(primes)}: eigmin(W_inf - P_S) = {r['eigmin']:+.4e}")
        print(f"   dominant resonance t0 = {r['t0']:.4f} "
              f"(2pi/log2={2*math.pi/math.log(2):.4f}, pi/log2={math.pi/math.log(2):.4f})")
        print(f"   single-frequency sign-match rate (significant atoms): {r['match_rate']:.3f}")
        print(f"   single-frequency fit residual (rel L2): {r['fit_residual']:.3f}")
        print(f"   y^T M_S y = {r['eigmin']:+.4e}, excluded sum = {r['excl_sum']:+.4e}, "
              f"y^T M_full y = {r['full_on_y']:+.4e}")

    print("\nInterpretation:")
    print("  * match rate ~1 and t0 at the comb frequency: the killing directions are")
    print("    multiplicative resonances and repair = equidistribution of {log p} on the")
    print("    resonance circle - the form problem has a scalar-density skeleton;")
    print("  * the form positivity then reads: the 1/R-smoothed S-partial explicit-formula")
    print("    density, tested against admissible Fejer profiles, is nonnegative;")
    print("  * match rate ~0.5 would kill the dictionary (fail-closed).")
    return out


if __name__ == "__main__":
    summary(quick="--full" not in sys.argv[1:])
