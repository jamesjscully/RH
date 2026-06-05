# Descent micro-test — 2026-06-05

Evaluating whether stacks/descent theory could organize the RH obstruction calculus.
The test: does the bandwidth-`W` Weil/explicit-formula obstruction carry genuine
**descent (cohomological) content**, or does it collapse to a single limiting positivity?

A descent obstruction is the cohomology of the **nerve of the template cover**, so the
question is structural and sharp:

- nested / additive cover (each refinement adds independent terms) → totally ordered →
  nerve is a chain → contractible → `H¹ = lim¹ = 0` → no obstruction (descent decoration);
- cover with **overlap cycles** (genuine gluing/cocycle conditions) → nerve has nontrivial
  `H¹` → real descent obstruction (descent has teeth).

`scripts/numerics/witness/descent_test.py` implements both halves.

## Soundness

Riemann–Weil explicit formula validated for `h(r)=e^{-(r/R)²}` (positive type):
`Σ_γ h(γ) = h(i/2)+h(-i/2) − g(0)logπ + (1/2π)∫ h(r)Re ψ(¼+ir/2)dr − 2Σ_n Λ(n)n^{-½}g(log n)`
balances to **~1e-13** (R=6,10). So the bandwidth family genuinely reconstructs the zeros.

## Result

**The Weil/explicit-formula bandwidth family is additive in the primes:**
`W(g;P') − W(g;P) = −2 Σ_{P<n≤P'} Λ(n)n^{-½}g(log n)` — independent local terms, **no
cocycle** (verified: each cutoff increment equals exactly the new-prime terms). Its
prime-cutoff cover is a chain → contractible nerve → `H¹ = 0`.

Nerve `H¹` computed exactly (Čech coboundary ranks):

| cover | H¹ | descent |
|---|--:|---|
| chain / nested bandwidths (Weil family) | 0 | none |
| 3-arc circle (overlap cycle) | 1 | obstruction |
| filled triangle (triple overlap) | 0 | none |
| 4-box loop (overlap cycle) | 1 | obstruction |

## Verdict

For the explicit-formula / NB-BD family the obstruction is **cohomologically trivial** —
it collapses to the single limiting Weil positivity (the dispersing equivalence we already
flagged). **Descent is decoration here.** The reason is structural: the explicit formula is
*linear in the prime measure*, so primes contribute independently — there is no consistency
condition between scales, hence no cocycle, hence no `H¹`.

Descent has teeth only on a family whose cover has **overlap cycles** — i.e. a recursive
cert/tail/bridge family with genuine gluing (Jensen degree/shift boxes, interval
subdivisions). That is exactly the structure the explicit-formula reformulation discarded,
and it vindicates the original recursive-bridge instinct.

**Reusable criterion (the payoff):** *descent helps a template family iff the nerve of its
cover has nontrivial `H¹`.* `cech_h1(V, edges, triangles)` computes it in linear algebra —
a cheap structural gate to run on any candidate family before investing in a descent
calculus. The honest next step is to write down the Jensen (or interval-subdivision) cover's
overlap structure explicitly and run `cech_h1` on it: if `H¹ = 0` there too, descent is dead
for RH-shaped problems; if `H¹ ≠ 0`, that family is where a descent/obstruction calculus
could actually live.
