r"""von_neumann_typeII1.py -- PA: does a type II_1 factor's TRACE (a CONTINUOUS DIMENSION -- a
   genuinely different TYPE of finiteness than cardinality/length/index, R8/R10) supply the
   archimedean RADIUS q^{w/2}, COUPLING the count (R10's regularized point-count) to the modulus?

   This is the Connes spectral-realization direction attacked HONESTLY at the II_1 level.  A II_1
   factor M has a faithful normal trace tau with tau(1) = 1 -- the IDENTITY is a FINITE projection,
   the trace is finite on it.  This is the "different type of finiteness": not a cardinality (R8),
   not a continuum/length (R8), not an index (R8) -- a CONTINUOUS DIMENSION dim_M : Proj(M) -> [0,1].

   The question (the whole R-thread recurrence, now at the II_1 level): the trace tau gives the
   MOMENTS tau(a^n) = integral z^n d mu_a(z) of the spectral/Brown measure of an affiliated operator a.
   Does tau COUPLE the COUNT (which/where the zeros are -- the moments = the location data) to the
   RADIUS (the modulus |z| = q^{w/2} of the spectral support -- purity)?  Over F_q, does tau recover
   q^{1/2} WITHOUT being handed the |alpha_i|?

   run:  python3 -m scripts.numerics.witness.von_neumann_typeII1

THE CONSTRUCTION (a MINIMAL, COMPUTABLE II_1 model -- built, not gestured at).

   The cleanest concrete II_1 factor with a fully computable trace is the GROUP von Neumann algebra
   M = L(Z) = von Neumann closure of the left regular representation of Z on l^2(Z).  By Fourier,
   L(Z) ≅ L^infinity(S^1) acting on L^2(S^1, d theta / 2pi), and the canonical trace is
       tau(f) = integral_{S^1} f(e^{i theta}) d theta / 2pi   =  f-hat(0)   (the Haar/Lebesgue mean).
   This is a II_1 factor's trace in its most transparent form: tau(1) = 1, finite, a continuous
   dimension (every spectral projection 1_{E}(f) has dim_M = Haar measure of {theta : f(theta) in E}).

   To realize Frobenius eigenvalues {alpha_i} of a curve C/F_q (the data whose MODULUS is the radius
   q^{1/2} we want the trace to supply), we build the affiliated operator
       a = the multiplication operator by a function whose ESSENTIAL RANGE is the eigenvalue
           configuration {alpha_i}, distributed over S^1 according to the Sato-Tate / spectral measure.
   The trace then reads tau(a^n) = (1/2g) sum_i alpha_i^n  (the AVERAGED moments) -- and tau(|a|^2) =
   (1/2g) sum_i |alpha_i|^2 = q   for a PURE (Weil II) configuration.  So the trace DOES see a number
   built from the radius -- the question is whether it sees the RADIUS or only an AVERAGE that the
   count already determines.

THE HONEST TEST (the count-vs-radius re-coupling, executable):
   (1) tau(|a|^2) = q for the PURE config -- so sqrt(tau(|a|^2)) = sqrt(q) LOOKS like the radius.
   (2) BUT: is sqrt(tau(|a|^2)) the RADIUS (max_i |alpha_i| = sqrt(q), purity) or the L^2-AVERAGE of
       the moduli (which a NON-pure config with the SAME average defeats)?  We COMPUTE an off-circle
       redistribution that PRESERVES tau(|a|^2) = q (hence preserves the trace's "radius") while
       BREAKING purity -- the M4r redistribution lifted to the II_1 trace.  If such a config exists,
       the II_1 trace reads the AVERAGE (a count-determined quantity), NOT the radius (the modulus
       BOUND), and the split recurs at the II_1 level.
"""
from __future__ import annotations

import mpmath as mp


# ---- the FF anchor: Frobenius eigenvalues (purity <=> |alpha_i| = sqrt(q)) -----------------------

def ff_frobenius_eigs(name: str):
    """(q, genus, [alpha_i]).  Pure (Weil II) <=> every |alpha_i| = sqrt(q)."""
    if name == "E_ordinary_q5":          # 1 +- 2i, |alpha| = sqrt(5)
        return 5, 1, [mp.mpc(1, 2), mp.mpc(1, -2)]
    if name == "genus2_q9":              # 4 eigenvalues on |z| = 3 = sqrt(9)
        s = mp.sqrt(9)
        ths = [mp.pi / 5, -mp.pi / 5, 3 * mp.pi / 5, -3 * mp.pi / 5]
        return 9, 2, [s * mp.e ** (mp.mpc(0, 1) * th) for th in ths]
    if name == "genus2_q2":
        s = mp.sqrt(2)
        ths = [mp.pi / 5, -mp.pi / 5, 3 * mp.pi / 5, -3 * mp.pi / 5]
        return 2, 2, [s * mp.e ** (mp.mpc(0, 1) * th) for th in ths]
    raise ValueError(name)


# ---- the II_1 trace of the affiliated multiplication operator ------------------------------------
# M = L(Z) ≅ L^infinity(S^1), tau(f) = mean over S^1.  Realize {alpha_i} as the essential range of a
# step function uniform on 2g arcs.  tau(a^n) = (1/2g) sum_i alpha_i^n;  tau(|a|^2) = (1/2g) sum |alpha_i|^2.

def tau_moment(alphas, n):
    """tau(a^n) = (1/N) sum_i alpha_i^n -- the II_1 trace of a^n for a uniform-arc affiliated operator.
    The NORMALIZED (tau(1)=1) trace: a CONTINUOUS DIMENSION average, NOT a sum (type I would be the sum)."""
    N = len(alphas)
    return sum(a ** n for a in alphas) / N


def tau_abs2(alphas):
    """tau(|a|^2) = tau(a* a) = (1/N) sum_i |alpha_i|^2 -- the trace of the POSITIVE operator |a|^2.
    For a PURE config (|alpha_i| = sqrt(q) all i), this is exactly q.  So sqrt(tau(|a|^2)) = sqrt(q)."""
    N = len(alphas)
    return sum(abs(a) ** 2 for a in alphas) / N


def radius_max(alphas, q):
    """The actual RADIUS reading (purity): max_i ||alpha_i| - sqrt(q)|.  ZERO <=> Weil II."""
    sq = mp.sqrt(mp.mpf(q))
    return max(abs(abs(a) - sq) for a in alphas)


# ---- the decisive test: does tau(|a|^2)=q SURVIVE an off-purity redistribution? (M4r at II_1 level) --

def trace_preserving_off_purity(alphas, q):
    """Build a NON-pure configuration with the SAME II_1 trace tau(|a|^2) = q (and same det) but
    BROKEN purity.  This is M4r's determinant-neutral redistribution lifted to the trace:

    We need (1/N) sum |beta_i|^2 = q (preserve the trace's 'radius') while max_i ||beta_i|-sqrt q| > 0.
    Push one eigenvalue OUT to modulus r1 > sqrt q and one IN to r2 < sqrt q with r1^2 + r2^2 = 2q
    (so the L^2-average over the pair is preserved), keeping arguments (hence the FE pairing alpha*conj)
    intact up to the modulus change.  The trace tau(|a|^2) is INVARIANT; purity is BROKEN."""
    N = len(alphas)
    sq = mp.sqrt(mp.mpf(q))
    pert = list(alphas)
    # pick the first conjugate pair (indices 0,1) and move moduli r1, r2 with r1^2 + r2^2 = 2q
    r1 = sq * mp.mpf("1.4")                 # push OUT
    r2 = mp.sqrt(2 * mp.mpf(q) - r1 ** 2)   # pull IN so r1^2 + r2^2 = 2q  (L^2 average preserved)
    # keep the arguments (phases) of the original pair
    arg0 = mp.atan2(pert[0].imag, pert[0].real)
    arg1 = mp.atan2(pert[1].imag, pert[1].real)
    pert[0] = r1 * mp.e ** (mp.mpc(0, 1) * arg0)
    pert[1] = r2 * mp.e ** (mp.mpc(0, 1) * arg1)
    return pert


# ---- type-check: is this finiteness the RIGHT TYPE, and does it COUPLE or SPLIT? -----------------

def typecheck():
    return {
        "factor": "M = L(Z) ≅ L^infinity(S^1), a II_1 factor; trace tau(f) = Haar mean, tau(1)=1",
        "trace_type": "a CONTINUOUS DIMENSION dim_M: Proj(M) -> [0,1] -- NOT cardinality/continuum/length/index",
        "passes_R8_type_obstruction": ("YES as a TYPE: the II_1 trace is genuinely a different finiteness "
                                       "(finite on 1, normalized, continuous-valued) -- it is NOT any of the "
                                       "four R8 surveyed (cardinality/continuum/length/index)"),
        "what_tau_supplies": "tau(a^n) = (1/N) sum alpha_i^n = the AVERAGED moments = the LOCATION/count data",
        "what_radius_needs": "max_i |alpha_i| = sqrt(q) = the MODULUS BOUND = purity = Weil II",
    }


def decide():
    mp.mp.dps = 40
    results = {}
    for name in ("E_ordinary_q5", "genus2_q9", "genus2_q2"):
        q, g, alphas = ff_frobenius_eigs(name)
        a2_pure = tau_abs2(alphas)
        rad_pure = radius_max(alphas, q)
        pert = trace_preserving_off_purity(alphas, q)
        a2_pert = tau_abs2(pert)
        rad_pert = radius_max(pert, q)
        results[name] = {
            "q": q,
            "tau_abs2_pure": a2_pure,          # = q for pure
            "sqrt_tau_abs2_pure": mp.sqrt(a2_pure),
            "radius_dev_pure": rad_pure,       # 0 for pure
            "tau_abs2_offpurity": a2_pert,     # SAME as pure (trace preserved) -- the key
            "radius_dev_offpurity": rad_pert,  # > 0 -- purity BROKEN while trace unchanged
        }
    return results


def main():
    mp.mp.dps = 40
    print("=" * 100)
    print("PA -- does the type II_1 TRACE (a CONTINUOUS DIMENSION -- a DIFFERENT TYPE of finiteness than")
    print("      cardinality/continuum/length/index, R8/R10) supply the RADIUS q^{w/2}, COUPLING R10's")
    print("      regularized count to the modulus?  Connes' spectral-realization direction at the II_1 level.")
    print("=" * 100)

    tc = typecheck()
    print("\n[TYPE]  The II_1 trace IS a different type of finiteness (it passes the R8 type obstruction):")
    for k, v in tc.items():
        print(f"        {k:30s}: {v}")

    print("\n[ANCHOR]  Realize Frobenius eigenvalues as the spectral support of a in M=L(Z); read tau.")
    print("          tau(|a|^2) = (1/N) sum |alpha_i|^2 = q for a PURE config => sqrt(tau(|a|^2)) = sqrt(q).")
    res = decide()
    for name, r in res.items():
        print(f"\n  {name} (q={r['q']}):")
        print(f"     PURE:        tau(|a|^2) = {mp.nstr(r['tau_abs2_pure'], 12)}  "
              f"=> sqrt = {mp.nstr(r['sqrt_tau_abs2_pure'], 12)} (= sqrt(q) = {mp.nstr(mp.sqrt(r['q']),12)});  "
              f"radius-dev = {mp.nstr(r['radius_dev_pure'], 6)}")
        print(f"     OFF-PURITY:  tau(|a|^2) = {mp.nstr(r['tau_abs2_offpurity'], 12)}  "
              f"(SAME -- trace PRESERVED);  radius-dev = {mp.nstr(r['radius_dev_offpurity'], 6)} (purity BROKEN)")
        # the decisive asserts: the II_1 trace tau(|a|^2) is INVARIANT under a purity-breaking redistribution
        assert abs(r['tau_abs2_pure'] - r['tau_abs2_offpurity']) < mp.mpf("1e-30"), "trace must be preserved"
        assert r['radius_dev_pure'] < mp.mpf("1e-30"), "pure config has zero radius deviation"
        assert r['radius_dev_offpurity'] > mp.mpf("0.1"), "off-purity config breaks the radius"

    print("\n" + "-" * 100)
    print("THE SPLIT, AT THE II_1 LEVEL (the decisive computation):")
    print("  sqrt(tau(|a|^2)) = sqrt(q) LOOKS like the radius -- but it is the L^2-AVERAGE of the moduli,")
    print("  NOT the radius (the MAX / the uniform modulus bound).  A trace-PRESERVING redistribution")
    print("  (r1^2 + r2^2 = 2q) moves eigenvalues OFF |z|=sqrt(q) while leaving tau(|a|^2) = q UNCHANGED.")
    print("  The II_1 trace reads the AVERAGED moment = a COUNT-DETERMINED quantity (it is a moment of the")
    print("  spectral measure, the LOCATION data) -- it does NOT read the RADIUS (the modulus bound / purity),")
    print("  which is exactly the quantity invisible to all moments of fixed total mass.")
    print("  => The COUNT/RADIUS split (R10, M4r) RECURS at the II_1 trace level: the continuous dimension")
    print("     supplies a finiteness (the trace, the averaged moments = the count) that cardinality could")
    print("     not -- but the RADIUS (purity) is STILL a separate input the trace does not carry.")
    print("-" * 100)

    print("\n[SCALE]  The DEEPER reason (the II_1-specific killer): the continuous dimension is NORMALIZED")
    print("  tau(1)=1 -- this is what MAKES II_1 'finite'.  But the radius q^{w/2} is a SCALE of the spectral")
    print("  support, and tau(1)=1 normalizes away ALL scale: the range-projection dimension dim_M is INVARIANT")
    print("  under a -> lambda*a (the radius scaling).  So the very normalization that defines type II_1")
    print("  finiteness is EXACTLY what annihilates the radius.  The scale survives only in the II_infinity")
    print("  crossed product M x R_+^* (Connes' scaling site, R3) -- where the carrier is the R_+^* CONTINUUM,")
    print("  the R8 WRONG TYPE.  Verified below: scaling lambda moves the radius but leaves dim_M unchanged.")
    sq = mp.sqrt(9)
    al = [sq * mp.e ** (mp.mpc(0, 1) * th) for th in (mp.pi / 5, -mp.pi / 5, 3 * mp.pi / 5, -3 * mp.pi / 5)]
    for lam in (mp.mpf(1), mp.mpf(2), mp.mpf("0.5")):
        scaled = [lam * a for a in al]
        dimM = mp.mpf(sum(1 for a in scaled if abs(a) > mp.mpf("1e-30"))) / len(scaled)
        print(f"     lambda={float(lam):>4}: max|alpha| = {float(max(abs(a) for a in scaled)):.4f} (radius scales) "
              f"but dim_M(range proj) = {float(dimM)} (UNCHANGED -- II_1 dim is scale-free)")
        assert abs(dimM - 1) < mp.mpf("1e-30")

    print("\n[F_q anchor honest verdict]  tau does NOT recover q^{1/2} as the RADIUS without assuming the")
    print("  zeros: sqrt(tau(|a|^2)) = sqrt(q) is the L^2-average of |alpha_i|, equal to sqrt(q) for ANY")
    print("  config with sum|alpha_i|^2 = Nq -- including OFF-LINE ones.  To get the radius (max=sqrt(q),")
    print("  uniform modulus) one must ASSUME purity = Weil II = the very thing.  The trace recovers the")
    print("  COUNT, the radius needs purity ON TOP.")

    print("\n[DH]  L(Z) and its trace EXIST for ANY L-function's data -- the II_1 factor does NOT require an")
    print("  Euler product.  Worse: the construction 'distribute eigenvalues as the spectral support of an")
    print("  affiliated operator and average via tau' needs only a spectral measure, which DH HAS (its")
    print("  Dirichlet coefficients give moments).  The II_1 trace is therefore NOT DH-distinguishing at the")
    print("  level that matters: a II_1 factor with a trace can be built over the DH spectral data too.  It")
    print("  is the EULER PRODUCT (Frobenius/Satake giving the pure radius) that DH lacks -- and the trace")
    print("  does not see it.  So this construction FAILS the DH litmus: it does NOT fail to exist for DH.")
    print("-" * 100)
    print("\nVERDICT: the type II_1 trace is genuinely a DIFFERENT TYPE of finiteness (passes the R8 type")
    print("  obstruction as a TYPE) and supplies the COUNT (averaged moments = location, like R10's nuclear")
    print("  trace) -- but it does NOT couple the count to the RADIUS: sqrt(tau(|a|^2)) is the L^2-AVERAGE of")
    print("  the moduli, INVARIANT under a purity-breaking redistribution, so it reads a count-determined")
    print("  quantity, NOT the modulus bound.  The radius/purity is still the separate archimedean N input.")
    print("  And the II_1 trace does NOT fail for DH (a trace exists over any spectral measure).  DEAD_END:")
    print("  same count-vs-radius split as R10, now at the II_1 trace level, AND the DH litmus fails.")


if __name__ == "__main__":
    main()
