# 195 - Strict norm filtration does not construct the square carrier

Status: no-go + CC strict norm/MAX-face promotion deletion, 2026-06-20.
Fifty-eighth cycle of the doc-137 construction arc. Doc 194 killed the
naive tolerant-smash/Kunneth relation. This document returns to the best
positive CC strict-layer result in the worker record: AA's theorem that
CC's norm filtration, transported through the strict-square character, is
the archimedean half of the product formula on the monoid ring. The question
tested here is whether that strict norm/MAX face itself can be promoted to
End(S^2/Z).

Witness, lead-reran this cycle:
`prime_int_n1b_cc_norm_filtration_no_go` (CNF1-CNF10 ALL PASS) -- strict
norm facts from AA, exact integer valuation reconstruction, sign/algebra
erasure by norm weights alone, carrier-blindness of the archimedean norm
face, missing derived degree/Bokstedt dictionary, missing non-EM square
functor, missing square H^2/intersection/correspondence/Rosati data, missing
Laurent boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent heavy witness, lead-reran this cycle:
`prime_cc_thh_norm_filtration` (N1-N9 ALL PASS) -- the positive AA strict
result and the carrier guard: CC norm transported along V's character is the
archimedean monoid-ring filtration, the cyclic bar faces preserve it, MAX
and MIN faces recompose the product-formula split on the integer carrier,
and the archimedean face alone is formable on Epstein-style metric controls.

## 1. Purpose

AA supplies the strongest CC strict-layer positive result still in play:

```text
CC norm filtration + V character = archimedean product-formula half.
```

More explicitly, on monoid classes `[A]` in the strict-square character
lattice,

```text
N([A]) = |A|,
log N([A]) = Sum_p v_p(A) log p,
```

and on the geometric family `[p^i]` the norm gives the MAX face while the
same character labels carry the p-adic MIN face. This is real structure, not
a selector.

The promotion tested here is:

```text
strict CC norm filtration / MAX face = End(S^2/Z).
```

That promotion fails. The norm filtration supplies weights, not degrees. It
does not construct the derived THH/Bokstedt axis, square H^2, an
intersection form, correspondences, a Frobenius graph, Laurent boundary data,
a torsor splitter, DD.4 weights>=1, or a positive Rosati involution. AA's own
carrier guard also shows the archimedean norm face alone is carrier-blind:
metric controls keep the MAX face while lacking multiplication, valuations,
the product formula, and cyclic bar faces.

This document is local. It does not reject AA's posed derived object
`THH^{||.||}(Z)` or any future normed/tolerant square construction. It
rejects only the strict norm/MAX-face filtration by itself as the missing
square carrier.

## 2. Lemma

```text
Lemma 195.1 (Strict norm weights are not square correspondences).

In the strict CC square, the norm filtration transported through the
universal character has the AA exactness properties:

  N([A]) = |A|,
  N([p^i] - [p^j]) = 2 p^max(i,j) for i != j,
  log N([A]) = Sum_p v_p(A) log p.

The integer product-formula split is exact because the carrier has
multiplication and unique prime factorization. The witness reconstructs
every integer 2 <= n <= 500 from its valuations.

However, norm weights alone are not the monoid-ring algebra and are not a
degree axis. They identify `[A]` and `[-A]` at the level of `|A|`, and AA's
degree dictionary remains observation-grade: the strict filtration has not
constructed a derived spectral sequence whose abutment is THH(Z) with a
weight filtration. The first place where the desired square could live is
the still-unbuilt derived/normed/tolerant object where THH degree and norm
weight coexist.

Moreover the archimedean norm face is carrier-blind by itself. It is
formable on metric controls, but without integer multiplication there are no
valuation MIN faces, no product formula, and no cyclic bar character
algebra. The discriminating content is in the coupled carrier, not in the
MAX face alone.

Therefore strict norm/MAX-face data cannot itself be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_CC_NORM_FILTRATION__STRICT_MAX_FACE_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_norm_filtration_no_go` verifies the local R1 gate, with
`prime_cc_thh_norm_filtration` rerun as the adjacent positive witness.

CNF1 records the positive fact inherited from AA: the strict norm filtration
is real object data. It is exact on monoid classes and on checked difference
classes.

CNF2 records that the product-formula split is an integer-carrier fact:
integer labels reconstruct exactly from prime valuations. This is precisely
what a metric-only control lacks.

CNF3 records that the norm itself is only a weight. It sees `|A|`; it does
not see the signed monoid-ring class, construct a degree, or define a
cohomological grading.

CNF4 records AA's carrier guard. Epstein-style metric controls have
archimedean norm values and the AA witness certifies the corresponding
MAX-face behavior, but they have no integer factorization, valuation MIN
faces, product formula, or cyclic bar algebra. The norm face alone is
therefore carrier-blind.

CNF5 records the exact missing ingredient: no derived normed spectral
sequence and no Bokstedt/THH degree dictionary has been constructed. AA's
index dictionary remains observation-grade.

CNF6 records that the strict norm filtration does not build a non-EM square
functor extracting square cohomology from the strict character object.

CNF7-CNF8 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

CNF9 records the surviving evasion: a derived/normed/tolerant square in
which weight and THH degree coexist carrier-natively.

CNF10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-195:
  NEWLY CLOSED THIS CYCLE:
    - strict CC norm filtration / archimedean MAX face, even with the AA
      product-formula split on strict character labels, as End(S^2/Z),
      square H^2, intersection form, correspondence algebra, Frobenius
      graph, Laurent boundary data, torsor splitter, DD.4 weight>=1 datum,
      or positive Rosati (doc 195).

  STILL ADMISSIBLE:
    - a derived/normed/tolerant square construction whose spectral sequence
      makes norm weight and THH degree coexist and whose abutment constructs
      square cohomology/correspondences;
    - a non-EM square functor extracting new joint/cell-shape data from the
      strict object as actual intersection theory;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The strict norm filtration is a real positive shadow, but
not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CNF.1 strict CC norm filtration as End(S^2/Z)
  A proposal identifies the AA strict norm/MAX face with the square carrier.
  Kill it unless it constructs square H^2 and correspondences.

KILL-CNF.2 MAX face as intersection form
  A proposal uses the Lorentzian MAX face as the intersection form. Kill it:
  the archimedean face alone is carrier-blind and formable on metric controls.

KILL-CNF.3 product-formula weight as THH degree
  A proposal reads log|A| or the product-formula split as the Bokstedt degree
  axis. Kill it unless a derived spectral sequence or degree dictionary is
  constructed with independent constraints.

KILL-CNF.4 normed monoid-ring shadow without non-EM square functor
  A proposal gives normed character data but no non-EM square functor
  extracting H^2/intersection/correspondence data. This is not the square
  correspondence algebra.

KILL-CNF.5 norm filtration without Rosati/Frobenius correspondence
  A proposal gives the MAX/MIN product-formula split but no Frobenius graph
  or positive Rosati. This is not End(S^2/Z).

KILL-CNF.6 norm filtration without Laurent boundary/torsor
  A proposal gives norm weights but no Laurent axis, boundary map, torsor
  splitter, or DD.4 weight>=1 datum. This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 58 = doc 195:
  N1B_CC_NORM_FILTRATION__STRICT_MAX_FACE_NOT_SQUARE_CARRIER__NO_GO.

What got built: no End object. The value is a deletion: AA's strict norm
filtration remains a real product-formula shadow, but strict weights are not
derived degrees or square correspondences.

What remains: construct the derived/normed/tolerant square AA posed, build a
non-EM square functor extracting H^2/intersection/correspondence data, find a
new joint/cell-shape invariant, or return to the in-house PFD/Xbar DD.4
weight>=1 obstruction.
```
