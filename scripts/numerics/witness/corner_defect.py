"""The corner, made concrete: the archimedean fixed point as a Coulomb singularity.

The "missing object" (the arithmetic C×C) breaks at the archimedean **corner** ∞×∞ — the fixed
point of the scaling flow, `u = 0` (`ρ = 1`) — where the diagonal self-intersection `Δ·Δ` diverges
(BGS §6.3 / Connes–Consani's "small square"). This module makes that corner a concrete, computable
object and exhibits the tropical↔spectral fusion at it.

Two computed facts:

1. **The corner is a divergence of the archimedean Weil functional at the fixed point.** As a test
   function localizes (width `ε → 0`) at `u = 0`, the archimedean Weil functional `W_∞` DIVERGES;
   localized off the fixed point (e.g. at a prime `u = log p`) it CONVERGES. So the RH-relevant
   trouble is entirely at the archimedean fixed point — the corner.

2. **The corner kernel is Coulomb: `K_∞(u) ~ −1/(2|u|)` as `u → 0`.** The archimedean Weil
   distribution `K_∞(u) = (1/2π)∫ Re ψ(¼ + it/2) e^{−iut} dt` has, from the `log|t|` growth of the
   digamma, a `−1/(2|u|)` singularity at the fixed point (verified: `K_∞(u)·|u| → −½`). Hence
   `Δ·Δ = ∫ K_∞` near `0` is **log-divergent** (`~ −log ε`): the diagonal's self-intersection at the
   archimedean place is `−∞` (the "infinite arithmetic genus").

**The fusion (tropical ↔ spectral) — and the honest correction.** A `−1/|u|` (scale-invariant /
conformal) kernel at the fixed point is the locus where one would *hope* to make the scaling/dilation
Hamiltonian self-adjoint (Berry–Keating `xp`; the naive Hilbert–Pólya hope: compactify the corner ⟺
choose a self-adjoint extension). **That hope is false in the actual construction.** Connes–Consani
(2006.13771) show the corner cutoff (the `Λ=1` prolate/Sonin projection that compactifies the corner)
*"lack[s] invariance under the scaling action"* and *"the scaling action ϑ does not restrict to
[Sonin's] space"* — so the self-adjoint restriction is **obstructed, not chosen**. They retreat to a
**positive projection `S`**, giving the *weaker* "corner cutoff ⟹ `Tr(ϑ(g)Sϑ(g)*) ≥ 0`", not a
self-adjoint generator with spectrum = the zeros. See research/literature/geometry-of-the-square.md §2.

So the precise, corrected picture: the tropical `Δ·Δ` divergence and the spectral side **meet at this
`−1/(2|u|)` corner kernel**, but "corner-compact AND self-adjoint" is exactly the pair that is in
**tension** — the cutoff that tames the corner breaks the invariance needed for self-adjointness. That
tension *is* the difficulty; the reverse force would be a construction achieving both at once, and none
exists. RH-signed `Δ·Δ` on the square (equiv. a genuine self-adjoint generator) is the open
BGS §6.3 / Hilbert–Pólya question. This module computes the corner; it does not resolve the tension.

Run:  python3 -m scripts.numerics.witness.corner_defect
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx


def _repsi(t):
    return float(acb(0.25, t / 2).digamma().real)


def archimedean_functional(eps, u0, T=400.0, N=120001):
    """W_∞ on an even Gaussian of width eps at ±u0:  −g(0)logπ + (1/2π)∫ e^{−ε²t²/2} cos(u0 t) Reψ dt."""
    ts = np.linspace(-T, T, N)
    dt = ts[1] - ts[0]
    ps = np.array([_repsi(t) for t in ts])
    g0 = np.exp(-u0 ** 2 / (2 * eps ** 2)) / (eps * np.sqrt(2 * np.pi))
    integ = np.sum(np.exp(-eps ** 2 * ts ** 2 / 2) * np.cos(u0 * ts) * ps) * dt / (2 * np.pi)
    return -g0 * np.log(np.pi) + integ


def corner_kernel(u, T=2000.0, N=400001):
    """K_∞(u) = (1/2π)∫ Reψ(¼+it/2) e^{−iut} dt, via smooth remainder + analytic FT of the log."""
    ts = np.linspace(-T, T, N)
    dt = ts[1] - ts[0]
    rho = np.array([_repsi(t) - 0.5 * np.log(1 / 16 + t * t / 4) for t in ts])
    ksmooth = np.sum(rho * np.cos(u * ts)) * dt / (2 * np.pi)
    klog = (1 / (2 * np.pi)) * 0.5 * (-(2 * np.pi / abs(u)) * np.exp(-abs(u) / 2))
    return ksmooth + klog


def summary():
    print("The corner, concretely: the archimedean fixed point as a Coulomb singularity\n")
    print("[1] W_∞ DIVERGES at the fixed point (u0=0), CONVERGES off it (u0=log2≈0.69):")
    print("   ε       u0=0 (corner)    u0=0.69 (off)")
    for eps in [0.5, 0.25, 0.125, 0.0625, 0.03125]:
        print(f"   {eps:.5f}   {archimedean_functional(eps, 0.0):+8.3f}        {archimedean_functional(eps, 0.69):+7.4f}")

    print("\n[2] corner kernel K_∞(u) ~ −1/(2|u|) (Coulomb); K_∞(u)·|u| → −½:")
    print("    u      K_∞(u)     K_∞(u)·|u|")
    for u in [0.1, 0.2, 0.4, 0.8]:
        k = corner_kernel(u)
        print(f"   {u:.2f}   {k:+.4f}     {k * abs(u):+.4f}")

    print("\n[fusion -- corrected] the −1/(2|u|) corner kernel is where the tropical Δ·Δ divergence and")
    print("  the spectral side MEET. But 'corner-compact AND self-adjoint' is a TENSION, not an identity:")
    print("  Connes–Consani show the cutoff that compactifies the corner breaks the scaling invariance,")
    print("  so the self-adjoint restriction is OBSTRUCTED — they retreat to a positive projection S")
    print("  (Tr(ϑSϑ*)≥0), NOT a self-adjoint generator with spectrum=zeros. That tension is the")
    print("  difficulty; the reverse force (a construction with both at once) is the open BGS §6.3 /")
    print("  Hilbert–Pólya question. (geometry-of-the-square.md §2) This module locates; it does not resolve.")


if __name__ == "__main__":
    summary()
