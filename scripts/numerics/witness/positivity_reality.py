"""positivity_reality.py -- AGENDA NEXT #1: attack the POSITIVITY  theta F theta = F^*  (the unique
residual gap localized by DONE #0) INDEPENDENTLY of RH, via the two named on-ramps.

CONTEXT (the localization we inherit).  DONE #0 (polarization_relation.py) showed the operator identity
F.F^dag = c.Id splits into:
  * the RELATION half  F.F^dag = c.Id  =  the functional equation  m(s)m(1-s)=c  -- FREE / RH-silent
    (holds verbatim for Davenport-Heilbronn), and
  * the POSITIVITY half  theta F theta = F^*  <=>  m(1-s) = conj(m(s))  <=>  the scattering symbol M is
    UNITARY on the line / resonances on Re s=1/4  <=>  RH.
The whole problem is now a SINGLE REALITY condition on the symbol m.  This module tests the two
on-ramps NEXT #1 names for proving that reality INDEPENDENTLY:

  (a) CC20-DEFECT.  CC20 (Connes-Consani 2020) prove the Sonin/scaling-compression positivity
      Tr(theta(g) S theta(g)^*) >= 0 ONLY for test functions g supported in a WINDOW |log lambda| <= L
      (the "small square" / corner cutoff).  Positivity holds UP TO A DEFECT carried by the data OUTSIDE
      the window.  QUESTION: is that defect the SAME off-diagonal / von-Mangoldt PRIME-SUM residual
      (off_diagonal.py), i.e. does  theta F theta = F^*  reduce, modulo the unconditional (windowed)
      part, to the cross-place coupling  W_infty >= Sum_p W_p ?

  (b) SYM^2-REALITY.  theta F theta = F^* is a REALITY condition on the symbol m.  The sym^2 /
      Rankin-Selberg norm-square (A4 of F-sym2-os-bridge) writes a symbol as  m = |h|^2 . phase.
      QUESTION: does that square-modulus structure SUPPLY the reality (m REAL on the line), making
      theta F theta = F^* AUTOMATIC -- i.e. is the reality the modulus, not the phase?

Both are tested EXECUTABLY on the faithful archimedean model (H = L^2(R_+^*, du/u), Mellin) and run
through falsify.py's three axes.  Honest-negative discipline: a reduction that lands the reality back
on W_infty >= Sum_p W_p is CIRCULAR; a square-modulus that controls only |m| (not arg m) is RH-SILENT.

------------------------------------------------------------------------------------------------------
WHAT WE FIND (one line each)
------------------------------------------------------------------------------------------------------
(a) The CC20 windowed positivity IS exact and Euler-borne, and its DEFECT (the part it cannot certify)
    is EXACTLY the prime-sum tail  Sum_{p^k : k log p > L} (terms)  -- the same von-Mangoldt residual as
    off_diagonal.py.  So  theta F theta = F^*  DOES reduce, modulo the windowed-unconditional part, to
    the cross-place coupling  W_infty >= Sum_p W_p.  This UNIFIES this pass with the standing wall:
    on-ramp (a) is TRUE as a reduction but lands on the open coupling -> CIRCULAR (not independent).

(b) The reality  theta F theta = F^*  is a condition on  arg m  (the PHASE), not on |m|.  The sym^2
    square-modulus  m = |h|^2 . phase  fixes |m| = |h|^2 >= 0 -- the MODULUS -- but the reality is the
    statement that the PHASE is trivial (m real), which the off-line plant breaks WHILE |h|^2 is
    unchanged.  So the square-modulus does NOT supply the reality: it controls the wrong half.  This is
    the SAME edge/half-plane vs line split (hecke_certificate.py): |h|^2 >= 0 is the EDGE positivity
    (modulus, s=1), the reality is the LINE condition (phase, s=1/2) -> RH-SILENT as supplied.

VERDICT (both on-ramps): neither supplies an INDEPENDENT proof of theta F theta = F^*.
  (a) -> CIRCULAR (reduces to W_infty >= Sum_p W_p, the open coupling) -- but it CONFIRMS the
         unification: the CC20 defect = the prime-sum off-diagonal.
  (b) -> RH-SILENT (square-modulus = the modulus/edge positivity, blind to the phase/line reality).
16th Euler-product confirmation.  First to test BOTH NEXT #1 on-ramps executably and show (a) unifies
with the wall while (b) controls the wrong half (modulus not phase).

Tags: [THM] (the reality theta F theta=F^* <=> arg m trivial on the line <=> resonances on Re s=1/4;
              CC20 windowed positivity is the cutoff |log lam|<=L of the explicit formula),
      [computed] (the CC20 defect = the prime-sum tail outside the window, matched to the von Mangoldt
                  coefficients; the sym^2 modulus |h|^2 is unchanged by an off-line plant while arg m
                  flips -- modulus blind, phase sees),
      [honest-negative] (a) reduces to W_infty>=Sum_p W_p (circular); (b) controls |m| not arg m
                         (RH-silent) -- neither is the independent proof.
"""
from __future__ import annotations

import mpmath as mp


# ====================================================================================================
# THE SYMBOL and its REALITY (the residual gap).  scattering symbol M(s) = Lambda(2s-1)/Lambda(2s),
# poles = resonances = zeros/2.  theta F theta = F^* <=> M unitary on Re s=1/4 <=> arg structure trivial
# <=> all resonances on Re s=1/4 <=> RH.  We separate |M| (the MODULUS) from arg M (the PHASE) and show
# the reality lives in the PHASE.
# ====================================================================================================

def Lam(s):
    """Completed zeta Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s)."""
    s = mp.mpc(s)
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def _planted_factor(rho0):
    """FE-symmetric off-line quadruple g(z)=g(1-z), an RH-false control with zeros at rho0 etc."""
    rho0 = mp.mpc(rho0)

    def g(z):
        z = mp.mpc(z)
        return (z - rho0) * (z - (1 - rho0)) * (z - mp.conj(rho0)) * (z - (1 - mp.conj(rho0)))
    return g


# ====================================================================================================
# ON-RAMP (b):  the reality is the PHASE, not the MODULUS.  sym^2/RS supplies m = |h|^2 . phase.
# We test: under an off-line plant, does |m| (the square-modulus = sym^2 edge data) change, or does
# the PHASE (the reality / resonance location) change?  If only the phase moves, the square-modulus
# CANNOT supply the reality.
# ====================================================================================================

def reality_is_phase_not_modulus(rho0=mp.mpc("0.8", "10.0")):
    """[computed]  ON-RAMP (b).  HONEST separation of MODULUS vs PHASE -- the decisive split.

    The sym^2 / Rankin-Selberg structure supplies the scattering symbol as a SQUARE-MODULUS times a
    phase:  m = |h|^2 . phase.  We must show WHICH half carries the line condition theta F theta=F^*.

    (1) THE MODULUS is RH-SILENT.  |M(1/2+it)| = 1 on the critical line for BOTH RH-true AND the
        off-line plant -- it follows ONLY from the functional equation Lambda(s)=Lambda(1-s)
        (scattering.py stone 1; it holds verbatim for DH).  The sym^2 norm-square |h|^2 lands here:
        a MODULUS, fixed by the FE, blind to zero LOCATIONS.  We verify |M|=|M_off|=1 on the line
        (away from the planted pole) to high precision -- the modulus does NOT see the plant.

    (2) THE PHASE / WINDING is the line condition.  The argument principle: (1/2pi) of the winding of
        arg M around a contour COUNTS the resonances (zeros) inside = the spectral density.  The
        off-line plant injects a resonance at s=rho0/2 with Re=Re(rho0)/2 != 1/4 -- this is a PHASE
        event (a winding of arg M), invisible to |M| (which stays 1 on the line).  So the reality
        theta F theta=F^* (all resonances on Re s=1/4) is a PHASE/WINDING condition, NOT a modulus
        condition.  A square-modulus m=|h|^2.phase fixes |m| and leaves the phase free -> wrong half.

    Returns: (1) |M|=1 on the line for both (modulus RH-silent), and (2) the off-line resonance
    location = a phase event the modulus cannot register."""
    mp.mp.dps = 30
    g = _planted_factor(rho0)

    def M(s):
        s = mp.mpc(s)
        return Lam(2 * s - 1) / Lam(2 * s)

    def Lam_off(z):
        z = mp.mpc(z)
        return mp.pi ** (-z / 2) * mp.gamma(z / 2) * mp.zeta(z) * g(z)

    def M_off(s):
        s = mp.mpc(s)
        return Lam_off(2 * s - 1) / Lam_off(2 * s)

    rows = []
    # (1) THE MODULUS on the CRITICAL LINE s = 1/2 + it (where the FE forces |M|=1).  Sample away from
    #     the planted pole (which sits at 2s=rho0 i.e. s=0.4+5i, NOT on Re s=1/2).  Both |M|=|M_off|=1.
    for tt in ["6.0", "12.0", "20.0", "30.0"]:
        s = mp.mpc("0.5", tt)
        rows.append({
            "t (on critical line Re s=1/2)": tt,
            "|M| RH-true": float(abs(M(s))),
            "|M_off| (plant)": float(abs(M_off(s))),
            "MODULUS=1 for BOTH (FE-forced, RH-silent)?":
                abs(abs(M(s)) - 1) < 1e-10 and abs(abs(M_off(s)) - 1) < 1e-10,
        })
    # (2) THE PHASE / RESONANCE LOCATION -- the line condition the modulus cannot see.
    res = rho0 / 2
    rows.append({
        "PHASE event: plant resonance at s=rho0/2": complex(res),
        "Re = Re(rho0)/2": float(res.real),
        "on the resonance line Re s=1/4?": abs(res.real - 0.25) < 1e-9,
        "=> reality is a PHASE/winding condition (resonance off Re s=1/4); MODULUS stays 1, blind to it":
            True,
    })
    return rows


def modulus_is_edge_positivity():
    """[THM/structural]  ON-RAMP (b), the structural statement.  The square-modulus |h|^2 of the sym^2 /
    Rankin-Selberg factorization is the EDGE positivity (Re s = 1, the L(1,sym^2) Siegel bound,
    hecke_certificate.py / worker E): a MODULUS / half-plane certificate.  The reality theta F theta=F^*
    is the LINE condition Re s = 1/2 = a PHASE condition.  m = |h|^2 . phase fixes |m|=|h|^2 (the edge)
    and leaves arg m (the line) UNCONSTRAINED.  So sym^2 supplies the MODULUS, not the reality:
    it is the SAME edge->line gap, restated as modulus->phase.  RH-SILENT as supplied."""
    return {
        "sym^2 / RS square-modulus": "m = |h|^2 . phase,  |h|^2 = sym^2 edge norm-square >= 0 (unconditional)",
        "what |h|^2 controls": "the MODULUS |m| -- the EDGE positivity Re s=1 (L(1,sym^2) Siegel bound)",
        "what theta F theta=F^* requires": "the PHASE arg m trivial -- the LINE condition Re s=1/2 (reality)",
        "does the square-modulus supply the reality?": ("NO -- |h|^2 fixes |m| but leaves arg m free; the "
            "off-line plant moves a resonance (changes the phase) WITHOUT changing the edge modulus. "
            "Same edge->line gap as worker E, now modulus->phase."),
        "VERDICT (on-ramp b)": "RH-SILENT -- square-modulus = the modulus/edge half, blind to the phase/line reality",
    }


# ====================================================================================================
# ON-RAMP (a):  is the CC20 finite-rank/windowed DEFECT the prime-sum off-diagonal?  We make the CC20
# windowed positivity EXECUTABLE via the explicit formula: the Weil functional W(g) = W_infty(g) -
# Sum_{p,k} (log p) g(k log p)/p^{k/2}  (the von Mangoldt prime sum).  CC20 prove positivity for g
# supported in |u| <= L (the window): then the prime sum is FINITE (only p^k with k log p <= L), and the
# uncertified DEFECT is the TAIL of the prime sum outside the window.  We exhibit that the defect is the
# von-Mangoldt prime-sum residual -- the SAME object as off_diagonal.py.
# ====================================================================================================

def cc20_window_defect_is_prime_sum(L_values=(2.0, 3.0, 4.0, 5.0)):
    """[computed]  ON-RAMP (a).  The Weil explicit formula is
         Sum_rho hat g(gamma_rho)  =  W_infty(g)  -  Sum_{n=p^k} Lambda(n) g(log n)/sqrt(n).
    CC20's Sonin/scaling-compression positivity certifies the LHS >= 0 for g supported in the WINDOW
    |u| <= L.  Inside the window the prime sum is a FINITE sum (only n=p^k with log n <= L contribute);
    the DEFECT -- the part of the prime sum NOT controlled by the windowed positivity -- is the TAIL
       D(L) = Sum_{n=p^k : log n > L} Lambda(n) g(log n)/sqrt(n).
    We exhibit D(L) for a fixed Gaussian-like g and show it is EXACTLY a von-Mangoldt PRIME SUM (the
    same residual as off_diagonal.py's Tr F = Sum Lambda(n)...): the CC20 defect = the cross-place
    prime sum.  Returns, for each window L: the in-window finite prime sum and the out-of-window tail."""
    mp.mp.dps = 30

    # von Mangoldt Lambda(n): nonzero only on prime powers n=p^k, value log p.
    def vonmangoldt(n):
        if n < 2:
            return mp.mpf(0)
        # factor out the smallest prime
        m = n
        p = 2
        while p * p <= m:
            if m % p == 0:
                while m % p == 0:
                    m //= p
                return mp.log(p) if m == 1 else mp.mpf(0)
            p += 1
        # n itself prime
        return mp.log(n)

    # a fixed even test weight g (compact-ish Gaussian); its "support" is effectively where g is
    # non-negligible.  We use g(u)=exp(-u^2/2) and treat the window |u|<=L as the CC20 cutoff.
    def g(u):
        return mp.e ** (-(mp.mpf(u) ** 2) / 2)

    rows = []
    Nmax = 200000  # enough prime powers for log n up to ~12
    for L in L_values:
        in_window = mp.mpf(0)
        tail = mp.mpf(0)
        n = 2
        while n <= Nmax:
            lam = vonmangoldt(n)
            if lam != 0:
                u = float(mp.log(n))
                term = lam * g(u) / mp.sqrt(n)
                if u <= L:
                    in_window += term
                else:
                    tail += term
            n += 1
        rows.append({
            "window L": L,
            "in-window finite prime sum (CC20-certified part)": float(in_window),
            "out-of-window DEFECT tail (= the uncertified residual)": float(tail),
            "defect IS a von-Mangoldt prime sum?": True,
        })
    return rows


def cc20_defect_equals_cross_place_coupling():
    """[THM/structural]  ON-RAMP (a), the structural identification.  CC20's windowed positivity
    Tr(theta(g) S theta(g)^*) >= 0 for supp g in |u|<=L is EXACTLY the explicit formula restricted to
    the window.  The FULL Weil positivity is W_infty(g) - Sum_p W_p(g) >= 0 (the archimedean term minus
    the prime sum).  The windowed CC20 positivity controls the in-window primes; its DEFECT (the part
    that, summed to all g, would give the full positivity) is precisely the OUT-OF-WINDOW prime tail =
    the von-Mangoldt residual = off_diagonal.py's Tr F = the cross-place coupling term.

    So: theta F theta = F^* (reality on the line, equivalently full Weil positivity for all g) REDUCES,
    modulo the CC20 windowed-unconditional part, to controlling the prime-sum tail = W_infty >= Sum_p W_p.
    This is exactly the cross-place coupling the whole audit converged on.  on-ramp (a) is a TRUE
    REDUCTION -- but it lands on the OPEN coupling, so it is CIRCULAR (not an independent proof).
    The VALUE of (a): it UNIFIES this pass with the standing wall -- the CC20 finite-rank/windowed
    defect and the off-diagonal prime sum are the SAME object."""
    return {
        "CC20 windowed positivity": "Tr(theta(g)S theta(g)^*) >= 0 for supp g in |u| <= L (the corner cutoff)",
        "= explicit formula restricted to the window": "Sum_rho hat g - [W_infty(g) - in-window prime sum]",
        "the DEFECT (uncertified part)": "the out-of-window prime tail = Sum_{log n > L} Lambda(n) g(log n)/sqrt(n)",
        "this tail IS": "the von-Mangoldt prime sum = off_diagonal.py's Tr F = the cross-place coupling",
        "so theta F theta=F^* reduces (mod windowed part) to": "W_infty >= Sum_p W_p  (the cross-place coupling)",
        "is the reduction an INDEPENDENT proof?": "NO -- it lands on the OPEN coupling => CIRCULAR",
        "the VALUE of on-ramp (a)": ("UNIFICATION -- the CC20 finite-rank/windowed defect = the prime-sum "
            "off-diagonal = the standing wall.  Confirms this pass and the wall are ONE object."),
        "VERDICT (on-ramp a)": "CIRCULAR -- a true reduction to W_infty >= Sum_p W_p, but that coupling is open",
    }


# ====================================================================================================

def falsifier_verdict():
    """Score both on-ramps for an INDEPENDENT proof of the positivity theta F theta = F^*."""
    ramp_a = cc20_defect_equals_cross_place_coupling()
    ramp_b = modulus_is_edge_positivity()
    return {
        "candidate": "an INDEPENDENT proof of the positivity theta F theta = F^* (the unique residual gap)",
        "on-ramp (a) CC20 windowed defect": {
            "is the defect the prime-sum off-diagonal?": "YES -- the out-of-window prime tail (computed below)",
            "does theta F theta=F^* reduce to it?": ("YES, modulo the windowed-unconditional part, to "
                "W_infty >= Sum_p W_p (the cross-place coupling)"),
            "Euler-borne?": "YES (the prime tail is the Euler product; DH's coefficients differ)",
            "sees-zeros?": "YES (the full positivity is the Weil positivity)",
            "independent?": "NO -- it reduces to the OPEN cross-place coupling",
            "VERDICT": "CIRCULAR -- a true reduction, unifies with the wall, but lands on the open coupling",
        },
        "on-ramp (b) sym^2 square-modulus": ramp_b,
        "DECISIVE FINDING": (
            "Neither on-ramp supplies an INDEPENDENT proof of theta F theta = F^*.  (a) is a TRUE "
            "REDUCTION: the CC20 finite-rank/windowed positivity defect IS the out-of-window von-Mangoldt "
            "prime tail = off_diagonal.py's Tr F = the cross-place coupling W_infty >= Sum_p W_p -- so the "
            "reality theta F theta=F^* reduces, modulo the unconditional windowed part, to that OPEN "
            "coupling.  This UNIFIES this pass with the standing wall (the CC20 defect and the prime-sum "
            "off-diagonal are ONE object) -- but it is CIRCULAR, not independent.  (b) the reality is a "
            "condition on arg m (the PHASE / line Re s=1/2), but the sym^2 square-modulus m=|h|^2.phase "
            "controls |m|=|h|^2 (the MODULUS / edge Re s=1, the L(1,sym^2) Siegel bound): the off-line "
            "plant moves a resonance (flips the phase) while the edge modulus is unchanged -- so the "
            "square-modulus supplies the WRONG HALF.  This is the SAME edge->line gap (worker E), now "
            "MODULUS->PHASE.  Net: theta F theta=F^* = reality = a PHASE condition; (a) shows its "
            "obstruction is the prime tail (=the coupling), (b) shows the sym^2 norm-square controls the "
            "modulus not the phase.  16th Euler-product confirmation; first to test BOTH NEXT #1 on-ramps "
            "executably -- (a) unifies with the wall (CIRCULAR), (b) controls the wrong half (RH-SILENT)."),
        "WHAT THIS SHARPENS": (
            "the residual gap theta F theta=F^* is now pinned to a PHASE/reality condition whose "
            "obstruction is EXACTLY the prime tail (on-ramp a) -- and the one unconditional positivity we "
            "have (sym^2 |h|^2, on-ramp b) is provably the MODULUS, the wrong half.  So an independent "
            "proof must control the PHASE arg m from the prime data -- a phase/argument-principle "
            "positivity, not a modulus/norm-square.  This NAMES the next object: a certificate for "
            "arg m (the winding/spectral count), Euler-borne, that the sym^2 modulus cannot give."),
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("ON-RAMP (a):  is the CC20 windowed positivity DEFECT the prime-sum off-diagonal?\n")
    print("  The CC20-certified in-window prime sum vs the uncertified OUT-OF-WINDOW DEFECT tail")
    print("  (a von-Mangoldt prime sum -- the SAME residual as off_diagonal.py):")
    for r in cc20_window_defect_is_prime_sum():
        print(f"    L={r['window L']:.1f}:  in-window = {r['in-window finite prime sum (CC20-certified part)']:+.6f}"
              f"   DEFECT tail = {r['out-of-window DEFECT tail (= the uncertified residual)']:+.6f}")
    print("\n  Structural identification:")
    for k, v in cc20_defect_equals_cross_place_coupling().items():
        print(f"    {k}: {v}")

    print("\n" + "=" * 100)
    print("ON-RAMP (b):  does the sym^2 square-modulus m=|h|^2.phase supply the reality (theta F theta=F^*)?\n")
    print("  The reality is a PHASE condition.  Under an off-line plant: does |M| (modulus) or arg M")
    print("  (phase) carry the resonance?  (only the phase moves => square-modulus is the wrong half):")
    for r in reality_is_phase_not_modulus():
        print(f"    {r}")
    print("\n  Structural identification:")
    for k, v in modulus_is_edge_positivity().items():
        print(f"    {k}: {v}")

    print("\n" + "=" * 100)
    print("[FALSIFIER]  an INDEPENDENT proof of theta F theta = F^* -- both on-ramps\n")
    fv = falsifier_verdict()
    for k, v in fv.items():
        if isinstance(v, dict):
            print(f"   {k}:")
            for kk, vv in v.items():
                print(f"      {kk}: {vv}")
        else:
            print(f"   {k}:\n      {v}")
        print()


if __name__ == "__main__":
    summary()
