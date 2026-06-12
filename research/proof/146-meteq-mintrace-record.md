# 146 - METEQ mintrace record

Status: smallest trace-detection attempt / Q134.4 internal target,
2026-06-11. This is not a B1 construction, not an LT76 pass, not an
external answer, and not a witness license.

## 1. Purpose

Docs 133 and 138 leave S2 alive only if metric/equivariant/liquid scale
is trace-visible before evaluation. Late Haar, density, determinant,
Poisson, or normalization factors are already rejected.

This document names the smallest honest trace-detection record inside
METEQ-DETECTED.

## 2. Candidate Record

Name:

```text
METEQ-MINTRACE.
```

Proposed triple:

```text
(O_l, D_l, Tr_l)
```

where:

```text
O_l
  an enriched circle object, roughly R_L/lZ, not bare Shv(S^1) or B_l.

D_l
  a trace/proper-pushforward/nuclearity domain whose hypotheses use the
  metric/equivariant/liquid/density/kernel scale datum l.

Tr_l
  a legal trace theorem on D_l.
```

The required frozen-domain test is:

```text
freeze (O_l, D_l, Tr_l);
replace l by m > 0 before trace evaluation;
ask whether D_l, traceability, or the frozen trace value changes by
theorem.
```

## 3. Local Pass Condition

`METEQ-MINTRACE` obtains `PASS_A1` for METEQ only if it names:

```text
O_l:
  the enriched circle object.

D_l:
  the trace/proper-pushforward/nuclearity domain whose hypotheses use l.

Tr_l:
  the legal trace theorem.

detection theorem:
  l -> m changes D_l, traceability, or the frozen trace value before
  Haar, Poisson, determinant, density, or normalization factors enter.

LS4 hook:
  a plausible same-structure path into a future mixed object with
  b1(p^Z), without claiming LS4 passed.
```

This would not prove B1. It would only advance the A1 scale-retention
side of METEQ.

## 4. Kill Conditions

A kill is licensed only for the named MINTRACE formalism or class:

```text
KILL-MINTRACE.1
  D_l is defined only after forgetting to bare circle/localizing data.

KILL-MINTRACE.2
  l affects only post-trace density, Haar, Poisson, determinant, or
  normalization terms.

KILL-MINTRACE.3
  l changes object isomorphism class but not the trace domain/theorem.

KILL-MINTRACE.4
  the trace-detected structure cannot be the same structure used later
  for LS4 coupling.
```

Do not broaden this into another generic METEQ no-go unless the theorem
actually covers a named class beyond the attempted formalism.

## 5. Sharpen Conditions

If the record reduces to a smaller theorem, use one of:

```text
METEQ-NUCLEAR-DETECT
  nuclearity/properness bounds for enriched circle kernels depend on l.

METEQ-EQUIV-DETECT
  equivariant trace domains detect translation length l before trace.

METEQ-DENSITY-INTERNAL
  density/measure data is internal trace-domain structure, not
  post-trace normalization.
```

## 6. Current Gate Run

```text
O_l:
  schema named, not constructed.

D_l:
  not named.

Tr_l:
  not named.

deletion/detection theorem:
  not proved.

LS4 hook:
  not named beyond requirement.
```

Verdict:

```text
METEQ-DETECTED:
  HOLD_MINTRACE.

METEQ-MINTRACE:
  ACCEPT_AS_NEXT_INTERNAL_TARGET.

S2 witness:
  still not licensed.
```

## 7. Board Update

Update Q134.4 and doc 139 as follows:

```text
The immediate internal target is METEQ-MINTRACE.

Ask first for the frozen triple (O_l, D_l, Tr_l) and the deletion
theorem.

Do not build a numerical witness until the trace/domain theorem exists
or a boundary theorem identifies what the witness would measure.
```

## 8. Relation To Existing Docs

```text
doc 133
  METEQ-A1 remains the broader scale-retention theorem. MINTRACE is the
  first concrete trace-domain record.

doc 138
  Late/factor-through enrichments remain rejected. MINTRACE is the live
  escape clause.

doc 81
  Updated to PASS_A1 only after a real O_l/D_l/Tr_l theorem is named.

doc 114
  Not changed by MINTRACE alone; A6/LT76 still requires carrier
  selectivity and same-form LS4.
```
