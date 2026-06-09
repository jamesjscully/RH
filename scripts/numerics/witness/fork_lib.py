"""fork_lib: shared infrastructure for the FORK PROTOCOL (research/proof/14).

The fork test is the derivedness detector distilled from the R-TRACK terminal
result (doc 13): any quantity constructed from (W_inf, prime atoms, support
filtration) is transported losslessly to a zero-side functional by the
explicit formula. Before investing in a proposed "new object", compute its
zero-side image; if the candidate equals its image to truncation, the proposal
is a coordinate change of the explicit formula, not an attack surface.

This module provides the zero-side image machinery so a fork test is ~5 lines:

    from scripts.numerics.witness.fork_lib import zeta_gammas, zero_gram, fork_compare
    Mz = zero_gram(lad.centers, lad.hw, K=3000)   # raw bump coordinates
    q_zeros = (proj_to_my_coords @ Mz @ data_vec)  # candidate's zero image
    print(fork_compare(q_candidate, q_zeros))      # rel + cos verdict

Existing validated witnesses (prime_edge_residual_zerosum, certify_chain C5)
predate this module and keep their inline copies; new probes should use this.

Protocol summary (full statement in research/proof/14-fork-protocol.md):
  F1 value fork      - candidate vs zero-side image (this module).
  F2 deformation kill - run the candidate's SIGN MECHANISM on DH coefficients,
                        beta != 1/2 weights, smooth surrogates; surviving any
                        of them = over-proving = wrong (guard G5).
  F3 slack audit     - if the mechanism's inequality carries slack, it is dead
                        a priori: margins sit e^{-1.5R} below natural scale.
"""
import numpy as np
from flint import acb, ctx

from .semilocal_2 import _phihat

_GAMMA_CACHE: dict[int, np.ndarray] = {}


def zeta_gammas(K: int) -> np.ndarray:
    """First K positive ordinates of nontrivial zeta zeros (cached per process)."""
    if K not in _GAMMA_CACHE:
        ctx.prec = 80
        best = max((k for k in _GAMMA_CACHE if k > K), default=None)
        if best is not None:
            _GAMMA_CACHE[K] = _GAMMA_CACHE[best][:K]
        else:
            _GAMMA_CACHE[K] = np.array(
                [float(acb.zeta_zero(k).imag) for k in range(1, K + 1)])
    return _GAMMA_CACHE[K]


def zero_gram(centers: np.ndarray, hw: float, K: int = 3000) -> np.ndarray:
    """The zero-side Gram matrix in raw bump coordinates:
        (M_z)_{ab} = 2 sum_{k<=K} phihat_a(gamma_k) phihat_b(gamma_k).
    On the pole-killed space this equals the margin form M_R exactly up to
    zero truncation (closure theorem, doc 09 6'''; doc 13). Truncation scale
    for the standard ladder (hw=0.06, R<5): rel ~1e-3 at K=3000."""
    gam = zeta_gammas(K)
    PHz = np.array([_phihat(gam, c, hw) for c in centers])
    return 2.0 * (PHz @ PHz.T)


def fork_compare(candidate: np.ndarray, zero_image: np.ndarray) -> dict:
    """Verdict numbers for F1. rel ~ truncation and cos ~ 1 mean the candidate
    IS its zero image: a redescription of the explicit formula."""
    c = np.asarray(candidate, dtype=float).ravel()
    z = np.asarray(zero_image, dtype=float).ravel()
    nz = float(np.linalg.norm(z))
    rel = float(np.linalg.norm(c - z) / nz) if nz > 0 else float("inf")
    nc = float(np.linalg.norm(c))
    cos = float(c @ z / (nc * nz)) if nc > 0 and nz > 0 else float("nan")
    return {"rel": rel, "cos": cos,
            "verdict": "EF-DERIVED (coordinate change)" if rel < 0.05 and cos > 0.99
            else "carries non-spectral content - investigate"}
