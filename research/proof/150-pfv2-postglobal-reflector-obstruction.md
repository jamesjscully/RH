# 150 - PFV2 post-global reflector obstruction

Status: bounded no-go from the PFV2-REL-REFLECT target / Q134.1
internal result, 2026-06-11. This is not a B1 construction, not an
external answer, and not a witness license. It kills only reflectors,
localizations, or carrier-reflecting envelopes applied after an
all-places source object is already accepted.

## 1. Purpose

Doc 149 left the surviving PFV2 route:

```text
PFV2-REL-REFLECT.
```

The most obvious next attempt is to use a reflector or localization:

```text
R_{p,q}: G -> Rel_{p,q}
```

from an all-places adelic/divisor source category `G` into a relative
p,q category. This document asks whether such a post-global reflector
can satisfy the relative-first requirement.

Answer:

```text
No, not if the reflector is applied after G-objects already exist and
kappa_rel factors through the reflected image of those G-objects.
```

## 2. Covered Class

Call a proposal `PFV2_REL_REFLECT_postG` if it satisfies all of:

```text
P150.1 all-places source category
  There is a source category G of all-places adelic/divisor/idele or
  product-formula objects.

P150.2 post-global reflector
  There is a functor, reflector, localization, completion, or envelope

    R_{p,q}: G -> Rel_{p,q}

  whose input must already be an object of G.

P150.3 relative data extracted by R
  The p,q components, complement, and product-formula certificate in
  Rel_{p,q} are obtained by applying R_{p,q} to a G-object.

P150.4 unit/counit is post-source
  The unit, counit, localization map, or envelope map is defined only
  after the G-object exists. It does not decide whether the G-object
  itself can be formed.

P150.5 kappa inherited from R(G)
  Any first map kappa_rel is defined on R_{p,q}(D) for D in G and
  factors through the post-global reflected object.

P150.6 inherited control exclusion
  Epstein/DH controls are excluded, if at all, because they cannot form
  D in G. They are not excluded by pre-global relative descent data.

P150.7 downstream uses reflected shadow
  M_C, F_C, or Tr_L uses only R_{p,q}(D) or its p,q boundary readout,
  not a relative descent datum that existed before D.
```

This class includes:

```text
localizing an all-places divisor category at p,q;
reflecting global ideles into a two-place subcategory;
carrier-reflecting envelopes whose input is already a global divisor;
relative completions or quotient functors applied to G after G is
formed.
```

## 3. Lemma

### Lemma 150.1

`PFV2_REL_REFLECT_postG` does not satisfy PFV2-REL-REFLECT.

Verdict:

```text
REJECT_POSTGLOBAL_REFLECTOR
  if R_{p,q} only acts on already accepted G-objects.

REJECT_INHERITED_SELECTIVITY
  if controls fail only at G-object formability.

REJECT_REFLECTED_SHADOW
  if downstream uses only R_{p,q}(D) after D is accepted.

HOLD_PREGLOBAL_DESCENT
  if a later proposal supplies descent/gluing data that forms before
  the all-places object.
```

### Proof

PFV2-REL-REFLECT asks for a relative structure whose unit/counit,
descent datum, or reflection theorem makes the p,q+complement field
source-defining before all-places projection.

Under P150.1-P150.3, the reflector starts with a G-object. Therefore
the all-places source is already accepted before the relative object is
formed. The relative data are extracted by applying R_{p,q}; they are
not source-prior data deciding whether the object exists.

Under P150.4, the unit/counit is post-source. It may be a genuine
adjunction or localization, but it does not change the order relevant
to PFV2: first G, then relative reflection. That is still all-places
source followed by p,q-relative readout.

Under P150.5, kappa_rel is inherited from the reflected G-object. A
first map on R_{p,q}(D) is not a first carrier-consuming map unless D
itself was formed from relative data that controls cannot form.

Under P150.6, control exclusion is inherited from G. PFV2 needs
relative-source selectivity: Epstein/DH must fail because they cannot
form the p,q+complement reflection/descent data, not merely because
they are not global-field divisors.

Under P150.7, downstream dependence is only on the reflected shadow
R_{p,q}(D). If M_C/F_C/Tr_L can be formed from this post-global image,
doc 111 still blocks promotion unless the relative field remains
load-bearing and control-exclusive there.

Thus post-global reflectors do not pass PFV2-REL-REFLECT. QED.

## 4. What Post-Global Reflectors Still Supply

Allowed:

```text
clean functorial language for external questions;
evidence that a proposed relative object has real categorical structure;
possible downstream bookkeeping if a pre-global source later passes;
tests for whether a proposed reflector is only post-global.
```

Not allowed:

```text
claiming relative-first source priority;
claiming FIRST_MAP_PASS;
declaring Epstein/DH dead at the relative map;
using R_{p,q}(D) as a witness input;
promoting inherited global exclusion to PFV2 selectivity.
```

## 5. Surviving Escape

The remaining PFV2 relative route is:

```text
PFV2-REL-DESCENT.
```

The target:

```text
There is a pre-global relative descent/gluing source

  Desc_{p,q}

whose objects consist of p and q towers, a structural complement, and
compatibility data. An all-places object D in G, if it exists, is
assembled from Desc_{p,q}; it is not the input to the relative
construction.

kappa_desc is legal because Desc_{p,q} exists; Epstein/DH controls
cannot form Desc_{p,q} or kappa_desc; B0_p and B0_q embed
conservatively; and the relative descent field remains load-bearing in
M_C/F_C/Tr_L.
```

This is narrower than PFV2-REL-REFLECT. It forbids post-global
reflectors and asks for pre-global descent/gluing source data.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named pre-global descent class:

```text
KILL-REL-DESCENT.1 assembly equivalence
  Desc_{p,q} is equivalent to first choosing D in G and then marking
  p,q.

KILL-REL-DESCENT.2 control descent
  Epstein/DH shadows can form the same descent datum while preserving
  their theta/count shadows.

KILL-REL-DESCENT.3 bank replacement
  Desc_{p,q} replaces B0_p/B0_q by the full global source rather than
  embedding them conservatively.

KILL-REL-DESCENT.4 downstream forgetfulness
  Every legal M_C/F_C/Tr_L forgets the descent datum after assembly.
```

Do not apply these to all PFV2-ADELIC-LOCAL attempts without a theorem
covering all pre-global descent sources.

## 7. Board Update

```text
PFV2_REL_REFLECT_postG:
  REJECT_POSTGLOBAL_REFLECTOR.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-REL-DESCENT or another structural
  complement source that forms before all-places assembly.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 143
  Supplies the complement-reflection/no-free-complement target.

doc 147
  Supplies the relative divisor candidate shot.

doc 148
  Rejects the ordinary classical relative tuple.

doc 149
  Rejects formal slice/fiber/pullback universal properties.

doc 111
  Still blocks downstream forgetfulness.
```

## 9. Post-doc-151 Update

Doc 151 tests the pre-global descent shot:

```text
PFV2-DESC(p,q):
  LOCAL_SCHEMA_PASS;
  LOCAL_COMP_PASS;
  HOLD_EFFECTIVE_DESCENT;
  HOLD_CONTROL_DESCENT;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.
```

The surviving target is:

```text
PFV2-DESC-SELECT.
```

Thus PFV2-REL-DESCENT remains the enclosing target, but future work
should decide whether pre-global descent data are genuinely
source-selective and downstream load-bearing, not merely equivalent to
all-places objects with p,q marking.
