# 271 - Endpoint valuation registers are not carrier degree maps

Status: no-go + endpoint-valuation-register deletion, 2026-06-20.
One-hundred-thirty-fourth cycle of the doc-137 construction arc. Docs 269
and 270 killed one additive degree character and one scalar endpoint codec.
This document tests the next repair:

```text
add a rank-two endpoint register Z^2 and twist the valuation cover by a
chosen linear functional ell(d1,d2).
```

Witness, lead-reran this cycle:
`prime_int_n1b_endpoint_valuation_register_no_go` (EVR1-EVR6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_degree_pair_codec_no_go`,
`prime_int_n1b_valuation_degree_character_no_go`,
`prime_int_n1b_formal_ns_envelope_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

This repair is not merely doc 218's formal `Z^2 + Z[F]` envelope. It is the
targeted DD.4/valuation repair after docs 267-270:

```text
keep two endpoint registers and let a chosen valuation direction kill c.
```

The positive fact is real. A `Z^2` register has two coordinate projections.
If one chooses a primitive linear functional

```text
ell(d1,d2)=a d1 + b d2,
```

then the endpoint cover can be twisted by `c^ell`. For any vector `v` with
`ell(v)=1`, the element `sigma(v,1)` has boundary `c=(1+z)^-1`.

The no-go is that the boundary direction is chosen. The `Z^2` register does
not say whether the DD.4 boundary is left degree, right degree, total degree,
difference degree, or another primitive direction. It also does not construct
the square carrier, `rep_NS`, graph degrees, proper correspondence
composition, projection formula, Rosati, or control death.

## 2. Lemma

```text
Lemma 271.1 (rank-two valuation registers choose boundary direction).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For a primitive linear functional ell: Z^2 -> Z, form

    E_ell = Z^2 x U_1,
    sigma(v,u) = (v, c^{ell(v)} phi(u)).

Then sigma^2=id. If ell(v)=1, then

    boundary(sigma(v,1)) = (0,c).

Thus the endpoint register can both declare two integer projections and kill
the named DD.4 representative.

However, the same `Z^2` register admits many incompatible boundary
directions:

    ell=d1, ell=d2, ell=d1+d2, ell=d1-d2, ell=2d1+d2, ...

The register itself does not determine which direction is the carrier
boundary/properness/self-duality map. The Frobenius graph degrees also remain
freely assigned: with the same z-action, endpoint assignments `(7,1)`,
`(10,1)`, `(7,4)`, and `(11,1)` are all available, and `(10,1)` and `(7,4)`
have the same diagonal intersection while different endpoint probes.

The same rank-two register split can be declared on controls. Therefore it
constructs no actual square, integral rep_NS, two carrier-native degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_ENDPOINT_VALUATION_REGISTER__Z2_PROJECTIONS_WITH_CHOSEN_BOUNDARY__NO_GO.
```

## 3. Proof

`prime_int_n1b_endpoint_valuation_register_no_go` verifies six gates.

EVR1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

EVR2 checks the positive endpoint-register split. For `ell=d1`, `ell=d2`,
and `ell=d1+d2`, in truncations `L=6,8,10,12`, the witness verifies:

```text
sigma^2=id,
boundary(sigma(v,1)) = (0,c) for ell(v)=1,
the two coordinate projections remain exact on the tested register window.
```

EVR3 records the choice defect. The same `Z^2` register supports distinct
boundary directions:

```text
d1, d2, d1+d2, d1-d2, 2d1+d2.
```

No carrier data in the register selects one as the DD.4 boundary map.

EVR4 records graph-degree freedom. With the same z-action and trace `1`, the
endpoint assignments

```text
(7,1)->7, (10,1)->10, (7,4)->10, (11,1)->11
```

are all available. The rank-two register supplies labels, not a Frobenius
graph degree theorem.

EVR5 repeats the same rank-two register split on controls in dimensions
`2,4,8`. No square-carrier data is used and controls do not die.

EVR6 applies the SCC contract: the endpoint valuation register supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-271:
  NEWLY CLOSED THIS CYCLE:
    - adjoining a free rank-two endpoint valuation register Z^2 and choosing
      a linear DD.4 boundary direction ell(d1,d2) as if this constructed the
      two SCC degree maps and carrier boundary.

  POSITIVE INFORMATION RETAINED:
    - a Z^2 register can carry two coordinate projections;
    - after choosing ell, the valuation twist c^ell kills the named DD.4
      representative.

  STILL ADMISSIBLE:
    - a square carrier where the two endpoint maps and the DD.4 boundary
      direction are produced by the same properness/self-duality geometry;
    - a carrier-native valuation/uniformizer axis that coexists with endpoint
      degrees and whose boundary direction is not externally chosen;
    - a proof that no such carrier-native endpoint/boundary extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the external endpoint-register shortcut. It does not close a
future carrier where the square itself constructs the endpoint maps and
boundary direction.

## 5. Kill conditions

```text
KILL-EVR.1 free Z^2 endpoint register promoted to degree maps
  A proposal adds endpoint coordinates by hand. Kill it unless the square
  carrier represents them as carrier-native degree maps.

KILL-EVR.2 chosen linear boundary direction
  A proposal chooses ell(d1,d2) so c dies. Kill it unless ell is forced by
  carrier boundary/properness/self-duality.

KILL-EVR.3 endpoint labels promoted to Frobenius graph degrees
  The same z-action admits many endpoint assignments. Kill it unless the
  graph degrees are constructed and tied to composition/counts.

KILL-EVR.4 register split confused with rep_NS
  A rank-two register is not an integral Neron-Severi correspondence lattice,
  intersection theory, projection formula, or Rosati pairing.

KILL-EVR.5 control formability ignored
  The same Z^2 register split can be declared on controls. If the move
  exists before carrier formation, DH/Epstein have not died.

KILL-EVR.6 SCC slots bypassed
  Endpoint valuation registers without the square, integral rep_NS, two
  carrier-native degree maps, diagonal, graph, proper correspondences,
  projection formula, Rosati, carrier boundary, and control death are not
  End(S^2/Z).
```
