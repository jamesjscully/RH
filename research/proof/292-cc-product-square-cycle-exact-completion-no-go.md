# 292 - CC product square-cycle exact completion is not the square carrier

Status: no-go + CC-product-square-cycle-exact-completion deletion,
2026-06-22. One-hundred-fifty-fifth cycle of the doc-137 construction arc.
Doc 291 killed freely adjoining a square-cycle category around the
product+`rep_NS` visible data. This document tests the next categorical
repair:

```text
pass to an exact/regular completion and count completion-internal pullbacks,
localizations, Rosati cells, and control-death cells as actual.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_exact_completion_no_go` (SEC1-SEC8
ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_category_no_go`,
`prime_int_n1b_cc_product_repns_graft_no_go`,
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 291 rejected free category structure as represented evidence. The next
shortcut is subtler:

```text
free square-cycle syntax -> exact/regular completion -> internal pullbacks
and exact localization are now "actual" in the completion.
```

This is still not carrier geometry. The represented-carrier gate asks for
object/map/cycle/pullback/boundary evidence from `Qbar`, not for objects that
exist only because a completion formally added them.

## 2. Lemma

```text
Lemma 292.1 (exact completion of syntax is not represented Qbar geometry).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The exact-completion wrapper internally supplies all eleven named slots:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But the represented-carrier gate still sees only the five visible slots
above. Completion-internal pullbacks, projection relations, localization
objects, Rosati cells, and control-death cells are not actual `Qbar`
evidence.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the completion projection relation only declares defect zero.
The semantic projection defect remains 27.

Forcing that relation back into the NS triple semantics repeats the doc 284
retuning damage:

    graph degree d1 changes from 7 to -20,

while the genuine second point count remains 63.

Completion exact localization does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Completion does not supply the carrier Rosati theorem or the DD.4 boundary
direction. The q=7 primitive sign is -13.500 on the Weil anchor and +2.431
on the planted off-circle q-similitude; the tested boundary window still has
16 primitive directions.

The same exact-completion wrapper is formable on positive controls. The q=3
control has semantic projection defect 11, negative primitive sign -5.500,
the same five represented slots, and no formation-level control death.

Consequently exact completion still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_EXACT_COMPLETION__COMPLETION_INTERNAL_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_exact_completion_no_go` verifies
eight gates.

SEC1 checks that product+`rep_NS` visible data has only the five represented
slots.

SEC2 checks that exact completion internalizes all eleven slots but
represents no new `Qbar` evidence.

SEC3 checks projection: completion relation gives defect zero internally,
while the semantic defect remains 27.

SEC4 checks that forcing the relation into NS triples changes graph degree
`d1` from 7 to -20 while the count anchor remains 63.

SEC5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

SEC6 checks Rosati and boundary-direction semantics: on/off-circle signs
still differ and 16 primitive directions remain.

SEC7 checks positive control survival with projection defect 11 and no
represented control death.

SEC8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-292:
  NEWLY CLOSED THIS CYCLE:
    - exact/regular completion of the free square-cycle wrapper;
    - completion-internal pullbacks as represented proper pullbacks;
    - completion projection relations as the carrier projection formula;
    - completion localization as DD.4 boundary killing;
    - completion Rosati/control cells as carrier Rosati/control death.

  POSITIVE INFORMATION RETAINED:
    - exactness and pullbacks are still required in the actual carrier
      correspondence category;
    - the completion operation is admissible only after its objects and maps
      are represented by Qbar geometry.

  STILL ADMISSIBLE:
    - a construction of Qbar whose actual proper correspondence category has
      exact localization, pullbacks, projection formula, Rosati, DD.4
      boundary, graph composition, and control death as theorems.

  STILL OPEN:
    - construct those exact and proper structures from the carrier, not from
      completion of syntax.
```

## 5. Kill Conditions

```text
KILL-SEC.1 completion-internal actualization
  Kill exact/regular completion arguments unless the completed objects are
  represented by actual Qbar maps, cycles, pullbacks, and boundary maps.

KILL-SEC.2 projection by completion relation
  A completion relation is not the projection formula. Kill unless semantic
  push-pull against the carrier intersection form is proved.

KILL-SEC.3 NS retuning by relation
  Kill any relation whose realization in NS triples changes graph degree,
  trace, count, or endpoint data.

KILL-SEC.4 localization by completion
  Completion exactness is not DD.4 killing. Kill unless the actual class
  [(1+z)^-1] maps to zero through carrier localization.

KILL-SEC.5 Rosati by completion
  Completion Rosati cells do not count unless the carrier supplies the
  duality/evaluation theorem and primitive sign.

KILL-SEC.6 control death by completion
  Controls must fail to instantiate the carrier at formation; completion
  control-death objects do not count.
```
