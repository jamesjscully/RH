# 176 - Symplectic buildings are dualizing representations, not boundary glue

Status: no-go + symplectic building/Steinberg repair deletion, 2026-06-20.
Thirty-ninth cycle of the doc-137 construction arc. Doc 175 killed
classifying-space, group-cohomology, and Tate-cohomology packages of the
support Sp stabilizers. This document tests the next repair: use the
spherical Tits building of the finite symplectic stabilizer, or its top
reduced homology / Steinberg module, as the dualizing object or Laurent
boundary line.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_building_steinberg_no_go` (SBT1-SBT13 ALL PASS)
-- exact finite-window stabilizer, building-degree, chamber-count,
Steinberg-dimension, graph/type, endpoint, idempotent, twist, obstruction,
and control-formability checks.

## 1. Purpose

After doc 175, the support-symplectic repair can say:

```text
finite stabilizer cohomology is not periodic;
use the Tits building of the residual Sp stabilizer instead;
its top reduced homology is the Steinberg module, a dualizing object;
read the top class / apartment / chamber as the missing boundary line.
```

This is distinct from doc 175. The tested object is not group cohomology of
the stabilizer but its building and Steinberg module. The repair is
tempting because the building top degrees in the tested windows are:

```text
1,2,4,8,
```

which match the finite support cutoffs. But this match is only a
finite-window shadow. It does not construct a shift map or Laurent
generator. The Steinberg module itself is a large representation, not a
rank-one boundary line, and selecting a chamber, apartment, or top vector is
another support choice.

This document is local. It does not reject carrier-native buildings,
dualizing modules, or Steinberg-type data. It rejects only the Tits building
of the visible finite support Sp stabilizer as the R1 Laurent carrier.

## 2. Lemma

```text
Lemma 176.1 (support Sp buildings do not supply boundary glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The full-frame stabilizer is trivial:

  1,1,1,1.

So the full-frame stabilizer has no nontrivial building or Steinberg
dualizing module.

The ordered first-pair stabilizers are Sp(2m,F_2) for:

  m = 2,3,5,9.

Their orders are:

  720,
  1451520,
  24815256521932800,
  2060902435720151186326095525680721766346957783040000.

The spherical buildings of type C_m have top reduced homology in degrees:

  m-1 = 1,2,4,8.

These degrees equal the tested finite cutoffs N, but this equality supplies
no adjacent shift map, no inverse shift, no Laurent generator, and no
boundary glue.

The chamber counts are:

  45,
  2835,
  739552275,
  852369269595510700600441875.

The Steinberg module dimensions are:

  16,
  512,
  33554432,
  2417851639229258349412352.

Thus the top homology is not a rank-one line in any tested window. A chamber,
apartment, or top vector must still be chosen before a line is visible.

The building/Steinberg package constructs no DMP multiplication, no
carrier-native building, no carrier-native endpoint, no carrier-native
boundary glue, no pinned Laurent twist, and no torsor splitter. The graph,
endpoint/matching, idempotent, and Laurent-twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same building/Steinberg
package is formable on controls.

Therefore support Sp-building/Steinberg data is not construction-grade R1
carrier duality or boundary glue. A surviving route must construct the
building/dualizing data, endpoint, boundary map, Laurent twist, and torsor
splitter as carrier-native correspondence data and prove DH/Epstein death at
that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_BUILDING_STEINBERG__DUALIZING_REPRESENTATION_NOT_BOUNDARY_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_building_steinberg_no_go` verifies the
finite-window model.

SBT1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SBT2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SBT3 records that the full-frame stabilizer is trivial:

```text
1,1,1,1.
```

So it has no nontrivial building.

SBT4 records the first-pair stabilizers. They are finite `Sp(2m,F_2)`
groups with:

```text
m = 2,3,5,9.
```

and orders:

```text
720,
1451520,
24815256521932800,
2060902435720151186326095525680721766346957783040000.
```

SBT5 records the building top degrees:

```text
1,2,4,8.
```

They track the finite window cutoffs but construct no shift map. A degree
coincidence is not a Laurent generator.

SBT6 records the chamber counts:

```text
45,
2835,
739552275,
852369269595510700600441875.
```

Choosing a chamber is substantial support data.

SBT7 records the Steinberg module dimensions:

```text
16,
512,
33554432,
2417851639229258349412352.
```

These dimensions are all greater than one, so the Steinberg modules are not
rank-one Laurent lines.

SBT8 records that choosing an apartment or top vector is another support
choice and that the carrier has supplied no building.

SBT9 records that Steinberg data does not construct the boundary map,
Laurent generator, or torsor splitter.

SBT10 records that the graph, endpoint, matching, idempotent, and twist
choices remain:

```text
graph choices = 64,1024,2097152,36028797018963968;
endpoint pairs = 9,16,36,100;
half matchings = 6,24,720,3628800;
rank-one idempotents = 2016,32640,8386560,549755289600;
Laurent twists = 3,5,9,17.
```

SBT11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SBT12 applies the carrier guard: finite symplectic buildings and Steinberg
modules of support stabilizers are support operations, so controls can form
the same package. SBT13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-176:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144);
    - formally adjoining a torsor splitter b with phi(b)=b*c^-1 (doc 145);
    - quotienting a free/tensor Laurent repair to one line (doc 146);
    - shift-coinvariant collapse of the tensor copies to one line (doc 147);
    - shift telescope/direct-limit packaging of that collapse (doc 148);
    - formal shift-operator insertion as the missing carrier shift (doc 149);
    - support-module End envelope as the missing correspondence algebra
      (doc 150);
    - Morita/idempotent corner of the support End envelope as the selected
      carrier line (doc 151);
    - trace/minimality selection of that idempotent (doc 152);
    - conjugacy-invariant or symmetrized selection of that idempotent
      (doc 153);
    - support-degree flag/Borel reduction as the canonical idempotent
      selector (doc 154);
    - support-chain incidence/path algebra as the carrier correspondence
      algebra (doc 155);
    - groupoid completion / formal inversion of support-chain arrows as the
      carrier correspondence algebra (doc 156);
    - stabilizer/Laurent-loop decoration of the support groupoid as carrier
      isotropy (doc 157);
    - unit-labeled support-chain connections as carrier holonomy (doc 158);
    - support-filtration Rees parameter as carrier shift/deformation
      (doc 159);
    - support/Rees-derived nilpotent, unipotent, or Euler operator as carrier
      monodromy (doc 160);
    - support filtered extension/unipotent gluing as carrier correspondence
      (doc 161);
    - support derived/Yoneda/Massey/A_infinity gluing as carrier
      correspondence (doc 162);
    - pro/infinite completion of the visible one-sided support chain as
      carrier orbit (doc 163);
    - Tate/continuous-dual completion of the visible support as carrier orbit
      (doc 164);
    - support evaluation/coevaluation as automatic Tate boundary glue
      (doc 165);
    - support hyperbolic form/swap as automatic Tate boundary glue (doc 166);
    - support Lagrangian/polarization as carrier half-identification
      (doc 167);
    - support opposite/transverse Lagrangian graph as carrier
      half-identification or boundary glue (doc 168);
    - boundary corner/minor/determinant/cofactor/Schur extraction from the
      support opposite graph as carrier boundary glue (doc 169);
    - determinant-one/orientation normalization of the support opposite graph
      as carrier endpoint, boundary glue, or Laurent twist (doc 170);
    - quadratic refinement, Arf invariant, or Maslov/triple-Lagrangian scalar
      of the support hyperbolic package as carrier boundary glue (doc 171);
    - Darboux/symplectic-frame selection of the support hyperbolic package as
      carrier endpoint, half-identification, or boundary glue (doc 172);
    - Sp-quotient/orbit averaging of the support Darboux-frame package as
      carrier endpoint, boundary glue, or Laurent twist (doc 173);
    - quotient-stack/stabilizer isotropy of the support Darboux-frame package
      as carrier endpoint, loop, boundary glue, or Laurent twist (doc 174);
    - classifying-space/group/Tate cohomology of the support symplectic
      stabilizers as carrier endpoint, Laurent line, boundary glue, or
      torsor splitter (doc 175);
    - Tits-building/Steinberg dualizing data of the support symplectic
      stabilizers as carrier endpoint, Laurent line, boundary glue, or
      torsor splitter (doc 176).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building descent data,
      quadratic refinement or Maslov datum, orientation, half-identification,
      boundary endpoint, and Laurent twist/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Building/Steinberg data is admissible only if the carrier
constructs the building/dualizing package together with the endpoint,
boundary map, Laurent twist, and torsor splitter. Support-stabilizer
buildings alone are bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SBT.1 full-frame stabilizer building as carrier loop
  A proposal uses the building of the full-frame stabilizer. The stabilizer
  is trivial, so this supplies no nontrivial building or loop data.

KILL-SBT.2 building top degree as carrier shift
  A proposal uses the top degree of the residual Sp building as the shift.
  The top degree matches the finite cutoff but constructs no adjacent map,
  inverse shift, Laurent generator, or boundary glue.

KILL-SBT.3 Steinberg module as carrier Laurent line
  A proposal uses the Steinberg module as the missing line. The tested
  Steinberg modules have dimensions 16,512,33554432, and
  2417851639229258349412352, not rank one.

KILL-SBT.4 building chamber/apartment/top-vector selection
  A proposal chooses a chamber, apartment, or top vector to extract a line.
  This is another support choice unless a carrier correspondence constructs
  it.

KILL-SBT.5 building/Steinberg package formable on controls
  Finite symplectic buildings and Steinberg modules of support stabilizers
  are support operations. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 39 = doc 176:
  N1B_SYMPLECTIC_BUILDING_STEINBERG__DUALIZING_REPRESENTATION_NOT_BOUNDARY_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: Tits-building
and Steinberg dualizing packages of the support symplectic stabilizers do
not construct the carrier endpoint, rank-one boundary map, Laurent line,
Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
  symplectic quotient/stack/isotropy/cohomology/building descent data,
  quadratic refinement or Maslov datum, orientation, half-identification,
  boundary endpoint, and Laurent twist/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
