# 236 - Chow and Hilbert cycle moduli do not construct the square

Status: no-go + Chow/Hilbert cycle-moduli carrier boundary, 2026-06-20.
Ninety-ninth cycle of the doc-137 construction arc. Doc 235 killed the
CM/Shimura-Taniyama carrier shortcut. This document tests the next
representability repair: instead of fixed classes, formal correspondences,
or CM endomorphism fields, take a Hilbert scheme or Chow variety of cycles
and promote its universal family to the missing correspondence carrier.

```text
Hilbert scheme / Chow variety of cycles
  -> universal family of correspondences
  -> rep_NS and degree maps
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_chow_hilbert_cycle_moduli_no_go` (CHM1-CHM7 ALL PASS) --
abstract Chow/Hilbert profiles do not determine finite-field count anchors;
cycle moduli do not construct NS degree slots; universal families do not
construct the ambient intersection form; cycle-moduli membership does not
select diagonal/graph triples; finite Chow/Hilbert windows admit ghost cycle
components; the same formal cycle-moduli schema is formable on controls; and
no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_tate_cycle_fixed_subspace_no_go` (TCF1-TCF7 ALL PASS),
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS),
and `prime_int_n1b_formal_ns_envelope_no_go` (FNE1-FNE6 ALL PASS).

## 1. Purpose

Docs 218-222 killed formal NS envelopes, formal composition, projection
quotients, and presented correspondence carriers. Doc 234 killed fixed
Tate/Hodge classes as `rep_NS`. A natural repair is to use a more geometric
representability tool:

```text
do not merely present the correspondence category;
use the Hilbert scheme or Chow variety of cycles and its universal family.
```

This is still not construction of `End(S^2/Z)`. A Hilbert scheme or Chow
variety parameterizes subschemes or cycles after an ambient projective
carrier exists. It does not by itself construct the over-`Z` square, the two
fiber degree maps, the diagonal, Frobenius graph, ambient intersection
pairing, fiber-product correspondence composition, projection formula, or
positive Rosati relation.

This document rejects only the shortcut:

```text
the Hilbert/Chow cycle moduli space itself constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category first constructs an ambient square and then uses Hilbert or Chow
representability to organize its cycles.

## 2. Lemma

```text
Lemma 236.1 (Cycle moduli are downstream of the square).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Chow/Hilbert profile:

    cycle component count      = 1,
    Hilbert polynomial profile = (1,1),
    projective moduli          = present,
    universal family           = present,
    cycle class map            = declared.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract cycle-moduli profile does not determine the
finite-field count anchor.

Nor do cycle moduli construct the NS degree slots. Keeping the same z-cycle
label and profile while changing the formal triple from (7,F,1) to (10,F,1)
changes

    Delta . Gamma  from 7 to 10.

A universal family also requires the ambient intersection form. The same
cycle vector and Hilbert profile can have self-intersection

    0 or 2

depending on the ambient pairing. The universal family has not constructed
that pairing.

Cycle-moduli membership does not select the diagonal or Frobenius graph
correspondence triples. In the q=7 anchor, the identity graph and Frobenius
graph have the same coarse graph-cycle profile, but

    Delta . Id     = 0,
    Delta . Gamma  = 7.

Finite Chow/Hilbert windows remain unsafe: a 5-cycle ghost component
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal cycle-moduli schema is formable on arbitrary control
companion data with no actual Hilbert scheme, Chow variety, ambient square,
`rep_NS`, or positive Rosati.

Consequently a Chow/Hilbert cycle-moduli package constructs no Hilbert
scheme over the zeta square, Chow variety, universal family, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, DH/Epstein death, DD.4 weight>=1
datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_CHOW_HILBERT_CYCLE_MODULI__PARAMETER_SPACE_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_chow_hilbert_cycle_moduli_no_go` verifies the seven gates.

CHM1 records profile non-determination. The q=7 and q=5 anchors have the
same abstract Chow/Hilbert profile but different count windows.

CHM2 records the NS-degree-slot failure. With the same z-cycle label and
profile, changing only the formal degree slot changes `Delta.Gamma` from `7`
to `10`.

CHM3 records the ambient-pairing dependence. The same cycle vector/profile
has self-intersection `0` in one ambient pairing and `2` in another. A
universal family does not construct the ambient intersection form.

CHM4 records cycle-moduli membership versus correspondence-triple
separation. The identity and Frobenius graph have the same coarse graph-cycle
profile, but `Delta.Id=0` while `Delta.Gamma=7`.

CHM5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

CHM6 records control formability. A control companion with the same formal
cycle-moduli schema has count window `8,112,1064` and metric defect `9.950`,
with no actual Hilbert scheme, Chow variety, square, `rep_NS`, or Rosati
input.

CHM7 records the construction failure: no Hilbert scheme, Chow variety,
universal family, ambient square, `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-236:
  NEWLY CLOSED THIS CYCLE:
    - Hilbert scheme as global square carrier, Chow variety as rep_NS
      construction, universal family as ambient square construction,
      Hilbert polynomial or Chow profile as count anchor, cycle-moduli point
      as diagonal/graph selector, finite Chow/Hilbert windows as ghost
      exclusion, and formal cycle-moduli schemas as DH/Epstein carrier guards
      (doc 236).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose projective/proper
      correspondence category is constructed before Hilbert or Chow moduli
      are invoked;
    - Hilbert/Chow representability downstream of an actual square with
      degree maps, correspondences, projection formula, Frobenius graph, and
      Rosati;
    - a theorem excluding ghost cycle components from the actual carrier;
    - controls killed at carrier formation, not after parameterizing cycles.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the cycle-moduli shortcut: Hilbert and
Chow spaces are useful only after the ambient square and its correspondence
calculus have already been constructed.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-CHM.1 Hilbert/Chow moduli as square construction
  A proposal supplies a Hilbert scheme or Chow variety and calls it the
  square. Kill it unless the global over-Z square carrier was already
  constructed.

KILL-CHM.2 cycle profile as count anchor
  A proposal reads the zeta count anchor from a Hilbert polynomial, Chow
  profile, or component count. Kill it: the same profile can support
  different count windows.

KILL-CHM.3 universal family as ambient pairing
  A proposal uses the universal family as the intersection form. Kill it
  unless the ambient square pairing is constructed carrier-natively.

KILL-CHM.4 moduli point as diagonal or graph
  A proposal reads the diagonal or Frobenius graph from cycle-moduli
  membership. Kill it unless those correspondence triples and their degree
  slots are constructed.

KILL-CHM.5 finite cycle-moduli window
  A proposal verifies finitely many Chow/Hilbert, Frobenius, or trace
  identities. Kill it unless ghost cycle components are excluded
  carrier-natively.

KILL-CHM.6 formal cycle-moduli schema
  A proposal declares Hilbert/Chow labels on arbitrary control companion
  data. Kill it unless an actual projective/proper square and cycle moduli
  over it are built.

KILL-CHM.7 cycle moduli as End(S^2/Z)
  A proposal promotes cycle moduli directly to End(S^2/Z). Kill it unless it
  constructs square H2, intersection form, correspondences, Frobenius graph,
  Laurent boundary data, DD.4 weight>=1 datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 99 = doc 236:
  N1B_CHOW_HILBERT_CYCLE_MODULI__PARAMETER_SPACE_NOT_SQUARE__NO_GO.

What got built: no End object. The value is a sharper representability
boundary: cycle moduli are downstream organizers of cycles on a square, not
the construction of the square or its correspondence calculus.

What remains: construct the global square carrier first; construct degree
maps, diagonal, Frobenius graph, correspondence composition, projection
formula, and positive Rosati; then Hilbert/Chow moduli may be used to
organize the cycles.
```
