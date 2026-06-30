# 179 - Affine Hecke translations are inserted, not carrier-supplied

Status: no-go + symplectic affine Weyl/Hecke translation repair deletion,
2026-06-20. Forty-second cycle of the doc-137 construction arc. Doc 178
killed the finite Hecke/Iwahori/BN-pair double-coset algebra of the support
building. This document tests the next repair: pass to the affine Weyl group
or affine Hecke algebra and use its translation lattice as the missing
carrier shift.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_affine_hecke_no_go` (SAH1-SAH13 ALL PASS) --
exact finite-window support rank, residual stabilizer, finite Weyl/Hecke
data, affine translation-rank, affine-generator, axis-choice,
building/Weyl/Hecke/Steinberg, obstruction, and control-formability checks.

## 1. Purpose

After doc 178, the support-symplectic repair can say:

```text
the finite Hecke algebra has no translation;
pass to the affine Weyl group or affine Hecke algebra;
use the translation lattice as the missing Laurent shift;
select one primitive translation as the carrier generator.
```

This is distinct from doc 178. The tested object is not the finite
double-coset algebra, but the affine translation lattice added to it.

The repair is tempting because affine Hecke algebras do contain invertible
translations. But the finite support building does not supply an affine
valuation, an affine apartment, a translation lattice, or a preferred
primitive translation. Passing to affine type adds a rank-m lattice:

```text
Z^m,  m = 2,3,5,9.
```

That is not a rank-one Laurent line. Selecting one axis is another support
choice unless a carrier correspondence constructs it. The affine basis is
infinite only after adding the translation lattice externally.

This document is local. It does not reject carrier-native affine Hecke
algebras, loop-group correspondences, or genuine translation lattices. It
rejects only the move from the finite support symplectic building to an
affine Weyl/Hecke package as the R1 Laurent carrier.

## 2. Lemma

```text
Lemma 179.1 (support affine translations are external lattice insertion).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

The stabilizer orders are:

  720,
  1451520,
  24815256521932800,
  2060902435720151186326095525680721766346957783040000.

The finite Weyl/Hecke data before affine insertion is unchanged:

  |W(C_m)|:                 8,48,3840,185794560;
  finite longest lengths:   4,9,25,81;
  Coxeter orders:           4,6,10,18.

Passing to affine type adds a translation lattice of ranks:

  2,3,5,9.

The affine simple-generator counts are:

  m+1 = 3,4,6,10.

These counts match the support ranks, but only as finite bookkeeping. They
do not construct the affine valuation or translation lattice.

The obvious simple coroot axis choices are:

  4,6,10,18.

So even after affine insertion, a rank-one Laurent axis is not selected. The
finite support building supplies no affine valuation, no translation lattice,
no preferred primitive translation, no boundary map, and no torsor splitter.

The building, Weyl, finite Hecke, and Steinberg obstructions remain:

  building top degrees: 1,2,4,8;
  chamber counts:       45,2835,739552275,852369269595510700600441875;
  Steinberg dimensions: 16,512,33554432,2417851639229258349412352;
  finite Hecke ranks:   8,48,3840,185794560.

The graph, endpoint/matching, idempotent, and twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same affine Weyl/Hecke package
is formable on controls.

Therefore support affine Weyl/Hecke translation data is not
construction-grade R1 carrier monodromy or Laurent boundary glue. A
surviving route must construct the affine valuation, translation lattice,
selected Laurent axis, endpoint, boundary map, Laurent twist, and torsor
splitter as carrier-native correspondence data and prove DH/Epstein death at
that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_AFFINE_HECKE__TRANSLATION_LATTICE_INSERTION_NOT_CARRIER_SHIFT__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_affine_hecke_no_go` verifies the finite-window
model.

SAH1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SAH2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SAH3 records the residual first-pair stabilizers. They are finite
`Sp(2m,F_2)` groups with:

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

SAH4 records that finite Weyl/Hecke data is unchanged before affine
insertion:

```text
finite Weyl orders = 8,48,3840,185794560;
finite longest lengths = 4,9,25,81;
Coxeter orders = 4,6,10,18.
```

SAH5 records the affine translation lattice ranks:

```text
2,3,5,9.
```

All are greater than one, so no rank-one Laurent line is selected.

SAH6 records the affine simple-generator counts:

```text
3,4,6,10.
```

These equal the support ranks, but the equality supplies no affine
valuation. SAH6 also records the simple coroot axis choices:

```text
4,6,10,18.
```

SAH7 records that the affine basis is infinite only after adding translation
data and that the support building supplies neither affine valuation nor
translation lattice.

SAH8 records that selecting one primitive translation axis is another choice.

SAH9 records that affine Weyl/Hecke data does not construct the boundary map
or torsor splitter.

SAH10 records that the building/Weyl/Hecke/Steinberg finite-data
obstructions remain.

SAH11 records that graph, endpoint, matching, idempotent, and twist choices
remain.

SAH12 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SAH13 applies the carrier guard: adjoining the affine Weyl/Hecke translation
lattice to support-building data is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-179:

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
      torsor splitter (doc 176);
    - finite Weyl/Coxeter/apartment monodromy of the support symplectic
      building as carrier monodromy, Laurent shift, boundary glue, or torsor
      splitter (doc 177);
    - finite Hecke/Iwahori/BN-pair double-coset algebra of the support
      symplectic building as carrier correspondence algebra, monodromy,
      Laurent line, boundary glue, or torsor splitter (doc 178);
    - affine Weyl/Hecke translation lattice appended to the support
      symplectic building as carrier monodromy, Laurent shift, boundary glue,
      or torsor splitter (doc 179).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building/Weyl/Coxeter/
      Hecke/Iwahori/affine-translation descent data, quadratic refinement or
      Maslov datum, orientation, half-identification, boundary endpoint, and
      Laurent twist/flag/idempotent/line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Affine Weyl/Hecke data is admissible only if the carrier
constructs the affine valuation, translation lattice, selected Laurent axis,
endpoint, boundary map, Laurent twist, and torsor splitter. Appending an
affine translation lattice to finite support-building data is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SAH.1 affine Weyl group as carrier monodromy
  A proposal passes from the finite support Weyl group to the affine Weyl
  group and uses its translations as monodromy. The translation lattice is
  not supplied by the finite support building.

KILL-SAH.2 affine Hecke algebra as carrier correspondence
  A proposal repairs finite Hecke data by adjoining affine translations. This
  makes an infinite algebra only after adding a translation lattice external
  to the support package.

KILL-SAH.3 translation lattice as Laurent shift
  A proposal uses the affine translation lattice as the Laurent shift. The
  lattice ranks are 2,3,5,9, not one, so a Laurent axis still has to be
  selected.

KILL-SAH.4 primitive translation selection as carrier endpoint
  A proposal chooses a simple coroot, coweight, alcove direction, or
  primitive translation to extract one line. This is another support choice
  unless a carrier correspondence constructs it.

KILL-SAH.5 affine valuation insertion
  A proposal adds an affine valuation, loop parameter, or apartment at
  infinity to the finite support building. That datum must be carrier-native;
  otherwise it is the same external shift insertion killed earlier.

KILL-SAH.6 affine Weyl/Hecke package formable on controls
  Appending an affine translation lattice to finite support-building data is
  a support operation. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 42 = doc 179:
  N1B_SYMPLECTIC_AFFINE_HECKE__TRANSLATION_LATTICE_INSERTION_NOT_CARRIER_SHIFT__NO_GO.

What got built: no new sub-object. The value is a deletion: affine
Weyl/Hecke translation lattices appended to finite support-building data do
not construct the R1 Laurent carrier.

What remains: the route must produce carrier-native affine valuation and
translation data together with endpoint, boundary glue, Laurent twist, and
torsor splitting. Appending Z^m to support data is not enough.

Next admissible move: either find a carrier-consuming multiplication/
correspondence that constructs affine translation data internally, or move to
the next deletion test for support-building descent data.
```
