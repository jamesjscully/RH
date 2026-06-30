# 182 - Principal cocharacter does not select the Laurent carrier

Status: no-go + symplectic principal-SL2 / principal-cocharacter repair
deletion, 2026-06-20. Forty-fifth cycle of the doc-137 construction arc.
Doc 181 killed appending geometric Satake / dual-representation data to the
support building. This document tests the next repair: use the principal SL2
of the dual type-B group, and read its principal cocharacter as the missing
rank-one Laurent carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_principal_cocharacter_no_go` (SPC1-SPC11 ALL
PASS) -- exact finite-window support ranks, residual stabilizers, appended
dual type-B ranks, principal-cocharacter coordinates, positive-system choices,
finite vector and adjoint principal strings, missing support-supplied
principal torus coordinate, missing boundary/torsor data, residual choices,
and control-formability checks.

## 1. Purpose

After doc 181, the Satake repair can answer the rank-m objection:

```text
Rep(G^vee) has many dominant weights, but G^vee has a principal SL2.
Its cocharacter h = 2rho^vee is a canonical rank-one axis.
Use that principal G_m as the Laurent line.
```

This is a real objection to the previous no-go, because the principal
cocharacter is rank one. The question is whether it is the missing carrier
shift, boundary map, or torsor splitter.

In this support setting it is not. The principal cocharacter is a finite
root-data grading inside an appended dual group. It is defined after choosing
a positive system/pinning, its representations decompose into finite strings,
and the coordinate ring of the source G_m is an external Laurent coordinate
unless a carrier constructs it. None of this builds the boundary map, Laurent
twist, or torsor splitter.

This document is local. It does not reject carrier-native principal SL2 data
or a future carrier-native dual group. It rejects only invoking the principal
cocharacter after appending the Satake / dual-group package to the finite
support symplectic building.

## 2. Lemma

```text
Lemma 182.1 (support principal-cocharacter data is not a Laurent carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

Appending Satake gives dual root type B_m with the same ranks:

  m = 2,3,5,9.

For type B_m, the principal cocharacter h = 2rho^vee has coordinates:

  m=2: (4,2);
  m=3: (6,4,2);
  m=5: (10,8,6,4,2);
  m=9: (18,16,14,12,10,8,6,4,2).

It pairs by 2 with every simple root. Thus it is a rank-one grading after a
positive system is chosen. But positive systems/pinnings are not supplied by
the support carrier; the corresponding Weyl-choice counts are:

  8,48,3840,185794560

with an additional sign/opposite choice.

The principal grading on finite representations is finite. The vector
representation has principal weight counts and maximal weights:

  counts: 5,7,11,19;
  max:    4,6,10,18.

The adjoint representation decomposes under the principal SL2 into finite
irreducible strings of dimensions:

  m=2: 3,7;
  m=3: 3,7,11;
  m=5: 3,7,11,15,19;
  m=9: 3,7,11,15,19,23,27,31,35.

The adjoint dimensions are:

  10,21,55,171.

The highest principal weights are finite:

  6,10,18,34.

Therefore the principal cocharacter supplies a finite representation grading,
not a bi-infinite Laurent shift. To get a Laurent line one must use the
coordinate ring of the source torus G_m, i.e. insert F_2[q^{+-1}] or an
analogous external coordinate. The finite support building supplies no
Satake category, no dual group, no pinning, no principal SL2, no principal
torus coordinate, no carrier boundary map, no Laurent generator, and no
torsor splitter. The graph/endpoint/idempotent/twist choices and the
bottom/shear/torsor obstructions remain, and the same principal-cocharacter
package is formable on controls.

Therefore support principal-SL2 / principal-cocharacter data is not
construction-grade R1 carrier correspondence algebra or Laurent boundary
glue. A surviving route must construct the dual group, pinning if used,
principal SL2, principal torus coordinate, selected Laurent axis, endpoint,
boundary map, Laurent twist, and torsor splitter as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_PRINCIPAL_COCHARACTER__FINITE_GRADING_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_principal_cocharacter_no_go` verifies the
finite-window model.

SPC1-SPC3 record the unchanged support ranks, Tate windows, residual
stabilizers, and appended dual type-B ranks:

```text
r = 3,4,6,10;
dual ranks = 2,3,5,9.
```

SPC4 records the core subtlety: the principal axis has rank one, but only
after choosing positive roots/pinning. The positive-system choice counts are:

```text
8,48,3840,185794560.
```

SPC5 records h = 2rho^vee and checks alpha_i(h)=2 for every simple root.

SPC6 records that the vector representation gives finite principal strings,
not a bi-infinite Laurent orbit:

```text
counts: 5,7,11,19;
max weights: 4,6,10,18.
```

SPC7 records that the adjoint decomposition overproduces finite SL2 strings:

```text
m=2: 3,7;
m=3: 3,7,11;
m=5: 3,7,11,15,19;
m=9: 3,7,11,15,19,23,27,31,35.
```

SPC8 records that the Satake category, dual group, principal SL2, and
principal torus coordinate are not support-supplied.

SPC9 records that the principal grading does not construct the shift,
boundary map, or torsor splitter.

SPC10 records that support choices and base obstructions remain: the DMP
bottom class still has no degree -2 support, the support choices persist,
and no carrier multiplication or torsor splitter is supplied.

SPC11 applies the carrier guard: using the coordinate ring of the principal
torus is an external Laurent-coordinate insertion, and the same principal
cocharacter package is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-182:
  NEWLY CLOSED THIS CYCLE:
    - principal SL2 / principal cocharacter of the appended dual group as
      carrier Laurent axis, boundary glue, or torsor splitter (doc 182).

  PREVIOUSLY CLOSED:
    - docs 138-181 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, Schubert-convolution, and Satake-dual repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs its dual/Satake/principal data internally if such data is
      used, and whose carrier-native map produces the endpoint, boundary map,
      Laurent twist/axis, torsor splitter, shift operator, and weight>=1
      datum while making DH/Epstein controls fail at named points.
```

R1 is still open. Principal-SL2 / principal-cocharacter data is admissible
only if the carrier constructs the dual group, pinning, principal SL2,
principal torus coordinate, selected Laurent axis, endpoint, boundary map,
Laurent twist, and torsor splitter. Invoking the principal cocharacter of an
inserted dual group is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SPC.1 principal cocharacter as carrier construction
  A proposal invokes the principal cocharacter after appending a dual group
  to support-building data. It gives a finite grading inside inserted
  root data; it does not construct the carrier.

KILL-SPC.2 rank-one principal axis as Laurent shift
  A proposal uses the fact that h=2rho^vee is rank one. The rank-one axis is
  not a bi-infinite carrier shift; finite representations have finite
  principal strings.

KILL-SPC.3 principal G_m coordinate as Laurent line
  A proposal uses O(G_m)=F_2[q^{+-1}] as the line. The coordinate q is
  external unless the carrier constructs the principal torus coordinate and
  its boundary glue.

KILL-SPC.4 principal SL2 as canonical selector
  A proposal treats principal SL2 as canonical without accounting for the
  positive system/pinning and opposite-sign choices. The finite support
  building supplies none of those data carrier-natively.

KILL-SPC.5 principal grading as boundary map or torsor splitter
  A proposal reads principal weights as the endpoint, boundary map, Laurent
  twist, or b/phi(b)=c splitter. The grading supplies no such map.

KILL-SPC.6 principal-cocharacter package formable on controls
  Appending root data, a principal SL2, and a G_m coordinate to finite support
  data is a support operation. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 45 = doc 182:
  N1B_SYMPLECTIC_PRINCIPAL_COCHARACTER__FINITE_GRADING_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: the principal
SL2 / principal cocharacter of an appended dual group cannot be used as the
missing Laurent carrier.

What remains: the route must produce carrier-native dual/principal data or
leave the Satake-dual branch. A rank-one grading inside inserted root data is
not enough.
```
