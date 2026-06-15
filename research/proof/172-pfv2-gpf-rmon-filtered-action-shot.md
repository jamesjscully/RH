# 172 - PFV2 GPF residual monodromy filtered action shot

Status: concrete PFV2-GPF-RMON-COMM-NONSCALAR candidate shot /
Q134.1 internal result, 2026-06-12. This is not a B1 construction, not
an external answer, not a witness license, and not a no-go. It names
the smallest non-scalar commutator residue left by doc 171.

## 1. Purpose

Doc 171 rejects commutators that are only scalar product-formula
balance, p,q marking, complement bookkeeping, or abelian compatibility.
The remaining target is:

```text
PFV2-GPF-RMON-COMM-NONSCALAR.
```

The target still says "non-scalar action residue" abstractly. This
document makes the next shot concrete: the commutator must be detected
on a structural filtration or grading of the complement.

## 2. Candidate Record

Name:

```text
PFV2-GPF-RMON-FILT(p,q).
```

Proposed source object:

```text
S_{p,q}^{G,filt} in ECar_L1^{GPF,pq,filt}
```

Fields inherited from doc 170:

```text
A_p, A_q
  B0_p and B0_q one-place carrier records.

Comb_p, Comb_q
  effective prime-power combs.

v_p, v_q, ell_p, ell_q
  valuation/tower maps and structural lengths.

C_{not p,q}
  structural complement source.

GPF_{p,q}, Eff_{p,q}, gamma_G
  p,q+complement GPF axiom, effectivity data, and pre-assembly gluing.

Act_p, Act_q
  p and q tower operations acting on C_{not p,q}.

rho_G^{comm}
  the commutator/holonomy class of Act_p and Act_q.

bank_iota, surv_G
  conservative bank embeddings and downstream visibility data.
```

New filtered-action fields:

```text
Fil_C
  a structural filtration, grading, or layer decomposition of
  C_{not p,q} inside the GPF source.

rho_G^{fil}
  the induced graded/layer action residue of [Act_p, Act_q] on Fil_C.
```

The intended first map is:

```text
kappa_G^{fil} : S_{p,q}^{G,filt} -> Y_G^{fil}.
```

It must consume:

```text
(Fil_C, Act_p, Act_q, rho_G^{fil}, GPF_{p,q}, Eff_{p,q})
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is A Real Shot

This candidate is stricter than a generic non-scalar commutator:

```text
filtered complement:
  the residue is detected on named structure of C_{not p,q}, not only
  by saying "non-scalar."

not scalar bookkeeping:
  Fil_C and rho_G^{fil} are not determined by scalar PF balance,
  p,q marking, complement degree, or an abelian compatibility equation.

not presentation coherence:
  the filtration belongs to the source complement, not to choices of
  descent presentation for D.

not first-map inert:
  kappa_G^{fil} must change if rho_G^{fil} changes while D, marking,
  scalar PF, and presentation data are held fixed.
```

Thus the shot gives the non-scalar residue a concrete place to live.

## 4. Gate Run

### Gate 172.1 - Filtered residue placement

Verdict:

```text
LOCAL_FILTERED_RESIDUE_SCHEMA_PASS
```

Reason: the record places `Fil_C` and `rho_G^{fil}` inside the
pre-assembly GPF source and makes them first-map inputs.

This is only a schema pass. It does not construct
`ECar_L1^{GPF,pq,filt}`.

### Gate 172.2 - Filtration existence

Verdict:

```text
HOLD_FILTRATION_EXISTENCE
```

Reason: no theorem has supplied a structural filtration, grading, or
layer decomposition of the complement as source data.

### Gate 172.3 - Non-scalar detection

Verdict:

```text
HOLD_FILTERED_NONSCALAR
```

Reason: no theorem has shown that `rho_G^{fil}` is not determined by
scalar PF, p,q marking, complement bookkeeping, or abelian
compatibility.

### Gate 172.4 - Non-presentation

Verdict:

```text
HOLD_FILTERED_NONPRESENTATION
```

Reason: no theorem has shown that `Fil_C` and `rho_G^{fil}` are not
presentation or coherence data for all-places assembly.

### Gate 172.5 - Control exclusion

Verdict:

```text
HOLD_FILTERED_CONTROL_EXCLUSION
```

Reason: no theorem has shown that Epstein/DH controls cannot
instantiate the same filtered complement action while retaining
theta/count shadows.

### Gate 172.6 - First-map dependence

Verdict:

```text
HOLD_FILTERED_FIRST_MAP
```

Reason: no theorem has constructed `kappa_G^{fil}` or shown that
changing `rho_G^{fil}` while holding D, p,q marking, scalar PF, and
presentation data fixed changes the first map or its target.

### Gate 172.7 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the filtered action source must preserve the B0_p and B0_q
comb, address, count, and guard data. If the filtration exists only
after replacing the banks by a full global source, docs 150 and 165
apply.

### Gate 172.8 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes
`rho_G^{fil}` as load-bearing source data. If downstream only sees D,
scalar PF, or p,q marking, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-GPF-RMON-FILT(p,q):
  LOCAL_FILTERED_RESIDUE_SCHEMA_PASS;
  HOLD_FILTRATION_EXISTENCE;
  HOLD_FILTERED_NONSCALAR;
  HOLD_FILTERED_NONPRESENTATION;
  HOLD_FILTERED_CONTROL_EXCLUSION;
  HOLD_FILTERED_FIRST_MAP;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-GPF-RMON-COMM-NONSCALAR:
  SHARPEN to PFV2-GPF-RMON-FILT-SELECT.

A2 witness:
  still not licensed.
```

This is construction progress only as a named filtered action record.
It narrows the next target from "some non-scalar commutator" to a
filtered complement-action residue.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GPF-RMON-FILT-SELECT.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF,pq,filt} with objects
S_{p,q}^{G,filt}, a structural complement filtration Fil_C, p and q
tower actions Act_p and Act_q, and a graded/layer action residue
rho_G^{fil} such that:

1. Fil_C exists before all-places assembly inside the p,q+complement
   GPF source;
2. rho_G^{fil} is defined from the commutator/holonomy action on
   Fil_C under GPF_{p,q} and Eff_{p,q};
3. rho_G^{fil} is not recovered from D plus p,q marking;
4. rho_G^{fil} is not scalar PF bookkeeping, complement bookkeeping,
   abelian compatibility, presentation coherence, or gauge data;
5. kappa_G^{fil} consumes rho_G^{fil} before assembly;
6. changing rho_G^{fil} while holding D, p,q marking, scalar PF, and
   presentation data fixed changes kappa_G^{fil} or its target;
7. Epstein/DH controls cannot instantiate Fil_C, rho_G^{fil}, or
   kappa_G^{fil} while retaining theta/count shadows;
8. B0_p and B0_q embed conservatively before rho_G^{fil} is consumed;
9. rho_G^{fil} remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-GPF-RMON-COMM-NONSCALAR because it
demands a filtered complement-action residue.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named filtered action proposal:

```text
KILL-FILT.1 no filtration
  The proposed source does not define Fil_C before all-places assembly.

KILL-FILT.2 scalar collapse
  rho_G^{fil} is determined by scalar PF, marking, complement
  bookkeeping, or abelian compatibility.

KILL-FILT.3 presentation collapse
  Fil_C or rho_G^{fil} is only presentation coherence or gauge data.

KILL-FILT.4 control formability
  Epstein/DH controls can instantiate Fil_C, rho_G^{fil}, and
  kappa_G^{fil} while retaining theta/count shadows.

KILL-FILT.5 inherited first map
  kappa_G^{fil} is unchanged when rho_G^{fil} changes while D,
  marking, scalar PF, and presentation data are fixed.

KILL-FILT.6 bank replacement
  the filtered residue requires replacing B0_p/B0_q by a full global
  source.

KILL-FILT.7 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_G^{fil}.
```

Do not apply these beyond the named filtered action proposal.

## 8. Board Update

```text
PFV2-GPF-RMON-FILT(p,q):
  LOCAL_FILTERED_RESIDUE_SCHEMA_PASS.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-FILT-SELECT or another
  filtered non-scalar p,q+complement GPF action class.

A2 witness:
  still not licensed.
```

## 9. Relation To Existing Docs

```text
doc 171
  Forces the commutator residue to be non-scalar.

doc 170
  Supplies the commutator/holonomy source record.

doc 161
  Rejects scalar product-formula operations.

doc 159
  Rejects broad carrier-torsor/groupoid packages formable by controls.

doc 111
  Still blocks downstream-erased strict prefixes.
```
