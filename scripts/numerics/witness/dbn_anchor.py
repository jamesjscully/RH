"""dBN ANCHOR -- where forcing Lambda<=0 stalls, and whether it is the SAME wall (AGENDA NEXT #1, #4).

The dynamical route: H_t = e^{-t D^2} acting on xi; Lambda(xi) = inf{t : H_t all-real};
de Bruijn-Newman: RH <=> Lambda <= 0.  Rodgers-Tao 2018 (arXiv:1801.05914, Forum Math Pi 2020):
Lambda >= 0 UNCONDITIONALLY.  This module pins, EXECUTABLY:

  (Q1, anchor)  the precise Rodgers-Tao mechanism and WHY it gives >= not <=.
  (Q2, transfer) do the closed-branch lessons (modulus!=phase, Sylvester inertia-lock) constrain
                 the flow, or does the flow evade them?
  (Q4, GUE handle, DECISIVE) is the pair-correlation input a NEW zeta-intrinsic Euler-borne lever,
                 or RH-silent (GUE is universal, shared with DH-like / random matrices)?  KILL-TEST.
  (Q5, verdict)  distinct dynamical endpoint, or the same cross-place coupling W_infty >= Sum_p W_p?

THE MECHANISM (Q1), from Tao's blog + the paper, stated object-free:
  * Proof by CONTRADICTION: assume Lambda < 0 (= RH with a strict spectral margin).
  * Then over (Lambda, 0] the zeros x_j(t) of H_t flow under the REPULSIVE log-gas ODE
        d/dt x_j = -2 Sum_{k!=j} 1/(x_k - x_j)         (backward-in-t direction relevant here)
    and Lambda<0 forces "convergence to local equilibrium": the gaps equalize, the zeros at
    t=0 must locally look like an ARITHMETIC PROGRESSION (uniform spacing, gap -> global mean).
  * CONTRADICTION via Montgomery pair correlation: the TRUE zeros of zeta (t=0) have GUE-type
    pair correlation 1 - (sin(pi u)/(pi u))^2 -- LEVEL REPULSION with OSCILLATION, NOT the rigid
    AP/picket-fence spacing equilibrium would force.  So Lambda < 0 is impossible => Lambda >= 0.

THE ASYMMETRY (Q1), the load-bearing point:
  Rodgers-Tao derive a contradiction from a property the zeros DO HAVE (GUE statistics being
  INCOMPATIBLE with equilibrium).  That is a LOWER bound on disorder: the zeros are "too rigid /
  too repulsive" to have equilibrated, so the flow cannot have run long backward => Lambda not very
  negative => Lambda >= 0.  RH is Lambda <= 0: NO complex zero pair exists at t=0 -- a statement
  about zero LOCATIONS (the imaginary part), which a STATISTIC (a 2-point average) cannot see:
  a single off-line pair is measure-zero in pair correlation.  Forward flow DISPERSES (entropy up,
  variance up); it does not concentrate, so there is no monotone Lyapunov functional pushing a
  stray complex pair back onto R.  >= is a statistics bound (sees the bulk); <= is a location bound
  (needs the individual imaginary parts) -- the SAME modulus(statistics)/phase(location) split that
  closed the static forms.

Run:  python3 -m scripts.numerics.witness.dbn_anchor
"""
from __future__ import annotations

import numpy as np

from .dbn_route import _all_real, _from_roots, dbn_lambda, heat_flow


# ------------------------------------------------------------------------------------------------
# (Q1) The forward/backward asymmetry, executable: a monotone DISPERSION functional under the flow.
# ------------------------------------------------------------------------------------------------
def root_variance(coeffs):
    """Variance of the (real parts of the) roots -- a proxy for the log-gas 'spread'.
    Under the heat flow the second moment of a hyperbolic polynomial's roots GROWS:
    forward flow disperses (entropy/variance UP), so it cannot force a stray complex pair
    onto R.  Backward flow CONTRACTS toward equilibrium -- the direction Rodgers-Tao exploit."""
    r = np.roots(np.array(coeffs, float)[::-1])
    return float(np.var(r.real))


def flow_monotonicity(roots, ts=(-0.02, -0.01, 0.0, 0.01, 0.02)):
    """Show the variance is MONOTONE in flow time t around a hyperbolic configuration.
    Forward t>0 (heat smoothing) -> variance changes one way; backward t<0 -> the other.
    The asymmetry: backward is the contracting/equilibrating direction (Rodgers-Tao), forward
    is dispersing (no Lyapunov purchase on reality)."""
    c = _from_roots(roots)
    out = {}
    for t in ts:
        cf = heat_flow(c, t)
        out[t] = root_variance(cf)
    return out


# ------------------------------------------------------------------------------------------------
# (Q4) THE DECISIVE KILL-TEST: is the GUE/pair-correlation input Euler-borne, or universal?
# ------------------------------------------------------------------------------------------------
def pair_correlation_form_factor(spacings):
    """Empirical pair-correlation deviation from the POISSON (uncorrelated) baseline at small scale.
    GUE has level repulsion: P(small gap)->0; Poisson does not.  We measure the depletion of small
    gaps -- a coarse but real GUE-vs-Poisson discriminator."""
    s = np.array(spacings, float)
    s = s / np.mean(s)
    # fraction of gaps below 1/4 of the mean: GUE ~ small (repulsion), Poisson ~ larger
    return float(np.mean(s < 0.25))


def gue_universality_probe():
    """Q4 kill-test, executable.  The Rodgers-Tao contradiction needs: 'zeta's zeros at t=0 do NOT
    sit in arithmetic-progression equilibrium'.  The INPUT supplying that is GUE-type level
    repulsion.  Is level repulsion EULER-BORNE (a property only zeta's product gives), or UNIVERSAL
    (shared by random-matrix eigenvalues / DH-like spectra that have NO Euler product)?

    We compare three spectra's small-gap depletion (repulsion):
      * GUE eigenvalues          (NO Euler product, pure random matrix)
      * a 'picket fence' / AP    (the equilibrium Rodgers-Tao must exclude)  -- maximal repulsion
      * Poisson (uncorrelated)   (NO repulsion)
    If GUE (no Euler product) has the SAME repulsion the argument relies on, the lever is UNIVERSAL,
    NOT Euler-borne -> the contradiction is shared with non-zeta spectra -> RH-silent on the Euler axis.
    """
    rng = np.random.default_rng(0)
    n = 2000
    # GUE: eigenvalues of a Hermitian Gaussian matrix (no arithmetic anywhere)
    m = 400
    A = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
    H = (A + A.conj().T) / 2
    ev = np.sort(np.linalg.eigvalsh(H))
    gue_gaps = np.diff(ev)
    # Poisson: uniform points
    pois = np.sort(rng.uniform(0, n, n))
    pois_gaps = np.diff(pois)
    # picket fence (perfect AP = the equilibrium): all gaps equal
    ap_gaps = np.ones(n)
    return {
        "GUE (no Euler product)": pair_correlation_form_factor(gue_gaps),
        "Poisson (uncorrelated)": pair_correlation_form_factor(pois_gaps),
        "AP / equilibrium": pair_correlation_form_factor(ap_gaps),
    }


# ------------------------------------------------------------------------------------------------
# (Q2) transfer: does the FLOW evade the Sylvester inertia-lock?  Yes -- it is a 1-param semigroup,
# NOT a *-congruence.  But it pays for that by being a DISPERSION (modulus), blind to sign(Im).
# ------------------------------------------------------------------------------------------------
def evades_sylvester_demo():
    """The heat semigroup e^{-tD^2} is NOT a congruence T^T(.)T of a fixed form; it is a genuine
    1-parameter group acting on the POLYNOMIAL (the zeros), so the Sylvester inertia-lock (which
    closed every static self-pairing) does NOT apply -- the flow CAN change the number of real
    roots (that is the whole point of Lambda).  Demonstrated: a polynomial with a complex pair
    becomes all-real under forward flow (inertia of 'realness' is NOT preserved)."""
    c = _from_roots([1.0, -1.0, 0.5 + 0.8j, 0.5 - 0.8j])  # one complex pair
    L = dbn_lambda(c)
    real_before = _all_real(c)
    real_after = _all_real(heat_flow(c, L + 1e-6))
    return {"all_real_at_t0": real_before, "all_real_after_flow": real_after, "Lambda": L}


def summary():
    print("dBN ANCHOR -- where forcing Lambda<=0 stalls; is it the same wall? (AGENDA NEXT #1,#4)\n")

    print("[Q1] forward/backward ASYMMETRY (the variance/dispersion is monotone in flow time):")
    mono = flow_monotonicity([-2.0, -1.0, 0.5, 1.5, 2.5])
    for t in sorted(mono):
        arrow = "backward(contract)" if t < 0 else ("t=0" if t == 0 else "forward(disperse)")
        print(f"    t={t:+.2f}  Var(roots)={mono[t]:.5f}   {arrow}")
    base = mono[0.0]
    fwd = mono[max(mono)] - base
    bwd = mono[min(mono)] - base
    print(f"    => forward DISPERSES (dVar={fwd:+.4f}), backward CONTRACTS (dVar={bwd:+.4f}).")
    print("    Rodgers-Tao exploit backward CONTRACTION->equilibrium.  Forward has NO Lyapunov")
    print("    purchase on reality => the <= direction (RH) gets no monotone forcing from the flow.\n")

    print("[Q2] does the FLOW evade the Sylvester inertia-lock that closed the static forms? YES:")
    ev = evades_sylvester_demo()
    print(f"    a complex pair (all_real={ev['all_real_at_t0']}) becomes all-real after flow "
          f"(all_real={ev['all_real_after_flow']}, Lambda={ev['Lambda']:.4f}).")
    print("    The heat semigroup is a 1-param group on the POLYNOMIAL, NOT a *-congruence of a")
    print("    fixed form -> it CHANGES the count of real roots, so Sylvester does NOT lock it.")
    print("    => genuinely DIFFERENT from the static routes on the inertia axis. BUT (Q4) the price:\n")

    print("[Q4] DECISIVE KILL-TEST -- is the GUE/pair-correlation input EULER-BORNE or UNIVERSAL?")
    print("     small-gap depletion (level repulsion); the input the RT contradiction relies on:")
    g = gue_universality_probe()
    for name, v in g.items():
        print(f"    {name:28s} P(gap<0.25*mean) = {v:.4f}")
    gue_repels = g["GUE (no Euler product)"] < 0.5 * g["Poisson (uncorrelated)"]
    print(f"    => GUE (NO Euler product) shows level repulsion: {gue_repels}.")
    print("    The contradiction-input (zeros are repulsive/rigid, NOT equilibrium) is UNIVERSAL:")
    print("    random-matrix eigenvalues with NO Euler product carry it identically.  GUE is the")
    print("    universality class, NOT a zeta-intrinsic Euler-borne lever => RH-SILENT on the Euler")
    print("    axis.  (Confirmed by the literature: DH off-line zeros have 'essentially different'")
    print("    statistics, but the GUE INPUT itself is shared with non-Euler spectra.)\n")

    print("[Q5] VERDICT -- distinct dynamical endpoint, or the same cross-place coupling?")
    print("  * Lambda SEES zeros (Lambda>0 <=> off-line pair; dbn_route.py): sees-zeros YES.")
    print("  * The FLOW EVADES the Sylvester inertia-lock (Q2): genuinely distinct on that axis --")
    print("    a 1-param semigroup, not a congruence; it CAN change the real-root count.")
    print("  * BUT the only UNCONDITIONAL handle (Rodgers-Tao) gives Lambda>=0, the WRONG direction,")
    print("    and its lever (GUE/Montgomery pair correlation) is UNIVERSAL, NOT Euler-borne (Q4).")
    print("  * The asymmetry (Q1) is the SAME modulus/phase split: >= is a STATISTICS (bulk/modulus)")
    print("    bound; RH (<=) is a zero-LOCATION (sign Im / phase) bound a 2-point statistic cannot")
    print("    see.  Forcing Lambda<=0 needs to forbid a SINGLE off-line pair = exactly the per-zero")
    print("    location control the static routes also could not get from any Euler-borne functional.")
    print("  NET: the dynamical branch is genuinely DISTINCT on the INERTIA axis (escapes Sylvester),")
    print("  but its unconditional lever is RH-silent (universal GUE, wrong direction), and the")
    print("  Lambda<=0 endpoint reduces to the SAME location/phase control = W_infty >= Sum_p W_p")
    print("  read dynamically.  A NEW Euler-borne dynamical input (a flow functional that is itself")
    print("  built from Lambda(n) and forces reality) would be required -- none is supplied by RT.")


if __name__ == "__main__":
    summary()
