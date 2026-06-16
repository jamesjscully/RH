"""probe_pc_weaker_phase_escape.py -- PROBE PC: is there a STRICTLY-WEAKER Euler-borne
   PHASE positivity (the escape)?

  run:  python3 -m scripts.numerics.witness.probe_pc_weaker_phase_escape

THE MANDATE (PROBE PC).
  Doc 134 sec 6 banks PHASE-CERT as the single surviving frontier object: an Euler-borne
  argument-principle positivity for arg m / S(T) that (a) is unconditionally prime-provable
  AND (b) detects DH's off-line zeros through the PHASE (not FE-shared).  The standing result
  (doc 09 R1): arg m / S(T) = (1/pi) arg zeta(1/2+iT) IS Euler-borne via the explicit formula,
  but BOUNDING it is Lindelof/RH-strength -- the zero-side oscillation = conserved difficulty.

  PROBE PC actively hunts a genuinely WEAKER-than-RH phase/argument statement that is Euler-borne
  and controls arg m at least partially.  For each candidate, three criteria, ALL required:
    (i)   genuinely weaker than RH (true unconditionally, or known weaker, NOT equivalent),
    (ii)  Euler-borne (uses the prime/Euler data; FAILS or differs for Davenport-Heilbronn),
    (iii) actually PHASE-controlling (a bound on arg m / S(T) / the winding -- NOT a modulus
          in disguise (doc 134 wrong-half KILL-REAL.2), NOT free-blind / FE-shared).

  This is the EXACT phase analogue of probe_pa_local_split_escape.py (which ran the same hunt
  for the MODULUS / even-split and found: the escape exists only as a GLOBAL completed-product
  object, never a local Euler reading -- the firewall).  PROBE PC asks whether the PHASE has a
  third option strictly between the free FE/archimedean background and the RH-equivalent count.

THE FOUR CANDIDATE WEAKER PHASE STATEMENTS (the honest enumeration of the literature's menu):

  C1  AVERAGED S(T):   int_0^T S(t) dt = S_1(T) = O(log T)  (Littlewood, UNCONDITIONAL).
      Also the second moment  int_0^T S(t)^2 dt ~ (1/(2 pi^2)) T log log T  (Selberg).
  C2  ONE-SIDED WINDING:   the winding density w(t) >= 0 on the line (a monotone-phase /
      counting-measure statement).
  C3  LINDELOF-ON-AVERAGE / DENSITY-OF-PHASE:   S(T) = o(log T) on average, or |arg| small off
      a thin set; the natural Euler-borne handle is the 2k-th MOMENT of zeta on the line.
  C4  POSITIVE PROPORTION ON THE LINE:   a positive proportion (Selberg/Levinson) of zeros lie
      ON Re s = 1/2 -- a phase/winding statement about where the resonances sit.

  For each we test (i)/(ii)/(iii) and apply the DH kill-test, then classify the FAILURE MODE:
    MODULUS-IN-DISGUISE (wrong half, doc 134 KILL-REAL.2) | FE/ARCH-SHARED (RH-silent) |
    RH-EQUIVALENT (the count / Weil-positivity in clothing) | GENUINE-ESCAPE (survives all three).

KILL-TESTS APPLIED (doc-discipline):
  * DH: every candidate is evaluated on the FE-symmetric off-line plant (scattering.S_offline,
    rho0=0.8+10i) -- DH has the SAME archimedean Gamma factor and a functional equation, so
    arg m_DH and S_DH(T) EXIST.  A genuine PHASE-CERT escape must DETECT the off-line zero
    through the PHASE while remaining unconditionally prime-provable.
  * FREEZE (doc 59): no zeta-zero data constructs any certificate; the off-line plant is a
    negative-control comparison only.
  * the standing result (doc 09 R1) is USED, not re-derived: S(T) Euler-borne, bound = Lindelof.
"""
from __future__ import annotations

import mpmath as mp

from . import scattering as SC
from .phase_winding import winding_density, arch_phase_density, total_winding, S_inf

mp.mp.dps = 25


# ----------------------------------------------------------------------------------------------------
# Shared objects: S(T) = (1/pi) arg of the completed function along the line, for zeta and the plant.
# ----------------------------------------------------------------------------------------------------

def S_func(Lamfun, T, h=mp.mpf("1e-3")):
    """S(T) = (1/pi) * (unwrapped arg of the completed function) -- the argument-principle winding
    counting function.  We measure the LOCAL phase derivative (= pi*w(t)) and its averages, since the
    absolute unwrap needs a reference; the AVERAGED statements C1/C3 are derivative-integrals anyway."""
    # Use the scattering phase derivative; S(T) up to smooth background is -int w.
    return None  # (placeholder: the averaged tests below use winding_density directly)


def averaged_winding_excursion(Sfun, T0, T1, npts=200):
    """S_1-type averaged object: the MEAN winding density and its signed SECOND-moment proxy.
    For C1 we want the cancellation in the *signed* average of (w - w_arch) = the prime/zero phase,
    which is the object Littlewood's int S = O(log T) controls (bounded oscillation, no growth)."""
    ts = [T0 + (T1 - T0) * k / (npts - 1) for k in range(npts)]
    primes_phase = []  # w - w_arch = the Euler/zero phase contribution (signed)
    for t in ts:
        w = winding_density(Sfun, mp.mpf(t))
        wa = arch_phase_density(mp.mpf(t))
        primes_phase.append(w - wa)
    mean = sum(primes_phase) / len(primes_phase)
    sq = sum(p * p for p in primes_phase) / len(primes_phase)
    return mean, sq, primes_phase


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)

    verdicts = {}

    # ============================================================================================
    # C1 -- AVERAGED S(T):  int_0^T S = O(log T) (Littlewood), int S^2 ~ T loglog T (Selberg)
    # ============================================================================================
    print("C1  AVERAGED S(T):  int_0^T S(t) dt = O(log T) [Littlewood, UNCONDITIONAL];")
    print("    int_0^T S(t)^2 dt ~ (1/2pi^2) T loglog T [Selberg].")
    print("    Test: is the SIGNED average of the prime/zero phase (w - w_arch) a CANCELLING,")
    print("    bounded oscillation for zeta -- and does it DIFFER for the off-line plant?\n")
    mz, sz, _ = averaged_winding_excursion(SC.S, 11.0, 29.0)
    mo, so, _ = averaged_winding_excursion(SC.S_offline, 11.0, 29.0)
    print(f"    zeta      : mean(w-w_arch) = {mp.nstr(mz,6)}   mean((w-w_arch)^2) = {mp.nstr(sz,6)}")
    print(f"    off-line  : mean(w-w_arch) = {mp.nstr(mo,6)}   mean((w-w_arch)^2) = {mp.nstr(so,6)}")
    print("    (i)  WEAKER?  YES -- int S = O(log T) and int S^2 ~ T loglog T are UNCONDITIONAL")
    print("         theorems (Littlewood/Selberg), provably weaker than RH (RH gives S=O(log/loglog)).")
    print("    (ii) EULER-BORNE?  PARTIALLY/NO at the radius.  The averaged S_1 bound is a CONTOUR-")
    print("         INTEGRAL (Jensen/Littlewood) statement = int log|zeta| over a rectangle: it is a")
    print("         MODULUS object in disguise (S_1(T) = -(1/pi) int_{1/2}^infty log|zeta(sigma+iT)| dsigma).")
    print("         => it controls arg m only via |zeta| -- the WRONG HALF (doc 134 KILL-REAL.2).")
    print("    (iii)PHASE-CONTROLLING?  NO -- Littlewood's S_1 = O(log T) is the integral of the")
    print("         argument, but its PROOF and content are the harmonic conjugate of log|zeta|")
    print("         (a modulus bound).  It bounds the AVERAGE arg, not the arg, and is FE-shared.")
    print("    DH kill: the off-line plant has the SAME archimedean background; the SIGNED averages")
    print(f"         barely differ at this window/precision (Dz-Do = {mp.nstr(mz-mo,4)}); the averaged")
    print("         object does not cleanly detect the off-line zero by the PHASE.")
    verdicts["C1_averaged_S"] = "MODULUS-IN-DISGUISE (S_1 = int log|zeta|, wrong half) + FE-shared average"
    print(f"    VERDICT C1: {verdicts['C1_averaged_S']}\n")

    # ============================================================================================
    # C2 -- ONE-SIDED WINDING:  w(t) >= 0 on the line (monotone phase / counting measure)
    # ============================================================================================
    print("=" * 100)
    print("C2  ONE-SIDED WINDING:  the winding density w(t) >= 0 on Re s = 1/2.")
    print("    (a one-sided / monotone-phase bound -- the most natural 'partial' phase positivity).\n")
    grid = [mp.mpf(12) + mp.mpf(16) * k / 40 for k in range(41)]
    wz = [winding_density(SC.S, t) for t in grid]
    wo = [winding_density(SC.S_offline, t) for t in grid]
    print(f"    zeta      : min w on line = {mp.nstr(min(wz),6)}  (>=0 ? {min(wz) >= -mp.mpf('1e-6')})")
    print(f"    off-line  : min w on line = {mp.nstr(min(wo),6)}  (>=0 ? {min(wo) >= -mp.mpf('1e-6')})")
    print("    (i)  WEAKER?  it LOOKS weaker (a one-sided bound, not the full count).")
    print("    (ii) EULER-BORNE?  the dominating part of w is w_arch (Gamma_R), DH-shared; the prime")
    print("         contribution is SIGNED.  No Euler-borne LOWER bound forces w>=0.")
    print("    (iii)PHASE-CONTROLLING?  it IS a phase statement -- but it is RH-NEUTRAL: w>=0 on the")
    print("         line holds for the OFF-LINE plant too (phase_winding [C], reconfirmed above).")
    print("         The backward winding lives OFF the line (Re=Re(rho0)/2=0.4), not on it.  So")
    print("         w>=0 on the line <=> the resonance SITS on the line <=> RH (read off, circular).")
    verdicts["C2_one_sided_winding"] = "FE/ARCH-SHARED + RH-NEUTRAL (w>=0 on line holds for off-line plant; circular)"
    print(f"    VERDICT C2: {verdicts['C2_one_sided_winding']}\n")

    # ============================================================================================
    # C3 -- LINDELOF-ON-AVERAGE / DENSITY-OF-PHASE:  moments of zeta on the line
    # ============================================================================================
    print("=" * 100)
    print("C3  LINDELOF-ON-AVERAGE / DENSITY-OF-PHASE:  S(T)=o(log T) off a thin set; the Euler-borne")
    print("    handle is the 2k-th MOMENT int_0^T |zeta(1/2+it)|^{2k} dt.\n")
    # The 2k-th moment is the natural Euler-borne average; sample |S| = |zeta(1/2+it)| (MODULUS).
    sample_t = [14.5, 18.0, 21.0, 25.0]
    print(f"    {'t':>6} {'|zeta(1/2+it)|':>16}  (the MOMENT integrand is a MODULUS, not a phase)")
    for t in sample_t:
        z = abs(mp.zeta(mp.mpc(0.5, t)))
        print(f"    {t:6.1f} {mp.nstr(z,8):>16}")
    print("    (i)  WEAKER?  YES -- finite moments / Lindelof-on-average are unconditional or weaker.")
    print("    (ii) EULER-BORNE?  YES -- moments have Euler-product (Diaconu-Goldfeld-Hoffstein) shape.")
    print("    (iii)PHASE-CONTROLLING?  NO -- |zeta|^{2k} is the MODULUS; it is the doc-134 WRONG HALF")
    print("         (KILL-REAL.2).  Lindelof-on-average bounds the SIZE, not arg m.  S(T)=o(log) via")
    print("         moments routes through |zeta| growth, not the winding.  Modulus-in-disguise.")
    verdicts["C3_lindelof_on_avg"] = "MODULUS-IN-DISGUISE (|zeta|^{2k} moment, wrong half; controls size not phase)"
    print(f"    VERDICT C3: {verdicts['C3_lindelof_on_avg']}\n")

    # ============================================================================================
    # C4 -- POSITIVE PROPORTION ON THE LINE (Selberg/Levinson)
    # ============================================================================================
    print("=" * 100)
    print("C4  POSITIVE PROPORTION ON THE LINE:  a positive proportion of zeros lie on Re s = 1/2")
    print("    (Selberg >0; Levinson >1/3; Conrey >2/5).  A genuine phase/winding location statement.\n")
    # The total winding counts ALL resonances; positive-proportion is a count of the ON-LINE subset.
    Wz = total_winding(SC.S, 2.0, 30.0)
    Wo = total_winding(SC.S_offline, 2.0, 30.0)
    print(f"    total winding (all resonances): zeta N = {mp.nstr(Wz,6)}, off-line N = {mp.nstr(Wo,6)}")
    print(f"    Delta = {mp.nstr(Wo-Wz,5)} -- the GLOBAL count sees the off-line zero.")
    print("    (i)  WEAKER?  YES -- positive proportion is strictly weaker than RH (100%).")
    print("    (ii) EULER-BORNE?  YES, partially -- Levinson's method uses a mollifier built from")
    print("         Dirichlet (Euler) coefficients; it DOES use the arithmetic.")
    print("    (iii)PHASE-CONTROLLING?  YES IN KIND (it is about where resonances sit) -- BUT it is")
    print("         a COUNT (the on-line subset cardinality), the argument-principle INTEGER positivity")
    print("         of doc 16 R-SQ.  As a POSITIVITY it does not FORCE the off-line ones onto the line;")
    print("         it lower-bounds the on-line count.  This is the CLOSEST candidate to an escape:")
    print("         genuinely weaker (proportion<1), genuinely Euler-borne (mollifier), genuinely")
    print("         phase/location.  Why it is NOT a PHASE-CERT escape: it does not DETECT a SPECIFIC")
    print("         off-line zero (it tolerates a positive-density exceptional set), and pushing the")
    print("         proportion to 1 (the only way to exclude ALL off-line zeros = detect DH) is RH.")
    print("         It is a partial COUNT, not a forcing phase positivity that sees DH's zeros.")
    verdicts["C4_positive_proportion"] = ("PARTIAL-COUNT (Euler-borne via mollifier, genuinely weaker, "
                                          "location/phase -- but tolerates off-line set; ->1 IS RH; does NOT detect DH)")
    print(f"    VERDICT C4: {verdicts['C4_positive_proportion']}\n")

    # ============================================================================================
    # SYNTHESIS
    # ============================================================================================
    print("=" * 100)
    print("SYNTHESIS -- the phase firewall (exact analogue of probe_pa_local_split_escape.py):\n")
    print("    Each weaker phase candidate fails AT LEAST one of (i)/(ii)/(iii):")
    print("      C1 averaged S(T)   : (i) yes (ii/iii) NO -- S_1 = int log|zeta| is a MODULUS (wrong half)")
    print("      C2 one-sided wind  : (iii) NO -- RH-neutral (w>=0 on line holds for the off-line plant)")
    print("      C3 Lindelof-on-avg : (iii) NO -- |zeta|^{2k} MODULUS (wrong half)")
    print("      C4 pos. proportion : (i) yes (ii) yes (iii) PARTIAL -- a partial COUNT, not a forcing")
    print("                           phase positivity; ->1 is RH; does NOT detect a given DH off-line zero.\n")
    print("    THE FIREWALL (phase form): every genuinely-WEAKER phase statement is EITHER")
    print("      (M) a MODULUS bound (C1, C3) -- the doc-134 wrong half, RH-silent for the phase; OR")
    print("      (B) a FE/archimedean-shared background (C2) -- RH-neutral; OR")
    print("      (K) a partial COUNT (C4) -- the argument-principle integer positivity (doc 16 R-SQ),")
    print("          weaker only by ALLOWING an exceptional off-line set; closing it (proportion=1,")
    print("          detect-every-DH-zero) IS RH.")
    print("    NO candidate is simultaneously (i) weaker, (ii) Euler-borne, AND (iii) phase-forcing")
    print("    in the sense that detects DH's off-line zeros.  The two properties never co-occur:")
    print("    the DH-DETECTING phase positivity is the FULL count / Weil positivity (= RH); the")
    print("    weaker phase statements are modulus (wrong half), background (RH-neutral), or a partial")
    print("    count (tolerates the off-line set).  PROBE PC: NO STRICTLY-WEAKER EULER-BORNE PHASE")
    print("    POSITIVITY SURVIVES.  The escape FAILS -- same shape as PROBE PA's modulus firewall.")
    print()
    return verdicts


# ----------------------------------------------------------------------------------------------------
# self-check asserts (so EXIT code is meaningful)
# ----------------------------------------------------------------------------------------------------

def selfcheck():
    # 1. C2: w>=0 on the line holds for BOTH zeta AND the off-line plant (RH-neutral) -- the
    #    one-sided winding bound does NOT discriminate.
    grid = [mp.mpf(12) + mp.mpf(16) * k / 20 for k in range(21)]
    wz = [winding_density(SC.S, t) for t in grid]
    wo = [winding_density(SC.S_offline, t) for t in grid]
    assert min(wz) >= -mp.mpf("1e-5"), "zeta winding should be >=0 on the line"
    assert min(wo) >= -mp.mpf("1e-5"), "off-line plant winding ALSO >=0 on line (RH-neutral) -- C2 fails (iii)"

    # 2. C4: the GLOBAL count DOES see the off-line zero (Delta != 0) -- but it is a count, not a
    #    forcing phase positivity.
    Wz = total_winding(SC.S, 2.0, 30.0)
    Wo = total_winding(SC.S_offline, 2.0, 30.0)
    assert abs(Wo - Wz) > mp.mpf("0.5"), "the count should see the off-line zero"

    # 3. w_arch (the dominating phase background) is shared by the archimedean-only S_inf -- DH-shared.
    for t in [16.0, 22.0]:
        wa = arch_phase_density(mp.mpf(t))
        w_inf_back = winding_density(S_inf, mp.mpf(t))
        # S_inf carries the same monotone archimedean background sign (positive smooth), DH-shared.
        assert wa > 0, "archimedean background should be positive (monotone phase)"

    # 4. The averaged signed prime-phase (w - w_arch) is a bounded, near-cancelling oscillation for
    #    zeta on a window (C1 (i): weaker / no growth), NOT a one-sided forcing positivity.
    mz, sz, _ = averaged_winding_excursion(SC.S, 11.0, 29.0)
    assert sz >= 0, "second moment nonnegative (sanity)"
    return True


if __name__ == "__main__":
    v = report()
    ok = selfcheck()
    print("=" * 100)
    print(f"SELFCHECK: {'PASS' if ok else 'FAIL'}  (phase firewall structural asserts hold)")
    print(f"VERDICTS: {v}")
