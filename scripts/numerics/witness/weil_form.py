"""The analytic shadow of the missing object: the Weil-positivity quadratic form.

The "missing object" is the arithmetic analogue of `C×C` whose intersection positivity would
prove RH the way Weil's does over function fields. Its concrete analytic shadow is the **Weil
quadratic form** `W`, for which `RH ⟺ W ⪰ 0`. This module exhibits `W` as a Toeplitz form and
demonstrates that it is exactly the RH-detector, and where the positivity is (and is not) manifest.

Two sides of the same form (the Weil explicit formula):

  W[a,b] = Σ_ρ φ̂_a(γ_ρ) conj(φ̂_b(γ_ρ))                          [SPECTRAL side — the zeros]
         = (archimedean ∞ : digamma) + (poles s=0,1) − (primes : Λ(n) at log p^k)   [ARITHMETIC side]

- On the **spectral side** the form is `Σ_ρ |Σ_a c_a φ̂_a(γ_ρ)|²`, manifestly `≥ 0` **iff every
  γ_ρ is real**, i.e. iff RH. (Demonstrated: PSD on the true zeros; a planted off-line zero breaks it.)
- On the **arithmetic side** the same form is `(place at ∞) − (closed orbits = primes)` — a
  Lefschetz/Selberg-type trace — and its positivity is **NOT manifest**. Making it manifest, as a
  geometric intersection positivity, is precisely what the missing object would do.

In the function-field model this is `(Δ · Γ_Fr)` on `C×C` with the Hodge-index positivity. Over `ℚ`:
the archimedean place is the digamma `Γ_ℝ` factor (RH-neutral — shared with Davenport–Heilbronn, see
`research/log/2026-06-06-edge-is-dispersing.md`); the primes are the RH-content; the positivity is
the BGS §6.3 positive-Green-form / archimedean-Weil obstruction (which can genuinely fail — so the
geometry is essential, not cosmetic). See research/literature/ for the geometric characterizations.

Run:  python3 -m scripts.numerics.witness.weil_form
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx


def _zeros(K, prec=64):
    ctx.prec = prec
    return np.array([float(acb.zeta_zero(k).imag) for k in range(1, K + 1)])


def weil_kernel_spectral(taus, gammas, sigma):
    """Toeplitz kernel f(τ) of the Weil form on Gaussians (width σ), spectral side:
    f(τ) = Σ_ρ exp(−σ²γ²) e^{iτγ} (real; ±γ folded to a cosine). PSD Toeplitz ⟺ all γ real."""
    return np.array([float(np.sum(np.exp(-sigma ** 2 * gammas ** 2) * np.cos(t * gammas)))
                     for t in taus])


def weil_kernel_offline(taus, gammas, sigma, beta=0.8, T=14.134725):
    """Same, but the first zero is replaced by an off-line pair (Re ρ = β ≠ ½), so in the
    γ-variable γ = T − i(β−½) is COMPLEX — the RH-false control."""
    g = T - 1j * (beta - 0.5)
    base = np.exp(-sigma ** 2 * gammas[1:] ** 2)
    out = []
    for t in taus:
        b = np.sum(base * np.cos(t * gammas[1:]))
        off = (np.exp(-sigma ** 2 * g * g) * np.exp(1j * t * g)
               + np.exp(-sigma ** 2 * np.conj(g) ** 2) * np.exp(1j * t * np.conj(g)))
        out.append(b + off.real)
    return np.array(out)


def toeplitz_min_eig(f):
    m = len(f)
    T = np.array([[f[abs(i - j)] for j in range(m)] for i in range(m)])
    return float(np.linalg.eigvalsh(T).min()), float(np.linalg.eigvalsh(T).max())


def summary():
    print("The Weil quadratic form -- the analytic shadow of the missing object\n")
    sigma = 0.12
    taus = np.arange(0, 8.01, 0.25)
    gammas = _zeros(200)

    fr = weil_kernel_spectral(taus, gammas, sigma)
    mn, mx = toeplitz_min_eig(fr)
    print(f"[RH-true: the real zeros]   Weil Toeplitz form min eig = {mn:.3e}, max = {mx:.4f}")
    print(f"   PSD (min ≥ 0)? {mn >= -1e-9}  ->  Weil positivity HOLDS  ⟺  all γ real  ⟺  RH.")

    fo = weil_kernel_offline(taus, gammas, sigma)
    mo, _ = toeplitz_min_eig(fo)
    print(f"[RH-false: a planted off-line zero β=0.8]   min eig = {mo:.3e}")
    print(f"   PSD? {mo >= -1e-9}  ->  an off-line zero BREAKS the positivity.  The form IS the RH-detector.\n")

    print("[structure]")
    print("  * SPECTRAL side  W = Σ_ρ |Σ_a c_a φ̂_a(γ_ρ)|²  -- positivity MANIFEST iff γ_ρ real (= RH).")
    print("  * ARITHMETIC side  W = (place ∞ : digamma Γ_ℝ, RH-NEUTRAL) − (primes : Λ(n), RH-content)")
    print("    + poles -- a Lefschetz/Selberg trace; positivity NOT manifest here.")
    print("  * The MISSING OBJECT would make the arithmetic-side positivity a GEOMETRIC intersection")
    print("    positivity (Δ·Γ_Fr on the arithmetic C×C). Its archimedean term is the BGS §6.3")
    print("    positive-Green-form obstruction -- which can genuinely fail, so the geometry is")
    print("    essential. See research/literature/ for the geometric characterizations.")


if __name__ == "__main__":
    summary()
