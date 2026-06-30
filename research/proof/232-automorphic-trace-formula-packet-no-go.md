# 232 - Automorphic trace-formula packets do not construct the square

Status: no-go + automorphic/trace-formula/Langlands-packet boundary,
2026-06-20. Ninety-fifth cycle of the doc-137 construction arc. Doc 231
killed adelic restricted-product/all-place assembly as square construction.
This document tests the next repair: enrich the all-place package with
automorphic spectral data, Hecke action, Satake parameters, Euler product,
functional equation, trace formula, and Rankin-Selberg edge data, then
promote that packet to the missing global square carrier.

```text
adelic restricted product
  -> automorphic / Hecke / Satake / trace-formula packet
  -> global square correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_automorphic_trace_formula_packet_no_go` (ATF1-ATF7 ALL
PASS) -- identical automorphic packet profiles do not determine finite-field
count anchors; Hecke/Satake data does not construct NS degree slots; scalar
trace-formula data is not carrier-native graph composition; Rankin-Selberg
edge data does not impose radius split or Rosati; finite trace-formula
windows admit ghost summands; the same formal packet schema is formable on
controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_adelic_restricted_product_assembly_no_go` (ARP1-ARP7 ALL
PASS) and `cw_radius_assembly` (exit 0).

## 1. Purpose

Docs 230-231 say local p-adic packages and their adelic restricted product
are downstream bookkeeping unless the global square has already been built.
The obvious research-grade repair is:

```text
do not stop at local products;
add Hecke operators, Satake parameters, automorphic representation data,
trace formula, and Rankin-Selberg edge/pole structure;
use the automorphic packet as the square.
```

This is still not construction of `End(S^2/Z)`. Automorphic packets can
organize scalar spectral data, Euler factors, trace identities, and global
reciprocity constraints. They do not by themselves construct the over-`Z`
square, `rep_NS`, carrier-native degree maps, proper correspondence
category, fiber-product composition, Frobenius graph, projection formula, or
positive Rosati relation.

This document rejects only the shortcut:

```text
an automorphic / Langlands / trace-formula packet constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category first constructs the geometric side and whose automorphic or trace
formula is then a theorem about that carrier.

## 2. Lemma

```text
Lemma 232.1 (Automorphic packets are not square carriers).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy automorphic packet profile:

    rank                = 2,
    Hecke action         = present,
    Satake parameters    = present,
    Euler product        = present,
    functional equation  = present,
    trace formula        = present,
    Rankin-Selberg edge  = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract automorphic packet profile does not determine the
finite-field count anchor.

Nor does Hecke/Satake data construct the NS degree slots. Keeping the same
packet profile and z-action while changing the formal triple from (7,F,1)
to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A scalar trace formula at one test function is not graph composition. A
trace-zero perturbation can preserve the first scalar trace and first count

    #1 = 7,

while changing the second count

    #2: 63 -> 61.

The missing datum is the carrier-native Frobenius graph and its composition
law, not another scalar trace identity.

Rankin-Selberg/product edge data also does not force the individual radius
split or Rosati compatibility. With q=9, the moduli

    e^0.4 * 3, e^-0.4 * 3, e^-0.4 * 3, e^0.4 * 3

have pair-products 9 and determinant 81, but they are not all equal to 3.
Separately, the off-circle integral q-similitude control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Finite trace-formula windows remain unsafe. A 5-cycle ghost summand
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal spectral-packet schema is formable on arbitrary control
companion data with no actual automorphic realization, rep_NS, square
carrier, proper correspondences, or positive Rosati.

Consequently an automorphic/trace-formula packet constructs no automorphic
moduli carrier, geometric trace-formula side, rep_NS, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_AUTOMORPHIC_TRACE_FORMULA_PACKET__SPECTRAL_PACKET_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_automorphic_trace_formula_packet_no_go` verifies the seven
gates.

ATF1 records profile non-determination. The q=7 and q=5 anchors have the
same abstract automorphic packet profile but different count windows.

ATF2 records the NS-degree-slot failure. With the same packet profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

ATF3 records scalar trace versus graph-law separation. The first trace and
first count can agree while the second count changes from `63` to `61`,
because no carrier-native Frobenius graph or composition law has been built.

ATF4 records Rankin-Selberg edge versus Rosati separation. Balanced local
radius redistribution preserves pair-products and determinant while breaking
the individual even split, and an off-circle q-similitude still has positive
metric defect `5.916`. The missing datum is global carrier-native Rosati,
not another edge identity.

ATF5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

ATF6 records control formability. A control companion with the same formal
packet schema has count window `8,112,1064` and metric defect `9.950`, with
no actual automorphic realization, `rep_NS`, square, proper correspondences,
or Rosati input.

ATF7 records the construction failure: no automorphic moduli carrier,
geometric trace-formula side, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-232:
  NEWLY CLOSED THIS CYCLE:
    - automorphic packet as global square carrier, Hecke/Satake data as
      rep_NS construction, scalar trace formula as Frobenius graph law,
      Rankin-Selberg edge as degree/Rosati construction, finite
      trace-formula windows as carrier determination, and formal
      automorphic schemas as DH/Epstein carrier guards (doc 232).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper correspondence
      category constructs the geometric side before any trace formula is
      invoked;
    - a Langlands or trace-formula theorem downstream of an actual
      square carrier with degree maps, correspondences, projection formula,
      Frobenius graph, and Rosati;
    - a theorem excluding ghost spectral summands from the actual carrier;
    - controls killed at carrier formation, not after spectral packaging.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the automorphic-packet shortcut:
spectral/Hecke/trace-formula data is not construction of the global square
carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-ATF.1 automorphic packet as square construction
  A proposal supplies automorphic, Langlands, or trace-formula data and calls
  it the square. Kill it unless the global over-Z square carrier was already
  constructed carrier-natively.

KILL-ATF.2 Hecke/Satake data as rep_NS
  A proposal treats Hecke eigenvalues, Satake parameters, or an L-packet as
  the NS triple. Kill it unless the degree slots, off-diagonal
  intersections, and projection formula are constructed.

KILL-ATF.3 scalar trace formula as graph law
  A proposal reads the Frobenius graph from scalar trace identities. Kill it
  unless graph composition and proper correspondences are constructed by the
  carrier.

KILL-ATF.4 Rankin-Selberg edge as Rosati
  A proposal reads positive Rosati from the Rankin-Selberg edge, pole, or
  determinant product. Kill it unless Frobenius/Rosati compatibility is
  constructed globally.

KILL-ATF.5 finite trace-formula window
  A proposal verifies finitely many spectral or trace-formula identities.
  Kill it unless ghost spectral summands are excluded carrier-natively.

KILL-ATF.6 control survival
  A proposal's spectral packet schema can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
