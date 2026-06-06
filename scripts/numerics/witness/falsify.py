"""falsify.py -- the unified falsification harness for positivity candidates (upgraded 2026-06-06).

The kill-test discipline, sharpened by the thread/worker audit. A candidate positivity for RH is
classified on three independent axes, each a falsifiable test:

  1. EULER-BORNE   -- does it FAIL for Davenport-Heilbronn (no Euler product)?  [necessary]
  2. SEES-ZEROS    -- is it SENSITIVE to a planted off-line zero (does it depend on zero LOCATIONS,
                      not just the real-axis Dirichlet coefficients)?           [necessary for content]
  3. INDEPENDENT   -- is its positivity provable WITHOUT assuming RH (not = the Weil/Li positivity)?

Four verdicts:

  DISPERSING   : not Euler-borne (holds for DH). RH-neutral. [de Branges, Nyman-Beurling, bare
                 self-adjointness, RTF/period, the unitary scattering structure]
  RH-SILENT    : Euler-borne but does NOT see the zeros -- an "Euler-product detector". It confirms
                 ζ HAS a product (passes DH) but is blind to where the zeros sit. THIS IS THE NEW
                 CATEGORY the workers exposed: QSM free energy, the prime Gram/Hankel form. The trap
                 is that these PASS the DH kill-test yet carry no RH content.
  CIRCULAR     : Euler-borne, sees the zeros, but its positivity for ζ IS RH (Weil/Li). Correct
                 forcing functional, no independent proof.
  FORCING      : Euler-borne, sees the zeros, AND independently provable. The prize. NONE YET.

The decisive upgrade over the old harness: the SEES-ZEROS axis. Passing the DH test ("has a
product") is necessary but cheap; the content is whether a candidate is sensitive to the zero
LOCATIONS. `offline_sensitivity` makes that axis executable.

Run:  python3 -m scripts.numerics.witness.falsify
"""
from __future__ import annotations

import mpmath as mp


# ---- the executable SEES-ZEROS probe -------------------------------------------------------------

def li_coeff(zeros_plus, n):
    """Li-type functional Σ_ρ [1−(1−1/ρ)^n] over a zero multiset (the canonical zero-functional)."""
    return sum((1 - (1 - 1 / mp.mpc(r)) ** n) for r in zeros_plus).real


def offline_sensitivity(zero_functional, nmax=40, rho0=mp.mpc(0.99, 2.0)):
    """Is a zero-functional SENSITIVE to a planted off-line zero quadruple? Returns (sensitive, n*).
    A functional that does not change sign when an off-line quadruple is injected is RH-SILENT."""
    on_line = [mp.mpc(0.5, 14.1347), mp.mpc(0.5, -14.1347), mp.mpc(0.5, 21.022), mp.mpc(0.5, -21.022)]
    quad = [rho0, 1 - rho0, mp.conj(rho0), 1 - mp.conj(rho0)]
    for n in range(1, nmax + 1):
        base = zero_functional(on_line, n)
        pert = zero_functional(on_line + quad, n)
        # sensitive if injecting the off-line quadruple flips the sign of the functional
        if pert < 0 <= base or (base >= 0 and pert < 0):
            return True, n
    return False, None


# ---- the classifier ------------------------------------------------------------------------------

def classify(euler_borne, sees_zeros, independent):
    if not euler_borne:
        return "DISPERSING"
    if not sees_zeros:
        return "RH-SILENT"
    if not independent:
        return "CIRCULAR"
    return "FORCING"


# candidate registry: (name, euler_borne, sees_zeros, independent, note)
REGISTRY = [
    ("Weil form / Li coefficients", True, True, False, "= RH (stone 2); the canonical forcing functional"),
    ("QSM free energy −log ζ(β)", True, False, False, "worker A: real-axis, RH-silent"),
    ("prime Gram / adelic Hankel", True, False, False, "worker B: Euler product in a Hankel skin"),
    ("Birman–Krein phase winding", True, True, False, "worker B: detects off-line zero, but counts not forces"),
    ("Beurling–Selberg / Cohn–Elkies majorant", True, False, False, "worker D: a sup over {ĝ≥0}, RH-agnostic bound"),
    ("BRS modular interpolation (primes+zeros nodes)", True, True, False, "worker D: records RH (frame⟺RH); Eisenstein dual cert = archimedean"),
    ("semilocal {∞,2} Weil form", True, False, False, "worker C: sees Euler product in VALUES, but PSD for both ζ and DH at one place"),
    ("Hecke L Li-positivity (route I)", True, True, False, "worker E: = GRH for L(s,π); circular"),
    ("sym²/Rankin–Selberg L(1,sym²) (route II)", True, False, True, "worker E: FIRST to clear independent (unconditional Siegel bound) -- but EDGE s=1, not line; RH-silent"),
    ("Hodge-index SIGNATURE of intersection form on H¹_prim", True, True, False, "signature_forcing.py: a FORM not a NUMBER -- Euler-borne (needs Satake lattice, DH-refuses) AND sees-zeros (off-circle Weil pair flips (0,2g,0)->(1,2g-2,1)); == Weil positivity over Z, CIRCULAR. Relocates ||f||²/deg·χ out of RH-SILENT"),
    ("Rosati Gram [[||f||²,Tr F],[Tr F,<F,F>]] pos-def", True, True, False, "rosati_reflection.py: reflection θ=Rosati(=FE) carries EDGE norm-square F.F'=q to CENTRE |α|=√q via Rosati positivity (det M=4q-a²≥0 ⟺ on-line, all 5 planted cases). Edge diagonal ||f||² + reflection FE both transfer to Z; missing piece = the OFF-DIAGONAL Tr(F) (primes/cross-place coupling). CIRCULAR, but wall sharpened to ONE matrix entry: RH ⟺ |Tr F|²≤<Id,Id><F,F> (a Cauchy-Schwarz the primes must satisfy)"),
    ("off-diagonal Cauchy-Schwarz |Tr F|²≤<Id,Id><F,F>", True, True, False, "off_diagonal.py: CORRECTS DONE #1. Off-diagonal Tr F IS available over Z (=von Mangoldt prime sum, RH-independent arithmetic side); edge diagonal <Id,Id>=||f||² available. The MISSING entry is the OTHER diagonal <F,F>=deg(F) (Frobenius self-norm): over F_q =2q unconditionally (deg of the correspondence); over Z it is a SUM OVER ZEROS, 'is a norm' iff RH. CS holds on-line, FAILS off-line (Weil Toeplitz min eig -2.29). CIRCULAR; the wall is the Frobenius self-norm = the missing correspondence-algebra"),
    ("Frobenius self-norm <F,F>=deg(F), ALGEBRAIC/Arakelov reading", True, False, True, "frobenius_self_norm.py: the UNCONDITIONAL reading. <F,F>=2gq = Tr(F.qF^{-1}) (Rosati uses ONLY the polarization q) = Faltings-Hriljac h_NT (a theorem). RH-BLIND: unchanged by a planted off-line zero (28.0->28.0). Pure (g,q)=topology x base-size, no zeta zeros (h_NT = height of a point on a FIXED curve's J(X_K), the 'wrong divisor'). -> RH-SILENT"),
    ("Frobenius self-norm <F,F>=deg(F), HILBERT/CC20 forcing reading", True, True, False, "frobenius_self_norm.py: the FORCING reading. <F,F>=Tr(F.F^*)=sum|alpha|² = CC20 archimedean diagonal Delta.Delta_arch=W_infty. SEES zeros (28.0->30.25 off-line). algebraic=Hilbert (Rosati F^dag=F^*) IS RH. -> CIRCULAR. The two readings are separated by EXACTLY the polarization relation F^dagger=q.F^{-1} (the missing algebra End(S²/Z) / operator identity F.F^dagger=q.Id). 14th Euler-product confirmation"),
    ("polarization RELATION F.F^dag=c.Id (=theta F theta closure)", False, False, False, "polarization_relation.py: ON-RAMP (1)+(2). The polarization relation F.F^dag=c.Id at the archimedean place IS the functional equation m(s)m(1-s)=c (a unitarity): verified =1 to ~1e-31 for BOTH RH-true AND the off-line plant (holds verbatim for DH, which has a FE) -> RH-SILENT/DISPERSING. The RELATION is NOT the wall; F^dag=(deg)F^{-1} is the free FE, not a missing structure. BC on-ramp (1) same: KMS modular sigma_t unitarity, RH-silent. Localizes the gap WITHIN the operator identity: relation-half free, positivity-half = whole problem"),
    ("polarization POSITIVITY dag=* (theta F theta=F^*, resonances on line)", True, True, False, "polarization_relation.py: the RH-content half of F.F^dag=c.Id. dag=* <=> m(1-s)=conj m(s) <=> scattering resonances (poles of M=Lam(2s-1)/Lam(2s) at rho/2) all on Re s=1/4 <=> RH. Off-line plant rho0 moves a resonance to Re=rho0/2=0.4 != 1/4, breaking it. = Weil/CC20 positivity over Z, CIRCULAR. The unique residual gap once the relation is recognized as the (free) FE. 15th Euler-product confirmation"),
    ("CC20 windowed positivity DEFECT (on-ramp a for theta F theta=F^*)", True, True, False, "positivity_reality.py: CC20 prove Tr(theta(g)S theta(g)^*)>=0 only for supp g in |u|<=L (corner cutoff). The DEFECT (uncertified part) = the OUT-OF-WINDOW prime tail Sum_{log n>L} Lambda(n)g(log n)/sqrt(n) -- a von-Mangoldt prime sum, computed decreasing 0.168->1e-5 as L:2->5 = off_diagonal.py's Tr F = the cross-place coupling W_infty>=Sum_p W_p. So theta F theta=F^* REDUCES (mod windowed part) to that OPEN coupling => CIRCULAR. UNIFIES this pass with the wall: CC20 finite-rank defect = prime-sum off-diagonal = ONE object. 16th Euler-product confirmation"),
    ("scattering-phase WINDING DENSITY w(t)=-(1/2pi)d arg S/dt (phase certificate, NEXT#1 on-ramp a forcing)", True, True, False, "phase_winding.py: the PHASE half (vs the RH-silent sym^2 MODULUS) -- the RIGHT half. w = w_arch (Euler-FREE Gamma_R phase, shared verbatim with DH) - w_zeros (resonance Poisson kernels). SEES zeros via the GLOBAL winding (Birman-Krein count: zeta 12.96 vs off-line 14.92, [B]). But (i) LOCAL density-positivity w(t)>=0 ON THE LINE is RH-NEUTRAL -- computed: the off-line plant's density is POSITIVE on Re=1/2 (a Lorentzian tail ~+4); the backward winding (~-2500) lives at Re=Re(rho0)/2=0.4, the resonance line, NOT on 1/2. So w>=0 on the line holds for the off-line plant too. (ii) the only DOMINATING positivity is the archimedean phase w_arch (Gamma_R), shared with DH => NOT Euler-borne. (iii) w>=0 read at the resonance location IS the resonances-on-line statement = RH. So the phase has the right half but is CIRCULAR: a COUNTING (global winding) not a local FORCING; dominator not Euler-borne; density-positivity = RH. Sharpens DONE#0 MODULUS/PHASE split: the PHASE is the winding count, and counting != forcing"),
    ("sym^2 square-modulus m=|h|^2.phase (on-ramp b for theta F theta=F^*)", True, False, True, "positivity_reality.py: theta F theta=F^* is a REALITY = a PHASE condition (arg m trivial / resonances on line). The sym^2/RS square-modulus supplies |m|=|h|^2 (the MODULUS, = L(1,sym^2) edge positivity Re s=1, unconditional). DECISIVE SPLIT: |M(1/2+it)|=1 on the line for BOTH RH-true AND the off-line plant (FE-forced, RH-silent) while the resonance LOCATION (phase event, Re=0.4!=1/4) distinguishes them. So the modulus is blind to the line; sym^2 controls the WRONG HALF (modulus not phase) -> RH-SILENT. Same edge->line gap as worker E, now MODULUS->PHASE"),
    ("scattering unitarity |S|=1", False, False, False, "stone 1: holds for off-line control too"),
    ("self-adjointness (Hilbert–Pólya)", False, False, False, "reflects, does not force"),
    ("de Branges reproducing kernel", False, True, False, "falsified, Conrey–Li 2000"),
    ("Nyman–Beurling / Hardy", False, False, False, "dispersing"),
    ("RTF / period (Waldspurger)", False, False, False, "central value, not zeros"),
    ("naive Yamabe / conformal Laplacian", False, False, False, "wrong sign (negative curvature)"),
]


def summary():
    mp.mp.dps = 30
    print("falsify.py -- positivity-candidate classification (upgraded with the SEES-ZEROS axis)\n")

    # demonstrate the SEES-ZEROS probe is executable and discriminating
    sens, nstar = offline_sensitivity(li_coeff)
    print(f"[SEES-ZEROS probe] Li functional sensitive to a planted off-line zero? {sens} (first n*={nstar})")
    print("   -> the canonical zero-functional SEES the zeros; a real-axis (QSM) candidate cannot.\n")

    print(f"  {'candidate':34s} {'Euler':5s} {'sees0':5s} {'indep':5s} -> verdict")
    for name, eb, sz, ind, note in REGISTRY:
        v = classify(eb, sz, ind)
        print(f"  {name:34s} {'Y' if eb else '.':5s} {'Y' if sz else '.':5s} {'Y' if ind else '.':5s} -> {v:11s}  ({note})")

    print("\n[the upgrade] the RH-SILENT verdict is new: QSM free energy and the prime Gram PASS the")
    print("  DH kill-test (Euler-borne) yet carry NO RH content -- they see the product, not the zeros.")
    print("  The prize (FORCING: Euler-borne + sees-zeros + independently provable) is still empty.")
    print("  Standing falsifier for any new candidate: run all three axes; DH-passing is necessary, cheap.")


if __name__ == "__main__":
    summary()
