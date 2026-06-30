# 247 - Weil-etale / L-function special values do not construct the square

Status: no-go + Weil-etale / Lichtenbaum special-value / regulator carrier
boundary, 2026-06-20. One-hundred-tenth cycle of the doc-137 construction
arc. Doc 246 killed algebraic K-theory / cyclotomic trace / TC/TR/TP as
direct square construction. This document tests the adjacent special-value
repair: use Weil-etale cohomology, Lichtenbaum special values, determinant
lines, Euler characteristics, regulators, and Tamagawa/order formulas as the
carrier.

```text
Weil-etale cohomology / Lichtenbaum special values / determinant lines
  + Euler characteristic / regulator / Tamagawa-order formula
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_weil_etale_lfunction_special_value_no_go` (WET1-WET8 ALL
PASS) -- Weil-etale/L-value profiles do not determine finite-field count
anchors; Weil-etale cohomology data does not construct NS degree slots;
Euler-characteristic/regulator shadows lose correspondence endpoint data;
special-value positivity does not impose Frobenius/Rosati compatibility;
Weil-etale/L-value declarations are not constructed projection formulas;
finite special-value windows admit trace ghosts; the same formal schema is
formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_algebraic_k_cyclotomic_trace_no_go`,
`prime_int_n1b_motivic_cohomology_regulator_no_go`, and
`prime_int_n1b_galois_compatible_system_no_go`.

## 1. Purpose

The project has real evidence that special-value formulas and determinant
lines remember important arithmetic. Earlier cycles already killed motivic
regulators, triangulated motives, Arakelov intersection, Weil-standard
packages, Galois compatible systems, and algebraic K/TC as direct carriers.
The present repair is narrower:

```text
use Weil-etale cohomology and Lichtenbaum special values;
read the determinant/regulator/Euler-characteristic formula as the square
calculus.
```

This is still not construction of `End(S^2/Z)`. Weil-etale cohomology and
L-function special values are invariant or realization packages after the
object exists. They do not by themselves construct the zeta-native square
over `Z`, `rep_NS`, two degree maps, proper correspondence category,
fiber-product composition, carrier-native Frobenius graph, projection
formula, or positive Rosati.

This document rejects only the shortcut:

```text
Weil-etale / Lichtenbaum special-value / determinant-regulator data
constructs the square correspondence carrier required by End(S^2/Z).
```

It does not reject Weil-etale cohomology, Lichtenbaum formulas, regulators,
determinant lines, or special-value theorems downstream of a future global
square whose degree maps, correspondences, projection formula, Frobenius
graph, and Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 247.1 (Weil-etale/L-value special values are not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Weil-etale/L-value profile:

    Weil-etale cohomology = present
    Lichtenbaum special value = present
    determinant line = present
    regulator = present
    Euler characteristic = present
    Tamagawa/order formula = present
    duality complex = present
    finite generation = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract Weil-etale/L-value profile does not determine the
finite-field count anchor.

Nor does Weil-etale cohomology data construct the NS degree slots. Keeping
the same profile and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

An Euler-characteristic or regulator shadow can lose correspondence endpoint
data. Two classes can have the same special-value shadow (1,2) while their
endpoint coordinate differs by 4.

Special-value positivity does not impose Frobenius/Rosati compatibility. The
off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring Weil-etale duality, an L-function special-value formula, or a
regulator compatibility does not construct the square projection formula. In
the componentwise realization, the semantic projection defect remains

    27.

Finite Weil-etale/L-value windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal Weil-etale/L-value schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a Weil-etale / Lichtenbaum / L-function special-value package
constructs no Weil-etale carrier, L-function special-value carrier,
determinant-line carrier, regulator carrier, Euler-characteristic carrier,
Tamagawa/order formula, ambient square, `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_WEIL_ETALE_LFUNCTION_SPECIAL_VALUE__SPECIAL_VALUE_SHADOW_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_weil_etale_lfunction_special_value_no_go` verifies the eight
gates.

WET1 records profile non-determination. The q=7 and q=5 anchors have the
same Weil-etale/L-value profile but different count windows.

WET2 records the NS-degree-slot failure. With the same profile and z-action,
changing only the formal degree slot changes `Delta.Gamma` from `7` to `10`.

WET3 records correspondence-data loss. The special-value shadow sees the
order-of-vanishing and regulator-rank part `(1,2)` but forgets an endpoint
coordinate differing by `4`.

WET4 records Rosati non-construction. Regulator positivity and determinant
line data do not force Frobenius to be a q-similitude for the required
carrier pairing; the normalized metric defect is `5.916`.

WET5 records projection-formula failure. Weil-etale duality, L-function
special-value formulas, and regulator declarations do not construct the
square calculus; the componentwise semantic defect is still `27`.

WET6 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

WET7 records control formability. A control companion with the same formal
Weil-etale/L-value schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

WET8 records the construction failure: no Weil-etale carrier, L-value
carrier, determinant-line carrier, regulator carrier, Euler-characteristic
carrier, Tamagawa/order formula, ambient square, `rep_NS`, actual square,
proper correspondence category, fiber-product composition, carrier-native
degree maps, carrier-native pairing, projection formula, Frobenius graph,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-247:
  NEWLY CLOSED THIS CYCLE:
    - Weil-etale cohomology as square carrier, Lichtenbaum special values as
      count-anchor construction, determinant lines as correspondence
      calculus, regulator/Euler-characteristic positivity as Rosati,
      Tamagawa/order formulas as degree maps, finite special-value windows
      as ghost exclusion, and formal special-value schemas as DH/Epstein
      carrier guards (doc 247).

  STILL ADMISSIBLE:
    - Weil-etale cohomology, Lichtenbaum formulas, determinant lines,
      regulators, and special-value theorems downstream of an actual global
      square carrier;
    - a theorem showing the actual carrier's Weil-etale or special-value
      realization preserves exact integral correspondence endpoints, degree
      slots, projection formula, and Rosati;
    - controls killed at carrier formation, not after applying a
      determinant/regulator/special-value realization.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

R1 remains open. This cycle closes the Weil-etale / Lichtenbaum /
L-function special-value shortcut: these tools are allowed only after the
square carrier and its correspondence calculus have been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-WET.1 Weil-etale as square construction
  A proposal supplies Weil-etale cohomology, Lichtenbaum special values,
  determinant lines, regulators, Euler characteristics, or Tamagawa/order
  formulas and calls that the square. Kill it unless the global over-Z
  square carrier and proper maps were already constructed.

KILL-WET.2 special-value profile as count anchor
  A proposal reads the finite-field count anchor from Weil-etale groups,
  L-function special values, determinant lines, or Euler characteristics.
  Kill it: the same profile can support different count windows.

KILL-WET.3 Weil-etale class as degree maps
  A proposal uses Weil-etale classes, determinant-line degrees, regulator
  ranks, or Tamagawa/order data as the two NS degree maps. Kill it unless
  those degree maps are constructed carrier-natively.

KILL-WET.4 regulator positivity as Rosati
  A proposal uses regulator positivity, determinant-line positivity, or a
  special-value sign as the positive Rosati relation. Kill it unless
  Frobenius/Rosati compatibility is proved for the actual carrier pairing.

KILL-WET.5 special-value shadow as integral correspondence
  A proposal relies on special-value, regulator, determinant, or Euler
  characteristic shadows after forgetting endpoint, extension, or lattice
  data. Kill it unless the exact integral correspondence class is recovered
  carrier-natively.

KILL-WET.6 Weil-etale duality as projection formula
  A proposal treats Weil-etale duality, determinant-line functoriality, or
  regulator compatibility as the projection formula for End(S^2/Z). Kill it
  unless the formula is proved for the actual proper correspondence calculus.

KILL-WET.7 finite special-value checks as ghost exclusion
  A proposal verifies only a finite Weil-etale, L-value, determinant, or
  regulator window. Kill it unless ghost summands are excluded from the
  actual carrier.

KILL-WET.8 control survival
  A proposal's Weil-etale/L-value schema is formable on arbitrary control
  companion data. Kill it unless controls die at carrier construction.
```
