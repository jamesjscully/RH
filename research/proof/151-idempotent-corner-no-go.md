# 151 - A Morita corner is a selector unless the carrier chooses it

Status: no-go + idempotent/Morita-corner deletion, 2026-06-20. Fourteenth
cycle of the doc-137 construction arc. Doc 150 killed the support-module
End envelope because `End_L(L^r)=Mat_r(L)` is matrix overproduction. This
document tests the immediate repair: choose a rank-one idempotent and take
the corner

```text
e Mat_r(L) e ~= L.
```

Witness, lead-reran this cycle:
`prime_int_n1b_idempotent_corner_no_go` (IDC1-IDC10 ALL PASS) -- exact
finite-rank idempotent-choice, corner-rank, obstruction, and
control-formability checks.

## 1. Purpose

Doc 150 says the support End envelope overproduces maps. The next repair
is to say:

```text
Mat_r(L) is Morita equivalent to L;
choose a rank-one idempotent e;
use e Mat_r(L) e as the selected line.
```

The algebraic statement is true. The problem is the word "choose." R1 does
not need the existence of some line inside a matrix envelope; it needs the
carrier to produce the line, selector/functional, shift operator, torsor
splitter, and weight>=1 datum. A Morita corner supplies the first item only
after a noncanonical idempotent choice, and supplies none of the rest.

This document is local. It does not reject idempotents or Morita theory in
a genuine carrier correspondence algebra. It rejects the support-envelope
move

```text
M -> End(M) -> e End(M) e
```

when `e` is chosen from finite-free module data before any primitive carrier
correspondence is constructed.

## 2. Lemma

```text
Lemma 151.1 (rank-one corners are selector choices in the support envelope).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let A_N = End_L(M_N) ~= Mat_r(L).

Then a rank-one idempotent e in A_N gives a Laurent rank-one corner

  e A_N e ~= L.

But the idempotent is not supplied by DMP support or by the carrier. Over
F_2, the finite truncations have:

  coordinate idempotents:       r;
  image-line choices:           2^r - 1;
  rank-one idempotent choices:  (2^r - 1) 2^(r-1).

For r=3,4,6,10 these are:

  coordinate choices:   3,4,6,10;
  image-line choices:   7,15,63,1023;
  idempotent choices:   28,120,2016,523776.

Choosing the bottom coordinate idempotent recovers the external scalar line
L from the tensor repair; it does not make the DMP bottom class invertible.
The corner does not select a shift operator or torsor splitter. The DMP
bottom and doc-138 shear obstructions remain. The same idempotent-corner
construction is formable on controls.

Therefore a Morita/idempotent corner of the support End envelope is not a
construction-grade R1 carrier unless the idempotent itself is constructed by
carrier correspondence data and DH/Epstein controls fail at that construction.
```

Verdict label:

```text
N1B_IDEMPOTENT_CORNER__MORITA_SELECTOR_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_idempotent_corner_no_go` verifies the finite models.

IDC1 records the starting envelope:

```text
N = 1,2,4,8  =>  r = 3,4,6,10,
rank_L Mat_r(L) = 9,16,36,100.
```

IDC2 records the algebraic positive fact: a rank-one idempotent corner has
Laurent rank one. This is not denied.

IDC3-IDC5 record the selection problem:

```text
coordinate idempotents:       3,4,6,10;
image-line choices:           7,15,63,1023;
rank-one idempotent choices:  28,120,2016,523776.
```

The line appears only after choosing `e`.

IDC6 tests the bottom-coordinate story. That corner's scalar is the
external `L` from the tensor repair; the original DMP bottom class still
has no degree `-2` product target and remains square-zero.

IDC7 records that choosing an idempotent does not choose the missing shift
operator or a torsor splitter. It gives a corner line, not `S` and not
`b/phi(b)=c`.

IDC8 records that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

IDC9 applies the carrier guard: rank-one idempotents in `Mat_r(L)` are
finite-free module data, so the same construction is formable on controls.
IDC10 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-151:

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
      carrier line (doc 151).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the idempotent or line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. A corner is admissible only if the carrier constructs the
idempotent. A post-hoc Morita reduction of the support matrix envelope is
another selector.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-IDC.1 Morita equivalence as carrier construction
  A proposal replaces Mat_r(L) by a rank-one corner and points to the line.
  The corner exists only after choosing an idempotent; Morita equivalence
  itself does not choose one.

KILL-IDC.2 bottom idempotent as DMP generator
  A proposal chooses the coordinate idempotent indexed by the DMP bottom.
  The corner scalar is the external L, while the DMP bottom class remains
  square-zero.

KILL-IDC.3 idempotent hides missing shift/torsor data
  A proposal supplies e but not S, the selector/functional, and the torsor
  splitter from the carrier. The corner line alone is not the R1 datum.

KILL-IDC.4 idempotent corner formable on controls
  Rank-one idempotent corners in Mat_r(L) are finite-free module data.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 14 = doc 151:
  N1B_IDEMPOTENT_CORNER__MORITA_SELECTOR_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: a corner of
the support End envelope is a selector, not End(S^2/Z).

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data choose the idempotent/line, shift operator, selector/functional,
  and torsor splitter, with DH/Epstein death at that correspondence.
```
