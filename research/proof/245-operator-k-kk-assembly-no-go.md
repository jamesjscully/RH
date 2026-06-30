# 245 - Operator K-theory / KK assembly does not construct the square

Status: no-go + operator K-theory / crossed-product / KK assembly carrier
boundary, 2026-06-20. One-hundred-eighth cycle of the doc-137 construction
arc. Doc 244 killed the Bost-Connes / adele-class / spectral-triple package
as direct square construction. This document tests the adjacent
operator-algebraic repair: use groupoid or crossed-product C*-algebras,
Baum-Connes style assembly, K-theory, index pairings, and the Kasparov `KK`
product as the carrier.

```text
groupoid C*-algebra / crossed product / assembly
  + K0,K1 / index pairing / Kasparov product
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_operator_k_kk_assembly_no_go` (OKK1-OKK8 ALL PASS) --
operator K/KK profiles do not determine finite-field count anchors;
K-theory assembly data does not construct NS degree slots; K0/index shadows
lose correspondence endpoint data; C*-positivity and positive index pairings
do not impose Frobenius/Rosati compatibility; KK-product declarations are
not constructed projection formulas; finite K/KK windows admit trace ghosts;
the same formal schema is formable on controls; and no square package over
`Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_perfect_morita_envelope_no_go`,
`prime_int_n1b_nc_hodge_realization_no_go`, and
`prime_int_n1b_bost_connes_adele_class_spectral_no_go`.

## 1. Purpose

Doc 225 already killed perfect-module/dg-Morita envelopes and
noncommutative motives of relation data. Doc 244 killed the
Bost-Connes/KMS/spectral-triple package as the carrier. The present repair
is different and narrower:

```text
build an operator-algebraic groupoid or crossed-product C*-algebra;
apply a Baum-Connes style assembly map;
use K-theory, index pairings, and the Kasparov product as the
correspondence calculus.
```

This is still not construction of `End(S^2/Z)`. Operator K-theory and `KK`
are functorial and robust after the analytic or groupoid carrier exists.
They do not by themselves construct the zeta-native square over `Z`,
`rep_NS`, two degree maps, proper correspondence category, fiber-product
composition, carrier-native Frobenius graph, projection formula, or positive
Rosati.

This document rejects only the shortcut:

```text
operator K-theory / Baum-Connes assembly / Kasparov product constructs the
square correspondence carrier required by End(S^2/Z).
```

It does not reject operator K-theory, assembly, crossed products, groupoid
C*-algebras, or `KK` products downstream of a future global square whose
degree maps, correspondences, projection formula, Frobenius graph, and Rosati
are already carrier-native.

## 2. Lemma

```text
Lemma 245.1 (Operator K/KK assembly is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy operator K-theory profile:

    groupoid C*-algebra        = present
    crossed product            = present
    Baum-Connes assembly       = present
    K0,K1                      = present
    Kasparov product           = present
    Morita invariance          = present
    index pairing              = present
    positive C*-state          = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract operator K/KK profile does not determine the
finite-field count anchor.

Nor does K-theory assembly data construct the NS degree slots. Keeping the
same profile and z-action while changing the formal triple from (7,F,1) to
(10,F,1) changes

    Delta . Gamma  from 7 to 10.

A K0 or index shadow can lose correspondence endpoint data. Two K-classes
can have the same rank/index shadow (1,2) while their endpoint coordinate
differs by 4.

C*-positivity and positive index pairings do not impose Frobenius/Rosati
compatibility. The off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring Baum-Connes assembly, a Kasparov product, or an index pairing does
not construct the square projection formula. In the componentwise
realization, the semantic projection defect remains

    27.

Finite K/KK windows remain unsafe: a 5-cycle trace ghost preserves traces in
powers 1,2,3,4 and changes count 5 by 5.

The same formal operator K/KK schema is formable on arbitrary control
companion data with no groupoid square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently an operator K-theory / Baum-Connes / KK package constructs no
groupoid C*-carrier, crossed-product carrier, assembly carrier, K-theory
carrier, KK-product carrier, index-pairing carrier, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, DH/Epstein death, DD.4 weight>=1
datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_OPERATOR_K_KK_ASSEMBLY__K_THEORY_SHADOW_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_operator_k_kk_assembly_no_go` verifies the eight gates.

OKK1 records profile non-determination. The q=7 and q=5 anchors have the
same operator K/KK profile but different count windows.

OKK2 records the NS-degree-slot failure. With the same K/KK profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

OKK3 records correspondence-data loss. The K0/index shadow sees the
rank/index part `(1,2)` but forgets an endpoint coordinate differing by `4`.

OKK4 records Rosati non-construction. C*-positivity and a positive index
pairing do not force Frobenius to be a q-similitude for the required carrier
pairing; the normalized metric defect is `5.916`.

OKK5 records projection-formula failure. Baum-Connes assembly,
KK-product, and index-pairing declarations do not construct the square
calculus; the componentwise semantic defect is still `27`.

OKK6 records finite-window trace ghosts. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

OKK7 records control formability. A control companion with the same formal
operator K/KK schema has count window `8,112,1064` and metric defect
`9.950`, with no groupoid square carrier, `rep_NS`, degree maps, projection
formula, or Rosati input.

OKK8 records the construction failure: no groupoid C*-carrier,
crossed-product carrier, Baum-Connes assembly carrier, K-theory carrier,
KK-product carrier, index-pairing carrier, ambient square, `rep_NS`, actual
square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-245:
  NEWLY CLOSED THIS CYCLE:
    - groupoid C*-algebra as square carrier, crossed product as proper
      correspondence category, Baum-Connes assembly as count-anchor
      construction, K0/K1 or index pairing as degree maps, Kasparov product
      as projection formula, C*-positivity as Rosati, finite K/KK windows as
      ghost exclusion, and formal operator K/KK schemas as DH/Epstein carrier
      guards (doc 245).

  STILL ADMISSIBLE:
    - operator K-theory, assembly, crossed products, and KK products
      downstream of an actual global square carrier;
    - a theorem showing the actual carrier's operator K-theory realization
      preserves exact integral correspondence endpoints, degree slots,
      projection formula, and Rosati;
    - controls killed at carrier formation, not after applying K-theory or
      assembly.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the operator K-theory shortcut:
K-theory, index pairings, Baum-Connes style assembly, and the Kasparov
product are allowed only after the square carrier and its correspondence
calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-OKK.1 groupoid C*-algebra as square construction
  A proposal supplies a groupoid C*-algebra, crossed product, assembly map,
  K-theory group, or KK-category and calls that the square. Kill it unless
  the global over-Z square carrier and proper maps were already constructed.

KILL-OKK.2 K/KK profile as count anchor
  A proposal reads the finite-field count anchor from operator K-theory,
  assembly, or index-pairing profile data. Kill it: the same profile can
  support different count windows.

KILL-OKK.3 K0/index class as degree maps
  A proposal uses K0 classes, Fredholm indices, or assembly images as the
  two NS degree maps. Kill it unless those degree maps are constructed
  carrier-natively.

KILL-OKK.4 C*-positivity as Rosati
  A proposal uses C*-positivity, positivity of an index pairing, or
  positivity of a state as the positive Rosati relation. Kill it unless
  Frobenius/Rosati compatibility is proved for the actual carrier pairing.

KILL-OKK.5 K-theory shadow as integral correspondence
  A proposal relies on K0/K1, index, or KK shadows after forgetting endpoint,
  extension, or lattice data. Kill it unless the exact integral
  correspondence class is recovered carrier-natively.

KILL-OKK.6 KK product as projection formula
  A proposal treats the Kasparov product, naturality of assembly, or an index
  pairing as the projection formula for End(S^2/Z). Kill it unless the
  formula is proved for the actual proper correspondence calculus.

KILL-OKK.7 finite K/KK checks as ghost exclusion
  A proposal verifies only a finite K-theory, index, or trace window. Kill it
  unless ghost summands are excluded from the actual carrier.

KILL-OKK.8 control survival
  A proposal's operator K/KK schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
