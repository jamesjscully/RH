# 156 - PFV2 rho torsor-extension shot

Status: concrete PFV2-RHO-SURVIVES candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a broad no-go. It tests the
most plausible surviving rho family after docs 154-155: torsor,
extension, cocycle, and coherence data.

## 1. Purpose

Doc 155 leaves residual data that survive successful assembly:

```text
torsor;
extension;
automorphism;
cocycle;
coherence;
surviving non-scalar obstruction.
```

This document takes the direct shot at the torsor/extension/cocycle
subfamily. The goal is to decide whether it can be a source-selective
PFV2 residual, or whether it is ordinary cohomological decoration.

## 2. Candidate Record

Name:

```text
PFV2-RHO-TOR(p,q).
```

Proposed source object:

```text
Desc_{p,q}^{tor}
```

with fields:

```text
T_p, T_q, C_{not p,q}
  the pre-global p, q, and complement source data.

gamma
  gluing compatibility data.

pf_desc
  product-formula descent certificate.

rho_tor
  a torsor, extension, cocycle, or coherence class attached to the
  p,q+complement gluing problem.
```

The intended assembly is:

```text
Assemble(Desc_{p,q}^{tor}) = (D, rho_tor)
```

where `rho_tor` remains object data after assembly, not just a
presentation of D.

The intended first map is:

```text
kappa_tor : Desc_{p,q}^{tor} -> Y_{p,q}^{tor}
```

and it must consume `rho_tor` before all-places assembly, trace,
determinant, kernel, mixed object, or positivity.

## 3. Local Promise

This candidate is better than scalar residuals if all of the following
are true:

```text
1. rho_tor is not equivalent to p,q marking or complement degree;
2. rho_tor survives successful assembly;
3. rho_tor is non-scalar object data;
4. kappa_tor consumes rho_tor before assembly;
5. rho_tor can plausibly remain visible downstream.
```

It is the first residual subfamily that could survive doc 155.

## 4. Gate Run

### Gate 156.1 - Nontrivial residual class

Verdict:

```text
LOCAL_RHO_CLASS_PASS
```

Reason: torsor, extension, cocycle, and coherence classes can be
genuine non-scalar residual data. This passes the doc-154
marking/scalar filter at the schema level.

### Gate 156.2 - Survival through assembly

Verdict:

```text
HOLD_SURVIVAL
```

Reason: no theorem has been named showing that `rho_tor` remains
object data after successful assembly rather than becoming an
isomorphic presentation, gauge choice, or ordinary cohomology label
forgotten by the assembled object.

### Gate 156.3 - Control non-formability

Verdict:

```text
HOLD_CONTROL_TORSOR
```

Reason: torsors, extensions, cocycles, and coherence classes are broad
categorical structures. Epstein/DH shadows may be able to carry the
same kind of torsor/cocycle decoration while retaining theta/count
shadows. PFV2 needs a theorem that the specific rho_tor is meaningful
only for the carrier source.

### Gate 156.4 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: `rho_tor` must not require replacing B0_p and B0_q by the full
global source before embedding. If the torsor/extension class exists
only after global assembly, doc 150 applies.

### Gate 156.5 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that M_C, F_C, or Tr_L sees rho_tor as
load-bearing object data. If downstream forgets the torsor/extension
class, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-RHO-TOR(p,q):
  LOCAL_RHO_CLASS_PASS;
  HOLD_SURVIVAL;
  HOLD_CONTROL_TORSOR;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-RHO-SURVIVES:
  SHARPEN to PFV2-TOR-SELECT.

A2 witness:
  still not licensed.
```

This is a live construction-facing candidate, not a pass.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-TOR-SELECT.
```

The theorem:

```text
There is a torsor, extension, cocycle, or coherence residual
rho_tor inside Desc_{p,q}^{tor} such that:

1. rho_tor survives successful assembly as object data;
2. rho_tor is not an isomorphic presentation, gauge choice, or ordinary
   decoration of D;
3. kappa_tor consumes rho_tor before assembly;
4. Epstein/DH controls cannot form rho_tor or kappa_tor while
   preserving theta/count shadows;
5. B0_p and B0_q embed conservatively before rho_tor is consumed;
6. rho_tor remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-RHO-SURVIVES and is paid for by the
PFV2-RHO-TOR shot.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named torsor/extension/cocycle
class if one proves:

```text
KILL-TOR.1 decoration collapse
  rho_tor is only a gauge choice, presentation, or ordinary cohomology
  decoration of D.

KILL-TOR.2 control formability
  Epstein/DH shadows can form the same rho_tor and kappa_tor while
  retaining theta/count shadows.

KILL-TOR.3 post-assembly origin
  rho_tor exists only after all-places assembly or post-global
  reflection.

KILL-TOR.4 bank replacement
  rho_tor requires replacing B0_p/B0_q by the full global source.

KILL-TOR.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_tor.
```

Do not apply these beyond the named torsor/extension/cocycle class.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  torsor/extension/cocycle residual is the current best concrete shot;
  nontrivial residual class locally passes;
  survival, control selectivity, bank preservation, and downstream
  dependence remain HOLD.

Immediate theorem target:
  PFV2-TOR-SELECT.
```

## 9. Relation To Existing Docs

```text
doc 154
  Rejects marking/bookkeeping/scalar residuals.

doc 155
  Rejects vanishing obstruction/scalar defect residuals.

doc 153
  Supplies the residual source record.

doc 111
  Still blocks downstream forgetfulness.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```

## 10. Post-doc-157 Update

Doc 157 rejects decorative torsor/extension/cocycle residuals:

```text
PFV2_TOR_decor:
  REJECT_TOR_DECORATION.
```

The surviving target is:

```text
PFV2-TOR-NATIVE.
```

Thus PFV2-TOR-SELECT remains the enclosing target, but future work
should ask for a carrier-native torsor, extension, cocycle,
automorphism, or coherence datum whose existence is part of
Desc_{p,q}^{tor} before assembly, not a decoration of the assembled
object.
