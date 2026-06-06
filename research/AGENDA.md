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

1. **[ANCHOR · load-bearing]** Verify **A5 in the function-field case**. Over `𝔽_q` the Weil proof uses
   the Hodge index on `C×C`; the square root `|α|²=q → |α|=q^{1/2}` is a self-intersection number. A5
   claims that self-intersection equals a **Rankin–Selberg / Petersson-norm analog**. *Is it a theorem
   there?* Check for a concrete curve (e.g. an elliptic curve over `𝔽_q`: compute `Δ·Δ`, the relevant
   correspondence self-intersections, and the Rankin–Selberg residue) + literature. **If A5 fails
   where everything is provable, the sym²→surface reduction is wrong — flag loudly and add a "back up
   to pass two" item.**
2. **[ANCHOR]** Same verification in the **Selberg / hyperbolic-surface** case (Maass/Petersson norm vs
   the spectral self-intersection / the Selberg-zeta resonance condition).
3. **[ADVERSARIAL]** Try genuinely hard to **refute** the A5 anchor claims (items 1–2): a precise
   counterexample or a mismatch between the self-intersection and the Petersson norm.
4. **[CONSTRUCT]** Condensed **stack-of-norms** (Clausen–Scholze / F. Charles): can it realize a
   surface over `\overline{Spec ℤ}` with self-intersection `= ‖f‖²`? Where exactly does the
   "archimedean Deligne–Illusie ⟶ Kähler" open question sit relative to this target?
5. **[CONSTRUCT]** **Tropical / Connes–Consani** square: the diagonal self-intersection in the `q→1`
   limit — does it carry the `‖f‖²` target, and where does it diverge?
6. **[CONSTRUCT · representability]** Is **"the square root of the Rankin–Selberg/Petersson
   edge-positivity"** functor representable (Brown representability / a moduli description)? What object
   would represent it?
7. **[DEFORM]** Trace the `C×C` Hodge index through the `q→1` degeneration explicitly; identify the
   **obstruction-cocycle** (what breaks) — that names the next axiom (pass-four input).

## DONE
(the loop appends here, newest first)
