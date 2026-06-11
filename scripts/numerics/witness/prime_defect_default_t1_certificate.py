"""Default finite T1 certificate for the active-23 repair.

The earlier geometric/KKT diagnostics explain why Schur-negative shell
directions have edge-convolution surplus.  For the default two-dimensional
late shell there is a simpler finite endpoint:

    H = S + G > 0.

Here ``S`` is the Schur complement before the exact 23-cell residual and
``G = Q - square`` is the exact Riccati Schur increment for that cell.  If
``H`` is positive definite, every nonzero shell direction is repaired, hence
in particular every direction with ``y.T S y < 0`` is repaired.

Run:
    python3 -m scripts.numerics.witness.prime_defect_default_t1_certificate
    python3 -m scripts.numerics.witness.prime_defect_default_t1_certificate --refinements
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
from .prime_defect_riccati_storage import _blocks


def t1_matrices(ncenters: int = 25, half_width: float = 0.06,
                physical_ngrid: int = 6001) -> dict:
    state = active_state(ncenters, half_width, physical_ngrid=physical_ngrid)
    old_dim = state["old_dim"]
    A, C, D = _blocks(state["current"], old_dim)
    X = np.linalg.solve(A, C)
    S = _sym(D - C.T @ X)

    atom_unit = _compressed_atom_block(state, state["logn"], 1.0)
    atom = _sym(state["atom_weight"] * atom_unit)
    cell = _sym(state["smooth_block"] - atom)
    EA, EC, ED = _blocks(cell, old_dim)
    A_plus = _sym(A + EA)
    residual = EC - EA @ X
    Q = _sym(ED - X.T @ EC - EC.T @ X + X.T @ EA @ X)
    square = _sym(residual.T @ np.linalg.solve(A_plus, residual))
    G = _sym(Q - square)
    H = _sym(S + G)

    shell_dim = S.shape[0]
    f_map = np.vstack([X, -np.eye(shell_dim)])
    smooth_ray_matrix = _sym(f_map.T @ state["smooth_block"] @ f_map)
    atom_unit_ray_matrix = _sym(f_map.T @ atom_unit @ f_map)
    smooth_mass = 4.0 * (
        math.exp(0.5 * state["cell"][1]) - math.exp(0.5 * state["cell"][0])
    )

    return {
        "state": state,
        "A": A,
        "C": C,
        "D": D,
        "X": X,
        "S": S,
        "Q": Q,
        "square": square,
        "G": G,
        "H": H,
        "smooth_ray_matrix": smooth_ray_matrix,
        "atom_unit_ray_matrix": atom_unit_ray_matrix,
        "smooth_mass": smooth_mass,
        "Q_reconstruction_error": float(np.max(np.abs(Q - (smooth_ray_matrix - state["atom_weight"] * atom_unit_ray_matrix)))),
    }


def sylvester_certificate(H: np.ndarray) -> dict:
    H = _sym(H)
    eigs = np.linalg.eigvalsh(H)
    out = {
        "dim": H.shape[0],
        "eigs": eigs,
        "eigmin": float(eigs[0]) if eigs.size else float("nan"),
        "spd": bool(eigs.size and eigs[0] > 0.0),
    }
    if H.shape == (2, 2):
        out.update({
            "h11": float(H[0, 0]),
            "det": float(np.linalg.det(H)),
            "sylvester_spd": bool(H[0, 0] > 0.0 and np.linalg.det(H) > 0.0),
        })
    return out


def _unit_directions(dim: int, samples: int) -> list[np.ndarray]:
    if dim == 2:
        return [
            np.array([math.cos(theta), math.sin(theta)])
            for theta in np.linspace(0.0, math.pi, samples, endpoint=False)
        ]
    rng = np.random.default_rng(20260609 + dim)
    dirs = []
    for idx in range(dim):
        e = np.zeros(dim)
        e[idx] = 1.0
        dirs.append(e)
    random_dirs = rng.normal(size=(samples, dim))
    random_dirs /= np.linalg.norm(random_dirs, axis=1)[:, None]
    dirs.extend(random_dirs)
    return dirs


def beta_identity_stats(model: dict, samples: int = 721) -> dict:
    S = model["S"]
    H = model["H"]
    square = model["square"]
    smooth = model["smooth_ray_matrix"]
    atom_unit = model["atom_unit_ray_matrix"]
    smooth_mass = model["smooth_mass"]
    atom_weight = model["state"]["atom_weight"]

    negative = 0
    positive_atom = 0
    atom_helpful = 0
    repaired = 0
    max_identity_error = 0.0
    min_surplus = float("inf")
    min_after_negative = float("inf")
    min_after_atom_helpful = float("inf")
    for y in _unit_directions(S.shape[0], samples):
        y = y / np.linalg.norm(y)
        before = float(y.T @ S @ y)
        after = float(y.T @ H @ y)
        if before >= -1e-10:
            continue
        negative += 1
        min_after_negative = min(min_after_negative, after)
        if after >= -1e-10:
            repaired += 1
        k_atom = float(y.T @ atom_unit @ y)
        if k_atom <= 1e-12:
            atom_helpful += 1
            min_after_atom_helpful = min(min_after_atom_helpful, after)
            continue
        positive_atom += 1
        smooth_y = float(y.T @ smooth @ y)
        square_y = float(y.T @ square @ y)
        beta = smooth_y / (smooth_mass * k_atom)
        required = (
            atom_weight / smooth_mass
            + (-before + square_y) / (smooth_mass * k_atom)
        )
        surplus = beta - required
        identity_error = surplus - after / (smooth_mass * k_atom)
        max_identity_error = max(max_identity_error, abs(identity_error))
        min_surplus = min(min_surplus, surplus)

    return {
        "samples": samples if S.shape[0] == 2 else samples + S.shape[0],
        "negative": negative,
        "positive_atom": positive_atom,
        "atom_helpful": atom_helpful,
        "repaired": repaired,
        "min_after_negative": min_after_negative,
        "min_after_atom_helpful": min_after_atom_helpful,
        "min_surplus": min_surplus,
        "max_identity_error": max_identity_error,
    }


def _format_matrix(M: np.ndarray) -> str:
    rows = []
    for row in np.asarray(M):
        rows.append("[" + "  ".join(f"{float(x):+.12e}" for x in row) + "]")
    return "\n".join(rows)


def certificate(ncenters: int = 25, half_width: float = 0.06,
                samples: int = 721, physical_ngrid: int = 6001) -> dict:
    model = t1_matrices(ncenters, half_width, physical_ngrid=physical_ngrid)
    model["sylvester"] = sylvester_certificate(model["H"])
    model["identity_stats"] = beta_identity_stats(model, samples=samples)
    return model


def print_certificate(model: dict) -> None:
    state = model["state"]
    syl = model["sylvester"]
    stats = model["identity_stats"]
    print("=" * 78)
    print("Default active-23 T1 finite certificate")
    print("=" * 78)
    print(f"basis n={state['ncenters']} hw={state['half_width']:.3f}, "
          f"shell dim={model['S'].shape[0]}, "
          f"cell {state['repair_n']}=[{state['cell'][0]:.6f},{state['cell'][1]:.6f}], "
          f"log n={state['logn']:.6f}")
    print(f"smooth_mass={model['smooth_mass']:.12e}, "
          f"atom_weight={state['atom_weight']:.12e}, "
          f"Q reconstruction error={model['Q_reconstruction_error']:.3e}")
    print("\nS:")
    print(_format_matrix(model["S"]))
    print("\nG = Q - square:")
    print(_format_matrix(model["G"]))
    print("\nH = S + G:")
    print(_format_matrix(model["H"]))
    print(f"\neig(S): {', '.join(f'{x:+.12e}' for x in np.linalg.eigvalsh(model['S']))}")
    print(f"eig(H): {', '.join(f'{x:+.12e}' for x in syl['eigs'])}")
    if model["H"].shape == (2, 2):
        print(f"Sylvester: h11={syl['h11']:+.12e}, det={syl['det']:+.12e}, "
              f"spd={syl['sylvester_spd']}")
    else:
        print(f"SPD by eigenvalue check: eigmin={syl['eigmin']:+.12e}, spd={syl['spd']}")
    print("\nSampled budget identity on Schur-negative directions:")
    print(f"negative={stats['negative']}/{stats['samples']}, "
          f"positive_atom={stats['positive_atom']}, "
          f"atom_helpful={stats['atom_helpful']}, "
          f"repaired={stats['repaired']}")
    print(f"min after on negative sector={stats['min_after_negative']:+.12e}, "
          f"min beta surplus={stats['min_surplus']:+.12e}, "
          f"max identity error={stats['max_identity_error']:.3e}")
    if stats["atom_helpful"]:
        print(f"min after on atom-helpful sector={stats['min_after_atom_helpful']:+.12e}")
    print("\nInterpretation:")
    print("  H>0 is stronger than the stated T1 sector claim: every nonzero shell")
    print("  direction is repaired, so every Schur-negative direction is repaired.")
    print("  On the positive-atom part of the Schur-negative sector,")
    print("  beta_surplus = y^T H y / (smooth_mass * K_atom(y)).")


def refinement_table(samples: int = 361) -> list[dict]:
    rows = []
    print("\n[T1 H=S+G refinement table]")
    print("      basis       dim eigmin(H)   eigmin(S)   neg/samp repaired minSurp")
    for ncenters, half_width in REFINEMENTS:
        model = certificate(ncenters, half_width, samples=samples)
        stats = model["identity_stats"]
        row = {
            "ncenters": ncenters,
            "half_width": half_width,
            "dim": model["S"].shape[0],
            "eigmin_H": model["sylvester"]["eigmin"],
            "eigmin_S": float(np.linalg.eigvalsh(model["S"])[0]),
            "negative": stats["negative"],
            "samples": stats["samples"],
            "repaired": stats["repaired"],
            "min_surplus": stats["min_surplus"],
        }
        rows.append(row)
        print(f"      n{ncenters:<2d}/h{half_width:.3f} "
              f"{row['dim']:>2d}  "
              f"{row['eigmin_H']:+.6e} "
              f"{row['eigmin_S']:+.6e} "
              f"{row['negative']:>3d}/{row['samples']:<3d} "
              f"{row['repaired']:>3d}      "
              f"{row['min_surplus']:+.3e}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinements", action="store_true")
    parser.add_argument("--samples", type=int, default=721)
    args = parser.parse_args()
    model = certificate(samples=args.samples)
    print_certificate(model)
    if args.refinements:
        refinement_table(samples=max(181, args.samples // 2))


if __name__ == "__main__":
    main()
