# 228 - Weil standard packages do not construct the square

Status: no-go + Weil-cohomology/standard-conjectures-package boundary,
2026-06-20. Ninety-first cycle of the doc-137 construction arc. Doc 227
killed NC-Hodge/periodic-cyclic/de Rham realization as square construction.
This document tests the next classical repair: add Kunneth projectors,
Poincare duality, Hard Lefschetz, and Hodge-standard positivity, then promote
that standard package to the square carrier and positive Rosati.

```text
NC-Hodge / realization shadow
  -> Weil cohomology + Kunneth projectors
  -> Poincare duality + Hard Lefschetz + Hodge-standard positivity
  -> square correspondence carrier / positive Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_weil_standard_package_no_go` (WSC1-WSC7 ALL PASS) -- identical
abstract Weil-standard profiles do not determine finite-field count anchors;
Kunneth data does not construct NS degree slots; Hodge-standard positivity
does not impose Frobenius/Rosati compatibility; Hard Lefschetz existence does
not pin the degree character; finite windows admit ghost cohomology; the same
package is formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_nc_hodge_realization_no_go` (NHR1-NHR6 ALL PASS) and
`prime_int_n1b_smooth_proper_cy_mukai_no_go` (CYM1-CYM7 ALL PASS).

## 1. Purpose

Doc 227 says realization data is a shadow, not the square. The natural
classical repair is:

```text
do not use bare realization data;
equip it with the full Weil/standard-conjecture package.
```

That package is still not construction of `End(S^2/Z)`. Kunneth projectors,
Poincare duality, Hard Lefschetz, and Hodge-standard positivity are powerful
once there is an actual smooth/proper square and an actual correspondence
category. But if they are appended to relation data, they do not construct
`rep_NS`, the fiber degree maps, the Frobenius graph, the projection formula,
the carrier-native pairing, or the Rosati compatibility relation.

This document rejects only the shortcut:

```text
an abstract Weil cohomology / standard-conjectures package constructs the
square correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category first constructs the Kunneth projectors, Lefschetz operator,
Poincare pairing, Hodge-standard sign theorem, Frobenius graph, and Rosati
relation carrier-natively.

## 2. Lemma

```text
Lemma 228.1 (Standard conjecture packages are downstream data).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy standard package:

    Betti dimensions        = (1,2,1),
    Kunneth projectors      = present,
    Poincare duality        = present,
    Hard Lefschetz          = present,
    Hodge-standard positive = present.

The packages are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract standard package does not determine the finite-field
count anchor.

Nor does it construct the NS degree slots. Keeping the same Kunneth/H^1 data
and changing the formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Hodge-standard positivity is not Frobenius/Rosati compatibility. For the
off-circle integral q-similitude control

    F = [[0,-2],[1,3]], q=2,

a positive form exists, but

    ||(F/sqrt(q))^T H (F/sqrt(q)) - H|| = 5.916.

Hard Lefschetz existence also does not pin the degree character: scalar maps
H0 -> H2 of size 7 and 10 are both isomorphisms in the toy package, but they
encode different degree data.

Finite standard windows remain unsafe. A hyperbolic pair of 5-cycle ghost
summands preserves traces in powers 1,2,3,4, carries a symplectic Poincare
form, and changes count 5 by 10.

The same abstract package is formable on arbitrary control companion data
with no Euler product, Satake parameters, rep_NS, square carrier, or positive
Rosati.

Consequently a Weil-cohomology/standard-conjectures package constructs no
rep_NS, actual square, proper correspondence category, fiber-product
composition, carrier-native Weil cohomology theorem, carrier-native Kunneth
projectors, carrier-native Lefschetz class, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_WEIL_STANDARD_PACKAGE__STANDARD_AXIOMS_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_weil_standard_package_no_go` verifies the seven gates.

WSC1 records profile non-determination. The q=7 and q=5 anchors have the same
abstract standard package but different count windows.

WSC2 records the NS-degree-slot failure. With the same Kunneth/H^1 data and
z-action, changing only the formal degree slot changes `Delta.Gamma` from `7`
to `10`.

WSC3 records positivity/compatibility separation. A positive form exists on
the off-circle q-similitude control, but the normalized Frobenius metric
compatibility defect is `5.916`. The missing datum is the carrier-native
Rosati relation.

WSC4 records Lefschetz degree ambiguity. Hard Lefschetz says the map
`H0 -> H2` is an isomorphism, but its scalar degree is still unconstructed:
scales `7` and `10` satisfy the same existence predicate.

WSC5 records finite-window ghost survival. A hyperbolic pair of 5-cycle ghost
summands preserves the first four traces, carries a Poincare/symplectic form,
and changes count 5 by `10`.

WSC6 records control formability. A control companion with the same abstract
standard profile has count window `8,112,1064` and metric defect `9.950`, with
no Euler/Satake/`rep_NS`/square/Rosati input.

WSC7 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native Weil
cohomology theorem, carrier-native Kunneth projectors, carrier-native
Lefschetz class, carrier-native degree maps, carrier-native pairing,
projection formula, Frobenius graph, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-228:
  NEWLY CLOSED THIS CYCLE:
    - abstract Weil cohomology as square carrier, Kunneth projectors as
      rep_NS construction, Hard Lefschetz existence as degree-character
      construction, Hodge-standard positivity as Rosati compatibility,
      finite standard-conjecture windows as carrier determination, and
      standard-package axioms as DH/Epstein carrier guards (doc 228).

  STILL ADMISSIBLE:
    - a carrier-native square whose proper correspondence category first
      constructs its Kunneth projectors, Lefschetz class, Poincare pairing,
      degree maps, projection formula, Frobenius graph, and Rosati relation;
    - a standard-conjecture theorem downstream of rep_NS and proper
      correspondences, not a replacement for them;
    - a theorem excluding ghost cohomology from the actual carrier;
    - controls killed at carrier formation, not after imposing standard
      axioms.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the abstract Weil/standard-conjecture
repair: standard axioms are not construction of the square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-WSC.1 abstract Weil cohomology as square construction
  A proposal supplies a Weil cohomology package and calls it the square. Kill
  it unless the square correspondence carrier was already constructed
  carrier-natively.

KILL-WSC.2 Kunneth projectors as rep_NS
  A proposal treats Kunneth projectors or Betti dimensions as the NS triple.
  Kill it unless the degree slots, off-diagonal intersections, and projection
  formula are constructed.

KILL-WSC.3 Hodge-standard positivity as Rosati
  A proposal reads positive Rosati from a positive standard form. Kill it
  unless Frobenius/Rosati compatibility is constructed by the square.

KILL-WSC.4 Hard Lefschetz as degree construction
  A proposal uses Hard Lefschetz existence to pin the degree character. Kill
  it unless the Lefschetz class and degree maps are carrier-native.

KILL-WSC.5 finite standard window
  A proposal verifies finitely many standard-conjecture relations or traces.
  Kill it unless ghost cohomology is excluded carrier-natively.

KILL-WSC.6 control survival
  A proposal's standard package can be formed on arbitrary control companion
  data. Kill it unless controls die at carrier formation.
```
