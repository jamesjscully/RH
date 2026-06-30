# 300 - CC product square-cycle Tannakian reconstruction is not the square carrier

Status: no-go + CC-product-square-cycle-Tannakian-reconstruction deletion, 2026-06-22.
One-hundred-sixty-third cycle of the doc-137 construction arc. Doc 299 killed
the Artin/Schlessinger/Lurie representability-criterion shortcut. This
document tests the next categorical repair:

```text
reconstruct the compactified zeta square from a tensor category, fiber
functor, coend/Hopf algebra, or monadic reconstruction theorem, and count the
reconstructed object as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_tannakian_reconstruction_no_go`
(TAN1-TAN8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_artin_representability_no_go`,
`prime_int_n1b_cc_product_square_cycle_pro_representable_limit_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 299 rejected treating representability criteria as the carrier. The next
repair is reconstruction:

```text
tensor category + fiber functor + coend/Hopf/monadic reconstruction
= compactified zeta square.
```

A genuine carrier may later have a useful category of sheaves, motives, or
correspondences. The shortcut is to count reconstruction data and a fiber
functor as the represented square geometry itself.

## 2. Lemma

```text
Lemma 300.1 (reconstruction data is not the reconstructed square).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The Tannakian/monadic reconstruction package lists all eleven required
predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Tensor categories, fiber functors, coends, Hopf algebras, and monadic
comparison maps are not actual zeta square maps, pullbacks, boundary
localization, Rosati evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the reconstructed projection relation only declares defect zero.
The semantic projection defect remains 27.

Realizing the reconstruction relation in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The coend/Hopf zero does not kill the actual DD.4 class. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Fiber functors parameterize choices rather than selecting carrier data. The
tested boundary window has 16 primitive directions, two Rosati branches, and
three fiber-functor normalizations, hence 96 reconstruction branches. The
q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls admit the same reconstruction package. The q=3 control has
semantic projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the Tannakian/monadic reconstruction wrapper still misses
represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_TANNAKIAN_RECONSTRUCTION__FIBER_FUNCTOR_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_tannakian_reconstruction_no_go`
verifies eight gates.

TAN1 checks that product+`rep_NS` visible data has only the five represented
slots.

TAN2 checks that the reconstruction package lists all eleven slots but
represents no new `Qbar` evidence.

TAN3 checks projection: the reconstructed relation has declared defect zero,
while the semantic defect remains 27.

TAN4 checks that realizing the reconstruction relation changes graph degree
`d1` from 7 to -20 while the count anchor remains 63.

TAN5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

TAN6 checks parameterization rather than selection: 16 boundary directions,
two Rosati branches, three fiber-functor normalizations, 96 reconstruction
branches, and on/off-circle sign separation remain.

TAN7 checks positive control survival: the q=3 control admits the same
reconstruction package with projection defect 11 and no represented control
death.

TAN8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-300:
  NEWLY CLOSED THIS CYCLE:
    - Tannakian/fiber-functor reconstruction as the carrier;
    - coend/Hopf algebra as compactified zeta square;
    - reconstructed projection relation as carrier projection formula;
    - coend/Hopf zero as carrier boundary killing;
    - fiber-functor choices as boundary/Rosati/control selection.

  POSITIVE INFORMATION RETAINED:
    - a real carrier may later have a useful carrier-native tensor category;
    - reconstruction is admissible only downstream of constructed carrier
      geometry, or when the reconstructed object is proved to be Qbar.

  STILL ADMISSIBLE:
    - a reconstruction theorem whose input category is constructed from the
      actual compactified zeta square and whose output is identified with that
      square carrying actual maps, pullbacks, projection, Rosati, DD.4
      boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not just a tensor category with a
      fiber functor.
```

## 5. Kill Conditions

```text
KILL-TAN.1 reconstruction as carrier
  Kill Tannakian/monadic reconstruction arguments unless the reconstructed
  output is proved to be actual Qbar geometry with maps, boundary, and cycles.

KILL-TAN.2 fiber functor as construction
  A fiber functor does not construct carrier maps, pullbacks, Rosati, or
  boundary localization.

KILL-TAN.3 reconstructed projection relation
  A reconstructed relation is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-TAN.4 coend/Hopf DD.4 zero
  A coend/Hopf zero is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-TAN.5 fiber-functor choices as selection
  Parameterizing boundary directions, Rosati branches, or fiber-functor
  normalizations is not carrier selection.

KILL-TAN.6 controls admitting reconstruction
  If positive controls admit the same reconstruction package, formation-level
  control death has failed.
```
