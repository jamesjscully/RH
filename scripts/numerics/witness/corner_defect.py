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

**The fusion (tropical ↔ spectral), now precise.** A `−1/|u|` (scale-invariant / conformal) kernel
at the fixed point is exactly the locus where the **scaling/dilation Hamiltonian needs a self-adjoint
extension** (conformal quantum mechanics; Berry–Keating `xp`; Connes' scaling operator). So:

  *compactify the corner* (regularize the `−1/(2|u|)` / the log-divergent `Δ·Δ`)
      ⟺  *choose a self-adjoint extension* (a boundary condition at `u=0`) of the scaling operator.

"Corner compact ⟺ spectrum self-adjoint" is therefore **one object seen twice**: the tropical
diagonal self-intersection `Δ·Δ` and the spectral self-adjointness defect are both governed by the
same `−1/(2|u|)` corner kernel. RH = the extension whose spectrum is the zeros (equivalently the
regularization that makes `Δ·Δ` give the Hodge-index sign). This is a precise *location* of the
fusion, not a proof — the extension/sign is the open BGS §6.3 / Hilbert–Pólya question.

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

    print("\n[fusion] the −1/(2|u|) corner kernel is the scale-invariant (conformal) locus where the")
    print("  scaling Hamiltonian needs a self-adjoint extension. Compactifying the corner (regularizing")
    print("  Δ·Δ ~ −log ε) ⟺ choosing that extension (a boundary condition at u=0). The tropical Δ·Δ and")
    print("  the spectral self-adjointness defect are ONE object — the corner kernel. RH = the extension")
    print("  whose spectrum is the zeros. [precise location of the fusion; the extension is BGS §6.3-open]")


if __name__ == "__main__":
    summary()
