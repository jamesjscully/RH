"""frobenius_self_norm.py -- AGENDA NEXT #1: attack the WALL, the Frobenius self-norm <F,F>=deg(F).

DONE #1 (off_diagonal.py) localized the single entry with no unconditional Z-meaning to the SECOND
DIAGONAL of the Rosati Gram, <F,F>=deg(F): over F_q it is 2q (g=1) / 2gq (the self-pairing of the
Frobenius correspondence, RH-independent); over Z it appears only as a SUM OVER ZEROS, a norm iff RH.

The agenda asks the sharp constructive question:
    WHAT GIVES <F,F>=deg(F) AN UNCONDITIONAL Z-MEANING (a Frobenius self-intersection / degree
    independent of the zeros)?
with two named candidate handles:
   (a) the Arakelov self-intersection of an arithmetic correspondence / the BGS positive-Green-form
       (a Z-degree CAN be defined, but its positivity can FAIL -- BGS Cor. 6.3.2);
   (b) the q->1 / condensed limit of the F_q degree 2q -- but it must enter as a self-intersection
       FORM's diagonal, not a bare scalar (DONE #2's caveat).

This module makes the decisive structural fact EXECUTABLE and certified.  The finding, in one line:

  <F,F>=deg(F) HAS an unconditional value over F_q ONLY BECAUSE the algebra End(Jac) supplies the
  RELATION  F^dagger = q F^{-1}  (the Rosati involution / the degree-q polarization), giving the
  OPERATOR IDENTITY  F F^dagger = q . Id  hence  <F,F> = Tr(F F^dagger) = 2gq, an RH-BLIND number.
  This SAME number, written as a Hilbert-space norm Tr(F F^*) = sum_i |alpha_i|^2, is RH-CONDITIONAL.
  The two AGREE iff |alpha_i|^2 = q for all i = RH.  So:

      * the unconditional <F,F>=2gq requires the algebra-relation F^dagger=qF^{-1} (the missing
        correspondence algebra End(S^2/Z)) -- and once you have it the number is RH-SILENT (RH-blind);
      * the RH-CONTENT is exactly the identity  <F,F>_algebraic = <F,F>_Hilbert  (Rosati = adjoint),
        i.e. the POSITIVITY of the Rosati involution, which IS RH.

Both named handles land here:
   (a) Faltings-Hriljac DOES give an unconditional Z self-intersection  <D,D> = -h_NT(D,D)  -- but it
       is the Neron-Tate height of a point on J(X_K), with NO zeta zeros in it: the algebraic / RH-SILENT
       type (the "wrong divisor", arakelov-arithmetic-surface.md S2.4).  The CC20 archimedean diagonal
       self-intersection DOES carry the zeros (= W_infty), but its positivity is the OPEN BGS 6.3 /
       Weil-positivity condition: CIRCULAR.
   (b) q->1: 2gq -> 2g.|F_1| ; the limit gives a NUMBER (RH-silent, DONE #2) unless it enters as the
       self-intersection FORM's diagonal -- and the FORM's positivity is again Rosati = adjoint = RH.

VERDICT (falsify.py three axes):  the unconditional handle (algebraic <F,F>=2gq, Arakelov h_NT) is
   EULER-BORNE? partial / NO-as-stated  (h_NT is a height of a fixed curve, blind to the Euler product),
   SEES-ZEROS? NO (RH-blind by construction),  INDEPENDENT? YES (unconditional Z-number).
   => RH-SILENT.   The forcing handle (Hilbert <F,F>, or the Rosati=adjoint identity) is
   EULER-BORNE YES, SEES-ZEROS YES, INDEPENDENT NO => CIRCULAR (= Weil positivity over Z).
   The two are SEPARATED BY EXACTLY THE POLARIZATION RELATION F^dagger=qF^{-1}: supplying it
   unconditionally over Z (an algebra End(S^2/Z) with a POSITIVE Rosati involution) is the wall.

Tags: [THM] (adjunction Gamma.Gamma=q(2-2g); Rosati F^dag=qF^{-1}=>Tr=2gq; Faltings-Hriljac),
      [computed] (the two-definitions divergence under a planted off-line zero),
      [honest-negative] (the unconditional self-norm is RH-silent; the forcing one is circular).
"""
from __future__ import annotations

import cmath

import mpmath as mp
import numpy as np


# ----------------------------------------------------------------------------------------------------
# PART A -- over F_q the self-norm is UNCONDITIONAL *because of the polarization relation* F^dag = qF^{-1}
# ----------------------------------------------------------------------------------------------------
#
# Two distinct objects both called "the Frobenius self-norm <F,F>":
#   (A.alg)  the GEOMETRIC self-intersection of the Frobenius GRAPH on C x C, via ADJUNCTION:
#               Gamma_F . Gamma_F = (2g-2) - K_S.Gamma_F = (2g-2) - (2g-2)(q+1) = q(2-2g),
#            and the ROSATI self-pairing on H^1 (rank 2g): F^dagger := q F^{-1} (the deg-q
#            polarization), F F^dagger = q.Id, so Tr(F F^dagger) = 2gq.  BOTH are computed from
#            (g, q) ALONE -- RH-INDEPENDENT -- because the ALGEBRA End(Jac) supplies F^dagger=qF^{-1}.
#   (A.hs)   the HILBERT-SPACE norm Tr(F F^*) = sum_i |alpha_i|^2 (F^* = conjugate-transpose, the
#            spectral adjoint).  This DEPENDS on where the alpha_i sit; = 2gq IFF |alpha_i|^2=q = RH.
#
# The decisive point: over F_q (A.alg) and (A.hs) COINCIDE *because RH holds there* (a theorem).
# Equivalently: the Rosati involution is POSITIVE (Tr(F F^dagger)>0 is a positive-definite form), and
# positivity of Rosati  <=>  F^dagger = F^*  <=>  |alpha_i|=sqrt q  <=>  RH.

def adjunction_self_intersection(g, q):
    """[THM] Geometric self-intersection of the Frobenius graph via adjunction on S=CxC.
    Gamma_F.Gamma_F = (2g-2) - K_S.Gamma_F, K_S=(2g-2)(f1+f2), f1.Gamma=q, f2.Gamma=1.
    Returns the exact integer = q(2-2g) -- computed from (g,q) ALONE, RH-independent."""
    pa = g                                    # Gamma_F ~ C, arithmetic genus g
    K_dot = (2 * g - 2) * (q + 1)             # K_S.Gamma_F = (2g-2)(f1.Gamma + f2.Gamma) = (2g-2)(q+1)
    GG = (2 * pa - 2) - K_dot                 # adjunction: D.D = 2p_a-2 - K.D
    return {"Gamma_F.Gamma_F (adjunction)": GG, "q(2-2g)": q * (2 - 2 * g),
            "match": GG == q * (2 - 2 * g)}


def rosati_self_norm_is_polarization(g, q, seed=0):
    """[THM/computed] The Rosati self-norm <F,F>=Tr(F F^dagger) with F^dagger:=qF^{-1} equals 2gq for
    ANY Frobenius-like F with det F = q^g -- RH-BLIND, because F^dagger=qF^{-1} uses ONLY the
    polarization degree q, not the eigenvalue locations.  We verify with a random such F."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((2 * g, 2 * g))
    A = A * (q ** g / abs(np.linalg.det(A))) ** (1.0 / (2 * g))   # det A = q^g
    Fdag = q * np.linalg.inv(A)                                   # algebraic Rosati: F^dag = q F^{-1}
    tr = float(np.trace(A @ Fdag).real)
    return {"Tr(F F^dagger), F^dagger=qF^{-1}": round(tr, 6), "2gq": 2 * g * q,
            "match (RH-blind, uses only the polarization q)": abs(tr - 2 * g * q) < 1e-6}


# ----------------------------------------------------------------------------------------------------
# PART B -- the LOAD-BEARING test: the two definitions DIVERGE exactly at an off-line zero
# ----------------------------------------------------------------------------------------------------

def two_definitions_diverge_offline(g=2, q=7, r=2.0):
    """[computed] THE decisive test.  Build a Frobenius F=diag(alpha_i) on H^1 (rank 2g), conjugate
    pairs.  Compute <F,F> two ways:
       (alg) Tr(F . qF^{-1})  -- the ALGEBRAIC Rosati (uses the polarization q);
       (hs)  Tr(F . F^*)      -- the HILBERT adjoint (the spectral norm sum|alpha|^2).
    On the CIRCLE (|alpha|=sqrt q, RH) they AGREE = 2gq.  Plant ONE off-line pair (radius r and its
    FE partner q/r): the ALGEBRAIC stays 2gq (RH-blind), the HILBERT changes (sees the zero).
    This proves: the unconditional self-norm is RH-SILENT; the forcing one is RH-conditional."""
    rng = np.random.default_rng(1)
    th = rng.uniform(0.3, np.pi - 0.3, g)
    # RH-true: |alpha|=sqrt q
    al = np.array([cmath.rect(np.sqrt(q), t) for t in th]
                  + [cmath.rect(np.sqrt(q), -t) for t in th])
    F = np.diag(al)
    alg_on = float(np.trace(F @ (q * np.linalg.inv(F))).real)
    hs_on = float(np.trace(F @ F.conj().T).real)
    # off-line: one pair to (r, q/r) respecting the FE rho<->1-rho (radii multiply to q)
    al2 = al.copy()
    al2[0] = cmath.rect(r, th[0])
    al2[g] = cmath.rect(q / r, -th[0])
    F2 = np.diag(al2)
    alg_off = float(np.trace(F2 @ (q * np.linalg.inv(F2))).real)
    hs_off = float(np.trace(F2 @ F2.conj().T).real)
    return {
        "g": g, "q": q, "2gq": 2 * g * q,
        "ON-line  <F,F>_algebraic (Tr F.qF^{-1})": round(alg_on, 4),
        "ON-line  <F,F>_Hilbert   (Tr F.F^*)":     round(hs_on, 4),
        "on-line agree?": abs(alg_on - hs_on) < 1e-6,
        "OFF-line <F,F>_algebraic (RH-blind)":     round(alg_off, 4),
        "OFF-line <F,F>_Hilbert   (sees zero)":    round(hs_off, 4),
        "off-line: algebraic unchanged (=2gq)?": abs(alg_off - 2 * g * q) < 1e-6,
        "off-line: Hilbert CHANGED (sees the zero)?": abs(hs_off - 2 * g * q) > 1e-3,
        "VERDICT": ("The unconditional self-norm <F,F>=2gq is the ALGEBRAIC Rosati Tr(F.qF^{-1}); it is "
                    "RH-BLIND (unchanged by an off-line zero) because F^dagger:=qF^{-1} uses ONLY the "
                    "polarization degree q.  The HILBERT norm Tr(F.F^*)=sum|alpha|^2 SEES the zero but "
                    "is RH-conditional.  They AGREE iff |alpha_i|^2=q for all i = RH = POSITIVITY of "
                    "the Rosati involution (F^dagger=F^*).  So the RH content is the IDENTITY "
                    "algebraic=Hilbert, not either number alone."),
    }


# ----------------------------------------------------------------------------------------------------
# PART C -- handle (a): does the Arakelov route give an unconditional Z self-norm?  Which type?
# ----------------------------------------------------------------------------------------------------

def arakelov_handle_classification():
    """[THM-citation] Classify the Arakelov candidates for an unconditional Z self-intersection.
    Faltings-Hriljac (1984/85): <D,D>_Arakelov = -h_NT(D,D), the Neron-Tate height pairing on
    J(X_K), NEGATIVE-definite on the primitive (degree-0) part.  This IS an unconditional Z-valued
    self-intersection -- but it is the height of a POINT on the Jacobian of a FIXED curve X_K, with
    NO zeta(s) eigenvalues in it (arakelov-arithmetic-surface.md S2.4, the 'wrong divisor').  So it
    is the ALGEBRAIC / RH-SILENT type: it has the unconditional VALUE but is blind to the zeros.
    The CC20 archimedean diagonal self-intersection Delta.Delta_arch = W_infty(g*g^*) DOES carry the
    zeros, but its positivity is exactly the OPEN BGS Cor.6.3.2 / Weil-positivity condition (a
    positive Green form, which BGS prove can FAIL): the CIRCULAR / forcing-shaped type."""
    return [
        {"candidate": "Faltings-Hriljac <D,D>=-h_NT(D,D)",
         "unconditional Z-value?": "YES (a theorem)",
         "sees zeta zeros?": "NO (height of a point on J(X_K), no zeta in it)",
         "type": "ALGEBRAIC / RH-SILENT (the 'wrong divisor')"},
        {"candidate": "CC20 archimedean diagonal Delta.Delta_arch = W_infty(g*g^*)",
         "unconditional Z-value?": "defined, but positivity OPEN (BGS Cor.6.3.2 can fail)",
         "sees zeta zeros?": "YES (= the explicit-formula sum over zeros)",
         "type": "CIRCULAR / forcing-shaped (= Weil positivity)"},
        {"candidate": "q->1 limit of 2gq (handle b)",
         "unconditional Z-value?": "a NUMBER 2g.|F_1| (RH-silent, DONE #2) unless it enters as a FORM",
         "sees zeta zeros?": "only via the FORM's signature (Rosati=adjoint = RH)",
         "type": "RH-SILENT as a number; CIRCULAR as the form's diagonal"},
    ]


# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    """Score BOTH the unconditional and the forcing reading of <F,F>=deg(F)."""
    div = two_definitions_diverge_offline()
    return {
        "candidate": "RH <= an unconditional Z-meaning for the Frobenius self-norm <F,F>=deg(F)",
        "the two readings": "ALGEBRAIC <F,F>=2gq (=Arakelov h_NT) vs HILBERT <F,F>=sum|alpha|^2",
        "UNCONDITIONAL reading (algebraic / Arakelov h_NT)": {
            "Euler-borne?": ("NO as stated -- h_NT is the height of a point on a FIXED curve's Jacobian, "
                             "carries no Euler product / no zeta zeros; 2gq is pure (g,q)=topology x "
                             "base-size, the same RH-silent flavor as deg.chi (DONE #2)."),
            "sees-zeros?": (f"NO -- RH-BLIND by construction: the off-line plant leaves it unchanged "
                            f"(2gq={div['2gq']}, off-line algebraic={div['OFF-line <F,F>_algebraic (RH-blind)']})."),
            "independent?": "YES -- it is an unconditional Z-number (Faltings-Hriljac is a theorem).",
            "VERDICT": "RH-SILENT.",
        },
        "FORCING reading (Hilbert / Rosati=adjoint identity / CC20 archimedean diagonal)": {
            "Euler-borne?": "YES -- the archimedean W_infty needs the Satake/prime data DH lacks.",
            "sees-zeros?": (f"YES -- the Hilbert norm changes off-line "
                            f"({div['ON-line  <F,F>_Hilbert   (Tr F.F^*)']} -> "
                            f"{div['OFF-line <F,F>_Hilbert   (sees zero)']})."),
            "independent?": "NO -- algebraic=Hilbert (Rosati=adjoint) IS RH = Weil positivity over Z.",
            "VERDICT": "CIRCULAR.",
        },
        "DECISIVE FINDING": (
            "<F,F>=deg(F) does NOT have a single Z-meaning -- it SPLITS into an unconditional RH-SILENT "
            "number (algebraic Rosati 2gq = Arakelov h_NT, blind to the zeros) and a forcing RH-conditional "
            "norm (Hilbert sum|alpha|^2 = CC20 archimedean diagonal).  The TWO ARE SEPARATED BY EXACTLY "
            "ONE RELATION: the algebraic-Rosati identity F^dagger = q F^{-1} (the deg-q polarization), "
            "which makes F F^dagger = q.Id an OPERATOR identity in End(Jac).  Over F_q that algebra EXISTS "
            "and gives 2gq unconditionally; its POSITIVITY (F^dagger=F^*) is then RH.  Over Z there is NO "
            "such algebra (no correspondence S^2/Z), so the only available <F,F> is the Hilbert one = sum "
            "over zeros = RH-conditional, and the unconditional Arakelov substitute (h_NT) is the WRONG "
            "divisor (RH-silent).  So 'what gives <F,F> an unconditional Z-meaning' = 'construct an algebra "
            "End(S^2/Z) with a POSITIVE Rosati involution F^dagger=(deg)F^{-1}' -- the SAME missing "
            "correspondence algebra, now pinned to a SINGLE OPERATOR RELATION.  14th Euler-product "
            "confirmation; sharpens the wall from 'the self-norm is missing' to 'the POLARIZATION RELATION "
            "F^dagger=(deg).F^{-1} is missing', and shows the two named handles (a Arakelov, b q->1) supply "
            "the unconditional VALUE but in the RH-SILENT (wrong-divisor) channel, never the forcing one."),
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[A] Over F_q the self-norm is unconditional BECAUSE the polarization gives F^dagger=qF^{-1}\n")
    print("  Adjunction (geometric self-intersection of the Frobenius graph):")
    for g in [1, 2, 3]:
        for q in [5, 7, 9]:
            r = adjunction_self_intersection(g, q)
            print(f"     g={g} q={q}: Gamma_F.Gamma_F={r['Gamma_F.Gamma_F (adjunction)']:4d} "
                  f"(=q(2-2g)={r['q(2-2g)']}, match={r['match']})")
    print("\n  Rosati self-pairing on H^1 (F^dagger=qF^{-1}, the deg-q polarization):")
    for g, q in [(1, 5), (2, 7), (3, 9)]:
        r = rosati_self_norm_is_polarization(g, q)
        print(f"     g={g} q={q}: Tr(F F^dagger)={r['Tr(F F^dagger), F^dagger=qF^{-1}']} "
              f"(=2gq={r['2gq']}, RH-blind match={r['match (RH-blind, uses only the polarization q)']})")
    print()

    print("=" * 100)
    print("[B] LOAD-BEARING: the two definitions DIVERGE at an off-line zero (algebraic RH-blind)\n")
    d = two_definitions_diverge_offline()
    for k, v in d.items():
        if k != "VERDICT":
            print(f"     {k}: {v}")
    print(f"\n     VERDICT: {d['VERDICT']}\n")

    print("=" * 100)
    print("[C] handle (a): the Arakelov candidates -- which give an unconditional Z self-norm, of which type\n")
    for row in arakelov_handle_classification():
        print(f"     {row['candidate']}")
        print(f"        unconditional value? {row['unconditional Z-value?']}")
        print(f"        sees zeta zeros?     {row['sees zeta zeros?']}")
        print(f"        type:                {row['type']}")
    print()

    print("=" * 100)
    print("[FALSIFIER] the Frobenius self-norm candidate, both readings\n")
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
