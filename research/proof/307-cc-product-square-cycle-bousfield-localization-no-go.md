# 307 - CC product square-cycle Bousfield localization is not the square carrier

Status: no-go + CC-product-square-cycle-Bousfield-localization deletion, 2026-06-22.
One-hundred-seventieth cycle of the doc-137 construction arc. Doc 306 killed
the model-category replacement shortcut. This document tests the next
categorical repair:

```text
localize the model/category of square-carrier specifications at the missing
projection, DD.4, Rosati, sign, and control-death predicates, then count the
localized object as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_bousfield_localization_no_go`
(BSL1-BSL8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_model_replacement_no_go`,
`prime_int_n1b_cc_product_square_cycle_rezk_completion_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 306 rejected turning a fibrant-cofibrant replacement into represented
existence. The next repair is localization:

```text
Bousfield/model localization at the missing carrier predicates
= local object satisfying projection/DD.4/Rosati/sign/control predicates
= represented compactified zeta square.
```

Genuine localization is useful after the carrier and maps being inverted are
represented. The shortcut is to count localization of a predicate presentation
as construction of the carrier itself.

## 2. Lemma

```text
Lemma 307.1 (Bousfield localization is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The Bousfield-localization package lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new Qbar evidence.
A local object, local equivalence, inverted projection map, inverted boundary
map, inverted Rosati map, inverted sign map, or inverted control-death map is
not an actual zeta square map, proper pullback, boundary localization, Rosati
evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the localized projection equivalence only declares defect zero.
The semantic projection defect remains 27.

Realizing a localized projection map in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The localized DD.4 equivalence does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Localization inverts maps but does not select carrier data. The tested local
object window has 16 primitive directions, two Rosati branches, five
localizing map sets, and two saturation witnesses, hence 320 raw local objects
collapsed to one declared local object with fiber size 320. The q=7 primitive
sign is -13.500 on the Weil anchor and +2.431 on the planted off-circle
q-similitude.

Positive controls have the same Bousfield localization. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the Bousfield-localization wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_BOUSFIELD_LOCALIZATION__LOCAL_OBJECT_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_bousfield_localization_no_go` verifies
eight gates.

BSL1 checks that product+`rep_NS` visible data has only the five represented
slots.

BSL2 checks that the Bousfield-localization package lists all eleven slots but
represents no new `Qbar` evidence.

BSL3 checks projection: the localized projection equivalence has declared
defect zero, while the semantic defect remains 27.

BSL4 checks that realizing a localized projection map changes graph degree
`d1` from 7 to -20 while the count anchor remains 63.

BSL5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

BSL6 checks localization rather than selection: 16 boundary directions, two
Rosati branches, five localizing map sets, two saturation witnesses, 320 raw
local objects, one declared local object, fiber size 320, and on/off-circle
sign separation remain.

BSL7 checks positive control survival: the q=3 control has the same
Bousfield localization, projection defect 11, and no represented control
death.

BSL8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-307:
  NEWLY CLOSED THIS CYCLE:
    - Bousfield/model localization as the carrier;
    - local object as represented Qbar construction;
    - localized projection equivalence as carrier projection formula;
    - localized DD.4 equivalence as boundary killing;
    - inverted Rosati/sign/control maps as carrier selection;
    - controls with the same Bousfield localization.

  POSITIVE INFORMATION RETAINED:
    - localization may invert represented maps of an actual constructed carrier;
    - localization is admissible only after represented carrier data exists.

  STILL ADMISSIBLE:
    - localizing an already constructed compactified zeta square at represented
      maps, preserving actual pullbacks, projection, Rosati, DD.4 boundary,
      graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely a local object in a
      localized specification category.
```

## 5. Kill Conditions

```text
KILL-BSL.1 Bousfield localization as carrier
  Kill localization arguments unless represented Qbar geometry is already
  constructed.

KILL-BSL.2 local object as construction
  A local object in a predicate category is not an actual carrier object with
  maps, proper pullbacks, boundary localization, Rosati, or controls.

KILL-BSL.3 localized projection equivalence
  Inverting a projection predicate is not the projection formula unless
  semantic carrier push-pull against the intersection form is proved.

KILL-BSL.4 localized DD.4 equivalence
  Inverting a DD.4 zero predicate is not DD.4 boundary killing. The actual
  class [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-BSL.5 inverted maps as selection
  Inverting Rosati, sign, or control-death predicates does not select
  carrier-native boundary direction, Rosati branch, or formation obstruction.

KILL-BSL.6 controls with the same localization
  If positive controls have the same localization, formation-level control
  death has failed.
```
