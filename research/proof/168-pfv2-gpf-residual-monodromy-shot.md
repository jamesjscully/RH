# 168 - PFV2 GPF residual monodromy shot

Status: concrete PFV2-GPF-RESIDUAL candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a no-go. It writes the smallest
named residual local GPF datum left by doc 167.

## 1. Purpose

Doc 167 rejects GPF local sources that are only effective-descent
presentations of all-places objects with p,q marking. The remaining
target is:

```text
PFV2-GPF-RESIDUAL.
```

The target cannot be met by saying that `S_{p,q}^G` has more notation
than the assembled object. It must name residual local GPF data that is
not recovered from all-places `D` plus p,q marking.

This document takes the direct shot: residual p,q+complement monodromy
inside the GPF source.

## 2. Candidate Record

Name:

```text
PFV2-GPF-RMON(p,q).
```

Proposed source object:

```text
S_{p,q}^{G,rho} in ECar_L1^{GPF,pq,rho}
```

Fields inherited from doc 166:

```text
A_p, A_q
  B0_p and B0_q one-place carrier records.

Comb_p, Comb_q
  effective prime-power combs.

v_p, v_q, ell_p, ell_q
  valuation/tower maps and structural lengths ell_p=log p,
  ell_q=log q.

C_{not p,q}
  structural complement source.

GPF_{p,q}, Eff_{p,q}, gamma_G
  p,q+complement global product-formula tower axiom, effectivity data,
  and pre-assembly gluing/descent compatibility.

bank_iota
  conservative embeddings of B0_p and B0_q before kappa_G.

surv_G
  downstream visibility data for GPF source fields.
```

New residual field:

```text
rho_G^{mon}
  a source-native monodromy, extension, or action class measuring how
  the p and q tower operations act on the structural complement while
  preserving GPF_{p,q} and Eff_{p,q}.
```

The intended point is not that every gluing has monodromy. The point is
that a legal residual candidate must supply a class whose definition
uses the simultaneous p,q+complement GPF source before assembly.

The intended first map is:

```text
kappa_G^{mon} : S_{p,q}^{G,rho} -> Y_G^{mon}.
```

It must consume:

```text
(rho_G^{mon}, GPF_{p,q}, Eff_{p,q}, gamma_G)
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is A Real Shot

This shot is stricter than doc 166 and responds directly to doc 167:

```text
not effective descent:
  rho_G^{mon} is not recovered from D plus p,q marking.

not ordinary presentation data:
  rho_G^{mon} is not the torsor of choices of descent presentation,
  a gauge of gamma_G, or a coherence witness for assembling D.

not scalar product-formula bookkeeping:
  rho_G^{mon} is an action/extension class tied to the complement,
  not the statement that the p,q valuations balance the other places.

not bank replacement:
  B0_p and B0_q must embed before rho_G^{mon} is consumed.

not downstream inert:
  M_C/F_C/Tr_L must see the monodromy class as load-bearing data,
  not only the assembled D or scalar PF.
```

Thus the shot reaches the side of doc 167 that remained open without
claiming a construction.

## 4. Gate Run

### Gate 168.1 - Residual source placement

Verdict:

```text
LOCAL_GPF_RESIDUAL_SCHEMA_PASS
```

Reason: the record places a named `rho_G^{mon}` inside the
pre-assembly GPF source and makes it part of the first-map input.

This is only a schema pass. It does not construct
`ECar_L1^{GPF,pq,rho}` or prove that such monodromy exists.

### Gate 168.2 - Native monodromy existence

Verdict:

```text
HOLD_RMON_EXISTENCE
```

Reason: no mathematical source category has yet supplied a genuine
monodromy, extension, or action class on the p,q+complement GPF source.
The phrase must become a construction or theorem, not a label.

### Gate 168.3 - Non-presentation

Verdict:

```text
HOLD_RMON_NONPRESENTATION
```

Reason: no theorem has shown that `rho_G^{mon}` is not equivalent to
descent presentation data, a gauge of `gamma_G`, or an ordinary
coherence witness for all-places assembly.

### Gate 168.4 - Control exclusion

Verdict:

```text
HOLD_RMON_CONTROL_EXCLUSION
```

Reason: no theorem has shown that Epstein/DH controls cannot
instantiate the same monodromy/action field while retaining
theta/count shadows. A broad groupoid of compatible local actions
would still be control-formable.

### Gate 168.5 - First-map dependence

Verdict:

```text
HOLD_RMON_FIRST_MAP
```

Reason: no theorem has constructed `kappa_G^{mon}` or shown that
changing `rho_G^{mon}` while holding `D`, p,q marking, and complement
bookkeeping fixed changes the first map or its target.

### Gate 168.6 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the monodromy source must preserve the B0_p and B0_q comb,
address, count, and guard data. If the class exists only after
replacing the banks by a full global source, docs 150 and 165 apply.

### Gate 168.7 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes
`rho_G^{mon}` as load-bearing source data. If downstream only sees the
assembled object, scalar product-formula balance, or p,q marking, doc
111 rejects the route.

## 5. Current Verdict

```text
PFV2-GPF-RMON(p,q):
  LOCAL_GPF_RESIDUAL_SCHEMA_PASS;
  HOLD_RMON_EXISTENCE;
  HOLD_RMON_NONPRESENTATION;
  HOLD_RMON_CONTROL_EXCLUSION;
  HOLD_RMON_FIRST_MAP;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-GPF-RESIDUAL:
  SHARPEN to PFV2-GPF-RMON-SELECT.

A2 witness:
  still not licensed.
```

This is construction progress only as a named residual source record.
It narrows the next target to a monodromy/action class rather than an
unnamed residual slot.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GPF-RMON-SELECT.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF,pq,rho} with objects
S_{p,q}^{G,rho} and a class rho_G^{mon} such that:

1. rho_G^{mon} exists before all-places assembly inside the
   p,q+complement GPF source;
2. rho_G^{mon} is not recovered from all-places D plus p,q marking;
3. rho_G^{mon} is not merely descent presentation data, a gauge of
   gamma_G, or a coherence witness for assembly;
4. kappa_G^{mon} consumes rho_G^{mon} before assembly;
5. changing rho_G^{mon} while holding D, p,q marking, and complement
   bookkeeping fixed changes kappa_G^{mon} or its target;
6. Epstein/DH controls cannot instantiate rho_G^{mon} or
   kappa_G^{mon} while retaining theta/count shadows;
7. B0_p and B0_q embed conservatively before rho_G^{mon} is consumed;
8. rho_G^{mon} remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-GPF-RESIDUAL because it demands a
specific residual monodromy/action class.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `rho_G^{mon}` proposal if
one proves:

```text
KILL-RMON.1 no monodromy object
  The proposed source category does not define a monodromy, extension,
  or action class before all-places assembly.

KILL-RMON.2 presentation collapse
  rho_G^{mon} is only descent presentation data, a gauge of gamma_G, or
  a coherence witness for assembling D.

KILL-RMON.3 marking collapse
  rho_G^{mon} is recovered from D plus p,q marking and complement
  readout.

KILL-RMON.4 control formability
  Epstein/DH controls can instantiate rho_G^{mon} and kappa_G^{mon}
  while retaining theta/count shadows.

KILL-RMON.5 inherited first map
  kappa_G^{mon} factors through D plus p,q marking or through
  GPF_{p,q}, Eff_{p,q}, and gamma_G after forgetting rho_G^{mon}.

KILL-RMON.6 bank replacement
  rho_G^{mon} requires replacing B0_p/B0_q by a full global source.

KILL-RMON.7 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_G^{mon}.
```

Do not apply these beyond a named residual monodromy/action proposal.

## 8. Board Update

```text
PFV2-GPF-RMON(p,q):
  LOCAL_GPF_RESIDUAL_SCHEMA_PASS.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-SELECT or another residual
  p,q+complement GPF datum not recovered from all-places marking.

A2 witness:
  still not licensed.
```

## 9. Relation To Existing Docs

```text
doc 166
  Supplies PFV2-GPF-LOCAL(p,q), the source into which rho_G^{mon} is
  inserted.

doc 167
  Forces rho_G^{mon} to be residual, not effective-descent
  presentation data.

doc 158
  Explains why torsor/extension language must be carrier-native rather
  than decorative.

doc 160
  Explains why Euler/product-formula fields must define operations,
  not only scalar balance.

doc 111
  Still blocks downstream-erased strict prefixes.
```
