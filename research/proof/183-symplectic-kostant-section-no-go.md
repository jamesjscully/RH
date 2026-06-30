# 183 - Kostant section does not construct the Laurent carrier

Status: no-go + symplectic regular-nilpotent / Kostant-section repair
deletion, 2026-06-20. Forty-sixth cycle of the doc-137 construction arc.
Doc 182 killed using the principal cocharacter of the appended dual type-B
group as the rank-one Laurent axis. This document tests the next repair: use
the principal nilpotent, Kostant slice, or Chevalley adjoint quotient of that
dual group as the missing carrier correspondence algebra.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_kostant_section_no_go` (SKS1-SKS10 ALL PASS) --
exact finite-window support ranks, residual stabilizers, dual type-B ranks,
regular nilpotent orbit dimensions, positive-system/pinning choices,
nilpotency indices, Chevalley invariant degrees, Kostant slice dimensions,
missing support-supplied inputs, missing boundary/torsor data, residual
choices, and control-formability checks.

## 1. Purpose

After doc 182, the principal-cocharacter repair can say:

```text
The cocharacter was only a grading.
Use the principal nilpotent and Kostant section instead.
The Chevalley/Kostant quotient is the canonical carrier algebra.
```

This is a distinct repair. It tries to replace the finite principal grading
by a canonical slice through regular elements, and then read the invariant
coordinates as the carrier correspondence algebra.

In this support setting it still fails. A regular nilpotent is nilpotent,
not invertible. The Kostant slice and Chevalley adjoint quotient are affine
rank-m polynomial data with invariant degrees 2,4,...,2m, not a rank-one
Laurent carrier. The dual group, pinning, principal nilpotent, Kostant
slice, quotient coordinates, boundary map, Laurent shift, and torsor splitter
are not supplied by the finite support building.

This document is local. It does not reject carrier-native Kostant, Springer,
Hitchin, or regular-centralizer data. It rejects only invoking the
regular-nilpotent / Kostant-section package after appending dual-group data
to the finite support symplectic building.

## 2. Lemma

```text
Lemma 183.1 (support Kostant data is not a Laurent carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

Appending Satake gives dual root type B_m. The Lie algebra dimensions are:

  10,21,55,171.

Regular centralizer dimensions are:

  2,3,5,9.

Regular nilpotent orbit dimensions are:

  8,18,50,162.

The principal nilpotent is defined only after positive-system/pinning data.
The corresponding Weyl-choice counts are:

  8,48,3840,185794560.

The principal nilpotent acts by finite strings. In the vector representation,
the nilpotency indices are:

  5,7,11,19.

In the adjoint representation, using the principal SL2 decomposition, the
nilpotency indices are:

  7,11,19,35.

Thus the regular nilpotent is not an invertible shift.

The Chevalley invariant degrees of type B_m are:

  m=2: 2,4;
  m=3: 2,4,6;
  m=5: 2,4,6,8,10;
  m=9: 2,4,6,8,10,12,14,16,18.

The Kostant slice and adjoint quotient therefore have dimensions:

  2,3,5,9.

This is affine rank-m polynomial data, not a Laurent line. Localizing or
choosing one invariant coordinate would be another selector or external
coordinate insertion.

The finite support building supplies no Satake category, no dual group, no
pinning, no principal nilpotent, no Kostant slice, no Chevalley quotient
coordinates, no carrier boundary map, no Laurent generator, and no torsor
splitter. The graph/endpoint/idempotent/twist choices and the
bottom/shear/torsor obstructions remain, and the same Kostant-section package
is formable on controls.

Therefore support regular-nilpotent / Kostant-section data is not
construction-grade R1 carrier correspondence algebra or Laurent boundary
glue. A surviving route must construct the dual group, pinning if used,
regular centralizer/Kostant/Hitchin data if used, selected Laurent axis,
endpoint, boundary map, Laurent twist, and torsor splitter as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_KOSTANT_SECTION__REGULAR_NILPOTENT_AFFINE_QUOTIENT_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_kostant_section_no_go` verifies the finite-window
model.

SKS1-SKS3 record the unchanged support ranks, Tate windows, residual
stabilizers, and appended dual type-B dimensions:

```text
r = 3,4,6,10;
dual ranks = 2,3,5,9;
dual dimensions = 10,21,55,171.
```

SKS4 records that a regular nilpotent requires positive-system/pinning data,
with choice counts:

```text
8,48,3840,185794560.
```

SKS5 records that the regular nilpotent is finite nilpotent data, not an
invertible Laurent shift:

```text
vector nilpotency indices: 5,7,11,19;
adjoint nilpotency indices: 7,11,19,35.
```

SKS6 records that the Kostant slice and Chevalley quotient are rank-m affine
data with invariant degrees:

```text
m=2: 2,4;
m=3: 2,4,6;
m=5: 2,4,6,8,10;
m=9: 2,4,6,8,10,12,14,16,18.
```

SKS7 records that the Satake category, dual group, Kostant slice, and
Chevalley coordinates are not support-supplied.

SKS8 records that the Kostant section does not construct the shift, boundary
map, or torsor splitter.

SKS9 records that support choices and base obstructions remain: the DMP
bottom class still has no degree -2 support, the support choices persist,
and no carrier multiplication or torsor splitter is supplied.

SKS10 applies the carrier guard: appending Chevalley/Kostant coordinates to
finite support data is external affine insertion, and the same package is
formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-183:
  NEWLY CLOSED THIS CYCLE:
    - regular nilpotent / Kostant section / Chevalley quotient of the
      appended dual group as carrier correspondence algebra, Laurent axis,
      boundary glue, or torsor splitter (doc 183).

  PREVIOUSLY CLOSED:
    - docs 138-182 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, Schubert-convolution, Satake-dual, and
      principal-cocharacter repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs any dual/Kostant/Springer/Hitchin data internally if such
      data is used, and whose carrier-native map produces the endpoint,
      boundary map, Laurent twist/axis, torsor splitter, shift operator, and
      weight>=1 datum while making DH/Epstein controls fail at named points.
```

R1 is still open. Regular-nilpotent / Kostant-section data is admissible only
if the carrier constructs the dual group, pinning, regular centralizer,
Kostant slice, invariant coordinates, selected Laurent axis, endpoint,
boundary map, Laurent twist, and torsor splitter. Invoking the Kostant
section of an inserted dual group is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SKS.1 regular nilpotent as carrier construction
  A proposal invokes a principal or regular nilpotent after appending a dual
  group to support-building data. The nilpotent is inserted root data; it
  does not construct the carrier.

KILL-SKS.2 nilpotent as Laurent shift
  A proposal reads the regular nilpotent as the shift. It has finite
  nilpotency indices in finite representations and is not invertible.

KILL-SKS.3 Kostant slice as correspondence algebra
  A proposal reads the Kostant section or Chevalley quotient as End(Xbar).
  The slice/quotient is affine rank-m polynomial data, not a selected
  rank-one Laurent line.

KILL-SKS.4 Chevalley coordinate as Laurent axis
  A proposal chooses one invariant coordinate or localizes the quotient.
  That is a selector or external coordinate insertion unless constructed by
  the carrier.

KILL-SKS.5 Kostant data as boundary map or torsor splitter
  A proposal reads the regular centralizer, invariant degrees, or Kostant
  coordinates as the endpoint, boundary map, Laurent twist, or b/phi(b)=c
  splitter. The package supplies no such map.

KILL-SKS.6 Kostant package formable on controls
  Appending root data, a regular nilpotent, a Kostant slice, and Chevalley
  coordinates to finite support data is a support operation. DH/Epstein have
  not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 46 = doc 183:
  N1B_SYMPLECTIC_KOSTANT_SECTION__REGULAR_NILPOTENT_AFFINE_QUOTIENT_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: the regular
nilpotent / Kostant section / Chevalley quotient of an appended dual group
cannot be used as the missing Laurent carrier.

What remains: the route must produce carrier-native dual/Kostant data or
leave the Satake-dual branch. Affine invariant coordinates inside inserted
root data are not enough.
```
