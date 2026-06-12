# 149 - PFV2 formal relative universal-property obstruction

Status: bounded no-go from the PFV2-REL-UPROP target / Q134.1
internal result, 2026-06-11. This is not a B1 construction, not an
external answer, and not a witness license. It kills only formal
slice/fiber/pullback relative universal-property packages.

## 1. Purpose

Doc 148 left a narrow escape:

```text
PFV2-REL-UPROP.
```

The escape asks for a relative adelic/divisor source with a universal
property, reflection theorem, or descent/gluing axiom not equivalent to
all-places assembly plus marked p,q coordinates.

The first obvious attempt is formal: define the relative source as a
slice, fiber, pullback, or comma category over the ordinary global
divisor/idele category. This document tests that attempt.

Answer:

```text
Formal relative universal properties do not pass PFV2-REL-UPROP if the
universal property only presents marked all-places objects.
```

## 2. Covered Class

Call a proposal `PFV2_REL_UPROP_formal` if it satisfies all of:

```text
F149.1 global base category
  There is an all-places adelic/divisor/idele category G with ordinary
  product-formula or principal-divisor source objects.

F149.2 boundary/readout functor
  There is a functor

    r_{p,q}: G -> B_{p,q}

  recording p and q components, degrees, lengths, or boundary data.

F149.3 formal relative category
  The proposed relative source is built as one of:

    G / b
    b / G
    G x_{B_{p,q}} E
    a comma category involving r_{p,q}
    a fiber over a chosen p,q boundary object

  or an equivalent slice/fiber/pullback construction.

F149.4 no native relative reflector
  The construction has no reflector, localization, descent theorem, or
  gluing axiom whose unit/counit changes source formability before the
  all-places object is accepted.

F149.5 inherited kappa
  Any first map kappa_rel factors through the forgetful projection to G
  or through r_{p,q}.

F149.6 inherited control exclusion
  Epstein/DH are excluded, if at all, only because they are not objects
  of G. They are not excluded by a relative p,q+complement theorem.

F149.7 downstream not relative
  M_C, F_C, or Tr_L uses only the image in G or the p,q readout, not
  the formal relative universal property.
```

This class includes:

```text
the fiber of all divisors with fixed p,q boundary;
the slice of principal divisors over a chosen p,q divisor;
pullbacks of global divisor categories along p,q degree functors;
comma categories recording a complement object but forgetting it after
projection to G.
```

## 3. Lemma

### Lemma 149.1

`PFV2_REL_UPROP_formal` does not satisfy PFV2-REL-UPROP.

Verdict:

```text
REJECT_FORMAL_UPROP
  if the universal property presents only a marked or fibered
  all-places source.

REJECT_INHERITED_KAPPA
  if kappa_rel factors through G or r_{p,q}.

REJECT_INHERITED_SELECTIVITY
  if controls fail only because G excludes them.

HOLD_NATIVE_REFLECTOR
  if a later proposal supplies a reflector/descent theorem not covered
  by F149.1-F149.7.
```

### Proof

PFV2-REL-UPROP is not asking for any universal property. It asks for a
relative source whose universal property makes the p,q+complement
record first.

Under F149.1-F149.3, the relative category is constructed from the
all-places category G and the p,q readout functor. Its universal
property is the universal property of a slice, fiber, pullback, or
comma category. Such a property classifies maps into a diagram already
containing G and r_{p,q}. It does not by itself create a new
carrier-consuming source before the all-places object.

Under F149.4, there is no extra native relative reflection or descent
operation. Thus the relative object is a global object with typed
boundary bookkeeping. This is exactly the doc-148 surviving concern:
the notation has changed from tuple to universal property, but the
source priority has not changed.

Under F149.5, kappa_rel is inherited. PFV2 needs the first map to exist
because of the relative p,q+complement source. A map that factors
through G or r_{p,q} is still all-places source plus coordinate
readout.

Under F149.6, control exclusion is inherited from G. That may be a
valid global-field distinction, but it is not PFV2 relative
selectivity. The control must fail at the relative source or first map
while theta/count shadows remain meaningful.

Under F149.7, the relative universal property is downstream-forgotten.
Doc 111 rejects any prefix whose consumed field does not remain
load-bearing in M_C/F_C/Tr_L.

Therefore formal slice/fiber/pullback universal-property packages do
not pass PFV2-REL-UPROP. QED.

## 4. What Formal UPROP Still Supplies

Allowed:

```text
clean language for bookkeeping p,q boundary data;
a useful external question format;
tests for whether a proposed source is merely a pullback of G;
calibration for complement structurality and no-free-complement.
```

Not allowed:

```text
claiming relative-first source priority;
claiming FIRST_MAP_PASS;
declaring controls dead at the relative map;
running an A2 witness;
promoting inherited global exclusion to PFV2 selectivity.
```

## 5. Surviving Escape

The remaining PFV2 relative route is:

```text
PFV2-REL-REFLECT.
```

The target:

```text
There is a native relative reflector, localization, descent/gluing
theorem, or carrier-reflecting envelope

  R_{p,q}: G_or_preG -> Rel_{p,q}

whose unit/counit or descent datum makes the p,q+complement field
source-defining before any all-places projection, trace, determinant,
kernel, or mixed object.

kappa_rel is legal because of this native relative structure; controls
cannot form R_{p,q}(control) or kappa_rel; B0_p and B0_q embed
conservatively; and the relative field remains load-bearing downstream.
```

This is narrower than PFV2-REL-UPROP. It excludes formal pullback
universal properties and asks for a native relative reflection theorem.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only if it covers a named native-reflector
class:

```text
KILL-REL-REFLECT.1 reflector triviality
  The reflector is equivalent to inclusion of a formal slice/fiber of
  G.

KILL-REL-REFLECT.2 control reflection
  The reflector also forms for Epstein/DH shadows while preserving
  their theta/count data.

KILL-REL-REFLECT.3 bank replacement
  The reflector replaces B0_p/B0_q by the full global source instead of
  embedding them conservatively.

KILL-REL-REFLECT.4 downstream forgetfulness
  The reflected p,q+complement field is forgotten by every legal
  downstream M_C/F_C/Tr_L.
```

Do not apply these to all PFV2-ADELIC-LOCAL attempts without a theorem
covering all native relative reflectors.

## 7. Board Update

```text
PFV2_REL_UPROP_formal:
  REJECT_FORMAL_UPROP.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-REL-REFLECT or another structural
  complement source not equivalent to all-places assembly or formal
  pullback.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 142
  Rejects all-places projection.

doc 143
  Supplies the complement-reflection/no-free-complement target.

doc 147
  Supplies the relative divisor candidate shot.

doc 148
  Rejects the ordinary classical relative tuple; this document rejects
  the formal universal-property repair of that tuple.

doc 103
  Still HOLD: no FIRST_MAP_PASS.

doc 111
  Still blocks downstream forgetfulness.
```

## 9. Post-doc-150 Update

Doc 150 rejects post-global reflectors:

```text
PFV2_REL_REFLECT_postG:
  REJECT_POSTGLOBAL_REFLECTOR.
```

The surviving target is:

```text
PFV2-REL-DESCENT.
```

Thus PFV2-REL-REFLECT remains only as an enclosing historical stage.
Future work should ask for pre-global descent/gluing source data, not
a reflector applied after an all-places source object exists.
