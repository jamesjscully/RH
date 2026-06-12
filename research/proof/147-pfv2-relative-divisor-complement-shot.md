# 147 - PFV2 relative divisor complement shot

Status: concrete PFV2-COMP-REFLECT candidate shot / Q134.1 internal
result, 2026-06-11. This is not a B1 construction, not an external
answer, not a witness license, and not a broad no-go. It attacks the
specific complement-reflection gap exposed by doc 143.

## 1. Purpose

Doc 143 showed that a formal complement slot is not enough. The
complement must be structural and not freely attachable, or controls
can carry the same bookkeeping.

The most honest next shot is the classical relative divisor/idele
record: make the complement an actual divisor or adelic complement
rather than a scalar. This document tests that candidate directly.

## 2. Candidate Record

Name:

```text
PFV2-REL-DIV(p,q).
```

Intended source object:

```text
S_{p,q}^{div}
```

with fields:

```text
K
  a global product-formula carrier, initially K=Q unless a later
  answer names a better field or Arakelov category.

D_p, D_q
  distinguished p and q valuation-divisor components.

ell_p, ell_q
  structural log norm lengths.

D_{not p,q}
  a divisor/idele/Arakelov complement on all places other than p and q.

principal_or_PF_certificate
  source data certifying that the full divisor/idele satisfies the
  product formula.
```

The intended relation is:

```text
deg(D_p) + deg(D_q) + deg(D_{not p,q}) = 0
```

where `D_{not p,q}` is an object of the source, not a frozen scalar.

The intended first map is:

```text
kappa_div : S_{p,q}^{div} -> Y_{p,q}^{div}
```

and it must consume:

```text
(D_p, D_q, ell_p, ell_q, D_{not p,q}, principal_or_PF_certificate)
```

before M_C, F_C, Tr_L, kernels, determinants, correspondences, or
positivity.

## 3. Why This Is A Real Shot

This candidate is not merely a renamed coordinate pair:

```text
D_{not p,q}
  is an actual complement object.

principal_or_PF_certificate
  makes the product-formula relation source-level.

p and q
  are distinguished in the source record, not selected only after a
  trace or kernel exists.
```

It is also not a formal free-complement slot if the source requires the
complement to extend p and q to a principal/product-formula divisor.
The complement is then constrained by the global carrier category.

## 4. Gate Run

### Gate 147.1 - Structural complement

Verdict:

```text
LOCAL_COMP_PASS
```

Reason: `D_{not p,q}` can be a genuine divisor, idele, or Arakelov
complement object. This is the first PFV2 shot that makes the
complement more than a scalar or placeholder.

### Gate 147.2 - No-free-complement

Verdict:

```text
LOCAL_NO_FREE_PASS if principal_or_PF_certificate is source data;
HOLD_NO_FREE if arbitrary complements may be attached.
```

Reason: a complement constrained by a principal/product-formula
certificate is not freely attachable to arbitrary two-tower data. But
if the formalism allows any `D_{not p,q}` to be appended and then
declares a compensating degree, doc 143's free-complement objection
returns.

### Gate 147.3 - Two-place first map

Verdict:

```text
HOLD_RELATIVE_FIRST_MAP
```

Reason: the record distinguishes p and q before trace, but it may still
be only a relative presentation of an all-places principal divisor. To
pass, kappa_div must exist because the relative p,q+complement record
exists, not because a global all-places object was accepted first and
then read at p and q.

### Gate 147.4 - Control non-formability

Verdict:

```text
HOLD_SOURCE_SELECTIVITY
```

Reason: Epstein/DH controls cannot form a principal divisor object of
K if the source category is genuinely global-field adelic/divisor data.
That is promising. But PFV2 needs the exclusion at the relative first
map, not merely at the ambient all-places source. The control branch is
not closed until the theorem says controls cannot form
`S_{p,q}^{div}` or `kappa_div`, while their theta/count shadows remain
meaningful.

### Gate 147.5 - Bank replacement

Verdict:

```text
HOLD_BANK_REPLACEMENT
```

Reason: a full principal divisor or idele source may carry too much
global Euler-product structure at once. If PFV2-REL-DIV imports the
whole global arithmetic object and then uses p,q only as readout
coordinates, it repeats doc 142. The candidate must show that B0_p and
B0_q embed conservatively without replacing the bank by the entire
principal-divisor apparatus.

### Gate 147.6 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that the consumed relative divisor field
remains load-bearing inside M_C, F_C, or Tr_L. Doc 111 still blocks
promotion if D_{not p,q} disappears after kappa_div.

## 5. Current Verdict

```text
PFV2-REL-DIV(p,q):
  LOCAL_COMP_PASS;
  HOLD_RELATIVE_FIRST_MAP;
  HOLD_SOURCE_SELECTIVITY;
  HOLD_BANK_REPLACEMENT;
  HOLD_DOWNSTREAM.

PFV2-COMP-REFLECT:
  SHARPEN to PFV2-REL-FIRST.

A2 witness:
  still not licensed.
```

The candidate is valuable because it supplies the first serious
complement object. It is not yet a first-map pass.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-REL-FIRST.
```

The theorem:

```text
There is a relative adelic/divisor source category whose objects are
S_{p,q}^{div}, with p and q components, structural lengths, a
non-free complement D_{not p,q}, and a principal/product-formula
certificate as source data.

The first map kappa_div exists because this relative record exists,
not because an all-places object was first accepted and later projected.

Epstein represented-norm data and DH coefficient/measure shadows cannot
form S_{p,q}^{div} or kappa_div, B0_p and B0_q embed conservatively,
and the consumed relative divisor field remains load-bearing
downstream.
```

This theorem is narrower than PFV2-COMP-REFLECT and is paid for by the
PFV2-REL-DIV shot.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for the relative divisor/idele class if
one proves:

```text
KILL-REL-DIV.1 projection collapse
  Every PFV2-REL-DIV source is equivalent to accepting an all-places
  principal divisor first and then reading p,q coordinates.

KILL-REL-DIV.2 free complement
  The complement can be attached to arbitrary two-tower data without a
  source-level principal/product-formula certificate.

KILL-REL-DIV.3 control formability
  Epstein/DH controls can form the same relative source or first map
  while retaining their theta/count shadows.

KILL-REL-DIV.4 bank replacement
  The only way to get the complement is to replace B0_p/B0_q by a
  full global divisor apparatus rather than embedding them
  conservatively.

KILL-REL-DIV.5 downstream forgetfulness
  Every legal downstream M_C/F_C/Tr_L forgets D_{not p,q} after the
  first map.
```

Do not generalize these to all PFV2-ADELIC-LOCAL attempts unless the
theorem actually covers all structural complement sources.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  relative divisor complement is the current best concrete shot;
  complement structurality locally passes;
  first-map priority, source selectivity, bank preservation, and
  downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-REL-FIRST.
```

## 9. Relation To Existing Docs

```text
doc 142
  Rejects all-places bookkeeping. PFV2-REL-DIV must avoid becoming
  that by proving relative-first priority.

doc 143
  Supplies PFV2-COMP-REFLECT and the free-complement test. This
  document is the first concrete complement shot against that test.

doc 103
  Still HOLD: FIRST_MAP_PASS is not obtained.

doc 111
  Still blocking: downstream load-bearing is unproved.

doc 134 and doc 139
  Were first updated to mention PFV2-REL-FIRST. After doc 148, they
  should mention PFV2-REL-UPROP as the surviving internal target.
```

## 10. Post-doc-148 Update

Doc 148 rejects the ordinary classical relative divisor/idele tuple:

```text
PFV2_REL_DIV_classical:
  REJECT_RELATIVE_PROJECTION.
```

The surviving target is:

```text
PFV2-REL-UPROP.
```

Thus PFV2-REL-DIV remains useful as a calibration shot for structural
complement data, but the classical assembled all-places presentation is
not live. Future work should ask for a relative universal property,
reflection theorem, or descent/gluing axiom not equivalent to
all-places assembly plus marked p,q coordinates.
