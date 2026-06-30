# 269 - Valuation degree character is not the square carrier

Status: no-go + valuation-degree-character deletion, 2026-06-20.
One-hundred-thirty-second cycle of the doc-137 construction arc. Docs 267
and 268 isolated the valuation repair:

```text
full Laurent field kills the class, but imports the valuation line;
valuation parity kills the class, but forgets integer degree.
```

This document tests the next minimal repair:

```text
keep the full integer valuation character, then read it as the SCC degree data.
```

Witness, lead-reran this cycle:
`prime_int_n1b_valuation_degree_character_no_go` (VDC1-VDC6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_valuation_parity_cover_no_go`,
`prime_int_n1b_laurent_field_hilbert90_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The full Laurent valuation axis has one real advantage over doc 268's parity
cover: it remembers the exact integer valuation. That makes a tempting
shortcut:

```text
use the valuation as the missing carrier-native degree datum.
```

This document rejects only that shortcut. The obstruction is not parity now.
The obstruction is rank and endpoint geometry. A single additive valuation
character is one integer. The square-carrier contract needs two independent
endpoint degree maps, plus a correspondence category in which those endpoints
compose, satisfy projection, and pair with diagonal/graph classes.

## 2. Lemma

```text
Lemma 269.1 (one valuation character is not two endpoint degrees).

Let K=F_2((z)), U_1=1+z F_2[[z]], phi(z)=z/(1+z), and
c=(1+z)^-1. In U_1, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

In K^*, the Laurent element phi(z)=z/(1+z) has boundary

    phi(z) / phi(phi(z)) = c,

so the full valuation axis kills the named DD.4 representative and retains
the exact integer valuation m.

However, any promoted additive degree character

    chi(d_1,d_2)=a d_1 + b d_2 : Z^2 -> Z

has rank at most one. If (a,b) != (0,0), then (b,-a) is a nonzero endpoint
direction in ker(chi). Moving by that direction preserves the single
valuation character while changing an endpoint pairing. Thus chi cannot
recover the two carrier-native degree maps required by SCC.3.

The finite-field SCC anchor sees the same loss:

    (7,F,1).Delta  = 7,
    (10,F,1).Delta = 10,
    (7,F,4).Delta  = 10.

The last two have the same total degree 11 and the same diagonal
intersection, but left/right fiber probes distinguish them:

    left fiber:  1 versus 4,
    right fiber: 10 versus 7.

Therefore a valuation-degree character may be useful boundary data, but it
is not the square carrier. It supplies no actual square, integral rep_NS,
two degree maps, indecomposable diagonal, Frobenius graph, proper
correspondence category, fiber-product composition, projection formula,
canonical Rosati, positive primitive sign, carrier boundary, or control
death.
```

Verdict label:

```text
N1B_VALUATION_DEGREE_CHARACTER__KILLS_C_BUT_LOSES_ENDPOINT_RANK__NO_GO.
```

## 3. Proof

`prime_int_n1b_valuation_degree_character_no_go` verifies six gates.

VDC1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

VDC2 checks the positive Laurent fact. In pairs `(valuation, unit)`,

```text
phi(z) = (1,c),
boundary(phi(z)) = (0,c).
```

It also checks valuations `-4..4` remain exact integers, not merely parity
classes, and that the odd valuation classes are precisely the ones that kill
the mod-2 DD.4 obstruction.

VDC3 rejects the rank-one promotion. For every tested additive character
`chi(d1,d2)=a d1+b d2`, the witness moves by `(b,-a)`. The single character
is unchanged, but an endpoint probe changes. The witness checks:

```text
chi(1,0), chi(0,1), chi(1,1), chi(1,-1), chi(2,3), chi(-2,5).
```

This is the structural defect: one additive valuation character cannot
recover two carrier-native degree maps.

VDC4 anchors the defect in the square-carrier finite-field model. For
`q=7`, the diagonal intersections are:

```text
(7,F,1)  ->  7,
(10,F,1) -> 10,
(7,F,4)  -> 10.
```

The pairs `(10,F,1)` and `(7,F,4)` have the same total degree and the same
diagonal intersection, while the left/right fiber probes distinguish their
endpoints. Endpoint data is not optional bookkeeping.

VDC5 records that the same single-degree-character package is formable on
controls. It can be declared on finite control dimensions `2,4,8` without
using a square carrier.

VDC6 applies the SCC contract: the valuation-degree character supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-269:
  NEWLY CLOSED THIS CYCLE:
    - promoting the full integer valuation character, total degree, or any
      rank-one additive degree character to the two SCC degree maps.

  POSITIVE INFORMATION RETAINED:
    - the full Laurent valuation axis kills the DD.4 representative and
      remembers exact integer valuation;
    - this is stronger than valuation parity, but still only one additive
      character.

  STILL ADMISSIBLE:
    - a carrier-native valuation/uniformizer axis produced by the actual
      square carrier together with two independent endpoint degree maps;
    - a carrier-native boundary/properness/self-duality map killing [c] while
      preserving endpoint data, projection, Rosati, and control death;
    - a proof that no such carrier-native valuation/boundary extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the rank-one degree-character shortcut. It does not close a
future carrier where the square itself constructs valuation data and the two
endpoint degree maps as separate carrier-native maps.

## 5. Kill conditions

```text
KILL-VDC.1 valuation character promoted to both degree maps
  A proposal says the full integer valuation is enough because it kills c
  and remembers m. Kill it unless it constructs two independent endpoint
  degree maps inside the square carrier.

KILL-VDC.2 total degree confused with endpoint data
  Total degree or any rank-one additive character loses endpoint direction.
  SCC.3 requires d1 and d2, not only a scalar function of them.

KILL-VDC.3 diagonal intersection confused with correspondence data
  Matching the diagonal intersection does not recover left/right fiber
  probes, proper endpoints, or composition.

KILL-VDC.4 Laurent valuation line read as rep_NS
  The Laurent valuation axis is boundary data. It is not an integral
  Neron-Severi correspondence lattice with diagonal, graph, and projection.

KILL-VDC.5 control formability ignored
  A single integer degree character can be declared on controls. If the
  move exists before carrier formation, DH/Epstein have not died.

KILL-VDC.6 SCC slots bypassed
  Valuation degree without the square, integral rep_NS, two degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, carrier boundary, and control death is not
  End(S^2/Z).
```
