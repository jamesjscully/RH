# 315 - Qbar_BECD boundary-defect duality contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-eighth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 314 fixed the live Phase-A self-duality interface:

```text
boundary-native self-dual properness for the oriented-Cartier boundary on O+E.
```

This document sharpens the word "self-dual." The live datum is not scalar
evaluation, coevaluation, a full hyperbolic swap, an imposed degree-zero
normalization, or shape-only oriented-Cartier data. It must be the
carrier-produced duality map between the two rank-one boundary defect lines.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_defect_duality_contract`
(BDD1-BDD7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_self_duality_interface`,
`prime_int_n1b_qbar_becd_oriented_cartier_residual_sieve`,
`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract`,
`prime_int_n1b_eval_boundary_glue_no_go`,
`prime_int_n1b_hyperbolic_swap_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

Docs 165 and 166 already explain the type problem. Evaluation is
scalar-valued. Coevaluation is diagonal. A hyperbolic form is a full duality
`W -> W^vee`; turning it into an operator requires matching the primal and
dual halves. None of these is the missing rank-one boundary glue.

Doc 314 says the self-duality must be boundary-native. The sharper contract
is:

```text
dual boundary defect line -> primal boundary defect line,
rank one,
Laurent twist pinned by oriented-Cartier carrier data,
boundary equals the DD.4 representative c,
p1,p2 kept primary,
not formable on controls.
```

This is still a construction-spec target. The object is not constructed here.
The point is to prevent the next pass from spending effort on abstract
duality labels that have the wrong type, rank, twist, or control behavior.

## 2. Lemma

```text
Lemma 315.1 (boundary-defect duality contract).

In the finite support windows N=1,2,4,8, the visible support ranks are:

    3,4,6,10.

The Tate/hyperbolic windows have ranks:

    6,8,12,20.

But the boundary defect that must be glued is rank one in every window:

    1,1,1,1.

Therefore a live Phase-A self-duality cannot be a scalar pairing, a diagonal
class, or a full-support hyperbolic duality. It must produce a map:

    dual boundary defect line -> primal boundary defect line.

The same map must pin the Laurent twist. In Laurent windows |k|<=1,2,4,8,
the unit twists are:

    3,5,9,17,

and the nonzero boundary maps are:

    7,31,511,131071.

Choosing degree zero gives one map only by normalization. It is not carrier
output unless the oriented-Cartier boundary itself pins that twist.

Shape-only OCB data selects the direction d1-d2 and splits the DD.4 class
once chosen, but it still does not make the DD.4 representative the boundary
of a carrier-produced duality map.

The accepted S atom is exactly:

    carrier-native,
    rank-one defect map,
    not scalar-only,
    not diagonal-only,
    not full-support duality,
    no inserted matching,
    twist pinned by oriented-Cartier data,
    no degree-zero fiat,
    orientation fixed,
    DD.4 representative is the boundary of the map,
    p1,p2 primary,
    not formable on controls.

If this atom is constructed on top of O+E and OCB shape, it completes live B.
The remaining Phase-A proof is formation-level control death.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_DEFECT_DUALITY__RANK_ONE_PINNED_TWIST_CONTRACT__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_defect_duality_contract` verifies seven
gates.

BDD1 checks the rank type: support and Tate/hyperbolic windows have ranks
`3,4,6,10` and `6,8,12,20`, while the boundary defect is rank one.

BDD2 rejects evaluation and coevaluation because their outputs are scalar or
diagonal, not a dual-boundary-to-primal-boundary map.

BDD3 rejects hyperbolic swap data because it is full-support duality plus
inserted matching. The matching counts are `6,24,720,3628800`, and the swap
is involutive rather than a Laurent generator.

BDD4 rejects degree-zero normalization. Laurent unit twists and nonzero maps
overproduce unless the carrier pins the twist.

BDD5 records the OCB residual: direction selection and representative
splitting do not yet pin the self-dual twist or make the DD.4 representative
the boundary of the carrier duality map.

BDD6 records the live predicate. Evaluation, hyperbolic swap, degree-zero
normalization, and shape-only OCB all fail; only the boundary-defect duality
contract passes.

BDD7 checks slot accounting. `O+E` plus OCB shape still represents only
`carrier_object, endpoint_maps`; adding the boundary-defect duality contract
represents `DD.4_boundary_killing`; adding control death completes Phase A.

## 4. Impact on R1

```text
R1 after docs 138-315:
  NEWLY FIXED THIS CYCLE:
    - the live S atom is a rank-one boundary-defect duality map with pinned
      twist, not generic self-duality or properness language.

  CURRENT LIVE TARGET:
    - construct the carrier-produced map
          dual boundary defect line -> primal boundary defect line;
    - prove its Laurent twist is pinned by the oriented-Cartier normal data;
    - prove its boundary is the DD.4 representative c, not just the Z/2 class;
    - keep p1,p2 primary and preserve counts;
    - prove the resulting datum is not formable on controls.

  DISCIPLINE:
    - evaluation, coevaluation, hyperbolic swap, inserted matching, and
      degree-zero normalization are diagnostics only.

  STILL OPEN:
    - construct the boundary-defect duality map inside Qbar_BECD;
    - prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BDD.1  The carrier produces a rank-one dual-boundary-to-primal-boundary
              map.
ACCEPT-BDD.2  The Laurent twist is pinned by oriented-Cartier carrier data.
ACCEPT-BDD.3  The boundary of the map is the DD.4 representative c, not only
              its cohomology class.
ACCEPT-BDD.4  The construction fixes orientation/sign.
ACCEPT-BDD.5  p1,p2 remain represented primary endpoint maps.
ACCEPT-BDD.6  The construction is not formable on controls.

KILL-BDD.1    Reject evaluation as boundary self-duality.
KILL-BDD.2    Reject coevaluation as boundary self-duality.
KILL-BDD.3    Reject full hyperbolic duality or swap as rank-one boundary
              defect glue.
KILL-BDD.4    Reject inserted dual-to-primal matching data.
KILL-BDD.5    Reject degree-zero Laurent twist normalization unless the
              carrier pins it.
KILL-BDD.6    Reject shape-only OCB as self-dual properness.
KILL-BDD.7    Reject any duality/properness package still formable on
              controls.
```
