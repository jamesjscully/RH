# 312 - Qbar_BECD oriented Cartier boundary contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-fifth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 311 reduced the live Phase-A boundary target to a carrier-native
self-dual boundary source on `O+E`. The strongest positive banked pieces are:

```text
Cartier normal line        gives the Hilbert-90 normal splitter;
oriented boundary complex  selects the DD.4 direction d1-d2.
```

This document records the combined live contract:

```text
oriented Cartier boundary on O+E.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract`
(OCB1-OCB7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_source_matrix`,
`prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve`,
`prime_int_n1b_cartier_boundary_normal_no_go`,
`prime_int_n1b_oriented_boundary_complex_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

Doc 277 retained one positive fact:

```text
a Cartier normal coordinate t with sigma(t)=t*c gives boundary c.
```

Doc 278 retained another positive fact:

```text
the oriented two-component boundary complex selects ell=d1-d2.
```

Doc 311 says the live B source must supply map, exact localization, zero
image, self-dual properness, carrier-nativity, unique direction, endpoint-rank
preservation, and non-formability on controls. The combined oriented Cartier
boundary is the first local shape matching the positive pieces of that list.

It is not yet `B`. It becomes live `B` only if the carrier proves the remaining
structure.

## 2. Lemma

```text
Lemma 312.1 (oriented Cartier boundary contract).

Start from the endpoint-fixed line:

    O+E = actual Qbar/Q/dQ plus p1,p2 and proper pushforward.

An oriented Cartier normal-crossing boundary with incidence d1-d2 supplies:

    M: actual boundary-map shape,
    L: exact-localization shape,
    Z: DD.4 class mapped to zero,
    unique DD.4 direction.

In truncations L=6,8,10,12, the base class remains nonzero:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

But the oriented Cartier normal action with incidence (1,-1) splits the class:

    sigma(v,u) = (v, c^(d1-d2)(v) phi(u)),
    boundary(sigma((1,0),1)) = c.

Orientation is carrier data. Reversing orientation changes the representative
from c to c^-1. These are cohomologous in the Z/2 class, but they are not the
same representative.

Endpoint rank is preserved only if the actual p1,p2 maps remain primary. The
boundary difference alone has rank one. Total plus difference has determinant
-2 and requires parity/half-sum integrality. Therefore the boundary incidence
must be auxiliary to actual p1,p2, not a replacement decoder.

Shape-only oriented Cartier data is still not live B. The carrier must also
prove:

    orientation fixed by the carrier,
    carrier-native source on O+E,
    self-dual boundary/properness,
    endpoint-rank preservation through actual p1,p2,
    non-formability on controls.

If these are proved, the represented Phase-A slots become:

    carrier_object, endpoint_maps, DD.4_boundary_killing,

and the only remaining Phase-A slot is:

    control_death.
```

Verdict label:

```text
N1B_QBAR_BECD_ORIENTED_CARTIER_BOUNDARY__LIVE_B_CONTRACT_ON_OE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract` verifies seven
gates.

OCB1 checks the start line: `O+E` gives exactly `carrier_object` and
`endpoint_maps`.

OCB2 recomputes the base DD.4 obstruction and checks that oriented Cartier
normal data with incidence `(1,-1)` splits `c` for L=6,8,10,12.

OCB3 checks the orientation-sign issue: `c` and `c^-1` are cohomologous but
not equal as representatives.

OCB4 checks that orientation selects one primitive direction from the
16-direction normal-crossing family in the tested window.

OCB5 checks endpoint-rank discipline: boundary difference alone has rank one;
actual `p1,p2` plus boundary difference has rank two; total/difference
decoding has half-sum defects.

OCB6 separates shape-only data from live B. The missing obligations are
carrier-fixed orientation, carrier-native source, self-dual properness, and
control non-formability.

OCB7 checks that live oriented Cartier B would leave exactly formation-level
control death.

## 4. Impact on R1

```text
R1 after docs 138-312:
  NEWLY FIXED THIS CYCLE:
    - the live B source has a concrete local shape:
      oriented Cartier boundary on O+E.

  CURRENT LIVE CONTRACT:
    - combine the Cartier normal splitter with oriented boundary incidence;
    - keep p1,p2 as primary endpoint maps;
    - prove carrier-fixed orientation, carrier-nativity, self-dual
      properness, and control non-formability.

  STILL OPEN:
    - construct this oriented Cartier boundary as carrier-native data on
      Qbar_BECD;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-OCB.1  The boundary must be an oriented Cartier normal-crossing source
              on O+E.
ACCEPT-OCB.2  The carrier must fix the orientation/sign of c.
ACCEPT-OCB.3  The boundary incidence must be auxiliary to actual p1,p2, not a
              total/difference endpoint decoder.
ACCEPT-OCB.4  Self-dual boundary/properness must be proved by the carrier.
ACCEPT-OCB.5  The boundary source must not be formable on controls.

KILL-OCB.1    Reject a Cartier normal line without oriented direction
              selection.
KILL-OCB.2    Reject oriented incidence without Cartier normal zero image.
KILL-OCB.3    Reject orientation up to cohomology class only.
KILL-OCB.4    Reject boundary difference as a replacement for p1,p2.
KILL-OCB.5    Reject shape-only boundary data without self-dual properness and
              control non-formability.
```
