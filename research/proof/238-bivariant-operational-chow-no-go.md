# 238 - Bivariant operational Chow does not construct the square

Status: no-go + bivariant / operational Chow carrier boundary, 2026-06-20.
One-hundred-first cycle of the doc-137 construction arc. Doc 237 killed
derived cycle-stack / virtual-intersection data as square construction. This
document tests the intersection-theory repair: use operational Chow,
bivariant oriented cohomology, refined Gysin maps, cap products, and
projection formulas to supply the missing correspondence calculus.

```text
operational Chow / bivariant theory
  -> refined Gysin maps and cap products
  -> projection formula and rep_NS
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_bivariant_operational_chow_no_go` (BOC1-BOC8 ALL PASS) --
operational Chow profiles do not determine finite-field count anchors;
bivariant classes do not construct NS degree slots; finite operational tests
admit ghost bivariant classes; declaring projection in the operational
profile is not constructed calculus; oriented Gysin data does not construct
the degree character; the same formal operational schema is formable on
controls; finite operational windows admit trace ghosts; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_derived_cycle_stack_no_go` (DCS1-DCS7 ALL PASS),
`prime_int_n1b_six_functor_trace_no_go` (SFT1-SFT7 ALL PASS), and
`prime_int_n1b_projection_formula_quotient_no_go` (PFQ1-PFQ6 ALL PASS).

## 1. Purpose

Doc 237 says derived/virtual intersection machinery is downstream of an
ambient oriented square. The next repair is more formal:

```text
do not derive the moduli;
use operational Chow or bivariant oriented cohomology,
where Gysin maps and projection formulas are part of the package.
```

This is still not construction of `End(S^2/Z)`. Operational Chow and
bivariant theories act on cycles of existing spaces and proper maps. They
do not by themselves construct the over-`Z` square, orientations, the two
fiber degree maps, the diagonal, Frobenius graph, ambient pairing,
fiber-product correspondence composition, or positive Rosati relation.

This document rejects only the shortcut:

```text
the operational/bivariant formalism constructs the square correspondence
carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose bivariant or
operational Chow theory is constructed after the square, its proper maps,
orientations, and degree maps are already carrier-native.

## 2. Lemma

```text
Lemma 238.1 (Operational Chow is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy operational profile:

    refined Gysin       = present,
    proper pushforward  = present,
    flat pullback       = present,
    cap product         = present,
    projection formula  = declared.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract operational profile does not determine the
finite-field count anchor.

Nor does a bivariant class construct the NS degree slots. Keeping the same
operational z-action while changing the formal triple from (7,F,1) to
(10,F,1) changes

    Delta . Gamma  from 7 to 10.

Finite operational tests do not determine the operation. Two operations can
agree on all tested cycle classes and differ on a ghost class.

Declaring the projection formula in the operational profile is not
constructed correspondence calculus. In the componentwise realization, the
semantic projection defect remains

    27.

Oriented Gysin data also does not construct the degree character. The same
base degree 7 gives pushforwards

    7 and -7

under two orientation choices.

The same formal operational Chow schema is formable on arbitrary control
companion data with no actual bivariant theory, operational Chow ring,
ambient square, `rep_NS`, or positive Rosati.

Finite operational windows remain unsafe: a 5-cycle trace ghost preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

Consequently a bivariant / operational Chow package constructs no bivariant
theory over the zeta square, operational Chow ring, refined Gysin calculus,
orientation, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_BIVARIANT_OPERATIONAL_CHOW__OPERATIONS_NEED_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_bivariant_operational_chow_no_go` verifies the eight gates.

BOC1 records profile non-determination. The q=7 and q=5 anchors have the
same operational Chow profile but different count windows.

BOC2 records the NS-degree-slot failure. With the same operational z-action,
changing only the formal degree slot changes `Delta.Gamma` from `7` to `10`.

BOC3 records operational ghost freedom. Two operations agree on two tested
cycle classes and differ on a ghost class by norm `1`.

BOC4 records projection-formula failure. Declaring refined Gysin and
projection does not construct the calculus; the componentwise semantic
defect is still `27`.

BOC5 records orientation dependence. The same base degree `7` gives
pushforwards `7` and `-7` under two orientations. Thus oriented Gysin data
does not construct the degree character unless the orientation is
carrier-native.

BOC6 records control formability. A control companion with the same formal
operational Chow schema has count window `8,112,1064` and metric defect
`9.950`, with no actual bivariant theory, operational Chow ring, square,
`rep_NS`, or Rosati input.

BOC7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

BOC8 records the construction failure: no bivariant theory, operational
Chow ring, refined Gysin calculus, orientation, ambient square, `rep_NS`,
actual square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-238:
  NEWLY CLOSED THIS CYCLE:
    - operational Chow as global square carrier, bivariant class as rep_NS
      construction, refined Gysin calculus as degree-map construction,
      operational projection formula as correspondence calculus, finite
      operational tests as ghost exclusion, and formal operational schemas
      as DH/Epstein carrier guards (doc 238).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper maps, orientations,
      and degree maps are constructed before bivariant operations are
      invoked;
    - operational or bivariant intersection theory downstream of an actual
      square with degree maps, correspondences, projection formula,
      Frobenius graph, and Rosati;
    - a theorem excluding ghost bivariant classes from the actual carrier;
    - controls killed at carrier formation, not after applying operational
      Chow.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the operational/bivariant shortcut:
Gysin and projection operations are useful only after the spaces, proper
maps, orientations, and degree maps have already been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-BOC.1 operational Chow as square construction
  A proposal supplies operational Chow or bivariant theory and calls it the
  square. Kill it unless the global over-Z square carrier and proper maps
  were already constructed.

KILL-BOC.2 operational profile as count anchor
  A proposal reads the zeta count anchor from the existence of Gysin,
  pushforward, pullback, cap product, or projection operations. Kill it: the
  same profile can support different count windows.

KILL-BOC.3 bivariant class as degree maps
  A proposal uses a bivariant class as the two NS degree maps. Kill it unless
  those degree maps are constructed carrier-natively.

KILL-BOC.4 projection formula by operational declaration
  A proposal declares the projection formula as part of the formalism. Kill
  it unless the formula is proved for the actual carrier and preserves the
  finite-field count anchor.

KILL-BOC.5 orientation as external sign
  A proposal chooses an orientation or Thom class externally. Kill it unless
  the orientation is constructed by the square carrier.

KILL-BOC.6 finite operational tests
  A proposal verifies finitely many operational or trace identities. Kill it
  unless ghost bivariant classes are excluded carrier-natively.

KILL-BOC.7 operational schema on controls
  A proposal declares operational Chow labels on arbitrary control companion
  data. Kill it unless controls die at carrier formation.

KILL-BOC.8 bivariant package as End(S^2/Z)
  A proposal promotes bivariant operations directly to End(S^2/Z). Kill it
  unless it constructs square H2, intersection form, correspondences,
  Frobenius graph, Laurent boundary data, DD.4 weight>=1 datum, and positive
  Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 101 = doc 238:
  N1B_BIVARIANT_OPERATIONAL_CHOW__OPERATIONS_NEED_CARRIER__NO_GO.

What got built: no End object. The value is a sharper operational boundary:
bivariant operations act on an already-constructed carrier; they are not the
construction of that carrier.

What remains: construct the global square carrier first; construct degree
maps, diagonal, Frobenius graph, correspondence composition, projection
formula, and positive Rosati; then operational/bivariant Chow may be used to
organize the calculus.
```
