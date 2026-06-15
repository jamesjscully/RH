# 186 - PFV2 GPF residual monodromy effsep control collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-INTERNAL / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 185 leaves only separators proved internal to the fixed residual
fiber:

```text
sep_G^{fib} : Fib_Eff^{res}(Read_{desc}) -> Y_G^{sep}.
```

The next false positive is an internal separator whose defining rule is
still broad enough for Epstein represented-norm data or DH
coefficient/measure shadows to instantiate while retaining theta/count
shadows. Such a separator does not satisfy
PFV2-GPF-RMON-EFFSEP-INTERNAL.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a separator sep_G^{fib} well-defined inside
   Fib_Eff^{res}(Read_{desc});
3. sep_G^{fib} distinguishes the pair before assembly;
4. the defining rule for sep_G^{fib} is functorial, invariant, or
   otherwise available for Epstein/DH controls while their theta/count
   shadows remain meaningful.
```

It does not cover a separator whose source category, domain condition,
or first map is structurally unavailable to those controls before
trace, sign, positivity, or zero comparison.

## 3. Lemma

Lemma 186.1:

```text
If an internal separator sep_G^{fib} can also be instantiated by
Epstein represented-norm or DH coefficient/measure controls while
retaining theta/count shadows, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-INTERNAL.
```

The recorded verdict is:

```text
REJECT_EFFSEP_CONTROL_FORMABLE.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-INTERNAL requires more than internal
well-definedness. It remains an A2 strict-source target, so the
separator must be unavailable to the standard controls at the source or
first-map level.

Assume the covered class. The separator is internal to the residual
fiber and distinguishes the two classes, but its defining rule is
still broad: represented-norm controls or DH coefficient/measure
shadows can form the same separator while preserving theta/count
readouts. Then the separator is not source-selective. It does not force
the product-formula, p/q+complement, effectivity-boundary residual
structure to be present before the first map.

Consequently the route collapses to the carrier-overreach pattern
already enforced by docs 87, 97, 100, 105, and 107: the proposed
source has not excluded controls before signs, trace, regularization,
positivity, or zero comparison. The separator may be an internal
diagnostic of a broad class, but it is not the missing PFV2 carrier
source datum. Thus the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-INTERNAL.

Therefore the covered class is rejected.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.
```

It must prove that `sep_G^{fib}` is internal to the fixed residual
fiber and that Epstein/DH controls cannot instantiate the same
separator or first separator map while retaining theta/count shadows.

## 6. Kill Conditions

A future proposal is killed by this no-go only when control formability
is explicit:

```text
KILL-EFFSEP-CTRL.1 represented-norm formability
  Epstein represented-norm data instantiate sep_G^{fib} and
  kappa_G^{sep} while theta/count shadows remain meaningful.

KILL-EFFSEP-CTRL.2 DH formability
  DH coefficient/measure shadows instantiate sep_G^{fib} and
  kappa_G^{sep} while theta/count shadows remain meaningful.

KILL-EFFSEP-CTRL.3 broad functorial separator
  the separator is functorial for broad local-shadow data before
  primitive carrier checking.

KILL-EFFSEP-CTRL.4 late control failure
  controls fail only after trace, sign, regularization, positivity, or
  zero comparison.
```

Do not apply this no-go against a separator whose source category or
first map is proved structurally unavailable to controls before
downstream construction.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-INTERNAL:
  REJECT_EFFSEP_CONTROL_FORMABLE for internal but control-formable
  separators.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.

A2 witness:
  still not licensed.
```
