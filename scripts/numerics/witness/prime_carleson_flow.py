"""Prime-Toeplitz / passive-scattering flow diagnostic.

This is a follow-up to ``research/work/G-prime-carleson.md``.  It tests the
proposed "prime sampling is contractive in the archimedean/Sonin norm" picture
in the actual pole-killed Weil convention used by ``semilocal_2``.

The important correction is that, after writing the Weil-positive test as
``g = h * h#``, the prime term is not a sum of point-evaluation squares
``|h(log n)|^2``.  It is a translation/correlation operator

    g(log n) = <h, tau_{log n} h>.

So each prime-power contribution is a symmetric Toeplitz/cosine kernel, often
indefinite on a finite Sonin window.  The right finite diagnostic is therefore
not "does each rank-one atom fit under the current margin?", but:

    M_N = W_infty - sum_{2 <= n <= N} 2 c(n) n^{-1/2} T_{log n}

on the pole-killed subspace, tracking how the coefficient pattern repairs or
destroys the margin as new logarithms enter.

Run:
    python3 -m scripts.numerics.witness.prime_carleson_flow
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from .explicit_formula import dh_coeffs, log_deriv_coeffs
from .semilocal_2 import _grids, _phihat, _proj_null, build_gram


def _sym(M: np.ndarray) -> np.ndarray:
    return 0.5 * (M + M.T)


def _eig_range(M: np.ndarray) -> tuple[float, float]:
    ev = np.linalg.eigvalsh(_sym(M))
    return float(ev[0]), float(ev[-1])


def _min_eigenpair(M: np.ndarray) -> tuple[float, np.ndarray]:
    ev, vecs = np.linalg.eigh(_sym(M))
    return float(ev[0]), vecs[:, 0]


def _restricted_relative_eigs(jump: np.ndarray, margin: np.ndarray) -> np.ndarray:
    """Eigenvalues of margin^{-1/2} jump margin^{-1/2} on margin's positive subspace.

    When the current margin is already indefinite, this remains a useful scale
    diagnostic but no longer gives a Loewner-preservation criterion.
    """
    w, V = np.linalg.eigh(_sym(margin))
    tol = 1e-10 * max(1.0, float(np.max(np.abs(w))))
    keep = w > tol
    if not np.any(keep):
        return np.array([np.nan])
    inv_half = (V[:, keep] / np.sqrt(w[keep])) @ V[:, keep].T
    return np.linalg.eigvalsh(_sym(inv_half @ jump @ inv_half))


def _toeplitz_atom(centers: np.ndarray, hw: float, U: float, weight: float) -> np.ndarray:
    """Projected bilinear atom weight * g_ij(U) for g_ij = phi_i * phi_j#.

    ``semilocal_2`` works in Fourier variables:

        g_ij(U) = (1/2pi) int phihat_i(t) phihat_j(t) cos(U t) dt.

    This is a translation/correlation kernel, not a point-evaluation square.
    """
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    ph = np.array([_phihat(ts, c, hw) for c in centers])
    cos_u = np.cos(U * ts)
    n = len(centers)
    atom = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            val = weight * np.sum(ph[i] * ph[j] * cos_u) * dt / (2.0 * np.pi)
            atom[i, j] = atom[j, i] = float(val)
    return atom


def _raised_cosine_even(centers: np.ndarray, hw: float, u: np.ndarray) -> np.ndarray:
    """Physical raised-cosine basis values, folded evenly around zero."""

    def one_side(x: np.ndarray, center: float) -> np.ndarray:
        rel = (x - center) / hw
        out = np.zeros_like(x, dtype=float)
        mask = np.abs(rel) <= 1.0
        out[mask] = np.cos(np.pi * (x[mask] - center) / (2.0 * hw)) ** 2
        return out

    return np.array([one_side(u, c) + one_side(-u, c) for c in centers])


def _physical_shape(centers: np.ndarray, hw: float, coeffs: np.ndarray, u: np.ndarray) -> np.ndarray:
    return coeffs @ _raised_cosine_even(centers, hw, u)


def _fourier_shape(centers: np.ndarray, hw: float, coeffs: np.ndarray, t: np.ndarray) -> np.ndarray:
    return sum(coeff * _phihat(t, c, hw) for coeff, c in zip(coeffs, centers))


def _grid_correlation(a: np.ndarray, b: np.ndarray, grid: np.ndarray) -> float:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    inner = float(trap(a * b, x=grid))
    na = math.sqrt(max(0.0, float(trap(a * a, x=grid))))
    nb = math.sqrt(max(0.0, float(trap(b * b, x=grid))))
    if na == 0.0 or nb == 0.0:
        return float("nan")
    return abs(inner) / (na * nb)


def _physical_gram(config: "FlowConfig", ngrid: int = 6001) -> np.ndarray:
    umax = config.cmax + config.half_width
    u = np.linspace(-umax, umax, ngrid)
    basis = _raised_cosine_even(config.centers, config.half_width, u)
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    n = len(config.centers)
    gram = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            gram[i, j] = gram[j, i] = float(trap(basis[i] * basis[j], x=u))
    return gram


def _gram_orthonormalize(B: np.ndarray, gram: np.ndarray) -> np.ndarray:
    """Return columns spanning B, orthonormal for the given positive Gram form."""
    S = _sym(B.T @ gram @ B)
    w, V = np.linalg.eigh(S)
    tol = 1e-10 * max(1.0, float(np.max(np.abs(w))))
    keep = w > tol
    if not np.any(keep):
        return np.zeros((B.shape[0], 0))
    return B @ V[:, keep] @ np.diag(1.0 / np.sqrt(w[keep]))


def _dominant_repair(result: dict) -> dict | None:
    repairs = [row for row in result["rows"] if row["delta_min"] > 1e-3]
    if not repairs:
        return None
    return max(repairs, key=lambda row: row["delta_min"])


@dataclass(frozen=True)
class FlowConfig:
    ncenters: int = 13
    half_width: float = 0.14
    cmax: float = 0.80

    @property
    def centers(self) -> np.ndarray:
        return np.linspace(0.02, self.cmax, self.ncenters)


def coefficient_table(kind: str, max_n: int) -> list[float]:
    if kind == "zeta":
        return [float(x) for x in log_deriv_coeffs([1] * max_n, max_n)]
    if kind == "DH":
        return [float(x) for x in log_deriv_coeffs(dh_coeffs(max_n), max_n)]
    raise ValueError(f"unknown coefficient table: {kind!r}")


def flow_rows(config: FlowConfig, kind: str) -> dict:
    centers = config.centers
    gram = build_gram(centers, config.half_width)
    null = _proj_null(gram)
    winf = _sym(null.T @ gram["Winf"] @ null)

    gmax = float(gram["gmax"])
    max_n = max(2, int(math.floor(math.exp(gmax) - 1e-12)))
    coeffs = coefficient_table(kind, max_n)

    margin = winf.copy()
    margin_full = gram["Winf"].copy()
    rows = []
    for n in range(2, max_n + 1):
        coeff = coeffs[n - 1]
        if abs(coeff) < 1e-12:
            continue
        U = math.log(n)
        if U >= gmax:
            continue
        weight = 2.0 * coeff / math.sqrt(n)
        atom_full = _toeplitz_atom(centers, config.half_width, U, weight)
        atom = _sym(null.T @ atom_full @ null)
        before_min, before_vec = _min_eigenpair(margin)
        before_max = _eig_range(margin)[1]
        atom_min, atom_bad_vec = _min_eigenpair(atom)
        atom_max = _eig_range(atom)[1]
        rel = _restricted_relative_eigs(atom, margin)
        next_margin = _sym(margin - atom)
        next_margin_full = _sym(margin_full - atom_full)
        after_min, after_vec = _min_eigenpair(next_margin)
        after_max = _eig_range(next_margin)[1]
        ray_before = float(before_vec.T @ atom @ before_vec)
        ray_after = float(after_vec.T @ atom @ after_vec)
        rows.append({
            "n": n,
            "logn": U,
            "coeff": coeff,
            "before_min": before_min,
            "before_max": before_max,
            "atom_min": atom_min,
            "atom_max": atom_max,
            "rel_min": float(np.nanmin(rel)),
            "rel_max": float(np.nanmax(rel)),
            "after_min": after_min,
            "after_max": after_max,
            "delta_min": after_min - before_min,
            "ray_before": ray_before,
            "ray_after": ray_after,
            "align_before_after": float(abs(before_vec.T @ after_vec)),
            "align_before_atom_bad": float(abs(before_vec.T @ atom_bad_vec)),
            "_before_full": null @ before_vec,
            "_after_full": null @ after_vec,
            "_atom_bad_full": null @ atom_bad_vec,
            "_before_form_full": margin_full.copy(),
            "_after_form_full": next_margin_full.copy(),
        })
        margin = next_margin
        margin_full = next_margin_full

    return {
        "kind": kind,
        "config": config,
        "gmax": gmax,
        "dimension": int(winf.shape[0]),
        "winf_min": _eig_range(winf)[0],
        "winf_max": _eig_range(winf)[1],
        "rows": rows,
        "final_min": _eig_range(margin)[0],
        "final_max": _eig_range(margin)[1],
        "_final_full": null @ _min_eigenpair(margin)[1],
        "_final_form_full": margin_full.copy(),
    }


def _print_flow(result: dict) -> None:
    cfg = result["config"]
    print(f"\n[{result['kind']}] ncenters={cfg.ncenters} hw={cfg.half_width:.3f} "
          f"cmax={cfg.cmax:.3f} gmax={result['gmax']:.4f} dim={result['dimension']}")
    print(f"    W_inf eig range: [{result['winf_min']:+.3e}, {result['winf_max']:+.3e}]")
    print("    n   log n    c(n)       min before   atom eig range          rel range        min after")
    for r in result["rows"]:
        print(f"   {r['n']:2d}  {r['logn']:.4f}  {r['coeff']:+.4f}   "
              f"{r['before_min']:+.3e}   "
              f"[{r['atom_min']:+.2e},{r['atom_max']:+.2e}]   "
              f"[{r['rel_min']:+.3f},{r['rel_max']:+.3f}]   "
              f"{r['after_min']:+.3e}")
        if r["delta_min"] > 1e-3:
            print(f"       repair: delta_min={r['delta_min']:+.3e}, "
                  f"<v_before,Jv_before>={r['ray_before']:+.3e}, "
                  f"align(before,after)={r['align_before_after']:.3f}, "
                  f"align(before,atom_bad)={r['align_before_atom_bad']:.3f}")
    print(f"    final eig range: [{result['final_min']:+.3e}, {result['final_max']:+.3e}]")


def _repair_row(result: dict, target_n: int) -> dict | None:
    for row in result["rows"]:
        if row["n"] == target_n:
            return row
    return None


def repair_shape_coherence(configs: list[FlowConfig], target_n: int = 5) -> list[dict]:
    """Compare physical/Fourier shapes for the same repairing jump across refinements."""
    results = [flow_rows(cfg, "zeta") for cfg in configs]
    repair_rows = [_repair_row(result, target_n) for result in results]
    if any(row is None for row in repair_rows):
        return []

    umax = max(cfg.cmax + cfg.half_width for cfg in configs)
    u = np.linspace(-umax, umax, 4001)
    t = np.linspace(-80.0, 80.0, 12001)

    shapes = []
    for result, row in zip(results, repair_rows):
        cfg = result["config"]
        centers = cfg.centers
        shapes.append({
            "result": result,
            "row": row,
            "bad_u": _physical_shape(centers, cfg.half_width, row["_before_full"], u),
            "bad_t": _fourier_shape(centers, cfg.half_width, row["_before_full"], t),
            "atom_u": _physical_shape(centers, cfg.half_width, row["_atom_bad_full"], u),
            "atom_t": _fourier_shape(centers, cfg.half_width, row["_atom_bad_full"], t),
            "final_u": _physical_shape(centers, cfg.half_width, result["_final_full"], u),
            "final_t": _fourier_shape(centers, cfg.half_width, result["_final_full"], t),
        })

    rows = []
    for i in range(len(shapes) - 1):
        left = shapes[i]
        right = shapes[i + 1]
        lc = left["result"]["config"]
        rc = right["result"]["config"]
        rows.append({
            "left": f"n{lc.ncenters}/hw{lc.half_width:.2f}",
            "right": f"n{rc.ncenters}/hw{rc.half_width:.2f}",
            "left_final_min": left["result"]["final_min"],
            "right_final_min": right["result"]["final_min"],
            "bad_phys_corr": _grid_correlation(left["bad_u"], right["bad_u"], u),
            "bad_fourier_corr": _grid_correlation(left["bad_t"], right["bad_t"], t),
            "atom_phys_corr": _grid_correlation(left["atom_u"], right["atom_u"], u),
            "atom_fourier_corr": _grid_correlation(left["atom_t"], right["atom_t"], t),
            "final_phys_corr": _grid_correlation(left["final_u"], right["final_u"], u),
            "final_fourier_corr": _grid_correlation(left["final_t"], right["final_t"], t),
            "left_delta": left["row"]["delta_min"],
            "right_delta": right["row"]["delta_min"],
        })
    return rows


def _print_coherence(rows: list[dict], target_n: int) -> None:
    print(f"\n[coherence] fixed-edge zeta repair at n={target_n}")
    if not rows:
        print("    target repair not present in all refinement windows")
        return
    print("    compare adjacent refinements by absolute L2 correlation of reconstructed shapes")
    print("      pair             final mins           bad vec      atom neg     final vec")
    for row in rows:
        print(f"      {row['left']} -> {row['right']}  "
              f"{row['left_final_min']:+.2e}/{row['right_final_min']:+.2e}   "
              f"phys {row['bad_phys_corr']:.3f}, FT {row['bad_fourier_corr']:.3f}   "
              f"phys {row['atom_phys_corr']:.3f}, FT {row['atom_fourier_corr']:.3f}   "
              f"phys {row['final_phys_corr']:.3f}, FT {row['final_fourier_corr']:.3f}")
    print("    high atom/final correlations would support a stable boundary mode;")
    print("    low bad-vector correlations mean the pre-repair obstruction is still basis-sensitive.")


def support_edge_tracking(configs: list[FlowConfig]) -> list[dict]:
    """Track the near-null mode and dominant repair as the support edge grows."""
    return support_edge_tracking_from_results([flow_rows(cfg, "zeta") for cfg in configs])


def support_edge_tracking_from_results(results: list[dict]) -> list[dict]:
    """Track the near-null mode and dominant repair as the support edge grows."""
    umax = max(result["config"].cmax + result["config"].half_width for result in results)
    u = np.linspace(-umax, umax, 5001)
    t = np.linspace(-80.0, 80.0, 12001)

    shapes = []
    for result in results:
        cfg = result["config"]
        centers = cfg.centers
        repairs = [row for row in result["rows"] if row["delta_min"] > 1e-3]
        dominant = max(repairs, key=lambda row: row["delta_min"]) if repairs else result["rows"][-1]
        shapes.append({
            "result": result,
            "dominant": dominant,
            "final_u": _physical_shape(centers, cfg.half_width, result["_final_full"], u),
            "final_t": _fourier_shape(centers, cfg.half_width, result["_final_full"], t),
            "bad_u": _physical_shape(centers, cfg.half_width, dominant["_before_full"], u),
            "bad_t": _fourier_shape(centers, cfg.half_width, dominant["_before_full"], t),
            "atom_u": _physical_shape(centers, cfg.half_width, dominant["_atom_bad_full"], u),
            "atom_t": _fourier_shape(centers, cfg.half_width, dominant["_atom_bad_full"], t),
        })

    rows = []
    for i in range(len(shapes) - 1):
        left = shapes[i]
        right = shapes[i + 1]
        lr = left["result"]
        rr = right["result"]
        ld = left["dominant"]
        rd = right["dominant"]
        rows.append({
            "left_gmax": lr["gmax"],
            "right_gmax": rr["gmax"],
            "left_final_min": lr["final_min"],
            "right_final_min": rr["final_min"],
            "left_repair_n": ld["n"],
            "right_repair_n": rd["n"],
            "left_repair_delta": ld["delta_min"],
            "right_repair_delta": rd["delta_min"],
            "final_phys_corr": _grid_correlation(left["final_u"], right["final_u"], u),
            "final_fourier_corr": _grid_correlation(left["final_t"], right["final_t"], t),
            "repair_bad_phys_corr": _grid_correlation(left["bad_u"], right["bad_u"], u),
            "repair_bad_fourier_corr": _grid_correlation(left["bad_t"], right["bad_t"], t),
            "repair_atom_phys_corr": _grid_correlation(left["atom_u"], right["atom_u"], u),
            "repair_atom_fourier_corr": _grid_correlation(left["atom_t"], right["atom_t"], t),
        })
    return rows


def _print_support_tracking(rows: list[dict]) -> None:
    print("\n[edge tracking] zeta near-null mode as support grows")
    print("    fixed ncenters=17, hw=0.10; dominant repair is the largest positive delta_min")
    print("      gmax pair     final corr      dominant repair       bad corr      atom corr")
    for row in rows:
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}   "
              f"phys {row['final_phys_corr']:.3f}, FT {row['final_fourier_corr']:.3f}   "
              f"n{row['left_repair_n']}->{row['right_repair_n']}   "
              f"phys {row['repair_bad_phys_corr']:.3f}, FT {row['repair_bad_fourier_corr']:.3f}   "
              f"phys {row['repair_atom_phys_corr']:.3f}, FT {row['repair_atom_fourier_corr']:.3f}")
    print("    reading: high correlations within a repair stage, low correlations at n3->n5->n7")
    print("    handoffs suggest a relay of obstruction modes, not one fixed global vector.")


def relay_comparison(configs: list[FlowConfig]) -> list[dict]:
    return relay_comparison_from_results(
        [flow_rows(cfg, "zeta") for cfg in configs],
        [flow_rows(cfg, "DH") for cfg in configs],
    )

def relay_comparison_from_results(zeta_results: list[dict], dh_results: list[dict]) -> list[dict]:
    rows = []
    for zeta, dh in zip(zeta_results, dh_results):
        zr = _dominant_repair(zeta)
        dr = _dominant_repair(dh)
        rows.append({
            "gmax": zeta["gmax"],
            "zeta_final": zeta["final_min"],
            "dh_final": dh["final_min"],
            "zeta_repair_n": zr["n"] if zr else None,
            "zeta_repair_delta": zr["delta_min"] if zr else 0.0,
            "zeta_repair_align": zr["align_before_atom_bad"] if zr else 0.0,
            "dh_repair_n": dr["n"] if dr else None,
            "dh_repair_delta": dr["delta_min"] if dr else 0.0,
            "dh_repair_align": dr["align_before_atom_bad"] if dr else 0.0,
        })
    return rows


def _print_relay_comparison(rows: list[dict]) -> None:
    print("\n[relay comparison] zeta vs DH over the same growing windows")
    print("      gmax      zeta final / dominant repair        DH final / dominant repair")
    for row in rows:
        zr = "none" if row["zeta_repair_n"] is None else (
            f"n{row['zeta_repair_n']} d={row['zeta_repair_delta']:+.2e} "
            f"a={row['zeta_repair_align']:.2f}")
        dr = "none" if row["dh_repair_n"] is None else (
            f"n{row['dh_repair_n']} d={row['dh_repair_delta']:+.2e} "
            f"a={row['dh_repair_align']:.2f}")
        print(f"      {row['gmax']:.2f}   {row['zeta_final']:+.2e} / {zr:<20}   "
              f"{row['dh_final']:+.2e} / {dr}")
    print("    zeta repairs hand off along the Euler support; DH's wrong coefficients lose PSD")
    print("    and its later repairs do not restore the margin.")


def _orthonormalize_shape_columns(shapes: np.ndarray, grid: np.ndarray) -> np.ndarray:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    cols = []
    for j in range(shapes.shape[1]):
        v = shapes[:, j].copy()
        for q in cols:
            v -= q * float(trap(q * v, x=grid))
        norm = math.sqrt(max(0.0, float(trap(v * v, x=grid))))
        if norm > 1e-10:
            cols.append(v / norm)
    if not cols:
        return np.zeros((len(grid), 0))
    return np.column_stack(cols)


def handoff_transfer_matrices(results: list[dict]) -> list[dict]:
    """2x2 L2 handoff matrices between zeta active channels [bad, atom-negative]."""
    umax = max(result["config"].cmax + result["config"].half_width for result in results)
    u = np.linspace(-umax, umax, 6001)
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz

    channels = []
    for result in results:
        repair = _dominant_repair(result)
        if repair is None:
            channels.append(None)
            continue
        cfg = result["config"]
        shapes = np.column_stack([
            _physical_shape(cfg.centers, cfg.half_width, repair["_before_full"], u),
            _physical_shape(cfg.centers, cfg.half_width, repair["_atom_bad_full"], u),
        ])
        channels.append({
            "result": result,
            "repair": repair,
            "Q": _orthonormalize_shape_columns(shapes, u),
        })

    rows = []
    for i in range(len(channels) - 1):
        left = channels[i]
        right = channels[i + 1]
        if left is None or right is None:
            continue
        Ql, Qr = left["Q"], right["Q"]
        if Ql.shape[1] == 0 or Qr.shape[1] == 0:
            continue
        matrix = np.array([[float(trap(Qr[:, a] * Ql[:, b], x=u))
                            for b in range(Ql.shape[1])]
                           for a in range(Qr.shape[1])])
        svals = np.linalg.svd(matrix, compute_uv=False)
        rows.append({
            "left_gmax": left["result"]["gmax"],
            "right_gmax": right["result"]["gmax"],
            "left_n": left["repair"]["n"],
            "right_n": right["repair"]["n"],
            "handoff": left["repair"]["n"] != right["repair"]["n"],
            "matrix": matrix,
            "svals": svals,
        })
    return rows


def _print_handoff_transfer(rows: list[dict]) -> None:
    print("\n[handoff transfer] zeta active-channel matrices")
    print("    channels are L2-orthonormal [incoming bad, jump-negative] pairs")
    for row in rows:
        if not row["handoff"]:
            continue
        M = row["matrix"]
        s = row["svals"]
        print(f"      gmax {row['left_gmax']:.2f}->{row['right_gmax']:.2f} "
              f"n{row['left_n']}->n{row['right_n']}")
        print(f"        matrix [[{M[0, 0]:+.3f}, {M[0, 1]:+.3f}], "
              f"[{M[1, 0]:+.3f}, {M[1, 1]:+.3f}]]")
        print(f"        singular values [{s[0]:.3f}, {s[1]:.3f}]")
    print("    these are finite handoff couplings, not proofs; singular values below one")
    print("    mean the projected channel-to-channel transmission is L2-contractive.")


def _minimum_background_for_psd(defect: np.ndarray, background: np.ndarray) -> float:
    """Smallest lambda >= 0 found by bisection so defect + lambda background is PSD."""

    def min_eig(lam: float) -> float:
        return float(np.linalg.eigvalsh(_sym(defect + lam * background))[0])

    if min_eig(0.0) >= -1e-10:
        return 0.0

    hi = 1.0
    while min_eig(hi) < -1e-10 and hi < 1e8:
        hi *= 2.0
    if hi >= 1e8 and min_eig(hi) < -1e-10:
        return float("inf")

    lo = 0.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if min_eig(mid) >= -1e-10:
            hi = mid
        else:
            lo = mid
    return hi


def _logdet_spd(M: np.ndarray, tol: float = 1e-12) -> float:
    ev = np.linalg.eigvalsh(_sym(M))
    if ev[0] <= tol:
        return float("nan")
    return float(np.sum(np.log(ev)))


def _metric_transgression(J_left: np.ndarray, J_right: np.ndarray, T: np.ndarray,
                          lam: float) -> dict:
    """Log-det transgression for the metric-pair connection.

    G_L = J_L + lam I, G_R = J_R + lam I.

    tau = log det(G_L) - log det(T^* G_R T)

    Positive tau means the handoff loses metric volume in this finite channel.
    This is the CS/Bott-Chern-like anomaly diagnostic; the Loewner defect is
    tracked separately because determinant positivity alone is too weak.
    """
    if not np.isfinite(lam):
        return {
            "tau": float("nan"),
            "metric_delta": float("nan"),
            "connection_volume": float("nan"),
            "defect_min": float("nan"),
        }
    I_left = np.eye(J_left.shape[0])
    I_right = np.eye(J_right.shape[0])
    G_left = _sym(J_left + lam * I_left)
    G_right = _sym(J_right + lam * I_right)
    pulled = _sym(T.T @ G_right @ T)
    logdet_left = _logdet_spd(G_left)
    logdet_right = _logdet_spd(G_right)
    logdet_pulled = _logdet_spd(pulled)
    sign, logabsdet = np.linalg.slogdet(T)
    connection_volume = float("nan") if sign == 0 else float(-2.0 * logabsdet)
    tau = float("nan") if np.isnan(logdet_left) or np.isnan(logdet_pulled) else (
        logdet_left - logdet_pulled
    )
    metric_delta = float("nan") if np.isnan(logdet_left) or np.isnan(logdet_right) else (
        logdet_left - logdet_right
    )
    defect_min = float(np.linalg.eigvalsh(_sym(G_left - pulled))[0])
    return {
        "tau": tau,
        "metric_delta": metric_delta,
        "connection_volume": connection_volume,
        "defect_min": defect_min,
    }


def j_metric_fit(results: list[dict]) -> list[dict]:
    """Discrete bundle metric test.

    Fiber: the two-dimensional active channel [incoming bad, jump-negative].
    Metric tensor J_L: post-jump local energy form compressed to the fiber.
    Connection T: L2 projection of the next active fiber onto the current one.

    We test whether the connection is contractive for J, and if not, how much
    ambient L2 capacity must be added:

        J_L + lambda I - T^T (J_R + lambda I) T >= 0.
    """
    umax = max(result["config"].cmax + result["config"].half_width for result in results)
    u = np.linspace(-umax, umax, 6001)
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz

    fibers = []
    for result in results:
        repair = _dominant_repair(result)
        if repair is None:
            fibers.append(None)
            continue
        cfg = result["config"]
        coeff_basis = np.column_stack([
            repair["_before_full"],
            repair["_atom_bad_full"],
        ])
        Q = _gram_orthonormalize(coeff_basis, _physical_gram(cfg))
        shapes = np.column_stack([
            _physical_shape(cfg.centers, cfg.half_width, Q[:, j], u)
            for j in range(Q.shape[1])
        ])
        metric = _sym(Q.T @ repair["_after_form_full"] @ Q)
        fibers.append({
            "result": result,
            "repair": repair,
            "Q": Q,
            "shapes": shapes,
            "metric": metric,
        })

    rows = []
    for i in range(len(fibers) - 1):
        left = fibers[i]
        right = fibers[i + 1]
        if left is None or right is None:
            continue
        T = np.array([[float(trap(right["shapes"][:, a] * left["shapes"][:, b], x=u))
                       for b in range(left["shapes"].shape[1])]
                      for a in range(right["shapes"].shape[1])])
        J_left = left["metric"]
        J_right = right["metric"]
        raw_defect = _sym(J_left - T.T @ J_right @ T)
        l2_capacity = _sym(np.eye(T.shape[1]) - T.T @ T)
        lam = _minimum_background_for_psd(raw_defect, l2_capacity)
        raw_transgression = _metric_transgression(J_left, J_right, T, 0.0)
        fitted_transgression = _metric_transgression(J_left, J_right, T, lam)
        rows.append({
            "left_gmax": left["result"]["gmax"],
            "right_gmax": right["result"]["gmax"],
            "kind": left["result"]["kind"],
            "left_n": left["repair"]["n"],
            "right_n": right["repair"]["n"],
            "handoff": left["repair"]["n"] != right["repair"]["n"],
            "metric_left_eigs": np.linalg.eigvalsh(J_left),
            "metric_right_eigs": np.linalg.eigvalsh(J_right),
            "raw_defect_eigs": np.linalg.eigvalsh(raw_defect),
            "l2_capacity_eigs": np.linalg.eigvalsh(l2_capacity),
            "min_l2_background": lam,
            "raw_transgression": raw_transgression,
            "fitted_transgression": fitted_transgression,
        })
    return rows


def _print_j_metric_fit(rows: list[dict], label: str = "zeta") -> None:
    print(f"\n[J-fit] {label} active-channel metric tensor and connection defect")
    print("    J_L is post-jump local energy on the active fiber; T is the L2 connection")
    print("      edge        repair   raw defect eigs        min L2 background")
    for row in rows:
        tag = "*" if row["handoff"] else " "
        ev = row["raw_defect_eigs"]
        print(f"    {tag} {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"n{row['left_n']}->n{row['right_n']}   "
              f"[{ev[0]:+.2e},{ev[-1]:+.2e}]      "
              f"{row['min_l2_background']:.3g}")
    print("    * marks repair handoffs. Pure local energy is close but not invariant;")
    print("    adding modest ambient L2 capacity gives the candidate metric tensor.")


def _print_transgression(rows: list[dict], label: str = "zeta") -> None:
    print(f"\n[transgression] {label} log-det metric anomaly")
    print("    tau_lambda = log det(G_L) - log det(T^* G_R T), G=J+lambda h")
    print("      edge        repair    lambda   tau_lambda   metric_delta   conn_volume   defect_min")
    if not rows:
        print("      no adjacent active fibers")
        return
    for row in rows:
        tr = row["fitted_transgression"]
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"n{row['left_n']}->n{row['right_n']}   "
              f"{row['min_l2_background']:.3g}   "
              f"{tr['tau']:+.3f}       "
              f"{tr['metric_delta']:+.3f}        "
              f"{tr['connection_volume']:+.3f}      "
              f"{tr['defect_min']:+.2e}")
    print("    tau splits into metric volume change plus connection-volume loss;")
    print("    it is a navigation functional, not by itself a positivity theorem.")


def active_channel_passivity(results: list[dict]) -> list[dict]:
    """Eigenvalues of the final Weil form on each local active channel."""
    rows = []
    for result in results:
        cfg = result["config"]
        repair = _dominant_repair(result)
        if repair is None:
            label = "none"
            B = np.column_stack([result["_final_full"]])
            delta = 0.0
            align = 0.0
        else:
            label = f"n{repair['n']}"
            B = np.column_stack([
                repair["_before_full"],
                repair["_atom_bad_full"],
                repair["_after_full"],
                result["_final_full"],
            ])
            delta = repair["delta_min"]
            align = repair["align_before_atom_bad"]
        Q = _gram_orthonormalize(B, _physical_gram(cfg))
        block = _sym(Q.T @ result["_final_form_full"] @ Q)
        ev = np.linalg.eigvalsh(block) if block.size else np.array([float("nan")])
        rows.append({
            "kind": result["kind"],
            "gmax": result["gmax"],
            "final_min": result["final_min"],
            "channel": label,
            "channel_dim": int(Q.shape[1]),
            "repair_delta": delta,
            "repair_align": align,
            "block_min": float(ev[0]),
            "block_max": float(ev[-1]),
            "indefinite": bool(ev[0] < -1e-9),
        })
    return rows


def _print_active_passivity(zeta_rows: list[dict], dh_rows: list[dict]) -> None:
    print("\n[active-channel passivity] final form on local relay channels")
    print("      gmax      zeta channel eig range           DH channel eig range")
    for z, d in zip(zeta_rows, dh_rows):
        print(f"      {z['gmax']:.2f}   {z['channel']:<4} "
              f"[{z['block_min']:+.2e},{z['block_max']:+.2e}]   "
              f"{d['channel']:<4} [{d['block_min']:+.2e},{d['block_max']:+.2e}]")
    print("    zeta's active channel remains positive in this sweep; DH becomes indefinite")
    print("    once the relay test reaches the first failing windows.")


def summary() -> dict:
    print("=" * 78)
    print("Prime-Toeplitz / passive-scattering flow diagnostic")
    print("=" * 78)
    print("Pole-killed Sonin window.  Atoms are translation/correlation kernels,")
    print("not positive point-evaluation masses; signs below are therefore meaningful.")

    configs = [
        FlowConfig(ncenters=13, half_width=0.14, cmax=0.80),
        FlowConfig(ncenters=17, half_width=0.10, cmax=0.95),
    ]
    out = {}
    for cfg in configs:
        key = f"n{cfg.ncenters}_hw{cfg.half_width}_c{cfg.cmax}"
        out[key] = {}
        for kind in ("zeta", "DH"):
            result = flow_rows(cfg, kind)
            _print_flow(result)
            out[key][kind] = result

    coherence_configs = [
        FlowConfig(ncenters=13, half_width=0.14, cmax=0.80),
        FlowConfig(ncenters=17, half_width=0.10, cmax=0.84),
        FlowConfig(ncenters=21, half_width=0.08, cmax=0.86),
    ]
    coherence = repair_shape_coherence(coherence_configs, target_n=5)
    _print_coherence(coherence, target_n=5)
    out["coherence_n5"] = coherence

    edge_configs = [FlowConfig(ncenters=17, half_width=0.10, cmax=cmax)
                    for cmax in (0.70, 0.76, 0.84, 0.95, 1.05, 1.16)]
    edge_zeta = [flow_rows(cfg, "zeta") for cfg in edge_configs]
    edge_dh = [flow_rows(cfg, "DH") for cfg in edge_configs]

    edge_rows = support_edge_tracking_from_results(edge_zeta)
    _print_support_tracking(edge_rows)
    out["support_edge_tracking"] = edge_rows

    relay_rows = relay_comparison_from_results(edge_zeta, edge_dh)
    _print_relay_comparison(relay_rows)
    out["relay_comparison"] = relay_rows

    transfer_rows = handoff_transfer_matrices(edge_zeta)
    _print_handoff_transfer(transfer_rows)
    out["handoff_transfer"] = transfer_rows

    j_fit_rows = j_metric_fit(edge_zeta)
    _print_j_metric_fit(j_fit_rows)
    _print_transgression(j_fit_rows)
    out["j_metric_fit"] = j_fit_rows

    dh_j_fit_rows = j_metric_fit(edge_dh)
    _print_transgression(dh_j_fit_rows, "DH active")
    out["dh_j_metric_fit"] = dh_j_fit_rows

    zeta_passivity = active_channel_passivity(edge_zeta)
    dh_passivity = active_channel_passivity(edge_dh)
    _print_active_passivity(zeta_passivity, dh_passivity)
    out["active_channel_passivity"] = {
        "zeta": zeta_passivity,
        "DH": dh_passivity,
    }

    print("\nInterpretation:")
    print("  * The naive rank-one Carleson picture is false in this convention.")
    print("  * Zeta survives by a critical sequence of indefinite Toeplitz jumps; later")
    print("    prime powers can repair damage from earlier ones.")
    print("  * DH has the same archimedean side, but its log-derivative coefficients send")
    print("    the wrong jumps, and the margin goes negative in these windows.")
    return out


if __name__ == "__main__":
    summary()
