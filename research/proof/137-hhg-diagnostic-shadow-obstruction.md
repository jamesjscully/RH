# 137 - HHG diagnostic-shadow obstruction

Status: bounded candidate-driven no-go / Q134.3 internal result,
2026-06-11. This attacks HHG-FIRST after doc 132. It does not kill all
HH graph-index routes. It rejects the diagnostic-shadow realization
and leaves only a structural HH carrier source live.

## 1. Purpose

Doc 132 named:

```text
HHG-FIRST
```

as the missing theorem for the A3 HH graph-index route. The first
internal question is whether the banked HH/Frobenius graph-index data
can be used as-is.

This document records the answer:

```text
HH graph/index data used only as a Gram, index, signature, determinant,
stress, or graph-label readout is diagnostic supply, not a strict
first carrier-consuming source.
```

## 2. Covered Class

Call an A3 proposal `HHG_diag` if it satisfies all of:

```text
D137.1 banked diagnostic source
  The source data are HH/Frobenius graph, index, Gram, Lorentzian,
  signature, determinant, coker, or stress-flow records already
  available as banked diagnostics or supply.

D137.2 graph labels
  alpha, v, depth, ell, or graph_class are labels, coordinates, chosen
  graph directions, stress parameters, or readouts attached to an
  existing shadow/index object.

D137.3 no primitive HH_C object
  No L1 object HH_C is defined whose existence requires the
  graph-depth/prime-power carrier fields before Gram, determinant,
  index, trace, mixed-object, or codomain formation.

D137.4 first map is diagnostic evaluation
  The proposed kappa_HH is the operation of reading, evaluating,
  constraining, or packaging the diagnostic index/Gram/determinant
  data.

D137.5 shadow or side-block stability
  The same diagnostic package remains meaningful after forgetting the
  Euler labels, or appears as an archimedean/index side block rather
  than one mixed object receiving bank and continuum before evaluation.

D137.6 late promotion
  P3, BC13, carrier selectivity, or LS4 is claimed only after the
  diagnostic package is re-read as Count, H_odd, positivity, or
  same-form coupling.
```

This class includes:

```text
Lorentzian/Gram witness scans;
HH graph-depth labels read by a generic determinant or index package;
stress kernels promoted to carrier maps;
graph-index forms beside a separate archimedean trace;
same diagnostic package re-read as both index and Count.
```

## 3. Lemma

### Lemma 137.1

Every `HHG_diag` proposal fails doc-103 `FIRST_MAP_PASS` and cannot
advance A3 as a B1 candidate.

Verdict:

```text
REJECT_RELABELING
  if HH graph/depth fields are labels on a shadow/index object.

REJECT_FREE_WEIGHT
  if the load-bearing form, stress parameter, determinant presentation,
  or codomain is externally supplied.

REJECT_SIDE_BLOCK
  if the HH/index package and archimedean continuum are evaluated as
  separate blocks.

DEMOTE_TO_DIAGNOSTIC
  if the result is valid supply or compatibility data but not a strict
  carrier source.
```

### Proof

Doc 103 requires a source object and first map whose definition consumes
primitive Euler-carrier fields before mixed object, trace, determinant,
Gram, or codomain formation.

Under D137.1-D137.4, the proposed source and first map are not earlier
than the diagnostic package. They are the diagnostic package, or a
labeling/readout of it. Doc 109 therefore applies when the graph/depth
fields are labels on an existing shadow object. Doc 93 applies when
the carrier-sensitive form, stress, determinant, or codomain is
externally supplied. Doc 70 applies when Gram/index/signature data are
promoted as Count, H_odd, P3, BC13, or positivity without separate
structures.

Under D137.5, if the diagnostic package appears beside a separate
archimedean contribution, doc 79 and doc 86 reject the LS4 claim as a
side block. If the package remains meaningful after forgetting the
Euler labels, docs 108 and 109 classify the route as shadow-stable or
decorated shadow.

Thus `HHG_diag` cannot supply `FIRST_MAP_PASS`. It may remain useful
as theorem-grade supply, compatibility check, or diagnostic data, but
not as A3/B1 admission evidence. QED.

## 4. Consequence For HHG-FIRST

HHG-FIRST is narrowed.

The following no longer count as live A3 construction work:

```text
Gram/index/signature scans;
stress-flow or Lorentzian margin witnesses;
graph-depth labels on a shadow-stable HH/index object;
determinant/coker packages that read graph labels after formation;
side-block HH index plus archimedean correction.
```

The live target is:

```text
HHG-STRUCTURAL.
There exists a liquid/metrized L1 object HH_C whose existence requires
prime-power graph-depth carrier fields as primitive object data before
any Gram, determinant, trace, mixed-object, or codomain construction.
The first map kappa_HH consumes those fields and is structurally
unavailable for Epstein/DH controls.
```

## 5. Updated Landing For Q134.3

Current Q134.3 status:

```text
HHG-FIRST:
  SHARPEN.
```

The sharpened target is:

```text
HHG-STRUCTURAL.
```

Answer landing:

```text
PASS:
  Name HH_C, kappa_HH, the primitive graph-depth field, conservative
  B0 embedding, Epstein/DH non-formability, and downstream dependence.

KILL:
  Prove every HHG-STRUCTURAL attempt collapses to HHG_diag,
  control-formable shadow data, side-block index data, or downstream
  forgetfulness.

SHARPEN:
  Name the exact HH/THH/graph-index lifting theorem or obstruction
  that decides HHG-STRUCTURAL.
```

## 6. What This Does Not Kill

This no-go does not cover a proposal that supplies:

```text
1. HH_C as an L1 object, not a readout;
2. graph-depth/prime-power fields as object-defining data;
3. kappa_HH before Gram, determinant, trace, M_C, or F_C;
4. control non-formability at HH_C or kappa_HH;
5. conservative B0 bank embedding;
6. downstream dependence through M_C/F_C/Tr_L;
7. zero-free freeze.
```

Such a proposal returns to docs 103, 113, 98, and 94 as a strict A3
candidate.

## 7. Witness Rule

No A3 witness is licensed.

Additional Gram/index/stress witnesses are allowed only as diagnostics
or compatibility checks. They must not be promoted to carrier evidence
unless HHG-STRUCTURAL first supplies a real object and first map.

## 8. Board Update

```text
A3:
  HHG_diag rejected/demoted.
  HHG-FIRST sharpened to HHG-STRUCTURAL.
  A3 remains HOLD_STRICT_ROUTE.
  No A3 witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 70
  Supplies the Gram diagnostic normal form used here.

doc 79 and doc 86
  Reject side-block archimedean/index coupling.

doc 93
  Rejects externally supplied forms, weights, stresses, and codomains.

doc 109
  Rejects graph/depth labels on shadow data as strict first maps.

doc 132
  Named HHG-FIRST. Doc 137 sharpens it to HHG-STRUCTURAL.

doc 134
  Follow-up board. Q134.3 should now dispatch HHG-STRUCTURAL, not a
  diagnostic HH/index package.
```

## 10. Post-doc-145 Escape Clause

Doc 145 makes the immediate live escape:

```text
HHG-SOURCE-1.
```

Do not write another diagnostic HH/index no-go unless a named
HH_C/kappa_HH source family collapses by theorem. The next HHG work
should decide source object data, first-map consumption, control
non-formability, and one downstream load-bearing slot.
