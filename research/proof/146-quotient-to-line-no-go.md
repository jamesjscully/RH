# 146 - Quotienting to one Laurent line is a choice, not a carrier

Status: no-go + quotient/augmentation repair deletion, 2026-06-20. Ninth
cycle of the doc-137 construction arc. Doc 144 killed selecting a
rank-one Laurent subobject from the free/tensor repair. This document
tests the dual repair: quotient the overproduced free Laurent module down
to one line by an augmentation or diagonal functional.

Witness, lead-reran this cycle:
`prime_int_n1b_quotient_to_line_no_go` (QTL1-QTL9 ALL PASS) -- exact
finite-rank quotient-functional counts and control-formability check.

## 1. Purpose

The tensor repair produces

```text
R_DMP[-1..N] tensor F_2[u^{+-1}] ~= L^{N+2},
L = F_2[u^{+-1}].
```

Doc 144 says selecting one copy `L -> L^{N+2}` is noncanonical unless a
carrier-native selector is constructed. The dual move is to use a quotient

```text
L^{N+2} -> L
```

such as "sum all copies" or "take the diagonal quotient." That also
requires choosing a functional. Support and Laurent periodicity do not
choose it.

## 2. Lemma

```text
Lemma 146.1 (rank-one Laurent quotients are noncanonical without a
carrier functional). For the truncated tensor repair

  M_N = R_DMP[-1..N] tensor F_2[u^{+-1}],

M_N is a free L-module of rank r=N+2. A degree-preserving L-linear quotient
M_N -> L is specified by a nonzero vector in F_2^r. Therefore there are

  2^r - 1 = 2^(N+2)-1

rank-one quotient functionals, including r coordinate quotients and the
all-ones diagonal/augmentation quotient.

Every nonzero quotient has the same visible one-dimensional Laurent support
profile. Choosing the all-ones functional, or any other functional, is
additional data not supplied by DMP support, u-periodicity, or the base
torsor. The quotient generator is still the external u; the original DMP
bottom class remains square-zero, and the doc-138 shear obstruction remains.

The same quotient operation is formable on any same-rank free Laurent module,
including controls. Hence quotienting to one line is not a construction-grade
R1 carrier unless the quotient functional is produced by a carrier-native
first map and that map is undefined on DH/Epstein controls.
```

Verdict label:

```text
N1B_QUOTIENT_TO_LAURENT_LINE__NONCANONICAL_FUNCTIONAL__NO_GO.
```

## 3. Proof

`prime_int_n1b_quotient_to_line_no_go` verifies the finite models.

QTL1 records the starting rank:

```text
N = 1,2,4,8  =>  rank = 3,4,6,10.
```

QTL2 counts coordinate quotient choices; there are `N+2`, and the count
grows with the truncation.

QTL3 counts all rank-one quotient functionals:

```text
N = 1,2,4,8  =>  7,15,63,1023.
```

QTL4 records that all nonzero quotient functionals have the same visible
Laurent support profile, so support and `u`-periodicity do not select one.

QTL5 identifies the diagonal/augmentation quotient as one arbitrary
functional. At `N=4`, the all-ones functional is one of `63` possible
nonzero functionals.

QTL6-QTL7 record that this quotient does not repair the base obstructions:
the DMP bottom class still satisfies `y^2=0`, and the doc-138
`res_1(c)=1` obstruction is unchanged unless a torsor splitter is also
inserted.

QTL8 applies the carrier guard: the same quotient operation is available
for same-rank control modules. QTL9 records the only escape: construct the
functional carrier-natively and show where controls fail.

## 4. Impact on R1

```text
R1 after docs 138-146:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144);
    - formally adjoining a torsor splitter b with phi(b)=b*c^-1 (doc 145);
    - quotienting a free/tensor Laurent repair to one line (doc 146).

  STILL OPEN:
    - a genuinely different carrier whose first map produces the full line,
      selector/functional, torsor splitter, and weight>=1 datum from carrier
      data, and where DH/Epstein controls fail before signs, zeros, or
      comparison.
```

R1 is still open, but quotienting the overproduced free module is no longer
an admissible shortcut. The line must be born rank-one, or the rank-one
functional must itself be constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-QTL.1 diagonal quotient by support
  A proposal tensors with a Laurent line and then quotients by "sum all
  copies." The all-ones functional is one of many; support/u-periodicity do
  not select it.

KILL-QTL.2 coordinate quotient promoted to carrier
  A proposal chooses one coordinate quotient. This is dual to the projection
  choice of doc 144 and is not canonical without a carrier-native map.

KILL-QTL.3 quotient hides the DMP bottom obstruction
  A quotient maps to an external u-line. It does not make the original DMP
  bottom class invertible and does not kill the doc-138 torsor obstruction.

KILL-QTL.4 quotient formable on controls
  If the quotient is any nonzero L-linear functional from a finite-rank free
  Laurent module, controls can form the same quotient. DH/Epstein have not
  died at a carrier-consuming map.
```

## 6. Board

```text
doc-137 R1, cycle 9 = doc 146:
  N1B_QUOTIENT_TO_LAURENT_LINE__NONCANONICAL_FUNCTIONAL__NO_GO.

What got built: no new sub-object. The value is a deletion: quotienting to
one Laurent line is not a carrier unless the quotient functional is
constructed.

Next valid R1 work:
  construct the first carrier-native map/relation that produces a rank-one
  line or quotient functional, the selector, and the torsor splitter, with
  DH/Epstein death at that map.
```
