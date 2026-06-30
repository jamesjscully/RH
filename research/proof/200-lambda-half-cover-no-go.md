# 200 - Formal lambda-half cover does not construct End(S^2/Z)

Status: no-go + lambda-half cover boundary, 2026-06-20. Sixty-third
cycle of the doc-137 construction arc. Doc 199 killed promoting analytic
H-r3 scheme rigidity, current real-cyclotomic C2 action, the lambda^{1/2}
double-cover demand, or the p=2 THR-Tate local object itself to
End(S^2/Z). This document tests the immediate repair left open by that
boundary: formally pass to the double cover

```text
eta^2 = lambda
```

and read the KMS-half determinant factor on that cover.

Witness, lead-reran this cycle:
`prime_int_n1b_lambda_half_cover_no_go` (LHC1-LHC10 ALL PASS) -- the
formal cover has the correct sign under one vertical period, has two
sheets and no canonical section, makes the linear half-factor
anti-invariant rather than descended, is formable on arbitrary controls,
has deck action commuting with the ladder operator rather than inverting
it, gives only a rank-2 scalar base-change algebra, and constructs no
square H2/intersection/correspondence/Frobenius/Rosati, no square-side
`iota`/properness, and no R1 Laurent boundary/torsor/DD.4 data.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_real_cyclotomic_negation_no_go` (ALL PASS) -- the doc-199
boundary separating analytic H-r3 scheme selection from the compactified
square;
`prime_int_hr3_scheme_rigidity` (ALL PASS) -- the positive theorem that
negation-naturality forces the KMS-half scheme and requires the
lambda^{1/2} double cover.

## 1. Purpose

The H-r3 theorem says the symmetric determinant scheme is not an ordinary
branch convention. It needs a lambda-half datum:

```text
lambda = q^w,       eta = lambda^{1/2},
f_{1/2}(w) = eta * (1 - lambda^{-1}).
```

On the double cover, shifting one vertical period fixes `lambda` and
flips `eta`, so the KMS-half factor gets the required sign. This is the
right analytic behavior.

The construction target is stronger. The lambda-half datum has to be
produced by the compactified square correspondence object itself. A formal
double cover is only a base change: it has a deck ambiguity, it does not
descend the linear half-factor without an extra orientation/linearization,
and its deck action is scalar rather than a homotopy ladder-negation
operator. It also creates no square cohomology, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, square-side
properness, Laurent boundary map, torsor splitter, or DD.4 weight>=1
datum.

This document is local. It does not reject a future compactified
duality/PFD/real-cyclotomic carrier whose correspondence algebra
constructs the half-cover. It rejects only the shortcut:

```text
formal eta^2=lambda cover = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 200.1 (The formal lambda-half cover is not the square).

The base change eta^2=lambda supplies a two-sheet cover on which the
KMS-half determinant factor has the expected sign behavior: one vertical
period fixes lambda and sends eta to -eta.

However, this cover has no canonical section. The linear half-factor is
anti-invariant under the deck involution and only its square descends to
the lambda-torus. The deck action is scalar and commutes with the ladder
operator; true ladder negation must conjugate Theta to -Theta. The
resulting algebra R[eta]/(eta^2-lambda) is a rank-2 scalar base change,
not a square correspondence algebra.

Moreover, the same double-cover base change is formable on arbitrary
controls, and it constructs no square-side iota/properness theorem,
compactified arithmetic square, square H2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati involution,
Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum.

Therefore formally adjoining lambda^{1/2} cannot itself be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_LAMBDA_HALF_COVER__FORMAL_DOUBLE_COVER_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_lambda_half_cover_no_go` verifies the R1 gate, with
`prime_int_n1b_real_cyclotomic_negation_no_go` and
`prime_int_hr3_scheme_rigidity` rerun as adjacent witnesses.

LHC1 records the positive analytic sign: for `lambda=q^w` and
`eta=q^{w/2}`, one vertical period fixes `lambda` and flips `eta`. Thus
`eta(1-lambda^{-1})` flips sign, as the KMS-half scheme requires.

LHC2 records the deck ambiguity: both `eta` and `-eta` lie over the same
`lambda`, and the half-factors are opposite. No canonical section is
defined.

LHC3 records descent failure: the linear half-factor is anti-invariant
under the deck involution. Its square descends, but the square has already
forgotten the linear sign/orientation data the determinant scheme needed.

LHC4 records carrier blindness: the same formal double-cover base change
can be performed for arbitrary nonzero control eigenvalues. It is not
Euler- or carrier-specific.

LHC5 records the operator failure: the deck sign commutes with the ladder
operator `Theta`, while true ladder negation must conjugate `Theta` to
`-Theta`.

LHC6 records the algebraic shape: multiplication by `eta` in
`R[eta]/(eta^2-lambda)` squares to the scalar `lambda`. This is a rank-2
base-change algebra, not an off-diagonal square correspondence algebra.

LHC7-LHC9 record the carrier failure: no square H2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, square-side
properness, compactified duality object, Laurent boundary map, torsor
splitter, DD.4 weight>=1 datum, or control death is constructed.

## 4. Impact on R1

```text
R1 after docs 138-200:
  NEWLY CLOSED THIS CYCLE:
    - formal lambda^{1/2} / eta^2=lambda cover insertion as End(S^2/Z),
      linear determinant descent, homotopy ladder negation, square H2,
      intersection form, correspondence algebra, Frobenius graph,
      square-side iota/properness, Laurent boundary data, torsor splitter,
      DD.4 weight>=1 datum, or positive Rosati (doc 200).

  STILL ADMISSIBLE:
    - a compactified duality/PFD/real-cyclotomic construction that supplies
      lambda^{1/2} carrier-natively as part of the square correspondence
      object;
    - a homotopy-level ladder negation operator on the determinant input;
    - a square-side iota/properness theorem replacing the formal cover by
      global archimedean assembly;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The formal half-cover is useful bookkeeping for the
analytic scheme, but it is not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-LHC.1 formal eta^2=lambda cover as End(S^2/Z)
  A proposal identifies the lambda-half double cover with the compactified
  square. Kill it unless the cover is constructed by the square
  correspondence object.

KILL-LHC.2 deck choice as canonical determinant linearization
  A proposal chooses one sheet eta and treats the linear half-factor as
  descended. Kill it: eta and -eta are indistinguishable without an
  additional carrier-native orientation/linearization.

KILL-LHC.3 squared half-factor as the determinant datum
  A proposal descends only f_{1/2}^2 and claims the half-scheme is solved.
  Kill it: the square forgets the sign/linear datum the half-cover was
  introduced to carry.

KILL-LHC.4 deck sign as ladder negation
  A proposal uses the deck involution eta -> -eta as homotopy negation.
  Kill it: the deck sign commutes with Theta; ladder negation must invert
  Theta.

KILL-LHC.5 rank-2 cover algebra as correspondence algebra
  A proposal treats R[eta]/(eta^2-lambda) as the square correspondence
  algebra. Kill it: multiplication by eta squares to a scalar and gives no
  off-diagonal correspondences, Frobenius graph, or Rosati involution.

KILL-LHC.6 control-formable cover as carrier-native data
  A proposal adjoins the same cover on controls and then calls it
  arithmetic. Kill it unless DH/Epstein die at the square map before the
  half-cover can be formed.
```

## 6. Board

```text
doc-137 R1, cycle 63 = doc 200:
  N1B_LAMBDA_HALF_COVER__FORMAL_DOUBLE_COVER_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
the formal lambda-half cover supplies the expected sign torsor, but it is
only an inserted double cover. It does not descend the linear determinant,
construct ladder negation, build square correspondences or positive
Rosati, or repair R1 boundary data.

What remains: construct the half-cover carrier-natively inside a
compactified square correspondence algebra; construct homotopy ladder
negation; solve square-side iota/properness; or return to the in-house
PFD/Xbar DD.4 weight>=1 obstruction.
```
