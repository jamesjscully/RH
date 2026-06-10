"""R-SQ experiment E1: the doubled (pair) laboratory - closure of the two-variable system.

Object: A(t) = sum_rho cos(z_rho t) hhat(z_rho)^2, the cosine transform of the
zero measure weighted by an admissible pole-killed test. Two computations:

  zero side:        A_z(t) = sum_{k<=K} cos(gamma_k t) hhat(gamma_k)^2
  arithmetic side:  EF applied to the translated test F_t(u) = g(u-t) + g(u+t),
                    g = h * h (autoconvolution), hhat = p Ghat with
                    p(z) = z^2 (z^2 + 1/4): the pole kills hhat(0) = hhat(i/2) = 0
                    are POLYNOMIAL, hence survive translation:
                    Fhat_t(i/2) = 2 cos(it/2) ghat(i/2) = 0 for every t.

  4 A(t) = -2 sum_n Lambda(n) n^{-1/2} [g(log n - t) + g(log n + t)]
           - 2 log(pi) g(t)
           + (1/pi) int cos(tau t) ghat(tau) Re psi(1/4 + i tau/2) dtau .

Then the DOUBLED form: for a taper k >= 0,
  D(k) = int k(t) A(t)^2 dt = sum_{j,l} hhat(gamma_j)^2 hhat(gamma_l)^2
         * (1/2)[khat(gamma_j - gamma_l) + khat(gamma_j + gamma_l)]
- a zero-PAIR sum, manifestly >= 0 (the free positivity), with an arithmetic
representation D = int k A_arith^2. This is the finite Montgomery form-factor
structure: the arithmetic side of A contains the multiplicative correlations
Lambda(n) Lambda(m) at log-ratio shifts once squared.

Fail-closed reading (fixed in advance, TODO R-SQ): E1 establishes the lab's
exactness; disagreement at more than zero-truncation scale means a convention
bug to fix before E2/E3 - not mathematics.

Run:
    python3 -m scripts.numerics.witness.prime_pair_closure
"""
import math
import numpy as np
from flint import acb, ctx

from scripts.numerics.witness.fork_lib import zeta_gammas

# --- admissible test: hhat = p * Ghat, G = even C^7 bump pair (cos^8) ---------
c0, hw = 2.0, 0.5            # supp h in [-2.5, 2.5]; supp g in [-5, 5]
R = 2.0 * (c0 + hw)
T, N = 120.0, 60001          # tau grid; hhat^2 ~ tau^{-10} at the tail
K = 3000                     # zeros

taus = np.linspace(0.0, T, N)          # even integrands: use half-line x2
dtau = taus[1] - taus[0]

ub = np.linspace(c0 - hw, c0 + hw, 3001)
bump = np.cos(np.pi * (ub - c0) / (2 * hw)) ** 8
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def Ghat(t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.empty_like(t)
    for i in range(0, len(t), 2000):                       # chunked quadrature
        tt = t[i:i + 2000][:, None]
        out[i:i + 2000] = 2.0 * trap(bump[None, :] * np.cos(tt * ub[None, :]),
                                     x=ub, axis=1)
    return out


def p(z):
    return z * z * (z * z + 0.25)


hhat_tau = p(taus) * Ghat(taus)
ghat_tau = hhat_tau ** 2

# physical g on [0, R+0.1] by inverse cosine transform (g even)
ug = np.linspace(0.0, R + 0.1, 4001)
g_u = np.empty_like(ug)
for i in range(0, len(ug), 500):
    uu = ug[i:i + 500][:, None]
    g_u[i:i + 500] = (1.0 / math.pi) * trap(
        ghat_tau[None, :] * np.cos(uu * taus[None, :]), x=taus, axis=1)


def g(x):
    return np.interp(np.abs(np.asarray(x, dtype=float)), ug, g_u, right=0.0)


# archimedean kernel
ctx.prec = 80
psi_re = np.array([float(acb(0.25, tv / 2).digamma().real) for tv in taus])

# prime data: the TRANSLATED test g(log n - t) reaches primes up to e^{R + t_max}
T_MAX = 3.2
nmax = int(math.exp(R + T_MAX)) + 1
lam = np.zeros(nmax + 1)
for pr in range(2, nmax + 1):
    if all(pr % q for q in range(2, int(pr ** 0.5) + 1)):
        pk = pr
        while pk <= nmax:
            lam[pk] = math.log(pr)
            pk *= pr
ns = np.flatnonzero(lam > 0)
wn = lam[ns] / np.sqrt(ns)

# zeros
gam = zeta_gammas(K)
hhat_gam2 = (p(gam) * Ghat(gam)) ** 2


def A_zero(t):
    return float(np.sum(np.cos(gam * t) * hhat_gam2))


def A_arith(t):
    prime = -2.0 * float(np.sum(wn * (g(np.log(ns) - t) + g(np.log(ns) + t))))
    arch = (1.0 / math.pi) * float(trap(np.cos(taus * t) * ghat_tau * psi_re, x=taus)) \
           * 2.0   # half-line doubled for even integrand
    return 0.25 * (prime - 2.0 * math.log(math.pi) * float(g(t)) + arch)


print(f"test: c={c0}, hw={hw}, supp g = [-{R},{R}], n <= {nmax}, K={K} zeros "
      f"(gamma_max={gam[-1]:.0f})")
print("\n[E1a] pointwise closure of A(t) = sum_rho cos(z_rho t) hhat(z_rho)^2")
print("t        A_zero        A_arith       rel err")
ts_show = (0.0, 0.3, 0.7, 1.0, math.log(2), 1.5, 2.0, math.log(8), 2.5, 3.0)
worst = 0.0
for t in ts_show:
    az, aa = A_zero(t), A_arith(t)
    rel = abs(az - aa) / max(abs(az), abs(aa), 1e-300)
    worst = max(worst, rel)
    print(f"{t:6.3f}  {az:+.6e}  {aa:+.6e}  {rel:8.1e}")

print("\n[E1b] doubled form D(k) = int_0^{T0} k(t) A(t)^2 dt, Fejer taper")
T0 = 2.5
tg = np.linspace(0.0, T0, 401)
kf = 1.0 - tg / T0
Az = np.array([A_zero(t) for t in tg])
Aa = np.array([A_arith(t) for t in tg])
Dz = float(trap(kf * Az ** 2, x=tg))
Da = float(trap(kf * Aa ** 2, x=tg))
print(f"D_zero = {Dz:.8e}   D_arith = {Da:.8e}   rel = {abs(Dz-Da)/abs(Dz):.1e}")
print(f"positivity: D >= 0 both ways: {Dz >= 0 and Da >= 0}")

print(f"""
Interpretation:
  * worst pointwise rel err = {worst:.1e}; at or below zero-truncation scale
    means the doubled lab is EXACT in the same sense as the one-variable lab
    (E1 passes; E2/E3 may proceed on this machinery).
  * the arithmetic side of A(t) is prime data only (plus archimedean kernel);
    squaring it makes D's arithmetic side carry Lambda(n)Lambda(m) at
    multiplicative shifts - the pair correlations enter exactly here.
""")
