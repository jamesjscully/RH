# 306 - CC product square-cycle model replacement is not the square carrier

Status: no-go + CC-product-square-cycle-model-replacement deletion, 2026-06-22.
One-hundred-sixty-ninth cycle of the doc-137 construction arc. Doc 305 killed
the Rezk/coherent-nerve completion shortcut. This document tests the next
categorical repair:

```text
replace the compactified zeta square by a fibrant-cofibrant replacement of the
square-carrier specification, use lifting/path objects to fill the missing
predicates, and count the replacement as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_model_replacement_no_go`
(MCR1-MCR8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_rezk_completion_no_go`,
`prime_int_n1b_cc_product_square_cycle_homotopy_quotient_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 305 rejected turning a completed presentation into represented existence.
The next repair is model replacement:

```text
fibrant-cofibrant replacement of the square-carrier specification
+ lifting/path/cylinder fillers
= represented compactified zeta square.
```

Genuine model replacements are useful for already constructed objects inside a
model category. The shortcut is to count replacement of a predicate
presentation as construction of the carrier itself.

## 2. Lemma

```text
Lemma 306.1 (model replacement is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The fibrant-cofibrant replacement package lists all eleven required
predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new Qbar evidence.
A weak equivalence to the specification, fibrant replacement, cofibrant
replacement, path object, cylinder object, or lifting filler is not an actual
zeta square map, proper pullback, boundary localization, Rosati evaluation, or
control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the lifting projection filler only declares defect zero. The
semantic projection defect remains 27.

Realizing a lifting filler in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The replacement nullhomotopy does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Model replacement adds lifts but does not select carrier data. The tested
replacement window has 16 primitive directions, two Rosati branches, two
cofibrant replacements, three fibrant lifting choices, and two cylinder/path
choices, hence 384 raw model replacements collapsed to one declared
replacement object with fiber size 384. The q=7 primitive sign is -13.500 on
the Weil anchor and +2.431 on the planted off-circle q-similitude.

Positive controls have the same model replacement. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the fibrant-cofibrant replacement wrapper still misses
represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_MODEL_REPLACEMENT__FIBRANT_COFIBRANT_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_model_replacement_no_go` verifies
eight gates.

MCR1 checks that product+`rep_NS` visible data has only the five represented
slots.

MCR2 checks that the fibrant-cofibrant replacement package lists all eleven
slots but represents no new `Qbar` evidence.

MCR3 checks projection: the lifting projection filler has declared defect
zero, while the semantic defect remains 27.

MCR4 checks that realizing a lifting filler changes graph degree `d1` from 7
to -20 while the count anchor remains 63.

MCR5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

MCR6 checks lift addition rather than selection: 16 boundary directions, two
Rosati branches, two cofibrant replacements, three fibrant lifting choices,
two cylinder/path choices, 384 raw model replacements, one declared
replacement object, fiber size 384, and on/off-circle sign separation remain.

MCR7 checks positive control survival: the q=3 control has the same model
replacement, projection defect 11, and no represented control death.

MCR8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-306:
  NEWLY CLOSED THIS CYCLE:
    - fibrant-cofibrant replacement as the carrier;
    - weak equivalence to specification as represented Qbar construction;
    - lifting filler as carrier projection formula;
    - replacement nullhomotopy as DD.4 boundary killing;
    - path/cylinder/lifting choices as boundary/Rosati/control selection;
    - controls with the same model replacement.

  POSITIVE INFORMATION RETAINED:
    - model-category replacement may present an actual constructed carrier;
    - replacement is admissible only after represented carrier data exists.

  STILL ADMISSIBLE:
    - replacing an already constructed compactified zeta square inside a model
      category, preserving actual maps, pullbacks, projection, Rosati, DD.4
      boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely a fibrant-cofibrant
      replacement of a specification.
```

## 5. Kill Conditions

```text
KILL-MCR.1 fibrant-cofibrant replacement as carrier
  Kill model-replacement arguments unless represented Qbar geometry is already
  constructed.

KILL-MCR.2 weak equivalence as construction
  A weak equivalence to a predicate specification is not an actual carrier
  object with maps, proper pullbacks, boundary localization, Rosati, or
  controls.

KILL-MCR.3 lifting projection filler
  A model lifting filler for projection is not the projection formula unless
  semantic carrier push-pull against the intersection form is proved.

KILL-MCR.4 replacement DD.4 nullhomotopy
  A replacement nullhomotopy is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-MCR.5 path/cylinder/lifting choices as selection
  Adding path objects, cylinder objects, or lifting fillers does not select
  carrier-native boundary direction, Rosati branch, or formation obstruction.

KILL-MCR.6 controls with the same replacement
  If positive controls have the same model replacement, formation-level control
  death has failed.
```
