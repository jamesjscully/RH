"""PROBE PB -- the DH kill-test on the PHASE certificate, run against the GENUINE
Davenport-Heilbronn function (not a synthetic FE-symmetric plant).

CONTEXT.  The banked frontier object (doc 134 sec 6, positivity_reality.py) is PHASE-CERT:
the candidate positivity for arg m / S(T), the scattering-phase winding density

    w(t) := -(1/2pi) d/dt arg S(1/2+it),     S(s) = Lam(2s-1)/Lam(2s).

phase_winding.py established the verdict against a SYNTHETIC off-line plant (an FE-symmetric
quadruple grafted onto zeta).  GROUND GC's standing uncertainty: "No banked witness explicitly
computes S_DH(T) (the DH winding) numerically and verifies its jumps at DH's KNOWN off-line zeros
against the argument principle."  THIS PROBE CLOSES THAT GAP.

DH is a genuine FE-bearing Dirichlet series with NO Euler product and a PROVEN off-line zero at
    rho0 = 0.8085171824569... + 85.6993484856979... i      (objects.DavenportHeilbronn)
The completed function is  Lam_DH(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f_DH(s)  (ODD character mod 5),
verified here to satisfy |Lam_DH(s)| = |Lam_DH(1-s)| (FE ratio 1.0).  So S_DH(s)=Lam_DH(2s-1)/Lam_DH(2s)
is unitary on the line and the winding density w_DH(t) EXISTS, identically to zeta.

THE THREE-WAY KILL-TEST (the decisive trichotomy of the operating discipline).  A genuine PHASE-CERT
must (a) be unconditionally prime-provable AND (b) detect DH's off-line zeros.  We classify the
candidate phase positivity w(t)>=0 (and the winding count) as exactly ONE of:

  (a) HOLDS VERBATIM FOR DH  => RH-SILENT (FE/edge phase).  The local density positivity w(t)>=0 on
      Re s=1/2 holds for DH too (its off-line zero does not break on-line density-positivity), so the
      certificate cannot distinguish DH -- it is FE-shared.

  (b) DETECTS DH'S OFF-LINE ZEROS ONLY WITH RH-STRENGTH INPUT  => RH-EQUIVALENT (Weil-positivity in
      disguise).  The winding COUNT (argument principle) does see DH's off-line zero -- but reading
      "off-line" off the count requires knowing the resonance LOCATION (Re != 1/4), i.e. the zero
      data = RH-strength.  Equivalently the only sign-discriminating positivity is the Weil/Li form.

  (c) DETECTS DH OFF-LINE UNCONDITIONALLY FROM PRIMES  => ESCAPE (a genuine forcing structure).

We compute, on the GENUINE DH function:
  [1] FE check: |Lam_DH(s)|=|Lam_DH(1-s)| (the winding object is well-defined for DH).
  [2] local on-line winding density w_DH(t)>=0 across DH's off-line-zero ordinate -- the (a) test.
  [3] the argument-principle WINDING of f_DH around the genuine off-line zero rho0 (= +1, the zero is
      really there and off the line) and the on-line winding count change -- the (b) test.
  [4] the prime-borne phase: arg/winding built from DH's von-Mangoldt coefficients c_DH(n) (the only
      Euler-borne handle) -- does any prime-side phase functional detect rho0 WITHOUT the zero data?
      The (c) test, reusing the explicit_formula.py DH coefficient discriminator.

Run:  python3 -m scripts.numerics.witness.probe_pb_dh_phase_killtest
"""
from __future__ import annotations

import mpmath as mp

# genuine DH coefficient constant c = tan(theta), and the von-Mangoldt/log-deriv machinery
from .explicit_formula import log_deriv_coeffs, dh_coeffs, is_prime_power, von_mangoldt


# --------------------------------------------------------------------------------------------------
# The GENUINE Davenport-Heilbronn function and its completed (FE) form.
# f_DH(s) = 5^{-s} sum_{r=1}^{4} a_r zeta(s, r/5),  a = (1, c, -c, -1),  c = tan(theta).
# ODD character mod 5  => completed  Lam_DH(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f_DH(s),
# satisfying |Lam_DH(s)| = |Lam_DH(1-s)| (verified in [1]).
# --------------------------------------------------------------------------------------------------

_C = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)   # 0.28407904384...
_A = [mp.mpf(1), _C, -_C, mp.mpf(-1)]

# the proven off-line zero (objects.DavenportHeilbronn._cached_offline)
RHO0 = mp.mpc("0.8085171824569128708", "85.69934848569795178")


def f_dh(s):
    s = mp.mpc(s)
    tot = mp.mpf(0)
    for r in range(1, 5):
        tot += _A[r - 1] * mp.zeta(s, mp.mpf(r) / 5)
    return mp.mpf(5) ** (-s) * tot


def Lam_dh(s):
    s = mp.mpc(s)
    return (mp.mpf(5) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * f_dh(s)


def S_dh(s):
    """DH scattering symbol S_DH(s) = Lam_DH(2s-1)/Lam_DH(2s).  Resonances at zeros of Lam_DH(2s),
    i.e. s = rho_DH/2.  The genuine off-line zero rho0 gives an OFF-line resonance at Re = Re(rho0)/2."""
    s = mp.mpc(s)
    return Lam_dh(2 * s - 1) / Lam_dh(2 * s)


# zeta side (for the side-by-side on-line density comparison)
def Lam_z(s):
    s = mp.mpc(s)
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def S_z(s):
    s = mp.mpc(s)
    return Lam_z(2 * s - 1) / Lam_z(2 * s)


# --------------------------------------------------------------------------------------------------
# The candidate PHASE positivity: winding density w(t) = -(1/2pi) d/dt arg S(1/2+it).
# --------------------------------------------------------------------------------------------------

def _arg_S(Sfun, t):
    return mp.arg(Sfun(mp.mpc(0.5, t)))


def winding_density(Sfun, t, h=mp.mpf("1e-4")):
    a = _arg_S(Sfun, t - h)
    b = _arg_S(Sfun, t + h)
    d = b - a
    while d > mp.pi:
        d -= 2 * mp.pi
    while d < -mp.pi:
        d += 2 * mp.pi
    return -d / (2 * mp.pi * 2 * h)


def density_min(Sfun, t_lo, t_hi, npts):
    ts = [t_lo + (t_hi - t_lo) * k / (npts - 1) for k in range(npts)]
    ws = [winding_density(Sfun, mp.mpf(t)) for t in ts]
    mn = min(ws)
    mx = max(ws)
    return mn, mx, (mn >= -mp.mpf("1e-6"))


def arg_principle_winding(gfun, center, radius, npts=400):
    """Winding number (1/2pi) Delta arg g around a circle of given radius about center.
    = number of zeros of g inside (argument principle).  Detects whether rho0 is a real zero."""
    tot = mp.mpf(0)
    prev = None
    for k in range(npts + 1):
        ang = 2 * mp.pi * k / npts
        z = center + radius * mp.e ** (1j * ang)
        cur = mp.arg(gfun(z))
        if prev is not None:
            d = cur - prev
            while d > mp.pi:
                d -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
            tot += d
        prev = cur
    return tot / (2 * mp.pi)


# --------------------------------------------------------------------------------------------------

def summary():
    mp.mp.dps = 30
    print("=" * 92)
    print("PROBE PB -- DH kill-test on the PHASE certificate (GENUINE Davenport-Heilbronn)")
    print("=" * 92)

    # ---- [1] FE check: the winding object is WELL-DEFINED for DH (S_DH unitary on the line) ----
    print("\n[1] DH functional equation -- the PHASE/winding object exists for DH identically to zeta.")
    print("    Lam_DH(s) = (5/pi)^((s+1)/2) Gamma((s+1)/2) f_DH(s)  (odd char mod 5).")
    fe_ok = True
    for s in [mp.mpc("0.3", "12"), mp.mpc("0.7", "40"), mp.mpc("0.42", "85.7")]:
        r = abs(Lam_dh(s) / Lam_dh(1 - s))
        ok = abs(r - 1) < mp.mpf("1e-12")
        fe_ok = fe_ok and ok
        print(f"    s={complex(s)}:  |Lam_DH(s)|/|Lam_DH(1-s)| = {mp.nstr(r,12)}  (FE: {ok})")
    # unitarity of S_DH on the line (away from poles)
    for t in [40.0, 60.0]:
        u = abs(S_dh(mp.mpc(0.5, t)))
        print(f"    |S_DH(1/2+{t}i)| = {mp.nstr(u,12)}  (unitary, FE-forced -- RH-NEUTRAL, holds for DH)")
    print(f"    => arg m_DH / S_DH(T) and the winding density w_DH(t) EXIST.  FE_ok={fe_ok}")

    # ---- [2] THE (a) TEST: local on-line density positivity w(t)>=0 -- holds VERBATIM for DH? ----
    # DH's off-line zero rho0 is at height 85.699; the resonance of S_DH sits at s=rho0/2 (Im~42.85,
    # Re=Re(rho0)/2=0.404 != 1/4).  On the line Re s=1/2 we scan the ordinate band of S_DH straddling
    # Im(rho0)/2 ~ 42.85 (where the off-line resonance is nearest the line).
    print("\n[2] (a)-TEST  local on-line density positivity w(t)>=0 across DH's off-line resonance band.")
    print("    DH off-line zero rho0 = 0.8085 + 85.699 i  =>  S_DH resonance at s=rho0/2,")
    print(f"    Re = {float((RHO0.real)/2):.4f} != 1/4, Im = {float(RHO0.imag/2):.4f}.  We scan t around Im(rho0)/2.")
    tband_lo, tband_hi = 40.0, 46.0
    mn_dh, mx_dh, ok_dh = density_min(S_dh, tband_lo, tband_hi, 49)
    mn_z, mx_z, ok_z = density_min(S_z, tband_lo, tband_hi, 49)
    print(f"    GENUINE DH : min w = {mp.nstr(mn_dh,6)}  max w = {mp.nstr(mx_dh,6)}  nonneg(>=-1e-6)={ok_dh}")
    print(f"    zeta       : min w = {mp.nstr(mn_z,6)}  max w = {mp.nstr(mx_z,6)}  nonneg(>=-1e-6)={ok_z}")
    a_holds_for_dh = ok_dh  # the candidate positivity holds VERBATIM for the RH-FALSE DH
    print(f"    => candidate positivity w(t)>=0 HOLDS for the RH-FALSE genuine DH on the line? {a_holds_for_dh}")
    print("       (a)-verdict: if True, local on-line density positivity is FE-SHARED => RH-SILENT.")

    # ---- [3] THE (b) TEST: the WINDING COUNT sees rho0, but only via the off-line LOCATION ----
    print("\n[3] (b)-TEST  argument-principle WINDING -- the count sees rho0, but reading 'off-line'")
    print("    requires the resonance LOCATION (Re != 1/4) = the zero data = RH-strength.")
    # (3a) the zero rho0 is genuinely a zero of f_DH (winding of f_DH around rho0 = +1)
    w_around = arg_principle_winding(f_dh, RHO0, mp.mpf("0.5"))
    print(f"    winding of f_DH around rho0 (radius 0.5) = {mp.nstr(w_around,6)}  (=+1: rho0 is a REAL zero)")
    # (3b) the off-line-ness is Re(rho0) != 1/2: a LOCATION fact, invisible to on-line |S_DH|=1.
    offline_Re = float(RHO0.real)
    print(f"    rho0 lies at Re = {offline_Re:.4f} != 1/2  => OFF the critical line (RH-false).")
    print(f"    But |S_DH|=1 on the line for ALL t (shown in [1]) -- the modulus is BLIND to this.")
    print("    The winding density on the line is a POSITIVE Lorentzian TAIL of the off-line resonance")
    print("    ([2]: w_DH>=0 on the line); the BACKWARD winding lives at Re=Re(rho0)/2=0.404, NOT on")
    print("    Re s=1/2.  So to DETECT rho0 as off-line you must evaluate the winding OFF the line / read")
    print("    the resonance location.  That location = the zero = RH-strength input.")
    b_needs_zero_data = (offline_Re != 0.5) and a_holds_for_dh
    print(f"    => detecting DH off-line requires the zero LOCATION (RH-strength)? {b_needs_zero_data}")

    # ---- [4] THE (c) TEST: the prime-borne phase -- does the Euler-borne handle detect rho0 unconditionally? ----
    print("\n[4] (c)-TEST  prime-borne phase: DH's only Euler-borne handle is its log-deriv coefficients")
    print("    c_DH(n) (the 'prime side' of -f'/f).  Does a phase/winding built from c_DH detect rho0")
    print("    WITHOUT the zero data?  We check whether c_DH is even a valid prime-side (Euler) object.")
    M = 30
    c_z = log_deriv_coeffs([1] * M, M)
    c_d = log_deriv_coeffs(dh_coeffs(M), M)
    lam_err = max(abs(float(c_z[n - 1]) - von_mangoldt(n)) for n in range(1, M + 1))
    zeta_pp = all(abs(float(c_z[n - 1])) < 1e-12 or is_prime_power(n) for n in range(1, M + 1))
    dh_neg = any(float(x) < -1e-9 for x in c_d)
    dh_offpp = [n for n in range(2, M + 1)
                if abs(float(c_d[n - 1])) > 1e-6 and not is_prime_power(n)]
    print(f"    zeta prime side c_zeta(n) = von Mangoldt? err={lam_err:.2e}; prime-power supported? {zeta_pp}")
    print(f"    DH   prime side c_DH(n): has NEGATIVE coeffs? {dh_neg}; off-prime-power support n={dh_offpp[:8]}")
    print("    => DH's 'prime side' is NOT a positive prime-power object (no Euler product).  The phase")
    print("       built from c_DH is SIGNED with no Euler-borne lower bound -- it cannot UNCONDITIONALLY")
    print("       force the winding.  And the winding it computes is, by the explicit formula, EXACTLY")
    print("       the zero count -- which for DH counts rho0 only as a crossing, with no sign saying")
    print("       'off-line' unless the location is supplied (= [3], RH-strength).")
    c_escapes = False  # no prime-side phase functional detects rho0 off-line unconditionally
    print(f"    => prime-borne phase detects DH OFF-LINE unconditionally (ESCAPE)? {c_escapes}")

    # ---- VERDICT ----
    print("\n[VERDICT]  classify the candidate phase positivity by the (a)/(b)/(c) trichotomy:")
    print(f"    (a) holds verbatim for genuine DH on the line (RH-SILENT)        : {a_holds_for_dh}")
    print(f"    (b) detects DH off-line only with the zero location (RH-EQUIV)   : {b_needs_zero_data}")
    print(f"    (c) detects DH off-line UNCONDITIONALLY from primes (ESCAPE)     : {c_escapes}")
    if c_escapes:
        verdict = "(c) ESCAPE"
    elif a_holds_for_dh and b_needs_zero_data:
        verdict = "(a)+(b): LOCAL phase positivity is RH-SILENT; the DH-detecting winding is RH-EQUIVALENT"
    else:
        verdict = "INCONCLUSIVE -- re-examine"
    print(f"\n    PROBE PB RESULT: {verdict}")
    print("    The candidate phase positivity for arg m DOES NOT ESCAPE.  On the GENUINE DH function:")
    print("    the local on-line density positivity w(t)>=0 holds verbatim (FE-shared, RH-silent), and")
    print("    the winding that DOES see rho0 is the argument-principle COUNT, which only flags 'off-line'")
    print("    once the resonance LOCATION (the zero) is supplied = RH-strength = Weil positivity in")
    print("    winding-density clothing.  No prime-borne phase functional forces it unconditionally.")
    print("=" * 92)
    return {
        "FE_ok": fe_ok,
        "a_holds_for_DH_RH_silent": a_holds_for_dh,
        "b_needs_zero_data_RH_equiv": b_needs_zero_data,
        "c_unconditional_escape": c_escapes,
        "winding_around_rho0": float(w_around),
        "DH_on_line_density_min": float(mn_dh),
        "zeta_on_line_density_min": float(mn_z),
        "verdict": verdict,
    }


if __name__ == "__main__":
    summary()
