# 242 - Perfectoid diamonds and the Fargues-Fontaine curve do not construct the square

Status: no-go + perfectoid / diamond / Fargues-Fontaine carrier boundary,
2026-06-20. One-hundred-fifth cycle of the doc-137 construction arc. Doc
241 killed condensed, liquid, and solid analytic enrichment as direct square
construction. This document tests the next p-adic geometric repair: use
perfectoid covers, untilts, `A_inf` period rings, diamonds or v-stacks, and
the Fargues-Fontaine curve/vector-bundle category to supply the square
carrier.

```text
perfectoid covers / untilts / A_inf / diamonds / Fargues-Fontaine curve
  -> period geometry and vector bundles
  -> rep_NS, global degree maps, projection formula, and positivity
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_perfectoid_diamond_ff_curve_no_go` (FDC1-FDC9 ALL PASS) --
perfectoid/diamond profiles do not determine finite-field count anchors;
perfectoid/diamond data does not construct NS degree slots; untilt or local
period shadows lose global correspondence data; local p-adic period data
does not assemble the global degree character; Fargues-Fontaine
slope/positivity data does not impose Frobenius/Rosati compatibility;
Fargues-Fontaine tensor/projection declarations are not a constructed
projection formula; finite perfectoid/diamond windows admit trace ghosts;
the same formal schema is formable on controls; and no square package over
`Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_prismatic_syntomic_package_no_go` (PSP1-PSP7 ALL PASS),
`prime_int_n1b_condensed_liquid_analytic_carrier_no_go` (CLA1-CLA8 ALL PASS),
and `prime_int_n1b_adelic_restricted_product_assembly_no_go` (ARP1-ARP7
ALL PASS).

## 1. Purpose

Doc 230 already killed prismatic/syntomic comparison packages as direct
global-square construction, and doc 241 killed analytic enrichment. The
next repair is sharper:

```text
construct a perfectoid/diamond/Fargues-Fontaine carrier;
use untilts, period rings, vector bundles, and local Frobenius;
read the global square, degree character, projection formula, and Rosati.
```

This is still not construction of `End(S^2/Z)`. Perfectoid and
Fargues-Fontaine geometry is powerful local p-adic period geometry. The
target needs a global over-`Z` square with all-prime plus archimedean
assembly, proper correspondences, two degree maps, fiber-product
composition, Frobenius graph, projection formula, and positive Rosati. A
local p-adic period carrier or vector-bundle category does not manufacture
that global arithmetic square.

This document rejects only the shortcut:

```text
perfectoid/diamond/Fargues-Fontaine geometry constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject perfectoid covers, diamonds, v-stacks, period rings, or
Fargues-Fontaine vector bundles downstream of a future global square whose
local p-adic realization is already known to preserve the carrier-native
degree maps, correspondences, projection formula, Frobenius graph, and
Rosati.

## 2. Lemma

```text
Lemma 242.1 (Perfectoid/Fargues-Fontaine geometry is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy perfectoid/diamond profile:

    perfectoid cover          = present,
    untilt                    = present,
    A_inf / period ring       = present,
    diamond or v-stack        = present,
    Fargues-Fontaine curve    = present,
    vector-bundle category    = present,
    local Frobenius           = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract perfectoid/diamond profile does not determine the
finite-field count anchor.

Nor does perfectoid/diamond data construct the NS degree slots. Keeping the
same local period profile and z-action while changing the formal triple
from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

An untilt or local-period shadow can also lose global correspondence data.
Two global classes can have the same local shadow (2,1) while their
all-place assembly coordinate differs by 3.

A single local p-adic period component does not assemble the global degree
character. Two all-place vectors can have the same p-adic component 7 while
their all-place gap is 2.236.

Fargues-Fontaine semistability, slopes, or positivity do not impose the
Frobenius/Rosati compatibility relation. A positive metric can coexist with
a normalized metric defect of 5.916.

Declaring vector-bundle tensor products, diamond descent, and projection on
the Fargues-Fontaine side does not construct the square projection formula.
In the componentwise realization, the semantic projection defect remains

    27.

Finite perfectoid/diamond windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal perfectoid/diamond schema is formable on arbitrary control
companion data with no perfectoid zeta square, Fargues-Fontaine curve
carrier, all-prime assembly, `rep_NS`, or positive Rosati.

Consequently a perfectoid / diamond / Fargues-Fontaine package constructs
no perfectoid cover, untilt, `A_inf` period ring, diamond or v-stack,
Fargues-Fontaine curve, vector-bundle category, all-prime plus archimedean
assembly, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_PERFECTOID_DIAMOND_FF_CURVE__LOCAL_PERIOD_GEOMETRY_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_perfectoid_diamond_ff_curve_no_go` verifies the nine gates.

FDC1 records profile non-determination. The q=7 and q=5 anchors have the
same perfectoid/diamond profile but different count windows.

FDC2 records the NS-degree-slot failure. With the same local period profile
and z-action, changing only the formal degree slot changes `Delta.Gamma`
from `7` to `10`.

FDC3 records global-data loss. The local period shadow sees the local
rank/slope pair `(2,1)` but forgets a global assembly coordinate differing
by `3`.

FDC4 records local-to-global failure. A single p-adic component cannot
assemble all primes plus the archimedean component; the tested all-place
gap is `2.236`.

FDC5 records Rosati non-construction. Fargues-Fontaine slope or positivity
data does not force Frobenius to be a q-similitude for the required pairing;
the normalized metric defect is `5.916`.

FDC6 records projection-formula failure. Vector-bundle tensor, diamond
descent, and projection declarations do not construct the square calculus;
the componentwise semantic defect is still `27`.

FDC7 records finite-window trace ghosts. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

FDC8 records control formability. A control companion with the same formal
perfectoid/diamond schema has count window `8,112,1064` and metric defect
`9.950`, with no perfectoid zeta square, Fargues-Fontaine curve carrier,
all-prime assembly, `rep_NS`, or Rosati input.

FDC9 records the construction failure: no perfectoid cover, untilt, `A_inf`
period ring, diamond or v-stack, Fargues-Fontaine curve, vector-bundle
category, all-prime plus archimedean assembly, ambient square, `rep_NS`,
actual square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-242:
  NEWLY CLOSED THIS CYCLE:
    - perfectoid covers as global square carrier, untilts or period rings as
      global correspondence construction, diamonds/v-stacks as rep_NS
      construction, the Fargues-Fontaine curve or its vector bundles as
      degree-map/projection construction, finite perfectoid windows as ghost
      exclusion, and formal perfectoid/diamond schemas as DH/Epstein carrier
      guards (doc 242).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose local p-adic realization
      lands in perfectoid/diamond/Fargues-Fontaine geometry after the square
      object, proper maps, degree maps, correspondence composition,
      projection formula, Frobenius graph, all-prime plus archimedean
      assembly, and Rosati are constructed;
    - perfectoid covers, diamonds, period rings, and FF vector bundles
      downstream of that actual square;
    - a theorem showing local period shadows preserve the exact integral
      global correspondence and degree data of the actual carrier;
    - controls killed at carrier formation, not after passing to local
      p-adic period geometry.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the perfectoid/Fargues-Fontaine shortcut:
local p-adic period geometry is allowed only after the global square carrier
and its arithmetic correspondence calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FDC.1 perfectoid geometry as square construction
  A proposal supplies perfectoid covers, untilts, period rings, diamonds,
  v-stacks, or a Fargues-Fontaine curve and calls that the square. Kill it
  unless the global over-Z square carrier and proper maps were already
  constructed.

KILL-FDC.2 local period profile as count anchor
  A proposal reads the zeta count anchor from a perfectoid cover, untilt,
  A_inf period ring, diamond, FF curve, vector-bundle category, or local
  Frobenius profile. Kill it: the same profile can support different count
  windows.

KILL-FDC.3 local p-adic object as degree maps
  A proposal uses a local period object or FF vector bundle as the two NS
  degree maps. Kill it unless those degree maps are constructed
  carrier-natively.

KILL-FDC.4 untilt/local shadow as global correspondence
  A proposal relies on an untilt or local period shadow after forgetting
  global all-prime or archimedean data. Kill it unless the exact integral
  global correspondence class is recovered carrier-natively.

KILL-FDC.5 local p-adic data as all-prime assembly
  A proposal promotes one p-adic period component to the over-Z degree
  character. Kill it unless all primes and the archimedean component are
  assembled in the actual carrier.

KILL-FDC.6 FF slope positivity as Rosati
  A proposal uses FF semistability, slopes, or vector-bundle positivity as
  the positive Rosati relation. Kill it unless Frobenius/Rosati compatibility
  is proved for the actual carrier pairing.

KILL-FDC.7 FF tensor/descent as projection formula
  A proposal treats vector-bundle tensor products, diamond descent, or local
  projection as the projection formula for End(S^2/Z). Kill it unless the
  formula is proved for the actual proper correspondence calculus.

KILL-FDC.8 finite perfectoid checks as ghost exclusion
  A proposal verifies only a finite perfectoid, diamond, or local-period
  trace window. Kill it unless ghost summands are excluded from the actual
  carrier.

KILL-FDC.9 control survival
  A proposal's perfectoid/diamond schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
