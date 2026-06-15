# 162 - PFV2 Euler tower operation shot

Status: concrete PFV2-EULER-TOWER-OP candidate shot / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, not a witness license, and not a no-go. It writes the
smallest honest operation record after doc 161: an operation on the
effective Euler valuation towers, not on the scalar product-formula
equation alone.

## 1. Purpose

Doc 161 rejects scalar product-formula balance operations. The
remaining target is:

```text
PFV2-EULER-TOWER-OP.
```

The target must consume actual tower/comb/effectivity data:

```text
alpha_p, alpha_q, p^Z, q^Z, v_p, v_q, ell_p, ell_q, PF.
```

This document states the smallest record that would count as a real
tower operation.

## 2. Candidate Record

Name:

```text
PFV2-TOWER-OP(p,q).
```

Proposed source object:

```text
TowerDesc_{p,q}
```

with fields:

```text
A_p, A_q
  the B0_p and B0_q one-place carrier records.

alpha_p, alpha_q
  the distinguished prime-power carrier atoms.

Comb_p, Comb_q
  effective prime-power combs, intended as p^Z and q^Z source data,
  not as marked monoid labels.

v_p, v_q
  valuation/tower maps on the effective combs.

ell_p, ell_q
  structural lengths ell_p=log p and ell_q=log q tied to the combs and
  valuation maps.

gamma
  pre-assembly p,q+complement gluing compatibility.

PF
  product-formula compatibility for the tower data.

Eff
  an effectivity predicate saying which tower lifts preserve the
  prime-power carrier atoms and comb order.

C_{not p,q}
  structural complement source.
```

The proposed operation is:

```text
Op_T(TowerDesc_{p,q}) = (G_T, tau_T)
```

where:

```text
G_T
  the groupoid of effective PF-compatible tower lifts preserving
  alpha_p, alpha_q, Comb_p, Comb_q, v_p, v_q, ell_p, ell_q, and
  C_{not p,q}.

tau_T
  the torsor of such effective tower lifts.
```

The intended first map is:

```text
kappa_T : TowerDesc_{p,q} -> Y_T
```

and it must consume:

```text
(Comb_p, Comb_q, Eff, G_T, tau_T)
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is Not The Linear Class

This shot differs from doc 161 by requiring:

```text
atom consumption:
  alpha_p and alpha_q are not labels; Op_T must preserve or act on
  their generated combs.

comb effectivity:
  p^Z and q^Z enter as effective tower data, not as abstract monoids or
  scalar length addresses.

valuation action:
  v_p and v_q are maps on the combs, not just coordinates in a vector.

PF compatibility:
  PF constrains effective tower lifts, not merely a scalar weighted
  sum.
```

This still does not evade docs 140-141 unless the effective tower
operation is more than a marked product, marked monoid, or bare
factorization pair.

## 4. Gate Run

### Gate 162.1 - Tower field placement

Verdict:

```text
LOCAL_TOWER_FIELD_SCHEMA_PASS
```

Reason: the record places atoms, combs, valuation maps, structural
lengths, PF, and effectivity before assembly and before the first map.

This is not a theorem that those fields are primitive object data.

### Gate 162.2 - Beyond marked monoid

Verdict:

```text
HOLD_NOT_MARKED_MONOID
```

Reason: no theorem has shown that `Comb_p`, `Comb_q`, and `Eff` are
more than marked monoid/factorization data. Docs 140-141 still reject
bare product/monoid/UFD-pair versions.

### Gate 162.3 - Operation construction

Verdict:

```text
HOLD_TOWER_OPERATION
```

Reason: `Op_T` is named but not constructed. A theorem must define the
effective PF-compatible tower-lift groupoid and show it is source data.

### Gate 162.4 - Control exclusion

Verdict:

```text
HOLD_CONTROL_TOWER
```

Reason: no theorem has shown that Epstein/DH controls cannot carry an
analogous effective tower-lift operation while retaining theta/count
shadows. The failure must occur at source or first-map formability, not
at positivity, trace, or zero comparison.

### Gate 162.5 - First-map dependence

Verdict:

```text
HOLD_KAPPA_T_DEPENDENCE
```

Reason: no theorem has shown that changing `tau_T` while holding D,
p,q marking, scalar PF, and complement bookkeeping fixed changes
`kappa_T` or its target.

### Gate 162.6 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the operation must preserve the B0_p and B0_q comb/address/
count/guard data. If it replaces the banks by a new global tower
source, doc 130's KILL-A2.5 applies.

### Gate 162.7 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L sees `tau_T` as
load-bearing source data. If downstream only sees scalar PF or the
assembled object, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-TOWER-OP(p,q):
  LOCAL_TOWER_FIELD_SCHEMA_PASS;
  HOLD_NOT_MARKED_MONOID;
  HOLD_TOWER_OPERATION;
  HOLD_CONTROL_TOWER;
  HOLD_KAPPA_T_DEPENDENCE;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-EULER-TOWER-OP:
  SHARPEN to PFV2-TOWER-EFFECTIVE.

A2 witness:
  still not licensed.
```

This is progress only as a sharper operation record. It says exactly
what must be more than scalar PF and more than marked monoid data.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-TOWER-EFFECTIVE.
```

The theorem:

```text
There is an effective Euler tower operation Op_T such that:

1. Op_T consumes alpha_p, alpha_q, Comb_p, Comb_q, v_p, v_q, ell_p,
   ell_q, PF, and Eff before all-places assembly;
2. Comb_p, Comb_q, and Eff are primitive carrier data, not marked
   monoid/factorization labels;
3. Op_T constructs G_T and tau_T before kappa_T;
4. Epstein/DH controls cannot instantiate Op_T while preserving
   theta/count shadows;
5. kappa_T depends on tau_T before kernel, determinant, mixed object,
   trace, positivity, or zero comparison;
6. B0_p and B0_q embed conservatively before tau_T is consumed;
7. tau_T remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-EULER-TOWER-OP because it names the
missing ingredient: effectivity as primitive Euler carrier data.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named effective tower operation
if one proves:

```text
KILL-TOWER-EFF.1 marked monoid collapse
  Comb_p, Comb_q, and Eff are only marked monoid/factorization labels.

KILL-TOWER-EFF.2 scalar PF factorization
  Op_T factors through scalar PF or a length-weighted valuation vector.

KILL-TOWER-EFF.3 control tower
  Epstein/DH controls can instantiate the same effective tower
  operation while retaining theta/count shadows.

KILL-TOWER-EFF.4 bank replacement
  Op_T replaces B0_p/B0_q instead of embedding them conservatively.

KILL-TOWER-EFF.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_T or sees only scalar PF.
```

Do not apply these beyond a named effective tower operation.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  the active construction-facing shot is now effective Euler tower
  operation, not scalar product-formula balance;
  tower field placement locally passes;
  non-monoid status, operation construction, control exclusion,
  first-map dependence, bank preservation, and downstream dependence
  remain HOLD.

Immediate theorem target:
  PFV2-TOWER-EFFECTIVE.
```

## 9. Relation To Existing Docs

```text
doc 161
  Rejects scalar product-formula operations and leaves
  PFV2-EULER-TOWER-OP.

doc 160
  Supplies the product-formula valuation vector shot.

docs 140-141
  Still reject marked monoid and bare factorization-pair versions.

doc 130
  Names the primitive A2 fields and records FIRST_MAP_HOLD.

doc 103
  Supplies the strict first-map record template.

doc 111
  Still blocks downstream forgetfulness.
```
