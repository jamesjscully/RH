# 169 - PFV2 GPF residual monodromy presentation collapse

Status: bounded no-go from the PFV2-GPF-RMON-SELECT target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only residual
monodromy/action proposals that are presentation, gauge, or coherence
data for assembling the all-places object.

## 1. Purpose

Doc 168 writes the residual monodromy shot:

```text
PFV2-GPF-RMON(p,q).
```

The first false positive is ordinary presentation monodromy: a
proposal names `rho_G^{mon}`, but the class is only a gauge of
`gamma_G`, a torsor of descent presentations, or a coherence witness
for all-places assembly. This document rejects that class.

## 2. Covered Class

Call a proposal `PFV2_GPF_RMON_pres` if it satisfies all of:

```text
D169.1 residual monodromy syntax
  The proposal names S_{p,q}^{G,rho}, rho_G^{mon}, and
  kappa_G^{mon} before an assembly functor.

D169.2 presentation origin
  rho_G^{mon} is a monodromy, action, extension, torsor, gauge, or
  coherence datum whose role is to present, trivialize, compare, or
  assemble the all-places object D.

D169.3 no native GPF action
  No theorem says rho_G^{mon} exists only because GPF_{p,q},
  Eff_{p,q}, and the p,q+complement source act on each other as
  source data before assembly.

D169.4 inherited first map
  kappa_G^{mon} factors through a choice of descent presentation,
  through D plus p,q marking, or through GPF_{p,q}, Eff_{p,q}, and
  gamma_G after forgetting rho_G^{mon}.

D169.5 downstream presentation erasure
  M_C/F_C/Tr_L either forgets rho_G^{mon} or sees it only as a
  presentation/gauge/coherence choice.
```

This class includes:

```text
monodromy of the descent presentation stack;
torsors of choices of gamma_G;
automorphisms of an assembly diagram;
coherence data for comparing equivalent GPF presentations;
actions that become ordinary labels on D after assembly.
```

## 3. Lemma

### Lemma 169.1

`PFV2_GPF_RMON_pres` does not satisfy PFV2-GPF-RMON-SELECT.

Verdict:

```text
REJECT_RMON_PRESENTATION
  if rho_G^{mon} is only presentation, gauge, or coherence data.

REJECT_RMON_INHERITED_MAP
  if kappa_G^{mon} factors through D, marking, or gamma_G after
  forgetting rho_G^{mon}.

REJECT_RMON_DOWNSTREAM_ERASURE
  if downstream sees only D, scalar PF, p,q marking, or presentation
  choice.

HOLD_RMON_NATIVE
  if a later proposal supplies a native residual monodromy/action class
  whose existence is part of the p,q+complement GPF source and is not
  equivalent to presentation data.
```

### Proof

PFV2-GPF-RMON-SELECT requires `rho_G^{mon}` to be residual source data,
not merely a way to present or compare an assembled object.

Under D169.1-D169.2, the proposal has the right names but the wrong
load-bearing content. A torsor of presentations, a gauge of `gamma_G`,
or a coherence witness for assembly records how to describe `D`; it
does not supply a native p,q+complement GPF datum.

Under D169.3, no native GPF action is present. Broad descent and
gluing diagrams can carry monodromy, automorphisms, gauges, and
coherence witnesses without becoming selective Euler-carrier sources.
Thus the class has not escaped the decoration logic of doc 157 or the
effective-descent logic of doc 167.

Under D169.4, the first map is inherited. Once `rho_G^{mon}` is
forgotten, the map still factors through the presentation data or
through `D` plus marking/readout. That is not first consumption of a
residual primitive.

Under D169.5, downstream dependence fails. If M_C/F_C/Tr_L forgets the
class or treats it as a presentation choice, doc 111 rejects the route.

Therefore presentation/gauge/coherence residual monodromy does not
satisfy PFV2-GPF-RMON-SELECT. QED.

## 4. What Presentation Monodromy Still Supplies

Allowed:

```text
language for comparing stricter residual-monodromy proposals;
diagnostics for whether rho_G^{mon} survives assembly as object data;
compatibility checks after a native residual class has been named;
external examples of classes that do not count.
```

Not allowed:

```text
claiming PFV2-GPF-RMON-SELECT;
claiming FIRST_MAP_PASS;
claiming control non-formability;
running an A2 witness;
promoting presentation/gauge/coherence data to residual source data;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 residual-monodromy route is:

```text
PFV2-GPF-RMON-NATIVE.
```

The target:

```text
There is a native residual monodromy, action, or extension class
rho_G^{nat} inside S_{p,q}^{G,rho} whose existence is part of the
p,q+complement GPF source before assembly and is not equivalent to a
presentation, gauge, or coherence witness for D.

kappa_G^{nat} consumes rho_G^{nat} before assembly; changing
rho_G^{nat} while holding D, p,q marking, and presentation data fixed
changes the first map or its target; Epstein/DH controls cannot form
rho_G^{nat} or kappa_G^{nat}; B0_p and B0_q embed conservatively; and
rho_G^{nat} remains load-bearing in M_C/F_C/Tr_L.
```

This is narrower than PFV2-GPF-RMON-SELECT because it removes
presentation/gauge/coherence monodromy and demands native residual
action data.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named native residual monodromy
class:

```text
KILL-RMON-NATIVE.1 no native action
  The proposed rho_G^{nat} is not defined by a native action,
  extension, or monodromy of the p,q+complement GPF source.

KILL-RMON-NATIVE.2 control formability
  Epstein/DH controls can form rho_G^{nat} and kappa_G^{nat} while
  retaining theta/count shadows.

KILL-RMON-NATIVE.3 inherited first map
  kappa_G^{nat} is unchanged when rho_G^{nat} is changed while D,
  p,q marking, and presentation data are fixed.

KILL-RMON-NATIVE.4 bank replacement
  rho_G^{nat} requires replacing B0_p/B0_q by a full global source.

KILL-RMON-NATIVE.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_G^{nat}.
```

Do not apply these beyond the named native residual monodromy class.

## 7. Board Update

```text
PFV2_GPF_RMON_pres:
  REJECT_RMON_PRESENTATION.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-NATIVE or another native
  residual p,q+complement GPF action class.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 168
  Supplies PFV2-GPF-RMON(p,q) and the PFV2-GPF-RMON-SELECT target.

doc 167
  Rejects effective-descent-equivalent GPF local sources.

doc 157
  Rejects decorative torsor/extension/cocycle residuals.

doc 158
  Records the carrier-native torsor source standard.

doc 111
  Still blocks downstream forgetfulness.
```
