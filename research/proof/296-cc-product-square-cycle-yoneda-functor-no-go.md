# 296 - CC product square-cycle Yoneda functor is not the square carrier

Status: no-go + CC-product-square-cycle-Yoneda-functor deletion, 2026-06-22.
One-hundred-fifty-ninth cycle of the doc-137 construction arc. Doc 295
killed the moduli/classifying-stack shortcut. This document tests the next
categorical repair:

```text
replace the carrier by the functor of points/specification functor of
square-carrier packages, and use Yoneda language to treat formal points and
natural transformations as represented geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_yoneda_functor_no_go` (YND1-YND8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_moduli_stack_no_go`,
`prime_int_n1b_cc_product_square_cycle_hyperdescent_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 295 rejected a classifying stack as the carrier. The next repair is to
shift from moduli objects to functors:

```text
square-carrier specification functor + Yoneda language = represented carrier.
```

Yoneda is a theorem after representability: if `Qbar` exists, its functor of
points determines it. The shortcut reverses the direction by treating the
specification functor itself as represented geometry.

## 2. Lemma

```text
Lemma 296.1 (a specification functor is not a representing object).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The square-carrier functor of points lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Formal points, predicates, and natural transformations are not actual zeta
square maps, pullbacks, boundary localization, Rosati evaluation, or
control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the Yoneda projection predicate only declares defect zero. The
semantic projection defect remains 27.

Realizing the projection predicate in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The DD.4 zero predicate does not kill the actual DD.4 class. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Functor points parameterize choices rather than selecting carrier data. The
tested boundary window has 16 primitive directions; including two Rosati
branches gives 32 natural branches. The q=7 primitive sign is -13.500 on the
Weil anchor and +2.431 on the planted off-circle q-similitude.

Positive controls are points of the same specification functor. The q=3
control has semantic projection defect 11, negative primitive sign -5.500,
the same five represented slots, and no formation-level control death.

Consequently the Yoneda/functor wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_YONEDA_FUNCTOR__SPECIFICATION_FUNCTOR_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_yoneda_functor_no_go` verifies eight
gates.

YND1 checks that product+`rep_NS` visible data has only the five represented
slots.

YND2 checks that the functor of points lists all eleven slots but represents
no new `Qbar` evidence.

YND3 checks projection: the predicate has declared defect zero, while the
semantic defect remains 27.

YND4 checks that realizing the predicate changes graph degree `d1` from 7 to
-20 while the count anchor remains 63.

YND5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

YND6 checks parameterization rather than selection: 16 boundary directions,
32 natural branches, and on/off-circle sign separation remain.

YND7 checks positive control survival: the q=3 control is a point of the same
specification functor with projection defect 11 and no represented control
death.

YND8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-296:
  NEWLY CLOSED THIS CYCLE:
    - square-carrier specification functor as the carrier;
    - Yoneda language as representability proof;
    - projection predicate as carrier projection formula;
    - DD.4 zero predicate as carrier boundary killing;
    - functor points/natural transformations as boundary/Rosati/control
      selection.

  POSITIVE INFORMATION RETAINED:
    - once Qbar exists, its functor of points will be useful and determining;
    - Yoneda is admissible only after a representing object is constructed or
      a representability theorem is proved.

  STILL ADMISSIBLE:
    - a representability theorem proving that the square-carrier functor is
      represented by a compactified zeta square with actual maps, pullbacks,
      projection, Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - prove representability by constructing the representing object.
```

## 5. Kill Conditions

```text
KILL-YND.1 functor of points as carrier
  Kill functor-of-points arguments unless a representing Qbar object is
  constructed.

KILL-YND.2 Yoneda as construction
  Yoneda determines represented objects; it does not turn a specification
  functor into geometry without representability.

KILL-YND.3 projection predicate
  A projection predicate is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-YND.4 DD.4 zero predicate
  A zero predicate is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-YND.5 functor points as selection
  Parameterizing boundary directions, Rosati branches, or controls is not
  carrier selection.

KILL-YND.6 controls as functor points
  If positive controls are points of the same specification functor,
  formation-level control death has failed.
```
