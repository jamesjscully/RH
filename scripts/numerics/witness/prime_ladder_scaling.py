"""R1b ladder-scaling witness: push the nested pole-killed chain toward R ~ 6.

Purpose (research/proof/TODO.md, rung R1b). The proof track's candidate lemmas were built
from one late edge at R ~ 3.24, where repair is carried by a single atom (n=23) inside one
cell. Two structural facts say that mechanism cannot be asymptotic: cells shrink like
e^{-R} while the window (L,R] holds ~ e^R atoms, and unconditional Chebyshev bounds diverge
relative to O(1) Schur margins. This witness measures, per nested edge L -> R:

    dim(H_L), shell dim, atoms in (L,R],
    eigmin(A)            -- the induction margin on the old window,
    eigmin(J_R)          -- full-window margin,
    Schur min            -- shell obstruction,
    rho                  -- transfer norm ||A^{-1/2} C D^{-1/2}||^2,
    chronological cell mechanism on the shell:
        base Schur (smooth new), final Schur (exact new), peak debt,
        repair concentration (top positive jump / sum of positive jumps).

Fail-closed readings:
    * Schur surplus decaying to 0 faster than eigmin(A): the storage step cannot stay
      cell-local; the sectoral lemma shape dies.
    * repair concentration falling with R: single-atom repair is a small-R artifact and
      the lemma must be restated statistically (this is the expected outcome).
    * DH must keep failing on the same ladder; if DH ever passes an edge, the whole
      target is dispersing and dies.

Run:
    python3 -m scripts.numerics.witness.prime_ladder_scaling
    python3 -m scripts.numerics.witness.prime_ladder_scaling --quick   (coarser, ~1/4 cost)

Numerical caveats: Fourier grid T=300 truncation gives ~1e-6 entry error (see
prime_defect_t1_winf_tail.py); margins below ~1e-5 are not trustworthy here and are
flagged. This is a scaling diagnostic, not a certificate.
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
from flint import acb, ctx

from .prime_carleson_flow import _gram_orthonormalize, _raised_cosine_even, _sym, coefficient_table
from .semilocal_2 import _phihat, _phihat_ihalf


# ---------------------------------------------------------------------------
# self-contained fast kernels (no zeta zeros, vectorized atoms)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Ladder:
    centers: np.ndarray
    hw: float
    ts: np.ndarray
    dt: float
    PH: np.ndarray          # (n, N) phihat values
    Winf: np.ndarray
    l2: np.ndarray
    v0: np.ndarray
    vih: np.ndarray
    atoms: dict[str, list[tuple[float, float, np.ndarray]]]   # kind -> [(logn, weight, block)]


def _digamma_grid(ts: np.ndarray) -> np.ndarray:
    ctx.prec = 80
    return np.array([float(acb(0.25, t / 2).digamma().real) for t in ts])


def build_ladder(cmax: float, ncenters: int, hw: float, max_gmax: float,
                 T: float = 300.0, N: int = 120001, ngrid_l2: int = 12001) -> Ladder:
    centers = np.linspace(0.02, cmax, ncenters)
    ts = np.linspace(-T, T, N)
    dt = ts[1] - ts[0]
    psi = _digamma_grid(ts)
    PH = np.array([_phihat(ts, c, hw) for c in centers])

    scale = dt / (2.0 * np.pi)
    G0 = (PH @ PH.T) * scale
    Winf = _sym(-math.log(math.pi) * G0 + ((PH * psi) @ PH.T) * scale)

    umax = cmax + hw
    u = np.linspace(-umax, umax, ngrid_l2)
    basis = _raised_cosine_even(centers, hw, u)
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    n = len(centers)
    l2 = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            l2[i, j] = l2[j, i] = float(trap(basis[i] * basis[j], x=u))

    v0 = np.array([_phihat(np.array([0.0]), c, hw)[0] for c in centers])
    vih = np.array([_phihat_ihalf(c, hw) for c in centers])

    max_n = max(2, int(math.floor(math.exp(max_gmax) - 1e-12)))
    atoms: dict[str, list[tuple[float, float, np.ndarray]]] = {}
    for kind in ("zeta", "DH"):
        coeffs = coefficient_table(kind, max_n)
        rows = []
        for m in range(2, max_n + 1):
            coeff = coeffs[m - 1]
            if abs(coeff) < 1e-12:
                continue
            logn = math.log(m)
            if logn >= max_gmax:
                continue
            weight = 2.0 * coeff / math.sqrt(m)
            block = _sym(weight * ((PH * np.cos(logn * ts)) @ PH.T) * scale)
            rows.append((logn, weight, block))
        atoms[kind] = rows
    return Ladder(centers=centers, hw=hw, ts=ts, dt=dt, PH=PH, Winf=Winf,
                  l2=l2, v0=v0, vih=vih, atoms=atoms)


def smooth_block(lad: Ladder, a: float, b: float) -> np.ndarray:
    """Projected form of the smooth Euler surrogate 2 e^{U/2} dU on [a,b]:
    w(t) = 2 Re[(e^{b(1/2+it)} - e^{a(1/2+it)}) / (1/2+it)]."""
    s = 0.5 + 1j * lad.ts
    w = 2.0 * np.real((np.exp(b * s) - np.exp(a * s)) / s)
    return _sym(((lad.PH * w) @ lad.PH.T) * lad.dt / (2.0 * np.pi))


def margin_at(lad: Ladder, kind: str, gmax: float) -> np.ndarray:
    M = lad.Winf.copy()
    for logn, _w, block in lad.atoms[kind]:
        if logn < gmax:
            M = M - block
    return _sym(M)


def nested_basis(lad: Ladder, gmax: float) -> np.ndarray:
    idx = np.flatnonzero(lad.centers + lad.hw <= gmax / 2.0 + 1e-12)
    if len(idx) <= 2:
        return np.zeros((len(lad.centers), 0))
    constraints = np.vstack([lad.v0[idx], lad.vih[idx]])
    _u, _s, vt = np.linalg.svd(constraints)
    null_sel = vt[2:].T
    embed = np.zeros((len(lad.centers), len(idx)))
    embed[idx, np.arange(len(idx))] = 1.0
    return _gram_orthonormalize(embed @ null_sel, lad.l2)


# ---------------------------------------------------------------------------
# per-edge extension + chronological mechanism
# ---------------------------------------------------------------------------


def _schur_stats(block: np.ndarray, dl: int) -> dict:
    A = _sym(block[:dl, :dl])
    D = _sym(block[dl:, dl:])
    C = block[:dl, dl:]
    a_eigs = np.linalg.eigvalsh(A)
    d_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    out = {"a_min": float(a_eigs[0]), "d_min": float(d_eigs[0]),
           "schur_min": float("nan"), "rho": float("nan")}
    if D.size and a_eigs[0] > 1e-12:
        schur = _sym(D - C.T @ np.linalg.solve(A, C))
        out["schur_min"] = float(np.linalg.eigvalsh(schur)[0])
        if d_eigs[0] > 1e-12:
            wa, Va = np.linalg.eigh(A)
            wd, Vd = np.linalg.eigh(D)
            Ai = (Va / np.sqrt(wa)) @ Va.T
            Di = (Vd / np.sqrt(wd)) @ Vd.T
            K = Ai @ C @ Di
            sv = np.linalg.svd(K, compute_uv=False)
            out["rho"] = float(sv[0] ** 2)
    return out


def edge_row(lad: Ladder, kind: str, L: float, R: float) -> dict:
    Ql = nested_basis(lad, L)
    Qr = nested_basis(lad, R)
    if Ql.shape[1] == 0 or Qr.shape[1] == 0:
        return {}
    proj = Ql.T @ lad.l2 @ Qr
    shell = _gram_orthonormalize(Qr - Ql @ proj, lad.l2)
    B = np.column_stack([Ql, shell])
    dl = Ql.shape[1]
    MR = margin_at(lad, kind, R)
    block = _sym(B.T @ MR @ B)
    stats = _schur_stats(block, dl)
    win_eigs = np.linalg.eigvalsh(_sym(Qr.T @ MR @ Qr))

    new_atoms = [(logn, w, blk) for (logn, w, blk) in lad.atoms[kind] if L <= logn < R]

    mech = {"base_schur": float("nan"), "final_schur": float("nan"),
            "peak_debt": float("nan"), "top_share": float("nan"), "ncells": len(new_atoms)}
    if new_atoms and stats["a_min"] > 1e-12 and shell.shape[1]:
        logs = [a[0] for a in new_atoms]
        bounds = [L] + [0.5 * (x + y) for x, y in zip(logs, logs[1:])] + [R]
        # base margin: exact history < L, smooth surrogate on [L, R]
        Mbase = margin_at(lad, kind, L) - smooth_block(lad, L, R)
        cur = _sym(B.T @ Mbase @ B)
        mins = []
        s0 = _schur_stats(cur, dl)
        mins.append(s0["schur_min"])
        jumps = []
        for (lo, hi), (logn, w, blk) in zip(zip(bounds, bounds[1:]), new_atoms):
            Ej = smooth_block(lad, lo, hi) - blk
            cur = _sym(cur + B.T @ Ej @ B)
            sj = _schur_stats(cur, dl)
            jumps.append(sj["schur_min"] - mins[-1])
            mins.append(sj["schur_min"])
        mins_arr = np.array(mins, dtype=float)
        pos = [j for j in jumps if np.isfinite(j) and j > 0]
        mech = {
            "base_schur": float(mins_arr[0]),
            "final_schur": float(mins_arr[-1]),
            "peak_debt": float(max(0.0, -np.nanmin(mins_arr))),
            "top_share": float(max(pos) / sum(pos)) if pos else float("nan"),
            "ncells": len(new_atoms),
        }

    return {
        "kind": kind, "L": L, "R": R,
        "dl": dl, "ds": int(shell.shape[1]),
        "win_min": float(win_eigs[0]),
        **stats, **mech,
    }


def _fit_rate(xs: list[float], ys: list[float]) -> float:
    pts = [(x, math.log(y)) for x, y in zip(xs, ys) if np.isfinite(y) and y > 0]
    if len(pts) < 3:
        return float("nan")
    x = np.array([p[0] for p in pts])
    z = np.array([p[1] for p in pts])
    return float(np.polyfit(x, z, 1)[0])


def summary(quick: bool = False) -> dict:
    print("=" * 96)
    print("R1b ladder-scaling witness: nested pole-killed chain toward R ~ 6")
    print("=" * 96)
    if quick:
        cmax, ncenters, hw, T, N = 2.42, 38, 0.06, 250.0, 100001
        gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
                 4.00, 4.26, 4.50, 4.76, 4.96)
    else:
        cmax, ncenters, hw, T, N = 2.89, 46, 0.06, 300.0, 120001
        gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
                 4.00, 4.26, 4.50, 4.76, 5.00, 5.26, 5.50, 5.76, 5.90)
    max_gmax = gmaxs[-1]
    print(f"ambient: ncenters={ncenters}, hw={hw}, cmax={cmax}, T={T}, N={N}, "
          f"max gmax={max_gmax} (atoms to n={int(math.exp(max_gmax))})")
    lad = build_ladder(cmax, ncenters, hw, max_gmax, T=T, N=N)
    print(f"atoms: zeta={len(lad.atoms['zeta'])}, DH={len(lad.atoms['DH'])}")

    results: dict[str, list[dict]] = {}
    for kind in ("zeta", "DH"):
        rows = []
        for L, R in zip(gmaxs, gmaxs[1:]):
            row = edge_row(lad, kind, L, R)
            if row:
                rows.append(row)
        results[kind] = rows
        print(f"\n[{kind}] nested extension ladder")
        print("   edge          dim      cells  eigmin(A)   win min     Schur min   rho      "
              "base->final Schur     peak debt  top share")
        for r in rows:
            print(f"   {r['L']:.2f}->{r['R']:.2f}  {r['dl']:2d}+{r['ds']:<2d}   "
                  f"{r['ncells']:3d}   {r['a_min']:+.3e}  {r['win_min']:+.3e}  "
                  f"{r['schur_min']:+.3e}  {r['rho']:5.3f}   "
                  f"{r['base_schur']:+.2e}->{r['final_schur']:+.2e}   "
                  f"{r['peak_debt']:.2e}   {r['top_share']:.3f}")

    zr = results["zeta"]
    late = [r for r in zr if r["R"] >= 3.0]
    rate_a = _fit_rate([r["R"] for r in late], [r["a_min"] for r in late])
    rate_s = _fit_rate([r["R"] for r in late], [r["schur_min"] for r in late])
    print("\n[scaling fits over edges with R >= 3.0] (d/dR of log margin)")
    print(f"   eigmin(A) rate:   {rate_a:+.3f} per unit R "
          f"(margin ~ e^{{{rate_a:+.2f} R}})")
    print(f"   Schur-min rate:   {rate_s:+.3f} per unit R")
    shares = [(r["R"], r["top_share"], r["ncells"]) for r in zr
              if np.isfinite(r.get("top_share", float("nan")))]
    print("\n[repair concentration] top positive Schur jump / total positive jumps")
    for R, share, ncells in shares:
        print(f"   R={R:.2f}  cells={ncells:3d}  top share={share:.3f}")

    print("\nInterpretation:")
    print("  * eigmin(A) is the induction margin; its decay rate vs the Schur-min decay rate")
    print("    decides whether cell-local storage can survive (fail-closed if Schur dies faster).")
    print("  * top share falling with R = single-atom repair is a small-R artifact; the lemma")
    print("    must be restated at the aggregated/statistical level.")
    print("  * DH must stay broken on every edge; a DH pass would kill the target as dispersing.")
    print("  * entries below ~1e-5 are within Fourier-truncation noise (T1 tail budget); treat")
    print("    such margins as 'consistent with zero', not as certified signs.")
    return results


if __name__ == "__main__":
    summary(quick="--quick" in sys.argv[1:])
