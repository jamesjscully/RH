"""Rigorous interval certification of the doc-13 tracking criterion tau_2 < 1
on the computed zeta ladder (X rung; terminal equivalence RH <=> uniform
tau_r < 1, research/proof/13-tracking-equivalence.md section 4').

WHAT IS CERTIFIED, EXACTLY (statement fixed before any ball computation).
For each edge L -> R of the doc-13 ladder (cmax=2.42, ncenters=38, hw=0.06,
gmaxs 1.60..4.96), with the FIXED float matrices

    B   = [Ql | shell]  (38 x (dl+ds), the float nested pole-killed edge basis
          of prime_ladder_scaling / prime_edge_tracking, entries taken as
          EXACT dyadic rationals -- part of the statement, not of the error
          budget; same discipline as the T1/T2 certificates),
    U2  = the float top-2 left singular basis of the stacked per-cell
          couplings hstack(E_C^(k)) (dl x 2, exact dyadics, statement data),

and the EXACT ambient operators (all enclosed in Arb balls):

    W_inf(i,j) = -g_ij(0) log pi + (1/pi) int_0^inf phihat_i phihat_j
                 Re psi(1/4 + it/2) dt        (holomorphic-symmetrized
                 integrand on [0,T] + the rigorous closed-form tail lemma of
                 prime_defect_t1_interval_certificate, REUSED VERBATIM),
    T(log n)   = exact Toeplitz atom (compact physical overlap, REUSED),
    w_n        = 2 Lambda(n) / sqrt(n) in arb (exact von Mangoldt weights),
    smooth cells = density 2 e^{U/2} on [b_k, b_{k+1}] (REUSED), with the
                 cell bounds b_k = the float midpoints of consecutive log n
                 (exact dyadic statement endpoints, as in the float pipeline),

define (frozen old block; E_A = 0 EXACTLY by the support lemma, asserted):

    M_N  = W_inf - sum_{log n < R} w_n T(log n)            (ambient)
    A    = old-old block of B^T (W_inf - sum_{log n < L} w_n T(log n)) B
    C_N, D_N = old-shell / shell-shell blocks of B^T M_N B
    S_N  = D_N - C_N^T A^{-1} C_N                          (terminal Schur)
    E_k  = smooth(cell_k) - w_k T(log n_k), G = sum_k (B^T E_k B)[old, shell]
    C_0  = C_N - G,  D_0 = D_N - sum E_D,  S_0 = D_0 - C_0^T A^{-1} C_0
    M_c  = U2^T A^{-1} U2,  B_m = C_0^T A^{-1} U2
    BULK = S_0 + sum E_D + B_m M_c^{-1} B_m^T              (doc-13 BULK_2)
    tau  = 1 - lambda_min( BULK^{-1/2} S_N BULK^{-1/2} )   (exact pencil form)

EXACTNESS NOTE. tau < 1 <=> S_N > 0 holds EXACTLY given BULK > 0 (no rank
hypothesis): BULK - S_N = W M_c W^T + R' with W = V + B_m M_c^{-1},
V = (M_c^{-1} U2^T A^{-1} G)^T the A^{-1}-orthogonal projection coefficient,
and R' the (computed, enclosed) doc-11 rank-2 residual.  The doc-13 float
tau_2 used the rank-2 factorization; float cross-check (this session, before
any ball ran): |tau_pencil - tau_2(rank-2 svd code path)| <= 3.3e-5 on every
edge of the ladder, so the pencil tau IS doc-13's tau_2 up to the doc-11
rank residual, which this witness encloses (reported per edge as ||R'||_F
and ||G_perp||_F balls).  The per-edge criterion certified is therefore the
exact-hypothesis tracking criterion of doc 13 section 4'.

REUSED CERTIFIED COMPONENT LIBRARY (import, not rebuilt; see
research/work/L-t1-interval.md): atom_matrix_ball / smooth entry and matrix
balls (compact overlaps + ENDPOINT_SLOP = 1e-13 on every overlap entry, S2
discipline), winf_matrix_ball (holomorphic symmetrized digamma, S1 fix),
winf_tail_envelope (rigorous tail lemma), von_mangoldt_arb, compress
(symmetric-pair intersection), interval_cholesky, forward_substitute.

NEW IN THIS WITNESS (statement-level, not numerical-kernel-level): the edge
bases B and coupling bases U2 (fixed floats from the doc-13 ladder), the
frozen-A support-margin gate, the residual-preconditioned verified Schur
products (P^T A^{-1} Q = Xp^T Q + Ep^T Xq + Ep^T A^{-1} Eq with float dyadic
Xp, Xq and the last term bounded by ||Ep_i|| ||Eq_j|| / lambda_min(A); this
replaces interval triangular solves through the cond ~ 2e4 old block and
realizes the true sensitivity ~ ||A^{-1}C||_1^2 instead of the worst case),
and the pencil bisection enclosures for tau.

FAIL-CLOSED GATES (all fixed before the ball run; ABORT = exit 2):
  G1 float reproduction: the in-witness float tau_2 (verbatim rank-2 code
     path on a freshly built ladder) must match the doc-13 reference table
     REFERENCE_TAU2 below to 5e-5 per edge (late 8 edges pinned by the
     2026-06-10 rerun of prime_edge_rank2_exact which reproduces doc 13's
     recorded max 0.954 at 4.00->4.26; early 6 edges pinned by the same code
     path run this session, recorded here as the reference).
  G2 pencil-vs-rank2 float agreement: |tau_pencil - tau_2| <= 5e-4 per edge
     (measured <= 3.3e-5 before registration).
  G3 frozen-A support margin: L - 2*(max old center + hw) >= 1e-3 and
     L/2 >= hw + 1e-9 (these make E_A = 0 exact, so A is frozen along the
     edge chain and S_N above IS the terminal Schur of the edge);
     additionally every compressed E_k old-old entry ball must contain 0.
  G4 atom-set / weight drift: the window atom set must be exactly the prime
     powers in [L, R); |ladder float weight - 2 Lambda(n)/sqrt(n)| <= 1e-12.
  G5 kernel cross-checks at this hw: arb_phi_hat vs float _phihat (1e-10);
     digamma envelope dominance on samples; closed-form tail brackets the
     scipy envelope (sanity only).
  P0 midpoint drift: the all-ball midpoint tau must match the float tau
     (pencil form) to 5e-2 per edge (known Fourier-grid T=250 systematic is
     ~1e-6 per ambient entry; gross construction drift is O(1) and must be
     caught BEFORE certificate language is printed).

PRE-REGISTERED READINGS (fixed before the computation; epistemically
asymmetric exactly as in the T1/T2 certificates):
  X1 CONFIRMATION: every swept edge certifies A > 0, M_c > 0, BULK > 0 and
     S_N > 0 by interval Cholesky (hence tau < 1 EXACTLY, by the pencil
     equivalence), with the [tau] enclosure reported per edge.  Then the
     tracking inequality holds certificate-grade on the computed ladder:
     the finite side of doc 13's equivalence is rigorous as far as computed.
     This CONFIRMS the floats; it proves nothing asymptotic (doc 13's wall
     -- no estimate-based route to uniform tau < 1 -- stands regardless).
  X2 GAP: some enclosure straddles its threshold (a Cholesky pivot of A,
     M_c, BULK or S_N straddles 0, or the [tau] enclosure straddles 1 while
     S_N is not decided).  NOT a refutation.  Report the per-ingredient
     width budget and the dominating ingredient; the cure is cutoff /
     precision / tighter slop, never a weakened target.  Exit 1.
  X3 TRACKING VIOLATION (major): some edge certifies tau > 1 rigorously
     (S_N certifiably NOT positive definite -- a float eigenvector x with
     upper(x^T S_N x) < 0 -- while A > 0 and BULK > 0 are certified).  On
     the zeta ladder this is a certified tracking violation = evidence
     against RH through doc 13's equivalence.  PRE-REGISTERED DISCIPLINE:
     X3 demands an independent re-derivation pass (fresh basis audit, exact
     statement re-check, second integration route) BEFORE being recorded as
     a finding; the verdict line prints REQUIRES-REDERIVATION.  Exit 0
     (definite outcome) but escalate immediately.

The DH negative control (doc 13: tau = 1.554 > 1 on 1.60->1.88) can be run
with --dh-control: same machinery, DH float atom weights taken as exact
statement data; expected outcome is the certified failure S_N < 0 (the
control must NOT certify tau < 1; if it does, the frame is dispersing and
the rung dies fail-closed).

Run:
    python3 -m scripts.numerics.witness.prime_edge_tau_interval \
        --edges 4.00-4.26                  # most informative edge first
    python3 -m scripts.numerics.witness.prime_edge_tau_interval --edges all
    python3 -m scripts.numerics.witness.prime_edge_tau_interval --dh-control
    python3 -m scripts.numerics.witness.prime_edge_tau_interval \
        --edges all --float-only           # gates G1-G5 only, no balls

AUDIT RECORD (X session, 2026-06-10; fresh-context resume of the cut-off
author).  Fixes applied before any certifying run: (1) build_ladder clobbered
ctx.prec to 80 for the whole ball stage -- restored to --prec after the float
build (fidelity, not soundness); (2) single-proc mode ignored --prec in
workers; (3) the DH-control final verdict had confirmation-style semantics --
the control is PASSED by a certified violation and KILLED by a certified
tau<1, now enforced with its own exit codes (0 pass / 3 dispersing / 1
inconclusive); (4) --float-only added; (5) the A>0 / lambda_min(A) step ran
interval Cholesky DIRECTLY on the cond~1e5+ old block, which is sound but
width-fragile and produced spurious X2 gaps on the last three ladder edges
(eigmin(A) ~ 1e-5 vs compressed radii ~3e-9 amplified by ~cond) -- replaced
by Rump-style congruence-preconditioned PD certification (pd_certify), with
the float triangular-inverse preconditioner taken as exact dyadic data and
every decision still in ball arithmetic.  The enclosure chain itself
(ainv_product identity, lambda_min_lb shifted interval Cholesky, pencil
bisection lower bounds + ball Rayleigh upper bounds, reball slop, G3 support
gate vs nested_basis's center selection) was re-derived and found sound; see
research/work/X-tau-interval.md for the full audit.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
import time
from multiprocessing import Pool

import numpy as np
from flint import acb, arb, ctx

from .prime_carleson_flow import _sym, _gram_orthonormalize
from .prime_ladder_scaling import build_ladder, nested_basis, smooth_block, margin_at
from .prime_defect_t1_interval_certificate import (
    ENDPOINT_SLOP, _ball, atom_entry_ball, smooth_entry_ball,
    winf_entry_ball, winf_tail_envelope, von_mangoldt_arb,
    compress, interval_cholesky, forward_substitute, max_rad, max_mid, mid_np)
from .prime_defect_t1_winf_tail import arb_phi_hat, winf_tail_bound
from .semilocal_2 import _phihat

# ladder parameters (doc 13 / prime_edge_tracking, taken as the statement)
CMAX, NCENTERS, HW, T_GRID, N_GRID = 2.42, 38, 0.06, 250.0, 100001
GMAXS = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
         4.00, 4.26, 4.50, 4.76, 4.96)

# G1 reference (pre-registered): late 8 edges = prime_edge_rank2_exact rerun
# 2026-06-10 (matches doc 13's recorded max 0.954); early 6 edges = the same
# rank-2 code path evaluated on the full ladder this session (float stage).
REFERENCE_TAU2 = {
    (1.60, 1.88): 0.7900, (1.88, 2.10): 0.5749, (2.10, 2.30): 0.8049,
    (2.30, 2.52): 0.8025, (2.52, 2.76): 0.6996, (2.76, 3.00): 0.8364,
    (3.00, 3.24): 0.8659, (3.24, 3.50): 0.7249, (3.50, 3.76): 0.8163,
    (3.76, 4.00): 0.9173, (4.00, 4.26): 0.9539, (4.26, 4.50): 0.8094,
    (4.50, 4.76): 0.2574, (4.76, 4.96): 0.2763,
}
G1_TOL, G2_TOL, G3_MARGIN, G4_TOL, P0_TOL = 5e-5, 5e-4, 1e-3, 1e-12, 5e-2


# ---------------------------------------------------------------------------
# ball-matrix helpers (list-of-lists of arb)
# ---------------------------------------------------------------------------

def bm_from_float(F: np.ndarray):
    return [[arb(float(F[i, j])) for j in range(F.shape[1])]
            for i in range(F.shape[0])]


def bm_zeros(nr, nc):
    return [[arb(0)] * nc for _ in range(nr)]


def bm_add(X, Y):
    return [[a + b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def bm_sub(X, Y):
    return [[a - b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def bm_scale(X, s):
    return [[s * a for a in row] for row in X]


def bm_T(X):
    return [list(col) for col in zip(*X)]


def bm_mul(X, Y):
    nr, ni, nc = len(X), len(Y), len(Y[0])
    return [[sum((X[i][k] * Y[k][j] for k in range(ni)), arb(0))
             for j in range(nc)] for i in range(nr)]


def bm_symmetrize(X):
    """Pairwise intersection (valid: the true matrix is symmetric)."""
    n = len(X)
    for i in range(n):
        for j in range(i + 1, n):
            both = X[i][j].intersection(X[j][i]) \
                if hasattr(X[i][j], "intersection") else X[i][j]
            X[i][j] = both
            X[j][i] = both
    return X


def bm_slice(X, r0, r1, c0, c1):
    return [[X[i][j] for j in range(c0, c1)] for i in range(r0, r1)]


def bm_contains_zero(X) -> bool:
    return all(x.contains(arb(0)) for row in X for x in row)


def bm_fro_upper(X) -> float:
    s = 0.0
    for row in X:
        for x in row:
            u = (abs(float(x.mid())) + float(x.rad())) * (1.0 + 1e-12)
            s += u * u
    return math.sqrt(s) * (1.0 + 1e-12)


def col_norm_upper(X, j) -> float:
    s = 0.0
    for row in X:
        u = (abs(float(row[j].mid())) + float(row[j].rad())) * (1.0 + 1e-12)
        s += u * u
    return math.sqrt(s) * (1.0 + 1e-12)


def reball(m: float, r: float) -> arb:
    """Sound ball from float (mid, rad) pairs produced by workers/cache."""
    return arb(m) + arb(0, r * (1.0 + 1e-9) + abs(m) * 3e-16 + 1e-300)


def back_substitute(L, Y, dim: int, ncol: int):
    """X with L^T X = Y (enclosure)."""
    X = [[arb(0)] * ncol for _ in range(dim)]
    for col in range(ncol):
        for i in range(dim - 1, -1, -1):
            s = Y[i][col]
            for k in range(i + 1, dim):
                s = s - L[k][i] * X[k][col]
            X[i][col] = s / L[i][i]
    return X


def solve_spd(Mball, RHS, dim, ncol):
    ok, L, _ = interval_cholesky(Mball, dim)
    if not ok:
        return None
    return back_substitute(L, forward_substitute(L, RHS, dim, ncol), dim, ncol)


# ---------------------------------------------------------------------------
# residual-preconditioned verified Schur product
# ---------------------------------------------------------------------------

def _tri_inv_float(Lf: np.ndarray) -> np.ndarray | None:
    """Float inverse of a lower-triangular factor, EXACTLY lower triangular
    (zeros above the diagonal are exact, so the dyadic matrix is exactly
    nonsingular iff every diagonal entry is nonzero -- checkable in floats).
    Used only as a congruence preconditioner; taken as exact dyadic data."""
    n = Lf.shape[0]
    Y = np.zeros((n, n))
    for j in range(n):
        d = Lf[j, j]
        if d == 0.0 or not math.isfinite(d):
            return None
        Y[j, j] = 1.0 / d
        for i in range(j + 1, n):
            s = 0.0
            for k in range(j, i):
                s += Lf[i, k] * Y[k, j]
            Y[i, j] = -s / Lf[i, i]
    if not np.all(np.isfinite(Y)) or np.any(np.diag(Y) == 0.0):
        return None
    return Y


def pd_certify(Aball, dim: int, mu: float = 0.0) -> bool:
    """Certify A - mu I > 0 for every symmetric member of the ball family.

    Audit fix (X session): the inherited code ran interval Cholesky DIRECTLY
    on A; that is sound but compounds entry radii by ~cond(A), and on the
    late ladder edges (eigmin(A) ~ 1e-5, cond ~ 1e5..1e6, compressed radii
    ~3e-9) it fails to certify, producing spurious X2 gaps.  Standard cure
    (Rump-style congruence preconditioning): with Y the float triangular
    inverse of the midpoint Cholesky factor of A - mu I, taken as an EXACT
    dyadic lower-triangular nonsingular matrix,

        A - mu I > 0   <=>   Z = Y (A - mu I) Y^T > 0    (congruence),

    and Z ~ I has O(rad * ||Y||^2) radii, on which interval Cholesky
    succeeds easily.  Decisions stay entirely in ball arithmetic; the float
    inverse is only a (statement-exact) change of basis.  Falls back to the
    direct interval Cholesky if the preconditioner cannot be built."""
    shifted = [[Aball[i][j] - (arb(mu) if i == j else arb(0))
                for j in range(dim)] for i in range(dim)]
    Amid = mid_np(shifted)
    try:
        Lf = np.linalg.cholesky(_sym(Amid))
        Y = _tri_inv_float(Lf)
    except np.linalg.LinAlgError:
        Y = None
    if Y is None:
        ok, _, _ = interval_cholesky(shifted, dim)
        return ok
    Yb = bm_from_float(Y)
    Z = bm_symmetrize(bm_mul(Yb, bm_mul(shifted, bm_T(Yb))))
    ok, _, _ = interval_cholesky(Z, dim)
    return ok


def lambda_min_lb(Aball, dim: int) -> float:
    """Certified lower bound for lambda_min over all members (0.0 on failure
    to certify a positive bound; caller treats that as a gap)."""
    Amid = mid_np(Aball)
    lam = float(np.linalg.eigvalsh(_sym(Amid))[0])
    if lam <= 0:
        return 0.0
    for f in (0.99, 0.9, 0.5, 0.25, 0.1, 0.01):
        mu = f * lam
        if pd_certify(Aball, dim, mu):
            return mu
    return 0.0


def ainv_product(Aball, lamA_lo: float, Pball, Qball, symmetric=False):
    """Enclosure of P^T A^{-1} Q via float preconditioning:
    P^T A^{-1} Q = Xp^T Q + Ep^T Xq + Ep^T A^{-1} Eq,  E* = * - A X*."""
    assert lamA_lo > 0.0
    Amid = mid_np(Aball)
    Pmid, Qmid = mid_np(Pball), mid_np(Qball)
    Xp = bm_from_float(np.linalg.solve(Amid, Pmid))
    Xq = Xp if symmetric else bm_from_float(np.linalg.solve(Amid, Qmid))
    Ep = bm_sub(Pball, bm_mul(Aball, Xp))
    Eq = Ep if symmetric else bm_sub(Qball, bm_mul(Aball, Xq))
    out = bm_add(bm_mul(bm_T(Xp), Qball), bm_mul(bm_T(Ep), Xq))
    np_, nq = len(out), len(out[0])
    epn = [col_norm_upper(Ep, j) for j in range(np_)]
    eqn = epn if symmetric else [col_norm_upper(Eq, j) for j in range(nq)]
    for i in range(np_):
        for j in range(nq):
            out[i][j] = out[i][j] + arb(0, epn[i] * eqn[j] / lamA_lo * (1 + 1e-12))
    if symmetric:
        bm_symmetrize(out)
    return out


# ---------------------------------------------------------------------------
# pencil enclosures: lambda_min(S, B) for SPD-certified B
# ---------------------------------------------------------------------------

def pencil_shift_pd(Sball, Bball, mu: float, dim: int) -> bool:
    """True only if S - mu B is certifiably PD for every member."""
    M = [[Sball[i][j] - arb(mu) * Bball[i][j] for j in range(dim)]
         for i in range(dim)]
    ok, _, _ = interval_cholesky(M, dim)
    return ok


def pencil_lambda_min(Sball, Bball, dim: int, iters: int = 60):
    """Certified enclosure [lo, hi] of lambda_min of the pencil (S, B)."""
    Smid, Bmid = mid_np(Sball), mid_np(Bball)
    LBf = np.linalg.cholesky(_sym(Bmid))
    Kf = np.linalg.solve(LBf, np.linalg.solve(LBf, _sym(Smid)).T)
    wf, Vf = np.linalg.eigh(_sym(Kf))
    lam_f = float(wf[0])
    # certified lower bound: largest mu with S - mu B PD
    lo, hi = lam_f - max(1.0, abs(lam_f)), lam_f + 10.0 * max(1e-6, abs(lam_f))
    if not pencil_shift_pd(Sball, Bball, lo, dim):
        lo = -10.0 * max(1.0, abs(lam_f))
        if not pencil_shift_pd(Sball, Bball, lo, dim):
            return None, None
    good, bad = lo, hi
    for _ in range(iters):
        mid = 0.5 * (good + bad)
        if pencil_shift_pd(Sball, Bball, mid, dim):
            good = mid
        else:
            bad = mid
    lam_lo = good
    # certified upper bound: Rayleigh quotient at the float eigenvector
    x = np.linalg.solve(LBf.T, Vf[:, 0])
    xb = [[arb(float(v))] for v in x]
    num = bm_mul(bm_T(xb), bm_mul(Sball, xb))[0][0]
    den = bm_mul(bm_T(xb), bm_mul(Bball, xb))[0][0]
    if not (den > 0):
        return lam_lo, None
    lam_hi = float((num / den).upper())
    return lam_lo, lam_hi


def pencil_lambda_max(Sball, Bball, dim: int, iters: int = 60):
    lo, hi = pencil_lambda_min(bm_scale(Sball, arb(-1)), Bball, dim, iters)
    if lo is None:
        return None, None
    return (None if hi is None else -hi), -lo


# ---------------------------------------------------------------------------
# ambient ball ingredients with /tmp cache + multiprocessing
# ---------------------------------------------------------------------------

_WORKER_PREC = 120


def _init_worker(prec):
    global _WORKER_PREC
    _WORKER_PREC = prec
    ctx.prec = prec


def _entry_job(args):
    kind, i, j, params = args
    ctx.prec = _WORKER_PREC
    if kind == "atom":
        ci, cj, hw, U = params
        v = atom_entry_ball(ci, cj, hw, U)
    elif kind == "smooth":
        ci, cj, hw, lo, hi = params
        v = smooth_entry_ball(ci, cj, hw, lo, hi)
    elif kind == "winf":
        ci, cj, hw, T, g0m, g0r, tail_up = params
        g0 = reball(g0m, g0r)
        # winf_entry_ball adds arb(0, upper(tail)*(1+1e-9)) to the radius;
        # arb(tail_up) has upper() == tail_up, reproducing the T1 behaviour.
        v = winf_entry_ball(ci, cj, hw, T, g0, arb(tail_up))
    else:
        raise ValueError(kind)
    return i, j, float(v.mid()), float(v.rad())


def _build_matrix(kind, centers, hw, params_extra, procs):
    n = len(centers)
    jobs = []
    for i in range(n):
        for j in range(i, n):
            if kind == "winf":
                g0m, g0r = params_extra["g0mid"][i][j], params_extra["g0rad"][i][j]
                p = (float(centers[i]), float(centers[j]), hw,
                     params_extra["T"], g0m, g0r, params_extra["tail_up"])
            elif kind == "atom":
                p = (float(centers[i]), float(centers[j]), hw, params_extra["U"])
            else:
                p = (float(centers[i]), float(centers[j]), hw,
                     params_extra["lo"], params_extra["hi"])
            jobs.append((kind, i, j, p))
    out_mid = np.zeros((n, n))
    out_rad = np.zeros((n, n))
    if procs > 1:
        with Pool(procs, initializer=_init_worker, initargs=(ctx.prec,)) as pool:
            for i, j, m, r in pool.imap_unordered(_entry_job, jobs, chunksize=4):
                out_mid[i, j] = out_mid[j, i] = m
                out_rad[i, j] = out_rad[j, i] = r
    else:
        _init_worker(ctx.prec)  # audit fix: honor --prec in single-proc mode too
        for job in jobs:
            i, j, m, r = _entry_job(job)
            out_mid[i, j] = out_mid[j, i] = m
            out_rad[i, j] = out_rad[j, i] = r
    return out_mid, out_rad


def cached_matrix(cache_dir, key, builder):
    path = os.path.join(cache_dir, key + ".npz")
    if os.path.exists(path):
        z = np.load(path)
        return z["mid"], z["rad"]
    mid, rad = builder()
    os.makedirs(cache_dir, exist_ok=True)
    np.savez(path, mid=mid, rad=rad)
    return mid, rad


def to_balls(mid: np.ndarray, rad: np.ndarray):
    n, m = mid.shape
    return [[reball(float(mid[i, j]), float(rad[i, j])) for j in range(m)]
            for i in range(n)]


# ---------------------------------------------------------------------------
# float stage: ladder, bases, gates, reference taus
# ---------------------------------------------------------------------------

def float_edge_state(lad, kind, L, R):
    Ql, Qr = nested_basis(lad, L), nested_basis(lad, R)
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    if shell.shape[1] == 0:
        return None
    B = np.column_stack([Ql, shell])
    dl, ds = Ql.shape[1], shell.shape[1]
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
        return {"dead": True, "L": L, "R": R}
    C0 = M0[:dl, dl:]
    D0 = _sym(M0[dl:, dl:])
    ECs = [E[:dl, dl:] for E in Es]
    sumED = sum(_sym(E[dl:, dl:]) for E in Es)
    S0 = _sym(D0 - C0.T @ np.linalg.solve(A, C0))
    CN = C0 + sum(ECs)
    DN = D0 + sumED
    SN = _sym(DN - CN.T @ np.linalg.solve(A, CN))
    r = min(2, np.hstack(ECs).shape[1])
    U2 = np.linalg.svd(np.hstack(ECs))[0][:, :r]
    Mc = U2.T @ np.linalg.solve(A, U2)
    Bm = C0.T @ np.linalg.solve(A, U2)
    V = sum(EC.T @ U2 for EC in ECs)
    Wv = V + Bm @ np.linalg.inv(Mc)
    BULK = _sym(S0 + sumED + Bm @ np.linalg.inv(Mc) @ Bm.T)
    Mh = np.linalg.cholesky(_sym(Mc))
    K2 = Mh.T @ (Wv.T @ np.linalg.solve(BULK, Wv)) @ Mh
    tau2 = float(np.linalg.eigvalsh(_sym(K2))[-1])
    LB = np.linalg.cholesky(BULK)
    K = np.linalg.solve(LB, np.linalg.solve(LB, SN).T)
    tau_pencil = 1.0 - float(np.linalg.eigvalsh(_sym(K))[0])
    return {
        "dead": False, "L": L, "R": R, "B": B, "dl": dl, "ds": ds, "U2": U2,
        "new_atoms": new_atoms, "bounds": bounds, "tau2": tau2,
        "tau_pencil": tau_pencil, "lminSN": float(np.linalg.eigvalsh(SN)[0]),
        "lminBULK": float(np.linalg.eigvalsh(BULK)[0]),
    }


def crosschecks_generic(hw: float, T: float) -> None:
    for c in (0.02, 1.22, 2.42):
        for t in (1e-3, 1.0, 7.5, math.pi / hw, 300.0):
            a = float(arb_phi_hat(c, hw, acb(t)).real.mid())
            f = float(_phihat(np.array([t]), c, hw)[0])
            assert abs(a - f) < 1e-10, ("phihat mismatch", c, t, a, f)
    for t in (2.0, 10.0, T, 2 * T, 100 * T):
        z = acb(0.25, 0.5 * t)
        re_psi = abs(float(z.digamma().real.mid()))
        assert re_psi <= math.log(t) + math.log(2.0) + 1.0, ("digamma env", t)
    tau = float(winf_tail_envelope(hw, T).mid())
    tau_scipy = winf_tail_bound(hw, T)
    assert 0.9 * tau_scipy <= tau <= 10.0 * tau_scipy, ("tail form", tau, tau_scipy)


# ---------------------------------------------------------------------------
# per-edge certificate
# ---------------------------------------------------------------------------

def certify_edge(st, W_ball, atom_balls, atom_w, cache_dir, procs, centers,
                 kind) -> dict:
    L, R, B, dl, ds = st["L"], st["R"], st["B"], st["dl"], st["ds"]
    t0 = time.time()
    n = len(centers)
    res = {"L": L, "R": R, "dl": dl, "ds": ds, "verdict": "GAP", "notes": []}

    # G3: frozen-A support margin (makes E_A = 0 exact, A frozen)
    idxL = np.flatnonzero(centers + HW <= L / 2.0 + 1e-12)
    supp_margin = L - 2.0 * (float(centers[idxL].max()) + HW)
    assert supp_margin >= G3_MARGIN, ("G3 support margin", L, supp_margin)
    assert L / 2.0 >= HW + 1e-9, ("G3 hw condition", L)

    # ambient margins (ball sums over precomputed weighted atom balls)
    def margin_ambient(g):
        M = [[W_ball[i][j] for j in range(n)] for i in range(n)]
        for nn, Ab in atom_balls.items():
            if math.log(nn) < g - 1e-15:
                M = bm_sub(M, bm_scale(Ab, atom_w[nn]))
        return M

    margL = margin_ambient(L)
    margR = margin_ambient(R)

    # smooth cells (cached per (lo,hi))
    cells = list(zip(st["bounds"], st["bounds"][1:]))
    sumE = bm_zeros(n, n)
    for (lo, hi), (ln, _w, _b) in zip(cells, st["new_atoms"]):
        assert lo <= ln < hi or abs(ln - lo) < 1e-12, ("cell bound drift", ln, lo, hi)
        key = f"smooth_{lo:.17g}_{hi:.17g}_n{n}_hw{HW:.17g}"
        smid, srad = cached_matrix(
            cache_dir, key,
            lambda lo=lo, hi=hi: _build_matrix(
                "smooth", centers, HW, {"lo": lo, "hi": hi}, procs))
        sumE = bm_add(sumE, to_balls(smid, srad))
        nn = round(math.exp(ln))
        sumE = bm_sub(sumE, bm_scale(atom_balls[nn], atom_w[nn]))
    res["t_ambient"] = time.time() - t0

    # compressions
    t0 = time.time()
    McL = compress(margL, B)
    McR = compress(margR, B)
    McE = compress(sumE, B)
    res["t_compress"] = time.time() - t0
    res["rad_compressed"] = max(max_rad(McL), max_rad(McR), max_rad(McE))

    dim = dl + ds
    A = bm_slice(McL, 0, dl, 0, dl)
    CN = bm_slice(McR, 0, dl, dl, dim)
    DN = bm_slice(McR, dl, dim, dl, dim)
    G = bm_slice(McE, 0, dl, dl, dim)
    sED = bm_slice(McE, dl, dim, dl, dim)
    EA = bm_slice(McE, 0, dl, 0, dl)
    # G3 ball-level: compressed E old-old must contain 0 (E_A = 0 exactly)
    assert bm_contains_zero(EA), "G3: compressed E_A ball does not contain 0"
    C0 = bm_sub(CN, G)
    D0 = bm_sub(DN, sED)
    U2b = bm_from_float(st["U2"])
    r2 = st["U2"].shape[1]

    # A > 0 and lambda_min lower bound (congruence-preconditioned, audit fix)
    t0 = time.time()
    okA = pd_certify(A, dl, 0.0)
    if not okA:
        res["notes"].append("A pivot not certified positive")
        res["verdict"] = "GAP-A"
        return res
    lamA = lambda_min_lb(A, dl)
    if lamA <= 0.0:
        res["notes"].append("lambda_min(A) lower bound not certified")
        res["verdict"] = "GAP-A"
        return res
    res["lamA_lb"] = lamA

    # verified Schur pieces
    SN = bm_symmetrize(bm_sub(DN, ainv_product(A, lamA, CN, CN, symmetric=True)))
    S0 = bm_symmetrize(bm_sub(D0, ainv_product(A, lamA, C0, C0, symmetric=True)))
    Mc = bm_symmetrize(ainv_product(A, lamA, U2b, U2b, symmetric=True))
    BmT = ainv_product(A, lamA, U2b, C0)          # r x ds = (C0^T A^{-1} U2)^T
    Bm = bm_T(BmT)
    UtAG = ainv_product(A, lamA, U2b, G)          # r x ds
    res["t_schur"] = time.time() - t0
    res["rad_SN"] = max_rad(SN)

    okM, _, _ = interval_cholesky(Mc, r2)
    if not okM:
        res["notes"].append("M_c not certified PD")
        res["verdict"] = "GAP-MC"
        return res
    Y = solve_spd(Mc, BmT, r2, ds)                 # M_c^{-1} B_m^T
    PI = bm_symmetrize(bm_mul(Bm, Y))
    BULK = bm_symmetrize(bm_add(bm_add(S0, sED), PI))
    res["rad_BULK"] = max_rad(BULK)

    okB, _, _ = interval_cholesky(BULK, ds)
    if not okB:
        res["notes"].append("BULK not certified PD")
        res["verdict"] = "GAP-BULK"
        return res

    # doc-11 rank residual (enclosed): V, W, R' and G_perp
    Tm = solve_spd(Mc, UtAG, r2, ds)               # M_c^{-1} U^T A^{-1} G
    V = bm_T(Tm)
    Wm = bm_add(V, bm_T(Y))                        # ds x r
    WMW = bm_symmetrize(bm_mul(bm_mul(Wm, Mc), bm_T(Wm)))
    Rres = bm_sub(bm_sub(BULK, SN), WMW)
    Gperp = bm_sub(G, bm_mul(U2b, Tm))
    res["Rres_fro_up"] = bm_fro_upper(Rres)
    res["Gperp_fro_up"] = bm_fro_upper(Gperp)

    # P0: midpoint tau vs float tau (pencil form)
    SNm, BKm = _sym(mid_np(SN)), _sym(mid_np(BULK))
    LBf = np.linalg.cholesky(BKm)
    Kf = np.linalg.solve(LBf, np.linalg.solve(LBf, SNm).T)
    tau_mid = 1.0 - float(np.linalg.eigvalsh(_sym(Kf))[0])
    res["tau_mid"] = tau_mid
    res["p0_drift"] = abs(tau_mid - st["tau_pencil"])
    if res["p0_drift"] > P0_TOL:
        res["verdict"] = "ABORT-P0"
        res["notes"].append(f"P0 drift {res['p0_drift']:.3e} > {P0_TOL}")
        return res

    # decision: S_N > 0 (=> tau < 1 exactly) or certified violation
    okS, _, _ = interval_cholesky(SN, ds)
    lam_lo, lam_hi = pencil_lambda_min(SN, BULK, ds)
    if lam_lo is not None:
        res["tau_lo"] = None if lam_hi is None else 1.0 - lam_hi
        res["tau_hi"] = 1.0 - lam_lo
    # certified SN lambda_min lower bound for the report
    res["lamSN_lb"] = lambda_min_lb(SN, ds) if okS else 0.0
    # doc-13-form tau_2 (rank-2 packaging) enclosure
    t2lo, t2hi = pencil_lambda_max(WMW, BULK, ds)
    res["tau2_lo"], res["tau2_hi"] = t2lo, t2hi

    if okS:
        res["verdict"] = "CERTIFIED"   # X1 branch for this edge
        return res
    # not certified PD: certified violation? (X3 branch)
    w_f, V_f = np.linalg.eigh(SNm)
    xb = [[arb(float(v))] for v in V_f[:, 0]]
    q = bm_mul(bm_T(xb), bm_mul(SN, xb))[0][0]
    if float(q.upper()) < 0.0:
        res["verdict"] = "VIOLATION-REQUIRES-REDERIVATION"
        res["notes"].append(f"certified x^T S_N x <= {float(q.upper()):.3e} < 0")
        return res
    res["verdict"] = "GAP-SN"
    res["notes"].append("S_N enclosure straddles 0")
    return res


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def run(edges_arg: str, T: float, prec: int, procs: int, cache_dir: str,
        dh_control: bool, float_only: bool = False) -> int:
    ctx.prec = prec
    kind = "DH" if dh_control else "zeta"
    print("=" * 78)
    print("X rung: interval certification of the doc-13 tracking criterion "
          f"(tau < 1), kind={kind}")
    print("=" * 78)
    print(f"prec={prec} bits, W_inf cutoff T={T:.0f}, ladder 38/hw=0.06 "
          f"cmax=2.42, procs={procs}, cache={cache_dir}")

    crosschecks_generic(HW, T)
    print("G5 kernel cross-checks (phihat, digamma envelope, tail form): PASS")

    t0 = time.time()
    lad = build_ladder(CMAX, NCENTERS, HW, GMAXS[-1], T=T_GRID, N=N_GRID)
    # audit fix (X session): build_ladder._digamma_grid sets ctx.prec = 80
    # globally and never restores it; without this reset every subsequent ball
    # operation (workers, compression, interval Cholesky, pencil bisection)
    # would silently run at 80 bits instead of --prec.  Soundness was never at
    # stake (arb is outward-rounded at any precision) but the requested
    # precision and the p{prec} cache tag were being violated.
    ctx.prec = prec
    print(f"float ladder built ({time.time()-t0:.0f}s)")
    centers = lad.centers

    if dh_control:
        edge_list = [(1.60, 1.88)]
    elif edges_arg == "all":
        edge_list = list(zip(GMAXS, GMAXS[1:]))
        edge_list.sort(key=lambda e: -REFERENCE_TAU2[e])  # informative first
    else:
        edge_list = []
        for tok in edges_arg.split(","):
            a, b = tok.split("-")
            edge_list.append((float(a), float(b)))

    # float stage + gates
    states = {}
    for (L, R) in edge_list:
        st = float_edge_state(lad, kind, L, R)
        assert st is not None and not st.get("dead"), ("edge unusable", L, R)
        states[(L, R)] = st
        if kind == "zeta":
            ref = REFERENCE_TAU2[(L, R)]
            assert abs(st["tau2"] - ref) <= G1_TOL, \
                ("G1 float tau2 drift", L, R, st["tau2"], ref)
        assert abs(st["tau2"] - st["tau_pencil"]) <= G2_TOL, \
            ("G2 pencil vs rank-2", L, R, st["tau2"], st["tau_pencil"])
        # G4 atom set / weights
        for (ln, w, _b) in st["new_atoms"]:
            nn = round(math.exp(ln))
            assert abs(math.log(nn) - ln) < 1e-9, ("atom log drift", ln)
            if kind == "zeta":
                lam = von_mangoldt_arb(nn)
                w_exact = 2 * lam / arb(nn).sqrt()
                assert float(lam.mid()) > 0, ("non prime power atom", nn)
                assert abs(float(w_exact.mid()) - w) <= G4_TOL, \
                    ("G4 weight drift", nn, w)
    print(f"float gates G1-G4 PASS on {len(edge_list)} edge(s)")
    print("float reference: " + ", ".join(
        f"{L:.2f}->{R:.2f} tau2={states[(L, R)]['tau2']:.4f}"
        for (L, R) in edge_list))
    if float_only:
        print("\nfloat-only mode: gates pass; no ball computation requested.")
        for (L, R) in sorted(edge_list):
            st = states[(L, R)]
            print(f"  {L:.2f}->{R:.2f}  dl={st['dl']:2d} ds={st['ds']}  "
                  f"cells={len(st['new_atoms']):2d}  tau2={st['tau2']:.6f}  "
                  f"tau_pencil={st['tau_pencil']:.6f}  "
                  f"|d|={abs(st['tau2']-st['tau_pencil']):.2e}")
        return 0

    # exact statement weights
    if kind == "zeta":
        def weight_of(nn: int) -> arb:
            return 2 * von_mangoldt_arb(nn) / arb(nn).sqrt()
    else:
        float_w = {round(math.exp(ln)): w for (ln, w, _b) in lad.atoms["DH"]}

        def weight_of(nn: int) -> arb:
            return arb(float_w[nn])  # float weights ARE the DH statement

    # ambient cache: g0, W_inf, atoms up to max R needed
    tag = f"n{NCENTERS}_hw{HW:.17g}_p{prec}"
    t0 = time.time()
    g0mid, g0rad = cached_matrix(
        cache_dir, f"g0_{tag}",
        lambda: _build_matrix("atom", centers, HW, {"U": 0.0}, procs))
    print(f"g(0) gram ready ({time.time()-t0:.0f}s) max rad={g0rad.max():.2e}")

    t0 = time.time()
    tail_up = float(winf_tail_envelope(HW, T).upper())
    wmid, wrad = cached_matrix(
        cache_dir, f"winf_T{T:.0f}_{tag}",
        lambda: _build_matrix("winf", centers, HW,
                              {"T": T, "g0mid": g0mid, "g0rad": g0rad,
                               "tail_up": tail_up}, procs))
    W_ball = to_balls(wmid, wrad)
    print(f"W_inf ready ({time.time()-t0:.0f}s) max rad={wrad.max():.2e} "
          f"tail={tail_up:.2e}")

    maxR = max(R for (_L, R) in edge_list)
    atom_ns = sorted({round(math.exp(ln)) for (ln, _w, _b) in lad.atoms[kind]
                      if ln < maxR})
    t0 = time.time()
    atom_balls, atom_w = {}, {}
    for nn in atom_ns:
        amid, arad = cached_matrix(
            cache_dir, f"atom{nn}_{tag}",
            lambda nn=nn: _build_matrix("atom", centers, HW,
                                        {"U": math.log(nn)}, procs))
        atom_balls[nn] = to_balls(amid, arad)
        atom_w[nn] = weight_of(nn)
    print(f"{len(atom_balls)} atom matrices ready ({time.time()-t0:.0f}s)")

    # per-edge certification
    rows = []
    for (L, R) in edge_list:
        st = states[(L, R)]
        print("\n" + "-" * 78)
        print(f"edge {L:.2f}->{R:.2f}  (dl={st['dl']}, ds={st['ds']}, "
              f"cells={len(st['new_atoms'])}, float tau2={st['tau2']:.4f}, "
              f"float tau_pencil={st['tau_pencil']:.6f})")
        row = certify_edge(st, W_ball, atom_balls, atom_w, cache_dir, procs,
                           centers, kind)
        rows.append(row)
        if "tau_mid" in row:
            print(f"  P0 midpoint tau={row['tau_mid']:.6f} "
                  f"(drift {row['p0_drift']:.2e}, limit {P0_TOL})")
        if "lamA_lb" in row:
            print(f"  A>0 CERTIFIED, lambda_min(A) >= {row['lamA_lb']:.3e}; "
                  f"rad: compressed {row['rad_compressed']:.2e}, "
                  f"S_N {row.get('rad_SN', float('nan')):.2e}, "
                  f"BULK {row.get('rad_BULK', float('nan')):.2e}")
        if row.get("tau_hi") is not None:
            tlo = row.get("tau_lo")
            print(f"  [tau] = [{tlo if tlo is not None else float('nan'):.6f}, "
                  f"{row['tau_hi']:.6f}]  width="
                  f"{(row['tau_hi']-tlo) if tlo is not None else float('nan'):.2e}"
                  f"  margin-to-1={(1.0-row['tau_hi']):.4f}")
        if row.get("tau2_hi") is not None and row.get("tau2_lo") is not None:
            print(f"  [tau_2 rank-2 form] = [{row['tau2_lo']:.6f}, "
                  f"{row['tau2_hi']:.6f}]  ||R'||_F <= {row['Rres_fro_up']:.2e}"
                  f"  ||G_perp||_F <= {row['Gperp_fro_up']:.2e}")
        if row.get("lamSN_lb", 0.0) > 0:
            print(f"  S_N > 0 CERTIFIED, lambda_min(S_N) >= {row['lamSN_lb']:.3e}")
        print(f"  VERDICT: {row['verdict']}" +
              ("" if not row["notes"] else f"  ({'; '.join(row['notes'])})"))

    # summary
    print("\n" + "=" * 78)
    print("edge          dl+ds  float tau2  [tau] enclosure          verdict")
    for row in sorted(rows, key=lambda r: r["L"]):
        st = states[(row["L"], row["R"])]
        enc = ("[{:.4f}, {:.4f}]".format(row["tau_lo"], row["tau_hi"])
               if row.get("tau_hi") is not None and row.get("tau_lo") is not None
               else "n/a")
        print(f"{row['L']:.2f}->{row['R']:.2f}   {row['dl']:2d}+{row['ds']:<2d} "
              f"  {st['tau2']:.4f}     {enc:24s} {row['verdict']}")

    verdicts = [r["verdict"] for r in rows]
    if any(v.startswith("ABORT") for v in verdicts):
        print("\nOUTCOME: ABORT (construction drift); no certificate issued.")
        return 2
    if dh_control:
        # audit fix (X session): the negative control has INVERTED semantics --
        # a certified DH violation is the control PASSING (the machinery can
        # certify a failure where doc 13 says one exists); a DH tau<1
        # certificate means the frame is dispersing and the rung dies.
        if any(v.startswith("VIOLATION") for v in verdicts):
            print("\nOUTCOME: DH CONTROL PASS -- S_N certifiably NOT PD on the "
                  "DH edge (doc 13: tau=1.554>1); the machinery certifies the "
                  "expected failure.  Not an escalation.")
            return 0
        if any(v == "CERTIFIED" for v in verdicts):
            print("\nOUTCOME: DH CONTROL FAIL -- DH certified tau<1 with a "
                  "living old block: the frame is dispersing; the rung DIES "
                  "fail-closed.")
            return 3
        print("\nOUTCOME: DH CONTROL INCONCLUSIVE (enclosure too wide).")
        return 1
    if any(v.startswith("GAP") for v in verdicts):
        print("\nOUTCOME: X2 GAP on at least one edge -- see width budget; "
              "cure is cutoff/precision, never a weakened target.")
        return 1
    if any(v.startswith("VIOLATION") for v in verdicts):
        print("\nOUTCOME: X3 -- certified tracking violation; PRE-REGISTERED "
              "discipline: independent re-derivation REQUIRED before this is "
              "recorded as a finding.  Escalate.")
        return 0
    print("\nOUTCOME: X1 -- every swept edge certifies A>0, M_c>0, BULK>0, "
          "S_N>0; hence tau < 1 holds rigorously (exact pencil equivalence) "
          "on the swept ladder edges.  This confirms the floats; doc 13's "
          "wall (no estimate-based route to uniform tau<1) stands.")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", default="4.00-4.26",
                    help='"all", or comma list like "4.00-4.26,3.76-4.00"')
    ap.add_argument("--T", type=float, default=5000.0)
    ap.add_argument("--prec", type=int, default=120)
    ap.add_argument("--procs", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    ap.add_argument("--cache-dir", default="/tmp/x_tau_cache")
    ap.add_argument("--dh-control", action="store_true")
    ap.add_argument("--float-only", action="store_true",
                    help="run the float stage and gates G1-G5 only (no balls)")
    args = ap.parse_args()
    rc = run(args.edges, args.T, args.prec, args.procs, args.cache_dir,
             args.dh_control, float_only=args.float_only)
    sys.exit(rc)


if __name__ == "__main__":
    main()
