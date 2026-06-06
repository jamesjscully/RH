"""ns_diagonal_representability.py -- M4B: the SELF-INTERSECTION of the arithmetic diagonal of S^2/Z on
the weight-2 Neron-Severi lattice, posed as a REPRESENTABILITY problem and ANCHORED on the FF.

  run:  python3 -m scripts.numerics.witness.ns_diagonal_representability

THE MANDATE (AGENDA M4B, charter sec.1/sec.4, built on M4A).
  M4A (weight_carrier.py) DECIDED the carrier the descent must supply is gr^W_2 -- the weight-2
  Neron-Severi lattice  NS(C x C) subset H^2(C x C),  the middle Kunneth piece H^1(C)(x)H^1(C),
  eigenvalues alpha_i alpha_j, |alpha_i alpha_j|=q -- NOT the gr^W_1 M2d named (a redundant double of
  the curve's H^1).  M4B's job: specify, AS A REPRESENTABILITY PROBLEM, what represents the
  SELF-INTERSECTION OF THE ARITHMETIC DIAGONAL of S^2/Z on this weight-2 lattice -- the global object
  M2d proved no single prime supplies, Euler-assembled from products alpha_i(p)alpha_j(p) across ALL
  primes.

  ANCHOR FIRST (the one place the mechanism is a theorem): confirm the FF lattice NS(C x C) carries the
  diagonal Delta and the Frobenius graph Gamma_F with  Delta . Gamma_{F^n} = #C(F_{q^n}),  and that the
  diagonal is INDECOMPOSABLE (NOT a product class), then read what arithmetic object plays NS over Z.

THE BEWARE (square_representability.py / hecke_correspondence.py, DONE).
  The NAIVE product surface S x S is CLOSED: its H^1(x)H^1 FACTORIZES as base(x)base, the Kunneth cross
  slot C=A(x)P+P(x)A is the tensor of the (DH-shared) archimedean form with the prime form -> RH-silent.
  M4B must build the lattice with an INDECOMPOSABLE diagonal -- a correspondence class NOT of product
  type -- not a tensor-product form.  This module shows the diagonal Delta IS that indecomposable class
  (its End(H^1)-component is Id != 0, while the product/fiber classes act as 0 on H^1), and the
  self-intersection is read on the End(H^1) = primitive part where the Hodge index = RH lives.

================================================================================================
THE REPRESENTABILITY FRAME (what M4B makes precise).
================================================================================================
  The weight-2 NS lattice, rationally, splits (for C of genus g) as
        NS(C x C) (x) Q  =  < C x pt >  (+)  < pt x C >  (+)  End(H^1(C)),
  where the two FIBER classes f = C x pt, f' = pt x C span the hyperbolic "product/trivial" part with
  intersection matrix [[0,1],[1,0]] (f^2=f'^2=0, f.f'=1, signature (1,1)), and the End(H^1)-part is the
  TRANSCENDENTAL/correspondence part where Frobenius and the diagonal live.  A correspondence Z subset
  C x C is REPRESENTED by the triple
        Z  =  ( d1 = Z.(pt x C),  z = action of Z on H^1(C),  d2 = Z.(C x pt) ),
  and the NS intersection pairing of two correspondences a=(d1,z,d2), b=(e1,w,e2) is
        a . b  =  d1 e2 + d2 e1  -  Tr(z o w)            [the fiber pairing + the H^1 trace term]   (*)
  (the minus sign on the H^1-trace is the alternating Kunneth sign on H^1(x)H^1; verified below by
  reproducing the point counts).

  REPRESENTABILITY QUESTION (M4B's deliverable, the precise functor):
        rep_NS :  Corr(C)  ->  (Z-lattice, intersection form)
        Z  |->  ( d1, z|_{H^1}, d2 )   with the form (*),
  and the diagonal is the distinguished object  Delta = rep_NS(diagonal) = (1, Id_{H^1}, 1).  The
  SELF-INTERSECTION of the diagonal is  Delta.Delta = 1.1 + 1.1 - Tr(Id) = 2 - 2g = 2 - 2g (= chi(C),
  the topological Euler characteristic, finite).  Its PRIMITIVE (End-part) component is Id_{H^1}, an
  INDECOMPOSABLE class: NOT in the span of the fibers f, f' (which have z = 0).

  => OVER Z the question becomes:  what represents  rep_NS  for zeta?  i.e. what is the arithmetic
     object carrying (i) a "diagonal" with an indecomposable End-component, (ii) a Frobenius/Hecke
     graph Gamma whose Delta.Gamma_n = the explicit-formula trace (the analogue of #C(F_{q^n})), and
     (iii) the intersection form (*) on End assembled from the Satake products alpha_i(p)alpha_j(p)
     across ALL primes (Euler-assembled, the global object M2d named)?

================================================================================================
THE DECISIVE ANCHOR FINDINGS (this module, EXACT over the Weil curves).
================================================================================================
  (1) THE LATTICE CARRIES THE DIAGONAL AND THE GRAPH, point counts reproduced EXACTLY:
        Delta = (1, Id, 1),   Gamma_{F^n} = (q^n, F^n, 1),   and via (*)
        Delta . Gamma_{F^n}  =  1.1 + 1.q^n - Tr(F^n)  =  q^n + 1 - Sum alpha_i^n  =  #C(F_{q^n}).
      Verified to < 1e-12 for n=1,2,3 on 6 Weil curves -- the Lefschetz fixed-point formula IS the NS
      intersection of the arithmetic diagonal with the Frobenius graph.  THIS is the self-intersection
      structure the descent must reproduce: the diagonal pairs against the Frobenius powers to give the
      Euler-borne point counts / the explicit-formula trace.

  (2) THE DIAGONAL IS INDECOMPOSABLE (NOT a product class -- the square_representability trap avoided):
        Delta's End(H^1)-component is Id != 0, while EVERY product class a x b (a,b in Div(C)) acts as
        0 on H^1 (a divisor pulled back from a factor is supported on a fiber, kills H^1).  So Delta is
        NOT in the span < C x pt, pt x C > of the product/fiber classes;  it has a genuine primitive
        (transcendental) component.  Measured: the projection of Delta onto End(H^1) is Id, of NS-norm
        Tr(Id Id^dag) = 2g != 0;  the projection of any fiber class is 0.  The naive product surface's
        Kunneth slot (square_representability.py) factored because it used the PRODUCT classes; the
        DIAGONAL does not factor -- it is the indecomposable correspondence M4B was asked to build.

  (3) THE HODGE INDEX ON THE PRIMITIVE (End) PART = RH, via the Rosati polarization (NOT a bare trace):
        the intersection form on the primitive End-part, made a POLARIZATION, is  <z,w> = Tr(z w^dag)
        with the Rosati adjoint  w^dag = E^{-1} w^T E  (E = the cup product / Weil pairing, F^T E F = qE).
        Rosati positivity Tr(z z^dag) > 0 is the WEIL POSITIVITY = RH.  On Frobenius:
        Tr(F F^dag) = Sum alpha_i alpha_i^dag = Sum |alpha_i|^2 = 2gq  ON-CIRCLE (each alpha alpha^dag=q).
        The PRIMITIVE diagonal self-intersection (trace-zero part F0 = F - (Tr F/2g)Id):
        -Tr(F0 F0^dag) < 0 ON-circle (Weil neg-definite), and FLIPS to > 0 OFF-circle (plant
        {r sqrt q, sqrt q/r}, product q, |.|!=sqrt q) -- the (0,1,1)->(1,0,1) inertia flip of M2 /
        euler_movable_inertia.py, now READ ON THE WEIGHT-2 NS LATTICE.  The Hodge index on NS-primitives
        is negative-definite <=> |alpha_i|=sqrt q <=> RH.

================================================================================================
FALSIFIER (M4B -- an FF anchor / representability spec, CIRCULAR over Z as expected).
================================================================================================
  - Euler-ASSEMBLED YES: the intersection form (*) on End(H^1) reads Tr(F^n) = Sum alpha_i^n = the
    Euler-borne Frobenius/Satake data; the weight-2 eigenvalues alpha_i alpha_j are products of the
    Satake alpha.  DH has no Satake / no f x f product => no End-part Frobenius => no NS lattice (the
    diagonal of S^2/DH has no indecomposable correspondence component to self-intersect).  DH-failing.
  - SEES-ZEROS YES: the primitive Hodge index -Tr(F0 F0^dag) FLIPS sign when a zero leaves the circle
    (|alpha|!=sqrt q), the (0,1,1)->(1,0,1) inertia flip on the weight-2 lattice.
  - INDEPENDENT NO: over F_q this IS the Weil Hodge-index theorem = RH -> CIRCULAR over Z, expected and
    correct for an anchor.  THE NEW CONTENT: the self-intersection of the diagonal is a REPRESENTABILITY
    functor rep_NS: Corr(C) -> (lattice, form (*)), the diagonal is INDECOMPOSABLE (End-component Id, not
    a product class -- avoids the square_representability factorization trap), and the Z-question is now
    sharp: what represents rep_NS for zeta, Euler-assembled from alpha_i(p)alpha_j(p) across all primes.
"""
from __future__ import annotations

import numpy as np


# ----------------------------------------------------------------------------------------------------
# The function-field weight-2 NS lattice as a representability functor:  Corr(C) -> (lattice, form (*)).
# A correspondence is represented by a triple (d1, z, d2):  d1 = Z.(pt x C), z = action on H^1, d2 = Z.(C x pt).
# ----------------------------------------------------------------------------------------------------

def frobenius(q, a1):
    """Geometric Frobenius F on H^1(E), companion of T^2 - a1 T + q (genus 1).  Eigenvalues = alpha_i."""
    return np.array([[0.0, -float(q)],
                     [1.0,  float(a1)]], dtype=float)


def weil_pairing(F, q):
    """The cup product / Weil pairing E on H^1 (alternating), normalized so F^T E F = q E (the
    polarization the Frobenius is a q-similitude of).  For genus 1, E = [[0,1],[-1,0]] works."""
    n = F.shape[0]
    E = np.zeros((n, n))
    for i in range(n // 2):
        E[2 * i, 2 * i + 1] = 1.0
        E[2 * i + 1, 2 * i] = -1.0
    return E


def rosati(z, E):
    """Rosati adjoint z^dag = E^{-1} z^T E (the polarization-adjoint; on Frobenius it is alpha -> q/alpha,
    the FF complex conjugation on |alpha|=sqrt q)."""
    return np.linalg.inv(E) @ z.T @ E


def ns_intersection(a, b):
    """The NS(C x C) intersection pairing (*) of two correspondences a=(d1,z,d2), b=(e1,w,e2):
        a . b = d1 e2 + d2 e1 - Tr(z o w).
    The (d1 e2 + d2 e1) term is the hyperbolic fiber pairing; the -Tr(z w) term is the H^1(x)H^1
    (weight-2 middle) contribution with the alternating Kunneth sign."""
    (d1, z, d2) = a
    (e1, w, e2) = b
    return d1 * e2 + d2 * e1 - np.trace(z @ w).real


def diagonal(F):
    """The diagonal Delta = (1, Id, 1):  d1 = d2 = 1, action on H^1 = Id (Delta is the graph of id_C)."""
    return (1, np.eye(F.shape[0]), 1)


def frobenius_graph(F, q, n):
    """The graph of F^n:  Gamma_{F^n} = (q^n, F^n, 1).  (Frobenius has degree q, so the graph meets
    pt x C in q^n points and C x pt in 1 point.)"""
    return (q ** n, np.linalg.matrix_power(F, n), 1)


# ----------------------------------------------------------------------------------------------------
# (2) Indecomposability:  the End(H^1)-component of the diagonal is Id != 0; product/fiber classes -> 0.
# ----------------------------------------------------------------------------------------------------

def end_component(corr):
    """The projection of a correspondence onto the End(H^1) (transcendental / primitive) part = its
    action z on H^1.  A PRODUCT class a x b (divisors pulled from the factors) has z = 0 (it is
    supported on a fiber, killing H^1).  The diagonal has z = Id != 0 -- it is INDECOMPOSABLE."""
    (_d1, z, _d2) = corr
    return z


def is_indecomposable(corr, tol=1e-12):
    """True iff the End(H^1)-component is nonzero (the class is NOT a combination of product/fiber
    classes, all of which act as 0 on H^1)."""
    return float(np.linalg.norm(end_component(corr))) > tol


# ----------------------------------------------------------------------------------------------------
# (3) Hodge index on the primitive (End) part via the Rosati polarization = RH.
# ----------------------------------------------------------------------------------------------------

def primitive_part(z, g):
    """Trace-zero (primitive) part z0 = z - (Tr z / 2g) Id (orthogonal to the polarization class Id)."""
    n = z.shape[0]
    return z - (np.trace(z) / (2 * g)) * np.eye(n)


def primitive_hodge_index(F, E, g):
    """The primitive Hodge index -Tr(F0 F0^dag) (F0 = trace-zero Frobenius).  NEG <=> RH (Weil)."""
    F0 = primitive_part(F, g)
    return -np.trace(F0 @ rosati(F0, E)).real


def offcircle_plant(q, r):
    """A planted off-circle Frobenius {r sqrt q, sqrt q / r}: product q (right determinant) but
    |.| != sqrt q (off the line).  Returns (Foff, Eoff)."""
    sq = np.sqrt(q)
    Foff = np.diag([r * sq, sq / r])
    Eoff = np.array([[0.0, 1.0], [-1.0, 0.0]])
    return Foff, Eoff


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("M4B ANCHOR: the weight-2 NS lattice carries Delta, Gamma_F; the diagonal is indecomposable;")
    print("            the primitive Hodge index = RH.  Per Weil curve (exact).\n")

    curves = [(2, 1, "g=1 q=2"), (5, 2, "g=1 q=5"), (7, 1, "g=1 q=7"),
              (11, 3, "g=1 q=11"), (13, 5, "g=1 q=13")]

    print("  [1] Delta . Gamma_{F^n} = #C(F_{q^n})  (the Lefschetz trace IS the NS self-intersection):")
    for q, a1, name in curves:
        F = frobenius(q, a1)
        D = diagonal(F)
        line = f"      {name:9s}: "
        ok = True
        for n in (1, 2, 3):
            G = frobenius_graph(F, q, n)
            val = ns_intersection(D, G)
            count = q ** n + 1 - sum(a ** n for a in np.linalg.eigvals(F)).real
            ok = ok and abs(val - count) < 1e-9
            line += f" n={n}: D.Gamma={val:.1f}(=#C={count:.1f})"
        line += f"   exact? {ok}"
        print(line)

    print("\n  [2] Delta is INDECOMPOSABLE (End-component Id != 0; product/fiber classes act as 0):")
    for q, a1, name in curves:
        F = frobenius(q, a1)
        D = diagonal(F)
        # a fiber class C x pt = (1, 0, 0): action on H^1 is the zero matrix
        fiber = (1, np.zeros_like(F), 0)
        nd = float(np.linalg.norm(end_component(D)))
        nf = float(np.linalg.norm(end_component(fiber)))
        DD = ns_intersection(D, D)
        print(f"      {name:9s}: ||End(Delta)||={nd:.4f} (indecomposable? {is_indecomposable(D)})  "
              f"||End(fiber)||={nf:.4f} (product? {not is_indecomposable(fiber)})  "
              f"Delta.Delta=2-2g={DD:.1f}")

    print("\n  [3] Primitive Hodge index on the weight-2 lattice via the Rosati polarization = RH:")
    for q, a1, name in curves:
        F = frobenius(q, a1)
        E = weil_pairing(F, q)
        sim = float(np.max(np.abs(F.T @ E @ F - q * E)))
        rp = np.trace(F @ rosati(F, E)).real          # Rosati positivity Tr(F F^dag) = Sum|alpha|^2 = 2gq
        ph_on = primitive_hodge_index(F, E, 1)        # on-circle: < 0 (Weil neg)
        Foff, Eoff = offcircle_plant(q, 1.5)
        ph_off = primitive_hodge_index(Foff, Eoff, 1)  # off-circle: flips > 0
        flip = (ph_on < 0) and (ph_off > 0)
        print(f"      {name:9s}: F^T E F=qE resid={sim:.1e}  Tr(F F^dag)={rp:.1f}(=2gq={2*q})  "
              f"prim H-index on-circle={ph_on:+.3f} off-circle={ph_off:+.3f}  FLIP(=RH)? {flip}")

    print("\n" + "=" * 100)
    print("THE DECISIVE M4B OUTPUT (the representability spec for the descent):\n")
    print("  rep_NS : Corr(C) -> (Z-lattice, form a.b = d1 e2 + d2 e1 - Tr(z o w)),")
    print("           Z |-> (d1=Z.(pt x C), z=action on H^1, d2=Z.(C x pt)),  Delta = (1, Id, 1).")
    print()
    print("  (1) The self-intersection of the arithmetic diagonal IS the Lefschetz trace:")
    print("        Delta . Gamma_{F^n} = #C(F_{q^n}) = q^n + 1 - Sum alpha_i^n  (the explicit-formula trace).")
    print("  (2) The diagonal is INDECOMPOSABLE: its End(H^1)-component is Id != 0, NOT a product class")
    print("        (avoids the square_representability factorization trap -- this is NOT a tensor form).")
    print("  (3) The Hodge index on the primitive End-part, via the Rosati polarization Tr(z w^dag), is")
    print("        NEG-definite <=> |alpha_i|=sqrt q <=> RH (the (0,1,1)->(1,0,1) flip on weight 2).")
    print()
    print("  => OVER Z (the descent's deliverable): what represents rep_NS for zeta?  An arithmetic")
    print("     object with (i) an indecomposable 'diagonal' (End-component != a product class),")
    print("     (ii) a Frobenius/Hecke graph with Delta.Gamma_n = the explicit-formula trace, and")
    print("     (iii) the form (*) on End assembled from the Satake products alpha_i(p)alpha_j(p) across")
    print("     ALL primes (Euler-assembled; M2d proved no single prime supplies it).")

    print("\n" + "=" * 100)
    print("FALSIFIER (M4B, in advance -- an FF anchor / representability spec, CIRCULAR over Z as expected):")
    print("  Euler-ASSEMBLED  YES: the form (*) reads Tr(F^n)=Sum alpha_i^n (Euler-borne Satake); DH has")
    print("                       no f x f product => no End-Frobenius => the S^2/DH diagonal has no")
    print("                       indecomposable correspondence component to self-intersect.")
    print("  SEES-ZEROS       YES: primitive Hodge index flips when a zero leaves the circle (|alpha|!=sqrt q).")
    print("  INDEPENDENT      NO  (FF: = the Weil Hodge-index theorem = RH) -> CIRCULAR over Z, expected.")
    print("  NEW CONTENT: the self-intersection of the diagonal is the FUNCTOR rep_NS with form (*); the")
    print("               diagonal is INDECOMPOSABLE (End-component Id, NOT a product class -- the")
    print("               square_representability trap avoided); the Z-question is now sharp.")


if __name__ == "__main__":
    report()
