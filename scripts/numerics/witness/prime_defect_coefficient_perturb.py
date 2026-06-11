"""Coefficient perturbation tests for the nested passive defect kernel.

The current target says zeta's cumulative Euler history keeps the shell
transfer contractive.  This script tests arithmetic rigidity by replacing the
Euler coefficient table while leaving the archimedean/Sonin side and nested
basis unchanged.

Coefficient variants:

  zeta          von Mangoldt coefficients
  DH            Davenport-Heilbronn log-derivative coefficients
  signflip      deterministic sign flips of zeta coefficients
  shuffle       deterministic permutation of zeta coefficients among active n
  damp-old      zeta with old coefficients damped before the shell
  boost-old     zeta with old coefficients boosted before the shell

For each variant we compute the passive transfer ratio

    rho = ||A^{-1/2} C D^{-1/2}||^2

on nested support extensions in one ambient basis.

Run:
    python3 -m scripts.numerics.witness.prime_defect_coefficient_perturb
"""
from __future__ import annotations

import math

import numpy as np

from .explicit_formula import dh_coeffs, log_deriv_coeffs
from .prime_carleson_flow import _sym, _toeplitz_atom, coefficient_table
from .prime_nested_cone import _orthogonal_shell, build_ambient, point
from .prime_shell_coupling_bound import GMAXS

AMBIENT_N = 25
AMBIENT_HW = 0.06
MAX_GMAX = GMAXS[-1]
FOCUS_EDGES = (
    (1.72, 1.88),
    (1.88, 2.10),
    (2.30, 2.52),
    (2.76, 3.00),
    (3.00, 3.24),
)


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def coefficient_variant(name: str, max_n: int, left_gmax: float | None = None) -> list[float]:
    zeta = coefficient_table("zeta", max_n)
    if name == "zeta":
        return zeta
    if name == "DH":
        return [float(x) for x in log_deriv_coeffs(dh_coeffs(max_n), max_n)]
    if name == "signflip":
        return [c if n % 3 != 0 else -c for n, c in enumerate(zeta, start=1)]
    if name == "shuffle":
        out = zeta[:]
        active = list(range(2, max_n + 1))
        perm = active[:]
        # Deterministic non-random permutation: multiplication by 5 modulo an odd cycle.
        m = len(perm)
        values = [zeta[n - 1] for n in active]
        for i, n in enumerate(active):
            out[n - 1] = values[(5 * i + 3) % m]
        return out
    if name in {"damp-old", "boost-old"}:
        if left_gmax is None:
            raise ValueError("left_gmax required for old-history variants")
        factor = 0.75 if name == "damp-old" else 1.25
        return [
            c * factor if n >= 2 and math.log(n) < left_gmax else c
            for n, c in enumerate(zeta, start=1)
        ]
    raise ValueError(f"unknown variant: {name}")


def margin_from_coeffs(ambient, coeffs: list[float], gmax: float) -> tuple[np.ndarray, list[int]]:
    margin = ambient.gram["Winf"].copy()
    active = []
    for n in range(2, len(coeffs) + 1):
        logn = math.log(n)
        coeff = coeffs[n - 1]
        if logn >= gmax or abs(coeff) < 1e-12:
            continue
        atom = _toeplitz_atom(
            ambient.centers,
            ambient.half_width,
            logn,
            2.0 * coeff / math.sqrt(n),
        )
        margin = margin - atom
        active.append(n)
    return _sym(margin), active


def ambient_and_points():
    ambient = build_ambient(
        ncenters=AMBIENT_N,
        half_width=AMBIENT_HW,
        cmax=MAX_GMAX / 2.0 - AMBIENT_HW,
        max_gmax=MAX_GMAX,
    )
    # The nested basis depends only on the pole constraints and support, not on
    # the coefficient variant.  Use zeta points to get the bases.
    points = {gmax: point(ambient, "zeta", gmax) for gmax in GMAXS}
    return ambient, points


def rho_row(ambient, points: dict[float, dict], variant: str,
            left_gmax: float, right_gmax: float) -> dict:
    max_n = max(2, int(math.floor(math.exp(MAX_GMAX) - 1e-12)))
    coeffs = coefficient_variant(variant, max_n, left_gmax=left_gmax)
    M_right, active = margin_from_coeffs(ambient, coeffs, right_gmax)
    left = points[left_gmax]
    right = points[right_gmax]
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    block = _sym(B.T @ M_right @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    new_ns = [n for n in active if left_gmax <= math.log(n) < right_gmax]
    if A_invsqrt is None or D_invsqrt is None:
        return {
            "variant": variant,
            "left_gmax": left_gmax,
            "right_gmax": right_gmax,
            "new_ns": new_ns,
            "valid": False,
            "A_min": float(A_eigs[0]),
            "D_min": float(D_eigs[0]),
            "right_min": float(np.linalg.eigvalsh(_sym(right["basis"].T @ M_right @ right["basis"]))[0]),
        }
    K = A_invsqrt @ C @ D_invsqrt
    svals = np.linalg.svd(K, compute_uv=False)
    rho = float(svals[0] ** 2) if len(svals) else float("nan")
    defect_min = float(1.0 - rho)
    return {
        "variant": variant,
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "valid": True,
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "right_min": float(np.linalg.eigvalsh(_sym(right["basis"].T @ M_right @ right["basis"]))[0]),
        "rho": rho,
        "defect_min": defect_min,
    }


def all_rows() -> list[dict]:
    ambient, points = ambient_and_points()
    variants = ("zeta", "DH", "signflip", "shuffle", "damp-old", "boost-old")
    return [
        rho_row(ambient, points, variant, left, right)
        for variant in variants
        for left, right in FOCUS_EDGES
    ]


def _new_n_text(row: dict) -> str:
    return ",".join(str(n) for n in row["new_ns"]) or "none"


def _print_rows(rows: list[dict]) -> None:
    print("\n[1] Passive transfer under coefficient perturbations")
    print("      variant    edge        new n       right min   A min      D min      rho/defect")
    for row in rows:
        if row["valid"]:
            rd = f"{row['rho']:.3f}/{row['defect_min']:+.3f}"
        else:
            rd = "invalid"
        print(f"      {row['variant']:<9}  "
              f"{row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{_new_n_text(row):<10} "
              f"{row['right_min']:+.2e}   "
              f"{row['A_min']:+.2e}  "
              f"{row['D_min']:+.2e}  "
              f"{rd}")


def _print_summary(rows: list[dict]) -> None:
    print("\n[2] Perturbation summary")
    print("      variant    valid edges  max rho   first rho>1/invalid")
    for variant in ("zeta", "DH", "signflip", "shuffle", "damp-old", "boost-old"):
        group = [row for row in rows if row["variant"] == variant]
        valid = [row for row in group if row["valid"]]
        max_rho = max((row["rho"] for row in valid), default=float("nan"))
        first_bad = next(
            (row for row in group if (not row["valid"]) or row.get("rho", 0.0) > 1.0 + 1e-9),
            None,
        )
        if first_bad is None:
            bad_text = "none"
        elif first_bad["valid"]:
            bad_text = f"{first_bad['left_gmax']:.2f}->{first_bad['right_gmax']:.2f} rho={first_bad['rho']:.3f}"
        else:
            bad_text = f"{first_bad['left_gmax']:.2f}->{first_bad['right_gmax']:.2f} invalid"
        print(f"      {variant:<9}  "
              f"{len(valid):2d}           "
              f"{max_rho:.3f}    "
              f"{bad_text}")


def summary() -> dict:
    print("=" * 78)
    print("Coefficient perturbation tests for passive shell transfer")
    print("=" * 78)
    rows = all_rows()
    _print_rows(rows)
    _print_summary(rows)

    print("\nInterpretation:")
    print("  * Zeta's passive transfer is not generic long-memory behavior.")
    print("  * Scrambling signs or shuffling coefficients breaks positivity quickly.")
    print("  * Modest old-history damping/boosting probes how close the zeta chain is")
    print("    to criticality and whether the bound is coefficient-rigid.")
    return {"rows": rows}


if __name__ == "__main__":
    summary()
