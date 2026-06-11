# 98 - Strict Euler-carrier trace domain target

Status: theorem target / S3 positive-negative boundary, 2026-06-11.
This states the exact trace-domain theorem needed after doc 97. It is
not a construction and does not authorize a witness.

## 1. Purpose

Docs 74, 93, and 97 now remove three broad S3 false positives:

```text
doc 74
  generic theta/count/Poisson/discrete-measure shadows;

doc 93
  free weights, windows, forms, stress parameters, determinant
  wrappers, or codomains;

doc 97
  trace-derived-looking forms whose naturality domain still accepts
  represented-norm, commutative-monoid, or measure shadows.
```

The surviving S3 escape must be stricter:

```text
the trace domain itself must be Euler-carrier selective.
```

That means it must support the trace on prime-power carriers while
excluding Epstein/DH controls at the first carrier-consuming map.

## 2. Positive Theorem Target

A positive answer must provide a strict Euler-carrier trace domain
`ECar_L1`:

```text
SE98.1 domain
  A category or subcategory ECar_L1 inside L1 whose objects require
  primitive Euler-carrier fields.

SE98.2 primitive carrier fields
  The domain has load-bearing alpha, v, depth, ell, mu_C, and an
  Euler-product factorization or graph-depth object before evaluation.

SE98.3 legal trace
  The trace/properness/duality/nuclearity theorem applies to ECar_L1
  objects and to the kernels/correspondences needed by LS4, without
  first passing through a carrier-forgetting traceable envelope.

SE98.4 bank embedding
  b1 embeds the B0 p^Z comb, q/log p address, Count0/RR layer, and
  graph-depth data if claimed into ECar_L1 without replacing them by
  shadows; it preserves the Epstein guard as a control/rejection test,
  not as an Epstein object in ECar_L1.

SE98.5 same-form mixed object
  b1(comb_C) and R_L/T_C enter one mixed object M_C before trace, and
  the trace derives a same-form codomain F_C.

SE98.6 control exclusion
  For Q=x^2+5y^2, represented-norm and theta/count shadows exist, but
  there is no ECar_L1 object or first carrier-consuming map because
  there is no distinguished atom, unique valuation, tower coordinate,
  or Euler factorization domain.

SE98.7 DH exclusion
  DH-type coefficient/measure shadows either have no ECar_L1 object or
  fail at the same structural carrier map.

SE98.8 zero-free freeze
  The domain, b1, M_C, F_C, control exclusions, and first zero contact
  are frozen before zero-side comparison.
```

Passing SE98 would still advance only the local S3/B1 front. It does
not prove Count/Compare, positivity, BC13, H_odd, RH, or full B1
admission.

## 3. Negative Theorem Target

A negative answer is useful if it proves one of:

```text
NSE98.1 no trace on strict Euler domains
  Any domain strict enough to exclude represented-norm and DH controls
  lacks the traceability/properness/nuclearity needed for Tr_L.

NSE98.2 no conservative bank embedding
  The B0 bank cannot embed into the strict Euler trace domain while
  preserving comb/address/count/guard data.

NSE98.3 no same-form mixed object
  Strict Euler trace domains cannot also host R_L/T_C in one mixed
  object before evaluation.

NSE98.4 forced shadow enlargement
  Any trace domain large enough to support the mixed object must close
  under represented-norm, commutative-monoid, or measure shadows, so
  doc 97 applies.

NSE98.4b traceable envelope collapse
  The strict carrier prefix exists, but Tr_L is legal only after a
  traceable envelope or completion that forgets the primitive carrier
  field, so doc 118 applies.

NSE98.5 external-form dependence
  Strict Euler domains exist, but the carrier-reading form/codomain is
  not trace-derived and doc 93 applies.

NSE98.6 freeze impossibility
  The domain or control exclusion can only be chosen after zero-side
  comparison.
```

The no-go must state its hypotheses. If it covers only a narrow
formalism, record `SHARPEN` rather than killing S3.

## 4. Fillable Record

```text
candidate:
source theorem:

strict domain:
  ECar_L1:
  primitive carrier fields:
  first carrier-consuming map:

trace legality:
  theorem:
  hypotheses:
  intrinsic on ECar_L1? YES/NO:
  traceable envelope Q, if any:
  carrier field retained after Q? YES/NO:
  kernel/correspondence strength:
  codomain:

bank embedding:
  b1:
  B0 fields preserved:
  guard preserved:

mixed object:
  M_C:
  bank-to-M_C:
  continuum-to-M_C:
  before-evaluation proof:

trace-derived codomain:
  F_C:
  theorem deriving F_C:
  external-form audit:

control exclusion:
  Epstein shadow status:
  Epstein ECar_L1 object? YES/NO:
  Epstein first-map status:
  DH shadow status:
  DH ECar_L1 object? YES/NO:
  DH first-map status:

zero-free freeze:
  frozen domain:
  frozen maps:
  frozen control exclusions:
  first zero contact:

verdict:
  PASS_STRICT_EULER | HOLD_STRICT_EULER |
  REJECT_TRACE_ILLEGAL | REJECT_BANK | REJECT_SIDE_BLOCK |
  REJECT_CARRIER_OVERREACH | REJECT_TRACEABLE_ENVELOPE_COLLAPSE |
  REJECT_FREE_WEIGHT |
  REJECT_FREEZE | OUT_OF_SCOPE:
```

These verdicts are local to this theorem target. They do not replace
doc-87, doc-88, doc-89, doc-91, or doc-94 verdicts.

## 5. Decision Rule

```text
PASS_STRICT_EULER
  SE98.1-SE98.8 are supplied. Route to docs 71, 72, 75, 87, 88, 89,
  91, and 94 before any witness.

HOLD_STRICT_EULER
  A strict Euler domain is plausible, but trace legality, bank
  embedding, mixed object, control exclusion, or freeze is incomplete.

REJECT_TRACE_ILLEGAL
  The strict domain lacks the trace theorem required by doc 88.

REJECT_BANK
  The B0 bank cannot embed conservatively; route to doc 89.

REJECT_SIDE_BLOCK
  The domain cannot host bank and continuum in one M_C; route to doc
  86 and doc 79.

REJECT_CARRIER_OVERREACH
  The trace domain admits represented-norm, monoid, or measure
  controls; route to docs 87, 94, and 97.

REJECT_TRACEABLE_ENVELOPE_COLLAPSE
  The strict prefix is traceable only after a carrier-forgetting
  envelope; route to doc 118.

REJECT_FREE_WEIGHT
  The strict domain exists, but the carrier-reading form is externally
  supplied; route to doc 93.

REJECT_FREEZE
  The domain or control exclusions are selected after zero-side
  contact; route to doc 91.

OUT_OF_SCOPE
  The answer concerns trace, carriers, or kernels without deciding the
  strict Euler-domain target.
```

Classify failures by the earliest broken gate. Do not promote a later
pass to compensate for trace illegality, bank nonconservation,
side-block collapse, carrier overreach, or freeze failure.

## 6. Expert Question

Ask:

```text
Is there a trace-class category or subcategory whose objects require
prime-power Euler carrier fields before trace evaluation, so that
Epstein/DH shadows are not objects at the first carrier-consuming map,
while b1(comb_C) and R_L/T_C still enter one mixed trace object?
```

Useful answers must identify:

```text
strict domain:
trace theorem:
trace passage intrinsic or envelope-mediated:
b1 embedding:
M_C and F_C:
first carrier-consuming map:
Epstein/DH exclusion theorem:
zero-free freeze status:
```

## 7. Relation To Existing Docs

```text
doc 87
  Gives the carrier-selectivity ledger.

doc 88
  Gives trace legality requirements.

doc 89
  Gives conservative bank embedding requirements.

doc 91
  Gives zero-free freeze requirements.

doc 94
  Gives the trace-derived form/codomain target.

doc 97
  Rejects overbroad trace domains that accept represented-norm or
  measure shadows.

doc 103
  Gives the first-map record required before a candidate can claim it
  has escaped the doc-100/doc-101/doc-102 shadow-stability rejection and
  returned to this strict-domain target.

doc 109
  Rejects relabeled-shadow attempts to pass the first-map record.

doc 111
  Rejects dead strict prefixes whose primitive field is forgotten before
  the downstream trace package is formed.

doc 112
  Rejects late carrier reintroduction after a shadow-stable trace
  package already exists.

doc 118
  Rejects strict prefixes whose trace theorem becomes legal only after
  a carrier-forgetting traceable envelope.
```

The surviving S3 question is now:

```text
Can one make the trace domain strict enough to exclude controls before
the first load-bearing trace package, keep that primitive field
load-bearing through M_C/F_C/Tr_L and any traceable passage, and still
support traceability, bank embedding, and same-form comb-continuum
coupling?
```
