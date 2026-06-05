# Read the three Arakelov/metric papers — 2026-06-05

Obtained and read (in `research/papers/`, gitignored): Pardo–Pardo (condition numbers /
height of the discriminant, AAECC 2016), Bost–Gillet–Soulé (heights + positive Green forms,
JAMS 1994), Connes–Consani (Weil positivity at the archimedean place, arXiv:2006.13771).
Full synthesis folded into `research/metric-arakelov-probe.md`. Highlights:

## The bridge is now precise

- **Slack = condition number = `1/dist` to the discriminant variety, in the Bombieri–Weyl
  metric** (Pardo–Pardo). The discriminant factors as `resultant × ∏_ζ(conditioning at ζ)`;
  the *height* of the discriminant variety is the average `log`-condition-number, a
  Gamma/digamma/**harmonic-number** closed form.
- **Metric correction:** recomputing the Hermite slack in the BW norm (the correct height
  metric) gives `log(1/ρ_BW(d)) ≈ 0.93–1.04 d`, **consistent with `(3/2)ln2 = 1.04`** — the
  Hermite-discriminant structural constant — and cleaner than naive-L²'s `1.22`. Evidence the
  slack is genuinely a height. (`jensen_real.py: stability_radius_bw`.)
- **Positivity = forcing structure, in Arakelov form** (BGS): `h(X) ≥ 0`; arithmetic Bézout;
  **positive Green forms are the analytic positivity, and §6.3 gives an explicit obstruction to
  their existence** — the metric analogue of the (topologically trivial) descent obstruction.
  Resultant height `= ½(∏dᵢ)((N+1)H_N − N)` — harmonic numbers again.
- **The RH-specific positivity** (Connes–Consani): archimedean Weil positivity = positivity of
  a **trace of the compressed scaling action** on Sonin's space, controlled by
  prolate-spheroidal functions and Toeplitz matrices; the `±i/2` vanishing is the `H¹`-Lefschetz
  analogue; the geometry is the **square of the Scaling Site** (the missing `C×C`).

## Two unifying threads

1. **Harmonic number / digamma** is the common archimedean height: the Weil archimedean term
   (`ψ`), the resultant height (`H_N`), the expected solution log-norm (`½H_n`) are one object.
2. **The obstruction is already Arakelov** — BGS §6.3's obstruction to positive Green forms is
   exactly "the obstruction whose marginal vanishing is the forcing structure" (STRATEGY §3),
   realized with the metric, not the topology.

## Assessment unchanged, sharper

The metric "stack-analogue" exists (Arakelov heights, positive Green forms + their obstruction,
Connes–Consani archimedean trace positivity, the Scaling Site). The slack has a precise home
(condition number = height of discriminant, BW metric). The forcing endpoints remain RH-hard.
The novel, cheap, certifiable next step: **P1** — certify the exact BW distance from `H_d` to
the discriminant variety and pin the `(3/2)ln2` constant; then **P4** — recast "error-height ≤
slack-height uniformly in `d`" as a positive-Green-form / arithmetic-Bézout positivity and
kill-test it.
