# 318 - Qbar_BECD boundary fiber anchor contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eighty-first cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 317 fixed the component-order target:

```text
D1 is the p1 boundary component,
D2 is the p2 boundary component.
```

This document sharpens "is." The components cannot be just named or
endpoint-anchored labels. They must be actual Cartier boundary fibers of the
primary endpoint maps inside the carrier boundary:

```text
D1 = actual p1 boundary fiber inside dQ,
D2 = actual p2 boundary fiber inside dQ.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_fiber_anchor_contract`
(BFA1-BFA10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_component_anchor_contract`,
`prime_int_n1b_qbar_becd_boundary_twist_pinning_contract`,
`prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve`,
`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go`,
`prime_int_n1b_oriented_endpoint_difference_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The previous anchors narrowed live B to an endpoint-anchored oriented-Cartier
normal ratio. There is still a possible shortcut:

```text
name two components D1,D2 and declare them anchored to p1,p2.
```

That is not yet a carrier construction. The endpoint maps must produce the
components as boundary fibers, and the localization sequence must restrict to
those fibers. Otherwise the normal ratio is still a label-level
trivialization.

The live object must therefore provide:

```text
actual p1 boundary fiber,
actual p2 boundary fiber,
Cartier normal lines for both fibers,
both fibers inside dQ,
endpoint order fixing orientation,
exact localization restricted to the ordered normal ratio,
unique twist with boundary c.
```

## 2. Lemma

```text
Lemma 318.1 (boundary fiber anchor contract).

On the current O+E line:

    carrier_object, endpoint_maps

are represented. Product boundary shape still represents only those slots.
It does not supply actual endpoint boundary fibers.

The endpoint order matters at representative level. In truncations
L=6,8,10,12:

    [c] != 0,
    res_1(c)=1,
    c != c^-1 as representatives.

Thus swapping the p1 and p2 boundary fibers changes the DD.4 representative.

Component labels are not enough. A label may say "D1 belongs to p1" and
"D2 belongs to p2", but without actual p_i boundary fibers it supplies no
Cartier normal fiber, no boundary-fiber inclusion in dQ, and no restricted
localization.

Product endpoint fibers are not enough by shape alone. Product geometry may
name endpoint fibers, but live B also needs Cartier normality, the ordered
normal ratio from those fibers, exact localization, unique twist, and
boundary c.

Declared localization is not enough. A proposal must prove the actual
localization sequence restricts to the endpoint boundary fibers.

Endpoint-coordinate decoders are not endpoint boundary fibers. Boundary
difference has rank one; primary endpoint fibers have rank two; total plus
difference is a decoder, not a boundary-fiber construction.

The accepted boundary-fiber anchor is exactly:

    carrier-native,
    p1,p2 primary,
    actual p1 boundary fiber,
    actual p2 boundary fiber,
    Cartier boundary fibers,
    fibers inside dQ,
    endpoint order fixes orientation,
    normal ratio from the fibers,
    exact localization restricts to the fibers,
    unique twist,
    boundary is c,
    endpoint rank preserved,
    not product shape only,
    not component labels,
    not coordinate decoding,
    not declared localization,
    not formable on controls.

If this is constructed, live B is represented on O+E. After that, only
formation-level control death remains in Phase A.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_FIBER_ANCHOR__P1P2_ACTUAL_CARTIER_FIBERS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_fiber_anchor_contract` verifies ten gates.

BFA1 checks slot accounting: `O+E` and product boundary shape still represent
only `carrier_object, endpoint_maps`; actual endpoint boundary fibers plus
the B atoms represent `DD.4_boundary_killing`.

BFA2 checks representative-level endpoint order: `c` and `c^-1` remain
distinct representatives, and `res_1(c)=1`.

BFA3 rejects component labels as actual endpoint boundary fibers.

BFA4 rejects product endpoint fibers without actual Cartier and localization
data.

BFA5 rejects declared localization. Exactness must restrict to the endpoint
boundary fibers.

BFA6 rejects endpoint-coordinate decoders as boundary-fiber construction.

BFA7 records that direction selection alone is not endpoint-fiber
construction.

BFA8 records control survival for endpoint-fiber-looking product packages.

BFA9 records the live predicate. Only actual `p1,p2` boundary-fiber data
passes.

BFA10 checks that actual endpoint boundary fibers complete live B and leave
only control death.

## 4. Impact on R1

```text
R1 after docs 138-318:
  NEWLY FIXED THIS CYCLE:
    - D1,D2 must be actual Cartier boundary fibers of p1,p2 inside dQ, not
      endpoint-anchored component labels.

  CURRENT LIVE TARGET:
    - construct actual p1 and p2 boundary fibers inside dQ;
    - prove these fibers are Cartier and carry normal lines;
    - prove exact localization restricts to them;
    - form their ordered normal ratio;
    - prove the ratio gives the unique twist with boundary c;
    - preserve primary p1,p2 and endpoint rank;
    - prove non-formability on controls.

  DISCIPLINE:
    - component labels, product shape, declared localization,
      total/difference decoders, and direction selection are diagnostics only.

  STILL OPEN:
    - construct the endpoint boundary fibers in Qbar_BECD;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BFA.1  p1 and p2 produce actual boundary fibers inside dQ.
ACCEPT-BFA.2  Those fibers are Cartier boundary components with normal lines.
ACCEPT-BFA.3  Exact localization restricts to those endpoint boundary fibers.
ACCEPT-BFA.4  The endpoint order fixes the orientation/sign.
ACCEPT-BFA.5  The ordered normal ratio of those fibers produces the unique
              twist with boundary c.
ACCEPT-BFA.6  p1,p2 remain primary and endpoint rank is preserved.
ACCEPT-BFA.7  Controls cannot form the endpoint boundary-fiber package.

KILL-BFA.1    Reject component labels as endpoint boundary fibers.
KILL-BFA.2    Reject product boundary shape without actual Cartier fiber and
              localization evidence.
KILL-BFA.3    Reject declared localization or declared DD.4 death.
KILL-BFA.4    Reject endpoint-coordinate decoders as boundary-fiber
              construction.
KILL-BFA.5    Reject direction selection alone as endpoint-fiber evidence.
KILL-BFA.6    Reject endpoint-fiber-looking packages formable on controls.
```
