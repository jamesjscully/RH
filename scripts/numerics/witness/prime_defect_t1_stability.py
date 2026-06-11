"""Numerical stability probes for the default T1 matrix endpoint.

This is not a rigorous interval certificate.  It is a dependency check for the
certificate target in ``research/proof/08-default-t1-certificate.md``.  It
reruns the active-23 matrix construction under nearby quadrature choices and
reports how much the final matrix

    H = S + G

moves relative to its positive-definite margin.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t1_stability
    python3 -m scripts.numerics.witness.prime_defect_t1_stability --cases default,l2-fine
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

from . import semilocal_2
from .prime_defect_default_t1_certificate import certificate


@dataclass(frozen=True)
class StabilityCase:
    name: str
    fourier_T: float
    fourier_N: int
    physical_ngrid: int


CASES = {
    "coarse": StabilityCase("coarse", 220.0, 80001, 6001),
    "default": StabilityCase("default", 250.0, 100001, 6001),
    "wide": StabilityCase("wide", 300.0, 120001, 6001),
    "l2-fine": StabilityCase("l2-fine", 250.0, 100001, 12001),
}


def _load_fourier_grid(case: StabilityCase, loaded: tuple[float, int] | None) -> tuple[float, int]:
    key = (case.fourier_T, case.fourier_N)
    if loaded == key:
        return loaded
    semilocal_2._CACHE.clear()
    semilocal_2._grids(T=case.fourier_T, N=case.fourier_N)
    return key


def run_cases(case_names: list[str], samples: int = 181) -> list[dict]:
    rows = []
    loaded = None
    reference_H = None
    reference_eigs = None
    reference_det = None
    for name in case_names:
        case = CASES[name]
        loaded = _load_fourier_grid(case, loaded)
        model = certificate(samples=samples, physical_ngrid=case.physical_ngrid)
        H = model["H"]
        eigs_H = model["sylvester"]["eigs"]
        if reference_H is None:
            reference_H = H.copy()
            reference_eigs = eigs_H.copy()
            reference_det = model["sylvester"].get("det", float("nan"))
        if reference_eigs is not None and len(reference_eigs) == len(eigs_H):
            max_delta_eig = float(np.max(np.abs(eigs_H - reference_eigs)))
        else:
            max_delta_eig = float("nan")
        det_H = model["sylvester"].get("det", float("nan"))
        rows.append({
            "case": case,
            "H": H,
            "eigmin_H": model["sylvester"]["eigmin"],
            "det_H": det_H,
            "h11": model["sylvester"].get("h11", float("nan")),
            "max_delta_H": float(np.max(np.abs(H - reference_H))),
            "max_delta_eig_H": max_delta_eig,
            "delta_det_H": abs(det_H - reference_det) if reference_det is not None else float("nan"),
            "q_reconstruction_error": model["Q_reconstruction_error"],
            "identity_error": model["identity_stats"]["max_identity_error"],
            "min_after_negative": model["identity_stats"]["min_after_negative"],
        })
    return rows


def print_rows(rows: list[dict]) -> None:
    print("=" * 78)
    print("Default T1 matrix stability probe")
    print("=" * 78)
    print("      case       T      N       L2 grid  eigmin(H)    det(H)      max|deig|  ddet      id err")
    for row in rows:
        case = row["case"]
        print(f"      {case.name:<9} "
              f"{case.fourier_T:>5.0f}  "
              f"{case.fourier_N:<7d} "
              f"{case.physical_ngrid:<7d} "
              f"{row['eigmin_H']:+.6e} "
              f"{row['det_H']:+.6e} "
              f"{row['max_delta_eig_H']:.1e} "
              f"{row['delta_det_H']:.1e} "
              f"{row['identity_error']:.1e}")
    print("\nInterpretation:")
    print("  This probes numerical sensitivity only. A proof still needs rigorous")
    print("  enclosures for the Fourier tails, quadrature error, basis projection,")
    print("  and linear solves entering H[1,1] and det(H).")
    print("  Entrywise H deltas are not reported because changing the L2 grid can")
    print("  rotate the shell basis; eigenvalue and determinant drift are the useful")
    print("  invariants for this probe.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases",
        default="default,l2-fine",
        help=f"comma-separated cases from: {', '.join(CASES)}",
    )
    parser.add_argument("--samples", type=int, default=181)
    args = parser.parse_args()
    names = [name.strip() for name in args.cases.split(",") if name.strip()]
    unknown = sorted(set(names) - set(CASES))
    if unknown:
        raise SystemExit(f"unknown stability case(s): {', '.join(unknown)}")
    print_rows(run_cases(names, samples=args.samples))


if __name__ == "__main__":
    main()
