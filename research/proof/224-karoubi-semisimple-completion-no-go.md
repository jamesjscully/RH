# 224 - Karoubi completion does not construct the square carrier

Status: no-go + Karoubi/semisimple-completion boundary, 2026-06-20.
Eighty-seventh cycle of the doc-137 construction arc. Doc 223 killed
numerical/GNS quotienting of a presented carrier as positive Rosati
construction. This document tests the next repair: pseudo-abelianize or
Karoubi-complete the presented/numerical correspondence category, then pass to
its semisimple or numerical-motive quotient.

```text
presented/numerical correspondence carrier
  -> Karoubi / pseudo-abelian completion
  -> semisimple or numerical-motive quotient
  -> projectors and positive Rosati carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_karoubi_semisimple_completion_no_go` (KSC1-KSC6 ALL PASS) --
the finite-field `q=7, Tr(F)=1` Frobenius algebra has no nontrivial rational
idempotents; spectral projectors require scalar extension by the Frobenius
eigenvalue field; finite relation windows admit ghost Karoubi summands;
semisimplification erases extension data; the same completion operations are
formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_numerical_gns_quotient_no_go` (NGQ1-NGQ6 ALL PASS) and
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS).

## 1. Purpose

Doc 223 says numerical radical/GNS quotienting does not construct positive
Rosati. The natural motivic repair is:

```text
complete the category under idempotent splittings;
then semisimplify or pass to numerical motives.
```

This is still not a construction of `End(S^2/Z)`. Karoubi completion can only
split idempotents already present after the chosen scalar and relation
environment. If the finite-field anchor is kept over the rational carrier, the
basic Frobenius algebra has no nontrivial idempotent to split. If one extends
scalars to split the Frobenius polynomial, the spectral projectors use the
eigenvalue field and eigenline choice. If one completes a finite presentation,
ghost summands and their central projectors are not excluded by the finite
relations. If one semisimplifies, nilpotent extension data is erased, not
converted into proper correspondences.

This document rejects only the shortcut:

```text
Karoubi/pseudo-abelian completion or semisimplification of a presented or
numerical correspondence category constructs the square correspondence carrier
required by End(S^2/Z).
```

It does not reject a genuine square carrier whose actual correspondence
category is already pseudo-abelian or semisimple because the carrier produced
the projectors and numerical equivalence theorem first.

## 2. Lemma

```text
Lemma 224.1 (Karoubi completion is closure, not square construction).

For the finite-field q=7, Tr(F)=1 anchor, Frobenius satisfies

    chi_F(T) = T^2 - T + 7,
    discriminant = -27.

Thus Q[F] is a quadratic field. Its rational idempotents are only 0 and 1.
Karoubi completion over the rational carrier therefore supplies no nontrivial
projector.

After scalar extension to the splitting field, spectral projectors exist:

    P_alpha = (F - beta)/(alpha - beta),
    P_beta  = (F - alpha)/(beta - alpha),

but alpha-beta = sqrt(-27). These projectors are not integral/rational
carrier data over Z; they import the eigenvalue field and eigenline split.

Finite presented or numerical windows are not protected by Karoubi completion.
A 5-cycle ghost summand has zero traces in powers 1,2,3,4 and trace 5 in
power 5. Therefore the first four count/trace relations of the finite-field
anchor are unchanged, while the fifth count changes and a new central ghost
projector appears in the completed category.

Semisimplification is also not construction. A Jordan block and its
semisimple part have identical power traces, while the nilpotent arrow is
discarded. This forgets extension data instead of producing fiber-product
composition, projection formula, or Rosati positivity.

The same Karoubi, spectral-splitting, ghost-projector, and semisimplification
operations are formable on control operators with no Euler product, Satake
parameters, rep_NS, square carrier, or positive Rosati.

Consequently Karoubi/pseudo-abelian or semisimple completion constructs no
rep_NS, actual square, proper correspondence category, fiber-product
composition, carrier-native projectors, carrier-native pairing, numerical
motive theorem, Frobenius graph, positive Rosati, DH/Epstein death, DD.4
weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_KAROUBI_SEMISIMPLE_COMPLETION__PROJECTOR_CLOSURE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_karoubi_semisimple_completion_no_go` verifies the six gates.

KSC1 records the finite-field anchor. For `q=7, Tr(F)=1`,

```text
disc(T^2 - T + 7) = -27,
counts n=1..4 = 7, 63, 364, 2331.
```

Since the polynomial is irreducible over `Q`, the rational Frobenius algebra
has only the idempotents `0` and `1`. Rational Karoubi completion adds no
projector that could be promoted to the missing `rep_NS` square.

KSC2 records the scalar-extension escape. Over the splitting field the
spectral projectors are idempotent and complementary, but their coefficients
use `sqrt(-27)`; numerically the projectors have nonzero imaginary part. This
is eigenline import, not carrier construction over `Z`.

KSC3 records finite-window non-determination after completion. Adding a
5-cycle ghost summand preserves the first four traces exactly, creates a
central idempotent projector onto the ghost summand, and changes the fifth
count by

```text
5.
```

Thus finite Karoubi-completed relation data still does not determine the
carrier.

KSC4 records semisimplification erasure. A size-two Jordan block and its
semisimple part have the same power traces through the tested window, while
the nilpotent arrow has rank one and square zero. Passing to the semisimple
part forgets this data; it does not construct proper correspondences.

KSC5 records control formability. A control companion operator with
discriminant `-31` has the same pattern: rationally no nontrivial idempotent,
spectral projectors after scalar extension, and no Euler/Satake/`rep_NS`/
square/Rosati input.

KSC6 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native projectors,
carrier-native pairing, numerical motive theorem, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-224:
  NEWLY CLOSED THIS CYCLE:
    - Karoubi or pseudo-abelian completion of a presented/numerical carrier as
      square construction, spectral projector splitting as carrier-native
      projector construction, finite completed relation windows as carrier
      determination, and semisimplification as proper correspondence calculus
      (doc 224).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose correspondence category supplies
      projectors before completion is invoked;
    - a carrier-native numerical equivalence theorem, not a post-hoc
      semisimple quotient of relation data;
    - a theorem excluding ghost summands from the actual carrier;
    - a positive Rosati pairing produced by the square polarization, with
      controls killed at carrier formation.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category, carrier-native projectors and numerical
      equivalence, fiber-product composition, carrier-native degree maps,
      canonical pairing and projection formula, off-diagonal intersection
      form, preserved trace/count anchor, positive Rosati, DD.4 weight>=1
      data, and square-side properness.
```

R1 remains open. This cycle closes the Karoubi/semisimple completion repair:
closure under projectors is not construction of the projectors' square
carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-KSC.1 Karoubi completion as square construction
  A proposal pseudo-abelianizes a presented or numerical category and calls
  the completed category the square. Kill it unless the underlying square
  carrier constructed the projectors first.

KILL-KSC.2 spectral projectors as carrier-native idempotents
  A proposal splits Frobenius by eigenprojectors. Kill it unless the scalar
  field, eigenlines, and projectors are constructed over the zeta carrier, not
  imported by scalar extension.

KILL-KSC.3 finite completed window
  A proposal verifies finitely many relations after Karoubi completion. Kill
  it unless ghost idempotent summands are excluded carrier-natively.

KILL-KSC.4 semisimplification as correspondence calculus
  A proposal passes to a semisimple quotient and treats the result as proper
  correspondence composition. Kill it unless no required carrier extension,
  nilpotent, projection, degree, or pairing data has merely been erased.

KILL-KSC.5 control survival
  A proposal's Karoubi/semisimple completion can be formed on arbitrary
  control operators or count windows. Kill it unless controls die at carrier
  formation.
```
