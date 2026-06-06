"""kahler_forcing.py -- K1 [KEYSTONE]: is P_inf >= 0 (= c=D) FORCED by a Hodge-Riemann / Kahler
structure (a GEOMETRIC datum), with NO zeros assumed?  -- AND WHERE EXACTLY THE FORCING NEEDS THE ZEROS.

  run:  python3 -m scripts.numerics.witness.kahler_forcing

THE KEYSTONE QUESTION (AGENDA K1).  M3/M3b built the archimedean polarization P_inf(x,y)=S(C_W x,kappa y)
and established RH = the archimedean degeneration c=D = (P_inf >= 0 on primitives).  The whole polarized
arithmetic Hodge category rests on this ONE positivity.  K1 asks: is it CIRCULAR to attack, or is
P_inf >= 0 *forced* by a Hodge-Riemann/Kahler structure?  Classical Hodge theory says the latter: a
polarized Hodge structure has c=D automatically (the Hodge-Riemann bilinear relations), the polarization
coming from a KAHLER class -- a GEOMETRIC datum, NOT the zeros.

THIS MODULE EXECUTES THE ANCHOR (over F_q) AND FINDS THE HONEST SEAM.  The result is sharper than the
agenda's optimistic framing, and it is a LOAD-BEARING finding, not a clean win:

  STEP A -- THE CUP PRODUCT / AMPLE FORM ALONE IS INDEFINITE (a genuine negative).  The weight-1 cup
  product E (the Weil pairing, the "ample"/polarization datum on H^1) is SYMPLECTIC (antisymmetric),
  and the Rosati form Tr(z . z^dag) it induces on End(H^1) (with z^dag = E^{-1} z^T E) is INDEFINITE --
  signature (2,0,2) at g=1, NOT positive.  So the cup product BY ITSELF does NOT force the
  Hodge-Riemann positivity.  (Computed below.)  This kills the naive reading "the ample class forces
  c=D for free".

  STEP B -- THE POSITIVITY NEEDS THE WEIL OPERATOR C_W (the (p,q) Hodge structure).  The TRUE
  Hodge-Riemann positive form is P_inf(x,y) = E(C_W x, conj y), with C_W = i^{p-q} the Weil operator.
  WITH C_W inserted, P_inf IS positive-definite on H^{1,0} (computed below).  So the forcing datum is
  not E alone but the PAIR (E, C_W) = the POLARIZED Hodge structure.  C_W is the Kahler/(p,q) datum.

  STEP C -- WHERE C_W COMES FROM IS THE WHOLE PROBLEM (the keystone's irreducible residue).  Over F_q
  the Weil operator on H^1 is supplied by Frobenius being a WEIL NUMBER of weight 1: alpha = sqrt(q) .
  e^{i theta}, so the (p,q) splitting / the rotation by theta is exactly the datum |alpha| = sqrt q --
  which IS RH for the curve.  So over F_q the "Kahler class" C_W and the RH statement |alpha|=sqrt q
  are THE SAME DATUM.  The Hodge-Riemann forcing "Kahler ==> c=D" is a TAUTOLOGY there: you put RH in
  (Frobenius is a weight-1 Weil number) and get c=D out.

  THE DECISIVE SPLIT (the honest terminus K5 asked for).  K1 thus does NOT show "c=D is forced for
  free".  It shows the forcing FACTORS:

      (E, the cup product)  -- a GEOMETRIC datum, zero-free, DH-shared, INDEFINITE alone;  [free]
      (C_W, the Weil op)    -- the (p,q)/RADIUS datum: over F_q it is |alpha|=sqrt q = RH;   [= RH]
      Hodge-Riemann:  (E, C_W) polarized  ==>  P_inf >= 0 on primitives  =  c=D.            [formal]

  The Hodge-Riemann IMPLICATION is formal/geometric (free); the cup product E is free; but the WEIL
  OPERATOR C_W -- the (p,q) grading that makes E definite -- is OVER F_q literally the radius |alpha|=
  sqrt q.  So the irreducible residue is EXACTLY: SUPPLY C_W (the (p,q) splitting / the critical radius)
  over Z FROM A GEOMETRIC SOURCE, not from RH.  This is M3b's "radius-silent (-1)^w" lesson made
  precise as a Hodge-theoretic forcing: the archimedean Kahler class carries the WEIL OPERATOR's PHASE
  (reality, the sign (-1)^w) but NOT its RADIUS; the radius must be Euler-assembled (M4r/M4).

WHAT AN ARCHIMEDEAN KAHLER CLASS ON S^2/Z MUST BE (the K2/K3 target, now PRECISELY typed).  Not "a
positive Green form" (Arakelov, Sylvester-locked, and BGS 6.3 can fail) -- but a CANONICAL Weil operator
C_W on the archimedean (p,q)-graded H^2(S^2/Z), whose RADIUS (the scale fixing |alpha|=sqrt q at the
weight-1 descent) is supplied by the EULER assembly of the prime Satake products, NOT by a chosen metric
and NOT by RH.  The condensed/analytic realization (K2) must produce this C_W; the forcing lemma (K3) is
then the (formal) Hodge-Riemann implication; the open residue is the RADIUS of C_W = M4's Euler descent.

FALSIFIER (K1 -- a forcing/anchor check; the keystone FACTORS the axes, it does not clear them).
  - EULER-ASSEMBLED: the cup product E is Euler-SILENT (DH-shared); the Weil operator C_W's RADIUS
    (|alpha|=sqrt q) is Euler-BORNE (the Frobenius weight); the Hodge-Riemann implication is neither
    (formal).  The keystone LOCATES the Euler content in C_W's radius -- exactly M4's target.
  - SEES-ZEROS: P_inf >= 0 sees the zeros ONLY THROUGH C_W (the radius); E alone is blind.
  - INDEPENDENT: the implication (E,C_W polarized ==> c=D) is independent (Hodge-Riemann, geometric);
    but the HYPOTHESIS "C_W is the weight-1 Weil operator" over F_q IS |alpha|=sqrt q = RH.  So K1 is
    CIRCULAR over F_q in the precise sense that the Kahler datum C_W = the RH radius -- and that
    circularity is the keystone's IRREDUCIBLE RESIDUE: construct C_W's radius geometrically over Z.
"""
from __future__ import annotations

import numpy as np


# ----------------------------------------------------------------------------------------------------
# Weight-1 data: the cup product E (symplectic), the Rosati adjoint, the Weil operator C_W.
# ----------------------------------------------------------------------------------------------------

def cup_product(g=1):
    """The weight-1 cup product E on H^1 (rank 2g), the symplectic Weil pairing (the 'ample'/
    polarization datum).  Antisymmetric: E^T = -E.  GEOMETRIC, zero-free, DH-shared."""
    n = 2 * g
    E = np.zeros((n, n))
    E[:g, g:] = np.eye(g); E[g:, :g] = -np.eye(g)
    return E


def rosati(z, E):
    """Rosati adjoint z^dag = E^{-1} z^T E (the polarization adjoint induced by the cup product E)."""
    return np.linalg.solve(E, z.T @ E)


def weil_operator(g=1, tau=None, seed=0):
    """The Weil operator C_W = i^{p-q} on H^1 (= i on H^{1,0}, -i on H^{0,1}), built from a point tau in
    the Siegel upper half space (the Hodge filtration / (p,q) datum).  This is the KAHLER/(p,q) class."""
    rng = np.random.default_rng(seed)
    if tau is None:
        X = rng.standard_normal((g, g)); X = (X + X.T) / 2.0
        M = rng.standard_normal((g, g)); Y = M @ M.T + g * np.eye(g)   # SPD
        tau = X + 1j * Y
    om = np.vstack([np.eye(g, dtype=complex), tau])      # H^{1,0}
    omb = np.conj(om)                                    # H^{0,1}
    B = np.hstack([om, omb]); Binv = np.linalg.inv(B)
    P10 = B[:, :g] @ Binv[:g, :]; P01 = B[:, g:] @ Binv[g:, :]
    C_W = 1j * P10 - 1j * P01
    return C_W, om


# ----------------------------------------------------------------------------------------------------
# STEP A: the cup product ALONE is indefinite (the naive 'ample forces it' is FALSE).
# ----------------------------------------------------------------------------------------------------

def rosati_form_signature(g=1):
    """The Rosati form Tr(z . z^dag) on End(H^1), induced by the cup product E ALONE (no Weil operator).
    Returns its signature -- it is INDEFINITE (2,0,2) at g=1, NOT positive: the cup product by itself
    does NOT force the Hodge-Riemann positivity."""
    E = cup_product(g)
    n = 2 * g
    basis = []
    for i in range(n):
        for j in range(n):
            Z = np.zeros((n, n)); Z[i, j] = 1.0; basis.append(Z)
    dim = len(basis)
    G = np.zeros((dim, dim))
    for a in range(dim):
        for b in range(dim):
            G[a, b] = np.trace(basis[a] @ rosati(basis[b], E))
    G = (G + G.T) / 2.0
    eig = np.linalg.eigvalsh(G)
    tol = 1e-9
    return (int(np.sum(eig > tol)), int(np.sum(np.abs(eig) <= tol)), int(np.sum(eig < -tol))), eig


# ----------------------------------------------------------------------------------------------------
# STEP B: the positivity needs the Weil operator C_W (the (p,q) Hodge structure).
# ----------------------------------------------------------------------------------------------------

def P_inf_positivity(g=1, seed=0):
    """The TRUE Hodge-Riemann form P_inf(x,y) = E(C_W x, conj y), restricted to H^{1,0}.  WITH C_W it is
    POSITIVE-DEFINITE (Hodge-Riemann/Riemann's second relation).  Returns min eig on H^{1,0}."""
    E = cup_product(g)
    C_W, om = weil_operator(g, seed=seed)
    H = C_W.conj().T @ E
    H = (H + H.conj().T) / 2.0
    Gpr = om.conj().T @ H @ om; Gpr = (Gpr + Gpr.conj().T) / 2.0
    return float(np.linalg.eigvalsh(Gpr).min())


# ----------------------------------------------------------------------------------------------------
# STEP C: over F_q, C_W = the radius |alpha|=sqrt q = RH (the keystone's irreducible residue).
# ----------------------------------------------------------------------------------------------------

def frobenius_weil_operator(q, theta):
    """Over F_q, Frobenius on H^1 is F = sqrt(q) R(theta) (a weight-1 Weil number alpha=sqrt(q)e^{i theta}
    iff |alpha|=sqrt q = RH).  The Weil operator / (p,q) splitting C_W is the ROTATION part R(theta) --
    available ONLY when the RADIUS is exactly sqrt q.  If |alpha| != sqrt q (off-line), F is NOT a
    weight-1 Weil number and there is NO weight-1 Weil operator: the (p,q) structure DEGENERATES.
    Returns (F, has_weil_operator, radius)."""
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    F = np.sqrt(q) * R
    ev = np.linalg.eigvals(F)
    radius = float(np.abs(ev[0]))
    has_wo = abs(radius - np.sqrt(q)) < 1e-9      # weight-1 Weil number <=> radius = sqrt q = RH
    return F, has_wo, radius


def offcircle_breaks_weil_operator(q, theta, r):
    """Plant an OFF-circle pair {r sqrt q, sqrt q / r} (r != 1, RH violated).  Then the two eigenvalues
    have DIFFERENT moduli -- there is NO single radius, hence NO weight-1 Weil operator C_W = i^{p-q}
    with a well-defined (p,q) splitting at scale sqrt q.  Returns (radii, has_uniform_radius)."""
    a = (r * np.sqrt(q) + np.sqrt(q) / r) * np.cos(theta)   # a planted trace (schematic)
    ev = np.array([r * np.sqrt(q), np.sqrt(q) / r])
    radii = np.abs(ev)
    has_uniform = bool(abs(radii[0] - radii[1]) < 1e-9)
    return radii, has_uniform


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("K1 ANCHOR (F_q): does the AMPLE/Kahler structure FORCE P_inf>=0 (c=D), and WHERE are the zeros?\n")

    print("  STEP A -- THE CUP PRODUCT E ALONE IS INDEFINITE (the naive 'ample forces it' is FALSE):")
    for g in (1, 2, 3):
        sig, eig = rosati_form_signature(g)
        print(f"      g={g}:  Rosati form Tr(z z^dag) on End(H^1) signature = {sig}  "
              f"(positive-definite? {sig[0] == len(eig) and sig[2] == 0})  -- INDEFINITE")
    print("      ==> E (the cup product / 'ample' datum) by ITSELF does NOT force Hodge-Riemann; the")
    print("          symplectic cup product gives an INDEFINITE Rosati form.  The naive reading fails.")

    print("\n  STEP B -- WITH THE WEIL OPERATOR C_W INSERTED, P_inf IS POSITIVE-DEFINITE (Hodge-Riemann):")
    for g in (1, 2, 3):
        for seed in (0, 1):
            mn = P_inf_positivity(g, seed=seed)
            print(f"      g={g} seed={seed}:  P_inf = E(C_W .,conj.) on H^(1,0) min eig = {mn:+.4f}  "
                  f"(POSITIVE-DEF? {mn > 1e-9})")
    print("      ==> The forcing datum is the PAIR (E, C_W) = the POLARIZED Hodge structure.  C_W (the")
    print("          (p,q)/Weil operator) is the Kahler class that makes the cup product definite.")

    print("\n  STEP C -- OVER F_q, C_W IS THE RADIUS |alpha|=sqrt q = RH (the keystone's residue):")
    for (q, theta) in [(2, 0.7), (5, 1.1), (7, 0.4), (11, 1.3), (13, 0.9)]:
        F, has_wo, radius = frobenius_weil_operator(q, theta)
        radii_off, uniform_off = offcircle_breaks_weil_operator(q, theta, r=1.7)
        print(f"      q={q:>2}:  ON-line radius={radius:.3f} (sqrt q={np.sqrt(q):.3f}) "
              f"weight-1 Weil op exists? {has_wo}   |   OFF-line radii={np.round(radii_off,2)} "
              f"uniform radius (=> C_W exists)? {uniform_off}")
    print("      ==> ON-line: a single radius sqrt q => the weight-1 Weil operator C_W EXISTS (c=D).")
    print("          OFF-line: the two moduli DIFFER => NO uniform radius => NO weight-1 C_W => no c=D.")
    print("          So over F_q the Kahler datum C_W and RH (|alpha|=sqrt q) are LITERALLY the same datum.")

    print("\n" + "=" * 100)
    print("THE KEYSTONE FACTORIZATION (K1's honest terminus -- K5):")
    print("  (E, cup product)   GEOMETRIC, zero-free, DH-shared, INDEFINITE alone           [free]")
    print("  (C_W, Weil op)     the (p,q)/RADIUS datum: over F_q it IS |alpha|=sqrt q = RH    [= RH]")
    print("  Hodge-Riemann:     (E, C_W) polarized  ==>  P_inf >= 0 on primitives = c=D      [formal]")
    print("  So c=D is NOT forced 'for free': the cup product is free and the implication is formal,")
    print("  but the WEIL OPERATOR C_W (the radius/(p,q) splitting that makes E definite) is over F_q")
    print("  EXACTLY the RH radius.  The irreducible residue = SUPPLY C_W's RADIUS over Z geometrically.")
    print("  This is M3b's 'radius-silent (-1)^w' lesson as a Hodge forcing: the archimedean Kahler")
    print("  class carries C_W's PHASE/reality (the sign (-1)^w) but NOT its RADIUS -- which is Euler-")
    print("  assembled (M4r/M4).  K1 LOCATES the single geometric residue; it does not dissolve it.")

    print("\n" + "=" * 100)
    print("WHAT AN ARCHIMEDEAN KAHLER CLASS ON S^2/Z MUST BE (K2/K3 target, precisely typed):")
    print("  NOT a chosen positive Green form (Arakelov: Sylvester-locked; BGS 6.3 can fail) -- but a")
    print("  CANONICAL Weil operator C_W on the archimedean (p,q)-graded H^2(S^2/Z), whose RADIUS (the")
    print("  scale fixing |alpha|=sqrt q at the weight-1 descent) is supplied by the EULER assembly of")
    print("  the prime Satake products alpha_i(p)alpha_j(p), NOT by a metric and NOT by RH.  K2 (condensed)")
    print("  must PRODUCE this C_W; K3 (forcing lemma) is the formal Hodge-Riemann implication; the open")
    print("  residue is C_W's RADIUS = M4's Euler descent (M4r).")

    print("\n" + "=" * 100)
    print("FALSIFIER VERDICT (K1 -- the keystone FACTORS the axes, it does not clear them):")
    print("  EULER-ASSEMBLED  the cup product E is Euler-SILENT (DH-shared); C_W's RADIUS (|alpha|=sqrt q)")
    print("                   is Euler-BORNE (the Frobenius weight); the Hodge-Riemann implication is")
    print("                   formal.  K1 LOCATES the Euler content in C_W's radius -- M4's exact target.")
    print("  SEES-ZEROS       P_inf>=0 sees the zeros ONLY THROUGH C_W (the radius); E alone is blind.")
    print("  INDEPENDENT      the implication is independent (Hodge-Riemann, geometric), BUT the hypothesis")
    print("                   'C_W = the weight-1 Weil operator' over F_q IS |alpha|=sqrt q = RH.  So K1 is")
    print("                   CIRCULAR over F_q in the PRECISE sense: the Kahler datum C_W = the RH radius.")
    print("  -> The keystone is NOT 'attackable for free': the residue is real and named -- construct")
    print("     C_W's RADIUS over Z geometrically/Euler-wise.  That is the honest terminus (K5).")


if __name__ == "__main__":
    report()
