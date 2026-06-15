# 170 - PFV2 GPF residual monodromy commutator shot

Status: concrete PFV2-GPF-RMON-NATIVE candidate shot / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, not a witness license, and not a no-go. It names the
smallest native residual monodromy/action class left by doc 169.

## 1. Purpose

Doc 169 rejects residual monodromy that is only presentation, gauge, or
coherence data for assembly. The remaining target is:

```text
PFV2-GPF-RMON-NATIVE.
```

The target asks for a native action class inside the p,q+complement
GPF source. The most direct candidate is not an arbitrary torsor: it is
the commutator or holonomy defect of the p and q tower operations when
they act on the structural complement while preserving GPF and
effectivity.

## 2. Candidate Record

Name:

```text
PFV2-GPF-RMON-COMM(p,q).
```

Proposed source object:

```text
S_{p,q}^{G,comm} in ECar_L1^{GPF,pq,comm}
```

Fields inherited from doc 168:

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

bank_iota
  conservative embeddings of B0_p and B0_q before the first map.

surv_G
  downstream visibility data.
```

New native action fields:

```text
Act_p, Act_q
  p and q tower operations acting on the structural complement inside
  the GPF source while preserving GPF_{p,q} and Eff_{p,q}.

rho_G^{comm}
  the commutator/holonomy class [Act_p, Act_q] on C_{not p,q}, or the
  obstruction to interchanging the p and q tower actions under the GPF
  effectivity constraints.
```

The intended first map is:

```text
kappa_G^{comm} : S_{p,q}^{G,comm} -> Y_G^{comm}.
```

It must consume:

```text
(Act_p, Act_q, rho_G^{comm}, GPF_{p,q}, Eff_{p,q})
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is A Real Shot

This candidate is stricter than a generic native monodromy:

```text
native source of action:
  Act_p and Act_q are operations of the p,q+complement GPF source, not
  automorphisms of an assembled D.

not presentation coherence:
  rho_G^{comm} measures noncommuting tower action on the complement,
  not coherence for a descent presentation.

not scalar PF bookkeeping:
  rho_G^{comm} is not the scalar statement that p and q valuation
  lengths balance the remaining places.

not independent tower decoration:
  the class exists only if the p and q towers act on the same
  structural complement under the same GPF/Eff constraints.

not first-map inert:
  kappa_G^{comm} must change if the commutator class changes while D,
  marking, and presentation data are held fixed.
```

Thus the shot reaches the native side left open by doc 169 without
claiming the commutator exists.

## 4. Gate Run

### Gate 170.1 - Native commutator placement

Verdict:

```text
LOCAL_RMON_COMM_SCHEMA_PASS
```

Reason: the record places `Act_p`, `Act_q`, and `rho_G^{comm}` inside
the pre-assembly GPF source and makes them first-map inputs.

This is only a schema pass. It does not construct
`ECar_L1^{GPF,pq,comm}`.

### Gate 170.2 - Action existence

Verdict:

```text
HOLD_COMM_ACTION_EXISTENCE
```

Reason: no theorem has yet supplied p and q tower operations acting on
the structural complement as source data while preserving GPF and
effectivity.

### Gate 170.3 - Non-presentation

Verdict:

```text
HOLD_COMM_NONPRESENTATION
```

Reason: no theorem has shown that `rho_G^{comm}` is not equivalent to
presentation coherence, a gauge of `gamma_G`, or an automorphism label
on the assembled object.

### Gate 170.4 - Non-scalarity

Verdict:

```text
HOLD_COMM_NONSCALAR
```

Reason: no theorem has shown that the commutator class is more than
scalar product-formula balance or complement bookkeeping.

### Gate 170.5 - Control exclusion

Verdict:

```text
HOLD_COMM_CONTROL_EXCLUSION
```

Reason: no theorem has shown that Epstein/DH controls cannot
instantiate compatible p and q actions and the same commutator while
retaining theta/count shadows.

### Gate 170.6 - First-map dependence

Verdict:

```text
HOLD_COMM_FIRST_MAP
```

Reason: no theorem has constructed `kappa_G^{comm}` or shown that
changing `rho_G^{comm}` while holding D, p,q marking, and presentation
data fixed changes the first map or its target.

### Gate 170.7 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the action source must preserve the B0_p and B0_q comb,
address, count, and guard data. If the actions exist only after
replacing the banks by a full global source, docs 150 and 165 apply.

### Gate 170.8 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes
`rho_G^{comm}` as load-bearing source data. If downstream only sees D,
scalar PF, or p,q marking, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-GPF-RMON-COMM(p,q):
  LOCAL_RMON_COMM_SCHEMA_PASS;
  HOLD_COMM_ACTION_EXISTENCE;
  HOLD_COMM_NONPRESENTATION;
  HOLD_COMM_NONSCALAR;
  HOLD_COMM_CONTROL_EXCLUSION;
  HOLD_COMM_FIRST_MAP;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-GPF-RMON-NATIVE:
  SHARPEN to PFV2-GPF-RMON-COMM-SELECT.

A2 witness:
  still not licensed.
```

This is construction progress only as a named native action record. It
narrows the next target from "some native monodromy" to the
commutator/holonomy of p and q tower actions on the structural
complement.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GPF-RMON-COMM-SELECT.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF,pq,comm} with objects
S_{p,q}^{G,comm}, p and q tower actions Act_p and Act_q on the
structural complement, and a commutator/holonomy class rho_G^{comm}
such that:

1. Act_p and Act_q exist before all-places assembly inside the
   p,q+complement GPF source;
2. rho_G^{comm} is defined from their action on C_{not p,q} under
   GPF_{p,q} and Eff_{p,q};
3. rho_G^{comm} is not recovered from D plus p,q marking;
4. rho_G^{comm} is not presentation coherence, gauge data, or scalar
   product-formula bookkeeping;
5. kappa_G^{comm} consumes rho_G^{comm} before assembly;
6. changing rho_G^{comm} while holding D, p,q marking, and
   presentation data fixed changes kappa_G^{comm} or its target;
7. Epstein/DH controls cannot instantiate Act_p, Act_q,
   rho_G^{comm}, or kappa_G^{comm} while retaining theta/count
   shadows;
8. B0_p and B0_q embed conservatively before rho_G^{comm} is consumed;
9. rho_G^{comm} remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-GPF-RMON-NATIVE because it demands
a specific commutator/holonomy action class.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named commutator/holonomy
proposal if one proves:

```text
KILL-COMM.1 no action
  The proposed source does not define Act_p and Act_q on the structural
  complement before all-places assembly.

KILL-COMM.2 presentation collapse
  rho_G^{comm} is only presentation coherence, a gauge of gamma_G, or
  an automorphism label on D.

KILL-COMM.3 scalar collapse
  rho_G^{comm} is only scalar product-formula balance, p,q marking, or
  complement bookkeeping.

KILL-COMM.4 control formability
  Epstein/DH controls can instantiate Act_p, Act_q, rho_G^{comm}, and
  kappa_G^{comm} while retaining theta/count shadows.

KILL-COMM.5 inherited first map
  kappa_G^{comm} is unchanged when rho_G^{comm} changes while D,
  p,q marking, and presentation data are fixed.

KILL-COMM.6 bank replacement
  rho_G^{comm} requires replacing B0_p/B0_q by a full global source.

KILL-COMM.7 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho_G^{comm}.
```

Do not apply these beyond the named commutator/holonomy proposal.

## 8. Board Update

```text
PFV2-GPF-RMON-COMM(p,q):
  LOCAL_RMON_COMM_SCHEMA_PASS.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-COMM-SELECT or another native
  residual p,q+complement GPF action class.

A2 witness:
  still not licensed.
```

## 9. Relation To Existing Docs

```text
doc 169
  Forces the residual monodromy to be native rather than presentation
  or gauge data.

doc 168
  Supplies the generic residual monodromy source record.

doc 160
  Explains why product-formula fields must define operations, not only
  scalar balance.

doc 159
  Rejects broad carrier-torsor/groupoid packages formable by controls.

doc 111
  Still blocks downstream-erased strict prefixes.
```
