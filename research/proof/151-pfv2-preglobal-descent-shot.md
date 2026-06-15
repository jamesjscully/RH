# 151 - PFV2 pre-global descent shot

Status: concrete PFV2-REL-DESCENT candidate shot / Q134.1 internal
result, 2026-06-11. This is not a B1 construction, not an external
answer, not a witness license, and not a broad no-go. It tests the
pre-global descent/gluing source left open by doc 150.

## 1. Purpose

Doc 150 rejects relative reflectors applied after an all-places source
object exists. The remaining PFV2 route must form the p,q+complement
data before global assembly:

```text
PFV2-REL-DESCENT.
```

This document writes the smallest honest descent candidate and runs the
existing gates.

## 2. Candidate Record

Name:

```text
PFV2-DESC(p,q).
```

Proposed source object:

```text
Desc_{p,q}
```

with fields:

```text
T_p
  p-tower/divisor/comb source with structural length ell_p.

T_q
  q-tower/divisor/comb source with structural length ell_q.

C_{not p,q}
  structural complement source for all remaining places.

gamma
  descent/gluing compatibility data relating T_p, T_q, and C_{not p,q}.

pf_desc
  product-formula descent certificate at the level of the gluing data.
```

Assembly, if legal, is a later operation:

```text
Assemble(Desc_{p,q}) = D
```

where `D` is an all-places adelic/divisor/idele object. The order is
part of the candidate:

```text
Desc_{p,q} first;
D second.
```

The intended first map is:

```text
kappa_desc : Desc_{p,q} -> Y_{p,q}^{desc}
```

and it must consume:

```text
(T_p, T_q, C_{not p,q}, gamma, pf_desc)
```

before assembly into D, and before M_C, F_C, Tr_L, determinant, kernel,
trace, or positivity.

## 3. Why This Is A Real Shot

This candidate avoids the failures of docs 147-150 if the descent data
are genuinely prior:

```text
not classical tuple:
  Desc_{p,q} is not just D split into p,q,complement components.

not formal pullback:
  Desc_{p,q} is not a fiber or slice of an already named all-places
  category.

not post-global reflector:
  D is assembled from Desc_{p,q}; D is not the input to the relative
  construction.
```

Thus the shot reaches the right side of the order-of-formation test.

## 4. Gate Run

### Gate 151.1 - Source priority

Verdict:

```text
LOCAL_SCHEMA_PASS
```

Reason: the record explicitly forms `Desc_{p,q}` before all-places
assembly. This passes the order schema that docs 148-150 demanded.

This is not a theorem pass. It is a schema pass until a named descent
category proves that `Desc_{p,q}` exists independently of first
choosing D.

### Gate 151.2 - Complement structurality

Verdict:

```text
LOCAL_COMP_PASS
```

Reason: `C_{not p,q}` is a field of the descent object, not a scalar
degree. This inherits the real improvement from doc 147.

### Gate 151.3 - Effective descent equivalence

Verdict:

```text
HOLD_EFFECTIVE_DESCENT
```

Reason: standard effective descent often identifies descent data with
global objects. If `Desc_{p,q}` is equivalent to the category of
assembled all-places objects D with p,q marking, then the construction
collapses back to docs 148-150. PFV2 needs descent data whose source
priority is load-bearing, not a presentation theorem for G.

### Gate 151.4 - Control non-formability

Verdict:

```text
HOLD_CONTROL_DESCENT
```

Reason: Epstein/DH controls may fail to form global divisors, but PFV2
needs them to fail to form the descent datum itself. If `gamma` and
`pf_desc` are just abstract compatibility data attachable to any local
theta/count shadows, controls may form the same pre-global record.

### Gate 151.5 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the descent source must embed B0_p and B0_q conservatively. If
the only way to define `Desc_{p,q}` is to replace the bank by a full
global adelic object during assembly, the route fails.

### Gate 151.6 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that `gamma` or `pf_desc` remains
load-bearing in M_C, F_C, or Tr_L. If downstream only sees the
assembled D or its p,q readout, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-DESC(p,q):
  LOCAL_SCHEMA_PASS;
  LOCAL_COMP_PASS;
  HOLD_EFFECTIVE_DESCENT;
  HOLD_CONTROL_DESCENT;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-REL-DESCENT:
  SHARPEN to PFV2-DESC-SELECT.

A2 witness:
  still not licensed.
```

This is real progress only in the sense that the candidate finally has
the correct formation order. It still has not proved selectivity or
downstream load-bearing.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-DESC-SELECT.
```

The theorem:

```text
There is a pre-global descent/gluing source category with objects
Desc_{p,q}. These objects contain p and q towers, a structural
complement, gluing data gamma, and a product-formula descent
certificate pf_desc before all-places assembly.

Desc_{p,q} is not merely an effective-descent presentation equivalent
to all-places objects with p,q marking. Epstein/DH controls cannot form
Desc_{p,q} or kappa_desc while preserving their theta/count shadows.
B0_p and B0_q embed conservatively, and gamma or pf_desc remains
load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-REL-DESCENT and is paid for by the
PFV2-DESC shot.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named pre-global descent class if
one proves:

```text
KILL-DESC.1 effective descent collapse
  Desc_{p,q} is equivalent to all-places objects with p,q marking.

KILL-DESC.2 control descent
  Epstein/DH controls can form the same Desc_{p,q} and kappa_desc
  while preserving theta/count shadows.

KILL-DESC.3 bank replacement
  Desc_{p,q} replaces B0_p/B0_q by the full global source rather than
  embedding them conservatively.

KILL-DESC.4 downstream forgetfulness
  Every legal M_C/F_C/Tr_L forgets gamma and pf_desc after assembly.
```

Do not apply these to all PFV2-ADELIC-LOCAL attempts without a theorem
covering all pre-global descent sources.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  pre-global descent is the current best concrete shot;
  source-priority schema and complement structurality locally pass;
  effective descent equivalence, control selectivity, bank preservation,
  and downstream dependence remain HOLD.

Immediate theorem target:
  PFV2-DESC-SELECT.
```

## 9. Relation To Existing Docs

```text
doc 143
  Supplies PFV2-COMP-REFLECT and the no-free-complement test.

doc 147
  Supplies the relative divisor complement shot.

doc 148
  Rejects classical relative tuples.

doc 149
  Rejects formal slice/fiber/pullback relative categories.

doc 150
  Rejects post-global reflectors.

doc 103
  Still HOLD: no FIRST_MAP_PASS.

doc 111
  Still blocks downstream forgetfulness.
```

## 10. Post-doc-152 Update

Doc 152 rejects ordinary effective descent:

```text
PFV2_DESC_effective:
  REJECT_EFFECTIVE_DESCENT_COLLAPSE.
```

The surviving target is:

```text
PFV2-DESC-RESIDUAL.
```

Thus PFV2-DESC(p,q) remains useful as the first correctly ordered
descent shot, but ordinary effective reconstruction is not enough.
Future work should ask for residual descent data rho that are not
erased by assembly, cannot be formed by controls, and remain
load-bearing downstream.
