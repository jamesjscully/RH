# 273 - Oriented endpoint difference is not the square carrier

Status: no-go + oriented-endpoint-difference deletion, 2026-06-20.
One-hundred-thirty-sixth cycle of the doc-137 construction arc. Doc 272
killed the endpoint-swap repair because ordinary swap selects only total
degree. This document tests the next repair:

```text
add endpoint orientation/sign data so the anti-invariant direction d1-d2
commutes with swap, then recover endpoints from total and difference.
```

Witness, lead-reran this cycle:
`prime_int_n1b_oriented_endpoint_difference_no_go` (OED1-OED6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_endpoint_swap_boundary_no_go`,
`prime_int_n1b_endpoint_valuation_register_no_go`,
`prime_int_n1b_orientation_normalization_no_go`,
`prime_int_n1b_lambda_half_cover_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

This is not doc 170's generic orientation-normalization deletion, and it is
not doc 200's analytic lambda-half-cover deletion. Those kill support
orientation and formal half-cover shortcuts. The endpoint-specific repair is
more pointed:

```text
doc 272 left d1-d2 as anti-invariant;
add an orientation sign so d1-d2 descends with the swap;
use (d1+d2,d1-d2) to reconstruct d1,d2.
```

The positive fact is real. With an extra sign action on the unit line, the
difference-direction valuation twist commutes with the oriented endpoint
swap and splits `c=(1+z)^-1`.

The no-go is that the sign action and endpoint reconstruction are imported
decoders. The linear map

```text
(d1,d2) |-> (s,a) = (d1+d2, d1-d2)
```

has determinant `-2`, not `+/-1`. Its inverse is

```text
d1 = (s+a)/2,
d2 = (s-a)/2,
```

so endpoint recovery requires a parity condition and division by `2`. The
orientation sign also decides left versus right. None of this constructs the
actual square, `rep_NS`, carrier-native endpoint degree maps, Frobenius
graph, proper correspondence composition, projection formula, Rosati,
carrier boundary, or control death.

## 2. Lemma

```text
Lemma 273.1 (oriented difference needs a sign and a half-sum decoder).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Let tau(d1,d2)=(d2,d1) and ell_-(d1,d2)=d1-d2. With the ordinary endpoint
swap, the twist

    sigma(v,u) = (v, c^{ell_-(v)} phi(u))

does not commute with tau, because ell_- changes sign. If tau is extended by
the sign action u |-> u^-1 on the unit line, then sigma is involutive,
commutes with the oriented tau, and for v=(1,0):

    boundary(sigma(v,1)) = (0,c).

Thus the oriented-difference repair can split the named DD.4 representative.

However, endpoint recovery from total and difference is not an integral
unimodular coordinate change:

    det [[1,1],[1,-1]] = -2.

Only the index-two parity sublattice with s and a of the same parity decodes
to integer endpoints, and the inverse uses half-sums. For example:

    (s,a)=(11,9) -> (10,1),
    (s,a)=(11,3) -> (7,4),
    (s,a)=(11,8) -> no integer endpoint pair.

Changing the orientation sign changes left and right:

    (11,+9) -> (10,1),
    (11,-9) -> (1,10).

The same oriented-difference package is formable on controls. Therefore it
constructs no actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_ORIENTED_ENDPOINT_DIFFERENCE__SIGN_AND_HALF_SUM_DECODER_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_oriented_endpoint_difference_no_go` verifies six gates.

OED1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

OED2 checks the positive oriented-difference split. For `ell=d1-d2`, the
ordinary endpoint swap fails to commute with the valuation twist. The
sign-extended swap commutes with the twist in truncations `L=6,8,10,12`, and
`v=(1,0)` has boundary `c`.

OED3 records the decoder defect. The sum/difference map has determinant
`-2`, so it is not a unimodular change of integral endpoint coordinates. The
inverse uses half-sums and is defined only on the index-two same-parity
sublattice.

OED4 records the sign defect. The two signs of the difference direction give
the same unordered endpoints but swap left/right probes:

```text
(11,+9) -> (10,1),
(11,-9) -> (1,10).
```

Without carrier geometry forcing the sign, this is still endpoint choice.

OED5 repeats the same oriented-difference package on controls in dimensions
`2,4,8`. It is formable before the square is built, and controls do not die.

OED6 applies the SCC contract: oriented endpoint difference supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-273:
  NEWLY CLOSED THIS CYCLE:
    - adding endpoint orientation/sign data to the doc-272 anti-invariant
      difference direction and claiming total+difference reconstructs the
      carrier endpoint maps.

  POSITIVE INFORMATION RETAINED:
    - with an extra sign action, d1-d2 can be made equivariant for endpoint
      swap and can split the named DD.4 representative;
    - total plus oriented difference is enough to decode endpoints after a
      parity condition.

  STILL ADMISSIBLE:
    - an actual square carrier where orientation/sign, endpoint maps,
      boundary self-duality, and graph degrees are constructed together;
    - a carrier-native reason that the half-sum/parity reconstruction is
      represented by proper correspondences and projection/Rosati data;
    - a proof that no such carrier-native oriented endpoint extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the external orientation-sign repair of the endpoint
register. It does not close a future carrier where the square itself
constructs orientation, two endpoint maps, boundary direction, and proper
correspondence composition in one object.

## 5. Kill conditions

```text
KILL-OED.1 endpoint orientation as carrier sign
  A proposal adds a sign action so d1-d2 descends under endpoint swap. Kill it
  unless the sign is produced by the actual square carrier.

KILL-OED.2 sum/difference as integral endpoint coordinates
  The map (d1,d2)->(d1+d2,d1-d2) has determinant -2. Kill it unless the
  parity condition and half-sum decoder are carrier-native correspondences.

KILL-OED.3 orientation sign confused with left/right geometry
  Changing the sign swaps endpoint probes. Kill any route where the sign is
  chosen externally rather than forced by projection/Rosati geometry.

KILL-OED.4 decoded endpoint labels promoted to graph degrees
  Decoding endpoints from total/difference is not a Frobenius graph theorem.
  Kill it unless graph degrees and count anchors are constructed.

KILL-OED.5 control formability ignored
  The same oriented-difference package can be declared on controls. If the
  move exists before carrier formation, DH/Epstein have not died.

KILL-OED.6 SCC slots bypassed
  Oriented endpoint difference without the square, integral rep_NS, two
  carrier-native degree maps, diagonal, graph, proper correspondences,
  projection formula, Rosati, carrier boundary, and control death is not
  End(S^2/Z).
```
