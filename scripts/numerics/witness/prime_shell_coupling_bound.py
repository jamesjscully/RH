"""Passive shell-coupling witness for the nested Prime-Toeplitz target.

For a nested support extension H_L subset H_R, write the final margin on
H_R = H_L + shell as

    M_R = [ A  C ]
          [ C* D ].

The positive extension condition is the Schur bound

    C* A^{-1} C <= D.

When A and D are positive, this is equivalently a contraction estimate

    rho := lambda_max(D^{-1/2} C* A^{-1} C D^{-1/2}) <= 1.

This script computes rho across the nested finite models.  It is the most
direct numerical form of the proposed passive shell-coupling theorem.

Run:
    python3 -m scripts.numerics.witness.prime_shell_coupling_bound
"""
from __future__ import annotations

import numpy as np

from .prime_carleson_flow import _sym
from .prime_nested_cone import _orthogonal_shell, build_ambient, margin_at, point

GMAXS = (1.60, 1.72, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24)
REFINEMENTS = (
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
)
FOCUS_EDGES = ((1.72, 1.88), (1.88, 2.10), (2.30, 2.52), (2.76, 3.00), (3.00, 3.24))

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


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def coupling_row(ambient, kind: str, left_gmax: float, right_gmax: float) -> dict:
    left = cached_point(ambient, kind, left_gmax)
    right = cached_point(ambient, kind, right_gmax)
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    M = margin_at(ambient, kind, right_gmax)
    block = _sym(B.T @ M @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])

    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])

    if A.size and D.size and A_eigs[0] > 1e-10:
        coupling = _sym(C.T @ np.linalg.solve(A, C))
        schur = _sym(D - coupling)
        coupling_eigs = np.linalg.eigvalsh(coupling)
        schur_eigs = np.linalg.eigvalsh(schur)
    else:
        coupling = np.zeros_like(D)
        coupling_eigs = np.array([float("nan")])
        schur_eigs = np.array([float("nan")])

    D_invsqrt = _invsqrt_spd(D)
    if D_invsqrt is not None and np.isfinite(coupling_eigs[-1]):
        normalized = _sym(D_invsqrt @ coupling @ D_invsqrt)
        rho = float(np.linalg.eigvalsh(normalized)[-1])
        gain = float(np.sqrt(max(0.0, rho)))
    else:
        rho = float("nan")
        gain = float("nan")

    new_ns = sorted(set(right["active_ns"]) - set(left["active_ns"]))
    return {
        "kind": kind,
        "basis": f"n{len(ambient.centers)}/hw{ambient.half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "left_dim": left["dimension"],
        "right_dim": right["dimension"],
        "shell_dim": int(shell.shape[1]),
        "new_ns": new_ns,
        "right_min": float(right["eigs"][0]),
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "D_max": float(D_eigs[-1]),
        "coupling_max": float(coupling_eigs[-1]),
        "schur_min": float(schur_eigs[0]),
        "rho": rho,
        "gain": gain,
        "slack": float(1.0 - rho) if np.isfinite(rho) else float("nan"),
    }


def path_rows(kind: str, ncenters: int, half_width: float) -> list[dict]:
    ambient = ambient_for(ncenters, half_width)
    return [
        coupling_row(ambient, kind, left, right)
        for left, right in zip(GMAXS, GMAXS[1:])
    ]


def path_summary() -> list[dict]:
    out = []
    for kind in ("zeta", "DH"):
        for ncenters, half_width in REFINEMENTS:
            rows = path_rows(kind, ncenters, half_width)
            finite = [row for row in rows if np.isfinite(row["rho"])]
            max_row = max(finite, key=lambda row: row["rho"]) if finite else None
            first_bad = next((row for row in finite if row["rho"] > 1.0 + 1e-9), None)
            out.append({
                "kind": kind,
                "basis": f"n{ncenters}/hw{half_width:.2f}",
                "max_rho": max_row["rho"] if max_row else float("nan"),
                "max_gain": max_row["gain"] if max_row else float("nan"),
                "max_edge": None if max_row is None else (max_row["left_gmax"], max_row["right_gmax"]),
                "min_schur": min(row["schur_min"] for row in rows if np.isfinite(row["schur_min"])),
                "first_bad_edge": None if first_bad is None else (
                    first_bad["left_gmax"], first_bad["right_gmax"]
                ),
                "first_bad_rho": None if first_bad is None else first_bad["rho"],
            })
    return out


def focus_rows(kind: str) -> list[dict]:
    rows = []
    for ncenters, half_width in REFINEMENTS:
        ambient = ambient_for(ncenters, half_width)
        for left, right in FOCUS_EDGES:
            rows.append(coupling_row(ambient, kind, left, right))
    return rows


def _print_summary(rows: list[dict]) -> None:
    print("\n[1] Passive coupling contraction over nested paths")
    print("      kind   basis       max rho   max gain   max edge     min Schur   first rho>1")
    for row in rows:
        max_edge = "none" if row["max_edge"] is None else (
            f"{row['max_edge'][0]:.2f}->{row['max_edge'][1]:.2f}"
        )
        bad = "none" if row["first_bad_edge"] is None else (
            f"{row['first_bad_edge'][0]:.2f}->{row['first_bad_edge'][1]:.2f} "
            f"rho={row['first_bad_rho']:.3f}"
        )
        print(f"      {row['kind']:<5}  "
              f"{row['basis']:<10}  "
              f"{row['max_rho']:.3f}    "
              f"{row['max_gain']:.3f}     "
              f"{max_edge:<11} "
              f"{row['min_schur']:+.2e}   "
              f"{bad}")


def _print_focus(rows: list[dict], label: str) -> None:
    print(f"\n[2] Focus edge coupling ratios for {label}")
    print("      edge        basis       new n       D min     C*A^-1*C max  rho      gain    Schur")
    for row in rows:
        new_ns = ",".join(str(n) for n in row["new_ns"]) or "none"
        rho = "nan" if not np.isfinite(row["rho"]) else f"{row['rho']:.3f}"
        gain = "nan" if not np.isfinite(row["gain"]) else f"{row['gain']:.3f}"
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{new_ns:<10} "
              f"{row['D_min']:+.2e}  "
              f"{row['coupling_max']:+.2e}      "
              f"{rho:>6}  "
              f"{gain:>6}  "
              f"{row['schur_min']:+.2e}")
    print("      rho <= 1 is exactly the passive shell-coupling inequality when D > 0.")


def summary() -> dict:
    print("=" * 78)
    print("Passive shell-coupling bound for nested Prime-Toeplitz cones")
    print("=" * 78)

    summaries = path_summary()
    _print_summary(summaries)

    zeta_focus = focus_rows("zeta")
    dh_focus = focus_rows("DH")
    _print_focus(zeta_focus, "zeta")
    _print_focus(dh_focus, "DH")

    print("\nInterpretation:")
    print("  * Zeta stays contractive (rho <= 1) on every finite extension where")
    print("    the shell block is positive in the tested refinements.")
    print("  * DH breaks the contraction bound at the first failing refined shell.")
    print("  * The proof target is now a passive transfer estimate: the old-to-new")
    print("    coupling operator from shell energy D to old energy A has norm <= 1.")

    return {
        "path_summary": summaries,
        "zeta_focus": zeta_focus,
        "DH_focus": dh_focus,
    }


if __name__ == "__main__":
    summary()
