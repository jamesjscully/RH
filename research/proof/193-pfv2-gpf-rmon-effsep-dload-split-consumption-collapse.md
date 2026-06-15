# 193 - PFV2 GPF residual monodromy effsep dload split consumption collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 192 forces `sep_G^{fib}` or `delta_rho_G^{fib}` to be consumed by
the first trace-facing object or map downstream of `DLoad_G^{sep}`. The
next false positive is a consumer that is still split over the
`B0_p` and `B0_q` banks: the separator enters an operation, but the
operation is a product, direct sum, independent pair of traces, or
coordinatewise bookkeeping rather than a mixed p/q formation.

Such a proposal does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a fiber-internal separator sep_G^{fib};
3. a separator-sensitive first downstream slot DLoad_G^{sep};
4. a nonforgetful route from DLoad_G^{sep} to the strict trace
   interface;
5. a first trace-facing operation that consumes sep_G^{fib} or
   delta_rho_G^{fib};
6. that consuming operation decomposes into independent p-bank and
   q-bank operations, or is functorial in a direct product/direct sum
   of the two bank records before any mixed p/q use.
```

It does not cover a consumer where the p-bank and q-bank data are
jointly required to form the trace-facing object or map.

## 3. Lemma

Lemma 193.1:

```text
If the first separator-consuming trace-facing operation splits into
independent one-place bank operations, then the candidate does not
satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED.
```

The recorded verdict is:

```text
REJECT_DLOAD_SPLIT_CONSUMPTION.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED requires the separator difference
to become load-bearing in the trace-facing construction. Because the
current A2 branch is a two-place p/q source branch, load-bearing use is
not enough if it occurs through independent one-place consumers that
never form a mixed object.

Assume the covered class. The separator is sensitive, nonforgotten, and
consumed. However, the consuming operation factors as

```text
DLoad_G^{sep} -> C_p(DLoad_G^{sep}|_p) x C_q(DLoad_G^{sep}|_q)
              -> M_C/F_C/Tr_L
```

or through the analogous direct sum, product, pair-of-traces, or
coordinatewise construction. Then the construction can be evaluated by
separate p-bank and q-bank procedures before any p/q interaction is
used. The same-readout residual pair has not forced a mixed
carrier-consuming formation; it has only supplied two independent
banked consumers.

This is the A2 version of the doc-86 same-form coupling guard and the
doc-100 shadow-enlargement guard. A two-place route cannot be promoted
when the decisive operation is still functorial in separated bank
records. Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.
```

It must prove that the first trace-facing consumer of `sep_G^{fib}` or
`delta_rho_G^{fib}` is a mixed p/q operation: neither p-bank nor q-bank
data alone forms the consumer, and the consumer does not factor through
a direct product, direct sum, pair of one-place traces, coordinatewise
kernel, or separated determinant before the mixed use.

## 6. Kill Conditions

A future proposal is killed by this no-go only when split consumption
is explicit:

```text
KILL-DLOAD-SPLIT.1 product consumer
  the first consuming operation is C_p x C_q with independent p/q
  inputs.

KILL-DLOAD-SPLIT.2 direct-sum consumer
  the separator is consumed separately on summands before any mixed
  object is formed.

KILL-DLOAD-SPLIT.3 pair of traces
  the trace-facing value is a pair or sum of one-place traces.

KILL-DLOAD-SPLIT.4 coordinatewise kernel or determinant
  the kernel, determinant, regularization, or codomain is formed
  coordinatewise from separated bank data.
```

Do not apply this no-go against a consumer whose formation genuinely
requires both banks in one mixed operation before trace evaluation.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED:
  REJECT_DLOAD_SPLIT_CONSUMPTION for separator-consuming operations
  that split over the two banks before any mixed p/q use.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.

A2 witness:
  still not licensed.
```
