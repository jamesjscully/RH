# 249 - Witt/Lambda/delta-ring absolute geometry does not construct the square

Status: no-go + Witt / Lambda-ring / delta-ring absolute-geometry carrier
boundary, 2026-06-20. One-hundred-twelfth cycle of the doc-137 construction
arc. Doc 248 killed epicyclic / Frobenius-lift coherence as direct square
construction. This document tests the adjacent absolute-geometry repair:
use Borger-style Lambda-rings, big-Witt vectors, Witt ghost coordinates,
all-prime Frobenius lifts, p-typical delta structures, arithmetic jet spaces,
Verschiebung/Restriction operations, and absolute-base interpretation as the
carrier.

```text
Lambda-ring / big-Witt / ghost coordinates / all-prime Frobenius lifts
  + p-typical delta structures / arithmetic jets / V,R,F operations
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_witt_lambda_delta_ring_no_go` (WLD1-WLD9 ALL PASS) --
Witt/Lambda/delta profiles do not determine finite-field count anchors;
all-prime Frobenius lifts and Witt ghosts do not construct NS degree slots;
finite p-typical Witt truncations do not pin the global degree character;
Witt ghost shadows lose correspondence endpoint data; Lambda/delta data does
not impose Frobenius/Rosati compatibility; Witt/delta functoriality is not a
constructed projection formula; finite Witt/Lambda/delta windows admit trace
ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_f1_constant_tower_no_go`,
`prime_int_n1b_prismatic_syntomic_package_no_go`, and
`prime_int_n1b_epicyclic_frobenius_lift_no_go`.

## 1. Purpose

Earlier cycles killed three nearby shortcuts:

```text
doc 203: Borger/Witt ghosts as one finite constant field q;
doc 230: p-complete prismatic/syntomic comparison as the global square;
doc 248: epicyclic Frobenius-lift coherence as the square calculus.
```

The present repair is stronger than each of those alone:

```text
do not ask Witt ghosts merely to be one finite q;
do not stop at p-complete comparison;
do not stop at epicyclic power-map coherence;
use the all-prime Lambda/delta/Witt absolute-geometry package itself as the
missing square correspondence carrier.
```

This is still not construction of `End(S^2/Z)`. Lambda-rings, Witt vectors,
delta-rings, and arithmetic jets are Frobenius-lift and arithmetic-geometry
machinery. They do not by themselves construct the zeta-native square over
`Z`, `rep_NS`, two degree maps, proper correspondence category,
fiber-product composition, carrier-native Frobenius graph, projection
formula, or positive Rosati.

This document rejects only the shortcut:

```text
Witt / Lambda / delta-ring absolute geometry constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject Lambda-rings, Witt vectors, delta structures, arithmetic
jets, or Frobenius-lift packages downstream of a future global square whose
degree maps, correspondences, projection formula, Frobenius graph, and
Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 249.1 (Witt/Lambda/delta data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Witt/Lambda/delta profile:

    Lambda-ring structure = present
    big-Witt functor = present
    ghost map = present
    commuting Frobenius lifts = present
    p-typical delta structures = present
    arithmetic jets = present
    Verschiebung/Restriction operations = present
    absolute-base interpretation = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract Witt/Lambda/delta profile does not determine the
finite-field count anchor.

Nor do all-prime Frobenius lifts or Witt ghosts construct the NS degree
slots. The toy lifts commute for the checked indices 2,3,5,7, but keeping
the same lift data and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Finite p-typical Witt truncation cannot pin the global over-Z degree
character. At p=3 and precision 3^2=9, degrees 7 and 16 agree modulo 9, but

    Delta . Gamma  changes from 7 to 16.

A Witt ghost shadow can lose correspondence endpoint data. Two classes can
have the same ghost shadow (4,2) while their endpoint coordinate differs by
4.

Lambda/delta data does not impose Frobenius/Rosati compatibility. The
off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring big-Witt functoriality, delta-jet spaces, or absolute-base
structure does not construct the square projection formula. In the
componentwise realization, the semantic projection defect remains

    27.

Finite Witt/Lambda/delta windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal Witt/Lambda/delta schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a Witt / Lambda / delta-ring absolute-geometry package
constructs no Lambda-ring carrier, big-Witt carrier, delta-ring carrier,
arithmetic-jet carrier, Witt-ghost degree carrier, all-prime Frobenius
carrier, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_WITT_LAMBDA_DELTA_RING__ABSOLUTE_GEOMETRY_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_witt_lambda_delta_ring_no_go` verifies the nine gates.

WLD1 records profile non-determination. The q=7 and q=5 anchors have the
same Witt/Lambda/delta profile but different count windows.

WLD2 records the NS-degree-slot failure. The toy Frobenius lifts commute,
but with the same lift data and z-action, changing only the formal degree
slot changes `Delta.Gamma` from `7` to `10`.

WLD3 records p-typical ambiguity. Degrees `7` and `16` agree modulo `9` at
`p=3` and precision `3^2`, but the diagonal/graph intersection changes from
`7` to `16`.

WLD4 records correspondence-data loss. The Witt ghost shadow sees the
ghost-degree and Frobenius-index part `(4,2)` but forgets an endpoint
coordinate differing by `4`.

WLD5 records Rosati non-construction. Lambda-ring Frobenius lifts and
delta structures do not force Frobenius to be a q-similitude for the
required carrier pairing; the normalized metric defect is `5.916`.

WLD6 records projection-formula failure. Big-Witt functoriality,
delta-jet spaces, and absolute-base declarations do not construct the
square calculus; the componentwise semantic defect is still `27`.

WLD7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

WLD8 records control formability. A control companion with the same formal
Witt/Lambda/delta schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

WLD9 records the construction failure: no Lambda-ring carrier, big-Witt
carrier, delta-ring carrier, arithmetic-jet carrier, Witt-ghost degree
carrier, all-prime Frobenius carrier, ambient square, `rep_NS`, actual
square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-249:
  NEWLY CLOSED THIS CYCLE:
    - Lambda-ring structure as square carrier, big-Witt vectors as square
      construction, Witt ghost coordinates as degree maps, all-prime
      Frobenius lifts as Frobenius graph, p-typical delta structures as
      global degree character, arithmetic jet spaces as projection formula,
      finite Witt/Lambda/delta windows as ghost exclusion, and formal
      absolute-geometry schemas as DH/Epstein carrier guards (doc 249).

  STILL ADMISSIBLE:
    - Lambda-rings, Witt vectors, delta structures, arithmetic jets, and
      Frobenius-lift packages downstream of an actual global square carrier;
    - a theorem showing the actual carrier's Witt/Lambda/delta realization
      preserves exact integral correspondence endpoints, degree slots,
      projection formula, and Rosati;
    - controls killed at carrier formation, not after applying Witt ghosts,
      delta structures, or Frobenius-lift realizations.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the Witt / Lambda / delta-ring
absolute-geometry shortcut: the package is allowed only after the square
carrier and its correspondence calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-WLD.1 Lambda-ring as square construction
  A proposal supplies a Lambda-ring, big-Witt functor, delta-ring,
  arithmetic jet, or all-prime Frobenius-lift package and calls that the
  square. Kill it unless the global over-Z square carrier and proper maps
  were already constructed.

KILL-WLD.2 Witt/Lambda profile as count anchor
  A proposal reads the finite-field count anchor from a Witt/Lambda/delta
  profile, ghost coordinates, or Frobenius-lift existence. Kill it: the same
  profile can support different count windows.

KILL-WLD.3 Witt ghosts as degree maps
  A proposal uses Witt ghost coordinates, Lambda operations, p-typical
  residues, or delta-jet coordinates as the two NS degree maps. Kill it
  unless those degree maps are constructed carrier-natively.

KILL-WLD.4 finite p-typical truncation as global degree
  A proposal pins the global degree character using finite p-typical Witt or
  delta truncations. Kill it unless all-prime plus archimedean assembly and
  the integral degree character are constructed carrier-natively.

KILL-WLD.5 Lambda/delta data as Rosati
  A proposal uses Frobenius-lift commutation, delta structure, or Witt
  functoriality as the positive Rosati relation. Kill it unless
  Frobenius/Rosati compatibility is proved for the actual carrier pairing.

KILL-WLD.6 Witt shadow as integral correspondence
  A proposal relies on Witt ghost, Lambda-ring, delta-ring, or arithmetic-jet
  shadows after forgetting endpoint, extension, or lattice data. Kill it
  unless the exact integral correspondence class is recovered
  carrier-natively.

KILL-WLD.7 Witt/delta functoriality as projection formula
  A proposal treats big-Witt functoriality, delta-jet functoriality, or
  absolute-base formalism as the projection formula for End(S^2/Z). Kill it
  unless the formula is proved for the actual proper correspondence calculus.

KILL-WLD.8 finite Witt/Lambda checks as ghost exclusion
  A proposal verifies only a finite Witt, Lambda, delta, or arithmetic-jet
  window. Kill it unless ghost summands are excluded from the actual carrier.

KILL-WLD.9 control survival
  A proposal's Witt/Lambda/delta schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
