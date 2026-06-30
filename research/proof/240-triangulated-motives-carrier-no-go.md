# 240 - Triangulated motives do not construct the square

Status: no-go + triangulated / mixed motives carrier boundary, 2026-06-20.
One-hundred-third cycle of the doc-137 construction arc. Doc 239 killed
motivic cohomology, higher Chow, Chern characters, and regulators as direct
square construction. This document tests the next repair: use the ambient
motivic category itself, with tensor products, Tate twists, t-structures,
weight structures, realizations, and conservativity, to supply `rep_NS` and
the correspondence calculus.

```text
triangulated / mixed motives
  -> tensor, Tate twists, t-structure, weight structure, realizations
  -> rep_NS, graph, projection formula, and positivity
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_triangulated_motives_carrier_no_go` (TMC1-TMC8 ALL PASS) --
abstract motivic-category profiles do not determine finite-field count
anchors; motivic category data does not construct NS degree slots;
triangulated `K_0` shadows lose extension/correspondence data; declared
realization conservativity does not exclude phantom motives; tensor, Tate,
and projection declarations are not a constructed projection formula;
finite motivic-category windows admit trace ghosts; the same formal schema
is formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_motivic_cohomology_regulator_no_go` (MCR1-MCR8 ALL PASS),
`prime_int_n1b_six_functor_trace_no_go` (SFT1-SFT7 ALL PASS), and
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS).

## 1. Purpose

Doc 239 says motivic cohomology, higher Chow complexes, Chern characters,
and regulators are downstream of a carrier. The next repair is to make the
carrier the ambient motivic category:

```text
construct a triangulated or mixed-motive category for zeta;
use tensor, Tate twists, t-structures, weight structures, and realizations;
declare or prove enough conservativity to recover the square.
```

This is still not construction of `End(S^2/Z)`. A motivic category can
house a square only after the square object, proper correspondences, degree
maps, Frobenius graph, projection formula, and positive Rosati have been
constructed in it. The abstract category profile, tensor structure, Tate
twist, or realization functor is not itself the over-`Z` square.

This document rejects only the shortcut:

```text
the ambient triangulated/mixed-motive category constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square inside a motivic category,
provided the square, proper maps, correspondence category, degree maps,
projection formula, Frobenius graph, and Rosati are carrier-native and not
read from categorical labels alone.

## 2. Lemma

```text
Lemma 240.1 (Triangulated motives are not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy motivic-category profile:

    tensor triangulated category       = present,
    Tate twists                        = present,
    compact generation                 = present,
    six-functor-style operations       = present,
    t-/weight-structure data           = present,
    realization functor                = present,
    realization conservativity declared= present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract motivic-category profile does not determine the
finite-field count anchor.

Nor does the category data construct the NS degree slots. Keeping the same
abstract motive and z-action while changing the formal triple from (7,F,1)
to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Triangulated `K_0` shadows lose extension and correspondence data. Two
objects can have the same Euler shadow 1 while their extension coordinate
differs by 3. The square needs actual correspondences and composition, not
only a decategorified class.

Declaring realization conservativity is not a carrier theorem. A phantom
summand can have zero tested realization coordinates while retaining
internal norm 1 unless conservativity is proved for the actual carrier.

Tensor, Tate twist, and projection declarations do not construct the
projection formula for the square. In the componentwise realization, the
semantic projection defect remains

    27.

Finite motivic-category windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal motivic-category schema is formable on arbitrary control
companion data with no zeta square motive, actual motivic category,
`rep_NS`, correspondence composition, or positive Rosati.

Consequently a triangulated / mixed motives package constructs no motivic
category for the zeta square, mixed-motive heart, motivic t-structure,
weight structure, Tate-twist degree character, realization conservativity
theorem, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_TRIANGULATED_MOTIVES__CATEGORY_LABELS_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_triangulated_motives_carrier_no_go` verifies the eight gates.

TMC1 records profile non-determination. The q=7 and q=5 anchors have the
same motivic-category profile but different count windows.

TMC2 records the NS-degree-slot failure. With the same abstract motive and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

TMC3 records decategorification loss. The same `K_0` Euler shadow can hide
different extension/correspondence data.

TMC4 records the phantom/conservativity failure. Declaring realization
conservativity does not exclude a nonzero internal phantom unless a
carrier-native conservativity theorem is proved.

TMC5 records projection-formula failure. Declaring tensor, Tate twists, and
projection does not construct the square calculus; the componentwise
semantic defect is still `27`.

TMC6 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

TMC7 records control formability. A control companion with the same formal
motivic-category schema has count window `8,112,1064` and metric defect
`9.950`, with no zeta square motive, actual motivic category, `rep_NS`,
correspondence composition, or Rosati input.

TMC8 records the construction failure: no triangulated motive category,
mixed-motive heart, motivic t-structure, weight structure, Tate-twist
degree character, realization conservativity theorem, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing,
projection formula, Frobenius graph, positive Rosati, control death, or
DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-240:
  NEWLY CLOSED THIS CYCLE:
    - triangulated motives as global square carrier, mixed-motive heart as
      rep_NS construction, Tate twists as the degree character, realization
      conservativity as phantom exclusion, tensor/product structure as
      projection formula, finite motivic-category windows as ghost
      exclusion, and formal motivic-category schemas as DH/Epstein carrier
      guards (doc 240).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z constructed inside a motivic
      category after its square object, proper maps, degree maps,
      correspondence composition, projection formula, Frobenius graph, and
      Rosati are built;
    - motivic t-/weight-structures, Tate twists, realizations, and
      conservativity downstream of that actual square;
    - a theorem excluding phantom or ghost motivic summands from the actual
      carrier;
    - controls killed at carrier formation, not after applying the motivic
      category formalism.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      and square-side properness.
```

R1 remains open. This cycle closes the ambient-motivic-category shortcut:
categories, hearts, weights, Tate twists, and realizations are allowed only
after the square carrier and its correspondence calculus have been
constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-TMC.1 motivic category as square construction
  A proposal supplies triangulated motives, mixed motives, or a universal
  motivic category and calls it the square. Kill it unless the global over-Z
  square carrier and proper maps were already constructed inside it.

KILL-TMC.2 category profile as count anchor
  A proposal reads the zeta count anchor from tensor, Tate twists, compact
  generation, six functors, t-/weight-structures, or realizations. Kill it:
  the same profile can support different count windows.

KILL-TMC.3 category object as degree maps
  A proposal uses a motivic object or Hom group as the two NS degree maps.
  Kill it unless those degree maps are constructed carrier-natively.

KILL-TMC.4 K0 shadow as correspondence calculus
  A proposal works only after decategorifying to K0 or Euler data. Kill it
  unless extension data and correspondence composition are recovered
  carrier-natively.

KILL-TMC.5 realization conservativity as phantom exclusion
  A proposal assumes realization conservativity to exclude phantom motives.
  Kill it unless the conservativity theorem is proved for the actual
  carrier.

KILL-TMC.6 tensor/Tate declarations as projection formula
  A proposal treats tensor products, Tate twists, or formal projection
  operations as the projection formula for End(S^2/Z). Kill it unless the
  formula is proved for the actual proper correspondence calculus.

KILL-TMC.7 finite motivic-category checks as ghost exclusion
  A proposal verifies only a finite motivic trace or realization window.
  Kill it unless ghost motivic summands are excluded from the actual carrier.

KILL-TMC.8 control survival
  A proposal's motivic-category schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
