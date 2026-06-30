# 251 - Anabelian/profinite fundamental-group data does not construct the square

Status: no-go + anabelian / profinite pi1 / finite-cover carrier boundary,
2026-06-20. One-hundred-fourteenth cycle of the doc-137 construction arc.
Docs 233 and 241 killed compatible Galois systems and condensed/pro-etale
analytic enrichment as direct square carriers. This document tests the
category-level repair:

```text
profinite pi1 / finite-cover Galois category / inertia and decomposition
  + Frobenius conjugacy, outer action, sections, anabelian reconstruction
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_anabelian_fundamental_group_no_go` (AFG1-AFG9 ALL PASS) --
anabelian/pi1 profiles do not determine finite-field count anchors;
finite-cover/pi1 data does not construct NS degree slots; finite-cover
shadows lose correspondence endpoint data; anabelian reconstruction does not
select diagonal/graph triples; pi1 duality/section data does not impose
Frobenius/Rosati compatibility; cover pull-push functoriality is not a
constructed projection formula; finite pi1/profinite windows admit trace
ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_galois_compatible_system_no_go`,
`prime_int_n1b_condensed_liquid_analytic_carrier_no_go`, and
`prime_int_n1b_tambara_mackey_norm_no_go`.

## 1. Purpose

Anabelian and profinite fundamental-group methods are genuinely strong. A
category of finite covers, inertia and decomposition groups, Frobenius
classes, outer actions, and section data can reconstruct object-level
geometry in settings where the hypotheses are available.

The R1 target is stricter. We do not only need an object reconstructed from
covering data. We need the zeta-native compactified square, `rep_NS`, an
indecomposable diagonal, two carrier-native degree maps, proper
correspondence composition by fiber product, the Frobenius/Hecke graph, the
projection formula, and positive Rosati pairing.

This document rejects only the shortcut:

```text
profinite pi1 / finite-cover Galois category / anabelian reconstruction
constructs the square correspondence carrier required by End(S^2/Z).
```

It does not reject fundamental groups, finite covers, section methods,
decomposition/inertia data, or anabelian reconstruction downstream of a
future global square whose degree maps, correspondences, projection formula,
Frobenius graph, and Rosati are already carrier-native.

## 2. Lemma

```text
Lemma 251.1 (Anabelian/profinite-cover data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy anabelian/fundamental-group profile:

    profinite pi1 = present
    finite-cover Galois category = present
    inertia groups = present
    decomposition groups = present
    Frobenius conjugacy classes = present
    outer action = present
    section/anabelian reconstruction = present
    open-subgroup lattice = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract anabelian/pi1 profile does not determine the
finite-field count anchor.

Nor do finite-cover, open-subgroup, or fundamental-group data construct the
NS degree slots. Keeping the same quotient window and z-action while
changing the formal triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A finite-cover shadow can lose correspondence endpoint data. Two classes can
have the same cover shadow (6,2) while their endpoint coordinate differs by
4.

Anabelian object reconstruction is not selection of square correspondences.
Keeping the same reconstructed-object profile while changing the formal
endpoint from (1,Id,1) to (4,Id,1) changes the tested endpoint intersection
by 3. The reconstructed object profile has not selected the diagonal and
graph triples of `rep_NS`.

Poincare-duality-group or section data does not impose Frobenius/Rosati
compatibility. The off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring cover pullback, corestriction pushforward, and base-change
functoriality does not construct the square projection formula. In the
componentwise realization, the semantic projection defect remains

    27.

Finite pi1/profinite windows remain unsafe: a 5-cycle trace ghost preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal anabelian/pi1 schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently an anabelian / profinite pi1 / finite-cover package constructs
no pi1 carrier, Galois-category carrier, finite-cover carrier, anabelian
carrier, inertia/decomposition carrier, ambient square, `rep_NS`, actual
square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or
End(S^2/Z).
```

Verdict label:

```text
N1B_ANABELIAN_FUNDAMENTAL_GROUP__PI1_COVER_DATA_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_anabelian_fundamental_group_no_go` verifies the nine gates.

AFG1 records profile non-determination. The q=7 and q=5 anchors have the
same anabelian/pi1 profile but different count windows.

AFG2 records the NS-degree-slot failure. The finite quotient window and
z-action are kept fixed, but changing only the formal degree slot changes
`Delta.Gamma` from `7` to `10`.

AFG3 records correspondence-data loss. The finite-cover shadow sees the
cover degree and inertia rank `(6,2)` but forgets an endpoint coordinate
differing by `4`.

AFG4 records object reconstruction versus square correspondence selection.
The reconstructed-object profile is unchanged, but changing the formal
endpoint changes a tested endpoint intersection by `3`.

AFG5 records Rosati non-construction. Poincare-duality-group and section
data do not force Frobenius to be a q-similitude for the required carrier
pairing; the normalized metric defect is `5.916`.

AFG6 records projection-formula failure. Cover pullback, corestriction, and
base-change declarations do not construct the square calculus; the
componentwise semantic defect is still `27`.

AFG7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

AFG8 records control formability. A control companion with the same formal
anabelian/pi1 schema has count window `8,112,1064` and metric defect
`9.950`, with no square, `rep_NS`, degree maps, projection formula, or
Rosati input.

AFG9 records the construction failure: no pi1 carrier, Galois-category
carrier, finite-cover carrier, anabelian carrier, inertia/decomposition
carrier, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-251:
  NEWLY CLOSED THIS CYCLE:
    - profinite pi1 as square carrier, finite-cover Galois category as
      correspondence category, inertia/decomposition data as degree maps,
      anabelian reconstruction as diagonal/graph selection, section data as
      Rosati, cover pull-push as the square projection formula, finite
      quotient windows as ghost exclusion, and formal anabelian schemas as
      DH/Epstein carrier guards (doc 251).

  STILL ADMISSIBLE:
    - fundamental-group, finite-cover, section, and anabelian packages
      downstream of an actual global square carrier;
    - a theorem showing the actual carrier's cover/fundamental-group
      realization preserves exact integral correspondence endpoints, degree
      slots, projection formula, and Rosati;
    - controls killed at carrier formation, not after applying pi1,
      cover-category, inertia/decomposition, or section realizations.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is again carrier-level. Anabelian reconstruction can at best
be a theorem about an already constructed object. It cannot replace the
construction of the compactified square and its `rep_NS` correspondence
calculus.

## 5. Kill Conditions Added To The Ledger

```text
KILL-AFG.1: Do not use profinite pi1 itself as the End(S^2/Z) square
            construction.
KILL-AFG.2: Do not use a finite-cover Galois category as the proper
            correspondence category unless the square correspondences already
            exist.
KILL-AFG.3: Do not use inertia/decomposition/open-subgroup data as
            carrier-native degree maps or endpoint data.
KILL-AFG.4: Do not use anabelian object reconstruction as selection of the
            diagonal and Frobenius graph triples.
KILL-AFG.5: Do not use section data or duality of pi1 as Rosati positivity.
KILL-AFG.6: Do not use cover pullback/corestriction/base-change as the square
            projection formula unless the square carrier has already supplied
            the relevant correspondences.
KILL-AFG.7: Do not treat finite quotient or profinite-window checks as ghost
            exclusion.
KILL-AFG.8: Do not let control objects survive by merely carrying a formal
            anabelian/pi1 schema.
```

The next admissible move remains constructive: build a carrier whose square,
`rep_NS`, degree maps, composition, projection formula, Frobenius graph, and
Rosati exist before any fundamental-group or cover-category reconstruction
is invoked.
