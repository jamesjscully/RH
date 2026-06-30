# 301 - CC product square-cycle universal-property recognition is not the square carrier

Status: no-go + CC-product-square-cycle-universal-property-recognition deletion, 2026-06-22.
One-hundred-sixty-fourth cycle of the doc-137 construction arc. Doc 300
killed the Tannakian/monadic reconstruction shortcut. This document tests the
next categorical repair:

```text
characterize the compactified zeta square by a universal property,
initial/final object, or uniqueness-up-to-unique-isomorphism recognition
theorem, and count recognition as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_universal_property_recognition_no_go`
(UPR1-UPR8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_tannakian_reconstruction_no_go`,
`prime_int_n1b_cc_product_square_cycle_artin_representability_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 300 rejected reconstructing the square from tensor/fiber-functor data.
The next repair is recognition:

```text
universal property + initial/final square-carrier package + unique isomorphism
= compactified zeta square.
```

A genuine carrier should satisfy a strong universal property once it exists.
The shortcut is to count uniqueness, initiality, finality, or a recognition
theorem as represented existence.

## 2. Lemma

```text
Lemma 301.1 (recognition is not represented existence).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The universal-property recognition package lists all eleven required
predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Universal properties, initial/final objects, and unique-isomorphism statements
are not actual zeta square maps, pullbacks, boundary localization, Rosati
evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the universal projection square only declares defect zero. The
semantic projection defect remains 27.

Realizing the universal relation in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The universal zero morphism does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Universal properties parameterize choices rather than selecting carrier data.
The tested boundary window has 16 primitive directions, two Rosati branches,
and two variance choices (initial/final), hence 64 recognition branches. The
q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls satisfy the same recognition theorem. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the universal-property recognition wrapper still misses
represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_UNIVERSAL_PROPERTY_RECOGNITION__UNIQUENESS_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_universal_property_recognition_no_go`
verifies eight gates.

UPR1 checks that product+`rep_NS` visible data has only the five represented
slots.

UPR2 checks that the recognition package lists all eleven slots but
represents no new `Qbar` evidence.

UPR3 checks projection: the universal square has declared defect zero, while
the semantic defect remains 27.

UPR4 checks that realizing the universal relation changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

UPR5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

UPR6 checks parameterization rather than selection: 16 boundary directions,
two Rosati branches, two variance choices, 64 recognition branches, and
on/off-circle sign separation remain.

UPR7 checks positive control survival: the q=3 control satisfies the same
recognition theorem with projection defect 11 and no represented control
death.

UPR8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-301:
  NEWLY CLOSED THIS CYCLE:
    - universal property as the carrier;
    - initial/final object as represented existence;
    - unique isomorphism as carrier construction;
    - universal projection square as carrier projection formula;
    - universal zero morphism as carrier boundary killing;
    - recognition choices as boundary/Rosati/control selection.

  POSITIVE INFORMATION RETAINED:
    - an actual carrier should satisfy a strong universal property;
    - recognition is admissible only after existence, or when the recognized
      object is explicitly constructed and proved to be Qbar.

  STILL ADMISSIBLE:
    - a recognition theorem whose recognized object is explicitly constructed
      as the compactified zeta square and whose universal property proves
      actual maps, pullbacks, projection, Rosati, DD.4 boundary, graph
      composition, and control death.

  STILL OPEN:
    - construct the represented square, not just a uniqueness theorem for one.
```

## 5. Kill Conditions

```text
KILL-UPR.1 universal property as carrier
  Kill universal-property arguments unless the object satisfying the property
  is constructed as actual Qbar geometry with maps, boundary, and cycles.

KILL-UPR.2 uniqueness as existence
  Unique isomorphism characterizes an object after existence; it does not
  construct carrier maps, pullbacks, Rosati, or boundary localization.

KILL-UPR.3 universal projection square
  A universal commuting square is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-UPR.4 universal DD.4 zero
  A universal zero morphism is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-UPR.5 universal choices as selection
  Parameterizing boundary directions, Rosati branches, or variance choices is
  not carrier selection.

KILL-UPR.6 controls satisfying recognition
  If positive controls satisfy the same recognition theorem, formation-level
  control death has failed.
```
