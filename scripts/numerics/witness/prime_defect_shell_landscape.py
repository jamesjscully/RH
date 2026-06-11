"""Shell-direction landscape for the active edge repair.

The edge-cone witness studies the active negative Schur eigenvector.  This
script asks whether its edge-layer geometry is forced by the surrounding Schur
debt landscape.

On the late edge the shell is two-dimensional.  For each unit shell direction
``y`` we form

    x = A^{-1} C y,
    f = [x, -y],

then compute the edge-convolution beta and the exact Riccati update on that
same direction.  This separates three questions:

  * which shell directions are Schur-negative before the repair cell?
  * do all negative directions have enough beta to be repaired directionally?
  * is terminal anti-concentration correlated with Schur negativity?

Run:
    python3 -m scripts.numerics.witness.prime_defect_shell_landscape
    python3 -m scripts.numerics.witness.prime_defect_shell_landscape --refinements
"""
from __future__ import annotations

import argparse
import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_active_atom_shift import (
    REFINEMENTS,
    _compressed_atom_block,
    active_state,
)
from .prime_defect_edge_cone import _profile_from_coeffs, _required_beta
from .prime_defect_riccati_storage import _blocks


def _schur_landscape_mats(state: dict) -> dict:
    old_dim = state["old_dim"]
    A, C, D = _blocks(state["current"], old_dim)
    X = np.linalg.solve(A, C)
    S = _sym(D - C.T @ X)

    atom = _compressed_atom_block(state, state["logn"], state["atom_weight"])
    cell = _sym(state["smooth_block"] - atom)
    EA, EC, ED = _blocks(cell, old_dim)
    A_plus = _sym(A + EA)
    residual = EC - EA @ X
    Q = _sym(ED - X.T @ EC - EC.T @ X + X.T @ EA @ X)
    square = _sym(residual.T @ np.linalg.solve(A_plus, residual))
    G = _sym(Q - square)
    return {
        "A": A,
        "C": C,
        "D": D,
        "X": X,
        "S": S,
        "Q": Q,
        "square": square,
        "G": G,
        "S_after": _sym(S + G),
    }


def _row_for_y(state: dict, mats: dict, y: np.ndarray, ngrid: int,
               theta: float | None = None, label: str = "") -> dict:
    y = np.asarray(y, dtype=float)
    norm = float(np.linalg.norm(y))
    if norm <= 1e-14:
        raise ValueError("zero shell direction")
    y = y / norm
    f = np.concatenate([mats["X"] @ y, -y])
    coeffs = state["B"] @ f
    profile = _profile_from_coeffs(state, coeffs, ngrid=ngrid)
    before = float(y.T @ mats["S"] @ y)
    Q = float(y.T @ mats["Q"] @ y)
    square = float(y.T @ mats["square"] @ y)
    G = float(y.T @ mats["G"] @ y)
    after = before + G
    smooth_mass = 4.0 * (
        math.exp(0.5 * state["cell"][1]) - math.exp(0.5 * state["cell"][0])
    )
    k_atom = profile["K_atom"]
    beta_applicable = k_atom > 1e-12
    if beta_applicable:
        dir_required_beta = (
            state["atom_weight"] / smooth_mass
            + max(0.0, -before) / (smooth_mass * k_atom)
            + square / (smooth_mass * k_atom)
        )
        beta_surplus = profile["beta"] - dir_required_beta
    else:
        dir_required_beta = float("nan")
        beta_surplus = float("nan")
    return {
        "theta": float(theta) if theta is not None else float("nan"),
        "label": label,
        "y": y,
        "y0": float(y[0]) if len(y) > 0 else float("nan"),
        "y1": float(y[1]) if len(y) > 1 else float("nan"),
        "before": before,
        "Q": Q,
        "square": square,
        "G": G,
        "after": after,
        "beta": profile["beta"],
        "beta_applicable": beta_applicable,
        "required_beta": dir_required_beta,
        "beta_surplus": beta_surplus,
        "centroid_u": profile["centroid_u_rel"],
        "mass_left": profile["K_mass_beyond_atom"],
        "q_l2_beyond": profile["q_l2_beyond_atom"],
        "q_sign_changes": profile["q_sign_changes"],
        "K_atom": k_atom,
    }


def shell_landscape_report(ncenters: int = 25, half_width: float = 0.06,
                           samples: int = 721, ngrid: int = 1025) -> dict:
    state = active_state(ncenters, half_width)
    mats = _schur_landscape_mats(state)
    eigs, vecs = np.linalg.eigh(mats["S"])
    active = vecs[:, 0]
    dim = mats["S"].shape[0]
    if dim == 2:
        active_theta = math.atan2(float(active[1]), float(active[0]))
        if active_theta < 0.0:
            active_theta += math.pi
        thetas = np.linspace(0.0, math.pi, samples, endpoint=False)
        rows = [
            _row_for_y(
                state,
                mats,
                np.array([math.cos(float(theta)), math.sin(float(theta))]),
                ngrid,
                theta=float(theta),
            )
            for theta in thetas
        ]
        active_row = min(
            rows,
            key=lambda row: abs(((row["theta"] - active_theta + 0.5 * math.pi) % math.pi) - 0.5 * math.pi),
        )
    else:
        rng = np.random.default_rng(20260609 + 1000 * ncenters + int(round(1000.0 * half_width)))
        dirs = []
        labels = []
        for idx in range(dim):
            dirs.append(vecs[:, idx])
            labels.append(f"eig{idx}")
        random_dirs = rng.normal(size=(samples, dim))
        random_dirs /= np.linalg.norm(random_dirs, axis=1)[:, None]
        dirs.extend(random_dirs)
        labels.extend(["random"] * len(random_dirs))
        rows = [
            _row_for_y(state, mats, y, ngrid, label=label)
            for y, label in zip(dirs, labels)
        ]
        active_theta = float("nan")
        active_row = rows[0]
    negative = [row for row in rows if row["before"] < -1e-9]
    negative_applicable = [row for row in negative if row["beta_applicable"]]
    negative_atom_helpful = [row for row in negative if not row["beta_applicable"]]
    repaired = [row for row in negative if row["after"] >= -1e-9]
    failed = [row for row in negative if row["after"] < -1e-9]
    min_beta_negative = min((row["beta"] for row in negative_applicable), default=float("nan"))
    min_surplus_negative = min((row["beta_surplus"] for row in negative_applicable), default=float("nan"))
    min_after_negative = min((row["after"] for row in negative), default=float("nan"))
    worst_after = min(rows, key=lambda row: row["after"])
    most_negative = min(rows, key=lambda row: row["before"])
    lowest_beta_negative = (
        min(negative_applicable, key=lambda row: row["beta"])
        if negative_applicable else None
    )
    before_vals = np.array([row["before"] for row in rows])
    beta_vals = np.array([row["beta"] for row in rows])
    mass_vals = np.array([row["mass_left"] for row in rows])
    finite = np.isfinite(beta_vals)
    neg_finite = np.array([
        row["before"] < -1e-9 and row["beta_applicable"] and np.isfinite(row["beta"])
        for row in rows
    ])
    corr_before_beta = (
        float(np.corrcoef(before_vals[finite], beta_vals[finite])[0, 1])
        if np.count_nonzero(finite) > 2 else float("nan")
    )
    corr_before_beta_negative = (
        float(np.corrcoef(before_vals[neg_finite], beta_vals[neg_finite])[0, 1])
        if np.count_nonzero(neg_finite) > 2 else float("nan")
    )
    corr_beta_mass = (
        float(np.corrcoef(beta_vals[finite], mass_vals[finite])[0, 1])
        if np.count_nonzero(finite) > 2 else float("nan")
    )
    global_required = _required_beta(state)
    return {
        "state": state,
        "mats": mats,
        "rows": rows,
        "eigs": eigs,
        "active_theta": active_theta,
        "active_row": active_row,
        "most_negative": most_negative,
        "worst_after": worst_after,
        "lowest_beta_negative": lowest_beta_negative,
        "negative_count": len(negative),
        "negative_applicable_count": len(negative_applicable),
        "negative_atom_helpful_count": len(negative_atom_helpful),
        "repaired_count": len(repaired),
        "failed_count": len(failed),
        "samples": len(rows),
        "min_beta_negative": min_beta_negative,
        "min_surplus_negative": min_surplus_negative,
        "min_after_negative": min_after_negative,
        "corr_before_beta": corr_before_beta,
        "corr_before_beta_negative": corr_before_beta_negative,
        "corr_beta_mass": corr_beta_mass,
        "global_required": global_required,
    }


def _fmt_dir(row: dict) -> str:
    beta_text = (
        f"{row['beta']:.3f}/{row['required_beta']:.3f}"
        if row["beta_applicable"] else f"inapplicable(Katom={row['K_atom']:+.2e})"
    )
    if np.isfinite(row["theta"]):
        where = f"theta={row['theta']:.3f}"
    else:
        where = f"{row['label'] or 'dir'}"
    y_preview = ",".join(f"{val:+.3f}" for val in row["y"][:4])
    if len(row["y"]) > 4:
        y_preview += ",..."
    return (
        f"{where} y=({y_preview}) "
        f"S={row['before']:+.3e} G={row['G']:+.3e} after={row['after']:+.3e} "
        f"beta={beta_text} "
        f"massLeft={row['mass_left']:.3f}"
    )


def _print_report(report: dict) -> None:
    state = report["state"]
    print("=" * 78)
    print("Shell-direction landscape for active edge repair")
    print("=" * 78)
    print(f"basis n={state['ncenters']} hw={state['half_width']:.3f}, "
          f"shell dim={report['mats']['S'].shape[0]}, "
          f"cell {state['repair_n']}=[{state['cell'][0]:.6f},{state['cell'][1]:.6f}]")
    print(f"Schur eigs before repair: "
          f"{', '.join(f'{x:+.6e}' for x in report['eigs'])}")
    print(f"negative directions: {report['negative_count']}/{report['samples']}, "
          f"positive-atom beta sector: {report['negative_applicable_count']}, "
          f"atom-helpful sector: {report['negative_atom_helpful_count']}, "
          f"directionally repaired: {report['repaired_count']}, "
          f"failed: {report['failed_count']}")
    print(f"min beta on negative sector={report['min_beta_negative']:.3f}, "
          f"min beta surplus={report['min_surplus_negative']:+.3f}, "
          f"min after on negative sector={report['min_after_negative']:+.3e}")
    print(f"corr(S,beta)={report['corr_before_beta']:+.3f}, "
          f"corr(S,beta | neg)={report['corr_before_beta_negative']:+.3f}, "
          f"corr(beta,massLeft)={report['corr_beta_mass']:+.3f}, "
          f"active global required beta={report['global_required']:.3f}")
    print("\n      active eigendirection:")
    print(f"        {_fmt_dir(report['active_row'])}")
    print("      most negative direction:")
    print(f"        {_fmt_dir(report['most_negative'])}")
    print("      worst after-repair direction:")
    print(f"        {_fmt_dir(report['worst_after'])}")
    if report["lowest_beta_negative"] is not None:
        print("      lowest applicable beta in negative sector:")
        print(f"        {_fmt_dir(report['lowest_beta_negative'])}")


def refinement_table() -> list[dict]:
    rows = []
    print("\n[shell landscape refinement table]")
    print("      basis       neg/samp betaSec atomHelp repaired failed minBeta minSurp minAfter")
    for ncenters, half_width in REFINEMENTS:
        report = shell_landscape_report(ncenters, half_width, samples=361, ngrid=769)
        row = {
            "ncenters": ncenters,
            "half_width": half_width,
            "negative": report["negative_count"],
            "negative_applicable": report["negative_applicable_count"],
            "negative_atom_helpful": report["negative_atom_helpful_count"],
            "samples": report["samples"],
            "repaired": report["repaired_count"],
            "failed": report["failed_count"],
            "min_beta_negative": report["min_beta_negative"],
            "min_surplus_negative": report["min_surplus_negative"],
            "min_after_negative": report["min_after_negative"],
            "corr_before_beta": report["corr_before_beta"],
        }
        rows.append(row)
        print(f"      n{ncenters:<2d}/h{half_width:.3f} "
              f"{row['negative']:>3d}/{row['samples']:<3d} "
              f"{row['negative_applicable']:>3d}     "
              f"{row['negative_atom_helpful']:>3d}      "
              f"{row['repaired']:>3d}      "
              f"{row['failed']:>3d}    "
              f"{row['min_beta_negative']:.3f}      "
              f"{row['min_surplus_negative']:+.3f}   "
              f"{row['min_after_negative']:+.3e}")
    return rows


def summary(with_refinements: bool = False) -> dict:
    report = shell_landscape_report()
    _print_report(report)
    if with_refinements:
        report["refinements"] = refinement_table()
    print("\nInterpretation:")
    print("  * The repair inequality should be imposed on the Schur-negative sector,")
    print("    not on arbitrary shell directions.")
    print("  * If low-beta directions are Schur-positive, terminal concentration is")
    print("    controlled by the active-state eigengeometry rather than by a broad")
    print("    positivity cone.")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinements", action="store_true")
    args = parser.parse_args()
    summary(with_refinements=args.refinements)
