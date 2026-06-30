# 290 - CC product rep_NS graft is not the square carrier

Status: no-go + CC-product-repNS-graft deletion, 2026-06-22.
One-hundred-fifty-third cycle of the doc-137 construction arc. Doc 289
killed the product boundary+endpoint bundle as a full carrier. This document
tests the next repair:

```text
graft curve Pic data or the finite-field NS triple model onto the
CC product boundary/endpoints as the square rep_NS.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_repns_graft_no_go` (CRG1-CRG8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_cc_pic_jacobian_square_no_go`,
`prime_int_n1b_positive_rosati_end_envelope_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 289 retained a positive point: product boundary and `p1,p2` are the
right geometric shape. The next repair is to add the visible finite-field
square model:

```text
rep_NS triples (d1,z,d2), diagonal, Frobenius graph, and intersection form.
```

This is also the right target. The no-go is that grafting that model onto
the product is not the same as constructing square cycle theory. Even if the
visible anchors are granted, the carrier still needs proper pullback
composition, projection formula, DD.4 boundary localization, carrier Rosati,
primitive sign, and control death.

## 2. Lemma

```text
Lemma 290.1 (rep_NS grafting is not represented square cycle theory).

The CC product boundary-endpoint evidence currently represents:

    carrier_object, endpoint_maps.

Grafting finite-field or curve-level `rep_NS` data by labels is rejected by
the represented-carrier gate. The represented slots remain:

    carrier_object, endpoint_maps.

If one grants actual `rep_NS`, diagonal, and Frobenius graph tokens, the
finite-field visible anchors are correct:

    Delta.Gamma_n = #C(F_{q^n}) for n=1,2,3,
    Gamma_1 o Gamma_2 = Gamma_3.

But the represented slots are still only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

They do not include proper composition, projection formula, DD.4 boundary
killing, Rosati duality, primitive positive sign, or control death.

The componentwise graph law is not the carrier projection theorem. In the
q=7, Tr(F)=1 anchor, the primitive sign is negative, but the semantic
projection defect remains 27.

Curve Pic tensor product is rank one, while the visible square NS model has
two endpoint slots plus the End component; in the genus-one finite-field
model this visible rank is 6. Curve Pic data is not the square NS triple.

The DD.4 obstruction remains nonzero in truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

The same rep_NS graft remains formable on positive controls: the q=3 control
has negative primitive sign and semantic projection defect 11, with no
formation-level control death.

Even after adding the represented blocker bundle from doc 289, the product
rep_NS graft still lacks:

    proper_composition, projection_formula, Rosati_duality,
    primitive_positive_sign.

Consequently a CC product rep_NS graft is not the square carrier and not
`End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_REPNS_GRAFT__VISIBLE_NS_MODEL_NOT_REPRESENTED_SQUARE_CYCLES__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_repns_graft_no_go` verifies eight gates.

CRG1 checks that product boundary endpoints still lack square `rep_NS`.

CRG2 checks that grafted finite-field/curve `rep_NS` labels are rejected as
unrepresented.

CRG3 grants actual `rep_NS`, diagonal, and graph tokens and confirms the
finite-field count anchors and graph law. This fills visible model slots but
not proper composition or projection.

CRG4 checks the projection defect: the primitive sign is negative, but the
semantic projection defect is 27.

CRG5 compares curve Pic tensor rank 1 with the endpoint+End visible square
rank 6.

CRG6 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

CRG7 checks control survival: the q=3 positive control admits the same
visible graft and has projection defect 11.

CRG8 adds the represented blocker bundle and records the remaining missing
slots: proper composition, projection formula, Rosati duality, and primitive
positive sign.

## 4. Impact on R1

```text
R1 after docs 138-290:
  NEWLY CLOSED THIS CYCLE:
    - finite-field NS triple graft as represented square cycle theory;
    - curve Pic tensor product as square rep_NS;
    - diagonal/graph labels grafted onto product endpoints as proper
      correspondence composition;
    - visible count anchors as projection/Rosati/DD.4/control-death proof.

  POSITIVE INFORMATION RETAINED:
    - the finite-field NS triple remains the correct visible target;
    - product boundary and p1,p2 remain useful shape data;
    - a surviving CC/product route must now construct actual square cycles,
      proper pullbacks, projection formula, and carrier Rosati, not graft
      their finite-field shadows.

  STILL ADMISSIBLE:
    - a CC-derived square cycle theory whose rep_NS, diagonal, Frobenius
      graph, pullbacks, projection formula, Rosati, DD.4 boundary, and
      control death are represented by the product carrier.

  STILL OPEN:
    - construct proper square correspondences and projection/Rosati on top
      of represented product boundary/endpoints.
```

## 5. Kill Conditions

```text
KILL-CRG.1 finite-field rep_NS graft
  Kill pasted finite-field triples unless the product carrier constructs the
  cycle lattice and representability functor.

KILL-CRG.2 curve Pic as square NS
  Curve Pic tensor product is rank one; kill promotion to endpoint+End
  square NS unless the square cycle group is constructed.

KILL-CRG.3 graph law as proper composition
  Componentwise Gamma_m Gamma_n=Gamma_{m+n} is not proper pullback
  composition.

KILL-CRG.4 count anchors as projection formula
  Count anchors do not prove projection; semantic projection defect remains
  unless proper push-pull is constructed.

KILL-CRG.5 visible positivity as carrier Rosati
  Primitive sign in the finite-field model is not carrier Rosati unless the
  product supplies the duality/evaluation theorem.

KILL-CRG.6 rep_NS graft on controls
  If the same visible graft is formable on positive controls, formation-level
  control death has failed.
```
