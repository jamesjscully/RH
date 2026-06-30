# 152 - Trace and minimality do not choose the corner

Status: no-go + trace/minimal-idempotent selection deletion, 2026-06-20.
Fifteenth cycle of the doc-137 construction arc. Doc 151 killed a
Morita/rank-one corner of the support End envelope unless the carrier
chooses the idempotent. This document tests the immediate repair: use trace,
rank, or minimality to choose that idempotent canonically.

Witness, lead-reran this cycle:
`prime_int_n1b_trace_minimal_idempotent_no_go` (TMI1-TMI10 ALL PASS) --
exact finite-rank trace-one, minimal-idempotent, obstruction, and
control-formability checks.

## 1. Purpose

Doc 151 left only one possible support-envelope rescue:

```text
do not choose e arbitrarily;
choose the primitive / minimal / trace-one idempotent.
```

This does not work. Trace-one is too weak: it already includes many
diagonal idempotents of odd rank. Minimality is too weak in the opposite
direction: it cuts to rank-one idempotents, but all rank-one idempotents
have the same trace and minimality profile, and there are still many of
them.

The issue is the same as before: R1 needs a carrier-selected idempotent or
line. A support-level predicate on `Mat_r(L)` is not carrier selection.

## 2. Lemma

```text
Lemma 152.1 (trace/minimality is nonselective on the support End envelope).
Let M_N = R_DMP[-1..N] tensor L ~= L^r with r=N+2 and
L=F_2[u^{+-1}]. Let A_N = End_L(M_N) ~= Mat_r(L).

Trace-one does not choose a rank-one corner. Even among diagonal
idempotents, trace over F_2 is only parity of rank. Thus the trace-one
diagonal idempotents number 2^(r-1), and include ranks 1,3,5,...

Minimality/rank-one also does not choose a corner. A rank-one idempotent
has the form e=u v^T with u != 0 and v(u)=1. Therefore tr(e)=v(u)=1, so
all rank-one idempotents have trace one. Their count is

  (2^r - 1) 2^(r-1).

For r=3,4,6,10:

  trace-one diagonal idempotents:  4,8,32,512;
  rank-one idempotents:           28,120,2016,523776.

The support data does not distinguish one of these idempotents. The bottom
coordinate trace-one corner is still the external scalar line L from the
tensor repair, not an invertible DMP bottom class. Trace/minimality does
not choose a shift operator or torsor splitter, does not kill the DMP
bottom obstruction, and does not kill the doc-138 shear obstruction.

The same trace/minimality predicates are formable on controls, since they
are finite-free module predicates inside a matrix algebra.

Therefore trace, rank, and minimality do not make the support End-envelope
corner construction-grade. A surviving route must construct the idempotent
from carrier correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_TRACE_MINIMAL_IDEMPOTENT__NONSELECTIVE_PREDICATE_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_trace_minimal_idempotent_no_go` verifies the finite models.

TMI1 records the ranks inherited from doc 151:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

TMI2 counts diagonal trace-one idempotents:

```text
2^(r-1) = 4,8,32,512.
```

TMI3 records that trace-one does not imply rank-one. The diagonal
trace-one ranks include:

```text
r=3:   rank 1:3, rank 3:1;
r=4:   rank 1:4, rank 3:4;
r=6:   rank 1:6, rank 3:20, rank 5:6;
r=10:  rank 1:10, rank 3:120, rank 5:252, rank 7:120, rank 9:10.
```

TMI4 records the converse direction: every rank-one idempotent has trace
one, because `e=u v^T` and `e^2=e` imply `v(u)=1`, hence `tr(e)=1`.

TMI5 records that minimal/rank-one idempotents still form a large family:

```text
28,120,2016,523776.
```

TMI6 records the selection failure: rank, trace, and minimality give the
same support-level profile for all rank-one corners. They do not choose one.

TMI7 tests the bottom trace-one corner. Its scalar is the external `L`
from the tensor repair; the original DMP bottom class still has no degree
`-2` product target and remains square-zero.

TMI8 records that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

TMI9 applies the carrier guard: trace, rank, and minimality are finite-free
module predicates, so controls can run the same selection test. TMI10
records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-152:

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
    - trace/minimality selection of that idempotent (doc 152).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the idempotent or line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Minimality is now part of the selector guard: it is a
valid algebraic property, but not a carrier-native choice.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-TMI.1 trace-one idempotent as canonical corner
  A proposal uses trace one to select e. Trace one is parity over F_2 and
  includes many diagonal idempotents, including higher odd ranks.

KILL-TMI.2 minimal idempotent as canonical corner
  A proposal uses minimality/rank one to select e. All rank-one idempotents
  have trace one and the same support-level profile; there are many.

KILL-TMI.3 trace/minimality hides missing R1 data
  A proposal supplies a trace/minimal corner but not S, the
  selector/functional, and the torsor splitter from the carrier. The corner
  line alone is not the R1 datum.

KILL-TMI.4 trace/minimality formable on controls
  Trace, rank, and minimality are finite-free module predicates in Mat_r(L).
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 15 = doc 152:
  N1B_TRACE_MINIMAL_IDEMPOTENT__NONSELECTIVE_PREDICATE_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: trace and
minimality do not choose the support End-envelope corner.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data choose the idempotent/line, shift operator, selector/functional,
  and torsor splitter, with DH/Epstein death at that correspondence.
```
