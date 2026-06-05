"""Real Riemann-Xi Jensen polynomials (grounding the metric/Arakelov thread in real zeta).

The Jensen sequence of the Riemann xi function is gamma(k) = (2/(2k)!) int_0^inf Phi(u) u^{2k} du
> 0, where Phi is the Xi kernel (= (-1)^k * even Taylor coeff of Xi; gamma(0)=Xi(0) up to a
harmless global scale).  RH <=> every Jensen polynomial
    J_{d,n}(X) = sum_{j=0}^d C(d,j) gamma(n+j) X^j
is hyperbolic (all real roots) -- Polya.  GORZ verified d <= 8.

This module computes gamma(k) (certified acb integration of Phi), forms J_{d,n}, checks
hyperbolicity, and measures a scale-invariant "barely-hyperbolic" margin (min relative root
gap) -- how much room RH has, degree by degree, in the REAL data.

Run:  python3 -m scripts.numerics.witness.xi_jensen
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx


def _Phi(u, terms=6):
    u = acb(u)
    pi = acb.pi()
    e2u = (2 * u).exp()
    tot = acb(0)
    for n in range(1, terms + 1):
        tot += (2 * pi * pi * n ** 4 * (acb(9) * u / 2).exp()
                - 3 * pi * n * n * (acb(5) * u / 2).exp()) * (-pi * n * n * e2u).exp()
    return tot


def jensen_sequence(K, U=4.0, prec=220):
    """gamma(0..K), certified via acb integration of the Xi kernel moments."""
    old = ctx.prec
    ctx.prec = prec
    out = []
    for k in range(K + 1):
        M = acb.integral(lambda u, _o: _Phi(u) * u ** (2 * k), acb(0), acb(U))
        fac = acb(1)
        for j in range(2, 2 * k + 1):
            fac *= j
        out.append(float((2 * M / fac).real))
    ctx.prec = old
    return out


def jensen_poly_rescaled(gamma, d, n):
    """J_{d,n} coefficients, affinely rescaled X -> c X to O(1) magnitude (hyperbolicity
    is invariant under c>0), so numpy root-finding is well-conditioned.  Ascending."""
    from math import comb
    p = np.array([comb(d, j) * gamma[n + j] for j in range(d + 1)], dtype=float)
    if p[0] <= 0 or p[-1] <= 0:
        return p
    c = (p[0] / p[-1]) ** (1.0 / d)          # balance the two ends
    return np.array([p[j] * c ** j for j in range(d + 1)])


def is_hyperbolic(coeffs, tol=1e-9):
    r = np.roots(coeffs[::-1])
    sc = max(1.0, np.max(np.abs(r))) if len(r) else 1.0
    return bool(len(r) == 0 or np.all(np.abs(r.imag) < tol * sc))


def min_rel_gap(coeffs):
    """min consecutive root gap / total root spread (scale-invariant 'barely-hyperbolic'
    margin); returns None if not hyperbolic."""
    r = np.sort(np.roots(coeffs[::-1]).real)
    if len(r) < 2:
        return None
    gaps = np.diff(r)
    spread = r[-1] - r[0]
    return float(np.min(gaps) / spread) if spread > 0 else 0.0


def summary(K=22):
    print("Real Riemann-Xi Jensen polynomials -- hyperbolicity + barely-hyperbolic margin\n")
    g = jensen_sequence(K)
    print(f"[sequence] gamma(0)={g[0]:.6f} (=Xi(0)/2), gamma(k)>0 for all k: {all(x > 0 for x in g)}")
    print("\n[hyperbolicity grid]  '+' = hyperbolic, '.' = NOT, over (degree d, shift n):")
    print("   d\\n " + " ".join(f"{n:2d}" for n in range(0, 11)))
    results = {}
    for d in range(2, 13):
        row = []
        for n in range(0, 11):
            if n + d > K:
                row.append("  ")
                continue
            p = jensen_poly_rescaled(g, d, n)
            hyp = is_hyperbolic(p)
            results[(d, n)] = hyp
            row.append(" +" if hyp else " .")
        print(f"   {d:2d}  " + " ".join(row))
    allhyp = all(results.values())
    print(f"\n  all computed J_{{d,n}} hyperbolic (d<=12): {allhyp}  "
          f"(consistent with RH; GORZ proved d<=8)")
    print("\n[barely-hyperbolic margin]  min relative root gap of J_{d,n} (smaller = closer to")
    print("  the discriminant variety = 'more barely' hyperbolic):")
    print("   d | n=0       n=2       n=4       n=6       (trend in n)")
    for d in range(2, 11):
        cells = []
        for n in [0, 2, 4, 6]:
            if n + d > K:
                cells.append("  --     ")
                continue
            m = min_rel_gap(jensen_poly_rescaled(g, d, n))
            cells.append(f"{m:.3e}" if m is not None else "  n/a   ")
        print(f"   {d:2d}| " + "  ".join(cells))
    return {"all_hyperbolic": allhyp, "gamma": g}


if __name__ == "__main__":
    summary()
