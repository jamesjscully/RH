# 275 - Endpoint parity tags are not carrier degree maps

Status: no-go + endpoint-parity-tag deletion, 2026-06-20.
One-hundred-thirty-eighth cycle of the doc-137 construction arc. Doc 274
killed selecting the same-parity total/difference lattice or saturating by
half-sums. This document tests the next repair:

```text
keep the full total/difference register, but add a Z/2 parity tag
delta=s-a mod 2 and use the tag as the missing integrality datum.
```

Witness, lead-reran this cycle:
`prime_int_n1b_endpoint_parity_tag_no_go` (EPT1-EPT6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_endpoint_parity_saturation_no_go`,
`prime_int_n1b_oriented_endpoint_difference_no_go`,
`prime_int_n1b_endpoint_swap_boundary_no_go`,
`prime_int_n1b_valuation_parity_cover_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 274 says the same-parity condition is imported endpoint integrality.
The next repair is to avoid choosing the sublattice by remembering the parity
defect as an extra bit:

```text
delta(s,a) = s-a mod 2.
```

The positive fact is real. The tag detects exactly when the half-sum decoder

```text
(s,a) |-> ((s+a)/2,(s-a)/2)
```

is integral. The oriented difference twist still splits `c=(1+z)^-1`.

The no-go is that a parity tag is a diagnostic or selector, not the square
carrier. If the `delta=1` labels are discarded, the move is exactly doc 274's
externally selected same-parity lattice. If they are retained, the register
still contains labels that are not endpoint degree pairs, yet they can still
split the DD.4 representative and decode only to half-integral endpoints.
No actual square, `rep_NS`, carrier-native endpoint maps, Frobenius graph,
proper correspondence composition, projection formula, Rosati, carrier
boundary, or control death is constructed.

## 2. Lemma

```text
Lemma 275.1 (a parity tag diagnoses integrality but does not construct it).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For a total/difference label (s,a), attach

    delta = s-a mod 2.

Then delta=0 exactly on the same-parity lattice P={(s,a):s=a mod 2}, the
image of the endpoint lattice. On delta=0 labels the decoder

    (s,a) |-> ((s+a)/2,(s-a)/2)

is integral. With the oriented swap

    (s,a,delta,u) |-> (s,-a,delta,u^-1),

the twist

    sigma((s,a,delta),u)=((s,a,delta), c^a phi(u))

is involutive and commutes with swap on the tagged register. For the integral
label (1,1,0), the boundary is c.

However, the full tagged register also contains delta=1 labels:

    (0,1,1), (11,8,1), (10,1,1).

They do not decode to integer endpoint pairs, but the same twist still
splits the DD.4 representative when a=1. If they are kept, no integral
endpoint degree maps are constructed. If they are discarded, one has simply
selected the same-parity lattice P again.

The same parity-tag package is formable on controls. Therefore it constructs
no actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_ENDPOINT_PARITY_TAG__DIAGNOSTIC_NOT_CARRIER_INTEGRALITY__NO_GO.
```

## 3. Proof

`prime_int_n1b_endpoint_parity_tag_no_go` verifies six gates.

EPT1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

EPT2 checks the positive tag fact. On the finite tested window, `delta`
exactly detects when the half-sum decoder is integral. The tag has two
classes: `0` for the same-parity lattice and `1` for the excluded labels.

EPT3 checks the integral tagged split. The label `(1,1,0)` decodes to
endpoint pair `(1,0)` and splits `c`; this is only the doc-274 same-parity
lattice case with a tag attached.

EPT4 checks the non-endpoint tagged split. The labels `(0,1,1)`, `(11,8,1)`,
and `(10,1,1)` have no integral endpoint decode, yet the same oriented twist
still splits `c` whenever `a=1`. Keeping the `delta=1` side does not build
endpoint degree maps.

EPT5 repeats the same parity-tag package on controls in dimensions `2,4,8`.
Both `delta=0` and `delta=1` split chosen control classes, and controls do
not die.

EPT6 applies the SCC contract: endpoint parity tags supply no square-carrier
slot.

## 4. Impact on R1

```text
R1 after docs 138-275:
  NEWLY CLOSED THIS CYCLE:
    - repairing endpoint parity saturation by adding a Z/2 parity tag to the
      full total/difference register.

  POSITIVE INFORMATION RETAINED:
    - the parity tag exactly diagnoses half-sum integrality;
    - the tagged oriented-difference twist still splits the named DD.4
      representative.

  STILL ADMISSIBLE:
    - an actual square carrier where endpoint integrality, parity/2-divisibility,
      orientation/sign, boundary self-duality, and graph degrees are produced
      together;
    - a carrier-native theorem that excludes the non-endpoint parity class
      through proper correspondence geometry rather than a selector bit;
    - a proof that no such carrier-native parity-tagged endpoint extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the parity-tag bookkeeping repair. It does not close a
future carrier where the square itself constructs the integral endpoint
lattice and any necessary parity or 2-divisibility data.

## 5. Kill conditions

```text
KILL-EPT.1 parity tag as carrier integrality
  A proposal attaches delta=s-a mod 2 and treats it as endpoint construction.
  Kill it unless the square carrier constructs the integral endpoint lattice.

KILL-EPT.2 projecting to tag zero
  If delta=1 labels are discarded, the move is doc 274's selected
  same-parity lattice. Kill it unless the carrier forces that projection.

KILL-EPT.3 retaining tag one
  If delta=1 labels are retained, they have no integral endpoint decode and
  can still split c. Kill it unless proper correspondences explain them.

KILL-EPT.4 tag confused with degree map
  A Z/2 diagnostic bit is not two integral carrier-native degree maps.

KILL-EPT.5 control formability ignored
  The same parity-tag package can be declared on controls. If the move exists
  before carrier formation, DH/Epstein have not died.

KILL-EPT.6 SCC slots bypassed
  Endpoint parity tags without the square, integral rep_NS, two carrier-native
  degree maps, diagonal, graph, proper correspondences, projection formula,
  Rosati, carrier boundary, and control death are not End(S^2/Z).
```
