"""S(s) -- the conformal-boundary scattering operator (first stone of the lift program).

The lift program (research/the-lift-program.md) realizes the nontrivial zeros as the SCATTERING
RESONANCES of a conformally-covariant boundary operator. The concrete model is the cusp/Eisenstein
scattering matrix of the modular surface PSL(2,ℤ)\\ℍ (Lax–Phillips):

    Λ(s) = π^{-s/2} Γ(s/2) ζ(s)            (completed zeta = archimedean Γ_ℝ × Euler product)
    S(s) = Λ(2s-1) / Λ(2s)                 (the boundary scattering operator)

Three computed facts (verify with `summary()`):

1. **Resonances = zeros.** S(s) has simple poles at s = ρ/2 (the zeros of Λ(2s)). Under RH every
   ρ = ½+iγ, so every resonance sits on Re s = ¼. RH ⟺ all scattering resonances on Re s = ¼.
2. **Unitary on the critical line.** |S(½+it)| = 1, and S(s)S(1-s) = 1 — the conservation/self-
   adjointness condition. This comes ONLY from the functional equation Λ(s)=Λ(1-s).
3. **The kill-test (the honest catch).** Plant an off-line zero quadruple preserving the functional
   equation (the RH-false / Davenport–Heilbronn situation): unitarity is *unchanged* (still |S|=1),
   but the off-line zero produces an OFF-LINE resonance (Re s ≠ ¼). So the unitary/self-adjoint
   STRUCTURE is **RH-neutral** — it holds verbatim for an RH-false function. S(s) faithfully
   *reflects* the zeros as resonances; it does **not force** them onto the line.

Conclusion (and the next stone): self-adjointness/unitarity is necessary but RH-neutral — exactly the
Lax–Phillips obstruction, made precise. The RH content is the **forcing**: a positivity that *pins*
the scattering resonances to Re s = ¼, which the off-line-zero function must fail. It must be
**Euler-product-borne** (the only thing ζ has that the RH-false function lacks). Building that
positivity functional on S(s) — the conformal-geometric / Weil-positivity forcing — is stone two.

Run:  python3 -m scripts.numerics.witness.scattering
"""
from __future__ import annotations

import mpmath as mp


def Lam(s):
    """Completed zeta Λ(s) = π^{-s/2} Γ(s/2) ζ(s) = archimedean Γ_ℝ × Euler product."""
    s = mp.mpc(s)
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def S(s):
    """The conformal-boundary scattering operator S(s) = Λ(2s-1)/Λ(2s)."""
    s = mp.mpc(s)
    return Lam(2 * s - 1) / Lam(2 * s)


def _planted(rho0):
    """An FE-symmetric factor g(s)=g(1-s) with an off-line zero quadruple at rho0,1-rho0,conj —
    the RH-false control."""
    rho0 = mp.mpc(rho0)
    def g(s):
        s = mp.mpc(s)
        return (s - rho0) * (s - (1 - rho0)) * (s - mp.conj(rho0)) * (s - (1 - mp.conj(rho0)))
    return g


def S_offline(s, rho0=mp.mpc(0.8, 10.0)):
    """Scattering matrix of ζ times an off-line-zero factor (functional equation preserved)."""
    g = _planted(rho0)
    s = mp.mpc(s)
    L = lambda z: Lam(z) * g(z)
    return L(2 * s - 1) / L(2 * s)


def summary():
    mp.mp.dps = 30
    print("S(s) = Λ(2s-1)/Λ(2s) -- the conformal-boundary scattering operator\n")

    rho1 = mp.mpc(0.5, 14.134725141734693)
    sres = rho1 / 2
    print(f"(1) resonances = zeros: pole at s = ρ₁/2 = {complex(sres)} (Re = {float(sres.real):.4f})")
    for d in [1e-2, 1e-3, 1e-4]:
        print(f"      |S(s_res + {d:.0e})| = {float(abs(S(sres + d))):12.1f}   (pole)")

    print("\n(2) unitary on the critical line (only the functional equation is used):")
    for t in [3.0, 10.0, 25.0]:
        print(f"      |S(½ + {t:4.1f} i)| = {float(abs(S(mp.mpc(0.5, t)))):.10f}")

    print("\n(3) KILL-TEST -- off-line zero (RH-false), functional equation preserved:")
    rho0 = mp.mpc(0.8, 10.0)
    for t in [3.0, 10.0]:
        print(f"      |S_offline(½ + {t:4.1f} i)| = {float(abs(S_offline(mp.mpc(0.5, t)))):.10f}   (still 1: unitarity RH-NEUTRAL)")
    so = rho0 / 2
    print(f"      but pole at s = ρ₀/2 = {complex(so)} (Re = {float(so.real)} ≠ ¼): |S_offline(s+1e-3)| = {float(abs(S_offline(so + 1e-3))):.1f}")
    print("\n  => S reflects the zeros but does NOT force them. The forcing (pin resonances to Re=¼)")
    print("     is the Euler-product-borne bulk positivity -- stone two.")


if __name__ == "__main__":
    summary()
