# 278 - Oriented boundary complex is not the square carrier

Status: no-go + oriented-boundary-complex deletion, 2026-06-21.
One-hundred-forty-first cycle of the doc-137 construction arc. Doc 277
showed that a normal-crossing boundary gives two valuations but does not
select the DD.4 primitive direction. This document tests the next geometric
repair:

```text
use the oriented boundary complex of the two-component normal-crossing
boundary to select the alternating direction D1-D2.
```

Witness, lead-reran this cycle:
`prime_int_n1b_oriented_boundary_complex_no_go` (OBC1-OBC7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cartier_boundary_normal_no_go`,
`prime_int_n1b_oriented_endpoint_difference_no_go`,
`prime_int_n1b_endpoint_swap_boundary_no_go`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 277 did not kill boundary geometry. It killed only the claim that a
Cartier normal line or unadorned normal-crossing pair is already the square
carrier. The positive residue was:

```text
the boundary normal line is exactly the right local DD.4 shape.
```

The next natural repair is to use the boundary complex itself. For a
two-component normal-crossing boundary with components `D1,D2`, an oriented
edge has incidence

```text
partial e = D1 - D2.
```

This is a geometric-looking way to select the previously free direction
`ell=d1-d2`.

This document rejects only the shortcut:

```text
oriented boundary incidence constructs the square carrier.
```

It does not reject a future carrier where the oriented boundary complex is
part of `Qbar` and is coupled to `p1,p2`, `rep_NS`, graph composition,
Rosati, projection, parity, and control death.

## 2. Lemma

```text
Lemma 278.1 (oriented incidence selects a difference, not the square).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Let the oriented boundary complex have incidence vector (1,-1), so

    ell(d1,d2)=d1-d2.

For

    sigma(v,u) = (v, c^ell(v) phi(u)),

the map is involutive and the split vector v=(1,0) satisfies

    boundary(sigma(v,1)) = (0,c).

Thus oriented boundary incidence really can select a DD.4 splitting
direction. This is positive construction information.

However, reversing the boundary orientation changes c to c^-1. These two
representatives define the same Z/2 cohomology class because c^-2 is a
coboundary, but they are not the same representative. Orientation remains
sign data unless the square carrier fixes it.

The alternating direction is still rank one. Endpoint pairs (10,1) and
(11,2) have the same difference 9 but different totals and different
diagonal intersections in the finite-field SCC model. Therefore the
boundary-complex incidence does not recover the two endpoint degree maps or
the graph degree theorem.

If one combines total degree with the oriented difference to recover
endpoints, the coordinate transform

    (d1,d2) |-> (d1+d2, d1-d2)

has determinant -2. The inverse uses half-sums and is integral only on the
same-parity sublattice. Non-endpoint labels such as (11,8), (0,1), and
(10,1) still decode half-integrally.

The same oriented boundary complex can be attached to controls. Therefore it
constructs no actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary with control death, or DD.4 carrier-native
weight>=1 datum.
```

Verdict label:

```text
N1B_ORIENTED_BOUNDARY_COMPLEX__INCIDENCE_SELECTOR_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_oriented_boundary_complex_no_go` verifies seven gates.

OBC1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

OBC2 checks the positive oriented-boundary fact. The incidence vector
`(1,-1)` selects `ell=d1-d2`, and the split vector `(1,0)` has boundary `c`
in all tested truncations.

OBC3 records the orientation sign issue. Reversing orientation changes the
representative from `c` to `c^-1`; these are cohomologous in the Z/2 class,
but not equal as representatives.

OBC4 records the rank-one endpoint loss. The pairs `(10,1)` and `(11,2)`
have the same difference but different diagonal intersections.

OBC5 records the decoder defect. Total plus oriented difference has
determinant `-2`, so endpoint recovery requires parity and half-sums.

OBC6 attaches the same oriented boundary complex to controls in dimensions
2,4,8. No square data is consumed and controls do not die.

OBC7 applies the SCC/CFC contract: DD.4 splitting by oriented incidence does
not construct `Qbar`, `p1`, `p2`, `rep_NS`, graph, composition, Rosati,
projection, or control death.

## 4. Impact on R1

```text
R1 after docs 138-278:
  NEWLY CLOSED THIS CYCLE:
    - promoting the oriented boundary complex, incidence vector, or
      alternating boundary direction D1-D2 to the full square carrier.

  POSITIVE INFORMATION RETAINED:
    - oriented boundary incidence is a plausible carrier-native selector for
      the DD.4 difference direction;
    - the remaining carrier must tie that incidence to endpoint maps,
      parity/2-divisibility, rep_NS, graph composition, Rosati, and control
      death.

  STILL ADMISSIBLE:
    - a compactified zeta square whose oriented boundary complex selects the
      DD.4 direction and whose integral cycle theory proves the required
      parity theorem;
    - a construction where total, difference, endpoint maps, graph degrees,
      and Rosati are all consequences of one proper correspondence category;
    - a proof that no such oriented-boundary square can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct Qbar with boundary incidence coupled to integral rep_NS and
      proper correspondences.
```

## 5. Kill conditions

```text
KILL-OBC.1 oriented incidence promoted to carrier
  A proposal says the boundary complex gives D1-D2, hence the square is
  built. Kill it unless rep_NS, graph, Rosati, projection, and control death
  are built at the same step.

KILL-OBC.2 orientation sign ignored
  Reversing orientation changes the representative c to c^-1. Kill it unless
  the square carrier fixes the orientation/sign.

KILL-OBC.3 difference confused with endpoint maps
  The alternating direction is rank one. Kill it unless two endpoint degree
  maps are separately constructed.

KILL-OBC.4 total+difference decoder imported
  The total/difference transform has determinant -2. Kill it unless parity
  and half-sum decoding are carrier-native.

KILL-OBC.5 control formability ignored
  Boundary complexes can be attached to controls. If controls survive until a
  later filter, carrier formation has failed.

KILL-OBC.6 CFC bypassed
  Boundary incidence not embedded in the carrier-first square contract is not
  End(S^2/Z).
```
