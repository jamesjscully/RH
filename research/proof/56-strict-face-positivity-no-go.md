# 56 - Strict-face positivity no-go

Status: broad no-go proof draft, 2026-06-11. This turns T48.4 into a
reusable BC13 gate. It rules out positivity certificates whose natural
domain is a favorable face, finite panel, rung tower, strict square, or
proper subcone rather than the full Sonin/Frobenius-graph core.
Doc 67 isolates the reusable exhaustion normal form behind this gate.

## 1. Statement

Let `I` be a proposed nonnegative index, Gram, dimension, or count
form for the missing structure. Let `N_full` denote the full class
family required by doc 45 D2:

```text
the doc-00 Sonin core / HH Frobenius-graph cone, including k=1
boundary directions, recurrent deep graph steps, mixed towers,
real/conic directions, and uniform infinite-support filtration
behavior.
```

Assume that the proof of nonnegativity is certified only on a proper
subfamily `N_0`:

```text
N_0 proper subset N_full,
```

such as a strict square family, a ku face, a max-Gram/signature face, a
rung tower, a finite scanned window, a small-place panel, or any
hand-picked positive cone omitting the hard boundary directions.

Then the certificate cannot satisfy doc 45 D2-D4. If the attempted
extension from `N_0` to `N_full` requires a hand-inserted unit, repair
atom, chosen Gaussian, signed analytic correction, or estimate-based
positivity, it also fails doc 45 D1/D3.

## 2. Hypotheses

The no-go applies under the following hypotheses.

```text
H1 strict domain
  Positivity is proved on a named family N_0 strictly smaller than
  the full Frobenius-graph/Sonin core N_full.

H2 omitted hard directions
  N_0 omits at least one required direction type: k=1 boundary prime
  atoms, recurrent deep graph steps, mixed towers, real/conic
  directions, or uniform infinite-support behavior.

H3 no spanning theorem
  There is no theorem proving that N_0 spans, exhausts, or controls
  N_full in the candidate's native category.

H4 no candidate-native unit for extension
  Any attempted extension uses a chosen unit, strict repair atom,
  signed analytic correction, or estimate rather than the candidate's
  own derived unit and forced-nonnegative value type.
```

H4 is needed only for the D1/D3 part. H1-H3 already kill D2-D4.

## 3. Local Dependencies

```text
doc 45 D1-D4
  D1 requires forced nonnegativity by native structure. D2 requires
  full graph-cone exhaustion. D3 requires the candidate's own unit.
  D4 requires persistence along the infinite support filtration.

doc 44
  M-B(strict proxy) is done: NN kills the strict-square /
  hand-inserted-unit extension to Frobenius-graph classes. M-B(live
  candidate) is not runnable until a genuine liquid/index candidate
  exists.

doc 43
  The named Gaussian deep-cell phase is slot data: AB's self-dual
  Hermite unit flips the banked `(11;2)@4.96` cell. Therefore a
  strict-face repair using a chosen unit is not object data.

doc 42
  The banked carrier classification marks strict-face, ku-face, and
  max-Gram/signature carriers as supply or face data, not survivors
  passing BC-E3' plus BC13 at decision grade.
```

## 4. Proof

### Step 1: Proper subfamily fails D2

Doc 45 D2 requires positivity over the full graph-cone class family.
If positivity is proved only on `N_0` and `N_0` is a proper subfamily
of `N_full`, then the certificate does not cover all required classes.

This is a logical implication, not a numerical one:

```text
positive on N_0
  does not imply
positive on N_full
```

unless a spanning or exhaustion theorem connects the two. H3 says no
such theorem is present. Therefore D2 fails.

### Step 2: Omitted boundary directions fail D4

Doc 45 D4 requires uniform persistence along the infinite support
filtration. A finite window, small-place panel, rung tower, or strict
face that omits recurrent direction types has not proved persistence.

In doc 44/NN, the hard omitted or breaking classes include:

```text
k=1 prime-atom steps;
recurrent deep graph steps;
mixed or rung behavior not tracking tau;
strict-family small-place artifacts.
```

If those directions are outside the certificate, D4 is not addressed.
If they are inside and break, the strict-face certificate is killed.
Either way, a strict-face certificate is not BC13.

### Step 3: Inserted repairs fail D1/D3

Doc 45 D1 requires nonnegativity to be forced by native type:
dimension, count, Gram norm, index-level integer, or a comparably
structural nonnegative value. Doc 45 D3 requires the candidate's own
unit and covariant slot data.

If the extension to `N_full` uses a hand-inserted unit, chosen
Gaussian, strict repair atom, or signed analytic correction, the sign
is not forced by the candidate's native value type. It is a repaired
presentation.

Doc 43 strengthens this point: the Gaussian deep-cell sign is
unit-parametric. Since an admissible self-dual Hermite unit flips the
banked `(11;2)@4.96` cell, a proof depending on that chosen unit's
sign cannot be promoted to an object condition.

Thus H4 implies D1/D3 failure.

Combining the steps gives the theorem:

```text
strict positivity domain without a spanning theorem
  => D2/D4 failure;

strict extension by inserted unit or signed repair
  => D1/D3 failure.
```

## 5. Classified Failure Modes

```text
strict square / LL unit-repaired inequality
  Posable and useful, but NN/doc 44 kill its verbatim extension to
  Frobenius-graph classes. It does not exhaust the full cone.

ku face
  The best theorem-grade supply model and depth-wall shadow, but one
  face is not the full graph-cone family and it supplies no P3
  second evaluation by itself.

max-Gram / signature flow
  Certifies Lorentzian shape and useful signatures, but it is a face
  or supply-grade diagnostic unless paired with full-cone exhaustion
  and an independent odd-slot comparison.

finite scanned panels
  Useful fail-closed witnesses. They cannot establish D4 uniformity
  without a theorem along the infinite support filtration.

rung towers and small-place panels
  Useful for locating structure. They fail as BC13 certificates if
  their margins do not control the omitted classes or do not persist
  uniformly.

Gaussian deep-cell signs
  Slot-parametric by doc 43. A chosen deep-cell phase is not an object
  condition and cannot certify full-cone positivity.
```

## 6. Candidate Gate

Before promoting any positivity result to BC13, require the following.

```text
G56.1 Value type
  Is I nonnegative by native structure: dimension, count, Gram norm,
  index-level integer, or equivalent forced-positive type?
  If no, reject D1.

G56.2 Unit source
  Is the unit the candidate's own derived unit, with all slot data
  stated covariantly?
  If no, reject D3 or route to doc 55.

G56.3 Domain
  Name N_full and N_0. Prove N_0 = N_full, or give a spanning theorem
  from N_0 to N_full in the candidate's native category.
  If no, reject D2. See doc 67.

G56.4 Hard directions
  Exhibit k=1 boundary directions, recurrent deep graph steps, mixed
  towers, real/conic directions, and infinite-support behavior inside
  the covered class family.
  If any are omitted, reject D2/D4.

G56.5 Uniformity
  Prove persistence along the support filtration. Finite panels,
  scanned windows, and small-place tests are not enough.
  If no, reject D4. See doc 67.

G56.6 Independence
  If I is meant to be the index side of the final comparison, pair it
  with the doc-52 P3 gate: a nonempty unforced odd slot and an
  independent Count domain are still required.
```

Passing G56 does not prove RH. It only keeps the positivity side from
being rejected as a strict-face BC13 failure.

## 7. Exact Escape Profile

A candidate escapes this no-go only by supplying all of the following.

```text
E1 full native class family
  A class family N whose native definition already includes the
  full Sonin/Frobenius-graph core.

E2 forced nonnegativity
  A value I that is nonnegative by type, not by a signed estimate or
  repaired presentation.

E3 candidate-native unit
  The unit used in I is derived by the candidate, and all slot data is
  stated in covariant coordinates.

E4 exhaustion theorem
  A theorem proving N exhausts the required graph cone and persists
  uniformly along the infinite support filtration.

E5 P3 compatibility
  The positive index/Gram side is compatible with an independent
  Count evaluation and nonempty unforced odd slot.
```

This is exactly the live M-B target from doc 44. It is not currently
runnable because no present liquid/index candidate supplies E1-E5.

## 8. Program Consequence

T48.4 is now a reusable gate:

```text
Do not promote strict-square positivity, ku-face positivity,
max-Gram signatures, finite windows, rung towers, or Gaussian
deep-cell phases to BC13.
```

The live target remains: construct a liquid/metrized Euler-product
carrier with a candidate-native unit whose forced-nonnegative
index/Gram value exhausts the full graph cone and is paired with a
P3-grade second evaluation.
