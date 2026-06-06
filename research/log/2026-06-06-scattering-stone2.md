# Stone two of the lift: the forcing functional — and where it lands — 2026-06-06

`scripts/numerics/witness/scattering_forcing.py`. Stone two = the Euler-product-borne positivity that
pins S(s)'s resonances to `Re s = ¼` and fails for the off-line control.

## What was built and verified

The forcing functional is the **Li/Weil positivity** via S(s)'s resonances (resonances at `s=ρ/2`;
pinning to `Re ¼` ⟺ all `ρ` on the line):
`λ_n = Σ_ρ [1 − (1−1/ρ)^n] ≥ 0 ∀n ⟺ RH` (Bombieri–Lagarias / Li). It is Euler-product-borne and
**passes the kill-test**: on-line zeros contribute positively; an off-line quadruple (FE-preserved)
drives `λ_n < 0` (verified, first at `n=12` for a zero at `0.99+2i`).

## Two §8 catches in this stone (the discipline working)

1. My stone-one "corner-compact ⟺ self-adjoint" framing was wrong (CC20: self-adjointness avoided);
   corrected to the tension.
2. My **first** stone-two kill-test used `ρ₀=0.8+10i`, whose Li-violation is at impractically large
   `n` — the contribution stayed *positive* through `n=160`, so the kill-test **did not fire** and my
   first diagnosis overclaimed it. Fixed with a reachable off-line zero (`0.99+2i`, violation at
   `n=12`). The kill-test now genuinely passes — demonstrated, not asserted.

## The honest verdict — where stone two lands

The forcing functional **exists**, is **Euler-product-borne**, and **passes the kill-test**. But its
positivity *for ζ* (`λ_n ≥ 0` for all `n`) **is the Riemann Hypothesis itself** (Li 1997). So stone
two is a *correct* forcing functional whose positivity is **the unproven core — not a free proof**.

- The conformal/scattering construction supplied the **scaffold**: `S(s)` with resonances=zeros,
  unitarity on `Re ½`, and a built-in DH-discriminator (the kill-test).
- The **forcing** (`λ_n ≥ 0`) is **the wall**. A *geometric* proof of that positivity is exactly a
  positive Green form / metric `h_∞` on the canonical `Ω¹` — **the missing object itself**.

So the conformal route, **fully built**, reaches the same wall — but cleanly: a kill-test-passing
spine (`S(s)` + the forcing functional), with the **entire difficulty isolated to one positivity**,
and a precise statement of what would discharge it (a geometric `h_∞`). That is the honest endpoint of
the construction attempt: not a proof, but the object reduced to its single irreducible positivity,
with the scaffolding around it actually built and tested.

## What this rules in / out for the program

- **In:** the scattering/conformal realization is sound and discriminating (passes kill-tests). `S(s)`
  is a genuine, correct object; the resonance picture is faithful.
- **Out (no free lunch):** the conformal dressing does **not** make the positivity provable for free.
  Lax–Phillips's lesson stands — the resonances are not self-adjoint eigenvalues, and unitarity is
  RH-neutral. The remaining work is the geometric positivity (`h_∞`), which is the deep frontier.
