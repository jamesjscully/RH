"""HH PROBE 1 witness (doc 32): does the Weil/tracking form factor through the
certified Lorentzian index face?

Both sides are banked: the Weil side is the doc-13 margin form M_R = W_inf - P_R
on the pole-killed ladder (prime_ladder_scaling conventions: atom block value on
a test x is  weight_n * (phi_x * phi_x)(log n),  weight_n = 2 Lambda(n)/sqrt(n));
the index side is the certified Lorentzian norm-Gram on the geometric monoid
family {[p^i]}:  M = (w log p) MAX + E  (W-doc sec 5, exact lemma) and AA's
strict CC version  M_CC = (log p) MAX + log2 (J - I)  (certified (1, n)).

THE MAP T (G-INT6, every choice logged in the doc HH-weil-restriction-fork.md):
    T_p(g) = sum_{k=1}^{n_p} c_{p,k}(g) d_k,   c_{p,k}(g) = (f*f)(k log p)
             = the sample of the convolution-square test g at the ladder
             frequency k log p   (doc 19's dictionary: g restricts to atom
             weights at {k log p}),
    d_k = [p^k] - [p^{k-1}]  (AA's difference classes; the only non-sample
    choice is the receptacle [p^0] = the monoid unit, forced by sum-zero),
    Theta_p = 2 sum_k p^{-k/2} d_k  (the KMS-1/2 geometric-series vector; the
    p^{-k/2} is doc 19's self-dual normalization, the 2 is the even-test fold).

CANDIDATE THEOREM HH.1 (exact, to be gated): the difference classes
DIAGONALIZE the certified face:
    <d_k, d_l>_{(w log p) MAX} = -(w log p) delta_{kl},
    i.e. Lambda(p^k) = -<d_k, d_k>  (w = 1):  the von Mangoldt atom weight is
    MINUS THE SELF-INTERSECTION of the ladder step.  Consequently
    P_R(g) = - sum_p <T_p(g), Theta_p>_{(log p) MAX}     EXACTLY (defect 0),
and the full Weil form on the pole-killed class reads
    Q(g) = M_R(g) = W_inf(g) + sum_p <T_p(g), Theta_p>_M:
the defect of the index-face factorization is R(g) = W_inf(g), the archimedean
supply -- NOT a new object (fork (b) expected, defect = doc 31 exit B).

PRE-REGISTERED GATES (fail-closed, exit-code gated; tolerances fixed in
advance from the known budgets: T=250 Fourier truncation ~1e-6/entry, doc 11;
exact gates use Fraction arithmetic, zero tolerance):

  H1 (EXACT, Fraction): for n <= 12, w in {1,2,3}:
      (a) D^T MAX_w D = -w I_n  (units of log p),
      (b) D^T (J - I) D = -(2 I_n - S), S = nearest-neighbor 0/1 (units log 2),
      (c) the unit class e_0 = [1] is NULL in both faces; <e_0, d_k> =
          w (log p units) + delta_{k1} (log 2 units)  [= log N([p^w]-[1]) at
          k=1: AA's N = 2 p^max],
      (d) 1^T MAX^{-1} 1 > 0: the M-orthocomplement of span{d_k} (= the
          sum-zero hyperplane = maximal spacelike) is TIMELIKE.
  H2 (float, T-truncation budget): wiring of the dictionary: per zeta atom,
      x^T blk_n x = weight_n * autocorr_x(log n) with autocorr computed by an
      INDEPENDENT u-space quadrature (no t-grid): assembled prime-side value
      agrees rel <= 5e-3 on each of 5 random pole-killed tests (per-atom
      stats reported).
  H3 (float, exact rearrangement, rel <= 1e-12): on the same tests,
      (a) sum-of-samples prime side  = - sum_p <T_p, Theta_p>_{(log p) MAX},
      (b) CC-strict defect: <T,Theta>_CC - <T,Theta>_MAX = -log2 (t . theta)
          (J-part annihilated: both vectors sum-zero, |t^T J theta| <= 1e-14),
      (c) <Theta_p, Theta_p> = -4 log p sum_k p^{-k}  (per-place Euler tail;
          sum_p diverges = the s=1 pole sits OUTSIDE the lattice completion).
  H4 (float, wiring + measurement): per rung R of the doc-13 ladder:
      Q^T M_R Q = Q^T W_inf Q - Q^T P_R Q to 1e-10 rel; REPORT eigmin of the
      W_inf block, the inertia of the P_R block, margin eigmin.  Reading
      pre-registered BOTH ways: eigmin(W_inf) > 0 on the pole-killed class =>
      the archimedean defect is a positive budget (half-space form is a
      gauge-cone form); eigmin <= 0 => the defect is signed, record honestly.
  H5 (Bochner/cone): 200 random pole-killed tests, places p in {2,3,5,7}:
      (a) the sample sequences (c_0, c_1, ..., c_{n_p}) are PSD-Toeplitz
          (eigmin >= -1e-8 c_0): T(class) lands in the MOMENT CONE
          (Herglotz; the CC20/doc-16 level-1 mechanism in lattice coords),
      (b) properness: ||T(g)||_{-M} <= c_0 sqrt(psi(e^R)) (theorem-implied;
          psi = Chebyshev over the atom window); measured max ratio reported
          (the content is the measured aperture, not the bound).
  H6 (CARRIER GUARD, decisive gate rerun on DH): zeta: coeff(p^k)/log p = 1
      exactly (rel 1e-12) -- the Theta vector is the pure KMS geometric
      series, no per-atom retuning; DH: the same dictionary is UNFORMABLE:
      gate requires BOTH (#negative-weight DH atoms > 0) AND
      (#non-prime-power DH atoms > 0) in the window: no tower address, and
      Lambda = -<d,d> >= 0 is violated.  (Epstein: the MAX face itself is
      carrier-blind -- AA gate N9, banked; the discrimination lives in T.)
  H7 (F1 fork, zeros COMPARISON ONLY, fork_lib): margin-form values vs
      zero-side values on pole-killed vectors at R = 4.96, K = 3000 zeros:
      gate verdict must be "EF-DERIVED (coordinate change)" (rel < 0.05,
      cos > 0.99).  Pre-registered honesty: the factorization IS the explicit
      formula in lattice coordinates; the probe's product is the geometry
      ledger (frame, null unit, idle Perron direction, moment-cone image),
      not a new positivity.

FORK VERDICT CRITERIA (fixed in advance):
  (a) FACTORS: would need R == 0 including W_inf homed in the lattice -- NOT
      expected (the archimedean supply is a continuum, no frequency comb).
  (b) DEFECT, STRUCTURED: H1+H3 pass and R(g) = W_inf(g) identically: the
      defect IS the archimedean supply (doc 31 exit B / BB's missing Poisson
      unit) -- the task-card prediction "R = zero-side term" is then REFUTED
      in the precise sense (by doc-09 closure the zero side equals the WHOLE
      form, not the defect).
  (c) NO FACTORIZATION: H1 or H3 fail.

Run:
    python3 -m scripts.numerics.witness.prime_hh_weil_index_factorization
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction

import numpy as np

from .prime_carleson_flow import _raised_cosine_even, _sym, coefficient_table
from .prime_ladder_scaling import build_ladder, margin_at, nested_basis
from .fork_lib import zero_gram, fork_compare

GATES: list[tuple[str, bool, str]] = []


def gate(name: str, ok: bool, detail: str) -> None:
    GATES.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------------------------------------
# H1: exact d-frame diagonalization of the index faces (Fraction arithmetic)
# ---------------------------------------------------------------------------

def _frac_solve(A: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]


def h1_exact() -> None:
    print("\nH1: exact d-frame diagonalization (Fraction; n <= 12, w in {1,2,3})")
    worst = "ok"
    ok_all = True
    for n in (3, 5, 8, 12):
        for w in (1, 2, 3):
            N = n + 1
            MAX = [[Fraction(w * max(i, j)) for j in range(N)] for i in range(N)]
            E = [[Fraction(0 if i == j else 1) for j in range(N)] for i in range(N)]
            # columns d_k = e_k - e_{k-1}, k = 1..n
            def dvec(k):
                v = [Fraction(0)] * N
                v[k], v[k - 1] = Fraction(1), Fraction(-1)
                return v
            for k in range(1, n + 1):
                for l in range(1, n + 1):
                    gM = sum(dvec(k)[i] * MAX[i][j] * dvec(l)[j]
                             for i in range(N) for j in range(N))
                    gE = sum(dvec(k)[i] * E[i][j] * dvec(l)[j]
                             for i in range(N) for j in range(N))
                    expM = Fraction(-w) if k == l else Fraction(0)
                    expE = Fraction(-2) if k == l else (Fraction(1) if abs(k - l) == 1 else Fraction(0))
                    if gM != expM or gE != expE:
                        ok_all = False
                        worst = f"n={n} w={w} (k,l)=({k},{l}): got ({gM},{gE}) want ({expM},{expE})"
            # e_0 null + cross terms
            if MAX[0][0] != 0 or E[0][0] != 0:
                ok_all, worst = False, f"e_0 not null at n={n},w={w}"
            for k in range(1, n + 1):
                cM = sum(MAX[0][j] * dvec(k)[j] for j in range(N))
                cE = sum(E[0][j] * dvec(k)[j] for j in range(N))
                if cM != Fraction(w) or cE != (Fraction(1) if k == 1 else Fraction(0)):
                    ok_all, worst = False, f"<e0,d_{k}> wrong at n={n},w={w}: ({cM},{cE})"
    gate("H1abc d-frame Gram exact", ok_all,
         "D^T MAX D = -w I, D^T(J-I)D = -(2I - S), [1] null, <e0,dk> = w logp + d_k1 log2"
         if ok_all else worst)
    # H1d: timelike complement
    ok_d, vals = True, []
    for n in (3, 5, 8, 12):
        N = n + 1
        MAX = [[Fraction(max(i, j)) for j in range(N)] for i in range(N)]
        z = _frac_solve(MAX, [Fraction(1)] * N)
        q = sum(z)  # 1^T MAX^{-1} 1
        vals.append(f"n={n}: {q}")
        if q <= 0:
            ok_d = False
    gate("H1d timelike complement", ok_d,
         "1^T MAX^{-1} 1 = " + "; ".join(vals) + " (all > 0: sum-zero hyperplane is maximal spacelike)")


# ---------------------------------------------------------------------------
# ladder + sample machinery
# ---------------------------------------------------------------------------

CMAX, NCENT, HW, GMAX, T, NGRID = 2.42, 38, 0.06, 4.96, 250.0, 100001
UPTS = 24001


class Sampler:
    def __init__(self, lad):
        self.lad = lad
        self.umax = CMAX + HW
        self.u = np.linspace(-self.umax, self.umax, UPTS)
        self.BAS = _raised_cosine_even(lad.centers, HW, self.u)
        self._trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
        self._shift_cache: dict[float, np.ndarray] = {}

    def autocorr(self, x: np.ndarray, tau: float) -> float:
        """(f*f)(tau) for f = sum x_a bump_a, by direct u-space quadrature."""
        key = round(tau, 12)
        if key not in self._shift_cache:
            self._shift_cache[key] = _raised_cosine_even(self.lad.centers, HW, tau - self.u)
        phi = x @ self.BAS
        phis = x @ self._shift_cache[key]
        return float(self._trap(phi * phis, x=self.u))


def towers(gmax: float, max_n: int) -> dict[int, int]:
    """prime -> n_p (number of ladder steps p^k with log p^k < gmax)."""
    out = {}
    for p in range(2, max_n + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            np_ = int(math.floor((gmax - 1e-12) / math.log(p)))
            if np_ >= 1:
                out[p] = np_
    return out


def lattice_pairing(p: int, n_p: int, c: np.ndarray, strict_cc: bool = False):
    """<T, Theta>_M with T = sum c_k d_k, Theta = 2 sum p^{-k/2} d_k, in the
    (n_p+1)-dim coefficient space of {[p^0..p^{n_p}]}."""
    N = n_p + 1
    logp = math.log(p)
    MAX = logp * np.maximum.outer(np.arange(N), np.arange(N)).astype(float)
    M = MAX.copy()
    if strict_cc:
        M = M + math.log(2.0) * (np.ones((N, N)) - np.eye(N))
    D = np.zeros((N, n_p))
    for k in range(1, N):
        D[k, k - 1], D[k - 1, k - 1] = 1.0, -1.0
    t = D @ c
    theta = D @ (2.0 * np.array([p ** (-(k + 1) / 2.0) for k in range(n_p)]))
    return float(t @ M @ theta), t, theta


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 96)
    print("HH PROBE 1: Weil form vs the certified Lorentzian index face")
    print("=" * 96)

    h1_exact()

    print(f"\n[build] doc-13 quick ladder: ncenters={NCENT}, hw={HW}, cmax={CMAX}, "
          f"T={T}, N={NGRID}, gmax={GMAX}")
    lad = build_ladder(CMAX, NCENT, HW, GMAX, T=T, N=NGRID)
    smp = Sampler(lad)
    max_n = int(math.floor(math.exp(GMAX)))
    tw = towers(GMAX, max_n)
    psi_window = sum(math.log(p) * n_p for p, n_p in tw.items())
    print(f"[build] zeta atoms={len(lad.atoms['zeta'])}, towers={len(tw)} places, "
          f"psi(e^R) over window = {psi_window:.3f}")

    rng = np.random.default_rng(20260610)
    Q = nested_basis(lad, GMAX)
    dimQ = Q.shape[1]
    print(f"[build] pole-killed nested basis at R={GMAX}: dim={dimQ}")

    # ---- H2 + H3 on 5 random pole-killed tests --------------------------
    print("\nH2/H3: dictionary wiring + exact lattice rearrangement (5 tests)")
    h2_rels, h3a_rels, h3b_errs, h3j_errs = [], [], [], []
    atom_rel_worst = 0.0
    for it in range(5):
        y = Q @ rng.standard_normal(dimQ)
        y /= np.linalg.norm(y)
        # per-atom: block value vs weight * autocorr
        pred_sum, act_sum = 0.0, 0.0
        samples: dict[float, float] = {}
        for (logn, w_n, blk) in lad.atoms["zeta"]:
            a = smp.autocorr(y, logn)
            samples[round(logn, 12)] = a
            pred = w_n * a
            act = float(y @ blk @ y)
            pred_sum += pred
            act_sum += act
            if abs(act) > 1e-7:
                atom_rel_worst = max(atom_rel_worst, abs(pred - act) / abs(act))
        h2_rels.append(abs(pred_sum - act_sum) / max(abs(act_sum), 1e-300))
        # lattice side
        pair_sum, side_sum = 0.0, 0.0
        jmax, ccerr = 0.0, 0.0
        for p, n_p in tw.items():
            logp = math.log(p)
            c = np.array([samples.get(round(k * logp, 12),
                                      smp.autocorr(y, k * logp))
                          for k in range(1, n_p + 1)])
            side = float(sum(2.0 * logp * p ** (-k / 2.0) * c[k - 1]
                             for k in range(1, n_p + 1)))
            pair, t, theta = lattice_pairing(p, n_p, c, strict_cc=False)
            pair_cc, _, _ = lattice_pairing(p, n_p, c, strict_cc=True)
            side_sum += side
            pair_sum += pair
            jmax = max(jmax, abs(float(np.sum(t)) * float(np.sum(theta))))
            ccerr = max(ccerr, abs((pair_cc - pair) - (-math.log(2.0) * float(t @ theta))))
        h3a_rels.append(abs(side_sum - (-pair_sum)) / max(abs(side_sum), 1e-300))
        h3b_errs.append(ccerr)
        h3j_errs.append(jmax)
    gate("H2 wiring (t-grid vs u-quadrature)", max(h2_rels) <= 5e-3,
         f"assembled prime-side rel diff per test max {max(h2_rels):.2e} "
         f"(per-atom worst rel {atom_rel_worst:.2e}; budget: T={T} truncation)")
    gate("H3a exact factorization P_R = -sum_p <T,Theta>_MAX", max(h3a_rels) <= 1e-12,
         f"rel diff max {max(h3a_rels):.2e} over 5 tests x {len(tw)} places")
    gate("H3b CC-strict defect = -log2 (t.theta)", max(h3b_errs) <= 1e-12 and max(h3j_errs) <= 1e-14,
         f"closed-form err max {max(h3b_errs):.2e}; |sum(t) sum(theta)| max {max(h3j_errs):.2e}")
    # H3c Theta norms
    h3c_err, tail_sum = 0.0, 0.0
    for p, n_p in tw.items():
        logp = math.log(p)
        theta_c = 2.0 * np.array([p ** (-(k + 1) / 2.0) for k in range(n_p)])
        # <Theta,Theta>_MAX = -logp * sum theta_k^2 (d-frame diagonal)
        pair, _, _ = lattice_pairing(p, n_p, np.asarray(theta_c) / 2.0 * 0.0 + theta_c / 2.0)
        # direct: build explicitly
        N = n_p + 1
        MAXm = logp * np.maximum.outer(np.arange(N), np.arange(N)).astype(float)
        D = np.zeros((N, n_p))
        for k in range(1, N):
            D[k, k - 1], D[k - 1, k - 1] = 1.0, -1.0
        th = D @ theta_c
        got = float(th @ MAXm @ th)
        want = -4.0 * logp * sum(p ** (-k) for k in range(1, n_p + 1))
        h3c_err = max(h3c_err, abs(got - want) / abs(want))
        tail_sum += -want
    gate("H3c <Theta_p,Theta_p> = -4 logp sum p^-k", h3c_err <= 1e-12,
         f"rel err max {h3c_err:.2e}; sum_p ||Theta_p||^2_{{-M}} = {tail_sum:.3f} "
         f"(-> 4 sum_p logp/(p-1), divergent: the s=1 pole is outside the lattice completion)")

    # ---- H4: rung decomposition ------------------------------------------
    print("\nH4: rung decomposition  M_R = W_inf - P_R  on pole-killed bases")
    gmaxs = (1.60, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50, 3.76,
             4.00, 4.26, 4.50, 4.76, 4.96)
    ok_h4, winf_mins = True, []
    print("   rung    dim   eigmin(Winf)  eigmin(P)    n-(P)  eigmin(M_R)")
    for R in gmaxs:
        QR = nested_basis(lad, R)
        if QR.shape[1] == 0:
            continue
        MR = margin_at(lad, "zeta", R)
        PR = lad.Winf - MR
        Wb = _sym(QR.T @ lad.Winf @ QR)
        Pb = _sym(QR.T @ PR @ QR)
        Mb = _sym(QR.T @ MR @ QR)
        rearr = float(np.linalg.norm(Mb - (Wb - Pb)) / max(np.linalg.norm(Mb), 1e-300))
        if rearr > 1e-10:
            ok_h4 = False
        ew, ep, em = (np.linalg.eigvalsh(Wb), np.linalg.eigvalsh(Pb),
                      np.linalg.eigvalsh(Mb))
        nneg = int(np.sum(ep < 0))
        winf_mins.append(float(ew[0]))
        print(f"   {R:4.2f}   {QR.shape[1]:3d}   {ew[0]:+.4e}   {ep[0]:+.4e}  "
              f"{nneg:3d}   {em[0]:+.4e}")
    gate("H4 rung rearrangement", ok_h4, "M_R = W_inf - P_R block-exact (rel <= 1e-10) on all rungs")
    reading = ("POSITIVE BUDGET: eigmin(W_inf) > 0 on every pole-killed rung -- the "
               "archimedean defect is a positive coordinate; gauge-cone form holds"
               if min(winf_mins) > 0 else
               "SIGNED DEFECT: eigmin(W_inf) <= 0 on some rung -- record honestly")
    print(f"   reading: {reading} (min over rungs = {min(winf_mins):+.4e})")

    # ---- H5: Bochner / moment cone + properness --------------------------
    print("\nH5: Bochner image (moment cone) + properness aperture (200 tests)")
    ntest = 200
    toep_viol, ratios = 0.0, []
    places = [p for p in (2, 3, 5, 7) if p in tw]
    for _ in range(ntest):
        y = Q @ rng.standard_normal(dimQ)
        y /= np.linalg.norm(y)
        c0 = smp.autocorr(y, 0.0)
        norm2 = 0.0
        for p, n_p in tw.items():
            logp = math.log(p)
            cks = [smp.autocorr(y, k * logp) for k in range(1, n_p + 1)]
            norm2 += logp * float(np.sum(np.square(cks)))
            if p in places:
                seq = np.array([c0] + cks)
                Tm = np.array([[seq[abs(i - j)] for j in range(len(seq))]
                               for i in range(len(seq))])
                toep_viol = max(toep_viol, -float(np.linalg.eigvalsh(Tm)[0]) / c0)
        ratios.append(math.sqrt(norm2) / c0)
    bound = math.sqrt(psi_window)
    gate("H5a Toeplitz PSD (Herglotz image)", toep_viol <= 1e-8,
         f"worst -eigmin/c0 = {toep_viol:.2e} over {ntest} tests x places {places}")
    gate("H5b properness", max(ratios) <= bound,
         f"||T(g)||_-M / c0: max {max(ratios):.3f}, median {float(np.median(ratios)):.3f} "
         f"vs theorem bound sqrt(psi) = {bound:.3f} (measured aperture is the content)")

    # ---- H6: carrier guard (decisive gate rerun on DH) -------------------
    print("\nH6: carrier guard -- the dictionary on DH")
    coeffs_z = coefficient_table("zeta", max_n)
    coeffs_dh = coefficient_table("DH", max_n)
    worst_z = 0.0
    for p, n_p in tw.items():
        for k in range(1, n_p + 1):
            m = p ** k
            if m <= max_n:
                worst_z = max(worst_z, abs(coeffs_z[m - 1] / math.log(p) - 1.0))
    pp = set()
    for p in tw:
        k, m = 1, p
        while m <= max_n:
            pp.add(m)
            k += 1
            m = p ** k
    nneg = sum(1 for m in range(2, max_n + 1)
               if abs(coeffs_dh[m - 1]) > 1e-12 and coeffs_dh[m - 1] < 0
               and math.log(m) < GMAX)
    nnonpp = sum(1 for m in range(2, max_n + 1)
                 if abs(coeffs_dh[m - 1]) > 1e-12 and m not in pp
                 and math.log(m) < GMAX)
    gate("H6a zeta: Lambda(p^k) = -<d_k,d_k> exactly", worst_z <= 1e-12,
         f"max |coeff(p^k)/log p - 1| = {worst_z:.2e}: Theta is the pure KMS-1/2 "
         f"geometric series, zero per-atom retuning")
    gate("H6b DH: dictionary unformable", nneg > 0 and nnonpp > 0,
         f"DH atoms in window: {nneg} with NEGATIVE weight (Lambda = -<d,d> >= 0 violated), "
         f"{nnonpp} at non-prime-powers (no tower address). Epstein: MAX face itself "
         f"carrier-blind (AA N9, banked); ALL discrimination lives in T")

    # ---- H7: F1 fork (zeros, COMPARISON ONLY) -----------------------------
    print("\nH7: F1 fork -- rearranged form vs zero-side image (COMPARISON ONLY, K=3000)")
    Mz = zero_gram(lad.centers, HW, K=3000)
    MR = margin_at(lad, "zeta", GMAX)
    cands, zsides = [], []
    for _ in range(30):
        y = Q @ rng.standard_normal(dimQ)
        y /= np.linalg.norm(y)
        cands.append(float(y @ MR @ y))
        zsides.append(float(y @ Mz @ y))
    fc = fork_compare(np.array(cands), np.array(zsides))
    gate("H7 F1 verdict = EF-DERIVED", fc["verdict"].startswith("EF-DERIVED"),
         f"rel={fc['rel']:.2e}, cos={fc['cos']:.6f}: the factorization is the explicit "
         f"formula in lattice coordinates (pre-registered honesty)")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 96)
    nfail = sum(1 for _, ok, _ in GATES if not ok)
    if nfail == 0:
        print("VERDICT (pre-registered): fork (b) with an EXACT sub-factorization --")
        print("  P_R(g) = -sum_p <T_p(g), Theta_p>_{(log p)MAX}  (defect 0, Theorem HH.1),")
        print("  Q(g)   = W_inf(g) + sum_p <T_p(g), Theta_p>_M:")
        print("  the defect R(g) = W_inf(g) IS the archimedean supply (doc 31 exit B);")
        print("  the task-card prediction R = zero-term is REFUTED (the zero side is the")
        print("  WHOLE form, doc-09 closure); T(class) lands in the MOMENT CONE inside the")
        print("  spacelike boundary of the face -- the Perron direction is IDLE: positivity")
        print("  must be supplied at the one slot with no comb, the archimedean place.")
        print("ALL PASS")
        return 0
    print(f"{nfail} GATE(S) FAILED -- fail-closed: fork (c) territory, see table")
    return 1


if __name__ == "__main__":
    sys.exit(main())
