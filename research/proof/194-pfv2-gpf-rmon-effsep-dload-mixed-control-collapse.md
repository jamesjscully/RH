# 194 - PFV2 GPF residual monodromy effsep dload mixed control collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 193 forces the first separator-consuming trace-facing operation to
be a mixed p/q operation. The next false positive is a mixed operation
that is still available to the control world: Epstein represented-norm
data, DH coefficient/measure shadows, or broad product/kernel shadows
can instantiate the same mixed consumer before carrier-selective use.

Such a proposal does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.

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
6. Epstein/DH or broad shadow controls can instantiate the same mixed
   operation while retaining their theta/count shadows.
```

It does not cover a mixed consumer with a proved carrier-selectivity
theorem excluding those controls at the object/map formation stage.

## 3. Lemma

Lemma 194.1:

```text
If the first mixed separator-consuming operation can also be formed for
Epstein/DH or broad shadow controls, then the candidate does not
satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.
```

The recorded verdict is:

```text
REJECT_DLOAD_MIXED_CONTROL_FORMABLE.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED requires a mixed p/q
consumer, but the program's carrier gate also requires that the
load-bearing operation be unavailable to the represented-norm and
measure-shadow controls before signs, trace evaluation, positivity, or
zero comparison.

Assume the covered class. The separator reaches a mixed p/q
trace-facing consumer and is used there. However, the same construction
rule also forms a mixed consumer for Epstein/DH or broad shadow data.
Then the operation is mixed only in an abstract product/kernel sense;
it is not selective for the PFV2 carrier source. Its apparent p/q
interaction is therefore a shared shadow operation, not evidence that
the residual monodromy source has supplied a new carrier-consuming map.

This is not the doc-193 split-consumption collapse, because the
operation may genuinely mix two inputs. It is the carrier-selectivity
failure at the mixed-consumer level: the decisive operation is still
available to the controls. Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.
```

It must prove that the first mixed p/q trace-facing consumer of
`sep_G^{fib}` or `delta_rho_G^{fib}` is carrier-selective: the
consumer can be formed from the PFV2 residual source but cannot be
formed for Epstein represented-norm data, DH coefficient/measure
shadows, or broad product/kernel shadow data while their theta/count
shadows remain meaningful.

## 6. Kill Conditions

A future proposal is killed by this no-go only when mixed-consumer
control formability is explicit:

```text
KILL-DLOAD-MIXCTL.1 represented-norm consumer
  the same mixed consumer forms for Q=x^2+5y^2 data.

KILL-DLOAD-MIXCTL.2 DH shadow consumer
  DH coefficient or measure data instantiate the same consumer before
  trace/sign/positivity use.

KILL-DLOAD-MIXCTL.3 broad product/kernel consumer
  the mixed operation is functorial in broad product, kernel,
  correspondence, or determinant shadow data.

KILL-DLOAD-MIXCTL.4 control survives deletion
  deleting the PFV2 residual source still leaves the mixed consumer
  formable from control shadows.
```

Do not apply this no-go against a mixed consumer with a proved
carrier-selectivity theorem at the first object/map formation.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED:
  REJECT_DLOAD_MIXED_CONTROL_FORMABLE for mixed p/q consumers that
  are still formable for Epstein/DH or broad shadow controls.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE.

A2 witness:
  still not licensed.
```
