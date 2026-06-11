# 100 - Mixed-object shadow-enlargement no-go

Status: proof lemma / S3 conditional no-go, 2026-06-11. This hardens
the doc-98 `NSE98.4` target under explicit closure hypotheses. It does
not prove that every strict Euler-carrier trace domain is impossible.

## 1. Purpose

Doc 99 names the next local hardening target:

```text
prove that any trace domain rich enough to host the required mixed
object M_C must enlarge to represented-norm, commutative-monoid, or
measure shadows, triggering doc 97.
```

That statement is false without hypotheses: a genuinely strict
`ECar_L1` domain might require primitive Euler-carrier fields before the
mixed object or trace exists. This document proves the bounded version:
if the mixed object is built functorially from shadow data before any
primitive carrier check, then the domain is overbroad.

## 2. Shadow-Enlargement Hypotheses

Let an S3 proposal claim:

```text
b1(comb_C) -> M_C <- R_L/T_C
M_C -> F_C -> Tr_L(F_C).
```

Say it is shadow-enlarging if it satisfies all of:

```text
H100.0 shadow functor
  There is a forgetful or detection functor U from the proposed trace
  domain to a shadow category Sh containing length/weight data,
  positive multisets, commutative monoids, represented-norm monoids, or
  positive discrete measures.

H100.1 pre-carrier shadow input
  Before the first carrier-consuming map, the construction of M_C uses
  only monoidal product, additive/count data, length or log-size
  functions, positive discrete measures, theta/count shadows,
  coefficient multisets, determinant/coker shadows, or functorial
  module/kernel operations on those data.

H100.2 control closure
  The input class is closed under replacing the prime-power comb by any
  represented-norm monoid or positive coefficient/measure shadow with
  the same kind of length/count data.

H100.3 natural mixed object
  The maps b1(comb_C) -> M_C and R_L/T_C -> M_C are natural for the
  shadow input class, commute with U, or are detected after applying U.
  They do not require a distinguished atom alpha, unique valuation v,
  tower/depth coordinate, ell, mu_C, or Euler-product factorization
  domain as primitive object data.

H100.4 trace theorem follows the shadow
  The trace/properness/duality/nuclearity theorem invoked for M_C also
  applies to the shadow-replaced mixed object.

H100.5 derived codomain follows the shadow
  The same-form codomain F_C and the carrier-reading form are derived
  from M_C by functorial operations that still make sense after the
  shadow replacement.
```

These hypotheses are intentionally checkable. A proposal can escape
this lemma only by naming the first step where primitive carrier fields
are required before M_C, F_C, or the trace is defined.

## 3. Lemma

### Lemma 100.1

Any S3 proposal satisfying H100.0-H100.5 is rejected by doc 97 as
carrier overreach.

### Proof

By H100.0-H100.3, the proposed mixed object construction is functorial
for a shadow input class broader than primitive Euler carriers. H100.2
says this class includes represented-norm monoids and positive
coefficient/measure shadows.

Apply the construction to the Epstein control

```text
Q(x,y) = x^2 + 5y^2.
```

Doc 64 records that this control has a represented-norm and theta/count
shadow but lacks a free prime-power valuation, distinguished atom, or
unique tower coordinate:

```text
1, 4, 6, 9, 36 are represented;
2, 3 are absent;
4, 6, 9 are represented-norm irreducibles;
36 = 4*9 = 6*6.
```

Under H100.2-H100.5, the shadow replacement still produces

```text
M_Q -> F_Q -> Tr_L(F_Q).
```

Thus the first mixed-object, codomain, or trace map is formable for the
Epstein control. The proposed carrier/effectivity failure does not occur
before signs, positivity, zeros, or comparison. This is exactly the doc
97 overreach condition and the doc 87 carrier-selectivity failure:

```text
REJECT_CARRIER_OVERREACH;
REJECT_CARRIER_BLIND.
```

The same argument applies to any DH-type coefficient or positive
measure shadow covered by H100.2. Therefore the S3 proposal cannot pass
carrier selectivity. QED.

## 4. What This Proves

The lemma kills a broad class:

```text
mixed objects built from count/measure/monoid shadows;
kernel traces natural for positive discrete measures;
determinant or coker packages functorial before carrier checking;
trace-derived codomains whose derivation does not require primitive
Euler fields until after M_C or F_C exists.
```

It also explains why a trace-derived form can be insufficient. Escaping
doc 93 is not enough: if the trace-derived codomain follows shadow
replacement, doc 97 still applies.

## 5. What This Does Not Prove

This is not a global rejection of S3. It does not cover a proposal that
provides:

```text
1. a named ECar_L1 domain whose objects require alpha, v, depth, ell,
   mu_C, and Euler factorization before M_C exists;
2. a trace theorem legal on that strict domain;
3. a conservative B0 bank embedding into that strict domain;
4. one mixed M_C receiving both bank and continuum before trace;
5. a proof that Epstein/DH shadows are not ECar_L1 objects or fail at
   the first carrier-consuming map;
6. zero-free freeze before first zero contact.
```

Such a proposal remains governed by doc 98 and doc 99. This document
only says that if the mixed object is available by shadow functoriality
first, the strict-domain escape has already been lost.

## 6. Falsification Checklist

For any future S3 proposal, ask:

```text
F100.1
  Is M_C constructed before any primitive alpha/v/depth/ell/mu_C/Euler
  factorization check?

F100.2
  Are the M_C input operations functorial for commutative monoids,
  represented-norm data, positive multisets, coefficient multisets, or
  positive measures?

F100.3
  Does the trace theorem still apply after replacing the prime-power
  comb by the Epstein represented-norm shadow?

F100.4
  Does F_C still exist after that replacement?

F100.5
  If the answer to any of F100.1-F100.4 is no, what exact first map or
  object requires primitive Euler carrier fields?
```

If F100.1-F100.4 are yes, record doc-98 `REJECT_CARRIER_OVERREACH` and
doc-99 `KILL` for the covered class. If F100.5 names a genuine strict
first map, route the proposal back to doc 98 as `HOLD_STRICT_EULER` or
`PASS_STRICT_EULER` according to the remaining fields.

## 7. Relation To Existing Docs

```text
doc 64
  Supplies the Epstein represented-norm obstruction.

doc 87
  Gives the carrier-selectivity ledger.

doc 93
  Rejects free externally supplied forms. Doc 100 is separate: it can
  reject even trace-derived forms if they follow shadows.

doc 97
  Gives the carrier-overreach no-go that doc 100 triggers under
  shadow-enlargement hypotheses.

doc 98
  Gives the strict ECar_L1 escape target outside this lemma's
  hypotheses.

doc 99
  Names this as the next local hardening target and keeps S3 at HOLD
  outside the covered class.

doc 107
  Extracts this proof into the shared carrier-overreach meta-lemma.
```
