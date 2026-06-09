"""Rank-r exact compliance form (doc 13 section 5): the tracking equivalence
with exact hypotheses.

With U_r spanning the coupling column space (doc 11: rank <= #bumps reaching
the terminal window W*, = 2 in these bases), M_c = U_r* A^{-1} U_r the r x r
compliance matrix, B = C_0* A^{-1} U_r, V = sum_k T_k:

    S_N = S_0 + sum E_D - V B* - B V* - V M_c V*            (exact algebra)
        = BULK_r - (V + B M_c^{-1}) M_c (V + B M_c^{-1})*,
    BULK_r = S_0 + sum E_D + B M_c^{-1} B*,
    S_N > 0  <=>  BULK_r > 0 and
    tau_r = lambda_max[ M_c^{1/2} W* BULK_r^{-1} W M_c^{1/2} ] < 1,
    W = V + B M_c^{-1}.

Measured: one-mode and rank-2/3 predictions all sit at the Fourier-grid noise
floor (1e-7..2e-5 rel; T=250 truncation gives ~1e-6 entry error) - the
residual is grid noise, not rank truncation. tau_2 < 1 on every edge
(max 0.954 at 4.00->4.26). Fail-closed note: if a future run shows rank-2
relerr ABOVE the contemporaneous noise floor, doc 11's rank bound is being
violated in that basis and the support arithmetic must be re-audited.

Run:
    python3 -m scripts.numerics.witness.prime_edge_rank2_exact
"""
import numpy as np
from scripts.numerics.witness.prime_carleson_flow import _sym, _gram_orthonormalize
from scripts.numerics.witness.prime_ladder_scaling import (
    build_ladder, nested_basis, margin_at, smooth_block)

cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
gmaxs = (3.00, 3.24, 3.50, 3.76, 4.00, 4.26, 4.50, 4.76, 4.96)
lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

print("edge        rel(one-mode)  rel(rank-2)  rel(rank-3)  tau2(rank-2)")
for L, R in zip(gmaxs, gmaxs[1:]):
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0: continue
    B = np.column_stack([Ql, shell]); dl = Ql.shape[1]
    new_atoms = [(ln, w, blk) for (ln, w, blk) in lad.atoms["zeta"] if L <= ln < R]
    if not new_atoms: continue
    logs = [a[0] for a in new_atoms]
    bounds = [L] + [0.5*(x+y) for x, y in zip(logs, logs[1:])] + [R]
    Es = [_sym(B.T @ (smooth_block(lad, lo, hi) - blk) @ B)
          for (lo, hi), (ln, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms)]
    M0 = _sym(B.T @ (margin_at(lad, "zeta", L) - smooth_block(lad, L, R)) @ B)
    A = _sym(M0[:dl, :dl]); C0 = M0[:dl, dl:]; D0 = _sym(M0[dl:, dl:])
    if np.linalg.eigvalsh(A)[0] <= 1e-12: continue
    ECs = [E[:dl, dl:] for E in Es]
    sumED = sum(_sym(E[dl:, dl:]) for E in Es)
    S0 = _sym(D0 - C0.T @ np.linalg.solve(A, C0))
    CN = C0 + sum(ECs); DN = D0 + sumED
    e_ex = float(np.linalg.eigvalsh(_sym(DN - CN.T @ np.linalg.solve(A, CN)))[0])
    rels, tau2 = [], None
    for r in (1, 2, 3):
        Ur = np.linalg.svd(np.hstack(ECs))[0][:, :r]
        Mc = Ur.T @ np.linalg.solve(A, Ur)
        Bm = C0.T @ np.linalg.solve(A, Ur)
        V = sum(EC.T @ Ur for EC in ECs)
        SN_pred = _sym(S0 + sumED - V @ Bm.T - Bm @ V.T - V @ Mc @ V.T)
        rels.append(abs(float(np.linalg.eigvalsh(SN_pred)[0]) - e_ex) / abs(e_ex))
        if r == 2:
            Wv = V + Bm @ np.linalg.inv(Mc)
            BULK2 = _sym(S0 + sumED + Bm @ np.linalg.inv(Mc) @ Bm.T)
            if np.linalg.eigvalsh(BULK2)[0] > 0:
                Mh = np.linalg.cholesky(_sym(Mc))
                K = Mh.T @ (Wv.T @ np.linalg.solve(BULK2, Wv)) @ Mh
                tau2 = float(np.linalg.eigvalsh(_sym(K))[-1])
    print(f"{L:.2f}->{R:.2f}  {rels[0]:11.2e}  {rels[1]:10.2e}  {rels[2]:10.2e}  "
          f"{tau2 if tau2 is not None else float('nan'):9.4f}")
