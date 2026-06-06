# Examining paths (a)/(b): the edge is DISPERSING — 2026-06-06

Examining the static-edge path (a) through the kill-test lens (b) raises the pivotal question:
**is the edge deviation RH-content-bearing (ξ-specific / Euler-product) or dispersing
(functional-equation / universal)?** A clean probe answers it.

## The probe

The Ξ kernel `Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}}`. The `n=1` term is the
leading (functional-equation) structure; `n≥2` are higher modes (exponentially suppressed at
large `u`, hence at high index `k`). Compared the standardized edge deviation `J_{d,n}−H_d` using
the full kernel vs the `n=1`-only kernel.

## Result (decisive)

The edge deviation is **identical** for full Ξ and `n=1`-only — to `~1e-8` (the `n≥2` effect at the
edge root is `1e-8…1e-11`, numerical noise). The higher-mode (arithmetic) difference is maximal at
the **shoulder** (standardized `loc +0.42`), not the edge (`loc +1`), and is tiny.

Reason: `u^{2k}` weights the large-`u` tail, where the `n=1` term dominates (`e^{−πe^{2u}}` vs
`e^{−4πe^{2u}}` for `n=2`). So the **edge / high-index Jensen structure sees only the leading kernel
term**; the higher modes are exponentially suppressed there.

## Verdict — the edge is dispersing (the thread's premise revised)

The large edge deviation `J_{d,n}−H_d` (pull 1) is **real but universal** — it is the deviation of
the leading functional-equation kernel's moments from the Gaussian/Hermite limit, *independent of
the higher arithmetic*. By the program's Farmer/kill-test criterion this is **dispersing**
(functional-equation structure, the RH-neutral class — cf. the shared digamma `Γ_ℝ` factor, Angle
3). The spectral-edge thread conflated "where the deviation is large" (the edge, universal) with
"where the RH-content is" — they are different. The RH-content (the Euler-product / zero-
distribution part) is the **subleading** structure, which lives at the **shoulder/bulk** and is
**tiny** (`~1e-8`) at accessible `(d,n)`.

## Consequence for the two paths

- **Path (a) — static edge:** the edge has **no reverse force** (dispersing). Killed by the
  kill-test. Pushing it further is pushing a functional-equation feature.
- **Path (b) — obstruction calculus / kill-tests:** the kill-test discipline *worked* — it
  correctly identified the edge as dispersing. The sharper map relocates the RH-content to the
  **subleading shoulder/bulk arithmetic** (the Euler-product part), tiny and hard — consistent with
  the program's standing finding that the RH content is the Euler-product/zero-distribution
  structure, not any leading/archimedean/edge feature.

Net: a genuine (negative) result that sharpens the map and *corrects* the spectral-edge premise —
the edge is dispersing; the RH content is the subleading arithmetic, where it has always been.
