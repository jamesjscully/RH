# 157 - Stabilizer loops are not carrier isotropy

Status: no-go + stabilizer/Laurent-loop repair deletion, 2026-06-20.
Twentieth cycle of the doc-137 construction arc. Doc 156 killed formal
groupoid completion of the support chain because the completed line groupoid
has trivial basepoint loops and category algebra `Mat_r(L)`. This document
tests the next repair: add a nontrivial stabilizer, typically `Z`, at a
support vertex and transport it across the connected support groupoid so the
category algebra has Laurent loops.

Witness, lead-reran this cycle:
`prime_int_n1b_stabilizer_loop_no_go` (SLP1-SLP11 ALL PASS) -- exact
finite-rank stabilizer-window, matrix-with-loop, corner, idempotent-choice,
obstruction, and control-formability checks.

## 1. Purpose

The groupoid-completion repair can now say:

```text
the thin groupoid has trivial loops;
therefore attach Z as isotropy;
then a basepoint has Laurent loops and a corner sees L[s^{+-1}].
```

This does create Laurent loops. But it creates them by inserting isotropy
at the support groupoid. The minimal charitable construction is the
connected transitive groupoid on the same support vertices with isotropy
`Z`; its category algebra over `L` is `Mat_r(L[s^{+-1}])`. That is matrix
overproduction with a new Laurent variable. Identifying `s` with the
external tensor variable `u` is an extra relation, not a carrier
construction.

This document is local. It does not reject carrier-native isotropy or loops.
It rejects only stabilizer/Laurent-loop decoration attached to the visible
support groupoid.

## 2. Lemma

```text
Lemma 157.1 (support stabilizer loops are inserted Laurent data).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let G_r be the connected thin support groupoid from doc
156. Let G_r[Z] be the minimal stabilizer repair: a connected transitive
groupoid on the same r objects with isotropy Z at a basepoint.

Then the category algebra is:

  L[G_r[Z]] ~= Mat_r(L[s^{+-1}]).

For a finite loop window |k| <= K, the number of support morphism/loop
basis elements is:

  r^2(2K+1).

At K=0 and r=3,4,6,10 this recovers the doc-156 matrix ranks:

  9,16,36,100.

At K=1 it becomes:

  27,48,108,300,

with extra loop layers:

  18,32,72,200.

At K=2 it becomes:

  45,80,180,500.

A corner sees the inserted Laurent line L[s^{+-1}], but the corner still
requires choosing a support vertex or rank-one idempotent. The endpoint
choices are:

  3,4,6,10,

and the rank-one idempotent counts over F_2 remain:

  28,120,2016,523776.

The loop generator s is not the DMP bottom class. If s is new, the repair
has freely added a Laurent variable; if s is identified with the tensor
variable u, that identification is imposed externally. Either way, the
original DMP bottom class remains square-zero because there is no degree -2
target.

The stabilizer loop supplies no DMP multiplication and no torsor splitter.
The doc-138 shear obstruction remains res_1(c)=1, the bottom obstruction
remains y^2=0, and the same stabilizer-loop extension is formable on
controls.

Therefore attaching Z isotropy to the support groupoid is not a
construction-grade R1 carrier correspondence. A surviving route must
construct the nontrivial isotropy/loops as carrier-native correspondences
and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_STABILIZER_LOOP__INSERTED_LAURENT_ISOTROPY_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_stabilizer_loop_no_go` verifies the finite models.

SLP1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SLP2 records that the zero loop window recovers the doc-156 thin
groupoid/matrix envelope:

```text
9,16,36,100.
```

SLP3 records the first nontrivial stabilizer window:

```text
K = 1:           27,48,108,300
extra layers:    18,32,72,200.
```

SLP4 records the next window:

```text
K = 2:           45,80,180,500.
```

These counts are exactly `r^2(2K+1)`, the finite-window shadow of
`Mat_r(L[s^{+-1}])`.

SLP5 records that a corner sees the inserted Laurent loop line:

```text
2K+1 = 5    for K=2.
```

SLP6 records that the stabilizer generator consumes no primitive carrier map.

SLP7 records the dichotomy:

```text
s is new Laurent data, or s=u is imposed by fiat.
```

Neither option constructs the loop from DMP multiplication.

SLP8 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

SLP9 records that the stabilizer loop does not invert the DMP bottom class:

```text
dim DMP[-1] = 1,     dim DMP[-2] = 0.
```

SLP10 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1.
```

No relation `b/phi(b)=c` is constructed.

SLP11 applies the carrier guard: attaching `Z` isotropy to a finite support
groupoid is shadow-level data, so controls can form the same construction.

## 4. Impact on R1

```text
R1 after docs 138-157:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144);
    - formally adjoining a torsor splitter b with phi(b)=b*c^-1 (doc 145);
    - quotienting a free/tensor Laurent repair to one line (doc 146);
    - shift-coinvariant collapse of the tensor copies to one line (doc 147);
    - shift telescope/direct-limit packaging of that collapse (doc 148);
    - formal shift-operator insertion as the missing carrier shift (doc 149);
    - support-module End envelope as the missing correspondence algebra
      (doc 150);
    - Morita/idempotent corner of the support End envelope as the selected
      carrier line (doc 151);
    - trace/minimality selection of that idempotent (doc 152);
    - conjugacy-invariant or symmetrized selection of that idempotent
      (doc 153);
    - support-degree flag/Borel reduction as the canonical idempotent
      selector (doc 154);
    - support-chain incidence/path algebra as the carrier correspondence
      algebra (doc 155);
    - groupoid completion / formal inversion of support-chain arrows as the
      carrier correspondence algebra (doc 156);
    - stabilizer/Laurent-loop decoration of the support groupoid as carrier
      isotropy (doc 157).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/flag/idempotent/
      line, selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Nontrivial loops are admissible only if the carrier
constructs them. Stabilizer decoration of the support groupoid is
bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SLP.1 support-groupoid stabilizer as carrier isotropy
  A proposal attaches Z or another loop group to the support groupoid.
  The loop is inserted isotropy unless a carrier constructs it.

KILL-SLP.2 stabilizer loop as Laurent shift
  A proposal uses the stabilizer generator as the shift. This freely adds
  s, or identifies s with u by fiat; it does not invert the DMP bottom class.

KILL-SLP.3 stabilizer category algebra as new End
  A proposal uses the category algebra Mat_r(L[s^{+-1}]). This is the
  support matrix envelope with an extra Laurent variable.

KILL-SLP.4 stabilizer-loop extension formable on controls
  Attaching isotropy to a finite support groupoid is shadow-level data.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 20 = doc 157:
  N1B_STABILIZER_LOOP__INSERTED_LAURENT_ISOTROPY_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: nontrivial
support-groupoid loops obtained by attaching stabilizers are inserted
Laurent data.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/flag/
  idempotent/line, shift operator, selector/functional, and torsor splitter,
  with DH/Epstein death at that correspondence.
```
