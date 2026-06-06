# PA — re-couple COUNT and RADIUS via a SINGLE archimedean Frobenius

[ATTACK · coherence-checked vs F_q · 2026-06-06]
Module: `scripts/numerics/witness/recouple_count_radius.py` (FF anchor COMPUTED; the three attempts COMPUTED/type-checked; off-line plant breaks the radius while preserving the count-scale; no zeros assumed on the radius axis). Built on R10 (the count/radius split at the trace-class level) and `frobenius_self_norm.py` (the polarization relation `F F^dag = q Id`).

## The angle (R10's terminus, attacked head-on)

Over F_q the geometric Frobenius `F = x^q` does BOTH jobs from the SAME q:
- COUNT: `#C(F_{q^n}) = q^n + 1 − Tr(F^n | H^1)` (Lefschetz; F's TRACE is the point-count);
- RADIUS: `|alpha_i| = q^{1/2}` (purity; F's eigenvalue MODULUS is the radius).

R10's terminus: at infinity compactness (Connes) supplies the COUNT (regularized trace = explicit formula) but the RADIUS DECOUPLES — a separate input (purity / FE-fixed locus, pinned only by Weil positivity = RH). PA's mandate: construct a SINGLE archimedean operator `F_inf` whose TRACE gives the count AND whose EIGENVALUE-MODULUS gives the radius — the archimedean analogue of "F = x^q does both." Anchor on F_q, falsify DH.

## What was actually built

A minimal model on `H^1` (rank 2g, conjugate-paired Weil numbers), with the COUNT data (`Tr(F^n)`, `det F`) and the RADIUS data (`|alpha_i|`) separated, plus an off-line plant that preserves the count-scale `det F = q^g` (FE partner radii multiply to q) while breaking purity. Three concrete re-coupling attempts were defined and COMPUTED:

- **[A] count → radius via the determinant.** `det F = q^g` is the count-scale (leading coeff of the L-function). It forces only the **geometric mean** of the moduli, `(det)^{1/2g} = q^{1/2}` — COMPUTED `2.6458 = sqrt(7)`. The radius is the **per-eigenvalue equality case** `|alpha_i| = sqrt(q)` for EACH i (the AM–GM equality), which the count NEVER forces: the off-line config has the SAME `det = q^g` (count-scale `49.0` for both) and a broken radius (`max dev 0 → 1.6`). FAILS.

- **[B] why x^q couples them — and no archimedean analogue.** `x^q` is a RING ENDOMORPHISM of a finite field: the single arithmetic q is BOTH the field size (⟹ Lefschetz count ~ q^n, the trace source) AND the q-th-power SCALING (⟹ modulus = q^{1/2} on the half-weight line, the radius source). At infinity the continuous field automorphisms (identity, conjugation = the COUNTING/Galois maps) are **isometries** (all eigenvalue moduli = 1, COMPUTED, NO scaling); the SCALING (modulus character `|.|^s`) is NOT a field endomorphism and has NO fixed points (NO count). Counting and scaling are carried by DIFFERENT, orthogonal archimedean operators. FAILS.

- **[C] graded / tensor repair.** `F_inf = U ⊗ m` (U unitary = the count/phase carrier `Tr U^n` = the location data; `m > 0` = scaling on the weight line = the radius). COMPUTED: the count `Tr(U^n)` is INVARIANT under rescaling m (`[2.806, 0.059, −2.381]` for both true and wrong m; eigenvalue moduli `2.6458` vs unchanged structure). The grading does NOT re-couple — it makes the decoupling MANIFEST (count in the U-factor, radius in the scalar m). Forcing `m = sqrt(q)` is exactly `F_inf F_inf^dag = q Id` (U unitary AND m²=q) = the polarization relation = purity = RH. FAILS (circular).

## The decisive new content (PA's sharpening of R10)

R10 said "compactness gives the count, the radius is a separate input." PA names WHY the single-operator coupling cannot be repaired, as a precise two-part fact:

> **The decoupling is an AM–GM equality fact crossed with a ring-endomorphism fact.**
> The count (a TRACE/determinant — additive, Lefschetz) fixes only the **geometric mean** `(det F)^{1/2g} = q^{1/2}` of the moduli. The radius is the **equality case** `|alpha_i| = sqrt(q)` for every i. Over F_q the equality is FORCED because `F = x^q` is a **ring endomorphism**: its single q is simultaneously the field size (count) and the scaling power (radius), so the trace-source and the modulus are the SAME arithmetic number by construction. At infinity there is NO ring endomorphism that scales — the Galois/counting maps are isometries (modulus 1) and the scaling modulus-character has no fixed points (no count) — so the equality case is NOT forced by the count; it is an EXTRA input, and the only operator relation that supplies it, `F_inf F_inf^dag = q Id`, IS purity = RH.

This ties R10's "count vs radius" split directly to the type obstruction (R8): COUNT is a trace (additive); RADIUS is a multiplicative scaling; the F_q coupler is a ring map fusing additive and multiplicative q; the archimedean place has no such map, and "supply one" = "supply the polarization relation" = RH.

## Falsifier verdict (PA — a re-coupling attempt, classified; Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Anchors at F_q and type-checks the archimedean operators; not a standalone Z-positivity. DH structural verdict SHARP: no Euler product ⟹ no Frobenius / no Satake ⟹ no operator whose trace is a Lefschetz count ⟹ NOTHING to be the "count-source" of ⟹ the re-coupling question is UNPOSABLE for DH (the `F_inf` to re-couple does not exist).
- **SEES-ZEROS — YES.** The sought radius = purity = where the zeros sit; the off-line plant breaks it (radius dev `0 → 1.6`) while the count-scale `det = q^g` is preserved.
- **INDEPENDENT — NO.** Forcing `m = sqrt(q)` = `F_inf F_inf^dag = q Id` = the polarization relation = purity = RH (Connes/Weil).

→ classifier verdict **DISPERSING-by-design / CIRCULAR** (a terminus-characterizer; the re-coupling reduces to the polarization relation = RH). **Ladder `DH < ζ < FF`:** DH — no Frobenius ⟹ no count-source ⟹ the re-coupling unposable; ζ — the count (regularized trace, Connes) EXISTS but the radius is the per-eigenvalue equality case the count never forces, supplied only by `F_inf F_inf^dag = q Id` = RH; FF — `F = x^q` a ring endomorphism whose single q is field-size (count) AND scaling-power (radius), so the equality case is forced by construction (the modulus IS the trace-source).

## Verdict

**DEAD_END (with an exact, named reason).** The construction — a single archimedean `F_inf` whose trace gives the count and whose modulus gives the radius — does not exist independently of RH, and the reason is exact and twofold: (1) the count is a trace/determinant fixing only the **geometric mean** of the moduli, while the radius is the per-eigenvalue **AM–GM equality case** the count never forces; (2) over F_q the equality is forced only because `x^q` is a **ring endomorphism** fusing the additive field-size (count) and the multiplicative scaling-power (radius) into one arithmetic q, and the archimedean place has no scaling field-endomorphism — its Galois/counting maps are isometries and its scaling character has no fixed points. The only operator relation that re-couples them, `F_inf F_inf^dag = q Id`, is purity = RH (CIRCULAR). This does NOT prove no future non-commutative/graded structure could supply the equality — it pins the open problem to its sharpest single-operator form: **supply, at infinity, a single map whose multiplicative scaling (modulus) equals its additive trace-source (count)** = the archimedean ring-endomorphism `x^q` has no isometry-distinct, fixed-point-having analogue, and substituting the relation `F_inf F_inf^dag = q Id` for the missing ring map is RH itself.

**Not overclaimed:** PA classifies the single-archimedean-Frobenius re-coupling (count → radius FAILS by AM–GM; no archimedean ring-scaling map; the graded repair makes the split manifest and reduces to the polarization relation = RH). It does not claim no non-commutative structure exists; it identifies the exact type wall (additive trace vs multiplicative scaling, fused by a finite-field ring endo, absent at infinity).

**Successor:** the residue stays where R11 left it — purity ON Connes' discrete spectrum as an archimedean `N` / Hodge–Riemann positivity that is the modulus bound, not the count. PA adds: any such positivity must enforce the AM–GM **equality case** (per-eigenvalue `|alpha|=sqrt q`), not merely the geometric-mean/determinant constraint the count already gives — i.e. it must be the equality clause of a Hodge–Riemann bilinear relation, the one place a per-eigenvalue modulus bound is a positivity rather than a count.
