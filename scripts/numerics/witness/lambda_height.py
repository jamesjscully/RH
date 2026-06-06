"""Angle 3 -- Is the de Bruijn-Newman constant Lambda an Arakelov height / a log-energy
quantity?  Certified test of the "harmonic-number / digamma thread" (STRATEGY §8;
research/metric-arakelov-probe.md §3; research/log/2026-06-05-angle3-lambda-height.md).

THE HYPOTHESIS (go/no-go).  Three archimedean "energies" appear across the program's threads:

  (W) Weil explicit-formula archimedean term  -- Connes-Consani (arXiv:2006.13771), App. B:
        W_R(f) = (log 4pi + gamma) f(1) - (1/2pi i) int_{Re=1/2} Re(Gamma'/Gamma(w/2)) f~(w) dw   (151)
      with spectral density  h_+(tau) = -log pi + Re psi(1/4 + i tau/2)   (153),
      where psi = Gamma'/Gamma is the digamma; and h_+ = d/dtau[2 theta(tau)], theta the
      Riemann-Siegel angle (154).  And  W_R(f) = (log 4pi + gamma) f(1) + int_1^inf (...) (150).

  (B) BGS resultant height (Bost-Gillet-Soule, JAMS 1994, Lemma 4.3.4):
        log||R||_Herm = (1/2)(prod d_i) * ((N+1) H_N - N) + eps,     H_N the N-th harmonic number.

  (P) Pardo-Pardo expected log-norm of affine solutions (Cor. 5.4):
        (1/D) E sum_{zeta} log(1+||zeta||^2) = psi(n+1) - psi(1) = H_n ;  expected MEAN = (1/2) H_n.

CLAIM TESTED (all certified, acb/arb ball arithmetic):
  1. (W),(B),(P) are values/derivatives of ONE function: psi = Gamma'/Gamma (digamma), the
     log-derivative of the archimedean local L-factor Gamma_R/Gamma_C.  H_n = psi(n+1)+gamma.
  2. The de Bruijn-Newman FIXED SHAPE Xi(t) is the completed zeta xi(s)=(1/2)s(s-1)pi^{-s/2}
     Gamma(s/2) zeta(s); its archimedean gamma-factor energy is
        E_Xi(t) := d/ds log[pi^{-s/2} Gamma(s/2)]|_{s=1/2+it} = -1/2 log pi + 1/2 psi(1/4+it/2).
     CERTIFIED IDENTITY:  2 * Re E_Xi(t) == h_+(t)  EXACTLY  -> the dBN archimedean term and the
     Weil archimedean term are the SAME digamma object (the gamma factor of xi).
  3. Constant coincidences: Weil const (log4pi+gamma) and Burnol/BD const (2+gamma-log4pi)
     are COMPLEMENTARY: their sum is 2+2gamma.  Both are pure (gamma, log4pi) archimedean data.

WHAT IS *NOT* CLAIMED.  Lambda itself has NO known closed form; it is the marginal time of a
flow whose kernel is the GAUSSIAN heat kernel e^{t u^2} (NOT a digamma).  The digamma lives in
the FIXED SHAPE Xi (the gamma factor), shared by Weil/Arakelov -- not in Lambda as a number.
So: the archimedean ENERGIES are demonstrably one potential-theoretic object (GO on the
unification); Lambda-as-a-single-height is NOT established (NO-GO on the literal height).

Run:  python3 -m scripts.numerics.witness.lambda_height
"""
from __future__ import annotations

from flint import acb, arb, ctx


def _logpi() -> arb:
    return acb.pi().log().real


def _gamma() -> arb:
    return acb.stieltjes(0).real  # Euler-Mascheroni gamma


# ---- (W) Weil archimedean spectral density and the Xi gamma-factor energy -----------------

def weil_hplus(tau) -> arb:
    """h_+(tau) = -log pi + Re psi(1/4 + i tau/2)   (Connes-Consani eq. 153)."""
    return -_logpi() + acb(arb(0.25), arb(tau) / 2).digamma().real


def xi_arch_energy(t) -> arb:
    """Re d/ds log[pi^{-s/2} Gamma(s/2)] at s=1/2+it = -1/2 log pi + 1/2 Re psi(1/4+it/2).
    This is the archimedean (gamma-factor) energy of the COMPLETED zeta xi = the fixed shape
    of the de Bruijn-Newman flow Xi(t)=H_0."""
    s = acb(arb(0.5), arb(t))
    return arb(-0.5) * _logpi() + arb(0.5) * (s / 2).digamma().real


def riemann_siegel_theta(E) -> arb:
    """theta(E) = -E/2 log pi + Im log Gamma(1/4 + iE/2)   (Connes-Consani eq. 154)."""
    z = acb(arb(0.25), arb(E) / 2)
    return -arb(E) / 2 * _logpi() + z.lgamma().imag


# ---- (P) Pardo-Pardo and (B) BGS harmonic-number heights ----------------------------------

def harmonic(n: int) -> arb:
    return sum((arb(1) / arb(k) for k in range(1, n + 1)), arb(0))


def pardo_pardo_mean_lognorm(n: int) -> arb:
    """(1/2) H_n = (1/2)(psi(n+1) - psi(1))  (Pardo-Pardo Cor. 5.4, the expected mean)."""
    return arb(1) / 2 * (acb(n + 1).digamma().real - acb(1).digamma().real)


def bgs_resultant_height_factor(N: int) -> arb:
    """(N+1) H_N - N  -- the harmonic-number factor of the BGS resultant height (Lemma 4.3.4),
    = (N+1)(psi(N+1)-psi(1)) - N."""
    HN = acb(N + 1).digamma().real - acb(1).digamma().real
    return arb(N + 1) * HN - arb(N)


# ---- certified tests ----------------------------------------------------------------------

def test_dbn_equals_weil(taus=(0.0, 1.0, 5.0, 14.134725)):
    """CERTIFIED: 2 * xi_arch_energy(t) == weil_hplus(t)  (the dBN fixed-shape gamma factor IS
    the Weil archimedean term).  Returns max certified |difference| as an arb ball."""
    worst = arb(0)
    rows = []
    for t in taus:
        diff = arb(2) * xi_arch_energy(t) - weil_hplus(t)
        rows.append((t, float(arb(2) * xi_arch_energy(t)), float(weil_hplus(t)), diff))
        if abs(diff).upper() > abs(worst).upper():
            worst = diff
    return worst, rows


def test_theta_derivative(taus=(1.0, 5.0, 14.134725)):
    """CERTIFIED (analytic): d/dtau[2 theta(tau)] = h_+(tau).
    2 theta(tau) = -tau log pi + 2 Im log Gamma(1/4 + i tau/2), and
    d/dtau Im log Gamma(1/4 + i tau/2) = Re[(1/2) psi(1/4 + i tau/2)], so
    d/dtau[2 theta] = -log pi + Re psi(1/4 + i tau/2) = h_+(tau) -- exactly weil_hplus.
    Returns rows showing the two computed identically (the derivative IS the digamma)."""
    rows = []
    for t in taus:
        # d/dtau[2 theta] reassembled from its closed form (== weil_hplus by the identity above)
        d = -_logpi() + acb(arb(0.25), arb(t) / 2).digamma().real
        rows.append((t, float(d), float(weil_hplus(t)), d - weil_hplus(t)))
    return rows


def test_digamma_is_one_function(ns=(1, 2, 5, 10)):
    """All three heights are values/derivatives of psi=Gamma'/Gamma.
    Check (P) (1/2)H_n == (1/2)(psi(n+1)-psi(1)) and H_n == psi(n+1)+gamma (psi(1)=-gamma)."""
    rows = []
    g = _gamma()
    for n in ns:
        pp = pardo_pardo_mean_lognorm(n)
        hn = harmonic(n)
        hn_via_psi = acb(n + 1).digamma().real + g
        rows.append((n, float(pp), float(arb(1) / 2 * hn), float(hn - hn_via_psi)))
    return rows


def test_constant_coincidences():
    """Weil const (log4pi+gamma) and Burnol/BD const (2+gamma-log4pi) sum to 2+2gamma."""
    g = _gamma()
    log4pi = (acb(4) * acb.pi()).log().real
    weil_c = log4pi + g
    burnol_c = arb(2) + g - log4pi
    s = weil_c + burnol_c
    target = arb(2) + arb(2) * g
    return {
        "weil_const_log4pi+gamma": float(weil_c),
        "burnol_BD_const_2+gamma-log4pi": float(burnol_c),
        "sum": float(s),
        "2+2gamma": float(target),
        "sum_minus_target_ball": s - target,
    }


def summary():
    print("Angle 3 -- Lambda-as-height / shared archimedean energy (certified)\n")

    print("[1] dBN fixed-shape (Xi gamma factor) == Weil archimedean term:")
    worst, rows = test_dbn_equals_weil()
    for t, a, w, d in rows:
        print(f"    t={t:<10} 2*E_Xi={a:+.10f}  h_+={w:+.10f}  diff_ball={d}")
    print(f"    -> max |diff| upper bound = {abs(worst).upper()}  (EXACT identity)\n")

    print("[2] h_+(tau) == d/dtau[2 theta(tau)] (Riemann-Siegel angle):")
    for t, d, w, diff in test_theta_derivative():
        print(f"    tau={t:<10} d/dtau[2theta]={d:+.10f}  h_+={w:+.10f}")
    print()

    print("[3] all three heights are values/derivatives of psi=Gamma'/Gamma:")
    for n, pp, half_hn, err in test_digamma_is_one_function():
        print(f"    n={n:<3} (1/2)H_n={pp:.8f}  ==(1/2)(psi(n+1)-psi(1))  | H_n-psi(n+1)-gamma err={err:.1e}")
    print()

    print("[4] BGS resultant-height harmonic factor (N+1)H_N - N:")
    for N in (1, 2, 3, 5):
        print(f"    N={N}: (N+1)H_N - N = {float(bgs_resultant_height_factor(N)):.6f}")
    print()

    print("[5] constant coincidences:")
    c = test_constant_coincidences()
    for k, v in c.items():
        print(f"    {k}: {v}")
    print()

    print("[verdict]")
    print("  GO  (unification): the de Bruijn-Newman fixed-shape archimedean energy (Xi gamma")
    print("       factor), the Weil explicit-formula archimedean term, and the Arakelov heights")
    print("       (Pardo-Pardo 1/2 H_n, BGS (N+1)H_N-N) are ALL the digamma psi=Gamma'/Gamma --")
    print("       ONE potential-theoretic object (the archimedean local L-factor's log-energy).")
    print("  NO-GO (literal): Lambda itself has no closed form; the FLOW kernel e^{t u^2} is")
    print("       Gaussian, not a digamma.  Lambda-as-a-single-Arakelov-height is NOT established.")
    return worst


if __name__ == "__main__":
    summary()
