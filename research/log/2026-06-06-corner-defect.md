# The corner, made concrete — and the tropical↔spectral fusion located — 2026-06-06

> **CORRECTION (same day, from the geometry deep-dive).** The "fusion = self-adjoint extension"
> framing below is the *naive* hope and is **false in the actual construction**: Connes–Consani show
> the corner cutoff breaks the scaling invariance, so self-adjointness is **obstructed, not chosen**;
> they retreat to a positive projection. The corrected picture (corner-compact vs self-adjoint are in
> **tension**, not identity) is in `research/literature/the-fusion.md` and the updated
> `corner_defect.py`. The *computed* facts below (corner divergence; `−1/(2|u|)` kernel; log-divergent
> `Δ·Δ`) stand and match CC20's `δ'`-jump at `ρ=1`.

Path 1 of the fusion thread (`scripts/numerics/witness/corner_defect.py`). Goal: turn "the corner"
from a phrase into a computed object, and see whether the tropical `Δ·Δ` and the spectral self-
adjointness defect are literally the same thing.

## Two computed facts

1. **The corner is a divergence at the archimedean fixed point.** As a test function localizes
   (width `ε→0`) at `u=0` (`ρ=1`), the archimedean Weil functional `W_∞` **diverges** (the digamma
   part climbs `−0.74 → +27`, the total `→ +12` by `ε=0.03`); localized at a *prime* location
   `u=log 2` it **converges** (`→ −0.95`). So the RH-relevant trouble is entirely at the archimedean
   fixed point — the corner — not at the primes.
2. **The corner kernel is Coulomb.** `K_∞(u) = (1/2π)∫ Reψ(¼+it/2)e^{−iut}dt ~ −1/(2|u|)` as `u→0`
   (verified: `K_∞(u)·|u| → −½`, from the `log|t|` growth of the digamma). Hence the diagonal
   self-intersection `Δ·Δ = ∫K_∞` near `0` is **log-divergent, `~ −log ε`** — the diagonal's
   archimedean self-intersection is `−∞` ("infinite arithmetic genus").

## The fusion, located precisely

A `−1/|u|` (scale-invariant / conformal) kernel at the fixed point is exactly the locus where the
**scaling/dilation Hamiltonian needs a self-adjoint extension** (conformal quantum mechanics;
Berry–Keating `xp`; Connes' scaling operator). Therefore:

> **compactify the corner** (regularize `−1/(2|u|)` / the log-divergent `Δ·Δ`)
>   ⟺  **choose a self-adjoint extension** (a boundary condition at `u=0`) of the scaling operator.

So "corner compact ⟺ spectrum self-adjoint" is **one object seen twice**: the tropical diagonal
self-intersection `Δ·Δ` and the spectral self-adjointness defect are both governed by the *same*
`−1/(2|u|)` corner kernel. RH = the extension whose spectrum is the zeros (equivalently, the
regularization that gives `Δ·Δ` the Hodge-index sign).

## Honest status

This is a **precise location** of the fusion, not a proof. What it adds: the fusion is no longer a
slogan — both sides are the conformal corner kernel `−1/(2|u|)`, and the open question is sharply
named: **which self-adjoint extension / boundary condition at the fixed point** (equivalently, which
regularization of `Δ·Δ`) is realized — the BGS §6.3 / Hilbert–Pólya / Berry–Keating question. The
characterization did not hand us the extension; it handed us the precise object whose extension is RH.
