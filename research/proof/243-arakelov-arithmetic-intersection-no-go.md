# 243 - Arakelov arithmetic intersection theory does not construct the square

Status: no-go + Arakelov / arithmetic intersection carrier boundary,
2026-06-20. One-hundred-sixth cycle of the doc-137 construction arc. Doc
242 killed perfectoid, diamond, and Fargues-Fontaine local period geometry
as direct square construction. This document tests another square-like
repair: use arithmetic Chow groups, Green currents, hermitian line bundles,
height pairings, Deligne pairings, and the arithmetic Hodge index theorem to
supply the square carrier.

```text
Arakelov arithmetic Chow / Green currents / heights / arithmetic Hodge index
  -> arithmetic intersection form and positivity
  -> rep_NS, degree maps, projection formula, and Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_arakelov_arithmetic_intersection_no_go` (AIC1-AIC8 ALL PASS)
-- Arakelov profiles do not determine finite-field count anchors; arithmetic
intersection data does not construct NS degree slots; height/Green-current
shadows lose correspondence endpoint data; Green metric positivity does not
impose Frobenius/Rosati compatibility; arithmetic Hodge/projection
declarations are not a constructed projection formula; finite
Arakelov/intersection windows admit trace ghosts; the same formal schema is
formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_weil_standard_package_no_go` (WSC1-WSC7 ALL PASS),
`prime_int_n1b_bivariant_operational_chow_no_go` (BOC1-BOC8 ALL PASS), and
`prime_int_n1b_condensed_liquid_analytic_carrier_no_go` (CLA1-CLA8 ALL PASS).

## 1. Purpose

Earlier cycles killed Chow/Hilbert cycle moduli, bivariant/operational
Chow, motivic regulators, and analytic enrichment as direct square
construction. The Arakelov repair is tempting because it looks closest to
the desired shape:

```text
build arithmetic Chow groups with Green currents;
use hermitian metrics, height pairings, Deligne pairings, and arithmetic
Hodge index;
read the missing square intersection form and Rosati.
```

This is still not construction of `End(S^2/Z)`. Arakelov intersection
theory applies after an arithmetic surface or higher arithmetic variety,
proper maps, hermitian line bundles, and intersection theory have been
constructed. The target needs a zeta-native square over `Z`, `rep_NS`, two
degree maps, proper correspondence category, fiber-product composition,
Frobenius graph, projection formula, and positive Rosati. Arithmetic Hodge
index and Green-current formalism do not manufacture those inputs.

This document rejects only the shortcut:

```text
Arakelov arithmetic intersection theory constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject Arakelov arithmetic Chow groups, heights, Green currents,
or arithmetic Hodge index downstream of a future global square whose proper
maps, degree maps, correspondences, projection formula, Frobenius graph, and
Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 243.1 (Arakelov intersection theory is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Arakelov profile:

    arithmetic Chow group      = present,
    Green current              = present,
    hermitian line bundle      = present,
    height pairing             = present,
    Deligne pairing            = present,
    arithmetic Hodge index     = present,
    archimedean metric data    = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract Arakelov profile does not determine the finite-field
count anchor.

Nor does arithmetic intersection data construct the NS degree slots. Keeping
the same Arakelov profile and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A height or Green-current shadow can also lose correspondence endpoint data.
Two arithmetic classes can have the same height shadow (1,2) while their
endpoint coordinate differs by 4.

Green metric positivity does not impose the Frobenius/Rosati compatibility
relation. A positive metric can coexist with a normalized metric defect of
5.916.

Declaring the arithmetic Hodge index theorem, Deligne pairing, and
projection formula does not construct the square projection formula. In the
componentwise realization, the semantic projection defect remains

    27.

Finite Arakelov/intersection windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal Arakelov schema is formable on arbitrary control companion
data with no arithmetic surface, arithmetic Chow group, `rep_NS`, degree
maps, or positive Rosati.

Consequently an Arakelov arithmetic-intersection package constructs no
arithmetic surface, arithmetic Chow group, Green current, hermitian ample
line, height pairing, Deligne pairing, arithmetic Hodge index theorem,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_ARAKELOV_ARITHMETIC_INTERSECTION__HEIGHTS_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_arakelov_arithmetic_intersection_no_go` verifies the eight
gates.

AIC1 records profile non-determination. The q=7 and q=5 anchors have the
same Arakelov profile but different count windows.

AIC2 records the NS-degree-slot failure. With the same Arakelov profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

AIC3 records correspondence-data loss. The height/Green-current shadow sees
the degree and metric part `(1,2)` but forgets an endpoint coordinate
differing by `4`.

AIC4 records Rosati non-construction. Green metric positivity does not force
Frobenius to be a q-similitude for the required carrier pairing; the
normalized metric defect is `5.916`.

AIC5 records projection-formula failure. Arithmetic Hodge index, Deligne
pairing, and projection declarations do not construct the square calculus;
the componentwise semantic defect is still `27`.

AIC6 records finite-window trace ghosts. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

AIC7 records control formability. A control companion with the same formal
Arakelov schema has count window `8,112,1064` and metric defect `9.950`,
with no arithmetic surface, arithmetic Chow group, `rep_NS`, degree maps, or
Rosati input.

AIC8 records the construction failure: no arithmetic surface, arithmetic
Chow group, Green current, hermitian ample line, height pairing, Deligne
pairing, arithmetic Hodge index, ambient square, `rep_NS`, actual square,
proper correspondence category, fiber-product composition, carrier-native
degree maps, carrier-native pairing, projection formula, Frobenius graph,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-243:
  NEWLY CLOSED THIS CYCLE:
    - arithmetic Chow as global square carrier, Green currents or metrized
      line bundles as integral correspondence construction, height pairings
      as rep_NS construction, Deligne pairing or arithmetic Hodge index as
      projection/Rosati construction, finite Arakelov windows as ghost
      exclusion, and formal Arakelov schemas as DH/Epstein carrier guards
      (doc 243).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose arithmetic Chow,
      Green-current, height-pairing, Deligne-pairing, and arithmetic Hodge
      structures are constructed only after the square object, proper maps,
      degree maps, correspondence composition, projection formula, Frobenius
      graph, all-prime plus archimedean assembly, and Rosati are built;
    - Arakelov intersection theory downstream of that actual square;
    - a theorem showing height/Green-current shadows preserve the exact
      integral correspondence and degree data of the actual carrier;
    - controls killed at carrier formation, not after applying Arakelov
      intersection formalism.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the Arakelov shortcut: arithmetic
intersection theory is allowed only after the square carrier and its
arithmetic correspondence calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-AIC.1 arithmetic Chow as square construction
  A proposal supplies arithmetic Chow groups, Green currents, hermitian line
  bundles, height pairings, Deligne pairings, or arithmetic Hodge index and
  calls that the square. Kill it unless the global over-Z square carrier and
  proper maps were already constructed.

KILL-AIC.2 Arakelov profile as count anchor
  A proposal reads the zeta count anchor from the existence of arithmetic
  Chow, Green currents, metrics, heights, Deligne pairings, or arithmetic
  Hodge index. Kill it: the same profile can support different count
  windows.

KILL-AIC.3 arithmetic intersection class as degree maps
  A proposal uses an arithmetic intersection class or height as the two NS
  degree maps. Kill it unless those degree maps are constructed
  carrier-natively.

KILL-AIC.4 height/Green shadow as integral correspondence
  A proposal relies on a height or Green-current shadow after forgetting
  endpoint or lattice data. Kill it unless the exact integral correspondence
  class is recovered carrier-natively.

KILL-AIC.5 metric positivity as Rosati
  A proposal uses Green-form or hermitian metric positivity as the positive
  Rosati relation. Kill it unless Frobenius/Rosati compatibility is proved
  for the actual carrier pairing.

KILL-AIC.6 arithmetic Hodge index as projection formula
  A proposal treats Deligne pairing, arithmetic Hodge index, or formal
  arithmetic intersection projection as the projection formula for
  End(S^2/Z). Kill it unless the formula is proved for the actual proper
  correspondence calculus.

KILL-AIC.7 finite Arakelov checks as ghost exclusion
  A proposal verifies only a finite arithmetic intersection or height window.
  Kill it unless ghost summands are excluded from the actual carrier.

KILL-AIC.8 control survival
  A proposal's Arakelov schema is formable on arbitrary control companion
  data. Kill it unless controls die at carrier construction.
```
