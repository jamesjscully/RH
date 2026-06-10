"""Rigorous interval-certificate sweep over the refinement bases (T2 direction).

GOAL (T2, TODO.md "Refinement-Stable Active-Sector Theorem"): extend the
certified T1 endpoint from the default basis n25/h0.060 to the refinement
bases of prime_defect_active_atom_shift.REFINEMENTS:

    n17/h0.100  (old 13, shell 2)      n29/h0.050  (old 24, shell 3)
    n21/h0.080  (old 17, shell 2)      n33/h0.045  (old 28, shell 3)
    n25/h0.060  (old 21, shell 2; the already-certified T1 default, kept as
                 an in-sweep control)

For EACH basis the exact statement is the same as the T1 certificate
(prime_defect_t1_interval_certificate, docstring section "EXACT STATEMENT
CERTIFIED"), with only the ambient raised-cosine family and the fixed basis
matrix B changed:

    centers = linspace(0.02, 1.62 - hw, ncenters),  half_width = hw,
    B = active_state(ncenters, hw)["B"]   (floats taken as EXACT dyadic
        rationals; old block = first old_dim columns, shell = rest),
    M_+ = W_inf - sum_{n in OLD_NS} (2 Lambda(n)/sqrt n) T(log n)
              - (2 log23/sqrt23) T(log 23) - P_smooth([b23, 3.24]),
    b23 = the double 0.5*(log 23 + log 25) = 3.1771850203986753,
    W_inf = -g(0) log pi + (1/pi) int_0^inf phihat_i phihat_j Re psi(1/4+it/2),
        Arb-integrated on [0,T] with the HOLOMORPHIC SYMMETRIZATION
        (psi(1/4+it/2)+psi(1/4-it/2))/2 plus the rigorous closed-form tail
        envelope tau(T) of the T1 lemma added to every radius (the lemma is
        hw-generic: c = hw^2 - pi^2/T^2 > 0 holds for every swept hw at the
        default T = 5000).

CLAIM DECIDED PER BASIS, all arithmetic in arb balls at prec bits
(components REUSED VERBATIM from prime_defect_t1_interval_certificate:
atom_matrix_ball / smooth_matrix_ball / winf_matrix_ball with ENDPOINT_SLOP
= 1e-13 on every overlap entry, compress with symmetric-pair intersection,
interval_cholesky, forward_substitute):

    A_+ > 0   (pivot-complete interval Cholesky, old_dim pivots), and
    H = D - C^T A_+^{-1} C > 0 by PIVOT-COMPLETE INTERVAL CHOLESKY ON H
        (shell_dim pivots, each with a rigorous positive lower bound).

The H-side decision is the dimension-generic replacement for the default
certificate's 2x2 Sylvester step, as required for the 3D shells (n29, n33).
For shell_dim = 2 the h11 / det H balls are also printed as a cross-check
against the T1 certificate format.  Success of interval Cholesky certifies
every symmetric matrix in the ball family PD, in particular the true H.

FAIL-CLOSED GATES, fixed before the run (any failure => verdict ABORT for
that basis, no certificate language):
  D1 snapshot reproduction: the FLOAT pipeline eigmin(H) recomputed here
     (t1_matrices midpoints, the exact code path that produced the TODO.md
     refinement table) must equal the hardcoded snapshot value to 6e-9
     (the snapshot is printed to 7 significant digits).  A mismatch is a
     fail-closed finding to report, never to tune away.
  D2 statement drift: cell bounds == (3.0, 3.1771850203986753), right ==
     3.24, repair atom == 23, for every basis.
  D3 old-atom set == {2,3,4,5,7,8,9,11,13,16,17,19} (prime powers < e^3).
  D4 grid-derived atom weight vs exact 2 log23/sqrt23 within 1e-10.
  D5 analytic cross-checks at the basis hw: arb_phi_hat vs float _phihat
     (first/middle/last center, |diff| < 1e-10), digamma envelope dominance
     samples, closed-form tail vs scipy envelope bracket [0.9x, 10x].
  P0 midpoint drift gate: the all-ball MIDPOINT endpoint eigmin(H_mid) must
     be within 2e-3 of the float snapshot eigmin.  Rationale, fixed in
     advance: the certified statement (exact W_inf) differs from the
     Fourier-grid floats by +1.75e-4 in eigmin at hw=0.06 (T1 record), and
     the W_inf grid-truncation envelope scales like 1/c^2, a factor <= 4.5
     at hw=0.045, so the expected systematic is < 1e-3; gross construction
     drift (the starved-T control aborted at -0.227) is orders larger.

PRE-REGISTERED READINGS (fixed before the computation):
  R1 ALL FIVE bases CERTIFIED (A_+ > 0 and all H pivots strictly positive)
     => the H > 0 endpoint is refinement-stable at certificate grade across
     the tested bases; T2's "main weakness" line in TODO.md (3D shells SPD
     numerically but without rigorous matrix-entry bounds) is discharged AT
     THE TESTED BASES.  Per the standing asymmetry this only confirms the
     floats; it does not extend the asymptotic mechanism (R1 verdict in the
     risk ladder stands), and says nothing about bases not swept.
  R2 some basis fails to certify because an enclosure straddles 0 (GAP)
     => report the per-ingredient width-budget ledger and which ingredient
     dominates; the cure is more cutoff/precision, NOT a weakened target.
     Expected stress point fixed in advance: n17 has the smallest margin
     (eigmin 4.9e-3, ~5x below the default's 2.5e-2) while the fine-hw
     bases have the largest tail envelopes and basis l1 factors.
  R3 some basis has a CERTIFIED NEGATIVE pivot (upper bound < 0, all
     earlier pivots certified positive) on the H side
     => REFUTATION of refinement stability of the H > 0 endpoint: the
     major-result branch; escalate immediately.  (Certified negative pivot
     on the A_+ side is likewise refutation-grade for the old block.)

Exit codes: 0 = every swept basis reached a DEFINITE outcome (CERTIFIED or
REFUTED); 1 = at least one GAP and no ABORT; 2 = at least one ABORT.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t2_interval_sweep                 # full sweep
    python3 -m scripts.numerics.witness.prime_defect_t2_interval_sweep --bases 17      # one basis
    python3 -m scripts.numerics.witness.prime_defect_t2_interval_sweep --T 2000        # looser tail
"""
from __future__ import annotations

import argparse
import math
import sys
import time

import numpy as np
from flint import acb, arb, ctx

from .prime_defect_active_atom_shift import REFINEMENTS, active_state
from .prime_defect_default_t1_certificate import t1_matrices
from .prime_defect_t1_interval_certificate import (
    ENDPOINT_SLOP,
    OLD_NS_EXPECTED,
    _ball,
    atom_matrix_ball,
    compress,
    forward_substitute,
    interval_cholesky,
    mat_scale,
    mat_sub,
    max_mid,
    max_rad,
    mid_np,
    smooth_matrix_ball,
    von_mangoldt_arb,
    winf_matrix_ball,
    winf_tail_envelope,
)
from .prime_defect_t1_winf_tail import arb_phi_hat, winf_tail_bound
from .semilocal_2 import _phihat

# TODO.md "Current Evidence Snapshot", refinement H=S+G table (floats).
SNAPSHOT_EIGMIN = {
    (17, 0.10): +4.897369e-03,
    (21, 0.08): +4.989831e-03,
    (25, 0.06): +2.493626e-02,
    (29, 0.05): +5.153857e-02,
    (33, 0.045): +2.760913e-02,
}
B23_DOUBLE = 3.1771850203986753  # the double 0.5*(log 23 + log 25)
FLOAT_SNAPSHOT_TOL = 6e-9        # D1 (7 printed significant digits)
P0_DRIFT_TOL = 2e-3              # P0 (justified in module docstring)


class DriftAbort(Exception):
    """A fail-closed gate fired; no certificate language for this basis."""


# ---------------------------------------------------------------------------
# gates
# ---------------------------------------------------------------------------

def gate_float_snapshot(ncenters: int, hw: float) -> tuple[float, dict]:
    """D1: rerun the float pipeline that produced the TODO refinement table."""
    model = t1_matrices(ncenters, hw)
    eig_float = float(np.linalg.eigvalsh(model["H"])[0])
    ref = SNAPSHOT_EIGMIN[(ncenters, hw)]
    drift = abs(eig_float - ref)
    print(f"D1 float pipeline eigmin(H) = {eig_float:+.12e} "
          f"(snapshot {ref:+.6e}, drift {drift:.3e}, tol {FLOAT_SNAPSHOT_TOL:.0e})")
    if drift > FLOAT_SNAPSHOT_TOL:
        raise DriftAbort(
            f"D1 snapshot reproduction failed: {eig_float!r} vs {ref!r}")
    return eig_float, model


def gate_statement(state: dict) -> None:
    """D2/D3/D4: the exact statement is the one fixed in the docstring."""
    lo, hi = state["cell"]
    if not (lo == 3.0 and hi == B23_DOUBLE and float(state["right"]) == 3.24
            and int(state["repair_n"]) == 23):
        raise DriftAbort(f"D2 statement drift: cell={state['cell']!r} "
                         f"right={state['right']!r} repair={state['repair_n']!r}")
    old_ns = sorted(n for n in state["ambient"].atoms["zeta"]
                    if math.log(n) < state["left"])
    if tuple(old_ns) != OLD_NS_EXPECTED:
        raise DriftAbort(f"D3 old atom set drift: {old_ns!r}")
    w_exact = 2 * arb(23).log() / arb(23).sqrt()
    if abs(float(w_exact.mid()) - state["atom_weight"]) > 1e-10:
        raise DriftAbort(f"D4 atom weight drift: {state['atom_weight']!r}")
    print(f"D2/D3/D4 statement gates: PASS (cell=[3.0,{B23_DOUBLE!r}], "
          f"12 old atoms, exact-weight drift "
          f"{abs(float(w_exact.mid()) - state['atom_weight']):.2e})")


def gate_analytic(centers: np.ndarray, hw: float, T: float) -> None:
    """D5: per-basis analogue of the T1 cross-checks."""
    probe = (float(centers[0]), float(centers[len(centers) // 2]),
             float(centers[-1]))
    for c in probe:
        for t in (1e-3, 1.0, 7.5, math.pi / hw, 300.0):
            a = float(arb_phi_hat(c, hw, acb(t)).real.mid())
            f = float(_phihat(np.array([t]), c, hw)[0])
            if abs(a - f) > 1e-10:
                raise DriftAbort(f"D5 phihat mismatch c={c} t={t}: {a} vs {f}")
    for t in (2.0, 10.0, T, 2 * T, 10 * T, 100 * T):
        re_psi = abs(float(acb(0.25, 0.5 * t).digamma().real.mid()))
        if re_psi > math.log(t) + math.log(2.0) + 1.0:
            raise DriftAbort(f"D5 digamma envelope fails at t={t}")
    tau = float(winf_tail_envelope(hw, T).mid())
    tau_scipy = winf_tail_bound(hw, T)
    if not (0.9 * tau_scipy <= tau <= 10.0 * tau_scipy):
        raise DriftAbort(f"D5 tail bracket: closed {tau:.3e} scipy {tau_scipy:.3e}")
    print(f"D5 analytic gates: PASS (hw={hw}, tail tau({T:.0f})={tau:.3e})")


# ---------------------------------------------------------------------------
# per-basis certificate
# ---------------------------------------------------------------------------

def run_basis(ncenters: int, hw: float, T: float) -> dict:
    out: dict = {"basis": f"n{ncenters}/h{hw:.3f}", "verdict": "ABORT",
                 "detail": "", "t_wall": 0.0}
    t_basis = time.time()
    print("=" * 78)
    print(f"T2 interval certificate: basis n{ncenters}/h{hw:.3f}, T={T:.0f}")
    print("=" * 78)
    try:
        eig_float, _model = gate_float_snapshot(ncenters, hw)
        state = active_state(ncenters, hw)
        gate_statement(state)
        ambient = state["ambient"]
        centers = ambient.centers
        Bf = state["B"]
        old_dim = int(state["old_dim"])
        shell_dim = Bf.shape[1] - old_dim
        out.update({"old_dim": old_dim, "shell_dim": shell_dim,
                    "eig_float": eig_float})
        print(f"centers [{centers[0]:.3f}..{centers[-1]:.3f}] x{len(centers)}, "
              f"old_dim={old_dim}, shell_dim={shell_dim}")
        gate_analytic(centers, hw, T)

        ledger: list[tuple[str, float, float]] = []

        # --- ambient ball ingredients (T1 components, per-basis centers/hw)
        t0 = time.time()
        g0 = atom_matrix_ball(centers, hw, 0.0)
        ledger.append(("g(0) overlap gram", max_mid(g0), max_rad(g0)))
        print(f"g(0) gram done ({time.time()-t0:.1f}s) max rad={max_rad(g0):.2e}")

        t0 = time.time()
        tail = winf_tail_envelope(hw, T)
        W = winf_matrix_ball(centers, hw, T, g0)
        ledger.append((f"W_inf (T={T:.0f} + tail {float(tail.upper()):.2e})",
                       max_mid(W), max_rad(W)))
        print(f"W_inf done ({time.time()-t0:.1f}s) max rad={max_rad(W):.2e}")

        t0 = time.time()
        n_amb = len(centers)
        old_sum = [[arb(0)] * n_amb for _ in range(n_amb)]
        for n in OLD_NS_EXPECTED:
            w_n = 2 * von_mangoldt_arb(n) / arb(n).sqrt()
            atom_n = atom_matrix_ball(centers, hw, math.log(n))
            for i in range(n_amb):
                for j in range(n_amb):
                    old_sum[i][j] = old_sum[i][j] + w_n * atom_n[i][j]
        ledger.append(("old atoms (12 prime powers < e^3)",
                       max_mid(old_sum), max_rad(old_sum)))
        print(f"old atoms done ({time.time()-t0:.1f}s) max rad={max_rad(old_sum):.2e}")

        t0 = time.time()
        w23 = 2 * arb(23).log() / arb(23).sqrt()
        atom23 = mat_scale(atom_matrix_ball(centers, hw, math.log(23)), w23)
        ledger.append(("atom(23), weight 2log23/sqrt23",
                       max_mid(atom23), max_rad(atom23)))
        suffix = smooth_matrix_ball(centers, hw, float(state["cell"][1]),
                                    float(state["right"]))
        ledger.append(("smooth suffix", max_mid(suffix), max_rad(suffix)))
        print(f"atom(23) + smooth suffix done ({time.time()-t0:.1f}s)")

        M = mat_sub(mat_sub(mat_sub(W, old_sum), atom23), suffix)
        ledger.append(("ambient M_+", max_mid(M), max_rad(M)))
        t0 = time.time()
        Mc = compress(M, Bf)
        ledger.append(("compressed B^T M_+ B", max_mid(Mc), max_rad(Mc)))
        print(f"compression done ({time.time()-t0:.1f}s) max rad={max_rad(Mc):.2e}")

        A = [[Mc[i][j] for j in range(old_dim)] for i in range(old_dim)]
        C = [[Mc[i][old_dim + j] for j in range(shell_dim)] for i in range(old_dim)]
        D = [[Mc[old_dim + i][old_dim + j] for j in range(shell_dim)]
             for i in range(shell_dim)]

        # --- P0 midpoint drift gate ----------------------------------------
        Mc_mid = mid_np(Mc)
        A_m = Mc_mid[:old_dim, :old_dim]
        C_m = Mc_mid[:old_dim, old_dim:]
        D_m = Mc_mid[old_dim:, old_dim:]
        H_mid = D_m - C_m.T @ np.linalg.solve(A_m, C_m)
        eig_mid = np.linalg.eigvalsh(0.5 * (H_mid + H_mid.T))
        drift = abs(float(eig_mid[0]) - eig_float)
        out["eig_mid"] = float(eig_mid[0])
        print(f"P0 midpoint endpoint: eigmin(H_mid) = {eig_mid[0]:+.12e}  "
              f"(float {eig_float:+.12e}, drift {drift:.3e}, tol {P0_DRIFT_TOL:.0e})")
        if drift > P0_DRIFT_TOL:
            raise DriftAbort(f"P0 midpoint drift {drift:.3e} > {P0_DRIFT_TOL}")

        # --- A_+ > 0 ---------------------------------------------------------
        ok_a, L, piv_a = interval_cholesky(A, old_dim)
        min_piv = min((float(p.lower()) for p in piv_a), default=float("nan"))
        max_piv_rad = max((float(p.rad()) for p in piv_a), default=float("nan"))
        ledger.append(("A_+ Cholesky pivots", min_piv, max_piv_rad))
        print(f"A_+ interval Cholesky: {len(piv_a)}/{old_dim} pivots, "
              f"min pivot lower bound={min_piv:+.6e}, max rad={max_piv_rad:.2e}")
        if not ok_a:
            if piv_a[-1] < 0:
                out["verdict"] = "REFUTED"
                out["detail"] = (f"A_+ pivot {len(piv_a)} certifiably negative: "
                                 f"{_ball(piv_a[-1])}")
                print("A_+ has a certified NEGATIVE pivot -> old block NOT PD.")
                print("OUTCOME: REFUTED (R3 branch, old block). ESCALATE.")
            else:
                out["verdict"] = "GAP"
                out["detail"] = f"A_+ pivot {len(piv_a)} straddles 0"
                print("A_+ pivot straddles 0: GAP (width too large).")
            _print_ledger(ledger)
            return out
        print(f"A_+ > 0 CERTIFIED (all {old_dim} pivot balls strictly positive).")

        # --- H = D - V^T V, pivot-complete interval Cholesky on H ------------
        V = forward_substitute(L, C, old_dim, shell_dim)
        H = [[D[i][j] - sum((V[k][i] * V[k][j] for k in range(old_dim)), arb(0))
              for j in range(shell_dim)] for i in range(shell_dim)]
        ledger.append(("H entries", max_mid(H), max_rad(H)))
        print(f"\nH = S+G enclosure ({shell_dim}x{shell_dim}):")
        for i in range(shell_dim):
            print("   " + "  ".join(_ball(H[i][j]) for j in range(shell_dim)))
        if shell_dim == 2:
            det2 = H[0][0] * H[1][1] - H[0][1] * H[1][0]
            ledger.append(("det H (2x2 cross-check)",
                           abs(float(det2.mid())), float(det2.rad())))
            print(f"   2x2 cross-check: h11 = {_ball(H[0][0])}, det H = {_ball(det2)}")

        ok_h, _Lh, piv_h = interval_cholesky(H, shell_dim)
        det_ball = piv_h[0]
        for p in piv_h[1:]:
            det_ball = det_ball * p
        out["pivots_H"] = [( float(p.mid()), float(p.rad()), float(p.lower()))
                           for p in piv_h]
        print(f"\nH interval Cholesky pivots ({len(piv_h)}/{shell_dim}):")
        for k, p in enumerate(piv_h):
            lo_k = float(p.lower())
            ratio = lo_k / max(float(p.rad()), 1e-300)
            print(f"   pivot {k+1}: {_ball(p)}  lower={lo_k:+.6e}  "
                  f"margin/width={ratio:.2e}")
        if ok_h:
            print(f"   det H (pivot product) = {_ball(det_ball)}")
        ledger.append(("H Cholesky pivots",
                       min(float(p.lower()) for p in piv_h),
                       max(float(p.rad()) for p in piv_h)))
        _print_ledger(ledger)

        if ok_h:
            out["verdict"] = "CERTIFIED"
            out["min_pivot_lower"] = min(float(p.lower()) for p in piv_h)
            out["max_pivot_rad"] = max(float(p.rad()) for p in piv_h)
            out["detail"] = (f"{shell_dim} H pivots > 0, min lower "
                             f"{out['min_pivot_lower']:+.3e}")
            print(f"\nOUTCOME: CERTIFIED -- A_+ > 0 and H > 0 "
                  f"(pivot-complete interval Cholesky, rigorous balls).")
            print("  Every nonzero shell direction y satisfies y^T(S+G)y > 0 for")
            print("  the exact statement (module docstring) at this basis.")
        elif piv_h[-1] < 0:
            out["verdict"] = "REFUTED"
            out["detail"] = (f"H pivot {len(piv_h)} certifiably negative: "
                             f"{_ball(piv_h[-1])} (earlier pivots certified > 0)")
            print("\nOUTCOME: REFUTED -- H has a certified negative pivot while")
            print("  A_+ > 0 is certified: H is NOT positive definite at this")
            print("  basis.  R3 branch (refinement stability fails): ESCALATE.")
        else:
            out["verdict"] = "GAP"
            out["detail"] = f"H pivot {len(piv_h)} straddles 0: {_ball(piv_h[-1])}"
            print("\nOUTCOME: GAP -- an H pivot straddles 0; see width budget.")
        return out
    except DriftAbort as exc:
        out["verdict"] = "ABORT"
        out["detail"] = str(exc)
        print(f"ABORT (fail-closed gate): {exc}")
        return out
    finally:
        out["t_wall"] = time.time() - t_basis
        print(f"[basis wall time {out['t_wall']:.1f}s]")


def _print_ledger(ledger) -> None:
    print("\nWidth budget ledger (per ingredient):")
    print(f"      {'ingredient':44s} {'max|mid| / min':>14s} {'max rad':>10s}")
    for name, mid, rad in ledger:
        print(f"      {name:44s} {mid:+.6e} {rad:10.2e}")


# ---------------------------------------------------------------------------
# sweep driver
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--T", type=float, default=5000.0)
    parser.add_argument("--prec", type=int, default=120)
    parser.add_argument("--bases", type=int, nargs="*", default=None,
                        help="subset of ncenters values, e.g. --bases 17 21")
    args = parser.parse_args()
    ctx.prec = args.prec

    todo = [(n, h) for n, h in REFINEMENTS
            if args.bases is None or n in args.bases]
    results = [run_basis(n, h, args.T) for n, h in todo]

    print("\n" + "=" * 78)
    print("T2 sweep verdict table")
    print("=" * 78)
    print(f"   {'basis':<12} {'old+shell':<10} {'float eigmin':>13} "
          f"{'mid eigmin':>13} {'verdict':<10} detail")
    for r in results:
        dims = (f"{r.get('old_dim','?')}+{r.get('shell_dim','?')}"
                if "old_dim" in r else "?")
        ef = f"{r['eig_float']:+.6e}" if "eig_float" in r else "-"
        em = f"{r['eig_mid']:+.6e}" if "eig_mid" in r else "-"
        print(f"   {r['basis']:<12} {dims:<10} {ef:>13} {em:>13} "
              f"{r['verdict']:<10} {r['detail']}")
    verdicts = {r["verdict"] for r in results}
    if "ABORT" in verdicts:
        sys.exit(2)
    if "GAP" in verdicts:
        sys.exit(1)
    if "REFUTED" in verdicts:
        print("\nREFUTATION present: escalate immediately (R3).")
    sys.exit(0)


if __name__ == "__main__":
    main()
