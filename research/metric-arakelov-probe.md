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

This is a real, computed bridge — not an analogy. References below make the
condition-number/height identity precise.

## 2. Literature map (real, with access notes)

**Slack = height of discriminant (the linchpin).**
- *On the zeta Mahler measure function of the Jacobian determinant, condition numbers and the
  height of the generic discriminant*, Applicable Algebra in Eng. Comm. Comp. (2016),
  doi:10.1007/s00200-016-0284-9 — **the** paper connecting condition numbers, (zeta) Mahler
  measure, and the **arithmetic height of the discriminant variety**. *Likely paywalled — want
  full access.*
- *Heights of polynomials over lemniscates*, arXiv:2101.06708 — heights as `L^p` energies
  against **equilibrium measures**; `p=0` = Mahler measure. *Open.*
- Bost–Gillet–Soulé, *Heights of projective varieties and positive Green forms*, JAMS 1994 —
  Arakelov heights + **positive Green forms** (the positivity). *Paywalled — want access.*
- Pengo, *Mahler measures: from small heights to big conjectures* (survey) — Mahler/heights/
  L-functions (Beilinson). *Open PDF.*

**de Bruijn–Newman = log-gas potential flow (the marginal/critical point).**
- Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914 — the backward
  heat flow is a **first-order log-gas** (zeros repel like charges); equilibrium = arithmetic
  progression; the obstruction `Λ≥0` comes from **Montgomery pair correlation (GUE)**. Same
  equilibrium/potential structure as the Hermite slack. *Open.*

**Metric arithmetic geometry aimed at RH (Option 1, already built).**
- Connes–Consani, *Weil positivity and the trace formula, the archimedean place*,
  arXiv:2006.13771 — the **archimedean** contribution to Weil positivity (prolate-spheroidal /
  potential-theoretic). *Open; PDF didn't text-extract — want a readable copy.*
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

## 4. The expanded probe (gated, certifiable)

- **P1 — slack as a height (compute).** Certify `ρ(d)`, `disc(H_d)` (closed form), `Mahler(H_d)`,
  the semicircle log-energy. Establish `log(1/ρ(d)) = (height term, linear) − (energy, cancelled)`
  rigorously. *Status: grounded numerically (§1); upgrade to certified intervals (FLINT).*
- **P2 — GUE-universality.** Is the `1.22` rate / the energy `d²log d` coefficient the
  **semicircle (GUE) universal** constant, or Hermite-specific? Compare to the equilibrium-measure
  log-energy and to Montgomery's pair-correlation constant. A match is the structural bridge:
  *the proof's slack and the zeros' statistics share one universality.*
- **P3 — potential-theory unification.** Put the Hermite/semicircle equilibrium (Jensen) and the
  arithmetic-progression equilibrium (dBN log-gas) in one frame; identify `ρ(d) → 0` and `Λ = 0`
  as the same critical/marginal point of a log-gas.
- **P4 — the forcing reframe (the payoff).** Recast "drive the `ζ^{(2n)}(½)` asymptotic error
  below `ρ(d)` uniformly in `d`" as a **positivity of a difference of heights** (error-height
  ≤ slack-height) — an arithmetic-Hodge-index-flavored inequality. Then **kill-test** the recast
  statement (must fail for DH and Epstein; survive Weil positivity; not be Weil-positivity-in-
  disguise). If it passes, it is the first forcing-structure candidate in Arakelov language → §8
  formalization trigger.
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

## 6. Papers to access (help wanted)

Priority for full text (open ones I can fetch myself; these are the gated/awkward ones):
1. AAECC 2016, condition numbers / height of the generic discriminant (doi:10.1007/s00200-016-0284-9) — **the linchpin identity.**
2. Bost–Gillet–Soulé, *Heights of projective varieties and positive Green forms*, JAMS 1994 — the positivity.
3. Connes–Consani, arXiv:2006.13771 — a text-extractable copy (the PDF did not parse).
