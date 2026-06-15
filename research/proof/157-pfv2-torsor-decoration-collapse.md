# 157 - PFV2 torsor decoration collapse

Status: bounded no-go from the PFV2-TOR-SELECT target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only
torsor/extension/cocycle residuals that are gauge choices,
presentations, or ordinary decorations of the assembled object.

## 1. Purpose

Doc 156 identifies the torsor/extension/cocycle family as the most
plausible surviving PFV2 residual shot:

```text
PFV2-RHO-TOR(p,q).
```

The first licensed kill condition is:

```text
KILL-TOR.1 decoration collapse.
```

This document applies that kill condition.

## 2. Covered Class

Call a proposal `PFV2_TOR_decor` if it satisfies all of:

```text
D157.1 torsor residual
  The source contains a residual rho_tor described as a torsor,
  extension, cocycle, automorphism, or coherence datum.

D157.2 assembled-object decoration
  After successful assembly, rho_tor is equivalent to one of:

    a choice of trivialization;
    a gauge choice;
    a presentation of D;
    an ordinary cohomology label attached to D;
    an automorphism group action not changing the source type;
    a coherence witness for an already accepted diagram.

D157.3 no carrier-native condition
  No theorem says rho_tor exists only for the Euler carrier source,
  rather than for any object with comparable local pieces or shadows.

D157.4 inherited first map
  kappa_tor either ignores rho_tor after choosing a representative, or
  corresponds to a map on D plus the decorative label.

D157.5 downstream decoration
  M_C, F_C, or Tr_L either forgets rho_tor or sees it only as an
  ordinary decoration/gauge choice.
```

This class includes:

```text
torsors of trivializations of D;
extension classes attached after D exists;
cocycles whose only role is to present an already accepted descent
object;
automorphism labels that do not change source formability;
coherence data for a diagram that controls can also decorate.
```

## 3. Lemma

### Lemma 157.1

`PFV2_TOR_decor` does not satisfy PFV2-TOR-SELECT.

Verdict:

```text
REJECT_TOR_DECORATION
  if rho_tor is only a decoration or presentation of D.

REJECT_TOR_GAUGE
  if rho_tor is only a gauge/trivialization choice.

REJECT_TOR_INHERITED_MAP
  if kappa_tor factors through D plus the decoration.

HOLD_CARRIER_NATIVE_TOR
  if a later proposal supplies a torsor/extension/cocycle class whose
  existence is carrier-native and not covered by D157.1-D157.5.
```

### Proof

PFV2-TOR-SELECT requires rho_tor to be source-selective and
load-bearing. It is not enough for rho_tor to be a non-scalar
decoration of an assembled object.

Under D157.1-D157.2, rho_tor survives only as a choice of
presentation, gauge, cohomology label, automorphism label, or coherence
witness for D. Such data may be mathematically nontrivial, but it does
not decide whether the PFV2 source exists before D. It is post-source
or source-neutral decoration.

Under D157.3, no carrier-native theorem excludes controls. Broad
shadow objects can often be decorated with torsors, extensions,
cocycles, automorphism labels, or coherence witnesses while retaining
their theta/count shadows.

Under D157.4, kappa_tor is inherited from the assembled object plus
decoration. That is not a first carrier-consuming map for the residual
field.

Under D157.5, downstream dependence fails. If M_C/F_C/Tr_L forgets
rho_tor or treats it as a gauge/presentation choice, doc 111 rejects
the route.

Thus decorative torsor/extension/cocycle residuals do not pass
PFV2-TOR-SELECT. QED.

## 4. What Decorative Torsors Still Supply

Allowed:

```text
language for comparing residual proposals;
tests for whether a torsor is carrier-native or merely decorative;
possible compatibility diagnostics after a stricter source passes;
external-question examples of what does not count.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming control non-formability;
running an A2 witness;
promoting gauge/trivialization data to carrier source evidence;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 torsor route is:

```text
PFV2-TOR-NATIVE.
```

The target:

```text
There is a carrier-native torsor, extension, cocycle, automorphism, or
coherence datum rho_tor whose existence is part of Desc_{p,q}^{tor}
before assembly and is not a decoration of the assembled object D.

kappa_tor consumes rho_tor before assembly; Epstein/DH controls cannot
form rho_tor or kappa_tor; B0_p and B0_q embed conservatively; and
rho_tor remains load-bearing in M_C/F_C/Tr_L.
```

This is narrower than PFV2-TOR-SELECT. It removes ordinary
decoration/gauge/presentation torsors and demands carrier-native
torsor data.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named carrier-native torsor class:

```text
KILL-TOR-NATIVE.1 control formability
  Epstein/DH shadows can form the same carrier-native torsor and
  kappa_tor.

KILL-TOR-NATIVE.2 post-assembly origin
  the torsor exists only after all-places assembly or post-global
  reflection.

KILL-TOR-NATIVE.3 bank replacement
  the torsor requires replacing B0_p/B0_q by the full global source.

KILL-TOR-NATIVE.4 downstream erasure
  every legal M_C/F_C/Tr_L forgets the torsor.
```

Do not apply these beyond the named carrier-native torsor class.

## 7. Board Update

```text
PFV2_TOR_decor:
  REJECT_TOR_DECORATION.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-TOR-NATIVE or another non-decorative
  surviving residual source.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 156
  Supplies PFV2-RHO-TOR(p,q) and licenses KILL-TOR.1.

doc 155
  Rejects obstruction/defect residuals that vanish or become scalar.

doc 154
  Rejects marking/bookkeeping residuals.

doc 111
  Still blocks downstream forgetfulness.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```
