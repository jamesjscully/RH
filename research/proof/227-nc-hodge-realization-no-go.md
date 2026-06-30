# 227 - NC-Hodge realization does not construct the square

Status: no-go + noncommutative-Hodge/periodic-cyclic-realization boundary,
2026-06-20. Ninetieth cycle of the doc-137 construction arc. Doc 226 killed
smooth-proper/Calabi-Yau/Mukai enrichment as positive Rosati construction.
This document tests the next realization repair: apply periodic cyclic
homology, a Hodge-to-de Rham package, or a polarized noncommutative Hodge
realization to the smooth proper category and promote the realized Hodge data
to the square carrier.

```text
smooth-proper / CY / Mukai category
  -> HP / de Rham / NC-Hodge realization
  -> Hodge filtration + positive polarization
  -> square H2 / positive Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_nc_hodge_realization_no_go` (NHR1-NHR6 ALL PASS) -- identical
HP/Hodge realization profiles do not determine finite-field count anchors;
realization data does not construct NS degree slots; positive realized Hodge
metrics do not impose Frobenius/Rosati compatibility; finite windows admit
ghost realization summands; the same realization package is formable on
controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_smooth_proper_cy_mukai_no_go` (CYM1-CYM7 ALL PASS) and
`prime_int_n1b_perfect_morita_envelope_no_go` (PME1-PME6 ALL PASS).

## 1. Purpose

Doc 226 says a smooth-proper/CY/Mukai pairing is not the arithmetic Rosati
square. The next repair is to pass to a realization:

```text
periodic cyclic homology / de Rham realization gives the right vector space;
the Hodge filtration supplies the square H2;
a positive polarization supplies Rosati.
```

This is still not construction of `End(S^2/Z)`. A realization functor is a
shadow of a category. It can be useful only after the square carrier and its
correspondence category are built. By itself it does not construct the NS
triple `(d1,z,d2)`, the degree maps, the projection formula, the Frobenius
graph, or the carrier-native positive Rosati relation.

This document rejects only the shortcut:

```text
NC-Hodge / HP / de Rham realization data of a smooth proper category
constructs the square correspondence carrier required by End(S^2/Z).
```

It does not reject a future square carrier whose already-constructed proper
correspondence category admits a realization compatible with its
carrier-native degree maps, pairings, and Rosati involution.

## 2. Lemma

```text
Lemma 227.1 (Realization profiles are not carrier construction).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy HP/Hodge profile:

    HP_even dimension = 2,
    HP_odd dimension  = 0,
    Hodge split       = (1,1),
    positive metric   = present.

The profiles are identical, but the first count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore a realization profile does not determine the finite-field count
anchor.

Nor does the realization construct the NS degree slots. Keeping the same
realized vector space and the same z-action F while changing the formal
triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A positive realized metric is not the Rosati relation. For the off-circle
integral q-similitude control

    F = [[0,-2],[1,3]], q=2,

the realized vector space still has a positive metric, but

    ||(F/sqrt(q))^T H (F/sqrt(q)) - H|| = 5.916.

Compatibility with Frobenius is the missing carrier-native polarization
relation, not a consequence of realization.

Finite windows remain unsafe: a 5-cycle ghost summand preserves traces in
powers 1,2,3,4, contributes an extra HP/Hodge summand, and changes count 5 by
5. The same realization package is formable on arbitrary control companion
data with no Euler product, Satake parameters, rep_NS, square carrier, or
positive Rosati.

Consequently NC-Hodge/HP/de Rham realization constructs no rep_NS, actual
square, proper correspondence category, fiber-product composition,
carrier-native realization theorem, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_NC_HODGE_REALIZATION__REALIZATION_SHADOW_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_nc_hodge_realization_no_go` verifies the six gates.

NHR1 records realization-profile non-determination. The q=7 and q=5 anchors
have the same HP/Hodge profile but different count windows.

NHR2 records the NS-degree-slot failure. With the same realization and
z-action, changing only the formal degree slot changes `Delta.Gamma` from `7`
to `10`.

NHR3 records positivity/compatibility separation. A positive realized metric
exists on the off-circle q-similitude control, but the normalized Frobenius
metric-compatibility defect is `5.916`. The missing datum is the
carrier-native Rosati/polarization compatibility.

NHR4 records finite-window ghost survival. A 5-cycle ghost preserves the first
four traces, adds an HP-even summand of dimension `5`, and changes count 5 by
`5`.

NHR5 records control formability. A control companion with realization profile
`(2,0,(1,1),positive)`, count window `8,112,1064`, and metric defect `9.950`
supports the same realization package without Euler/Satake/`rep_NS`/square/
Rosati input.

NHR6 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native Hodge
realization theorem, carrier-native degree maps, carrier-native pairing,
projection formula, Frobenius graph, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-227:
  NEWLY CLOSED THIS CYCLE:
    - periodic cyclic/HP/de Rham/NC-Hodge realization profiles as square H2,
      Hodge filtration as NS degree construction, positive realized metric as
      Rosati, finite realization windows as carrier determination, and
      realization functors as DH/Epstein carrier guards (doc 227).

  STILL ADMISSIBLE:
    - a carrier-native square whose proper correspondence category is already
      constructed and then admits compatible HP/de Rham/Hodge realizations;
    - a realization theorem that is downstream of rep_NS, degree maps,
      projection formula, Frobenius graph, and Rosati rather than a substitute
      for them;
    - a theorem excluding ghost realization summands from the actual carrier;
    - controls killed at carrier formation, not after taking realizations.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the realization repair: HP/Hodge data is a
shadow of the square, not the construction of the square.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-NHR.1 HP/Hodge realization as square construction
  A proposal takes periodic cyclic, de Rham, or NC-Hodge realization data as
  the square. Kill it unless the square correspondence category was already
  constructed carrier-natively.

KILL-NHR.2 Hodge profile as count carrier
  A proposal uses Hodge numbers or realization dimensions to recover counts.
  Kill it: different finite-field anchors can have the same profile.

KILL-NHR.3 realized vector space as NS triple
  A proposal uses the realized vector space and z-action as rep_NS. Kill it
  unless the degree slots, projection formula, and off-diagonal intersections
  are constructed.

KILL-NHR.4 positive realized metric as Rosati
  A proposal reads positive Rosati from a positive metric on the realization.
  Kill it unless Frobenius/Rosati compatibility is constructed by the square.

KILL-NHR.5 finite realization window
  A proposal verifies finitely many traces or realized classes. Kill it unless
  ghost realization summands are excluded carrier-natively.

KILL-NHR.6 control survival
  A proposal's realization package can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
