# 130 - Second-evaluation no-go: no unforced odd slot without properness

Status: no-go theorem, 2026-06-15. First post-reset cycle (the
disciplined-narrowing front, doc 129). This unifies the row-by-row
verdicts of doc 42 (M-C), the lemmas of doc 65, and the operator-level
witness `zero_in_form_pairing` under one named mechanism, and ties the
located wall (properness) to the second-evaluation demand as a theorem.

Witness (lead-rerun, exit 0): `zero_in_form_pairing` -> VERDICT
RH-SILENT (axis2_sees_zeros False, axis3_independent False).

## 1. Purpose

Doc 45 clause E / BC-E3' requires a decision-grade SECOND EVALUATION:
a nonempty odd determinant/cohomological/spectral slot whose
eigenvalues are supplied by the carrier, not by the acting map
(doc 65 E4+E5). Doc 42 found that no banked carrier supplies one, and
its consequence #1 forbids re-sweeping the bank for a sleeper.

This document proves WHY, with a single mechanism, and states the exact
structural input a candidate must add. It is the second-evaluation face
of the program's located wall: properness / an S-level duality that does
more than reproduce the functional equation (doc 18, BB.1, STRATEGY
sec 1).

## 2. Covered Class

The no-go covers any second-evaluation candidate whose carrier data is
drawn from the banked NON-PROPER classes:

```text
- finite-field / K(F_q) / TP at a point (affine, no zeros);
- THH or the derived square Z (x)^L_S Z (affine over S; the Ext tower
  is untruncated, doc 18);
- p-complete TP/TR/Witt transport;
- any pairing presented as a *-congruence T^* F T of a fixed
  FE-shared archimedean form F, or as functorial transport of one
  object's evaluation into another presentation.
```

It does NOT cover a candidate that supplies its odd slot through a
genuine properness / Poincare-duality truncation (sec 6).

## 3. Lemma

```text
Lemma 130.1 (no unforced odd slot without properness).
Let a candidate present a count evaluation Count and a spectral
evaluation Spec drawn from the covered class, with an agreement
Compare. Then exactly one of the following holds, and each fails
BC-E3' / doc-65 E4+E5:

  (C) Congruence/transport. Spec = T^* F T for an FE-shared form F and
      an invertible plant T, or Spec is a functorial transport of
      Count. By Sylvester's law of inertia, inertia(T^* F T) =
      inertia(F), independent of T's spectrum; transport likewise moves
      both sides together. The form cannot detect an off-line zero.
      [P3-a / P3-c fail; doc 65 secs 4-5.]

  (S) Self-supply. Spec is built from the plant's own entries (the
      non-congruence forms Omega = T - T^*, C = [T, T^*], or the
      FE-defect Omega_theta = T - Theta T^* Theta). Then its spectral
      parameter is the acting plant's own data; the carrier supplied no
      independent eigenvalue. [P3-c / E5 fail; doc 65 sec 6.]

  (E) Empty slot. The odd determinant/cohomology slot is zero
      (TP_odd(F_q) = 0; the affine square's Ext tower is untruncated).
      There is no eigenvalue to constrain. [E4 fails; doc 65 sec 7.]

Hence no carrier in the covered class supplies an unforced,
zero-seeing odd slot.
```

Verdict label:

```text
REJECT_AFFINE_SECOND_EVALUATION_FORCED.
```

## 4. Proof

(C) is the content of `zero_in_form_pairing`. Every self-pairing in the
banked family - symmetric `T^T A T`, real theta-twist `T^T A Theta T`,
Hermitian `T^T (A + iAJ) T` - has the shape `(plant)^* (fixed
DH-shared form)(plant)`. For invertible real `T` this is a
*-congruence, so by Sylvester's law of inertia the inertia of the
pairing equals the inertia of the fixed form `F` (the form built from
the DH-shared archimedean `A`), independent of `T`'s spectrum. The
witness plants the FE-forced Weil pair at `beta` and checks on-line
(`beta = 1/2`) against off-line (`beta = 0.6`): no inertia of any
`T`-built congruence form flips (RH-SILENT). The zeros enter only as the
congruence factor `T`, where Sylvester erases them. This is the
operator-level form of doc 65's transport lemma (sec 4).

(S) is doc 65 sec 6 (self-supply) made concrete. The escape from (C) is
to put the zeros into the FORM, via a non-congruence object built from
`T`'s own entries (`Omega`, `C`, `Omega_theta`). The witness computes
all three and finds their inertia does not flip either: the planted
overlap kernel is symmetric, so `Omega approx 0`, and where the forms
are nonzero their spectral parameter is `T`'s own data - the acting map
supplies the eigenvalue it was meant to query. P3-c / E5 fail.

(E) is doc 42 rows 1-2 and doc 18. `K(F_q)`'s two-evaluation embryo
`q^w - 1` is genuine, but `zeta(F_q, s)` has no zeros and
`TP_odd(F_q) = 0`; the odd slot is empty. Structurally: the diagonal's
self-intersection in `Z (x)^L_S Z` is `THH(Z)`, the square is AFFINE
over the sphere, and nothing truncates the Ext tower (doc 18) - so there
is no finite odd cohomology to carry an unforced eigenvalue. The
function-field forcing structure that DOES carry it (Frobenius
eigenvalues + Poincare duality + intersection positivity, STRATEGY
sec 1) lives on a PROPER surface, which the affine `Spec Z` square is
not.

The three cases are exhaustive for the covered class: a presented
second evaluation is either a congruence/transport of the shared form
(C), a non-congruence object built from the plant (S), or has no odd
slot at all (E). Each fails BC-E3'. []

## 5. Program Consequence

```text
1. The missing second evaluation is GATED by properness. The zeros can
   enter a decision-grade form only through a duality truncation that
   produces finite, unforced odd cohomology. Absent it, every candidate
   degenerates to (C), (S), or (E).

2. This is the same wall as the missing arithmetic object (doc 42 sec 3
   residue: ku-face supply + liquid address + index/Gram positivity +
   Quillen second-evaluation independence, merged by no object). The
   merger is blocked at exactly the properness/duality input.

3. Frontier engagement is now PROVEN-NECESSARY, not optional: any
   decision-grade second evaluation requires the Connes-Consani /
   scaling-site proper object (the only banked place an S-level
   Poincare duality could live), with a runnable witness.
```

## 6. Surviving Escape

A candidate escapes Lemma 130.1 only by supplying all of:

```text
E4' nonempty odd slot from a genuine properness / Poincare-duality
    truncation (finite odd cohomology that the affine bank lacks);
E5' eigenvalues fixed by that duality structure BEFORE the acting
    correspondence is chosen (not a congruence factor, not the plant's
    own entries, not an imported zero ordinate).
```

Equivalently: a non-congruence, non-self-supplied odd slot produced by
an actual S-level duality theorem. That theorem is the frontier; this
no-go converts "we have not built it" into "the second evaluation
cannot exist without it."

## 7. Kill Conditions

A future second-evaluation proposal is killed by this no-go when:

```text
KILL-2EV.1 congruence form
  the spectral form is T^* F T / a *-congruence of an FE-shared form;
  Sylvester locks its inertia (witness: zero_in_form_pairing).

KILL-2EV.2 self-supplied spectrum
  the form is built from the plant's own entries (Omega/C/Omega_theta)
  and its eigenvalue is the acting map's data.

KILL-2EV.3 empty / untruncated tower
  the odd slot is zero because the carrier is affine / a finite-field
  point / a p-complete transport with no duality truncation.
```

Do not apply this no-go to a proposal carrying a proved
properness/Poincare-duality truncation with carrier-fixed odd-slot
eigenvalues (sec 6).

## 8. Board

```text
Second-evaluation wall:
  REJECT_AFFINE_SECOND_EVALUATION_FORCED for the banked non-proper
  class; unified mechanism (Sylvester inertia-lock + self-supply +
  untruncated tower); witness zero_in_form_pairing RH-SILENT.

Doc-45 clause E / BC-E3':
  open only through E4'/E5' (a genuine S-level duality truncation).

Next valid work:
  engage the properness frontier (Connes-Consani proper object) with a
  runnable witness, OR harden an adjacent no-go; do not re-sweep the
  banked carriers (doc 42 consequence #1).
```
