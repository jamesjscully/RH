# 285 - Fiber-product saturated positive envelope is not the square carrier

Status: no-go + fiber-product-saturated-positive-envelope deletion,
2026-06-21. One-hundred-forty-eighth cycle of the doc-137 construction arc.
Doc 284 killed forcing the projection formula on the positive `U+End`
envelope by quotient relations or local degree retuning. This document tests
the next categorical repair:

```text
freely adjoin formal fiber-product objects and projection cells to the
positive U+End envelope.
```

Witness, lead-reran this cycle:
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go` (FPS1-FPS8
ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_projection_forced_positive_envelope_no_go`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_presented_correspondence_carrier_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The categorical idea is still the right shape:

```text
projection formula should come from fiber-product composition in
Corr^prop(Qbar).
```

The shortcut is to add the categorical words before constructing `Qbar`.
Instead of quotienting numerical defects, this repair creates formal
fiber-product symbols and declares projection cells. That can make the
presentation look like a correspondence category, but unless those cells are
represented by actual proper pullbacks on a compactified square, the
projection theorem has not been constructed.

This document rejects only the shortcut. It does not reject a carrier-first
categorical construction of `Corr^prop(Qbar)`.

## 2. Lemma

```text
Lemma 285.1 (formal fiber products are not the compactified square).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the positive `U+End` data before
fiber-product saturation has:

    Delta.Gamma_1 = 7,
    Gamma_1.Gamma_2 = 76,
    Gamma_1 o Gamma_2 = Gamma_3,
    F^T E F = qE,
    primitive Hodge/Rosati sign < 0.

Freely adjoining a formal fiber-product object

    Gamma_1 x_Delta Gamma_1

and a projection cell can declare the projection defect to be zero, but the
componentwise `U+End` semantics still has defect 27 and the cell is not
represented by a `Qbar` pullback. If the cell is instead represented back in
the NS triple model by local retuning, it repeats the doc 284 failure:

    d1 changes from 7 to -20,

while the genuine second point count remains 63.

Finite fiber-product/projection samples remain cherry-pickable. For the
positive q=2, Tr(F)=0 anchor, one sample has projection defect 0 while the
adjacent sample has defect 8.

Fiber-product saturation still does not couple DD.4 to the square data: the
endpoint DD.4 split works with labels `fiber_product_cell`,
`qbar_boundary_placeholder`, and `control_cell`. Positive controls admit the
same formal fiber-product saturation with projection cells, q-similitude, and
negative primitive sign, while lacking `Qbar`, carrier boundary, and control
death.

Consequently fiber-product-saturated positive-envelope data constructs no
actual compactified square `Qbar`, no structural maps `p1,p2`, no
carrier-produced integral `rep_NS`, no proper correspondence category, no
fiber-product composition from geometry, no projection formula from geometry,
no carrier boundary, no DD.4 carrier-native boundary killing, and no control
death.
```

Verdict label:

```text
N1B_FIBER_PRODUCT_SATURATED_POSITIVE_ENVELOPE__FORMAL_CELLS_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go` verifies
eight gates.

FPS1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

FPS2 checks that the positive finite-field anchor is intact before the
categorical saturation: diagonal count, off-diagonal pairing, graph law,
q-similitude, and negative primitive sign all hold.

FPS3 checks projection by declaration: the formal cell records defect 0, but
the componentwise semantic projection defect remains 27 and there is no
`Qbar` pullback representing the cell.

FPS4 checks represented-cell damage: realizing the cell inside NS triples
forces the same local degree retuning as doc 284, changing graph degree `d1`
from `7` to `-20`.

FPS5 checks finite-sample overfitting: a q=2 positive anchor has one
projection sample with defect 0 and an adjacent sample with defect 8.

FPS6 checks DD.4 independence: the endpoint DD.4 split is unchanged by
fiber-product labels or boundary placeholders.

FPS7 checks positive control formability: a positive q-similitude control can
carry the same formal cells while lacking `Qbar`, boundary, and death.

FPS8 applies the carrier-first contract: formal fiber products and declared
projection cells are not `Qbar`, `p1,p2`, integral pushforward, proper
correspondences, projection from geometry, carrier boundary, DD.4 boundary
killing, or control death.

## 4. Impact on R1

```text
R1 after docs 138-285:
  NEWLY CLOSED THIS CYCLE:
    - free fiber-product saturation of the positive U+End envelope;
    - projection cells as substitute for the projection theorem;
    - formal pullback objects represented only by declaration;
    - local NS-triple retuning of a declared pullback cell;
    - finite fiber-product/projection sample checks as carrier evidence.

  POSITIVE INFORMATION RETAINED:
    - the categorical route is still the right route only after Qbar exists;
    - fiber-product composition and projection formula must be theorems of
      Corr^prop(Qbar);
    - categorical syntax must be downstream of endpoint integrality, degree
      maps, DD.4 boundary, Rosati, graph composition, and control death.

  STILL ADMISSIBLE:
    - a compactified zeta square whose proper correspondence category is
      represented by actual carrier pullbacks;
    - a construction proving projection formula from proper pushforward and
      fiber products while preserving finite-field anchors;
    - a boundary/properness/self-duality mechanism that kills DD.4 and
      controls at formation.

  STILL OPEN:
    - construct Qbar, p1,p2, dQ, Corr^prop(Qbar), carrier-native rep_NS,
      projection formula, Rosati, DD.4 boundary killing, and control death
      as one object.
```

## 5. Kill conditions

```text
KILL-FPS.1 formal fiber-product cell
  Kill any proposal that adjoins pullback/fiber-product objects without
  representing them as proper fiber products on Qbar.

KILL-FPS.2 projection by cell
  Kill projection formulas declared by a 2-cell unless the identity is proved
  from proper pushforward and carrier-native intersection.

KILL-FPS.3 represented-cell retuning
  Kill repairs where realizing the formal cell in rep_NS changes graph
  degree, trace, count, or endpoint data.

KILL-FPS.4 finite pullback window
  Kill finite fiber-product/projection sample checks unless the full
  correspondence category is constructed.

KILL-FPS.5 DD.4 placeholder boundary
  Kill boundary placeholders where the DD.4 split remains independent of
  End/Rosati/projection data.

KILL-FPS.6 positive controls survive
  Kill categorical envelopes formable on positive controls unless the
  controls fail to instantiate Qbar and its structural maps at formation.
```
