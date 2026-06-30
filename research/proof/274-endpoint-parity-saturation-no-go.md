# 274 - Endpoint parity saturation is not the square carrier

Status: no-go + endpoint-parity-saturation deletion, 2026-06-20.
One-hundred-thirty-seventh cycle of the doc-137 construction arc. Doc 273
killed oriented endpoint difference because total/difference reconstruction
requires a same-parity condition and a half-sum decoder. This document tests
the next repair:

```text
build the parity condition into the endpoint register, or saturate the
register by adjoining the half-sums.
```

Witness, lead-reran this cycle:
`prime_int_n1b_endpoint_parity_saturation_no_go` (EPS1-EPS6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_oriented_endpoint_difference_no_go`,
`prime_int_n1b_endpoint_swap_boundary_no_go`,
`prime_int_n1b_endpoint_valuation_register_no_go`,
`prime_int_n1b_valuation_parity_cover_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 273 left a specific defect:

```text
(d1,d2) |-> (s,a) = (d1+d2,d1-d2)
```

has determinant `-2`, so decoding endpoints from `(s,a)` uses

```text
d1=(s+a)/2,
d2=(s-a)/2.
```

The natural repair is to hide that denominator by replacing the full
`Z^2_{s,a}` register with the same-parity lattice

```text
P = {(s,a) in Z^2 : s = a mod 2},
```

or else to saturate the full register by allowing half-integral endpoint
coordinates. The positive facts are real. `P` is exactly the image of the
endpoint lattice under total/difference coordinates; the half-sum decoder is
integral on `P`; and the oriented difference twist still splits
`c=(1+z)^-1`.

The no-go is that choosing `P` is just importing endpoint integrality in
disguise. The full total/difference register still has labels that split the
DD.4 class but do not decode to integer endpoints. Saturating the register
decodes those labels only by making endpoint degrees half-integral. Neither
move constructs the square, `rep_NS`, carrier-native endpoint degree maps,
Frobenius graph, proper correspondence composition, projection formula,
Rosati, carrier boundary, or control death.

## 2. Lemma

```text
Lemma 274.1 (endpoint parity is imported lattice data).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Let P={(s,a):s=a mod 2}. The total/difference map

    A(d1,d2)=(d1+d2,d1-d2)

has determinant -2 and image P. Therefore P has index two in Z^2_{s,a};
modulo 2, it contains only classes (0,0) and (1,1), excluding (0,1) and
(1,0). On P the decoder

    (s,a) |-> ((s+a)/2,(s-a)/2)

is integral and recovers the endpoint pair. With the oriented swap
(s,a,u) |-> (s,-a,u^-1), the twist

    sigma((s,a),u)=((s,a), c^a phi(u))

is involutive, commutes with the swap, and for (s,a)=(1,1):

    boundary(sigma((1,1),1)) = (0,c).

Thus the parity-saturated endpoint lattice can split the named DD.4
representative.

However, the full total/difference register has non-endpoint labels such as

    (0,1), (11,8), (10,1).

They are outside P, yet the same oriented twist still splits the DD.4 class
on the full register when a=1. Restricting to P is therefore an added
integrality condition, not a consequence of the DD.4 split.

If instead the full register is saturated by applying the half-sum decoder to
all labels, those excluded labels become half-integral endpoints:

    (0,1)  -> (1/2,-1/2),
    (11,8) -> (19/2,3/2),
    (10,1) -> (11/2,9/2).

That is not an integral Neron-Severi degree lattice. The same parity or
saturation package is formable on controls. Therefore it constructs no
actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_ENDPOINT_PARITY_SATURATION__INDEX_TWO_LATTICE_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_endpoint_parity_saturation_no_go` verifies six gates.

EPS1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

EPS2 checks the positive parity-lattice fact. The image of endpoints in
sum/difference coordinates is the same-parity sublattice with mod-2 classes
`(0,0)` and `(1,1)`. The excluded classes are `(0,1)` and `(1,0)`. On this
lattice, the decoder round-trips endpoint pairs and the oriented difference
twist splits `c` in truncations `L=6,8,10,12`.

EPS3 records the choice defect. The excluded labels `(0,1)`, `(11,8)`, and
`(10,1)` do not decode to integer endpoints, but the full total/difference
register can still run the same oriented twist. In particular `(0,1)` has
`a=1` and splits `c`. The parity condition is therefore extra integrality
data.

EPS4 records the saturation defect. Applying the half-sum decoder on the full
register sends excluded labels to half-integral endpoint degrees, while valid
same-parity labels remain integral.

EPS5 repeats the same parity/saturation package on controls in dimensions
`2,4,8`. It is formable before the square is built, and controls do not die.

EPS6 applies the SCC contract: endpoint parity saturation supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-274:
  NEWLY CLOSED THIS CYCLE:
    - repairing oriented endpoint difference by selecting the same-parity
      total/difference lattice or saturating the full register by half-sums.

  POSITIVE INFORMATION RETAINED:
    - the same-parity lattice is exactly the image of the endpoint lattice in
      total/difference coordinates;
    - on that lattice, the half-sum decoder is integral and the oriented
      difference twist splits the named DD.4 representative.

  STILL ADMISSIBLE:
    - an actual square carrier where the integral endpoint lattice,
      orientation/sign, boundary self-duality, and graph degrees are produced
      together;
    - a carrier-native parity or 2-divisibility theorem tied to proper
      correspondences, projection, and Rosati;
    - a proof that no such carrier-native parity-saturated endpoint extension
      can exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the external parity-lattice or half-sum-saturation repair.
It does not close a future carrier where the square itself constructs the
integral endpoint lattice and proves the needed parity/2-divisibility through
proper correspondence geometry.

## 5. Kill conditions

```text
KILL-EPS.1 same-parity lattice as carrier construction
  A proposal replaces Z^2_{s,a} by s=a mod 2. Kill it unless the index-two
  integrality condition is forced by the actual square carrier.

KILL-EPS.2 half-sum decoder hidden in coordinates
  A proposal says endpoints are recovered by (s+a)/2 and (s-a)/2. Kill it
  unless the half-sum maps are carrier-native integral correspondences.

KILL-EPS.3 saturation by half-integral endpoints
  Saturating the full register makes excluded labels half-integral. Kill it
  unless integral rep_NS degree maps are preserved.

KILL-EPS.4 invalid split labels ignored
  The full total/difference register has non-endpoint labels that still split
  the DD.4 class. Kill it unless the carrier itself excludes them.

KILL-EPS.5 control formability ignored
  The same parity/saturation package can be declared on controls. If the move
  exists before carrier formation, DH/Epstein have not died.

KILL-EPS.6 SCC slots bypassed
  Endpoint parity saturation without the square, integral rep_NS, two
  carrier-native degree maps, diagonal, graph, proper correspondences,
  projection formula, Rosati, carrier boundary, and control death is not
  End(S^2/Z).
```
