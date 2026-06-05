# Bibliography Notes

What each reference contributes, with attributions corrected per the 2026-06-05 review.
See [`tracker.md`](tracker.md) §7 for the short anchor list.

## Nyman / Beurling / Báez-Duarte — the closure criterion and its rate

- **Báez-Duarte (2003)**, *Rend. Mat. Acc. Lincei* 14 — discrete/strong NB criterion:
  `RH ⟺ d_N → 0`. Optimal coefficients `~ −μ(n) n^{−ε}` (Euler product enters here).
- **Burnol (2002)**, *Adv. Math.* 170 — **unconditional lower bound**
  `d_N² ≥ (Σ_ρ m(ρ)²/|ρ|² + o(1))/log N`.
- **Báez-Duarte–Balazard–Landreau–Saias (2000)**, *Adv. Math.* 149 — conjecture
  `d_N² ∼ (2+γ−log 4π)/log N` (implies RH + simple zeros).
- **Balazard–de Roton (2008/2010)**, arXiv:0812.1689 — best **conditional** upper bound
  `d_N² ≪ (log log N)^{5/2+o(1)} (log N)^{−1/2}`.

Program use: forward error is the binding constraint; **no unconditional rate to 0 is
known** (that is RH). Möbius locking is the in-coordinate necessary condition (Check 3).

## Disk Hardy criterion

- **Ghosh–Kremnizer–Noor–Santos (2024)**, *Adv. Math.* 455; **Noor (2019)**, *Adv.
  Math.* — `RH ⟺ 1 ∈ closure span{h_k}` in `H²(D)`, with
  `h_k(z) = (1/k)(1/(1−z)) log((1+⋯+z^{k−1})/k)` (note leading `1/k`). Iff at the disk;
  Thm 4.8 half-plane version is **one-directional**.

Program use: critical Hardy avatar; topology warning; semigroup `W_n` entry point
(Manzur/Noor/Santos).

## Half-plane module/range criterion

- **Ge (2019)**, Acta Math. Sinica 62 / Sci. China Math. 49 (Chinese) — the operator
  criterion: `RH ⟺ Ran(M_φ)` dense, `φ = ((s−1)/s²)ζ`. *(Primary source not read in
  original; via Wei–Wu's citation.)*
- **Wei–Wu (2022)**, *Expo. Math.* — closure-of-range characterization; zero-free in
  `Re s > τ ⟺` closed range; bounded-norm Dirichlet-polynomial form (Thm 1.5).

Program use: this **is** the forward theorem (Theorem F). Half-plane module avatar;
evaluation annihilators at zeros (the cheap oracle).

## Dual / biorthogonal infrastructure

- **Calderaro / Manzur / Noor / Santos** — orthogonal complements, Toeplitz /
  de Branges–Rovnyak, biorthogonal sequences. Useful for the oracle, not the bottleneck.

## Weighted / off-critical deformations

- **Gallardo-Gutiérrez / Seco** — weighted Dirichlet criteria, finite Hilbert
  projection, coefficient rigidity. Forward frontier `σ(τ)`, which stalls at
  `Θ = sup{Re ρ}` (`Θ = 1/2 ⟺ RH`).

## Barrier objects  *(the litmus tests)*

- **Davenport–Heilbronn (1936)**, *J. London Math. Soc.* 11; **Bombieri–Ghosh (2011)**,
  *Russian Math. Surveys* 66(2); **Bian–Hejhal (2007)**, *Math. Comp.* 76 — DH function:
  ζ-type functional equation, analytic continuation, **no Euler product**, infinitely
  many **off-line zeros incl. `Re s > 1`**. The relativization barrier: any RH "proof"
  not using the Euler product proves the false statement DH-RH. *(Disregard arXiv
  2503.24275, which contradicts the established record.)*

## Explicit-formula / positivity  *(primary backpressure oracle)*

- **Weil explicit formula / Weil positivity**; **Li coefficients**; **de
  Bruijn–Newman** (Rodgers–Tao); **Toeplitz minors** (Bombieri/Lagarias/Suzuki). The
  exact identity coupling zeros and primes; finite truncations give cheap necessary
  inequalities (harness Check 4), DH-discriminating because DH's prime side is not `Λ(n)`.

## Burnol / Sonine / de Branges tracks

- Co-Poisson formulas, Sonine spaces, zeta-zero systems — possible normal forms;
  secondary until they preserve finite margins and remain Euler-product-load-bearing.
