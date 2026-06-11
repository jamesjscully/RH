"""Stress tests for the nested Prime-Toeplitz cone extension target.

``prime_nested_cone.py`` fixes one ambient basis and turns support growth into
an inclusion problem H_L subset H_R.  This script varies the ambient refinement
and decomposes the shell Schur complement

    S = D - C^* A^{-1} C.

Here D is the new shell energy and C is the old-to-new coupling.  A negative
Schur complement means the larger support window is not a positive extension
of the smaller one.

Run:
    python3 -m scripts.numerics.witness.prime_nested_cone_stress
"""
from __future__ import annotations

import numpy as np

from .prime_nested_cone import (
    _orthogonal_shell,
    build_ambient,
    extension_rows,
    margin_at,
    point,
)
from .prime_carleson_flow import _sym

GMAXS = (1.60, 1.72, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24)
REFINEMENTS = (
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
)
FOCUS_EDGES = ((1.72, 1.88), (1.88, 2.10), (2.30, 2.52), (2.76, 3.00))

_AMBIENT_CACHE = {}
_POINT_CACHE = {}


def ambient_for(ncenters: int, half_width: float):
    key = (ncenters, half_width)
    if key not in _AMBIENT_CACHE:
        _AMBIENT_CACHE[key] = build_ambient(
            ncenters=ncenters,
            half_width=half_width,
            cmax=GMAXS[-1] / 2.0 - half_width,
            max_gmax=GMAXS[-1],
        )
    return _AMBIENT_CACHE[key]


def cached_point(ambient, kind: str, gmax: float) -> dict:
    key = (len(ambient.centers), ambient.half_width, kind, gmax)
    if key not in _POINT_CACHE:
        _POINT_CACHE[key] = point(ambient, kind, gmax)
    return _POINT_CACHE[key]


def nested_path(ambient, kind: str) -> list[dict]:
    return [cached_point(ambient, kind, gmax) for gmax in GMAXS]


def path_summary(kind: str, ncenters: int, half_width: float) -> dict:
    ambient = ambient_for(ncenters, half_width)
    points = nested_path(ambient, kind)
    rows = extension_rows(ambient, points)
    point_mins = [float(row["eigs"][0]) for row in points]
    first_bad_point = next(
        (row["gmax"] for row in points if float(row["eigs"][0]) < -1e-9),
        None,
    )
    finite_schurs = [row for row in rows if np.isfinite(row["schur_min"])]
    first_bad_schur = next(
        (row for row in finite_schurs if row["schur_min"] < -1e-9),
        None,
    )
    min_schur_row = min(finite_schurs, key=lambda row: row["schur_min"])
    return {
        "kind": kind,
        "basis": f"n{ncenters}/hw{half_width:.2f}",
        "min_point": min(point_mins),
        "first_bad_point": first_bad_point,
        "min_schur": min_schur_row["schur_min"],
        "min_schur_edge": (min_schur_row["left_gmax"], min_schur_row["right_gmax"]),
        "first_bad_schur_edge": None if first_bad_schur is None else (
            first_bad_schur["left_gmax"], first_bad_schur["right_gmax"]
        ),
        "first_bad_schur": None if first_bad_schur is None else first_bad_schur["schur_min"],
    }


def component_row(ambient, kind: str, left_gmax: float, right_gmax: float) -> dict:
    left = cached_point(ambient, kind, left_gmax)
    right = cached_point(ambient, kind, right_gmax)
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]

    total = margin_at(ambient, kind, right_gmax)
    winf = ambient.gram["Winf"]
    prime = _sym(winf - total)

    total_block = _sym(B.T @ total @ B)
    old_block = _sym(total_block[:old_dim, :old_dim])
    cross = total_block[:old_dim, old_dim:]
    shell_block = _sym(total_block[old_dim:, old_dim:])
    if old_block.size and shell_block.size and np.linalg.eigvalsh(old_block)[0] > 1e-10:
        coupling = _sym(cross.T @ np.linalg.solve(old_block, cross))
        schur = _sym(shell_block - coupling)
        coupling_max = float(np.linalg.eigvalsh(coupling)[-1])
        schur_min = float(np.linalg.eigvalsh(schur)[0])
    else:
        coupling_max = float("nan")
        schur_min = float("nan")

    winf_shell = _sym(shell.T @ winf @ shell)
    prime_shell = _sym(shell.T @ prime @ shell)
    total_shell = _sym(shell.T @ total @ shell)
    prime_cross = left["basis"].T @ prime @ shell
    total_cross = left["basis"].T @ total @ shell

    new_ns = sorted(set(right["active_ns"]) - set(left["active_ns"]))
    return {
        "kind": kind,
        "basis": f"n{len(ambient.centers)}/hw{ambient.half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "left_dim": left["dimension"],
        "right_dim": right["dimension"],
        "right_min": float(right["eigs"][0]),
        "shell_total_min": float(np.linalg.eigvalsh(total_shell)[0]),
        "schur_min": schur_min,
        "coupling_max": coupling_max,
        "winf_shell_min": float(np.linalg.eigvalsh(winf_shell)[0]),
        "winf_shell_max": float(np.linalg.eigvalsh(winf_shell)[-1]),
        "prime_shell_min": float(np.linalg.eigvalsh(prime_shell)[0]),
        "prime_shell_max": float(np.linalg.eigvalsh(prime_shell)[-1]),
        "prime_cross_norm": float(np.linalg.norm(prime_cross, ord=2)),
        "total_cross_norm": float(np.linalg.norm(total_cross, ord=2)),
    }


def focus_components(kind: str) -> list[dict]:
    rows = []
    for ncenters, half_width in REFINEMENTS:
        ambient = ambient_for(ncenters, half_width)
        for left_gmax, right_gmax in FOCUS_EDGES:
            rows.append(component_row(ambient, kind, left_gmax, right_gmax))
    return rows


def _print_path_summary(rows: list[dict]) -> None:
    print("\n[1] Nested path stability across ambient refinements")
    print("      kind   basis       min point eig   first bad point   min Schur   min edge    first bad Schur")
    for row in rows:
        first_point = "none" if row["first_bad_point"] is None else f"{row['first_bad_point']:.2f}"
        first_schur = "none" if row["first_bad_schur_edge"] is None else (
            f"{row['first_bad_schur_edge'][0]:.2f}->{row['first_bad_schur_edge'][1]:.2f} "
            f"{row['first_bad_schur']:+.2e}"
        )
        print(f"      {row['kind']:<5}  "
              f"{row['basis']:<10}  "
              f"{row['min_point']:+.2e}      "
              f"{first_point:<15} "
              f"{row['min_schur']:+.2e}  "
              f"{row['min_schur_edge'][0]:.2f}->{row['min_schur_edge'][1]:.2f}  "
              f"{first_schur}")


def _print_components(rows: list[dict], label: str) -> None:
    print(f"\n[2] Shell anatomy for {label}")
    print("      edge        basis       new n       shell   coupling  Schur    Winf shell      Prime shell      ||Pcross||")
    for row in rows:
        new_ns = ",".join(str(n) for n in row["new_ns"]) or "none"
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{new_ns:<10} "
              f"{row['shell_total_min']:+.2e}  "
              f"{row['coupling_max']:+.2e}  "
              f"{row['schur_min']:+.2e}  "
              f"[{row['winf_shell_min']:+.2e},{row['winf_shell_max']:+.2e}]  "
              f"[{row['prime_shell_min']:+.2e},{row['prime_shell_max']:+.2e}]  "
              f"{row['prime_cross_norm']:.1e}")
    print("      reading: Schur failure can occur even when the shell block is positive;")
    print("      the decisive comparison is shell energy versus old-to-new coupling.")


def summary() -> dict:
    print("=" * 78)
    print("Nested Prime-Toeplitz cone stress tests")
    print("=" * 78)

    summaries = [
        path_summary(kind, ncenters, half_width)
        for kind in ("zeta", "DH")
        for ncenters, half_width in REFINEMENTS
    ]
    _print_path_summary(summaries)

    zeta_components = focus_components("zeta")
    dh_components = focus_components("DH")
    _print_components(zeta_components, "zeta")
    _print_components(dh_components, "DH")

    print("\nInterpretation:")
    print("  * The nested Schur-complement discriminator is stable under the tested")
    print("    ambient refinements: zeta stays positive, while DH fails by the first")
    print("    refined crossing window (1.72->1.88 on finer grids, one edge later")
    print("    on the coarsest grid).")
    print("  * The first DH failure has positive shell energy but excessive coupling")
    print("    through the old block.  The theorem should bound that coupling.")
    print("  * This points to a de Branges/canonical-system style extension theorem:")
    print("    each support shell must enter as a passive positive extension.")

    return {
        "path_summary": summaries,
        "zeta_components": zeta_components,
        "DH_components": dh_components,
    }


if __name__ == "__main__":
    summary()
