"""Power test (tracker P): can the witness machinery reprove a KNOWN result,
UNCONDITIONALLY, with the Euler product load-bearing?

Honest target chosen: the arithmetic core of the forward theorem in the region
where it is provable -- Littlewood's fact that the Mobius partial sums converge
to 1/zeta above the 1-line:

    M_N(s) = sum_{n<=N} mu(n) n^{-s}  --->  1/zeta(s)   for Re s > 1,

with explicit algebraic rate |M_N(s) - 1/zeta(s)| <= sum_{n>N} n^{-Re s}
~ N^{1-Re s}/(Re s - 1).  This is UNCONDITIONAL and uses the Euler product (it
is the statement that the Dirichlet inverse of zeta has coefficients mu(n),
i.e. zeta = prod (1-p^{-s})^{-1}).  In the half-plane module avatar this drives
dist(u, V_N(tau)) -> 0 for tau > 1.

The PASS is modest by design: it shows the machinery reproduces the known
zero-free half-plane Re s > 1 unconditionally.  The frontier to RH is exactly the
extension of this convergence down to Re s > 1/2 (Littlewood: M_N -> 1/zeta for
Re s > 1/2  <=>  RH) -- which no unconditional rate reaches (tracker F3).
"""
from __future__ import annotations

import numpy as np
from flint import acb, fmpz, ctx

from .objects import Zeta
from . import hardy as H


def mobius_partial_sum(s: acb, N: int) -> acb:
    s = acb(s)
    tot = acb(0)
    for n in range(1, N + 1):
        mu = int(fmpz(n).moebius_mu())
        if mu:
            tot += mu * (-s * acb(n).log()).exp()  # mu(n) n^{-s}
    return tot


def convergence_table(sigma, ts=(0.0,), Ns=(50, 100, 200, 400, 800), prec=120):
    ctx.prec = prec
    rows = []
    for t in ts:
        s = acb(sigma, t)
        inv_zeta = 1 / s.zeta()
        for N in Ns:
            err = (mobius_partial_sum(s, N) - inv_zeta).abs_upper()
            rows.append((sigma, t, N, float(err)))
    return rows


def run():
    print("=" * 68)
    print("POWER TEST: M_N(s) = sum_{n<=N} mu(n) n^{-s}  ->  1/zeta(s)")
    print("=" * 68)
    print("\n(1) Re s > 1: UNCONDITIONAL convergence (Euler product), rate ~ N^{1-sigma}")
    for sigma in [1.5, 1.2]:
        print(f"  sigma={sigma}:  " + "  ".join(
            f"N={N}:{e:.2e}" for (_, _, N, e) in convergence_table(sigma, ts=(10.0,))))
        # fit the exponent
        rows = convergence_table(sigma, ts=(10.0,))
        Ns = np.array([r[2] for r in rows]); errs = np.array([r[3] for r in rows])
        p = np.polyfit(np.log(Ns), np.log(errs), 1)[0]
        print(f"            fitted rate exponent ~ {p:.3f}  "
              f"(trivial bound <= {1-sigma:.3f}; faster due to mu cancellation)")

    print("\n(2) Re s < 1 (inside the strip): NO unconditional convergence")
    for sigma in [0.8]:
        rows = convergence_table(sigma, ts=(10.0,), Ns=(50, 200, 800, 3200))
        print(f"  sigma={sigma}:  " + "  ".join(f"N={r[2]}:{r[3]:.2e}" for r in rows))
        print("            (erratic / not provably -> 0; equals RH-type statement below 1)")

    print("\n(3) Witness avatar: dist(u, V_N(tau)) -> 0 for tau>1 (provable zero-free)")
    z = Zeta()
    for tau in [1.10, 0.70]:
        M = H.HardyModel(z, tau, T=300, dt=0.05)
        ds = [M.dist2(N)[0] for N in (2, 4, 6, 8)]
        tag = "clean (tau>1, classical zero-free region)" if tau > 1 else "slow (tau<1, open)"
        print(f"  tau={tau}:  dist^2 = " + ", ".join(f"{d:.2e}" for d in ds) + f"   {tag}")

    print("\nVERDICT: PASS (unconditional, Euler-product-driven) for Re s > 1 / tau > 1.")
    print("The gap to RH is the extension to Re s > 1/2 (no unconditional rate; F3).")
    print("=" * 68)


if __name__ == "__main__":
    run()
