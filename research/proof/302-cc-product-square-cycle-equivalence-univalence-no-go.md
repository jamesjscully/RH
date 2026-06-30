# 302 - CC product square-cycle equivalence/univalence is not the square carrier

Status: no-go + CC-product-square-cycle-equivalence-univalence deletion, 2026-06-22.
One-hundred-sixty-fifth cycle of the doc-137 construction arc. Doc 301 killed
the universal-property/recognition shortcut. This document tests the next
categorical repair:

```text
replace construction of the compactified zeta square by an equivalence of
square-carrier specifications, univalence, or transport of structure along
equivalence, and count equivalent packages as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_equivalence_univalence_no_go`
(EQV1-EQV8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_universal_property_recognition_no_go`,
`prime_int_n1b_cc_product_square_cycle_tannakian_reconstruction_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 301 rejected turning universal recognition into represented existence.
The next repair is equivalence:

```text
equivalent square-carrier specifications + univalence/transport
= represented compactified zeta square.
```

Genuine equivalent presentations of an already constructed carrier should be
interchangeable. The shortcut is to count equivalence or definitional
identification as construction.

## 2. Lemma

```text
Lemma 302.1 (equivalence is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The equivalence/univalence package lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Equivalences of specifications, univalence paths, and transported predicates
are not actual zeta square maps, pullbacks, boundary localization, Rosati
evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but transported projection equality only declares defect zero. The
semantic projection defect remains 27.

Realizing the transported equality in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The equivalence-class zero does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Equivalences parameterize choices rather than selecting carrier data. The
tested boundary window has 16 primitive directions, two Rosati branches, and
two equivalence orientations, hence 64 equivalence branches. The q=7
primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls are equivalent packages too. The q=3 control has semantic
projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the equivalence/univalence wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_EQUIVALENCE_UNIVALENCE__TRANSPORT_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_equivalence_univalence_no_go` verifies
eight gates.

EQV1 checks that product+`rep_NS` visible data has only the five represented
slots.

EQV2 checks that the equivalence package lists all eleven slots but represents
no new `Qbar` evidence.

EQV3 checks projection: transported projection equality has declared defect
zero, while the semantic defect remains 27.

EQV4 checks that realizing the transported equality changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

EQV5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

EQV6 checks parameterization rather than selection: 16 boundary directions,
two Rosati branches, two equivalence orientations, 64 equivalence branches,
and on/off-circle sign separation remain.

EQV7 checks positive control survival: the q=3 control is an equivalent
package with projection defect 11 and no represented control death.

EQV8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-302:
  NEWLY CLOSED THIS CYCLE:
    - equivalence of square-carrier specifications as the carrier;
    - univalence/path equality as represented existence;
    - transport as carrier construction;
    - transported projection equality as carrier projection formula;
    - equivalence-class zero as carrier boundary killing;
    - equivalence choices as boundary/Rosati/control selection.

  POSITIVE INFORMATION RETAINED:
    - actual equivalent presentations of Qbar should be interchangeable;
    - equivalence and univalence are admissible only after one side is already
      represented by the compactified zeta square.

  STILL ADMISSIBLE:
    - an equivalence theorem between two already constructed represented
      carriers, preserving actual maps, pullbacks, projection, Rosati, DD.4
      boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely an equivalence class of
      specifications.
```

## 5. Kill Conditions

```text
KILL-EQV.1 equivalence as carrier
  Kill equivalence/univalence arguments unless at least one equivalent object
  is constructed as actual Qbar geometry with maps, boundary, and cycles.

KILL-EQV.2 transport as construction
  Transport moves represented structure after construction; it does not
  construct carrier maps, pullbacks, Rosati, or boundary localization.

KILL-EQV.3 transported projection equality
  A transported equality is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-EQV.4 equivalence-class DD.4 zero
  An equivalence-class zero is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-EQV.5 equivalence choices as selection
  Parameterizing boundary directions, Rosati branches, or equivalence
  orientations is not carrier selection.

KILL-EQV.6 controls as equivalent packages
  If positive controls are equivalent packages too, formation-level control
  death has failed.
```
