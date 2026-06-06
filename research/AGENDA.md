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

1. **[CONSTRUCT · load-bearing · the relocated target]** **The line is forced by a FORM's SIGNATURE,
   not a self-intersection NUMBER** (see DONE #1). Both `‖f‖²` (pass two, refuted) and its correction
   `deg(F)·(Δ·Δ)` (DONE #1, shown RH-silent *and not even Euler-borne*) fail because the self-intersection
   *number* is the wrong kind of object. The genuine Weil mechanism is the **Hodge index theorem**: the
   intersection form on `NS(S)`/`H¹_prim` has signature `(1, ρ−1)` and RH `⟺` it is **negative-definite
   on the primitive part** (verified on `E×E`: Gram `[[0,1,1],[1,0,1],[1,1,0]]`, signature `(1,2)`).
   **Re-run `method.md` step 4 (REPAIR + UNIVERSAL PROPERTY) with the SIGNATURE target:** what object
   over `ℤ` carries a self-dual pairing on a `ρ`-dim space whose **signature** is `(1, ρ−1)` and whose
   negative part forces the zeros? This is the OS/reflection-positivity thread re-stated (a signature
   *is* a positivity) but with the geometric object corrected — NOT a Petersson norm, NOT `deg·χ`, but
   the **negative-definite intersection FORM on `H¹_prim` of a (hypothetical) arithmetic surface**.
   Does the falsifier change verdict when the candidate is a *form's signature* rather than a *number*?
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

> **CAVEAT on items 3–7 (post DONE #1 + #2):** all five were written with the **`‖f‖²`
> self-intersection target**, which was refuted (DONE #1), and its first correction `deg·χ` (a NUMBER)
> was then shown RH-silent + not-even-Euler-borne (DONE #2). The corrected target is **the signature
> `(1, ρ−1)` of the negative-definite intersection FORM on `H¹_prim`** (item 1), *not any number*. So
> for items 3–7: the construction must realize an object whose intersection FORM has the Hodge-index
> SIGNATURE — replace every "self-intersection `=‖f‖²`" with "intersection form has signature
> `(1, ρ−1)`, negative-definite on the primitive part."

## DONE
(the loop appends here, newest first)

- **2026-06-06 — Re-ran step 2 with the corrected mechanism: the line is a FORM's SIGNATURE, not a
  NUMBER.** [BACK UP · load-bearing → honest negative + relocation].
  `scripts/numerics/witness/a5_corrected.py`, `research/log/2026-06-06-a5-corrected-mechanism.md`.
  **Finding [THM+computed]:** the corrected forcing input `Γ_F·Γ_F = deg(F)·(Δ·Δ)` (verified exactly:
  ratio `= deg(F)` for `F∈{id,Frob_q,Frob_{q²},[2],[3]}`, line `= log(q^{1/2})/log q = ½` for every
  `q`) is, on the falsifier, **RH-SILENT *and not even Euler-borne*** — `deg·χ` is pure
  topology×base-field-size, carried by DH too (strictly **worse** than `‖f‖²`, which at least
  DH-refused). The decisive relocation: the RH content is the **Hodge-index SIGNATURE `(1, ρ−1)`** —
  negative-definiteness of the intersection FORM on the primitive part — verified on `E×E` (Gram
  `[[0,1,1],[1,0,1],[1,1,0]]`, eigenvalues `{−1,−1,2}`, signature `(1,2)`). The self-intersection
  *number* (`‖f‖²` OR `deg·χ`) is merely a value the form is evaluated on. **Both the `‖f‖²` axiom and
  its correction are the WRONG KIND of object: the line is forced by a FORM's signature, not a NUMBER.**
  `‖f‖²` confirmed RH-silent scaffolding (enters only as a lattice value, never as forcing). 10th wall
  confirmation; relocates the target to the negative-definite `H¹_prim` form over `ℤ` (NEXT #1, reconnects
  to the OS/reflection-positivity thread).
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
