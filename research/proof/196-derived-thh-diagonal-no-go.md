# 196 - Derived THH diagonal does not construct the square carrier

Status: no-go + derived/normed abutment shortcut deletion, 2026-06-20.
Fifty-ninth cycle of the doc-137 construction arc. Doc 195 killed promoting
the strict CC norm/MAX-face filtration itself to End(S^2/Z), while leaving
open AA's genuine derived/normed/tolerant square demand: a carrier where
norm weight and THH degree coexist. This document tests the shortcut that
uses the already-known derived diagonal abutment `THH(Z)`, together with the
AA norm-weight dictionary, as the missing square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_derived_thh_diagonal_no_go` (DTD1-DTD10 ALL PASS) -- exact
Bokstedt torsion tower, AA weight dictionary only as a dictionary, divergent
finite diagonal products, regularized diagonal constant, missing
compactified derived square/properness theorem, missing derived normed
spectral sequence, missing off-diagonal correspondences/Frobenius graph,
missing square H^2/intersection/correspondence/Rosati data, missing Laurent
boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent witness, lead-reran this cycle:
`prime_int_derived_square` (ALL PASS) -- doc 18's positive fact that
`Delta ^_{HZ^HZ} Delta = THH(Z)` gives a sign-bearing diagonal
self-intersection with value `zeta'(0) = -1/2 log(2pi)` after
regularization, and relocates the wall to compactified properness over the
sphere.

## 1. Purpose

Doc 18 built a real positive datum:

```text
Delta ^_{HZ^HZ} Delta = THH(Z),
pi_{2k-1} THH(Z) = Z/k,
<Delta,Delta>_tors = - sum_reg log k = zeta'(0).
```

Unlike the strict norm filtration, this object has the THH degree axis. It
is therefore the obvious next shortcut after doc 195:

```text
ordinary THH(Z), with AA's weight log k on degree 2k-1, is already the
derived/normed square carrier.
```

That shortcut fails. `THH(Z)` is the diagonal self-intersection tower of the
uncompactified derived square. It is not a compactified square
correspondence algebra. It has no off-diagonal graph classes, no Frobenius
correspondence, no positive Rosati, no Laurent boundary, and no torsor
splitter. Its diagonal number requires regularizing an infinite tower; the
properness theorem that would make the pairing finite-rank per class is
exactly the missing construction named in doc 18.

This document is local. It does not reject a future compactified
derived/normed/tolerant square whose spectral sequence abuts to `THH(Z)`
with a carrier-native weight filtration. It rejects only the shortcut:

```text
uncompactified THH(Z) diagonal abutment = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 196.1 (The THH diagonal abutment is not the square carrier).

The derived diagonal self-intersection over the sphere satisfies

  Delta ^_{HZ^HZ} Delta = THH(Z),

and Bokstedt's tower gives

  |pi_{2k-1} THH(Z)| = k   for k >= 1.

Thus the AA norm-weight dictionary can assign the degree-(2k-1) torsion
line weight `log k`. This is the right numerical ladder, and the witness
checks the first terms exactly.

However, the finite diagonal products diverge:

  Sum_{k <= N} log k = log(N!) -> infinity.

The constant `1/2 log(2pi)` appears only after subtracting the Stirling
divergence, equivalently after zeta regularization. This is the
uncompactified/nonproper tower described in doc 18, not a finite-rank
intersection theory.

Moreover, `THH(Z)` computes only `Delta cap Delta`. It does not construct
off-diagonal correspondence classes, a Frobenius graph, square H^2, an
intersection form, positive Rosati, Laurent boundary data, a torsor
splitter, or DD.4 weight>=1 data.

Therefore the known derived diagonal abutment cannot itself be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_DERIVED_THH_DIAGONAL__UNCOMPACTIFIED_ABUTMENT_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_derived_thh_diagonal_no_go` verifies the R1 gate, with
`prime_int_derived_square` rerun as the adjacent positive witness.

DTD1 records the positive fact: the derived diagonal self-intersection is
`THH(Z)`, with Bokstedt torsion orders `1,2,3,4,5,6,7,...`.

DTD2 records the AA compatibility: the same ladder can be assigned weight
`log k`. This is only a dictionary unless a normed derived carrier constructs
the filtration and abutment.

DTD3 records nonproperness at the most basic finite level: the partial
diagonal products grow with the cutoff.

DTD4 records that the diagonal constant is recovered only after subtracting
the Stirling divergence. The sign-bearing value is real, but it is still a
regularized infinite-tower diagonal value, not a finite-rank intersection
theory.

DTD5 records the missing construction named by doc 18: no compactified
derived square, properness theorem, or finite-rank Euler pairing is built.

DTD6 records that no derived normed spectral sequence or non-EM square
functor is constructed. Weight and degree have been aligned by dictionary,
not by a carrier.

DTD7 records that the diagonal self-intersection is not the full
correspondence algebra: no off-diagonal graph classes or Frobenius graph are
defined.

DTD8-DTD9 record the carrier failure: no square H^2, intersection form,
correspondence algebra, positive Rosati, Laurent axis, boundary map, torsor
splitter, or DD.4 weight>=1 datum is constructed.

DTD10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-196:
  NEWLY CLOSED THIS CYCLE:
    - uncompactified THH(Z) diagonal abutment, even with AA's norm-weight
      dictionary on the Bokstedt tower, as End(S^2/Z), square H^2,
      intersection form, correspondence algebra, Frobenius graph, Laurent
      boundary data, torsor splitter, DD.4 weight>=1 datum, or positive
      Rosati (doc 196).

  STILL ADMISSIBLE:
    - a compactified derived/normed/tolerant square whose spectral sequence
      abuts to THH(Z) with carrier-native weights and finite-rank
      properness/duality;
    - a non-EM square functor extracting off-diagonal correspondences and
      intersection theory, not only the diagonal tower;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The derived THH diagonal is a real positive diagonal
shadow, but not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-DTD.1 THH(Z) diagonal as End(S^2/Z)
  A proposal identifies the known THH(Z) diagonal self-intersection with the
  whole square carrier. Kill it unless it constructs off-diagonal
  correspondences and square H^2.

KILL-DTD.2 Bokstedt tower as compactified properness
  A proposal uses the infinite Z/k tower as a finite-rank intersection
  theory. Kill it unless a compactification/properness theorem truncates or
  dualizes the tower carrier-natively.

KILL-DTD.3 regularized zeta'(0) as construction
  A proposal treats the regularized diagonal constant as the correspondence
  algebra. Kill it: the constant is a diagonal shadow, not End(S^2/Z).

KILL-DTD.4 AA weight dictionary as derived normed carrier
  A proposal assigns weight log k to degree 2k-1 without constructing a
  normed derived spectral sequence. This is only a dictionary.

KILL-DTD.5 diagonal tower without Rosati/Frobenius correspondence
  A proposal gives THH(Z) but no Frobenius graph or positive Rosati. This is
  not End(S^2/Z).

KILL-DTD.6 diagonal tower without Laurent boundary/torsor
  A proposal gives THH(Z) but no Laurent axis, boundary map, torsor splitter,
  or DD.4 weight>=1 datum. This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 59 = doc 196:
  N1B_DERIVED_THH_DIAGONAL__UNCOMPACTIFIED_ABUTMENT_NOT_SQUARE_CARRIER__NO_GO.

What got built: no End object. The value is a deletion: the THH(Z)
diagonal abutment and AA weight dictionary give the right local tower, but
ordinary uncompactified THH(Z) is not the square correspondence algebra.

What remains: construct the compactified derived/normed/tolerant square with
properness and off-diagonal correspondences, build another non-EM square
functor extracting H^2/intersection/correspondence data, find a new
joint/cell-shape invariant, or return to the in-house PFD/Xbar DD.4
weight>=1 obstruction.
```
