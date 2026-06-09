"""Fork-deciding witness (R-TRACK sub-target 2): is the tracking residual a zero-sum?

Doc 12 + one-mode algebra give the exact identity chain:
    C_N = C_0 + sum E_C  (one-mode: E_C ~ u t^*)
    =>  r := v + b/alpha  ~  C_N^* A^{-1} u / alpha   (exact up to rank-one defect).
The closure theorem (09 sections 6''') says the full margin form on pole-killed
type-R tests IS the explicit-formula spectral side:
    M_R(h_i, h_j) = 2 sum_{gamma > 0} hhat_i(gamma) hhat_j(gamma)
(actual zeta zeros, truncation-limited). Therefore the tracking residual should
be LITERALLY a zero cross-correlation:

    r_s = (2 / alpha) sum_gamma hhat_{A^{-1}u}(gamma) hhat_{shell_s}(gamma).

This witness compares, per edge:
    r_chain    = v + b/alpha                       (cell-data accumulation)
    r_coupling = C_N^* A^{-1} u / alpha            (exact terminal coupling)
    r_zeros    = shell^T M_z (Q_L A^{-1} u)/alpha  (M_z = zero-sum Gram, K zeros)

Fork readings (decided fail-closed, in advance):
  * r_chain ~ r_coupling ~ r_zeros (to truncation): FORK (ii) CONFIRMED - the
    geometric center -b/alpha is the explicit-formula prediction of v, and
    "v tracks -b/alpha" is zero-repulsion restated. The honest program output
    is then the exact per-edge equivalence, not an independent attack surface.
  * r_chain ~ r_coupling but NOT r_zeros: closure fails at the residual level -
    the residual contains non-spectral content; fork (i) is alive and the
    discrepancy vector is the new object.
  * r_chain != r_coupling beyond the doc-11 sigma_2 budget: one-mode form is
    degrading; rank-2 exact form required before any conclusion.

Run:
    python3 -m scripts.numerics.witness.prime_edge_residual_zerosum
"""
import math
import numpy as np
from flint import acb, ctx
from scripts.numerics.witness.prime_carleson_flow import _sym, _gram_orthonormalize
from scripts.numerics.witness.prime_ladder_scaling import (
    build_ladder, nested_basis, margin_at, smooth_block)
from scripts.numerics.witness.semilocal_2 import _phihat

cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
gmaxs = (4.00, 4.26, 4.50, 4.76, 4.96)
NZERO = 5000
lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

ctx.prec = 80
gam = np.array([float(acb.zeta_zero(k).imag) for k in range(1, NZERO + 1)])
PHz = np.array([_phihat(gam, c, hw) for c in lad.centers])   # (n, K)
Mz = 2.0 * (PHz @ PHz.T)                                      # zero-sum Gram, raw basis


def rel(a, b):
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(b), 1e-300))


def cosv(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(a @ b / (na * nb)) if na > 0 and nb > 0 else float("nan")


print(f"zeros: K={NZERO}, gamma_max={gam[-1]:.1f}")
print("\nedge        |r_chain|  |r_coup|   |r_zeros|  cos(ch,zr) rel(ch,coup) "
      "rel(coup,zr) rel(ch,zr)")
for L, R in zip(gmaxs, gmaxs[1:]):
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0:
        continue
    B = np.column_stack([Ql, shell])
    dl = Ql.shape[1]
    new_atoms = [(logn, w, blk) for (logn, w, blk) in lad.atoms["zeta"] if L <= logn < R]
    if not new_atoms:
        continue
    logs = [a[0] for a in new_atoms]
    bounds = [L] + [0.5 * (x + y) for x, y in zip(logs, logs[1:])] + [R]
    Es = [_sym(B.T @ (smooth_block(lad, lo, hi) - blk) @ B)
          for (lo, hi), (logn, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms)]
    M0 = _sym(B.T @ (margin_at(lad, "zeta", L) - smooth_block(lad, L, R)) @ B)
    A = _sym(M0[:dl, :dl])
    if np.linalg.eigvalsh(A)[0] <= 1e-12:
        continue
    C0 = M0[:dl, dl:]
    ECs = [E[:dl, dl:] for E in Es]
    U_, sv, _ = np.linalg.svd(np.hstack(ECs))
    u = U_[:, 0]
    Ainv_u = np.linalg.solve(A, u)
    alpha = float(u @ Ainv_u)
    b = C0.T @ Ainv_u
    v = sum(EC.T @ u for EC in ECs)
    r_chain = v + b / alpha
    CN = C0 + sum(ECs)
    r_coup = (CN.T @ Ainv_u) / alpha
    # zero-sum: r_zeros = shell^T M_z x / alpha, x = Q_L A^{-1}u in raw coords
    x_raw = Ql @ Ainv_u
    r_zeros = (shell.T @ (Mz @ x_raw)) / alpha
    print(f"{L:.2f}->{R:.2f}  {np.linalg.norm(r_chain):9.3e} "
          f"{np.linalg.norm(r_coup):9.3e} {np.linalg.norm(r_zeros):9.3e} "
          f"{cosv(r_chain, r_zeros):+9.5f} {rel(r_chain, r_coup):11.2e} "
          f"{rel(r_coup, r_zeros):11.2e} {rel(r_chain, r_zeros):10.2e}")

# sanity: closure of the full terminal form on the last edge window
R = gmaxs[-1]
Qr = nested_basis(lad, R)
MW = _sym(Qr.T @ margin_at(lad, "zeta", R) @ Qr)
MZ = _sym(Qr.T @ Mz @ Qr)
print(f"\n[closure sanity, window R={R}] eigmin(form)={np.linalg.eigvalsh(MW)[0]:+.3e}  "
      f"eigmin(zero-sum)={np.linalg.eigvalsh(MZ)[0]:+.3e}  "
      f"rel Frobenius={np.linalg.norm(MW - MZ) / np.linalg.norm(MW):.2e}")

print("""
Interpretation (fail-closed, fixed in advance):
  * rel(chain, zeros) small (~ closure truncation): FORK (ii) - the residual is
    a zero cross-correlation; -b/alpha IS the explicit-formula prediction of v.
  * rel(coup, zeros) large with closure sanity passing: residual carries
    non-spectral content - fork (i) alive, discrepancy is the new object.
  * rel(chain, coup) beyond doc-11 sigma_2 budget: one-mode degradation;
    rerun with rank-2 exact form before concluding anything.
""")
