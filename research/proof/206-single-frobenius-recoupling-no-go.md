# 206 - Single-Frobenius recoupling does not construct End(S^2/Z)

Status: no-go + count/radius recoupling boundary, 2026-06-20.
Sixty-ninth cycle of the doc-137 construction arc. Docs 204-205
classified two finiteness repairs: regularized determinant and type II_1
trace. Both supply trace/count finiteness but not carrier-native radius.
This document tests the next repair: ask for one archimedean
Frobenius-style operator `F_inf` that recouples count and radius the way
finite-field Frobenius does.

```text
single archimedean Frobenius
  = trace/count source + eigenvalue radius source
  = End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_single_frobenius_recoupling_no_go` (SFR1-SFR6 ALL PASS) --
the finite-field anchor separates count scale from radius; determinant
fixes only geometric mean, not uniform modulus; archimedean field
automorphisms are isometries rather than q-power maps; graded/tensor
repairs split count from radius; DH has no Frobenius count-source; and no
square/Rosati/R1 data is built.

Adjacent witness, lead-reran this cycle:
`recouple_count_radius` (exit 0) -- the older probe showing that the
finite-field identity uses two facts, `|det F|=q^g` and `F F^dag=q Id`;
the second is the polarization/Rosati relation, not a consequence of trace
or determinant.

## 1. Purpose

Over `F_q`, the same Frobenius map appears to do two jobs:

```text
count:   #C(F_{q^n}) = q^n + 1 - Tr(F^n | H^1)
radius:  |alpha_i| = sqrt(q)
```

The tempting repair says that the archimedean place should have one
operator `F_inf` whose trace gives the count and whose eigenvalue modulus
forces the radius. If true, this would bypass the split found in docs
132-135 and strengthened in docs 204-205.

The test is anchored at the finite-field model. There, the apparent
single-q coupling actually uses two separate conditions:

```text
|det F| = q^g       count scale / geometric mean
F F^dag = q Id      polarization / uniform radius
```

The first is determinant data. The second is the purity/Rosati relation.
The question is whether a single archimedean operator can derive the
second from the first without importing the missing positive Rosati.

This document is local. It rejects only the shortcut:

```text
one archimedean Frobenius-style operator itself recouples count and radius
and therefore constructs End(S^2/Z).
```

## 2. Lemma

```text
Lemma 206.1 (Single-operator count/radius recoupling is not construction).

The finite-field count scale `|det F|=q^g` fixes only the geometric mean of
the Frobenius eigenvalue moduli. It does not imply the uniform bound
`|alpha_i|=sqrt(q)` for every eigenvalue. Off-purity configurations can
preserve determinant/count scale while breaking radius.

The reason finite-field Frobenius couples the two sides is not that trace
alone controls modulus. It is that `x -> x^q` is a q-power ring
endomorphism of a finite field: the same arithmetic q is field size for
fixed-point counting and power/scaling for the Tate-weight side.

At the archimedean place, continuous field automorphisms are the identity
on R and identity/conjugation on C. They are isometries with modulus 1.
The modulus character supplies scaling, but it is not a field endomorphism
and has no fixed-point count. Thus count and scale are carried by different
archimedean operations.

Graded/tensor repairs `F_inf = U * m` make the split explicit: the count
or phase data lives in the unitary `U` factor, while the radius lives in
the scalar `m`. The trace data does not determine `m`; forcing
`m=sqrt(q)` is exactly imposing `F_inf F_inf^dag=q Id`, the missing
polarization/Rosati relation.

Consequently single-Frobenius recoupling constructs no carrier-native
q-power map, no uniform modulus bound, no DH-killing carrier, no finite
constant field, no square-side iota/properness theorem, no square H2,
intersection form, correspondence algebra, Frobenius graph, Laurent
boundary data, torsor splitter, DD.4 weight>=1 datum, or positive Rosati.

Therefore a single archimedean Frobenius-style recoupling package cannot
itself be promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_SINGLE_FROBENIUS_RECOUPLING__COUNT_NOT_RADIUS_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_single_frobenius_recoupling_no_go` verifies the R1 gate,
with `recouple_count_radius` rerun as the adjacent witness.

SFR1 records the anchor. In genus `g=2`, `q=7`, both the pure and
off-purity configurations have `|det F|=49=q^g`. The pure configuration
has radius deviation `0`; the off-purity configuration has radius
deviation `1.587451`. Thus count scale can be preserved while radius is
broken.

SFR2 records the determinant failure. For the off-purity configuration,
the geometric mean modulus is still `sqrt(q)=2.645751`, but the individual
moduli are not all `sqrt(q)`. Determinant is the geometric-mean condition,
not the per-eigenvalue equality condition.

SFR3 records the archimedean type failure. The continuous field
endomorphisms at infinity are:

```text
R: identity
C: identity, conjugation
```

All have eigenvalue modulus `1`. The scaling/modulus character is not a
field endomorphism, and therefore is not a fixed-point counting map.

SFR4 records the graded repair failure. In `F_inf=U*m`, `U` is unitary and
stores the count/phase trace data; changing `m` changes the eigenvalue
moduli from `2.6458` to `3.9686` while leaving `Tr(U^n)` unchanged. The
grading does not couple count to radius. It isolates them.

SFR5 records the carrier guard. DH has no Euler product and no Frobenius or
Satake data, so there is no operator whose trace is a Lefschetz count-source
to recouple. A claimed DH-instantiable recoupling is therefore not the zeta
carrier.

SFR6 records the construction failure: no carrier-native q-power map,
single count/radius operator, polarization relation, uniform modulus bound,
DH-killing carrier, finite constant field, square-side `iota`/properness,
square H2, intersection form, correspondence algebra, Frobenius graph,
positive Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum
is constructed.

## 4. Impact on R1

```text
R1 after docs 138-206:
  NEWLY CLOSED THIS CYCLE:
    - single archimedean Frobenius / count-radius recoupling as
      End(S^2/Z), independent determinant-to-radius forcing,
      archimedean q-power ring endomorphism, graded/tensor count-radius
      recoupling, carrier-native q-power map, polarization relation,
      finite constant field, Frobenius/base size, square-side
      iota/properness, square H2/intersection form, Laurent boundary data,
      torsor splitter, DD.4 weight>=1 datum, or positive Rosati (doc 206).

  STILL ADMISSIBLE:
    - a carrier that constructs a genuine q-power-like map at infinity,
      including fixed-point/count and scaling roles, rather than naming one
      operator after Frobenius;
    - a carrier that constructs the polarization relation
      `F F^dag=q Id` internally, rather than deriving it from determinant;
    - a non-product compactified square whose correspondence algebra
      constructs the Rosati relation before any radius conclusion is read.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The phrase "single Frobenius" is now disciplined: it is
admissible only if the carrier constructs the q-power/fixed-point/scaling
structure and the Rosati relation. An operator abstraction, determinant
normalization, or graded scalar factor does not unblock R2.

## 5. Kill Conditions

```text
KILL-SFR.1 determinant/count scale as radius
  A proposal identifies `|det F|=q^g` with purity. Kill it unless it proves
  the per-eigenvalue bound `|alpha_i|=sqrt(q)`.

KILL-SFR.2 geometric mean as uniform modulus
  A proposal reads `(det F)^{1/2g}=sqrt(q)` as the radius. Kill it: this is
  only the geometric mean of moduli.

KILL-SFR.3 archimedean field automorphism as q-power map
  A proposal treats identity or conjugation at infinity as the q-power map.
  Kill it: archimedean field automorphisms are isometries with modulus 1.

KILL-SFR.4 graded/tensor `U*m` as recoupling
  A proposal places count in `U` and radius in a scalar `m`. Kill it unless
  the carrier determines `m` internally.

KILL-SFR.5 polarization relation imported as proof
  A proposal imposes `F F^dag=q Id` after the fact. Kill it unless the
  carrier constructs that relation as structure.

KILL-SFR.6 single operator as End(S^2/Z)
  A proposal promotes one operator directly to the square correspondence
  algebra. Kill it unless it constructs square H2, intersection form,
  correspondences, Frobenius graph, Laurent boundary data, DD.4 weight>=1
  datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 69 = doc 206:
  N1B_SINGLE_FROBENIUS_RECOUPLING__COUNT_NOT_RADIUS_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
single-operator Frobenius language does not recouple count and radius unless
it constructs the missing q-power/Rosati structure.

What remains: construct a carrier-native q-power/fixed-point/scaling map;
construct the polarization/Rosati relation `F F^dag=q Id`; construct an
indecomposable compactified square correspondence; solve square-side
iota/properness; or return to the in-house PFD/Xbar DD.4 weight>=1
obstruction.
```
