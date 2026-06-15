# 167 - PFV2 GPF effective descent collapse

Status: bounded no-go from the PFV2-GPF-SELECT target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only
p,q+complement GPF local sources that are ordinary effective-descent
presentations equivalent to all-places objects with p,q marking.

## 1. Purpose

Doc 166 writes the local source:

```text
PFV2-GPF-LOCAL(p,q).
```

The first selection failure is ordinary effective descent: the source
may be written before assembly, but be equivalent to the category of
assembled all-places objects plus p,q marking. This document rejects
that class.

## 2. Covered Class

Call a proposal `PFV2_GPF_effective` if it satisfies all of:

```text
D167.1 local GPF source syntax
  The proposal names S_{p,q}^G with p and q towers, complement,
  GPF_{p,q}, Eff_{p,q}, and gamma_G before an assembly functor.

D167.2 effective descent equivalence
  The assembly functor identifies S_{p,q}^G with all-places objects D
  equipped with p,q marking and complement readout.

D167.3 no residual local datum
  GPF_{p,q}, Eff_{p,q}, and gamma_G are fully recovered from D plus
  p,q marking.

D167.4 inherited first map
  kappa_G factors through D plus the marking/readout.

D167.5 downstream sees only D
  M_C/F_C/Tr_L sees D, scalar PF, or p,q marking, but not extra local
  source data.
```

This class includes:

```text
descent presentations equivalent to all-places GPF towers;
gluing data whose only role is reconstructing D;
local source categories that are stacks for the all-places object;
assembly equivalences with no residual p,q+complement data.
```

## 3. Lemma

### Lemma 167.1

`PFV2_GPF_effective` does not satisfy PFV2-GPF-SELECT.

Verdict:

```text
REJECT_GPF_EFFECTIVE_DESCENT
  if S_{p,q}^G is equivalent to all-places objects with p,q marking.

REJECT_GPF_INHERITED_MAP
  if kappa_G factors through D plus marking/readout.

REJECT_GPF_DOWNSTREAM_ERASURE
  if downstream sees only D, scalar PF, or p,q marking.

HOLD_GPF_RESIDUAL
  if a later proposal supplies residual p,q+complement GPF data not
  recovered from D plus marking.
```

### Proof

PFV2-GPF-SELECT requires the p,q+complement GPF source to be
non-equivalent to all-places marking, control-selective,
bank-preserving, and downstream load-bearing.

Under D167.1-D167.2, the source has the right syntax but not the right
mathematical content. It is an effective-descent presentation of D with
p,q marking. This is the same obstruction as docs 152 and 165 in the
new GPF-local language.

Under D167.3, no residual local source datum survives assembly. Thus
GPF_{p,q}, Eff_{p,q}, and gamma_G are presentation data, not a
source-selective object.

Under D167.4, the first map is inherited from D plus marking/readout.
It is not a first carrier-consuming map.

Under D167.5, downstream dependence fails. Doc 111 rejects a strict
prefix whose consumed primitive field is forgotten before M_C/F_C/Tr_L.

Therefore ordinary effective-descent GPF local sources do not satisfy
PFV2-GPF-SELECT. QED.

## 4. What Effective Descent Still Supplies

Allowed:

```text
checking formation order;
notation for assembly and gluing;
comparison tests for residual proposals;
post-pass compatibility diagnostics if a stricter source passes.
```

Not allowed:

```text
claiming PFV2-GPF-SELECT;
claiming FIRST_MAP_PASS;
claiming p,q source selectivity;
promoting presentation data to residual source data;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 GPF-local route is:

```text
PFV2-GPF-RESIDUAL.
```

The target:

```text
There is residual p,q+complement GPF data rho_G inside S_{p,q}^G such
that:

1. rho_G is not recovered from all-places D plus p,q marking;
2. kappa_G consumes rho_G before assembly;
3. Epstein/DH controls cannot instantiate rho_G or kappa_G while
   retaining theta/count shadows;
4. B0_p and B0_q embed conservatively before rho_G is consumed;
5. rho_G remains load-bearing downstream in M_C/F_C/Tr_L.
```

This is narrower than PFV2-GPF-SELECT because it demands residual
local GPF data not erased by effective assembly.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named residual `rho_G` proposal
if one proves:

```text
KILL-GPF-RES.1 marking collapse
  rho_G is only p,q marking, complement bookkeeping, or scalar PF.

KILL-GPF-RES.2 presentation collapse
  rho_G is only descent presentation data for D.

KILL-GPF-RES.3 control formability
  Epstein/DH controls can instantiate rho_G and kappa_G while retaining
  theta/count shadows.

KILL-GPF-RES.4 bank replacement
  rho_G requires replacing B0_p/B0_q by a full global source.

KILL-GPF-RES.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_G.
```

Do not apply these beyond a named residual GPF-local datum.

## 7. Board Update

```text
PFV2_GPF_effective:
  REJECT_GPF_EFFECTIVE_DESCENT.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RESIDUAL or another local GPF source
  with non-erased p,q+complement data.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 166
  Supplies PFV2-GPF-LOCAL(p,q) and the PFV2-GPF-SELECT target.

doc 165
  Rejects all-places-first GPF readouts.

doc 152
  Rejects ordinary effective descent in the earlier PFV2-DESC thread.

doc 111
  Still blocks downstream forgetfulness.
```
