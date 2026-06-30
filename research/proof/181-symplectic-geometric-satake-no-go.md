# 181 - Geometric Satake does not select the Laurent carrier

Status: no-go + symplectic geometric-Satake / dual-representation repair
deletion, 2026-06-20. Forty-fourth cycle of the doc-137 construction arc.
Doc 180 killed appending affine Grassmannian / Schubert convolution data to
the support building. This document tests the next repair: invoke geometric
Satake and read the dual-group representation category as the missing
carrier correspondence algebra.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_geometric_satake_no_go` (SGS1-SGS13 ALL PASS) --
exact finite-window support rank, residual stabilizer, finite
Weyl/Hecke/affine/Schubert data, type-B dual rank, dominant-weight counts,
fundamental representation dimensions, one-dimensional representation check,
choice, obstruction, and control-formability checks.

## 1. Purpose

After doc 180, the support-symplectic repair can say:

```text
Schubert convolution is not just appended data;
geometric Satake identifies it with Rep(G^vee);
the dual-group tensor category is the carrier correspondence algebra;
read a representation, tensor unit, or fiber functor as the Laurent line.
```

This is distinct from doc 180. The tested object is not only the Schubert
label monoid, but the Tannakian / dual-representation package obtained after
the Satake wrapper.

The repair is tempting because geometric Satake is a powerful structure
theorem. But in this local support setting it still depends on the same
inserted affine Grassmannian data. For support buildings of type C_m, the
dual root system is type B_m, with:

```text
m = 2,3,5,9.
```

Dominant weights still form a rank-m monoid, not a rank-one Laurent axis.
The fundamental representations are higher-dimensional. The only
one-dimensional representation of the semisimple dual group is the trivial
unit, which supplies no shift, boundary map, or torsor splitter.

This document is local. It does not reject carrier-native geometric Satake,
dual groups, Tannakian categories, or representation categories. It rejects
only invoking the Satake wrapper after appending affine-Grassmannian data to
the finite support symplectic building.

## 2. Lemma

```text
Lemma 181.1 (support Satake data is not a Laurent carrier).
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

The finite Weyl, finite Hecke, affine, and Schubert data from docs 177-180
is unchanged:

  |W(C_m)|:                    8,48,3840,185794560;
  finite longest lengths:      4,9,25,81;
  Coxeter orders:              4,6,10,18;
  affine translation ranks:    2,3,5,9;
  affine simple-generator cts: 3,4,6,10;
  Schubert labels <= N:        3,10,126,24310.

Geometric Satake replaces dominant coweights of type C_m by dominant
weights of the Langlands dual type B_m. The rank remains:

  2,3,5,9.

In the same finite height windows, the dominant-weight counts are still:

  height <= N: 3,10,126,24310;
  height  = N: 2,6,70,12870.

The fundamental representation dimensions of type B_m are:

  m=2: 5,4;
  m=3: 7,21,8;
  m=5: 11,55,165,330,32;
  m=9: 19,171,969,3876,11628,27132,50388,75582,512.

All are greater than one. The only one-dimensional representation is the
trivial tensor unit:

  nontrivial invertible lines = 0.

Thus the Satake wrapper does not select a nontrivial Laurent generator. A
fundamental representation, highest-weight object, or fiber functor still
has to be chosen, and none constructs the boundary map or torsor splitter.

The finite support building supplies no loop parameter, no affine valuation,
no Satake category, no dual group, no fiber functor, no carrier boundary map,
no Laurent generator, and no torsor splitter. The graph/endpoint/idempotent/
twist choices and bottom/shear/torsor obstructions remain, and the same
Satake / dual-representation package is formable on controls.

Therefore support geometric-Satake / dual-representation data is not
construction-grade R1 carrier correspondence algebra or Laurent boundary
glue. A surviving route must construct the Satake category, dual group,
fiber functor if used, selected Laurent axis, endpoint, boundary map,
Laurent twist, and torsor splitter as carrier-native correspondence data and
prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_GEOMETRIC_SATAKE__DUAL_REPRESENTATION_CATEGORY_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_geometric_satake_no_go` verifies the finite-window
model.

SGS1-SGS4 record the unchanged support, stabilizer, finite Weyl/Hecke,
affine, and Schubert data.

SGS5 records that the dual type-B dominant-weight monoid has ranks:

```text
2,3,5,9.
```

SGS6 records the finite weight-window counts:

```text
height <= N: 3,10,126,24310;
height  = N: 2,6,70,12870.
```

SGS7 records the fundamental representation dimensions:

```text
m=2: 5,4;
m=3: 7,21,8;
m=5: 11,55,165,330,32;
m=9: 19,171,969,3876,11628,27132,50388,75582,512.
```

SGS8 records that there are no nontrivial one-dimensional representations;
the only line is the trivial unit.

SGS9 records that choosing one representation generator is another support
choice.

SGS10 records that the loop parameter, affine valuation, Satake category,
dual group, and fiber functor are not support-supplied.

SGS11 records that Satake data does not construct the boundary map, Laurent
generator, or torsor splitter.

SGS12 records that the finite choices and bottom/shear/torsor obstructions
remain.

SGS13 applies the carrier guard: appending geometric Satake / dual
representation data to support-building data is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-181:
  NEWLY CLOSED THIS CYCLE:
    - geometric Satake / dual-representation data appended to the support
      symplectic building as carrier correspondence algebra, Laurent line,
      boundary glue, or torsor splitter (doc 181).

  PREVIOUSLY CLOSED:
    - docs 138-180 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, and Schubert-convolution repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building/Weyl/Coxeter/
      Hecke/Iwahori/affine-translation/Schubert-convolution/Satake-dual
      descent data, quadratic refinement or Maslov datum, orientation,
      half-identification, boundary endpoint, and Laurent
      twist/flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. Geometric Satake / dual-representation data is admissible
only if the carrier constructs the loop parameter, affine valuation, Satake
category, dual group, fiber functor if used, selected Laurent axis, endpoint,
boundary map, Laurent twist, and torsor splitter. Invoking Satake after
appending affine-Grassmannian data is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SGS.1 geometric Satake as carrier construction
  A proposal invokes geometric Satake after appending affine-Grassmannian
  data to the support building. The theorem identifies an inserted
  convolution category; it does not construct the carrier.

KILL-SGS.2 dual group as carrier correspondence algebra
  A proposal reads Rep(G^vee) as End(Xbar). The dual type-B representation
  category has rank-m dominant weights, not a selected Laurent line.

KILL-SGS.3 fundamental representation as carrier endpoint
  A proposal chooses one fundamental representation or highest-weight object.
  The fundamental dimensions are all greater than one, and the choice is not
  carrier-supplied.

KILL-SGS.4 tensor unit as Laurent line
  A proposal uses the tensor unit as the line. It is the trivial
  representation and supplies no nontrivial shift, boundary map, twist, or
  torsor splitter.

KILL-SGS.5 fiber functor as carrier selector
  A proposal uses a Tannakian fiber functor to select the line. The fiber
  functor is not supplied by the finite support building and does not
  construct the boundary glue.

KILL-SGS.6 Satake package formable on controls
  Appending Satake / dual-representation data to finite support-building data
  is a support operation. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 44 = doc 181:
  N1B_SYMPLECTIC_GEOMETRIC_SATAKE__DUAL_REPRESENTATION_CATEGORY_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: geometric Satake
or the dual-group representation category appended to finite support-building
data does not construct the R1 carrier correspondence algebra or Laurent
boundary glue.

What remains: the route must produce carrier-native Satake/dual-group data
together with endpoint, boundary glue, Laurent twist, and torsor splitting.
Invoking Satake on an inserted affine Grassmannian is not enough.

Next admissible move: either find a carrier-consuming multiplication/
correspondence that constructs Satake data internally, or move to the next
deletion test for support-building descent data.
```
