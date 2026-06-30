# 04 — the self-product does not escape the pole; W2 closes toward fundamental

Status: NO-GO with named mechanism, 2026-06-29. Closes the decisive weak link
W2 of doc 03 (the fundamentality investigation). Deliverable type: no-go
(DISCIPLINE sec 1b).

Named mechanism: **finite ⟺ alternating ⟺ transcendental.** A finite diagonal
self-intersection requires the alternating/Tate (derived) structure, which over
Z yields the archimedean transcendental −ζ'(0)/log b; an integer requires the
non-alternating ceiling, which diverges. The genuinely 2-dimensional content
(H¹⊗H¹) of the self-product is the WORST case — a double pole. The square does
not supply the properness that would truncate the tower; it inherits
non-properness twice. So no 2-variable regularization escapes to a finite
integer: W2 does NOT leak.

## The W2 question (the decisive fork from doc 03)

doc 02 showed the 1-variable regularized total of CC's integer dimension
diverges (simple pole at s=0, residue r = −1/(2 log b)). doc 03 reduced
fundamentality to W2: is `⟨Δ,Δ⟩` the 1-variable tower (divergent), or does a
2-variable self-product zeta have a finite value at the origin — and if finite,
INTEGER (leak → construction handle) or transcendental (no leak → bounded
negative)?

## The probe (three natural 2-variable models + the derived comparison)

Built from the 1-variable defect `D_δ(s) = r/s + FP + O(s)`, r = −1/(2 log b)
certified (prime_cc_quantization_defect). The genuine 2-dimensional part of the
intersection form is built from the defect (the obstruction-carrier); the smooth
log part is the FE-layer pullback.

```text
M1  product (H^1 (x) H^1, the genuine 2-dim intersection content):
      Z_x(s,t) = D_δ(s) D_δ(t);  diagonal Z_x(s,s) = r^2/s^2 + ...
      => DOUBLE pole, leading coeff r^2 != 0. The square is WORSE than the curve.
M2  additive (mixed pullback (+) defect):
      Z_+(s,t) = D_δ(s) zeta(t) + zeta(s) D_δ(t);  zeta(0) = -1/2 (finite),
      diagonal = 2 zeta(s) D_δ(s) = -r/s + ...  => SIMPLE pole, residue -r != 0.
M3  antisymmetric / normal bundle (the STANDARD geometric route to a finite
    self-intersection -- the transverse/normal direction to the diagonal):
      transverse derivative of [D_δ(s) - D_δ(t)] = -r/(s t) + ...
      => DOUBLE pole on s=t, coeff -r != 0. Even the normal-bundle route diverges.
DERIVED (alternating/Tate, doc 18): V = -zeta'(0)/log b = (log 2pi)/(2 log b),
    FINITE but the archimedean TRANSCENDENTAL -- certified NOT an integer
    (b=2: V=1.3257, dist to nearest int 0.326; b=3: V=0.8365, dist 0.164).
```

**Verdict (Certified, gf_selfproduct_pole_escape, exit 0):** every natural
2-variable model is polar on the diagonal at the origin (coeffs nonzero
multiples of r); the only finite self-intersection is the derived transcendental;
**no model yields a finite integer.** Outcome (a)+(b) of doc 03; outcome (c)
(the leak) is ABSENT.

## Why (the structural reason — this is the content)

```text
A finite diagonal self-intersection is, in any cohomological theory, an
ALTERNATING sum over a TRUNCATED (proper) cohomology -- Lefschetz: <Delta,Delta>
= Sum (-1)^i Tr(F | H^i), finite because properness makes the H^i finite. Over
F_q this gives the integer 2-2g.

Over bar(Spec Z) there is NO PROPERNESS (the square is affine over S; the Ext /
homotopy tower never truncates -- doc 18/19's named wall). So <Delta,Delta> is an
INFINITE tower sum, and it has exactly two fates:
  - regularize it with the ALTERNATING / Tate structure -> finite, but the value
    is the archimedean constant -zeta'(0)/log b, TRANSCENDENTAL;
  - keep it INTEGER (the non-alternating ceiling) -> the sum diverges.
The 2-variable square does not add properness; it adds a second factor of the
same non-proper tower, so the genuine 2-dimensional content (M1) DOUBLE-diverges.

This is the properness wall (doc 18/19) and the carrier wall (doc 02), now seen
a third way: the archimedean place forces a transcendental regularization for any
finite self-intersection, which is irreconcilable with integrality. F_q has no
archimedean place, hence no tension, hence the integer form. The dichotomy is the
arithmetic of one missing place.
```

## Carrier guard (DISCIPLINE sec 4) — PASS

The transcendental value −ζ'(0)/log b is the archimedean datum (FE-layer,
DH/Epstein-shared); the integer side dies on the controls by non-existence
(divergence). Neither side is a false carrier; the wall is that no side is both.

## DOF / Freeze / Scope

```text
DOF (G-INT6): the pole coefficients (r^2, -r) and the finite value (1/log b
  factor) are base-laden -- a would-be integer self-intersection is calibration.
Freeze: no zero data; -zeta'(0) is the archimedean constant, named, not imported.
Scope: bounds the route (no additive 2-variable self-product gives a finite
  integer intersection form), NOT RH. Certified for the natural models + the
  additive class; "no exotic non-additive escape" is Reading (residual scope).
  Existence => RH, not iff: a fundamentality theorem here does NOT disprove RH.
```

## Convergence check (DISCIPLINE sec 7) — FIRES (fifth venue), and CLOSES W2

```text
finite<=>alternating<=>transcendental = the PROPERNESS wall (doc 18/19) = the
carrier wall (doc 02) = the integrality-summability dichotomy (doc 02/03). FIVE
venues now (analytic 132-136; homotopic 138-340; CC-Frobenius-free doc 01;
CC-integer-dim doc 02; self-product doc 04), one wall, same shape.

CRUCIALLY: this CLOSES the decisive weak link W2 from doc 03 in the
NON-LEAK direction. The self-product does not rescue integrality; it doubles the
obstruction. The fork resolves toward BOUNDED-NEGATIVE.
```

## Updated state — fundamentality now rests on one low-risk lemma

```text
doc 03 gated the bounded-negative pivot on closing W1 (the elementary sawtooth
lemma) AND W2 (this probe). W2 is now CLOSED (no leak). Remaining:
  W1 (LOW risk): "the sawtooth part of (integer staircase - log_b) is regular at
     s=0" for general staircases -- a standard Mellin lemma; the combinatorial
     core (geometric jump density 1/log b) is already Census-certified
     (gf_dichotomy_jump_density). This is the ONLY obstacle left to writing the
     fundamentality theorem (within the additive class).
The two-sided theorem is otherwise assembled: side A (scale-aware => non-summable)
modulo W1; side B (scale-blind => no content) = Efimov arXiv:2405.12169, proven.
```

## Witness

```text
Certified (new, lead-run this cycle, exit 0):
  python3 -m scripts.numerics.witness.gf_selfproduct_pole_escape   [ALL PASS]
  -- M1 double pole (r^2), M2 simple pole (-r), M3 normal-bundle double pole
     (-r), all nonzero; derived value -zeta'(0)/log b finite and certified
     non-integer for b=2,3. No 2-variable model yields a finite integer.
Reused/cited: prime_cc_quantization_defect (r); gf_dichotomy_jump_density (W1
  combinatorial core); Efimov arXiv:2405.12169 (side B).
```

## Recommendation (updated)

```text
The decisive fork has resolved toward BOUNDED-NEGATIVE. The honest next step is
the one remaining low-risk lemma W1; on closing it, the program can write the
fundamentality theorem:

  "No additive/localizing integer dimension theory over bar(Spec Z) yields a
   finite integer intersection form on the self-product carrying the archimedean
   datum -- equivalently, integrality and archimedean regularization cannot share
   one canonical (additive) object; finiteness forces the transcendental
   -zeta'(0), integrality forces divergence."

This is the CHARTER's bounded-negative branch, within the canonical/additive
class that contains every tested construction. It does NOT disprove RH. The one
genuine escape it leaves open -- a canonical-but-non-additive integer
intersection form -- is in tension with the rigidity spec S1 (the squeeze, doc
03). Recommend: a focused cycle to prove W1, then draft the theorem.
```

## Next

Cycle (W1): prove the general-staircase sawtooth-regularity lemma (Mellin
transform of a bounded log-periodic function is regular at s=0; the geometric
atom set carries the only s=0 pole). On success, draft the fundamentality
theorem as the program's bounded-negative result and bring it for review before
any full pivot.
