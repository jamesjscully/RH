# 199 - Real-cyclotomic negation does not construct End(S^2/Z)

Status: no-go + H-r3 scheme-selector boundary, 2026-06-20. Sixty-second
cycle of the doc-137 construction arc. Doc 198 killed promoting the
monoid/cyclotomic Frobenius shadow itself to End(S^2/Z). This document
tests the strongest remaining finite-place scheme-selector shortcut:
use the real-cyclotomic/`C_2` structure to force the symmetric KMS-1/2
determinant scheme, then promote that selection to the missing
compactified square.

Witness, lead-reran this cycle:
`prime_int_n1b_real_cyclotomic_negation_no_go` (RCN1-RCN10 ALL PASS) --
integer branch/window slopes, negation-naturality forcing the KMS-half
scheme, conjugation selecting nothing, the `lambda^{1/2}` double-cover
requirement, vacuity of the computed residual Weyl action, the computed
p=2 THR-Tate local object, missing homotopy ladder negation, missing
compactified duality object, missing square-side `iota`/properness,
missing compactified square cohomology/intersection/correspondence/
Frobenius/Rosati data, missing Laurent boundary/torsor/DD.4 data, and
residual R1 carrier-guard checks.

Adjacent witnesses, lead-reran this cycle:
`prime_int_hr3_scheme_rigidity` (ALL PASS) -- the positive O-record that
the analytic half of H-r3 is theorem-grade: negation-naturality forces
the symmetric scheme and requires a `lambda^{1/2}` double cover;
`prime_int_thr_p2_anomaly` (ALL PASS) -- the positive S-record computing
`THR(F_2)^{tC_2}` and the p=2 2-adic entanglement anomaly.

## 1. Purpose

The H-r3 record gives a real theorem:

```text
negation-naturality on the full vertical ladder forces c = 1/2,
f(w) = q^{w/2}(1 - q^{-w}) = 2 sinh(w log q / 2).
```

It also proves that no ordinary branch convention can supply this half
slope, and that the symmetric scheme lives on a `lambda^{1/2}` double
cover. This is exactly the analytic scheme shape the determinant side
needs.

But the construction needs more than the analytic scheme. It needs a
homotopy-theoretic source of ladder negation on the determinant input,
or a compactified duality object on which reflection really exchanges the
two halves of the ladder. The currently computed real-cyclotomic
structures do not do this. The residual Weyl action acts by signs on
lines and commutes with the determinant operator; the antilinear reading
only gives Schwarz reflection; the real cyclotomic Frobenius is
equivariant, not inverted. At p=2, `THR(F_2)^{tC_2}` is computed and
interesting, but it is a 2-adic completed local object, not the
archimedean compactified square.

This document is local. It does not reject a future real-cyclotomic,
PFD, or compactified duality carrier that supplies ladder negation and the
`lambda^{1/2}` datum geometrically. It rejects only the shortcut:

```text
analytic H-r3 scheme rigidity / current real-cyclotomic C2 action =
End(S^2/Z).
```

## 2. Lemma

```text
Lemma 199.1 (The real-cyclotomic scheme selector is not the square).

The analytic half of H-r3 is a genuine theorem: in the zeta-regularization
class, negation-naturality forces the KMS-1/2 scheme and no pointwise
branch convention can do it. The symmetric determinant requires a
lambda^{1/2} double-cover datum.

However, the homotopy half is not constructed. The residual Weyl action
computed on TP/THR acts on eigenlines and commutes with Theta; conjugation
selects no scheme; the real cyclotomic Frobenius is equivariant rather
than inverted; and the p=2 THR-Tate computation gives a completed
2-adic local object, not a compactified arithmetic square.

Moreover, no square-side iota, properness theorem, compactified
arithmetic square, square H2, intersection form, correspondence algebra,
Frobenius graph, positive Rosati involution, Laurent boundary map, torsor
splitter, or DD.4 weight>=1 datum is constructed.

Therefore the banked real-cyclotomic negation / lambda-half scheme
selector cannot itself be promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_REAL_CYCLOTOMIC_NEGATION__SCHEME_SELECTOR_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_real_cyclotomic_negation_no_go` verifies the R1 gate, with
`prime_int_hr3_scheme_rigidity` and `prime_int_thr_p2_anomaly` rerun as
adjacent positive witnesses.

RCN1 records the branch/window classification: all pointwise branch
schemes have integer vacuum slope. In particular, no branch convention
produces the half-slope `c=1/2`.

RCN2 records the positive analytic theorem: negation-naturality under
`w -> -w` forces exactly `c=1/2`, with unit `-1`.

RCN3 records that conjugation/Schwarz reflection selects nothing: every
real-`c` scheme satisfies it. Conjugation is not ladder negation.

RCN4 records the double-cover obstruction: integer-slope schemes are
invariant under recentering by one vertical lattice step, while the
KMS-half scheme changes sign. Thus the symmetric determinant needs a
`lambda^{1/2}` datum.

RCN5 records why the computed residual Weyl action does not supply the
geometric half: finite products are odd under true negation, but the
line-sign Weyl action commutes with `Theta`, so determinant equivariance
under that action is vacuous.

RCN6 records the p=2 input: `THR(F_2)^{tC_2}` is computed and has the
completed `F_2[[z]][t^{+-1}]` shape, but this is a 2-adic local object,
not the compactified arithmetic square.

RCN7 records that no homotopy ladder negation or compactified duality
object is built.

RCN8 records that no square-side `iota` or properness theorem is built.

RCN9-RCN10 record the carrier failure: no compactified square H2,
intersection form, correspondence algebra, Frobenius graph, positive
Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-199:
  NEWLY CLOSED THIS CYCLE:
    - analytic H-r3 scheme rigidity, current real-cyclotomic C2 action,
      lambda^{1/2} double-cover demand, and p=2 THR-Tate completed local
      object, as End(S^2/Z), square H2, intersection form, correspondence
      algebra, Frobenius graph, Laurent boundary data, torsor splitter,
      DD.4 weight>=1 datum, or positive Rosati (doc 199).

  STILL ADMISSIBLE:
    - a real-cyclotomic or PFD construction that supplies ladder negation
      on the determinant input as actual compactified duality;
    - a carrier-native lambda^{1/2} double cover tied to a square
      correspondence algebra;
    - a square-side iota/properness theorem replacing the finite-place
      determinant scheme with global archimedean assembly;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The analytic scheme selector is real and useful, but it
is not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-RCN.1 analytic H-r3 scheme as End(S^2/Z)
  A proposal identifies negation-natural regularization with the
  compactified arithmetic square. Kill it unless it constructs the
  homotopy negation/duality carrier.

KILL-RCN.2 branch convention as KMS-half selector
  A proposal obtains c=1/2 from an ordinary branch/window convention. Kill
  it: branch slopes are integer; KMS-half is not a branch convention.

KILL-RCN.3 conjugation or line-sign Weyl action as ladder negation
  A proposal uses conjugation or the residual Weyl action v -> -v as the
  required negation. Kill it: conjugation gives Schwarz only, and line
  signs commute with Theta.

KILL-RCN.4 lambda-half demand as constructed carrier
  A proposal notes the lambda^{1/2} double-cover requirement and treats
  that as construction. Kill it unless the double cover is supplied
  carrier-natively by the square correspondence object.

KILL-RCN.5 p=2 THR-Tate anomaly as archimedean compactification
  A proposal promotes THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}] to the
  archimedean square. Kill it unless it constructs the global
  compactified duality object and square-side iota.

KILL-RCN.6 scheme selector without Rosati/correspondences
  A proposal gives the symmetric determinant scheme but no correspondence
  algebra or positive Rosati. This is not End(S^2/Z).
```

## 6. Board

```text
doc-137 R1, cycle 62 = doc 199:
  N1B_REAL_CYCLOTOMIC_NEGATION__SCHEME_SELECTOR_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a separation theorem: H-r3's
analytic half is real and forces the KMS-half scheme, but the homotopy
negation/duality carrier and square-side iota/properness are not built.

What remains: construct a real-cyclotomic/PFD compactified duality object
that acts by ladder negation on the determinant input; construct the
carrier-native lambda^{1/2} double cover inside a correspondence algebra;
solve square-side iota/properness; or return to the in-house PFD/Xbar
DD.4 weight>=1 obstruction.
```
