# 185 - PFV2 GPF residual monodromy effsep external collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-SELECT / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 184 names the separator datum required to certify a separated
same-readout residual pair:

```text
sep_G^{fib}.
```

The immediate false positive is a separator that exists only after
leaving the fixed fiber, choosing representatives, changing
`Read_{desc}`, or applying a downstream diagnostic. Such a separator
does not satisfy PFV2-GPF-RMON-EFFSEP-SELECT.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout pair rho_G^{fib,0}, rho_G^{fib,1};
2. a named separator sep_G;
3. sep_G distinguishes the two symbols only after one of:
   a. changing Read_{desc};
   b. choosing presentations or representatives;
   c. passing to scalar PF/complement/assembly bookkeeping;
   d. applying passive filtered or ambient cone shadow data;
   e. forming a downstream kernel, determinant, trace, mixed object,
      regularization, positivity test, or zero comparison.
```

It does not cover a separator proved to be a well-defined function,
map, class, or invariant of `Fib_Eff^{res}(Read_{desc})` before first
map use.

## 3. Lemma

Lemma 185.1:

```text
If sep_G distinguishes rho_G^{fib,0} from rho_G^{fib,1} only after
leaving Fib_Eff^{res}(Read_{desc}) or only after choosing
representatives, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-SELECT.
```

The recorded verdict is:

```text
REJECT_EFFSEP_EXTERNAL.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-SELECT asks for a separator whose domain is the
fixed residual fiber and whose value distinguishes residual classes
before assembly or downstream evaluation.

Assume the covered class. The proposal names a `sep_G`, but its
separation happens only after changing the readout, choosing
representatives, adding bookkeeping, passing to passive shadows, or
forming downstream analytic/trace data. Then `sep_G` is not a
fiber-internal separator for the two residual classes. It is a
diagnostic of a presentation, a modified readout, a shadow, or a later
construction.

If `sep_G` depends on representatives, it is not defined on
`Fib_Eff^{res}(Read_{desc})`. If it depends on changed readout or
downstream data, it cannot be consumed by `kappa_G^{sep}` before
assembly. If it factors through passive shadows or bookkeeping, it is
available to the same controls already excluded by the target.

Therefore the covered class is rejected.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-INTERNAL.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-INTERNAL.
```

It must prove that `sep_G^{fib}` is defined inside
`Fib_Eff^{res}(Read_{desc})`, is invariant under allowed
representative changes, distinguishes `rho_G^{fib,0}` from
`rho_G^{fib,1}`, and is consumed before assembly or downstream
diagnostics.

## 6. Kill Conditions

A future proposal is killed by this no-go only when the externality or
representative dependence is explicit:

```text
KILL-EFFSEP-EXT.1 changed readout
  the separator distinguishes only after changing Read_{desc}.

KILL-EFFSEP-EXT.2 representative dependence
  the separator distinguishes representatives but is not well-defined
  on residual classes.

KILL-EFFSEP-EXT.3 bookkeeping diagnostic
  the separator is scalar PF, complement, or assembly bookkeeping.

KILL-EFFSEP-EXT.4 passive shadow diagnostic
  the separator is computed only after passive filtered or ambient cone
  shadow projection.

KILL-EFFSEP-EXT.5 downstream diagnostic
  the separator appears only after kernel, determinant, trace, mixed
  object, regularization, positivity, or zero comparison.
```

Do not apply this no-go against a separator with a well-defined
fiber-internal construction before first-map use.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-SELECT:
  REJECT_EFFSEP_EXTERNAL for external or representative-dependent
  separators.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-INTERNAL.

A2 witness:
  still not licensed.
```
