# 268 - Valuation-parity cover is not the carrier boundary

Status: no-go + valuation-parity-cover deletion, 2026-06-20.
One-hundred-thirty-first cycle of the doc-137 construction arc. Doc 267
showed that full Laurent-field Hilbert 90 kills the DD.4 class only by
using the odd valuation/uniformizer axis. This document tests the minimal
repair:

```text
do not import the full Laurent line; keep only valuation mod 2.
```

Witness, lead-reran this cycle:
`prime_int_n1b_valuation_parity_cover_no_go` (VPC1-VPC6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_laurent_field_hilbert90_no_go`,
`prime_int_n1b_prime_line_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 267 leaves a tempting repair. Since the boundary class of a valuation-m
element is only `m[c]` modulo 2, maybe the carrier does not need the whole
Laurent valuation line. Maybe it needs only a two-sheet parity cover.

This document rejects only that shortcut. The parity cover can kill the
named DD.4 representative, but it is still not the square carrier. It
forgets the integer valuation, supplies no full Laurent line, gives no
correspondence endpoints or degree maps, and is formable on controls.

## 2. Lemma

```text
Lemma 268.1 (valuation parity is a splitter quotient, not carrier data).

Let

    U_1 = 1 + z F_2[[z]],
    phi(z) = z/(1+z),
    c = (1+z)^-1.

In U_1, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Now form the parity cover

    E = (Z/2) x U_1

with generator action

    sigma(e,u) = (e, c^e phi(u)).

This is the mod-2 quotient of the Laurent valuation action. In `E`, the
element `sigma(1,1)=(1,c)` has boundary

    (1,c) / sigma(1,c) = (0,c).

Thus the named DD.4 representative is killed.

However, the cover remembers only valuation parity. It identifies valuations
`m` and `m+2`, so it cannot recover integer degree data or the two
carrier-native degree maps. It has two sheets, not a full Laurent line.
DMP/TCR support still lacks degrees <= -2, and the cover supplies no proper
correspondence endpoints. The same parity-cover splitting is formable on
controls. Therefore it constructs no actual square, integral rep_NS,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_VALUATION_PARITY_COVER__SPLITS_C_BUT_LOSES_DEGREES__NO_GO.
```

## 3. Proof

`prime_int_n1b_valuation_parity_cover_no_go` verifies six gates.

VPC1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

VPC2 checks the parity-cover split:

```text
sigma(e,u) = (e, c^e phi(u)),
sigma(1,1) = (1,c),
(1,c) / sigma(1,c) = (0,c).
```

This records the positive fact: mod-2 valuation data can kill the named
representative.

VPC3 records the loss. The parity cover keeps only valuation modulo 2:

```text
-4 and -2 have the same parity,
-4 and  0 have the same parity,
-4 and  2 have the same parity,
-4 and  4 have the same parity.
```

Thus it cannot recover the integer valuation/degree data the square carrier
requires.

VPC4 records that the two-sheet parity cover is neither the DMP/TCR Laurent
line nor a correspondence-endpoint object. DMP still lacks the negative
Laurent degrees.

VPC5 repeats the same split on exact `F_2` controls in dimensions
`1,2,4,8`. No square-carrier data is used.

VPC6 applies the SCC contract: the valuation-parity cover supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-268:
  NEWLY CLOSED THIS CYCLE:
    - replacing the full Laurent valuation axis by the mod-2 valuation
      character, orientation bit, or parity cover and promoting that to
      the DD.4/SCC carrier boundary.

  POSITIVE INFORMATION RETAINED:
    - the DD.4 representative is killed already by valuation parity;
    - but the square carrier needs the stronger integer valuation/degree
      and endpoint structure, not just the parity quotient.

  STILL ADMISSIBLE:
    - a carrier-native valuation/uniformizer axis produced by the actual
      square carrier, with integer degree data, proper endpoints, projection,
      Rosati, and control death;
    - a carrier-native boundary/properness/self-duality map killing [c]
      without collapsing the required degree data to parity;
    - a proof that no such carrier-native valuation/boundary extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the parity quotient of valuation. It does not close a
future carrier where the square itself constructs an integer valuation or
degree axis and the SCC slots.

## 5. Kill conditions

```text
KILL-VPC.1 parity cover promoted to carrier
  A proposal says only valuation mod 2 is needed because it kills c. Kill it
  unless the square carrier constructs the parity cover and the missing
  integer degree data.

KILL-VPC.2 parity confused with valuation
  The parity cover identifies m and m+2. It is not the Laurent valuation
  axis and cannot provide carrier-native degree maps.

KILL-VPC.3 two-sheet cover read as Laurent line
  A two-sheet cover is not a full Laurent line and does not repair the DMP
  missing negative degrees.

KILL-VPC.4 split representative promoted to properness
  The identity `(1,c)/sigma(1,c)=(0,c)` is a parity-cover coboundary. It is
  not the carrier's boundary/properness/self-duality map.

KILL-VPC.5 control formability ignored
  The same parity-cover split can be declared on controls. If the move
  exists before carrier formation, DH/Epstein have not died.

KILL-VPC.6 SCC slots bypassed
  Valuation parity without the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
