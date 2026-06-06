"""Stone two of the lift: the forcing functional on S(s) -- and where it lands.

Stone one (`scattering.py`) built S(s) and showed its unitary/self-adjoint structure REFLECTS the
zeros as resonances but does not FORCE them onto Re s = ¼ (the structure is RH-neutral). Stone two is
the FORCING: an Euler-product-borne positivity that pins the resonances to Re s = ¼ and FAILS for the
off-line control.

The concrete forcing functional is the **Li/Weil positivity** read through S(s)'s resonances
(resonances at s = ρ/2; pinning them to Re ¼ ⟺ all ρ on the line):

    λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ]    ≥ 0  for all n   ⟺   RH    (Bombieri–Lagarias / Li 1997).

It is Euler-product-borne (λ_n are the Taylor data of `log ξ`, i.e. of the Euler product + Γ_ℝ), and
it PASSES the kill-test:

- on-line zeros (resonances ON Re ¼) contribute positively;
- an off-line zero quadruple (RH-false, functional equation preserved) drives some `λ_n < 0` — its
  Re<½ mirror `1−ρ₀` has `|1−1/(1−ρ₀)| > 1`, so its term grows and goes negative (verified: a zero at
  `0.99+2i` first violates at `n=12`). So the functional KILLS the off-line control.

**The honest verdict (where stone two lands).** The forcing functional EXISTS, is Euler-product-borne,
and passes the kill-test. But its positivity *for ζ* (`λ_n ≥ 0` for all `n`) **is the Riemann
Hypothesis itself** (Li). So stone two is a *correct* forcing functional whose positivity is the
unproven core — **not a free proof**. The conformal/scattering construction supplied the **scaffold**
(S(s): resonances=zeros, unitarity on Re ½, a built-in DH-discriminator); the **forcing** (`λ_n ≥ 0`)
is the wall. A *geometric* proof of the positivity is exactly a positive Green form / metric `h_∞` on
the canonical `Ω¹` — i.e. the missing object itself (`the-lift-program.md`). **The conformal route,
fully built, reaches the same wall — cleanly, with a kill-test-passing spine and the entire difficulty
isolated to one positivity.**

Run:  python3 -m scripts.numerics.witness.scattering_forcing
"""
from __future__ import annotations

import mpmath as mp


def li_term(rho, n):
    """The contribution of a zero ρ to the n-th Li coefficient: 1 − (1−1/ρ)^n."""
    rho = mp.mpc(rho)
    return 1 - (1 - 1 / rho) ** n


def quad_contribution(rho0, n):
    """Contribution to λ_n of an off-line zero quadruple {ρ₀, 1−ρ₀, ρ̄₀, 1−ρ̄₀} (FE-symmetric)."""
    rho0 = mp.mpc(rho0)
    quad = [rho0, 1 - rho0, mp.conj(rho0), 1 - mp.conj(rho0)]
    return sum(li_term(r, n) for r in quad).real


def first_violation(rho0, nmax=60):
    """Smallest n at which the off-line quadruple drives the Li contribution negative (or None)."""
    for n in range(1, nmax + 1):
        if quad_contribution(rho0, n) < 0:
            return n
    return None


def summary():
    mp.mp.dps = 40
    print("Stone two: the forcing functional λ_n = Σ_ρ[1−(1−1/ρ)^n] ≥ 0 ⟺ RH\n")

    print("(a) on-line zeros (resonances ON Re ¼) contribute positively:")
    for rho in [mp.mpc(0.5, 14.1347), mp.mpc(0.5, 21.022)]:
        c = (li_term(rho, 1) + li_term(mp.conj(rho), 1)).real
        print(f"      ρ = {complex(rho)}: pair c₁ = {float(c):+.5f}")

    print("\n(b) KILL-TEST -- off-line zero quadruple (RH-false) drives λ_n < 0:")
    for rho0 in [mp.mpc(0.99, 2.0), mp.mpc(0.95, 3.0)]:
        nv = first_violation(rho0)
        print(f"      off-line ρ₀ = {complex(rho0)}: first n with negative contribution = {nv}")
        for n in [10, 15, 25]:
            print(f"          n={n:2d}: contribution = {float(quad_contribution(rho0, n)):+9.3f}")

    print("\n[verdict] forcing functional EXISTS, Euler-product-borne, kill-test PASSES.")
    print("  But λ_n ≥ 0 for ζ IS the Riemann Hypothesis (Li 1997) -- the unproven core, not a proof.")
    print("  The scattering construction gave the scaffold; the forcing is the wall; a geometric proof")
    print("  of the positivity = the metric h_∞ on the canonical = the missing object itself.")
    print("  The conformal route, fully built, reaches the same wall -- cleanly.")


if __name__ == "__main__":
    summary()
