# The spectral-edge thread (live)

The one fresh direction that survived the three-angle synthesis (`research/log/
2026-06-05-junction-synthesis.md`). This file is the working doc; it supersedes the
metric/Arakelov probe as the active frontier.

## Where it came from

The Hermite junction is mapped: the **static/archimedean side is understood and RH-neutral** —
the dBN flow acts on the Hermite fixed shape as a pure dilation (exactly marginal,
`e^{−tD²}H_n=(1+4t)^{n/2}H_n(x/√(1+4t))`), and the fixed shape's archimedean energy is the shared
digamma `Γ_ℝ` factor (identical for ξ and Davenport–Heilbronn ⇒ dispersing). The slack is an
intrinsic marginal height, super-exponential in *every* coordinate (incl. total positivity), and
**controlled at the outermost / spectral-edge critical point** (Airy regime).

So the RH content is in the **deviation from the fixed shape** — *transverse* to the marginal
flow, at the **spectral edge**, on the dynamical / Euler-product side.

## The precise question

> Does the **Tracy–Widom / Airy edge fluctuation** of `J_{d,n} − H_d` (the real-ξ Jensen
> polynomial minus its Hermite scaling limit) admit a one-sided (`Λ≥0`-compatible) bound under
> the de Bruijn–Newman flow, **uniform in `d`**?

If yes, that controls the uniform-in-`d` slack via the flow — the thing the static height cannot
do. It is where Rodgers–Tao's GUE input (zero statistics) meets the slack's edge control.

## The subtlety to resolve FIRST (do not assume "edge")

There is a genuine tension to settle before building on "edge", and §8 says verify it:

- the **BW-metric slack** (the Arakelov height) is **edge-dominated** — the `(1+s²)^{d/2}` factor
  makes perturbations at large-`s` (edge) critical points cheap;
- but **hyperbolicity is physically lost when two roots collide**, and Hermite/semicircle roots
  are **densest at the center** (smallest gaps in the **bulk**), not the edge.

So which controls RH — the edge (height metric) or the bulk (root collision)? This may even
*revise* the "edge" framing. The first pull must determine, for the **real ξ** Jensen
polynomials, where hyperbolicity is most marginal and which measure is RH-relevant.

## Plan (the pull)

1. **Locate the most-marginal direction** for the real-ξ `J_{d,n}` (rescaled to the Hermite
   frame): the smallest root gap (bulk?) vs the BW-cheapest valley (edge?). Resolve the
   edge-vs-bulk question on real data.
2. **Characterize the deviation** `J_{d,n} − H_d` where it most threatens hyperbolicity — its
   size, sign, and scaling in `(d,n)`; connect to Airy/Tracy–Widom at the edge if that's where it
   lives.
3. **The flow's transverse action**: how the dBN flow (pure dilation along the fixed shape) acts
   on the deviation — does it suppress the dangerous fluctuation? Is the action one-sided?
4. **Uniformity**: does any bound from (3) survive uniformly in `d`? (the RH-hard test.)

Each step is a cheap, certifiable go/no-go in the spirit of every micro-test. Honest stop
conditions: if the control is bulk not edge, re-aim; if the deviation has no clean edge scaling,
the Tracy–Widom framing is decoration; if the flow's action on the deviation isn't one-sided, the
`Λ≥0` transfer is dead.
