"""rosati_reflection.py -- method.md step 2 re-run with the UNIFIED axiom (AGENDA NEXT #1).

THE UNIFIED OPEN IMPLICATION (DONE #1 collapsed the two threads to one positivity):
    (sym^2 coefficients form a NORM-SQUARE at the edge s=1)
        ==>  (the H^1_prim intersection FORM is negative-definite / the OS form is positive at s=1/2).

The agenda names the lever sharply:  the Rosati positivity  F^* F = q  is a THEOREM over F_q -- what
is its Z-analog?  And the decisive question for step 2:

    IS THERE A REFLECTION / INVOLUTION under which the EDGE norm-square becomes the NEGATIVE-DEFINITE
    PRIMITIVE FORM at the CENTRE?

This module answers it by making the function-field archetype EXECUTABLE end to end, then locating
EXACTLY where the implication holds (F_q) and where it must be supplied (Z).  Honest negatives valued.

----------------------------------------------------------------------------------------------------
THE MECHANISM, OBJECT-FREE (method.md step 1, sharpened to name the reflection).
----------------------------------------------------------------------------------------------------
Over F_q the chain edge -> centre is:

  (i)   EDGE NUMBER (unconditional, s=1 analog):  deg(Frob) = q.  Equivalently the Rosati identity
        F . F' = q  in End(Jac)(x)Q, where ' is the ROSATI INVOLUTION.  This is a DEGREE -- the
        function-field shadow of the Petersson/Rankin-Selberg edge residue ||f||^2 = Res_{s=1}L(s,fxf).
        (Both are "the norm-square at the edge": F.F' = q = deg; ||f||^2 = the L(1) residue.)

  (ii)  THE REFLECTION:  theta(phi) = phi'  (Rosati).  On eigenvalues  theta: alpha |-> q/alpha-bar.
        Its FIXED LOCUS is exactly |alpha| = sqrt(q)  <=>  Re s = 1/2.  theta IS the functional
        equation s -> 1-s.  (alpha = q^s under q^{-s}=alpha^{-1}; theta sends s -> 1-s.)

  (iii) ROSATI POSITIVITY (THE LEVER, a THEOREM over F_q):  the Rosati trace form
            < phi, psi >  :=  Tr( phi . psi' )   on End(Jac)(x)R  is POSITIVE-DEFINITE.
        This positivity, applied to  phi = F + F' = a (trace) and the identity F.F' = q, gives
            a^2 <= 4q   (Hasse/Weil)   <=>   |alpha| = sqrt(q)   <=>   RH for the curve.

So the object-free mechanism is EXACTLY the agenda's question realized:  the reflection theta = Rosati
involution carries the EDGE NORM-SQUARE (F.F' = q, a positive number) into the CENTRE constraint
(|alpha|=sqrt q) THROUGH the POSITIVE-DEFINITENESS of the Rosati trace form.  The "edge norm-square
becomes the negative-definite primitive form at the centre" is, in the function field, a THEOREM:
the Rosati form < phi,phi > = Tr(phi phi') >= 0 IS the negative-definite primitive intersection form
(up to the sign convention -1x, DONE #1) and IS sourced by the degree F.F'=q at the edge.

THE WHOLE QUESTION over Z:  is the Rosati POSITIVITY available without assuming RH?  We test the chain
edge(deg=q) --Rosati positivity--> centre(|alpha|=sqrt q) executably, then audit each link's Z-analog.

Tags: [THM] (Rosati positivity over F_q, classical Weil), [computed] (the executable chain), [CONJ]
(the Z-analog of Rosati positivity = the unmoved wall).
"""
from __future__ import annotations

import cmath

import mpmath as mp
import numpy as np


# ----------------------------------------------------------------------------------------------------
# 1. The EDGE number: the Rosati identity F.F' = q (the function-field ||f||^2)
# ----------------------------------------------------------------------------------------------------

def rosati_edge_identity(q, alphas):
    """[THM] Rosati: F . F' = q = deg(Frob), where F' = q/F is the Rosati adjoint.  On eigenvalues
    alpha_k, the adjoint has eigenvalue q/alpha_k, and  alpha_k * (q/alpha_k) = q  for EVERY k --
    the identity is unconditional (true off-line too: it is the DEGREE, not RH).  We verify the
    PRODUCT alpha_k * (q/alpha_k) = q exactly, and report |alpha_k| (which RH constrains, the identity
    does NOT)."""
    rows = []
    for a in alphas:
        a = complex(a)
        adj = q / a                      # Rosati adjoint eigenvalue
        prod = a * adj                    # = q identically
        rows.append({
            "alpha": a, "F'=q/alpha (adjoint)": adj, "alpha*(q/alpha) = F.F'": prod,
            "== q exactly?": abs(prod - q) < 1e-9, "|alpha| (RH: =sqrt q)": abs(a),
        })
    return rows


# ----------------------------------------------------------------------------------------------------
# 2. The REFLECTION theta = Rosati involution; its FIXED LOCUS is |alpha|=sqrt(q) = Re s = 1/2
# ----------------------------------------------------------------------------------------------------

def reflection_fixed_locus(q, alphas):
    """theta(alpha) = q / alpha-bar  is the Rosati involution on eigenvalues (= the functional equation
    s -> 1-s).  theta(alpha) = alpha  <=>  q/alpha-bar = alpha  <=>  |alpha|^2 = q  <=>  |alpha|=sqrt q.
    So the FIXED LOCUS of the reflection is EXACTLY the critical line.  We measure |theta(alpha)-alpha|:
    zero <=> on the line."""
    s = float(mp.sqrt(q))
    rows = []
    for a in alphas:
        a = complex(a)
        th = q / a.conjugate()
        rows.append({
            "alpha": a, "theta(alpha)=q/alpha-bar": th,
            "|theta(alpha) - alpha| (0 <=> on line)": abs(th - a),
            "on fixed locus |alpha|=sqrt q?": abs(abs(a) - s) < 1e-7,
        })
    return rows


# ----------------------------------------------------------------------------------------------------
# 3. THE LEVER: the Rosati TRACE FORM is positive-definite, and that POSITIVITY forces the line
# ----------------------------------------------------------------------------------------------------

def rosati_trace_form(q, alphas, test_vectors=None):
    """[THM over F_q] The Rosati trace form  <phi, psi> = Tr(phi psi')  on End(Jac)(x)R is POSITIVE
    DEFINITE.  We model End acting on H^1 (the 2g-dim eigenspace) by DIAGONAL operators phi = diag(c_k)
    in the Frobenius eigenbasis; the Rosati adjoint is phi' = diag(q * conj(c_k) / |?|...) -- precisely,
    on H^1 with the Weil/polarization pairing, the Rosati adjoint of multiplication-by-alpha is
    multiplication-by  q/alpha-bar = theta(alpha).  So for phi = diag over eigen-lines with coefficient
    x_k on the line carrying alpha_k:

        <phi, phi> = Tr(phi phi') = sum_k x_k * conj(theta-action) ...

    The CLEAN, faithful model (matching Weil's a^2<=4q derivation): the Rosati form restricted to the
    R-span of {1, F} is the 2x2 Gram matrix in the basis (Id, F):

        M = [[ <1,1>,   <1,F>  ],
             [ <F,1>,   <F,F>  ]]
          = [[ Tr(Id),      Tr(F') = Tr(F)   ],
             [ Tr(F)= Tr(F'),  Tr(F F') = Tr(q) ]]   (using Tr on the 2-dim H^1 of an elliptic curve)

    For an elliptic curve: Tr(Id)=2, Tr(F)=a=alpha+beta (the trace of Frobenius, REAL integer),
    Tr(F.F')=Tr(q)=2q.  So

        M = [[2, a], [a, 2q]],   det M = 4q - a^2.

    ROSATI POSITIVITY  <=>  M positive-definite  <=>  det M = 4q - a^2 > 0  <=>  a^2 < 4q  <=>
    |alpha| = sqrt q (the Hasse/Weil bound = RH for the elliptic curve).  THE POSITIVE-DEFINITENESS
    OF THE EDGE-SOURCED ROSATI FORM IS, LITERALLY, RH FOR THE CURVE.  This is the executable witness
    that the reflection (Rosati) + the edge number (F.F'=q) + positivity ==> the line."""
    # a = trace of Frobenius = sum of eigenvalues (real for an elliptic curve / self-conjugate set)
    a = sum(complex(x) for x in alphas).real
    M = np.array([[2.0, a], [a, 2.0 * float(q)]])
    ev = np.linalg.eigvalsh(M)
    det = 4.0 * float(q) - a * a
    pos_def = bool((ev > 1e-9).all())            # det > 0 : a^2 < 4q  (strictly inside the disc)
    pos_semidef = bool((ev > -1e-9).all())        # det >= 0 : a^2 <= 4q (on or inside = RH for the curve)
    s = float(mp.sqrt(q))
    max_off = max(abs(abs(complex(x)) - s) for x in alphas)
    on_line = max_off < 1e-6
    return {
        "trace of Frobenius a": a,
        "Rosati Gram M = [[2,a],[a,2q]]": M.tolist(),
        "det M = 4q - a^2": det,
        "eigenvalues of M": [round(float(x), 6) for x in ev],
        "Rosati form positive-definite?": pos_def,
        "Rosati form positive-SEMIdefinite?": pos_semidef,
        "=> a^2 < 4q (Hasse/Weil, strict)?": bool(det > 1e-9),
        "max ||alpha|-sqrt q| (0 <=> on line)": max_off,
        # RH for the curve = |alpha|=sqrt q = a^2<=4q = positive-SEMIdefinite (boundary a^2=4q is on-line):
        "SEMIdefiniteness <=> on the line?": pos_semidef == on_line,
    }


def edge_to_centre_chain(q=7):
    """THE EXECUTABLE CHAIN (the agenda's question, realized over F_q):
        EDGE number F.F'=q  --[Rosati reflection theta]-->  via POSITIVE-DEFINITENESS  --> CENTRE |alpha|=sqrt q.
    Run it for an on-line curve (RH holds) and an off-line planted set (RH broken) and confirm the
    Rosati form's positivity TRACKS the line exactly -- i.e. the positivity SEES the zeros."""
    s = float(mp.sqrt(q))
    out = []
    # on-line: a real elliptic curve a with a^2 < 4q  (e.g. a=1 over F_7: alpha = (1 +- i sqrt(27))/2)
    for label, a in [("on-line a=1 (a^2=1<28)", 1), ("on-line a=5 (25<28)", 5),
                     ("BOUNDARY a^2=4q (a=2sqrt7)", 2 * s),
                     ("off-line a=6 (36>28!)", 6), ("off-line a=7 (49>28!)", 7)]:
        # reconstruct eigenvalues from (a, q): alpha,beta roots of x^2 - a x + q
        disc = a * a - 4.0 * float(q)
        if disc < 0:
            r = cmath.sqrt(complex(disc))
            al = (a + r) / 2.0
            be = (a - r) / 2.0
        else:
            r = cmath.sqrt(complex(disc))
            al = (a + r) / 2.0
            be = (a - r) / 2.0
        res = rosati_trace_form(q, [al, be])
        on_line = abs(abs(al) - s) < 1e-6
        out.append({
            "case": label, "a": round(float(a), 4),
            "det M = 4q-a^2": round(res["det M = 4q - a^2"], 4),
            "Rosati pos-semidef (=> on line)": res["Rosati form positive-SEMIdefinite?"],
            "|alpha|": round(abs(al), 4), "sqrt q": round(s, 4),
            "on line?": on_line,
            # RH(curve) = |alpha|=sqrt q = a^2<=4q = pos-SEMIdef; tracks the line including the boundary
            "POSITIVITY TRACKS LINE?": res["Rosati form positive-SEMIdefinite?"] == on_line,
        })
    return out


# ----------------------------------------------------------------------------------------------------
# 4. THE Z-ANALOG AUDIT: is the Rosati positivity available over Z without assuming RH?
# ----------------------------------------------------------------------------------------------------

def z_analog_audit():
    """method.md step 2: with the chain executable, where does each LINK import to Z, and where is the
    one open implication?  This is the load-bearing honest audit.

    LINK (i) EDGE NUMBER F.F'=q  -->  Z-analog: the Petersson/Rankin-Selberg edge residue
        ||f||^2 = Res_{s=1} L(s, f x fbar) > 0.  STATUS: AVAILABLE & UNCONDITIONAL (Worker E, the
        L(1,sym^2) Siegel bound).  Both are "the norm-square at the edge".  [transfers]

    LINK (ii) REFLECTION theta = Rosati involution alpha->q/alpha-bar  -->  Z-analog: the functional
        equation s -> 1-s.  STATUS: AVAILABLE & UNCONDITIONAL (the FE is a theorem).  Fixed locus
        Re s = 1/2.  [transfers]  BUT NOTE: over F_q theta is an ALGEBRAIC involution on the
        endomorphism RING (it permutes actual correspondences); over Z, s->1-s is an involution on the
        SPECTRAL PARAMETER only -- there is no endomorphism ring of a surface for it to act on.  This
        is the first crack: the reflection exists on s but NOT (yet) on an algebra of correspondences.

    LINK (iii) ROSATI POSITIVITY Tr(phi phi') > 0  -->  THE LEVER.  Z-analog: positive-definiteness of
        the form < phi, phi > on the (hypothetical) algebra of arithmetic correspondences on S/Z.
        STATUS: THIS IS THE WALL.  Over F_q it is a THEOREM (Weil), PROVED FROM THE INTERSECTION
        THEORY OF THE EXISTING SURFACE C x C (the Hodge index).  Over Z:
          - there is NO surface S^2/Z, no algebra of correspondences End, no intersection theory --
            so the Rosati form cannot even be WRITTEN, let alone proved positive.
          - the ANALYTIC shadow (the edge ||f||^2 > 0) gives positivity of ONE diagonal entry
            (the <Id,Id> / norm at s=1), NOT the 2x2 det 4q-a^2 > 0 that needs the OFF-diagonal
            coupling Tr(F) = a -- the cross term between Id and F.  The cross term is the explicit
            formula / the primes; ||f||^2 alone does not supply it.

    SO THE ONE OPEN IMPLICATION, NAMED PRECISELY:
        the edge norm-square gives the DIAGONAL <Id,Id> at s=1; RH needs the FULL Rosati form
        (including the off-diagonal Frobenius-coupling Tr(F)) to be positive-definite at s=1/2.
        The reflection theta=FE is available; the EDGE diagonal positivity is available; the missing
        piece is THE OFF-DIAGONAL / CROSS-PLACE COUPLING that makes the 2x2 (not just 1x1) positive.

    THIS IS EXACTLY THE STANDING WALL (cross-place coupling W_inf >= sum_p W_p), now RE-DERIVED from
    the Rosati form: the wall is the OFF-DIAGONAL entry Tr(F) of the Rosati Gram, coupling Id (the
    edge norm) to F (the Frobenius/primes).  The edge norm-square supplies the diagonal; the line
    needs the whole matrix.  THE REFLECTION DOES NOT, BY ITSELF, TURN ONE DIAGONAL ENTRY INTO A
    POSITIVE 2x2 MATRIX -- THAT REQUIRES THE CROSS TERM, WHICH IS THE PRIMES."""
    return {
        "(i) edge number F.F'=q": {
            "Z-analog": "Petersson residue ||f||^2 = Res_{s=1} L(s,fxf) > 0 (the sym^2 edge norm)",
            "status": "AVAILABLE, UNCONDITIONAL (Siegel bound, Worker E) -- the s=1 diagonal <Id,Id>",
            "transfers?": "YES",
        },
        "(ii) reflection theta = Rosati involution": {
            "Z-analog": "the functional equation s -> 1-s, fixed locus Re s=1/2",
            "status": "AVAILABLE, UNCONDITIONAL -- but acts on the SPECTRAL PARAMETER, not on an "
                      "algebra of correspondences (no surface over Z for it to permute)",
            "transfers?": "YES on s; NO as an algebraic involution on End(S^2/Z)",
        },
        "(iii) ROSATI POSITIVITY Tr(phi phi') > 0  [THE LEVER]": {
            "Z-analog": "positive-definiteness of the Rosati Gram [[<Id,Id>, Tr F],[Tr F, <F,F>]] over Z",
            "status": "THE WALL. Over F_q it is the Hodge index on the EXISTING C x C; over Z neither "
                      "the surface, End, nor the intersection form exists. The edge ||f||^2 gives only "
                      "the DIAGONAL <Id,Id>; the det = 4q - a^2 > 0 needs the OFF-DIAGONAL Tr(F)=a "
                      "(the Frobenius/primes coupling).",
            "transfers?": "NO -- this is RH",
        },
        "THE ONE OPEN IMPLICATION (named)": (
            "the reflection theta=FE + the edge diagonal ||f||^2 are BOTH available; what is missing is "
            "the OFF-DIAGONAL cross term Tr(F) coupling the edge-norm Id to Frobenius F, which makes the "
            "2x2 Rosati Gram (not just its 1x1 diagonal) positive-definite. That off-diagonal IS the "
            "cross-place coupling W_inf >= sum_p W_p / the explicit formula / the primes. The reflection "
            "does NOT manufacture a positive matrix from one positive diagonal entry."),
        "VERDICT": (
            "The unified axiom does NOT close: a reflection under which 'the edge norm-square becomes the "
            "negative-definite primitive form at the centre' EXISTS and is a THEOREM over F_q (Rosati), "
            "and BOTH its Z-ingredients (edge ||f||^2, reflection FE) transfer -- but the THEOREM-CONTENT "
            "(Rosati positivity) is precisely the OFF-DIAGONAL cross term, = the standing wall. The "
            "relocation SHARPENS the wall to a named matrix entry: RH = positivity of the FULL Rosati "
            "Gram, whose diagonal is the edge norm (have it) and whose off-diagonal is the prime coupling "
            "(the wall). CIRCULAR -- but now the missing piece is a SINGLE off-diagonal entry, not a "
            "vague 'positivity'."),
    }


# ----------------------------------------------------------------------------------------------------
# 5. FALSIFIER on the unified-axiom candidate (load-bearing)
# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    """Score 'RH <= positivity of the Rosati Gram, edge-diagonal sourced by ||f||^2' on three axes."""
    chain = edge_to_centre_chain(q=7)
    tracks = all(r["POSITIVITY TRACKS LINE?"] for r in chain)
    return {
        "candidate": "RH <= the Rosati trace form [[||f||^2-analog, Tr F],[Tr F, <F,F>]] positive-definite",
        "Euler-borne?": ("YES -- the form is built on F = Frobenius/Hecke (Satake parameters) and the "
                         "edge ||f||^2 = sym^2 residue, neither of which DH (no Euler product) supplies. "
                         "Same DH-refusal as the sym^2 / signature candidates."),
        "sees-zeros?": (f"YES -- the Rosati form's positive-SEMIdefiniteness TRACKS the line exactly over "
                        f"F_q (det M = 4q - a^2 >= 0 <=> |alpha|=sqrt q; tracks-line for all 5 planted "
                        f"cases = {tracks}). The off-diagonal Tr(F)=a IS the eigenvalue location."),
        "independent?": ("NO -- over F_q the positivity is the Hodge index THEOREM on C x C; over Z it is "
                         "exactly RH (the diagonal ||f||^2 is unconditional, but the FULL 2x2 positivity "
                         "= a^2 < 4q analog = the off-diagonal cross-place coupling = the wall)."),
        "VERDICT": ("CIRCULAR (= Weil positivity over Z), SAME box as the signature / Weil-Li form. The "
                    "NEW, SHARPER content: the unified axiom's missing piece is now a SINGLE NAMED MATRIX "
                    "ENTRY -- the OFF-DIAGONAL Rosati coupling Tr(F) between the edge-norm (have it: "
                    "||f||^2) and Frobenius (the primes: the wall). The reflection theta=FE turns the "
                    "edge norm-square into the centre form ONLY IF that off-diagonal is supplied; the "
                    "reflection alone does NOT. This is the most precise statement yet of the edge->line "
                    "gap: RH = the off-diagonal entry of the Rosati Gram is in the positive-definite "
                    "range, i.e. |Tr F|^2 < <Id,Id><F,F> -- a Cauchy-Schwarz the primes must satisfy."),
    }


# ----------------------------------------------------------------------------------------------------

def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[1] EDGE NUMBER: the Rosati identity F.F' = q (unconditional; the function-field ||f||^2)\n")
    s = float(mp.sqrt(7))
    on = [s * cmath.exp(0.6j), s * cmath.exp(-0.6j)]   # on-line elliptic curve over F_7
    for r in rosati_edge_identity(7, on):
        adj = r["F'=q/alpha (adjoint)"]
        ff = r["alpha*(q/alpha) = F.F'"]
        print(f"    alpha={r['alpha']:.4f}  F'=q/alpha={adj:.4f}  "
              f"F.F'={ff:.4f}  ==q? {r['== q exactly?']}  "
              f"|alpha|={r['|alpha| (RH: =sqrt q)']:.4f}")
    print()

    print("=" * 100)
    print("[2] REFLECTION theta=Rosati: fixed locus is |alpha|=sqrt q = Re s = 1/2\n")
    for r in reflection_fixed_locus(7, on):
        th = r["theta(alpha)=q/alpha-bar"]
        d = r["|theta(alpha) - alpha| (0 <=> on line)"]
        print(f"    alpha={r['alpha']:.4f}  theta(alpha)={th:.4f}  "
              f"|theta-alpha|={d:.2e}  "
              f"on locus? {r['on fixed locus |alpha|=sqrt q?']}")
    print()

    print("=" * 100)
    print("[3] THE LEVER: Rosati trace form positive-definite <=> on the line (det M = 4q - a^2)\n")
    print("    THE CHAIN edge(F.F'=q) --reflection--> via POSITIVITY --> centre(|alpha|=sqrt q):\n")
    for r in edge_to_centre_chain(7):
        print(f"    {r['case']:32s} a={r['a']:7.3f}  detM={r['det M = 4q-a^2']:9.3f}  "
              f"pos-semidef={str(r['Rosati pos-semidef (=> on line)']):5s}  on-line={str(r['on line?']):5s}  "
              f"TRACKS={r['POSITIVITY TRACKS LINE?']}")
    print()

    print("=" * 100)
    print("[4] Z-ANALOG AUDIT: where each link transfers, and the ONE open implication\n")
    d = z_analog_audit()
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"    {k}:")
            for kk, vv in v.items():
                print(f"        {kk}: {vv}")
        else:
            print(f"    {k}:\n        {v}")
        print()

    print("=" * 100)
    print("[5] FALSIFIER VERDICT on the unified-axiom (Rosati Gram) candidate\n")
    for k, v in falsifier_verdict().items():
        print(f"    {k}:\n        {v}\n")


if __name__ == "__main__":
    summary()
