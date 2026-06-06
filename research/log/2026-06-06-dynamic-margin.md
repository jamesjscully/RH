# Dynamic margin is polynomially conditioned — the fresh handle — 2026-06-06

Pulling the spectral-edge "next target" (the edge backward-margin's d-law) produced the cleanest
result of the thread. `scripts/numerics/witness/spectral_edge.py: dynamic_margin_conditioning`.

## The result

**The DYNAMIC (dBN flow) margin is polynomially conditioned, where the STATIC (BW height) slack is
super-exponential.**

- **Fixed shape (Hermite `H_d`): dynamic backward margin = `1/4` EXACTLY, d-independent.** Proof:
  the dBN flow is a pure dilation, `e^{sD²}H_n(x) = (1−4s)^{n/2} H_n(x/√(1−4s))` (Angle 2B), which
  is hyperbolic iff `1−4s>0` iff `s<1/4`. Contrast: `H_d`'s *static* BW slack is super-exponential
  (P1a/P1b). **Same object, two metrics — dynamic robust (`1/4`), static collapsed (super-exp).**
- **Real-ξ `J_{d,n}`: dynamic backward margin decays only POLYNOMIALLY**, `~ d^{−p}` with
  `p ≈ 4.0 (n=0), 3.0 (n=4), 2.5 (n=8)` — power-law fits beat exponential decisively (reliable
  mpmath reality check, `d=4..24`; resid ~0.1 power vs ~0.3–0.5 exp).

## Reading (honest)

The super-exponential slack that made the metric/Arakelov route look hopeless (`½ d log d` energy,
edge-controlled) is **substantially a height-metric artifact** — the `(1+s²)^{d/2}` Bombieri–Weyl
weighting blows up at the spectral edge. The **physical** hyperbolicity margin, measured by the
*actual de Bruijn–Newman flow*, is only **polynomially** small. So:

> The dBN/dynamic framing is the well-conditioned coordinate. It reduces the uniform-in-`d` target
> from "prove a **super-exponential** lower bound on the slack" (RH-hard) to "prove a **polynomial**
> lower bound on the dynamic margin" — far more tractable.

## What this does and does not do

- **Does not** prove RH: the dynamic margin still → 0 as `d→∞` (just polynomially), so "RH barely
  true" (`Λ=0`) is unchanged; and the rigorous link from the finite `J_{d,n}` backward margin to the
  dBN constant `Λ` itself needs care (the finite margin is a proxy).
- **Does** identify the right coordinate and dramatically improve the conditioning of the frontier.
  This is the genuine fresh handle the spectral-edge thread was chasing: the dynamic flow sees a
  polynomial margin where the static height saw a super-exponential one.

## Next

- Pin the exact `d`-power (and its `n`-dependence) of the real-ξ dynamic margin; certify it.
- The rigorous bridge: relate the finite-`J_{d,n}` backward margin to `Λ` (does a polynomial lower
  bound on the margin, uniform in `(d,n)`, imply `Λ ≤ 0`?). This is the genuine RH-relevant target,
  now in a polynomial (not super-exp) regime.
