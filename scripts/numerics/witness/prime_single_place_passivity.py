"""Single-place passivity probe: is W_inf - P_p >= 0 on the pole-killed ladder, per prime?

Motivation (R1a inverse analysis, research/proof/09). Each Euler local factor is a
Herglotz/positive-real object in its convergence region; the program's conjectured
realization is a passive interconnection of local systems against the archimedean
supply. The smallest nontrivial passivity lemma is then ONE place:

    W_inf - P_p >= 0   on pole-killed H_R, for all R,
    P_p = 2 sum_k (log p) p^{-k/2} B_{k log p}.

If true (and provable), it extends CC20's archimedean positivity past support log 2
with one prime's exact Euler data - an unconditional theorem target that is NOT RH
but is a real rung toward the interconnection. Fail-closed readings:

    * single-prime margin goes negative at some R: one-place passivity is false,
      the interconnection story dies in its simplest form, and the cross-prime
      interference is load-bearing even for one place's budget;
    * single-prime margin stays positive with a STABLE (non-decaying) floor while
      the all-prime margin decays: the RH content is purely in the prime
      interaction, and the one-place lemma is provable low-hanging fruit;
    * DH analogue (signed coefficients at one residue class) must fail.

Also probes pairs {2,3} and the full Euler margin for reference.

Run:
    python3 -m scripts.numerics.witness.prime_single_place_passivity
"""
from __future__ import annotations

import math
import sys

import numpy as np

from .prime_carleson_flow import _sym
from .prime_ladder_scaling import Ladder, build_ladder, nested_basis


def place_margin(lad: Ladder, primes: list[int] | None, gmax: float) -> np.ndarray:
    """W_inf minus the exact prime-power atoms of the given places (None = all)."""
    M = lad.Winf.copy()
    for logn, _w, block in lad.atoms["zeta"]:
        if logn >= gmax:
            continue
        n = round(math.exp(logn))
        if primes is not None:
            base = None
            for p in primes:
                k = round(logn / math.log(p))
                if k >= 1 and p ** k == n:
                    base = p
                    break
            if base is None:
                continue
        M = M - block
    return _sym(M)


def summary(quick: bool = True) -> dict:
    print("=" * 86)
    print("Single-place passivity probe: W_inf - P_S on the pole-killed nested ladder")
    print("=" * 86)
    if quick:
        cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
        gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
                 4.00, 4.26, 4.50, 4.76, 4.96)
    else:
        cmax, ncenters, hw, T, N = 2.89, 46, 0.06, 300.0, 120001
        gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
                 4.00, 4.26, 4.50, 4.76, 5.00, 5.26, 5.50, 5.76, 5.90)
    lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

    place_sets: list[tuple[str, list[int] | None]] = [
        ("p=2", [2]), ("p=3", [3]), ("p=5", [5]), ("p=7", [7]),
        ("{2,3}", [2, 3]), ("{2,3,5}", [2, 3, 5]), ("all", None),
    ]
    table: dict[str, list[float]] = {label: [] for label, _ in place_sets}
    for gmax in gmaxs:
        Q = nested_basis(lad, gmax)
        if Q.shape[1] == 0:
            for label, _ in place_sets:
                table[label].append(float("nan"))
            continue
        for label, primes in place_sets:
            M = place_margin(lad, primes, gmax)
            table[label].append(float(np.linalg.eigvalsh(_sym(Q.T @ M @ Q))[0]))

    header = "   gmax   " + "".join(f"{label:>12}" for label, _ in place_sets)
    print(header)
    for i, gmax in enumerate(gmaxs):
        row = "".join(f"{table[label][i]:+12.3e}" for label, _ in place_sets)
        print(f"   {gmax:4.2f} {row}")

    print("\n[late-edge ratios] margin(gmax) / margin(prev) per column")
    for label, _ in place_sets:
        vals = [v for v in table[label] if np.isfinite(v)]
        tail = vals[-5:]
        ratios = [tail[i + 1] / tail[i] if tail[i] > 0 else float("nan")
                  for i in range(len(tail) - 1)]
        print(f"   {label:>8}: " + "  ".join(f"{r:5.3f}" for r in ratios))

    print("\nInterpretation:")
    print("  * a single-place column staying positive with ratio -> 1 (stable floor) makes")
    print("    one-place passivity a provable-looking unconditional lemma (extends CC20);")
    print("  * a single-place column decaying like the all-prime column means even one place")
    print("    exhausts the archimedean budget and the interconnection must be global;")
    print("  * a negative single-place entry kills one-place passivity outright (fail-closed).")
    return table


if __name__ == "__main__":
    summary(quick="--full" not in sys.argv[1:])
