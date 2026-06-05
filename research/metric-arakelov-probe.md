# Metric / Arakelov probe — expanded design + literature

**Thesis.** The Jensen slack `ρ(d)` is potential-theoretic, and potential theory (logarithmic
energy, Green's functions, capacity, equilibrium measures) *is* the archimedean place of
Arakelov geometry. So the "stack-analogue where metric replaces topology" (STRATEGY §7, Option
1) **already exists** in several converging forms — Arakelov heights, the Connes–Consani
tropical arithmetic site, Berkovich/condensed analytic geometry — and the slack has a precise
home in it. Do not invent it; locate the slack inside it and test whether the location has
teeth.

This is a *probe*, gated by the kill-tests and certified per STRATEGY §8. The honest danger is
the same as always: a beautiful map that abstracts away the hard estimate. The map is only
worth pursuing if it reproduces a known tight bound retaining the constant.

---

## 1. The bridge, grounded

`jensen_real.py` gave `ρ(d) ~ e^{−1.22 d}`, i.e. `log(1/ρ(d)) ≈ 1.22 d` — **linear in `d`**.
Computing the height-theoretic quantities of `H_d` (the Jensen scaling limit):

| quantity | growth | meaning |
|---|---|---|
| `log|disc(H_d)|` | `~ d² log d` | the **semicircle log-energy** (GUE-universal) |
| `log Mahler(H_d)` | `~ 0.75 d` | a **height** (Weil/Mahler) |
| `log ‖coeffs‖` | `~ 1.5 d` | coefficient height |
| `log(1/ρ(d))` (the slack) | `~ 1.22 d` | **a height**, not the bare energy |

The slack decays *linearly in `d`* in the log, not like the `d² log d` discriminant. That is
exactly the **condition-number = height-of-the-discriminant-variety** relationship: the bare
discriminant is the (universal) log-energy; the *normalized* distance to the discriminant
variety — the condition number, our `ρ(d)` — is a **height** (linear). So:

> **The slack is (the exponential of minus) an Arakelov height of the discriminant variety,
> and its leading energy is the semicircle = GUE-universal.**

This is a real, computed bridge — not an analogy. The papers below make it precise, and
fix the metric: the height theory uses the **Bombieri–Weyl norm** (`‖Σ a_k X^k‖² = Σ a_k²/C(d,k)`,
the unitarily-invariant one), not naive L². Recomputing the slack in the BW metric gives a
**cleaner, recognizable rate**:

> `log(1/ρ_BW(d)) ≈ 0.93–1.04 · d` (range-dependent over `d ≤ 12…16`),  and  `(3/2)·ln 2 = 1.0397`.

i.e. the BW-metric slack rate is **consistent with the Hermite-discriminant structural constant**
(`disc(H_n)` carries a `2^{3n(n−1)/2}` factor → `(3/2)ln2` per degree), and is cleaner than the
messy `1.22` of naive L². The slack is the condition-number = `1/(distance to the discriminant
variety)` in the BW metric (Pardo–Pardo), an Arakelov-height quantity. The match is suggestive,
not yet tight: the random-direction stability radius is a noisy proxy — **P1 (certify the exact
BW distance to the discriminant) is what nails the constant.** `(jensen_real.py: stability_radius_bw.)`

## 2. Literature map (real, with access notes)

**Slack = height of discriminant (the linchpin).**
- **Pardo–Pardo**, *On the zeta Mahler measure function … condition numbers and the height of
  the generic discriminant* (AAECC 2016). **Read** (`research/papers/`). What it gives:
  (i) the slack is the **normalized condition number** `μ_norm(f,ζ)=‖f‖_Δ‖Diag(dᵢ^{−½})Df†‖` in
  the **Bombieri–Weyl** norm `‖·‖_Δ` (= Demmel's `‖A‖_F‖A†‖` in the matrix case); (ii) the
  **discriminant factors** as `|Disc(f)| ∝ |Res| · ∏_{ζ}|det(Df Df*)|^{½}/(1+‖ζ‖²)^{½}` (Prop 3.5)
  — discriminant = resultant × ∏(conditioning at each zero); (iii) the **arithmetic height of the
  discriminant variety** = the average `log μ_norm` = a **Gamma/digamma/harmonic-number** closed
  form (e.g. expected `log`-norm of solutions `= ½ H_n`, Cor 5.4). So the slack is a pointwise
  height; the discriminant height is its average.
- *Heights of polynomials over lemniscates*, arXiv:2101.06708 — heights as `L^p` energies
  against **equilibrium measures**; `p=0` = Mahler measure. *Open.*
- **Bost–Gillet–Soulé**, *Heights of projective varieties and positive Green forms*, JAMS 1994.
  **Read** (`research/papers/`). What it gives: the **arithmetic height `h(X) ≥ 0`** (`=0` iff a
  linear subspace) — the basic positivity; the **arithmetic Bézout** inequality
  `h(X·Y) ≤ h(X)deg(Y)+deg(X)h(Y)+c·deg·deg`; **positive Green forms** as the analytic
  positivity, **with an explicit obstruction to their existence** (§6.3) — the Arakelov
  obstruction-theory analogue; and the **resultant height** `log‖R‖ = ½(∏dᵢ)((N+1)H_N − N)+ε`
  — again a **harmonic number** (the archimedean digamma).
- Pengo, *Mahler measures: from small heights to big conjectures* (survey) — Mahler/heights/
  L-functions (Beilinson). *Open PDF.*

**de Bruijn–Newman = log-gas potential flow (the marginal/critical point).**
- Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914 — the backward
  heat flow is a **first-order log-gas** (zeros repel like charges); equilibrium = arithmetic
  progression; the obstruction `Λ≥0` comes from **Montgomery pair correlation (GUE)**. Same
  equilibrium/potential structure as the Hermite slack. *Open.*

**Metric arithmetic geometry aimed at RH (Option 1, already built).**
- **Connes–Consani**, *Weil positivity and the trace formula, the archimedean place*,
  arXiv:2006.13771. **Read** (`research/papers/`). What it gives: the archimedean Weil
  positivity is recast as the positivity of a **trace of the compressed scaling action**,
  `W_∞(g∗g*) ≥ Tr(ϑ(g) S ϑ(g)*)` (Thm 1), with `S` the projection onto **Sonin's space**
  (functions vanishing with their Fourier transform on `[−1,1]`); the gap is controlled by
  **prolate-spheroidal wave functions** and **Hermitian Toeplitz matrices**. The vanishing at
  `±i/2` is the analogue of the `H¹` contribution in the Lefschetz trace formula; the geometry
  is the **square of the Scaling Site** (the missing `C×C`, over the tropical/idempotent base).
  This is the RH-specific forcing positivity, in operator/metric form.
- Connes–Consani, *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392;
  the **arithmetic site** is over the **tropical** semifield `ℝ` (metric/idempotent geometry).
- Connes, *An essay on the RH* arXiv:1509.05576; *RH: Past, Present and a Letter Through Time*
  arXiv:2602.04022 (2026). *Open.*
- Deninger — foliated dynamical systems / leafwise cohomology for arithmetic schemes (the
  missing-cohomology program). *Mostly open.*

**Condensed / analytic geometry for L-functions (descent that remembers the metric).**
- Clausen–Scholze, *Analytic Geometry* / *Condensed Mathematics and Complex Geometry*; Scholze's
  motivic **six-functor formalism on Berkovich spaces / arc-stacks**; categorical zeta/L via
  traces. *Notes/PDFs open.*
- *Congruence zeta functions via a Berkovich approach*, arXiv:2605.26488. *Open.*

**Jensen / Hermite (the source).**
- Griffin–Ono–Rolen–Zagier, arXiv:1902.07321; *Jensen–Pólya program for various L-functions*,
  arXiv:1905.11269. Hermite discriminant closed form `D_n = 2^{n(n−1)/2} n ∏_{k=2}^{n} k^k`
  (classical) — confirms the `d² log d` energy.

**Gap / opportunity:** the Jensen/RH literature does **not** connect the Jensen slack to the
Arakelov-height machinery. The bridge in §1 appears unexplored and is computable.

## 3. The dictionary (topological/descent ↔ metric/Arakelov)

| descent / topology (decoration here, per the micro-tests) | metric / Arakelov analogue (exists) |
|---|---|
| nerve `H¹` | height / Mahler measure / log-energy (potential theory) |
| obstruction class | distance to the discriminant variety = condition number = **arithmetic height of the discriminant** |
| sheaf cohomology | Arakelov intersection / arithmetic Chow / **Green's functions** at `∞` |
| Grothendieck topos / site | Connes–Consani **arithmetic site (tropical)** / Berkovich / condensed |
| the forcing positivity | **arithmetic Hodge index** / Weil positivity at the archimedean place / positive Green forms |
| marginal vanishing of slack | **de Bruijn–Newman `Λ = 0`** (log-gas equilibrium, GUE) |

The connective tissue across the whole column is **potential theory** (equilibrium measures,
log-energy, Green's functions) — the same object governs the Hermite slack, the dBN flow, the
Arakelov archimedean place, and the GUE universality.

Two concrete threads tie the three papers together and are worth stating sharply:

- **The harmonic-number / digamma thread.** The archimedean term of the Weil explicit formula
  is a digamma `ψ`; the resultant height (BGS) is `½(∏dᵢ)((N+1)H_N − N)`; the expected
  log-norm of solutions (Pardo–Pardo) is `½ H_n`. *The same `H_n`/`ψ` closed form is the
  archimedean height in all of them* — the slack's height and the Weil archimedean term are the
  same kind of object.
- **The obstruction is already Arakelov.** BGS §6.3 — *an obstruction to the existence of
  positive Green forms* — is the metric analogue of the descent obstruction we found
  topologically trivial. The forcing structure (positive Green form / `h(X) ≥ 0` / archimedean
  trace positivity) and its obstruction live in the *same* Arakelov framework. This is precisely
  the "obstruction whose marginal vanishing is the forcing structure" (STRATEGY §3), realized
  with the metric, not the topology.

## 4. The expanded probe (gated, certifiable)

- **P1 — slack as a height.** *P1a DONE (certified, `jensen_p1.py`):*
  `disc(H_n) = 2^{3n(n−1)/2} ∏ₖ kᵏ` **exactly** (verified n≤12, exact integers via FLINT
  resultant) ⇒ `log|disc(H_n)|/n² → ½ln n + ((3/2)ln2 − ¼)`. The `½ln n` is the **semicircle
  (GUE) log-energy**; the **`(3/2)ln2 = 1.0397` is the exact 2-power structural constant** — the
  recognizable constant the BW-slack rate (~1.04) reflects. The discriminant (the energy/height)
  is pinned exactly, with the GUE-universal semicircle part. *P1b DONE (`jensen_p1b.py`),
  honest correction:* the slack-*distance* constant is **NOT** cleanly `(3/2)ln2`. A certified
  lower bound (sufficient hyperbolicity condition, certified acb roots) is **edge-dominated and
  loose** (super-exponential, dominated by the outer critical point where `(1+s²)^{d/2}~(2d)^{d/2}`);
  a direct search gives the slack `~e^{−1.04 d}` (heuristic). So `(3/2)ln2` is the discriminant
  **energy** (certified); the slack is energy **+ a conditioning factor** (Pardo–Pardo:
  `disc = res × ∏ conditioning`) and its exact constant is not tightly pinned. The §8 backpressure
  caught the over-claim. Solid: the slack is exponentially small and lives in the
  discriminant/condition-number (height) world.
- **P2 — GUE-universality.** Is the `1.22` rate / the energy `d²log d` coefficient the
  **semicircle (GUE) universal** constant, or Hermite-specific? Compare to the equilibrium-measure
  log-energy and to Montgomery's pair-correlation constant. A match is the structural bridge:
  *the proof's slack and the zeros' statistics share one universality.*
- **P3 — potential-theory unification.** Put the Hermite/semicircle equilibrium (Jensen) and the
  arithmetic-progression equilibrium (dBN log-gas) in one frame; identify `ρ(d) → 0` and `Λ = 0`
  as the same critical/marginal point of a log-gas.
- **P4 — the forcing reframe — DONE (`jensen_p4.py`).** Recast: `RH ⟺ dist_BW(Jensen point,
  discriminant variety) > 0 uniformly in d` = a **positive-Green-form / arithmetic-Bézout
  positivity** (BGS); its obstruction is **BGS §6.3** (obstruction to positive Green forms) — the
  RH-hard endpoint. **Kill-tests passed:** the Jensen/hyperbolicity criterion **detects off-line
  zeros** (demonstrated: `J(1+x²)` non-hyperbolic, `J(1−x²)` hyperbolic; a planted complex pair is
  detected) ⇒ it **fails for DH/Epstein** → genuine RH-content, not trivially dispersing; it is
  **not Weil-positivity-in-disguise** (xi's Taylor coefficients + discriminant geometry, a distinct
  positivity); honest **dispersion caveat** (Farmer): fixed-`d` hyperbolicity is RH-independent, so
  the reverse force sits **only** in the uniform-in-`d` limit = the §6.3 obstruction. **Outcome:** a
  legitimate forcing-structure candidate in height language, passing the object-level gates, not a
  shortcut. A certified uniform bound (a positive Green form for the Jensen-vs-discriminant
  configuration) is the §8 formalization trigger.
- **P5 — literature deepening.** Read the linchpin papers (condition-number/height-of-discriminant;
  Connes–Consani archimedean; lemniscate heights; positive Green forms) and extract the exact
  height/condition-number identity to make P1/P4 rigorous.

## 5. Honest assessment

- The metric stack-analogue **exists** (Arakelov / tropical arithmetic site / Berkovich /
  condensed) and the slack **has a precise home** in it (height of the discriminant). The
  potential-theory unification (Jensen-slack ↔ dBN ↔ Arakelov-`∞` ↔ GUE) is real and deep.
- **But every forcing endpoint is RH-hard open**: the arithmetic Hodge index / positive Green
  forms / archimedean Weil positivity / Connes–Consani positivity / Deninger cohomology. The
  Arakelov route is the real mountain, not a shortcut.
- **The one genuinely new, cheap, computable thing** is the Jensen-slack ↔ Arakelov-height bridge
  (apparently unexplored) and the recast P4. That is where to spend next — it is certifiable, and
  it either yields a forcing-structure candidate in height language (then formalize, §8) or it
  reduces, under kill-test, to a known dispersing positivity (then we have mapped another graveyard
  edge precisely, the win-win of STRATEGY §7.3).

## 6. Papers (read)

All three obtained and read — `research/papers/` (gitignored, local):
1. Pardo–Pardo, *condition numbers / height of the generic discriminant* (AAECC 2016) — the
   linchpin: slack = condition number (Bombieri–Weyl) = `1/dist` to the discriminant variety;
   discriminant = resultant × ∏(conditioning); height of the discriminant = `½ H_n`/Gamma form.
2. Bost–Gillet–Soulé, *Heights of projective varieties and positive Green forms* (JAMS 1994) —
   `h(X) ≥ 0` positivity; arithmetic Bézout; **positive Green forms + obstruction (§6.3)**;
   resultant height `= ½(∏dᵢ)((N+1)H_N − N)`.
3. Connes–Consani, *Weil positivity … the archimedean place* (arXiv:2006.13771) — archimedean
   Weil positivity = trace of the compressed scaling action on Sonin's space; prolate-spheroidal
   / Toeplitz control; `H¹`-Lefschetz analogue; square of the Scaling Site.

**Next read (open):** Pengo's Mahler-measure/heights survey; Connes–Consani *adeles class space*
(math/0703392) and the *Scaling Site* papers for the intersection theory on `C×C`.
