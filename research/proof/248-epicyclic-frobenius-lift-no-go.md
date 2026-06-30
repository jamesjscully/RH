# 248 - Epicyclic Frobenius-lift coherence does not construct the square

Status: no-go + epicyclic / Frobenius-lift / power-map coherence carrier
boundary, 2026-06-20. One-hundred-eleventh cycle of the doc-137
construction arc. Doc 247 killed Weil-etale / Lichtenbaum / L-function
special-value data as direct square construction. This document tests the
adjacent categorical repair: use epicyclic or cyclotomic-category power-map
coherence, cyclic-bar refinements, Frobenius lifts, geometric realization,
and THH-epi style realizations as the carrier.

```text
epicyclic category / cyclic bar / N^x power maps / Frobenius lifts
  + coherence / geometric realization / cyclotomic comparison / THH-epi
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_epicyclic_frobenius_lift_no_go` (EPF1-EPF8 ALL PASS) --
epicyclic/Frobenius-lift profiles do not determine finite-field count
anchors; coherent power maps do not construct NS degree slots;
epicyclic shadows lose correspondence endpoint data; coherent Frobenius
lifts do not impose Frobenius/Rosati compatibility; epicyclic realization
declarations are not constructed projection formulas; finite epicyclic
windows admit trace ghosts; the same formal schema is formable on controls;
and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_monoid_frobenius_shadow_no_go`,
`prime_int_n1b_cyclic_graph_algebra_no_go`, and
`prime_int_n1b_algebraic_k_cyclotomic_trace_no_go`.

## 1. Purpose

The project has real positive evidence around Frobenius shadows: monoid
fixed-point growth, cyclic/epicyclic power maps, cyclotomic structures, and
trace-method realizations all carry useful arithmetic. Earlier cycles
already killed monoid Frobenius shadows, cyclic graph algebras, formal NS
wrappers, algebraic K/TC, and Weil-etale special values as direct carriers.
The present repair is different:

```text
do not rely on a single monoid shadow or K/TC realization;
use the full epicyclic/cyclotomic-category coherence of all power maps and
Frobenius lifts as the missing square calculus.
```

This is still not construction of `End(S^2/Z)`. Epicyclic coherence supplies
a formalism for power maps and Frobenius lifts. It does not by itself
construct the zeta-native square over `Z`, `rep_NS`, two degree maps, proper
correspondence category, fiber-product composition, carrier-native
Frobenius graph, projection formula, or positive Rosati.

This document rejects only the shortcut:

```text
epicyclic / Frobenius-lift / power-map coherence constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject epicyclic objects, cyclic-bar refinements, Frobenius
lifts, or cyclotomic comparisons downstream of a future global square whose
degree maps, correspondences, projection formula, Frobenius graph, and
Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 248.1 (Epicyclic Frobenius-lift coherence is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy epicyclic/Frobenius-lift profile:

    epicyclic category = present
    cyclic bar refinement = present
    N^x power maps = present
    commuting Frobenius lifts = present
    geometric realization = present
    coherence relations = present
    cyclotomic comparison = present
    THH-epi realization = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract epicyclic/Frobenius-lift profile does not determine
the finite-field count anchor.

Nor does Frobenius-lift coherence construct the NS degree slots. The toy
power lifts psi_n satisfy

    psi_m psi_n = psi_mn

for the checked degrees 2,3,5, but keeping the same coherent power maps and
z-action while changing the formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

An epicyclic power-map shadow can lose correspondence endpoint data. Two
classes can have the same epicyclic shadow (3,2) while their endpoint
coordinate differs by 4.

Coherent Frobenius lifts do not impose Frobenius/Rosati compatibility. The
off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring an epicyclic bar construction, Frobenius-lift realization, or
cyclotomic comparison does not construct the square projection formula. In
the componentwise realization, the semantic projection defect remains

    27.

Finite epicyclic/Frobenius-lift windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal epicyclic/Frobenius-lift schema is formable on arbitrary
control companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently an epicyclic / Frobenius-lift / power-map coherence package
constructs no epicyclic carrier, cyclic-bar square, Frobenius-lift carrier,
power-map degree carrier, cyclotomic comparison carrier, THH-epi carrier,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_EPICYCLIC_FROBENIUS_LIFT__COHERENCE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_epicyclic_frobenius_lift_no_go` verifies the eight gates.

EPF1 records profile non-determination. The q=7 and q=5 anchors have the
same epicyclic/Frobenius-lift profile but different count windows.

EPF2 records the NS-degree-slot failure. The toy power lifts are coherent
under `psi_m psi_n = psi_mn`, but with the same coherence profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

EPF3 records correspondence-data loss. The epicyclic shadow sees the
power-map degree and cyclic-rank part `(3,2)` but forgets an endpoint
coordinate differing by `4`.

EPF4 records Rosati non-construction. Coherent Frobenius lifts and
epicyclic realization do not force Frobenius to be a q-similitude for the
required carrier pairing; the normalized metric defect is `5.916`.

EPF5 records projection-formula failure. Epicyclic bar data,
Frobenius-lift realization, and cyclotomic comparisons do not construct the
square calculus; the componentwise semantic defect is still `27`.

EPF6 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

EPF7 records control formability. A control companion with the same formal
epicyclic/Frobenius-lift schema has count window `8,112,1064` and metric
defect `9.950`, with no square, `rep_NS`, degree maps, projection formula,
or Rosati input.

EPF8 records the construction failure: no epicyclic carrier, cyclic-bar
square, Frobenius-lift carrier, power-map degree carrier, cyclotomic
comparison carrier, THH-epi carrier, ambient square, `rep_NS`, actual
square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-248:
  NEWLY CLOSED THIS CYCLE:
    - epicyclic category as square carrier, cyclic-bar refinements as
      square construction, N^x power maps as degree maps, Frobenius-lift
      coherence as Frobenius graph, geometric realization as projection
      formula, cyclotomic comparison as Rosati, finite epicyclic windows as
      ghost exclusion, and formal epicyclic schemas as DH/Epstein carrier
      guards (doc 248).

  STILL ADMISSIBLE:
    - epicyclic objects, cyclic-bar refinements, Frobenius lifts, and
      cyclotomic comparisons downstream of an actual global square carrier;
    - a theorem showing the actual carrier's epicyclic or cyclotomic
      realization preserves exact integral correspondence endpoints, degree
      slots, projection formula, and Rosati;
    - controls killed at carrier formation, not after applying epicyclic
      realization or Frobenius-lift coherence.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the epicyclic / Frobenius-lift coherence
shortcut: the coherence formalism is allowed only after the square carrier
and its correspondence calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-EPF.1 epicyclic category as square construction
  A proposal supplies an epicyclic object, cyclic-bar refinement, power-map
  formalism, Frobenius lifts, or THH-epi realization and calls that the
  square. Kill it unless the global over-Z square carrier and proper maps
  were already constructed.

KILL-EPF.2 epicyclic profile as count anchor
  A proposal reads the finite-field count anchor from epicyclic profile,
  power-map coherence, or Frobenius-lift existence. Kill it: the same profile
  can support different count windows.

KILL-EPF.3 power maps as degree maps
  A proposal uses N^x power-map degrees, epicyclic operators, or cyclic-bar
  ranks as the two NS degree maps. Kill it unless those degree maps are
  constructed carrier-natively.

KILL-EPF.4 Frobenius-lift coherence as Rosati
  A proposal uses commuting Frobenius lifts, power-map coherence, or
  cyclotomic comparison as the positive Rosati relation. Kill it unless
  Frobenius/Rosati compatibility is proved for the actual carrier pairing.

KILL-EPF.5 epicyclic shadow as integral correspondence
  A proposal relies on epicyclic, cyclic-bar, power-map, or Frobenius-lift
  shadows after forgetting endpoint, extension, or lattice data. Kill it
  unless the exact integral correspondence class is recovered
  carrier-natively.

KILL-EPF.6 epicyclic realization as projection formula
  A proposal treats epicyclic realization, cyclic-bar functoriality, or
  cyclotomic comparison as the projection formula for End(S^2/Z). Kill it
  unless the formula is proved for the actual proper correspondence calculus.

KILL-EPF.7 finite epicyclic checks as ghost exclusion
  A proposal verifies only a finite epicyclic, cyclic-bar, power-map, or
  Frobenius-lift window. Kill it unless ghost summands are excluded from the
  actual carrier.

KILL-EPF.8 control survival
  A proposal's epicyclic/Frobenius-lift schema is formable on arbitrary
  control companion data. Kill it unless controls die at carrier
  construction.
```
