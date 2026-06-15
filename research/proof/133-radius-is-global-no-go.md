# 133 - The radius is irreducibly global: the local route is automorphy-firewalled and the banked global suppliers are FE-blind

Status: characterization + no-go theorem, 2026-06-15. Third post-reset
cycle, synthesizing the two cycle-3 forks (Fork A: is the LOCAL even split
strictly weaker than RH or RH-equivalent? Fork B: does any BANKED GLOBAL
supplier fix the radius doing more than the functional equation?) against
adversarial verification (4 lenses; 2 evidentiary links refuted, 0 headline
verdicts overturned). This doc does NOT prove RH and does NOT produce a
strictly-weaker-than-RH lemma. It records, with a named mechanism, that the
radius (the even split = purity = |alpha| = sqrt q) is irreducibly GLOBAL
over Z, that the only local predicate that fixes it is the exact split (=
RH-for-f, firewalled by automorphy), and that the two banked global
suppliers do not do more than the functional equation. It extends doc 132
from "no banked per-prime carrier" to "no banked supplier, local or global,"
and converts the program to its two STRATEGY sec-7 frontiers.

Witnesses (re-ran this cycle, all exit 0, from repo root /home/jack/code/RH
as `python3 -m scripts.numerics.witness.<name>`):
`cw_radius_assembly` (EDGE Euler-free / RH-independent, SPLIT not supplied),
`cc_radius_deformation_probe` (flip_tracks = IMPORTED_ONLY -- but see the
SCOPING correction in sec 4: this is an F_q-lattice theorem, DH-domain-empty,
and does NOT bear on DH-blindness),
`ns_hodge_index_duality` (the weight-2 NS pairing, doc 130 escape realized),
`kahler_forcing` (the forcing factorization keystone),
`arakelov_signature` (max|A_zeta - A_DH| = 0.0 -- the ACTUAL carrier of the
CC-arm DH kill-test),
and the cycle-3 probe witnesses
`probe_pa_local_split_escape` (the eps-band is wider than the split but
radius-silent),
`rs_pole_radius_probe` (RS pole stays at the edge under the off-Ramanujan
plant; absolute-convergence abscissa moves to k-1+2delta = presupposes
Ramanujan),
`scaling_site_radius` (the scaling 1/2 is the DH-shared Haar/FE self-dual
axis; marked arithmetic q absent),
`dbn_flow_functional` (no Euler-borne flow functional is reality-monotone
under the dBN flow).

## 1. Purpose

Doc 132 proved that no banked PER-PRIME carrier supplies the Weil-operator
radius |alpha| = sqrt q over Z without RH, and left two surviving escapes
(sec 6): the M4r Euler-purity descent, and a GLOBAL / built-proper-object
supplier whose load-bearing input is not the per-prime modulus. Cycle 3
attacked both flanks of that residue:

  - Fork A asked whether the LOCAL even split is strictly weaker than
    RH-for-f (a sub-target) or RH-equivalent. Answer: RH-equivalent. The
    only weaker local predicate (a uniform eps-band) is radius-SILENT, and
    the operative firewall is AUTOMORPHY, not locality.

  - Fork B asked whether either BANKED global supplier (Rankin-Selberg pole
    at the edge; Connes-Consani integer RR + Pontryagin-Serre duality) does
    MORE than the functional equation at the radius. Answer: no -- both are
    FE-blind at the radius.

This doc reconciles the two, downgrades the one over-reach adversarial
verification caught (the "irreducibly Frobenius-WEIGHT datum over Z"
phrasing), repairs the two mis-attributed evidentiary links, and states the
surviving frontier and its kill conditions.

## 2. Covered Class

The no-go covers every BANKED proposal to fix the radius |alpha| = sqrt q
(= the even split = purity = the weight-2 NS Hodge-index positivity = RH),
in two layers:

```text
LOCAL layer (the per-prime even split):
  - the exact per-prime even split |alpha(p)| = |beta(p)| = p^{(k-1)/2};
  - any uniform per-prime eps-band |alpha(p)| in [p^{h-eps}, p^{h+eps}]
    with the determinant pinned (h = (k-1)/2), including the Kim-Sarnak
    subconvex band eps = 7/64 (a GENUINE local statement strictly weaker
    than RH-for-f);
  - the M4/M4r Euler/Satake supplier reading only local Euler-factor data.

GLOBAL layer (banked completed-product suppliers):
  - the Rankin-Selberg L(s, f x fbar) pole at the edge Re s = k-1;
  - the Connes-Consani integer Riemann-Roch + Pontryagin-Serre duality for
    compactified Spec Z (arXiv:2205.01391 Thm 1.1-1.2; 2306.00456 Thm 1.1),
    at CURVE level (genus 0, 1-dimensional base);
  - the two banked Z-FLOWS posed as Frobenius-analogues: the CC scaling-site
    R_{>0}^x action, and the de Bruijn-Newman heat flow (forcing Lambda<=0).
```

It does NOT cover (sec 6 surviving frontier): a GLOBAL completed-product
Rankin-Selberg / Eisenstein-at-the-pole construction that extracts the split
WITHOUT the absolute-convergence-past-the-edge presupposition and WITHOUT
the per-prime modulus; nor the intersection form of a GENUINELY-BUILT proper
self-product object (a CC C x C / scaling-site Jacobian over Z) carrying a
discrete Frobenius gap rather than the per-prime modulus. No banked witness
builds either; both stay unrefuted but unbuilt.

## 3. Lemma

```text
Lemma 133.1 (the radius is global, automorphy-firewalled, and the banked
global suppliers are FE-blind). Decompose the per-prime datum into its EDGE
(the Satake determinant |alpha(p) beta(p)| = p^{k-1}, the radius-SQUARED /
abscissa) and its SPLIT (the modulus equality |alpha(p)| = |beta(p)|, the
radius itself). Then:

  (A) [LOCAL, theorem-grade given automorphy] The EDGE assembles Euler-
      freely, RH-independently, uniformly across all primes, and survives
      the off-Ramanujan plant. The SPLIT is fixed by exactly one local
      predicate: the EXACT even split, which IS RH-for-f. Every strictly-
      weaker uniform eps-band is OFF-SPLIT-compatible hence RADIUS-SILENT
      (it confines |alpha| to a two-sided band but never to the centre).
      The firewall that makes "weaker band exists" non-vacuous yet
      non-radius-supplying is AUTOMORPHY: by Deligne (Ramanujan is a THEOREM
      for the holomorphic Hecke class) NO automorphic newform realizes a
      det-pinned off-split factor, so over the actual automorphic class the
      band and the exact split have the SAME truth value. Hence no local
      route: the local even split is RH-equivalent, not a sub-target.

  (B) [GLOBAL banked, no-go] Neither banked global supplier does more than
      the functional equation at the radius.
      (B1) Rankin-Selberg: the L(s, f x fbar) pole fixes only the EDGE
           (the determinant abscissa k-1); under the off-Ramanujan plant
           the pole stays at edge-exponent k-1 while the abscissa of
           ABSOLUTE convergence moves to k-1+2delta. "Simple pole at the
           edge AND series convergent to its right" is logically equivalent
           to absolute convergence past the edge = the Ramanujan/purity
           bound = the even split. So the RS pole PRESUPPOSES the split; it
           does not deliver it zero-free.
      (B2) Connes-Consani: the integer RR + Pontryagin-Serre duality is
           PROVEN and circularity-clean but at CURVE level (genus 0,
           1-dimensional base), supplying the symmetry/EDGE layer not the
           index-positivity/SPLIT. Its load-bearing positive piece -- the
           archimedean Kahler/Gamma_R form -- is byte-identical for zeta and
           the RH-FALSE Davenport-Heilbronn function (max|A_zeta-A_DH| = 0.0,
           arakelov_signature). FE-blind at the radius; the doc-21-sec-4
           standing kill-test fires.
      (B3) Both banked FLOWS reproduce only the FE/Haar self-dual axis
           Re s = 1/2 (DH-shared, the EDGE/symmetry) and carry NO discrete
           arithmetic gap: the scaling spectrum is a gapless continuum with
           no marked q; the dBN flow admits no reality-monotone Euler-borne
           functional. "Frobenius-analogue = the flow" is a FALSE ANALOGY at
           the radius: the flow supplies the edge, never the split.

  (C) [GLOBALITY over Z, theorem-grade] Over Z the per-prime purity carrier
      is EMPTY (M2d: numerator degree 1, one Satake parameter, |alpha(p)| =
      1 trivially per-prime). Therefore the radius is NOT a local modulus at
      all over Z -- it is a GLOBAL property of the completed product, with
      no F_q single-datum (one place, one Frobenius, edge=split) analogue.
```

Verdict label:

```text
RADIUS_IS_GLOBAL__LOCAL_ROUTE_AUTOMORPHY_FIREWALLED__BANKED_GLOBAL_FE_BLIND.
```

## 4. Proof

(A) LOCAL. cw_radius_assembly (exit 0): the determinant |alpha(p)beta(p)| =
p^{k-1} is uniform across primes 2..19 (match True every prime), Euler-borne,
and survives an off-Ramanujan PLANT at p=11 (delta=0.3): determinant
preserved at 285311670611, even split BROKEN (|alpha'| != |beta'|). So the
EDGE is free and the SPLIT is the residue. probe_pa_local_split_escape
(exit 0, SELFCHECK PASS): a uniform eps-band is strictly wider than the exact
split at a fixed prime (genuinely-wider-band True), and the band holds for
the off-Ramanujan plant at eps = 1/2 (RH-silent True) -- the band never
fixes the centre. The Kim-Sarnak bound |a(p)| <= 2 p^{(k-1)/2 + 7/64} is
exactly this band at eps = 7/64: a genuine LOCAL per-prime statement strictly
weaker than RH-for-f, yet a plant at delta = 7/64 is in-band, off-split, and
edge-preserved -- off-split-compatible hence radius-silent.

  [CORRECTED MECHANISM, per adversarial verification, lens weaker-lemma-is-RH]
  The probe first named the firewall "the LOCAL side has only EDGE and
  SPLIT_eq; everything genuinely weaker is GLOBAL," supported by a "second
  moment swap-invariant to <1e-25" selfcheck. That mechanism LEAKS: a uniform
  eps-band forces each second-moment contribution into [p^{-2eps}, p^{2eps}]
  term by term, so it is simultaneously a local predicate AND a two-sided
  global-mean bound -- the clean LOCAL/GLOBAL bifurcation fails (the probe's
  selfcheck was invariant only for band-VIOLATING swaps). The ACTUAL surviving
  firewall is AUTOMORPHY: the in-band off-split witnesses are exactly the
  det-pinned off-Ramanujan plants, and by Deligne NO holomorphic Hecke
  newform realizes them. Over the automorphic class the eps-band and the
  exact split have the SAME truth value; the band is "strictly weaker" only
  over a hypothetical non-automorphic class that automorphy already excludes.
  This makes the no-go CLEANER for the modular side (where Deligne supplies
  automorphy) and STRAINED for zeta (which lacks the per-prime automorphic
  carrier, M2d) -- exactly the surviving global gap.
  (Bookkeeping flag for the lead: probe_pa_local_split_escape's
  classification table mislabels subconvex/Kim-Sarnak as GLOBAL; it should
  read LOCAL-but-radius-silent. The verdict text already concedes weaker
  local bands are radius-silent, so the table is the only inconsistent
  surface -- a one-line relabel, not a verdict change.)

(B1) RS. rs_pole_radius_probe (exit 0; VERDICT_TAG = RS_POLE_EDGE_NOT_SPLIT__
FE_BLIND_AT_RADIUS__NO_GO; asserts enforce pole-stays-at-edge AND split-breaks
under the plant, so a forcing-shaped result would force exit 1): the pole
stays at edge-exponent k-1 = 11.0 under the off-Ramanujan plant while the
absolute-convergence abscissa moves to k-1+2delta = 11.6. DH has no Euler
product, so the RS local Satake product is UNDEFINED for DH (empty domain);
the only zeta-vs-DH shared piece is the FE/edge symmetry = RH-silent.

(B2) CC. arakelov_signature (exit 0): max|A_zeta - A_DH| = 0.0 -- the
archimedean Kahler/Gamma_R form (the dominating positive piece) is byte-
identical for zeta and the RH-FALSE DH function, with the only difference in
the finite/prime piece entering with a minus sign (dominated). This is the
doc-21-sec-4 standing kill-test firing on the CC arm.

  [SCOPING CORRECTION, per adversarial verification, lens FE-blindness-DH]
  The CC-arm DH-blindness is carried SOLELY by arakelov_signature. The
  witness cc_radius_deformation_probe (flip_tracks = IMPORTED_ONLY) must NOT
  be cited as evidence of DH-blindness: it constructs the inertia flip on a
  BORROWED genus-1 F_q Frobenius pair (alpha, beta) with det = q, where
  defect(s) = det*(2 cosh 2s - 2) >= 0 (= 0 iff s = 0) is the even split = a
  Deligne THEOREM on that lattice. DH has no Satake pair, so the flip
  construction has EMPTY DOMAIN for DH and is SILENT about zeta-vs-DH over Z.
  cc_radius_deformation_probe correctly shows the EDGE-blindness / self-supply
  (case S: the proper object fixes the radius-squared edge for free, the
  radius itself is the acting map's own modulus) -- that, and ONLY that, is
  what it licenses. A future builder citing it as if it discriminated zeta
  from DH over Z would be importing RH-for-the-curve and mistaking it for
  progress (the doc-22 "CC departs at the square joint" trap).

(B3) FLOWS. scaling_site_radius (exit 0): the CC scaling site carries a
genuine R_{>0}^x action (theta = t d/dt) and marks Re s = 1/2, but that
radius is the self-dual point of multiplicative Haar / the FE reflection
s <-> 1-s, which DH SHARES (DH has a functional equation, hence the same
self-dual 1/2, with no Euler product); marked_arithmetic_q_exists = False,
the archimedean spectrum is a gapless continuum, and the off-line set returns
all_on_axis = False (the structure does NOT exclude off-line zeros). The CC
spectral realization makes RH = "the scaling spectrum lies on the self-dual
axis," which is EQUIVALENT to RH, not a forcing of it. schmid_sl2_orbit_radius
(exit 0): Schmid's SL(2)-orbit N gives (N1)-(N3) + the weight parity (-1)^w
(free, DH-shared) but NOT (N4) the radius; over F_q the radius q^{w/2} comes
from the EXTRA l-adic/crystalline Frobenius, not from N. dbn_flow_functional
(exit 0): no Euler-borne flow functional is reality-monotone under the dBN
flow (the modulus reading is sign(Im)-blind; the signed reading is annihilated
by FE conjugation) -- the same wall on the dynamical side. kahler_forcing
(exit 0): the forcing "Kahler => P_inf >= 0 => RH" factors into E (cup
product: geometric, zero-free, DH-shared, INDEFINITE alone -- Rosati signature
(2g,0,2g)), C_W (the radius: over F_q literally |alpha| = sqrt q = RH), and a
formal Hodge-Riemann implication. The entire Euler/RH content sits in C_W's
radius; E forces nothing.

(C) GLOBALITY. M2d (doc 132): over Z the L-numerator has degree 1, one Satake
parameter, |alpha(p)| = 1 trivially per-prime -- the per-prime purity carrier
is empty. So over Z the radius cannot be a local modulus; it is a global
completed-product invariant. doc 18 C6 / doc 21 sec 4: the affine Spec Z
square has no Frobenius (ring maps HZ -> HZ trivial) and an untruncated Ext
tower; the F_q single-datum identity (edge = split in one eigenvalue's
modulus) has no Z analogue.

## 5. The linkage, honestly tagged (theorem vs analogy)

The cycle-3 ground claimed: Fork A (local radius) REDUCES TO Fork B (global
Frobenius-weight datum / a flow), and "Frobenius-analogue = the flow." This
doc tags each link:

```text
[THEOREM, FF side] Where the even split is PROVEN it goes through a global
  proper object carrying Frobenius-with-weights (Deligne / Weil II:
  Ramanujan-Petersson via the proper smooth Kuga-Sato variety). Verified at
  witness level (kahler_forcing C_W; cw_radius_assembly FF row).

[CATALOG-EXHAUSTION, not a metatheorem] Among the 5 STRATEGY-sec-1 forcing
  templates only the cohomological one is PROVEN to deliver purity. This is a
  survey of known mechanisms, NOT a proof that no other can exist.

[FALSE ANALOGY, refuted as a radius-supplier] "Frobenius-analogue = the
  banked flow (scaling site / dBN)." Both flows reproduce only the FE/Haar
  self-dual axis (the EDGE, DH-shared) and carry no discrete arithmetic gap q
  (the SPLIT). Refuted by scaling_site_radius + dbn_flow_functional. The
  ground's "Fork A => Fork B => build the flow" is a difficulty-CONSERVATION
  reduction, not a constructive route.

[DOWNGRADED to UNKNOWN, per adversarial verification, lens false-FF-analogy]
  "The radius is irreducibly a global Frobenius-WEIGHT datum [over Z]" is NOT
  type-correct: over Z there is no Frobenius whose weight it could be (affine
  square, untruncated tower, doc 18 C6). The witnesses establish only the
  NEGATIVE -- the banked flows do NOT carry q. From "no banked flow supplies
  q" one may NOT conclude "the radius IS necessarily a Frobenius-weight
  datum"; that affirms the FF template by exclusion over a non-exhaustive
  catalog. A purity-by-construction mechanism (Hilbert-Polya self-adjoint;
  global RS without the absolute-convergence presupposition) would make the
  split hold with NO q, falsifying the "irreducibly Frobenius-weight"
  identification. STATUS of that identification: UNKNOWN, not established.
  What survives certification over Z is the WEAKER, theorem-grade
  characterization: the radius is irreducibly GLOBAL over Z (M2d), and the
  banked local + banked global suppliers do not fix it without RH.
```

Net linkage status: PLAUSIBLE BUT ANALOGY. The forward (FF-side) half is
theorem-grade; the transplant to Z is analogy, not a Z-side theorem. The
honest, certified Z statement is the globality + the banked no-go, NOT the
Frobenius-weight necessity.

## 6. Surviving Escape

A candidate escapes Lemma 133.1 only by supplying the radius from a zero-free
invariant that is NOT the per-prime Satake modulus, NOT the FE-shared
archimedean positivity, and NOT keyed to the absolute-convergence-past-the-
edge presupposition:

```text
M4r (the Euler-purity descent). A zero-free proof that the assembled
    per-prime determinant edge p^{k-1} splits EVENLY at every prime WITHOUT
    importing the modulus, the automorphy class, or the F_q single-datum
    identity. Named, attackable, zero-free, RH-EQUIVALENT (the even split IS
    RH-for-f; relocates, does not dissolve, the wall).

A GLOBAL non-modulus constraint. The radius fixed by a completed-product
    invariant -- Rankin-Selberg / Eisenstein at the pole extracting the split
    WITHOUT the absolute-convergence presupposition, OR the intersection form
    of a GENUINELY-BUILT proper self-product (Connes-Consani C x C /
    scaling-site Jacobian) carrying a DISCRETE Frobenius gap not the per-prime
    modulus, OR forcing Lambda <= 0 (dBN) by a generator that carries primes
    non-passively. Over Z the per-prime carrier is empty (M2d), so this is
    where any new structure must live. No banked witness realizes any route;
    all stay unrefuted but unbuilt.

A non-Frobenius purity mechanism (the downgrade's residue). A self-adjoint /
    Hilbert-Polya construction that is purity-by-construction, carrying NO q.
    UNKNOWN, not excluded -- "UNKNOWN cuts both ways" and supplies no
    construction; but it is what forbids the "irreducibly Frobenius-weight"
    necessity claim.
```

## 7. Kill Conditions

A future radius proposal is killed by this no-go when:

```text
KILL-RAD133.1 self-supplied split (the doc-130 case S, at the SPLIT)
  the supplier delivers the determinant edge p^{k-1} Euler-freely but the
  even split |alpha| = |beta| is the acting map's own modulus (the off-
  Ramanujan plant preserves the edge and breaks the split).
  Witness: cw_radius_assembly, cc_radius_deformation_probe (flip_tracks =
  IMPORTED_ONLY -- cite ONLY for edge-blindness / self-supply, NEVER for
  DH-blindness; its F_q-lattice domain is empty for DH).

KILL-RAD133.2 weaker-band-but-radius-silent / automorphy-firewalled
  the supplier offers a uniform per-prime eps-band (incl. Kim-Sarnak
  subconvexity); it is off-split-compatible hence radius-silent, and over
  the automorphic class it has the same truth value as the exact split (=RH).
  Witness: probe_pa_local_split_escape (genuinely-wider-band True,
  RH-silent True).

KILL-RAD133.3 FE-blind global supplier (does not exceed the functional eq.)
  the supplier fixes only the EDGE / FE self-dual axis (RS pole at the edge
  presupposing Ramanujan; CC archimedean Kahler form DH-shared; the scaling
  1/2 = Haar self-dual point). Witness: rs_pole_radius_probe (VERDICT_TAG =
  RS_POLE_EDGE_NOT_SPLIT__FE_BLIND_AT_RADIUS__NO_GO), arakelov_signature
  (max|A_zeta - A_DH| = 0.0), scaling_site_radius (marked q absent),
  dbn_flow_functional.

KILL-RAD133.4 false-flow-analogy / decorative Frobenius-weight framing
  the supplier asserts a banked Z-flow IS the Frobenius-analogue, or that the
  radius is "necessarily a Frobenius-weight datum over Z." The first is a
  false analogy (flow = edge, never split); the second is type-incorrect
  (no Frobenius over Z) and rests on a non-exhaustive catalog. Witness:
  scaling_site_radius, schmid_sl2_orbit_radius (parity not radius).
```

Do not apply this no-go to a proposal carrying a GLOBAL completed-product /
built-proper-object radius supplier whose load-bearing input is NOT the
per-prime modulus and NOT the absolute-convergence presupposition (sec 6) --
that is the surviving frontier, not a kill.

## 8. Board

```text
Radius wall (the weight-2 even split), cycle 3:
  RADIUS_IS_GLOBAL__LOCAL_ROUTE_AUTOMORPHY_FIREWALLED__BANKED_GLOBAL_FE_BLIND.
  LOCAL: the only local predicate that fixes the radius is the exact even
  split = RH-for-f; every weaker band is radius-silent and automorphy-
  firewalled (corrected from "off-split-compatible / LOCAL-GLOBAL firewall").
  GLOBAL (banked): RS at the edge presupposes Ramanujan; CC's archimedean
  positivity is DH-shared (arakelov_signature, the SOLE DH-kill carrier);
  both flows reproduce only the FE self-dual axis.
  Witnesses cw_radius_assembly + cc_radius_deformation_probe (edge/self-supply
  ONLY) + arakelov_signature + rs_pole_radius_probe + scaling_site_radius +
  dbn_flow_functional + kahler_forcing.

Doc 132 extension:
  doc 132 closed the banked PER-PRIME suppliers; doc 133 closes the banked
  GLOBAL suppliers (RS-at-edge, CC curve-level RR+PS, both flows) and the
  weaker-local-band sub-target. No banked supplier, local or global, fixes
  the radius without RH.

Downgrade landed (adversarial verification):
  "radius is irreducibly a Frobenius-WEIGHT datum over Z" -> UNKNOWN /
  decorative FF-analogy. Certified Z statement: the radius is irreducibly
  GLOBAL over Z (M2d). Two evidentiary links repaired: cc_radius_deformation_
  probe does NOT bear on DH-blindness (F_q-domain empty for DH); the PA
  firewall is AUTOMORPHY, not LOCAL/GLOBAL.

Surviving frontier (the only escapes):
  M4r Euler-purity descent (zero-free, RH-equivalent, attackable) OR a GLOBAL
  non-modulus / built-proper-object supplier (CC C x C, scaling-site Jacobian,
  dBN Lambda <= 0) OR a non-Frobenius purity mechanism (UNKNOWN). All
  unrefuted AND unbuilt.

Next valid work:
  attack the M4r even-split lemma directly OR decide whether a GLOBAL RS /
  Eisenstein construction can extract the split WITHOUT the absolute-
  convergence-past-the-edge presupposition; do NOT re-sweep the banked
  per-prime OR banked global suppliers (each is killed by KILL-RAD133.1-4),
  and do NOT cite cc_radius_deformation_probe as a DH discriminator.
```
