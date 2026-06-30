# 143 - Freely adjoining a Laurent line is not the R1 carrier

Status: no-go + free-carrier insertion deletion, 2026-06-20. Sixth cycle
of the doc-137 construction arc. Doc 142 killed same-bottom localization.
This document tests the next cheapest "different carrier" dodge:
introduce a new Laurent generator by free direct-sum/product or tensor
extension, without a carrier-consuming map that produces it.

Witness, lead-reran this cycle:
`prime_int_n1b_free_laurent_insertion_no_go` (FLI1-FLI8 ALL PASS) --
exact support/multiplicity/control-formability checks.

## 1. Purpose

R1 now requires a genuinely different carrier:

```text
full line + weight>=1 datum + named DH/Epstein death.
```

After docs 139-142, the DMP bottom class cannot be the line generator and
cannot be inverted to make one. The next false repair is to add a fresh
Laurent generator `u` by hand:

```text
R_DMP  ->  R_DMP plus F_2[u^{+-1}]
R_DMP  ->  R_DMP tensor F_2[u^{+-1}]
```

This is not a construction of the missing carrier. It is either external
decoration, multiplicity blow-up, or carrier overreach.

## 2. Lemma

```text
Lemma 143.1 (free Laurent insertion does not construct the R1 carrier).
Let R_DMP denote the DMP support object for TCR(F_2;2)^{phi Z/2}:

  dim pi_d R_DMP = 0 for d <= -2,
                   1 for d = -1 and d >= 0.

Let L = F_2[u^{+-1}], |u| = -1, be an externally adjoined Laurent line.

1. Direct insertion R_DMP plus L contains a Laurent line only as an
   independent summand. Its graded dimensions are not the Lin line:
   degree -1 and every nonnegative degree have dimension 2. The original
   DMP bottom class remains square-zero and noninvertible.

2. Tensor insertion R_DMP tensor L gives full support, but not a singleton
   line. In truncation R_DMP[-1..N], every degree receives N+2 summands;
   in the untruncated DMP support, every degree receives infinitely many.

3. If the new line is independent of the U_1 shear action, the doc-138
   obstruction remains: res_1(c)=1 is still outside the first-coordinate
   coboundaries. If the action on u is chosen to make c a coboundary, then
   u is not free; the proposal has inserted the torsor solution and must
   prove the resulting carrier relation and its DH/Epstein death.

4. The free operation is formable on control shadows before any Euler
   carrier field is consumed. It therefore fails the doc-107 carrier-
   overreach test unless a nonfree first map is named.

Thus a surviving R1 carrier cannot be obtained by freely adjoining a
Laurent generator. It must produce the line through a carrier-consuming
relation or map, and that map must be undefined on DH/Epstein controls at
a named point.
```

Verdict label:

```text
N1B_FREE_LAURENT_INSERTION__DECORATION_OR_OVERREACH__NO_GO.
```

## 3. Proof

`prime_int_n1b_free_laurent_insertion_no_go` verifies the gates.

FLI1 records the starting failure from doc 139: DMP support is not already
the Lin line, since degree `-2` vanishes.

FLI2-FLI3 test direct insertion. Adding an external Laurent summand makes
degree `-1` and nonnegative degrees two-dimensional, and it does not change
the multiplication of the original DMP bottom class:

```text
y^2 = 0 remains true in the DMP component.
```

So the line is not produced by the DMP carrier; it is merely attached next
to it.

FLI4-FLI5 test tensor insertion. In the truncated support
`R_DMP[-1..N]`, each total degree receives one summand from every DMP
degree in `[-1,N]`, hence dimension `N+2`. The witness checks
`N=1,2,4,8`:

```text
dim_0 = 3,4,6,10.
```

The multiplicity grows with the truncation. The untruncated object is
therefore not the one-dimensional Lin line.

FLI6 records the doc-138 obstruction persistence for an independent line:
`res_1(c)=1` while first-coordinate coboundaries still have `res_1=0`.

FLI7 applies the carrier guard. The free operation can be applied to a
zero control or to an Epstein represented-norm/count shadow and still
produces a Laurent summand. It happens before any primitive Euler carrier
field is consumed, so it routes to doc 107's carrier-overreach lemma.

FLI8 records the escape condition: a surviving proposal must name the
nonfree carrier-consuming map or relation that produces the line and fails
on controls.

## 4. Impact on R1

```text
R1 after docs 138-143:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143).

  STILL OPEN:
    - a genuinely different carrier where a nonfree carrier-consuming map
      produces the full line and weight>=1 datum, and where DH/Epstein die
      at named points before signs, zeros, or comparison.
```

R1 remains open, but "add the missing generator" is no longer admissible
as a construction step. The next carrier must earn the generator.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FLI.1 external Laurent summand promoted to carrier
  A proposal forms R_DMP plus F_2[u^{+-1}] and points to the new summand as
  the missing line. That line is external decoration; the DMP bottom class
  remains square-zero and the combined graded object is not the singleton
  Lin line.

KILL-FLI.2 Laurent tensor promoted to Lin line
  A proposal tensors R_DMP with F_2[u^{+-1}] and calls the result a line.
  It overproduces multiplicities: every degree receives one copy for each
  DMP degree. Projection to one copy is a choice, not a carrier.

KILL-FLI.3 independent line claimed to kill the torsor obstruction
  A free line with independent shear action does not change the doc-138
  res_1 obstruction. A twisted action chosen to cancel c is no longer free;
  it must be proved as a carrier relation and must fail on DH/Epstein.

KILL-FLI.4 free operation before carrier death
  A proposal applies the same Laurent insertion to any graded/count shadow.
  Since the operation is formable on controls, it fails doc 107 unless a
  prior primitive carrier-consuming map is named.
```

## 6. Board

```text
doc-137 R1, cycle 6 = doc 143:
  N1B_FREE_LAURENT_INSERTION__DECORATION_OR_OVERREACH__NO_GO.

What got built: no new sub-object. The value is a deletion: a full line
cannot be obtained by free external insertion.

Next valid R1 work:
  produce a nonfree carrier-consuming map or relation that creates the
  full line and weight>=1 datum, and prove where DH/Epstein controls fail.
```
