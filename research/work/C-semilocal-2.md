# C — Semilocal {∞,2} Weil positivity: the minimal place-crossing (worker C, 2026-06-06)

**Task.** Build the Weil explicit-formula functional restricted to `S={∞,2}`,
`W_S(g) = W_∞(g) + W_2(g)` with `W_2 = 2 Σ_{k≥1} log2 · 2^{−k/2} g(k log2)` the `(1−2^{−s})`
Euler-factor log-derivative, as a quadratic form on positive-type test functions supported
in `u=log x ∈ (−log2, log2)`. Test thread 0's knife-edge (archimedean form goes indefinite,
`p=2` restores it, `<10⁻³` sensitivity) and run the Davenport–Heilbronn (DH) kill-test.

Module: `scripts/numerics/witness/semilocal_2.py` (python-flint + numpy). Run:
`python3 -m scripts.numerics.witness.semilocal_2`.

---

## 0. Convention, pinned and verified

The Weil explicit formula for ζ, `g` even, `ĝ(t)=∫g(u)e^{iut}du`:

```
  Σ_ρ ĝ(γ_ρ)  =  [ĝ(i/2)+ĝ(−i/2)]            (poles s=0,1)
              −  P(g)                          (primes)
              +  W_∞(g)                        (archimedean)
  P(g)     = 2 Σ_{p,k≥1} (log p) p^{−k/2} g(k log p)
  W_∞(g)   = −g(0) log π + (1/2π) ∫ ĝ(t) Re ψ(¼ + it/2) dt
```

Verified numerically against `acb.zeta_zero`: for a Gaussian `g`, `Σ_ρ ĝ(γ) = Poles − P + W_∞`
to residual **−4e-13** (`verify_explicit_formula`). So the `W_∞`/`P` signs below are the
correct Weil convention. The task's `W_2 = +2 Σ log2·2^{−k/2} g(k log2)` is, in this
convention, exactly the bare `p=2` prime term; on the positive (spectral) side it is
**subtracted**: `Q = W_∞ − P_2 − P_other`.

**The reliable route (spectral side).** For `g = h⋆h*(−·)`, `ĝ=|ĥ|²≥0`, the spectral side
`Q(h)=Σ_ρ|ĥ(γ_ρ)|²` is a **manifest sum of squares ⇒ PSD**. Killing the poles by the
Sonin/Fourier-vanishing constraints `ĥ(0)=ĥ(±i/2)=0` leaves `Q = W_∞ − P`. I build `Q` as a
Gram matrix over a basis of **compactly-supported even raised-cosine bumps**
`φ_c(u)=cos²(π(u−c)/2hw)` (closed-form transform), project onto the constraint null space,
and compare its min eigenvalue to the archimedean-only form and to the directly-summed
spectral Gram.

**Crucial support fact (the place bookkeeping).** `g = h⋆h*` has support up to
`gmax = 2(c_max+hw)` — the **convolution reaches twice as far** as a single bump. So
"support(g) ⊂ (½,2)" needs `c+hw ≤ log2/2`; and the clean `{∞,2}` window (p=2 active, p=3
*not*) is `gmax ∈ (log2, log3)`. The Gram identity `pr(Q) = pr(Spec)` closes to **~3e-8**
once *every* reachable prime power is included — this caught and fixed an early bug where
only `p=2` was summed while the convolution support reached `log3`.

---

## 1. Is `W_{∞,2} ⪰ 0` for ζ?  **Yes — and so is `W_∞` alone, here.**

On the Fourier-vanishing (Sonin) subspace, across `gmax` swept from `log2` past `log3`
(7–20 bumps, `hw` 0.06–0.22):

| object | min eigenvalue (typical) | PSD? |
|---|---|---|
| spectral `Σ_ρ|ĥ(γ)|²` (sum of squares) | `+5e-5 … +4e-4` | **yes** (always, by construction) |
| `Q = W_∞ − P_2 − P_other` | `= spectral` to ~1e-7 | **yes** |
| `W_∞` alone (archimedean) | `+1.8e-4 … +4.8e-4` | **yes** |

So **`W_{∞,2} ⪰ 0` for ζ — confirmed.** The identity `Q = spectral` closes, so the
construction is correct.

## 2. The knife-edge: does `p=2` restore an archimedean indefiniteness?  **No (in this form).**

**`W_∞` alone does NOT go indefinite** on support reaching the first prime, at any basis I
could resolve (incl. 20 bumps, `hw=0.06`, high-frequency content). The reason is structural:
`Q = W_∞ − P_2 − P_other = spectral ≥ 0`, hence `W_∞ = spectral + (P_2+P_other)`. The prime
defect `P_2+P_other = W_∞ − spectral` is **itself indefinite** (eigs `−0.10 … +0.11`), so the
`p=2` term genuinely *redistributes* in the form — but `W_∞` never drops below the (already
PSD) spectral value at this support. The `p=2` term is a **`~10⁻⁵`–`10⁻⁴` correction that
brings `W_∞` DOWN to the smaller true value**, not a sign-flipping rescue of a negative `W_∞`.

This is an **honest negative on the dramatic reading** of thread 0's claim. CC20's "`W_∞`
loses positivity on intervals, restored only by `p=2`" is about their *specific* prolate/
Sonin compression `Tr(ϑSϑ*)` and a delicate interval/derivative-jump (`δ'` jumps `−1→+1` at
`ρ=1`), **not** the natural Gram-form restriction to the vanishing subspace, where the
archimedean form is already ≥ spectral ≥ 0. The naive semilocal form does **not** reproduce
the knife-edge; the rescue lives in CC20's compression, not in `W_∞ − P_2` as a Gram form.

**The `<10⁻³` sensitivity IS confirmed — in the recovery sense.** Replacing the prime by
`2(1+δ)` and measuring `|spectral − (W_∞ − P_{2(1+δ)})|` (how well the true PSD form is
recovered):

| δ | `|spectral − (W_∞ − P_{2(1+δ)})|` |
|---|---|
| −0.01 | 1.6e-3 |
| −1e-3 | 1.5e-4 |
| **0** | **2.9e-8** (exact prime) |
| +1e-3 | 1.5e-4 |
| +0.01 | 1.4e-3 |

The recovery is sharp at δ=0 and degrades **linearly off the exact prime, an order of
magnitude per decade of δ** — only the integer prime `p=2` makes `W_∞ − P_2` equal the true
spectral form. This quantitatively matches thread 0 / CC20's `<10⁻³`-window report, located
in the *form-recovery* sense rather than a sign flip.

## 3. DH KILL-TEST: the form SEES the Euler product, but positivity does NOT yet discriminate.

DH shares ζ's `Γ_ℝ` (same `W_∞`) but has **no Euler product**: its prime-side coefficients
`c_DH(n)` (from `−Z'/Z`, computed in `explicit_formula.py`) are **not** von Mangoldt —
`c_DH(2)=0.197 ≠ log2=0.693`, and `c_DH(4)=−1.44` (negative, off prime-power support). I
built DH's semilocal form `W_∞ − P_DH` with these **actual** coefficients:

| support `gmax` | ζ: `W_∞−P_ζ` (=spectral) | DH: `W_∞−P_DH` | difference |
|---|---|---|---|
| 0.92 | +6.00e-5 | +6.25e-5 | −2.4e-6 |
| 1.10 | +2.06e-4 | +2.00e-4 | +5.9e-6 |
| 1.24 | +2.90e-4 | +2.56e-4 | +3.4e-5 |

- **The forms are provably different** (difference up to `3.4e-5`, tracking `Λ(2)` vs
  `c_DH(2)` exactly) — the place-crossing object **registers the Euler product**.
- **But both stay PSD** — DH's coefficient perturbation is too small to flip the min
  eigenvalue negative at `S={∞,2}`. The discrimination is in the **value**, not the **sign**.

So: **`W_{∞,2}` is positive for ζ AND positive for DH** at this support. It does *not*
discriminate by positivity. (Consistent with `li_positivity.py`: DH's positivity failure
shows up at Li-coefficient index `n≈521`, i.e. from *many* primes / high frequency — a single
prime at one place is far from enough.)

---

## 4. Verdict — honest

**Is semilocal `{∞,2}` positivity a genuine discriminating step?  Not yet — it is RH-neutral
*by positivity* at this place, though it is the first object that *registers* the Euler
product in its matrix entries.**

1. **`W_{∞,2} ⪰ 0` for ζ: YES** (verified, = spectral sum of squares).
2. **`p=2` restores an archimedean indefiniteness: NO** in the natural Sonin-Gram form —
   `W_∞` alone is already ≥ spectral ≥ 0; `p=2` is a `~10⁻⁴` *downward* correction, not a
   rescue. The dramatic knife-edge is an artifact of CC20's *specific compression*
   `Tr(ϑSϑ*)`, not of `W_∞−P_2` as a quadratic form. **Honest negative.**
3. **`<10⁻³` sensitivity: CONFIRMED** in the form-recovery sense — only the exact prime `p=2`
   recovers the true PSD spectral form, degrading ~1 order/decade of δ.
4. **DH kill-test: the form DIFFERS for DH (sees the Euler product) but both stay PSD** —
   no positivity discrimination at `{∞,2}`. The Euler product enters the *values* but the
   *sign* needs more places / higher frequency (cf. Li index `n≈521`).

**Why this is the expected, non-overclaimed outcome.** It re-confirms the program's standing
lesson (positivity-program.md §E): one archimedean place + one prime is the *minimal* crossing
but the prime perturbation is `O(10⁻⁴)` against an `O(1)` archimedean form — far too weak to
flip a sign. The Euler product is **present in the form** (the matrices provably differ from
DH) but **not yet load-bearing for positivity**. This neither advances nor refutes RH; it
pins the place where the difference first becomes *visible* (the matrix entries) versus where
it would become *forcing* (the sign), and shows those are not the same place.

## 5. Most concrete next step

The discrimination is in the **value gap** `‖P_ζ − P_DH‖`, which grows with the number of
places and the frequency content. Two on-ramps, in order:

- **(C′) `{∞,2,3,5,…}` accumulation — find the place-count `|S|` at which the
  von-Mangoldt-vs-`c_DH` value gap first drives the semilocal min eigenvalue negative for DH
  while ζ stays PSD.** This is the direct continuation: sweep `S` and watch
  `min eig(W_S^{ζ}) ≥ 0` vs `min eig(W_S^{DH}) < 0` cross. (Li `n≈521` suggests this needs
  *many* primes — quantify the onset.) Reuses `semilocal_2.build_gram` with `primes=(2,3,5,…)`
  and DH coefficients from `explicit_formula.log_deriv_coeffs`.
- **(deferred) The equivariance obstruction.** Even where positivity holds, it rests on the
  scale-breaking Fourier-vanishing/Sonin cutoff (the constraint null space here). The cutoff
  is exactly what makes `W_∞ ≥ spectral` (it *adds* the pole/UV mass). Removing it — a single
  scale-invariant operator reproducing the Sonin compression — is CC20's announced-but-undone
  metaplectic target and the real wall; numerics can only probe, not resolve it.

**Net for the program tracker:** semilocal `{∞,2}` is the first object that **carries the
Euler product in its quadratic form** (matrices differ from DH, tracking `Λ` vs `c_DH`), but
its **positivity is still RH-neutral** (PSD for both ζ and DH). The forcing is a *value gap*
that must *accumulate over places* before it becomes a *sign*. Direction C is alive but
demands `|S|` growth, not a single prime.
