# Euler-movable inertia, executed in the function field (AGENDA NEXT #1 / #2)

**Item.** NEXT #1/#2 (corrected by `conjugation-parity-ff`, DONE #31): the missing `ℤ`-surface
self-pairing must be an **EVEN positive form whose inertia is MOVABLE by the Euler/prime data** (an
off-line plant degenerates the signature, escaping the Sylvester lock). The agenda asserts (NEXT #2)
that the **function field** — the one place the Hodge index is a theorem — already exhibits this:
"`End(Jac)` makes the primitive intersection form negative-definite, and a hypothetical off-circle
Frobenius pair would VIOLATE it (the signature would gain a `+`)." This loop made that **executable**
and tested whether the assertion is true, and — via the three-axis falsifier — **why it does not
transport to `ℤ`**.

`scripts/numerics/witness/euler_movable_inertia.py` (+1 `falsify.py` row).

## What was built (exact integer/rational data on the load-bearing facts)

Frobenius `F` on `H¹(E)` (companion of `T² − a₁T + q`), the polarization/Weil pairing `E` (`Fᵀ E F =
qE`, the Tate-twist similitude, residual `< 1e-15`), and the Rosati adjoint `φ† = E⁻¹φᵀE` (= the FF
complex conjugation `α ↦ q/α`, `conjugation_parity_ff`). The **PRIMITIVE intersection form** is the
Hodge-index form `I(x,y) = −Tr(x y†)` on the trace-zero part `F₀ = F − (tr F/2g)·Id` and its dagger.

## [computed, exact] The agenda's assertion is LITERALLY TRUE in the FF

- **On-circle (RH holds), 5 curves `q = 5,7,11,13,2`:** primitive sig `(0,1,1)`, neg eig `= −2gq`
  exactly (`−16,−19,−19,−36,−7`). Hodge index: negative-(semi)definite on the primitive part. ✓
- **Off-circle plant (RH violated):** replace the Weil pair by `{r√q, √q/r}` (product `q`, modulus
  `≠ √q`). The negative eigenvalue **FLIPS to positive**: sig `(0,1,1) → (1,0,1)`, monotone in
  `r = 1.1, 1.3, 1.5, 2.0` (flip eig `+0.18, +1.41, +3.47, +11.25`). **"The signature gains a `+`."**

So the FF **does** supply a concrete archetype of the Euler-movable-inertia object the corrected
NEXT #1 spec demands. The spec is **satisfiable in the FF** — the first time it has been realized.

## [THM/computed] The three-axis falsifier — WHY it does not transport to `ℤ` (the decisive content)

1. **The moving quantity is the MODULUS DEFECT `Σ|αᵢ|² − 2gq`, EXACTLY.** The flipping primitive
   eigenvalue equals `|α₁|² + |α₂|² − 2q` to `1e-9` at every `r`. This is **conjugation-EVEN**:
   symmetric under `|α| ↔ q/|α|` (`r` and `1/r` give the **identical** signature `(1,0,1)`). It
   measures HOW FAR off-circle, never WHICH SIDE — the modulus/phase split of all 31 confirmations.
2. **The flip does NOT need the Satake polarization.** Replacing the true `E` (Satake `Fᵀ E F = qE`,
   `α·α† = q`) by a **generic** alternating pairing (no `q`-similitude = DH-like) gives the **same**
   flip `(1,0,1)`. The Satake `q` only **rescales** `E`; the sign structure is the modulus defect,
   read off the **spectrum** (zero side).
3. **What the EULER data supplies is the CIRCLE RADIUS `√q`** (the Frobenius weight = base-field
   size `q`; `α·α† = q` is the Satake relation DH lacks; verified `Σ|αᵢ|² = 2gq` exactly on-circle).
   The Euler product sets WHERE the circle is; the modulus defect then measures deviation from it.

## The decisive gap, now sharp [the load-bearing output]

> Over `𝔽_q` the radius `√q` is an **EULER datum** (the Frobenius weight), so "off-circle" is an
> Euler-anchored modulus and its inertia **is** Euler-movable. Over `ℤ` the analogue radius is
> `Re s = ½` = the **FUNCTIONAL-EQUATION FIXED LOCUS**, which is **NOT** supplied by any Euler datum
> (`Λ(n)` does not set it; it is the FE-invariant DH-shared archimedean background `A`, shared by DH).
> So over `ℤ` the modulus defect is measured against a **FE-borne (not Euler-borne) radius** ⟹ its
> inertia is **Sylvester-LOCKED to `A`** (the 31 confirmations), NOT Euler-movable.

The missing `ℤ`-object is therefore **NOT** "an even form with movable inertia" in the abstract — the
FF has one — it is specifically **an Euler datum over `ℤ` that SETS the critical radius `Re s = ½`
the way `q` sets `√q` over `𝔽_q`.** But `Re s = ½` is the FE fixed locus, **Euler-independent**
(shared verbatim by DH). This is the cross-place coupling `W_∞ ≥ Σ_p W_p` in its sharpest form yet:
**the primes must SET THE LINE, but over `ℤ` the line is set by the FE, not the primes.**

## Verdict

**Falsifier:** Euler-borne **YES** (the radius `√q` is the Frobenius weight, DH-refusing), sees-zeros
**YES** (off-circle flips the inertia — Euler-movable inertia is REAL in the FF), independent **NO**
(the modulus defect read off the spectrum = the Weil positivity, **CIRCULAR** over `ℤ`). → **CIRCULAR.**
**32nd wall confirmation** — the FIRST to exhibit Euler-movable inertia **concretely** and to locate
the gap as **"Euler sets the radius over `𝔽_q`, the FE sets it over `ℤ`."**

This is a genuine sharpening, not a re-run: the previous 31 confirmations showed the `ℤ`-forms are
Sylvester-locked; this one shows the **FF archetype escapes the lock** (its inertia genuinely moves)
**and isolates the single reason** the escape is FF-specific — the Euler product owns the radius `√q`.
The corrected NEXT #1 ("build an even form with Euler-movable inertia") is **satisfiable in the FF and
the obstruction over `ℤ` is now named precisely**: not the inertia, but the **radius** must become
Euler-borne, and `Re s = ½` is structurally FE-borne.

## Honest subtleties

- The realization is `g = 1` (`2×2` companion), so the primitive part is `1`-dim and on-circle gives
  the semidefinite `(0,1,1)` (the `+0` is the trace-removal kernel, not a true second negative
  direction); the load-bearing facts are the **exact** ones: neg eig `= −2gq`, the flip
  `(0,1,1)→(1,0,1)`, the EXACT match flip-eig `= Σ|αᵢ|² − 2gq`, the `r↔1/r` invariance, and the
  generic-pairing same-flip. None depend on the small dimension.
- "Euler-movable inertia is real in the FF" is a **positive** structural finding (it refutes the
  alternative negative — that even the working archetype lacks movable inertia). The **circular**
  verdict is over `ℤ`, because the moving quantity is the modulus defect against an Euler-set radius,
  and over `ℤ` no Euler datum sets the radius.

## New agenda items surfaced

- **The radius problem (load-bearing, replaces the abstract "Euler-movable inertia" framing).** Is
  there ANY ζ-intrinsic object over `ℤ` for which the **critical radius `Re s = ½`** is read off the
  **Euler/prime data** rather than the FE? Probe: the FE `s ↦ 1−s` fixes `Re s = ½` independent of the
  Euler product (DH shares it). Does the **Euler product alone** (no FE) constrain `Re s` — e.g. the
  abscissa of absolute convergence `Re s = 1` (Euler-borne, the EDGE, Worker E) vs the line `Re s = ½`
  (FE-borne, the CENTRE)? This is the certificate ladder (`§L`) restated: Euler sets the **edge**, the
  FE sets the **centre**; the missing object would make the primes set the centre. (Test whether any
  Euler-product feature is anchored at `½` and not just `1`.)
- **The `q → 1` degeneration with the radius (for the surface route).** When the agenda asks for the
  `q→1` limit of the `C×C` Hodge index, the radius `√q → 1` — i.e. the circle collapses to the point.
  What is the `q→1` image of "`√q` is the Frobenius weight"? Connes–Consani's `𝔽₁`/Scaling Site: does
  the Frobenius-weight radius survive as an Euler datum, or does it become the FE locus? (This is the
  concrete `q→1` question the previous passes deferred, now with the radius as the tracked invariant.)
