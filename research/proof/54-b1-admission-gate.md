# 54 - B1 admission gate

Status: construction gate, 2026-06-11. This is the next construction
artifact after B0. It is not a B1 construction. It states the minimum
data a proposed B1 must expose before it is worth building witnesses,
asking for positivity, or discussing RH.
Doc 71 turns this gate into an operational proposal ledger.

## 1. Why B1 Needs A Gate

Doc 49 landed B0:

```text
B0 = (L0, b0, R0/T0, tr0, comb_p, Count0).
```

B0 is honest because it is small. It reproduces the Tate/RR shadow and
the one-place p^Z comb address, then refuses to claim a unit, Frobenius,
odd slot, index form, full class family, or comparison theorem.

The next object cannot be "B0 with two primes". A two-place product
alone still risks being a tensor product of calibrated shadows. B1 is
admissible only if it names the first structural map where the
circumference `log p` remains visible before trace evaluation and where
the LS4-style coupling is carrier-selective.

## 2. Candidate Shape

An admissible B1 proposal has at least:

```text
B1 = (L1, b1, R1/T1, U1?, tr1, Fr1?, I1?, Count1?)
```

with:

```text
L1
  A liquid/gaseous or metric analytic category, not bare sheaves on a
  topological circle.

b1
  A conservative embedding of the banked prime-power combs and graph
  depth data into L1.

R1/T1
  Internal real line and circles T_p = R/(log p)Z, where log p is
  retained as metric, analytic-ring, equivariant, density, or kernel
  data before any trace is applied.

U1?
  A candidate-native Fourier unit only if LS3-type self-duality has
  already pinned it. Otherwise this field must remain open.

tr1
  A trace or kernel trace that couples the banked comb to the continuum
  on the same form, not an archimedean block added beside the bank.

Fr1?, I1?, Count1?
  Optional only at B1. If present, they must already obey the doc-45
  supplier, positivity, and comparison gates.
```

The first B1 pass may leave `U1`, `Fr1`, `I1`, and `Count1` partial.
It may not leave `L1`, `b1`, `R1/T1`, and the first LS4-like coupling
undefined.

## 3. The Four Admission Questions

Every proposed B1 must answer these questions in order.

```text
Q1. Where is log p retained?
  Name the first object carrying log p as structure:
  metric coefficient, liquid analytic ring, equivariant group datum,
  density, explicit kernel, or something stronger.

Q2. Where is LS3 consumed?
  State whether the Fourier unit is derived, still conjectural, or not
  used. If a Gaussian, Haar density, scale, or normalization is chosen
  externally, reject the proposal as inserted-unit calibration.

Q3. Where is LS4 formed?
  Give the actual map or trace expression that couples b1(comb_p) and
  the continuum R object on the same index/Gram/count form.

Q4. Where does Epstein die?
  Replace the prime-power carrier by the Epstein represented-norm
  monoid for Q=x^2+5y^2. The theta/Poisson/count layer must survive,
  but the LS4 coupling through b1 must become undefinable at
  carrier/effectivity.
```

The Q-gates are B1-local names; doc 60 wraps them into G60. Missing Q1
is the doc-51 scale-blind failure. Missing Q2 is the doc-43 unit-slot
failure and the doc-55 inserted-unit gate. Missing Q3 is only address
data. Missing Q4 is the doc-53 carrier-blind Poisson/Epstein failure.

## 4. Required Death Profile For Epstein

The B1 Epstein test is not a sign test.

For `Q=x^2+5y^2`, the represented-norm monoid contains:

```text
1, 4, 6, 9, 36
```

and omits:

```text
2, 3.
```

Inside that represented-norm monoid, `4`, `6`, and `9` are irreducible
but:

```text
36 = 4*9 = 6*6.
```

Therefore a theta/Poisson/count formalism can still see a lattice-like
shadow, but there is no free rank-one valuation tower or unique
prime-power address. A B1 coupling passes only if this is where it
breaks.

The required verdict is:

```text
theta/Poisson/count layer: defined
banked valuation coupling: undefined
failure point: carrier/effectivity
```

Any B1 proposal that computes a parallel LS4 coupling for this Epstein
monoid is carrier-blind, regardless of later positivity or numerical
behavior.

The proof-level version of this finite obstruction is doc 64.

## 5. Reject / Hold / Advance

Use this triage before any witness is built.

```text
REJECT: bare address
  L1 is Shv(R/(log p)Z; C), an LCA lattice formalism, or a continuous
  localizing invariant of the bare circle. Doc 51 applies.

REJECT: inserted unit
  U1 is a chosen Gaussian, chosen Haar density, chosen normalization,
  chosen scale, or Hermite repair. This is calibration, not LS3.

REJECT: uncoupled continuum
  The archimedean block is computed beside the bank rather than paired
  against the banked comb on the same form.

REJECT: carrier-blind
  The same trace/coupling computes for Epstein or DH controls.

HOLD: scale retained, coupling not yet written
  The category genuinely retains log p, but no LS4-like map has been
  stated. This is external-scoping material, not a construction.

HOLD: coupling written, unit not derived
  The LS4 map is formable and carrier-selective, but LS3 remains open.
  This can advance A/B but not C/D/E.

ADVANCE: B1 admitted
  The proposal names retained log p, a conservative bank embedding,
  an LS4-like coupling on the same form, and the Epstein death point.
  It may then proceed to unit extraction, index lift, odd-slot audit,
  and P3 comparison.
```

## 6. Minimal Evidence Packet

A B1 proposal should be recorded with this exact ledger.

```text
candidate name:
category L1:
first log p carrier:
bank embedding b1:
LS3 status: derived | conjectural | absent | inserted
LS4 map:
same-form coupling evidence:
Epstein result: undefined at carrier | computes | not tested
DH result: no carrier | computes | not tested
promotion fields present:
doc-45 clauses advanced:
doc-45 clauses still open:
verdict: REJECT | HOLD | ADVANCE
```

The ledger is intentionally harsher than B0. B0 was allowed to be a
scale-free calibration. B1 is the first place where calibrated shadows
must either become candidate-native structure or be rejected.

## 7. Current Status

No B1 candidate is admitted in the record.

The live construction work is therefore not a numerical run. It is to
find or define one of the following first maps:

```text
1. a liquid/gaseous analytic-ring module category for T_p whose trace
   is not equivalent to the bare Shv(S^1) localizing trace;
2. an equivariant or parametrized trace retaining the group object
   T_logp before trace evaluation;
3. an explicit kernel/correspondence trace coupling (log p)Z and R
   through the banked comb;
4. a stronger structure that proves why the Epstein represented-norm
   monoid has no object where the prime-power valuation tower does.
```

Until one of these maps is named, B1 remains a gate, not a construction.
