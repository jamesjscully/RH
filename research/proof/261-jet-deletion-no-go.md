# 261 - Jet deletion is not the carrier boundary

Status: no-go + leading-jet/filtration deletion, 2026-06-20.
One-hundred-twenty-fourth cycle of the doc-137 construction arc. Docs 257-260
left only the carrier-native DD.4 extension: the nonzero class
`[(1+z)^-1]` must die through a boundary/properness/self-duality map
produced by the actual square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_jet_deletion_no_go` (JQD1-JQD6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_mapping_cone_nullhomotopy_no_go`,
`prime_int_n1b_bar_resolution_boundary_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

After formal splitter, coinduced, bar-resolution, and cone repairs fail, a
tempting move is to erase the leading obstruction by filtration:

```text
replace U_1 = 1 + z F_2[[z]] by U_3 = 1 + z^3 F_2[[z]],
or pass to an associated-graded/jet deletion where res_1 and res_2 vanish.
```

This document rejects only that shortcut. `U_3` is acyclic in the tested
range, but the DD.4 class is not in `U_3`. The obstruction has been deleted,
not killed by a carrier boundary.

## 2. Lemma

```text
Lemma 261.1 (jet deletion is not carrier boundary).

Let

    U_1 = 1 + z F_2[[z]],
    phi(z) = z/(1+z),
    c = (1+z)^-1.

In the base coefficient system, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

The higher unit filtration

    U_3 = 1 + z^3 F_2[[z]]

is phi-stable, and in the same truncations:

    H^1(<phi>; U_3) = 0.

However,

    c = 1 + z + z^2 + ...

has deleted jets `(res_1(c), res_2(c)) = (1,1)`, so `c` is not an element of
`U_3`. The quotient `U_1/U_3`, computed as the two-jet unit group, still has:

    H^1(<phi>; U_1/U_3) = Z/2,
    [c mod U_3] != 0.

Therefore passing to `U_3` or deleting the leading jets removes the
obstruction-bearing quotient. It does not construct a boundary/properness/
self-duality map that sends [c] to zero.

The same operation is formable on arbitrary filtered controls: delete the
graded piece carrying the chosen class. It constructs no actual square,
integral rep_NS, two degree maps, indecomposable diagonal, Frobenius graph,
proper correspondence category, fiber-product composition, projection
formula, canonical Rosati, positive primitive sign, carrier boundary, or
control death.
```

Verdict label:

```text
N1B_JET_DELETION__DROPS_OBSTRUCTION_QUOTIENT_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_jet_deletion_no_go` verifies six gates.

JQD1 recomputes the base obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks that `c` is non-boundary with `res_1(c)=1`.

JQD2 computes the higher filtration `U_3`. It is `phi`-stable and has
trivial degree-one cohomology in the tested truncations:

```text
L6:  deleted_jets=(1,1), |H1(U3)|=1
L8:  deleted_jets=(1,1), |H1(U3)|=1
L10: deleted_jets=(1,1), |H1(U3)|=1
L12: deleted_jets=(1,1), |H1(U3)|=1
```

The same line records the reason this is not a solution: `c` has nonzero
first and second jets, so it is outside the retained coefficient system.

JQD3 computes the deleted quotient `U_1/U_3`:

```text
|B|=2^1, |Z1|=2^2, |H1|=2, c_jet=(1,1), c_jet not in B.
```

Thus the obstruction survives exactly in the quotient discarded by the
repair.

JQD4 checks neighboring cutoffs at L=8,10,12:

```text
U_2 and U_4 keep |H1|=2;
U_3 and U_5 make |H1|=1 by dropping lower jets.
```

The vanishing is a filtration cutoff effect, not a carrier-produced boundary
map.

JQD5 repeats the same deletion on exact filtered `F_2` controls in dimensions
`3,4,8`. No square-carrier data is used.

JQD6 applies the SCC contract: jet deletion satisfies no square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-261:
  NEWLY CLOSED THIS CYCLE:
    - replacing the DD.4 coefficient system by a higher unit filtration,
      associated graded, or leading-jet deletion that omits res_1/res_2.

  STILL ADMISSIBLE:
    - a carrier-native boundary/properness/self-duality extension in which
      [c] maps to zero because the actual square carrier supplies the map;
    - a construction where that same map kills DH/Epstein/controls at
      carrier formation;
    - a proof that no such carrier-native extension can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the jet-deletion shortcut. It does not close a carrier
whose own boundary map factors through a filtration while preserving the
deleted quotient as constructed square data.

## 5. Kill conditions

```text
KILL-JQD.1 higher filtration promoted to carrier boundary
  A proposal replaces U_1 by U_3, or another higher unit filtration, and
  claims DD.4 is solved because H^1 vanishes. This deletes the jets where
  c lives.

KILL-JQD.2 associated graded deletes the obstruction quotient
  If an associated-graded or jet quotient removes res_1/res_2, it has not
  killed [c]; it has discarded U_1/U_3, where the obstruction remains.

KILL-JQD.3 cutoff choice ignored
  Neighboring cutoffs behave differently. A cutoff that makes H^1 vanish is
  extra filtration data unless the carrier constructs it and preserves the
  SCC slots.

KILL-JQD.4 control formability ignored
  Filtered controls can delete the graded piece carrying any chosen class.
  If the operation can be run before carrier formation, DH/Epstein have not
  died.

KILL-JQD.5 SCC slots bypassed
  A filtration that drops the obstruction but lacks the square, integral
  rep_NS, degree maps, diagonal, graph, proper correspondences, projection
  formula, Rosati, positive primitive sign, and control death is not
  End(S^2/Z).
```
