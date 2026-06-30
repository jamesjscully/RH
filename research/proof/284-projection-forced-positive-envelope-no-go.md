# 284 - Projection forced positive envelope is not the square carrier

Status: no-go + projection-forced-positive-envelope deletion, 2026-06-21.
One-hundred-forty-seventh cycle of the doc-137 construction arc. Doc 283
killed the positive `U+End` matrix package because componentwise composition
still lacks the projection formula. This document tests the next repair:

```text
impose the projection formula on the positive U+End envelope by quotient
relations or local retuning.
```

Witness, lead-reran this cycle:
`prime_int_n1b_projection_forced_positive_envelope_no_go` (PFE1-PFE9 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_positive_rosati_end_envelope_no_go`,
`prime_int_n1b_projection_formula_quotient_no_go`,
`prime_int_n1b_formal_adjoint_projection_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 283 left a precise failure:

```text
<A o B, C> != <B, A^dag o C>
```

for the pasted pairing and componentwise matrix composition. The projection
formula is exactly the missing theorem a real proper-correspondence carrier
must supply. The shortcut is to impose it as a relation on the already
positive formal envelope.

This document rejects only that shortcut. It does not reject a future
compactified square where the projection formula is proved from actual
proper correspondences and fiber products.

## 2. Lemma

```text
Lemma 284.1 (projection forcing is not proper correspondence).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the positive `U+End` package
before projection forcing has:

    Delta.Gamma_1 = 7,
    Gamma_1.Gamma_2 = 76,
    Gamma_1 o Gamma_2 = Gamma_3,
    F^T E F = qE,
    primitive Hodge/Rosati sign < 0.

Forcing the projection formula on the componentwise law changes the genuine
finite-field trace/count data. The sampled projection defect is 27. The
forced relation changes

    Tr(F^2) = -13

to

    Tr(F^2) = 2q = 14,

and changes

    #C(F_{q^2}) = 63

to

    36.

Killing projection defects by scalar quotient also fails over positive
finite-field anchors: the defects 27 and 8 have gcd 1, so the universal
integer quotient collapses. Local retuning can force one projection equation
but changes the graph degree from 7 to -20. Finite projection samples can be
cherry-picked: for the q=2, Tr(F)=0 positive anchor, one sample has defect 0
while another has defect 8.

The projection repair still does not couple DD.4 to End/Rosati. The endpoint
DD.4 split works with labels `positive_projection`, `retuned_graph`, and
`control`. Positive controls also admit the same projection forcing/retuning
without Euler product, Satake data, proper correspondences, carrier boundary,
or control death.

Consequently projection-forced positive-envelope data constructs no actual
`Qbar`, no carrier-produced integral `rep_NS`, no proper correspondence
category, no fiber-product composition, no projection formula from geometry,
no carrier boundary with control death, and no DD.4 carrier-native
weight>=1 datum.
```

Verdict label:

```text
N1B_PROJECTION_FORCED_POSITIVE_ENVELOPE__RELATION_REPAIR_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_projection_forced_positive_envelope_no_go` verifies nine
gates.

PFE1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

PFE2 checks that the positive finite-field package is intact before the
repair: diagonal count, off-diagonal pairing, graph law, q-similitude, and
negative primitive sign all hold.

PFE3 checks the count distortion: projection forcing changes `Tr(F^2)` from
`-13` to `14`, and the second point count from `63` to `36`.

PFE4 checks universal scalar quotient collapse: positive-anchor defects 27
and 8 have gcd 1.

PFE5 checks local retuning: forcing one projection equation changes graph
degree `d1` from `7` to `-20`.

PFE6 checks finite-sample overfitting: one projection sample can pass while
another fails on the same positive anchor.

PFE7 checks DD.4 independence: endpoint DD.4 splitting is unchanged by
projection forcing or retuning.

PFE8 checks positive control formability: a positive q-similitude control has
the same projection defect/retuning story without carrier data or death.

PFE9 applies the carrier-first contract: relation repair is not `Qbar`,
`Corr^prop`, fiber products, geometric projection formula, carrier boundary,
or control death.

## 4. Impact on R1

```text
R1 after docs 138-284:
  NEWLY CLOSED THIS CYCLE:
    - forcing the projection formula on the positive U+End envelope by
      quotient relations;
    - scalar quotient of projection defects after positive Rosati has been
      imposed;
    - local degree retuning to make projection equations true;
    - finite projection samples as a substitute for the projection theorem.

  POSITIVE INFORMATION RETAINED:
    - the projection formula is the correct missing theorem;
    - a surviving route must get it from actual proper correspondences and
      fiber products;
    - positive Rosati, graph composition, endpoint integrality, DD.4
      boundary, and projection must be one carrier theorem.

  STILL ADMISSIBLE:
    - a compactified zeta square whose projection formula is proved from
      `Corr^prop(Qbar)` rather than imposed on formal triples;
    - a carrier-native proof preserving finite-field trace/count anchors and
      graph degree maps;
    - a proof that no such square can exist, with a named mechanism and
      witness.

  STILL OPEN:
    - construct Qbar and prove projection formula, Rosati, graph
      composition, DD.4 boundary killing, and control death from one
      carrier.
```

## 5. Kill conditions

```text
KILL-PFE.1 projection formula by quotient
  Kill any proposal that imposes the projection formula on formal U+End
  unless the identity is proved from proper correspondences and preserves the
  finite-field anchors.

KILL-PFE.2 scalar defect quotient
  Kill quotienting projection defects by scalars: positive anchors already
  force gcd 1.

KILL-PFE.3 local graph retuning
  Kill repairs that change degree slots to make projection equations true.

KILL-PFE.4 finite projection samples
  Kill finite projection checks unless the full formula follows from
  constructed fiber-product composition.

KILL-PFE.5 DD.4 still independent
  Kill projection repairs where DD.4 splitting remains an endpoint-side
  operation unrelated to graph/Rosati/projection data.

KILL-PFE.6 positive controls survive
  Kill projection repairs formable on positive controls unless controls die
  at carrier formation.
```
