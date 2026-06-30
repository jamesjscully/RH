# 313 - Qbar_BECD oriented-Cartier residual sieve

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-sixth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 312 fixed the live local shape:

```text
oriented Cartier boundary on O+E.
```

This document separates that local shape from the residual carrier proofs. The
endpoint-orientation bank shows that total degree, imported difference sign,
parity sublattices, and parity tags are not the missing carrier theorem.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_oriented_cartier_residual_sieve`
(OCR1-OCR7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract`,
`prime_int_n1b_endpoint_swap_boundary_no_go`,
`prime_int_n1b_oriented_endpoint_difference_no_go`,
`prime_int_n1b_endpoint_parity_saturation_no_go`,
`prime_int_n1b_endpoint_parity_tag_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The oriented-Cartier boundary shape supplies the local splitter and the
direction:

```text
M + L + Z + unique DD.4 direction.
```

It still does not supply live `B` until the carrier proves:

```text
carrier-fixed orientation,
self-dual boundary/properness,
p1,p2 remain primary endpoint maps,
non-formability on controls.
```

Docs 272-275 explain why the missing proof is not endpoint-coordinate
bookkeeping. Total degree is rank one. Difference direction imports a sign.
Parity sublattices restate endpoint integrality. Tags diagnose but do not
construct integral endpoint maps.

## 2. Lemma

```text
Lemma 313.1 (oriented-Cartier residual sieve).

Start from:

    O+E = carrier_object + endpoint_maps.

Shape-only oriented Cartier data gives:

    boundary-map shape,
    exact-localization shape,
    DD.4 zero-image shape,
    unique direction d1-d2.

But without self-dual boundary/properness it still does not represent:

    DD.4_boundary_killing.

Adding self-dual boundary/properness produces:

    carrier_object, endpoint_maps, DD.4_boundary_killing.

The endpoint-orientation repairs do not replace this carrier proof:

    total direction:
      (10,1) and (7,4) share total 11 but have different endpoints;

    imported difference sign:
      c and c^-1 are cohomologous but different representatives, and
      (10,1) and (11,2) share difference 9 but have different endpoints;

    parity sublattice:
      (11,9) and (11,3) decode integrally, but (11,8), (0,1), and (10,1)
      decode half-integrally;

    parity tag:
      tag zero diagnoses the same-parity lattice, while tag-one labels such
      as (0,1), (11,8), and (10,1) remain non-endpoints and can still contain
      a=1 split labels.

Therefore the residual construction order is:

    1. prove carrier-fixed orientation;
    2. prove self-dual boundary/properness;
    3. keep p1,p2 as primary endpoint maps, not decoded labels;
    4. prove non-formability on controls.

After the first two are proved, the represented Phase-A slots are:

    carrier_object, endpoint_maps, DD.4_boundary_killing.

After control non-formability is proved, Phase A is complete.
```

Verdict label:

```text
N1B_QBAR_BECD_ORIENTED_CARTIER_RESIDUAL__ORIENTATION_SELF_DUAL_THEN_CONTROL__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_oriented_cartier_residual_sieve` verifies seven
gates.

OCR1 checks slot accounting. `O+E` and shape-only oriented Cartier data both
represent only `carrier_object, endpoint_maps`; adding self-dual boundary
data yields `DD.4_boundary_killing`.

OCR2 rejects total direction as endpoint-primary data.

OCR3 rejects imported orientation sign as mere notation: `c` and `c^-1`
differ as representatives, and same-difference endpoint pairs still differ.

OCR4 rejects parity sublattice selection as construction: it separates
integral labels from half-integral labels but does not produce the carrier.

OCR5 rejects parity tags as construction: the tag diagnoses integrality but
does not produce the endpoint maps.

OCR6 records the residual obligation order:

```text
shape -> carrier-fixed orientation -> self-dual properness
      -> control non-formability.
```

OCR7 checks that once live B exists, adding formation-level control death
completes Phase A.

## 4. Impact on R1

```text
R1 after docs 138-313:
  NEWLY FIXED THIS CYCLE:
    - the next proof is not another endpoint-coordinate repair.

  CURRENT LIVE TARGET:
    - carrier-fixed orientation plus self-dual boundary/properness for the
      oriented-Cartier boundary on O+E.

  DISCIPLINE:
    - p1,p2 stay primary;
    - total/difference/parity/tag data may be diagnostics only.

  STILL OPEN:
    - prove the carrier fixes the orientation/sign;
    - prove self-dual boundary/properness;
    - prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-OCR.1  Carrier geometry fixes the orientation/sign of the DD.4
              representative.
ACCEPT-OCR.2  Carrier geometry proves self-dual boundary/properness.
ACCEPT-OCR.3  p1,p2 remain represented primary maps.
ACCEPT-OCR.4  Control non-formability is proved at carrier formation.

KILL-OCR.1    Reject total degree as endpoint maps.
KILL-OCR.2    Reject imported sign action as carrier orientation.
KILL-OCR.3    Reject same-parity sublattice selection as construction.
KILL-OCR.4    Reject parity tag as integral endpoint construction.
KILL-OCR.5    Reject shape-only oriented Cartier data as live B.
```
