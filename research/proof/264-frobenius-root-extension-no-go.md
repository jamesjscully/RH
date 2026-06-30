# 264 - Frobenius-root extension is not the carrier boundary

Status: no-go + Frobenius-root/perfect-closure deletion, 2026-06-20.
One-hundred-twenty-seventh cycle of the doc-137 construction arc. Docs
257-263 left only the carrier-native DD.4 extension: the nonzero class
`[(1+z)^-1]` must die through a boundary/properness/self-duality map
produced by the actual square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_frobenius_root_extension_no_go` (FRC1-FRC6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_norm_one_hilbert90_no_go`,
`prime_int_n1b_obstruction_quotient_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The next shortcut is to pass to a Frobenius root or perfect closure:

```text
adjoin w with w^2=z, extend phi by phi(w)=w/(1+w), and kill c after pullback.
```

This document rejects only that shortcut. The old class really does become
a coboundary after adjoining `w`. But the operation does not construct the
square-carrier boundary. It only shifts the same obstruction one Frobenius
root lower.

## 2. Lemma

```text
Lemma 264.1 (Frobenius-root extension shifts the DD.4 obstruction).

Let

    U_1(z) = 1 + z F_2[[z]],
    phi_z(z) = z/(1+z),
    c_z = (1+z)^-1.

For truncations L=6,8,10,12:

    H^1(<phi_z>; U_1(z)) = Z/2,
    [c_z] != 0,
    res_1(c_z)=1.

Now adjoin a Frobenius root

    z = w^2,
    phi_w(w) = w/(1+w).

This is compatible with the old action because

    phi_w(w)^2 = w^2/(1+w)^2 = z/(1+z) = phi_z(z).

Set

    d = (1+w)^-1 in U_1(w).

Then the pullback of the old obstruction is

    c_z |_{z=w^2} = (1+w)^-2 = d / phi_w(d).

Thus the old class becomes a coboundary after the root extension.

However,

    H^1(<phi_w>; U_1(w)) = Z/2,
    [d] != 0,
    res_1(d)=1.

The obstruction has not disappeared. It has been reindexed from `c_z` to
the new lower-root class `d`. The extension also refines coefficient support:
the old cutoff L maps to cutoff 2L, and the splitter `d` uses the new odd
`w`-slots that did not exist in the `z`-system.

The same root/splitter adjoining pattern is formable on controls before any
square carrier exists. Therefore Frobenius-rooting or passing to a perfect
closure constructs no actual square, integral rep_NS, two degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_FROBENIUS_ROOT_EXTENSION__OBSTRUCTION_REINDEXED_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_frobenius_root_extension_no_go` verifies six gates.

FRC1 recomputes the base obstruction:

```text
L6,L8,L10,L12: H1=2, c non-boundary, res_1(c)=1.
```

FRC2 verifies the root extension and explicit coboundary:

```text
L6 -> L12:  pull(c)=d/phi(d)
L8 -> L16:  pull(c)=d/phi(d)
L10 -> L20: pull(c)=d/phi(d)
L12 -> L24: pull(c)=d/phi(d)
```

FRC3 computes the new `w`-system:

```text
L12: |B|=2^6,  |Z1|=2^7,  d non-boundary
L16: |B|=2^8,  |Z1|=2^9,  d non-boundary
L20: |B|=2^10, |Z1|=2^11, d non-boundary
L24: |B|=2^12, |Z1|=2^13, d non-boundary
```

Thus the old class has become the boundary of the new nontrivial class.

FRC4 records support refinement:

```text
rank 6 -> 12, rank 8 -> 16, rank 10 -> 20, rank 12 -> 24.
```

The pulled old class uses only even `w`-powers. The splitter `d` uses the
new odd root slots.

FRC5 repeats the root/splitter-adjoining pattern on exact `F_2` controls in
dimensions `1,2,4,8`. No square-carrier data is used.

FRC6 applies the SCC contract: Frobenius-rooting supplies no square-carrier
slot.

## 4. Impact on R1

```text
R1 after docs 138-264:
  NEWLY CLOSED THIS CYCLE:
    - adjoining Frobenius roots, square roots, or a perfect closure of the
      DD.4 coefficient system and treating the old pulled class as solved.

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

This closes only coefficient perfection/root-adjoining. It does not close a
carrier-constructed perfectoid, prismatic, or Frobenius-root object if the
square carrier itself supplies the boundary/properness/self-duality map and
the SCC slots survive.

## 5. Kill conditions

```text
KILL-FRC.1 Frobenius root promoted to carrier boundary
  A proposal adjoins w with w^2=z and says the DD.4 obstruction is solved
  because c pulls back to d/phi(d). This is root-adjoining, not a
  carrier-native boundary map.

KILL-FRC.2 perfect closure treated as vanishing
  Passing to all 2-power roots can make each old finite-stage obstruction a
  boundary one stage later. It also produces a new lower-root obstruction at
  each stage unless the carrier supplies an actual vanishing mechanism.

KILL-FRC.3 support refinement ignored
  The old L-window becomes a 2L-window, and the splitter uses odd root
  slots. Projection back to the old support is extra data unless the square
  carrier constructs it.

KILL-FRC.4 control formability ignored
  Formal root/splitter adjoining can be run on controls before carrier
  formation. If controls die only by the same formal operation, DH/Epstein
  have not died at a carrier-native point.

KILL-FRC.5 SCC slots bypassed
  A Frobenius-root extension that lacks the square, integral rep_NS, degree
  maps, diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
