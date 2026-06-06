"""purity_carrier.py -- M2d: IS THE PURITY FUNCTOR rad:LocFac->G_m WELL-TYPED FOR zeta?

  run:  python3 -m scripts.numerics.witness.purity_carrier

THE MANDATE (AGENDA M2d, charter sec.1 clause C3b, built on M2b's purity refinement).
  M2b refined C3b to  rad = (.)^{1/2} o (edge-abscissa) : LocFac -> G_m, so
     Z-C3b  =  "zeta's local Euler factors {L_p} are PURE of weight 1"  (centre = sqrt(edge)).
  The edge datum is FF-clean (q=#A^1, read off the local product, exact, functorial).  The OPEN
  piece is the SQUARE-ROOT / PURITY step over Z.  M2d's job: DEFINE the weight/purity structure a
  SINGLE local factor must carry, and decide the TYPING question --

     is rad : LocFac -> G_m even WELL-TYPED for zeta, or does the edge->centre square root
     require the surface S^2/Z (the missing H^1) BEFORE purity has a carrier?

THE TRAP NAMED PRECISELY (the agenda's own statement of the hinge).
  Over F_q, PURITY is a property of H^1(C), which EXISTS because the *curve* supplies a weight-1
  cohomology.  Over Z, the abscissa Re s=1 is clean but there is NO PER-PRIME weight-1 object to be
  pure: zeta has no H^1 at a single prime.  So purity must be a property of the *global glued*
  factor (the M4 descent object).

WHAT THIS MODULE COMPUTES (the input slot of the purity functor, per place, EXACTLY).
  The purity functor needs, AT EACH PLACE, a WEIGHT-1 GRADED PIECE gr^W_1 to be pure of.  Its
  carrier, locally, is the NUMERATOR of the local zeta factor: for a curve C/F_q at a closed point,
  and for the GLOBAL zeta of C, the weight-1 cohomology H^1 shows up as the degree-2g numerator
  P(T)=prod(1-alpha_i T).  We measure, at each place, the DEGREE of the local numerator -- the rank
  of the weight-1 carrier the purity functor can act on:

    deg_num_local(place)  =  dim of the gr^W_1 the purity step has as INPUT at that place.

  FF GLOBAL zeta of a curve:  numerator degree 2g  -> a rank-2g weight-1 carrier EXISTS (H^1(C)).
  FF LOCAL factor at a point x of degree d:  L_x = (1-T^d)^{-1}, numerator degree 0 -> NO local H^1
    (the weight-1 cohomology is GLOBAL, assembled from all points via the Lefschetz/Euler product).
  zeta over Z, factor at prime p:  L_p = (1-p^{-s})^{-1}, numerator degree 0 -> NO per-prime H^1.
  zeta over Z, archimedean factor:  Gamma_R(s) -- an infinite product / no finite weight-1 numerator.

THE DECISIVE STRUCTURAL OUTPUT (the M2d deliverable).
  The per-prime carrier slot of the purity functor is EMPTY for BOTH the FF local factors AND zeta's
  primes -- numerator degree 0 in both.  The difference is NOT at the prime: it is that the FF
  ASSEMBLES a global weight-1 H^1 (degree 2g) from its local factors via the curve, whereas zeta's
  global numerator over the "Re s in (0,1)" strip is the COMPLETED xi -- whose 'H^1' (the nontrivial
  zeros) is NOT yet realized as a weight-1 cohomology of any geometric carrier.  So:

    rad_edge : LocFac -> G_m  IS well-typed for zeta (the EDGE q<->Re s=1 abscissa exists locally,
        per M2b -- the abscissa of abs. convergence is a property of the local product).
    rad = (.)^{1/2} o (edge) : LocFac -> G_m  is NOT well-typed PER-PRIME for zeta: the (.)^{1/2}
        (purity) factor needs a weight-1 carrier (gr^W_1) which does NOT exist per prime; it can only
        act on a GLOBAL glued object that SUPPLIES gr^W_1.  Over F_q the curve supplies it; over Z
        nothing yet does -- that carrier IS the missing surface S^2/Z (F-sym2-os-bridge.md).

  This RE-ROUTES M4: the descent must FIRST supply the weight-1 carrier (a global gr^W_1 of rank =
  "the count of nontrivial zeros' weight datum"), THEN the purity functor sets the centre Re s=1/2 as
  the square root of the edge.  C3b is NOT a per-prime condition; it is a condition on the WEIGHT
  FILTRATION of the glued object.  Purity has no LOCAL carrier; it is intrinsically GLOBAL for zeta.
"""
from __future__ import annotations

from fractions import Fraction
import numpy as np


# ----------------------------------------------------------------------------------------------------
# WEIGHT-1 CARRIER AT A PLACE = degree of the numerator of the local zeta factor.
#
# The purity functor rad = (.)^{1/2} o (edge) needs an object gr^W_1 (the weight-1 graded piece) to
# act on.  Cohomologically, gr^W_1 at a place is read off the numerator of the local zeta factor:
#   local factor  L(T) = P(T) / Q(T),  P = numerator (weight-1 H^1 contributions, the alpha_i),
#                                       Q = denominator (weight-0 H^0 and weight-2 H^2).
# deg P = rank of the weight-1 carrier available at that place.  deg P = 0 => NO weight-1 object to
# be pure of  =>  the purity (square-root) step has NO INPUT at that place.
# ----------------------------------------------------------------------------------------------------

def ff_global_numerator_degree(g):
    """FF: the GLOBAL zeta Z_C(T) = P(T)/((1-T)(1-qT)) of a curve C/F_q of genus g has numerator
    P(T)=prod_{i=1}^{2g}(1-alpha_i T) of degree 2g -- the weight-1 cohomology H^1(C) is a RANK-2g
    carrier.  This EXISTS because the CURVE supplies it (a geometric weight-1 object).  Returns 2g."""
    return 2 * g


def ff_local_factor_numerator_degree(deg_x):
    """FF: the LOCAL factor at a closed point x of degree d is L_x(T) = (1 - T^d)^{-1}: numerator
    degree 0 (it is purely a denominator -- a weight-0 / point datum).  There is NO local H^1: the
    weight-1 cohomology is assembled GLOBALLY from all the local factors via the Euler product
    (Z_C = prod_x L_x), not present at any single point.  Returns 0 for every closed point."""
    return 0


def zeta_prime_factor_numerator_degree(p):
    """zeta over Z: the factor at a prime p is L_p(s) = (1 - p^{-s})^{-1}: numerator degree 0 (pure
    denominator, a weight-0 'point' datum -- exactly like an FF closed point of degree 1).  There is
    NO per-prime H^1: zeta has no weight-1 cohomology at a single prime.  Returns 0."""
    return 0


def zeta_archimedean_factor_carrier():
    """zeta over Z: the archimedean factor is Gamma_R(s) = pi^{-s/2} Gamma(s/2): an INFINITE product
    of poles (s=0,-2,-4,...), NOT a finite-degree numerator.  It carries NO finite weight-1 numerator
    either -- the (p,q)-Hodge datum at infinity is a SEPARATE structure (M3), not a polynomial H^1.
    Returns the structural verdict (no finite weight-1 numerator)."""
    return dict(finite_weight1_numerator=False,
                note="Gamma_R is an infinite product of Gamma-poles; no finite-degree H^1 numerator")


# ----------------------------------------------------------------------------------------------------
# THE TYPING TEST: does the purity functor rad = (.)^{1/2} o (edge) have an INPUT at each place?
#
# rad_edge (the abscissa q<->Re s=1) is a property of the local PRODUCT (the convergence edge) and is
# well-typed locally (M2b).  The (.)^{1/2} (purity) FACTOR needs a weight-1 carrier gr^W_1 with deg>0.
# We check, per place, whether that carrier exists.
# ----------------------------------------------------------------------------------------------------

def purity_has_local_carrier(numerator_degree):
    """The (.)^{1/2} purity step acts on the weight-1 graded piece gr^W_1.  It has an INPUT at a place
    iff the local numerator degree > 0 (a nonzero weight-1 carrier).  Returns True/False."""
    return numerator_degree > 0


def edge_is_local(has_local_product):
    """rad_edge (the abscissa) is a property of the local PRODUCT's convergence; it exists wherever the
    Euler product does (per M2b: q = #A^1 read off any local factor's residue field; over Z, Re s=1 is
    the abscissa of abs. convergence of prod_p (1-p^{-s})^{-1}).  Returns has_local_product."""
    return has_local_product


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("M2d: the INPUT SLOT of the purity functor rad = (.)^{1/2} o (edge), per place.\n")
    print("  The (.)^{1/2} (purity) factor needs a WEIGHT-1 CARRIER gr^W_1 (numerator degree > 0).")
    print("  The (edge) factor (the abscissa) needs only the LOCAL PRODUCT (the convergence edge).\n")

    print(f"  {'place / object':42s} {'num.deg = rank gr^W_1':>22s} {'purity carrier?':>16s} {'edge?':>8s}")
    print("  " + "-" * 92)

    rows = []

    # FF GLOBAL: the curve supplies H^1 (rank 2g)
    for g in (1, 2, 3):
        d = ff_global_numerator_degree(g)
        rows.append((f"FF GLOBAL zeta_C, genus g={g}  (the CURVE)", d, purity_has_local_carrier(d), edge_is_local(True)))

    # FF LOCAL factor at closed points
    for deg_x in (1, 2, 3):
        d = ff_local_factor_numerator_degree(deg_x)
        rows.append((f"FF LOCAL factor L_x, deg x={deg_x}  (a POINT)", d, purity_has_local_carrier(d), edge_is_local(True)))

    # zeta over Z: per-prime factors
    for p in (2, 3, 5, 7):
        d = zeta_prime_factor_numerator_degree(p)
        rows.append((f"zeta/Z factor L_p, p={p}  (a PRIME)", d, purity_has_local_carrier(d), edge_is_local(True)))

    for name, d, carrier, edge in rows:
        print(f"  {name:42s} {d:>22d} {str(carrier):>16s} {str(edge):>8s}")

    # archimedean
    arch = zeta_archimedean_factor_carrier()
    print(f"  {'zeta/Z factor Gamma_R(s)  (place INFTY)':42s} {'(infinite prod)':>22s} "
          f"{str(arch['finite_weight1_numerator']):>16s} {'N/A':>8s}")

    print("\n" + "=" * 100)
    print("THE DECISIVE STRUCTURAL OUTPUT (M2d):\n")
    print("  (1) PER-PLACE, the weight-1 carrier is EMPTY for BOTH FF local factors AND zeta's primes")
    print("      (numerator degree 0 in both -- a local factor is a weight-0 'point').  So the purity")
    print("      step  (.)^{1/2}  has NO LOCAL INPUT in EITHER case.  The difference is NOT at the prime.")
    print()
    print("  (2) The FF ASSEMBLES a GLOBAL weight-1 H^1 (rank 2g) from its local factors -- because the")
    print("      CURVE is a 1-diml geometric object whose H^1 the Euler product computes (Lefschetz).")
    print("      zeta's primes assemble NO such weight-1 cohomology: Spec Z is 0-diml arithmetically,")
    print("      and zeta's 'H^1' (the nontrivial zeros) is NOT realized as the weight-1 cohomology of")
    print("      any geometric carrier.  THAT missing carrier is the surface S^2/Z (F-sym2-os-bridge).")
    print()
    print("  (3) TYPING VERDICT for the purity functor over zeta:")
    print("        rad_edge : LocFac -> G_m              WELL-TYPED  (the abscissa Re s=1 is local, M2b)")
    print("        rad = (.)^{1/2} o (edge) : per-prime  NOT WELL-TYPED  (no per-prime gr^W_1 to halve)")
    print("        rad = (.)^{1/2} o (edge) : GLOBAL      requires a glued object SUPPLYING gr^W_1 first")
    print()
    print("  => C3b is NOT a per-prime condition.  It is a condition on the WEIGHT FILTRATION of the")
    print("     GLOBAL GLUED object: the descent (M4) must FIRST construct a weight-1 carrier gr^W_1")
    print("     (the H^1 no single prime supplies), THEN the purity functor sets the centre Re s=1/2 as")
    print("     the square root of the edge Re s=1.  Purity has NO LOCAL carrier for zeta; it is")
    print("     intrinsically GLOBAL.  This RE-ROUTES M4: descent supplies the carrier BEFORE purity acts.")

    print("\n" + "=" * 100)
    print("CONTRAST WITH F_q (why the FF gets purity 'for free' and Z does not):\n")
    print("  Over F_q the weight-1 carrier H^1(C) is a GEOMETRIC object (etale cohomology of an actual")
    print("  curve), and Deligne PURITY (|alpha|=q^{1/2}) is a THEOREM about it.  The Euler product")
    print("  merely COMPUTES this pre-existing carrier (Lefschetz).  Over Z there is NO pre-existing")
    print("  geometric weight-1 carrier for zeta -- so purity has nothing to be a theorem ABOUT until a")
    print("  carrier is CONSTRUCTED.  Construction (M4 descent + the S^2/Z surface) must come BEFORE")
    print("  purity, not after.  THIS IS THE PRECISE SENSE IN WHICH C3b IS THE OPEN PROBLEM:")
    print("  not 'prove purity' but 'BUILD the carrier purity would be a property of'.")

    print("\n" + "=" * 100)
    print("DH FALSIFIER (C6), refined to the carrier level:\n")
    print("  DH has an FE (so the s<->1-s similitude, rad_FE=1, survives -- DH-shared) but NO Euler")
    print("  product, hence NO local factors, hence NEITHER the edge (no abscissa-of-product) NOR any")
    print("  hope of assembling a weight-1 carrier from local factors.  So for DH the purity functor")
    print("  fails at the FIRST factor (edge: empty LocFac) -- it never even reaches the carrier question.")
    print("  zeta at least HAS the edge (the Euler product gives Re s=1) and the OPEN problem of building")
    print("  the carrier; DH lacks even the edge.  C6 is thus a STRICT refinement: DH < zeta < FF on the")
    print("  'how much of the purity functor types' ladder:")
    print("       FF   : edge YES, local carrier NO but GLOBAL carrier YES (the curve)  -> purity THEOREM")
    print("       zeta : edge YES, local carrier NO, global carrier OPEN (S^2/Z)        -> purity OPEN")
    print("       DH   : edge NO (no product)                                           -> purity N/A")

    print("\n" + "=" * 100)
    print("VERDICT [DEF + coherence]: the purity functor rad = (.)^{1/2} o (edge) is NOT well-typed")
    print("  per-prime over zeta -- the (.)^{1/2} step needs a weight-1 carrier gr^W_1 that no single")
    print("  prime supplies (per-prime numerator degree 0, IDENTICAL to FF local factors).  rad_edge")
    print("  alone IS well-typed (the abscissa is local).  The carrier exists GLOBALLY in the FF (the")
    print("  curve's H^1, rank 2g) but is the OPEN object over Z (the surface S^2/Z).  So C3b is a")
    print("  condition on the WEIGHT FILTRATION OF THE GLUED OBJECT, and M4 must supply the carrier")
    print("  BEFORE purity sets Re s=1/2.  Purity is intrinsically GLOBAL for zeta -- not a per-prime")
    print("  property.  This NAMES THE NEXT DEFINITION: the weight-1 carrier (gr^W_1) the descent builds.")


if __name__ == "__main__":
    report()
