# 188 - PFV2 GPF residual monodromy effsep downstream erasure collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-BANKED / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 187 leaves only control-excluded internal separators that preserve
the B0_p and B0_q banks. The next false positive is a separator that
is valid at the source level but erased before the mixed object,
codomain, trace, or other downstream load-bearing structure. Such a
separator does not satisfy PFV2-GPF-RMON-EFFSEP-BANKED.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a fiber-internal separator sep_G^{fib};
3. source-level control exclusion;
4. conservative B0_p and B0_q bank embedding;
5. every legal downstream construction M_C, F_C, Tr_L, determinant,
   kernel, regularization, or positivity input factors through data
   that forget sep_G^{fib} and delta_rho_G^{fib}.
```

It does not cover a route where `sep_G^{fib}` or
`delta_rho_G^{fib}` is consumed as load-bearing input by a downstream
object before trace, positivity, or zero comparison.

## 3. Lemma

Lemma 188.1:

```text
If every legal downstream construction forgets sep_G^{fib} and
delta_rho_G^{fib}, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-BANKED.
```

The recorded verdict is:

```text
REJECT_DOWNSTREAM_ERASURE.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-BANKED is still only a source-side candidate
unless the separator remains load-bearing in the structures that would
eventually feed the strict S3/LT76 interface. A separator erased before
`M_C`, `F_C`, `Tr_L`, determinant, kernel, or regularization cannot
contribute to the missing object.

Assume the covered class. The separator exists, is internal,
control-excluded, and preserves the banks, but every downstream
construction factors through a quotient or forgetful functor that no
longer depends on `sep_G^{fib}` or `delta_rho_G^{fib}`. Then changing
the separator does not change the downstream object. The proposed
separation is source-local decoration, not a load-bearing carrier
datum.

This is exactly the downstream-erasure collapse isolated in docs 111
and 112 and repeatedly retained as a live clause through docs 180,
182, and 184. Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-BANKED.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-LOADBEARING.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-LOADBEARING.
```

It must prove that `sep_G^{fib}` or `delta_rho_G^{fib}` is consumed as
load-bearing input by the first legal downstream object that feeds
`M_C`, `F_C`, `Tr_L`, determinant, kernel, regularization, or the
strict trace interface.

## 6. Kill Conditions

A future proposal is killed by this no-go only when downstream erasure
is explicit:

```text
KILL-EFFSEP-DOWN.1 mixed-object erasure
  M_C is independent of sep_G^{fib} and delta_rho_G^{fib}.

KILL-EFFSEP-DOWN.2 codomain erasure
  F_C factors through a quotient that forgets the separator.

KILL-EFFSEP-DOWN.3 trace erasure
  Tr_L is legal only after a carrier-forgetting envelope.

KILL-EFFSEP-DOWN.4 determinant/kernel erasure
  determinant, kernel, or regularization data are unchanged by
  changing the separator.

KILL-EFFSEP-DOWN.5 positivity-only use
  the separator appears only as a diagnostic after positivity or zero
  comparison.
```

Do not apply this no-go against a separator with a named downstream
load-bearing theorem.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-BANKED:
  REJECT_DOWNSTREAM_ERASURE for separator sources erased before
  downstream load-bearing use.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-LOADBEARING.

A2 witness:
  still not licensed.
```
