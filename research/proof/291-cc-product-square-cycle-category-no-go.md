# 291 - CC product square-cycle category closure is not the square carrier

Status: no-go + CC-product-square-cycle-category deletion, 2026-06-22.
One-hundred-fifty-fourth cycle of the doc-137 construction arc. Doc 290
killed grafting finite-field `rep_NS` data onto CC product
boundary/endpoints. This document tests the next categorical repair:

```text
freely close the product+rep_NS visible data under a square-cycle category
with pullbacks, projection cells, Rosati cells, DD.4 boundary cells, and
control-death cells.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_category_no_go` (PSC1-PSC8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_repns_graft_no_go`,
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_positive_rosati_end_envelope_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 290 retained the finite-field `rep_NS` triple as the correct visible
target. The next tempting move is categorical:

```text
product boundary/endpoints + visible rep_NS + free Corr^prop-style closure.
```

This is the right vocabulary only after the carrier exists. The no-go is
that freely adjoining a category and coherence cells does not represent the
actual pullbacks, projection formula, Rosati theorem, DD.4 boundary map, or
formation-level control death.

## 2. Lemma

```text
Lemma 291.1 (free square-cycle categorical closure is syntax, not Qbar).

The CC product+rep_NS visible data currently represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

Freely adjoining a square-cycle category with names

    Qbar, p1,p2, rep_NS, Delta, Gamma_F, Corr^prop,
    pullbacks, composition, projection, localization, DD.4 zero,
    Rosati, primitive sign, and control death

declares all eleven represented-carrier slots, but under the
represented-carrier gate it represents no new slots. The represented slots
remain the five visible slots above.

For the q=7, Tr(F)=1 anchor, the finite-field visible data remains correct:

    Delta.Gamma_n = #C(F_{q^n}) for n=1,2,3,
    Gamma_1 o Gamma_2 = Gamma_3.

But a projection cell only declares projection defect zero. The componentwise
semantic projection defect remains 27, so projection is not proved by carrier
push-pull.

Rosati/sign cells do not replace a carrier Rosati theorem. The semantic
primitive sign is negative on the q=7 Weil anchor:

    -13.500,

while the planted off-circle q-similitude has positive primitive sign:

    +2.431.

A formal sign cell is unrepresented and can mask the off-circle failure.

DD.4 zero cells do not map the actual DD.4 class to zero. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

The product boundary direction is also not selected: the primitive directions
in the tested `[-2,2]^2` window are 16.

The same free square-cycle closure is formable on positive controls. The
q=3 control has semantic projection defect 11 and negative primitive sign
-5.500, while the represented slots are still only the five visible slots
and no control death occurs at formation.

Consequently the free square-cycle category still misses:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_CATEGORY__FREE_CLOSURE_NOT_REPRESENTED_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_category_no_go` verifies eight gates.

PSC1 checks that product+`rep_NS` visible data represents only the five
visible slots.

PSC2 checks that a free square-cycle category declares all eleven slots but
represents no new slots.

PSC3 checks projection: the formal projection cell gives defect zero only by
declaration, while the semantic projection defect remains 27.

PSC4 checks Rosati/sign semantics: the true q=7 sign is negative, an
off-circle q-similitude flips positive, and the sign cell is unrepresented.

PSC5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

PSC6 checks that the free category does not select the DD.4 boundary
direction: there are 16 primitive directions in the tested window.

PSC7 checks control survival: the q=3 positive control admits the same free
categorical closure with projection defect 11 and no represented control
death.

PSC8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-291:
  NEWLY CLOSED THIS CYCLE:
    - free square-cycle categorical closure of product+rep_NS data;
    - projection cells as substitute for carrier push-pull;
    - Rosati/sign cells as substitute for a carrier duality theorem;
    - DD.4 zero cells as substitute for an actual boundary map;
    - categorical control-death cells as substitute for formation failure.

  POSITIVE INFORMATION RETAINED:
    - the categorical route is still the right shape;
    - Corr^prop(Qbar), pullbacks, projection, Rosati, DD.4 boundary, graph
      composition, and control death must be carrier theorems.

  STILL ADMISSIBLE:
    - an actual CC-derived compactified zeta square whose product boundary,
      p1,p2, rep_NS, pullbacks, projection formula, Rosati, DD.4 boundary,
      and control death are represented by the same carrier.

  STILL OPEN:
    - construct the represented correspondence category from Qbar itself.
```

## 5. Kill Conditions

```text
KILL-PSC.1 free square-cycle category
  Kill any proposal that freely adjoins Corr^prop-style category structure
  before representing Qbar and its proper pullbacks.

KILL-PSC.2 projection by cell
  Projection cells do not count unless the carrier proves push-pull against
  the intersection form.

KILL-PSC.3 Rosati by cell
  Rosati/sign cells do not count unless the carrier supplies a duality
  functor, D^2=id, Rosati evaluation, and primitive sign theorem.

KILL-PSC.4 DD.4 zero by cell
  A DD.4 zero cell is not a boundary map. Kill unless exact localization
  maps [(1+z)^-1] to zero in the carrier boundary sequence.

KILL-PSC.5 boundary direction by category
  Category closure does not select the primitive DD.4 direction. Kill unless
  the carrier selects it.

KILL-PSC.6 control-death cell
  Control-death cells do not count. Controls must fail to instantiate the
  carrier at formation.
```
