# 294 - CC product square-cycle hyperdescent is not the square carrier

Status: no-go + CC-product-square-cycle-hyperdescent deletion, 2026-06-22.
One-hundred-fifty-seventh cycle of the doc-137 construction arc. Doc 293
killed ordinary local descent/stack gluing of product square-cycle syntax.
This document tests the next categorical repair:

```text
replace descent by hyperdescent/homotopy-coherent descent over repeated
refinements, with higher coherence cells for projection, DD.4 killing,
Rosati, and control death.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_hyperdescent_no_go` (HDS1-HDS8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_descent_stack_no_go`,
`prime_int_n1b_cc_product_square_cycle_exact_completion_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 293 rejected ordinary local descent as represented global evidence. The
next repair is to move the same local cells into a hyperdescent or
homotopy-coherent setting:

```text
local cells on repeated refinements + higher coherence
  = global square carrier.
```

A real `Qbar` construction should satisfy whatever descent its geometry
requires. But hyperdescent of local syntactic cells is still not a global
carrier object, map, boundary sequence, Rosati theorem, or control-formation
obstruction.

## 2. Lemma

```text
Lemma 294.1 (higher coherence is not global represented Qbar geometry).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

A hyperdescent wrapper can declare all eleven represented-carrier slots:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new global `Qbar`
evidence. The represented slots remain the five visible slots above.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but homotopy-coherent projection only declares defect zero. The
semantic projection defect remains 27.

Realizing that coherent projection relation in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

Hyperdescent DD.4 zero cells do not kill the global DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

At refinement chart counts 2,4,8 there are 14 local zero cells. The tested
boundary window still has 16 primitive directions, hence 2^56 possible
primitive-direction assignments across those local cells. Higher coherence
does not select the carrier boundary direction or supply carrier Rosati. The
q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls admit the same hyperdescent wrapper. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently hyperdescent still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_HYPERDESCENT__HIGHER_COHERENCE_NOT_GLOBAL_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_hyperdescent_no_go` verifies eight
gates.

HDS1 checks that product+`rep_NS` visible data has only the five represented
slots.

HDS2 checks that hyperdescent declares all eleven slots but represents no new
global `Qbar` evidence.

HDS3 checks projection: homotopy-coherent projection has declared defect
zero, while the semantic defect remains 27.

HDS4 checks that coherent projection realization changes graph degree `d1`
from 7 to -20 while the count anchor remains 63.

HDS5 recomputes DD.4 with 14 hypercover zero cells:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

HDS6 checks boundary-direction and Rosati nonselection: there are 16
primitive directions, 2^56 hypercover assignments across the tested
refinements, and the on/off-circle signs still differ.

HDS7 checks positive control survival with projection defect 11 and no
represented control death.

HDS8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-294:
  NEWLY CLOSED THIS CYCLE:
    - hyperdescent/homotopy-coherent wrappers for local square-cycle cells;
    - higher projection coherence as global projection formula;
    - hypercover DD.4 zero cells as global boundary killing;
    - higher coherence as DD.4 boundary-direction selection;
    - hyperdescent Rosati/control cells as carrier Rosati/control death.

  POSITIVE INFORMATION RETAINED:
    - the real carrier should satisfy descent/hyperdescent if its geometry
      demands it;
    - higher coherence is admissible only for actual represented carrier
      maps, boundary sequences, pullbacks, and dualities.

  STILL ADMISSIBLE:
    - a construction of Qbar with represented local charts and global
      hyperdescent for its actual correspondence category, projection formula,
      Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - construct global represented carrier geometry first; then prove the
      required descent or hyperdescent theorem.
```

## 5. Kill Conditions

```text
KILL-HDS.1 hyperdescent actualization
  Kill hyperdescent arguments unless the hypercover terms are represented
  pieces of one global Qbar and glue to actual global maps.

KILL-HDS.2 projection by higher coherence
  Higher projection cells do not count unless they prove a global carrier
  push-pull theorem against the intersection form.

KILL-HDS.3 NS retuning by coherence
  Kill coherent projection relations whose realization in NS triples changes
  graph degree, trace, count, or endpoint data.

KILL-HDS.4 DD.4 zero by hypercover cells
  Hypercover DD.4 zero cells do not count. The global class [(1+z)^-1] must
  map to zero in the carrier boundary sequence.

KILL-HDS.5 boundary direction by higher coherence
  Higher coherence does not select the primitive DD.4 direction unless the
  global carrier selects it.

KILL-HDS.6 control death by hyperdescent
  Controls must fail to instantiate the global carrier at formation;
  hyperdescent control-death cells do not count.
```
