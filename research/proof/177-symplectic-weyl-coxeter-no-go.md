# 177 - Finite Weyl/Coxeter monodromy is not the Laurent shift

Status: no-go + symplectic Weyl/Coxeter/apartment repair deletion,
2026-06-20. Fortieth cycle of the doc-137 construction arc. Doc 176 killed
using the support symplectic building or its Steinberg module as the missing
boundary line. This document tests the next repair: choose an apartment in
that building and use the type-C Weyl group, or a Coxeter element, as the
carrier monodromy / Laurent shift.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_weyl_coxeter_no_go` (SWC1-SWC13 ALL PASS) --
exact finite-window support rank, residual stabilizer, type-C Weyl group,
Coxeter order, finite-wrap, Laurent-window, building/Steinberg, choice,
obstruction, and control-formability checks.

## 1. Purpose

After doc 176, the support-symplectic repair can say:

```text
the whole building or Steinberg module is too large;
choose one apartment;
inside that apartment, use the type-C Weyl group or a Coxeter element;
read Coxeter rotation as the carrier shift / monodromy operator.
```

This is distinct from doc 176. The tested object is not top homology of the
building, but finite apartment monodromy inside the residual support
building.

The repair is tempting because a Coxeter element gives a canonical-looking
rotation once an apartment and simple-root ordering have been chosen. But in
the support windows the Weyl/Coxeter data is finite. A Coxeter element in
type C_m has order 2m, so its orbit closes:

```text
c^(2m) = 1.
```

A finite wrapped orbit is not the bi-infinite Laurent shift. It imposes a
periodic relation instead of constructing adjacent arrows, inverse arrows,
boundary glue, or a rank-one Laurent generator. Choosing the apartment and
Coxeter element is also support data unless the carrier correspondence
constructs it.

This document is local. It does not reject carrier-native Weyl groups,
apartments, Coxeter functors, or monodromy. It rejects only the finite
Weyl/Coxeter package of the visible support symplectic building as the R1
Laurent carrier.

## 2. Lemma

```text
Lemma 177.1 (support Weyl/Coxeter monodromy is finite wrap data).
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

The Weyl group orders |W(C_m)| = 2^m m! are:

  8,48,3840,185794560.

The Coxeter element orders h(C_m)=2m are:

  4,6,10,18.

Thus every Coxeter orbit in the tested support windows is finite. Reading
the Coxeter action as the Laurent shift imposes a finite wrap relation
c^(2m)=1. It does not construct a bi-infinite shift, an inverse shift beyond
the finite cyclic inverse, a carrier boundary map, a Laurent generator, or a
torsor splitter.

The Coxeter orders also miss the tested Laurent twist windows:

  Laurent twists: 3,5,9,17.

The offset is one in each tested window:

  4-3 = 6-5 = 10-9 = 18-17 = 1.

The building/Steinberg overproduction from doc 176 remains:

  building top degrees: 1,2,4,8;
  chamber counts:       45,2835,739552275,852369269595510700600441875;
  Steinberg dimensions: 16,512,33554432,2417851639229258349412352.

The graph, endpoint/matching, idempotent, and twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same finite Weyl/Coxeter
package is formable on controls.

Therefore support Weyl/Coxeter/apartment monodromy is not construction-grade
R1 carrier monodromy or Laurent boundary glue. A surviving route must
construct the apartment, monodromy, endpoint, boundary map, Laurent twist,
and torsor splitter as carrier-native correspondence data and prove
DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_WEYL_COXETER__FINITE_APARTMENT_MONODROMY_NOT_LAURENT_SHIFT__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_weyl_coxeter_no_go` verifies the finite-window
model.

SWC1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SWC2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SWC3 records the residual first-pair stabilizers. They are finite
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

SWC4 records the type-C Weyl group orders:

```text
8,48,3840,185794560.
```

These are finite apartment chamber counts, not carrier correspondences.

SWC5 records the Coxeter element orders:

```text
4,6,10,18.
```

SWC6 records the consequence: Coxeter monodromy closes up in a finite cyclic
subgroup. Treating it as the shift imposes finite wrap relations
`c^4=1`, `c^6=1`, `c^10=1`, `c^18=1`, not a Laurent line.

SWC7 records that the Coxeter orders do not match the finite Laurent twist
windows:

```text
Coxeter orders = 4,6,10,18;
Laurent twists = 3,5,9,17.
```

SWC8 records that the apartment, Weyl group, and Coxeter element are not
carrier-supplied in this repair.

SWC9 records that Weyl/Coxeter data does not construct the boundary map,
Laurent generator, or torsor splitter.

SWC10 records that the doc-176 building/Steinberg overproduction remains:

```text
top degrees = 1,2,4,8;
chamber counts = 45,2835,739552275,852369269595510700600441875;
Steinberg dimensions = 16,512,33554432,2417851639229258349412352.
```

SWC11 records that the graph, endpoint, matching, and idempotent choices
remain:

```text
graph choices = 64,1024,2097152,36028797018963968;
endpoint pairs = 9,16,36,100;
half matchings = 6,24,720,3628800;
rank-one idempotents = 2016,32640,8386560,549755289600.
```

SWC12 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SWC13 applies the carrier guard: finite Weyl groups, apartments, and Coxeter
elements of support stabilizer buildings are support operations, so controls
can form the same package.

## 4. Impact on R1

```text
R1 after docs 138-177:

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
      splitter (doc 177).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building/Weyl/Coxeter
      descent data, quadratic refinement or Maslov datum, orientation,
      half-identification, boundary endpoint, and Laurent twist/flag/
      idempotent/line, selector/functional/shift operator, torsor splitter,
      and weight>=1 datum from carrier data, and where DH/Epstein controls
      fail before signs, zeros, or comparison.
```

R1 is still open. Weyl/Coxeter/apartment data is admissible only if the
carrier constructs the apartment and monodromy together with the endpoint,
boundary map, Laurent twist, and torsor splitter. Finite support-building
monodromy alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SWC.1 apartment Weyl group as carrier monodromy
  A proposal uses the Weyl group of a chosen support-building apartment as
  carrier monodromy. The group is finite and supplied only after an apartment
  choice.

KILL-SWC.2 Coxeter element as Laurent shift
  A proposal uses a Coxeter element as the missing Laurent shift. The Coxeter
  element has finite order 4,6,10,18 in the tested windows, imposing a wrap
  relation rather than a bi-infinite Laurent generator.

KILL-SWC.3 finite Weyl orbit as boundary glue
  A proposal reads a finite Weyl/Coxeter orbit as the boundary map. A finite
  orbit supplies no endpoint, no rank-one boundary map, no Laurent twist, and
  no torsor splitter.

KILL-SWC.4 apartment/Coxeter selection as carrier endpoint
  A proposal chooses an apartment, chamber order, simple roots, or Coxeter
  element to extract a line. This is another support choice unless a carrier
  correspondence constructs it.

KILL-SWC.5 Weyl/Coxeter package formable on controls
  Finite Weyl groups, Coxeter elements, and apartment data of support
  stabilizer buildings are support operations. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 40 = doc 177:
  N1B_SYMPLECTIC_WEYL_COXETER__FINITE_APARTMENT_MONODROMY_NOT_LAURENT_SHIFT__NO_GO.

What got built: no new sub-object. The value is a deletion: finite
Weyl/Coxeter/apartment monodromy of the support symplectic building does not
construct the R1 Laurent carrier.

What remains: the route must produce carrier-native correspondence data that
constructs apartment/monodromy together with endpoint, boundary glue, Laurent
twist, and torsor splitting. Finite support-building monodromy is not enough.

Next admissible move: either find a carrier-consuming multiplication/
correspondence that constructs the Weyl/Coxeter data internally, or move to
the next deletion test for support-building descent data.
```
