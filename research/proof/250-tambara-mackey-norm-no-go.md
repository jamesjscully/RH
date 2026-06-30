# 250 - Tambara/Mackey norm-transfer calculus does not construct the square

Status: no-go + Tambara / Mackey / norm-transfer equivariant carrier
boundary, 2026-06-20. One-hundred-thirteenth cycle of the doc-137
construction arc. Docs 199, 246, 248, and 249 killed nearby real
cyclotomic, algebraic K/TC, epicyclic Frobenius-lift, and
Witt/Lambda/delta absolute-geometry shortcuts. This document tests the
adjacent equivariant repair:

```text
Tambara functors / Mackey functors / Burnside category
  + restriction, transfer, norms, double-coset formula, genuine fixed points
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_tambara_mackey_norm_no_go` (TMN1-TMN8 ALL PASS) --
Tambara/Mackey/norm profiles do not determine finite-field count anchors;
transfer/restriction/norm data does not construct NS degree slots;
Burnside/Mackey shadows lose correspondence endpoint data; norm positivity
does not impose Frobenius/Rosati compatibility; Mackey/norm functoriality is
not a constructed projection formula; finite Tambara/Mackey windows admit
trace ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_real_cyclotomic_negation_no_go`,
`prime_int_n1b_algebraic_k_cyclotomic_trace_no_go`, and
`prime_int_n1b_epicyclic_frobenius_lift_no_go`.

## 1. Purpose

Tambara and Mackey functors encode real equivariant multiplicative
structure: restrictions, transfers, norms, Burnside spans, double-coset
formulas, and genuine fixed-point operations. That is strong formal
machinery, and it is close enough to the existing cyclotomic and
real-cyclotomic sources to be a plausible repair after docs 246, 248, and
249.

The missing step is still the same R1 carrier step. The norm-transfer
package does not by itself construct the zeta-native square over `Z`,
`rep_NS`, two carrier-native degree maps, a proper correspondence category,
fiber-product composition, the Frobenius graph, a projection formula, or a
positive Rosati involution.

This document rejects only the shortcut:

```text
Tambara / Mackey / Burnside / norm-transfer calculus constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject Tambara functors, Mackey functors, Burnside categories,
norms, transfers, or equivariant stable homotopy downstream of a future
global square whose degree maps, correspondences, projection formula,
Frobenius graph, and Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 250.1 (Tambara/Mackey norm-transfer data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy Tambara/Mackey/norm profile:

    Tambara functor = present
    Mackey functor = present
    restriction maps = present
    transfer maps = present
    norm maps = present
    Burnside category = present
    double-coset formula = present
    genuine fixed points = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract norm-transfer profile does not determine the
finite-field count anchor.

Nor do transfer, restriction, norm, or double-coset data construct the NS
degree slots. Keeping the same formal Mackey laws and z-action while
changing the formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A Burnside/Mackey shadow can lose correspondence endpoint data. Two classes
can have the same Burnside shadow (3,2) while their endpoint coordinate
differs by 4.

Norm positivity and Wirthmuller-style duality do not impose
Frobenius/Rosati compatibility. The off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring restrictions, transfers, and norms does not construct the square
projection formula. In the componentwise realization, the semantic
projection defect remains

    27.

Finite Tambara/Mackey windows remain unsafe: a 5-cycle trace ghost preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal Tambara/Mackey/norm schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a Tambara / Mackey / Burnside / norm-transfer package
constructs no Tambara carrier, Mackey carrier, Burnside carrier,
norm-transfer carrier, equivariant stable homotopy carrier, ambient square,
`rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_TAMBARA_MACKEY_NORM__NORM_TRANSFER_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_tambara_mackey_norm_no_go` verifies the eight gates.

TMN1 records profile non-determination. The q=7 and q=5 anchors have the
same Tambara/Mackey/norm profile but different count windows.

TMN2 records the NS-degree-slot failure. The toy double-coset/Mackey laws
are present, but with the same z-action, changing only the formal degree
slot changes `Delta.Gamma` from `7` to `10`.

TMN3 records correspondence-data loss. The Burnside shadow sees the orbit
degree and rank `(3,2)` but forgets an endpoint coordinate differing by `4`.

TMN4 records Rosati non-construction. Norm positivity and
Wirthmuller-style duality do not force Frobenius to be a q-similitude for
the required carrier pairing; the normalized metric defect is `5.916`.

TMN5 records projection-formula failure. Restriction, transfer, and norm
declarations do not construct the square calculus; the componentwise
semantic defect is still `27`.

TMN6 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

TMN7 records control formability. A control companion with the same formal
Tambara/Mackey/norm schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

TMN8 records the construction failure: no Tambara carrier, Mackey carrier,
Burnside carrier, norm-transfer carrier, equivariant stable homotopy
carrier, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-250:
  NEWLY CLOSED THIS CYCLE:
    - Tambara functors as square carrier, Mackey functors as square
      correspondence calculus, Burnside categories as endpoint/degree data,
      restriction-transfer-norm profiles as finite-field count anchors,
      norm positivity as Rosati positivity, double-coset formulas as the
      square projection formula, finite equivariant windows as ghost
      exclusion, and formal equivariant stable homotopy schemas as
      DH/Epstein carrier guards (doc 250).

  STILL ADMISSIBLE:
    - Tambara/Mackey/norm and equivariant stable homotopy packages
      downstream of an actual global square carrier;
    - a theorem showing the actual carrier's equivariant realization
      preserves exact integral correspondence endpoints, degree slots,
      projection formula, and Rosati;
    - controls killed at carrier formation, not after applying Burnside,
      Mackey, Tambara, norm, or fixed-point realizations.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is carrier-level, not vocabulary-level. A successful use of
Tambara/Mackey/norm technology must first produce the square and then show
the norm-transfer formalism preserves its integral correspondence data. It
cannot replace the square construction itself.

## 5. Kill Conditions Added To The Ledger

```text
KILL-TMN.1: Do not use Tambara or Mackey functor structure itself as the
            End(S^2/Z) square construction.
KILL-TMN.2: Do not use a restriction-transfer-norm profile as the
            finite-field count anchor.
KILL-TMN.3: Do not use Burnside/Mackey classes as carrier-native degree maps
            or endpoint data.
KILL-TMN.4: Do not use norm positivity or Wirthmuller-style duality as
            Rosati positivity.
KILL-TMN.5: Do not use equivariant fixed-point shadows as integral
            correspondence construction.
KILL-TMN.6: Do not use the Mackey double-coset formula as the square
            projection formula unless the square correspondences already
            exist.
KILL-TMN.7: Do not treat finite equivariant/Tambara checks as ghost
            exclusion.
KILL-TMN.8: Do not let control objects survive by merely carrying a formal
            Tambara/Mackey/norm schema.
```

The next admissible move is unchanged but sharper: build a carrier whose
objects and correspondences already have the square, `rep_NS`, degree maps,
composition, projection formula, Frobenius graph, and Rosati before any
equivariant norm-transfer realization is invoked.
