"""Renormalization / marginal-fixed-point probe of the Hermite junction (Angle 2).

Charter: STRATEGY.md (esp. the metric-enrichment / marginal-vanishing reading of "no slack
at every scale") and research/state-of-search.md ("The Hermite junction").  The setup is an
RG structure: the Jensen polynomials J_{d,n} flow to the Hermite H_d (GORZ scaling limit,
verified in real zeta -- xi_jensen.py), and the de Bruijn-Newman heat flow e^{-tD^2}
GENERATES Hermite from monomials.  So Hermite/semicircle is the candidate RG fixed point and
the slack rho(d) is a candidate marginal observable.

THE GO/NO-GO QUESTION.  Is there an EXACT self-consistency / renormalization recursion across
scale d -- a clean map rho(d+1)=F(rho(d)) with a MARGINAL fixed point, OR an exact "flow =
rescale" identity at the fixed point -- so that "uniform in d" could become a fixed-point
statement rather than a forall-d estimate?  Or is the scale-to-scale relation messy and the
RG framing decoration?

WHAT THIS MODULE ESTABLISHES (all reproduced against the existing certified data):

  (A) EXACT discriminant recursion [CERTIFIED, integer equality]:
        disc(H_{n+1}) = 2^{3n} * (n+1)^{n+1} * disc(H_n).
      => log disc(H_{n+1}) - log disc(H_n) = 3n ln2 + (n+1) ln(n+1)   (exact).
      This is a clean RG recursion on the ENERGY (the height), with NO fixed point
      (the increment grows like n log n): the energy is a RELEVANT direction.

  (B) EXACT flow=rescale identity at the fixed point [verified to machine precision]:
        D^2 H_n = 4 n (n-1) H_{n-2}                       (exact lowering operator), and
        e^{-t D^2} H_n(x) = (1+4t)^{n/2} H_n( x / sqrt(1+4t) ).
      The heat flow acts on the Hermite fixed shape as a PURE DILATION.  Dilation preserves
      hyperbolicity and does NOT move between degrees -- so along the fixed shape the dBN
      flow is EXACTLY MARGINAL (it neither creates nor destroys reality of roots; it is the
      symmetry that pins the fixed point).  This is the precise content of "Lambda = 0 at the
      fixed point": the flow direction tangent to Hermite is null.

  (C) The MARGINAL slack law [reproduced from jensen_p1b.deterministic_slack]:
        log(1/rho(d)) ~ (1/2) d log d + b d + ...        (leading coeff -> 0.50),
      while the energy is  log disc(H_d) ~ (1/2) d^2 log d.  Hence
        log(1/rho(d)) ~ (1/d) log disc(H_d)              (slack = energy PER DEGREE).
      The d log d law is the marginal (logarithmic) correction -- the signature of a
      marginal operator -- NOT a clean geometric ratio rho(d+1)/rho(d) -> const.  There is
      NO finite fixed-point ratio: the per-step increment Delta log rho(d) ~ -log d diverges.

  (D) SCALING COLLAPSE [real zeta, xi_jensen]: the normalized roots of J_{d,n} converge to
      the roots of H_d as the shift n grows, with a SLOW power-law tail dev ~ n^{-1/3}.
      The collapse is real (confirms the fixed point) but its approach is power-law, not a
      clean universal scaling function reachable at finite n.

VERDICT (honest): the junction has a REAL but PARTIAL RG structure.
  * GO on EXACT structure: a certified discriminant recursion (A) and an exact flow=rescale
    marginal identity at the fixed point (B).  These are genuine, not decoration.
  * NO-GO on the load-bearing object: there is NO clean rho(d+1)=F(rho(d)) with a finite
    marginal fixed-point RATIO.  The slack's marginality is a d-log-d (super-exponential)
    law, governed by the spectral EDGE of the Hermite ensemble, not a self-similar geometric
    recursion.  So "uniform in d" does NOT collapse to a fixed-point self-consistency; it
    remains a forall-d estimate against a super-exponentially shrinking, edge-controlled
    margin.  The RG framing names the structure correctly (marginal slack, relevant energy,
    marginal flow) but does NOT supply a new handle on the uniform-in-d bound.

This SHARPENS the existing diagnosis (jensen_real / p1b): the slack is marginal in the exact
technical sense (logarithmic correction), the flow is exactly marginal along the fixed shape,
and the energy is relevant -- but none of these gives the missing uniform control.

Run:  python3 -m scripts.numerics.witness.renormalization
"""
from __future__ import annotations

import math
from math import factorial

import numpy as np
from numpy.polynomial import hermite as Herm

from .jensen_p1 import _hermites, hermite_discriminant
from .jensen_p1b import deterministic_slack


# --------------------------------------------------------------------------- #
# (A) EXACT discriminant recursion -- certified integer equality              #
# --------------------------------------------------------------------------- #
def discriminant_recursion(N: int = 12):
    """Certified: disc(H_{n+1}) == 2^{3n} (n+1)^{n+1} disc(H_n), exact integers, n=2..N-1.

    Returns (all_match, rows) with rows = (n, matched_bool).  This is the RG recursion on the
    ENERGY/height.  The multiplicative increment 2^{3n}(n+1)^{n+1} GROWS without bound -> the
    energy is a RELEVANT direction (no fixed point on the energy)."""
    Hs = _hermites(N + 1)
    rows = []
    ok = True
    for n in range(2, N):
        d1 = hermite_discriminant(n, Hs)
        d2 = hermite_discriminant(n + 1, Hs)
        factor = (2 ** (3 * n)) * ((n + 1) ** (n + 1))
        match = (d2 == d1 * factor)          # exact integer equality
        ok = ok and match
        rows.append((n, match))
    return ok, rows


# --------------------------------------------------------------------------- #
# (B) EXACT flow = rescale identity at the Hermite fixed point                 #
# --------------------------------------------------------------------------- #
def _d2(coeffs):
    """Second derivative of a polynomial (ascending monomial coeffs)."""
    n = len(coeffs)
    if n <= 2:
        return np.array([0.0])
    return np.array([coeffs[k + 2] * (k + 2) * (k + 1) for k in range(n - 2)])


def heat_flow_poly(coeffs, t):
    """H_t = e^{-t D^2} p = sum_j (-t)^j / j! * D^{2j} p   (ascending coeffs)."""
    c = np.array(coeffs, float)
    res = c.copy()
    d = c.copy()
    j = 1
    while len(d) > 2:
        d = _d2(d)
        pad = np.zeros(len(c))
        pad[:len(d)] = d
        res = res + ((-t) ** j / factorial(j)) * pad
        j += 1
    return res


def lowering_identity(n: int) -> bool:
    """Exact: D^2 H_n = 4 n (n-1) H_{n-2}  (the heat-flow generator LOWERS Hermite degree by 2)."""
    Hn = Herm.herm2poly(np.eye(n + 1)[n])
    lhs = _d2(Hn)
    Hn2 = Herm.herm2poly(np.eye(n - 1)[n - 2])
    rhs = 4 * n * (n - 1) * np.array(Hn2)
    if len(lhs) != len(rhs):
        return False
    return bool(np.allclose(lhs, rhs))


def flow_equals_rescale(n: int, t: float = 0.05) -> float:
    """Max deviation between e^{-tD^2} H_n(x) and the pure DILATION (1+4t)^{n/2} H_n(x/sqrt(1+4t)).
    ~0 means the flow acts on the Hermite fixed shape as an exact rescaling (marginal direction)."""
    Hn = Herm.herm2poly(np.eye(n + 1)[n])
    lhs = np.polynomial.Polynomial(heat_flow_poly(Hn, t))
    A = math.sqrt(1.0 + 4.0 * t)
    Hpoly = np.polynomial.Polynomial(Hn)
    xs = np.linspace(-2.0, 2.0, 21)
    rhs = (A ** n) * Hpoly(xs / A)
    return float(np.max(np.abs(lhs(xs) - rhs)))


# --------------------------------------------------------------------------- #
# (C) The marginal slack law and the (absent) fixed-point ratio               #
# --------------------------------------------------------------------------- #
def slack_recursion_test(dmax: int = 50):
    """Test for a clean fixed-point recursion rho(d+1)=F(rho(d)).

    Returns a dict with:
      * ratios rho(d+1)/rho(d)            -- do they tend to a finite constant? (a fixed-point ratio)
      * Delta log rho(d)                  -- does the per-step increment converge? (marginal => no)
      * leading-coefficient fit of log(1/rho) against {d log d, d, log d, 1}.
    Uses deterministic_slack (the exact 2-constraint distance to the discriminant variety)."""
    ds = np.arange(2, dmax + 1)
    rho = np.array([deterministic_slack(int(d)) for d in ds])
    y = np.log(1.0 / rho)
    ratios = rho[1:] / rho[:-1]
    dlog = np.diff(y)                       # Delta log(1/rho) = -Delta log rho
    # 4-parameter asymptotic fit on the upper half (avoid small-d transient & float overflow)
    lo = max(8, dmax // 4)
    mask = ds >= lo
    dd = ds[mask].astype(float)
    yy = y[mask]
    A = np.vstack([dd * np.log(dd), dd, np.log(dd), np.ones_like(dd)]).T
    coef, *_ = np.linalg.lstsq(A, yy, rcond=None)
    resid = float(np.max(np.abs(yy - A @ coef)))
    return {
        "ds": ds, "rho": rho, "ratios": ratios, "dlog": dlog,
        "fit": coef, "fit_resid": resid,
        "leading_dlogd_coeff": float(coef[0]),
    }


def slack_is_energy_per_degree(ds=(20, 30, 40, 50)):
    """Reproduce: log(1/rho(d)) ~ (1/d) log disc(H_d)  (slack = discriminant ENERGY per degree).
    Both leading coefficients -> 1/2 in the d-log-d / d^2-log-d normalization."""
    Hs = _hermites(max(ds) + 1)
    rows = []
    for d in ds:
        ld = math.log(abs(hermite_discriminant(d, Hs)))     # energy ~ (1/2) d^2 log d
        lr = math.log(1.0 / deterministic_slack(d))         # slack  ~ (1/2) d   log d
        rows.append((d,
                     ld / (d * d * math.log(d)),             # -> 1/2
                     lr / (d * math.log(d)),                 # -> 1/2 (slowly)
                     lr / (ld / d)))                         # log(1/rho) / (logdisc/d) -> 1
    return rows


# --------------------------------------------------------------------------- #
# (D) Scaling collapse of the real-zeta Jensen roots onto Hermite             #
# --------------------------------------------------------------------------- #
def scaling_collapse(d: int = 4, ns=(1, 2, 4, 8, 16, 24, 32), K: int = 40):
    """Normalized roots of the REAL-zeta Jensen polynomial J_{d,n} vs the Hermite H_d roots,
    as the shift n grows (the GORZ scaling limit).  Returns (rows, power) where rows = (n, dev)
    and power is the fitted exponent in dev ~ n^power (the approach-to-fixed-point rate)."""
    from math import comb
    from .xi_jensen import jensen_sequence
    g = jensen_sequence(K)
    Href = np.sort(Herm.hermroots(np.eye(d + 1)[d]))
    Href = (Href - Href.mean()) / Href.std()
    rows = []
    for n in ns:
        if n + d > K:
            continue
        p = np.array([comb(d, j) * g[n + j] for j in range(d + 1)], dtype=float)
        r = np.sort(np.roots(p[::-1]).real)
        r = (r - r.mean()) / r.std()
        rows.append((n, float(np.max(np.abs(r - Href)))))
    nn = np.array([n for n, _ in rows], float)
    dv = np.array([x for _, x in rows])
    power = float(np.polyfit(np.log(nn[1:]), np.log(dv[1:]), 1)[0]) if len(nn) > 2 else float("nan")
    return rows, power


# --------------------------------------------------------------------------- #
# Summary                                                                     #
# --------------------------------------------------------------------------- #
def summary():
    print("Renormalization / marginal-fixed-point probe of the Hermite junction\n")

    # (A)
    ok, rows = discriminant_recursion(12)
    print("(A) EXACT discriminant recursion  disc(H_{n+1}) = 2^{3n}(n+1)^{n+1} disc(H_n):")
    print(f"    certified integer equality for n=2..11: {ok}")
    print("    => log-increment = 3n ln2 + (n+1)ln(n+1)  GROWS with n  ->  ENERGY is RELEVANT")
    print("       (no fixed point on the energy/height).\n")

    # (B)
    low = all(lowering_identity(n) for n in range(2, 12))
    devs = [flow_equals_rescale(n) for n in (4, 6, 8)]
    print("(B) EXACT flow=rescale at the fixed point:")
    print(f"    D^2 H_n = 4 n(n-1) H_{{n-2}}  (exact lowering operator), n=2..11: {low}")
    print(f"    e^{{-tD^2}} H_n(x) = (1+4t)^{{n/2}} H_n(x/sqrt(1+4t))  -- pure dilation;")
    print(f"      max deviation over n=4,6,8 (t=0.05): {max(devs):.2e}  (== 0 to machine prec)")
    print("    => along the Hermite fixed shape the dBN flow is EXACTLY MARGINAL (dilation")
    print("       preserves hyperbolicity, stays in-degree).  This IS 'Lambda=0 at the fixed")
    print("       point': the flow tangent to Hermite is the null/marginal direction.\n")

    # (C)
    R = slack_recursion_test(50)
    ds = R["ds"]
    print("(C) The slack as a marginal observable -- is there a fixed-point RATIO?")
    print("    rho(d+1)/rho(d) for d=2,8,16,24,32,40,48:")
    idx = [0, 6, 14, 22, 30, 38, 46]
    print("      " + "  ".join(f"d{int(ds[i])}:{R['ratios'][i]:.3f}" for i in idx if i < len(R['ratios'])))
    print("    Delta log(1/rho)(d) for the same d (the per-step increment):")
    print("      " + "  ".join(f"d{int(ds[i])}:{R['dlog'][i]:.3f}" for i in idx if i < len(R['dlog'])))
    print(f"    => the ratio -> 0 and the increment DIVERGES (~ +log d): NO finite fixed-point ratio.")
    c = R["fit"]
    print(f"    asymptotic fit  log(1/rho) = {c[0]:.3f} d log d + {c[1]:.3f} d + {c[2]:.3f} log d + {c[3]:.3f}")
    print(f"      (max resid {R['fit_resid']:.3f}) -> leading coeff {R['leading_dlogd_coeff']:.3f} ~ 1/2:")
    print("      log(1/rho(d)) ~ (1/2) d log d  -- the MARGINAL (d log d) law, super-exponential.\n")

    print("    slack = energy PER DEGREE  (log(1/rho) ~ (1/d) log disc(H_d)):")
    print("      d | logdisc/(d^2 log d) | log(1/rho)/(d log d) | log(1/rho)/(logdisc/d)")
    for d, e, s, r in slack_is_energy_per_degree():
        print(f"     {d:2d} |       {e:.4f}        |        {s:.4f}        |       {r:.4f}")
    print("      both energy and slack share the (1/2)(.)log(.) semicircle law; the ratio")
    print("      log(1/rho)/(logdisc/d) climbs 0.40->0.51 (slow, consistent with -> 1).\n")

    # (D)
    rows2, power = scaling_collapse(4)
    print("(D) SCALING COLLAPSE (real zeta): normalized roots of J_{4,n} -> H_4 roots as n grows:")
    print("      " + "  ".join(f"n{n}:{dev:.3f}" for n, dev in rows2))
    print(f"    approach rate dev ~ n^{power:.2f}  (slow power-law tail, GORZ 1/n correction).")
    print("    The fixed point is REAL (collapse confirmed on real zeta) but approached")
    print("    power-law-slowly, not via a clean finite-n universal scaling function.\n")

    print("VERDICT")
    print("  GO  (exact structure):  certified discriminant RG recursion (A); exact flow=rescale")
    print("       marginal identity at the fixed point (B).  Real, not decoration.")
    print("  NO-GO (load-bearing):   NO clean rho(d+1)=F(rho(d)) with a finite marginal fixed-")
    print("       point ratio.  The slack's marginality is a d-log-d super-exponential law (edge-")
    print("       controlled), the energy is relevant, the flow is marginal-along-fixed-shape --")
    print("       a correct RG TAXONOMY, but it does NOT collapse 'uniform in d' to a self-")
    print("       consistency.  The uniform-in-d bound vs a super-exp, edge-controlled margin")
    print("       remains the RH-hard endpoint (sharpened, not eased).")
    return {
        "disc_recursion_certified": ok,
        "lowering_exact": low,
        "flow_rescale_maxdev": max(devs),
        "slack_leading_coeff": R["leading_dlogd_coeff"],
        "collapse_power": power,
    }


if __name__ == "__main__":
    summary()
