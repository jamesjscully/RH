# 191 - PFV2 GPF residual monodromy effsep dload forgetful route collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 190 forces the first downstream load slot

```text
DLoad_G^{sep}
```

to change when `sep_G^{fib}` or `delta_rho_G^{fib}` changes. The next
false positive is subtler: `DLoad_G^{sep}` is honestly sensitive, but
the only trace-legal route from that load slot to `M_C`, `F_C`,
`Tr_L`, or the strict trace interface factors through an envelope or
quotient that forgets the separator.

Such a proposal does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a fiber-internal separator sep_G^{fib};
3. a first downstream slot DLoad_G^{sep};
4. a proved sensitivity theorem: changing sep_G^{fib} or
   delta_rho_G^{fib} changes DLoad_G^{sep};
5. the only route from DLoad_G^{sep} to M_C/F_C/Tr_L or the strict
   trace interface passes through a carrier/separator-forgetting
   envelope, quotient, completion, pushforward, or trace closure.
```

It does not cover a route that preserves `sep_G^{fib}` or
`delta_rho_G^{fib}` up to the first trace-legal carrier-consuming
interface.

## 3. Lemma

Lemma 191.1:

```text
If DLoad_G^{sep} is separator-sensitive but every trace-legal route
from DLoad_G^{sep} to M_C/F_C/Tr_L factors through a separator-
forgetting envelope, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.
```

The recorded verdict is:

```text
REJECT_DLOAD_FORGETFUL_ROUTE.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE requires the separator difference
to become load-bearing before the downstream construction reaches
`M_C`, `F_C`, `Tr_L`, determinant, kernel, regularization, positivity,
or zero comparison. Sensitivity at the first slot is necessary but not
sufficient if the only legal continuation erases the data.

Assume the covered class. Changing `sep_G^{fib}` or
`delta_rho_G^{fib}` changes `DLoad_G^{sep}`. However, by hypothesis,
every available route from `DLoad_G^{sep}` to a trace-legal target
factors through a map

```text
DLoad_G^{sep} -> Env(DLoad_G^{sep}) -> M_C/F_C/Tr_L
```

where `Env` identifies records differing only by `sep_G^{fib}` or
`delta_rho_G^{fib}`. Therefore the trace-facing object sees the same
class for the two members of the residual pair. The downstream trace
package can be legal only after it has forgotten the separator.

This is the doc-118/doc-120 traceable-envelope failure in the current
effective-separator notation: trace legality is purchased by deleting
the only datum that made the downstream load slot non-control-like.
Thus the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-DLOAD-NONFORGETFUL.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-NONFORGETFUL.
```

It must prove that the route from `DLoad_G^{sep}` to `M_C`, `F_C`,
`Tr_L`, or the strict trace interface preserves `sep_G^{fib}` or
`delta_rho_G^{fib}` as load-bearing data. In particular, trace
legality cannot be obtained by passing through a carrier-forgetting or
separator-forgetting envelope before first carrier-consuming use.

## 6. Kill Conditions

A future proposal is killed by this no-go only when route-level
forgetting is explicit:

```text
KILL-DLOAD-FORG.1 separator-forgetting envelope
  the only trace-legal route from DLoad_G^{sep} identifies records
  differing by sep_G^{fib}.

KILL-DLOAD-FORG.2 difference-forgetting quotient
  the route to M_C/F_C/Tr_L quotients out delta_rho_G^{fib}.

KILL-DLOAD-FORG.3 trace closure after deletion
  trace legality is available only after completion, pushforward,
  regularization, or closure removes the separator datum.

KILL-DLOAD-FORG.4 carrier-forgetting envelope
  the route preserves a formal name for DLoad_G^{sep} but forgets the
  carrier source that distinguishes the residual pair.
```

Do not apply this no-go against a separator-sensitive downstream slot
with a proved nonforgetful route to the strict trace interface.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE:
  REJECT_DLOAD_FORGETFUL_ROUTE for separator-sensitive load slots whose
  only trace-legal route forgets the separator before trace-facing use.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-DLOAD-NONFORGETFUL.

A2 witness:
  still not licensed.
```
