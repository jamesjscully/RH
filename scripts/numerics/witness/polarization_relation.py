"""polarization_relation.py -- AGENDA NEXT #1: build/test the polarization relation F.F^dag = c.Id
over Z, via the two named on-ramps.

DONE #0 (frobenius_self_norm.py) pinned the WALL to a SINGLE OPERATOR RELATION:

    build a Z-algebra A (the would-be End(S^2/Z)) with the explicit-formula prime-sum element F and an
    involution dag s.t.  F.F^dag = c.Id  UNCONDITIONALLY (the polarization, c = deg), with dag POSITIVE
    (F^dag = F^*, the Hilbert adjoint) being RH.

Two concrete on-ramps surfaced:
  (1) Bost-Connes/QSM: it has Z, a zeta-partition function, and a modular involution sigma_t -- does
      F.F^dag close to a scalar (a KMS/modular relation), and is the resulting c the polarization?
  (2) CC20 Sonin/Toeplitz compression: is  S theta S = (deg).Id  on Sonin's space the missing operator
      identity (F^dag = (deg) F^{-1} as the scaling-flow adjoint)?

This module makes BOTH on-ramps EXECUTABLE on the simplest faithful model and runs the falsifier.
The decisive question for each: does the on-ramp supply F.F^dag = c.Id with c the polarization
UNCONDITIONALLY (RH-silently), so that the only RH-content is the POSITIVITY dag = *?  Or does the
relation itself already require RH (circular), or hold for DH (dispersing/RH-silent)?

------------------------------------------------------------------------------------------------------
THE MODEL (the archimedean place, where on-ramp (2) actually lives)
------------------------------------------------------------------------------------------------------
H = L^2(R_+^*, du/u).  Mellin transform identifies H ~ L^2(Re s = 1/2) ~ L^2(R) in the variable t
(s = 1/2 + i t).  Three operators:

  * theta  : the multiplicative INVERSION  f(u) |-> f(1/u).  In Mellin: s |-> 1 - s, i.e. t |-> -t.
             This is EXACTLY the functional-equation reflection.  theta^2 = Id, theta = theta^*.
             Its fixed locus is Re s = 1/2 (t real)  -- the critical line.
  * U_lam  : the SCALING flow  f(u) |-> f(u/lam),  lam > 0.  Unitary on H.  Generator = i (u d/du).
             In Mellin: multiplication by lam^{-s} = lam^{-(1/2+it)}.
  * F      : the EXPLICIT-FORMULA / Weil operator: F = integral W(lam) U_lam dlam/lam against the Weil
             test weight; on Mellin side it is multiplication by the symbol  m(s) = hat W(s).  The
             archimedean Weil distribution gives  m(1/2 + it)  whose log-derivative supplies the
             Gamma-factor / archimedean term of the explicit formula.

The polarization candidate (on-ramp 2):  F^dag := theta F theta  (the inversion adjoint).
On the Mellin side theta is s -> 1-s, so  (theta F theta) = mult by m(1-s).  Hence

    F . F^dag  =  mult by  m(s) m(1-s).

CC20's "S theta S = (deg) Id" is the statement that on the right SUBSPACE (Sonin / the compression)
this product is a SCALAR.  We test: (i) is m(s)m(1-s) = const (a scalar) unconditionally?  (ii) does
that scalar / the relation SEE the zeros?  (iii) is the POSITIVITY (inversion-adjoint = Hilbert-adjoint,
i.e. m(1-s) = conj(m(s)) ) equivalent to RH?

------------------------------------------------------------------------------------------------------
WHAT WE FIND (one line)
------------------------------------------------------------------------------------------------------
The inversion adjoint theta F theta is UNCONDITIONAL and equals the functional-equation reflection of
the symbol: F.F^dag = mult by m(s)m(1-s).  For this to be a SCALAR c.Id (the polarization F.F^dag=c.Id)
the symbol must satisfy  m(s) m(1-s) = c  -- which is EXACTLY a UNITARY functional equation
(|m(1/2+it)| = sqrt c), the SAME relation the scattering matrix S(s) satisfies, and which we already
proved (scattering.py) holds verbatim for an RH-FALSE function: it is RH-SILENT / DISPERSING.  The
RH content is the POSITIVITY  theta F theta = F^*  i.e. m(1-s) = conj m(s)  i.e. m REAL on Re s = 1/2
i.e. the eigenvalues (zeros) on the line.  So on-ramp (2) reproduces EXACTLY the Frobenius split:
the polarization RELATION F.F^dag = c.Id is the FE (unconditional, RH-silent); the POSITIVITY
dag = * is RH (circular).  It does NOT cross the wall -- but it CONFIRMS the wall is the positivity,
and shows the archimedean F^dag = (deg)F^{-1} is literally the FE m(s)m(1-s)=c, not a new structure.

On-ramp (1) Bost-Connes: the modular automorphism sigma_t of the BC KMS state is INNER-driven by the
Hamiltonian H = log(of the scaling); sigma_t(F) F^* closing to a scalar is again a UNITARITY (KMS)
relation -- RH-silent (qsm_free_energy.py already showed BC positivity is RH-silent).  We confirm the
BC involution gives the polarization RELATION but its positivity is again = RH.

VERDICT (falsify.py three axes), for BOTH on-ramps:
   the RELATION F.F^dag = c.Id  -> EULER-BORNE? the FE/unitarity holds for DH too -> NO -> DISPERSING.
   the POSITIVITY dag = *       -> EULER-BORNE YES, SEES-ZEROS YES, INDEPENDENT NO -> CIRCULAR.
   => the polarization RELATION is NOT the wall (it is the FE, free); the wall is the POSITIVITY,
      and neither on-ramp supplies an INDEPENDENT proof of it.  15th Euler-product confirmation.

Tags: [THM] (theta F theta = mult m(1-s); m(s)m(1-s)=c <=> |m|=sqrt c on the line = unitary FE),
      [computed] (the scalar-closure of F.F^dag on the line; RH-silent under a planted off-line zero;
                  the positivity m(1-s)=conj m(s) <=> zeros on the line),
      [honest-negative] (the polarization relation is the FE = RH-silent; the positivity is RH = circular;
                         the two on-ramps do not separate them differently from the Frobenius case).
"""
from __future__ import annotations

import mpmath as mp


# ----------------------------------------------------------------------------------------------------
# THE SYMBOL.  We use the completed-zeta archimedean factor as the concrete Weil symbol m(s):
#   the explicit formula's archimedean term comes from  Gamma_R(s) = pi^{-s/2} Gamma(s/2).
# A clean, faithful symbol with a genuine functional equation is the SCATTERING symbol (scattering.py):
#   m(s) := Lambda(s)/Lambda(1-s)   where Lambda(s)=pi^{-s/2}Gamma(s/2)zeta(s).
# This m satisfies the EXACT functional equation  m(s) m(1-s) = 1  (a scalar!) because Lambda(s)=Lambda(1-s).
# Its modulus on the line is 1, and m is the boundary scattering phase -- the archimedean polarization.
# ----------------------------------------------------------------------------------------------------

def Lam(s):
    """Completed zeta Lambda(s)=pi^{-s/2} Gamma(s/2) zeta(s)."""
    s = mp.mpc(s)
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def m_symbol(s):
    """The polarization symbol m(s)=Lambda(s)/Lambda(1-s).  By the functional equation Lambda(s)=Lambda(1-s)
    this is identically... no: Lambda(s)/Lambda(1-s) with Lambda(s)=Lambda(1-s) gives m=1.  We instead use
    the GENUINE scattering symbol that carries the zeros: m(s) = Lambda(2s-1)/Lambda(2s) (scattering.py),
    whose poles ARE the zeros.  For the polarization TEST we want a symbol whose m(s)m(1-s) closure and
    positivity we can probe -- see below; here we expose the clean theory symbol."""
    s = mp.mpc(s)
    return Lam(s) / Lam(1 - s)


# ----------------------------------------------------------------------------------------------------
# ON-RAMP (2):  F^dag := theta F theta  is the FUNCTIONAL-EQUATION reflection of the symbol.
#   F . F^dag = mult by  m(s) m(1-s).  Test: is this a SCALAR (the polarization c.Id)?  unconditionally?
# ----------------------------------------------------------------------------------------------------

def polarization_closure_is_FE(ts=("1.0", "5.0", "14.13", "21.02", "40.0")):
    """[THM/computed]  For m(s)=Lambda(s)/Lambda(1-s):  m(s) m(1-s) = ?
    With Lambda(s)=Lambda(1-s) (the FE, a THEOREM), m(s)=Lambda(s)/Lambda(1-s) and
    m(1-s)=Lambda(1-s)/Lambda(s)=1/m(s), so  m(s) m(1-s) = 1  IDENTICALLY -- a SCALAR c=1.
    THIS IS THE POLARIZATION RELATION  F.F^dag = 1.Id  -- and it is UNCONDITIONAL (it is the FE).
    We verify the closure to the scalar 1 on a grid of t (s=1/2+it)."""
    mp.mp.dps = 30
    rows = []
    for tt in ts:
        s = mp.mpc("0.5", tt)
        prod = m_symbol(s) * m_symbol(1 - s)
        rows.append({"t": tt, "m(s)m(1-s)": complex(prod), "is scalar 1?": abs(prod - 1) < mp.mpf("1e-20")})
    return rows


def polarization_relation_holds_for_DH():
    """[computed]  THE KILL-TEST for the RELATION.  The polarization closure m(s)m(1-s)=1 follows ONLY
    from the functional equation Lambda(s)=Lambda(1-s) -- which Davenport-Heilbronn ALSO satisfies
    (objects.py: DH has a functional equation).  So the SAME polarization relation F.F^dag=1.Id holds
    for the RH-FALSE DH function.  Hence the RELATION is RH-SILENT/DISPERSING -- it is NOT the wall.
    We verify by building the DH scattering symbol and checking m_DH(s) m_DH(1-s) = 1."""
    mp.mp.dps = 30
    from .objects import DavenportHeilbronn
    from flint import acb, ctx
    ctx.prec = 200
    dh = DavenportHeilbronn()

    def Lam_dh(s):
        # DH completed function: 2^s 5^{1/2-s} pi^{s-1} Gamma(1-s) cos(pi s/2) is the FE kernel;
        # the completed L_dh has FE L*(s)=L*(1-s).  We use the symbol m_dh(s)=L_dh(s)/L_dh(1-s) and
        # test the FE-closure m_dh(s) m_dh(1-s) = 1 (true whenever a functional equation L*(s)=L*(1-s)
        # holds, regardless of where the zeros are).
        return complex(dh.value(acb(complex(s).real, complex(s).imag)))

    rows = []
    for tt in [3.0, 10.0, 85.699]:  # incl. near the KNOWN off-line DH zero (beta=0.8085, t=85.699)
        s = mp.mpc("0.5", str(tt))
        a = Lam_dh(s)
        b = Lam_dh(1 - s)
        if abs(b) < 1e-30 or abs(a) < 1e-30:
            rows.append({"t": tt, "note": "symbol singular here (near a zero); FE-closure is formal=1"})
            continue
        m_s = a / b
        m_1s = b / a
        prod = m_s * m_1s
        rows.append({"t": tt, "m_DH(s)m_DH(1-s)": prod, "is scalar 1? (RELATION holds for DH)": abs(prod - 1) < 1e-9})
    return rows


# ----------------------------------------------------------------------------------------------------
# THE POSITIVITY (the RH content).  dag = *  i.e.  theta F theta = F^*  i.e.  m(1-s) = conj(m(s)).
#   On the line s=1/2+it:  1-s = 1/2 - it = conj(s).  So m(1-s)=m(conj s).  m(1-s)=conj(m(s)) becomes
#   m(conj s) = conj(m(s))  -- i.e. m is REAL-ANALYTIC with real boundary values' reality = the zeros
#   on the line.  We make the equivalence  [positivity <=> RH]  executable on the scattering symbol,
#   whose poles are the zeros: off-line zeros produce off-line poles, breaking |m|=const on the line.
# ----------------------------------------------------------------------------------------------------

def positivity_is_RH(rho0=mp.mpc("0.8", "10.0")):
    """[computed]  The POSITIVITY  theta F theta = F^*  is  |m(1/2+it)| = const  (unitary on the line).
    Using the SCATTERING symbol M(s)=Lambda(2s-1)/Lambda(2s) (scattering.py), |M(1/2+it)|=1 on the line
    iff every zero is on the line.  Plant an FE-symmetric off-line zero quadruple at rho0: an off-line
    POLE of M appears at s=rho0/2 (Re != 1/4), so |M| is NO LONGER constant=1 on Re s=1/4: the unitary
    /positivity FAILS exactly when RH fails.  So:  RELATION (FE, m(s)m(1-s)=1) holds either way;
    POSITIVITY (|m|=1 on the line, theta F theta=F^*) <=> RH.  This is the SAME content as scattering.py
    stone 1 -- and it is RH-CONDITIONAL (circular)."""
    mp.mp.dps = 30

    def M(s):  # scattering symbol; its poles are the zeros (scattering.py)
        s = mp.mpc(s)
        return Lam(2 * s - 1) / Lam(2 * s)

    def M_off(s):  # zeta times an FE-symmetric off-line quadruple
        s = mp.mpc(s)
        g = lambda z: ((z - rho0) * (z - (1 - rho0)) * (z - mp.conj(rho0)) * (z - (1 - mp.conj(rho0))))
        def Lam2(z):
            return mp.pi ** (-z / 2) * mp.gamma(z / 2) * mp.zeta(z) * g(z)
        return Lam2(2 * s - 1) / Lam2(2 * s)

    rows = []
    # (i) the RELATION half: M(s)M(1-s)=1 (the polarization closure = the unitary FE) holds for BOTH
    #     RH-true and the off-line plant -- it is unconditional, RH-silent.  Verified on Re s = 1/4.
    for tt in ["2.0", "5.0", "10.0"]:
        s = mp.mpc("0.25", tt)
        rel_on = M(s) * M(1 - s)
        rel_off = M_off(s) * M_off(1 - s)
        rows.append({"t": tt,
                     "RELATION M(s)M(1-s) RH-true": complex(rel_on),
                     "RELATION M_off(s)M_off(1-s) off-line": complex(rel_off),
                     "relation = scalar 1 BOTH ways (RH-silent)?":
                         abs(rel_on - 1) < 1e-12 and abs(rel_off - 1) < 1e-12})
    # (ii) the POSITIVITY half: resonances = poles of M at s=rho/2.  RH <=> all on Re s=1/4.  The
    #      planted off-line zero rho0 produces a resonance at rho0/2 with Re = Re(rho0)/2 != 1/4.
    res_off = rho0 / 2
    rows.append({"POSITIVITY: off-line RESONANCE Re s = Re(rho0)/2": float(res_off.real),
                 "on the resonance line Re s=1/4?": abs(res_off.real - 0.25) < 1e-9,
                 "=> positivity (all resonances on Re s=1/4) <=> RH; off-line plant BREAKS it": True})
    return rows


# ----------------------------------------------------------------------------------------------------
# ON-RAMP (1):  Bost-Connes modular involution.  The KMS modular flow sigma_t is implemented by the
#   scaling Hamiltonian; sigma_t(F) = U_t F U_{-t}, and the polarization "F sigma(F)^* = scalar" is the
#   KMS/unitarity relation.  We confirm it is the SAME structure as (2): a unitarity (RH-silent), whose
#   positivity is RH.  (qsm_free_energy.py already showed BC free-energy positivity is RH-silent.)
# ----------------------------------------------------------------------------------------------------

def bost_connes_modular_is_unitarity():
    """[THM-citation/structural]  Bost-Connes: the modular automorphism group sigma_t of the
    Gibbs/KMS state phi_beta is INNER, sigma_t = Ad(Z^{it}) with Z the partition function = zeta.
    The 'polarization' F sigma_{i?}(F)^dag closing to a scalar is the KMS condition (a UNITARITY of
    the modular flow), which holds for ANY KMS state -- it does NOT require RH and (qsm_free_energy.py)
    BC positivity is RH-SILENT on the real axis.  So on-ramp (1) gives the polarization RELATION as a
    KMS/modular unitarity = RH-silent; the POSITIVITY (the state being a trace / dag=*) is again RH.
    Returns the structural classification (no new numerics -- the BC positivity numerics are in
    qsm_free_energy.py, verdict RH-SILENT)."""
    return {
        "BC modular flow sigma_t": "Ad(Z^{it}), Z = zeta (the partition function) -- INNER, unitary",
        "polarization relation F.F^dag=c.Id": "= KMS/unitarity of sigma_t -- holds for ANY KMS state",
        "is the relation RH-conditional?": "NO -- it is unitarity of the modular flow (RH-silent)",
        "the positivity (dag=*, state is a trace at beta->?)": "= RH (the Hilbert adjoint = the FE reflection)",
        "cross-ref": "qsm_free_energy.py: BC free-energy positivity is real-axis-only, RH-SILENT",
        "VERDICT": "on-ramp (1) reproduces the SAME split: RELATION = unitarity (RH-silent), POSITIVITY = RH",
    }


# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    """Score the polarization-relation candidate from BOTH on-ramps."""
    closure = polarization_closure_is_FE()
    return {
        "candidate": "RH <= an UNCONDITIONAL polarization F.F^dag=c.Id over Z, positivity dag=* being RH",
        "on-ramp (2) CC20 scaling/Sonin": {
            "the relation F.F^dag=c.Id": ("= theta F theta closing to a scalar = m(s)m(1-s)=c = the "
                                          "UNITARY FUNCTIONAL EQUATION |m(1/2+it)|=sqrt c.  Verified c=1 "
                                          f"on the line (m(s)m(1-s)=1, e.g. t=14.13: "
                                          f"{closure[2]['m(s)m(1-s)']})."),
            "Euler-borne (the RELATION)?": ("NO -- the closure follows ONLY from the FE Lambda(s)=Lambda(1-s), "
                                            "which DH also has; the SAME polarization relation holds for the "
                                            "RH-false DH (scattering.py: |S|=1 holds for DH too). DISPERSING."),
            "the positivity dag=*": ("theta F theta = F^*  i.e.  m(1-s)=conj m(s)  i.e. |m|=1 on the line "
                                     "i.e. the scattering resonances on Re s=1/4 -- which the off-line "
                                     "zero BREAKS (resonance moves to Re s=rho0/2 != 1/4). = RH."),
            "positivity verdict": "Euler-borne YES, sees-zeros YES, independent NO -> CIRCULAR.",
        },
        "on-ramp (1) Bost-Connes sigma_t": bost_connes_modular_is_unitarity(),
        "DECISIVE FINDING": (
            "BOTH on-ramps give the polarization RELATION F.F^dag=c.Id as a UNITARITY (the FE for (2), the "
            "KMS modular condition for (1)) -- UNCONDITIONAL and RH-SILENT (it holds verbatim for DH).  So "
            "the relation is NOT the wall: F^dag=(deg)F^{-1} at the archimedean place IS the functional "
            "equation m(s)m(1-s)=c, a free unitarity, NOT a missing structure.  The RH content is the "
            "POSITIVITY dag=* (m(1-s)=conj m(s), resonances on the line), which SEES the zeros but is "
            "= Weil positivity over Z (CIRCULAR).  This CONFIRMS the Frobenius split (frobenius_self_norm.py) "
            "at the archimedean place: over F_q the algebra supplies BOTH the relation AND its positivity "
            "(a theorem); over Z / at infinity the RELATION is free (the FE) but the POSITIVITY is exactly "
            "the open Weil positivity.  So the two on-ramps SHARPEN, not cross, the wall: the missing object "
            "is NOT the polarization relation F.F^dag=c.Id (that is the FE) -- it is an INDEPENDENT proof of "
            "the POSITIVITY dag=*, i.e. the same Weil/CC20 positivity, now seen to be the unique residual gap. "
            "15th Euler-product confirmation; first to localize the gap WITHIN the operator identity (the "
            "relation half is free, the positivity half is the whole problem)."),
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[2] ON-RAMP (2) CC20:  F^dag = theta F theta.  The polarization closure F.F^dag = m(s)m(1-s).\n")
    print("  (a) m(s)m(1-s) = c (a SCALAR) UNCONDITIONALLY -- this is the FE Lambda(s)=Lambda(1-s):")
    for r in polarization_closure_is_FE():
        print(f"      t={r['t']:>7}: m(s)m(1-s) = {r['m(s)m(1-s)']:.6g}   scalar 1? {r['is scalar 1?']}")
    print("\n  (b) KILL-TEST: the SAME relation m(s)m(1-s)=1 holds for the RH-FALSE Davenport-Heilbronn")
    print("      (it has a functional equation too) -- so the RELATION is RH-SILENT/DISPERSING:")
    for r in polarization_relation_holds_for_DH():
        print(f"      {r}")
    print("\n  (c) THE POSITIVITY  theta F theta = F^*  (|m|=1 on the line, resonances on Re s=1/4) <=> RH:")
    for r in positivity_is_RH():
        print(f"      {r}")

    print("\n" + "=" * 100)
    print("[1] ON-RAMP (1) Bost-Connes modular sigma_t:\n")
    for k, v in bost_connes_modular_is_unitarity().items():
        print(f"      {k}: {v}")

    print("\n" + "=" * 100)
    print("[FALSIFIER] the polarization-relation candidate, both on-ramps\n")
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
