# Forward / Arithmetic Theorem (Workstream F)

This is THE bottleneck. By Ge (2019) / Wei-Wu (2022) it equals RH, so the job is not
to "prove" it frontally but to locate the **Euler-product mechanism** that could make
forward convergence unconditional, and to find an *unconditional intermediate frontier*
the machinery can move. Informed by the 2026-06-05 numerics.

## F1 — Precise statement

Half-plane module avatar. For `1/2 <= tau < 1`, `phi_tau = ((s-1)/s^2) zeta`,
`u = (s-1)/s^2`, `V_N(tau) = span{ phi_tau n^{-s} : n <= N }`. Then (Wei-Wu Thm 1.5)

> `zeta` is zero-free in `Re s > tau`  <=>  there exist Dirichlet polynomials `D_N`
> with `zeta D_N -> 1` (`Re s > 1`) and `{ ||phi_tau D_N||_{H^2(Omega_tau)} }` bounded.

The canonical choice is `D_N = M_N = sum_{n<=N} mu(n) n^{-s}` (the Mobius partial sum,
since `zeta * (1/zeta) = 1` and `1/zeta = sum mu(n) n^{-s}`). Forward convergence
`dist(u, V_N(tau)) -> 0` down to `tau = 1/2` is RH.

## F2 — Where the Euler product MUST enter  (must fail for DH)

Two places, both confirmed numerically (see log 2026-06-05):

1. **The coefficients are Mobius.** The extremal coefficients `a = G^{-1} b` lock onto
   `mu(n)` (harness Check 3: at tau=0.7, N=10 the `mu(n)=0` entries n=4,8,9 are already
   near zero). `mu` is the Dirichlet inverse of the *Euler product* `zeta = prod
   (1-p^{-s})^{-1}`. A forward construction with non-Mobius coefficients is provably
   suboptimal. DH has no Euler product, so its "1/DH" has no `mu`-like locking.

2. **The bounded-norm condition encodes zero-freeness.** `||phi_tau M_N||` bounded as
   `tau -> 1/2` is exactly Littlewood's `M_N -> 1/zeta` for `Re s > 1/2`, i.e. RH. This
   is the arithmetic statement; it is invisible to the Hardy geometry alone.

The prime-side positivity (`c_zeta(n) = Lambda(n) >= 0`, Check 4) is the same
Euler-product fact viewed additively. **Litmus:** any forward lemma must FAIL for DH;
if it survives DH it is using only functional-equation/Hardy structure and is dead.

## F3 — The stall point (what an unconditional result would have to beat)

- Above the 1-line the forward fact is **unconditional and modest** (power test PASS):
  `M_N(s) -> 1/zeta(s)` for `Re s > 1`, algebraic rate (faster than `N^{1-sigma}` by
  mu-cancellation); `dist(u,V_N(1.1))` falls cleanly. This reproves the classical
  zero-free half-plane `Re s > 1`.
- Below the 1-line: no unconditional rate. Conditionally (Balazard-de Roton 2008)
  `d_N^2 << (log N)^{-1/2+o(1)}`; unconditional lower bound (Burnol 2002)
  `d_N^2 >= (Sum_rho m^2/|rho|^2 + o(1))/log N`. There is even a conditional gap
  (`(log N)^{-1/2}` vs `(log N)^{-1}`).

**The only non-circular progress is to move an unconditional frontier below `tau = 1`.**
Concretely: extend the `M_N -> 1/zeta` convergence (or a bounded-norm surrogate) to some
fixed `tau_0 in (1/2, 1)` unconditionally -- this would already be a new zero-free
region and a major result. If the witness machinery cannot do this for *any* fixed
`tau_0 < 1`, it has no proving power toward RH beyond the classical region.

## F4 — results (2026-06-05; `scripts/numerics/witness/forward_bound.py`)

The central quantity is `||phi_tau M_N||^2 = mu^T G_{N,tau} mu
= sum_{n,m<=N} mu(n)mu(m)(nm)^{-tau} J(log(m/n))`, a Mertens-type double sum weighted
by the spectral kernel `J`.

**Proposition (unconditional, tau > 1).** For all `N`,
`||phi_tau M_N||^2_{H^2(Omega_tau)} <= zeta(tau)^2 * ||phi_tau||^2`.
*Proof.* `|M_N(tau+it)| <= sum_{n<=N} |mu(n)| n^{-tau} <= sum_{n>=1} n^{-tau} = zeta(tau)`
pointwise, so `||phi_tau M_N||^2 = (1/2pi)int |phi_tau|^2 |M_N|^2 <= zeta(tau)^2 *
(1/2pi)int|phi_tau|^2`. `||phi_tau||^2 = G[1,1] < infinity` for `tau>1/2`. ∎

**Corollary.** `{||phi_tau M_N||}` is bounded for `tau>1`; with `zeta M_N -> 1`
(`Re s>1`), Wei-Wu Thm 1.5 gives `zeta` zero-free in `Re s>tau` for every `tau>1`.
This is a genuine **unconditional reproof of the zero-free half-plane `Re s>1`** in the
*bounded-norm* (not just pointwise) form, Euler-product-driven through `mu`. It
strengthens the power test (P) from pointwise convergence to the actual Wei-Wu
criterion. (It also FAILS for DH: DH has no `mu`, and `|c_DH(n)|` are not `<=1`.)

**Numerics (norm vs N, across tau):** for `tau in {1.30,1.10,1.02}` the norm tracks
`||u||^2` and stays far below the crude bound (bounded, converging). For
`tau in {0.90,0.70,0.55}` it oscillates around `||u||^2` with amplitude **growing** as
`tau -> 1/2` (e.g. tau=0.55: 0.32, 0.87, 0.52, 1.03, 0.61 for N=2..40), and the crude
bound `zeta(tau)^2 G[1,1]` **diverges** as `tau -> 1`.

**Conclusion / open input.** The triangle-inequality bound is useless below `tau=1`
because it discards `mu`-cancellation. A real bound for a fixed `tau_0 in (1/2,1)`
must control the off-diagonal Mertens sum `sum_{n != m} mu(n)mu(m)(nm)^{-tau} J(log m/n)`
using the multiplicative structure of `mu` (Mertens / `sum mu(n)/n^s` boundedness) and
the explicit decay of the kernel `J`. **This is the first genuinely non-circular target
and the precise crux of the forward theorem.** It is, honestly, of RH difficulty for
`tau_0` near `1/2`; the tractable sub-target is to push *any* unconditional bounded-norm
result to a fixed `tau_0 < 1` (which would already be a new zero-free region).
