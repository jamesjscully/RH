# 298 - CC product square-cycle pro-representable limit is not the square carrier

Status: no-go + CC-product-square-cycle-pro-representable-limit deletion, 2026-06-22.
One-hundred-sixty-first cycle of the doc-137 construction arc. Doc 297 killed
the reflective-completion shortcut. This document tests the next categorical
repair:

```text
apply a pro-representable inverse-limit system to the square-carrier
specification functor, and count the resulting pro-object as represented
geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_pro_representable_limit_no_go` (PRL1-PRL8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_reflective_completion_no_go`,
`prime_int_n1b_cc_product_square_cycle_yoneda_functor_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 297 rejected freely forcing representability by reflection. The next
repair is to pass to a tower of finite approximations:

```text
pro-representable inverse-limit of the square-carrier specification
functor = represented carrier.
```

A genuine carrier may later be studied through compatible finite
approximations. The shortcut is to count a pro-object, transition maps, and
limit cones as the missing represented geometry.

## 2. Lemma

```text
Lemma 298.1 (a pro-representable limit is not a representing object).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The pro-representable inverse-limit lists or forces all eleven
required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Formal finite stages, transition maps, and limit cones are not actual zeta
square maps, pullbacks, boundary localization, Rosati evaluation, or
control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the pro-limit projection relation only declares defect zero. The
semantic projection defect remains 27.

Realizing the projection predicate in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The DD.4 zero relation does not kill the actual DD.4 class. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Pro-limit points parameterize choices rather than selecting carrier data. The
tested boundary window has 16 primitive directions; including two Rosati
branches gives 32 stage branches and 32768 three-stage tower prefixes. The
q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls pass through the same pro-limit system. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the pro-representable-limit wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_PRO_REPRESENTABLE_LIMIT__PRO_OBJECT_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_pro_representable_limit_no_go` verifies eight
gates.

PRL1 checks that product+`rep_NS` visible data has only the five represented
slots.

PRL2 checks that the pro-representable limit lists all eleven slots but
represents no new `Qbar` evidence.

PRL3 checks projection: the pro-limit relation has declared defect zero,
while the semantic defect remains 27.

PRL4 checks that realizing the pro-limit relation changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

PRL5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

PRL6 checks parameterization rather than selection: 16 boundary directions,
32 stage branches and 32768 tower prefixes, and on/off-circle sign separation
remain.

PRL7 checks positive control survival: the q=3 control passes through the
same pro-limit system with projection defect 11 and no represented control
death.

PRL8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-298:
  NEWLY CLOSED THIS CYCLE:
    - square-carrier pro-representable limit as the carrier;
    - pro-object/inverse-limit object as representability proof;
    - pro-limit projection relation as carrier projection formula;
    - DD.4 zero relation as carrier boundary killing;
    - pro-limit points/transition maps as boundary/Rosati/control
      selection.

  POSITIVE INFORMATION RETAINED:
    - a real representability theorem may be stated by an adjunction after the
      representing object exists;
    - Yoneda and pro-limit language are admissible only downstream of
      constructed carrier geometry.

  STILL ADMISSIBLE:
    - a representability theorem proving that the square-carrier functor is
      represented by a compactified zeta square with actual maps, pullbacks,
      projection, Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - prove representability by constructing the representing object.
```

## 5. Kill Conditions

```text
KILL-PRL.1 pro-representable limit as carrier
  Kill pro-object arguments unless the inverse limit is proved to be actual
  Qbar geometry with maps, boundary, and cycles.

KILL-PRL.2 finite stages as construction
  Compatible finite stages are not carrier construction unless the limit
  preserves the finite-field anchors and supplies actual pullbacks, boundary
  localization, Rosati, and control death.

KILL-PRL.3 pro-limit projection relation
  A freely imposed projection relation is not the projection formula unless
  semantic carrier push-pull against the intersection form is proved.

KILL-PRL.4 DD.4 zero relation
  A freely imposed zero relation is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-PRL.5 pro-limit points as selection
  Parameterizing boundary directions, Rosati branches, or controls is not
  carrier selection.

KILL-PRL.6 controls as pro-limit points
  If positive controls pass through the same pro-limit system,
  formation-level control death has failed.
```
