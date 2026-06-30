# 303 - CC product square-cycle contractible choice space is not the square carrier

Status: no-go + CC-product-square-cycle-contractible-choice-space deletion, 2026-06-22.
One-hundred-sixty-sixth cycle of the doc-137 construction arc. Doc 302 killed
the equivalence/univalence shortcut. This document tests the next categorical
repair:

```text
prove the space of square-carrier choices is contractible, extract a canonical
point, and count that canonical choice as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_contractible_choice_space_no_go`
(CTS1-CTS8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_equivalence_univalence_no_go`,
`prime_int_n1b_cc_product_square_cycle_universal_property_recognition_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 302 rejected turning equivalence or transport into represented existence.
The next repair is contractibility:

```text
the space of square-carrier choices is contractible
= there is a canonical point
= represented compactified zeta square.
```

Genuine coherently unique structure is desirable after a carrier is
constructed. The shortcut is to count contractible choice data or a canonical
point as construction of the carrier itself.

## 2. Lemma

```text
Lemma 303.1 (contractible choice space is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The contractible choice-space package lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new Qbar evidence.
A contraction of the predicate space, a canonical point, or a path to that
point is not an actual zeta square map, proper pullback, boundary
localization, Rosati evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the canonical projection choice only declares defect zero. The
semantic projection defect remains 27.

Realizing the canonical choice in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The contractible zero choice does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Contractibility collapses labels but does not select carrier data. The tested
choice window has 16 primitive directions, two Rosati branches, and three
contraction witnesses, hence 96 raw choices collapsed to one declared
canonical point. The q=7 primitive sign is -13.500 on the Weil anchor and
+2.431 on the planted off-circle q-similitude.

Positive controls have the same contractible choice space. The q=3 control
has semantic projection defect 11, negative primitive sign -5.500, the same
five represented slots, and no formation-level control death.

Consequently the contractible-choice-space wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_CONTRACTIBLE_CHOICE_SPACE__CANONICAL_POINT_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_contractible_choice_space_no_go`
verifies eight gates.

CTS1 checks that product+`rep_NS` visible data has only the five represented
slots.

CTS2 checks that the contractible choice-space package lists all eleven slots
but represents no new `Qbar` evidence.

CTS3 checks projection: the canonical projection choice has declared defect
zero, while the semantic defect remains 27.

CTS4 checks that realizing the canonical choice changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

CTS5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

CTS6 checks label collapse rather than selection: 16 boundary directions, two
Rosati branches, three contraction witnesses, 96 raw choices, one declared
canonical point, and on/off-circle sign separation remain.

CTS7 checks positive control survival: the q=3 control has the same
contractible choice space, projection defect 11, and no represented control
death.

CTS8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-303:
  NEWLY CLOSED THIS CYCLE:
    - contractible choice space as the carrier;
    - canonical point as represented Qbar construction;
    - canonical projection choice as carrier projection formula;
    - contractible zero choice as DD.4 boundary killing;
    - contraction as boundary/Rosati/control selection;
    - controls with the same contractible choice space.

  POSITIVE INFORMATION RETAINED:
    - an actual constructed carrier should have coherently unique structure;
    - contractibility is admissible only after represented carrier data exists.

  STILL ADMISSIBLE:
    - proving the choice space of an already constructed compactified zeta
      square is contractible, preserving actual maps, pullbacks, projection,
      Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely a canonical point in a
      contractible specification space.
```

## 5. Kill Conditions

```text
KILL-CTS.1 contractible choice space as carrier
  Kill contractibility arguments unless represented Qbar geometry is already
  constructed.

KILL-CTS.2 canonical point as construction
  A canonical point of a predicate space is not an actual carrier object with
  maps, proper pullbacks, boundary localization, Rosati, or controls.

KILL-CTS.3 canonical projection choice
  A chosen projection witness is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-CTS.4 contractible DD.4 zero
  A contractible zero choice is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-CTS.5 contraction as selection
  Collapsing labels to one canonical point does not select carrier-native
  boundary direction, Rosati branch, or formation obstruction.

KILL-CTS.6 controls with contractible choice space
  If positive controls have the same contractible choice space, formation-level
  control death has failed.
```
