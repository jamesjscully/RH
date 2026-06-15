# 184 - PFV2 GPF residual monodromy effpair separator shot

Status: concrete PFV2-GPF-RMON-EFFPAIR-SEPARATED candidate shot /
Q134.1 internal result, 2026-06-12. This is not a B1 construction, not
an external answer, not a witness license, and not a no-go.

## 1. Purpose

Doc 183 rejects same-readout residual pairs whose two named classes
are identified by the fixed readout/descent/shadow equivalence. The
remaining target is:

```text
PFV2-GPF-RMON-EFFPAIR-SEPARATED.
```

That target still says "prove nonidentification" abstractly. This
document makes the next shot concrete: name the internal separator
that would certify the two classes are distinct inside the fixed
residual fiber before first-map use.

## 2. Candidate Record

Name:

```text
PFV2-GPF-RMON-EFFSEP(p,q).
```

Proposed source object:

```text
S_{p,q}^{G,effsep} in ECar_L1^{GPF,pq,effsep}
```

Fields inherited from docs 180-183:

```text
Read_{desc}
  the fixed effective-descent/readout tuple.

Fib_Eff^{res}(Read_{desc})
  the native fixed-readout residual fiber.

rho_G^{fib,0}, rho_G^{fib,1}
  two residual classes over the same Read_{desc}.

delta_rho_G^{fib}
  the fiber-internal difference between the two classes.

kappa_G^{pair}
  the first pair-consuming map.
```

New separator field:

```text
sep_G^{fib}
  a fiber-internal separator or certificate whose domain is
  Fib_Eff^{res}(Read_{desc}) and whose value distinguishes
  rho_G^{fib,0} from rho_G^{fib,1} before kappa_G^{pair}.
```

The intended first separator map is:

```text
kappa_G^{sep} : S_{p,q}^{G,effsep} -> Y_G^{sep}.
```

It must consume:

```text
(rho_G^{fib,0}, rho_G^{fib,1}, delta_rho_G^{fib}, sep_G^{fib})
```

before all-places assembly, trace, determinant, mixed object,
regularization, positivity, or zero comparison.

## 3. Why This Is A Real Shot

This is stricter than the separated-pair target:

```text
named separator:
  nonidentification must be carried by sep_G^{fib}, not merely asserted.

fiber-internal:
  sep_G^{fib} lives over the same Read_{desc}; it is not a changed
  readout, a new presentation, or a downstream diagnostic.

first-use:
  kappa_G^{sep} consumes the separator before any shadow-stable
  closure can erase it.

not a witness:
  no theorem asserts that sep_G^{fib} exists or excludes controls.
```

Thus the shot makes the next falsification target inspectable.

## 4. Gate Run

### Gate 184.1 - Separator placement

Verdict:

```text
LOCAL_EFFSEP_SCHEMA_PASS
```

Reason: the record places `sep_G^{fib}` inside the fixed residual
fiber and makes it a first-map input.

### Gate 184.2 - Separator existence

Verdict:

```text
HOLD_EFFSEP_EXISTENCE
```

Reason: no theorem has supplied a fiber-internal separator for the two
classes.

### Gate 184.3 - Representative independence

Verdict:

```text
HOLD_EFFSEP_REPRESENTATIVE_INDEPENDENCE
```

Reason: no theorem has shown that `sep_G^{fib}` distinguishes residual
classes rather than chosen representatives.

### Gate 184.4 - Control exclusion

Verdict:

```text
HOLD_EFFSEP_CONTROL_EXCLUSION
```

Reason: no theorem has shown that Epstein/DH controls cannot supply
the same separator while retaining theta/count shadows.

### Gate 184.5 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: no theorem has shown that the separator preserves the B0_p and
B0_q comb, address, count, and guard data before use.

### Gate 184.6 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes
`sep_G^{fib}` or `delta_rho_G^{fib}` as load-bearing source data.

## 5. Current Verdict

```text
PFV2-GPF-RMON-EFFSEP(p,q):
  LOCAL_EFFSEP_SCHEMA_PASS;
  HOLD_EFFSEP_EXISTENCE;
  HOLD_EFFSEP_REPRESENTATIVE_INDEPENDENCE;
  HOLD_EFFSEP_CONTROL_EXCLUSION;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-GPF-RMON-EFFPAIR-SEPARATED:
  SHARPEN to PFV2-GPF-RMON-EFFSEP-SELECT.

A2 witness:
  still not licensed.
```

This is construction progress only as a named separator record.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GPF-RMON-EFFSEP-SELECT.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF,pq,effsep} with
objects S_{p,q}^{G,effsep}, a fixed Read_{desc}, a residual fiber
Fib_Eff^{res}(Read_{desc}), a same-readout pair
rho_G^{fib,0}, rho_G^{fib,1}, and a separator sep_G^{fib} such that:

1. sep_G^{fib} is defined inside the fixed residual fiber;
2. sep_G^{fib}(rho_G^{fib,0}) != sep_G^{fib}(rho_G^{fib,1});
3. the inequality is representative-independent;
4. kappa_G^{sep} consumes sep_G^{fib} before assembly;
5. Epstein/DH controls cannot instantiate the same separator while
   retaining theta/count shadows;
6. B0_p and B0_q embed conservatively before separator use;
7. sep_G^{fib} or delta_rho_G^{fib} remains load-bearing downstream.
```

This theorem is narrower than PFV2-GPF-RMON-EFFPAIR-SEPARATED because
it names the separator that certifies separation.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named separator proposal:

```text
KILL-EFFSEP.1 no separator
  the proposal asserts separation but names no sep_G^{fib}.

KILL-EFFSEP.2 external separator
  sep_G^{fib} is computed only after changing Read_{desc}, choosing a
  presentation, or leaving the fixed fiber.

KILL-EFFSEP.3 representative dependence
  sep_G^{fib} separates representatives but not residual classes.

KILL-EFFSEP.4 control formability
  Epstein/DH controls can instantiate the same separator and first map.

KILL-EFFSEP.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets sep_G^{fib} and delta_rho_G^{fib}.
```

Do not apply these beyond the named separator proposal.

## 8. Board Update

```text
PFV2-GPF-RMON-EFFSEP(p,q):
  LOCAL_EFFSEP_SCHEMA_PASS.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-SELECT or another
  internal separator source.

A2 witness:
  still not licensed.
```
