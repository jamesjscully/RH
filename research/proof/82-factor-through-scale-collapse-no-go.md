# 82 - Factor-through scale-collapse no-go

Status: proof lemma / NO76.1 boundary, 2026-06-11. This upgrades the
bare scale-collapse result into a reusable factorization criterion
without claiming a universal no-go for metric, liquid, equivariant, or
kernel traces.

## 1. Purpose

Docs 51 and 63 prove that bare circle and bare lattice-diagram
localizing-invariant data forget the scale `l = log p`. Doc 78 records
the overclaim guard: this does not prove broad NO76.1 for every
possible real/liquid trace package.

This document states the exact broader class that is killed:

```text
any candidate whose pre-trace data and trace factor through the bare
scale-blind diagram is scale-blind, even if it is presented with
enriched notation.
```

The useful distinction is:

```text
factor-through enrichment => REJECT_A1;
non-factoring enrichment => still live, but must pass doc 81.
```

## 2. Setup

For `l > 0`, let:

```text
D_l = (lZ -> R -> R/lZ)
```

be the bare topological lattice diagram, and let `B_l` denote any of
the following bare outputs:

```text
R/lZ as a bare circle;
Shv(R/lZ; C) with fixed dualizable coefficients C;
F^cont(Shv(R/lZ; C)) for an accessible/finitary localizing invariant;
the functorial localizing-invariant image of D_l.
```

By docs 51 and 63, `B_l` is naturally identified with `B_1`, before
metric, liquid analytic-ring, equivariant, density, or kernel data is
added.

## 3. Hypotheses

The lemma applies only under the following hypotheses.

```text
H1 bare factorization of pre-trace data
  The data seen by the trace factors through D_l, B_l, or the bare
  sheaf/localizing-invariant image of D_l.

H2 constant bare output
  The load-bearing target is built naturally from fixed dualizable
  coefficients C on lZ, R, R/lZ, and the induced maps.

H3 trace factorization
  The claimed trace/invariant is determined by the p-independent bare
  output, not by extra structure outside B_l.

H4 no surviving enriched carrier
  Any metric, liquid analytic-ring, equivariant, density, or kernel
  datum is absent, forgotten before trace evaluation, or used only
  after the scale-blind value has already been computed.
```

Removing H4 is exactly the live LT76.1/A1 escape route. The point of
the lemma is not that enrichment fails; it is that enrichment fails
when it does not survive to the load-bearing trace.

## 4. Factor-Through Normal Form

A proposed A1/LT76.1 scale-retention mechanism is in factor-through
normal form if there exist:

```text
1. a claimed pre-trace object O_l;
2. a trace/evaluation Tr_l;
3. a bare scale-blind object B_l;
4. maps Phi_l: O_l -> B_l and Psi_l from B_l to the trace domain;
5. a natural observable H;
```

such that the claimed trace value satisfies:

```text
Tr_l(O_l) = H(B_l)
```

or is naturally determined by the image of `O_l` in `B_l`.

Equivalently, after freezing all formulas before trace evaluation, the
candidate has no load-bearing data outside the scale-blind bare
diagram.

## 5. Lemma

### Lemma 82.1

If a proposed A1/LT76.1 mechanism is in factor-through normal form,
then it fails scale retention. In the doc-81 ledger its verdict is
`REJECT_A1`.

### Proof

Docs 51 and 63 give natural identifications:

```text
B_l ~= B_1
```

for every `l > 0`, in the allowed bare/localizing-invariant class.
Since the proposed trace value factors through `B_l`, it is naturally
identified with:

```text
H(B_l) = H(B_1).
```

Thus the frozen trace value is independent of `l`. Replacing
`l = log p` by any other positive real changes neither the factored
bare output nor any observable naturally built from it.

In particular:

```text
Tr_l(O_l) ~= Tr_1(O_1)
```

naturally through the factor-through diagram.

By doc 81, the deletion test therefore gives `REJECT_A1`. If `log p`
is appended afterward as notation, density, residue, normalization, or
comparison data, doc 80 additionally rejects the proposal as late
scale insertion. QED.

## 6. Examples Killed By The Lemma

The lemma kills a class, not isolated examples.

```text
K1 Enriched notation only
  O_l is written as a liquid/metric/equivariant object, but the trace
  first forgets to the bare Shv(R/lZ; C) or F^cont output.

K2 Density forgotten before trace
  A density or Haar scale is named, but the trace domain is obtained
  only after forgetting the density to the bare circle.

K3 Kernel shadow only
  A kernel is introduced, but the evaluated invariant depends only on
  its theta/count/Poisson shadow in B_l.

K4 Localizing readout with post-normalization
  The localizing-invariant value is computed first and then corrected
  by l, 1/l, 2pi/l, a determinant term, or a residue.

K5 Same underlying circle, isomorphic enriched structure
  The claimed enrichment is functorially isomorphic for all l before
  trace, so the trace still factors through B_1.
```

Each case can be rejected without running a new witness or positivity
cycle.

## 7. What Remains Live

The lemma does not apply to a candidate that proves non-factorization
before trace evaluation. Live escape profiles include:

```text
N1 Metric carrier
  The trace domain retains a metric coefficient, length, or growth
  structure that is not forgotten before trace.

N2 Liquid analytic-ring carrier
  O_l is a module/kernel category over an analytic ring whose norms or
  radii depend on l, and the trace theorem is stated in that category.

N3 Equivariant carrier
  The trace is genuinely parametrized or equivariant over the group
  object R/lZ, not merely over the underlying homotopy type S^1.

N4 Density carrier
  The density is an object in the trace domain, not an appended
  post-trace Haar normalization.

N5 Explicit kernel carrier
  The kernel uses l before trace and the trace theorem does not factor
  through theta/count/Poisson shadows or localizing-invariant data.
```

These profiles are not accepted automatically. They receive `HOLD_A1`
or `PASS_A1` only by the doc-81 ledger.

## 8. Diagnostic Test

Before accepting any claimed scale-retentive trace, ask for the
factor-through diagram:

```text
O_l -> B_l -> trace domain -> value.
```

Then apply:

```text
F82.1 Freeze
  Freeze O_l, Tr_l, and all maps before zero contact.

F82.2 Forget
  Apply every forgetful functor used by the construction before trace.

F82.3 Compare
  If the remaining load-bearing data is naturally B_l, replace l by 1.

F82.4 Verdict
  If the trace value survives unchanged, record REJECT_A1 by Lemma
  82.1. If some enriched datum cannot be forgotten without losing the
  trace theorem, record HOLD_A1 and route to doc 81.
```

## 9. Relation To NO76.1

This proves the following bounded NO76.1 theorem:

```text
NO76.1-factor-through:
  Any trace-class/localizing/kernel formalism whose load-bearing
  scale data factors through the bare scale-blind diagram forgets
  log p.
```

It does not prove:

```text
NO76.1-broad:
  every metric/liquid/equivariant/kernel trace forgets log p.
```

Doc 78's caveat remains in force. The external LT76 question is still
live exactly for non-factor-through trace packages.

## 10. Gate Update

For future B1/A6 proposals:

```text
1. run doc 81 first;
2. if the claimed carrier factors through B_l, reject by this lemma;
3. if it does not factor through B_l, answer the doc-84 theorem target
   before writing a witness;
4. never use post-trace scale readout as evidence against
   factor-through collapse.
```

This is the broad-class replacement for re-running bare-circle,
Poisson, theta/count, or post-normalization examples.
