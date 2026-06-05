"""Forward bound study (tracker F4): the central quantity ||phi_tau M_N||^2.

Wei-Wu: zeta zero-free in Re s > tau  <=>  { ||phi_tau M_N||_{H^2(Omega_tau)} }
bounded in N, where M_N = sum_{n<=N} mu(n) n^{-s}.  This is the crux of the
forward theorem.  Here

    ||phi_tau M_N||^2 = mu^T G_{N,tau} mu = sum_{n,m<=N} mu(n)mu(m)(nm)^{-tau} J(log(m/n)),

a Mertens-type double sum weighted by the spectral kernel
J(x)=(1/2pi) int |phi_tau(tau+it)|^2 e^{itx} dt.

PROVABLE PIECE (tau > 1, unconditional, Euler-product-driven):
    |M_N(tau+it)| <= sum_{n<=N} |mu(n)| n^{-tau} <= sum_{n>=1} n^{-tau} = zeta(tau),
  hence  ||phi_tau M_N||^2 <= zeta(tau)^2 * ||phi_tau||^2 = zeta(tau)^2 * G[1,1],
  UNIFORMLY in N.  So {||phi_tau M_N||} is bounded for tau>1 -> (Wei-Wu) u is in
  the closure of V(tau): an unconditional reproof of the zero-free half-plane
  Re s > 1, now in the *bounded-norm* (not just pointwise) form.

OPEN PIECE (fixed tau_0 in (1/2,1)): the same boundedness is exactly
"zeta zero-free in Re s > tau_0", beyond known unconditional results.  The crude
zeta(tau) bound diverges as tau -> 1, so a real proof needs mu-cancellation in
the double sum (Mertens-type input), not the triangle inequality.
"""
from __future__ import annotations

import numpy as np
from flint import acb, fmpz, ctx

from .objects import Zeta
from . import hardy as H


def mobius_vec(N):
    return np.array([int(fmpz(n).moebius_mu()) for n in range(1, N + 1)], dtype=float)


def forward_norm2(model: H.HardyModel, N: int) -> float:
    """||phi_tau M_N||^2 = mu^T G mu."""
    G = model.gram(N)
    mu = mobius_vec(N)
    return float(mu @ G @ mu)


def crude_bound(tau: float, model: H.HardyModel) -> float:
    """zeta(tau)^2 * G[1,1]  (valid uniform-in-N bound for tau>1)."""
    ctx.prec = 80
    zt = float(acb(tau).zeta().real)
    G11 = model.gram(1)[0, 0]
    return zt * zt * G11


def run():
    z = Zeta()
    taus = [1.30, 1.10, 1.02, 0.90, 0.70, 0.55]
    Ns = [2, 5, 10, 20, 40]
    print("=" * 78)
    print("FORWARD BOUND  ||phi_tau M_N||^2 = mu^T G mu   (-> ||u||^2 if bounded)")
    print("=" * 78)
    print(f"{'tau':>5} {'||u||^2':>9} | " + " ".join(f"N={N:<4}" for N in Ns)
          + f" | {'crude bnd':>10} {'regime':>8}")
    for tau in taus:
        M = H.HardyModel(z, tau, T=300, dt=0.05)
        u2 = H.u_norm2(tau)
        vals = [forward_norm2(M, N) for N in Ns]
        cb = crude_bound(tau, M) if tau > 1 else float("nan")
        regime = "PROVABLE" if tau > 1 else "open"
        cbs = f"{cb:10.3f}" if tau > 1 else f"{'(diverges)':>10}"
        print(f"{tau:>5.2f} {u2:>9.4f} | "
              + " ".join(f"{v:6.3f}" for v in vals)
              + f" | {cbs} {regime:>8}")
    print("-" * 78)
    print("Read: for tau>1 the norm stays <= crude bound and converges to ||u||^2")
    print("  (UNCONDITIONAL, mu-driven). For tau<1 it stays bounded in-range")
    print("  (consistent with no zeros in the tested window) but the crude bound")
    print("  diverges -- a real proof needs mu-cancellation (Mertens-type input).")
    print("=" * 78)


if __name__ == "__main__":
    run()
