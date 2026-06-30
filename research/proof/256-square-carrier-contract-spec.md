# 256 - Square-carrier contract for End(S^2/Z)

Status: construction-spec contract anchor, 2026-06-20. One-hundred-nineteenth
cycle of the doc-137 construction arc. This is not a no-go theorem, not an
RH proof, and not added to the no-go bank.

Docs 211-255 fixed the finite-field square anchor and killed the usual
language-level substitutes: formal NS envelopes, presented correspondence
categories, motivic and cohomological realizations, trace formulas, shtukas,
topoi, periods, and special-value packages. The remaining admissible task is
therefore narrow:

```text
construct the zeta-native square carrier whose finite-field model is
rep_NS : Corr(C) -> (integral lattice, intersection form).
```

Witness, lead-reran this cycle:
`prime_int_n1b_square_carrier_contract` (SCC1-SCC8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_ns_square_anchor`, `ns_diagonal_representability`, and
`ns_hodge_index_duality`.

## 1. Purpose

The project now has enough negative information that another carrier-name
survey is mostly waste. The advantage is process discipline: every failed
route has left an executable guard, and the finite-field anchor tells us
exactly what the missing object must do before any period, trace, topos,
shtuka, or automorphic language is allowed to count.

This document freezes that target as a contract. A future proposal is
admissible only if it fills the contract slots. It is rejected immediately
if it supplies a formal profile, scalar identity, realization functor,
period formula, or relation presentation without the carrier-native data.

## 2. Contract

A construction of `End(S^2/Z)` must provide all of the following before it
can be promoted beyond a vocabulary package.

```text
SCC.1  An actual compactified zeta square carrier over Z.

SCC.2  An integral representability functor

           rep_NS : Corr(square) -> (Z-lattice, intersection form)

       whose finite-field model sends a correspondence to a triple
       (d1, z, d2) and uses

           (d1,z,d2) . (e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).

SCC.3  Two carrier-native degree maps d1 and d2. They cannot be inserted
       after the fact and cannot be read from a scalar period shadow.

SCC.4  An indecomposable diagonal Delta, finite-field model (1, Id, 1),
       whose End component is nonzero and is not a product/fiber class.

SCC.5  A Frobenius or Hecke graph Gamma_n, finite-field model
       (q^n, F^n, 1), with Delta . Gamma_n equal to the trace/count term
       that replaces #C(F_{q^n}) in the explicit formula.

SCC.6  A proper correspondence category, or carrier-native proper derived
       enhancement, whose composition is fiber-product composition rather
       than symbolic multiplication on triples.

SCC.7  A projection formula proved from the carrier geometry and pairing.
       Declaring Beck-Chevalley, a trace identity, or an RTF comparison is
       not enough.

SCC.8  A canonical duality/Rosati pairing

           P_NS(z,w) = Tr(z w^dag)

       realized as evaluation of an involutive duality D with D^2 = id,
       not as a chosen metric.

SCC.9  Positive Rosati / primitive weight-2 Hodge-index sign on the
       carrier. The sign must come from the square carrier and must detect
       off-circle data.

SCC.10 DH/Epstein/control death at carrier formation, not after applying a
       period, trace, quotient, positivity, or realization functor.

SCC.11 DD.4 weight>=1 data, including the Laurent boundary and torsor
       splitter demanded by the R1 entry problem.
```

The finite-field anchor fills the visible square slots. The zeta-side
carrier does not yet exist in the record.

## 3. Lemma

```text
Lemma 256.1 (the square-carrier acceptance contract).

For the finite-field anchors q=2,5,7,11,13 with genus 1 Frobenius matrices,
the represented diagonal Delta=(1,Id,1) and Frobenius graphs
Gamma_n=(q^n,F^n,1) satisfy

    Delta . Gamma_n = #C(F_{q^n})

for n=1,2,3.

The two degree slots are necessary. At q=7, Tr(F)=1,

    Delta . (7,F,1)  = 7,
    Delta . (10,F,1) = 10,
    Delta . (7,F,4)  = 10,

with the same z-action. Therefore scalar z-action, period data, or trace
profile alone cannot replace the carrier-native degree maps.

The diagonal is indecomposable: its End(H^1)-component is Id != 0, while
left and right fiber classes have zero End component.

On the weight-2 End(H^1) lattice, the duality D is involutive, the canonical
evaluation pairing equals the Rosati Gram Tr(z w^dag), and
Tr(F F^dag)=2gq for the tested genus 1 and genus 2 Weil anchors.

The primitive Hodge/Rosati sign is negative on-circle and flips under an
off-circle plant. Thus the square contract is exactly the positive Rosati
target, not a metric profile.

Formal packages such as RTF/period/theta data, shtuka/Hecke profiles,
topos/hyperdescent shape data, and automorphic trace packets satisfy none of
the carrier slots by themselves. DH and arbitrary controls die before
carrier formation.

Consequently doc 256 supplies an executable contract for future proposals,
not a construction of End(S^2/Z).
```

## 4. Proof

`prime_int_n1b_square_carrier_contract` verifies the eight gates.

SCC1 reruns the finite-field `rep_NS` count anchor:
`Delta . Gamma_n = #C(F_{q^n})` for five genus 1 curves and n=1,2,3.

SCC2 tests the two degree maps. Changing only the first or second degree
slot while keeping the same z-action changes the intersection count. This
is the minimal executable reason period shadows and trace profiles cannot
substitute for `rep_NS`.

SCC3 checks indecomposability. `End(Delta)=Id`, while left and right fiber
classes have zero End component.

SCC4 checks the canonical weight-2 duality: `D^2=id`,
`P_NS = Tr(z w^dag)`, and `Tr(F F^dag)=2gq`.

SCC5 checks the primitive Hodge/Rosati sign. The on-circle finite-field
anchors have the expected negative primitive sign; the planted off-circle
control flips it.

SCC6 records that named formal packages fail the contract slotwise.

SCC7 records DH/control exclusion. DH has no Euler product, Satake data,
`F x F` product, End-Frobenius, or indecomposable NS diagonal component.
Controls can assert projection or positivity words but still lack the
square carrier, `rep_NS`, degree maps, and graph.

SCC8 records the status: the finite-field square anchor fills the visible
model slots, while over `Z` all carrier slots, control death, and DD.4 data
remain unconstructed.

## 5. Impact on R1

```text
R1 after docs 138-256:
  NEWLY FIXED THIS CYCLE:
    - the square-carrier acceptance contract. Future proposals must fill
      the SCC slots before any downstream language counts as evidence.

  STILL ADMISSIBLE:
    - a zeta-native global square with integral rep_NS, two carrier-native
      degree maps, indecomposable diagonal, Frobenius/Hecke graph, proper
      correspondence composition, carrier-proved projection formula,
      canonical D^2=id duality/Rosati pairing, positive primitive
      weight-2 Hodge/Rosati sign, control death, and DD.4 weight>=1 data;
    - downstream period, trace-formula, shtuka, motivic, or automorphic
      theorems after the actual carrier has supplied the contract slots.

  STILL OPEN:
    - construct that carrier over Z.
```

## 6. Acceptance and kill conditions

```text
ACCEPT-SCC.1  Produce the compactified zeta square carrier over Z.
ACCEPT-SCC.2  Define integral rep_NS with its intersection form.
ACCEPT-SCC.3  Construct both degree maps carrier-natively.
ACCEPT-SCC.4  Construct the indecomposable diagonal.
ACCEPT-SCC.5  Construct the Frobenius/Hecke graph and prove the count trace.
ACCEPT-SCC.6  Prove proper fiber-product composition.
ACCEPT-SCC.7  Prove the projection formula from the carrier.
ACCEPT-SCC.8  Realize Rosati as canonical D^2=id evaluation.
ACCEPT-SCC.9  Prove the primitive positive Rosati/Hodge-index sign.
ACCEPT-SCC.10 Kill DH/Epstein/controls at carrier formation.
ACCEPT-SCC.11 Supply DD.4 weight>=1, Laurent boundary, and torsor splitter.

KILL-SCC.1    Reject any proposal missing the actual square carrier.
KILL-SCC.2    Reject any proposal that supplies scalar traces or periods
              without degree slots and correspondence endpoint data.
KILL-SCC.3    Reject any proposal that declares projection or positivity
              instead of deriving it from the carrier.
KILL-SCC.4    Reject any proposal that works equally on DH or controls until
              a later filter is applied.
KILL-SCC.5    Reject any proposal that treats this contract itself as RH
              progress. It is a spec anchor only.
```
