"""R-SQ experiment E2: the pair functional - level-1 fork verdict + level-2 image.

The pure pair-arithmetic object of the doubled lab is

    Q_k = int_{-T0}^{T0} k(t) B(t)^2 dt,
    B(t) = -2 sum_n Lambda(n) n^{-1/2} [g(log n - t) + g(log n + t)]

(the prime part of 4A(t); expanding the square, Q_k is the smoothed
multiplicative pair correlation sum_{n,m} Lambda(n)Lambda(m)(nm)^{-1/2} x
[kernel](log n - log m, log n + log m) - genuinely Lambda (x) Lambda data,
the finite Goldston-Montgomery object).

LEVEL-1 FORK VERDICT (structural, recorded here, no numerics needed): the
level-1 EF orbit consists of functionals LINEAR in the zero measure
(equivalently linear in Lambda + archimedean data). Q_k is QUADRATIC in
Lambda, so it admits no level-1 transport - the first verified P1 instance
(extra information relative to the one-variable system). The conservation
law does NOT close at level 1.

LEVEL-2 IMAGE (numerical content): squaring the EF transports Q_k to
ZERO-PAIR data. With 4A = B + S (S = archimedean part) and the Fejer taper
k(t) = (1 - |t|/T0)_+, whose transform is khat(xi) = T0 sinc^2(xi T0 / 2):

    16 * PZ = int k B^2 + 2 int k B S + int k S^2,
    PZ = sum_{j,l} hhat(gamma_j)^2 hhat(gamma_l)^2
         * (1/2)[khat(gamma_j - gamma_l) + khat(gamma_j + gamma_l)]

- the explicit zero-pair double sum. If this identity closes to truncation,
the level-2 conservation holds on this object (the pair-Lambda data is
losslessly bound to zero-PAIR data): the fork moves up a level but does not
break. Fail-closed readings (TODO R-SQ): failure of the identity = bug;
closure = E2 PASSES with the predicted verdict pair (P1 at level 1, fork at
level 2), and E3 must hunt the index in inequalities BETWEEN pair objects,
not in their values.

Run:
    python3 -m scripts.numerics.witness.prime_pair_fork
"""
import math
import numpy as np
from flint import acb, ctx

from scripts.numerics.witness.fork_lib import zeta_gammas

# --- identical test setup to prime_pair_closure (E1-validated machinery) -----
c0, hw = 2.0, 0.5
R = 2.0 * (c0 + hw)
T, N = 120.0, 60001
K = 3000
T0, T_MAX = 2.5, 3.2

taus = np.linspace(0.0, T, N)
ub = np.linspace(c0 - hw, c0 + hw, 3001)
bump = np.cos(np.pi * (ub - c0) / (2 * hw)) ** 8
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def Ghat(t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.empty_like(t)
    for i in range(0, len(t), 2000):
        tt = t[i:i + 2000][:, None]
        out[i:i + 2000] = 2.0 * trap(bump[None, :] * np.cos(tt * ub[None, :]),
                                     x=ub, axis=1)
    return out


def p(z):
    return z * z * (z * z + 0.25)


hhat_tau = p(taus) * Ghat(taus)
ghat_tau = hhat_tau ** 2

ug = np.linspace(0.0, R + 0.1, 4001)
g_u = np.empty_like(ug)
for i in range(0, len(ug), 500):
    uu = ug[i:i + 500][:, None]
    g_u[i:i + 500] = (1.0 / math.pi) * trap(
        ghat_tau[None, :] * np.cos(uu * taus[None, :]), x=taus, axis=1)


def g(x):
    return np.interp(np.abs(np.asarray(x, dtype=float)), ug, g_u, right=0.0)


ctx.prec = 80
psi_re = np.array([float(acb(0.25, tv / 2).digamma().real) for tv in taus])

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
logn = np.log(ns)

gam = zeta_gammas(K)
h2 = (p(gam) * Ghat(gam)) ** 2

# --- the split 4A = B + S on a t-grid ----------------------------------------
tg = np.linspace(0.0, T0, 801)


def B_of(t):
    return -2.0 * float(np.sum(wn * (g(logn - t) + g(logn + t))))


def S_of(t):
    arch = (2.0 / math.pi) * float(trap(np.cos(taus * t) * ghat_tau * psi_re, x=taus))
    return -2.0 * math.log(math.pi) * float(g(t)) + arch


Bv = np.array([B_of(t) for t in tg])
Sv = np.array([S_of(t) for t in tg])
Av_zero = np.array([float(np.sum(np.cos(gam * t) * h2)) for t in tg])

kf = 1.0 - tg / T0
I_BB = 2.0 * float(trap(kf * Bv * Bv, x=tg))     # symmetric integrals: 2 x half-line
I_BS = 2.0 * float(trap(kf * Bv * Sv, x=tg))
I_SS = 2.0 * float(trap(kf * Sv * Sv, x=tg))

# --- explicit zero-pair double sum with the Fejer transform ------------------
def khat(xi):
    x = np.asarray(xi, dtype=float) * T0 / 2.0
    s = np.where(np.abs(x) < 1e-12, 1.0, np.sin(np.where(np.abs(x) < 1e-12, 1.0, x))
                 / np.where(np.abs(x) < 1e-12, 1.0, x))
    return T0 * s * s


PZ = 0.0
chunk = 400
for i in range(0, K, chunk):
    gi = gam[i:i + chunk][:, None]
    wi = h2[i:i + chunk][:, None]
    PZ += float(np.sum(wi * h2[None, :] *
                       0.5 * (khat(gi - gam[None, :]) + khat(gi + gam[None, :]))))

# internal consistency: PZ must equal 2 int k A_zero^2
PZ_int = 2.0 * float(trap(kf * Av_zero * Av_zero, x=tg))

lhs = 16.0 * PZ
rhs = I_BB + 2.0 * I_BS + I_SS

print(f"setup: K={K} zeros, n <= {nmax}, T0={T0}, Fejer taper")
print(f"\n[E2a] zero-pair double sum vs integral form (internal):")
print(f"  PZ(double sum) = {PZ:.8e}   2*int k A_z^2 = {PZ_int:.8e}   "
      f"rel = {abs(PZ-PZ_int)/abs(PZ):.1e}")
print(f"\n[E2b] level-2 image of the pair functional (finite Goldston-Montgomery):")
print(f"  Q_k = int k B^2 (pair-Lambda data) = {I_BB:.8e}")
print(f"  cross 2 int k B S                  = {2*I_BS:+.8e}")
print(f"  arch  int k S^2                    = {I_SS:.8e}")
print(f"  RHS total                          = {rhs:.8e}")
print(f"  16 * PZ (zero-pair side)           = {lhs:.8e}")
print(f"  identity rel err                   = {abs(lhs-rhs)/abs(lhs):.1e}")
print(f"""
Verdicts (fail-closed readings fixed in TODO R-SQ):
  * LEVEL 1: Q_k is quadratic in Lambda; the level-1 EF orbit is linear in
    the zero measure. NO level-1 transport exists - P1 (extra information)
    holds STRUCTURALLY for the pair data. First verified P1 instance.
  * LEVEL 2: if the identity above closes to truncation, the squared EF
    transports pair-Lambda data losslessly to zero-PAIR data - the
    conservation law moves up one level instead of breaking. E3 must
    therefore hunt the index in INEQUALITIES between pair objects (the
    Castelnuovo shape), not in their values.
""")
