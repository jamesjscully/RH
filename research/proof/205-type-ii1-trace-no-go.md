# 205 - Type II_1 trace does not construct End(S^2/Z)

Status: no-go + continuous-dimension/count-radius split boundary,
2026-06-20. Sixty-eighth cycle of the doc-137 construction arc. Doc 204
classified trace-class compactness: it supplies trace/count finiteness, but
not the radius/purity datum. This document tests the next repair: replace
trace-class compactness by a type II_1 factor trace, i.e. finite
Murray-von Neumann continuous dimension.

```text
type II_1 trace / continuous dimension
  = count-radius coupling
  = End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_type_ii1_trace_no_go` (II1T1-II1T6 ALL PASS) -- the II_1
trace is a genuinely different finiteness type; pure finite-field examples
make `sqrt(tau(|a|^2))` look like the radius; trace-preserving off-purity
redistributions keep `tau(|a|^2)=q` while breaking uniform modulus;
normalized continuous dimension is scale-free; the II_1 trace is not
DH-distinguishing; and no square/Rosati/R1 data is built.

Adjacent witness, lead-reran this cycle:
`von_neumann_typeII1` (exit 0) -- the older II_1 probe: continuous dimension
supplies averaged moments/count data but not the radius bound.

## 1. Purpose

Doc 204 left one attractive repair: use a finiteness notion stronger or
more intrinsic than a regularized determinant. Type II_1 factors have a
faithful normal trace with `tau(1)=1`; projections have continuous
Murray-von Neumann dimension. This is not a finite field cardinality, not a
continuum size, not a length, and not a discrete index. It is a real new
type of finiteness.

The model is concrete:

```text
M = L(Z) ~= L^infinity(S^1),
tau(f) = Haar mean of f.
```

Frobenius eigenvalues can be realized as the essential range of an
affiliated multiplication operator `a`. Then

```text
tau(a^n)      = average of alpha_i^n,
tau(|a|^2)   = average of |alpha_i|^2.
```

For pure finite-field Frobenius data, `tau(|a|^2)=q`, so
`sqrt(tau(|a|^2))=sqrt(q)`. The issue is that this is an average, not the
uniform radius condition. A non-pure configuration can preserve the same
average while breaking `|alpha_i|=sqrt(q)`.

This document is local. It rejects only the shortcut:

```text
type II_1 trace / continuous dimension itself supplies the radius and
constructs End(S^2/Z).
```

## 2. Lemma

```text
Lemma 205.1 (Continuous dimension averages the radius data).

The type II_1 trace is a genuine finiteness type and supplies averaged
spectral moments. In pure finite-field examples, tau(|a|^2)=q, so its
square root equals sqrt(q).

However, tau(|a|^2) is an L2 average of moduli. There exist off-purity
redistributions preserving tau(|a|^2)=q while moving eigenvalues off the
circle |alpha|=sqrt(q). Thus the trace does not enforce the uniform
modulus bound.

Moreover, normalized continuous dimension is scale-free: scaling the
operator changes the spectral radius but leaves the range projection
dimension unchanged. The same II_1 trace package can be formed over DH
spectral data, so it is not a zeta-only carrier guard.

Consequently type II_1 trace data constructs no carrier-native purity,
uniform radius bound, archimedean monodromy N, square-side
iota/properness theorem, square H2, intersection form, correspondence
algebra, Frobenius graph, Laurent boundary data, torsor splitter, DD.4
weight>=1 datum, or positive Rosati involution.

Therefore type II_1 trace / continuous dimension cannot itself be promoted
to End(S^2/Z).
```

Verdict label:

```text
N1B_TYPE_II1_TRACE__AVERAGE_NOT_RADIUS_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_type_ii1_trace_no_go` verifies the R1 gate, with
`von_neumann_typeII1` rerun as the adjacent witness.

II1T1 records the positive fact: II_1 trace is a genuinely different
finiteness type and passes the earlier finite-cardinality type obstruction.

II1T2 records the attractive finite-field anchor. In pure examples,
`tau(|a|^2)=q` and the radius deviation is zero.

II1T3 records the decisive split. The following off-purity configurations
preserve the same trace value while breaking radius:

```text
E_ordinary_q5: tau=5, radius deviation 1.7889
genus2_q9:    tau=9, radius deviation 2.4
genus2_q2:    tau=2, radius deviation 1.1314
```

Thus `sqrt(tau(|a|^2))` is an average, not the uniform modulus bound.

II1T4 records scale-freeness. Scaling the operator changes the maximum
modulus from `3` to `6` or `1.5`, while the normalized range projection
dimension remains `1`.

II1T5 records the carrier guard failure. The II_1 trace package can be
formed over spectral measures without an Euler product, so it does not die
on DH at the relevant point.

II1T6 records the carrier failure: no carrier-native purity, uniform
modulus bound, archimedean monodromy `N`, Weil positivity theorem, DH-killing
carrier, finite constant field, square-side `iota`/properness, square H2,
intersection form, correspondence algebra, Frobenius graph, positive
Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-205:
  NEWLY CLOSED THIS CYCLE:
    - type II_1 trace / continuous dimension as End(S^2/Z), independent
      count-radius coupling, carrier-native uniform modulus, archimedean
      monodromy N, DH-killing carrier, finite constant field,
      Frobenius/base size, square-side iota/properness, square
      H2/intersection form, Laurent boundary data, torsor splitter, DD.4
      weight>=1 datum, or positive Rosati (doc 205).

  STILL ADMISSIBLE:
    - a von Neumann or spectral construction that also constructs
      carrier-native uniform modulus/purity and kills DH, rather than only
      averaged moments;
    - a nuclear/trace-class construction that also constructs purity or the
      archimedean monodromy/Rosati datum carrier-natively, rather than only
      the trace/count;
    - a future F1 or family construction that manufactures a finite
      constant/residue-field cardinality at the archimedean place without
      selecting a finite level externally;
    - a non-product compactified square whose middle correspondence is
      indecomposable rather than Kunneth-factored.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. Type II_1 trace is a real positive datum only on the
averaged count axis. It does not construct the radius/purity or square/Rosati
axis. R2 remains locked.

## 5. Kill Conditions

```text
KILL-II1T.1 tau(|a|^2)=q as uniform radius
  A proposal identifies sqrt(tau(|a|^2)) with the radius. Kill it unless it
  proves the uniform modulus bound, not only the L2 average.

KILL-II1T.2 continuous dimension as scale
  A proposal uses normalized II_1 dimension to recover q. Kill it: the
  dimension is scale-free under operator rescaling.

KILL-II1T.3 averaged moments as purity
  A proposal treats tau(a^n) moments as the purity datum. Kill it unless it
  also constructs the modulus bound for every spectral point.

KILL-II1T.4 II_1 trace as carrier guard
  A proposal claims the II_1 trace distinguishes zeta from DH. Kill it: the
  trace package is formable over spectral measures without an Euler product.

KILL-II1T.5 II_1 trace as End(S^2/Z)
  A proposal promotes type II_1 trace directly to the square correspondence
  algebra. Kill it unless it constructs square H2, intersection form,
  correspondences, Frobenius graph, and Rosati.

KILL-II1T.6 continuous dimension as DD.4 weight>=1
  A proposal treats continuous dimension as the DD.4 weight datum. Kill it
  unless the carrier constructs the Laurent boundary and weight>=1
  self-duality datum.
```

## 6. Board

```text
doc-137 R1, cycle 68 = doc 205:
  N1B_TYPE_II1_TRACE__AVERAGE_NOT_RADIUS_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
continuous dimension is genuine finiteness, but it averages the moduli and
does not force uniform radius or Rosati positivity.

What remains: construct uniform modulus/purity/Rosati on the spectral
carrier; construct a finite base-size marker carrier-natively; construct an
indecomposable compactified square correspondence; solve square-side
iota/properness; or return to the in-house PFD/Xbar DD.4 weight>=1
obstruction.
```
