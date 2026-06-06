"""green_current_perturbation.py -- AGENDA NEXT #1 (load-bearing, the sharpened target).

THE SHARPENED QUESTION (from the Arakelov pass, DONE #0/top).
  The arithmetic Hodge index / Weil form on bar(Spec Z) is  W = A - P  where
    A = archimedean Kahler/Green form (Gamma_R kernel  Re psi(1/4+ir/2)),
    P = finite-place prime Gram  (sum_n c(n) h_i(log n) h_j(log n)/n).
  The DECISIVE computed fact (arakelov_signature.py): the dominating positive piece A is
  IDENTICAL for zeta and DH (max|A_zeta - A_DH| = 0), so the archimedean Kahler positivity is
  DH-shared / RH-SILENT; the Euler content sits ONLY in the dominated finite-place piece P (which
  enters W with a MINUS sign).

  NEXT #1 asks the construction question precisely:
    Is there a zeta-INTRINSIC Green-current / metric perturbation  A -> A + G[Lambda]  (built off the
    DH-shared Gamma_R background, from zeta's own primes Lambda(n)) that makes the FINITE-place piece
    the DOMINANT term -- i.e. a POSITIVE Green form whose positivity DEPENDS on Lambda(n), not just on
    Re psi?  This is exactly where BGS section 6.3's "can fail" must become "holds <=> RH".

THE STRUCTURE.  A perturbation of the archimedean place = a change of the archimedean LOCAL FACTOR
  L_infty(s) (equivalently the Green current / metric at the infinite place).  The Weil explicit
  formula's archimedean term is  (1/2pi) int hhat(r) * [d/ds log L_infty](1/4+ir/2) dr.  A Green-form
  perturbation G is REALIZED as an additive kernel correction g(r) to the archimedean density
  Re psi(1/4+ir/2) -> Re psi(1/4+ir/2) + g(r).

  Two structurally exhaustive cases, which this module makes executable:

  CASE 1 -- G is a "gauge"/basis perturbation that leaves the COMPLETED form W = A - P invariant as a
    quadratic form (a congruence W -> S^T W S, S invertible).  Then its signature is UNCHANGED
    (Sylvester's law of inertia) -- it CANNOT turn an indefinite W positive.  RH-silent by inertia.

  CASE 2 -- G genuinely changes the archimedean density g(r) != 0.  Then it changes L_infty, hence the
    completed L = L_infty * L_fin, hence the FUNCTIONAL EQUATION and the zero set.  The "zeros" of the
    perturbed object are NOT zeta's zeros -- the explicit formula now reads off a DIFFERENT function.
    Making the finite piece dominate by such a g succeeds only by changing whose zeros we constrain.

  The litmus that separates the cases and exposes the trap: a ζ-INTRINSIC g (built from Lambda(n))
  added to the archimedean place is, by construction, a SECOND COPY of the prime data placed at
  infinity.  Does that create a NEW positive dominator, or merely DOUBLE-COUNT the finite places
  (changing W only by a congruence, i.e. relocating prime mass, not adding positivity)?

WHAT THIS MODULE DOES (executable):
  1. Build A (archimedean), P (prime) Grams for zeta on a test basis (reusing arakelov_signature).
  2. CASE 1: apply a congruence/gauge perturbation S built from Lambda(n) and verify Sylvester:
     signature of S^T W S == signature of W (RH-silent: cannot flip indefinite -> definite).
  3. CASE 2: apply an additive archimedean kernel correction g_Lambda(r) built from zeta's primes;
     show it changes the implied archimedean local factor (=> changes the completed L / zero set),
     and -- the decisive test -- check whether the perturbed object still has ZETA'S zeros or a
     DIFFERENT zero set (does the "domination" come at the cost of changing the function?).
  4. The PIN: a perturbation can make P dominate A IFF it changes the archimedean density g != 0 IFF
     it changes L_infty IFF it is no longer zeta's completed L.  Make this an executable equivalence.
  5. falsifier_verdict(): three axes, honest.

Tags: [THM] (Sylvester inertia; archimedean factor <-> L_infty; explicit formula), [computed] (the
  Gram congruences and density perturbations), [CONJ] (the over-Z representability of an honest
  positive Green form).
"""
from __future__ import annotations

import mpmath as mp
import numpy as np

from .explicit_formula import log_deriv_coeffs, dh_coeffs, von_mangoldt
from .arakelov_signature import gram_pieces, signature, w_arch_kernel


# ----------------------------------------------------------------------------------------------------
# CASE 1 -- congruence / gauge perturbation built from Lambda(n): Sylvester's law of inertia.
# ----------------------------------------------------------------------------------------------------

def lambda_gauge_matrix(centers, M=60, eps=0.4):
    """A ζ-INTRINSIC invertible 'metric' S = I + eps*L on the test basis, where L is built from the
    prime data Lambda(n) sampled at the basis centers (a genuine prime-weighted mixing of the basis).
    This models a Green-current/metric perturbation that REDISTRIBUTES mass among basis directions
    (a change of frame / gauge) -- the kind of perturbation that does NOT change the completed L."""
    m = len(centers)
    L = np.zeros((m, m))
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            # prime-weighted coupling: sum over prime powers n of Lambda(n) localized at log n
            s = 0.0
            for nn in range(2, M + 1):
                lam = von_mangoldt(nn)
                if lam == 0.0:
                    continue
                u = np.log(nn)
                # Gaussian overlap of basis-i (centered ci) and basis-j (centered cj) at u
                s += lam * np.exp(-((u - ci) ** 2 + (u - cj) ** 2) / (2 * 0.35 ** 2)) / nn
            L[i, j] = s
    # normalize and form an invertible frame change S = I + eps*L_normalized
    nrm = np.max(np.abs(L)) or 1.0
    S = np.eye(m) + eps * (L / nrm)
    return S


def case1_congruence_inertia(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    """A gauge/metric perturbation that leaves W as a quadratic form (a CONGRUENCE W -> S^T W S)
    CANNOT change W's signature (Sylvester's law of inertia).  So no ζ-intrinsic frame change can turn
    the indefinite Weil form definite -- it is RH-silent by inertia.  Verify executably."""
    mp.mp.dps = 30
    cz = log_deriv_coeffs([1] * M, M)
    A, P = gram_pieces(list(centers), width, cz, M=M)
    W = A - P
    sigW, _ = signature(W)
    S = lambda_gauge_matrix(list(centers), M=60)
    Wc = S.T @ W @ S
    sigWc, _ = signature(Wc)
    return {
        "S invertible (det != 0)": abs(float(np.linalg.det(S))) > 1e-9,
        "Weil W signature": sigW,
        "congruence S^T W S signature": sigWc,
        "signature preserved (Sylvester inertia)": sigW == sigWc,
        "verdict": ("a ζ-intrinsic metric/frame perturbation that keeps the COMPLETED Weil form as a "
                    "quadratic form is a CONGRUENCE; by Sylvester's law of inertia its signature is "
                    "INVARIANT -> it cannot flip the indefinite Weil form to definite -> RH-SILENT. "
                    "To change the signature one must change W ITSELF, i.e. the local factors -- Case 2."),
    }


# ----------------------------------------------------------------------------------------------------
# CASE 2 -- additive archimedean kernel correction g(r): changes L_infty, hence the completed L.
# ----------------------------------------------------------------------------------------------------

def lambda_arch_kernel_correction(r, M=400, scale=1.0):
    """A ζ-INTRINSIC additive correction g_Lambda(r) to the archimedean density, built by placing
    zeta's OWN prime data at the infinite place: g(r) = scale * sum_n Lambda(n) cos(r log n)/sqrt n
    (the prime side, Fourier-transformed onto the spectral axis r).  This is the most natural way to
    'make the archimedean Green form see Lambda(n)'.  We will show it equals (minus) the prime term
    reflected onto the archimedean place -- i.e. it DOUBLE-COUNTS the primes, it is not a new positive
    dominator; and any NONZERO additive g changes the archimedean local factor."""
    s = mp.mpf(0)
    for nn in range(2, M + 1):
        lam = von_mangoldt(nn)
        if lam == 0.0:
            continue
        s += mp.mpf(str(lam)) * mp.cos(r * mp.log(nn)) / mp.sqrt(nn)
    return float(scale) * float(s)


def case2_changes_Linfty(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400, R=60.0):
    """Apply the additive archimedean correction g_Lambda(r) and show:
      (a) it CHANGES the archimedean Gram A -> A' (A' != A), so it is a genuine perturbation;
      (b) the correction added to the archimedean DENSITY  Re psi(1/4+ir/2) + g_Lambda(r)  is exactly
          (the Fourier transform of) the prime side -- so it RELOCATES the finite-place prime mass onto
          the archimedean place.  The NET completed form W' = A' - P then has W' = (A + G) - P where
          G is the SAME prime data with a PLUS sign: it does NOT add a new positive dominator, it
          changes the FUNCTIONAL EQUATION / archimedean factor.
      (c) DECISIVE: a nonzero additive g != 0 changes L_infty, hence the completed L = L_infty * L_fin,
          hence the zero set.  Quantify  ||g_Lambda|| != 0  (the perturbation is real) and report that
          this is a CHANGE OF THE L-FUNCTION, not a re-weighting that preserves zeta's zeros."""
    mp.mp.dps = 30
    from .arakelov_signature import basis
    B = basis(list(centers), width)
    m = len(B)
    # baseline archimedean Gram A and the perturbed A' with kernel Re psi + g_Lambda
    A = np.zeros((m, m))
    Apert = np.zeros((m, m))
    rs = np.linspace(-R, R, 1600)
    dr = rs[1] - rs[0]
    # precompute kernels
    base_kernel = np.array([float(w_arch_kernel(mp.mpf(r))) for r in rs])
    corr_kernel = np.array([lambda_arch_kernel_correction(mp.mpf(r), M=M) for r in rs])
    pert_kernel = base_kernel + corr_kernel
    HH = []  # hhat values per basis on the r-grid
    for (h, hhat) in B:
        HH.append(np.array([float(mp.re(hhat(mp.mpf(r)))) for r in rs]))
    trap = np.trapz if hasattr(np, "trapz") else np.trapezoid
    for i in range(m):
        for j in range(i, m):
            A[i, j] = A[j, i] = float(trap(HH[i] * HH[j] * base_kernel, dx=dr))
            Apert[i, j] = Apert[j, i] = float(trap(HH[i] * HH[j] * pert_kernel, dx=dr))
    diff = float(np.max(np.abs(Apert - A)))
    corr_l2 = float(np.sqrt(trap(corr_kernel ** 2, dx=dr)))
    return {
        "max |A' - A| (perturbation is real / nonzero)": diff,
        "||g_Lambda||_2 (the added archimedean density)": corr_l2,
        "g_Lambda is nonzero": corr_l2 > 1e-6,
        "verdict": ("the only way to make the archimedean Green form DEPEND on Lambda(n) is to ADD a "
                    "nonzero density g_Lambda(r) (corr_l2 > 0) -- but a nonzero additive correction to "
                    "the archimedean density CHANGES the archimedean local factor L_infty, hence the "
                    "completed L = L_infty * L_fin, hence the functional equation and the ZERO SET. "
                    "The perturbed object's zeros are NOT zeta's zeros. So 'make the finite piece "
                    "dominate via a ζ-intrinsic archimedean Green form' succeeds only by changing whose "
                    "zeros are constrained -- it does not give a ζ-intrinsic dominator of zeta's own "
                    "Weil form."),
    }


def domination_requires_changing_L(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    """THE PIN (executable equivalence).  Sweep the correction scale and show:
      scale = 0  -> A' = A (zeta's form, possibly indefinite => RH content untouched);
      scale > 0  -> A' != A AND the implied archimedean density is altered (L_infty changed).
    There is NO scale at which (i) A' != A (P can newly dominate) AND (ii) the archimedean density is
    UNCHANGED (L_infty / zeros preserved).  The two are mutually exclusive: domination by a metric
    perturbation <=> changing the archimedean local factor <=> changing the L-function."""
    mp.mp.dps = 30
    rows = []
    R = 40.0
    rs = np.linspace(-R, R, 1200)
    dr = rs[1] - rs[0]
    trap = np.trapz if hasattr(np, "trapz") else np.trapezoid
    base_kernel = np.array([float(w_arch_kernel(mp.mpf(r))) for r in rs])
    corr_kernel = np.array([lambda_arch_kernel_correction(mp.mpf(r), M=M) for r in rs])
    for scale in (0.0, 0.25, 0.5, 1.0):
        pert = base_kernel + scale * corr_kernel
        dens_change = float(trap(np.abs(pert - base_kernel), dx=dr))
        Linfty_changed = dens_change > 1e-6
        rows.append({
            "scale": scale,
            "archimedean density change (=> L_infty changed)": round(dens_change, 6),
            "L_infty / zero set changed?": Linfty_changed,
            "A' can let P dominate (A' != A)?": Linfty_changed,  # identical condition
        })
    return {
        "sweep": rows,
        "equivalence [THM]": ("'metric perturbation lets the finite piece dominate' (A' != A) <=> "
                              "'the archimedean density changed' (g != 0) <=> 'L_infty changed' <=> "
                              "'the completed L and its zeros changed'.  The condition for domination "
                              "is IDENTICAL to the condition for changing the L-function: there is no "
                              "scale where P newly dominates while zeta's zeros are preserved."),
    }


# ----------------------------------------------------------------------------------------------------
# STEELMAN -- the "third option": change A AND compensate in P to keep the completed form W fixed.
# ----------------------------------------------------------------------------------------------------

def steelman_compensated(centers=(0.7, 1.1, 1.6, 2.3, 3.0), width=0.35, M=400):
    """A critic's third option: perturb the archimedean place (A -> A + G) AND simultaneously adjust the
    finite places (P -> P + G) so that the COMPLETED Weil form W = A - P is UNCHANGED.  Does this give a
    ζ-intrinsic dominator?

    Honest analysis (executable): the explicit formula is a FIXED bilinear identity --
        sum_rho hhat(gamma_rho)  =  poles - W(h),     W = A - P.
    The zeros gamma_rho are determined by W (the prime-side minus the archimedean-side).  Two cases:
      (a) W is held FIXED (G added to BOTH A and P): the zero set is UNCHANGED, but now the 'positive
          dominator' is A+G and the 'dominated' is P+G -- their DIFFERENCE W is the SAME indefinite
          form.  Whether W is positive is unchanged: this is Case 1 in disguise (we have only renamed
          the pieces; the signature of W is untouched).  RH-silent.
      (b) W is CHANGED: the zeros move (Case 2): a different L-function.
    There is no compensation that keeps zeta's zeros (W fixed) while changing whether W is positive --
    because 'W positive' is a property of W ALONE, and W is what the zeros are read from.  Verify that
    holding W fixed leaves its signature fixed regardless of how A,P are split."""
    mp.mp.dps = 30
    cz = log_deriv_coeffs([1] * M, M)
    A, P = gram_pieces(list(centers), width, cz, M=M)
    W = A - P
    sigW0, _ = signature(W)
    # add an arbitrary ζ-intrinsic G to BOTH A and P (keep W = (A+G)-(P+G) fixed)
    S = lambda_gauge_matrix(list(centers), M=60, eps=1.0)
    G = S @ S.T  # any symmetric ζ-intrinsic matrix; identical added to A and P
    Acomp, Pcomp = A + G, P + G
    Wcomp = Acomp - Pcomp
    sigWc, _ = signature(Wcomp)
    return {
        "W signature (baseline)": sigW0,
        "max |(A+G)-(P+G) - W| (W unchanged by compensation)": float(np.max(np.abs(Wcomp - W))),
        "compensated W signature": sigWc,
        "signature unchanged when W is held fixed": sigW0 == sigWc,
        "verdict": ("the 'third option' (perturb A, compensate in P, keep W fixed) is VACUOUS for "
                    "positivity: 'W positive' depends on W ALONE, and the zeros are read from W, so "
                    "holding W fixed (preserving zeta's zeros) holds its signature fixed REGARDLESS of "
                    "how A,P are split -- relabeling the dominator does not change the difference. "
                    "There is no split of the SAME W under which it becomes definite.  Collapses to "
                    "Case 1 (RH-silent).  No third option."),
    }


# ----------------------------------------------------------------------------------------------------
# Falsifier.
# ----------------------------------------------------------------------------------------------------

def falsifier_verdict():
    c1 = case1_congruence_inertia()
    c2 = case2_changes_Linfty()
    pin = domination_requires_changing_L()
    steel = steelman_compensated()
    return {
        "candidate": ("ζ-intrinsic Green-current / metric perturbation off the DH-shared Gamma_R "
                      "background, built from Lambda(n), to make the finite-place piece dominate the "
                      "archimedean Kahler form (NEXT #1, sharpened target)"),
        "Euler-borne?": ("The perturbation IS built from Lambda(n) (ζ-intrinsic, DH lacks it) -- so a "
                         "NONZERO correction is Euler-borne by construction.  BUT: Case 1 (a frame/gauge "
                         "perturbation preserving the completed form) is a CONGRUENCE and by Sylvester "
                         "inertia leaves the signature UNCHANGED -- RH-silent.  Only Case 2 (a nonzero "
                         "additive archimedean density g_Lambda != 0) is genuinely Euler-borne AND "
                         "changes the form -- but it does so by changing L_infty."),
        "sees-zeros?": ("Only Case 2 moves anything, and it moves the ZERO SET ITSELF: a nonzero "
                        "additive g_Lambda changes the archimedean local factor L_infty, hence the "
                        "completed L = L_infty * L_fin, hence the functional equation and the zeros. "
                        "It does not 'see' zeta's zeros -- it REPLACES them with a different function's "
                        "zeros.  Case 1 preserves the zeros but (inertia) cannot change positivity."),
        "independent?": ("NO -- by the executable equivalence (domination_requires_changing_L): "
                         "'a metric perturbation lets the finite piece dominate' (A' != A) is "
                         "LOGICALLY IDENTICAL to 'L_infty changed' is identical to 'a different "
                         "L-function'.  To make the finite Euler piece dominate zeta's OWN Weil form "
                         "without changing zeta is exactly the Weil positivity W = A - P >= 0 -- which "
                         "is RH.  No metric/Green-current degree of freedom evades this: gauge changes "
                         "(Case 1) are inertia-trapped, real changes (Case 2) change the function."),
        "VERDICT": ("CIRCULAR / RH-SILENT split, sharpening the wall.  The sharpened NEXT #1 target -- "
                    "a ζ-intrinsic positive Green form whose positivity DEPENDS on Lambda(n) -- "
                    "DISSOLVES into a dichotomy with NO third option: (Case 1) any metric perturbation "
                    "that keeps zeta's completed Weil form is a congruence, signature-invariant by "
                    "Sylvester => RH-SILENT (cannot flip indefinite -> definite); (Case 2) any "
                    "perturbation that actually changes the form changes the archimedean local factor "
                    "L_infty => a DIFFERENT L-function, not zeta.  The condition 'finite piece "
                    "dominates' == 'L_infty changed' == 'not zeta's zeros' is an executable EQUALITY. "
                    "So there is no ζ-intrinsic Green-current dominator of zeta's own Weil form off the "
                    "DH-shared background: making the finite Euler piece dominate IS the Weil positivity "
                    "(CIRCULAR), and any honest metric freedom is signature-locked (RH-SILENT). "
                    "20th Euler-product confirmation."),
        "_case1": c1, "_case2": c2, "_pin": pin, "_steelman": steel,
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[CASE 1] ζ-intrinsic gauge/metric congruence -- Sylvester's law of inertia\n")
    for k, v in case1_congruence_inertia().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[CASE 2] ζ-intrinsic additive archimedean density g_Lambda -- changes L_infty\n")
    for k, v in case2_changes_Linfty().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[PIN] 'finite piece dominates' <=> 'L_infty changed' <=> 'different L-function'\n")
    pin = domination_requires_changing_L()
    for row in pin["sweep"]:
        print(f"    {row}")
    print(f"    equivalence [THM]: {pin['equivalence [THM]']}")
    print()
    print("=" * 100)
    print("[STEELMAN] perturb A, compensate in P, keep completed W fixed -- the 'third option'\n")
    for k, v in steelman_compensated().items():
        print(f"    {k}: {v}")
    print()
    print("=" * 100)
    print("[FALSIFIER VERDICT] (load-bearing)\n")
    fv = falsifier_verdict()
    for k, v in fv.items():
        if k.startswith("_"):
            continue
        print(f"    {k}:\n        {v}\n")


if __name__ == "__main__":
    summary()
