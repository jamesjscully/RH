# CORRECTION — the "dynamic margin" was the wrong flow — 2026-06-06

Trying to make rigorous the bridge from the finite-Jensen backward margin to the de Bruijn–Newman
constant `Λ` (the stated next target) exposed a conflation in the preceding two commits. The §8
verifiability discipline caught it. **Retracting the "fresh handle" claim.**

## The error

The de Bruijn–Newman flow on `Ξ` is `Ξ_t = e^{−tD²}Ξ` — the heat flow **in `Ξ`'s own variable**.
On the Taylor coefficients this is the **sequence flow** `γ(k) → γ_t(k) = (2/(2k)!)∫Φ(u)u^{2k}e^{tu²}du`,
and `Λ` is governed by the hyperbolicity of the Jensen polynomials of the *flowed sequence*
`J_{d,n}^{γ_t}`.

What I actually computed (`spectral_edge.py`: the "dynamic backward margin", step 3, and the
`d^{−3}` "dynamic-margin conditioning") was the heat flow `e^{sD²}` applied **to the Jensen
polynomial `J_{d,n}(X)` in its own variable `X`** — a *different* operation in a *different*
variable. It is Pólya's (hyperbolicity-preserving) heat flow on the degree-`d` polynomial, **not**
the dBN flow on `Ξ`.

## The two flows behave oppositely (verified)

Same `J_{8,2}` (hyperbolic at rest):
- **Polynomial heat flow** `e^{sD²}J`: loses hyperbolicity at `s ≈ 0.005` (small, decreasing ~`d^{−3}`).
- **dBN sequence flow** `γ → γ_t`: robust past `t = −1` — in fact the backward sequence margin is
  *infinite* for all accessible `(d,n)` (as `t→−∞` the kernel `e^{tu²}Φ` concentrates at `u=0` →
  Gaussian → Hermite → hyperbolic).

So they are genuinely different, and the polynomial-heat margin **does not bridge to `Λ`.**

## What is retracted vs what stands

**Retracted** (conflated polynomial heat flow with dBN):
- "the dynamic (dBN) margin is polynomially conditioned" — it was the polynomial heat flow, not dBN;
- "the super-exponential slack is a metric artifact / the dBN framing reduces the uniform-in-`d`
  target to a polynomial bound" — unfounded as an RH/`Λ` statement;
- the "edge localization of the `Λ` mechanism" (step 3) — that was the polynomial-heat-flow
  mechanism, not the dBN `Λ` mechanism.

**Still stands** (flow-independent or correctly-attributed):
- the **static** edge-concentration of the real-ξ deviation `J_{d,n} − H_d` (pull 1, standardized
  roots — no flow involved). Genuine.
- the polynomial-heat-flow facts themselves (margin `~d^{−3}`, edge-localized) are *true*, but they
  are facts about **Pólya hyperbolicity-robustness of the polynomial**, with **no established link
  to RH/`Λ`**.
- `dbn_route.py`'s demonstration (heat flow on a polynomial *as a function* detects off-line zeros)
  is correct — the heat flow on a function *is* its dBN flow; the error was specific to applying it
  to the *Jensen* polynomial and calling it dBN-on-`Ξ`.

## The honest reassessment

The actual dBN sequence flow shows the finite Jensen polynomials are **robustly hyperbolic** for
accessible `(d,n)` — the RH-criticality (`Λ = sup_{d,n} λ_{d,n} = 0`) is a **deep `(d,n)→∞` limit**,
inaccessible to direct computation (consistent with GORZ's `n ≳ e^d`). There is **no finite dynamic
handle**; the encouraging polynomial picture was the wrong flow.

This returns the spectral-edge thread to: a genuine *static* edge structure (the deviation lives at
the edge) plus the standing fact that the dynamical RH-criticality is asymptotic and not finitely
accessible. The "fresh handle" did not survive contact with the correct flow — but catching that is
the verifiability commitment doing exactly its job.
