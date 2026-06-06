# RH Research Agenda — autonomous loop

The `research-loop` workflow does the **top item under NEXT**, commits a result, moves the item to
DONE with a one-line finding, and appends any new items its work surfaced. Re-invoke the workflow to
continue. The agenda is the program driver; keep NEXT prioritized (load-bearing / falsifiable first).

**DISCIPLINE (every item).** §8 — certify load-bearing numerics (python-flint/mpmath, no bare floats),
never overclaim, **honest negatives are valuable** ("RH-silent" / "circular" / "the spec fails" are
real findings). Run every positivity candidate through `scripts/numerics/witness/falsify.py`'s three
axes (Euler-borne / sees-zeros / independent). Tag [THM] / [CONJ] / [computed]. Standing context: the
method is the bridge-building loop (`research/method.md`); the frontier is **RH ⟸ a self-product
surface over `Spec ℤ` whose self-intersection is the Petersson norm `‖f‖²`** (`research/work/
F-sym2-os-bridge.md`); the wall is the cross-place coupling (8 Euler-product confirmations,
`research/positivity-program.md` §E–L).

## NEXT

1. **[BACK UP TO PASS TWO · HIGH · load-bearing]** **A5 is refuted in the function field** (see DONE #1):
   the Weil self-intersection forcing the line is an **Euler characteristic times `q`** (`Δ·Δ=2−2g`,
   `Γ_q·Γ_q=q(2−2g)`), **NOT** the Petersson norm `‖f‖²`; `‖f‖²` is a *separate* RS L-value
   (Yun–Zhang `=L^{(r)}(1/2)` on Shtukas, or the Arakelov `s=1` residue) that is **Gross–Zagier /
   RH-silent**. So the pass-two axiom "self-intersection `=‖f‖²`" pins the surface to the **wrong
   number**. **Re-run `method.md` step 2 with the CORRECTED mechanism:** the line-forcing object is the
   **`q`-scaled Euler characteristic / the `Γ_q·Γ_q = q·Δ·Δ` relation** (the degree of Frobenius),
   *not* a Petersson norm. Re-axiomatize: what over `ℤ` plays the role of `Γ_q·Γ_q = q·(Δ·Δ)` — the
   self-intersection that **carries the factor `q=#𝔽_q` whose root is the line**? (This is the
   continuous-Frobenius `Δ·Δ=∞` corner, auditor row 1 — but now we know the *right target number*: a
   `q`-scaled self-intersection, not `‖f‖²`.) Where does `‖f‖²` legitimately enter, if at all (it may
   be RH-silent scaffolding, not the forcing input)?
2. **[ANCHOR]** Verify the analog in the **Selberg / hyperbolic-surface** case: does the line-forcing
   quantity there (the spectral parameter / Selberg-zeta resonance condition, self-adjoint Laplacian)
   coincide with the Petersson/Maass norm, or — as in the function field — is the norm a *separate,
   RH-silent* central value while the line is forced by a different (self-adjointness) mechanism? Predict
   from DONE #1: the norm and the line-forcing are DISTINCT; confirm or break.
3. **[CONSTRUCT]** Condensed **stack-of-norms** (Clausen–Scholze / F. Charles): can it realize a
   surface over `\overline{Spec ℤ}` with self-intersection `= ‖f‖²`? Where exactly does the
   "archimedean Deligne–Illusie ⟶ Kähler" open question sit relative to this target?
5. **[CONSTRUCT]** **Tropical / Connes–Consani** square: the diagonal self-intersection in the `q→1`
   limit — does it carry the `‖f‖²` target, and where does it diverge?
6. **[CONSTRUCT · representability]** Is **"the square root of the Rankin–Selberg/Petersson
   edge-positivity"** functor representable (Brown representability / a moduli description)? What object
   would represent it?
7. **[DEFORM]** Trace the `C×C` Hodge index through the `q→1` degeneration explicitly; identify the
   **obstruction-cocycle** (what breaks) — that names the next axiom (pass-four input).

> **CAVEAT on items 3–7 (post DONE #1):** all five were written with the **`‖f‖²` self-intersection
> target**, which DONE #1 refuted. Their "self-intersection `=‖f‖²`" target must be replaced by the
> **corrected target from item 1** (the `q`-scaled Euler-characteristic self-intersection `Γ_q·Γ_q =
> q·Δ·Δ`). Do item 1 FIRST; then these become "construct the *corrected* target."

## DONE
(the loop appends here, newest first)

- **2026-06-06 — A5 in the function-field case: REFUTED (false weld).** [ANCHOR · load-bearing →
  honest negative]. `scripts/numerics/witness/a5_function_field.py`,
  `research/log/2026-06-06-a5-function-field-refuted.md`. **Finding [THM+computed]:** Weil's
  line-forcing self-intersection on `C×C` is `Δ·Δ=2−2g` / `Γ_q·Γ_q=q(2−2g)` — an **Euler characteristic
  times `q=#𝔽_q`**, with NO modular form in it — verified yielding `|α|=√q` on elliptic curves (q=5,7,
  11,13). It is **NOT** the Petersson/Rankin–Selberg residue `‖f‖²`. The genuine "self-intersection =
  RS L-value" theorem over `𝔽_q` is **Yun–Zhang** (Shtukas; `=L^{(r)}(1/2)`) — a **DERIVATIVE at `s=1/2`
  on moduli of Shtukas (not `C×C`), Gross–Zagier-type, RH-SILENT**. Three steelman readings all fail.
  **A5 conflates two distinct theorems on distinct spaces about distinct `s`-values** ⟹ the pass-two
  axiom "surface self-intersection `=‖f‖²`" pins the wrong number; the bridge's central analogy fails
  *at the function-field archetype*. 9th wall confirmation, first one *inside* the FF model. Triggered
  HIGH-priority back-up item (NEXT #1).
