"""Rigorous interval certificate for the default active-23 T1 endpoint.

GOAL (T1, doc 08): certify with rigorous ball arithmetic that for the default
late edge 3.00 -> 3.24 (basis ncenters=25, half_width=0.06, repair cell n=23)
the post-cell matrix

    M_+ = W_inf - P_exact(log n < 3.00) - w_23 T(log 23) - P_smooth([b23, 3.24])

compressed by the FIXED basis B (25 x 23, old_dim = 21, shell dim = 2) has

    A_+ > 0           (old block, via interval Cholesky), and
    H = D_+ - C_+^T A_+^{-1} C_+ > 0   (Sylvester: h11 > 0 and det H > 0),

with every algebraic step performed in arb ball arithmetic, so that the final
enclosures are mathematically rigorous relative to the exact statement below.

EXACT STATEMENT CERTIFIED (construction dependencies, all fixed and exact):
  * B = the float matrix produced by ``active_state()`` (edge_basis on the
    physical_ngrid=6001 L2 gram).  Its double-precision entries are taken as
    EXACT dyadic rationals; the theorem is about the exact subspace they span
    and the exact 21/2 block split.  No enclosure of the basis construction is
    needed for rigor: H > 0 together with A_+ > 0 is equivalent to
    x^T M_+ x > 0 for every nonzero x in span(B), and the shell claim
    "y^T(S+G)y > 0 for all shell y" is exactly the Schur statement for this
    fixed split.  (That B approximately satisfies the pole-kill constraints
    and approximate L2 orthonormality is interpretation, not rigor.)
  * old atoms: n in {2,3,4,5,7,8,9,11,13,16,17,19} (all prime powers with
    log n < 3), weight w_n = 2 Lambda(n)/sqrt(n) computed in arb.
  * repair atom: n = 23, w_23 = 2 log(23)/sqrt(23) in arb (the EXACT weight;
    the float pipeline's grid-derived atom_weight differs by ~2e-14).
  * smooth suffix interval [b23, right]: b23 = the double 0.5*(log23+log25)
    and right = the double 3.24, taken as exact statement endpoints (the same
    dyadic numbers the float pipeline used).
  * W_inf(i,j) = -g_ij(0) log pi + (1/pi) int_0^inf phihat_i phihat_j
    Re psi(1/4 + i t/2) dt, split into an Arb-integrated finite part [0, T]
    plus a rigorous tail envelope (lemma below) added to the radius.

RIGOROUS TAIL LEMMA (W_inf cutoff T > pi/hw):
  (i)  |phihat_c(t)| <= 2 pi^2 / (t (hw^2 t^2 - pi^2)) <= 2 pi^2 / (c t^3)
       for t >= T, with c = hw^2 - pi^2/T^2  (phihat_c(t) =
       2 cos(ct) pi^2 sin(hw t) / (t(pi^2 - hw^2 t^2)), |sin|,|cos| <= 1).
  (ii) |Re psi(1/4 + i t/2)| <= log t + log 2 + 1 for t >= 2: from
       psi(z) = log z - 1/(2z) - 2 int_0^inf u/((u^2+z^2)(e^{2 pi u}-1)) du,
       |u^2 + z^2| >= 2 Re(z) Im(z) = t/4 and int_0^inf u/(e^{2pi u}-1) = 1/24
       give |Re psi| <= log|z| + 1/(2|z|) + 1/(3t); |z| <= (t+1)/2 and
       |z| >= t/2 give <= log(t+1) - log 2 + 4/(3t) <= log t + log 2 + 1.
  (iii) therefore the absolute W_inf tail per entry is at most
       tau(T) = (4 pi^4 / (pi c^2)) [ (log T + log 2 + 1)/(5 T^5)
                                       + 1/(25 T^5) ]
       using int_T^inf (log t)/t^6 dt = (log T)/(5T^5) + 1/(25T^5).
  Cross-check: tau(5000) ~ 6.4e-12 vs the witness's numerically integrated
  envelope 5.953e-12 (same envelope, scipy-integrated) -- consistent and
  slightly more conservative, as it must be.

SOUNDNESS FIXES vs the diagnostic witnesses (recorded, both also noted in
research/work/L-t1-interval.md):
  * prime_defect_t1_winf_tail.winf_entry_arb puts ``digamma(z).real`` INSIDE
    the acb integrand.  Re of a holomorphic function is not holomorphic, so
    Arb's Gauss quadrature error bounds (which require holomorphy on the
    evaluation ellipses) do not apply: that enclosure is not certificate
    grade.  Here the integrand uses the holomorphic symmetrization
    (psi(1/4+it/2) + psi(1/4-it/2))/2, which equals Re psi on the real line.
  * the compact-overlap endpoints (max/min of center/half-width arithmetic)
    are computed in double precision in the diagnostic witnesses; the
    rounding (<= ~4e-15 absolute, integrand bounded by ~1.3) is NOT included
    in the Arb ball.  Here a conservative ENDPOINT_SLOP = 1e-13 is added to
    the radius of every overlap-based entry (atoms, g(0), smooth suffix).

PRE-REGISTERED READINGS (fixed before the computation):
  P0 sanity: the midpoint endpoint must reproduce the snapshot
     all-arithmetic Arb midpoint eigmin(H) = +2.511097945288e-02 to 5e-6
     (same components: Arb W_inf(T=5000) + Arb old atoms + Arb atom(23,
     exact weight) + Arb smooth suffix).  A mismatch = construction drift =
     ABORT, no certificate.
  P1 CONFIRMATION branch: all 21 Cholesky pivots of A_+ strictly positive
     AND [h11] > 0 AND [det H] > 0 as balls  =>  print CERTIFIED.  This
     merely confirms the floats; expected widths: H entry radii ~1e-6
     (dominated by the W_inf tail envelope through the old-block solve).
  P2 REFUTATION branch: A_+ > 0 certified but [h11] < 0 or [det H] < 0 as
     balls  =>  print REFUTED (the local mechanism's default endpoint is
     not positive definite) -- the major-result branch; escalate.
  P3 INCONCLUSIVE: any enclosure straddles 0  =>  print the per-ingredient
     width budget table and exit nonzero.  Do not weaken the target.

Fail-closed: every cross-check is an assert; exit code 0 only for P1 or P2
(a definite outcome), exit 2 for P0 abort, exit 1 for P3.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t1_interval_certificate
    python3 -m scripts.numerics.witness.prime_defect_t1_interval_certificate --T 2000   (faster, looser tail)
"""
from __future__ import annotations

import argparse
import math
import sys
import time

import numpy as np
from flint import acb, arb, ctx

from .prime_defect_active_atom_shift import active_state
from .prime_defect_t1_winf_tail import arb_phi_hat, winf_tail_bound
from .semilocal_2 import _phihat

ENDPOINT_SLOP = 1e-13  # justified in module docstring
SNAPSHOT_ALL_ARB_EIGMIN = 2.511097945288e-02  # P0 reference (TODO.md snapshot)
OLD_NS_EXPECTED = (2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19)


# ---------------------------------------------------------------------------
# scalar helpers
# ---------------------------------------------------------------------------

def _ball(x: arb) -> str:
    return f"[{float(x.mid()):+.12e} +/- {float(x.rad()):.3e}]"


def von_mangoldt_arb(n: int) -> arb:
    """Exact Lambda(n) in arb: log p if n = p^k, else 0."""
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return arb(p).log() if m == 1 else arb(0)
    return arb(0)


def add_slop(x: arb, slop: float = ENDPOINT_SLOP) -> arb:
    return x + arb(0, slop)


# ---------------------------------------------------------------------------
# rigorous overlap entries (atoms / g0): same analytic decomposition as
# prime_defect_t1_arb_components but with endpoint slop tracked
# ---------------------------------------------------------------------------

def _overlap_integral(si: float, sj: float, hw: float, U: float) -> acb:
    lo = max(si - hw, U + sj - hw)
    hi = min(si + hw, U + sj + hw)
    if hi <= lo:
        return acb(0)
    si_b, sj_b, hw_b, U_b = arb(si), arb(sj), arb(hw), arb(U)
    scale = arb.pi() / (2 * hw_b)

    def integrand(x, analytic):
        a = scale * (x - si_b)
        b = scale * (x - U_b - sj_b)
        return (a.cos() ** 2) * (b.cos() ** 2)

    return acb.integral(integrand, arb(lo), arb(hi),
                        rel_tol=arb("1e-30"), abs_tol=arb("1e-30"))


def atom_entry_ball(ci: float, cj: float, hw: float, U: float) -> arb:
    out = acb(0)
    for si in (ci, -ci):
        for sj in (cj, -cj):
            out += _overlap_integral(si, sj, hw, U)
    return add_slop(out.real)


def atom_matrix_ball(centers: np.ndarray, hw: float, U: float) -> list[list[arb]]:
    n = len(centers)
    out = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = atom_entry_ball(float(centers[i]), float(centers[j]), hw, U)
            out[i][j] = v
            out[j][i] = v
    return out


# ---------------------------------------------------------------------------
# rigorous smooth suffix entries (nested analytic integrals + slop)
# ---------------------------------------------------------------------------

def _signed_pair_smooth(si: float, sj: float, hw: float,
                        lo: float, hi: float) -> acb:
    d = si - sj
    a = max(lo, d - 2.0 * hw)
    b = min(hi, d + 2.0 * hw)
    if b <= a:
        return acb(0)
    si_b, sj_b, hw_b = arb(si), arb(sj), arb(hw)
    scale = arb.pi() / (2 * hw_b)

    def inner_for_u(U, side: str):
        if side == "left":
            vlo, vhi = si_b - hw_b, U + sj_b + hw_b
        else:
            vlo, vhi = U + sj_b - hw_b, si_b + hw_b

        def inner(v, analytic):
            aa = scale * (v - si_b)
            bb = scale * (v - U - sj_b)
            return (aa.cos() ** 2) * (bb.cos() ** 2)

        return acb.integral(inner, vlo, vhi,
                            rel_tol=arb("1e-28"), abs_tol=arb("1e-28"))

    def outer(side: str):
        def integrand(U, analytic):
            return 2 * (U / 2).exp() * inner_for_u(U, side)
        return integrand

    out = acb(0)
    if a < min(d, b):
        out += acb.integral(outer("left"), arb(a), arb(min(d, b)),
                            rel_tol=arb("1e-24"), abs_tol=arb("1e-24"))
    if max(a, d) < b:
        out += acb.integral(outer("right"), arb(max(a, d)), arb(b),
                            rel_tol=arb("1e-24"), abs_tol=arb("1e-24"))
    return out


def smooth_entry_ball(ci: float, cj: float, hw: float, lo: float, hi: float) -> arb:
    out = acb(0)
    for si in (ci, -ci):
        for sj in (cj, -cj):
            out += _signed_pair_smooth(si, sj, hw, lo, hi)
    return add_slop(out.real)


def smooth_matrix_ball(centers: np.ndarray, hw: float, lo: float, hi: float) -> list[list[arb]]:
    n = len(centers)
    out = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = smooth_entry_ball(float(centers[i]), float(centers[j]), hw, lo, hi)
            out[i][j] = v
            out[j][i] = v
    return out


# ---------------------------------------------------------------------------
# rigorous W_inf entries: holomorphic symmetrized digamma + tail lemma
# ---------------------------------------------------------------------------

def winf_tail_envelope(hw: float, T: float) -> arb:
    """Rigorous absolute bound for the discarded W_inf tail (lemma (iii))."""
    hw_b, T_b, pi = arb(hw), arb(T), arb.pi()
    c = hw_b ** 2 - pi ** 2 / T_b ** 2
    assert c > 0, "cutoff below pi/hw: envelope invalid"
    a = arb(2).log() + 1
    integral = (T_b.log() + a) / (5 * T_b ** 5) + 1 / (25 * T_b ** 5)
    return (4 * pi ** 4 / c ** 2) * integral / pi


def winf_entry_ball(ci: float, cj: float, hw: float, T: float,
                    g0: arb, tail: arb) -> arb:
    quarter = arb(1) / 4
    half_i = acb(0, arb(1) / 2)

    def integrand(t, analytic):
        phi = arb_phi_hat(ci, hw, t) * arb_phi_hat(cj, hw, t)
        zp = quarter + t * half_i
        zm = quarter - t * half_i
        return phi * (zp.digamma() + zm.digamma()) / 2

    val = acb.integral(integrand, arb(0), arb(T),
                       rel_tol=arb("1e-22"), abs_tol=arb("1e-22"),
                       eval_limit=400000, depth_limit=120)
    assert val.imag.contains(arb(0)), "symmetrized digamma integral has nonzero imag"
    finite = val.real
    out = -g0 * arb.pi().log() + finite / arb.pi()
    # tail: add [-tau, tau]
    tau = float(tail.upper()) * (1.0 + 1e-9)
    return out + arb(0, tau)


def winf_matrix_ball(centers: np.ndarray, hw: float, T: float,
                     g0_mat: list[list[arb]]) -> list[list[arb]]:
    n = len(centers)
    tail = winf_tail_envelope(hw, T)
    out = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = winf_entry_ball(float(centers[i]), float(centers[j]), hw, T,
                                g0_mat[i][j], tail)
            out[i][j] = v
            out[j][i] = v
    return out


# ---------------------------------------------------------------------------
# ball matrix algebra
# ---------------------------------------------------------------------------

def mat_sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_scale(A, s: arb):
    return [[s * a for a in row] for row in A]


def compress(M, Bf: np.ndarray):
    """B^T M B with B exact dyadic (floats)."""
    m, k = Bf.shape
    Bb = [[arb(float(Bf[i, j])) for j in range(k)] for i in range(m)]
    P = [[sum((M[i][j] * Bb[j][l] for j in range(m)), arb(0)) for l in range(k)]
         for i in range(m)]
    out = [[sum((Bb[i][r] * P[i][cidx] for i in range(m)), arb(0)) for cidx in range(k)]
           for r in range(k)]
    # enforce exact symmetry of the enclosure (true matrix is symmetric;
    # intersection of the (r,c) and (c,r) balls is a valid enclosure)
    for r in range(k):
        for cidx in range(r + 1, k):
            both = out[r][cidx].intersection(out[cidx][r]) \
                if hasattr(out[r][cidx], "intersection") else out[r][cidx]
            out[r][cidx] = both
            out[cidx][r] = both
    return out


def interval_cholesky(A, dim: int):
    """Rigorous interval Cholesky.  Success => every symmetric matrix within
    the entry balls (in particular the true A_+) is positive definite."""
    L = [[arb(0)] * dim for _ in range(dim)]
    pivots = []
    for j in range(dim):
        s = A[j][j]
        for k in range(j):
            s = s - L[j][k] * L[j][k]
        pivots.append(s)
        if not (s > 0):
            return False, L, pivots
        L[j][j] = s.sqrt()
        for i in range(j + 1, dim):
            r = A[i][j]
            for k in range(j):
                r = r - L[i][k] * L[j][k]
            L[i][j] = r / L[j][j]
    return True, L, pivots


def forward_substitute(L, C, dim: int, ncol: int):
    """V = L^{-1} C (enclosure)."""
    V = [[arb(0)] * ncol for _ in range(dim)]
    for col in range(ncol):
        for i in range(dim):
            s = C[i][col]
            for k in range(i):
                s = s - L[i][k] * V[k][col]
            V[i][col] = s / L[i][i]
    return V


def max_rad(M) -> float:
    return max(float(x.rad()) for row in M for x in row)


def max_mid(M) -> float:
    return max(abs(float(x.mid())) for row in M for x in row)


def mid_np(M) -> np.ndarray:
    return np.array([[float(x.mid()) for x in row] for row in M])


# ---------------------------------------------------------------------------
# fail-closed cross-checks
# ---------------------------------------------------------------------------

def crosschecks(state, T: float) -> None:
    hw = float(state["ambient"].half_width)
    # (1) arb_phi_hat agrees with the float transform
    for c in (0.02, 0.7916666666666667, 1.56):
        for t in (1e-3, 1.0, 7.5, math.pi / hw, 300.0):
            a = float(arb_phi_hat(c, hw, acb(t)).real.mid())
            f = float(_phihat(np.array([t]), c, hw)[0])
            assert abs(a - f) < 1e-10, ("phihat mismatch", c, t, a, f)
    # (2) digamma envelope dominance on samples t >= 2 (lemma (ii))
    for t in (2.0, 10.0, T, 2 * T, 10 * T, 100 * T):
        z = acb(0.25, 0.5 * t)
        re_psi = abs(float(z.digamma().real.mid()))
        assert re_psi <= math.log(t) + math.log(2.0) + 1.0, ("digamma envelope", t)
    # (3) closed-form tail >= scipy-integrated same envelope (sanity, scipy
    #     itself is not part of the rigor chain)
    tau = float(winf_tail_envelope(hw, T).mid())
    tau_scipy = winf_tail_bound(hw, T)
    assert tau >= 0.9 * tau_scipy, ("tail closed form below numeric envelope", tau, tau_scipy)
    assert tau <= 10.0 * tau_scipy, ("tail closed form implausibly loose", tau, tau_scipy)
    # (4) old-atom set is exactly the prime powers below the edge
    old_ns = sorted(n for n in state["ambient"].atoms["zeta"]
                    if math.log(n) < state["left"])
    assert tuple(old_ns) == OLD_NS_EXPECTED, ("old atom set drift", old_ns)
    for n in old_ns:
        lam = von_mangoldt_arb(n)
        assert float(lam.mid()) > 0.0, ("old atom with zero von Mangoldt", n)
    # (5) exact vs pipeline atom weight for n=23
    w_exact = 2 * arb(23).log() / arb(23).sqrt()
    assert abs(float(w_exact.mid()) - state["atom_weight"]) < 1e-12, "atom weight drift"


# ---------------------------------------------------------------------------
# main certificate
# ---------------------------------------------------------------------------

def run(T: float = 5000.0, prec: int = 120) -> int:
    ctx.prec = prec
    t_start = time.time()
    state = active_state()
    ambient = state["ambient"]
    centers = ambient.centers
    hw = float(ambient.half_width)
    Bf = state["B"]
    old_dim = int(state["old_dim"])
    shell_dim = Bf.shape[1] - old_dim
    suffix_lo = float(state["cell"][1])
    suffix_hi = float(state["right"])

    print("=" * 78)
    print("T1 interval certificate: default active-23 endpoint, rigorous balls")
    print("=" * 78)
    print(f"prec={prec} bits, W_inf cutoff T={T:.0f}, basis 25/hw=0.06, "
          f"old_dim={old_dim}, shell_dim={shell_dim}")
    print(f"suffix=[{suffix_lo!r}, {suffix_hi!r}] (exact dyadic statement endpoints)")

    crosschecks(state, T)
    print("cross-checks (phihat, digamma envelope, tail form, atom set, weight): PASS")

    ledger: list[tuple[str, float, float]] = []  # (name, max|mid|, max rad)

    # --- ingredient 1: g(0) overlap gram --------------------------------
    t0 = time.time()
    g0 = atom_matrix_ball(centers, hw, 0.0)
    ledger.append(("g(0) overlap gram", max_mid(g0), max_rad(g0)))
    print(f"g(0) gram done ({time.time()-t0:.1f}s) max rad={max_rad(g0):.2e}")

    # --- ingredient 2: W_inf finite + tail ------------------------------
    t0 = time.time()
    tail = winf_tail_envelope(hw, T)
    W = winf_matrix_ball(centers, hw, T, g0)
    ledger.append((f"W_inf (T={T:.0f} + tail {float(tail.upper()):.2e})",
                   max_mid(W), max_rad(W)))
    print(f"W_inf done ({time.time()-t0:.1f}s) max rad={max_rad(W):.2e} "
          f"tail envelope={float(tail.upper()):.3e}")

    # --- ingredient 3: old exact atoms ----------------------------------
    t0 = time.time()
    n_amb = len(centers)
    old_sum = [[arb(0)] * n_amb for _ in range(n_amb)]
    for n in OLD_NS_EXPECTED:
        w_n = 2 * von_mangoldt_arb(n) / arb(n).sqrt()
        atom_n = atom_matrix_ball(centers, hw, math.log(n))
        for i in range(n_amb):
            for j in range(n_amb):
                old_sum[i][j] = old_sum[i][j] + w_n * atom_n[i][j]
    ledger.append(("old atoms (12 prime powers < e^3)", max_mid(old_sum), max_rad(old_sum)))
    print(f"old atoms done ({time.time()-t0:.1f}s) max rad={max_rad(old_sum):.2e}")

    # --- ingredient 4: repair atom 23 (exact weight) --------------------
    t0 = time.time()
    w23 = 2 * arb(23).log() / arb(23).sqrt()
    atom23 = mat_scale(atom_matrix_ball(centers, hw, math.log(23)), w23)
    ledger.append(("atom(23), weight 2log23/sqrt23", max_mid(atom23), max_rad(atom23)))
    print(f"atom(23) done ({time.time()-t0:.1f}s) max rad={max_rad(atom23):.2e}")

    # --- ingredient 5: smooth suffix ------------------------------------
    t0 = time.time()
    suffix = smooth_matrix_ball(centers, hw, suffix_lo, suffix_hi)
    ledger.append(("smooth suffix", max_mid(suffix), max_rad(suffix)))
    print(f"smooth suffix done ({time.time()-t0:.1f}s) max rad={max_rad(suffix):.2e}")

    # --- assemble + compress --------------------------------------------
    M = mat_sub(mat_sub(mat_sub(W, old_sum), atom23), suffix)
    ledger.append(("ambient M_+", max_mid(M), max_rad(M)))
    t0 = time.time()
    Mc = compress(M, Bf)
    ledger.append(("compressed B^T M_+ B", max_mid(Mc), max_rad(Mc)))
    print(f"compression done ({time.time()-t0:.1f}s) max rad={max_rad(Mc):.2e}")

    dim = Bf.shape[1]
    A = [[Mc[i][j] for j in range(old_dim)] for i in range(old_dim)]
    C = [[Mc[i][old_dim + j] for j in range(shell_dim)] for i in range(old_dim)]
    D = [[Mc[old_dim + i][old_dim + j] for j in range(shell_dim)] for i in range(shell_dim)]

    # --- P0 sanity: midpoint endpoint vs snapshot ------------------------
    Mc_mid = mid_np(Mc)
    A_m, C_m, D_m = (Mc_mid[:old_dim, :old_dim], Mc_mid[:old_dim, old_dim:],
                     Mc_mid[old_dim:, old_dim:])
    H_mid_float = D_m - C_m.T @ np.linalg.solve(A_m, C_m)
    eig_mid = np.linalg.eigvalsh(0.5 * (H_mid_float + H_mid_float.T))
    print(f"\nP0 midpoint endpoint: eig(H_mid) = {eig_mid[0]:+.12e}, {eig_mid[1]:+.12e}")
    drift = abs(float(eig_mid[0]) - SNAPSHOT_ALL_ARB_EIGMIN)
    print(f"P0 drift from snapshot all-arithmetic eigmin: {drift:.3e} (limit 5e-6)")
    if drift > 5e-6:
        print("P0 ABORT: construction drift; no certificate issued.")
        _print_ledger(ledger)
        return 2

    # --- A_+ > 0 by interval Cholesky ------------------------------------
    t0 = time.time()
    ok, L, pivots = interval_cholesky(A, old_dim)
    min_piv = min((float(p.lower()) for p in pivots), default=float("nan"))
    max_piv_rad = max((float(p.rad()) for p in pivots), default=float("nan"))
    ledger.append(("A_+ Cholesky pivots", min_piv, max_piv_rad))
    print(f"\ninterval Cholesky ({time.time()-t0:.1f}s): "
          f"{len(pivots)}/{old_dim} pivots, min pivot lower bound={min_piv:+.6e}, "
          f"max pivot rad={max_piv_rad:.2e}")
    a_plus_negative = (not ok) and (pivots[-1] < 0)
    if not ok:
        if a_plus_negative:
            print("A_+ has a certifiably NEGATIVE pivot: A_+ is NOT positive definite.")
            print("OUTCOME: REFUTATION-GRADE finding on the old block; escalate.")
            _print_ledger(ledger)
            return 0
        print("A_+ pivot straddles 0: INCONCLUSIVE (width too large).")
        _print_ledger(ledger)
        return 1
    print("A_+ > 0 CERTIFIED (all 21 pivot balls strictly positive).")

    # --- H = D - V^T V ----------------------------------------------------
    V = forward_substitute(L, C, old_dim, shell_dim)
    H = [[D[i][j] - sum((V[k][i] * V[k][j] for k in range(old_dim)), arb(0))
          for j in range(shell_dim)] for i in range(shell_dim)]
    h11, h12, h21, h22 = H[0][0], H[0][1], H[1][0], H[1][1]
    det = h11 * h22 - h12 * h21
    trace = h11 + h22
    disc = trace * trace - 4 * det
    eig_lo = (trace - disc.sqrt()) / 2 if disc > 0 else None
    ledger.append(("H entries", max_mid(H), max_rad(H)))
    ledger.append(("det H", abs(float(det.mid())), float(det.rad())))

    print("\nH = S + G enclosure (Schur complement of the certified A_+):")
    print(f"  h11 = {_ball(h11)}")
    print(f"  h12 = {_ball(h12)}")
    print(f"  h22 = {_ball(h22)}")
    print(f"  det H = {_ball(det)}")
    if eig_lo is not None:
        print(f"  eigmin(H) enclosure = {_ball(eig_lo)}")
    _print_ledger(ledger)

    # --- Sylvester decision ----------------------------------------------
    if (h11 > 0) and (det > 0):
        slack11 = float(h11.lower()) / max(float(h11.rad()), 1e-300)
        slackdet = float(det.lower()) / max(float(det.rad()), 1e-300)
        print("\nOUTCOME: CERTIFIED  --  A_+ > 0 and H > 0 (Sylvester, rigorous balls)")
        print(f"  h11 lower bound  = {float(h11.lower()):+.12e}  "
              f"(margin/width = {slack11:.2e})")
        print(f"  det H lower bound = {float(det.lower()):+.12e}  "
              f"(margin/width = {slackdet:.2e})")
        print("  Every nonzero shell direction y satisfies y^T (S+G) y > 0 for the")
        print("  exact statement fixed in the docstring.  This CONFIRMS the floats;")
        print("  per the pre-registered asymmetry it does not extend the mechanism.")
        return 0
    if (h11 < 0) or (det < 0):
        print("\nOUTCOME: REFUTED  --  H is certifiably NOT positive definite while")
        print("  A_+ > 0 is certified.  The default local mechanism endpoint FAILS.")
        print("  This is the major-result branch: escalate immediately.")
        return 0
    print("\nOUTCOME: INCONCLUSIVE -- an enclosure straddles 0; see width budget.")
    print(f"  needed: rad(h11) < |h11| ~ 3.6e-2 and rad(det) < |det| ~ 4.8e-3")
    return 1


def _print_ledger(ledger) -> None:
    print("\nWidth budget ledger (per ingredient):")
    print(f"      {'ingredient':44s} {'max|mid| / min':>14s} {'max rad':>10s}")
    for name, mid, rad in ledger:
        print(f"      {name:44s} {mid:+.6e} {rad:10.2e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--T", type=float, default=5000.0,
                        help="W_inf finite cutoff (tail lemma covers the rest)")
    parser.add_argument("--prec", type=int, default=120)
    args = parser.parse_args()
    rc = run(T=args.T, prec=args.prec)
    sys.exit(rc)


if __name__ == "__main__":
    main()
