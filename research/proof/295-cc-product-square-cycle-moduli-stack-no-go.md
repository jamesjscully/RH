# 295 - CC product square-cycle moduli stack is not the square carrier

Status: no-go + CC-product-square-cycle-moduli-stack deletion, 2026-06-22.
One-hundred-fifty-eighth cycle of the doc-137 construction arc. Doc 294
killed hyperdescent/homotopy-coherent descent of local square-cycle syntax.
This document tests the next categorical repair:

```text
form a moduli/classifying stack of square-carrier packages and use its
tautological universal package as the missing carrier.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_moduli_stack_no_go` (MDS1-MDS8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_hyperdescent_no_go`,
`prime_int_n1b_cc_product_square_cycle_descent_stack_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

After descent and hyperdescent fail as shortcuts, the next categorical move is
to classify the desired structure:

```text
stack of all square-carrier packages + universal tautological package.
```

A genuine carrier can have a moduli interpretation after it is constructed.
The no-go is that a classifying stack of packages is not itself represented
zeta-square geometry.

## 2. Lemma

```text
Lemma 295.1 (the tautological package is not represented Qbar geometry).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The moduli/classifying stack tautological package declares all eleven
represented-carrier slots:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
The represented slots remain the five visible slots above.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the universal projection relation only declares defect zero.
The semantic projection defect remains 27.

Realizing the universal projection relation in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The universal DD.4 zero object does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

The moduli package parameterizes choices rather than selecting carrier data.
The tested boundary window has 16 primitive directions; with two Rosati/sign
branches this gives 32 moduli branches. The q=7 primitive sign is -13.500 on
the Weil anchor and +2.431 on the planted off-circle q-similitude.

Positive controls define points of the same moduli stack. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the moduli/classifying stack wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_MODULI_STACK__TAUTOLOGICAL_PACKAGE_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_moduli_stack_no_go` verifies eight
gates.

MDS1 checks that product+`rep_NS` visible data has only the five represented
slots.

MDS2 checks that the tautological moduli package declares all eleven slots
but represents no new `Qbar` evidence.

MDS3 checks projection: universal projection has declared defect zero, while
the semantic defect remains 27.

MDS4 checks that realizing the universal relation changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

MDS5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

MDS6 checks parameterization rather than selection: 16 boundary directions,
two Rosati branches, and on/off-circle sign separation remain.

MDS7 checks positive control survival: the q=3 control defines a point of the
same moduli stack with projection defect 11 and no represented control death.

MDS8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-295:
  NEWLY CLOSED THIS CYCLE:
    - moduli/classifying stack of square-carrier packages;
    - tautological universal package as represented Qbar;
    - universal projection relation as carrier projection formula;
    - universal DD.4 zero object as carrier boundary killing;
    - moduli parameterization as boundary/Rosati/control selection.

  POSITIVE INFORMATION RETAINED:
    - an actual carrier may later have a useful moduli interpretation;
    - moduli language is admissible only downstream of represented carrier
      geometry or a representability theorem constructing Qbar.

  STILL ADMISSIBLE:
    - a moduli theorem whose representing object is the compactified zeta
      square itself and whose universal family is proved to be the actual
      carrier with proper pullbacks, projection, Rosati, DD.4 boundary, graph
      composition, and control death.

  STILL OPEN:
    - construct the representing object, not just the functor of desired
      square-carrier packages.
```

## 5. Kill Conditions

```text
KILL-MDS.1 classifying stack as carrier
  Kill moduli/classifying-stack arguments unless the stack is represented by
  an actual Qbar carrying the required maps and boundary.

KILL-MDS.2 tautological package as evidence
  Tautological universal labels do not count as represented evidence.

KILL-MDS.3 universal projection relation
  A universal relation is not the projection formula unless it proves
  semantic carrier push-pull against the intersection form.

KILL-MDS.4 universal DD.4 zero object
  A universal zero object is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-MDS.5 moduli parameterization as selection
  Parameterizing boundary directions, Rosati branches, or controls is not
  carrier selection.

KILL-MDS.6 controls as moduli points
  If positive controls define points of the same moduli stack, formation-level
  control death has failed.
```
