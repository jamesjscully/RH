# 305 - CC product square-cycle Rezk completion is not the square carrier

Status: no-go + CC-product-square-cycle-Rezk-completion deletion, 2026-06-22.
One-hundred-sixty-eighth cycle of the doc-137 construction arc. Doc 304
killed the homotopy quotient shortcut. This document tests the next
categorical repair:

```text
replace the compactified zeta square by the Rezk completion, coherent nerve,
or complete Segal presentation of the square-carrier specification, and count
the completed presentation as represented Qbar geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_rezk_completion_no_go`
(RZK1-RZK8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_homotopy_quotient_no_go`,
`prime_int_n1b_cc_product_square_cycle_contractible_choice_space_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 304 rejected turning a quotient class in a specification groupoid into
represented existence. The next repair is completion:

```text
Rezk completion / coherent nerve / complete Segal presentation
= completed square-carrier presentation
= represented compactified zeta square.
```

Genuine complete Segal or Rezk presentations are useful languages for already
constructed carriers. The shortcut is to count completion of a predicate
presentation as construction of the carrier itself.

## 2. Lemma

```text
Lemma 305.1 (Rezk completion is not represented construction).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The Rezk/coherent-nerve package lists all eleven required predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new Qbar evidence.
A Rezk completion, coherent nerve, complete Segal object, or equivalence
completion is not an actual zeta square map, proper pullback, boundary
localization, Rosati evaluation, or control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the Segal projection filler only declares defect zero. The
semantic projection defect remains 27.

Realizing a Segal filler in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The Rezk zero filler does not kill the actual DD.4 class. In truncations
L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Completion adds fillers but does not select carrier data. The tested
simplicial presentation window has 16 primitive directions, two Rosati
branches, three Segal filler choices, and two completeness witnesses, hence
192 raw presentations collapsed to one declared complete object with fiber
size 192. The q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on
the planted off-circle q-similitude.

Positive controls have the same Rezk completion. The q=3 control has semantic
projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the Rezk/coherent-nerve wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_REZK_COMPLETION__COMPLETE_PRESENTATION_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_rezk_completion_no_go` verifies eight
gates.

RZK1 checks that product+`rep_NS` visible data has only the five represented
slots.

RZK2 checks that the Rezk/coherent-nerve package lists all eleven slots but
represents no new `Qbar` evidence.

RZK3 checks projection: the Segal projection filler has declared defect zero,
while the semantic defect remains 27.

RZK4 checks that realizing a Segal filler changes graph degree `d1` from 7 to
-20 while the count anchor remains 63.

RZK5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

RZK6 checks filler addition rather than selection: 16 boundary directions,
two Rosati branches, three Segal filler choices, two completeness witnesses,
192 raw simplicial presentations, one declared complete object, fiber size
192, and on/off-circle sign separation remain.

RZK7 checks positive control survival: the q=3 control has the same Rezk
completion, projection defect 11, and no represented control death.

RZK8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-305:
  NEWLY CLOSED THIS CYCLE:
    - Rezk completion as the carrier;
    - coherent nerve as represented Qbar construction;
    - complete Segal presentation as carrier projection formula;
    - Rezk zero filler as DD.4 boundary killing;
    - Segal/completeness fillers as boundary/Rosati/control selection;
    - controls with the same Rezk completion.

  POSITIVE INFORMATION RETAINED:
    - complete Segal/Rezk language may organize an actual constructed carrier;
    - completion is admissible only after represented carrier data exists.

  STILL ADMISSIBLE:
    - presenting an already constructed compactified zeta square by a complete
      Segal or Rezk object, preserving actual maps, pullbacks, projection,
      Rosati, DD.4 boundary, graph composition, and control death.

  STILL OPEN:
    - construct the represented square, not merely a completed presentation of
      a specification.
```

## 5. Kill Conditions

```text
KILL-RZK.1 Rezk completion as carrier
  Kill Rezk-completion arguments unless represented Qbar geometry is already
  constructed.

KILL-RZK.2 coherent nerve as construction
  Taking the nerve of a predicate presentation is not an actual carrier object
  with maps, proper pullbacks, boundary localization, Rosati, or controls.

KILL-RZK.3 Segal projection filler
  A Segal filler for projection is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-RZK.4 Rezk DD.4 zero filler
  A completion filler is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-RZK.5 completion fillers as selection
  Adding Segal/completeness fillers does not select carrier-native boundary
  direction, Rosati branch, or formation obstruction.

KILL-RZK.6 controls with the same completion
  If positive controls have the same complete Segal/Rezk presentation,
  formation-level control death has failed.
```
