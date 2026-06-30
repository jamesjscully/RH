# 289 - CC product boundary-endpoint bundle is not the square carrier

Status: no-go + CC-product-boundary-endpoint-bundle deletion, 2026-06-22.
One-hundred-fifty-second cycle of the doc-137 construction arc. Doc 288
selected the shared boundary+endpoint+control-death bundle as the next
construction target, with Connes-Consani/C x C the best current represented
route only because it has curve-level object evidence. This document tests
the first repair:

```text
promote the curve-level/product boundary and product projections to the
represented square bundle.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go` (CBE1-CBE8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_represented_carrier_candidate_matrix_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_cc_pic_jacobian_square_no_go`,
`prime_int_n1b_cartier_boundary_normal_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 288 identified a concrete next bundle:

```text
actual boundary map + exact localization + DD.4 class mapped to zero
  + self-dual boundary/properness
  + actual p1,p2 and proper pushforward
  + formation-level control death.
```

The strongest immediate Connes-Consani repair is to say that the product
shape already supplies this bundle: take the curve-level compactified object,
form the product, use the two projections as `p1,p2`, and use the product
boundary as the square boundary.

The positive part is real: product projections and product boundary are the
right geometric shape. The no-go is that this shape alone does not represent
the DD.4 killing map, does not build square `rep_NS` or proper
correspondences, and does not make controls fail at formation.

## 2. Lemma

```text
Lemma 289.1 (product boundary-endpoint data is not the represented square).

Under the represented-carrier gate, the current Connes-Consani curve-level
evidence gets only:

    carrier_object.

Granting product projections `p1,p2` and proper pushforward adds:

    endpoint_maps.

Thus the product boundary-endpoint repair currently represents only:

    carrier_object, endpoint_maps.

It does not represent integral rep_NS, diagonal, Frobenius graph, proper
composition, projection formula, DD.4 boundary killing, Rosati, primitive
positive sign, or control death.

The DD.4 obstruction remains nonzero. In truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

A product normal-crossing boundary supplies boundary directions, but does
not select the DD.4 primitive direction. In the tested `[-2,2]^2` window,
there are 16 primitive directions.

Declaring product boundary localization and declaring that DD.4 maps to zero
still does not represent DD.4 killing: without an actual boundary map, exact
localization, the class mapped to zero, and self-dual boundary data, the
represented slot is absent.

Product endpoints do not construct the square `rep_NS`, Frobenius graph, or
projection formula. In the finite-field anchor, the separate count anchor
has `Delta.Gamma_1=7` and negative primitive sign, but the formal semantic
projection defect remains 27.

The same product boundary-endpoint package remains formable on positive
controls: the q=3 control has negative primitive sign and semantic
projection defect 11, while no formation-level control death is represented.

Even granting the full represented blocker bundle is necessary but not
sufficient. It fills only:

    carrier_object, endpoint_maps, DD.4 boundary killing, control_death.

It still lacks integral rep_NS, diagonal, Frobenius graph, proper
composition, projection formula, Rosati duality, and primitive positive
sign.

Consequently CC product boundary-endpoint data is not the square carrier and
not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_BOUNDARY_ENDPOINT_BUNDLE__RIGHT_SHAPE_NOT_REPRESENTED_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go` verifies eight
gates.

CBE1 checks the current CC curve-level evidence under RCG: it represents
only `carrier_object`.

CBE2 grants product projections and proper pushforward: this adds
`endpoint_maps`, but no square bundle.

CBE3 recomputes DD.4 and checks boundary-direction nonselection:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and 16 primitive normal-crossing directions in the tested window.

CBE4 checks that declared boundary localization is not represented DD.4
killing.

CBE5 checks that product endpoints do not construct `rep_NS`, Frobenius
graph, or projection formula. The finite-field anchor exists separately,
while the semantic projection defect remains 27.

CBE6 checks control survival: the q=3 positive control carries the same
product boundary-endpoint package with projection defect 11 and no formation
death.

CBE7 grants the full represented blocker bundle and records that it is still
insufficient without `rep_NS`, proper pullbacks, projection, Rosati, graph
data, and primitive sign.

CBE8 applies RCG: product endpoints, declarations, and the full blocker all
remain below the carrier contract.

## 4. Impact on R1

```text
R1 after docs 138-289:
  NEWLY CLOSED THIS CYCLE:
    - promoting curve-level/product boundary and p1,p2 data to the full
      represented square bundle;
    - product normal crossings as automatic DD.4 direction selection;
    - declared product boundary localization as represented DD.4 killing;
    - product endpoints as square rep_NS/projection/Rosati/graph data;
    - product boundary-endpoint shape as control death.

  POSITIVE INFORMATION RETAINED:
    - product boundary and product projections are the right geometric shape;
    - the next actual construction must keep them, but must add the real
      DD.4 boundary map, rep_NS, proper correspondences, projection, Rosati,
      graph, and control-death proofs.

  STILL ADMISSIBLE:
    - a strengthened Connes-Consani square where product boundary and p1,p2
      are tied to actual square cycles, exact localization killing DD.4,
      proper pullbacks, projection formula, Rosati, and formation-level
      control death.

  STILL OPEN:
    - construct the represented boundary+endpoint+control bundle as part of
      square `rep_NS`, not as product shape alone.
```

## 5. Kill Conditions

```text
KILL-CBE.1 product projections as full carrier
  Product p1,p2 may give endpoint-map shape, but kill promotion to the full
  carrier unless rep_NS, graph, projection, Rosati, DD.4, and control death
  are represented.

KILL-CBE.2 product boundary as DD.4 killing
  Kill product-boundary claims unless the actual boundary map sends the
  DD.4 class to zero through exact localization.

KILL-CBE.3 normal-crossing directions as canonical
  Product normal crossings give many primitive directions. Kill unless the
  carrier selects the DD.4 direction.

KILL-CBE.4 declared localization
  Declared localization and declared class death are not represented
  boundary evidence.

KILL-CBE.5 control guard by product shape
  Product shape does not kill controls. Kill unless controls fail to
  instantiate the bundle at formation.

KILL-CBE.6 necessary bundle as sufficient carrier
  Even a represented boundary+endpoint+control bundle is not the carrier
  until rep_NS, proper pullbacks, projection, Rosati, and graph data are
  constructed.
```
