# 67 - BC13 exhaustion normal form

Status: proof lemma / gate hardening, 2026-06-11. This isolates the
lasting content behind doc 56 and doc 44: a positivity result on a
proper face, finite panel, rung tower, or strict proxy is not a BC13
certificate unless it is promoted by a native spanning theorem over the
full graph cone.

## 1. Purpose

Doc 56 is the broad no-go. Doc 44 records the only concrete banked
proxy test: NN kills the strict-square / hand-inserted-unit extension
to Frobenius-graph classes. This document extracts the reusable normal
form so future D-side proposals are judged by a theorem obligation, not
by rerunning variants of the same example.

The target is doc 45 clause D:

```text
I is forced nonnegative on the full Sonin/Frobenius-graph core,
and this persists uniformly along the infinite support filtration.
```

Equivalently, the candidate must satisfy BC13:

```text
index positivity + full class/scale exhaustion.
```

## 2. Normal Form

Let `N_full` be the candidate's claimed class family for the full
Sonin/Frobenius-graph core. It must include:

```text
k=1 boundary directions;
recurrent deep graph steps;
mixed towers;
real/conic directions;
uniform infinite-support filtration behavior.
```

Let `N_0` be the domain on which nonnegativity has actually been
proved. A D-side certificate has BC13 normal form only if it supplies
all four pieces below.

```text
NF67.1 Native nonnegative value
  I takes values in a type that is nonnegative by construction:
  dimension, count, Gram norm, index-level integer, or equivalent.

NF67.2 Native unit and slot covariance
  The unit used to define I is candidate-native, and all slot choices
  are stated covariantly.

NF67.3 Exhaustion theorem
  Either N_0 = N_full by definition, or there is a theorem in the
  candidate's native category proving that N_0 spans, exhausts, or
  controls N_full for the same I.

NF67.4 Uniform filtration theorem
  The exhaustion persists uniformly along the infinite support
  filtration; finite windows, panels, and rung samples are only
  witnesses unless they come with this theorem.
```

Failure of any item demotes the result to supply, calibration,
diagnostic, or face data. The failures should be kept separated:
NF67.3-NF67.4 are the D2/D4 exhaustion and uniformity clauses, while
NF67.1-NF67.2 are the D1/D3 value and unit clauses.

## 3. Lemma

### Lemma 67.1

Assume `N_0` is a proper subfamily of `N_full`, and no theorem in the
candidate's native category proves that `N_0` spans, exhausts, or
controls `N_full` for the same index/Gram/count form `I`. Then
nonnegativity of `I` on `N_0` is not a BC13 certificate.

### Proof

BC13 requires positivity on the full class family, not only on a
favorable domain. By hypothesis the proved domain is proper:

```text
N_0 proper subset N_full.
```

Therefore the formal implication

```text
I >= 0 on N_0  =>  I >= 0 on N_full
```

is not available from the certificate itself. The only admissible way
to obtain that implication is an exhaustion/spanning/control theorem
in the candidate's native category for the same `I`. The hypothesis
says that no such theorem is present. Hence the certificate does not
prove the full-class positivity part of BC13.

If `N_0` is finite, a scanned window, or a rung tower, the same
argument also applies to the uniformity clause: finitely many checked
classes do not imply persistence along the infinite support filtration
without a uniform theorem.

Thus `N_0`-positivity without native exhaustion is not BC13. QED.

### Separate Value/Unit Failure

Lemma 67.1 proves only the D2/D4 failure. If the attempted extension
from `N_0` to `N_full` also uses a chosen Gaussian, inserted unit,
repair atom, signed correction, or estimate-based positivity, then it
fails D1/D3 independently. That additional failure is governed by docs
43, 55, and 66; it is not needed for the exhaustion lemma.

## 4. Corollaries

```text
C67.1 Strict square
  Positivity on the strict square is not BC13 unless the strict square
  is proved to exhaust the full Frobenius-graph core. Doc 44/NN shows
  the verbatim hand-inserted-unit extension fails.

C67.2 ku face
  A ku-face inequality package may be theorem-grade supply, but one
  face is not the full graph cone without an exhaustion theorem.

C67.3 max-Gram / signature / stress-flow
  A face, signature, or stress-flow diagnostic can identify useful
  shape constraints. It is not full D-side positivity unless paired
  with native nonnegativity and full-cone exhaustion. See doc 70 for
  the corresponding P3/diagnostic role discipline.

C67.4 finite panels and rung towers
  Finite checks and tower samples can refute or calibrate. They cannot
  prove BC13 uniformity unless promoted by a theorem along the whole
  support filtration.

C67.5 Gaussian deep-cell signs
  A chosen deep-cell sign is slot data by doc 43 and doc 66. Even a
  positive chosen presentation would still need native unit covariance
  plus NF67.3-NF67.4.
```

## 5. Relationship To Existing Gates

Doc 56 states the broad rejection rule. This document is the reusable
proof object behind G56.3-G56.5 and G60.6-G60.7. Its dependencies are:

```text
doc 45
  D1-D4 define the positivity/exhaustion target.

doc 44
  NN closes the strict-square hand-inserted-unit proxy and separates
  M-B(strict proxy) from M-B(live candidate).

doc 43
  Shows that Gaussian deep-cell signs are unit-slot data, not object
  data.

doc 56
  Lists the broad strict-face, finite-panel, rung-tower, and proper
  subcone failure modes.

doc 66
  Supplies the unit-covariance rule for signs and constants that vary
  under admissible self-dual unit replacement.
```

It does not prove that no live liquid/index candidate can satisfy
BC13. It does not prove positivity for any candidate, and it does not
settle P3 second-evaluation independence; that remains the doc 65 /
G60.8-G60.9 gate. It proves only the admission rule:

```text
No proper-face positivity certificate is BC13 without native
nonnegativity, native unit covariance, a full-cone exhaustion theorem,
and uniform support-filtration persistence.
```

## 6. Live D-Side Target

A surviving D-side proposal must now state:

```text
T_D67 value theorem
  I is nonnegative by native type.

T_D67 unit theorem
  the unit used in I is candidate-native and slot-covariant.

T_D67 exhaustion theorem
  the covered class family is the full Sonin/Frobenius-graph core, or
  a native theorem promotes the covered domain to it.

T_D67 uniformity theorem
  the result persists along the infinite support filtration.
```

Only after these are stated does it make sense to run a new D-side
witness. Otherwise the witness can be useful only as calibration or
refutation data.
