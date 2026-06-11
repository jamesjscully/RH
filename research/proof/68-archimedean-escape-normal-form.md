# 68 - Archimedean escape normal form

Status: proof lemma / gate hardening, 2026-06-11. This isolates the
reusable content behind doc 57: p-complete TP/TR/Witt/prismatic data
can be supply or address data, but it is not the missing archimedean
slot unless a structural archimedean escape is built into the same
candidate.

## 1. Purpose

Doc 57 is the broad no-go for purely p-complete towers. This document
extracts the admission normal form for a candidate that starts from
TP, TR, TC, Witt, prismatic, or Nygaard-complete material and wants to
claim doc 45 A/E content.

The target clauses are:

```text
A2
  internal R and T=R/Z with the archimedean completion present;

A4
  a trace/coupling pairing the p^Z comb and archimedean continuum on
  the same index/Gram/count form;

E1/E3
  independent Count and nonzero unforced odd spectrum, not merely
  TR/Witt/TP transport.
```

## 2. Normal Form

A p-complete-origin construction has archimedean escape normal form
only if it supplies all five pieces below.

```text
NF68.1 Internal real object
  The category contains a structural R object and T=R/Z object, not
  only p-adic coefficients plus an external complex readout.

NF68.2 Structural iota
  Any map playing the role of iota is constructed inside the global
  carrier and tied to the candidate's address object. A post hoc
  embedding into C is calibration or readout data.

NF68.3 Same-form LS4 coupling
  The trace implements the sequence 0 -> (log p)Z -> R -> T_p -> 0
  as a comb-continuum exchange on the same index/Gram/count form.
  A separate positive archimedean summand is not enough.

NF68.4 Non-transport Count
  Count has a natural extension domain different from the p-complete
  trace/index domain; TR_0=W, Witt fixed points, cyclotomic trace
  comparison, coker=det algebra, and regularization of one object do
  not supply this by themselves.

NF68.5 Unforced odd slot
  H_odd is nonzero, and its eigenvalues are supplied by the carrier
  before Frobenius, Adams weight, cyclotomic degree, q, p, or another
  acting parameter is chosen.
```

Without NF68.1-NF68.3, the construction fails the A-side archimedean
slot. Without NF68.4-NF68.5, it fails the E-side second evaluation.

## 3. Lemma

### Lemma 68.1

Assume a construction is pure p-complete in the sense of doc 57:
its coefficients and mapping objects are p-complete or p-adic, its
native operations are TP/TR/TC/Witt/prismatic/cyclotomic operations,
and it supplies no internal `R`, no internal `T=R/Z`, no structural
`iota`, and no same-form comb-continuum trace. Then it cannot satisfy
doc 45 A2 or A4.

### Proof

Doc 45 A2 requires the archimedean object itself, not just a finite
place address. Under the purity hypotheses, the construction's native
objects remain p-complete or p-adic. They may carry Frobenius,
Verschiebung, restriction, cyclotomic trace, Witt ghost data,
Nygaard/prismatic filtrations, and p-adic completions, but the real
additive line and the metrized circle are not internal objects.

Therefore A2 is absent by hypothesis.

Doc 45 A4 requires more than an archimedean value beside a p-complete
value. It requires a trace pairing the banked p^Z comb with an
archimedean continuum on the same form:

```text
0 -> (log p)Z -> R -> T_p -> 0.
```

Under the purity hypotheses, no such internal `R`, `T_p`, or
same-form trace exists. A later complex determinant, external
regularization, or separate archimedean correction term is a readout
or side block, not the LS4 coupling.

Thus a pure p-complete construction fails A2 and A4. QED.

### Lemma 68.2

If a p-complete-origin construction's proposed Count/Index equality is
only TR/Witt/TP/cyclotomic transport or determinant algebra on one
functorial trace object, then it does not satisfy doc 45 E1. If the
claimed odd spectrum is supplied by Frobenius, Adams weight,
cyclotomic degree, p, q, or the acting correspondence itself, then it
does not satisfy doc 45 E3.

### Proof

E1 requires different natural extension domains for Count and I.
Transport along

```text
TR_0 = W,
Witt fixed-point descriptions,
cyclotomic trace maps,
TC^- -> TP,
coker=det algebra,
regularization of the same p-complete object
```

does not create a second natural domain. It rereads one functorial
trace object. This is the doc 52/doc 65 P3 failure.

E3 requires eigenvalues supplied by the carrier/slot before the acting
correspondence queries them. Frobenius weights, Adams parameters,
cyclotomic degrees, q, p, and fixed-point eigenvalues are action-side
data in this setting. They do not form an unforced odd spectrum.

Therefore transport gives no E1/E3 escape. QED.

## 4. Caveats

This document does not say that p-complete, TP/TR/Witt, or prismatic
objects are useless. It says only that they are not the archimedean
slot or P3 second evaluation without the normal-form escapes above.

```text
finite-field TP determinant
  Useful calibration. Its complex determinant uses iota: W(F_q) -> C,
  so it is not a pure p-complete counterexample.

hybrid liquid construction
  Not ruled out. A construction may start from p-complete supply data
  if it adds internal R/T, structural iota, same-form LS4 coupling,
  and independent P3 data.

side archimedean block
  Not enough. The trace must couple comb and continuum on the same
  form, not add a positive correction term beside the p-complete bank.

transport equality
  May be a real theorem, but as transport it remains one evaluation
  unless an independent Count domain is supplied.
```

## 5. Relationship To Existing Gates

```text
doc 45
  Defines A2/A4 and E1/E3.

doc 57
  Gives the broad p-complete archimedean-blindness no-go.

doc 60
  Uses this at G60.2 scale retention, G60.3 internal R/T, G60.5 LS4
  coupling, G60.8 odd-slot supplier, and G60.9 Count/Compare.

doc 65
  Supplies the general P3 independence normal form for E-side failure.
```

The resulting admission rule is:

```text
Pure p-complete supply is not A/E content until it adds internal R/T,
structural iota, same-form LS4 coupling, non-transport Count, and
unforced nonzero H_odd.
```

## 6. Live A/E Target

A surviving p-complete-origin proposal must state:

```text
T_A68 address theorem
  internal R and T=R/Z live in the same category as the finite-place
  address data.

T_A68 iota theorem
  the archimedean realization is structural and carrier-native.

T_A68 coupling theorem
  the trace realizes comb-continuum exchange on the same form.

T_E68 independence theorem
  Count and I have different natural domains and agree by a theorem
  beyond TR/Witt/TP transport.

T_E68 odd-slot theorem
  H_odd is nonzero and its eigenvalues are unforced by the acting map.
```

Without these statements, further p-complete-origin witnesses should
be treated as supply calibration or fail-closed diagnostics, not as
candidate evidence.
