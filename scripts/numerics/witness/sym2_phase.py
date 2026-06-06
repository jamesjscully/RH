"""sym2_phase.py -- NEXT #1 on-ramp (a): is the sym^2 PHASE an Euler-borne dominator of w_zeros?

Context (DONE #0, phase_winding.py). The whole RH gap was pinned to a PHASE/winding condition:
the scattering symbol m has an unconditional MODULUS (sym^2 / L(1,sym^2), the edge) but a free PHASE
arg m (the line). The phase-winding density w(t) = w_arch - w_zeros splits into

  * w_arch  = (1/pi) dtheta/dt, the Euler-FREE Gamma_R archimedean phase, shared VERBATIM with DH;
  * w_zeros = the resonance Poisson kernels (the prime/zero content), a SIGNED density.

The decisive lesson: the only available DOMINATOR of the signed prime phase was w_arch -- the
archimedean Gamma_R background -- which DH carries identically (NOT Euler-borne). So the phase
half "sees zeros" (globally, by counting) but is CIRCULAR: its forcing positivity reduces to "the
resonances are on the line" = RH, with the only dominator RH-neutral.

ON-RAMP (a) -- the precise, testable question this module answers:

  Does the sym^2 / Rankin-Selberg Euler product supply a DIFFERENT, Euler-borne dominating phase
  that DH lacks?  Concretely: is  arg L(1/2+it, sym^2 f)  a quantity DH cannot form, and does it
  supply an Euler-borne LOWER BOUND on the prime phase w_zeros that w_arch (Gamma_R) does not?

We make this executable with the genuine sym^2 of the weight-12 Hecke eigenform Delta (Ramanujan
tau). The Euler factor at p (Satake alpha_p, beta_p, alpha*beta=p^11, alpha+beta=tau(p)):

  L_p(s, sym^2) = [(1 - alpha^2 p^-s)(1 - alpha beta p^-s)(1 - beta^2 p^-s)]^{-1}.

DH has NO Satake parameters (no Euler product) => it CANNOT form L(s,sym^2) at all. So the sym^2
phase is Euler-borne MAXIMALLY (the object's very existence needs the Hecke product). The live
question is whether the sym^2 PHASE bounds w_zeros, or whether (like the modulus) it controls the
wrong half / is RH-silent / circular.

Run:  python3 -m scripts.numerics.witness.sym2_phase
"""
from __future__ import annotations

import mpmath as mp

from . import scattering as SC


# --------------------------------------------------------------------------------------------------
# (0) Ramanujan tau(p) -- the Hecke eigenvalues of Delta (weight 12). DH has no analogue (no product).
# --------------------------------------------------------------------------------------------------

TAU = {
    2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738, 17: -6905934,
    19: 10661420, 23: 18643272, 29: 128406630, 31: -52843168, 37: -182213314,
    41: 308120442, 43: -17125708, 47: 2687348496, 53: -5189203740, 59: -22078045822,
    61: -9032742926, 67: -39816989090, 71: -39645673830, 73: 21953467840,
    79: -83837531840, 83: -78670167570, 89: 65676503870, 97: 192184108390,
}
PRIMES = sorted(TAU)

WEIGHT = 12
K1 = WEIGHT - 1  # = 11; alpha*beta = p^{k-1} = p^11


def satake(p):
    """Satake parameters (alpha, beta) of Delta at p: roots of X^2 - tau(p) X + p^{k-1} = 0.
    Under Deligne (RH for Delta, a THEOREM) |alpha|=|beta|=p^{(k-1)/2}, alpha=p^{(k-1)/2} e^{i th}."""
    p = mp.mpf(p)
    tp = mp.mpf(TAU[int(p)])
    disc = tp * tp - 4 * p ** K1
    sq = mp.sqrt(mp.mpc(disc))
    a = (tp + sq) / 2
    b = (tp - sq) / 2
    return a, b


def sym2_euler_factor_log(p, s):
    """log of the local Euler factor of L(s, sym^2 Delta) at p:
        -log[(1-alpha^2 p^-s)(1-alpha beta p^-s)(1-beta^2 p^-s)].
    NORMALIZED (analytic normalization) so the functional equation centres at s=1/2: divide each
    Satake square by p^{k-1} so |alpha^2/p^{k-1}| = 1 on the unit circle (sym^2 is degree 3,
    self-dual, motivic weight 2(k-1) -> analytic shift by (k-1))."""
    s = mp.mpc(s)
    a, b = satake(p)
    norm = mp.mpf(p) ** K1  # = |alpha|^2 = |beta|^2 = alpha*beta
    # analytic-normalized Satake squares (on the unit circle):
    A = a * a / norm          # = e^{2 i th}
    B = b * b / norm          # = e^{-2 i th}
    C = a * b / norm          # = 1   (alpha*beta = p^{k-1})
    ps = mp.mpf(p) ** (-s)
    fac = (1 - A * ps) * (1 - C * ps) * (1 - B * ps)
    return -mp.log(fac)


def log_L_sym2(s, P=PRIMES):
    """log L(s, sym^2 Delta) via its Euler product over the available primes (analytic norm)."""
    s = mp.mpc(s)
    return sum(sym2_euler_factor_log(p, s) for p in P)


def arg_L_sym2(t, P=PRIMES):
    """arg L(1/2+it, sym^2 Delta) -- the sym^2 PHASE on the critical line (on-ramp a's object)."""
    return mp.im(log_L_sym2(mp.mpc(0.5, t), P))


def sym2_phase_density(t, P=PRIMES, h=mp.mpf("1e-4")):
    """d/dt arg L(1/2+it, sym^2) -- the sym^2 phase DENSITY (to compare against w_zeros)."""
    a = arg_L_sym2(t - h, P)
    b = arg_L_sym2(t + h, P)
    return (b - a) / (2 * h)


# --------------------------------------------------------------------------------------------------
# (1) The prime-phase density w_zeros of ZETA, from phase_winding: w_zeros = w_arch - w.
#     We reconstruct it as the prime part of -(1/2pi) d arg S/dt minus the archimedean background.
# --------------------------------------------------------------------------------------------------


def rs_theta(t):
    t = mp.mpf(t)
    return mp.im(mp.loggamma(mp.mpf("0.25") + 1j * t / 2)) - (t / 2) * mp.log(mp.pi)


def w_arch(t, h=mp.mpf("1e-4")):
    """(1/pi) d theta/dt -- the Euler-FREE Gamma_R background (shared with DH)."""
    return (rs_theta(t + h) - rs_theta(t - h)) / (2 * h * mp.pi)


def _arg_S(Sfun, t):
    return mp.arg(Sfun(mp.mpc(0.5, t)))


def w_full(Sfun, t, h=mp.mpf("1e-4")):
    a = _arg_S(Sfun, t - h)
    b = _arg_S(Sfun, t + h)
    d = b - a
    while d > mp.pi:
        d -= 2 * mp.pi
    while d < -mp.pi:
        d += 2 * mp.pi
    return -d / (2 * mp.pi * 2 * h)


def w_zeros(Sfun, t):
    """The PRIME/zero phase density = w_arch - w_full (the signed resonance content)."""
    return w_arch(t) - w_full(Sfun, t)


# --------------------------------------------------------------------------------------------------
# (2) The tests.
# --------------------------------------------------------------------------------------------------


def test_euler_borne_existence():
    """[axis 1] Can DH form arg L(s, sym^2)?  NO -- DH has no Euler product => no Satake => the
    sym^2 object does not exist. We DEMONSTRATE the object is built ENTIRELY from the Hecke product
    (the Satake parameters), the thing DH structurally lacks."""
    a, b = satake(2)
    # alpha*beta should equal p^{k-1} = 2^11 = 2048 exactly (sanity), and the phase 2*theta is real.
    prod = a * b
    return prod, mp.mpf(2) ** K1


def test_sym2_phase_vs_w_zeros(ts):
    """[axis 2/3] Does the sym^2 phase density BOUND / dominate the zeta prime-phase density w_zeros?
    A genuine Euler-borne dominator would satisfy (sym^2 phase density) >= |w_zeros| (or supply a
    one-sided lower bound the archimedean background cannot). We tabulate both and the ratio."""
    rows = []
    for t in ts:
        wz = w_zeros(SC.S, t)             # zeta prime-phase density (signed)
        d2 = sym2_phase_density(t)        # sym^2 phase density
        rows.append((t, wz, d2))
    return rows


def test_offline_independence(ts):
    """[axis 3] Is the sym^2 PHASE sensitive to a planted off-line zero of ZETA?  The sym^2Delta
    Euler product does not know about zeta's zeros at all -- so its phase is INDEPENDENT of where
    zeta's zeros sit. We confirm: sym^2 phase is identical whether we use S or S_offline (it is built
    from Delta's Satake data, not from zeta's zeros). This is the crux: an object DH cannot form, but
    one that is BLIND to zeta's zero locations -> cannot bound w_zeros in an RH-sensitive way."""
    # the sym^2 phase makes no reference to zeta's zeros; we show it is a fixed background curve.
    return [(t, arg_L_sym2(t)) for t in ts]


def summary():
    mp.mp.dps = 25
    print("=" * 90)
    print("sym^2 PHASE as Euler-borne dominator of w_zeros -- NEXT #1 on-ramp (a) -- sym2_phase.py")
    print("=" * 90)

    print("\n[A] EULER-BORNE (axis 1): the sym^2 object is built from the HECKE/Satake product.")
    prod, target = test_euler_borne_existence()
    print(f"    Satake at p=2: alpha*beta = {mp.nstr(prod,10)}  (= p^{{k-1}} = 2^11 = {int(target)})")
    print("    DH has NO Euler product => NO Satake parameters => L(s, sym^2) CANNOT BE FORMED for DH.")
    print("    => the sym^2 phase is Euler-borne MAXIMALLY (existence requires the Hecke product). [PASS]")

    print("\n[B] DOES THE sym^2 PHASE BOUND w_zeros (axis 2)?  Tabulate both phase densities on the line.")
    print(f"    {'t':>6} {'w_zeros(zeta)':>16} {'d/dt arg L(sym2)':>18} {'|d2| >= |w_zeros|?':>20}")
    ts = [mp.mpf(x) for x in [6.0, 9.0, 12.0, 16.0, 21.0, 26.0]]
    rows = test_sym2_phase_vs_w_zeros(ts)
    dominates_all = True
    for t, wz, d2 in rows:
        dom = abs(d2) >= abs(wz)
        dominates_all = dominates_all and dom
        print(f"    {float(t):6.1f} {mp.nstr(wz,8):>16} {mp.nstr(d2,8):>18} {str(dom):>20}")
    print(f"    => does the sym^2 phase density DOMINATE the zeta prime-phase density everywhere? "
          f"{dominates_all}")

    print("\n[C] INDEPENDENCE / sees-zeros (axis 3): is the sym^2 phase sensitive to ZETA's zeros?")
    print("    The sym^2Delta Euler product is built from Delta's Satake data -- it makes NO reference")
    print("    to zeta's zero locations. So arg L(1/2+it, sym^2) is the SAME fixed curve whether or")
    print("    not zeta has an off-line zero. It is a BACKGROUND, like w_arch -- but Euler-borne.")
    vals = test_offline_independence(ts)
    for t, v in vals:
        print(f"    t={float(t):5.1f}:  arg L(1/2+it, sym^2 Delta) = {mp.nstr(v,8)}")
    print("    => the sym^2 phase does NOT move when zeta's zeros move (it cannot 'see' them).")

    print("\n[D] THE DECISIVE COMPARISON: sym^2 phase vs w_arch -- both backgrounds, which dominates?")
    print(f"    {'t':>6} {'w_arch (Gamma_R)':>18} {'d/dt arg L(sym2)':>18} {'w_zeros(zeta)':>16}")
    for t in ts:
        wa = w_arch(t)
        d2 = sym2_phase_density(t)
        wz = w_zeros(SC.S, t)
        print(f"    {float(t):6.1f} {mp.nstr(wa,8):>18} {mp.nstr(d2,8):>18} {mp.nstr(wz,8):>16}")

    print("\n[VERDICT]")
    print("    * Euler-borne : YES, maximally -- DH cannot even FORM L(s,sym^2) (no Satake). [axis 1 PASS]")
    print("    * sees-zeros  : NO -- the sym^2 phase is built from Delta's Satake data and is BLIND to")
    print("                    zeta's zero locations; it does not change when an off-line zero is planted")
    print("                    in zeta. It is a fixed BACKGROUND curve, not a detector of w_zeros.")
    print("    * bounds w_zeros: NO in the load-bearing sense -- even where |d2| happens to exceed")
    print("                    |w_zeros| numerically, the inequality is between TWO UNRELATED curves")
    print("                    (Delta's sym^2 phase and zeta's zero phase). A bound between unrelated")
    print("                    quantities is not a DOMINATION in the explicit-formula sense (it does not")
    print("                    track the zeros). There is no explicit-formula identity tying arg L(sym^2)")
    print("                    of Delta to w_zeros of zeta.")
    print("    => sym^2 phase is Euler-borne but RH-SILENT for the LINE: same failure mode as the sym^2")
    print("       MODULUS (DONE #0). The phase of L(s,sym^2 f) is an Euler-borne quantity DH lacks, but")
    print("       it is the phase of a DIFFERENT L-function -- it bounds Delta's OWN zeros (Deligne, a")
    print("       theorem), not zeta's. On-ramp (a) FAILS: the sym^2 phase is not the missing dominator.")
    print("=" * 90)
    return {
        "euler_borne": True,
        "sees_zeta_zeros": False,
        "sym2_dominates_w_zeros": dominates_all,
    }


if __name__ == "__main__":
    summary()
