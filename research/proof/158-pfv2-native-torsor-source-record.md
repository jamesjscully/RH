# 158 - PFV2 native torsor source record

Status: concrete PFV2-TOR-NATIVE candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a broad no-go. It writes the
smallest honest source record for the surviving carrier-native
torsor/extension/cocycle route left by doc 157.

## 1. Purpose

Doc 157 rejects torsor, extension, cocycle, automorphism, and coherence
data when they are only gauge, presentation, ordinary decoration, or
post-assembly labels. The remaining route is:

```text
PFV2-TOR-NATIVE.
```

This document takes that shot directly. The goal is not to prove the
route, but to specify the least object that would count.

## 2. Candidate Record

Name:

```text
PFV2-NATIVE-TOR(p,q).
```

Proposed source object:

```text
TorDesc_{p,q}
```

with fields:

```text
T_p, T_q, C_{not p,q}
  the pre-global p, q, and complement source data.

gamma
  gluing compatibility data.

pf_desc
  product-formula descent certificate.

G_car
  a carrier-native band, extension group, or automorphism/coherence
  groupoid defined from the pre-global carrier data.

tau_car
  a G_car-torsor, extension, cocycle, or coherence class whose
  existence is part of TorDesc_{p,q}.

lambda_car
  a carrier tag proving that G_car and tau_car are not definable from
  an already assembled all-places object D plus p,q marking.

bank_iota
  conservative embeddings of B0_p and B0_q into TorDesc_{p,q} before
  tau_car is consumed.

surv
  a named survival/visibility map recording where tau_car remains
  object data after successful assembly and inside M_C/F_C/Tr_L.
```

The intended assembly relation is:

```text
Assemble(TorDesc_{p,q}) = (D, tau_image)
```

where `tau_image` is the image of prior carrier-native data, not the
definition of the data.

The intended first map is:

```text
kappa_car : TorDesc_{p,q} -> Y_{p,q}^{car}
```

and it must consume:

```text
(G_car, tau_car, lambda_car, bank_iota, surv)
```

before all-places assembly, trace, determinant, kernel, mixed object,
positivity, or post-global reflection.

## 3. What Makes This A Real Shot

This candidate is stricter than PFV2-RHO-TOR(p,q):

```text
not decorative:
  tau_car is not a torsor of trivializations, a presentation of D, an
  ordinary cohomology label on D, or a coherence witness for a diagram
  controls can also decorate.

not post-assembly:
  G_car and tau_car are fields of TorDesc_{p,q}; they are not produced
  after choosing D.

not merely marked descent:
  lambda_car is not p,q marking, complement bookkeeping, or a scalar
  product-formula defect.

not control-neutral:
  the band/action/cocycle must depend on the Euler carrier source, not
  only on abstract local pieces or theta/count shadows.

not first-map inert:
  kappa_car must be undefined, inequivalent, or lose target structure
  if tau_car is removed, trivialized, or replaced by decoration on D.
```

Thus the shot reaches the side of doc 157 that remained open.

## 4. Gate Run

### Gate 158.1 - Native position

Verdict:

```text
LOCAL_NATIVE_POSITION_PASS
```

Reason: the record places `G_car`, `tau_car`, and `lambda_car` inside
the pre-assembly object. This passes the formation-order schema only.

It is not an existence theorem. A later proposal must name the actual
carrier-native band/groupoid and torsor class.

### Gate 158.2 - Carrier-native existence

Verdict:

```text
HOLD_NATIVE_EXISTENCE
```

Reason: no named source category has yet supplied `G_car` and
`tau_car`. The present record states the required slot, but does not
construct the object.

### Gate 158.3 - Non-decoration

Verdict:

```text
HOLD_NONDECORATION
```

Reason: no theorem has shown that `tau_car` is not equivalent to an
ordinary torsor, extension, cocycle, automorphism label, or coherence
witness attached to D after assembly.

### Gate 158.4 - Control non-formability

Verdict:

```text
HOLD_CONTROL_CARRIER_TOR
```

Reason: if `G_car` is any broad band/groupoid that Epstein or DH
shadows can also instantiate while retaining theta/count shadows, doc
157 does not help. The theorem must exclude controls for the named
native band and the first map `kappa_car`.

### Gate 158.5 - First-map dependence

Verdict:

```text
HOLD_FIRST_MAP_DEPENDENCE
```

Reason: no theorem has yet shown that changing `tau_car` while holding
the assembled object, p,q marking, and complement bookkeeping fixed
changes `kappa_car`. If the map factors through D plus an inert label,
doc 157 applies.

### Gate 158.6 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the native torsor must not require replacing B0_p and B0_q by
the full global source before embedding. If `G_car` or `tau_car`
exists only after full assembly, doc 150 applies.

### Gate 158.7 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that M_C, F_C, or Tr_L consumes
`tau_car` as load-bearing source data. If downstream only sees D,
p,q marking, or a forgotten torsor label, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-NATIVE-TOR(p,q):
  LOCAL_NATIVE_POSITION_PASS;
  HOLD_NATIVE_EXISTENCE;
  HOLD_NONDECORATION;
  HOLD_CONTROL_CARRIER_TOR;
  HOLD_FIRST_MAP_DEPENDENCE;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-TOR-NATIVE:
  SHARPEN to PFV2-TOR-CARRIER.

A2 witness:
  still not licensed.
```

This is construction progress only as a precise source record. It
does not yet pass PFV2 and does not license computation.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-TOR-CARRIER.
```

The theorem:

```text
There is a named carrier-native band, extension group, or
automorphism/coherence groupoid G_car and a class tau_car inside
TorDesc_{p,q} such that:

1. G_car and tau_car exist before all-places assembly;
2. tau_car is not equivalent to a decoration, gauge, presentation, or
   ordinary cohomology label on the assembled object D;
3. kappa_car consumes tau_car before assembly;
4. changing tau_car while holding D, p,q marking, and complement
   bookkeeping fixed changes kappa_car;
5. Epstein/DH controls cannot form the same G_car, tau_car, or
   kappa_car while preserving theta/count shadows;
6. B0_p and B0_q embed conservatively before tau_car is consumed;
7. tau_car remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-TOR-NATIVE because it asks for a
named carrier-native band and class, not merely the abstract existence
of some non-decorative torsor.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `G_car, tau_car` proposal
if one proves:

```text
KILL-CAR-TOR.1 no native source
  G_car or tau_car cannot be defined before all-places assembly.

KILL-CAR-TOR.2 decoration collapse
  tau_car is equivalent to an ordinary decoration, gauge,
  presentation, cohomology label, automorphism label, or coherence
  witness of D.

KILL-CAR-TOR.3 control formability
  Epstein/DH shadows can form the same G_car, tau_car, and kappa_car
  while retaining theta/count shadows.

KILL-CAR-TOR.4 inherited first map
  kappa_car factors through D plus an inert torsor label or
  representative choice.

KILL-CAR-TOR.5 bank replacement
  G_car or tau_car requires replacing B0_p/B0_q by the full global
  source.

KILL-CAR-TOR.6 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_car or sees it only as an
  inert label.
```

Do not apply these to all torsor/extension/cocycle attempts without a
theorem covering their native band or groupoid.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  the active construction-facing shot is a named carrier-native
  torsor source record;
  formation order locally passes;
  native existence, non-decoration, control selectivity, first-map
  dependence, bank preservation, and downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-TOR-CARRIER.
```

## 9. Relation To Existing Docs

```text
doc 157
  Rejects decorative torsor/extension/cocycle residuals and leaves
  PFV2-TOR-NATIVE.

doc 156
  Supplies the torsor/extension/cocycle residual shot.

doc 153
  Supplies the residual descent source slot.

doc 151
  Supplies the pre-global descent formation order.

doc 150
  Still rejects post-global relative reflection.

doc 111
  Still blocks downstream forgetfulness.
```
