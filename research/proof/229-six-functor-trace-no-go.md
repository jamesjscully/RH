# 229 - Six-functor trace formalism does not construct the square

Status: no-go + six-functor/Lefschetz-Verdier-trace boundary, 2026-06-20.
Ninety-second cycle of the doc-137 construction arc. Doc 228 killed abstract
Weil-cohomology/standard-conjectures packages as square construction. This
document tests the next formalism repair: use cohomological correspondences,
Verdier duality, proper pushforward, trace maps, and the Lefschetz-Verdier
fixed-point formula to supply the missing square correspondence calculus.

```text
Weil/standard package is downstream
  -> six-functor formalism + cohomological correspondences
  -> Verdier trace / Lefschetz fixed-point formula
  -> square correspondence carrier / Frobenius graph
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_six_functor_trace_no_go` (SFT1-SFT7 ALL PASS) -- identical
six-functor trace profiles do not determine finite-field count anchors; trace
formalism does not construct NS degree slots; scalar Lefschetz traces are not
carrier-native graphs; proper trace existence does not pin the degree
character; finite trace-formalism windows admit ghost correspondences; the
same package is formable on controls; and no square package over `Z` is
built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_weil_standard_package_no_go` (WSC1-WSC7 ALL PASS) and
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS).

## 1. Purpose

Doc 228 says standard axioms are downstream data. The stronger repair is to
say that the standard package is not merely appended; it is supplied by a
full six-functor trace formalism:

```text
construct cohomological correspondences,
take proper push-pull operations and Verdier duality,
then use the Lefschetz-Verdier trace formula for fixed points.
```

That still is not construction of `End(S^2/Z)`. Six-functor formalisms are
operations on a site, stack, scheme, or category with the relevant proper
maps already present. They can express traces and projection identities after
the carrier exists. They do not by themselves construct the zeta square, its
proper maps, `rep_NS`, fiber degree maps, Frobenius graph, projection
formula, positive Rosati relation, or control death.

This document rejects only the shortcut:

```text
an abstract six-functor / Lefschetz-Verdier trace formalism constructs the
square correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose actual proper
correspondence category carries a six-functor formalism and whose
Lefschetz-Verdier trace theorem is proved from that carrier.

## 2. Lemma

```text
Lemma 229.1 (Trace formalism is not carrier construction).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy six-functor profile:

    H1 dimension                  = 2,
    cohomological correspondences = present,
    f*, f_*, f_!, f!              = present,
    Verdier duality               = present,
    trace map                     = present,
    projection formula            = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore an abstract trace-formalism profile does not determine the
finite-field count anchor.

Nor does it construct the NS degree slots. Keeping the same cohomological
action and changing the formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A scalar Lefschetz trace is not a graph correspondence. A trace-zero
perturbation of the q=7 anchor preserves the first Lefschetz trace and the
first count:

    Tr(F) = 1,  #C(F_q) = 7,

but changes the second count from 63 to 61 and changes the determinant from
7 to 6. Thus scalar trace data is not a carrier-native Frobenius graph.

Proper trace or ambidexterity existence also does not pin the degree
character: trace degrees 7 and 10 both fit the same abstract six-functor
operation profile.

Finite trace-formalism windows remain unsafe. A 5-cycle ghost correspondence
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same abstract six-functor trace package is formable on arbitrary control
companion data with no Euler product, Satake parameters, rep_NS, square
carrier, or positive Rosati.

Consequently a six-functor/Lefschetz-Verdier trace package constructs no
site or stack, rep_NS, actual square, proper maps, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph,
carrier-native Lefschetz fixed-point theorem, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_SIX_FUNCTOR_TRACE__TRACE_FORMALISM_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_six_functor_trace_no_go` verifies the seven gates.

SFT1 records profile non-determination. The q=7 and q=5 anchors have the
same abstract six-functor trace profile but different count windows.

SFT2 records the NS-degree-slot failure. With the same cohomological action,
changing only the formal degree slot changes `Delta.Gamma` from `7` to `10`.

SFT3 records scalar trace insufficiency. A trace-zero perturbation preserves
`Tr1=1` and `count1=7`, while changing `count2` from `63` to `61` and the
determinant from `7` to `6`.

SFT4 records trace-degree ambiguity. Proper trace existence is compatible
with degree scalar `7` or `10`; the degree character is still unconstructed.

SFT5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

SFT6 records control formability. A control companion with the same abstract
six-functor trace profile has count window `8,112,1064` and metric defect
`9.950`, with no Euler/Satake/`rep_NS`/square/Rosati input.

SFT7 records the construction failure: no site or stack, `rep_NS`, actual
square, proper maps, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, carrier-native Lefschetz fixed-point theorem,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-229:
  NEWLY CLOSED THIS CYCLE:
    - abstract six-functor formalism as square carrier, cohomological
      correspondences as rep_NS construction, scalar Lefschetz traces as
      Frobenius graphs, proper trace existence as degree-character
      construction, finite trace-formalism windows as carrier
      determination, and trace-formalism axioms as DH/Epstein carrier guards
      (doc 229).

  STILL ADMISSIBLE:
    - a carrier-native square whose proper maps and proper correspondence
      category are constructed before six-functor operations are invoked;
    - a Lefschetz-Verdier trace theorem downstream of rep_NS, degree maps,
      projection formula, Frobenius graph, and Rosati;
    - a theorem excluding ghost cohomological correspondences from the actual
      carrier;
    - controls killed at carrier formation, not after taking traces.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the six-functor/Lefschetz-Verdier trace
repair: trace operations are not construction of the square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SFT.1 six-functor formalism as square construction
  A proposal supplies f*, f_*, f_!, f!, Verdier duality, and trace maps and
  calls that the square. Kill it unless the square carrier and proper maps
  were already constructed carrier-natively.

KILL-SFT.2 cohomological correspondences as rep_NS
  A proposal treats cohomological correspondences or trace maps as the NS
  triple. Kill it unless the degree slots, off-diagonal intersections, and
  projection formula are constructed.

KILL-SFT.3 scalar Lefschetz trace as Frobenius graph
  A proposal reads the Frobenius graph from scalar Lefschetz traces. Kill it
  unless the carrier constructs the graph operator and its composition law.

KILL-SFT.4 proper trace as degree construction
  A proposal uses proper trace or ambidexterity existence to pin the degree
  character. Kill it unless the proper map and degree maps are carrier-native.

KILL-SFT.5 finite trace-formalism window
  A proposal verifies finitely many traces or trace identities. Kill it
  unless ghost cohomological correspondences are excluded carrier-natively.

KILL-SFT.6 control survival
  A proposal's trace formalism can be formed on arbitrary control companion
  data. Kill it unless controls die at carrier formation.
```
