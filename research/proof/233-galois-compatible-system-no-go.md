# 233 - Galois compatible systems do not construct the square

Status: no-go + Galois/Chebotarev/compatible-system realization boundary,
2026-06-20. Ninety-sixth cycle of the doc-137 construction arc. Doc 232
killed automorphic/trace-formula/Langlands packets as square construction.
This document tests the dual repair: use a compatible `l`-adic/Galois
representation system with Frobenius conjugacy classes, Chebotarev density,
determinant character, local monodromy, and comparison data, then promote
that realization package to the missing global square carrier.

```text
automorphic / trace-formula packet
  -> compatible Galois system / Chebotarev Frobenius classes
  -> global square correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_galois_compatible_system_no_go` (GCS1-GCS7 ALL PASS) --
identical compatible-system profiles do not determine finite-field count
anchors; Frobenius conjugacy data does not construct NS degree slots;
Chebotarev semisimplification does not construct correspondence extension
data; determinant/local-monodromy data does not impose radius split or
Rosati; finite Frobenius windows admit ghost summands; the same formal
compatible-system schema is formable on controls; and no square package over
`Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_automorphic_trace_formula_packet_no_go` (ATF1-ATF7 ALL PASS)
and `prime_int_n1b_frobenius_tannakian_compactness_no_go` (FTC1-FTC6 ALL
PASS).

## 1. Purpose

Doc 232 says automorphic spectral packets are not the square carrier. The
natural dual repair is:

```text
do not use the automorphic packet as the object;
use the compatible Galois representation system;
recover the object from Frobenius conjugacy classes by Chebotarev;
use determinant/local monodromy/comparison data as the square.
```

This is still not construction of `End(S^2/Z)`. Compatible systems can
organize realization data and Frobenius characteristic polynomials after a
geometric or motivic object exists. Chebotarev can identify semisimple
representations from sufficiently many Frobenius classes. But these data do
not by themselves construct the over-`Z` square, `rep_NS`, carrier-native
degree maps, proper correspondence category, fiber-product composition,
Frobenius graph, projection formula, or positive Rosati relation.

This document rejects only the shortcut:

```text
a compatible Galois / l-adic / Chebotarev realization package constructs
the square correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category first constructs the motive or realization and whose compatible
Galois system is then a theorem about that carrier.

## 2. Lemma

```text
Lemma 233.1 (Compatible Galois systems are not square carriers).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy compatible-system profile:

    rank                       = 2,
    unramified Frobenius       = present,
    l-independence             = present,
    Chebotarev                 = present,
    determinant character      = present,
    local monodromy            = present,
    comparison isomorphisms    = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract compatible-system profile does not determine the
finite-field count anchor.

Nor does Frobenius conjugacy data construct the NS degree slots. Keeping the
same compatible-system profile and z-action while changing the formal triple
from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Chebotarev semisimplification is also not correspondence composition. The
identity and a nontrivial unipotent extension have the same semisimplified
trace profile

    2, 2, 2, 2

in powers 1,2,3,4, while the extension class is nonzero. Semisimple
Frobenius traces do not construct the extension/correspondence data needed
for the square.

Determinant and local-monodromy edge data do not force the individual radius
split or Rosati compatibility. With q=9, the moduli

    e^0.4 * 3, e^-0.4 * 3, e^-0.4 * 3, e^0.4 * 3

have pair-products 9 and determinant 81, but they are not all equal to 3.
Separately, the off-circle integral q-similitude control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Finite Frobenius windows remain unsafe. A 5-cycle ghost summand preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal compatible-system schema is formable on arbitrary control
companion data with no actual Galois representation, motivic source, rep_NS,
square carrier, or positive Rosati.

Consequently a compatible Galois system constructs no Galois representation,
motivic source, Chebotarev carrier, rep_NS, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_GALOIS_COMPATIBLE_SYSTEM__REALIZATION_DATA_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_galois_compatible_system_no_go` verifies the seven gates.

GCS1 records profile non-determination. The q=7 and q=5 anchors have the
same abstract compatible-system profile but different count windows.

GCS2 records the NS-degree-slot failure. With the same compatible-system
profile and z-action, changing only the formal degree slot changes
`Delta.Gamma` from `7` to `10`.

GCS3 records Chebotarev semisimplification versus extension/correspondence
data. The identity and a nontrivial unipotent extension have traces
`2,2,2,2` in the first four powers, but the extension norm is `1`.

GCS4 records determinant/local-monodromy edge versus Rosati separation.
Balanced local radius redistribution preserves pair-products and determinant
while breaking the individual even split, and an off-circle q-similitude
still has positive metric defect `5.916`. The missing datum is global
carrier-native Rosati, not another determinant or monodromy identity.

GCS5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

GCS6 records control formability. A control companion with the same formal
compatible-system schema has count window `8,112,1064` and metric defect
`9.950`, with no actual Galois representation, motivic source, `rep_NS`,
square, or Rosati input.

GCS7 records the construction failure: no Galois representation, motivic
source, Chebotarev carrier, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-233:
  NEWLY CLOSED THIS CYCLE:
    - compatible Galois system as global square carrier, Frobenius conjugacy
      data as rep_NS construction, Chebotarev semisimplification as
      correspondence composition, determinant/local-monodromy data as
      degree/Rosati construction, finite Frobenius windows as carrier
      determination, and formal compatible-system schemas as DH/Epstein
      carrier guards (doc 233).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper correspondence
      category constructs the motivic or Galois realization downstream;
    - a Chebotarev or compatible-system theorem downstream of an actual
      square carrier with degree maps, correspondences, projection formula,
      Frobenius graph, and Rosati;
    - a theorem excluding ghost Frobenius summands from the actual carrier;
    - controls killed at carrier formation, not after realization packaging.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the compatible-system shortcut:
Galois/Chebotarev realization data is not construction of the global square
carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-GCS.1 compatible system as square construction
  A proposal supplies l-adic, Galois, or compatible-system data and calls it
  the square. Kill it unless the global over-Z square carrier was already
  constructed carrier-natively.

KILL-GCS.2 Frobenius conjugacy data as rep_NS
  A proposal treats Frobenius characteristic polynomials or conjugacy classes
  as the NS triple. Kill it unless the degree slots, off-diagonal
  intersections, and projection formula are constructed.

KILL-GCS.3 Chebotarev semisimplification as graph law
  A proposal reads the Frobenius graph or correspondence composition from
  semisimple Chebotarev traces. Kill it unless extension data, graph
  composition, and proper correspondences are constructed by the carrier.

KILL-GCS.4 determinant/local monodromy as Rosati
  A proposal reads positive Rosati from determinant, weight, or local
  monodromy data. Kill it unless Frobenius/Rosati compatibility is
  constructed globally.

KILL-GCS.5 finite Frobenius window
  A proposal verifies finitely many Frobenius characteristic polynomials or
  local factors. Kill it unless ghost Frobenius summands are excluded
  carrier-natively.

KILL-GCS.6 control survival
  A proposal's compatible-system schema can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
