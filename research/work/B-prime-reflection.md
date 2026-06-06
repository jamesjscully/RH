# Worker B — the prime-place reflection / adelic Hankel form (2026-06-06)

*(§8 discipline: [THM] proven, [PROG] partial, [CONJ] conjecture, [AN] analogy. The SPECTRAL side
of the Weil form is the PSD-certified reliable one (`weil_form.py`); the non-even Toeplitz prime
convention has bitten us, so every prime-side claim below is cross-checked against the spectral side
and swept over width/basis/truncation. Module: `scripts/numerics/witness/prime_reflection.py`.)*

**Task.** Thread 1's lead: reflection positivity (OS/QFT) is RH-neutral UNLESS the reflection acts on
the PRIME places. Build the Weil form `W = W_∞ + Σ_p W_p` as a Gram/Hankel matrix split by place;
search for a prime-place involution `θ` making `W(h,h) = ⟨θh,h⟩` an OS pairing; kill-test against
Davenport–Heilbronn (FE, no Euler product); and (bonus) test the Thread-6 trace=scattering bridge.

---

## 1. The adelic Hankel structure (what `W` actually is)

Work with **even** test functions `h(u)=h(−u)` on the multiplicative line `u = log x ∈ ℝ`, in the
basis of even Gaussians `φ_a` centred at `±t_a`. The Weil explicit formula splits by place:

```
  Σ_ρ ĥ(γ_ρ)  =  [poles s=0,1]  +  W_∞[h]  −  Σ_{n≥2} Λ(n)/√n · h(log n)
                                   └ archimedean ┘   └────── primes ──────┘
```

Polarising on the basis gives a real symmetric **Gram/Hankel matrix** `W[a,b]` (CC20: the Weil
functional *is* a Hermitian Toeplitz/Hankel positivity problem). The split is explicit:

- **`W_∞` (digamma block).** The archimedean `Γ_ℝ` term. RH-neutral — identical for ζ and DH (both
  have the same `Γ_ℝ`). Not the discriminator. (Not recomputed here; its RH-neutrality is the
  program's standing finding.)
- **`W_p` (prime blocks).** Each prime place contributes
  `W_p[a,b] = Σ_k (Λ(p^k)/p^{k/2}) φ_a(k log p) φ_b(k log p) = P_p · P_pᵀ`,
  where `P_p[a] = √(Λ(p^k)/p^{k/2}) φ_a(k log p)` **samples** the test function on the log-prime-power
  lattice `u = k log p`. **This is the adelic Hankel structure:** each place `p` is a low-rank
  **Gram block** `W_p = P_p P_pᵀ`, manifestly PSD **because `Λ(p^k) ≥ 0`** — i.e. *because of the
  Euler product*. [verified — module §2: ranks 5/4/3 for p=2/3/5, all PSD; full prime block
  min eig `+5.2e-3` over 589 prime powers, robustly PSD across `σ∈{0.25,0.35,0.5}` and basis sizes.]

Sign note: in the explicit formula the prime sum enters with a **minus**, so the prime places
*resist* positivity and the archimedean place must dominate them — CC20's `W_∞ ≥ Σ_p W_p ≥ 0`. The
PSD-ness of `Σ_p W_p` is exactly the Euler-product content.

The **spectral side** is the certified RH-detector and is reproduced here only as a cross-check;
the off-line kill-test on it is **deferred to `weil_form.py`** (sec. §8: don't reimplement the
spectral side). [verified — `weil_form` Toeplitz min eig: RH-true `−3.4e-16` (PSD), off-line β
`−1.49` (BREAKS). My even-Gaussian Gram off-line perturbation is Gaussian-*damped* (`exp(−σ²γ₀²)`
with `γ₀≈14` kills the off-line weight) and does NOT visibly break at moderate width — a known
limitation of that basis, flagged honestly in the module, not a contradiction.]

---

## 2. Is there a prime-place involution `θ`? — **No (negative result).**

Three candidate reflections, all checked:

1. **Multiplicative inversion `u ↦ −u`** (= `n ↔ 1/n`, the adelic `p^{-1}` flip). On the even basis
   this is the **identity**: `max|φ(u) − φ(−u)| = 0` exactly. [verified — module §3.] So the
   "adelic flip" reflection collapses `⟨θh,h⟩` to `⟨h,h⟩` — it is the **archimedean** reflection,
   the one Thread 1 already classified **RH-neutral**.
2. **Functional-equation reflection `s ↦ 1−s`.** Even test functions are already self-dual under it,
   so it acts trivially on this basis too.
3. **The Gram/Hankel "doubling" `W_p = P_p P_pᵀ`.** This is the only reflection genuinely *carried by
   the primes* — the OS-doubling whose "reflection" is the transpose `P_p ↔ P_pᵀ`. But its
   OS-positivity is **identically the statement `Λ(p^k) ≥ 0`** — there is **no extra OS involution
   beyond the sign of `Λ`**.

**Verdict on `θ`:** there is no *new* prime-place reflection. The only object that makes the prime
block a "reflection-positive square" is the Gram factorisation `W_p = P_p P_pᵀ`, and its positivity
is just the non-negativity of the von Mangoldt weights — the Euler product, re-skinned as a Hankel
form. The OS/reflection language adds **no forcing** the Euler product did not already supply.

---

## 3. KILL-TEST against Davenport–Heilbronn — **discriminates, but trivially (the Euler product, relabelled).**

DH has a functional equation but **no Euler product**; its `−Z'/Z` coefficients `c_DH(n)` take
**both signs** and are **not** prime-power supported (`explicit_formula.py`, Gate 1). The DH analogue
of the prime block is therefore

```
  W_DH[a,b] = Σ_n c_DH(n)/√n · φ_a(log n) φ_b(log n)
```

which is **not** of Gram form (the weights are signed), hence generically **indefinite**.

| object | prime-block min eig | PSD? | mechanism |
|---|---|---|---|
| ζ  `Σ_p W_p = P Pᵀ` | `+5.2e-3` (… `+1.3e-2`) | **yes** | `Λ(n) ≥ 0` (Euler product), Gram form |
| DH `Σ_n c_DH(n)…`   | `−0.66` (… `−0.98`)  | **no**  | `c_DH(n)` signed (no Euler product) |

[verified — robust across `σ∈{0.25,0.35,0.5}`, 6- and 13-point bases, DH truncations `N∈{200,400,800}`:
ζ PSD everywhere, DH min eig `≈ −0.6…−1.0` everywhere — large-signal, not numerical noise.]

**So the prime-block OS-positivity *does* discriminate ζ from DH.** But the §2 verdict is the catch:
the "reflection-positive object that discriminates" is **the Euler product itself** (`sign Λ`),
wearing a Hankel/Gram skin. It is **not** a new prime-place reflection whose OS-positivity is the
lever. This is the Thread-1 falsifier resolving to the *honest middle*: the construction does isolate
an OS-positive object that fails for DH (so it is **not** the dead, RH-neutral archimedean
reflection), but that object is the Euler-product positivity `Λ ≥ 0` we already had — **circular as a
forcing**, exactly the program's standing diagnosis that *only the Euler product discriminates, and a
positivity built on it for ζ that fails for DH does not, by itself, force RH*.

**Net verdict: RH-NEUTRAL as a new lever / circular as forcing — confirming Thread 1.** Reflection
positivity, pushed onto the primes, does not become a free positivity: the prime reflection either
collapses to the archimedean one (candidates i, ii — RH-neutral) or *is* the Euler product (candidate
iii — circular). This is the **6th confirmation** the audit predicted (Thread 1 §4 falsifier).

---

## 4. Thread-6 bridge (bonus) — the scattering-phase side *sees* the off-line zero.

Read `Q(f)` two ways and kill-test against `S_offline` (`scattering.py`, an off-line resonance with
the functional equation preserved):

- **(A) trace side** — the prime+arch explicit-formula trace (the `Σ_p W_p` block above; RH-content
  in the `Λ(n)` weights).
- **(B) Birman–Krein scattering-phase side** — the resonance count
  `N = (1/2π) ∮ d arg S(½+it)` over a window, the spectral-shift winding.

[verified — winding over `t∈[2,30]`: ζ gives `N = −12.96`; `S_offline` gives `N = −14.92`. The
off-line resonance adds an **anomalous winding `Δ ≈ −1.96`** — the phase side `(B)` *does* see the
off-line zero.]

**Reading.** Unlike unitarity `|S|=1` (which is RH-neutral, stone 1), the **winding / phase
derivative discriminates** — it counts resonances and an off-line resonance changes the count. So the
trace=scattering bridge is **not** RH-neutral at the level of the *count*. **But counting zeros is not
forcing them on-line:** the winding tells you a resonance left `Re=¼`, it does not supply a positivity
that forbids it. The forcing remains pinned to the same place as §3 — the **Euler-product positivity
of the prime block** (the cross-place term `W_∞ ≥ Σ_p W_p`). The bridge localises *where* DH differs
(an extra resonance crossing); it does not, by itself, close it. Consistent with Thread 6's verdict:
the merger localises the wall, it does not pass it.

---

## 5. Honest next step

The clean negative is informative: **no prime-place reflection `θ` exists beyond the Euler product
itself.** The OS/reflection framing buys nothing the sign of `Λ` did not already give. The live gap
is therefore *not* "find `θ`" but the original CC20 wall — **why `W_∞` (digamma) dominates `Σ_p W_p`
(the signed-for-DH prime blocks) for ζ and fails to for DH** — i.e. the **cross-place inequality**
`W_∞ ≥ Σ_p W_p`, which §3 shows is exactly where ζ and DH part (DH's prime block is indefinite, so no
single-place archimedean term can dominate it the CC20 way). Concrete next probe (Worker C's
semilocal `{∞,2}` target): compute the CC20 archimedean-vs-prime *margin* `W_∞[h] − Σ_p W_p[h]` on a
shared test family for ζ and for DH, and check whether the margin stays `≥ 0` for ζ but goes negative
for DH **at the `p=2` term specifically** (the §8.2 "knife-edge": the sign is restored only by the
exact prime `p=2`). That margin — not a reflection — is the Euler-borne object that has to do the
forcing. The module's `weil_prime_block` / `weil_prime_block_dh` give the `Σ_p W_p` side ready for
that subtraction.

---

## Auditor / tracker deltas (to fold into `positivity-program.md`)

- §C row "reflection positivity (OS/QFT)": **resolve the open prime-`θ`.** No prime-place reflection
  exists beyond the Gram doubling `W_p = P_p P_pᵀ`, whose OS-positivity **IS** the Euler product
  `Λ ≥ 0`. It discriminates ζ from DH (DH prime block indefinite, min eig `≈ −0.7`) but is **circular
  as forcing** — the OS skin adds nothing to `sign Λ`. **Thread 1 → confirmed RH-neutral/circular;
  the open object closed negatively.** (Live edge stays the CC20 cross-place margin `W_∞ ≥ Σ_p W_p`.)
- §B new row: `(QFT) OS reflection on prime places` over ℤ → **closes**: the only prime "reflection"
  is the Gram factorisation of the von Mangoldt weights; no involution beyond `sign Λ`; positivity
  collapses to the Euler product.
- Thread-6 delta: the Birman–Krein **winding** (phase, not modulus) *does* discriminate
  (ζ `N=−12.96` vs `S_offline` `N=−14.92`) — counts the off-line zero but does not force; forcing
  stays the cross-place prime-block term.

---

### Module
`scripts/numerics/witness/prime_reflection.py` — `weil_gram_spectral` (cross-check),
`spectral_offline_certified` (defers to `weil_form.py`), `weil_prime_block` / `weil_prime_block_dh`
(the `Σ_p W_p` Gram block for ζ / the signed DH analogue), `theta_flip_acts_trivially`,
`os_reflection_positive`, `scattering_winding` / `thread6_bridge`. Run:
`python3 -m scripts.numerics.witness.prime_reflection`.

### Sources / internal
- Connes–Consani, *Weil positivity and trace formula, the archimedean place*, arXiv:2006.13771
  (Hermitian Toeplitz device; semilocal Weil positivity ⟹ RH).
- Neeb–Ólafsson, *Reflection positivity and Hankel operators*, arXiv:2105.08522 (RP ↔ positive
  Hankel forms — the structural bridge that here collapses to `sign Λ`).
- Internal: `research/threads/thread-1-reflection-positivity.md`, `thread-6-two-worlds.md`,
  `research/positivity-program.md` (§E knife-edge, §F worker B/C); scaffold `weil_form.py`,
  `scattering.py`, `scattering_forcing.py`, `explicit_formula.py`.
