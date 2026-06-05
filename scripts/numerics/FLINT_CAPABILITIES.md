# FLINT / python-flint capabilities map

Backend decision: **python-flint (FLINT 3 / Arb)** is the primary numerics engine,
because it gives *certified ball/interval enclosures* — exactly what the program
discipline demands ("every numeric used on the spine must become a certified finite
inequality"). mpmath is a convenience fallback only.

All of the following are verified to work in python-flint 0.8.0 in this environment.
Beyond plain `arb`/`acb` ball scalars, the high-leverage pieces are the **rigorous
linear algebra**, **rigorous zeta zeros**, **exact arithmetic (Möbius)**, and
**Dirichlet L-functions** — each maps directly onto a workstream.

## High-leverage features, by workstream

| Feature | Call | Rigor | Workstream / use |
|---|---|---|---|
| Rigorous matrix solve/inv/det | `acb_mat.solve/.inv/.det` | certified | **A/B** — certified `dist² = ‖u‖² − bᵀG⁻¹b` |
| Rigorous eigenvalues | `acb_mat.eig` | certified | **A** — certified condition number `κ(G_{N,τ})=λmax/λmin` |
| Rigorous integration | `acb.integral(f,a,b)` | certified on `[a,b]` | **A** — certified Gram entries; tail = Theorem-A `Err` |
| Riemann ζ (Riemann–Siegel) | `acb.zeta(s)` | certified | everywhere — ζ on vertical lines |
| Hurwitz ζ | `acb.zeta(s,a)` | certified | DH object, Lerch/co-Poisson normal forms |
| n-th nontrivial ζ zero | `acb.zeta_zero(n)`, `zeta_zeros(n,num)` | certified | **E** — explicit-formula sum over zeros |
| Exact Möbius μ(n) | `fmpz(n).moebius_mu()` | exact | **F / harness Check 3** — Möbius locking, approximants `M_N` |
| Exact factor/σ/φ/prime | `fmpz.factor/divisor_sigma/euler_phi/is_prime` | exact | **F/E** — prime sums, Euler products |
| Dirichlet L(s,χ) | `dirichlet_char(q,i).l(s)` | certified | DH (mod-5 combo), degree-2 Selberg test objects |
| Hardy Z / θ | `dirichlet_char.hardy_z`, `acb_dirichlet_hardy_*` | certified | **E** — zeros on the line, S(t) |
| Stieltjes / Euler γ | `acb.stieltjes(0)` | certified | **Check 3** — Burnol/BD constant `2+γ−log4π` |
| Logarithmic integral li | `acb(x).li()` | certified | **P** — `π(x)−li(x)` PNT/zero-free power test |
| ψ, Γ, Barnes G, polylog | `acb.digamma/gamma/barnes_g/polylog` | certified | explicit-formula archimedean term, Li coefficients |
| Exact rationals / poly | `fmpq`, `fmpq_mat`, `acb_poly` (root isolation) | exact / certified | exact Gram structure; rigorous DH zero isolation |
| Ball DFT | `acb_mat.dft`, `acb.dft` | certified | fast rigorous cosine transforms for `J(x)` |

## Notes / gotchas

- `acb.zeta_zero(n)` is rigorous and fast even at `n = 10⁶` (Riemann–Siegel + Turing).
- `acb_mat.eig` returns certified eigenvalue enclosures; for an SPD Gram matrix the
  condition number is `λmax/λmin` — this is the certified version of the numpy
  `cond()` used in the fast scans.
- For `H²(Ω_τ)` Gram entries, `acb.integral` certifies the integral over a finite
  `[-T,T]`; the **tail `∫_{|t|>T}` is the Theorem-A error term `Err_{N,τ}`** and needs
  an explicit `|ζ(τ+it)|` bound (`acb_dirichlet_zeta_bound` in C; see tracker A-tail).
- Plain numpy/float64 is retained for *exploration* (condition-number scans over many
  `(N,τ)`); FLINT certifies the specific inequalities that get promoted to the spine.

## What is NOT directly exposed (would need the C API / a wheel upgrade)

- `acb_dirichlet_zeta_bound` (explicit `|ζ|` upper bound on a line) — needed to certify
  the Gram tail. Workaround: derive an explicit convexity bound by hand, or call via
  ctypes. Tracked.
- Platt-style large-scale rigorous zero verification (`acb_dirichlet_platt_*`).

See the live mapping and follow-ups in [`../../research/tracker.md`](../../research/tracker.md)
(Workstream N — numerics infrastructure).
