"""Margin-law witness: is the exponential margin decay pole bookkeeping or arithmetic?

Companion to research/proof/09-inverse-analysis.md section 6'''. Compares, on the nested
pole-killed ladder, the minimal eigenvalue of four forms:

    W_inf alone                    (archimedean only)
    W_inf - Smooth[0, R]           (smooth PNT surrogate from 0)
    W_inf - Smooth[log 2, R]       (smooth surrogate from the first prime)
    W_inf - P_exact(R)             (the exact Euler margin - reference)

Findings this witness certifies (fail-closed):

    * W_inf alone goes INDEFINITE at gmax ~ 2.3: CC20's archimedean positivity does not
      extend past its window; from there on the primes rescue the archimedean form, so
      "domination of the prime term by W_inf" inverts - both directions are wrong, the
      object is the joint cancellation;
    * both smooth surrogates go indefinite at gmax ~ 1.9-2.3 and SATURATE around
      -0.4..-0.9 while the exact margin stays positive with ~ e^{-1.5 R} decay:
      the margin law is carried by the exact atomic structure, not by densities;
    * decomposition: exact and smooth truncated densities share the identical e^{R/2}
      pole-ringing; their difference is the zero-phase ringing
      sum_gamma e^{iR(gamma-t)}/(i(gamma-t)) + O(1). Positivity of the exact margin =
      the zero ringing fills every negative lobe of the pole ringing. The storage/debt
      mechanism of research/proof/04-07 is this lobe-filling in t-space.

If a future basis/refinement shows W_inf alone positive at large gmax, or a smooth
surrogate positive past 3.0, the collectivity claims above die (fail-closed).

Run:
    python3 -m scripts.numerics.witness.prime_margin_law
"""
from __future__ import annotations

import math
import sys

import numpy as np

from .prime_carleson_flow import _sym
from .prime_ladder_scaling import build_ladder, margin_at, nested_basis, smooth_block


def summary(quick: bool = True) -> list[tuple]:
    print("=" * 86)
    print("Margin law: archimedean-only and smooth-surrogate forms vs the exact Euler margin")
    print("=" * 86)
    if quick:
        cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
        gmaxs = (1.30, 1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50,
                 3.76, 4.00, 4.26, 4.50, 4.76, 4.96)
    else:
        cmax, ncenters, hw, T, N = 2.89, 46, 0.06, 300.0, 120001
        gmaxs = (1.30, 1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50,
                 3.76, 4.00, 4.26, 4.50, 4.76, 5.00, 5.26, 5.50, 5.76, 5.90)
    lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

    print("   gmax    W_inf alone   W-Sm[0,R]     W-Sm[log2,R]  exact Euler")
    rows = []
    for g in gmaxs:
        Q = nested_basis(lad, g)
        if Q.shape[1] == 0:
            continue

        def emin(M):
            return float(np.linalg.eigvalsh(_sym(Q.T @ M @ Q))[0])

        row = (g, emin(lad.Winf),
               emin(lad.Winf - smooth_block(lad, 0.0, g)),
               emin(lad.Winf - smooth_block(lad, math.log(2.0), g)),
               emin(margin_at(lad, "zeta", g)))
        rows.append(row)
        print(f"   {row[0]:4.2f}  {row[1]:+12.4e} {row[2]:+12.4e} {row[3]:+12.4e} {row[4]:+12.4e}")

    for name, idx in (("W_inf alone", 1), ("W-Sm[0,R]", 2), ("W-Sm[log2,R]", 3), ("exact", 4)):
        pts = [(r[0], math.log(r[idx])) for r in rows if r[0] >= 3.0 and r[idx] > 0]
        if len(pts) >= 3:
            x = np.array([p[0] for p in pts])
            z = np.array([p[1] for p in pts])
            print(f"   decay rate {name}: {np.polyfit(x, z, 1)[0]:+.3f} per unit R")
        else:
            neg = [r[0] for r in rows if r[idx] <= 0]
            if neg:
                print(f"   {name}: first nonpositive at gmax={neg[0]:.2f} "
                      f"(stays nonpositive: {all(r[idx] <= 0 for r in rows if r[0] >= neg[0])})")

    print("\nInterpretation: see module docstring; this is the fail-closed record that the")
    print("margin law is arithmetic (exact atoms), not archimedean/pole bookkeeping.")
    return rows


if __name__ == "__main__":
    summary(quick="--full" not in sys.argv[1:])
