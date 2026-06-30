# 184 - Springer/Steinberg convolution does not construct the Laurent carrier

Status: no-go + symplectic Springer-resolution / Steinberg-variety repair
deletion, 2026-06-20. Forty-seventh cycle of the doc-137 construction arc.
Doc 183 killed using the regular nilpotent, Kostant slice, or Chevalley
quotient of the appended dual type-B group as the carrier algebra. This
document tests the next repair: use the Springer resolution or Steinberg
variety convolution algebra of that dual group as the missing carrier
correspondence algebra.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_springer_steinberg_no_go` (SSV1-SSV10 ALL PASS)
-- exact finite-window support ranks, residual stabilizers, dual type-B
Springer dimensions, Weyl and flag counts, Steinberg component counts,
nil-Hecke/equivariant polynomial ranks, axis-choice counts, missing
support-supplied inputs, missing boundary/torsor data, residual choices, and
control-formability checks.

## 1. Purpose

After doc 183, the Kostant repair can say:

```text
Kostant coordinates are only affine invariant functions.
Use the actual Springer resolution or Steinberg variety.
The Steinberg convolution algebra is a genuine correspondence algebra.
```

This is distinct from doc 176. Doc 176 killed Tits-building/Steinberg
dualizing data of finite support stabilizers. This document tests the
Springer resolution and Steinberg variety of the appended dual type-B group.

The repair still fails locally. The non-equivariant Springer/Steinberg
package is finite Weyl/Schubert data. The equivariant or K-theoretic package
adds rank-m polynomial or weight-lattice data. Neither side selects a
carrier-native rank-one Laurent axis, boundary map, or torsor splitter.

This document is local. It does not reject carrier-native Springer,
Steinberg, Hitchin, or geometric-representation-theoretic data. It rejects
only invoking Springer/Steinberg convolution after appending dual-group data
to the finite support symplectic building.

## 2. Lemma

```text
Lemma 184.1 (support Springer/Steinberg data is not a Laurent carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

Appending Satake gives dual root type B_m. The finite Weyl group orders are:

  8,48,3840,185794560.

The flag variety dimensions, equal to the positive-root counts, are:

  4,9,25,81.

The top cohomological degrees are:

  8,18,50,162.

Non-equivariant Springer/Steinberg data is finite:

  flag cohomology dimensions = 8,48,3840,185794560;
  Steinberg component counts = 8,48,3840,185794560.

The Springer fiber over a regular nilpotent is a point in this model, while
the zero fiber is the full flag variety. Neither supplies an invertible
bi-infinite carrier shift.

Equivariant or nil-Hecke variants add rank-m torus data:

  nil-Hecke simple generators:       2,3,5,9;
  equivariant polynomial ranks:      2,3,5,9;
  affine Hecke weight-lattice ranks: 2,3,5,9.

The Steinberg convolution algebra therefore gives finite Weyl-indexed
correspondences over rank-m polynomial/equivariant data. Selecting one
weight direction or localizing one coordinate is another axis choice:

  fundamental choices = 2,3,5,9;
  signed choices      = 4,6,10,18.

The finite support building supplies no Satake category, no dual group, no
Borel, no Springer resolution, no Steinberg variety, no equivariant torus,
no preferred weight axis, no carrier boundary map, no Laurent generator, and
no torsor splitter. The graph/endpoint/idempotent/twist choices and the
bottom/shear/torsor obstructions remain, and the same Springer/Steinberg
package is formable on controls.

Therefore support Springer-resolution / Steinberg-variety convolution data
is not construction-grade R1 carrier correspondence algebra or Laurent
boundary glue. A surviving route must construct the dual group, Borel,
Springer/Steinberg/Hitchin data if used, selected Laurent axis, endpoint,
boundary map, Laurent twist, and torsor splitter as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_SPRINGER_STEINBERG__FINITE_WEYL_EQUIVARIANT_RANK_M_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_springer_steinberg_no_go` verifies the
finite-window model.

SSV1-SSV3 record the unchanged support ranks, Tate windows, residual
stabilizers, finite Weyl orders, and flag dimensions:

```text
r = 3,4,6,10;
dual ranks = 2,3,5,9;
|W| = 8,48,3840,185794560;
dim flag = 4,9,25,81.
```

SSV4 records that non-equivariant Springer/Steinberg data is finite and
Weyl-indexed:

```text
flag cohomology dimensions = 8,48,3840,185794560;
Steinberg component counts = 8,48,3840,185794560.
```

SSV5 records that equivariant/nil-Hecke variants introduce rank-m polynomial
or weight-lattice data:

```text
2,3,5,9.
```

SSV6 records that selecting one equivariant or Laurent axis is another
choice:

```text
fundamental choices = 2,3,5,9;
signed choices      = 4,6,10,18.
```

SSV7 records that the Satake category, dual group, Borel, Springer
resolution, Steinberg variety, and equivariant torus are not support-supplied.

SSV8 records that Springer/Steinberg convolution does not construct the
shift, boundary map, or torsor splitter.

SSV9 records that support choices and base obstructions remain: the DMP
bottom class still has no degree -2 support, the support choices persist,
and no carrier multiplication or torsor splitter is supplied.

SSV10 applies the carrier guard: appending the Springer/Steinberg package to
finite support data is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-184:
  NEWLY CLOSED THIS CYCLE:
    - Springer resolution / Steinberg variety convolution of the appended
      dual group as carrier correspondence algebra, Laurent axis, boundary
      glue, or torsor splitter (doc 184).

  PREVIOUSLY CLOSED:
    - docs 138-183 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, Schubert-convolution, Satake-dual,
      principal-cocharacter, and Kostant-section repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs any dual/Springer/Steinberg/Hitchin data internally if such
      data is used, and whose carrier-native map produces the endpoint,
      boundary map, Laurent twist/axis, torsor splitter, shift operator, and
      weight>=1 datum while making DH/Epstein controls fail at named points.
```

R1 is still open. Springer/Steinberg data is admissible only if the carrier
constructs the dual group, Borel, Springer resolution, Steinberg variety,
equivariant torus if used, selected Laurent axis, endpoint, boundary map,
Laurent twist, and torsor splitter. Invoking the Springer package of an
inserted dual group is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SSV.1 Springer resolution as carrier construction
  A proposal invokes the Springer resolution after appending a dual group to
  support-building data. The resolution is inserted dual-group data; it does
  not construct the carrier.

KILL-SSV.2 Steinberg variety as End(Xbar)
  A proposal reads Steinberg convolution as the missing correspondence
  algebra. The non-equivariant package is finite Weyl-indexed; the
  equivariant package is polynomial over rank-m torus data.

KILL-SSV.3 nil-Hecke or affine-Hecke variable as Laurent axis
  A proposal chooses one equivariant coordinate or weight direction. That is
  a selector unless the carrier constructs the axis.

KILL-SSV.4 Schubert basis as carrier shift
  A proposal reads Schubert or Weyl indexing as the shift. The indexing is
  finite and terminates at longest length m^2.

KILL-SSV.5 Springer/Steinberg data as boundary map or torsor splitter
  A proposal reads Springer fibers, Steinberg components, nil-Hecke
  generators, or equivariant classes as the endpoint, boundary map, Laurent
  twist, or b/phi(b)=c splitter. The package supplies no such map.

KILL-SSV.6 Springer/Steinberg package formable on controls
  Appending a dual group, Borel, Springer resolution, Steinberg variety, and
  equivariant torus to finite support data is a support operation. DH/Epstein
  have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 47 = doc 184:
  N1B_SYMPLECTIC_SPRINGER_STEINBERG__FINITE_WEYL_EQUIVARIANT_RANK_M_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: the Springer
resolution / Steinberg variety convolution package of an appended dual group
cannot be used as the missing Laurent carrier.

What remains: the route must produce carrier-native dual/Springer/Steinberg
data or leave the Satake-dual branch. Weyl-indexed correspondences over
rank-m equivariant data are not enough.
```
