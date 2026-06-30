# 254 - Shtuka/Hecke-stack data does not construct the square

Status: no-go + shtuka / Hecke-stack / excursion-operator carrier boundary,
2026-06-20. One-hundred-seventeenth cycle of the doc-137 construction arc.
Docs 229, 232, 252, and 253 killed six-functor trace formalisms,
automorphic trace-formula packets, generic span/profunctor correspondence
bicategories, and topos/hyperdescent packages as direct square carriers.
This document tests the stronger geometric repair:

```text
moduli of shtukas / Hecke stacks / Frobenius legs / excursion operators
  + Heegner-Drinfeld cycle intersections or central Rankin-Selberg heights
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_shtuka_hecke_stack_no_go` (SHT1-SHT9 ALL PASS) --
shtuka/Hecke-stack profiles do not determine finite-field count anchors;
Hecke modification data does not construct NS degree slots; Hecke-stack
shadows lose correspondence endpoint data; Frobenius-leg data does not
select diagonal/graph triples; central-value self-intersection data is not
Rosati/count construction; excursion/projection declarations are not a
constructed projection formula; finite shtuka/Hecke windows admit trace
ghosts; the same formal schema is formable on controls; and no square
package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`a5_function_field`, `hecke_correspondence`,
`prime_int_n1b_automorphic_trace_formula_packet_no_go`, and
`prime_int_n1b_topos_hyperdescent_shape_no_go`.

## 1. Purpose

This is the serious geometric repair after the previous categorical and
spectral shortcuts. Shtukas and Hecke stacks are not empty formalism: over
function fields they carry Frobenius legs, Hecke modifications, geometric
Langlands input, and cycle-intersection theorems. They are exactly the sort
of geometry one might hope would supply the missing square correspondence
carrier.

The R1 target is still stricter. `End(S^2/Z)` requires a compactified zeta
square and `rep_NS`: two carrier-native degree maps, an indecomposable
diagonal, proper correspondence composition by fiber product, a
Frobenius/Hecke graph, the projection formula, and positive Rosati pairing.
Function-field shtuka geometry can be an analogy or a downstream theorem
once the zeta-side carrier exists. It does not by itself construct the
over-`Z` square or the integral `rep_NS` functor.

This document rejects only the shortcut:

```text
the shtuka / Hecke-stack / excursion-operator package constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category admits a shtuka-like or Hecke-stack interpretation after the
carrier, degree maps, projection formula, Frobenius graph, and Rosati have
already been constructed.

## 2. Lemma

```text
Lemma 254.1 (Shtuka/Hecke-stack data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy shtuka/Hecke-stack profile:

    legs                         = 2
    Hecke stack                  = present
    Frobenius leg                = present
    paws                         = present
    excursion algebra            = present
    geometric Satake input       = present
    Heegner-Drinfeld cycle       = present
    central Rankin-Selberg height = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract shtuka/Hecke-stack profile does not determine the
finite-field count anchor.

Nor does Hecke modification or leg data construct the NS degree slots.
Keeping the same legs and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

A Hecke-stack shadow can lose correspondence endpoint data. Two classes can
have the same Hecke shadow (2,3,4) while their endpoint coordinate differs
by 6.

Frobenius legs and Hecke modifications do not select the diagonal and
Frobenius graph triples. Keeping the same leg profile while changing the
formal endpoint from (1,Id,1) to (4,Id,1) changes the tested endpoint
intersection by 3.

Central-value or Heegner-Drinfeld self-intersection data is not the Weil
square count mechanism and does not impose Frobenius/Rosati compatibility.
The witness separates a central-height scalar 1 from the square count
Delta.Gamma = 7, and the off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring excursion operators, geometric Satake input, and projection
formulas does not construct the square projection formula. In the
componentwise realization, the semantic projection defect remains

    27.

Finite shtuka/Hecke/excursion windows remain unsafe: a 5-cycle trace ghost
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal shtuka/Hecke schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a shtuka / Hecke-stack / excursion-operator package constructs
no shtuka moduli carrier over `Z`, Hecke stack carrier, Bun-stack carrier,
Frobenius-leg carrier, excursion-algebra carrier, Heegner-Drinfeld cycle
carrier, ambient square, `rep_NS`, actual square, proper correspondence
category, fiber-product composition, carrier-native degree maps,
carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_SHTUKA_HECKE_STACK__FUNCTION_FIELD_GEOMETRY_NOT_ZETA_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_shtuka_hecke_stack_no_go` verifies the nine gates.

SHT1 records profile non-determination. The q=7 and q=5 anchors have the
same shtuka/Hecke-stack profile but different count windows.

SHT2 records the NS-degree-slot failure. Hecke legs and z-action are kept
fixed, but changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

SHT3 records correspondence-data loss. The Hecke-stack shadow sees leg
number, modification degree, and excursion rank `(2,3,4)` but forgets an
endpoint coordinate differing by `6`.

SHT4 records Frobenius-leg data versus square correspondence selection. The
leg profile is unchanged, but changing the formal endpoint changes a tested
endpoint intersection by `3`.

SHT5 records central-value versus square-count/Rosati separation.
Heegner-Drinfeld cycle and central Rankin-Selberg height declarations give a
central scalar in the witness; they do not give the square count
`Delta.Gamma = 7`, and they do not force Frobenius to be a q-similitude for
the required carrier pairing. The normalized metric defect is `5.916`.

SHT6 records projection-formula failure. Excursion-operator, geometric
Satake, and projection declarations do not construct the square calculus;
the componentwise semantic defect is still `27`.

SHT7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

SHT8 records control formability. A control companion with the same formal
shtuka/Hecke schema has count window `8,112,1064` and metric defect `9.950`,
with no square, `rep_NS`, degree maps, projection formula, or Rosati input.

SHT9 records the construction failure: no zeta-side shtuka moduli carrier,
Hecke stack carrier, Bun-stack carrier, Frobenius-leg carrier,
excursion-algebra carrier, Heegner-Drinfeld cycle carrier, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

The adjacent witnesses explain why this matters. `a5_function_field`
separates Weil's `C x C` Hodge-index mechanism from genuine
function-field shtuka special-value theorems. `hecke_correspondence`
shows that explicit-formula Hecke-like non-productness is real but that
the self-pairing can collapse to a congruence of the archimedean form.
Docs 232 and 253 then close the spectral-packet and object-topos wrappers.

## 4. Impact on R1

```text
R1 after docs 138-254:
  NEWLY CLOSED THIS CYCLE:
    - importing moduli of shtukas as the zeta square carrier, Hecke stacks
      as rep_NS construction, Frobenius legs as diagonal/graph selection,
      excursion operators as square correspondence calculus,
      Heegner-Drinfeld self-intersections or central Rankin-Selberg heights
      as the Weil square count/Rosati mechanism, finite shtuka windows as
      ghost exclusion, and formal shtuka/Hecke schemas as DH/Epstein carrier
      guards (doc 254).

  STILL ADMISSIBLE:
    - a zeta-native global square whose proper correspondence category is
      constructed before any shtuka or Hecke-stack language is invoked;
    - a theorem showing that the actual carrier admits a shtuka-like or
      Hecke-stack realization preserving exact integral correspondence
      endpoints, degree slots, projection formula, Frobenius graph, and
      Rosati;
    - controls killed at carrier formation, not after applying a
      function-field analogy or central-value formula.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is not lack of a function-field template. The obstruction is
that the zeta square and its arithmetic correspondence data have not been
constructed. Shtuka and Hecke-stack geometry can guide or host a future
construction only after the over-`Z` carrier supplies the objects, proper
maps, degree maps, graph, projection formula, and Rosati.

## 5. Kill Conditions Added To The Ledger

```text
KILL-SHT.1: Do not import moduli of shtukas or Hecke stacks as the
            End(S^2/Z) square construction.
KILL-SHT.2: Do not use Hecke modifications, paws, or leg data as
            carrier-native NS degree slots.
KILL-SHT.3: Do not use a Hecke-stack or Bun-stack shadow as exact
            correspondence endpoint data.
KILL-SHT.4: Do not use Frobenius legs as selection of the diagonal and
            Frobenius graph triples unless the square carrier already
            constructs those triples.
KILL-SHT.5: Do not identify Heegner-Drinfeld or central Rankin-Selberg
            self-intersections with the Weil square count/Rosati mechanism.
KILL-SHT.6: Do not use excursion operators, geometric Satake input, or
            formal projection declarations as the square projection formula
            unless the square correspondence calculus is constructed.
KILL-SHT.7: Do not treat finite shtuka, Hecke, or excursion windows as ghost
            exclusion.
KILL-SHT.8: Do not let control objects survive by merely carrying a formal
            shtuka/Hecke schema.
```

The next admissible move remains constructive: build the actual global
square carrier first, then ask whether shtuka/Hecke-stack language is the
right description of its correspondence theory.
