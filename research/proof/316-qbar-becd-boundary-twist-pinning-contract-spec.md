# 316 - Qbar_BECD boundary twist-pinning contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 315 fixed the type of the live S atom:

```text
rank-one dual-boundary-to-primal-boundary map.
```

This document sharpens the remaining word "pinned." The Laurent twist in
that map cannot be a chosen Hom element, a formal torsor splitter, a full
Laurent Hilbert-90 valuation axis, a rank-one valuation degree character, a
degree-zero normalization, or shape-only OCB. It must be pinned by the
carrier oriented-Cartier normal-ratio data itself.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_twist_pinning_contract`
(BTP1-BTP8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_defect_duality_contract`,
`prime_int_n1b_qbar_becd_boundary_self_duality_interface`,
`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract`,
`prime_int_torsor_splitter_insertion_no_go`,
`prime_int_n1b_laurent_field_hilbert90_no_go`,
`prime_int_n1b_valuation_degree_character_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

There are several ways to make the DD.4 representative look like a boundary:

```text
adjoin a formal splitter b with b/phi(b)=c;
pass to the full Laurent field and use the odd valuation axis;
impose degree-zero glue;
choose a unit in Hom(L,L).
```

All of those are already too weak. They either insert the solution, import a
valuation axis, collapse a choice by normalization, or remain formable on
controls.

The live object must instead provide a carrier normal-ratio pinning:

```text
oriented-Cartier boundary components D1,D2,
their rank-one boundary defect lines,
a carrier rigidification of the normal ratio,
unique Laurent twist,
boundary equal to c,
p1,p2 primary,
not formable on controls.
```

This is still not the missing object. It is the next targeted construction
interface inside B.

## 2. Lemma

```text
Lemma 316.1 (boundary twist-pinning contract).

In the base 1-unit system U_1=1+z F_2[[z]], with phi(z)=z/(1+z) and
c=(1+z)^-1, the tested truncations L=6,8,10,12 satisfy:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Thus c is still the twist that must be pinned.

Formal torsor splitting has the right boundary only by insertion:

    phi(b)=b*c^-1,
    b/phi(b)=c.

Laurent Hilbert 90 has the right boundary only after importing the valuation
axis. Odd valuations kill [c]; even valuations do not.

A full integer valuation character is still rank one. It cannot preserve the
two independent endpoint maps required by p1,p2.

Degree-zero glue reduces the Laurent unit choice only by fiat. In windows
|k|<=1,2,4,8, the unit twists are:

    3,5,9,17,

and the nonzero maps are:

    7,31,511,131071.

Shape-only OCB selects the direction d1-d2, but not the normal-ratio
rigidification that makes the twist unique.

Therefore the accepted twist-pinning source is exactly:

    carrier-native,
    rank-one defect map,
    oriented-Cartier pair,
    normal ratio rigidified,
    unique twist,
    boundary is c,
    no inserted splitter,
    no external valuation axis,
    no degree-zero fiat,
    orientation fixed,
    p1,p2 primary,
    endpoint rank preserved,
    not formable on controls.

If this is constructed, the doc-315 boundary-defect duality map is live B.
After that, only formation-level control death remains in Phase A.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_TWIST_PINNING__CARRIER_NORMAL_RATIO_SOURCE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_twist_pinning_contract` verifies eight
gates.

BTP1 recomputes the base DD.4 class. The class remains nonzero and detected
by `res_1(c)=1`.

BTP2 rejects formal torsor splitting: the boundary is `c` only because the
splitter and its transformation law were inserted.

BTP3 rejects Laurent Hilbert 90 as the live pinning source: it uses an
imported odd valuation axis.

BTP4 rejects valuation degree characters: one valuation character cannot
preserve two endpoint maps.

BTP5 rejects degree-zero normalization: the Laurent twist choices still
overproduce unless the carrier itself pins the twist.

BTP6 rejects shape-only OCB as twist pinning: it selects direction but does
not rigidify the normal ratio.

BTP7 records the live predicate. Only carrier normal-ratio twist pinning
passes.

BTP8 checks slot accounting. OCB shape alone is still `O+E`; pinned twist in
the boundary-defect duality gives live B; adding control death completes
Phase A.

## 4. Impact on R1

```text
R1 after docs 138-316:
  NEWLY FIXED THIS CYCLE:
    - the live twist source is carrier oriented-Cartier normal-ratio pinning,
      not any unit choice whose boundary happens to be c.

  CURRENT LIVE TARGET:
    - construct the oriented-Cartier normal-ratio rigidification inside
      Qbar_BECD;
    - prove it produces a unique Laurent twist;
    - prove that twist has boundary c;
    - preserve primary p1,p2 and endpoint rank;
    - prove the pinning is not formable on controls.

  DISCIPLINE:
    - formal torsor splitters, full Laurent fields, valuation characters,
      degree-zero normalizations, and shape-only OCB are diagnostics only.

  STILL OPEN:
    - construct the carrier normal-ratio pinning;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BTP.1  The carrier supplies an oriented-Cartier boundary pair.
ACCEPT-BTP.2  The carrier rigidifies the normal ratio of the two boundary
              defect lines.
ACCEPT-BTP.3  The rigidification produces a unique Laurent twist.
ACCEPT-BTP.4  The boundary of that twist is the DD.4 representative c.
ACCEPT-BTP.5  p1,p2 remain primary and endpoint rank is preserved.
ACCEPT-BTP.6  The twist-pinning source is not formable on controls.

KILL-BTP.1    Reject a formal splitter b with b/phi(b)=c unless b is
              carrier-produced before the relation is asserted.
KILL-BTP.2    Reject full Laurent Hilbert 90 as the pinning source unless the
              valuation axis is carrier-native.
KILL-BTP.3    Reject a single valuation degree character as two endpoint maps.
KILL-BTP.4    Reject degree-zero normalization as twist pinning.
KILL-BTP.5    Reject choosing a Hom(L,L) unit as self-dual properness.
KILL-BTP.6    Reject shape-only OCB without normal-ratio rigidification.
KILL-BTP.7    Reject any twist-pinning package still formable on controls.
```
