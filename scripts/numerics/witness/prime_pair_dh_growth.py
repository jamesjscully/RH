"""R-SQ experiment E3a: phase-free detection - the doubled form's growth sees
off-line zeros from coefficient data alone.

The one-variable detection lemma (00a) needs phase engineering or
interpolation at the hypothetical zero. The doubled form needs NEITHER: an
off-line zero z0 = gamma0 + i sigma contributes cos(z0 t) ~ cosh(sigma t)
growth to A(t) REGARDLESS of the phase of hhat(z0)^2, and the Fejer-smoothed
pair form D(T0) = 2 int_0^{T0} (1 - t/T0) B(t)^2 dt accumulates cosh^2 - the
square is phase-free. The price: frequency targeting (smooth compact tests
weight gamma ~ 85 by ~(gamma_1/gamma)^{10}, starving the signal), paid by
MODULATING the bump: G(u) = bump(u) cos(gamma* u), which concentrates the
spectral weight near gamma* with no phase information.

Here B(t) = -2 sum_n c(n) n^{-1/2} [g(log n - t) + g(log n + t)] is the PRIME
part only - pure coefficient data (no zeros, no archimedean factor, hence no
Gamma-factor caveat for DH). Four cells: {zeta, DH} x {gamma* = 30 (control:
no off-line zeros near 30 for either), gamma* = 85.7 (DH's first off-line
pair, beta ~ 0.8085 at t ~ 85.70)}.

Fail-closed readings, fixed in advance:
  * zeta@30, zeta@85.7, DH@30: D(T0) growth comparable (no off-line zeros in
    the window for these cells).
  * DH@85.7: anomalous growth (slope excess ~ 2 sigma ~ 0.62 in log D) IF the
    phase-free mechanism works. If DH@85.7 shows NO excess, the phase-free
    claim is REFUTED at this support and E3b inherits the constraint.

Run:
    python3 -m scripts.numerics.witness.prime_pair_dh_growth
"""
import math
import numpy as np

from scripts.numerics.witness.prime_carleson_flow import coefficient_table

c0, hw = 2.0, 0.5
R = 2.0 * (c0 + hw)
T, N = 170.0, 80001
T_MAX = 5.0

taus = np.linspace(0.0, T, N)
ub = np.linspace(c0 - hw, c0 + hw, 4001)
bump0 = np.cos(np.pi * (ub - c0) / (2 * hw)) ** 8
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def p(z):
    return z * z * (z * z + 0.25)


def make_test(gstar: float):
    """Modulated even test: G = bump * cos(gstar u); returns ghat on taus and g(u)."""
    bump = bump0 * np.cos(gstar * ub)
    Gh = np.empty_like(taus)
    for i in range(0, len(taus), 2000):
        tt = taus[i:i + 2000][:, None]
        Gh[i:i + 2000] = 2.0 * trap(bump[None, :] * np.cos(tt * ub[None, :]),
                                    x=ub, axis=1)
    ghat = (p(taus) * Gh) ** 2
    ugrid = np.linspace(0.0, R + 0.1, 4001)
    gu = np.empty_like(ugrid)
    for i in range(0, len(ugrid), 400):
        uu = ugrid[i:i + 400][:, None]
        gu[i:i + 400] = (1.0 / math.pi) * trap(
            ghat[None, :] * np.cos(uu * taus[None, :]), x=taus, axis=1)
    return ugrid, gu


nmax = int(math.exp(R + T_MAX)) + 1
tables = {k: np.array([0.0, 0.0] + coefficient_table(k, nmax)[1:])  # 1-indexed pad
          for k in ("zeta", "DH")}
# coefficient_table returns list for n = 1..nmax; build weight arrays
weights = {}
for k in ("zeta", "DH"):
    cn = np.array(coefficient_table(k, nmax))           # index 0 -> n=1
    ns = np.arange(1, nmax + 1)
    sel = np.abs(cn) > 1e-12
    weights[k] = (np.log(ns[sel]), cn[sel] / np.sqrt(ns[sel]))

tg = np.linspace(0.0, T_MAX, 1001)
T0s = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)

print(f"setup: supp g = [-{R},{R}], n <= {nmax}, t_max = {T_MAX}")
print("\nD(T0) = 2 int_0^T0 (1-t/T0) B(t)^2 dt   [pure coefficient data]")
header = "kind   g*     " + "".join(f"D({x:.1f})".rjust(11) for x in T0s) + "   slope[3,5]"
print(header)
results = {}
for gstar in (30.0, 85.7):
    ugrid, gu = make_test(gstar)

    def g(x):
        return np.interp(np.abs(np.asarray(x, dtype=float)), ugrid, gu, right=0.0)

    for kind in ("zeta", "DH"):
        ln, wn = weights[kind]
        Bv = np.array([-2.0 * float(np.sum(wn * (g(ln - t) + g(ln + t)))) for t in tg])
        Ds = []
        for T0 in T0s:
            m = tg <= T0
            Ds.append(2.0 * float(trap((1 - tg[m] / T0) * Bv[m] ** 2, x=tg[m])))
        # log-slope over T0 in [3, 5]
        xs = np.array([x for x in T0s if x >= 3.0])
        ys = np.log([d for x, d in zip(T0s, Ds) if x >= 3.0])
        slope = float(np.polyfit(xs, ys, 1)[0])
        results[(kind, gstar)] = (Ds, slope)
        print(f"{kind:5s}  {gstar:5.1f} " +
              "".join(f"{d:11.3e}" for d in Ds) + f"   {slope:+.3f}")

print("\n[discriminator] slope excess of DH@85.7 over its three controls:")
s_dh = results[("DH", 85.7)][1]
for key in (("zeta", 85.7), ("DH", 30.0), ("zeta", 30.0)):
    print(f"  vs {key[0]}@{key[1]:.1f}: {s_dh - results[key][1]:+.3f}")
print("""
Reading (fixed in advance): excess ~ +0.6 (= 2 sigma of DH's first off-line
pair) in the DH@85.7 cell ONLY = phase-free detection works - the square
sees off-line zeros from coefficient data with no phase engineering and no
interpolation, the first structural ADVANTAGE of level 2 over level 1.
No excess = the phase-free claim is refuted at this support (informative
constraint for E3b). Excess in other cells = frequency targeting is leaking;
redesign before concluding anything.
""")
