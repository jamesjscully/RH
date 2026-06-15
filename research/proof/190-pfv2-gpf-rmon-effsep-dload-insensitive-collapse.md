# 190 - PFV2 GPF residual monodromy effsep dload insensitive collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license.

## 1. Purpose

Doc 189 names the first downstream load slot:

```text
DLoad_G^{sep}.
```

The immediate false positive is a named downstream slot that receives
the separator record syntactically but is unchanged when
`sep_G^{fib}` or `delta_rho_G^{fib}` changes. Such a slot does not
satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a separator sep_G^{fib};
3. a named first downstream slot DLoad_G^{sep};
4. a map lambda_G^{sep};
5. DLoad_G^{sep} is invariant under changing sep_G^{fib} and
   delta_rho_G^{fib} while holding the fixed readout and banks.
```

It does not cover a downstream slot with a proved sensitivity theorem.

## 3. Lemma

Lemma 190.1:

```text
If DLoad_G^{sep} is unchanged by changing sep_G^{fib} or
delta_rho_G^{fib}, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT.
```

The recorded verdict is:

```text
REJECT_DLOAD_INSENSITIVE.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT requires the downstream load slot to
be the first object that actually receives the separator difference.
The target is not satisfied by a slot whose definition merely carries
the separator as inert metadata.

Assume the covered class. The map `lambda_G^{sep}` is named, but
changing `sep_G^{fib}` or `delta_rho_G^{fib}` does not change
`DLoad_G^{sep}`. Then the downstream slot factors through the quotient
that forgets the separator. The separator may still be present in
notation, but it is not load-bearing.

This is the doc-188 downstream-erasure failure in its first-slot form:
erasure happens at `DLoad_G^{sep}` itself rather than later at
`M_C`, `F_C`, or `Tr_L`. Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.
```

It must prove that changing `sep_G^{fib}` or `delta_rho_G^{fib}`
changes `DLoad_G^{sep}` before `M_C`, `F_C`, `Tr_L`, determinant,
kernel, regularization, positivity, or zero comparison.

## 6. Kill Conditions

A future proposal is killed by this no-go only when first-slot
insensitivity is explicit:

```text
KILL-DLOAD-INS.1 separator-invariant slot
  DLoad_G^{sep} is unchanged under changing sep_G^{fib}.

KILL-DLOAD-INS.2 difference-invariant slot
  DLoad_G^{sep} is unchanged under changing delta_rho_G^{fib}.

KILL-DLOAD-INS.3 metadata-only separator
  the separator is attached as a label but no map or object changes.

KILL-DLOAD-INS.4 quotient-before-slot
  lambda_G^{sep} factors through a separator-forgetting quotient
  before DLoad_G^{sep}.
```

Do not apply this no-go against a downstream slot with a proved
separator-sensitivity theorem.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT:
  REJECT_DLOAD_INSENSITIVE for downstream slots unchanged by the
  separator.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE.

A2 witness:
  still not licensed.
```
