# 187 - PFV2 GPF residual monodromy effsep bank replacement collapse

Status: bounded no-go from PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED /
Q134.1 internal result, 2026-06-12. This is not a B1 construction, not
an external answer, and not a witness license.

## 1. Purpose

Doc 186 leaves only separators that are internal to the fixed residual
fiber and unavailable to Epstein/DH controls. The next false positive
is a separator that achieves this only by replacing the B0_p and B0_q
banks with a new global source. Such a separator does not satisfy
PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.

## 2. Covered Class

This no-go covers proposals with all of the following features:

```text
1. a same-readout residual pair rho_G^{fib,0}, rho_G^{fib,1};
2. a separator sep_G^{fib} internal to Fib_Eff^{res}(Read_{desc});
3. source-level exclusion of Epstein/DH controls;
4. construction of the separator only after replacing B0_p or B0_q,
   deleting their comb/address/count/guard data, or embedding them as
   non-load-bearing shadows of a new all-places source.
```

It does not cover a separator that receives B0_p and B0_q
conservatively before separator use.

## 3. Lemma

Lemma 187.1:

```text
If sep_G^{fib} is control-excluded only after replacing the B0_p/B0_q
banks, then the candidate does not satisfy
PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.
```

The recorded verdict is:

```text
REJECT_BANK_REPLACEMENT.
```

## 4. Proof

PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED remains an A2 continuation of
the conservative two-place bank route. The separator must refine the
B0_p and B0_q comb, address, count, and guard data, not discard them
and restart from a larger global object.

Assume the covered class. The separator is internal and
control-excluded, but the construction obtains those properties only
after replacing one of the two banks or demoting the banks to passive
readout shadows. Then the pair is no longer a conservative
two-place residual refinement. It is a new source whose relation to
the B0 calibration floor is not load-bearing.

This violates the bank-preservation clause inherited from docs 89,
130, 143, 180, 182, and 184. Therefore the candidate does not satisfy PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED.

## 5. Surviving Escape

PFV2-ADELIC-LOCAL is still live only through
PFV2-GPF-RMON-EFFSEP-BANKED.

The surviving target is:

```text
PFV2-GPF-RMON-EFFSEP-BANKED.
```

It must prove that B0_p and B0_q embed conservatively before
`sep_G^{fib}` is constructed or consumed, and that their
comb/address/count/guard data remain load-bearing source data.

## 6. Kill Conditions

A future proposal is killed by this no-go only when bank replacement
is explicit:

```text
KILL-EFFSEP-BANK.1 bank deletion
  B0_p or B0_q is removed before separator construction.

KILL-EFFSEP-BANK.2 passive bank shadow
  the banks appear only as readout shadows after a new global source is
  formed.

KILL-EFFSEP-BANK.3 guard loss
  the Epstein replacement guard is not preserved in the separator
  source.

KILL-EFFSEP-BANK.4 non-load-bearing embedding
  the banks embed, but changing/removing them does not affect
  sep_G^{fib}, kappa_G^{sep}, or downstream data.
```

Do not apply this no-go against a separator with a conservative bank
embedding theorem before first separator use.

## 7. Board Update

```text
PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED:
  REJECT_BANK_REPLACEMENT for separator sources that replace or erase
  the B0_p/B0_q banks.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-EFFSEP-BANKED.

A2 witness:
  still not licensed.
```
