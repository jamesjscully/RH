# 221 - Projection-formula quotients do not construct proper correspondences

Status: no-go + projection-quotient boundary, 2026-06-20. Eighty-fourth
cycle of the doc-137 construction arc. Doc 220 killed a formal dagger on
triples as positive Rosati because the formal componentwise law lacks the
correspondence projection formula. This document tests the next repair:
impose the projection formula as quotient relations or local retunings.

```text
formal NS envelope + composition + dagger
  -> projection formula imposed by quotient/relations
  -> proper correspondence calculus
  -> positive Rosati square carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_projection_formula_quotient_no_go` (PFQ1-PFQ6 ALL PASS) --
on genuine finite-field anchors, the projection relation for the formal
componentwise law forces false trace/count identities; scalar quotients over
multiple anchors collapse the base; local retuning can force one projection
equation only by destroying the graph degree; finite projection samples are
cherry-pickable; the same quotient/retuning is formable on controls; and no
square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_formal_adjoint_projection_no_go` (FAP1-FAP6 ALL PASS) and
`prime_int_n1b_formal_correspondence_composition_no_go` (FCC1-FCC6 ALL
PASS).

## 1. Purpose

Doc 220 identified a concrete failure: with the pasted NS pairing and the
componentwise formal composition law,

```text
<A o B, C> != <B, A^dag o C>
```

even on the finite-field block. The immediate repair is to force this identity
by quotienting the formal envelope or by retuning the formal product.

That repair fails. The projection identity is not a missing syntactic axiom
for the componentwise law. On finite-field graphs, imposing it forces trace
relations that are false for ordinary Weil curves. If one kills the scalar
defects by quotienting the coefficient ring, multiple finite-field anchors
already generate the unit ideal. If one retunes degree slots to kill a chosen
defect, the graph degree changes.

This document rejects only the shortcut:

```text
the projection formula can be imposed on the formal NS/composition/dagger
envelope by quotient or retuning, thereby constructing proper
correspondences and positive Rosati.
```

## 2. Lemma

```text
Lemma 221.1 (Projection quotients are not proper correspondence).

In the formal NS envelope with

    (d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2),
    dagger(d1,z,d2) = (d2,z^dag,d1),

the projection identity

    <A o B, C> = <B, A^dag o C>

is not a quotient repair of the componentwise law.

For a finite-field graph Gamma=(q,F,1), taking A=Gamma, B=Delta, C=Gamma
forces

    Tr(F^2) = 2q.

For the genuine q=7, Tr(F)=1 anchor, the actual value is Tr(F^2)=-13. Thus
the forced relation changes the n=2 point count from 63 to 36. This destroys
the finite-field anchor that the over-Z construction must reproduce.

Killing scalar projection defects by quotienting the base is worse: the
defects 27 (from q=7, Tr(F)=1) and 8 (from q=2, Tr(F)=0) are coprime, so a
universal scalar quotient over Z collapses.

Local retuning is also not construction. One can change a degree slot to make
a chosen projection equation true, but for the q=7 graph this changes the
first graph degree from 7 to -20. The graph class has been destroyed.

Finite projection samples can be cherry-picked: the q=2, Tr(F)=0 anchor has
zero defect for one sampled projection relation while another sampled relation
has defect 8. The same quotient/retuning operations are formable on arbitrary
determinant-q controls without Euler product, Satake parameters, rep_NS,
square properness, or carrier-native positivity.

Consequently projection-formula quotient/retuning constructs no rep_NS,
actual square, fiber-product correspondence composition, carrier-native
pairing, projection formula, degree character, Frobenius graph, preserved
point counts, positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or
End(S^2/Z).

Therefore the projection formula cannot be promoted by formal quotienting of
the symbolic NS envelope; it must come from an actual square carrier and
proper correspondence composition.
```

Verdict label:

```text
N1B_PROJECTION_FORMULA_QUOTIENT__RELATION_REPAIR_NOT_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_projection_formula_quotient_no_go` verifies the six gates.

PFQ1 records the finite-field contradiction. For `q=7`, `a=1`, the genuine
finite-field graph has

```text
Tr(F^2) = -13,
#C(F_{q^2}) = 63.
```

The projection quotient relation for the formal componentwise law forces

```text
Tr(F^2) = 2q = 14,
# forced = 36.
```

The measured projection defect is

```text
27.
```

Thus the quotient changes the finite-field count data rather than
constructing the finite-field correspondence calculus.

PFQ2 records scalar quotient collapse. The projection defects

```text
27  from q=7, a=1,
8   from q=2, a=0
```

generate the unit ideal in `Z`. Hence killing these defects by scalar quotient
is not an over-`Z` construction.

PFQ3 records local retuning failure. Retuning only the first degree of
`Gamma o Delta` can force one projection equation, but changes

```text
d1 : 7 -> -20.
```

The graph-degree defect is `27`; the graph has been destroyed.

PFQ4 records finite-sample overfitting. The `q=2`, `a=0` anchor has

```text
defect(1,2) = 0,
defect(1,1) = 8.
```

A finite projection sample can therefore pass without constructing the
projection formula.

PFQ5 records control formability. The determinant-`3` control matrix

```text
[[1,2],[1,5]]
```

has exact q-similitude, a projection defect of `24`, and can be retuned to
kill that chosen defect. It has no Euler product, Satake parameters, `rep_NS`,
square properness, or positive Rosati.

PFQ6 records the construction failure: no `rep_NS`, actual square,
fiber-product composition, carrier-native pairing, projection formula, degree
character, Frobenius graph, preserved point counts, positive Rosati, control
death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-221:
  NEWLY CLOSED THIS CYCLE:
    - projection-formula quotient of the formal NS envelope, scalar quotient
      of projection defects, local degree retuning to force projection
      identities, finite projection samples as correspondence calculus, and
      projection-relation repairs as DH/Epstein guard (doc 221).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose projection formula is a theorem of
      actual proper correspondences/fiber products;
    - carrier-native degree maps preserving the finite-field graph/count
      anchor;
    - a pairing and adjoint constructed before projection identities are
      asserted;
    - a positive Rosati theorem on the constructed off-diagonal intersection
      form, with controls killed at carrier formation.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, genuine
      correspondence composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the projection-formula quotient repair:
relations imposed on the symbolic envelope are not proper correspondences.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PFQ.1 projection formula by quotient
  A proposal imposes <A o B,C>=<B,A^dag o C> on the formal componentwise
  envelope. Kill it unless the identity is induced by actual proper
  correspondences and preserves finite-field trace/count anchors.

KILL-PFQ.2 scalar defect quotient
  A proposal kills projection defects by quotienting scalar coefficients. Kill
  it unless the quotient remains an over-Z carrier and does not collapse across
  finite-field anchors.

KILL-PFQ.3 local degree retuning
  A proposal changes degree slots to force projection identities. Kill it
  unless the graph degree maps remain carrier-native and unchanged.

KILL-PFQ.4 finite projection sample
  A proposal verifies only finitely many projection identities. Kill it unless
  the full projection formula follows from constructed fiber-product
  composition.

KILL-PFQ.5 control survival
  A proposal's projection quotient or retuning can be formed on determinant-q
  control matrices. Kill it unless controls die at carrier formation.
```

