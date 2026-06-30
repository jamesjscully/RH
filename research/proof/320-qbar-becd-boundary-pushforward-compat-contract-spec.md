# 320 - Qbar_BECD boundary pushforward compatibility contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eighty-third cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 319 fixed the exactness target:

```text
one carrier localization sequence on dQ
restricts to the actual p1,p2 boundary fibers
sends the original DD.4 representative c to zero
```

This document sharpens the interface with the endpoint maps. The restricted
localization cannot be a detached boundary null-homotopy. It must commute
with the primary endpoint proper pushforwards `p1_*` and `p2_*` in the same
carrier that supplies the endpoint degree maps. Symbolic composition, formal
adjoint/Rosati packages, declared Beck-Chevalley squares, projection
quotients, local degree retunings, and control-formable lookalikes do not
count.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`
(BPC1-BPC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract`,
`prime_int_n1b_qbar_becd_boundary_fiber_anchor_contract`,
`prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve`,
`prime_int_n1b_formal_correspondence_composition_no_go`,
`prime_int_n1b_formal_adjoint_projection_no_go`,
`prime_int_n1b_projection_formula_quotient_no_go`,
`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 319 the live boundary target could still split in the wrong way:

```text
boundary localization kills c,
but the killing does not commute with p1_*,p2_*.
```

That is not the square. It produces a boundary exactness story parallel to
the endpoint maps instead of a boundary exactness theorem inside the same
compactified carrier. The next admissible object must prove:

```text
restricted localization on dQ,
actual p1 and p2 boundary fibers,
commuting squares with p1_* and p2_*,
endpoint degree maps preserved,
finite-field count and graph-degree anchors preserved,
same carrier for boundary and endpoint data.
```

## 2. Lemma

```text
Lemma 320.1 (boundary localization must commute with endpoint pushforward).

The DD.4 class c remains the original nonzero class:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

The doc-319 restricted localization data represents:

    carrier_object,
    endpoint_maps,
    dd4_boundary_killing.

It does not yet represent:

    boundary_endpoint_pushforward_compat.

The accepted compatibility datum is exactly:

    carrier-native,
    p1,p2 primary,
    actual p1 boundary fiber,
    actual p2 boundary fiber,
    Cartier boundary fibers,
    one localization on dQ,
    restricts to p1 fiber,
    restricts to p2 fiber,
    common sequence for the ordered normal ratio,
    connecting map sends c to zero,
    c remains the original DD.4 class,
    normal ratio is the boundary,
    self-dual properness,
    endpoint rank preserved,
    actual p1_* pushforward,
    actual p2_* pushforward,
    boundary localization commutes with p1_*,
    boundary localization commutes with p2_*,
    endpoint degree maps remain primary,
    p1 degree preserved,
    p2 degree preserved,
    finite-field count anchor preserved,
    graph-degree anchor preserved,
    same carrier as the endpoint maps,
    no symbolic composition substitute,
    no formal adjoint substitute,
    no projection quotient or retuning,
    no declared pushforward square,
    no detached boundary exactness,
    not formable on controls.

If this is constructed, the boundary and endpoint sides of Phase A are tied
in the same carrier. Formation-level control death still remains.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_PUSHFORWARD_COMPAT__RESTRICTED_DQ_LOCALIZATION_COMMUTES_WITH_ENDPOINTS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract` verifies ten
gates.

BPC1 recomputes the original DD.4 class. The class is still the one pushed
through the boundary square.

BPC2 checks slot accounting. Doc-319 localization ties object, endpoints, and
DD.4 boundary killing, but not yet endpoint pushforward compatibility.

BPC3 rejects detached boundary exactness: killing `c` outside the actual
`p1_*`,`p2_*` pushforward squares is not the compactified square.

BPC4 rejects symbolic composition as pushforward commutation.

BPC5 rejects formal adjoint or Rosati data as a replacement for endpoint
pushforwards and primary degree maps.

BPC6 imports the projection-formula quotient diagnostic: on the genuine
`q=7`, trace-one finite-field anchor, quotient/retuning changes the
`F_{q^2}` count from `63` to `36` or retunes the graph degree to `-20`.

BPC7 rejects declared Beck-Chevalley squares without constructed
commutation.

BPC8 rejects pushforward-compatible-looking control packages.

BPC9 requires endpoint rank, both endpoint degrees, the finite-field count
anchor, and the graph-degree anchor to survive.

BPC10 records the live predicate. Only carrier boundary-localization
pushforward compatibility passes, and it still leaves formation-level control
death as the next target.

## 4. Impact on R1

```text
R1 after docs 138-320:
  NEWLY FIXED THIS CYCLE:
    - restricted dQ localization must commute with the actual p1_* and p2_*
      endpoint proper pushforwards in the same carrier.

  CURRENT LIVE TARGET:
    - construct the carrier localization sequence on dQ;
    - prove it restricts to the actual p1 and p2 boundary fibers;
    - prove the common restricted sequence gives the ordered normal ratio;
    - prove its connecting map sends the original representative c to zero;
    - prove the restricted boundary maps commute with p1_* and p2_*;
    - preserve endpoint rank, p1/p2 degree maps, finite-field counts, and
      graph-degree anchors;
    - keep self-dual properness and p1,p2 primary;
    - prove non-formability on controls.

  DISCIPLINE:
    - detached boundary exactness, symbolic composition, formal adjoints,
      declared Beck-Chevalley squares, projection quotients, and local
      retunings are diagnostics only.

  STILL OPEN:
    - construct the pushforward-compatible restricted dQ localization
      sequence in Qbar_BECD;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BPC.1  The carrier supplies one exact localization sequence on dQ.
ACCEPT-BPC.2  That sequence restricts to the actual p1 and p2 boundary fibers.
ACCEPT-BPC.3  The same sequence gives the ordered normal ratio.
ACCEPT-BPC.4  The connecting map sends the original representative c to zero.
ACCEPT-BPC.5  The restricted boundary square commutes with p1_*.
ACCEPT-BPC.6  The restricted boundary square commutes with p2_*.
ACCEPT-BPC.7  Endpoint rank, p1/p2 degree maps, finite-field count anchors,
              and graph-degree anchors are preserved.
ACCEPT-BPC.8  The boundary and endpoint data are supplied by the same carrier.
ACCEPT-BPC.9  Controls cannot form the pushforward-compatible package.

KILL-BPC.1    Reject boundary exactness detached from p1_* and p2_*.
KILL-BPC.2    Reject symbolic composition as endpoint pushforward
              commutation.
KILL-BPC.3    Reject formal adjoint/Rosati data as endpoint pushforward
              commutation.
KILL-BPC.4    Reject declared Beck-Chevalley squares.
KILL-BPC.5    Reject projection-formula quotient or local degree retuning.
KILL-BPC.6    Reject packages that change endpoint rank, degree maps,
              finite-field counts, or graph degrees.
KILL-BPC.7    Reject packages formable on controls.
```
