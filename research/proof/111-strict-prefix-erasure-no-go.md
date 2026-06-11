# 111 - Strict-prefix erasure no-go

Status: bounded no-go / post-doc-103 hardening, 2026-06-11. This
handles the next false positive after doc 109: a proposal names a real
strict first carrier-consuming map, but the later S3 trace package
forgets the consumed primitive field before building `M_C`, `F_C`, or
`Tr_L`.

## 1. Purpose

Doc 103 asks for a first map:

```text
kappa_C: S_C -> Y_C
```

that consumes primitive Euler-carrier data before shadow-stable
operations. Passing that precheck is not enough. The consumed primitive
field must remain load-bearing in the downstream mixed object,
same-form codomain, trace theorem, bank embedding, and control
exclusion.

This document rejects strict-prefix proposals of the form:

```text
S_C -> Y_C -> U(Y_C) -> M_C -> F_C -> Tr_L(F_C),
```

where `S_C -> Y_C` may be strict, but `U(Y_C)` forgets the primitive
carrier field before the trace package is formed.

## 2. Erasure Hypotheses

Let a proposal have a named strict first map `kappa_C: S_C -> Y_C`.
Say it has strict-prefix erasure if all of the following hold.

```text
H111.1 first map supplied
  A plausible S_C and kappa_C are named, and kappa_C consumes at least
  one primitive field among alpha, v, depth, ell, mu_C, Euler
  factorization, or graph-depth.

H111.2 downstream forgetful image
  Before M_C, F_C, or Tr_L is formed, the construction applies a
  forgetful, quotient, completion, pushforward, decategorification,
  measure, determinant/coker, kernel, trace-class, or localizing
  operation U that discards the consumed primitive field.

H111.3 trace package factors through U
  The later mixed object, same-form codomain, traceability theorem, or
  trace value depends only on U(Y_C), not on the primitive field
  consumed by kappa_C. Varying or deleting the consumed field inside
  one U-fiber leaves the same typed M_C, maps into M_C, F_C, trace
  theorem, codomain, or trace value.

H111.4 control reconstruction
  Epstein or DH controls can form the same U(Y_C) and the same typed
  downstream M_C/F_C/Tr_L package. One valid control branch is enough
  for rejection, but the branch must be named. The control need not
  form the original strict S_C or kappa_C if the no-go is downstream
  forgetfulness.

H111.5 no downstream carrier test
  After U, there is no second carrier/effectivity map where the
  consumed primitive field is required again before signs, positivity,
  regularization, zero comparison, or post-selection.

H111.6 bank and same-form dependence lost
  The B0 bank embedding and the comb-continuum mixed object, if named,
  preserve only the shadow image U(Y_C), not the primitive carrier data
  needed to exclude controls.
```

## 3. Lemma

### Lemma 111.1

Under H111.1-H111.6, a strict first map does not advance the S3
strict-domain target. The proposal routes to the downstream erasure
failure, not to witness construction.

Verdict:

```text
REJECT_DOWNSTREAM_FORGETFUL
  kappa_C may be strict, but the later trace package factors through a
  shadow image that forgets the consumed primitive field.

REJECT_ORPHAN_FIRST_MAP
  the primitive field is consumed by kappa_C but is not load-bearing for
  the mixed object, codomain, or trace.

REJECT_CARRIER_OVERREACH
  the same typed downstream package is formable for Epstein or DH
  controls after erasure.

REJECT_BANK
  the B0 comb/address/count/guard data are embedded only through the
  erased shadow image.

REJECT_LS4
  the mixed object does not keep the carrier-selective field
  load-bearing in the same-form coupling.

ROUTE_TO_DOC98
  a downstream carrier-dependent trace package is supplied and the
  consumed primitive field remains load-bearing through M_C/F_C/Tr_L.
```

### Proof

Doc 103 supplies only an admission precheck: a first primitive
carrier-consuming map exists before `M_C`, `F_C`, or `Tr_L`. Doc 98
requires more: the strict Euler-carrier domain must support legal
trace, conservative bank embedding, one same-form mixed object, a
trace-derived codomain, control exclusion, and zero-free freeze.

Under H111.1, the precheck may be plausible. Under H111.2-H111.3, the
load-bearing downstream trace package factors through `U(Y_C)` after
the primitive field has been discarded. Thus the primitive field
consumed by `kappa_C` is no longer used to form `M_C`, `F_C`, or
`Tr_L`.

By H111.4, the selected control can form the same typed downstream
package after erasure. By H111.5, no later carrier/effectivity map
restores structural control exclusion before signs, positivity, zeros,
comparison, or post-selection. By H111.6, the bank and same-form
coupling do not preserve the carrier-selective field either.

Therefore the proposal fails the doc-87 carrier-selectivity timing
condition at the actual load-bearing trace package, and it also fails
the doc-98 requirement that carrier exclusion, bank embedding, and
same-form M_C/F_C stay tied to the strict carrier domain. QED.

## 4. Decision Test

For any proposal with a plausible doc-103 first map, ask:

```text
F111.1
  Which primitive field does kappa_C consume?

F111.2
  Where does that field appear in M_C?

F111.3
  Where does that field appear in F_C or in the trace-derived form?

F111.4
  Does the trace theorem apply to Y_C as a carrier object, or only to a
  forgetful/quotient/completed shadow U(Y_C)?

F111.5
  Can Epstein or DH controls form U(Y_C) and the same downstream
  M_C/F_C/Tr_L package?

F111.6
  Does b1 preserve the primitive carrier field into the mixed object,
  or only the p^Z comb/count shadow?

F111.7
  If the field is forgotten, is there a second carrier-consuming map
  before signs, positivity, zeros, comparison, or post-selection?
```

If F111.2-F111.6 show downstream erasure, record
`REJECT_DOWNSTREAM_FORGETFUL` or `REJECT_ORPHAN_FIRST_MAP`. If F111.7
names a real second carrier map, route back to doc 98 as
`HOLD_STRICT_EULER` until all remaining fields are filled.

## 5. Covered Patterns

The no-go covers:

```text
a strict source followed by ordinary measure pushforward before trace;
a valuation-consuming map followed by a trace-class closure that
depends only on lengths or counts;
a graph-depth map followed by determinant/coker data that only sees a
shadow index;
a carrier source embedded into a liquid object whose trace theorem
uses only the bare circle or positive measure shadow;
a strict prefix whose output is used only to choose a later weight,
window, codomain, or regularization.
```

## 6. Non-Coverage

This no-go does not apply if:

```text
1. the trace theorem is stated on Y_C as a strict carrier object;
2. the consumed primitive field remains object data through M_C;
3. F_C or the trace-derived form depends on that field before
   evaluation;
4. b1 embeds the B0 bank while preserving the carrier-selective guard;
5. Epstein/DH controls cannot form the downstream trace package for the
   same structural reason that they could not form kappa_C;
6. zero-free freeze is recorded before first zero contact.
```

Such a proposal remains live and must be scored by doc 98 and the
local ledgers.

This document also does not claim the first map is fake. If `S_C` is
only decorated shadow data, use doc 109. Doc 111 starts after a
plausible local doc-103 first map and asks whether the consumed
primitive field remains load-bearing downstream.

## 7. Relation To Existing Docs

```text
doc 86
  Supplies the same-form coupling requirement; erasure before M_C is an
  LS4 failure.

doc 87
  Supplies the carrier-selectivity timing condition.

doc 89
  Supplies the conservative bank-embedding requirement; embedding only
  a forgotten shadow is bank failure.

doc 94
  Requires the carrier-reading form/codomain to be trace-derived, not
  reintroduced after erasure.

doc 98
  States the strict Euler-carrier trace-domain target that this no-go
  protects from dead-prefix passes.

doc 103
  Supplies the first-map precheck. Doc 111 starts after a plausible
  first map is named.

doc 108 and doc 109
  Cover earlier failures: broad shadow-functorial overreach and
  relabeled-shadow first maps.
```

## 8. Use Rule

Use doc 111 after a proposal has a plausible doc-103 first map but
before recording any doc-98 `PASS_STRICT_EULER`. The question is
whether the primitive field consumed by the first map remains
load-bearing in the actual trace package.

Do not cite doc 111 against a proposal whose downstream trace theorem,
mixed object, and codomain are genuinely carrier-dependent all the way
through evaluation. Score that proposal through doc 98 instead.
