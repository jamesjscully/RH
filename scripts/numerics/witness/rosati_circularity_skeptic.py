"""rosati_circularity_skeptic.py -- the ruthless-skeptic decidable test.

THE QUESTION (RF-circularity-skeptic mandate):
  The count/radius meditation says psi_infinity should be a CANONICAL FINITE-DEGREE SELF-MAP F of a
  polarized archimedean abelian variety, with radius |alpha|=sqrt(deg) FORCED by Rosati positivity
  (a free theorem over C, NOT RH). The Rosati positivity Tr(phi phi^dagger)>0 and F.F^dagger=[deg]
  are tautological. So IF the radius is forced, ALL the RH content must hide in the SPECTRAL
  REALIZATION: putting the zeta zeros into a polarized AV as eigenvalues of a canonical endomorphism.

  DECIDABLE: does an OFF-LINE eigenvalue OBSTRUCT the EXISTENCE of the polarized-AV-with-endomorphism
  realization?
    - If YES  -> genuine forcing: no AV with off-line F exists -> radius FORCED (RH because no AV).
    - If NO   -> the realization is possible for off-line F too -> the radius datum was ASSUMED
                 (RH smuggled into the *choice* of which F is "the canonical/geometric Frobenius"),
                 i.e. CIRCULAR.

We test three candidate obstructions named in the mandate:
  (a) FE/pairing: the AV exists only if eigenvalues pair up alpha <-> q/alpha. (claimed free)
  (b) ENDOMORPHISM/integrality: F integral on the lattice only if eigenvalues are algebraic of the
      right type (off-line zero -> non-endomorphism?).
  (c) POSITIVITY: the polarization is positive (a genuine AV, not a fake torus) only if eigenvalues
      are on the line.

The decisive computation: build a 2x2 'Frobenius' F with OFF-LINE eigenvalues and ASK, by linear
algebra, whether there exists a polarization (a real alternating form E whose associated Hermitian
H(x,y)=E(ix,y)+iE(x,y) is POSITIVE-DEFINITE) with respect to which F admits a Rosati adjoint
F^dagger = E^{-1} F^T E satisfying F.F^dagger = q.Id. Compute, do NOT assume.

Tags: [BUILT] [computed].
"""
from __future__ import annotations

import itertools

import numpy as np


# ----------------------------------------------------------------------------------------------------
# The setup: a complex torus C/L with a real endomorphism F. We work in the 2g=2 real model (g=1).
# A polarization is a real alternating form E on R^2 with:
#   (P1) E(Jx,Jy)=E(x,y)        (J-invariance: compatible with the complex structure J)
#   (P2) H(x,y):=E(Jx,y)+iE(x,y) is a POSITIVE-DEFINITE Hermitian form  <=>  E(Jx,x)>0 for all x!=0.
#   (P3) E integral on the lattice L (Riemann relation; we relax to "E real alternating" for the
#        EXISTENCE-over-R question, then comment on integrality = candidate (b)).
# The Rosati adjoint of phi w.r.t. E is phi^dagger = E^{-1} phi^T E (the E-adjoint, up to sign conv.).
# Rosati POSITIVITY (the free theorem): Tr(phi phi^dagger) > 0 for phi != 0, PROVIDED H is pos-def.
# ----------------------------------------------------------------------------------------------------

def companion(a, q):
    """F = companion matrix of x^2 - a x + q (a 'Frobenius' with char poly x^2-ax+q).
    Eigenvalues alpha,beta = (a +- sqrt(a^2-4q))/2, product q, sum a.  |alpha|=sqrt q  iff  a^2<=4q."""
    return np.array([[0.0, -float(q)], [1.0, float(a)]])


def eigs(F):
    return np.linalg.eigvals(F)


# ----------------------------------------------------------------------------------------------------
# (c) THE POSITIVITY OBSTRUCTION -- the decisive test.
# Given F (2x2 real), we ask: does there exist a complex structure J (J^2=-I) commuting with F,
# and a real alternating E with E(J.,.) pos-def (a polarization) such that F^dagger_E = E^{-1}F^T E
# satisfies F F^dagger = q I ?   We DERIVE F^dagger from the Rosati condition and check positivity.
# ----------------------------------------------------------------------------------------------------

def rosati_adjoint(F, E):
    """phi^dagger = E^{-1} phi^T E (E-adjoint)."""
    return np.linalg.inv(E) @ F.T @ E


def hermitian_from_polarization(E, J):
    """H(x,y) = E(Jx,y) + i E(x,y).  Matrix: H = (E J)^T ... we build the real symmetric part S=E J
    (must be symmetric & pos-def for a polarization) and report its eigenvalues.  H pos-def <=> S pos-def."""
    S = E @ J            # E(Jx,y) as bilinear matrix x^T (E J)^? -- careful with convention below
    return S


def standard_J():
    """The standard complex structure J on R^2 = C: multiplication by i.  J = [[0,-1],[1,0]]."""
    return np.array([[0.0, -1.0], [1.0, 0.0]])


def test_polarization_exists(a, q, verbose=False):
    """THE DECISIVE COMPUTATION.

    A complex structure on R^2=C^1 is any J with J^2=-I.  For F to be holomorphic (an endomorphism of
    the COMPLEX torus, i.e. a genuine AV endomorphism, candidate (b)), F must COMMUTE with J: FJ=JF.

    For a 2x2 real F with NON-REAL eigenvalues alpha=re^{i t}: F = r R(t) (scaling*rotation) in a
    suitable basis, and F commutes with a UNIQUE J (up to sign): the rotation part's J.  We construct
    it.  Then the polarization is E = lambda * (the area form) and H(x,x)=E(Jx,x); positivity of H is
    a SINGLE sign.  We then impose the Rosati identity F F^dagger = q I and read off whether it forces
    |alpha|=sqrt q OR holds for off-line too.
    """
    F = companion(a, q)
    ev = eigs(F)
    # need non-real eigenvalues for a complex structure to commute with F (the interesting AV case)
    nonreal = abs(ev[0].imag) > 1e-9

    out = {
        "a": a, "q": q, "eigenvalues": [complex(round(e.real, 6), round(e.imag, 6)) for e in ev],
        "|alpha|": float(abs(ev[0])), "sqrt q": float(np.sqrt(q)),
        "on_line(|alpha|=sqrt q)": bool(abs(abs(ev[0]) - np.sqrt(q)) < 1e-7),
        "nonreal_eigs": bool(nonreal),
    }
    if not nonreal:
        out["verdict"] = "real eigenvalues: F preserves no complex structure -> not the AV case (skip)"
        return out

    # --- build the J commuting with F.  Diagonalize F = P D P^{-1}, D=diag(alpha, alpha-bar).
    # The complex structure commuting with F: in the real form F = r*Rot(theta), J = Rot(+-pi/2).
    # Concretely: write F = sym + antisym ... simplest: F commutes with J := (F - (TrF/2) I)/|imag part|.
    half_tr = np.trace(F) / 2.0
    A = F - half_tr * np.eye(2)          # traceless part; A^2 = (det-... ) -- A^2 = (a^2/4 - q) I < 0
    A2 = A @ A
    # A^2 = ((a^2 - 4q)/4) I = -(disc) I, with disc>0 for nonreal eigs
    c2 = -A2[0, 0]                        # = q - a^2/4 > 0
    J = A / np.sqrt(c2)                   # J^2 = A^2 / c2 = -I.  commutes with F by construction.
    out["J^2 = -I check"] = float(np.linalg.norm(J @ J + np.eye(2)))
    out["[F,J] commutator norm"] = float(np.linalg.norm(F @ J - J @ F))

    # --- the polarization E: the unique-up-to-scale real alternating form on R^2 is
    #     E = lambda * [[0,1],[-1,0]] (the area form).  H(x,x) = E(Jx,x).  Positivity = sign of lambda.
    Omega = np.array([[0.0, 1.0], [-1.0, 0.0]])
    # choose lambda sign so that H is POSITIVE-definite (a polarization ALWAYS exists on a 1-dim
    # complex torus -- every elliptic curve is an abelian variety!).  This is the key free fact.
    for lam in (1.0, -1.0):
        E = lam * Omega
        # H(x,y) = E(Jx,y); as a symmetric matrix S with x^T S y, S = -J^T E (using E(Jx,y)=(Jx)^T E^? )
        # bilinear form B(x,y)=E(Jx,y) has matrix M with x^T M y = (Jx)^T E y = x^T (J^T E) y => M=J^T E
        S = J.T @ E
        Ssym = 0.5 * (S + S.T)
        evS = np.linalg.eigvalsh(Ssym)
        if (evS > 1e-9).all():
            out["polarization lambda (H pos-def)"] = lam
            out["H eigenvalues (pos-def)"] = [float(x) for x in evS]
            E_pol = E
            break
    else:
        out["polarization lambda (H pos-def)"] = None
        out["verdict"] = "NO positive polarization found (unexpected for 1-dim torus)"
        return out

    # --- Rosati adjoint and the identity F F^dagger = q I
    Fdag = rosati_adjoint(F, E_pol)
    FFdag = F @ Fdag
    out["F^dagger (Rosati adjoint)"] = Fdag.round(6).tolist()
    out["F.F^dagger"] = FFdag.round(6).tolist()
    # is F F^dagger a scalar?  what scalar?
    scal = FFdag[0, 0]
    is_scalar = np.linalg.norm(FFdag - scal * np.eye(2)) < 1e-7
    out["F.F^dagger is scalar?"] = bool(is_scalar)
    out["that scalar"] = float(scal.real) if is_scalar else None
    out["scalar == q?"] = bool(is_scalar and abs(scal.real - q) < 1e-7)
    out["scalar == |alpha|^2?"] = bool(is_scalar and abs(scal.real - abs(ev[0]) ** 2) < 1e-7)

    # --- Rosati POSITIVITY of the trace form Tr(phi phi^dagger) on End -- the "free theorem".
    # test on a basis {I, F} of the real endomorphism algebra (R[F]).
    basis = [np.eye(2), F]
    Gram = np.zeros((2, 2))
    for i, p in enumerate(basis):
        for j, r in enumerate(basis):
            pd = rosati_adjoint(p, E_pol)
            Gram[i, j] = np.trace(p @ rosati_adjoint(r, E_pol)).real
    evG = np.linalg.eigvalsh(0.5 * (Gram + Gram.T))
    out["Rosati Gram on {I,F}"] = Gram.round(6).tolist()
    out["Rosati Gram eigenvalues"] = [float(x) for x in evG]
    out["Rosati form positive-definite?"] = bool((evG > 1e-9).all())

    return out


def run_table():
    """Run the decisive test for ON-LINE and OFF-LINE 'Frobenius' eigenvalues at q=7."""
    q = 7
    s = np.sqrt(q)
    cases = [
        ("ON-LINE a=1 (a^2=1 < 28)", 1.0),
        ("ON-LINE a=4 (16 < 28)", 4.0),
        ("BOUNDARY a^2=4q", 2 * s),
        ("OFF-LINE a=6 (36 > 28!)", 6.0),
        ("OFF-LINE a=0,|alpha|!=sqrt q? (a=0 gives |alpha|=sqrt q!)", 0.0),
    ]
    results = []
    for label, a in cases:
        r = test_polarization_exists(a, q)
        r["label"] = label
        results.append(r)
    return results


# ----------------------------------------------------------------------------------------------------
# THE OFF-LINE-OFF-CIRCLE test done RIGHT: real eigenvalues OFF the circle.
# a=6,q=7: eigenvalues are real (3+-sqrt2), |alpha| differ, NOT a conjugate pair on a circle.
# To get a genuine OFF-LINE COMPLEX pair, plant eigenvalues {r e^{it}, r e^{-it}} with r != sqrt q
# directly (this is the M4r 'redistribution' / an off-line zero of zeta: Re(rho) != 1/2).
# ----------------------------------------------------------------------------------------------------

def planted_offline(r, t, q):
    """Plant a conjugate eigenvalue pair alpha = r e^{it}, alpha-bar; build the real 2x2 F with that
    char poly x^2 - (2 r cos t) x + r^2.  NOTE det F = r^2, so this F has 'degree' r^2, NOT q, unless
    r=sqrt q.  THIS IS THE CRUX: an off-circle conjugate pair is a perfectly good real matrix and a
    perfectly good complex-torus endomorphism -- but its DEGREE (det) is r^2 != q.  Does it admit a
    positive Rosati polarization?  YES (every 1-dim torus does).  Does F F^dagger = q?  NO -- it = r^2.
    The 'q' is NOT intrinsic to F; it is an EXTERNAL datum (which circle we declare critical)."""
    a = 2 * r * np.cos(t)
    detF = r * r
    F = np.array([[0.0, -detF], [1.0, a]])
    ev = np.linalg.eigvals(F)
    # build commuting J and the polarization exactly as above
    half_tr = np.trace(F) / 2.0
    A = F - half_tr * np.eye(2)
    c2 = -(A @ A)[0, 0]
    J = A / np.sqrt(c2)
    Omega = np.array([[0.0, 1.0], [-1.0, 0.0]])
    E_pol = None
    for lam in (1.0, -1.0):
        E = lam * Omega
        S = 0.5 * ((J.T @ E) + (J.T @ E).T)
        if (np.linalg.eigvalsh(S) > 1e-9).all():
            E_pol = E
            break
    Fdag = np.linalg.inv(E_pol) @ F.T @ E_pol
    FFdag = F @ Fdag
    scal = FFdag[0, 0].real
    # Rosati form on {I,F}
    basis = [np.eye(2), F]
    Gram = np.array([[np.trace(p @ (np.linalg.inv(E_pol) @ r2.T @ E_pol)).real
                      for r2 in basis] for p in basis])
    evG = np.linalg.eigvalsh(0.5 * (Gram + Gram.T))
    return {
        "planted alpha": complex(round(ev[0].real, 6), round(ev[0].imag, 6)),
        "|alpha| = r": float(r), "sqrt q": float(np.sqrt(q)),
        "off-circle?": bool(abs(r - np.sqrt(q)) > 1e-7),
        "polarization H pos-def?": E_pol is not None,
        "F.F^dagger scalar": float(scal),
        "== r^2 (det F)?": bool(abs(scal - r * r) < 1e-7),
        "== q (the critical radius)?": bool(abs(scal - q) < 1e-7),
        "Rosati form pos-def?": bool((evG > 1e-9).all()),
    }


def run_offcircle_table():
    q = 7.0
    s = np.sqrt(q)
    out = []
    for label, r in [("ON-CIRCLE r=sqrt q", s),
                     ("OFF-CIRCLE r=1.3 sqrt q (Re rho>1/2)", 1.3 * s),
                     ("OFF-CIRCLE r=0.7 sqrt q (Re rho<1/2)", 0.7 * s),
                     ("OFF-CIRCLE r=2.0 sqrt q", 2.0 * s)]:
        d = planted_offline(r, 0.6, q)
        d["label"] = label
        out.append(d)
    return out


# ----------------------------------------------------------------------------------------------------
# (b) THE INTEGRALITY / ENDOMORPHISM obstruction -- does off-line break F being an endomorphism?
# An endomorphism of an AV with CM by an imaginary quadratic order: F integral iff alpha is an
# algebraic integer in that order. For the 1-dim torus C/(Z+Z tau), End contains alpha iff
# alpha*(Z+Z tau) subset (Z+Z tau).  We test: is an off-circle conjugate pair {r e^{it}} ever an
# algebraic integer giving an endomorphism, with r != sqrt q?
# ----------------------------------------------------------------------------------------------------

def integrality_comment():
    return (
        "Integrality test (candidate b): F is an endomorphism of C/L iff its eigenvalue alpha is an "
        "algebraic integer with alpha*L subset L. For ANY algebraic integer alpha generating an "
        "imaginary quadratic field K, the torus C/O_K (O_K the ring of integers) has alpha as an "
        "endomorphism, with det(F on H_1) = N(alpha) = alpha*alpha-bar = |alpha|^2. There is NO "
        "constraint |alpha|^2 = q here: q is whatever N(alpha) happens to be. Example: alpha=1+i (in "
        "Z[i]) is an endomorphism of C/Z[i] with N(alpha)=2, |alpha|=sqrt 2. alpha=2+i: N=5, "
        "|alpha|=sqrt5. alpha=1+2i: N=5. These are all 'Frobenius-like' integral endomorphisms with "
        "|alpha|=sqrt(N(alpha)) -- i.e. they are AUTOMATICALLY on the circle of radius sqrt(their own "
        "degree). The circle |alpha|=sqrt(deg) is FORCED for an endomorphism *relative to ITS OWN "
        "degree N(alpha)*, but deg is N(alpha), read OFF alpha, NOT an independently-given q. To get an "
        "OFF-circle endomorphism (|alpha|^2 != deg) you would need alpha integral with |alpha|^2 != "
        "N(alpha) -- IMPOSSIBLE for an imaginary quadratic integer (N(alpha)=|alpha|^2 by definition of "
        "the complex absolute value = the field norm). SO: integrality FORCES |alpha|=sqrt(deg), but "
        "'deg' is alpha's OWN norm, a tautology -- it does NOT force |alpha|=sqrt(q) for an EXTERNALLY "
        "PRESCRIBED q. The radius is forced relative to the WRONG (self-referential) degree.")


def summary():
    np.set_printoptions(precision=6, suppress=True)
    print(__doc__)
    print("=" * 100)
    print("[A] companion-Frobenius x^2-ax+q at q=7: does a positive Rosati polarization exist,")
    print("    and does F.F^dagger = q HOLD, on-line vs off-line?\n")
    for r in run_table():
        print(f"  {r['label']}")
        print(f"     eigs={r['eigenvalues']}  |alpha|={r['|alpha|']:.4f}  on_line={r['on_line(|alpha|=sqrt q)']}")
        if r.get("polarization lambda (H pos-def)") is not None:
            print(f"     pos-def polarization EXISTS (lambda={r['polarization lambda (H pos-def)']});"
                  f"  F.F^dagger scalar?={r.get('F.F^dagger is scalar?')} = {r.get('that scalar')}"
                  f"  ==q?{r.get('scalar == q?')}  ==|alpha|^2?{r.get('scalar == |alpha|^2?')}")
            print(f"     Rosati form pos-def? {r.get('Rosati form positive-definite?')}")
        else:
            print(f"     {r.get('verdict')}")
        print()

    print("=" * 100)
    print("[B] PLANTED off-CIRCLE complex conjugate pair (a genuine off-line zeta zero), q=7 fixed:")
    print("    does it admit a positive Rosati polarization, and what is F.F^dagger?\n")
    for r in run_offcircle_table():
        print(f"  {r['label']}")
        print(f"     |alpha|={r['|alpha| = r']:.4f}  sqrt q={r['sqrt q']:.4f}  off-circle={r['off-circle?']}")
        print(f"     polarization H pos-def? {r['polarization H pos-def?']}   "
              f"Rosati form pos-def? {r['Rosati form pos-def?']}")
        print(f"     F.F^dagger = {r['F.F^dagger scalar']:.4f}   == r^2(=detF)? {r['== r^2 (det F)?']}   "
              f"== q? {r['== q (the critical radius)?']}")
        print()

    print("=" * 100)
    print("[C] INTEGRALITY / endomorphism obstruction (candidate b):\n")
    print("   " + integrality_comment().replace(". ", ".\n   "))


if __name__ == "__main__":
    summary()
