"""Full-operator smooth-vs-discrete Euler measure surrogate.

The stress-kernel diagnostics show that the smooth PNT density is not enough
at the first-variation level.  This script tests the same question on the
actual finite Toeplitz operator:

    P_discrete(R) = sum_{log n < R} 2 Lambda(n)n^{-1/2} T_{log n}
    P_smooth(R)   = int_{log 2}^R 2 exp(U/2) T_U dU.

For each nested support edge, compare passive transfer for

    Winf,
    Winf - P_smooth(R),
    Winf - P_discrete(R).

Run:
    python3 -m scripts.numerics.witness.prime_defect_measure_surrogate
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_scale_phase import FOCUS_EDGES, _invsqrt_spd, ambient_and_points, scaled_margin
from .prime_nested_cone import _orthogonal_shell
from .semilocal_2 import _grids, _phihat


LOG2 = math.log(2.0)


def smooth_weight_primitive(ts: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Return int_lo^hi 2 exp(U/2) cos(t U) dU for each t."""
    a = 0.5
    z = a + 1j * ts
    vals = 2.0 * np.real((np.exp(z * hi) - np.exp(z * lo)) / z)
    return vals


def smooth_prime_operator(ambient, right_gmax: float) -> np.ndarray:
    if right_gmax <= LOG2:
        return np.zeros_like(ambient.gram["Winf"])
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    ph = np.array([_phihat(ts, center, ambient.half_width) for center in ambient.centers])
    primitive = smooth_weight_primitive(ts, LOG2, right_gmax)
    weighted = ph * primitive
    return _sym((weighted @ ph.T) * dt / (2.0 * np.pi))


def is_prime_power(n: int) -> bool:
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p:
            continue
        m = n
        while m % p == 0:
            m //= p
        return m == 1
    return False


def discrete_operator(ambient, right_gmax: float, mode: str) -> np.ndarray:
    out = np.zeros_like(ambient.gram["Winf"])
    for n, atom in ambient.atoms["zeta"].items():
        if math.log(n) >= right_gmax:
            continue
        is_power = is_prime_power(n)
        if mode == "all":
            out = out + atom
        elif mode == "primes" and not is_power:
            out = out + atom
        elif mode == "powers" and is_power:
            out = out + atom
        elif mode not in {"all", "primes", "powers"}:
            raise ValueError(f"unknown discrete mode: {mode}")
    return _sym(out)


def edge_transfer_for_margin(ambient, points: dict[float, dict],
                             left_gmax: float, right_gmax: float,
                             margin: np.ndarray) -> dict:
    left = points[left_gmax]
    right = points[right_gmax]
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    block = _sym(B.T @ margin @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    right_block = _sym(right["basis"].T @ margin @ right["basis"])
    right_min = float(np.linalg.eigvalsh(right_block)[0])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    if A_invsqrt is None or D_invsqrt is None:
        return {
            "valid": False,
            "rho": float("nan"),
            "defect": float("nan"),
            "right_min": right_min,
            "A_min": float(A_eigs[0]),
            "D_min": float(D_eigs[0]),
            "schur_min": float("nan"),
        }
    K = A_invsqrt @ C @ D_invsqrt
    svals = np.linalg.svd(K, compute_uv=False)
    rho = float(svals[0] ** 2) if len(svals) else float("nan")
    schur = _sym(D - C.T @ np.linalg.solve(A, C))
    schur_min = float(np.linalg.eigvalsh(schur)[0]) if schur.size else float("nan")
    return {
        "valid": True,
        "rho": rho,
        "defect": float(1.0 - rho),
        "right_min": right_min,
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "schur_min": schur_min,
    }


def edge_report(ambient, points, left: float, right: float) -> dict:
    arch = ambient.gram["Winf"].copy()
    smooth_op = smooth_prime_operator(ambient, right)
    primes_op = discrete_operator(ambient, right, "primes")
    powers_op = discrete_operator(ambient, right, "powers")
    all_op = _sym(primes_op + powers_op)
    smooth = _sym(arch - smooth_op)
    primes_only = _sym(arch - primes_op)
    powers_only = _sym(arch - powers_op)
    discrete = _sym(arch - all_op)
    rows = {
        "arch": edge_transfer_for_margin(ambient, points, left, right, arch),
        "smooth": edge_transfer_for_margin(ambient, points, left, right, smooth),
        "primes": edge_transfer_for_margin(ambient, points, left, right, primes_only),
        "powers": edge_transfer_for_margin(ambient, points, left, right, powers_only),
        "discrete": edge_transfer_for_margin(ambient, points, left, right, discrete),
    }
    rows["residual_delta"] = {
        "right_min_gain": rows["discrete"]["right_min"] - rows["smooth"]["right_min"],
        "rho_gain": rows["smooth"]["rho"] - rows["discrete"]["rho"]
        if rows["smooth"]["valid"] and rows["discrete"]["valid"] else float("nan"),
        "schur_gain": rows["discrete"]["schur_min"] - rows["smooth"]["schur_min"]
        if rows["smooth"]["valid"] and rows["discrete"]["valid"] else float("nan"),
    }
    return {"left": left, "right": right, "rows": rows}


def _fmt_metric(row: dict) -> str:
    if not row["valid"]:
        return (f"invalid  rho=nan     defect=nan      "
                f"right={row['right_min']:+.2e} A={row['A_min']:+.2e} D={row['D_min']:+.2e}")
    return (f"valid    rho={row['rho']:.3f}  defect={row['defect']:+.3f}  "
            f"right={row['right_min']:+.2e} schur={row['schur_min']:+.2e}")


def _print_edge(report: dict) -> None:
    print(f"\n[edge {report['left']:.2f}->{report['right']:.2f}]")
    for name in ("arch", "smooth", "primes", "powers", "discrete"):
        print(f"      {name:<8} {_fmt_metric(report['rows'][name])}")
    delta = report["rows"]["residual_delta"]
    print("      discrete - smooth: "
          f"right_min {delta['right_min_gain']:+.2e}, "
          f"rho improvement {delta['rho_gain']:+.3f}, "
          f"schur gain {delta['schur_gain']:+.2e}")


def summary() -> dict:
    print("=" * 78)
    print("Full-operator smooth-vs-discrete Euler measure surrogate")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * The smooth PNT-density Toeplitz operator is not interchangeable")
    print("    with the discrete Euler operator in the shell-transfer test.")
    print("  * Prime-only and prime-power-only truncations do not reproduce the")
    print("    full zeta repair; the exact combined discrete measure is load-bearing.")
    print("  * The proof target should keep the exact Euler measure until the")
    print("    final Schur-complement positivity is established.")
    return reports


if __name__ == "__main__":
    summary()
