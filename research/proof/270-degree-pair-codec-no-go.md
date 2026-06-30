# 270 - Degree-pair codecs are not carrier degree maps

Status: no-go + degree-pair-codec deletion, 2026-06-20.
One-hundred-thirty-third cycle of the doc-137 construction arc. Doc 269
showed that one additive valuation character cannot replace the two SCC
endpoint degree maps. This document tests the immediate escape hatch:

```text
encode the pair (d1,d2) into one integer by a pairing function.
```

Witness, lead-reran this cycle:
`prime_int_n1b_degree_pair_codec_no_go` (DPC1-DPC7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_valuation_degree_character_no_go`,
`prime_int_n1b_square_carrier_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_presented_correspondence_carrier_no_go`.

## 1. Purpose

The codec repair is subtler than the rank-one additive character killed in
doc 269. It does not say the valuation is a homomorphism out of
`Z^2`. It says:

```text
use one integer as a code for the ordered endpoint pair.
```

This can be injective. Cantor pairing, prime-power coding, and finite
mixed-radix coding all label pairs of integers. The no-go is that an
injective label is not a carrier-native degree map. Recovering `d1` and `d2`
requires a decoder; transporting the SCC pairing through that decoder is
extra structure; and none of this constructs square geometry, proper
correspondences, projection, Rosati, or control death.

## 2. Lemma

```text
Lemma 270.1 (coding endpoint pairs is not constructing endpoints).

Let SCC.3 require two carrier-native endpoint degree maps

    d1, d2 : Corr(square) -> Z.

For any finite window, a pairing function can inject endpoint pairs
`(d1,d2)` into integer labels. For example, on the tested `7 x 7` window:

    Cantor pairing:     49/49 distinct labels,
    prime-power code:   49/49 distinct labels,
    mixed radix base 7: 49/49 distinct labels.

But the label is not the degree data. Cantor and prime-power labels do not
preserve endpoint addition or endpoint composition under ordinary valuation
arithmetic. Their left and right endpoint increments are not uniform Laurent
shifts. Mixed radix has uniform finite-window shifts only after an external
bound is chosen, and extending beyond the bound creates the collision

    code_7(1,0) = code_7(0,7).

More importantly, the SCC intersection form uses the endpoints themselves:

    (d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).

If the endpoints are recovered from a scalar label by a decoder, then the
decoder supplies the endpoint projections and the transported projection
pairing. The scalar label alone does not. The same label set can be decoded
in different ways, producing different left/right fiber probes and different
transported pairings.

Therefore degree-pair coding constructs no actual square, integral rep_NS,
two carrier-native degree maps, indecomposable diagonal, Frobenius graph,
proper correspondence category, fiber-product composition, projection
formula, canonical Rosati, positive primitive sign, carrier boundary, or
control death.
```

Verdict label:

```text
N1B_DEGREE_PAIR_CODEC__INJECTIVE_LABEL_NOT_CARRIER_DEGREES__NO_GO.
```

## 3. Proof

`prime_int_n1b_degree_pair_codec_no_go` verifies seven gates.

DPC1 records the positive fact. On the `7 x 7` window, Cantor pairing,
prime-power coding, and mixed radix all inject endpoint pairs:

```text
cantor:        49/49
prime_power:   49/49
mixed_radix_7: 49/49
```

DPC2 checks arithmetic compatibility. For the global injective codes, the
ordinary integer arithmetic on labels does not preserve endpoint addition or
endpoint product. The finite mixed-radix code is injective only with an
external bound:

```text
code_7(1,0) = code_7(0,7) = 7.
```

DPC3 checks endpoint shifts. Cantor and prime-power labels have varying left
and right increments. They do not supply two uniform Laurent endpoint shifts.
Mixed radix has uniform shifts only before the externally chosen bound and
then wraps into the same collision.

DPC4 checks decoder dependence. The Cantor labels of `(10,1)` and `(7,4)`
can be assigned the same scalar label set but swapped decoders. For label
`67`, the endpoint pair is either `(10,1)` or `(7,4)`, and left/right fiber
probes differ:

```text
left probe:   1 versus 4,
right probe: 10 versus 7.
```

DPC5 checks transported projection pairing. With the same scalar labels, the
standard and swapped decoders transport different endpoint pairings against
the probe `(2,5)`:

```text
standard: 52 / 43,
swapped:  43 / 52.
```

Thus the pairing is decoder data, not scalar valuation data.

DPC6 records control formability. The same endpoint codec can be declared on
finite controls in dimensions `2,4,8` without using square geometry and
without killing controls.

DPC7 applies the SCC contract: pair coding supplies no square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-270:
  NEWLY CLOSED THIS CYCLE:
    - encoding the two SCC endpoint degrees into one integer label by Cantor,
      prime-power, mixed-radix, lookup-table, or similar codec and then
      treating the label as the carrier degree data.

  POSITIVE INFORMATION RETAINED:
    - endpoint pairs can be injected into integer labels;
    - finite windows can always be coded.

  STILL ADMISSIBLE:
    - a carrier where the square itself constructs two endpoint maps and
      maybe also a harmless code downstream;
    - a carrier-native valuation/uniformizer axis that coexists with, rather
      than replaces, the two endpoint degree maps;
    - a carrier-native boundary/properness/self-duality map killing [c] while
      preserving endpoint data, projection, Rosati, and control death.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the codec shortcut. It does not close a future square
carrier that constructs real endpoint maps and later chooses a serialization
for bookkeeping.

## 5. Kill conditions

```text
KILL-DPC.1 pair codec promoted to degree maps
  A proposal encodes `(d1,d2)` into one integer and calls that the degree
  datum. Kill it unless the square constructs the two endpoint maps before
  any coding.

KILL-DPC.2 decoder smuggled in as geometry
  A decoder from labels to endpoints is not rep_NS, projection, or proper
  correspondence composition. Kill it unless the decoder is carrier-native.

KILL-DPC.3 finite mixed-radix window treated as global
  Mixed-radix coding is bounded bookkeeping. Extending past the bound creates
  collisions or requires a new external bound.

KILL-DPC.4 transported pairing promoted to projection formula
  A pairing transported through a decoder is not the carrier projection
  formula. Kill it unless the formula is proved from proper correspondences.

KILL-DPC.5 control formability ignored
  Pair codecs can be declared on controls. If the move exists before carrier
  formation, DH/Epstein have not died.

KILL-DPC.6 SCC slots bypassed
  Coded degree labels without the square, integral rep_NS, two degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  carrier boundary, and control death are not End(S^2/Z).
```
