# 69 - Zero-free freeze normal form

Status: proof lemma / protocol hardening, 2026-06-11. This isolates
the reusable content behind doc 59 and G60.10: zero-side data may
compare with a frozen candidate, but it may not choose, tune, repair,
or define the candidate.

## 1. Purpose

Doc 59 is the broad zero-import no-go. This document extracts the
normal form needed before any candidate can be fork-tested or compared
against zeta zeros without circularity.

The required factorization is:

```text
candidate construction C
  -> frozen record F
  -> optional zero comparison Z.
```

The construction stage `C` must define the carrier, address, unit,
class family, loci, constants, `H_odd`, `I`, `Count`, and `Compare`
without zeta zeros, RH-line information, zero-side signs, zero-side
eigenvalues, or explicit-formula zero expansions. The frozen record
`F` documents those choices before zero contact. Only after `F` may a
zero comparison `Z` be run.

## 2. Normal Form

A candidate has zero-free freeze normal form only if it supplies all
five pieces below.

```text
NF69.1 Zero-free suppliers
  Every object and choice in the candidate package has a supplier that
  is not zero-side data: carrier, address, unit, H_odd, I, Count,
  Compare, loci, class family, constants, signs, and phases.

NF69.2 Frozen record
  The formulas, files, class families, constants, parameters, and
  witness commands are recorded before any zero data is loaded.

NF69.3 Reproducibility witness
  The freeze has a proof-local definition, deterministic witness
  output, hash, or comparable record. Deterministic code is not enough
  unless its inputs are also zero-free and pre-frozen.

NF69.4 First zero-contact point
  The first use of zeta zeros, zero-side identities, RH-line facts, or
  fork_lib.zeta_gammas is named explicitly.

NF69.5 Permitted role
  Every post-freeze zero use is comparison, sanity check, deformation
  control, implication audit, or fork diagnosis. It is not a repair or
  construction input.
```

Passing NF69 proves only admissibility for later comparison. It does
not prove P3 independence, nonempty `H_odd`, carrier selectivity,
positivity, or RH.

## 3. Lemma

### Lemma 69.1

If any element of the frozen record `F` is selected by minimizing,
fitting, normalizing, tuning, validating, repairing, or choosing
against zero-side data before freeze, then the candidate fails doc 45
E3/E4 as a supply-side construction and is demoted to explicit-formula
transport or fork diagnostic.

### Proof

Doc 45 E3 requires odd-slot eigenvalues to be supplied by the
carrier/slot before the acting correspondence queries them. If
zero-side eigenvalues or RH-line spectral data choose `H_odd`, its
parameters, or its eigenvalues before freeze, then the carrier/slot did
not supply them. E3 fails.

Doc 45 E4 requires a contentful comparison theorem between independent
candidate-side evaluations. If the agreement locus, normalization,
constants, signs, positive cone, class family, or comparison theorem is
chosen because it matches zero-side data, then the target answer has
entered the construction. The comparison is not a supply-side theorem;
it is an explicit-formula or zero-side transport. E4 fails.

The same logic applies to validation before freeze. A choice that is
kept only because it matches zeros has been selected by zeros, even if
the formula was written down earlier. Therefore it belongs after the
freeze only as comparison or fork diagnosis.

Thus pre-freeze zero selection demotes the candidate. QED.

## 4. Allowed And Forbidden Uses

Allowed after freeze:

```text
comparison
  Compute the zero-side image of a frozen candidate quantity.

sanity check
  Check normalization or numerical scale after the candidate theorem is
  stated.

deformation control
  Test DH, beta != 1/2, smooth surrogates, or fork variants against
  the frozen formulas.

implication audit
  Ask whether the frozen package would imply RH.

fork diagnosis
  Decide whether a frozen match is merely EF-derived or carries extra
  information.
```

Forbidden before freeze:

```text
eigenvalue import
  Set H_odd eigenvalues from zero ordinates or fitted zero spectra.

sign import
  Choose signs, phases, repair atoms, units, or positive cones because
  they match zero-side signs.

locus import
  Select class families, test points, windows, or truncations after
  seeing zero data.

normalization import
  Choose kappa, Gaussian scale, Haar density, constants, or phases
  using zero-side agreement.

theorem import
  Define Compare by an explicit-formula identity whose load-bearing
  input is the zero expansion.
```

Classical analytic facts are not forbidden merely because they are
about zeta. The burden is to state why the fact is not equivalent to
importing zero locations, zero signs, RH-line spectral data, or the
zero side of the explicit formula as construction data.

## 5. Relationship To Existing Gates

```text
doc 14
  Fork protocol: matching a zero-side image is not new structure
  unless the frozen candidate carries extra information.

doc 45
  E3/E4 require unforced eigenvalues and a contentful Compare theorem.

doc 59
  Gives the broad zero-import circularity no-go and the G59 freeze
  ledger.

doc 60
  Uses this as G60.10, and also as a guard against fake G60.8/G60.9
  odd-slot or Compare data.

doc 61
  External answers that claim zero-free H_odd, Count, or Compare must
  be recorded before relaxing the freeze rule.
```

The resulting admission rule is:

```text
No zero-side data before construction freeze; no post-freeze zero
comparison may repair the frozen object.
```

## 6. Live Protocol Target

A surviving candidate must state:

```text
T_Z69 supplier ledger
  Each object, parameter, class, locus, unit, sign, and comparison has
  a zero-free supplier.

T_Z69 freeze record
  The formulas, files, constants, witness commands, and proof-local
  definitions are fixed before zero contact.

T_Z69 zero-contact declaration
  The first zero use and its role are named.

T_Z69 no-repair rule
  Post-freeze zero comparison may classify the candidate but cannot
  tune or repair it.
```

Only after T_Z69 is present should zero-side comparison or fork tools
be run.
