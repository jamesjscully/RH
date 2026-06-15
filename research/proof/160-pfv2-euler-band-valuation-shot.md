# 160 - PFV2 Euler-band valuation shot

Status: concrete PFV2-TOR-EULER-BAND candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a no-go. It tests the most
direct Euler-band candidate left by doc 159: a band built from the
product-formula valuation vector named in doc 130.

## 1. Purpose

Doc 159 rejects broadly functorial carrier-torsor packages. The
remaining target is:

```text
PFV2-TOR-EULER-BAND.
```

The target cannot be met by saying "some torsor exists." It must name
an Euler-carrier operation unavailable to Epstein/DH controls.

Doc 130 already names the primitive A2 field:

```text
(v_p, v_q; ell_p, ell_q; PF)
```

This document asks whether that field can define the required
Euler-carrier band.

## 2. Candidate Record

Name:

```text
PFV2-EULER-BAND(p,q).
```

Proposed source object:

```text
EBandDesc_{p,q}
```

with fields:

```text
T_p, T_q, C_{not p,q}
  the pre-global p, q, and complement source data.

gamma
  pre-assembly gluing compatibility.

pf_desc
  product-formula descent certificate.

V_PF
  the primitive product-formula valuation vector
  (v_p, v_q; ell_p, ell_q; PF), with ell_p=log p and ell_q=log q as
  structural length data.

G_E
  the proposed Euler valuation band: the groupoid of
  PF-compatible carrier-depth lifts of V_PF through
  (T_p, T_q, C_{not p,q}, gamma), preserving B0_p and B0_q.

tau_E
  the torsor of such PF-compatible carrier-depth lifts.

bank_iota
  conservative embeddings of B0_p and B0_q before tau_E is consumed.

surv_E
  a survival/visibility map showing where tau_E remains object data
  after assembly and in M_C/F_C/Tr_L.
```

The intended first map is:

```text
kappa_E : EBandDesc_{p,q} -> Y_E
```

and it must consume:

```text
(V_PF, G_E, tau_E)
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is The Direct Shot

This candidate is the direct successor to docs 130 and 159:

```text
doc 130
  names the primitive product-formula valuation vector and records
  FIRST_MAP_HOLD.

doc 159
  says a broad functorial band is control-formable and therefore not
  enough.

doc 160
  asks whether the product-formula valuation vector itself defines a
  non-broad Euler band.
```

The essential difference from a broad descent torsor is that `G_E` is
supposed to depend on the retained Euler valuation lengths
`ell_p=log p`, `ell_q=log q`, the carrier valuation maps `v_p, v_q`,
and the product-formula relation `PF` as object data.

## 4. Gate Run

### Gate 160.1 - Euler field placement

Verdict:

```text
LOCAL_EULER_FIELD_SCHEMA_PASS
```

Reason: the candidate places `V_PF` in the source object before
assembly and before the first map. This matches doc 130's intended
primitive field order.

This is not a theorem that `V_PF` is object data.

### Gate 160.2 - Euler band operation

Verdict:

```text
HOLD_EULER_BAND_OPERATION
```

Reason: no theorem has yet constructed `G_E` as a genuine band or
groupoid from `V_PF`. The phrase "PF-compatible carrier-depth lift"
must be made into a mathematical operation, not a label.

### Gate 160.3 - Non-broadness

Verdict:

```text
HOLD_NONBROAD_BAND
```

Reason: no theorem has shown that `G_E` is unavailable for arbitrary
p,q-marked local diagrams, assembled D plus labels, Epstein
represented-norm shadows, or DH coefficient/measure shadows. If
`G_E` is just a groupoid of compatible lifts for any local diagram,
doc 159 rejects it.

### Gate 160.4 - First-map dependence

Verdict:

```text
HOLD_KAPPA_E_DEPENDENCE
```

Reason: no map `kappa_E` has been constructed. The route needs a
theorem that changing `tau_E` while holding D, p,q marking, and
complement bookkeeping fixed changes the first map or its target.

### Gate 160.5 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the carrier-depth lift must preserve the B0_p and B0_q comb,
address, count, and guard data. If the lift exists only after replacing
the banks by a global source, doc 150 and doc 159 apply.

### Gate 160.6 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L sees `tau_E` as
load-bearing source data. If downstream only sees the assembled object
or the scalar product-formula constraint, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-EULER-BAND(p,q):
  LOCAL_EULER_FIELD_SCHEMA_PASS;
  HOLD_EULER_BAND_OPERATION;
  HOLD_NONBROAD_BAND;
  HOLD_KAPPA_E_DEPENDENCE;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-TOR-EULER-BAND:
  SHARPEN to PFV2-EULER-OP.

A2 witness:
  still not licensed.
```

This is real progress only in the sense that the target is no longer
"find an Euler band somewhere." It is now: make the product-formula
valuation vector define an Euler-only operation.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-EULER-OP.
```

The theorem:

```text
There is a mathematically named operation Op_E that takes the primitive
product-formula valuation vector V_PF inside EBandDesc_{p,q} and
constructs an Euler band/groupoid G_E and torsor tau_E such that:

1. Op_E is defined before all-places assembly and before kappa_E;
2. Op_E uses V_PF as object data, not as p,q labels or scalar defect;
3. Op_E is not functorial for broad local-shadow diagrams;
4. Epstein/DH controls cannot instantiate Op_E while preserving their
   theta/count shadows;
5. kappa_E consumes tau_E before kernel, determinant, mixed object,
   trace, positivity, or zero comparison;
6. B0_p and B0_q embed conservatively before tau_E is consumed;
7. tau_E remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-TOR-EULER-BAND because it requires
the named operation `Op_E`, not only a named band.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `Op_E` proposal if one
proves:

```text
KILL-EULER-OP.1 no operation
  V_PF does not define a band/groupoid operation before all-places
  assembly.

KILL-EULER-OP.2 label collapse
  Op_E uses V_PF only as p,q labels, complement bookkeeping, or a
  scalar product-formula defect.

KILL-EULER-OP.3 broad functoriality
  Op_E is functorial for arbitrary local-shadow diagrams or D plus
  labels.

KILL-EULER-OP.4 control formability
  Epstein/DH controls can instantiate Op_E while preserving theta/count
  shadows.

KILL-EULER-OP.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_E or sees only D and scalar PF.
```

Do not apply these beyond a named product-formula valuation operation.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  the active construction-facing shot is now the product-formula
  valuation vector as a possible Euler-band operation;
  Euler field placement locally passes;
  operation construction, non-broadness, first-map dependence, bank
  preservation, and downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-EULER-OP.
```

## 9. Relation To Existing Docs

```text
doc 159
  Rejects broad functorial carrier-torsor packages and leaves
  PFV2-TOR-EULER-BAND.

doc 158
  Supplies the native torsor source record.

doc 130
  Names the product-formula valuation vector and records
  FIRST_MAP_HOLD.

doc 103
  Supplies the strict first-map record template.

doc 111
  Still blocks downstream forgetfulness.
```
