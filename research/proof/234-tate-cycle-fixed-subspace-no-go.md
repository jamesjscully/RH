# 234 - Tate fixed subspaces do not construct the square

Status: no-go + Tate/Hodge-cycle/fixed-subspace carrier boundary,
2026-06-20. Ninety-seventh cycle of the doc-137 construction arc. Doc 233
killed compatible Galois/Chebotarev realization systems as square
construction. This document tests the stronger repair: take the
Galois/Frobenius fixed cycle subspace, add a Tate/Hodge/absolute-cycle
algebraicity theorem, and promote those fixed classes to the missing
`rep_NS` square carrier.

```text
compatible Galois system
  -> Tate / Hodge / absolute fixed cycle classes
  -> algebraic-cycle carrier / rep_NS
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_tate_cycle_fixed_subspace_no_go` (TCF1-TCF7 ALL PASS) --
identical Tate-cycle profiles do not determine finite-field count anchors;
Tate fixed classes do not construct NS degree slots; the fixed `z`-subspace
does not select diagonal/graph correspondence triples; fixed-cycle existence
does not impose Frobenius/Rosati compatibility; finite Tate windows admit
invariant ghost classes; the same formal Tate-cycle schema is formable on
controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_galois_compatible_system_no_go` (GCS1-GCS7 ALL PASS) and
`prime_int_n1b_formal_ns_envelope_no_go` (FNE1-FNE6 ALL PASS).

## 1. Purpose

Doc 233 says compatible Galois systems are realization data, not the square
carrier. The stronger repair is:

```text
do not stop at Frobenius characteristic polynomials;
take the Frobenius/Galois fixed subspace of the relevant realization;
invoke Tate/Hodge/absolute-cycle algebraicity;
declare those fixed classes to be rep_NS.
```

This is still not construction of `End(S^2/Z)`. A Tate theorem or Hodge
theorem can identify which cohomology classes come from algebraic cycles
after there is a variety, stack, motive, or square whose cycle map is
defined. It does not by itself construct the over-`Z` square, the two fiber
degree maps, carrier-native diagonal, Frobenius graph, proper correspondence
category, fiber-product composition, projection formula, or positive Rosati
relation.

This document rejects only the shortcut:

```text
the Tate/Hodge fixed cycle subspace constructs the square correspondence
carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category first constructs a cycle class map and for which a Tate/Hodge
algebraicity theorem is later proved.

## 2. Lemma

```text
Lemma 234.1 (Fixed cycle subspaces are not rep_NS).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Tate-cycle profile:

    fixed z-subspace dimension = 2,
    algebraicity theorem       = present,
    cycle class map            = present,
    semisimplicity             = present,
    pairing                    = present,
    comparison                 = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract fixed-cycle profile does not determine the
finite-field count anchor.

Nor do Tate fixed classes construct the NS degree slots. Keeping the same
fixed z-class and profile while changing the formal triple from (7,F,1) to
(10,F,1) changes

    Delta . Gamma  from 7 to 10.

The fixed z-subspace is also not the full correspondence carrier. For the
q=7 anchor, both Id and F commute with F and hence are fixed z-classes, but
they represent different correspondence triples:

    Delta . (1,Id,1) = 0,
    Delta . (7,F,1)  = 7.

Fixed-subspace membership does not select the diagonal, the Frobenius graph,
or the two degree slots.

Fixed-cycle existence does not impose Frobenius/Rosati compatibility. For
the off-circle integral q-similitude control

    F = [[0,-2],[1,3]], q=2,

the fixed classes Id and F still exist, but the normalized metric defect is
5.916 for the positive identity metric.

Finite Tate windows remain unsafe. A 5-cycle ghost summand preserves traces
in powers 1,2,3,4, changes count 5 by 5, and contributes a projector onto
the ghost summand that commutes with the augmented Frobenius.

The same formal Tate-cycle schema is formable on arbitrary control companion
data with no actual cycle class map, algebraicity theorem, rep_NS, square
carrier, or positive Rosati.

Consequently a Tate/Hodge fixed-subspace package constructs no Tate carrier,
cycle class map, algebraicity theorem, rep_NS, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_TATE_CYCLE_FIXED_SUBSPACE__FIXED_CLASSES_NOT_REP_NS__NO_GO.
```

## 3. Proof

`prime_int_n1b_tate_cycle_fixed_subspace_no_go` verifies the seven gates.

TCF1 records profile non-determination. The q=7 and q=5 anchors have the
same abstract Tate-cycle profile but different count windows.

TCF2 records the NS-degree-slot failure. With the same fixed z-class and
profile, changing only the formal degree slot changes `Delta.Gamma` from `7`
to `10`.

TCF3 records fixed z-subspace versus correspondence-triple separation. Both
`Id` and `F` are fixed z-classes, but `Delta.(1,Id,1)=0` while
`Delta.(7,F,1)=7`. The fixed subspace has not produced the diagonal, graph,
or degree slots.

TCF4 records fixed-cycle existence versus Rosati separation. The off-circle
q-similitude control still has fixed `Id` and `F` classes, but its normalized
Frobenius metric compatibility defect is `5.916`.

TCF5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces, changes count 5 by `5`, and supplies a fixed ghost
projector of rank `5`.

TCF6 records control formability. A control companion with the same formal
Tate-cycle schema has count window `8,112,1064` and metric defect `9.950`,
with no actual cycle class map, Tate theorem, `rep_NS`, square, or Rosati
input.

TCF7 records the construction failure: no Tate carrier, cycle class map,
algebraicity theorem, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-234:
  NEWLY CLOSED THIS CYCLE:
    - Tate/Hodge fixed subspace as global square carrier, cycle-class
      algebraicity as rep_NS construction, Frobenius-fixed z-classes as
      diagonal/graph triples, fixed-projector data as carrier determination,
      finite fixed-cycle windows as ghost exclusion, and formal Tate-cycle
      schemas as DH/Epstein carrier guards (doc 234).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper correspondence
      category constructs its cycle class map before any Tate/Hodge theorem
      is invoked;
    - a Tate/Hodge algebraicity theorem downstream of an actual square
      carrier with degree maps, correspondences, projection formula,
      Frobenius graph, and Rosati;
    - a theorem excluding ghost fixed classes from the actual carrier;
    - controls killed at carrier formation, not after taking fixed subspaces.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the fixed-cycle shortcut: Tate/Hodge
fixed subspaces are not construction of the global square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-TCF.1 fixed cycle subspace as square construction
  A proposal supplies Tate, Hodge, or absolute-cycle fixed classes and calls
  them the square. Kill it unless the global over-Z square carrier and cycle
  class map were already constructed carrier-natively.

KILL-TCF.2 fixed z-class as rep_NS
  A proposal treats a Frobenius/Galois fixed z-subspace as the NS triple.
  Kill it unless the two degree slots, off-diagonal intersections, and
  projection formula are constructed.

KILL-TCF.3 fixed class as diagonal or graph
  A proposal reads the diagonal or Frobenius graph from fixed-subspace
  membership. Kill it unless those correspondence triples and their
  composition are constructed by the carrier.

KILL-TCF.4 Tate algebraicity as Rosati
  A proposal reads positive Rosati from cycle algebraicity or fixedness. Kill
  it unless Frobenius/Rosati compatibility is constructed globally.

KILL-TCF.5 finite fixed-cycle window
  A proposal verifies finitely many fixed-cycle, Frobenius, or trace
  identities. Kill it unless ghost fixed classes are excluded
  carrier-natively.

KILL-TCF.6 control survival
  A proposal's fixed-cycle schema can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
