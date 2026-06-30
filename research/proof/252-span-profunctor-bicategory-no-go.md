# 252 - Span/profunctor bicategories do not construct the square

Status: no-go + span / profunctor / correspondence-bicategory carrier
boundary, 2026-06-20. One-hundred-fifteenth cycle of the doc-137
construction arc. Docs 219, 222, 229, 237, 238, 250, and 251 killed formal
composition, presented carriers, six-functor trace, derived/operational
intersection theory, Tambara/Burnside norms, and finite-cover categories as
direct square carriers. This document tests the more primitive categorical
repair:

```text
bicategory of spans / profunctors / distributors / polynomial functors
  + pullback composition, adjoints, Beck-Chevalley, traces
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_span_profunctor_bicategory_no_go` (SPB1-SPB9 ALL PASS) --
span/profunctor profiles do not determine finite-field count anchors;
generic span data does not construct NS degree slots; span/profunctor
shadows lose correspondence endpoint data; pullback composition does not
select the graph degree character; bicategorical adjoints do not impose
Frobenius/Rosati compatibility; Beck-Chevalley/projection declarations are
not a constructed projection formula; finite span/profunctor windows admit
trace ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_formal_correspondence_composition_no_go`,
`prime_int_n1b_presented_correspondence_carrier_no_go`, and
`prime_int_n1b_tambara_mackey_norm_no_go`.

## 1. Purpose

A bicategory of spans, profunctors, distributors, or polynomial functors is
the generic categorical environment in which correspondences can be composed.
It has source/target legs, pullback-like composition, adjoints or duals in
good cases, base-change squares, and trace-like operations.

That is still not the `End(S^2/Z)` construction. R1 asks for a specific
compactified zeta square and its `rep_NS`: two carrier-native degree maps,
an indecomposable diagonal, proper correspondence composition by fiber
product, the Frobenius/Hecke graph, the projection formula, and positive
Rosati pairing. Generic span/profunctor machinery supplies a language for
correspondences after the objects and maps are present; it does not supply
the zeta square or its arithmetic degree character.

This document rejects only the shortcut:

```text
the generic span/profunctor/correspondence bicategory constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject spans, profunctors, distributors, polynomial functors, or
correspondence bicategories downstream of a future global square whose
degree maps, correspondences, projection formula, Frobenius graph, and
Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 252.1 (Generic correspondence bicategories are not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy span/profunctor profile:

    span bicategory = present
    pullback composition = present
    profunctors = present
    distributors = present
    polynomial functors = present
    adjoints = present
    Beck-Chevalley = present
    traces = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract span/profunctor profile does not determine the
finite-field count anchor.

Nor does generic span data construct the NS degree slots. Keeping the same
span laws and z-action while changing the formal triple from (7,F,1) to
(10,F,1) changes

    Delta . Gamma  from 7 to 10.

A span/profunctor shadow can lose correspondence endpoint data. Two classes
can have the same source-target/apex shadow (2,5) while their endpoint
coordinate differs by 4.

Generic pullback composition does not select the Frobenius graph or degree
character. The same z^2 action can be paired with different external degree
slots, giving a tested diagonal/graph degree gap of 4.

Bicategorical adjoints and dualizable objects do not impose
Frobenius/Rosati compatibility. The off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring Beck-Chevalley, base change, and projection formulas does not
construct the square projection formula. In the componentwise realization,
the semantic projection defect remains

    27.

Finite span/profunctor windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal span/profunctor schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a span / profunctor / distributor / polynomial-functor package
constructs no span-bicategory carrier, profunctor carrier, distributor
carrier, polynomial-functor carrier, zeta correspondence-bicategory carrier,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_SPAN_PROFUNCTOR_BICATEGORY__GENERIC_CORRESPONDENCE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_span_profunctor_bicategory_no_go` verifies the nine gates.

SPB1 records profile non-determination. The q=7 and q=5 anchors have the
same span/profunctor profile but different count windows.

SPB2 records the NS-degree-slot failure. Generic pullback-composition laws
and z-action are kept fixed, but changing only the formal degree slot
changes `Delta.Gamma` from `7` to `10`.

SPB3 records correspondence-data loss. The span/profunctor shadow sees
source-target arity and apex rank `(2,5)` but forgets an endpoint coordinate
differing by `4`.

SPB4 records graph-degree non-selection. The same z-power action can be
paired with different external degree slots, producing diagonal/graph degree
gap `4`.

SPB5 records Rosati non-construction. Dualizable objects and bicategorical
adjoints do not force Frobenius to be a q-similitude for the required
carrier pairing; the normalized metric defect is `5.916`.

SPB6 records projection-formula failure. Beck-Chevalley, base change, and
projection declarations do not construct the square calculus; the
componentwise semantic defect is still `27`.

SPB7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

SPB8 records control formability. A control companion with the same formal
span/profunctor schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

SPB9 records the construction failure: no span-bicategory carrier,
profunctor carrier, distributor carrier, polynomial-functor carrier, zeta
correspondence-bicategory carrier, ambient square, `rep_NS`, actual square,
proper correspondence category, fiber-product composition, carrier-native
degree maps, carrier-native pairing, projection formula, Frobenius graph,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-252:
  NEWLY CLOSED THIS CYCLE:
    - span bicategory as square carrier, profunctors/distributors as
      zeta correspondences, polynomial functors as degree maps, generic
      pullback composition as fiber-product correspondence composition,
      bicategorical adjoints as Rosati, Beck-Chevalley/base-change as the
      square projection formula, finite span/profunctor windows as ghost
      exclusion, and formal correspondence-bicategory schemas as DH/Epstein
      carrier guards (doc 252).

  STILL ADMISSIBLE:
    - span/profunctor/correspondence-bicategory language downstream of an
      actual global square carrier;
    - a theorem showing the actual carrier's span/profunctor realization
      preserves exact integral correspondence endpoints, degree slots,
      projection formula, and Rosati;
    - controls killed at carrier formation, not after applying a generic
      correspondence bicategory.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is not lack of categorical syntax for correspondences. The
obstruction is that the zeta square and its arithmetic correspondence data
have not been constructed. A generic correspondence bicategory can host
`End(S^2/Z)` only after the objects, proper maps, degree maps, graph, and
Rosati have been supplied by the carrier.

## 5. Kill Conditions Added To The Ledger

```text
KILL-SPB.1: Do not use the generic bicategory of spans as the End(S^2/Z)
            square construction.
KILL-SPB.2: Do not use profunctors, distributors, or polynomial functors as
            carrier-native correspondences unless the zeta square objects
            and maps already exist.
KILL-SPB.3: Do not use generic source-target/apex data as carrier-native
            degree maps or endpoint data.
KILL-SPB.4: Do not use pullback composition in an ambient bicategory as the
            Frobenius graph degree character.
KILL-SPB.5: Do not use bicategorical adjoints or dualizability as Rosati
            positivity.
KILL-SPB.6: Do not use Beck-Chevalley, base-change, or formal projection
            declarations as the square projection formula unless the square
            carrier has already supplied the relevant correspondences.
KILL-SPB.7: Do not treat finite span/profunctor windows as ghost exclusion.
KILL-SPB.8: Do not let control objects survive by merely carrying a formal
            correspondence-bicategory schema.
```

The next admissible move is unchanged but sharper: build the actual square
carrier first, then express its correspondences in whatever categorical
language is appropriate.
