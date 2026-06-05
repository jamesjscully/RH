# Jensen real-data path — 2026-06-05

Continued the descent evaluation onto the *real* Jensen proof structure (GORZ,
arXiv:1902.07321), not a toy. `jensen_real.py`.

## The real slack: Hermite stability radius

GORZ models the rescaled Jensen polynomial `J_{d,n}` by the Hermite polynomial `H_d` and
proves hyperbolicity once the (all-orders) asymptotic coefficient error is within the
**stability radius of Hermite hyperbolicity**, `ρ(d)`. That `ρ(d)` is the method's real
slack. Computed from real Hermite data (smallest coefficient perturbation of `H_d` that
creates a non-real root, minimized over directions), `d = 2..16`:

```
ρ(2)=5.7e-1  ρ(4)=1.8e-1  ρ(6)=2.1e-2  ρ(8)=1.7e-3  ρ(10)=1.4e-4
ρ(12)=9.6e-6  ρ(14)=5.7e-7  ρ(16)=3.2e-8
```

Decay fit: **`ρ(d) ~ e^{−1.22 d}` (exponential, residual 0.52)** vs `d^{−8.2}` (residual
1.93) — exponential dominates. So the slack vanishes **exponentially** in degree. This is
exactly the "analysis has to be almost perfect — too much slack anywhere and you're dead,"
quantified; and it explains the `n ≥ c·e^d` matching threshold (the asymptotic error, a
power of `1/n`, must beat `e^{−1.22 d}` ⇒ `n` exponential in `d`).

## The structural test on the real diamond

Per degree, the finite check (cert) and the asymptotic (tail) both derive from the same
`ξ`-coefficient source, reconciled by the bridge — a **diamond** (4-cycle):

- filled diamond (overlaps consistent — a *correct* proof): `H¹ = 0`;
- hollow diamond (only pairwise consistent — a *gap*): `H¹ = 1`.

A correct Jensen proof therefore has `H¹ = 0`. The slack ratio across adjacent degrees is
`ρ(8)/ρ(9) = 2.68 ≠ 1`.

## Verdict (real data)

- **Descent topology is decoration here too**, exactly as for NB-BD: a correct proof's
  diamonds are filled → `H¹ = 0`. The cohomology is the wrong instrument. The stacks/descent
  instinct pointed at the right *shape* but the obstruction does not live in the constant-
  coefficient `H¹`.
- **The obstruction is metric.** `ρ(d) → 0` exponentially — the slack marginally vanishes
  (a `Λ = 0`-type phenomenon), which is a *rate*, not a gluing class. This confirms
  STRATEGY §3/§4: the load-bearing structure is the **metric enrichment** (the slack-decay
  rate), never the topology.
- **The forcing-structure question, made precise:** can the asymptotic coefficient error be
  driven below `ρ(d) ~ e^{−1.22 d}` **uniformly in `d`**? That is exactly the reverse-force
  content, and it is RH-hard precisely where `ρ(d) → 0`. No descent/cohomology machinery
  shortcuts it; the decisive object is the quantitative error-vs-`ρ(d)` rate.

## Consequence for the program

This closes the "could stacks/descent help?" thread with a clean, honest negative on the
topology and a positive on the diagnosis: **point effort at the metric (slack-decay rate),
not the descent topology.** The next concrete target is a *uniform-in-`d`* bound on the
`ζ^{(2n)}(½)` asymptotic error against `ρ(d)` — and to keep it honest, that bound must be a
certified inequality (STRATEGY §8), since it is the candidate spine.
