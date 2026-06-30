# 239 - Motivic cohomology regulators do not construct the square

Status: no-go + motivic cohomology / higher Chow / regulator carrier
boundary, 2026-06-20. One-hundred-second cycle of the doc-137 construction
arc. Doc 238 killed bivariant / operational Chow as square construction.
This document tests the next repair: use motivic cohomology, higher Chow
complexes, Chern characters, cycle maps, products, and regulators or
realizations to supply `rep_NS` and the correspondence calculus.

```text
motivic cohomology / higher Chow / Chern character / regulator
  -> cycle classes and realizations
  -> rep_NS and projection formula
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_motivic_cohomology_regulator_no_go` (MCR1-MCR8 ALL PASS) --
motivic/regulator profiles do not determine finite-field count anchors;
motivic cycle classes do not construct NS degree slots; rational
Chern/regulator images lose integral correspondence data; regulator
realizations do not impose Frobenius/Rosati compatibility; motivic
product/regulator declarations are not constructed projection formulas;
finite motivic/regulator windows admit trace ghosts; the same formal schema
is formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_bivariant_operational_chow_no_go` (BOC1-BOC8 ALL PASS),
`prime_int_n1b_nc_hodge_realization_no_go` (NHR1-NHR6 ALL PASS), and
`prime_int_n1b_prismatic_syntomic_package_no_go` (PSP1-PSP7 ALL PASS).

## 1. Purpose

Doc 238 says bivariant and operational Chow operations are downstream of
an ambient square with proper maps, orientations, and degree maps. The next
repair is to appeal to a more universal cycle package:

```text
construct motivic cohomology or higher Chow groups;
apply the cycle map, Chern character, and regulator;
read rep_NS, products, projection, and positivity from the realization.
```

This is still not construction of `End(S^2/Z)`. Motivic cohomology,
higher Chow complexes, Chern characters, and regulators are attached to a
carrier. They do not by themselves construct the over-`Z` square, the
proper correspondence category, the two degree maps, the diagonal,
Frobenius graph, ambient pairing, fiber-product correspondence composition,
projection formula, or positive Rosati relation.

This document rejects only the shortcut:

```text
motivic cohomology or a regulator package constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject motivic cohomology, higher Chow groups, Chern
characters, cycle maps, or regulators downstream of a future zeta-native
square whose carrier, proper maps, degree maps, correspondences, projection
formula, Frobenius graph, and Rosati have already been constructed.

## 2. Lemma

```text
Lemma 239.1 (Motivic/regulator packages are not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy motivic/regulator profile:

    higher Chow complex = present,
    motivic cohomology = present,
    cycle map          = present,
    Chern character    = present,
    regulator          = present,
    product            = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract motivic/regulator profile does not determine the
finite-field count anchor.

Nor does a motivic cycle class construct the NS degree slots. Keeping the
same z-component while changing the formal triple from (7,F,1) to (10,F,1)
changes

    Delta . Gamma  from 7 to 10.

Rational Chern/regulator images can also lose integral correspondence
data. Two integral classes with different torsion coordinate can have the
same rational image while the integral gap remains 2.

Positive regulator or realization data does not impose the Frobenius/Rosati
compatibility relation. A positive metric can coexist with a normalized
metric defect of 5.916.

Declaring product and regulator compatibility does not construct the
projection formula for the square. In the componentwise realization, the
semantic projection defect remains

    27.

Finite motivic/regulator windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal motivic/regulator schema is formable on arbitrary control
companion data with no motivic carrier, higher Chow complex, regulator
theorem, ambient square, `rep_NS`, or positive Rosati.

Consequently a motivic cohomology / higher Chow / regulator package
constructs no motivic cohomology object over the zeta square, higher Chow
complex, cycle map, Chern character, regulator, Deligne realization,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_MOTIVIC_COHOMOLOGY_REGULATOR__REALIZATION_DATA_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_motivic_cohomology_regulator_no_go` verifies the eight gates.

MCR1 records profile non-determination. The q=7 and q=5 anchors have the
same motivic/regulator profile but different count windows.

MCR2 records the NS-degree-slot failure. With the same motivic z-class,
changing only the formal degree slot changes `Delta.Gamma` from `7` to
`10`.

MCR3 records integral-data loss. A rationalized Chern/regulator image can
kill torsion while the integral correspondence class still differs.

MCR4 records Rosati non-construction. Positive realization data does not
force Frobenius to be a q-similitude for the required pairing; the
normalized metric defect is `5.916`.

MCR5 records projection-formula failure. Declaring product and regulator
compatibility does not construct the square calculus; the componentwise
semantic defect is still `27`.

MCR6 records finite-window trace ghosts. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

MCR7 records control formability. A control companion with the same formal
motivic/regulator schema has count window `8,112,1064` and metric defect
`9.950`, with no motivic carrier, higher Chow complex, regulator theorem,
ambient square, `rep_NS`, or Rosati input.

MCR8 records the construction failure: no motivic cohomology object,
higher Chow complex, cycle map, Chern character, regulator, Deligne
realization, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-239:
  NEWLY CLOSED THIS CYCLE:
    - motivic cohomology as global square carrier, higher Chow complex as
      rep_NS construction, Chern/regulator realization as integral
      correspondence construction, motivic product as projection formula,
      finite motivic windows as ghost exclusion, and formal
      motivic/regulator schemas as DH/Epstein carrier guards (doc 239).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper maps, degree maps,
      correspondence category, projection formula, Frobenius graph, and
      Rosati are constructed before motivic cohomology is invoked;
    - motivic cohomology, higher Chow, Chern character, cycle maps, and
      regulators downstream of an actual square;
    - a theorem excluding ghost motivic summands from the actual carrier;
    - controls killed at carrier formation, not after applying realization.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      and square-side properness.
```

R1 remains open. This cycle closes the motivic/regulator shortcut: cycle
complexes, Chern characters, and regulators are useful only after the
spaces, proper maps, correspondences, and degree maps have already been
constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-MCR.1 motivic cohomology as square construction
  A proposal supplies motivic cohomology or higher Chow data and calls it
  the square. Kill it unless the global over-Z square carrier and proper
  maps were already constructed.

KILL-MCR.2 motivic/regulator profile as count anchor
  A proposal reads the zeta count anchor from the existence of a motivic
  complex, cycle map, Chern character, regulator, realization, or product.
  Kill it: the same profile can support different count windows.

KILL-MCR.3 motivic cycle class as degree maps
  A proposal uses a motivic cycle class as the two NS degree maps. Kill it
  unless those degree maps are constructed carrier-natively.

KILL-MCR.4 rational Chern/regulator image as integral correspondence
  A proposal identifies the integral correspondence lattice through a
  rational Chern character or regulator alone. Kill it unless integral and
  torsion data are recovered carrier-natively.

KILL-MCR.5 regulator positivity as Rosati
  A proposal uses positive realization data as the positive Rosati relation.
  Kill it unless Frobenius/Rosati compatibility is proved for the actual
  carrier pairing.

KILL-MCR.6 motivic product as projection formula
  A proposal treats the motivic product or regulator compatibility as the
  projection formula for End(S^2/Z). Kill it unless the formula is proved
  for the actual proper correspondence calculus.

KILL-MCR.7 finite motivic checks as ghost exclusion
  A proposal verifies only a finite regulator or motivic trace window. Kill
  it unless ghost motivic summands are excluded from the actual carrier.

KILL-MCR.8 control survival
  A proposal's motivic/regulator schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
