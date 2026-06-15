# 195 - PFV2 GPF residual monodromy effsep dload free trace codomain collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 194 forces the mixed p/q separator-consuming operation to be
carrier-selective. The next false positive is a selective mixed
consumer whose trace codomain, trace wrapper, determinant codomain, or
regularized value is supplied externally. The consumer exists, but
`F_C`, `Tr_L`, or the trace-facing value is not derived from it.

Such a proposal does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a fiber-internal separator sep_G^{fib};
3. a separator-sensitive first downstream slot DLoad_G^{sep};
4. a nonforgetful route from DLoad_G^{sep} to the strict trace
   interface;
5. a mixed p/q trace-facing operation that consumes sep_G^{fib} or
   delta_rho_G^{fib};
6. the mixed consumer is not formable for Epstein/DH controls;
7. the trace codomain, trace wrapper, determinant target, regularized
   value, or comparison space is supplied as a free external codomain
   rather than being derived from the mixed consumer.
```

It does not cover a proposal where the mixed selective consumer itself
derives the trace codomain and trace map.

## 3. Lemma

Lemma 195.1:

```text
If a mixed carrier-selective separator consumer uses a free external
trace codomain or trace wrapper, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.
```

The recorded verdict is:

```text
REJECT_DLOAD_FREE_TRACE_CODOMAIN.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE requires a mixed p/q
consumer that controls cannot instantiate. That removes the obvious
control-formability failure, but it does not by itself derive a
load-bearing trace value. If the trace codomain is supplied freely
after the consumer exists, then the downstream trace can still be a
wrapper around a selective diagnostic rather than a native trace of
the candidate object.

Assume the covered class. The separator reaches a mixed p/q consumer,
the consumer uses the separator, and Epstein/DH controls cannot form
that consumer. However, the map to the trace-facing object factors as

```text
MixedConsumer(DLoad_G^{sep}) -> FreeCodomain -> Tr_L / determinant / value.
```

The second arrow is not derived from the mixed consumer. It may be a
chosen vector space, normed codomain, determinant target, regularized
comparison scale, or trace wrapper that can be attached after the
selective operation. Then the consumer has not supplied `F_C` or
`Tr_L` as candidate-native structure; it has only supplied an input to
an externally chosen trace interface.

This is the doc-94 strict trace-derived codomain issue in the current
DLoad notation. The program needs the trace-facing codomain/map to be
native to the selective mixed consumer, not an auxiliary wrapper.
Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-NATIVE.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-NATIVE.
```

It must prove that the mixed carrier-selective separator consumer
derives the trace-facing codomain and trace map natively: `F_C`,
`Tr_L`, determinant target, kernel codomain, regularized value, or
comparison space cannot be supplied after the fact as free auxiliary
structure.

## 6. Kill Conditions

A future proposal is killed by this no-go only when the trace codomain
is free or external:

```text
KILL-DLOAD-FREEFC.1 free F_C
  F_C is chosen independently of the mixed selective consumer.

KILL-DLOAD-FREEFC.2 external trace wrapper
  Tr_L is attached after the consumer is formed rather than derived
  from it.

KILL-DLOAD-FREEFC.3 free determinant target
  the determinant, kernel, or regularized value lands in a codomain
  supplied by hand.

KILL-DLOAD-FREEFC.4 comparison-space insertion
  the zero/sign/positivity comparison space is chosen after the mixed
  consumer exists.
```

Do not apply this no-go against a proposal with a proved native route
from the mixed selective consumer to `F_C` and `Tr_L`.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE:
  REJECT_DLOAD_FREE_TRACE_CODOMAIN for mixed selective consumers whose
  trace codomain or trace wrapper is supplied externally.

PFV2-ADELIC-LOCAL:
  still live only through
  PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-NATIVE.

A2 witness:
  still not licensed.
```
