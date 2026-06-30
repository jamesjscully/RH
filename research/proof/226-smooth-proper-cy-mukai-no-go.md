# 226 - Smooth proper Mukai pairing does not construct Rosati

Status: no-go + smooth-proper/Calabi-Yau-Mukai boundary, 2026-06-20.
Eighty-ninth cycle of the doc-137 construction arc. Doc 225 killed
perfect-module/dg Morita envelopes as square construction. This document
tests the next categorical repair: add smooth/proper/Calabi-Yau structure, a
Serre duality, or a Mukai/Euler/Frobenius trace pairing to the perfect-module
category and promote that categorical duality to the positive Rosati square
carrier.

```text
Perf(A) / dg Morita envelope
  -> smooth proper / Calabi-Yau / Mukai pairing
  -> categorical duality and trace pairing
  -> positive Rosati square carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_smooth_proper_cy_mukai_no_go` (CYM1-CYM7 ALL PASS) -- the
finite-field `q=7, Tr(F)=1` quadratic Frobenius algebra has a nondegenerate
categorical trace pairing, but it is indefinite; CY/Frobenius trace
normalization is extra data; smooth-proper/CY profiles do not determine count
anchors; Mukai/Frobenius pairings do not construct NS degree slots; finite
windows admit ghost CY summands; the same enrichment is formable on controls;
and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_perfect_morita_envelope_no_go` (PME1-PME6 ALL PASS) and
`prime_int_n1b_numerical_gns_quotient_no_go` (NGQ1-NGQ6 ALL PASS).

## 1. Purpose

Doc 225 says `Perf(A)`, dg Morita envelopes, and additive invariants do not
construct the square carrier. The next repair is to add duality:

```text
make Perf(A) smooth proper / Calabi-Yau;
use the Mukai or Euler pairing as the square intersection form;
read Rosati positivity from categorical duality.
```

This is still not construction of `End(S^2/Z)`. Smooth properness and a
nondegenerate trace pairing are categorical finiteness/duality data. They are
not the arithmetic NS representability functor, not the degree maps
`(d1,d2)`, not the projection formula, and not the positive Rosati pairing on
the Frobenius graph. The trace functional also has a normalization choice; a
Calabi-Yau volume form must be constructed by the carrier, not selected after
the fact.

This document rejects only the shortcut:

```text
smooth proper / Calabi-Yau / Mukai-paired enrichment of a presented or
perfect-module carrier constructs the positive Rosati square carrier required
by End(S^2/Z).
```

It does not reject a future square carrier whose actual proper correspondence
category is smooth/proper and whose Calabi-Yau or Mukai pairing is derived
from carrier-native intersection theory.

## 2. Lemma

```text
Lemma 226.1 (Categorical duality is not Rosati square construction).

For the finite-field q=7, Tr(F)=1 anchor, take the quadratic Frobenius
algebra

    A = Q[x] / (x^2 - x + 7).

The Frobenius trace pairing on basis 1,x has Gram

    [[2, 1],
     [1,-13]],

with determinant -27 and inertia (1,1,0). Thus the categorical trace pairing
is nondegenerate, but it is not the positive Rosati square pairing.

The trace normalization is also not carrier-native. Rescaling the trace by 3
or by -1 preserves nondegeneracy and the same underlying category while
changing the Gram. A proposed volume normalization is therefore extra data
unless the square carrier constructs it.

Coarse smooth-proper/Calabi-Yau profiles do not determine the finite-field
count anchor. The q=7, Tr(F)=1 and q=5, Tr(F)=2 genus-one anchors both have
profile

    dimension 2, nondegenerate trace, Serre=Id,

but their first count windows differ:

    7, 63, 364, 2331
    4, 32, 148, 640.

Nor does the categorical pairing on Q[F] construct the NS degree slots.
Keeping the same z-component and the same trace pairing while changing the
formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Finite windows remain unsafe: a 5-cycle ghost summand preserves traces in
powers 1,2,3,4, contributes an extra smooth-proper/CY summand, and changes
the fifth count by 5. The same smooth-proper/CY trace package is formable on
control companion data with no Euler product, Satake parameters, rep_NS,
square carrier, or positive Rosati.

Consequently smooth-proper/Calabi-Yau/Mukai enrichment constructs no rep_NS,
actual square, proper correspondence category, fiber-product composition,
carrier-native CY structure, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_SMOOTH_PROPER_CY_MUKAI__DUALITY_PAIRING_NOT_ROSATI_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_smooth_proper_cy_mukai_no_go` verifies the seven gates.

CYM1 records the finite-field anchor. The categorical trace pairing has Gram
`[[2,1],[1,-13]]`, determinant `-27`, and inertia `(1,1,0)`, while the count
window is `7,63,364,2331`. Nondegenerate categorical trace is not positive
Rosati.

CYM2 records normalization ambiguity. Scaling the trace changes the Gram
while preserving nondegeneracy and leaving the count window unchanged. A
normalization choice is not carrier-native unless the square constructs it.

CYM3 records profile non-determination. The q=7 and q=5 genus-one anchors
have the same smooth-proper/CY profile but different count windows.

CYM4 records the NS-degree-slot failure. The same `Q[F]` and categorical
pairing allow formal triples with different `Delta.Gamma` values. The missing
data are the carrier-native degrees `(d1,d2)` and the proper intersection
theory.

CYM5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces, adds a rank-5 CY summand, and changes count 5 by `5`.

CYM6 records control formability. A control companion with Gram
`[[2,3],[3,-11]]`, determinant `-31`, and count window `8,112,1064` supports
the same smooth-proper/CY trace package without Euler/Satake/`rep_NS`/square/
Rosati input.

CYM7 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native CY
structure, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, control death, or DD.4 weight>=1
datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-226:
  NEWLY CLOSED THIS CYCLE:
    - smooth properness, Calabi-Yau volume forms, Serre duality, Mukai/Euler
      pairings, and Frobenius trace pairings on Perf(A) or a dg Morita
      envelope as positive Rosati square construction (doc 226).

  STILL ADMISSIBLE:
    - a carrier-native proper correspondence category that is smooth/proper
      because the square carrier has already constructed properness;
    - a Calabi-Yau/Mukai pairing derived from the square intersection theory,
      with normalization, degree maps, projection formula, and Rosati all
      carrier-native;
    - a theorem excluding ghost CY summands from the actual carrier;
    - controls killed at carrier formation, not after adding duality data.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the categorical-duality repair: a
nondegenerate smooth-proper/CY/Mukai pairing is not the arithmetic Rosati
square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-CYM.1 smooth properness as square construction
  A proposal makes Perf(A) smooth/proper and calls this the square. Kill it
  unless A is already the carrier-native proper correspondence algebra.

KILL-CYM.2 Calabi-Yau volume as Rosati
  A proposal chooses a CY/Frobenius trace and reads Rosati positivity from it.
  Kill it unless the trace normalization and positive pairing are constructed
  by the square carrier.

KILL-CYM.3 Mukai/Euler pairing as NS intersection form
  A proposal uses a categorical Mukai or Euler pairing as the NS form. Kill it
  unless it also constructs the degree slots, projection formula, Frobenius
  graph, and off-diagonal intersections.

KILL-CYM.4 smooth-proper profile as count carrier
  A proposal uses smooth-proper/CY profile data to recover counts. Kill it:
  different finite-field anchors can have the same coarse profile.

KILL-CYM.5 finite CY window
  A proposal verifies finitely many traces or pairings after CY enrichment.
  Kill it unless ghost CY summands are excluded carrier-natively.

KILL-CYM.6 control survival
  A proposal's smooth-proper/CY/Mukai package can be formed on arbitrary
  control companion data. Kill it unless controls die at carrier formation.
```
