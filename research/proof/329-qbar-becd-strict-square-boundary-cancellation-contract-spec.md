# 329 - Qbar_BECD strict-square boundary-cancellation contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninety-second cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 328 left the strict-square branch live only through:

```text
a carrier-native effectivity orientation / positive cone on the signed
strict-square character algebra that retains cancellation as
boundary-localization data.
```

This document fixes what "as boundary-localization data" must mean. The
signed zero-fiber class must map through a represented boundary-cancellation
functor to the DD.4 boundary localization inside Qbar_BECD. A weighted-zero
equation, positive/negative bookkeeping, Grothendieck group completion,
external chain complex, formally attached boundary cell, endpoint kernel, or
declared boundary map is not enough.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_boundary_cancellation_contract`
(BCC1-BCC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_signed_character_effectivity_contract`,
`prime_int_n1b_qbar_becd_strict_square_character_stratum_functor_contract`,
`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_represented_carrier_gate_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 328, the cheap repair is:

```text
observe that chi(zero)=2[1]-[2] has weighted mass zero,
move [2] to the other side,
call that balanced relation the boundary.
```

That is still external algebra. It has not produced the DD.4 boundary map,
the boundary localization, or the pushforward/graph/control consequences.
The signed zero fiber has to be represented as a boundary-cancellation
object of the same square, not as a relation in a free group completion.

The live branch therefore narrows from "retain cancellation" to:

```text
construct a represented boundary-cancellation functor from the signed
strict-square zero fiber to the DD.4 boundary localization, compatible with
character convolution and feeding the internal effectivity domain, endpoint,
pushforward, graph/Rosati/count data, and formation-level control death.
```

## 2. Lemma

```text
Lemma 329.1 (balanced signed character is not a DD.4 boundary).

The strict-square zero fiber has

    chi(zero) = 2[1] - [2].

It is numerically balanced:

    mass(2[1] - [2]) = 0,
    positive mass = negative mass = 2.

But convolution carries nontrivial boundary content:

    (2[1] - [2]) * 2[2] = 4[2] - 2[4],
    positive mass = negative mass = 8.

Weighted-zero selection detects both balances, but it constructs no DD.4
boundary map. Positive/negative splitting records

    (2[1], [2])

as bookkeeping only. Grothendieck completion records the same pair in a group
completion, and after convolution records

    (4[2], 2[4]),

but still supplies no represented boundary map. Attaching a formal cell with
boundary `2[1]-[2]` kills the relation externally. Endpoint kernels and
diagonal-zero filters are downstream afterthoughts. Controls, DH, and Epstein
can mimic balanced signed profiles.

Thus the accepted datum is exactly:

    carrier-native,
    actual strict-square signed character,
    actual signed zero fiber,
    actual boundary-cancellation functor,
    actual DD.4 boundary map,
    represented square boundary edges,
    cancellation not reduced to weighted zero,
    positive/negative split retained,
    cancellation compatible with character convolution as a module,
    cancellation mapped to boundary localization,
    boundary localization mapped to the internal effectivity domain,
    endpoint integrality generated,
    pushforward compatibility generated,
    graph/Rosati/count data generated,
    control death generated,
    controls undefined at the boundary,
    DH undefined at the boundary,
    Epstein undefined at the boundary,
    no weighted-zero selector,
    no positive/negative split only,
    no Grothendieck group completion,
    no formal boundary cell,
    no external chain complex,
    no diagonal-total-zero selector,
    no endpoint-kernel definition,
    no declared boundary cancellation,
    no boundary afterthought filter,
    not formable on controls, DH, or Epstein.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_BOUNDARY_CANCELLATION__SIGNED_ZERO_FIBER_MUST_MAP_TO_DD4_BOUNDARY__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_boundary_cancellation_contract`
verifies ten gates.

BCC1 records the signed zero fiber, its positive/negative split, weighted
balance, and convolutional boundary content.

BCC2 rejects weighted-zero selectors and diagonal-total-zero selectors.

BCC3 rejects positive/negative splitting as mere bookkeeping.

BCC4 rejects Grothendieck group completion because it supplies no represented
boundary map and no convolution-module boundary functor.

BCC5 rejects formal attached boundary cells and external chain complexes.

BCC6 rejects endpoint kernels as downstream boundary afterthoughts.

BCC7 makes convolution-module compatibility mandatory.

BCC8 records the DH/Epstein/control failure mode: balanced signed profiles
can be mimicked without the square.

BCC9 makes endpoint, pushforward, and control death mandatory outputs.

BCC10 records the live predicate. Only a represented DD.4
boundary-cancellation functor passes.

## 4. Impact on R1

```text
R1 after docs 138-329:
  NEWLY FIXED THIS CYCLE:
    - retaining signed cancellation is not enough. The signed zero-fiber
      class must map through a represented boundary-cancellation functor to
      the DD.4 boundary localization.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct its carrier-native effectivity orientation / positive cone;
    - construct the boundary-cancellation functor from the signed zero fiber
      to the DD.4 boundary map;
    - prove this boundary functor is compatible with character convolution;
    - prove boundary localization maps to the internal effectivity domain and
      generates endpoint integrality, pushforward compatibility,
      graph/Rosati/count data, and formation-level control death;
    - prove DH, Epstein, and controls are undefined at boundary formation.

  DISCIPLINE:
    - balanced equations, split pairs, group completions, formal cells,
      endpoint kernels, and declared boundary maps are diagnostics only.

  STILL OPEN:
    - construct the represented boundary-cancellation functor, or kill the
      strict-square branch with a named mechanism at this point.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BCC.1  Exhibit the signed zero fiber in the strict-square signed
              character algebra.
ACCEPT-BCC.2  Exhibit a represented boundary-cancellation functor to the
              DD.4 boundary map.
ACCEPT-BCC.3  Prove cancellation is not just weighted zero and is compatible
              with character convolution.
ACCEPT-BCC.4  Map DD.4 boundary localization into the internal effectivity
              domain.
ACCEPT-BCC.5  Generate endpoint, pushforward, graph/Rosati/count, and
              control death from the boundary-cancellation functor.

KILL-BCC.1    Reject weighted-zero or diagonal-zero selectors.
KILL-BCC.2    Reject positive/negative split-only witnesses.
KILL-BCC.3    Reject Grothendieck group completion.
KILL-BCC.4    Reject formal boundary cells or external chain complexes.
KILL-BCC.5    Reject endpoint kernels or boundary afterthought filters.
KILL-BCC.6    Reject declared boundary-cancellation maps.
KILL-BCC.7    Reject control/DH/Epstein-formable balanced profiles.
```
