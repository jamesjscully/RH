# 225 - Perfect-module Morita envelopes do not construct the square

Status: no-go + perfect-module/dg-Morita-envelope boundary, 2026-06-20.
Eighty-eighth cycle of the doc-137 construction arc. Doc 224 killed
Karoubi/pseudo-abelian and semisimple completion of a presented/numerical
carrier as square construction. This document tests the next categorical
repair: replace the carrier by the dg category of perfect modules, or by a
noncommutative motive/additive invariant, and use Morita invariance to get
the correct projectors and traces.

```text
presented/numerical/Karoubi carrier algebra A
  -> Perf(A) / dg Morita envelope / noncommutative motive
  -> Morita-invariant traces and projectors
  -> square correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_perfect_morita_envelope_no_go` (PME1-PME6 ALL PASS) -- Morita
stabilization hides matrix overproduction; additive traces such as `HH0` and
`K0` do not determine finite-field count anchors; perfect modules over
`Q[F]` do not construct the NS degree slots; finite windows admit ghost
perfect summands; the same envelope is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_karoubi_semisimple_completion_no_go` (KSC1-KSC6 ALL PASS) and
`prime_int_n1b_numerical_gns_quotient_no_go` (NGQ1-NGQ6 ALL PASS).

## 1. Purpose

Doc 224 says closure under idempotents and semisimplification is not square
construction. The next categorical repair is stronger:

```text
the real object is not A but Perf(A), or its noncommutative motive;
Morita invariance removes the matrix-choice problem;
additive traces recover the correspondence data.
```

This still does not construct `End(S^2/Z)`. `Perf(A)` is a closure operation
around an algebra already supplied. If `A` is a presented or numerical
carrier, the perfect-module envelope inherits that import. Morita invariance
also cuts the wrong way: it deliberately identifies `A` and `Mat_r(A)`, so it
hides matrix overproduction rather than constructing the selected square
correspondences. Additive invariants such as `HH0` or `K0` are useful traces
of a category, but they are not the NS triple `(d1,z,d2)`, the degree maps,
the projection formula, or the positive Rosati pairing.

This document rejects only the shortcut:

```text
Perf(A), dg Morita completion, or a noncommutative motive of relation data
constructs the square correspondence carrier required by End(S^2/Z).
```

It does not reject a future carrier-native dg category of proper
correspondences whose objects, duality, degree maps, and Rosati pairing have
already been constructed.

## 2. Lemma

```text
Lemma 225.1 (Perfect-module envelopes are Morita closure, not square data).

For the finite-field q=7, Tr(F)=1 anchor, let A=Q[F], a quadratic algebra.
For r=1,2,5,

    dim_Q Mat_r(A) = 2, 8, 50,

but Morita-invariant traces remain

    dim HH0(Mat_r(A)) = 2,
    rank K0(Mat_r(A)) = 1.

Thus the dg Morita envelope identifies matrix stabilizations while the raw
endomorphism size changes. It does not choose the carrier correspondence
algebra or the selected maps inside it.

Moreover, coarse additive Morita traces do not determine the finite-field
count anchor. The q=7, Tr(F)=1 and q=5, Tr(F)=2 anchors have the same profile

    (dim A, dim HH0, rank K0) = (2,2,1),

but different first count windows:

    7, 63, 364, 2331
    4, 32, 148, 640.

Even for fixed z-component algebra Q[F], perfect modules over Q[F] do not
construct the NS degree slots. Keeping the same F but changing the formal
triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10,

while Perf(Q[F]) is unchanged. The missing data are the carrier-native fiber
degrees and intersection pairing, not the perfect-module closure of the
z-algebra.

Finite windows are still not safe: a 5-cycle ghost summand has zero traces in
powers 1,2,3,4 but changes the fifth count by 5, and contributes an extra
perfect summand. The same construction is formable on arbitrary control
companion data with no Euler product, Satake parameters, rep_NS, square
carrier, or positive Rosati.

Consequently Perf(A), dg Morita envelopes, and noncommutative motives of
presented/numerical relation data construct no rep_NS, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, Frobenius graph, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_PERFECT_MORITA_ENVELOPE__MORITA_CLOSURE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_perfect_morita_envelope_no_go` verifies the six gates.

PME1 records the Morita stabilization problem. For matrix ranks `1,2,5` over
the quadratic finite-field anchor algebra:

```text
raw End dimensions = 2, 8, 50,
HH0 dimensions     = 2, 2, 2,
K0 ranks           = 1, 1, 1.
```

The Morita envelope suppresses matrix overproduction; it does not construct
the correct square correspondence algebra.

PME2 records additive-trace insufficiency. The q=7 and q=5 anchors have the
same coarse profile `(2,2,1)` but different count windows. A Morita/additive
profile cannot be promoted to a count carrier.

PME3 records the NS-degree-slot failure. The same z-algebra `Q[F]` supports
different formal triples with different `Delta.Gamma` values. Perfect modules
over `Q[F]` do not construct the missing `(d1,z,d2)` correspondence data.

PME4 records finite-window ghost survival. A 5-cycle ghost preserves the first
four traces, contributes an extra perfect summand of `K0` rank `5`, and
changes count 5 by `5`.

PME5 records control formability. The control companion with profile

```text
(dim A, dim HH0, rank K0, discriminant) = (2,2,1,-31)
```

has a perfectly valid perfect-module/Morita envelope and count window
`8,112,1064`, but no Euler product, Satake parameters, `rep_NS`, square, or
positive Rosati.

PME6 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native perfect
category, carrier-native degree maps, carrier-native pairing, Frobenius graph,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-225:
  NEWLY CLOSED THIS CYCLE:
    - Perf(A), dg Morita completion, noncommutative motive/additive-invariant
      envelopes of a presented or numerical carrier as square construction,
      Morita invariance as a solution to matrix overproduction, HH0/K0-style
      traces as count/degree/pairing construction, and finite perfect-module
      windows as carrier determination (doc 225).

  STILL ADMISSIBLE:
    - a carrier-native proper dg category of actual correspondences, if the
      square carrier constructs it before Morita invariance is invoked;
    - additive or localizing invariants used only after rep_NS, degree maps,
      pairing, projection formula, and Rosati are already carrier-native;
    - a theorem excluding ghost perfect summands from the actual carrier;
    - controls killed at carrier formation, not after passing to invariants.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the perfect-module/dg Morita envelope
repair: Morita closure is not construction of the square carrier whose data it
would be allowed to invariantize.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PME.1 Perf(A) as square construction
  A proposal replaces a presented/numerical algebra A by Perf(A) and calls the
  result the square. Kill it unless A is already the carrier-native proper
  correspondence algebra of the square.

KILL-PME.2 Morita invariance as selector
  A proposal uses dg Morita invariance to remove matrix choices. Kill it
  unless the selected correspondences, degree maps, and pairing were
  constructed before passing to the Morita envelope.

KILL-PME.3 additive trace as count/degree construction
  A proposal uses HH0, K0, THH, or another additive/localizing invariant as
  the count or NS degree carrier. Kill it unless the invariant is applied to
  an already constructed square correspondence category.

KILL-PME.4 finite perfect-module window
  A proposal verifies finite trace or invariant windows after passing to
  Perf(A). Kill it unless ghost perfect summands are excluded carrier-natively.

KILL-PME.5 control survival
  A proposal's perfect-module/Morita envelope can be formed on arbitrary
  control operators or count windows. Kill it unless controls die at carrier
  formation.
```
