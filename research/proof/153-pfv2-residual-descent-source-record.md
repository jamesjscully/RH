# 153 - PFV2 residual descent source record

Status: concrete PFV2-DESC-RESIDUAL candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a broad no-go. It makes the
residual descent datum from doc 152 explicit.

## 1. Purpose

Doc 152 rejects ordinary effective descent. The remaining PFV2 descent
route must supply residual data:

```text
rho
```

that are not erased by assembly and not equivalent to p,q marking or
complement bookkeeping.

This document writes the smallest honest residual record and runs the
existing gates.

## 2. Candidate Record

Name:

```text
PFV2-RES(p,q).
```

Proposed source object:

```text
Desc_{p,q}^{rho}
```

with fields:

```text
T_p, T_q, C_{not p,q}
  the pre-global p, q, and complement source data from doc 151.

gamma
  gluing compatibility data.

pf_desc
  product-formula descent certificate.

rho
  residual descent datum: an obstruction, defect, torsor class,
  extension class, automorphism class, cocycle class, or coherence
  datum attached to the p,q+complement gluing problem.
```

The intended assembly relation is:

```text
Assemble(Desc_{p,q}^{rho}) = (D, rho_image)
```

where `rho_image` is not erased by the all-places object D and is not
equivalent to p,q marking.

The intended first map is:

```text
kappa_rho : Desc_{p,q}^{rho} -> Y_{p,q}^{rho}
```

and it must consume:

```text
(T_p, T_q, C_{not p,q}, gamma, pf_desc, rho)
```

before all-places assembly, trace, determinant, kernel, mixed object,
or positivity.

## 3. Candidate Subfamilies

The residual slot `rho` has several possible semantic homes:

```text
R153.1 obstruction class
  rho measures failure or ambiguity of gluing T_p, T_q, and
  C_{not p,q}.

R153.2 torsor/extension class
  rho is a torsor or extension datum for the relative p,q+complement
  assembly problem.

R153.3 automorphism/coherence class
  rho records nontrivial automorphisms or coherence data of descent not
  visible in the assembled object.

R153.4 defect current
  rho is a residual product-formula defect that is object data before
  assembly and is not a scalar complement.
```

This document does not choose among these. It asks what any such
residual must satisfy.

## 4. Gate Run

### Gate 153.1 - Residual non-erasure

Verdict:

```text
HOLD_RESIDUAL_NONERASURE
```

Reason: no theorem has been named showing that `rho` survives assembly
as more than p,q marking, complement bookkeeping, or an isomorphic copy
of D. This is the first required theorem.

### Gate 153.2 - Source priority

Verdict:

```text
LOCAL_SCHEMA_PASS
```

Reason: the record places `rho` inside `Desc_{p,q}^{rho}` before
assembly. This is a schema pass only.

### Gate 153.3 - Control non-formability

Verdict:

```text
HOLD_CONTROL_RESIDUAL
```

Reason: if `rho` is an abstract cocycle, torsor, coherence, or defect
label attachable to any theta/count shadow, Epstein/DH controls may
form it. The route needs a theorem that the same residual datum is
meaningful only for the carrier source.

### Gate 153.4 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: `rho` must not require replacing B0_p and B0_q by the full
global source before the bank embeds. If `rho` exists only after global
assembly, doc 150 applies.

### Gate 153.5 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that `rho` remains load-bearing in M_C,
F_C, or Tr_L. If downstream sees only D, p,q marking, or a scalar
defect, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-RES(p,q):
  LOCAL_SCHEMA_PASS;
  HOLD_RESIDUAL_NONERASURE;
  HOLD_CONTROL_RESIDUAL;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-DESC-RESIDUAL:
  SHARPEN to PFV2-RHO-SELECT.

A2 witness:
  still not licensed.
```

This is progress only as a sharper source record. It does not yet pass
PFV2 or license computation.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-RHO-SELECT.
```

The theorem:

```text
There is a residual descent datum rho inside Desc_{p,q}^{rho} such
that:

1. rho is not erased by assembly;
2. rho is not equivalent to p,q marking or complement bookkeeping;
3. kappa_rho consumes rho before all-places assembly;
4. Epstein/DH controls cannot form rho or kappa_rho while preserving
   their theta/count shadows;
5. B0_p and B0_q embed conservatively before rho is consumed;
6. rho remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-DESC-RESIDUAL and is paid for by
the PFV2-RES shot.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named residual class if one
proves:

```text
KILL-RHO.1 marking collapse
  rho is equivalent to p,q marking, complement bookkeeping, or a scalar
  defect.

KILL-RHO.2 control formability
  Epstein/DH controls can form the same rho and kappa_rho while
  retaining theta/count shadows.

KILL-RHO.3 post-assembly origin
  rho exists only after all-places assembly or a post-global reflector.

KILL-RHO.4 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho.
```

Do not generalize these beyond the named residual class.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  residual descent is the current best concrete shot;
  source-priority schema locally passes;
  residual non-erasure, control selectivity, bank preservation, and
  downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-RHO-SELECT.
```

## 9. Relation To Existing Docs

```text
doc 151
  Supplies PFV2-DESC(p,q).

doc 152
  Rejects ordinary effective descent and names residual descent data.

doc 111
  Still blocks downstream forgetfulness.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```

## 10. Post-doc-154 Update

Doc 154 rejects bookkeeping residuals:

```text
PFV2_RHO_marking:
  REJECT_RHO_MARKING.
```

The surviving target is:

```text
PFV2-RHO-NONTRIVIAL.
```

Thus PFV2-RHO-SELECT remains the enclosing target, but future work
should ask for nontrivial obstruction, torsor, extension, automorphism,
cocycle, or coherence content, not p,q marking, complement
bookkeeping, or scalar defect data.
