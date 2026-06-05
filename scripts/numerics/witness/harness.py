"""Refutation harness (tracker H2).

Four cheap *evaluations* every candidate forward lemma must pass before we invest
in proving it.  The governing principle: a statement is on the critical path to RH
iff it FAILS for Davenport-Heilbronn.

  Check 1  Barrier battery / DH-blindness  -> catches falsity + Euler-blindness
  Check 2  RH-content tag                  -> catches circularity (RH-neutrality)
  Check 3  In-coordinate necessary conds   -> Mobius locking, Burnol consistency
  Check 4  Finite explicit-formula check   -> delegated to explicit_formula.py (E)

Run:  python3 -m scripts.numerics.witness.harness
"""
from __future__ import annotations

import numpy as np
from flint import acb, fmpz, ctx

from .objects import Zeta, DavenportHeilbronn, PlantedZeroZeta
from . import hardy as H


def mobius(n: int) -> int:
    return int(fmpz(n).moebius_mu())


# --- Check 1: barrier battery / DH-blindness --------------------------------
def check1_dh_blindness(tau=0.7, Nmax=8):
    """The spine's reverse construction is identical for zeta and DH; only the
    zero LOCATION (an Euler-product fact) distinguishes them.  Returns the
    forward-distance curves and the (identical) barrier outputs."""
    z, dh = Zeta(), DavenportHeilbronn()
    Mz = H.HardyModel(z, tau, T=400, dt=0.04)
    Md = H.HardyModel(dh, tau, T=400, dt=0.04)
    curve_z = [Mz.dist2(N)[0] for N in range(1, Nmax + 1)]
    curve_d = [Md.dist2(N)[0] for N in range(1, Nmax + 1)]
    rho = dh.offline_zeros()[0]
    bnd_dh = H.barrier_bound(dh, rho, tau)[0]
    bnd_zeta_hypo = H.barrier_bound(z, rho, tau)[0]  # identical construction
    blind = abs(bnd_dh - bnd_zeta_hypo) < 1e-12
    return {
        "tau": tau, "curve_zeta": curve_z, "curve_dh": curve_d,
        "barrier_dh": bnd_dh, "barrier_zeta_hypothetical": bnd_zeta_hypo,
        "reverse_construction_identical": blind,
        # zeta's distance keeps falling (slowly!); DH's has flattened to a floor:
        "zeta_still_descending": curve_z[-1] < curve_z[-3],
        "dh_floored": curve_d[-1] > 0.85 * curve_d[-3],
    }


# --- Check 2: RH-content tag -------------------------------------------------
def check2_rh_content(predicate, objects=None):
    """predicate: TestObject -> bool, claiming an RH-relevant property.
    If predicate(DH) == predicate(zeta) the predicate cannot separate an
    RH-false object from an RH-true one -> RH-NEUTRAL (off the critical path)."""
    if objects is None:
        objects = [Zeta(), DavenportHeilbronn()]
    vals = {o.name: bool(predicate(o)) for o in objects}
    z = vals.get("zeta")
    d = vals.get("davenport-heilbronn")
    rh_neutral = (z == d)
    return {"values": vals, "rh_neutral": rh_neutral,
            "verdict": "RH-NEUTRAL (holds-for-DH==holds-for-zeta): off critical path"
                       if rh_neutral else "has RH-content (separates DH from zeta)"}


# --- Check 3: in-coordinate necessary conditions ----------------------------
def extremal_coeffs(obj, tau, N, T=400, dt=0.04):
    """Best D_N coefficients a = G^{-1} b for projecting u onto V_N(tau)."""
    M = H.HardyModel(obj, tau, T=T, dt=dt)
    G, b = M.gram(N), M.target(N)
    return np.linalg.solve(G, b)


def check3_mobius_locking(tau=0.7, N=10):
    """For the half-plane module avatar u = phi_tau/zeta = phi_tau * sum mu(n) n^{-s},
    the extremal coefficients should approach the Mobius function mu(n).
    (Arithmetic locking; the Euler product entering through the coefficients.)"""
    a = extremal_coeffs(Zeta(), tau, N)
    mu = np.array([mobius(n) for n in range(1, N + 1)], dtype=float)
    return {"tau": tau, "N": N, "coeffs": a.tolist(), "mobius": mu.tolist(),
            "max_abs_dev": float(np.max(np.abs(a - mu))),
            "rms_dev": float(np.sqrt(np.mean((a - mu) ** 2)))}


def check3_burnol_constant():
    """Burnol/BD constant 2 + gamma - log(4 pi) ~ 0.0461; the conditional decay
    is ~ 1/log N, so any claimed unconditional forward rate FASTER than 1/log N
    is inconsistent with the unconditional lower bound."""
    ctx.prec = 120
    g = acb.stieltjes(0)
    c = acb(2) + g - (4 * acb.pi()).log()
    return {"BD_constant_2+gamma-log4pi": float(c.real),
            "implied_lower_bound": "d_N^2 >= (Sum_rho m^2/|rho|^2 + o(1))/log N (unconditional)"}


# --- Check 4: finite explicit-formula consistency ---------------------------
def check4_explicit_formula(*args, **kwargs):
    from . import explicit_formula as EF
    return EF.weil_positivity_check(*args, **kwargs)


def _report():
    print("=" * 72)
    print("REFUTATION HARNESS REPORT")
    print("=" * 72)

    print("\n[Check 1] Barrier battery / DH-blindness  (tau=0.7)")
    c1 = check1_dh_blindness()
    print("  zeta forward dist^2 :", [f"{x:.3e}" for x in c1["curve_zeta"]])
    print("  DH   forward dist^2 :", [f"{x:.3e}" for x in c1["curve_dh"]])
    print(f"  barrier(DH real zero)        = {c1['barrier_dh']:.6e}")
    print(f"  barrier(zeta HYPO same zero)  = {c1['barrier_zeta_hypothetical']:.6e}")
    print(f"  reverse construction identical for zeta & DH: {c1['reverse_construction_identical']}")
    print(f"  -> zeta descending: {c1['zeta_still_descending']}, DH floored: {c1['dh_floored']}")
    print("  VERDICT: the reverse/Hardy spine cannot distinguish zeta from DH;")
    print("           only the Euler product (zero locations) can. Spine is DH-blind.")

    print("\n[Check 2] RH-content tag")
    # example: 'has a functional equation' is RH-neutral; both zeta and DH do.
    fe = check2_rh_content(lambda o: o.functional_equation)
    print("  predicate 'has functional equation':", fe["verdict"])
    ep = check2_rh_content(lambda o: o.has_euler_product)
    print("  predicate 'has Euler product'      :", ep["verdict"])

    print("\n[Check 3] In-coordinate necessary conditions")
    ml = check3_mobius_locking()
    print(f"  Mobius locking (tau={ml['tau']}, N={ml['N']}):")
    print("   extremal coeffs:", [f"{x:+.3f}" for x in ml["coeffs"]])
    print("   mobius mu(n)   :", [f"{x:+.0f}" for x in ml["mobius"]])
    print(f"   max|a-mu| = {ml['max_abs_dev']:.3f}   rms = {ml['rms_dev']:.3f}")
    bc = check3_burnol_constant()
    print(f"  Burnol/BD constant 2+gamma-log4pi = {bc['BD_constant_2+gamma-log4pi']:.6f}")

    print("\n[Check 4] Finite explicit-formula consistency")
    try:
        c4 = check4_explicit_formula()
        print("  ", c4)
    except Exception as e:
        print("   (explicit_formula module pending: %s)" % e)
    print("=" * 72)


if __name__ == "__main__":
    _report()
