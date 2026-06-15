# 166 - PFV2 GPF local source shot

Status: concrete PFV2-GPF-LOCAL candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a no-go. It writes the smallest
p,q+complement global product-formula tower source left by doc 165.

## 1. Purpose

Doc 165 rejects all-places-first global PF tower readouts. The
remaining target is:

```text
PFV2-GPF-LOCAL.
```

The target must form a p,q+complement source before any all-places
object D exists. This document writes the local source record.

## 2. Candidate Record

Name:

```text
PFV2-GPF-LOCAL(p,q).
```

Proposed source object:

```text
S_{p,q}^G in ECar_L1^{GPF,pq}
```

Fields:

```text
A_p, A_q
  B0_p and B0_q one-place carrier records.

alpha_p, alpha_q
  distinguished prime-power atoms.

Comb_p, Comb_q
  effective prime-power combs.

v_p, v_q
  valuation/tower maps on the combs.

ell_p, ell_q
  structural lengths ell_p=log p and ell_q=log q.

C_{not p,q}
  structural complement source, not scalar bookkeeping.

GPF_{p,q}
  p,q+complement global product-formula tower axiom. It is part of the
  source definition of S_{p,q}^G.

Eff_{p,q}
  effectivity data internal to GPF_{p,q}.

gamma_G
  pre-assembly gluing/descent compatibility for the p,q towers and
  complement.

bank_iota
  conservative embeddings of B0_p and B0_q before kappa_G.

surv_G
  survival/visibility data for GPF_{p,q} or a future torsor class
  downstream in M_C/F_C/Tr_L.
```

Assembly, if legal, is a later operation:

```text
Assemble(S_{p,q}^G) = D.
```

The intended first map is:

```text
kappa_G : S_{p,q}^G -> Y_G.
```

It must consume:

```text
(GPF_{p,q}, Eff_{p,q}, gamma_G)
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is Not The All-Places Class

This shot requires:

```text
source before assembly:
  S_{p,q}^G is not selected from D.

structural complement:
  C_{not p,q} is object data, not a residual scalar degree.

local global-PF axiom:
  GPF_{p,q} binds p, q, and complement inside the source definition.

later D:
  D may be assembled from S_{p,q}^G; D is not the input.
```

Thus the shot reaches the side of doc 165 that remained open.

## 4. Gate Run

### Gate 166.1 - Local source priority

Verdict:

```text
LOCAL_GPF_SOURCE_SCHEMA_PASS
```

Reason: the record forms `S_{p,q}^G` before all-places assembly and
places `GPF_{p,q}` inside the source.

This is only a schema pass. It does not construct
`ECar_L1^{GPF,pq}`.

### Gate 166.2 - Complement structurality

Verdict:

```text
LOCAL_COMPLEMENT_SCHEMA_PASS
```

Reason: the record requires a structural complement source rather than
a scalar remaining-degree slot.

This is not a theorem that such a complement exists.

### Gate 166.3 - Axiom existence

Verdict:

```text
HOLD_GPF_LOCAL_AXIOM
```

Reason: no mathematical category or axiom has been named that makes
`GPF_{p,q}` source data.

### Gate 166.4 - Non-equivalence to all-places objects

Verdict:

```text
HOLD_NOT_ALLPLACES_EQUIV
```

Reason: no theorem has shown that `S_{p,q}^G` is not equivalent to
all-places objects with p,q marking. If it is equivalent, doc 165
applies.

### Gate 166.5 - Control exclusion

Verdict:

```text
HOLD_CONTROL_GPF_LOCAL
```

Reason: no theorem has shown that Epstein/DH controls cannot
instantiate `S_{p,q}^G` and `kappa_G` while retaining theta/count
shadows.

### Gate 166.6 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the source must embed B0_p and B0_q conservatively. If it
replaces them by a new global source, doc 130's KILL-A2.5 applies.

### Gate 166.7 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes
`GPF_{p,q}`, `Eff_{p,q}`, or a resulting torsor as load-bearing data.
If downstream only sees D or scalar PF, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-GPF-LOCAL(p,q):
  LOCAL_GPF_SOURCE_SCHEMA_PASS;
  LOCAL_COMPLEMENT_SCHEMA_PASS;
  HOLD_GPF_LOCAL_AXIOM;
  HOLD_NOT_ALLPLACES_EQUIV;
  HOLD_CONTROL_GPF_LOCAL;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-GPF-LOCAL:
  SHARPEN to PFV2-GPF-SELECT.

A2 witness:
  still not licensed.
```

This is construction progress only as a source record. It states the
object that would be needed before a witness or FIRST_MAP_PASS is
meaningful.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GPF-SELECT.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF,pq} with objects
S_{p,q}^G such that:

1. S_{p,q}^G contains p and q effective towers, structural lengths, a
   structural complement, p,q+complement product-formula axiom, and
   effectivity data before all-places assembly;
2. S_{p,q}^G is not equivalent to all-places objects with p,q marking;
3. kappa_G consumes GPF_{p,q}, Eff_{p,q}, or gamma_G before assembly;
4. Epstein/DH controls cannot instantiate S_{p,q}^G or kappa_G while
   retaining theta/count shadows;
5. B0_p and B0_q embed conservatively into S_{p,q}^G;
6. GPF_{p,q}, Eff_{p,q}, gamma_G, or a resulting torsor remains
   load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-GPF-LOCAL because it adds
selectivity, non-equivalence, bank, and downstream obligations to the
local source record.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `S_{p,q}^G` proposal if one
proves:

```text
KILL-GPF-SELECT.1 all-places equivalence
  S_{p,q}^G is equivalent to all-places objects with p,q marking.

KILL-GPF-SELECT.2 marked tower collapse
  S_{p,q}^G unfolds into marked monoids, independent UFD towers, or a
  later PF relation.

KILL-GPF-SELECT.3 control formability
  Epstein/DH controls can instantiate S_{p,q}^G and kappa_G while
  retaining theta/count shadows.

KILL-GPF-SELECT.4 bank replacement
  S_{p,q}^G replaces B0_p/B0_q instead of embedding them
  conservatively.

KILL-GPF-SELECT.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets GPF_{p,q} and sees only D or scalar
  PF.
```

Do not apply these beyond a named p,q+complement global PF tower
source.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  the active construction-facing shot is now a p,q+complement global
  PF tower source formed before all-places assembly;
  local source priority and complement structurality locally pass;
  axiom existence, non-equivalence, control exclusion, bank
  preservation, and downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-GPF-SELECT.
```

## 9. Relation To Existing Docs

```text
doc 165
  Rejects all-places-first global PF tower readouts and leaves
  PFV2-GPF-LOCAL.

doc 164
  Supplies the global PF tower source shot.

doc 151
  Supplies the pre-global descent formation discipline.

doc 143
  Supplies the PFV2_local_record calibration object.

doc 103
  Still requires a first carrier-consuming map.

doc 111
  Still blocks downstream forgetfulness.
```
