# 237 - Derived cycle stacks do not construct the square

Status: no-go + derived cycle-stack / virtual-intersection carrier boundary,
2026-06-20. One-hundredth cycle of the doc-137 construction arc. Doc 236
killed ordinary Chow/Hilbert cycle moduli as square construction. This
document tests the derived repair: use a derived Hilbert/Chow stack, perfect
obstruction theory, virtual fundamental class, and derived intersections to
produce the missing correspondence calculus.

```text
derived Hilbert/Chow stack + perfect obstruction theory
  -> virtual fundamental classes and derived intersections
  -> projection formula and rep_NS
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_derived_cycle_stack_no_go` (DCS1-DCS7 ALL PASS) -- derived
cycle-stack profiles do not determine finite-field count anchors; virtual
cycle data does not construct NS degree slots; virtual classes depend on
extra obstruction/orientation data; derived pull-push declarations are not a
constructed projection formula; finite derived windows admit ghost
obstruction summands; the same formal derived cycle-stack schema is formable
on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_chow_hilbert_cycle_moduli_no_go` (CHM1-CHM7 ALL PASS),
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS),
and `prime_int_n1b_projection_formula_quotient_no_go` (PFQ1-PFQ6 ALL PASS).

## 1. Purpose

Doc 236 says ordinary Hilbert/Chow moduli are downstream of the ambient
square. The next repair is to say that the missing structure appears only
after deriving the cycle moduli:

```text
ordinary moduli miss intersections;
derived moduli carry the cotangent complex and obstruction theory;
virtual pull-push supplies the correspondence calculus.
```

This is still not construction of `End(S^2/Z)`. Derived intersections and
virtual fundamental classes refine intersection theory once the ambient
derived stack, orientation, proper maps, degree maps, and pull-push
formalism are already present. They do not by themselves construct the
over-`Z` square, the two fiber degree maps, the diagonal, Frobenius graph,
ambient pairing, projection formula, or positive Rosati relation.

This document rejects only the shortcut:

```text
the derived Hilbert/Chow stack and its virtual class construct the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose derived correspondence
stack and orientation are constructed carrier-natively before virtual
intersection theory is applied.

## 2. Lemma

```text
Lemma 237.1 (Derived virtual data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy derived-cycle profile:

    cotangent amplitude      = [-1,0],
    perfect obstruction      = present,
    orientation              = present,
    virtual fundamental class = present,
    derived intersection     = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract derived-cycle profile does not determine the
finite-field count anchor.

Nor does virtual cycle data construct the NS degree slots. Keeping the same
derived z-cycle while changing the formal triple from (7,F,1) to (10,F,1)
changes

    Delta . Gamma  from 7 to 10.

The virtual fundamental class depends on obstruction and orientation data not
supplied by the profile. The same classical degree 7 can yield virtual
degrees

    7 and -14

under different obstruction Euler factors.

Derived pull-push declarations do not construct the projection formula. In
the componentwise correspondence realization, the semantic projection defect
is

    27.

Finite derived windows remain unsafe: a 5-cycle ghost obstruction summand
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal derived cycle-stack schema is formable on arbitrary control
companion data with no actual derived Hilbert stack, perfect obstruction
theory, orientation, ambient square, or positive Rosati.

Consequently a derived cycle-stack / virtual-intersection package constructs
no derived Hilbert stack over the zeta square, derived Chow stack, perfect
obstruction theory, virtual fundamental class, orientation, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, DH/Epstein death, DD.4 weight>=1
datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_DERIVED_CYCLE_STACK__VIRTUAL_DATA_DOWNSTREAM_OF_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_derived_cycle_stack_no_go` verifies the seven gates.

DCS1 records profile non-determination. The q=7 and q=5 anchors have the
same derived-cycle profile but different count windows.

DCS2 records the NS-degree-slot failure. With the same derived z-cycle,
changing only the formal degree slot changes `Delta.Gamma` from `7` to `10`.

DCS3 records virtual-class dependence. The same classical degree `7` has
virtual degrees `7` and `-14` under different obstruction/orientation data.

DCS4 records projection-formula failure. Declaring derived fiber products and
virtual pull-push does not construct the calculus; the componentwise
semantic defect remains `27`.

DCS5 records finite-window ghost survival. A 5-cycle ghost obstruction
summand preserves the first four traces and changes count 5 by `5`.

DCS6 records control formability. A control companion with the same formal
derived cycle-stack schema has count window `8,112,1064` and metric defect
`9.950`, with no actual derived stack, perfect obstruction theory,
orientation, square, or Rosati input.

DCS7 records the construction failure: no derived Hilbert stack, derived Chow
stack, perfect obstruction theory, virtual fundamental class, orientation,
ambient square, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, control
death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-237:
  NEWLY CLOSED THIS CYCLE:
    - derived Hilbert/Chow stack as global square carrier, perfect
      obstruction theory as rep_NS construction, virtual fundamental class
      as ambient pairing, derived pull-push as projection formula, finite
      derived windows as ghost exclusion, and formal derived cycle-stack
      schemas as DH/Epstein carrier guards (doc 237).

  STILL ADMISSIBLE:
    - a carrier-native global derived square over Z whose proper
      correspondence stack, orientation, and degree maps are constructed
      before virtual intersection theory is invoked;
    - derived/virtual intersection theory downstream of an actual square
      with degree maps, correspondences, projection formula, Frobenius graph,
      and Rosati;
    - a theorem excluding ghost obstruction summands from the actual carrier;
    - controls killed at carrier formation, not after deriving cycle moduli.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the derived-cycle shortcut: virtual
intersection machinery is useful only after the ambient square, orientation,
and correspondence calculus have already been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-DCS.1 derived cycle stack as square construction
  A proposal supplies a derived Hilbert/Chow stack and calls it the square.
  Kill it unless the global over-Z square carrier was already constructed.

KILL-DCS.2 derived profile as count anchor
  A proposal reads the zeta count anchor from cotangent amplitude, obstruction
  theory, or virtual class data. Kill it: the same profile can support
  different count windows.

KILL-DCS.3 virtual class as degree map
  A proposal uses a virtual fundamental class as the two NS degree maps. Kill
  it unless those degree maps are constructed carrier-natively.

KILL-DCS.4 derived pull-push as projection formula
  A proposal declares virtual pull-push and treats projection as automatic.
  Kill it unless the projection formula is proved in the actual carrier.

KILL-DCS.5 finite derived window
  A proposal verifies finitely many derived, virtual, Frobenius, or trace
  identities. Kill it unless ghost obstruction summands are excluded
  carrier-natively.

KILL-DCS.6 formal derived schema
  A proposal declares derived stack, obstruction theory, or orientation
  labels on arbitrary control data. Kill it unless the actual oriented proper
  derived square is built.

KILL-DCS.7 virtual intersection as End(S^2/Z)
  A proposal promotes virtual intersection theory directly to End(S^2/Z).
  Kill it unless it constructs square H2, intersection form,
  correspondences, Frobenius graph, Laurent boundary data, DD.4 weight>=1
  datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 100 = doc 237:
  N1B_DERIVED_CYCLE_STACK__VIRTUAL_DATA_DOWNSTREAM_OF_SQUARE__NO_GO.

What got built: no End object. The value is a sharper derived
representability boundary: virtual data refines intersections on an already
oriented square; it is not construction of the square or its correspondence
calculus.

What remains: construct the global square carrier first; construct degree
maps, diagonal, Frobenius graph, correspondence composition, projection
formula, and positive Rosati; then derived/virtual intersection theory may
be used to refine the cycles.
```
