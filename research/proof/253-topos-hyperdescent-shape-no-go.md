# 253 - Topos/hyperdescent shape data does not construct the square

Status: no-go + topos / site / hyperdescent / shape carrier boundary,
2026-06-20. One-hundred-sixteenth cycle of the doc-137 construction arc.
Docs 229, 241, 242, 251, and 252 killed six-functor trace, condensed/liquid
analytic enrichment, perfectoid/diamond geometry, finite-cover categories,
and span/profunctor bicategories as direct square carriers. This document
tests the object-level topos repair:

```text
site / Grothendieck or infinity topos / sheaves / hypercovers
  + hyperdescent, shape, classifying topos, geometric morphisms
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_topos_hyperdescent_shape_no_go` (THS1-THS9 ALL PASS) --
topos/hyperdescent profiles do not determine finite-field count anchors;
site/topos data does not construct NS degree slots; topos shape shadows lose
correspondence endpoint data; hyperdescent does not select diagonal/graph
triples; topos duality/shape data does not impose Frobenius/Rosati
compatibility; geometric-morphism projection declarations are not a
constructed projection formula; finite topos/hypercover windows admit trace
ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_six_functor_trace_no_go`,
`prime_int_n1b_condensed_liquid_analytic_carrier_no_go`, and
`prime_int_n1b_span_profunctor_bicategory_no_go`.

## 1. Purpose

A site, Grothendieck topos, infinity topos, hypercover descent package, or
shape functor can encode object-level geometry rather than only an algebraic
presentation. That makes it a tempting repair after span/profunctor and
cover-category shortcuts have been closed.

The R1 target is still stricter. `End(S^2/Z)` requires a compactified zeta
square and `rep_NS`: two carrier-native degree maps, an indecomposable
diagonal, proper correspondence composition by fiber product, a
Frobenius/Hecke graph, the projection formula, and positive Rosati pairing.
Topos or shape data can organize sheaves and descent after a site or object
exists, but it does not by itself construct the arithmetic square or its
degree character.

This document rejects only the shortcut:

```text
the topos / site / hyperdescent / shape package constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject topoi, sites, sheaves, hypercovers, hyperdescent, shape,
classifying topoi, or geometric morphisms downstream of a future global
square whose degree maps, correspondences, projection formula, Frobenius
graph, and Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 253.1 (Topos/hyperdescent data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy topos/hyperdescent profile:

    site = present
    Grothendieck/infinity topos = present
    sheaves = present
    hypercovers = present
    hyperdescent = present
    shape = present
    classifying topos = present
    geometric morphisms = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract topos/hyperdescent profile does not determine the
finite-field count anchor.

Nor does site, topos, or hypercover data construct the NS degree slots.
Keeping the same hyperdescent data and z-action while changing the formal
triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A topos shape shadow can lose correspondence endpoint data. Two classes can
have the same shape shadow (2,4) while their endpoint coordinate differs by
4.

Hyperdescent and gluing do not select the diagonal and Frobenius graph
triples. Keeping the same descent profile while changing the formal endpoint
from (1,Id,1) to (4,Id,1) changes the tested endpoint intersection by 3.

Internal topos duality, cohesive shape data, or object-level shape does not
impose Frobenius/Rosati compatibility. The off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring geometric morphisms, base change, and projection formulas does not
construct the square projection formula. In the componentwise realization,
the semantic projection defect remains

    27.

Finite topos/hypercover windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal topos/hyperdescent schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a topos / site / hyperdescent / shape package constructs no
site carrier, topos carrier, sheaf-topos carrier, hyperdescent carrier,
shape carrier, classifying-topos carrier, geometric-morphism carrier,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_TOPOS_HYPERDESCENT_SHAPE__SITE_SHAPE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_topos_hyperdescent_shape_no_go` verifies the nine gates.

THS1 records profile non-determination. The q=7 and q=5 anchors have the
same topos/hyperdescent profile but different count windows.

THS2 records the NS-degree-slot failure. Hyperdescent and z-action are kept
fixed, but changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

THS3 records correspondence-data loss. The topos shape shadow sees homotopy
dimension and cover rank `(2,4)` but forgets an endpoint coordinate
differing by `4`.

THS4 records descent versus square correspondence selection. The descent
profile is unchanged, but changing the formal endpoint changes a tested
endpoint intersection by `3`.

THS5 records Rosati non-construction. Internal duality or shape data does
not force Frobenius to be a q-similitude for the required carrier pairing;
the normalized metric defect is `5.916`.

THS6 records projection-formula failure. Geometric-morphism, base-change,
and projection declarations do not construct the square calculus; the
componentwise semantic defect is still `27`.

THS7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

THS8 records control formability. A control companion with the same formal
topos/hyperdescent schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

THS9 records the construction failure: no site carrier, topos carrier,
sheaf-topos carrier, hyperdescent carrier, shape carrier,
classifying-topos carrier, geometric-morphism carrier, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-253:
  NEWLY CLOSED THIS CYCLE:
    - site or topos as square carrier, sheaf topos as zeta correspondence
      category, shape as endpoint/degree data, hyperdescent as diagonal and
      Frobenius graph selection, internal topos duality as Rosati,
      geometric-morphism/base-change as the square projection formula,
      finite hypercover windows as ghost exclusion, and formal
      topos/hyperdescent schemas as DH/Epstein carrier guards (doc 253).

  STILL ADMISSIBLE:
    - topos, site, sheaf, hyperdescent, or shape language downstream of an
      actual global square carrier;
    - a theorem showing the actual carrier's topos/sheaf realization
      preserves exact integral correspondence endpoints, degree slots,
      projection formula, and Rosati;
    - controls killed at carrier formation, not after applying a site,
      topos, hypercover, shape, or geometric-morphism package.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is not lack of a sheaf-theoretic home for the eventual
object. The obstruction is that the zeta square and its arithmetic
correspondence data have not been constructed. A topos can host the square
only after the carrier supplies the objects, proper maps, degree maps,
graph, projection formula, and Rosati.

## 5. Kill Conditions Added To The Ledger

```text
KILL-THS.1: Do not use a site, Grothendieck topos, or infinity topos itself
            as the End(S^2/Z) square construction.
KILL-THS.2: Do not use sheaves or a classifying topos as carrier-native
            correspondences unless the zeta square objects and maps already
            exist.
KILL-THS.3: Do not use shape or homotopy type as carrier-native degree maps
            or endpoint data.
KILL-THS.4: Do not use hyperdescent or gluing as selection of the diagonal
            and Frobenius graph triples.
KILL-THS.5: Do not use internal topos duality, cohesive shape, or localic
            duality as Rosati positivity.
KILL-THS.6: Do not use geometric morphism, base-change, or formal projection
            declarations as the square projection formula unless the square
            carrier has already supplied the relevant correspondences.
KILL-THS.7: Do not treat finite hypercover or topos-shape windows as ghost
            exclusion.
KILL-THS.8: Do not let control objects survive by merely carrying a formal
            topos/hyperdescent schema.
```

The next admissible move remains constructive: build the actual square
carrier first, then choose the site/topos language in which its sheaves and
descent are expressed.
