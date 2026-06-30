# 319 - Qbar_BECD boundary fiber localization contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eighty-second cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 318 fixed the endpoint-fiber target:

```text
D1,D2 are actual Cartier boundary fibers of p1,p2 inside dQ.
```

This document sharpens the exactness target. The localization sequence must
be a single carrier sequence on `dQ` that restricts to both endpoint boundary
fibers and maps the original DD.4 representative to zero through their
ordered normal ratio. Formal acyclic replacement, bar/coinduced boundaries,
cone nullhomotopies, jet deletion, obstruction quotient, declared
localization, and separate fiber exact sequences do not count.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract`
(BFL1-BFL10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_fiber_anchor_contract`,
`prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve`,
`prime_int_n1b_coinduced_dd4_extension_no_go`,
`prime_int_n1b_bar_resolution_boundary_no_go`,
`prime_int_n1b_mapping_cone_nullhomotopy_no_go`,
`prime_int_n1b_jet_deletion_no_go`,
`prime_int_n1b_obstruction_quotient_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The live boundary-fiber target still has a dangerous loophole:

```text
declare an exact sequence,
or replace/delete/quotient the coefficient system until c disappears.
```

The banked docs 258-262 already kill those moves. The remaining live route
must prove exactness inside the actual carrier boundary:

```text
one localization sequence on dQ,
restriction to the p1 boundary fiber,
restriction to the p2 boundary fiber,
one common sequence for the ordered normal ratio,
connecting map sends the original representative c to zero,
self-dual properness remains part of the same datum.
```

## 2. Lemma

```text
Lemma 319.1 (boundary fiber localization contract).

The DD.4 class c is still the original class that must be mapped to zero. In
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Endpoint fibers without restricted localization are not live B. O+E plus
fiber shape still represents only:

    carrier_object, endpoint_maps.

Coinduced/bar acyclic replacement is not carrier localization. It kills H^1
by changing the coefficient system, not by restricting the boundary sequence
of dQ to p1 and p2 fibers.

Cone nullhomotopy is not carrier localization. It declares dh=c rather than
producing the endpoint-fiber boundary map.

Jet deletion and obstruction quotient are not carrier localization. They
delete or quotient the obstruction instead of preserving c as the original
class mapped to zero.

Declared localization is not enough. Exactness must actually restrict to the
p1 and p2 boundary fibers.

Separate endpoint-fiber exact sequences are not enough. The ordered normal
ratio needs one common carrier sequence on dQ, not two independent fiber
sequences.

The accepted localization datum is exactly:

    carrier-native,
    p1,p2 primary,
    actual p1 boundary fiber,
    actual p2 boundary fiber,
    Cartier boundary fibers,
    single localization on dQ,
    restricts to p1 fiber,
    restricts to p2 fiber,
    common sequence for the ordered normal ratio,
    connecting map sends c to zero,
    preserves c as the original class,
    normal ratio is the boundary,
    self-dual properness,
    endpoint rank preserved,
    no formal acyclic replacement,
    no formal nullhomotopy,
    no deletion,
    no quotient,
    no declared localization,
    no separate fiber sequences,
    not formable on controls.

If this is constructed, the boundary-fiber datum represents live B. After
that, only formation-level control death remains in Phase A.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_FIBER_LOCALIZATION__RESTRICTED_DQ_EXACTNESS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract` verifies ten
gates.

BFL1 recomputes the original DD.4 class. The target is to map `c` to zero,
not delete or replace it.

BFL2 checks slot accounting: endpoint fibers without restricted localization
do not represent B; restricted localization plus the B atoms does.

BFL3 rejects coinduced/bar acyclic replacement as carrier localization.

BFL4 rejects cone nullhomotopy as carrier localization.

BFL5 rejects jet deletion and obstruction quotient as maps from the original
class to zero.

BFL6 rejects declared localization.

BFL7 rejects separate fiber exact sequences; the ordered normal ratio needs
a common sequence.

BFL8 rejects localization-looking control packages.

BFL9 records the live predicate. Only carrier restricted fiber localization
passes.

BFL10 checks that restricted fiber localization completes B and leaves only
control death.

## 4. Impact on R1

```text
R1 after docs 138-319:
  NEWLY FIXED THIS CYCLE:
    - exactness must be one carrier localization sequence on dQ restricted to
      the actual p1,p2 boundary fibers.

  CURRENT LIVE TARGET:
    - construct the carrier localization sequence on dQ;
    - prove it restricts to the p1 boundary fiber;
    - prove it restricts to the p2 boundary fiber;
    - prove the common restricted sequence gives the ordered normal ratio;
    - prove its connecting map sends the original representative c to zero;
    - keep self-dual properness, p1,p2 primary, and endpoint rank;
    - prove non-formability on controls.

  DISCIPLINE:
    - coinduction, bar boundaries, cones, deletion, quotient, declared
      localization, and separate fiber exact sequences are diagnostics only.

  STILL OPEN:
    - construct the restricted dQ localization sequence in Qbar_BECD;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BFL.1  The carrier supplies one exact localization sequence on dQ.
ACCEPT-BFL.2  That sequence restricts to the p1 boundary fiber.
ACCEPT-BFL.3  That sequence restricts to the p2 boundary fiber.
ACCEPT-BFL.4  The same sequence gives the ordered normal ratio.
ACCEPT-BFL.5  The connecting map sends the original representative c to zero.
ACCEPT-BFL.6  c is preserved as the original DD.4 class, not deleted or
              quotiented away.
ACCEPT-BFL.7  Self-dual properness, primary p1,p2, and endpoint rank remain.
ACCEPT-BFL.8  Controls cannot form the restricted localization package.

KILL-BFL.1    Reject coinduced/bar acyclic replacement as localization.
KILL-BFL.2    Reject cone/nullhomotopy dh=c as localization.
KILL-BFL.3    Reject jet deletion or obstruction quotient.
KILL-BFL.4    Reject declared localization or declared DD.4 death.
KILL-BFL.5    Reject separate p1 and p2 fiber exact sequences without one
              common dQ localization sequence for the ordered normal ratio.
KILL-BFL.6    Reject localization-looking packages formable on controls.
```
