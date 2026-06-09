"""Tracking witness (R-TRACK sub-target 1): does v track -b/alpha along the ladder?

Doc 12's completed square gives the exact per-edge positivity criterion in scalar
form: with BULK = S_0 + sum E_D + b b^*/alpha and residual r = v + b/alpha,

    S_N = BULK - alpha r r^*   =>   S_N > 0  <=>  BULK > 0  and
    tau := alpha * r^* BULK^{-1} r < 1.

tau is THE tracking ratio: the alpha-weighted (BULK-metric) distance of the
accumulated arithmetic transgression v from the geometrically determined center
-b/alpha, in units of the bulk budget. The tracking theorem = tau < 1 uniformly
along the filtration.

This witness computes, per edge and for both coefficient systems:
    alpha, |v|, |b|/alpha, cos(v, -b/alpha), |r|, |r|/(|b|/alpha),
    eigmin(BULK), tau, eigmin(S_N) exact (one-mode check).

Fail-closed readings:
    * zeta: tau must stay < 1 on every edge (it must - this is just the margin,
      restated); the QUESTION is whether the tracking signature is visible:
      cos -> 1 and relative residual |r|/(|b|/alpha) shrinking as alpha grows.
      If v shows no directional convergence to -b/alpha, the "tracking" frame
      is numerology and R-TRACK sub-target 2 must reexamine the coordinate.
    * DH (kill test): DH's v must NOT track. Expected: tau >= 1 or BULK
      indefinite on edges where DH's Schur fails, OR DH's old block A is
      already dead (never reaches the tracking regime). If DH tracks with
      tau < 1 wherever its A is alive, the tracking frame is dispersing
      (content-free) and R-TRACK DIES.

Run:
    python3 -m scripts.numerics.witness.prime_edge_tracking
"""
import math
import numpy as np
from scripts.numerics.witness.prime_carleson_flow import _sym, _gram_orthonormalize
from scripts.numerics.witness.prime_ladder_scaling import (
    build_ladder, nested_basis, margin_at, smooth_block)

cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
         4.00, 4.26, 4.50, 4.76, 4.96)
lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)


def edge_tracking(kind: str, L: float, R: float) -> dict | None:
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0:
        return None
    B = np.column_stack([Ql, shell])
    dl = Ql.shape[1]
    new_atoms = [(logn, w, blk) for (logn, w, blk) in lad.atoms[kind] if L <= logn < R]
    if not new_atoms:
        return None
    logs = [a[0] for a in new_atoms]
    bounds = [L] + [0.5 * (x + y) for x, y in zip(logs, logs[1:])] + [R]
    Es = [_sym(B.T @ (smooth_block(lad, lo, hi) - blk) @ B)
          for (lo, hi), (logn, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms)]
    M0 = _sym(B.T @ (margin_at(lad, kind, L) - smooth_block(lad, L, R)) @ B)
    A = _sym(M0[:dl, :dl])
    a_min = float(np.linalg.eigvalsh(A)[0])
    if a_min <= 1e-12:
        return {"kind": kind, "L": L, "R": R, "dead_A": True, "a_min": a_min}
    C0 = M0[:dl, dl:]
    D0 = _sym(M0[dl:, dl:])
    ECs = [E[:dl, dl:] for E in Es]
    U_, sv, _ = np.linalg.svd(np.hstack(ECs))
    u = U_[:, 0]
    alpha = float(u @ np.linalg.solve(A, u))
    b = C0.T @ np.linalg.solve(A, u)
    v = sum(EC.T @ u for EC in ECs)
    S0 = _sym(D0 - C0.T @ np.linalg.solve(A, C0))
    sumED = sum(_sym(E[dl:, dl:]) for E in Es)
    target = -b / alpha
    r = v - target
    BULK = _sym(S0 + sumED + np.outer(b, b) / alpha)
    bulk_min = float(np.linalg.eigvalsh(BULK)[0])
    tau = float("nan")
    if bulk_min > 0:
        tau = float(alpha * (r @ np.linalg.solve(BULK, r)))
    CN = C0 + sum(ECs)
    DN = D0 + sumED
    SN_exact = _sym(DN - CN.T @ np.linalg.solve(A, CN))
    nv, nt = np.linalg.norm(v), np.linalg.norm(target)
    cos = float(v @ target / (nv * nt)) if nv > 0 and nt > 0 else float("nan")
    return {
        "kind": kind, "L": L, "R": R, "dead_A": False, "a_min": a_min,
        "alpha": alpha, "nv": nv, "ntarget": nt, "cos": cos,
        "nr": float(np.linalg.norm(r)),
        "rel_r": float(np.linalg.norm(r) / nt) if nt > 0 else float("nan"),
        "bulk_min": bulk_min, "tau": tau,
        "sn_min": float(np.linalg.eigvalsh(SN_exact)[0]),
    }


for kind in ("zeta", "DH"):
    print(f"\n[{kind}] tracking of v against -b/alpha")
    print("edge        alpha      |v|       |b/a|     cos(v,t)  |r|       |r|/|t|  "
          "eigmin(BULK) tau        eigmin(SN)")
    for L, R in zip(gmaxs, gmaxs[1:]):
        row = edge_tracking(kind, L, R)
        if row is None:
            continue
        if row["dead_A"]:
            print(f"{L:.2f}->{R:.2f}  OLD BLOCK DEAD (eigmin(A) = {row['a_min']:+.3e}) "
                  "- never reaches the tracking regime")
            continue
        print(f"{L:.2f}->{R:.2f}  {row['alpha']:9.3e} {row['nv']:9.3e} "
              f"{row['ntarget']:9.3e} {row['cos']:+8.4f} {row['nr']:9.3e} "
              f"{row['rel_r']:8.2e} {row['bulk_min']:+11.3e} {row['tau']:9.3e}  "
              f"{row['sn_min']:+9.3e}")

print("""
Interpretation:
  * tau < 1 <=> terminal Schur positivity (exact, given BULK > 0); tau is the
    alpha-weighted distance-squared of v from -b/alpha in bulk-budget units.
  * tracking signature for zeta = cos(v, target) -> +1 and |r|/|t| falling as
    alpha grows; absence of both = the coordinate is not doing asymptotic work.
  * DH must NOT show tau < 1 with a living old block on edges where its window
    fails; if it does, R-TRACK is dispersing and dies (fail-closed).
""")
