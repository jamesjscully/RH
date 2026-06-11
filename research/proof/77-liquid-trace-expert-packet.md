# 77 - Liquid trace expert packet

Status: sendable external packet, 2026-06-11. This is the focused
packet for the doc-76 liquid trace theorem target. It should be sent
instead of the broader doc-50 packets when the recipient is likely to
know liquid/gaseous analytic geometry, trace-of-kernels formalisms, or
categorical trace theory.

## 1. Minimal Context

We are trying to decide whether the following B1-level trace package
can exist:

```text
K_B1 = Tr_L(b1(comb_C) acting on a trace-class object over R_L/T_C).
```

The purpose is not to prove RH. The purpose is narrower: decide
whether there is a category/trace package where `log p` is retained
before trace evaluation and where the trace is carrier-selective for
prime-power valuation towers.

The target package is:

```text
(L1, R_L, T_C, b1, Tr_L)
```

with:

```text
T_C = R_L / (log alpha)Z
```

for the prime-power carrier `C=A_p`, plus a trace/coupling that sees
the carrier-depth fields:

```text
(A, alpha, v, depth, ell, mu_C).
```

## 2. Core Question

Please answer one of the following.

```text
ADVANCE:
  Is there a named liquid/gaseous/analytic-ring or trace-of-kernels
  setting where T_C retains log alpha before trace evaluation, T_C ->
  pt is traceable, and Tr_L pairs b1(comb_C) with the continuum on one
  same-form object?

KILL:
  Is there a theorem showing that every such trace either factors
  through the bare circle S^1, lacks the needed real trace package,
  exists only as a side archimedean block, or computes equally for
  Epstein/DH controls?

SHARPEN:
  If neither is known, what is the minimal theorem or test object that
  would decide the question?
```

For convenience, the core question can be split into five direct
questions.

```text
Q1 scale retention
  Is there a named category where T_p = R_L/(log p)Z retains log p
  before trace evaluation, rather than reducing to bare Shv(S^1)?
  If the trace factors through a bare-circle functor, state the
  factor-through theorem and hypotheses. If it does not, name the
  pre-trace invariant where log p is detected by the trace domain or
  trace value and survives the deletion test.

Q2 traceability
  In that category, name the exact dualizability, properness,
  nuclearity, or trace-class theorem for T_p -> pt, its hypotheses,
  its codomain, and whether the scale/carrier enrichment survives into
  the trace.

Q3 same-form coupling
  Can b1(comb_p) and R_L/T_p map into one mixed object M_C with one
  same-form codomain before trace evaluation? If not, is there a
  theorem forcing the archimedean contribution to split as a coproduct,
  direct sum, external summand, correction, or side block?

Q4 carrier selectivity
  Does the construction require carrier-depth fields such as
  prime-power valuation/depth? If yes, name the first
  carrier-consuming map and the exact failure point for both the
  Epstein replacement Q=x^2+5y^2 and DH controls, while theta/count
  data remain meaningful.

Q4b trace-operation overreach
  Before that carrier-consuming map, are M_C, Tr_L, or the same-form
  codomain formed by broad measure, kernel, operator, determinant,
  cokernel, or trace-class operations that also accept represented-norm
  or coefficient/measure shadows? If yes, doc 105 routes to NO76.4.

Q5 obstruction class
  If this cannot work, is the obstruction scale-collapse, absence of
  real trace kernels, forced side-block decomposition, carrier
  overreach, or inserted Gaussian/Haar/normalization data?

Q5b conservative bank embedding
  Can b1 embed the B0 bank while preserving the p^Z comb, q/log p
  address, RR/count layer, Epstein guard, and no-promotion-field audit?
  If not, identify the first preservation failure.

Q5c internal archimedean objects
  Are R_L, T=R/Z, T_C=R_L/(log alpha)Z, and the archimedean completion
  internal objects of the named category, with a quotient theorem? If
  not, what theorem blocks them?

Q5d freeze/native-unit audit
  List all formulas, constants, densities, kernels, units, loci, and
  comparison maps fixed before first zero-side contact. Identify any
  Gaussian, Haar, scale, or normalization choice inserted externally.
```

For ledger landing, also answer:

```text
Q6 clause target
  Which exact clause do you decide:
  LT76.1 scale retention, LT76.2 internal archimedean objects,
  LT76.3 traceability, LT76.4 bank embedding, LT76.5 same-form
  coupling, LT76.6 carrier selectivity, or LT76.7 zero-free freeze?

Q7 ledger verdict
  Which doc-92 routed ledger verdict follows? Name the pass, hold,
  reject, or out-of-scope verdict and the fields supporting it.

Q8 adjacent unknowns
  Which nearby ledgers remain unknown? A scale answer should not
  silently claim traceability or LS4; a freeze answer should not
  silently claim mathematical success.

Q9 first zero contact
  If any zero-side data, RH-line signs, explicit-formula zero
  expansions, or zero ordinate files enter, where is the first contact
  and is it after the frozen record?
```

## 3. Exact Positive Requirements

A positive answer should specify:

```text
1. the category L1;
2. the internal R_L and T=R/Z objects;
3. the object T_C = R_L/(log alpha)Z and where log alpha lives;
4. the proper-pushforward / dualizability / trace-class theorem;
5. the embedding b1 of the prime-power comb and valuation/depth data;
6. the same-form codomain of Tr_L;
7. the first map that becomes unformable for Epstein/DH controls.
```

Use this answer template:

```text
ADVANCE
  Name category/theorem:
  LT76 clause(s) decided:
  Doc-92 ledger verdict:
  Where log p lives structurally:
  Internal R_L and T=R/Z:
  Trace/proper-pushforward theorem:
  Definition of b1(comb_p):
  Same-form codomain:
  Broad measure/kernel/trace-class input accepted? YES/NO:
  Epstein formability failure point:
  Doc-105 overreach audit:
  Adjacent ledgers still unknown:
  First zero contact:
  External unit/normalization used? YES/NO:
```

The key control is:

```text
Q(x,y) = x^2 + 5y^2.
```

For this Epstein replacement, theta/count data should remain
meaningful, but the carrier coupling should be unformable because the
represented-norm data has no distinguished atom, no unique valuation,
and no tower/depth coordinate.

## 4. Exact Negative Requirements

A useful no-go answer should prove one of:

```text
NO76.1
  Every admissible trace factors through the bare circle and forgets
  log p.

NO76.2
  Liquid/gaseous real circles lack the needed trace-class/proper
  pushforward package.

NO76.3
  Any archimedean term is necessarily a side block, not a same-form
  comb-continuum coupling.

NO76.4
  Any trace broad enough to host the proposed kernel also hosts
  Epstein/DH theta, represented-norm, coefficient, or measure data, so
  it is carrier-blind. Doc 105 records the broad trace-operation audit
  for this case.

NO76.5
  The construction requires choosing Gaussian/Haar/normalization data
  externally before the trace is defined.
```

Use this answer template:

```text
KILL
  No-go theorem or reason:
  LT76/NO76 clause killed:
  Doc-92 ledger verdict:
  Kills which clause:
    scale retention | traceability | same-form coupling |
    carrier selectivity | native unit
  Hypotheses of the no-go:
  Scope:
    liquid | gaseous | bare sheaves | other subcase
  Broader target still open? YES/NO:
```

If the answer is neither positive nor negative, use:

```text
SHARPEN
  Minimal undecided object:
  LT76 clause sharpened:
  Doc-92 ledger hold field:
  Exact missing theorem:
  Smallest test calculation:
  What answer would decide it:
```

## 5. Rejection Rules

The following do not count as progress.

```text
1. A trace of ordinary Shv(S^1) or bare localizing invariants.
2. A category where liquid R exists but no trace package is available
   for T_C -> pt.
3. A Poisson/theta identity that also computes for Epstein.
4. A Gaussian, Haar density, scale, or normalization inserted by hand.
5. A determinant, coker, or regularization of one shadow object.
6. A broad trace-class/kernel/operator package that also accepts
   represented-norm or DH coefficient/measure controls before primitive
   carrier checking.
7. Any answer using zeta zeros, RH-line data, or zero-side signs to
   choose constants or loci.
```

## 6. Short Reading List

```text
research/proof/76-liquid-trace-theorem-target.md
research/proof/50-external-falsification-packets.md sections 1-2
research/work/MM-liquid-slot.md sections 3-4
optional backup:
  research/proof/63-scale-blind-diagram-naturality-lemma.md
  research/proof/64-epstein-carrier-guard-lemma.md
  research/proof/73-s3-kernel-preregistration.md
  research/proof/74-s3-generic-kernel-carrier-blindness.md
  research/proof/75-kb1-ansatz-ledger.md
  research/proof/78-lt76-local-status-audit.md
  research/proof/79-side-block-archimedean-no-go.md
  research/proof/80-late-scale-insertion-no-go.md
  research/proof/81-scale-retention-decision-ledger.md
  research/proof/83-lt76-response-scoring-rubric.md
  research/proof/86-same-form-coupling-decision-ledger.md
  research/proof/87-carrier-selectivity-decision-ledger.md
  research/proof/88-traceability-proper-pushforward-ledger.md
  research/proof/89-conservative-bank-embedding-ledger.md
  research/proof/90-internal-archimedean-objects-ledger.md
  research/proof/91-zero-free-freeze-ledger.md
  research/proof/92-lt76-ledger-admission-matrix.md
  research/proof/105-lt76-trace-operation-overreach-audit.md
  research/proof/106-lt76-trace-operation-current-ledger.md
  research/proof/107-carrier-overreach-meta-lemma.md
  research/proof/108-carrier-overreach-proof-skeleton.md
  research/proof/112-late-carrier-reintroduction-no-go.md
  research/proof/114-lt76-strict-trace-admission-matrix.md
```

## 7. Landing Rule

Record any answer in doc 61 before updating the trajectory. A useful
answer must be classified as:

```text
KILL | ADVANCE | SHARPEN | DEMOTE | OUT_OF_SCOPE.
```

Encouraging analogies, literature pointers, or partial similarities
are background unless they decide one of the exact clauses above.
Doc 83 gives the scoring rubric for landing these answers. Doc 92
routes each claimed clause to the exact ledger and records which
claims must not be inferred.
