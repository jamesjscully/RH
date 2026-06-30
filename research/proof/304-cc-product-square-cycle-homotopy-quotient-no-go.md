# 304 - CC product square-cycle homotopy quotient is not the square carrier

Status: no-go + CC-product-square-cycle-homotopy-quotient deletion, 2026-06-22.
One-hundred-sixty-seventh cycle of the doc-137 construction arc. Doc 303
killed the contractible choice-space shortcut. This document tests the next
categorical repair:

```text
take the homotopy quotient or 0-truncation of the square-carrier specification
groupoid, collapse paths/automorphisms to a canonical class, and count that
quotient class as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_homotopy_quotient_no_go`
(HQT1-HQT8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_contractible_choice_space_no_go`,
`prime_int_n1b_cc_product_square_cycle_equivalence_univalence_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 303 rejected turning a contractible choice space into represented
existence. The next repair is quotienting:

```text
homotopy quotient / 0-truncation of the specification groupoid
= canonical quotient class
= represented compactified zeta square.
```

Genuine quotienting of redundant presentations is useful after a carrier is
constructed. The shortcut is to count the quotient class of a predicate
groupoid as construction of the carrier itself.

## 2. Lemma

```text
Lemma 304.1 (homotopy quotient is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The homotopy-quotient package lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new Qbar evidence.
A homotopy quotient, 0-truncation, orbit representative, or quotient class is
not an actual zeta square map, proper pullback, boundary localization, Rosati
evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the quotient projection class only declares defect zero. The
semantic projection defect remains 27.

Realizing a quotient representative in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The quotient zero class does not kill the actual DD.4 class. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

The quotient collapse erases labels but does not select carrier data. The
tested quotient window has 16 primitive directions, two Rosati branches, and
three path-cell choices, hence 96 raw states collapsed to one declared
quotient class with fiber size 96. The q=7 primitive sign is -13.500 on the
Weil anchor and +2.431 on the planted off-circle q-similitude.

Positive controls have the same homotopy quotient. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the homotopy-quotient wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_HOMOTOPY_QUOTIENT__QUOTIENT_CLASS_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_homotopy_quotient_no_go` verifies
eight gates.

HQT1 checks that product+`rep_NS` visible data has only the five represented
slots.

HQT2 checks that the homotopy-quotient package lists all eleven slots but
represents no new `Qbar` evidence.

HQT3 checks projection: the quotient projection class has declared defect
zero, while the semantic defect remains 27.

HQT4 checks that realizing a quotient representative changes graph degree
`d1` from 7 to -20 while the count anchor remains 63.

HQT5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

HQT6 checks label erasure rather than selection: 16 boundary directions, two
Rosati branches, three path-cell choices, 96 raw states, one declared quotient
class, fiber size 96, and on/off-circle sign separation remain.

HQT7 checks positive control survival: the q=3 control has the same homotopy
quotient, projection defect 11, and no represented control death.

HQT8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-304:
  NEWLY CLOSED THIS CYCLE:
    - homotopy quotient as the carrier;
    - 0-truncation as represented Qbar construction;
    - quotient class as carrier projection formula;
    - quotient zero class as DD.4 boundary killing;
    - quotient collapse as boundary/Rosati/control selection;
    - controls with the same homotopy quotient.

  POSITIVE INFORMATION RETAINED:
    - redundant presentations of an actual constructed carrier may be quotiented;
    - quotienting is admissible only after represented carrier data exists.

  STILL ADMISSIBLE:
    - forming a homotopy quotient of presentations of an already constructed
      compactified zeta square, preserving actual maps, pullbacks, projection,
      Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely a quotient class in a
      specification groupoid.
```

## 5. Kill Conditions

```text
KILL-HQT.1 homotopy quotient as carrier
  Kill homotopy-quotient arguments unless represented Qbar geometry is already
  constructed.

KILL-HQT.2 0-truncation as construction
  Truncating a predicate groupoid is not an actual carrier object with maps,
  proper pullbacks, boundary localization, Rosati, or controls.

KILL-HQT.3 quotient projection class
  A quotient projection class is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-HQT.4 quotient DD.4 zero
  A quotient zero class is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-HQT.5 quotient collapse as selection
  Erasing labels by quotienting does not select carrier-native boundary
  direction, Rosati branch, or formation obstruction.

KILL-HQT.6 controls with the same quotient
  If positive controls have the same homotopy quotient, formation-level control
  death has failed.
```
