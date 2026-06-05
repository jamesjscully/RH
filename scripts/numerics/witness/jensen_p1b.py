"""P1b -- certified two-sided bracket on the Jensen slack (STRATEGY §8).

The slack rho_BW(d) = distance from the unit (Bombieri-Weyl) H_d to the discriminant variety
(double-root locus).  Certified LOWER bound, via a sufficient hyperbolicity condition:

  H_d + q stays hyperbolic if |q(s_i)| < |H_d(s_i)| at every critical point s_i (root of
  H_d' = 2d H_{d-1}), because then H_d+q keeps the sign of H_d at all d-1 interior extrema and
  the leading term, hence d real roots.  Since |q(s)| <= (1+s^2)^{d/2} ||q||_BW (the BW dual
  norm of affine evaluation), this gives

  rho_BW(d) >= L(d) := min_i |H_d(s_i)| / [ (1+s_i^2)^{d/2} ||H_d||_BW ].

The critical points s_i and values H_d(s_i) are certified via fmpz_poly.complex_roots (acb
ball arithmetic) and ||H_d||_BW is exact rational -- so L(d) is a CERTIFIED lower bound.

Honest finding (corrects the tentative P1a identification): this sufficient-condition bound is
EDGE-DOMINATED -- the min over critical points sits at the outermost s_i, where (1+s_i^2)^{d/2}
~ (2d)^{d/2} blows up -- so L(d) decays SUPER-exponentially and is a LOOSE lower bound.  A direct
search gives the slack ~e^{-1.04 d} (heuristic, exponential).  So: (3/2)ln2 is the discriminant
ENERGY (P1a, certified); it is NOT confirmed as the slack constant.  The slack is energy + a
CONDITIONING factor (Pardo-Pardo: disc = resultant x prod conditioning) and its exact rate is not
tightly pinned here -- the §8 backpressure stopping an over-claim.  What is solid: the slack is
exponentially small ('no slack at every scale'), and lives in the discriminant/condition-number
(height) world.

Run:  python3 -m scripts.numerics.witness.jensen_p1b
"""
from __future__ import annotations

from math import comb, log

from flint import fmpz_poly, acb, arb, fmpq, ctx


def _hermites(N):
    Hs = [fmpz_poly([1]), fmpz_poly([0, 2])]
    x2 = fmpz_poly([0, 2])
    for n in range(1, N):
        Hs.append(x2 * Hs[n] - 2 * n * Hs[n - 1])
    return Hs


def _bw_norm(n, Hs):
    s = fmpq(0)
    for k, c in enumerate(Hs[n].coeffs()):
        ak = int(c)
        if ak:
            s += fmpq(ak * ak, comb(n, k))
    # sqrt as arb (certified)
    return arb(s.p).sqrt() / arb(s.q).sqrt()


def certified_lower_bound(d, Hs, prec=200):
    """Certified lower bound L(d) on rho_BW(d) (returns an arb lower enclosure)."""
    old = ctx.prec
    ctx.prec = prec
    Hd, Hdm1 = Hs[d], Hs[d - 1]
    bw = _bw_norm(d, Hs)
    best = None
    for root, mult in Hdm1.complex_roots():
        if float(root.imag.abs_upper()) > 1e-25:        # keep real critical points
            continue
        s = acb(root.real)                              # certified real critical point
        val = Hd(s).abs_lower()                         # |H_d(s_i)| lower enclosure (arb)
        denom = ((1 + s * s) ** (acb(d) / 2)).abs_upper()  # (1+s^2)^{d/2} upper
        ratio = arb(val) / (arb(denom) * bw)            # lower enclosure of the term
        best = ratio if best is None else (ratio if float(ratio) < float(best) else best)
    ctx.prec = old
    return best   # arb: certified L(d) <= rho_BW(d)


def summary(N=18):
    Hs = _hermites(N + 1)
    print("P1b -- certified lower bound on the Jensen slack + honest bracket\n")
    print(" d | certified L(d) <= rho_BW(d) | log(1/L)/d | (3/2)ln2=%.3f  2ln2=%.3f"
          % (1.5 * log(2), 2 * log(2)))
    ds, lr = [], []
    for d in range(2, N + 1):
        L = certified_lower_bound(d, Hs)
        Lf = float(L)
        ds.append(d)
        lr.append(log(1.0 / Lf))
        if d % 2 == 0:
            print(f"{d:2d} |   {Lf:.4e}             |   {log(1.0 / Lf) / d:6.4f}")
    # the certified bound's per-degree decay ACCELERATES (super-exponential): it is
    # edge-dominated -- min over critical points sits at the OUTERMOST s_i where
    # (1+s_i^2)^{d/2} ~ (2d)^{d/2} blows up.  So L(d) is a LOOSE (super-exp) lower bound.
    import numpy as np
    ds = np.array(ds, float)
    lr = np.array(lr)
    accel = (lr[-1] / ds[-1]) - (lr[len(lr) // 2] / ds[len(ds) // 2])
    print(f"\n[honest] the certified bound L(d) is EDGE-DOMINATED and LOOSE: log(1/L)/d keeps")
    print(f"  climbing ({lr[2]/ds[2]:.2f} -> {lr[-1]/ds[-1]:.2f}), i.e. L decays super-")
    print(f"  exponentially (the min sits at the outermost critical point, (1+s^2)^(d/2)~(2d)^(d/2)).")
    print("  So this sufficient-condition bound does NOT tightly certify the slack rate.")
    print("[what IS established]")
    print("  * P1a (certified): the discriminant ENERGY constant is (3/2)ln2 + (1/2)ln n (semicircle).")
    print("  * P1b: a direct search gives the slack ~ e^(-1.04 d) (heuristic, exponential), and")
    print("    rho_BW >= L(d) (certified but loose).  The slack is exponentially small.")
    print("[verdict / §8 backpressure] the tentative '(3/2)ln2 is the slack constant' is NOT")
    print("  confirmed: (3/2)ln2 is the discriminant ENERGY; the slack is energy + a CONDITIONING")
    print("  factor (Pardo-Pardo: disc = resultant x prod conditioning) and its exact constant is")
    print("  not tightly pinned here.  Tightening needs a non-edge-dominated certified bound")
    print("  (e.g. the 2-constraint min-norm perturbation at the shallowest interior valley).")
    return {"L_is_loose": True}


if __name__ == "__main__":
    summary()
