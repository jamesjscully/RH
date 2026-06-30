# 272 - Endpoint-swap symmetry does not construct the carrier boundary

Status: no-go + endpoint-swap-boundary deletion, 2026-06-20.
One-hundred-thirty-fifth cycle of the doc-137 construction arc. Doc 271
killed the free endpoint valuation register because the DD.4 boundary
direction was chosen. This document tests the immediate repair:

```text
impose the endpoint swap tau(d1,d2)=(d2,d1), then let symmetry choose the
boundary direction.
```

Witness, lead-reran this cycle:
`prime_int_n1b_endpoint_swap_boundary_no_go` (ESB1-ESB6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_endpoint_valuation_register_no_go`,
`prime_int_n1b_degree_pair_codec_no_go`,
`prime_int_n1b_valuation_degree_character_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

This is not a repeat of doc 269's rank-one valuation-character deletion.
Doc 269 killed the claim that total degree is enough endpoint data. Here the
question is sharper:

```text
can endpoint-swap symmetry force the DD.4 boundary direction that doc 271
left externally chosen?
```

The positive fact is real. In a free `Z^2` endpoint register, the primitive
swap-invariant direction

```text
ell_+(d1,d2)=d1+d2
```

commutes with the endpoint swap and can be used in the same valuation twist
`c^ell` to split `c=(1+z)^-1`.

The no-go is that symmetry has selected only a rank-one boundary direction.
It has not constructed two carrier-native endpoint maps, a Frobenius graph,
proper correspondence composition, projection formula, Rosati, carrier
boundary, or control death. The anti-invariant direction
`ell_-(d1,d2)=d1-d2` needs an extra sign/orientation action to commute with
the swap; with the ordinary swap it does not descend as boundary data.

## 2. Lemma

```text
Lemma 272.1 (endpoint swap selects total degree, not the square carrier).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Let tau(d1,d2)=(d2,d1). In the rank-two endpoint register, the primitive
tau-invariant linear functionals are exactly +/- (d1+d2). For

    ell_+(d1,d2)=d1+d2,
    E_+ = Z^2 x U_1,
    sigma(v,u) = (v, c^{ell_+(v)} phi(u)),

the map sigma is involutive, commutes with tau, and for any v with
ell_+(v)=1:

    boundary(sigma(v,1)) = (0,c).

Thus endpoint-swap symmetry can choose a total-degree split of the DD.4
representative.

However, total degree is one integer. The endpoint pairs `(10,1)` and
`(7,4)` have the same total degree 11 and the same diagonal intersection
`d1+d2-Tr(F)=10`, but their left/right endpoint probes differ. Therefore the
symmetry-selected boundary direction is not the two SCC degree maps.

The tau-anti-invariant primitive directions are exactly +/- (d1-d2). With
the ordinary endpoint swap, `d1-d2` changes sign and does not commute with
the valuation twist. It commutes only after adding a sign action on the unit
line, i.e. after importing orientation data not supplied by the square.

The same swap-symmetric total split is formable on controls. Therefore it
constructs no actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_ENDPOINT_SWAP_BOUNDARY__TOTAL_DIRECTION_NOT_TWO_ENDPOINT_MAPS__NO_GO.
```

## 3. Proof

`prime_int_n1b_endpoint_swap_boundary_no_go` verifies six gates.

ESB1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

ESB2 checks the positive symmetry fact. For `ell=d1+d2`, in truncations
`L=6,8,10,12`, the witness verifies:

```text
sigma^2=id,
tau sigma = sigma tau,
boundary(sigma(v,1)) = (0,c) for ell(v)=1.
```

No square-carrier data is used in this split.

ESB3 records the endpoint loss. Enumerating primitive forms in the tested
window shows the only swap-invariant primitive directions are
`+/- (d1+d2)`. The finite-field SCC anchor then checks:

```text
(10,1): total=11, diagonal=10
(7,4):  total=11, diagonal=10
```

while left and right endpoint probes distinguish the two pairs. Symmetry has
selected total degree, not the two endpoint maps.

ESB4 records the anti-invariant alternative. The primitive anti-invariant
directions are `+/- (d1-d2)`. With ordinary endpoint swap, the valuation twist
does not commute. It commutes only after adding a sign action on the unit
line; that is an imported orientation datum, not a carrier construction.

ESB5 repeats the same swap-symmetric total split on controls in dimensions
`2,4,8`. It is formable before any square is built, and controls do not die.

ESB6 applies the SCC contract: endpoint-swap boundary symmetry supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-272:
  NEWLY CLOSED THIS CYCLE:
    - imposing endpoint-swap symmetry on the doc-271 register and claiming
      the invariant total direction is now the carrier boundary.

  POSITIVE INFORMATION RETAINED:
    - endpoint swap canonically singles out total degree up to sign;
    - total degree can be used in the valuation twist to split the named
      DD.4 representative.

  STILL ADMISSIBLE:
    - an actual square carrier where swap symmetry, endpoint maps, boundary
      self-duality, and graph degrees are all constructed together;
    - a carrier-native orientation/sign datum tied to Rosati and projection,
      not imported as a sign action on a free register;
    - a proof that no such carrier-native endpoint-symmetric extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the symmetry repair of the external endpoint register. It
does not close a future carrier where the square itself constructs endpoint
swap, boundary direction, two degree maps, and proper correspondence
composition in one object.

## 5. Kill conditions

```text
KILL-ESB.1 endpoint swap promoted to carrier boundary
  A proposal says tau(d1,d2)=(d2,d1) forces the missing DD.4 boundary.
  Kill it unless the boundary is produced by the actual square carrier.

KILL-ESB.2 total degree confused with endpoint maps
  The invariant direction is d1+d2. Kill any use of it as SCC.3 unless the
  two endpoint degree maps are separately carrier-native.

KILL-ESB.3 diagonal intersection confused with correspondence data
  Same total degree and same diagonal intersection do not recover left/right
  endpoint probes, graph degrees, or proper composition.

KILL-ESB.4 anti-invariant direction smuggles orientation
  The direction d1-d2 changes sign under endpoint swap. Kill it unless the
  sign/orientation action is constructed by carrier geometry.

KILL-ESB.5 control formability ignored
  The same swap-symmetric total split can be declared on controls. If the
  move exists before carrier formation, DH/Epstein have not died.

KILL-ESB.6 SCC slots bypassed
  Endpoint-swap boundary symmetry without the square, integral rep_NS, two
  carrier-native degree maps, diagonal, graph, proper correspondences,
  projection formula, Rosati, carrier boundary, and control death is not
  End(S^2/Z).
```
