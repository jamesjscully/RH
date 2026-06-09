"""Edge-compliance witness (doc 12): compute (alpha, b, v) per ladder edge.

Validates the exact edge-compliance reduction (research/proof/12): with the old
block frozen within an edge (E_A = 0 exact) and the rank-one coupling of doc 11,
   S_N = S_0 + sum E_D - v b^* - b v^* - alpha v v^*,
alpha = u^* A^{-1} u (edge compliance), v = accumulated transgression of the
edge-convolution profiles. Reproduces exact terminal eigmin to ~2e-5 relative.

Race data (fail-closed for the asymptotic theorem): alpha grows ~e^{2.5R} while
|v| still grows at small R; the compliance charge alpha|v|^2 already exceeds the
final margin by 100s of times - positivity survives through the sign structure
of the v-b cross term. The theorem must control the DIRECTION of v against b
(equidistribution), not just |v|. If the prediction relerr degrades at larger R,
the rank-2 exact form of doc 11 must replace the one-mode form.

Run:
    python3 -m scripts.numerics.witness.prime_edge_compliance
"""
import math
import numpy as np
from scripts.numerics.witness.prime_carleson_flow import _sym, _gram_orthonormalize
from scripts.numerics.witness.prime_ladder_scaling import (
    build_ladder, nested_basis, margin_at, smooth_block)

cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
gmaxs = (3.00, 3.24, 3.50, 3.76, 4.00, 4.26, 4.50, 4.76, 4.96)
lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

print("edge        alpha      |v|       a|v|^2    eigmin(Sn) exact/pred    relerr")
for L, R in zip(gmaxs, gmaxs[1:]):
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0: continue
    B = np.column_stack([Ql, shell]); dl = Ql.shape[1]
    new_atoms = [(logn, w, blk) for (logn, w, blk) in lad.atoms["zeta"] if L <= logn < R]
    if not new_atoms: continue
    logs = [a[0] for a in new_atoms]
    bounds = [L] + [0.5*(x+y) for x, y in zip(logs, logs[1:])] + [R]
    Es = [_sym(B.T @ (smooth_block(lad, lo, hi) - blk) @ B)
          for (lo, hi), (logn, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms)]
    M0 = _sym(B.T @ (margin_at(lad, "zeta", L) - smooth_block(lad, L, R)) @ B)
    A = _sym(M0[:dl, :dl]); C0 = M0[:dl, dl:]; D0 = _sym(M0[dl:, dl:])
    if np.linalg.eigvalsh(A)[0] <= 1e-12: continue
    ECs = [E[:dl, dl:] for E in Es]
    U_, sv, Vt = np.linalg.svd(np.hstack(ECs))
    u = U_[:, 0]
    alpha = float(u @ np.linalg.solve(A, u))
    b = C0.T @ np.linalg.solve(A, u)
    ts = [EC.T @ u for EC in ECs]
    v = sum(ts)
    S0 = _sym(D0 - C0.T @ np.linalg.solve(A, C0))
    sumED = sum(_sym(E[dl:, dl:]) for E in Es)
    # cross term between C0 and the rank-one part also needs the v b* term; plus
    # the exact terminal for comparison:
    CN = C0 + sum(ECs)
    DN = D0 + sumED
    SN_exact = _sym(DN - CN.T @ np.linalg.solve(A, CN))
    SN_pred = _sym(S0 + sumED - np.outer(v, b) - np.outer(b, v) - alpha * np.outer(v, v))
    e_ex = float(np.linalg.eigvalsh(SN_exact)[0])
    e_pr = float(np.linalg.eigvalsh(SN_pred)[0])
    relerr = abs(e_pr - e_ex) / max(abs(e_ex), 1e-300)
    print(f"{L:.2f}->{R:.2f}  {alpha:9.3e}  {np.linalg.norm(v):8.3e}  "
          f"{alpha*np.linalg.norm(v)**2:9.3e}  {e_ex:+9.3e}/{e_pr:+9.3e}  {relerr:8.1e}")
