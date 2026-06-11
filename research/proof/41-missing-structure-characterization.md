# 41 - Missing-structure characterization

Status: 2026-06-11. Consolidates docs 34 and 38-40 plus workers XX,
YY, ZZ, AB, AC. This is a characterization target, not a construction
and not a proof of RH.

## 1. Normal form

An arriving candidate for the missing structure should be presented as a
package

```text
M = (carrier, liquid address, unit, Frobenius action, odd slot,
     index/Gram form, count evaluation, comparison theorem).
```

The names are intentionally interface-level. They are not new objects
by themselves; each slot must be filled by native mathematics in the
candidate's field.

```text
carrier
  A multiplicative/Euler-product carrier on which prime-power classes
  are defined. It must be unavailable for DH/Epstein for structural
  reasons, not because a later computation returns the wrong sign.

liquid address
  The place where log p survives. Bare sheaves on R/(log p)Z and their
  localizing invariants are scale-blind by XX; solenoids carry the
  address but self-supply their scale. A live address must therefore
  live in enriched/metrized coefficients, analytic rings, equivariant
  refinements, or nontrivial kernels, not in Shv(S^1; constant C).

unit
  A derived continuum unit, one per Lambda(p) class, not a hand-inserted
  repair term. Its own Mellin/Fourier data may determine slot-shapes,
  but the object conditions below must survive a change of admissible
  unit.

Frobenius action
  A class-and-scale indexed action/correspondence that queries the
  carrier. Its role is not to supply the relevant eigenvalues by
  definition; self-supplied degree data is the solenoid failure mode.

odd slot
  A nonempty determinant/cohomological/spectral odd slot. Nonempty is
  necessary but insufficient: TP_odd(F_q)=0 is empty, while H^1(S_p)
  is nonempty but self-supplied. The unknown must live on the spectral
  side of an agreement theorem.

index/Gram form
  The sign source. Values must be forced nonnegative by what they are
  (dimension, count, Gram norm, or index-level integer), not by analytic
  estimates with slack and not by a signed second evaluation.

count evaluation and comparison theorem
  A second evaluation in YY's P3 sense: two structures with larger
  natural domains, agreement on the common locus by a theorem with
  content, and at least one unforced spectral parameter constrained.
```

## 2. Object Conditions

These are the de-tautologized conditions from AB, with BC13/BC-E3'
inserted from AC/ZZ.

```text
OC1 integer charge
  The object supplies the -1 continuum-unit charge on every Lambda(p)
  class, while truncation bands remain 0-charge bookkeeping. This is
  charge quantization, not Gaussian silhouette data.

OC2 threading
  Per-place deficits are unpayable under every admissible unit, while
  the KMS-beta=1/2 global aggregate pays the scanned deficit. The
  object must move surplus across places. Which specific slot breaks
  for a chosen unit is slot data and is not admissible evidence. Doc 43
  sharpens this: the banked Gaussian `(11;2)@4.96` deep-cell failure
  flips positive under a self-dual Hermite unit, so deep-cell phase
  negativity is not part of OC2.

OC3 depth wall
  The demand/supply law is unit-free with constant 1 in covariant
  units. No estimate with a rescaled constant, epsilon, or asymptotic
  slack can count as the mechanism.

OC4 carrier consumption
  The Euler-product carrier is load-bearing. A candidate that can be
  run verbatim on Epstein/DH has not found the carrier.

BC13 index positivity and exhaustion
  The second evaluation takes forced-nonnegative index/Gram/count
  values, and the class/scale family on which the comparison theorem
  holds exhausts the doc-00 filtration core: all shells, all R, or
  equivalently the Frobenius-graph cone named in doc 34/AC.

BC-E3' unforced odd slot
  The odd slot is nonempty and its eigenvalues are not definitionally
  supplied by the acting map/correspondence. The structure fills the
  slot; the action queries it.
```

## 3. Slot Data To Demote

The following may be useful diagnostics, but are not evidence that the
missing structure has been characterized beyond its interface.

```text
shape law
  c_n log p = -2 Re f_tilde(2 pi i n / log p), evaluated with the
  candidate's own unit. Passing the Gaussian 12-number test is necessary
  only for a Gaussian-slotted candidate and is never sufficient.

payment constants
  The entry constants, payment schedules, and amplitudes are functionals
  of the inserted unit. AB shows their signs can change under admissible
  unit changes.

address without unit
  The solenoid gives p-addressed H^1 and entropy log p, but the
  eigenvalue is the map's own degree. This is carrier-grade data, not
  unit-grade data.

FE-layer conformance
  A construction that only reproduces the functional equation or Tate
  local silhouette is shape-complete and mechanism-empty unless it also
  supplies BC13 and BC-E3'.
```

## 4. Arrival Gates

Every proposed candidate should be scored on arrival, before any
cycle-specific enthusiasm.

```text
G1 Carrier selectivity
  Does the carrier fail to exist for DH/Epstein at the structural
  address? If not, the candidate is either over-broad or EF-derived.

G2 Scale retention
  Where exactly does log p live? Answers of the form "the circle
  R/(log p)Z" fail by XX unless the metric/enriched coefficient data is
  part of the object.

G3 P3 second evaluation
  Name the two evaluations, their larger deformation domains, and the
  theorem cutting the agreement locus. If both sides move through a
  natural isomorphism, it is one evaluation.

G4 BC-E3' supplier audit
  Who supplies the odd-slot eigenvalue? Empty = F_q failure. Supplied by
  the acting map's degree = solenoid failure. Read from zero-side input
  = circular. The only live answer is: supplied by the carrier/slot
  structure independently of the querying action.

G5 BC13 exhaustion
  Does the forced-nonnegative index/Gram family span the full doc-00
  core or only a strict/scanned face? Strict-family-only is not enough.

G6 Unit covariance
  Re-run the shape/payment claims with the candidate's own unit. Claims
  depending on the Gaussian values of slot data are demoted.

G7 Fork protocol
  Apply doc 14: value fork, deformation kill, and slack audit. Surviving
  candidates must supply extra information and carrier non-existence
  controls, then still pass the full-locus comparison requirement.
```

## 5. Fast Falsifiers

These are the cheapest ways to learn from a candidate.

```text
empty slot
  TP_odd or the analog is zero. Verdict: embryo asleep.

self-supplied slot
  The spectral parameter is the endomorphism's own degree or a chosen
  input. Verdict: one-evaluation or forced-spectrum embryo.

transport
  The comparison is a chain of natural isomorphisms, Poisson transport,
  coker=det linear algebra, or regularization of the same series.
  Verdict: one evaluation.

strict-face positivity
  The index/Gram is positive only on a strict family or scanned window.
  Verdict: fails BC13 until extended to the Frobenius-graph cone.

slot artifact
  The claimed obstruction or payment flips under an admissible unit.
  Verdict: slot data, not object data.

carrier overreach
  The construction computes for DH/Epstein. Verdict: wrong carrier or
  no load-bearing Euler product.

zero import
  The eigenvalues or signs are read from zeta zeros before the carrier
  is built. Verdict: circular by the freeze/fork protocol.
```

## 6. Dispatchable Consequences

This characterization changes the next work from "find another shadow"
to three concrete tests.

```text
M-C first
  Classify every banked carrier against BC-E3': empty, self-supplied,
  norm-collapsed, transport, strict-face-only, or survivor. First pass
  executed in doc 42: no promoted banked carrier survives at decision
  grade; the positive shadows remain separated across carriers.

M-A next
  Run the deep-cell self-dual LP only as a unit-independent test of OC2.
  First pass executed in doc 43: feasible at the banked deep cell under
  a self-dual Hermite unit. The obstruction remains k=1 threading plus
  global payability; the unit-free depth wall belongs to OC3.

M-B after supplier audit
  The g2/Frobenius-graph exhaustion probe is valuable only if it tests
  BC13 on the full graph cone rather than another slotted/scanned face.
  Doc 44 separates the cases: the strict-square / hand-inserted-unit
  proxy is already killed by NN, while the live M-B cannot run until a
  liquid/index candidate with its own unit exists.
```

## 7. Communicable Form

For external discussion, the missing structure can be stated without
the internal BC ledger:

```text
Find a liquid/metrized Euler-product carrier with a Frobenius-index
pairing whose values are intrinsically nonnegative and whose comparison
with an independent count evaluation has a nonempty odd spectral slot
with eigenvalues not supplied by the acting correspondence. The
comparison must range over the full Sonin/Frobenius-graph filtration,
not a strict face, and the carrier must fail structurally for DH/Epstein.
```

That sentence is not a theorem. It is the current sharp interface of
the missing object.
