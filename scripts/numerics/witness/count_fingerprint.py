"""R-INT pipeline + C0 calibration: fingerprinting count structures against the EF.

Generic chain (gate G-INT2 of TODO R-INT): integer counts c(n) (c(1) = 1)
  -> generalized von Mangoldt by the Dirichlet-log recursion
         lambda(n) = c(n) log n - sum_{d|n, d<n} lambda(d) c(n/d)
     (exact; lambda = coefficients of -Z'/Z for Z = sum c(n) n^{-s})
  -> prime-part correlation B_L(t) = -2 sum lambda(n) n^{-1/2}
         [g(log n - t) + g(log n + t)]   (same admissible g as E1)
  -> fingerprint: regression of B_L on B_zeta over the t-grid
     (k_hat = projection coefficient, residual = what the structure carries
     beyond k_hat copies of zeta's fingerprint).

Calibration cells (readings fixed in advance):
  C0  d(n) = #{(a,b): ab = n}  (Z = zeta^2):       k_hat = 2, residual ~ 0.
  AB  #{abelian groups of order n}  (Z = prod_k zeta(ks)): k_hat = 1 at the
      prime level plus an enhanced prime-POWER tail (lambda(p^m) =
      sigma(m) log p) - structured residual supported on prime powers.
  R2  r_2(n)/4  (Z = zeta(s) L(s, chi_4)):          k_hat = 1 plus a residual
      that IS the chi_4-comb (the L(chi_4) zeros' fingerprint) - the pipeline
      must distinguish WHICH zeros a count structure touches.

Any deviation = pipeline bug (calibration, not mathematics). Pass = G-INT2
machinery validated; novel candidates (C4 Hall, C1 dynamics) may be fed in.

Run:
    python3 -m scripts.numerics.witness.count_fingerprint
"""
import math
import numpy as np

c0, hw = 2.0, 0.5
R = 2.0 * (c0 + hw)
T, N = 120.0, 60001
T_MAX = 3.0
NMAX = int(math.exp(R + T_MAX)) + 1          # ~ 2981

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


ghat_tau = (taus * taus * (taus * taus + 0.25) * Ghat(taus)) ** 2
ugrid = np.linspace(0.0, R + 0.1, 4001)
g_u = np.empty_like(ugrid)
for i in range(0, len(ugrid), 500):
    uu = ugrid[i:i + 500][:, None]
    g_u[i:i + 500] = (1.0 / math.pi) * trap(
        ghat_tau[None, :] * np.cos(uu * taus[None, :]), x=taus, axis=1)


def g(x):
    return np.interp(np.abs(np.asarray(x, dtype=float)), ugrid, g_u, right=0.0)


def lambda_from_counts(c: np.ndarray) -> np.ndarray:
    """c[n] for n = 1..N (c[0] unused, c[1] must be 1). Returns lambda[n]."""
    Nn = len(c) - 1
    assert c[1] == 1, "counts must be normalized: c(1) = 1"
    lam = np.zeros(Nn + 1)
    logs = np.concatenate([[0.0], np.log(np.arange(1, Nn + 1))])
    for n in range(2, Nn + 1):
        s = c[n] * logs[n]
        for d in range(2, n):           # lambda(1) = 0; divisor d of n, d < n
            if n % d == 0:
                s -= lam[d] * c[n // d]
        lam[n] = s
    return lam


def B_profile(lam: np.ndarray, tg: np.ndarray) -> np.ndarray:
    ns = np.flatnonzero(np.abs(lam) > 1e-12)
    wn = lam[ns] / np.sqrt(ns)
    ln = np.log(ns)
    return np.array([-2.0 * float(np.sum(wn * (g(ln - t) + g(ln + t)))) for t in tg])


# --- count structures ---------------------------------------------------------
def counts_divisor(Nn):
    c = np.zeros(Nn + 1)
    for a in range(1, Nn + 1):
        c[a::a] += 1.0
    return c


def counts_abelian(Nn):
    """#abelian groups of order n = prod p(e_i): multiplicative; p(e) = partitions."""
    P = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56]   # partitions 0..11
    c = np.ones(Nn + 1)
    n = np.arange(Nn + 1)
    for pr in range(2, Nn + 1):
        if all(pr % q for q in range(2, int(pr ** 0.5) + 1)):
            for m in range(2, Nn + 1):
                k, e = m, 0
                while k % pr == 0:
                    k //= pr
                    e += 1
                if e:
                    c[m] *= P[e]
    return c


def counts_r2(Nn):
    """r_2(n)/4 = #{(a,b): a^2 + b^2 = n}/4 (multiplicative, c(1) = 1)."""
    c = np.zeros(Nn + 1)
    L = int(math.isqrt(Nn)) + 1
    for a in range(-L, L + 1):
        for b in range(-L, L + 1):
            v = a * a + b * b
            if 1 <= v <= Nn:
                c[v] += 0.25
    return c


tg = np.linspace(0.0, T_MAX, 601)

# zeta reference
c_z = np.ones(NMAX + 1)
lam_z = lambda_from_counts(c_z)
B_z = B_profile(lam_z, tg)
nz2 = float(np.dot(B_z, B_z))

print(f"pipeline: n <= {NMAX}, t in [0, {T_MAX}], admissible test c={c0}, hw={hw}")
print("\nstructure     k_hat    rel residual   residual support (top prime powers vs else)")
for name, cfun, expect in (
    ("C0 d(n)   ", counts_divisor, "k=2, residual ~ 0"),
    ("AB abelian ", counts_abelian, "k=1 + prime-power tail"),
    ("R2 squares ", counts_r2, "k=1 + chi_4 comb"),
    ("ZN order n ", lambda Nn: np.arange(Nn + 1, dtype=float),
     "shifted line: fingerprint NOT at s=1/2"),
):
    c = cfun(NMAX)
    lam = lambda_from_counts(c)
    B = B_profile(lam, tg)
    k_hat = float(np.dot(B, B_z) / nz2)
    res = B - k_hat * B_z
    rel = float(np.linalg.norm(res) / np.linalg.norm(B))
    # residual coefficient diagnosis: lambda - k_hat * Lambda
    dl = lam - k_hat * lam_z
    pp_mask = np.zeros(NMAX + 1, dtype=bool)
    for pr in range(2, NMAX + 1):
        if all(pr % q for q in range(2, int(pr ** 0.5) + 1)):
            pk = pr
            while pk <= NMAX:
                pp_mask[pk] = True
                pk *= pr
    on_pp = float(np.linalg.norm(dl[pp_mask]))
    off_pp = float(np.linalg.norm(dl[~pp_mask]))
    print(f"{name}  {k_hat:+.4f}   {rel:.3e}     |res| on prime powers = {on_pp:.3e}, "
          f"off = {off_pp:.3e}   [{expect}]")

print("""
Readings (fixed in advance): C0 must return k_hat = 2.0000 with residual at
numerical floor (calibration of the whole chain on a known-true integer count
structure whose generating function is zeta^2). AB must return k_hat ~ 1 with
residual SUPPORTED ON PRIME POWERS (lambda(p^m) = sigma(m) log p). R2 must
return k_hat ~ 1 with a signed residual on primes (the chi_4(p) comb: +Lambda
at p = 1 mod 4, -Lambda at p = 3 mod 4) - demonstrating the pipeline reports
WHICH zeros a count structure touches. Deviations = pipeline bug.
""")
