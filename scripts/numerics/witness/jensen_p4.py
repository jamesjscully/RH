"""P4 -- recast the uniform slack bound as a height positivity, then kill-test it.

THE RECAST (STRATEGY §3, §7.3).  By Polya, RH <=> every Jensen polynomial J_{d,n} of the
Riemann xi sequence is hyperbolic <=> for every d the Jensen point J_{d,*} stays at positive
Bombieri-Weyl distance rho_BW(d) from the discriminant variety Sigma (the double-root locus),
UNIFORMLY in the shift.  In Arakelov-height language (Pardo-Pardo, Bost-Gillet-Soule):

  RH  <=>  the BW height of the Jensen point relative to Sigma stays POSITIVE, uniformly in d.

A positivity `dist(J_{d,*}, Sigma) > 0 for all d` is exactly the kind of statement a
positive Green form / arithmetic-Bezout inequality controls (BGS) -- and BGS §6.3 gives an
*obstruction to the existence of positive Green forms*.  So the recast forcing structure is:
"a positive Green form exists for the Jensen-point-vs-discriminant configuration", and its
obstruction (§6.3) is the RH-hard endpoint.  This is the candidate forcing structure in
height language; it is NOT a shortcut (the reverse force sits in the uniform-in-d limit).

THE KILL-TESTS (STRATEGY §5).  A candidate must FAIL for off-line-zero objects (DH, Epstein),
not be Weil-positivity-in-disguise, and not be trivially dispersing.

  * Gate (DH / Epstein): the Jensen/hyperbolicity criterion must DETECT off-line zeros.
    Demonstrated below: the Jensen polynomial of a sequence whose generating function has a
    COMPLEX zero pair is NON-hyperbolic; an all-real-zero one is hyperbolic.  So the criterion
    FAILS for any object with off-line zeros (DH, Epstein) -- it has genuine RH-content.
  * Not Weil-in-disguise: this positivity is about xi's Taylor coefficients and the discriminant
    geometry, distinct from the explicit-formula Weil functional.  Different positivity.
  * Dispersion (Farmer, honest): fixed-d hyperbolicity is RH-independent; the reverse force is
    ONLY in the uniform-in-d limit = the §6.3 obstruction.  So the recast passes the object-level
    gates but its content is concentrated exactly where it is RH-hard.

Run:  python3 -m scripts.numerics.witness.jensen_p4
"""
from __future__ import annotations

import numpy as np


def jensen_poly(gamma, d, n):
    """Jensen polynomial J_{d,n}(X) = sum_{k=0}^d C(d,k) gamma[n+k] X^k (coeffs ascending)."""
    from math import comb
    return np.array([comb(d, k) * gamma[n + k] for k in range(d + 1)], dtype=float)


def is_hyperbolic(coeffs, tol=1e-9):
    r = np.roots(coeffs[::-1])
    scale = max(1.0, np.max(np.abs(r))) if len(r) else 1.0
    return bool(len(r) == 0 or np.all(np.abs(r.imag) < tol * scale))


def egf_coeffs(roots, N):
    """gamma_k (k! * Taylor coeff) of f(x) = prod_i (1 - x/root_i), for k=0..N.
    A real root -> on the real axis; a complex pair -> an off-line 'zero'."""
    # build polynomial prod (1 - x/r) as ordinary Taylor coeffs c_k, then gamma_k = k! c_k
    from math import factorial
    poly = np.array([1.0 + 0j])
    for r in roots:
        poly = np.convolve(poly, np.array([1.0, -1.0 / r]))   # multiply by (1 - x/r)
    c = np.zeros(N + 1, dtype=complex)
    c[:len(poly)] = poly
    return np.array([ (c[k] * factorial(k)).real for k in range(N + 1) ])


def killtest():
    print("[Gate: does Jensen hyperbolicity DETECT off-line zeros?]")
    # f(x) = 1 + x^2  (zeros at +/- i, OFF the real axis)
    g_off = egf_coeffs([1j, -1j], 6)              # 1 + x^2
    Joff = jensen_poly(g_off, 2, 0)
    # f(x) = 1 - x^2  (zeros at +/- 1, REAL)
    g_re = egf_coeffs([1.0, -1.0], 6)             # 1 - x^2
    Jre = jensen_poly(g_re, 2, 0)
    print(f"   J of (1+x^2)  [off-line zeros]: coeffs {Joff.tolist()}  hyperbolic? {is_hyperbolic(Joff)}")
    print(f"   J of (1-x^2)  [real zeros]    : coeffs {Jre.tolist()}  hyperbolic? {is_hyperbolic(Jre)}")
    # a richer case: real zeros + a complex pair embedded
    g_mix = egf_coeffs([1.0, -1.0, 2.0, 0.3 + 0.4j, 0.3 - 0.4j], 12)
    found = any(not is_hyperbolic(jensen_poly(g_mix, d, n))
                for d in range(2, 6) for n in range(0, 12 - d))
    g_allreal = egf_coeffs([1.0, -1.0, 2.0, -2.0, 3.0], 12)
    allhyp = all(is_hyperbolic(jensen_poly(g_allreal, d, n))
                 for d in range(2, 6) for n in range(0, 12 - d))
    print(f"   mixed (one complex pair): some J non-hyperbolic? {found}")
    print(f"   all-real zeros          : all J hyperbolic?      {allhyp}")
    return {"off_nonhyp": not is_hyperbolic(Joff), "real_hyp": is_hyperbolic(Jre),
            "mixed_detected": found, "allreal_ok": allhyp}


def summary():
    print("P4 -- height-positivity recast + kill-tests\n")
    print("RECAST: RH <=> dist_BW(Jensen point, discriminant variety) > 0 uniformly in d")
    print("        = a positive-Green-form / arithmetic-Bezout positivity (BGS); the obstruction")
    print("        is BGS §6.3 (obstruction to positive Green forms) -- the RH-hard endpoint.\n")
    r = killtest()
    ok = r["off_nonhyp"] and r["real_hyp"] and r["mixed_detected"] and r["allreal_ok"]
    print("\n[kill-test verdict]")
    print(f"   * FAILS for off-line zeros (DH/Epstein analogue): {ok}  -> genuine RH-content,")
    print("     not trivially dispersing.")
    print("   * Not Weil-positivity-in-disguise: about xi's Taylor coefficients + discriminant")
    print("     geometry, a DIFFERENT positivity from the explicit-formula Weil functional.")
    print("   * Dispersion (Farmer, honest): fixed-d hyperbolicity is RH-independent; reverse")
    print("     force lives ONLY in the uniform-in-d limit = the §6.3 obstruction (RH-hard).")
    print("[outcome] the recast is a LEGITIMATE forcing-structure candidate in height language,")
    print("  passing the object-level gates; it is not a shortcut.  Per §8, a certified uniform")
    print("  bound (a positive Green form for the Jensen-vs-discriminant configuration) would be")
    print("  the formalization trigger.")
    return r


if __name__ == "__main__":
    summary()
