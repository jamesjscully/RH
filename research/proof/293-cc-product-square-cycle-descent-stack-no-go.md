# 293 - CC product square-cycle descent stack is not the square carrier

Status: no-go + CC-product-square-cycle-descent-stack deletion,
2026-06-22. One-hundred-fifty-sixth cycle of the doc-137 construction arc.
Doc 292 killed exact/regular completion of the product square-cycle syntax.
This document tests the next categorical repair:

```text
cover the product by local square-cycle charts, make pullbacks, projection,
DD.4 killing, Rosati, and control death local, then claim
sheafification/descent glues them into global carrier evidence.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_descent_stack_no_go` (DSC1-DSC8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_exact_completion_no_go`,
`prime_int_n1b_cc_product_square_cycle_category_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 292 rejected exact completion of syntax as represented evidence. The next
shortcut is local-to-global:

```text
local square-cycle charts + local exact/projection/Rosati/DD.4 cells
  + descent glue = global square carrier.
```

Descent is a real requirement for any actual `Qbar` construction. The no-go
is that descent of local syntactic cells is not the same thing as represented
global carrier geometry.

## 2. Lemma

```text
Lemma 293.1 (descent of local cells is not global Qbar evidence).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

A local descent-stack wrapper can declare all eleven represented-carrier
slots on local charts:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But the represented-carrier gate still sees only the five visible slots
above. Local pullbacks, local projection relations, local localization
objects, local Rosati cells, local control-death cells, and formal descent
glue are not global `Qbar` maps or proofs.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but local projection descent only declares defect zero. The semantic
projection defect remains 27.

Gluing that relation into NS triples repeats the same retuning damage:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

Local DD.4 zero cells do not kill the global DD.4 class. With two local zero
cells and truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Descent gluing does not select the DD.4 boundary direction or carrier Rosati.
The tested boundary window has 16 primitive directions and two local charts
admit 256 primitive-direction assignments. The q=7 primitive sign is -13.500
on the Weil anchor and +2.431 on the planted off-circle q-similitude.

Positive controls admit the same descent-stack wrapper. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently descent still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_DESCENT_STACK__LOCAL_CELLS_NOT_GLOBAL_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_descent_stack_no_go` verifies eight
gates.

DSC1 checks that product+`rep_NS` visible data has only the five represented
slots.

DSC2 checks that local descent charts declare all eleven slots but represent
no new global `Qbar` evidence.

DSC3 checks projection: local projection has declared defect zero, while the
semantic defect remains 27.

DSC4 checks that gluing the projection relation into NS triples changes graph
degree `d1` from 7 to -20 while the count anchor remains 63.

DSC5 recomputes DD.4 with two local zero cells:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

DSC6 checks boundary-direction and Rosati nonselection: there are 16
primitive directions, 256 two-chart local assignments, and the on/off-circle
signs still differ.

DSC7 checks positive control survival with projection defect 11 and no
represented control death.

DSC8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-293:
  NEWLY CLOSED THIS CYCLE:
    - local descent-stack square-cycle wrappers;
    - local projection descent as the global projection formula;
    - local DD.4 zero cells as global boundary killing;
    - descent glue as DD.4 boundary-direction selection;
    - local Rosati/control cells as carrier Rosati/control death.

  POSITIVE INFORMATION RETAINED:
    - the real carrier should satisfy descent;
    - descent is admissible only after the local objects and maps are
      represented pieces of the same global Qbar.

  STILL ADMISSIBLE:
    - a construction of Qbar with a descent-compatible proper correspondence
      category whose global pullbacks, projection formula, Rosati, DD.4
      boundary, graph composition, and control death are carrier theorems.

  STILL OPEN:
    - construct global represented carrier geometry first; then prove descent.
```

## 5. Kill Conditions

```text
KILL-DSC.1 local chart actualization
  Kill local square-cycle chart arguments unless the charts are represented
  open pieces of one global Qbar and glue to actual global maps.

KILL-DSC.2 projection by local descent
  Local projection cells do not count unless they glue to a global carrier
  push-pull theorem against the intersection form.

KILL-DSC.3 NS retuning by gluing
  Kill descent relations whose realization in NS triples changes graph
  degree, trace, count, or endpoint data.

KILL-DSC.4 DD.4 zero by local cells
  Local DD.4 zero cells do not count. The global class [(1+z)^-1] must map
  to zero in the carrier boundary sequence.

KILL-DSC.5 boundary direction by descent glue
  Descent glue does not select the primitive DD.4 direction unless the global
  carrier selects it.

KILL-DSC.6 control death by local stack
  Controls must fail to instantiate the global carrier at formation; local
  stack control-death cells do not count.
```
