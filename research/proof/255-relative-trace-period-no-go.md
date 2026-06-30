# 255 - Relative trace formula and period data do not construct the square

Status: no-go + relative trace formula / period / theta carrier boundary,
2026-06-20. One-hundred-eighteenth cycle of the doc-137 construction arc.
Docs 232 and 254 killed automorphic trace-formula packets and
shtuka/Hecke-stack packages as direct square carriers. This document tests
the remaining period-geometric repair:

```text
relative trace formula / theta lift / toric period / orbital integrals
  + Waldspurger, Gross-Zagier, height or central-value identities
  -> rep_NS, degree maps, projection formula, Frobenius graph, Rosati
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_relative_trace_period_no_go` (RTP1-RTP9 ALL PASS) --
RTF/period profiles do not determine finite-field count anchors; period
data does not construct NS degree slots; period/orbital shadows lose
correspondence endpoint data; theta/period data does not select
diagonal/graph triples; central period/height data is not Rosati/count
construction; RTF comparison declarations are not a constructed projection
formula; finite RTF/period windows admit trace ghosts; the same formal
schema is formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_automorphic_trace_formula_packet_no_go`,
`prime_int_n1b_shtuka_hecke_stack_no_go`, `a5_function_field`, and
`theta_twisted_pairing`.

## 1. Purpose

Period identities are the strongest surviving scalar repair after generic
automorphic packets. Relative trace formulas compare geometric orbital
integrals with spectral periods; Waldspurger and Gross-Zagier type theorems
turn periods or heights into central `L`-values; theta lifts can move data
between representation-theoretic carriers. This is real structure, not a
mere slogan.

The R1 target is still stricter. `End(S^2/Z)` requires a compactified zeta
square and `rep_NS`: two carrier-native degree maps, an indecomposable
diagonal, proper correspondence composition by fiber product, a
Frobenius/Hecke graph, the projection formula, and positive Rosati pairing.
Period formulas can be theorems about cycles after the carrier exists, but
a period identity or central value is not the square correspondence carrier.

This document rejects only the shortcut:

```text
the relative trace formula / period / theta package constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose proper correspondence
category has period formulas or relative trace formulas as downstream
theorems.

## 2. Lemma

```text
Lemma 255.1 (RTF/period data is not the square carrier).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy RTF/period profile:

    rank                    = 2
    relative trace formula  = present
    orbital integrals       = present
    theta lift              = present
    toric period            = present
    Waldspurger formula     = present
    Gross-Zagier height     = present
    comparison theorem      = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract RTF/period profile does not determine the
finite-field count anchor.

Nor does period or orbital-integral data construct the NS degree slots.
Keeping the same period profile and z-action while changing the formal
triple from (7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Period and orbital-integral shadows can lose correspondence endpoint data.
Two classes can have the same period shadow (2,4,1) while their endpoint
coordinate differs by 5.

Theta lifts and period correspondences do not select the diagonal and
Frobenius graph triples. Keeping the same theta/period profile while
changing the formal endpoint from (1,Id,1) to (4,Id,1) changes the tested
endpoint intersection by 3.

Central-value period squares and height formulas are not the Weil square
count mechanism and do not impose Frobenius/Rosati compatibility. The
witness separates a central scalar 1 from the square count
Delta.Gamma = 7, and the off-circle control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Declaring an RTF comparison, transfer, and projection formula does not
construct the square projection formula. In the componentwise realization,
the semantic projection defect remains

    27.

Finite RTF/period windows remain unsafe: a 5-cycle trace ghost preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

The same formal RTF/period schema is formable on arbitrary control
companion data with no zeta square carrier, `rep_NS`, degree maps,
projection formula, or positive Rosati.

Consequently a relative trace formula / period / theta package constructs
no RTF carrier, period-stack carrier, theta-lift carrier, toric-period
carrier, orbital-integral carrier, height-pairing carrier, ambient square,
`rep_NS`, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, DH/Epstein death, DD.4
weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_RELATIVE_TRACE_PERIOD__CENTRAL_VALUE_NOT_ZETA_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_relative_trace_period_no_go` verifies the nine gates.

RTP1 records profile non-determination. The q=7 and q=5 anchors have the
same RTF/period profile but different count windows.

RTP2 records the NS-degree-slot failure. The period profile and z-action
are kept fixed, but changing only the formal degree slot changes
`Delta.Gamma` from `7` to `10`.

RTP3 records correspondence-data loss. The period/orbital shadow sees rank,
orbit dimension, and period rank `(2,4,1)` but forgets an endpoint
coordinate differing by `5`.

RTP4 records theta/period data versus square correspondence selection. The
theta/period profile is unchanged, but changing the formal endpoint changes
a tested endpoint intersection by `3`.

RTP5 records central-value versus square-count/Rosati separation.
Waldspurger-period and Gross-Zagier-height declarations give a central
scalar in the witness; they do not give the square count `Delta.Gamma = 7`,
and they do not force Frobenius to be a q-similitude for the required
carrier pairing. The normalized metric defect is `5.916`.

RTP6 records projection-formula failure. RTF comparison, transfer, and
projection declarations do not construct the square calculus; the
componentwise semantic defect is still `27`.

RTP7 records finite-window trace ghosts. A 5-cycle ghost preserves the first
four traces and changes count 5 by `5`.

RTP8 records control formability. A control companion with the same formal
RTF/period schema has count window `8,112,1064` and metric defect `9.950`,
with no square, `rep_NS`, degree maps, projection formula, or Rosati input.

RTP9 records the construction failure: no relative trace formula carrier,
period-stack carrier, theta-lift carrier, toric-period carrier,
orbital-integral carrier, height-pairing carrier, ambient square, `rep_NS`,
actual square, proper correspondence category, fiber-product composition,
carrier-native degree maps, carrier-native pairing, projection formula,
Frobenius graph, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

The adjacent witnesses explain the boundary. Doc 232 closes the scalar
automorphic packet. Doc 254 closes the function-field shtuka/Hecke-stack
import. `a5_function_field` separates Weil's `C x C` Hodge-index count
mechanism from central Rankin-Selberg or Gross-Zagier-type special-value
theorems. `theta_twisted_pairing` records why inserting a real theta twist
does not by itself escape the congruence-lock of the archimedean form.

## 4. Impact on R1

```text
R1 after docs 138-255:
  NEWLY CLOSED THIS CYCLE:
    - relative trace formula as square carrier, period stacks as rep_NS,
      theta lifts as diagonal/graph selection, toric periods or orbital
      integrals as endpoint data, Waldspurger/Gross-Zagier central values
      or heights as the Weil square count/Rosati mechanism, finite period
      windows as ghost exclusion, and formal RTF/period schemas as
      DH/Epstein carrier guards (doc 255).

  STILL ADMISSIBLE:
    - a zeta-native global square whose proper correspondence category is
      constructed before any period or RTF language is invoked;
    - a theorem showing that the actual carrier has period formulas or
      relative trace formulas preserving exact integral correspondence
      endpoints, degree slots, projection formula, Frobenius graph, and
      Rosati;
    - controls killed at carrier formation, not after applying a
      central-value or period identity.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper derived enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data,
      square-side properness, and all-prime plus archimedean assembly.
```

The obstruction is not lack of period identities. The obstruction is that
the zeta square and its arithmetic correspondence data have not been
constructed. Period/RTF/theta formulas can only be downstream theorems after
the carrier supplies the objects, proper maps, degree maps, graph,
projection formula, and Rosati.

## 5. Kill Conditions Added To The Ledger

```text
KILL-RTP.1: Do not use a relative trace formula or comparison theorem as
            the End(S^2/Z) square construction.
KILL-RTP.2: Do not use toric periods, orbital integrals, or period stacks
            as carrier-native NS degree slots.
KILL-RTP.3: Do not use period shadows as exact correspondence endpoint
            data.
KILL-RTP.4: Do not use theta lifts or period correspondences as selection
            of the diagonal and Frobenius graph triples unless the square
            carrier already constructs those triples.
KILL-RTP.5: Do not identify Waldspurger, Gross-Zagier, or central
            Rankin-Selberg formulas with the Weil square count/Rosati
            mechanism.
KILL-RTP.6: Do not use RTF transfer, orbital comparison, or projection
            declarations as the square projection formula unless the square
            correspondence calculus is constructed.
KILL-RTP.7: Do not treat finite period, RTF, theta, or orbital-integral
            windows as ghost exclusion.
KILL-RTP.8: Do not let control objects survive by merely carrying a formal
            RTF/period schema.
```

The next admissible move remains constructive: build the actual global
square carrier first, then ask which period or relative trace formula
theorems it satisfies.
