# 208 - Local purity carriers do not construct End(S^2/Z)

Status: no-go + purity-carrier typing boundary, 2026-06-20.
Seventy-first cycle of the doc-137 construction arc. Docs 206-207
classified two Frobenius repairs: a single operator does not recouple count
and radius, and rigid Tannakian reconstruction does not force compactness.
This document tests the next repair: treat purity/radius as a local
operation on Euler factors.

```text
local Euler factor
  -> edge / abscissa
  -> local square-root purity
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_local_purity_carrier_no_go` (LPC1-LPC6 ALL PASS) --
function-field global curves have weight-1 carriers; local factors have
edge but no weight-1 purity carrier; the archimedean factor has no finite
weight-1 numerator; zeta purity is not a per-prime condition; DH fails
before the carrier question; and no square/Rosati/R1 data is built.

Adjacent witness, lead-reran this cycle:
`purity_carrier` (exit 0) -- the older M2d typing probe: `rad_edge` is
well-typed locally for zeta, but `rad=(.)^{1/2} o edge` is not well-typed
per prime because the square-root/purity step needs a global weight-1
carrier `gr^W_1`.

## 1. Purpose

Over a function field, purity is a theorem about a geometric carrier:
`H^1(C)`. The local Euler factors are point data; the curve globally
supplies the weight-1 cohomology on which purity acts. The tempting zeta
repair says:

```text
Each prime factor has an edge.
Take the square root locally.
This supplies the center/radius.
```

The issue is that the edge and the purity step have different typing
requirements. The edge is local: the local product supplies the abscissa.
The square-root/purity step needs a weight-1 carrier `gr^W_1`. A local
factor with numerator degree zero has no such input.

This document is local. It rejects only the shortcut:

```text
local Euler factors themselves carry the weight-1 purity datum and therefore
construct End(S^2/Z).
```

## 2. Lemma

```text
Lemma 208.1 (Purity has no local carrier over zeta).

The edge datum of zeta is local: prime Euler factors give the product
abscissa. Thus `rad_edge : LocFac -> G_m` is well-typed.

The square-root/purity step is different. It needs a weight-1 graded carrier
`gr^W_1`, detected in the numerator degree of the relevant zeta factor.
For a function-field global curve of genus g, the global numerator degree is
`2g`, so `H^1(C)` supplies a weight-1 carrier. But for function-field local
factors at closed points, the numerator degree is zero. For zeta prime
factors `(1-p^-s)^-1`, the numerator degree is also zero. The archimedean
factor `Gamma_R(s)` is an infinite product and has no finite weight-1
numerator.

Therefore the local purity functor

    `rad = (.)^{1/2} o edge`

is not well-typed per prime over zeta. It can act only after a global glued
object supplies `gr^W_1`. Over `F_q` the curve supplies that carrier. Over
`Z`, that global carrier is the missing `S^2/Z` / End construction.

DH has a functional equation but no Euler product, hence no local factors,
no product edge, and no local-factor assembly of a weight-1 carrier. It
fails before the zeta carrier question.

Consequently local purity data constructs no local or global `gr^W_1`
carrier, no carrier-native purity theorem, no q-power map, no uniform
modulus bound, no DH-killing carrier, no finite constant field, no
square-side iota/properness theorem, no square H2, intersection form,
correspondence algebra, Frobenius graph, Laurent boundary data, torsor
splitter, DD.4 weight>=1 datum, or positive Rosati.

Therefore local purity carriers cannot themselves be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_LOCAL_PURITY_CARRIER__NO_GRW1_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_local_purity_carrier_no_go` verifies the R1 gate, with
`purity_carrier` rerun as the adjacent witness.

LPC1 records the function-field global anchor. For `g=1,2,3`, the global
numerator degrees are:

```text
2, 4, 6.
```

Thus a global curve supplies a weight-1 carrier.

LPC2 records the local failure. Function-field local factors at degrees
`1,2,3` all have numerator degree `0`; zeta prime factors for
`p=2,3,5,7` also have numerator degree `0`. In both cases the edge is
local, but the purity carrier is absent.

LPC3 records the archimedean failure. `Gamma_R(s)` is an infinite product
of gamma poles, not a finite-degree weight-1 numerator.

LPC4 records the typing split. `rad_edge` is locally well-typed for zeta,
but `rad=(.)^{1/2} o edge` is not well-typed per prime because no local
`gr^W_1` exists. The global glued carrier over `Z` remains open.

LPC5 records the carrier guard. DH has no Euler product, no local factors,
no edge from a product, and no local-factor route to a weight-1 carrier.

LPC6 records the construction failure: no local or global `gr^W_1` carrier,
carrier-native purity theorem, q-power map, uniform modulus bound,
DH-killing carrier, finite constant field, square-side `iota`/properness,
square H2, intersection form, correspondence algebra, Frobenius graph,
positive Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum
is constructed.

## 4. Impact on R1

```text
R1 after docs 138-208:
  NEWLY CLOSED THIS CYCLE:
    - local purity carrier as End(S^2/Z), per-prime `gr^W_1`, local
      square-root purity, archimedean finite weight-1 numerator,
      local-factor purity as carrier-native uniform modulus, finite
      constant field, Frobenius/base size, square-side iota/properness,
      square H2/intersection form, Laurent boundary data, torsor splitter,
      DD.4 weight>=1 datum, or positive Rosati (doc 208).

  STILL ADMISSIBLE:
    - a global glued carrier that actually constructs `gr^W_1` before
      applying purity;
    - a non-product compactified square whose correspondence algebra
      supplies the weight-1 carrier and the Rosati relation internally;
    - a zeta-native purity construction that kills DH/Epstein at the
      carrier-formation step, not merely at the Euler-product edge.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. This cycle sharpens the order of construction: build the
global weight-1 carrier first; only then can purity/radius be a theorem
about it. R2 remains locked.

## 5. Kill Conditions

```text
KILL-LPC.1 local edge as local purity
  A proposal treats the local edge/abscissa as the square-root purity datum.
  Kill it unless it also supplies a local weight-1 carrier.

KILL-LPC.2 per-prime `gr^W_1`
  A proposal claims a prime factor has weight-1 cohomology. Kill it:
  `(1-p^-s)^-1` has numerator degree zero.

KILL-LPC.3 archimedean gamma as finite weight-1 numerator
  A proposal uses `Gamma_R(s)` as a finite `H^1` numerator. Kill it: it is
  an infinite gamma product, not a finite carrier.

KILL-LPC.4 local factors assemble purity without a global object
  A proposal applies purity before constructing the glued `gr^W_1`. Kill it:
  over function fields the curve supplies `H^1` globally first.

KILL-LPC.5 purity carrier as DH guard
  A proposal says local purity distinguishes zeta from DH. Kill it unless
  the zeta carrier is constructed; DH already fails earlier at no Euler
  product/local factors.

KILL-LPC.6 local purity carrier as End(S^2/Z)
  A proposal promotes the typing slot directly to the square correspondence
  algebra. Kill it unless it constructs square H2, intersection form,
  correspondences, Frobenius graph, Laurent boundary data, DD.4 weight>=1
  datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 71 = doc 208:
  N1B_LOCAL_PURITY_CARRIER__NO_GRW1_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper typing theorem:
purity is not a per-prime operation over zeta; it requires a global
weight-1 carrier first.

What remains: construct the global `gr^W_1` carrier; construct the
q-power/fixed-point/scaling carrier; construct the polarization/Rosati
relation `F F^dag=q Id`; construct an indecomposable compactified square
correspondence; solve square-side iota/properness; or return to the
in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
