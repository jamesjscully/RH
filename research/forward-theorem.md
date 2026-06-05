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

**Correction (review #2).** That "tractable sub-target" is NOT tractable: there is no
fixed `tau_0 < 1` half-plane known zero-free at all (see §F5). The fixed-`tau`
formulation has no rung between `tau=1` (done) and RH. And the short-interval Mobius
route is dead (the kernel `J` is broad; the Mertens cancellation is long-range, not
near-diagonal -- review #2, dead-end D1). So F4-as-posed is RH-complete; the productive
move is F5.

## F5 -- height-localized criterion (the lead forward target)

**Why fixed-`tau` is the wrong frame.** Wei-Wu/Ge is a *fixed half-plane* statement:
`||phi_tau M_N||` bounded `<=>` zeta zero-free in `Re s > tau`. But **no fixed
`tau_0 < 1` half-plane is known zero-free** -- every unconditional zero-free result,
from de la Vallee Poussin (1899) to Vinogradov-Korobov (1958), is a *height-dependent
region*

>   `zeta(s) != 0` for `sigma > 1 - c / (log |t|)^{2/3} (log log |t|)^{1/3}`  (VK),

narrowing to the line as `|t| -> infinity`. The whole 120-year frontier lives there.
So the fixed-`tau` forward problem is all-or-nothing (`tau=1` free, next rung = RH);
to touch real progress the criterion must be *height-localized*.

**Proposed criterion (to be made precise).** Localize the witness problem to a height
window and let `tau` approach `1` with `T`. Concretely, for a window `|Im s| <= T` and a
threshold `tau(T) = 1 - c/log T`, study the windowed forward quantity
`d_{N,T} = dist_{H^2, |t|<=T}(u, V_N(tau(T)))` (inner product restricted to the band, or
a smooth height cutoff `w_T(t)` of Beurling-Selberg type to keep it an honest RKHS).
Target statement:

>   for every fixed `c < c_0`, `d_{N(T), T} -> 0` as `T -> infinity` along a suitable
>   `N(T)`, with constants depending only on `c`  ==>  zeta zero-free in the region
>   `sigma > 1 - c/log T` -- i.e. an unconditional zero-free region of de la Vallee
>   Poussin type, reproved in bounded-norm form.

The Euler product must enter exactly as in F2 (coefficients `-> mu(n)`; the bounded-norm
condition = a truncated `M_N -> 1/zeta`), and the statement must FAIL for DH and for the
Epstein second wall (harness Checks 1, 1b).

**Go/no-go.** The machinery already reproves `sigma > 1` in bounded-norm form (F4 prop).
The first milestone is to recover the **classical zero-free region** (`sigma > 1 -
c/log|t|`) windowed -- if the windowed witness problem cannot even reach de la Vallee
Poussin, the route is weaker than 1899 and is dead. If it can, the open frontier is to
*widen* the region (toward VK or beyond) unconditionally -- a publishable result short of
RH, which the fixed-`tau` form structurally cannot produce.

**What this needs (the real analytic input).** A rigorous handle on
`int_{|t|<=T} |zeta(tau(T)+it)|^2 w_T(t) dt` -- a *windowed second moment* of zeta near
the 1-line. This is the same ingredient N4 needs for the certified Gram tail, and it is
where classical zero-free-region technology (the `zeta'/zeta` bound, Borel-Caratheodory
+ the second moment) would be imported. That import -- not the Hilbert geometry -- is the
load-bearing step. Status: `active` (scoped; the windowed second moment is the next
concrete sub-task).

**Reduction (this session).** The N4 tail for `1/2 < tau < 1` reduces cleanly to the
classical *mean square*. With `|phi_tau|^2 <= |zeta(tau+it)|^2 / t^2` for large `t` and
`F(t) := int_0^t |zeta(tau+iu)|^2 du`, integrate by parts:
```
int_T^inf |zeta(tau+it)|^2 / t^2 dt = [F(t)/t^2]_T^inf + int_T^inf 2 F(t)/t^3 dt.
```
If `F(t) <= C(tau) * t` for all `t` (the Hardy-Littlewood/Ingham mean square,
`F(t) ~ zeta(2 tau) t` for `1/2<tau<1`), the boundary term vanishes and the tail is
`<= 2 C(tau)/T`.  So the ENTIRE remaining requirement for N4 (`tau<1`) and the F5 window
is a single rigorous constant: **`C(tau)` with `int_0^t |zeta(tau+iu)|^2 du <= C(tau) t`
for all `t>0`.**  python-flint can certify `F(t)` on any finite range via `acb.integral`
(so `C(tau)` is empirically `~ zeta(2 tau)`); making it hold for ALL `t` is the classical
explicit second-moment bound to import. This is the precise, isolated open input.
