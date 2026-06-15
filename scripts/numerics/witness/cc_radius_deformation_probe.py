"""cc_radius_deformation_probe.py -- P131.2: deform the Weil radius INDEPENDENTLY of the
   planted zero ordinate and test whether the weight-2 NS inertia flip tracks an
   Euler-ASSEMBLED radius or ONLY the imported |alpha| = sqrt q.

  run:  python3 -m scripts.numerics.witness.cc_radius_deformation_probe

THE MANDATE (doc 131 probe P131.2; built directly on ns_hodge_index_duality + cw_radius_assembly).
  ns_hodge_index_duality builds the weight-2 NS Hodge index H = -Tr(F0 F0^dag) on End(H^1) and
  shows the inertia FLIPS (neg-def -> gains a +) iff a zero leaves |alpha| = sqrt q.  But there the
  radius is supplied BY THE PLANTED SPECTRUM itself (offcircle_plant hard-codes [r sqrt q, sqrt q/r]).
  cw_radius_assembly shows the ONLY zero-free Euler datum is the DETERMINANT EDGE
  det = alpha*beta = q (= p^{k-1}); the radius itself (the even split |alpha|=|beta|=sqrt q) IS RH.

  P131.2's question (the decisive doc-131 fork ESCAPE vs COLLAPSE):
    Coordinatize the planted Frobenius spectrum by TWO INDEPENDENT data:
      (ORD) the "zero ordinate" / phase data  =  the L-coefficient a1 = Tr F = Sum alpha_i
            (the trace; the angle theta of the Frobenius eigenvalue on its circle), AND
      (RAD) the RADIUS data                   =  the moduli |alpha_i|.
    Then DEFORM (RAD) while HOLDING (ORD) fixed, supplying the radius candidate from the ONLY
    zero-free Euler source available (cw_radius_assembly): the determinant edge det = q, whose
    purity square root rho = sqrt(det) = sqrt q is the "Euler-assembled radius candidate".

    DECISIVE TEST.  Does the NS inertia flip (H <= 0  <=>  on-line) track
      (A) the Euler-assembled radius rho = sqrt(det)  -- i.e. flip <=> |alpha_i| deformed to rho?
          [ -> R-ESCAPE: the flip is driven by an independently-supplied Euler radius ]
    or
      (B) ONLY the EVEN SPLIT |alpha_1| = |alpha_2| = ... = sqrt q  -- i.e. the flip needs every
          modulus EQUAL to sqrt q, not merely the Euler edge det = q?
          [ -> R-COLLAPSE: the Euler edge is FREE but the flip reads the even split = RH ]

  THE CONSTRUCTION THAT MAKES (ORD) AND (RAD) INDEPENDENT (the whole point).
    For g=1 a Frobenius pair is (alpha, beta) with two real degrees of freedom we can choose freely:
      * the Euler edge      det = alpha*beta              (= q, the ZERO-FREE Satake determinant), and
      * the modulus split   s   s.t. |alpha| = sqrt(det)*e^{+s}, |beta| = sqrt(det)*e^{-s}.
    Holding det = q (the Euler edge, supplied free) and varying s sweeps the RADIUS away from the
    even split WITHOUT touching the edge.  We do NOT import any zero ordinate to set the radius:
    the radius candidate rho = sqrt(det) comes ONLY from the determinant det = q, which
    cw_radius_assembly certifies is Euler-borne / RH-independent.  s is a FREE deformation knob,
    not read from data.  (s = 0 is the even split; s != 0 is off-circle with the SAME edge.)

    The NS modulus defect that drives the flip is
        defect(s) = Sum_i |alpha_i|^2  -  2 g * det
                  = det * ( e^{2s} + e^{-2s} - 2 )                       (g = 1, one pair)
                  = det * ( 2 cosh(2s) - 2 )  >= 0,   = 0  iff  s = 0.
    So with det = q HELD FIXED at the Euler edge, the Hodge index H = -P_NS(F0,F0) is
    neg(semi)def IFF s = 0 (the EVEN SPLIT), and gains a + for ANY s != 0.  The flip therefore
    tracks the EVEN SPLIT, NOT the Euler edge: holding the Euler-assembled datum (det = q) fixed
    does NOT pin the radius; the flip still needs |alpha| = |beta| = sqrt q, which is RH.

  This is doc 131's R-COLLAPSE, made executable as a clean two-coordinate independence test:
  the Euler assembly supplies the edge (det) for free, and the inertia flip is INSENSITIVE to it
  (any det>0 with s=0 is on-line; any det>0 with s!=0 is off-line) -- the flip reads ONLY the
  even split.  flip_tracks = IMPORTED_ONLY.

FREEZE PROTOCOL HONORED.  No zeta-zero / RH-line data is imported to build the radius.  The radius
  candidate rho = sqrt(det) is the purity root of the Satake DETERMINANT (Euler-borne, doc-59 clean);
  the deformation knob s is a FREE real parameter, not fitted to any zero ordinate.  The only place
  sqrt q appears as a TARGET is in the COMPARISON (does the flip land at s=0 <=> |alpha|=sqrt q),
  which is doc-59 comparison-only zero contact (E4), never construction input.

DOC-130 TRICHOTOMY TAG.  The flip eigenvalue (the defect) is the acting plant F's OWN modulus split,
  supplied by F itself, NOT by the carrier/slot before F is chosen, and NOT by the Euler edge (which
  is flip-blind).  This is doc 130 case (S) self-supply / failed E5' (no carrier-fixed eigenvalue):
  the radius IS the answer, and the Euler edge cannot fix it.  Expected, full-value R-COLLAPSE.
"""
from __future__ import annotations

import numpy as np

# Reuse the ns_hodge_index_duality primitives -- we do NOT reimplement the pairing.
from scripts.numerics.witness.ns_hodge_index_duality import (
    frobenius_and_cup,
    primitive_hodge_index,
    P_gram,
)


# ----------------------------------------------------------------------------------------------------
# The two INDEPENDENT coordinates: the Euler edge (det, zero-free) and the radius split s (free knob).
# ----------------------------------------------------------------------------------------------------

def euler_edge_radius(q):
    """The Euler-ASSEMBLED radius candidate over Z: the purity square root of the Satake DETERMINANT
    edge det = alpha*beta = q.  cw_radius_assembly certifies det = q (= p^{k-1}) is Euler-borne and
    RH-INDEPENDENT -- it is the determinant of the Satake matrix, free even off-Ramanujan.  We use
    rho = sqrt(det) as the radius supplied WITHOUT any zero import."""
    det = float(q)            # the Euler edge: determinant of the Satake matrix, zero-free
    rho = np.sqrt(det)        # purity square root = the radius candidate
    return det, rho


def split_pair(det, s):
    """A g=1 Frobenius pair (alpha, beta) with the Euler edge det HELD FIXED and the radius deformed
    by the FREE split knob s:  |alpha| = sqrt(det) e^{+s}, |beta| = sqrt(det) e^{-s}, product = det.
    s = 0  <=>  the EVEN split (|alpha|=|beta|=sqrt det).  We place the pair on the positive real
    axis so the product is real = det (the FE/Rosati similitude F^T E F = det*E is preserved for ALL
    s -- the edge is radius-blind, exactly cw_radius_assembly's finding)."""
    sq = np.sqrt(det)
    alpha = sq * np.exp(+s)
    beta = sq * np.exp(-s)        # alpha*beta = det, independent of s
    return [alpha, beta]


def split_pair_with_ordinate(det, s, theta):
    """Same edge det and split s, but now carrying an INDEPENDENT 'zero ordinate' / phase theta:
    alpha = sqrt(det) e^{+s} e^{+i theta}, beta = sqrt(det) e^{-s} e^{-i theta}.  product = det still.
    Demonstrates ORD (theta) and RAD (s) are genuinely independent: theta moves the ordinate, s moves
    the radius, det stays the Euler edge.  The NS defect depends ONLY on s (the radius), NOT theta."""
    sq = np.sqrt(det)
    alpha = sq * np.exp(+s) * np.exp(+1j * theta)
    beta = sq * np.exp(-s) * np.exp(-1j * theta)
    return [alpha, beta]


def hodge_index_at(det, roots):
    """Build (F, E) via the ns_hodge_index_duality primitive on the given roots with the given edge
    det, and return the weight-2 NS Hodge index H = -Tr(F0 F0^dag) and the similitude residual."""
    F, E = frobenius_and_cup(roots, det)
    sim = float(np.max(np.abs(F.T @ E @ F - det * E)))
    H = primitive_hodge_index(F, E, 1)
    rp = P_gram(F, F, E)               # Tr(F F^dag) = Sum|alpha|^2
    return H, sim, rp


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("P131.2: DEFORM THE RADIUS INDEPENDENTLY OF THE ZERO ORDINATE; DOES THE NS FLIP TRACK")
    print("        THE EULER-ASSEMBLED RADIUS (det), OR ONLY THE EVEN SPLIT |alpha|=sqrt q?\n")

    QS = [2, 5, 7, 11, 13]

    # ---- [1] The Euler edge det = q is supplied ZERO-FREE; rho = sqrt(det) is the radius candidate.
    print("[1] The Euler-ASSEMBLED radius candidate rho = sqrt(det), det = q the Satake determinant")
    print("    edge (cw_radius_assembly: Euler-borne, RH-independent).  This is the ONLY zero-free")
    print("    radius datum available over Z.\n")
    print(f"    {'q':>3s} {'Euler edge det':>16s} {'rho=sqrt(det)':>16s}")
    for q in QS:
        det, rho = euler_edge_radius(q)
        print(f"    {q:>3d} {det:>16.6f} {rho:>16.6f}")

    # ---- [2] DECISIVE: hold the Euler edge det FIXED, sweep the radius split s.  Where does H flip?
    print("\n" + "=" * 100)
    print("[2] DECISIVE TEST.  HOLD the Euler edge det = q FIXED (supplied free), SWEEP the radius")
    print("    split s (FREE knob, no zero imported).  H <= 0 (on-line) IFF s = 0 (the EVEN split).")
    print("    If H tracked the Euler edge, det = q alone would pin it -- it does NOT; any s != 0")
    print("    flips it.  defect(s) = det*(2cosh(2s)-2) >= 0, = 0 iff s = 0.\n")
    print(f"    {'q':>3s} {'s':>7s} {'|alpha|':>10s} {'|beta|':>10s} {'edge det':>10s} {'Sum|a|^2':>10s}"
          f" {'H-index':>10s}  on-line(H<=0)?")
    collapse_confirmed = True
    for q in QS:
        det, rho = euler_edge_radius(q)
        for s in [0.0, 0.15, 0.30, -0.30]:
            roots = split_pair(det, s)
            H, sim, rp = hodge_index_at(det, roots)
            ra, rb = abs(roots[0]), abs(roots[1])
            on_line = H <= 1e-9
            # COLLAPSE = the flip is at s==0 only, and the edge det is identical for all these rows.
            expect_on = abs(s) < 1e-12
            if on_line != expect_on:
                collapse_confirmed = False
            tag = "" if (sim < 1e-9) else f"  [sim resid {sim:.1e}]"
            print(f"    {q:>3d} {s:>7.2f} {ra:>10.4f} {rb:>10.4f} {det:>10.4f} {rp:>10.4f}"
                  f" {H:>+10.4f}  {on_line}{tag}")
        print()

    # ---- [3] INDEPENDENCE: move the zero ORDINATE theta with s=0; H is UNCHANGED (radius != ordinate)
    print("=" * 100)
    print("[3] INDEPENDENCE of (ORD) and (RAD).  Hold s = 0 (even split, on-line) and SWEEP the zero")
    print("    ordinate / phase theta.  H stays <= 0 (on-line) for ALL theta -- the flip reads the")
    print("    RADIUS, not the ordinate.  Conversely [2] swept the radius with theta fixed and DID")
    print("    flip.  So (ORD, RAD) are independent coordinates and the flip tracks (RAD) only.\n")
    print(f"    {'q':>3s} {'theta':>7s} {'s':>5s} {'|alpha|':>10s} {'edge det':>10s} {'H-index':>10s}  on-line?")
    ordinate_independent = True
    for q in QS[:3]:
        det, rho = euler_edge_radius(q)
        for theta in [0.0, 0.4, 0.9, 1.3]:
            roots = split_pair_with_ordinate(det, 0.0, theta)
            H, sim, rp = hodge_index_at(det, roots)
            on_line = H <= 1e-9
            if not on_line:
                ordinate_independent = False
            print(f"    {q:>3d} {theta:>7.2f} {0.0:>5.1f} {abs(roots[0]):>10.4f} {det:>10.4f}"
                  f" {H:>+10.4f}  {on_line}")
        print()

    # ---- [4] CONTRAST: does the Euler edge det ALONE pin the flip?  Vary det at the even split s=0.
    print("=" * 100)
    print("[4] CONTRAST.  Vary the Euler edge det ITSELF (det = q, 4q, q/4) at the even split s = 0.")
    print("    H <= 0 (on-line) for EVERY det > 0 -- the flip is INSENSITIVE to the edge value; it")
    print("    only requires the EVEN split s = 0.  So 'supply det = q' does NOT supply the radius:")
    print("    the radius the flip needs is |alpha| = |beta| (the even split), for which det is blind.\n")
    print(f"    {'q':>3s} {'edge det':>10s} {'|alpha|':>10s} {'|beta|':>10s} {'H-index':>10s}  on-line?")
    edge_blind = True
    for q in QS[:3]:
        for det in [float(q), 4.0 * q, q / 4.0]:
            roots = split_pair(det, 0.0)        # even split, varying edge
            H, sim, rp = hodge_index_at(det, roots)
            on_line = H <= 1e-9
            if not on_line:
                edge_blind = False
            print(f"    {q:>3d} {det:>10.4f} {abs(roots[0]):>10.4f} {abs(roots[1]):>10.4f}"
                  f" {H:>+10.4f}  {on_line}")
        print()

    # ---- VERDICT ----
    print("=" * 100)
    print("VERDICT (P131.2):")
    print(f"  [2] flip tracks the EVEN SPLIT (s=0), edge held fixed   : COLLAPSE confirmed = {collapse_confirmed}")
    print(f"  [3] flip INDEPENDENT of the zero ordinate theta (s=0)   : ordinate-independent = {ordinate_independent}")
    print(f"  [4] flip INSENSITIVE to the Euler edge det value (s=0)  : edge-blind = {edge_blind}")
    print()
    if collapse_confirmed and ordinate_independent and edge_blind:
        verdict = "IMPORTED_ONLY"
        print("  flip_tracks = IMPORTED_ONLY.")
        print("  The weight-2 NS inertia flip tracks ONLY the even split |alpha| = |beta| = sqrt q")
        print("  (= |alpha| = sqrt q = RH), and is BLIND to the one zero-free Euler datum available")
        print("  (the determinant edge det = q, supplied free by cw_radius_assembly).  Deforming the")
        print("  radius independently of the planted zero ordinate (holding the Euler edge fixed)")
        print("  STILL flips the inertia at s != 0 -- the Euler-assembled radius does NOT drive the")
        print("  flip; only the imported |alpha| = sqrt q does.  This is doc 131 R-COLLAPSE / doc 130")
        print("  case (S) self-supply / failed E5': the radius is the answer and the Euler edge cannot")
        print("  fix it.  The construction CANNOT be made zero-free at the radius -- that is the finding.")
    else:
        verdict = "INCONCLUSIVE"
        print("  flip_tracks = INCONCLUSIVE (one of the three sub-tests did not hold as designed).")
    print()
    print("=" * 100)
    print("FREEZE / DOC-59 AUDIT:")
    print("  - radius candidate rho = sqrt(det), det = Satake determinant edge (Euler-borne, doc-59")
    print("    clean per cw_radius_assembly); split knob s is a FREE real parameter, NOT a zero ordinate.")
    print("  - sqrt q appears ONLY in the COMPARISON 'does the flip land at s=0' (doc-59 E4 comparison-")
    print("    only contact), never as construction input.  No zeta-zero data imported.")
    print(f"  - doc-130 tag: the flip eigenvalue (defect) is the acting plant's OWN modulus split,")
    print(f"    self-supplied; the Euler edge is flip-blind => case (S) / failed E5'.")
    return verdict


if __name__ == "__main__":
    report()
