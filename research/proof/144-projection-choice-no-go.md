# 144 - Projecting to one Laurent copy is a choice, not a carrier

Status: no-go + projection/splitting repair deletion, 2026-06-20. Seventh
cycle of the doc-137 construction arc. Doc 143 killed free Laurent
insertion. This document tests the immediate repair: tensor with the free
Laurent line, then project to the "right" or "diagonal" Laurent copy.

Witness, lead-reran this cycle:
`prime_int_n1b_projection_choice_no_go` (PJC1-PJC8 ALL PASS) -- exact
finite-rank Laurent-module choice count and control-formability check.

## 1. Purpose

Doc 143 showed that

```text
R_DMP tensor F_2[u^{+-1}]
```

has full support but overproduces multiplicities. The next proposal is to
repair that by selecting one rank-one Laurent summand:

```text
R_DMP tensor F_2[u^{+-1}]  ->  one copy of F_2[u^{+-1}].
```

This is allowed only if the selector is produced by the carrier. A
post-hoc projection, diagonal choice, bottom-coordinate choice, or support
normalization is not a carrier.

## 2. Lemma

```text
Lemma 144.1 (support-only projection is noncanonical). Truncate the DMP
support to degrees -1..N and tensor with an external Laurent line
L = F_2[u^{+-1}]. Then

  R_DMP[-1..N] tensor L

is a free L-module of rank N+2: one Laurent copy for each DMP degree
-1,0,...,N.

Consequently:

1. There are N+2 coordinate Laurent summands.
2. There are 2^(N+2)-1 rank-one L-submodules over F_2.
3. Every coordinate summand has the same one-dimensional support profile
   and the same u-periodicity as the Lin line.
4. Choosing the bottom coordinate does not make the DMP bottom class
   invertible; the invertible generator is the external u, while the
   original y still satisfies y^2=0.
5. The same projection operation is available for any same-rank free
   Laurent module, including controls, before any Euler carrier field is
   consumed.

Therefore projecting the free/tensor Laurent repair to one copy is not a
construction-grade R1 carrier unless a carrier-native selector is first
constructed and the selector is undefined on DH/Epstein controls.
```

Verdict label:

```text
N1B_PROJECTION_TO_LAURENT_COPY__NONCANONICAL_SELECTOR__NO_GO.
```

## 3. Proof

`prime_int_n1b_projection_choice_no_go` verifies the finite models.

PJC1 computes the Laurent rank after truncating DMP to `[-1..N]`:

```text
N = 1,2,4,8  =>  rank = 3,4,6,10.
```

This is not a singleton line.

PJC2 counts the coordinate projections. There are `N+2` coordinate
Laurent copies, and the count grows with the truncation.

PJC3 counts all rank-one Laurent submodules. Over `F_2`, a rank-one
submodule of a free module of rank `r` is determined by a nonzero vector
in `F_2^r`, so there are

```text
2^r - 1 = 2^(N+2)-1
```

choices. The witness records:

```text
N = 1,2,4,8  =>  7,15,63,1023 choices.
```

PJC4 shows that support and `u`-periodicity do not choose among coordinate
copies: every coordinate copy has the same one-dimensional Laurent support
profile as the Lin line.

PJC5 rules out the bottom-coordinate story. Selecting the bottom coordinate
does not turn the DMP bottom class into the Laurent generator; it only
chooses the external `u` line attached to that coordinate. The original
DMP class remains square-zero by doc 140.

PJC6 applies the carrier guard. The operation "choose a rank-one summand
from a finite-rank free Laurent module" is formable for controls too. It
does not consume a primitive Euler carrier field.

PJC7 records the G-INT6 failure: many choices, no support invariant
selecting one. PJC8 records the only escape: a nonfree carrier-native
selector with DH/Epstein death.

## 4. Impact on R1

```text
R1 after docs 138-144:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144).

  STILL OPEN:
    - a genuinely different carrier with a nonfree carrier-consuming map
      or relation that produces both the full line and weight>=1 datum, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is narrowed again. The next carrier must not only contain many Laurent
copies; it must construct the selector.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PJC.1 diagonal Laurent copy by support
  A proposal tensors with a Laurent line and chooses one "diagonal" copy
  using only support/u-periodicity. All coordinate copies have the same
  support and u-periodicity, so the selector is not canonical.

KILL-PJC.2 bottom coordinate promoted to generator
  A proposal chooses the copy indexed by the DMP bottom class. This does
  not make y invertible; the invertible generator is still the external u.

KILL-PJC.3 projection after multiplicity blow-up
  A proposal first creates N+2 copies per degree and then projects to one.
  Unless the projection is supplied by a carrier-native map, this is a
  post-hoc choice and violates G-INT6.

KILL-PJC.4 selector formable on controls
  A proposed projection is defined for any finite-rank free Laurent module.
  Then controls can use the same selector; DH/Epstein have not died at a
  carrier-consuming map.
```

## 6. Board

```text
doc-137 R1, cycle 7 = doc 144:
  N1B_PROJECTION_TO_LAURENT_COPY__NONCANONICAL_SELECTOR__NO_GO.

What got built: no new sub-object. The value is a deletion: projection to
one Laurent copy is not a carrier unless the selector itself is constructed.

Next valid R1 work:
  construct a nonfree selector/relation from carrier data, or move to a
  route where the full line is born already rank-one and DH/Epstein fail
  before any projection choice.
```
