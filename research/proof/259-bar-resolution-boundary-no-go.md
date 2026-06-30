# 259 - Bar resolution boundary is not the carrier boundary

Status: no-go + bar/coinduced-resolution boundary deletion, 2026-06-20.
One-hundred-twenty-second cycle of the doc-137 construction arc. Docs 257
and 258 isolated the remaining DD.4/SCC extension problem: the nonzero class
`[(1+z)^-1]` must die through a carrier-native
boundary/properness/self-duality extension, not by replacing the coefficient
system with an acyclic two-copy module.

Witness, lead-reran this cycle:
`prime_int_n1b_bar_resolution_boundary_no_go` (BRB1-BRB6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_coinduced_dd4_extension_no_go`,
`prime_int_n1b_dd4_scc_interface`,
`prime_int_pb_shear_h1_obstruction`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

After doc 258, the next standard repair is to say that the relevant
boundary is not merely coinduction but the universal bar-resolution
connecting boundary. This document rejects only that shortcut:

```text
the bar/coinduced resolution supplies a boundary, therefore DD.4/SCC is
constructed.
```

The boundary exists. The conclusion is false. It is a functorial resolution
coboundary certificate, available before any square carrier exists and
formable on controls. It does not supply the carrier-native
boundary/properness/self-duality map required by docs 256 and 257.

## 2. Lemma

```text
Lemma 259.1 (bar-resolution boundary is not the carrier boundary).

Let

    U_1 = 1 + z F_2[[z]],
    phi(z) = z/(1+z),
    c = (1+z)^-1.

In the base coefficient system, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

The coinduced/bar resolution coefficient system is

    C = U_1 x U_1,
    sigma(a,b) = (phi(b), phi(a)).

It is acyclic in degree one:

    H^1(<sigma>; C) = 0.

The diagonal DD.4 class is killed by the standard resolution coboundary:

    diag(c) = (c,c)
            = (c,1) / sigma(c,1)
            = (1,c) / sigma(1,c).

Thus the proposed boundary is a choice of 0-cochain in an acyclic
resolution. The same recipe works for arbitrary C_2 controls; it asks only
for the C_2-action and a cocycle. It does not use, construct, or force an
actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier-native boundary, or control death.

Consequently the bar/coinduced-resolution boundary is not construction-grade
End(S^2/Z). A surviving route must make [c] vanish through a boundary or
self-duality map produced by the actual square carrier.
```

Verdict label:

```text
N1B_BAR_RESOLUTION_BOUNDARY__UNIVERSAL_COBD_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_bar_resolution_boundary_no_go` verifies six gates.

BRB1 recomputes the base obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks that `c` is non-boundary with `res_1(c)=1`.

BRB2 computes the bar/coinduced resolution coefficient system:

```text
L6:  |B|=2^6,  |Z1|=2^6,  |H1|=1
L8:  |B|=2^8,  |Z1|=2^8,  |H1|=1
L10: |B|=2^10, |Z1|=2^10, |H1|=1
L12: |B|=2^12, |Z1|=2^12, |H1|=1
```

BRB3 verifies the explicit boundary certificate:

```text
diag(c)=(c,1)/sigma(c,1)=(1,c)/sigma(1,c).
```

The mirror formula matters: the boundary is not selecting carrier geometry.
It is selecting a resolution copy.

BRB4 repeats the same recipe on exact additive `F_2` control modules with
dimensions `2,4,6`, using only the `C_2` action and a cocycle. Therefore the
operation is not a DH/Epstein/control death point.

BRB5 records the support doubling:

```text
L=6:  6 -> 12
L=8:  8 -> 16
L=10: 10 -> 20
L=12: 12 -> 24
```

BRB6 applies the SCC contract: the bar boundary satisfies no square-carrier
slot.

## 4. Impact on R1

```text
R1 after docs 138-259:
  NEWLY CLOSED THIS CYCLE:
    - promoting the universal bar/coinduced-resolution boundary or
      connecting homomorphism to the DD.4/SCC carrier boundary.

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

This closes only the resolution-boundary shortcut. It does not close
carrier-native cohomological descent, provided the descent is produced by
the square carrier itself and preserves the SCC slots.

## 5. Kill conditions

```text
KILL-BRB.1 bar boundary promoted to carrier boundary
  A proposal says the DD.4 class dies because the bar/coinduced resolution
  has a connecting boundary. Unless that boundary is produced by the actual
  square carrier, this is a universal resolution coboundary.

KILL-BRB.2 diagonal coboundary promoted to properness
  The identity diag(c)=(c,1)/sigma(c,1)=(1,c)/sigma(1,c) is a 0-cochain
  certificate in the acyclic resolution. It is not the carrier's
  boundary/properness/self-duality map.

KILL-BRB.3 copy choice ignored
  Both (c,1) and (1,c) give the same diagonal coboundary. The bar resolution
  does not choose the geometric side; any side choice is extra data unless
  the carrier constructs it.

KILL-BRB.4 control formability ignored
  The same bar-boundary recipe applies to arbitrary C_2 controls. If the
  operation can be run before carrier formation, DH/Epstein have not died.

KILL-BRB.5 SCC slots bypassed
  A boundary certificate without the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
