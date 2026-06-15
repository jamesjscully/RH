# 132 - The radius-circularity no-go (the weight-2 proper object cannot supply its own radius)

Status: no-go theorem, 2026-06-15. Second post-reset cycle, executing
the pre-registration of doc 131 (the Weil-operator radius: Euler-assembled
or RH-circular?). Fail-closed reading R-COLLAPSE, the pre-registered and
expected full-value outcome. This doc extends doc 130 (the second-evaluation
properness no-go) from the affine banked class to the one banked PROPER
realization of doc 130's surviving escape: the weight-2 Neron-Severi
Hodge-index duality on the self-product surface. It records that even a
genuine properness / Poincare-Hodge-Riemann duality truncation cannot
supply the one scale that makes its index positive -- the Weil-operator
radius |alpha| = sqrt q.

Witnesses (lead-reran this cycle, all exit 0):
`cw_radius_assembly` (the M4 Euler/Satake supplier),
`cc_radius_deformation_probe` (flip_tracks = IMPORTED_ONLY),
`ns_hodge_index_duality` (the weight-2 NS pairing, doc 130 escape realized),
`kahler_forcing` (the forcing factorization keystone).

## 1. Purpose

Doc 130 proved that no carrier in the banked NON-PROPER class supplies an
unforced, zero-seeing odd slot, and located the surviving escape at E4'/E5':
a genuine S-level duality truncation whose odd-slot eigenvalues are
carrier-fixed BEFORE the acting correspondence is chosen. Doc 131 banked the
one realization of that escape at weight 2 (the NS Hodge-index duality,
`ns_hodge_index_duality`: a non-congruence pairing P_NS = canonical
evaluation of the duality D, D o D = id, NOT a metric, whose inertia FLIPS
iff a root leaves |alpha| = sqrt q) and reduced E5' to a single open factor:
the carrier-fixedness of the eigenvalue MODULUS, i.e. the radius |alpha| =
sqrt q.

This doc proves, with a named mechanism, that the radius is NOT carrier-fixed
by any banked supplier over Z: it is either self-supplied (the acting map's
own modulus) or absent. Hence E5' FAILS even for the proper object. Doc 130
extends to weight 2.

## 2. Covered Class

The no-go covers any proposal to supply the Weil-operator radius |alpha| =
sqrt q (equivalently: the weight-1 purity / even split of the per-prime
weight, the scale making the weight-2 NS Hodge index negative-definite on
primitives = c = D = the Hodge-Riemann polarization = RH) over Z from a
banked geometric/arithmetic source:

```text
- the Euler/Satake prime-product assembly (M4/M4r; the ku-face prime-power
  comb of doc 42, the best banked supply carrier);
- the Arakelov / positive-Green-form arithmetic Hodge-index signature;
- the polarization relation F.F^dag = c.Id (the unitary functional equation);
- the oriented / archimedean Hodge pairing (signed weight P_10^* A P_10 -
  P_01^* A P_01);
- the vdGS theta count / strict-square h^0 (the Epstein effectivity face);
- the kahler_forcing keystone pair (E cup product, C_W Weil operator).
```

It does NOT cover a supplier that fixes the radius from a zero-free invariant
not equal to the per-prime modulus -- specifically, a GLOBAL completed-product
constraint (Rankin-Selberg / Eisenstein at the pole) or the intersection form
of the as-yet-unbuilt proper self-product object, neither of which any banked
witness realizes (sec 6).

## 3. Lemma

```text
Lemma 132.1 (radius-circularity: no carrier-fixed radius without RH).
Let a candidate supply the weight-2 NS Hodge-index positivity (c = D) by
fixing the Weil-operator radius |alpha| = sqrt q over Z from a source in
the covered class. Decompose the per-prime datum into its EDGE (the
Satake determinant |alpha(p) beta(p)| = p^{k-1}, the radius-SQUARED /
abscissa) and its SPLIT (the modulus equality |alpha(p)| = |beta(p)| =
p^{(k-1)/2}, the radius itself). Then exactly one of the following holds,
and each fails doc-130 E5' / doc-65 E5:

  (S) Self-supplied split. The supplier delivers the EDGE Euler-freely and
      RH-independently (determinant = integer constant term, uniform across
      all primes, split-invariant), but the SPLIT is the acting map's own
      modulus -- the carrier supplies the SQUARE, not the SQUARE-ROOT. The
      even split is not carrier-fixed before the action; it IS the answer
      (= purity = RH-for-f). [doc 130 case S; doc 65 sec 6; E5' fails.]

  (C) Sylvester-locked / FE-shared. The supplier is a *-congruence of an
      FE-shared archimedean form, or the unitary functional equation
      F.F^dag = c.Id. Its inertia / relation is RH-silent (holds verbatim
      for the RH-FALSE Davenport-Heilbronn function); the radius POSITIVITY
      (phase reality m real on Re s = 1/2 / the Weil positivity) is INPUT =
      RH. [doc 130 case C; doc 59 F2; the radius is imported as positivity.]

  (E) Absent radius. The supplier has no per-prime Euler-product carrier
      address for the radius at all (the Epstein x^2+5y^2 replacement kills
      the carrier while the theta/count shadow survives), or its inertia is
      locked to a DH-shared background that does not see the modulus. There
      is no radius datum to fix. [doc 130 case E; doc 64; the radius is not
      addressable.]

Hence no banked carrier supplies the radius |alpha| = sqrt q from zero-free
data. The radius is self-supplied (= RH), imported as positivity (= RH), or
absent.
```

Verdict label:

```text
REJECT_SELF_SUPPLIED_RADIUS_AT_THE_EVEN_SPLIT.
```

## 4. Proof

(S) is the content of `cw_radius_assembly` and `cc_radius_deformation_probe`
(both lead-reran, exit 0). The M4 Euler/Satake assembly reads only local
Hecke eigenvalues (Euler-factor coefficients) by exact arithmetic. The
per-prime EDGE = the determinant of the Satake matrix |alpha(p) beta(p)| =
p^{k-1} is the integer constant term: verified uniform (gamma = k-1 = 11
match=True for all primes 2..19) and SPLIT-INVARIANT (identical at split
parameter delta = 0, 0.3, 1.5). The off-Ramanujan plant at p=11 (delta=0.3)
PRESERVES the edge (11^11 = 285311670611) and BREAKS the even split
(|alpha'| = 1096674 != |beta'| = 260160). So the supplier provably delivers
the radius-SQUARED edge Euler-freely and RH-independently, but the even split
|alpha| = |beta| is independent content. `cc_radius_deformation_probe`
coordinatizes the g=1 Frobenius pair by (Euler edge det, free split knob s)
and confirms the weight-2 NS Hodge index H = -Tr(F_0 F_0^dag) is on-line
(H <= 0) ONLY at s = 0, EDGE-BLIND (H <= 0 for det = q, 4q, q/4 at s = 0),
and ORDINATE-INDEPENDENT: the inertia flip tracks ONLY the even split s = 0
= |alpha| = sqrt q = RH (flip_tracks = IMPORTED_ONLY). Bypassing the
parametrization and feeding raw uneven-modulus roots into the pairing,
H = -(Sum|alpha|^2 - 2 det) <= 0 IFF |alpha| = |beta| by AM-GM with the
product pinned at det: the even split = on-line locus is a DERIVED inequality
of the trace pairing, not a coordinate artifact, and not a hand-set unit
(the radius base det may be anything; the verdict does not depend on its
value -- no zero-slack unit-insertion). The even split is the acting map's
own modulus: carrier-unforced, doc 130 case S, doc 65 sec 6 self-supply.

(C) is `polarization_relation` and `ns_hodge_index_duality` /
`oriented_hodge_pairing` (lead-reran where load-bearing). The relation
m(s) m(1-s) = c is the unitary functional equation; it holds UNCONDITIONALLY
and -- the decisive kill-test -- holds verbatim for the RH-FALSE
Davenport-Heilbronn function (m_DH(s) m_DH(1-s) = 1 at t = 3, 10, 85.699,
including near the off-line DH zero), so the relation is RH-SILENT. The
radius content is the POSITIVITY dag = * (|m| = 1 on the line, m real on
Re s = 1/2): selecting the phase reality that places the resonance on the
line is the critical-line statement (doc 59 F2 sign/phase import). The NS
pairing's building blocks E, D, rosati are q-INDEPENDENT (E = [[0,1],[-1,0]]);
the cup product / E ALONE is INDEFINITE (Rosati signature (2,0,2)/(8,0,8)/
(18,0,18) at g = 1,2,3), so the congruence form cannot detect the radius --
Sylvester locks its inertia to the FE-shared background. The radius enters
only as positivity = RH input.

(E) is doc 64 + `oriented_hodge_pairing`. The vdGS theta / strict-square
face dies at effectivity: replacing the prime-power valuation tower by the
represented-norm data of Q = x^2 + 5y^2 (represents 1,4,6,9,36 with 2,3
absent and 36 = 4*9 = 6*6 destroying unique atom factorization) leaves the
theta/count/Poisson shadow ALIVE but the Euler-product carrier ADDRESS
UNDEFINED -- the radius is carrier-blind, not importable. `oriented_hodge_
pairing` collapses to Q = -i.omega (certified ||.|| = 5.0e-15) with inertia
(4,4,0) locked to a DH-shared FE background (max|A_zeta - A_DH| = 0.0); REAL
and complex-oriented (steelman e^{i gamma u}) plants give no inertia flip
on-line vs off-line, no +/-gamma distinction. The radius is absent from the
inertia.

The three cases are exhaustive for the covered class: a presented radius
supplier either self-supplies the split (S), is a Sylvester-locked /
FE-shared form importing positivity (C), or has no carrier address for the
radius (E). Each fails E5'. []

NOTE ON THE MECHANISM (the precise kill, recorded honestly). The M4 supplier
imports NO zero ordinate: it reads only Euler-factor data by exact
arithmetic; sqrt q / p^{(k-1)/2} appear only in COMPARISON (doc 59 E4-allowed)
and the off-Ramanujan case is a negative-control PLANT (doc 59 A3), with the
freeze protocol honored (no zeta-zero data builds the radius). The kill is
therefore doc 130 case S (self-supply / RH-EQUIVALENCE), which is ZERO-FREE-
BUT-UNSOLVED -- NOT doc-59 forbidden F1 (zero/spectral import). The earlier
audit's grounding of the M4 kill in "F1 import" is corrected here: the radius
is not imported, it is the acting map's own modulus, and supplying it is
RH-equivalent. Doc 131's pre-registered R-COLLAPSE definition (lines 114-120)
deliberately bundles "doc 59 circular / doc 130 case S" together; the COLLAPSE
outcome fires under that reading, and the zero-free-but-RH-equivalent residue
(case S) is carried forward in sec 6 as the surviving frontier.

## 5. Program Consequence

```text
1. Doc 130 EXTENDS to the weight-2 proper object. Even a genuine
   Poincare-Hodge-Riemann duality truncation (the NS Hodge-index pairing,
   the one banked realization of doc 130's E4'/E5' escape) cannot supply its
   own radius: it fixes the radius-SQUARED edge for free but the radius
   itself (the even split) is self-supplied = RH. The properness escape of
   doc 130 is real at the EDGE and empty at the SPLIT.

2. Doc-45 clause E / BC-E3' is now closed even against the proper object,
   at the radius. The forcing Kahler => P_inf >= 0 => RH factors (E cup
   product free/indefinite-alone; Hodge-Riemann implication formal; the
   entire Euler content in C_W's radius), and the radius is the irreducible
   residue: it is RH put in by hand over F_q (a single-datum tautology:
   one place, one Frobenius, edge and split coincide in one eigenvalue's
   modulus) and self-supplied / RH-equivalent over Z.

3. The wall relocates to the EULER RADIUS ASSEMBLY itself = M4 = the even
   split / purity square-root, or to forcing Lambda <= 0 (de Bruijn-Newman).
   These are the two genuine open frontiers (STRATEGY sec 7); the no-go map
   gains its sharpest entry here.
```

## 6. Surviving Escape

A candidate escapes Lemma 132.1 only by supplying the radius from a zero-free
invariant that is NOT the per-prime Satake modulus and NOT the FE-shared
archimedean positivity:

```text
M4r (the Euler-purity descent). A zero-free proof that the assembled
    per-prime determinant edge p^{k-1} splits EVENLY into two equal moduli
    at every prime -- the purity square-root step -- WITHOUT importing the
    modulus and without the F_q single-datum identity. This is a named,
    attackable, zero-free open lemma (it passes doc 59 E1/E3: the supplier
    reads only local Euler-factor data). It is NOT strictly weaker than RH
    (the even split IS RH-for-f, a theorem for Delta via Deligne, the open
    statement for zeta), so it RELOCATES rather than dissolves the wall.

A GLOBAL constraint. The radius fixed by a completed-product invariant
    (Rankin-Selberg / Eisenstein at the pole) or by the intersection form
    of the genuinely-built proper self-product object (Connes-Consani C x C
    / scaling site), whose load-bearing input is NOT the per-prime modulus.
    Over Z the per-prime purity carrier is empty (M2d: numerator degree 1,
    one Satake parameter, |alpha(p)| = 1 trivially), so the radius is a
    GLOBAL property of the completed product, not any local modulus -- which
    is exactly why the F_q single-datum tautology has no Z analogue, and
    where a new structure could in principle live. No banked witness
    realizes either route; both stay unrefuted but unbuilt.
```

Equivalently: the radius needs an independent second/spectral evaluation
that the ku-face comb's every-entry-one-evaluation supply provably lacks
(doc 42 residue). That evaluation is the frontier; this no-go converts
"we have not supplied the radius" into "the radius cannot be carrier-fixed
by any banked supplier without RH."

## 7. Kill Conditions

A future radius proposal is killed by this no-go when:

```text
KILL-RAD.1 self-supplied split
  the supplier delivers the determinant edge p^{k-1} Euler-freely but the
  even split |alpha| = |beta| is the acting map's own modulus (the off-
  Ramanujan / off-split plant preserves the edge and breaks the split).
  Witness: cw_radius_assembly, cc_radius_deformation_probe (flip_tracks =
  IMPORTED_ONLY).

KILL-RAD.2 FE-shared / Sylvester-locked positivity
  the radius enters only as the unitary FE (RH-silent, holds for DH) or as
  a *-congruence positivity / phase reality (m real on Re s = 1/2) = RH
  input. Witness: polarization_relation, oriented_hodge_pairing,
  ns_hodge_index_duality (E q-independent, indefinite alone).

KILL-RAD.3 absent carrier address
  the supplier has no per-prime Euler-product carrier for the radius (dies
  under the Epstein x^2+5y^2 replacement while the theta/count shadow
  survives), or its inertia is locked to a DH-shared FE background.
  Witness: doc 64, oriented_hodge_pairing (max|A_zeta - A_DH| = 0.0).
```

Do not apply this no-go to a proposal carrying a GLOBAL completed-product
or built-proper-object radius supplier whose load-bearing input is NOT the
per-prime Satake modulus (sec 6) -- that is the surviving frontier, not a
kill.

## 8. Board

```text
Radius wall (the weight-2 even split):
  REJECT_SELF_SUPPLIED_RADIUS_AT_THE_EVEN_SPLIT for every banked supplier;
  unified mechanism (self-supplied split [case S] + Sylvester-locked /
  FE-shared positivity [case C] + absent carrier address [case E]);
  witnesses cw_radius_assembly + cc_radius_deformation_probe
  (flip_tracks = IMPORTED_ONLY), polarization_relation (RH-silent FE),
  kahler_forcing (radius = the irreducible residue).

Doc 130 extension:
  the weight-2 proper object (NS Hodge-index duality) realizes E4'/E5' at
  the EDGE but cannot fix its own radius at the SPLIT; doc-45 clause E is
  closed even against the proper object, at the radius.

Surviving frontier (the only escape):
  M4r Euler-purity descent (a zero-free, RH-equivalent, attackable open
  lemma) OR a GLOBAL / built-proper-object radius supplier (Connes-Consani
  C x C, forcing Lambda <= 0). Per-prime purity carrier empty over Z (M2d):
  the radius is global, with no F_q single-datum analogue.

Next valid work:
  attack the M4r even-split lemma directly OR build the global/proper
  radius supplier with a runnable witness; do NOT re-sweep the banked
  per-prime suppliers (each is killed by KILL-RAD.1/2/3).
```
