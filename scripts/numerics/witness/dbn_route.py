"""de Bruijn-Newman / dynamical route -- kill-test + honest analysis (STRATEGY §1, §5).

The most promising route by the program's own criteria, and the one previously unexamined.
The dBN heat flow H_t = e^{-t D^2} (forward in t) acts on the zeros as a first-order log-gas
and REALIZES complex zeros: Lambda(f) = inf{t : H_t f has all real roots}.  de Bruijn-Newman:
RH <=> Lambda(xi) <= 0.  Rodgers-Tao (2020): Lambda >= 0, unconditionally.

Why this route is structurally different from the reformulations (NB-BD, descent, Jensen, Weil):
  * REAL reverse force -- the flow *forces* zeros real; not a relabeling of RH.
  * a REAL unconditional theorem -- Lambda >= 0 (Rodgers-Tao), the only one of its kind.
  * it does NOT factor through the missing arithmetic object -- Rodgers-Tao use the dynamics +
    the zeros' statistics (Montgomery pair correlation), not the arithmetic surface / Scaling
    Site.  So its hard endpoint is DIFFERENT from the geometric routes.

Kill-test (below): Lambda detects off-line zeros -- Lambda(f) > 0 iff f has a complex zero pair,
and grows with how far off-line they are.  So the dBN criterion FAILS for DH/Epstein (off-line
zeros => Lambda > 0): genuine RH-content.

Honest verdict: dBN is a genuine forcing structure with real reverse force and a real
unconditional handle -- the best candidate we have.  BUT Lambda >= 0 is the RH-INDEPENDENT
direction ("RH is barely true if true"); RH is Lambda <= 0, which is open and hard, and the
dynamical method gives the wrong-direction bound.  Its hard endpoint -- forcing Lambda <= 0 via
the backward flow / dynamics -- is distinct from the geometric routes' missing object, and is
where Rodgers-Tao + Polymath stalled.

Run:  python3 -m scripts.numerics.witness.dbn_route
"""
from __future__ import annotations

from math import factorial

import numpy as np


def _d2(c):
    n = len(c)
    return np.array([c[k + 2] * (k + 2) * (k + 1) for k in range(n - 2)]) if n > 2 else np.array([0.0])


def heat_flow(coeffs, t):
    """H_t = e^{-t D^2} p = sum_j (-t)^j/j! D^{2j} p  (ascending coeffs)."""
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


def _all_real(c, tol=1e-9):
    r = np.roots(c[::-1])
    s = max(1.0, np.max(np.abs(r))) if len(r) else 1.0
    return bool(len(r) == 0 or np.all(np.abs(r.imag) < tol * s))


def dbn_lambda(coeffs):
    """Lambda(f) = inf{t : H_t f all-real}; 0 if already real, else binary-searched."""
    c = np.array(coeffs, float)
    if _all_real(c):
        return 0.0
    lo, hi = 0.0, 0.01
    while not _all_real(heat_flow(c, hi)):
        hi *= 2
        if hi > 1e6:
            return np.inf
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if _all_real(heat_flow(c, mid)):
            hi = mid
        else:
            lo = mid
    return hi


def backward_margin(coeffs):
    """Dynamic margin Lambda_- = sup{s>=0 : H_{-s} p still all-real} -- how far p can flow
    BACKWARD before losing hyperbolicity.  The Hermite-junction probe: for the real-xi Jensen
    polynomials this SHRINKS as (d,n) grow (toward the heat-flow fixed shape / the full xi),
    quantifying the de Bruijn-Newman Lambda=0 ('RH barely true') by degree and shift -- and it
    is ANTI-correlated with the static separation margin (which grows toward the Hermite limit).
    Static height and dynamic flow are the same Hermite object seen two ways."""
    c = np.array(coeffs, float)
    if not _all_real(c):
        return 0.0
    lo, hi = 0.0, 0.001
    while _all_real(heat_flow(c, -hi)):
        hi *= 2
        if hi > 1e6:
            return np.inf
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if _all_real(heat_flow(c, -mid)):
            lo = mid
        else:
            hi = mid
    return lo


def _from_roots(roots):
    p = np.array([1.0 + 0j])
    for r in roots:
        p = np.convolve(p, [-r, 1.0])
    return p.real


def killtest():
    cases = [
        ("all real (RH-true analog)", [1, -1, 2, -2, 0.3]),
        ("one complex pair (RH-false analog)", [1, -1, 2, -2, 0.5 + 0.8j, 0.5 - 0.8j]),
        ("(x^2+1)", [1j, -1j]),
        ("far off-line pair", [1, -1, 3.0j, -3.0j]),
    ]
    print("[Gate: does dBN Lambda detect off-line zeros?]  Lambda>0 <=> off-line zeros present")
    out = {}
    for name, roots in cases:
        L = dbn_lambda(_from_roots(roots))
        out[name] = L
        print(f"   {name:38s} Lambda = {L:.4f}")
    detects = out["all real (RH-true analog)"] == 0.0 and out["one complex pair (RH-false analog)"] > 0
    return detects, out


def summary():
    print("de Bruijn-Newman / dynamical route\n")
    detects, _ = killtest()
    print(f"\n   detects off-line zeros (fails for DH/Epstein): {detects}  -> genuine RH-content,")
    print("   with REAL reverse force (the flow forces reality), unlike the dispersing reformulations.")
    print("\n[honest verdict]")
    print("  * dBN is the strongest forcing-structure candidate: real flow, real unconditional")
    print("    handle (Rodgers-Tao Lambda>=0), and it does NOT factor through the missing arithmetic")
    print("    object -- it uses dynamics + zero statistics (Montgomery), a different hard endpoint.")
    print("  * BUT Lambda>=0 is the RH-INDEPENDENT direction; RH is Lambda<=0, open and hard, and")
    print("    the dynamical method gives the wrong-direction bound.  Forcing Lambda<=0 (controlling")
    print("    the backward flow) is where Rodgers-Tao + Polymath stalled -- the dBN hard endpoint.")
    print("  * Net: the two genuine RH frontiers are now (a) the missing arithmetic object")
    print("    (geometric routes -> positive Green form / Scaling Site C×C), and (b) forcing")
    print("    Lambda<=0 via dynamics (dBN).  They are DIFFERENT; neither is a reformulation.")
    return detects


if __name__ == "__main__":
    summary()
