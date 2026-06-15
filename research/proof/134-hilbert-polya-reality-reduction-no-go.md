# 134 - The Hilbert-Polya / reality route reduces to the radius wall

Status: no-go + characterization, 2026-06-15. Fourth post-reset cycle,
executed inline by the lead (no fan-out). It resolves the one residue
doc 133 left open -- the non-Frobenius / Hilbert-Polya purity mechanism
(UNKNOWN, not excluded) -- by showing it is NOT a new door: it reduces to
the same missing object as the radius, it cannot be imposed by axiom
(a confirmed no-go), and its UNKNOWN narrows to a single named target.

Witnesses (lead-reran this cycle, all exit 0):
`cstar_hermitian_witness` (off-line admits a consistent Krein-indefinite
Hermitian self-duality; positive-definiteness is a strict extra
restriction => positivity IMPORTED => NOGO_COMPLETE),
`positivity_reality` (the residual gap theta F theta = F* is a PHASE/line
condition arg m; the only unconditional positivity, the sym^2 norm-square,
controls the MODULUS/edge, the wrong half -- RH-SILENT),
`frobenius_self_norm` (the wall pins to ONE operator relation, the positive
Rosati involution F^dag = (deg) F^{-1} on a correspondence algebra
End(S^2/Z), present over F_q, absent over Z),
`operator_domination` (Sylvester's law locks every invertible *-congruence;
26 Euler-product confirmations),
`polarization_relation` (F F^dag = c.Id = the functional equation, free /
RH-silent / holds for Davenport-Heilbronn).

## 1. Purpose

Doc 133 sec 6 left a residue: a non-Frobenius purity mechanism (a
Hilbert-Polya / self-adjoint construction carrying no q) is UNKNOWN, not
excluded -- it is what forbids the "irreducibly Frobenius-weight" necessity
claim. This doc attacks that residue directly and asks: is the
Hilbert-Polya / self-adjoint route a genuinely new way to supply the
radius (= purity = reality), or does it reduce to the banked wall?

## 2. Covered Class

```text
- Hilbert-Polya / self-adjoint operator constructions whose spectrum is the
  zeros and whose REALITY (eigenvalues real <=> zeros on Re s = 1/2) is
  proposed as a forcing datum;
- Hermitian / *-autonomous / dagger / C*-tensor self-dualities imposing a
  POSITIVE Hermitian pairing BY AXIOM (Doplicher-Roberts route);
- any positivity certificate built from a MODULUS / norm-square
  (sym^2 |h|^2, the L(1,sym^2) Siegel datum, Arakelov h_NT).
```

It does NOT cover (sec 6) an Euler-borne PHASE / argument-principle
certificate for arg m -- the single named object this no-go isolates.

## 3. Lemma

```text
Lemma 134.1 (the reality route reduces to the missing Rosati algebra, and
positivity-by-axiom imports RH). Let the radius (= even split = purity) be
restated in operator form as the REALITY datum theta F theta = F*
(eigenvalues real / arg m trivial / the line Re s = 1/2). Then:

  (R) [the phase face of the same gap] theta F theta = F* is a PHASE
      condition on arg m (the LINE), exactly as the radius is a MODULUS
      condition on the Satake split (the EDGE-vs-SPLIT of doc 132/133 with
      modulus replaced by phase). Both share the SAME free half: the
      relation F F^dag = c.Id = the functional equation, which is RH-silent
      (holds for Davenport-Heilbronn). The RH content is the positivity /
      phase half in both.

  (X) [positivity-by-axiom is a no-go] Off-line, F admits a consistent
      NON-DEGENERATE INDEFINITE (Krein) Hermitian self-duality. Demanding a
      POSITIVE-definite (C*/dagger/polarization) Hermitian self-duality is a
      STRICT EXTRA RESTRICTION that fails exactly off-line -- so imposing
      Hilbert-Polya positivity by axiom IMPORTS RH. [cstar_hermitian_witness
      = NOGO_COMPLETE.]

  (A) [forcing positivity needs the missing algebra] The non-axiomatic
      route -- force theta F theta = F* from structure -- pins to ONE
      operator relation: the positive Rosati involution F^dag = (deg) F^{-1}
      (the deg-q polarization making F F^dag = q.Id an identity in
      End(Jac)). Over F_q that correspondence algebra EXISTS (giving the
      unconditional self-norm 2gq) and its positivity is RH. Over Z there is
      NO such algebra (no correspondence on S^2/Z); the only available
      self-norm is the Hilbert sum over zeros = RH-conditional, and the
      unconditional substitute (Arakelov h_NT) is the WRONG divisor
      (RH-silent). [frobenius_self_norm.]

Hence the Hilbert-Polya / reality route supplies no new radius datum: it is
the phase face of the radius gap, it cannot be axiomatized without importing
RH, and forcing it requires the SAME missing positive-Rosati correspondence
algebra End(S^2/Z) that the radius needs.
```

Verdict label:

```text
REALITY_ROUTE_REDUCES__POSITIVITY_BY_AXIOM_IMPORTS_RH__FORCING_NEEDS_MISSING_ROSATI_ALGEBRA.
```

## 4. Proof

(R) `positivity_reality` (exit 0): theta F theta = F* requires arg m trivial
(the line Re s = 1/2). On-ramp (b): the one unconditional positivity, the
sym^2 square-modulus m = |h|^2 . phase, fixes |m| = |h|^2 (the MODULUS, the
edge Re s = 1, the L(1,sym^2) Siegel bound) but leaves arg m FREE -- the
off-line plant moves a resonance (flips the phase) without changing the edge
modulus. So the banked unconditional positivity supplies the WRONG HALF.
On-ramp (a): the reality reduces, modulo the unconditional windowed part, to
the prime tail = the cross-place coupling W_infty >= Sum_p W_p -- which is
the standing wall itself (CIRCULAR, not independent). This is the SAME
edge->line gap as the radius, now modulus->phase. `polarization_relation`
(exit 0) supplies the free half: F F^dag = c.Id = the FE, RH-silent (DH).

(X) `cstar_hermitian_witness` (exit 0): on-line the Hermitian self-duality
is positive-definite; off-line and off-line2 it EXISTS but is indefinite
(signature (3,3), rank 6) -- a consistent Krein structure. Positive-
definiteness is therefore not a consequence of the *-structure; it is a
strict extra axiom that holds iff on-line. Imposing it = importing RH.
VERDICT NOGO_COMPLETE. (This is the C-side analogue of doc 130 case C /
doc 132 case C: `operator_domination` confirms Sylvester's law locks every
invertible *-congruence across 26 Euler-product instances.)

(A) `frobenius_self_norm` (exit 0): <F,F> = deg(F) splits into the algebraic
Rosati 2gq (unconditional, Arakelov h_NT, RH-SILENT, wrong divisor) and the
Hilbert sum |alpha|^2 (RH-conditional, CC20 archimedean diagonal). The two
are separated by exactly ONE relation -- the algebraic-Rosati identity
F^dag = q F^{-1} -- which over F_q makes F F^dag = q.Id an operator identity
in End(Jac) and whose positivity (F^dag = F*) is RH. Over Z there is no
correspondence algebra End(S^2/Z), so the forcing channel is absent and only
the RH-silent value survives. The missing object is the positive-Rosati
correspondence algebra. []

## 5. The unification: all post-reset cycles are one wall

```text
The three post-reset no-go cycles are three FACES of one missing object --
the positive-Rosati correspondence algebra End(S^2/Z) (= a proper
self-product carrier over Z, the Connes-Consani C x C / scaling-site
Jacobian):

  doc 130  SECOND EVALUATION   the odd slot is empty/self-supplied without a
                               properness/Poincare-duality truncation;
  doc 132/133  RADIUS (MODULUS) the even split |alpha|=|beta| is the acting
                               map's own modulus; the EDGE/FE is free;
  doc 134  REALITY (PHASE)     theta F theta = F* is arg m / the line; the
                               MODULUS/FE is free; positivity-by-axiom = RH.

In every face the FE / edge / modulus / relation half is FREE and DH-shared
(RH-silent); the RH content is the split / phase / positivity half; and
supplying it requires the same End(S^2/Z) with positive Rosati involution
F^dag = (deg) F^{-1}, which exists over F_q (Frobenius) and is absent over Z
(affine square, no Frobenius, doc 18). The program's whole residue is this
ONE algebra.
```

## 6. Surviving Escape

The UNKNOWN residue of doc 133 narrows from "some non-Frobenius mechanism"
to a SINGLE named, attackable, zero-free object:

```text
PHASE-CERT (the argument-principle positivity). An Euler-borne certificate
  for arg m (the winding / spectral count / the line Re s = 1/2) -- a
  phase/argument-principle positivity, NOT a modulus/norm-square. The banked
  unconditional positivity (sym^2 |h|^2) provably controls the modulus, the
  wrong half (positivity_reality on-ramp b); PHASE-CERT must control the
  phase from the prime data directly. This is the operator-side name for the
  missing positive Rosati involution: F^dag = (deg) F^{-1} carrying the
  phase, not the modulus.
```

It is RH-equivalent in content (the phase / reality IS the line condition),
so it RELOCATES the wall to a single named object rather than dissolving it.
Any PHASE-CERT proposal must pass the kill-tests (DH-silent on the modulus
half; not imposed by axiom; Euler-borne; freeze-honored).

## 7. Kill Conditions

```text
KILL-REAL.1 positivity-by-axiom
  the construction imposes a positive Hermitian / C* / dagger self-duality
  by axiom; off-line admits a consistent Krein-indefinite structure, so the
  axiom holds iff RH. Witness: cstar_hermitian_witness (NOGO_COMPLETE).

KILL-REAL.2 modulus-positivity for a phase condition
  the certificate is a norm-square / modulus bound (sym^2, Siegel, h_NT); it
  controls |m| (the edge), never arg m (the line). Witness: positivity_reality
  (on-ramp b RH-SILENT), frobenius_self_norm (algebraic Rosati = wrong divisor).

KILL-REAL.3 missing-algebra evasion
  the construction claims a self-adjoint forcing without supplying the
  positive Rosati involution F^dag = (deg) F^{-1} on a correspondence algebra
  End(S^2/Z); over Z that algebra is absent and the self-norm is a sum over
  zeros (RH). Witness: frobenius_self_norm.
```

Do not apply this no-go to a PHASE-CERT proposal (sec 6) -- an Euler-borne
argument-principle certificate for arg m -- which is the surviving frontier.

## 8. Board

```text
Reality / Hilbert-Polya route, cycle 4:
  REALITY_ROUTE_REDUCES__POSITIVITY_BY_AXIOM_IMPORTS_RH__FORCING_NEEDS_MISSING_ROSATI_ALGEBRA.
  The non-Frobenius purity residue of doc 133 is the PHASE face of the radius
  gap; it cannot be axiomatized (cstar_hermitian NOGO_COMPLETE); forcing it
  needs the same missing positive-Rosati End(S^2/Z).

Unification:
  docs 130 (second evaluation), 132/133 (radius/modulus), 134 (reality/phase)
  are three faces of ONE missing object: the positive-Rosati correspondence
  algebra End(S^2/Z) (CC C x C / scaling-site Jacobian). FE/edge/modulus free
  and DH-shared in every face; the RH content is the split/phase/positivity.

Surviving frontier (the single named object):
  PHASE-CERT -- an Euler-borne argument-principle certificate for arg m
  (the winding / line), the operator-side form of F^dag = (deg) F^{-1}
  carrying the phase. RH-equivalent; unbuilt.

Next valid work:
  attack PHASE-CERT directly (the phase/argument-principle positivity), OR
  build End(S^2/Z) with a positive Rosati involution (the CC C x C /
  scaling-site Jacobian) -- with a runnable witness. Do NOT propose a
  positive self-duality by axiom (KILL-REAL.1) or a modulus certificate for
  the phase (KILL-REAL.2).
```
