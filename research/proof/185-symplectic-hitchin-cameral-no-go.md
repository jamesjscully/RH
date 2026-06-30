# 185 - Hitchin/cameral data does not construct the Laurent carrier

Status: no-go + symplectic Hitchin-system / cameral-cover repair deletion,
2026-06-20. Forty-eighth cycle of the doc-137 construction arc. Doc 184
killed using Springer resolution or Steinberg variety convolution of the
appended dual type-B group as the carrier algebra. This document tests the
next repair: use Hitchin-system, spectral-curve, or cameral-cover data
attached to that dual group as the missing carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_hitchin_cameral_no_go` (SHC1-SHC10 ALL PASS) --
exact finite-window support ranks, residual stabilizers, dual type-B
dimensions, invariant degrees, Hitchin base ranks, cameral and spectral cover
degrees, axis-choice counts, missing support-supplied inputs, missing
boundary/torsor data, residual choices, and control-formability checks.

## 1. Purpose

After doc 184, the Springer/Steinberg repair can say:

```text
Springer/Steinberg is too finite.
Use the Hitchin system instead.
The spectral curve or cameral cover supplies the correspondence carrier.
```

This is distinct from doc 184. Hitchin/cameral data adds a base curve, a
canonical twist, spectral parameters, and generic abelian fibers. The test is
whether that package is support-supplied and whether it selects the missing
rank-one Laurent boundary datum.

In this support setting it does not. The Hitchin base is rank-m invariant
polynomial data with degrees 2,4,...,2m. The cameral cover has Weyl degree,
and the standard vector spectral cover has degree 2m+1. The package also
requires a base curve and line bundle data not supplied by the finite support
building. Choosing one invariant, sheet, or coordinate is another selector.

This document is local. It does not reject carrier-native Hitchin, spectral,
cameral, or Arakelov-geometric data. It rejects only invoking Hitchin/cameral
geometry after appending dual-group data to the finite support symplectic
building.

## 2. Lemma

```text
Lemma 185.1 (support Hitchin/cameral data is not a Laurent carrier).
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

The finite Weyl group orders are:

  8,48,3840,185794560.

The Hitchin base has one invariant generator in each type-B degree:

  m=2: 2,4;
  m=3: 2,4,6;
  m=5: 2,4,6,8,10;
  m=9: 2,4,6,8,10,12,14,16,18.

Thus the Hitchin base ranks are:

  2,3,5,9.

The cameral cover degrees are Weyl degrees:

  8,48,3840,185794560.

The standard vector spectral cover degrees are:

  5,7,11,19.

The generic Hitchin fiber ranks still mirror the group ranks:

  2,3,5,9.

Therefore Hitchin/cameral data is not a selected Laurent axis. Selecting one
invariant coordinate or sheet is another choice:

  fundamental choices = 2,3,5,9;
  signed choices      = 4,6,10,18.

The finite support building supplies no Satake category, no dual group, no
base curve, no canonical bundle, no Hitchin base, no cameral cover, no
spectral curve, no preferred Hitchin axis, no carrier boundary map, no
Laurent generator, and no torsor splitter. The graph/endpoint/idempotent/
twist choices and the bottom/shear/torsor obstructions remain, and the same
Hitchin/cameral package is formable on controls.

Therefore support Hitchin-system / cameral-cover data is not construction-
grade R1 carrier correspondence algebra or Laurent boundary glue. A
surviving route must construct the base geometry, Hitchin/cameral/spectral
data if used, selected Laurent axis, endpoint, boundary map, Laurent twist,
and torsor splitter as carrier-native correspondence data and prove
DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_HITCHIN_CAMERAL__RANK_M_EXTERNAL_GEOMETRY_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_hitchin_cameral_no_go` verifies the finite-window
model.

SHC1-SHC3 record the unchanged support ranks, Tate windows, residual
stabilizers, dual type-B dimensions, positive-root counts, and Weyl degrees:

```text
r = 3,4,6,10;
dual ranks = 2,3,5,9;
|W| = 8,48,3840,185794560.
```

SHC4 records that the Hitchin base is rank-m invariant-polynomial data with
degrees:

```text
m=2: 2,4;
m=3: 2,4,6;
m=5: 2,4,6,8,10;
m=9: 2,4,6,8,10,12,14,16,18.
```

SHC5 records the cameral and spectral cover degrees:

```text
cameral: 8,48,3840,185794560;
spectral: 5,7,11,19.
```

SHC6 records that selecting one Hitchin invariant or sheet axis is another
choice:

```text
fundamental choices = 2,3,5,9;
signed choices      = 4,6,10,18.
```

SHC7 records that the Satake category, dual group, Hitchin base, base curve,
canonical bundle, cameral cover, and spectral curve are not support-supplied.

SHC8 records that Hitchin/cameral data does not construct the shift, boundary
map, or torsor splitter.

SHC9 records that support choices and base obstructions remain: the DMP
bottom class still has no degree -2 support, the support choices persist,
and no carrier multiplication or torsor splitter is supplied.

SHC10 applies the carrier guard: appending a base curve, canonical bundle,
spectral parameter, and Hitchin/cameral package to finite support data is
external geometry formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-185:
  NEWLY CLOSED THIS CYCLE:
    - Hitchin system / cameral cover / spectral curve of the appended dual
      group as carrier correspondence algebra, Laurent axis, boundary glue,
      or torsor splitter (doc 185).

  PREVIOUSLY CLOSED:
    - docs 138-184 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, Schubert-convolution, Satake-dual,
      principal-cocharacter, Kostant-section, and Springer/Steinberg repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs any Hitchin/cameral/spectral data internally if such data is
      used, and whose carrier-native map produces the endpoint, boundary map,
      Laurent twist/axis, torsor splitter, shift operator, and weight>=1
      datum while making DH/Epstein controls fail at named points.
```

R1 is still open. Hitchin/cameral data is admissible only if the carrier
constructs the base geometry, dual group if used, Hitchin base, cameral or
spectral cover, selected Laurent axis, endpoint, boundary map, Laurent twist,
and torsor splitter. Invoking the Hitchin system of an inserted dual group is
bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SHC.1 Hitchin system as carrier construction
  A proposal invokes a Hitchin system after appending a dual group to
  support-building data. The base curve, twist, and Hitchin base are inserted
  geometry unless the carrier constructs them.

KILL-SHC.2 Hitchin base as Laurent line
  A proposal reads the Hitchin base as the line. The base has rank m with
  invariant degrees 2,4,...,2m, not a selected rank-one Laurent axis.

KILL-SHC.3 cameral or spectral cover as carrier shift
  A proposal reads cameral or spectral sheets as the shift. The covers have
  finite degrees |W| or 2m+1 and do not construct a bi-infinite Laurent
  generator.

KILL-SHC.4 invariant coordinate as Laurent axis
  A proposal chooses one Hitchin invariant coordinate, one sheet, or one
  weight direction. That is a selector unless the carrier constructs the
  axis.

KILL-SHC.5 Hitchin data as boundary map or torsor splitter
  A proposal reads generic fibers, cameral data, spectral curves, or
  invariant degrees as the endpoint, boundary map, Laurent twist, or
  b/phi(b)=c splitter. The package supplies no such map.

KILL-SHC.6 Hitchin/cameral package formable on controls
  Appending a base curve, line bundle, dual group, Hitchin base, cameral
  cover, and spectral curve to finite support data is a support operation.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 48 = doc 185:
  N1B_SYMPLECTIC_HITCHIN_CAMERAL__RANK_M_EXTERNAL_GEOMETRY_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: the Hitchin /
cameral / spectral-curve package of an appended dual group cannot be used as
the missing Laurent carrier.

What remains: the route must produce carrier-native base geometry and
Hitchin/cameral data or leave the Satake-dual branch. Rank-m invariant
geometry with finite covers is not enough.
```
