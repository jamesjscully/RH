"""Certification harness: fail-closed regression gate for the proof-track chain.

Re-derives the load-bearing numerical claims of docs 11-13 from scratch and
checks each against an explicit threshold. Prints PASS/FAIL per check and
exits nonzero on any FAIL. Refutation-grade by design: a FAIL here refutes
the recorded claim (or flags a regression in the stack); all-PASS certifies
nothing beyond reproducibility.

Checks:
  C1  zeta ladder positivity: eigmin(M_R | H_R) > 0 at every rung
  C2  DH kill: DH window margin < 0 at every rung past the first prime
  C3  one-mode compliance form reproduces terminal Schur eigmin (rel < 1e-3)
  C4  tracking criterion: tau < 1 on every living zeta edge; DH's only living
      edge has tau > 1 or dead bulk
  C5  residual zero-sum identity: rel(r_chain, r_zeros) < 5e-2 and
      cos > 0.999 on late edges (3000 zeros)

Run:
    python3 -m scripts.numerics.witness.certify_chain
"""
import math
import sys
import numpy as np
from flint import acb, ctx
from scripts.numerics.witness.prime_carleson_flow import _sym, _gram_orthonormalize
from scripts.numerics.witness.prime_ladder_scaling import (
    build_ladder, nested_basis, margin_at, smooth_block)
from scripts.numerics.witness.semilocal_2 import _phihat

cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
         4.00, 4.26, 4.50, 4.76, 4.96)
NZERO = 3000
lad = build_ladder(cmax, ncenters, hw, gmaxs[-1], T=T, N=N)

failures = []


def check(name: str, ok: bool, detail: str):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        failures.append(name)


# --- C1 / C2: ladder positivity and DH kill --------------------------------
# DH window stays positive through rung 1.60 (its old block at L=1.60 is the
# discriminating tracking edge, C4b) and is dead from 1.88 on - the kill claim
# (09/13) is "DH never passes again once the window opens": gate at g >= 1.88.
for kind, want_pos, gate in (("zeta", True, 0.0), ("DH", False, 1.88)):
    worst = None
    for g in gmaxs:
        if g < gate:
            continue
        Q = nested_basis(lad, g)
        if Q.shape[1] == 0:
            continue
        e = float(np.linalg.eigvalsh(_sym(Q.T @ margin_at(lad, kind, g) @ Q))[0])
        worst = e if worst is None else (min if want_pos else max)(worst, e)
    if want_pos:
        check("C1 zeta ladder positive", worst is not None and worst > 0,
              f"min eigmin over rungs = {worst:+.3e}")
    else:
        check("C2 DH dead on ladder", worst is not None and worst < 0,
              f"max eigmin over rungs >= {gate} = {worst:+.3e}")


# --- per-edge chain quantities ----------------------------------------------
def edge_chain(kind: str, L: float, R: float):
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0:
        return None
    B = np.column_stack([Ql, shell])
    dl = Ql.shape[1]
    new_atoms = [(ln, w, blk) for (ln, w, blk) in lad.atoms[kind] if L <= ln < R]
    if not new_atoms:
        return None
    logs = [a[0] for a in new_atoms]
    bounds = [L] + [0.5 * (x + y) for x, y in zip(logs, logs[1:])] + [R]
    Es = [_sym(B.T @ (smooth_block(lad, lo, hi) - blk) @ B)
          for (lo, hi), (ln, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms)]
    M0 = _sym(B.T @ (margin_at(lad, kind, L) - smooth_block(lad, L, R)) @ B)
    A = _sym(M0[:dl, :dl])
    if np.linalg.eigvalsh(A)[0] <= 1e-12:
        return {"dead_A": True}
    C0, D0 = M0[:dl, dl:], _sym(M0[dl:, dl:])
    ECs = [E[:dl, dl:] for E in Es]
    u = np.linalg.svd(np.hstack(ECs))[0][:, 0]
    Ainv_u = np.linalg.solve(A, u)
    alpha = float(u @ Ainv_u)
    b = C0.T @ Ainv_u
    v = sum(EC.T @ u for EC in ECs)
    S0 = _sym(D0 - C0.T @ np.linalg.solve(A, C0))
    sumED = sum(_sym(E[dl:, dl:]) for E in Es)
    CN, DN = C0 + sum(ECs), D0 + sumED
    SN = _sym(DN - CN.T @ np.linalg.solve(A, CN))
    SN_pred = _sym(S0 + sumED - np.outer(v, b) - np.outer(b, v) - alpha * np.outer(v, v))
    r = v + b / alpha
    BULK = _sym(S0 + sumED + np.outer(b, b) / alpha)
    bmin = float(np.linalg.eigvalsh(BULK)[0])
    tau = float(alpha * (r @ np.linalg.solve(BULK, r))) if bmin > 0 else float("inf")
    return {"dead_A": False, "Ql": Ql, "shell": shell, "Ainv_u": Ainv_u,
            "alpha": alpha, "r": r, "tau": tau, "bulk_min": bmin,
            "e_exact": float(np.linalg.eigvalsh(SN)[0]),
            "e_pred": float(np.linalg.eigvalsh(SN_pred)[0])}


# --- C3 / C4 -----------------------------------------------------------------
worst_rel, worst_tau, dh_witnessed = 0.0, 0.0, False
zeta_edges = {}
for L, R in zip(gmaxs, gmaxs[1:]):
    row = edge_chain("zeta", L, R)
    if row is None or row["dead_A"]:
        continue
    zeta_edges[(L, R)] = row
    # doc 12's one-mode error budget is claimed for edges L >= 3.00 only;
    # earlier edges may need the rank-2 form (doc 11 rank bound).
    if L >= 3.00:
        worst_rel = max(worst_rel, abs(row["e_pred"] - row["e_exact"]) / abs(row["e_exact"]))
    worst_tau = max(worst_tau, row["tau"])
check("C3 one-mode compliance (L >= 3)", worst_rel < 1e-3,
      f"max rel err of predicted eigmin = {worst_rel:.2e} (< 1e-3)")
check("C4a zeta tracking tau < 1", 0 < worst_tau < 1,
      f"max tau over living edges = {worst_tau:.3f}")
for L, R in zip(gmaxs, gmaxs[1:]):
    row = edge_chain("DH", L, R)
    if row is None or row["dead_A"]:
        continue
    dh_witnessed = True
    check("C4b DH fails tracking", not (row["tau"] < 1) or row["e_exact"] < 0,
          f"edge {L:.2f}->{R:.2f}: tau = {row['tau']:.3f}, eigmin(SN) = {row['e_exact']:+.3e}")
if not dh_witnessed:
    print("[note] C4b: no DH edge with living old block in this ladder config")

# --- C5: residual zero-sum identity -----------------------------------------
ctx.prec = 80
gam = np.array([float(acb.zeta_zero(k).imag) for k in range(1, NZERO + 1)])
PHz = np.array([_phihat(gam, c, hw) for c in lad.centers])
Mz = 2.0 * (PHz @ PHz.T)
worst_zrel, worst_zcos = 0.0, 1.0
for (L, R), row in zeta_edges.items():
    if L < 4.0:
        continue
    r_zeros = (row["shell"].T @ (Mz @ (row["Ql"] @ row["Ainv_u"]))) / row["alpha"]
    rel = float(np.linalg.norm(row["r"] - r_zeros) / np.linalg.norm(r_zeros))
    cos = float(row["r"] @ r_zeros / (np.linalg.norm(row["r"]) * np.linalg.norm(r_zeros)))
    worst_zrel, worst_zcos = max(worst_zrel, rel), min(worst_zcos, cos)
check("C5 residual = zero cross-correlation", worst_zrel < 5e-2 and worst_zcos > 0.999,
      f"max rel = {worst_zrel:.2e} (< 5e-2), min cos = {worst_zcos:.5f} (> 0.999)")

print(f"\n{'ALL PASS' if not failures else 'FAILURES: ' + ', '.join(failures)}")
sys.exit(1 if failures else 0)
