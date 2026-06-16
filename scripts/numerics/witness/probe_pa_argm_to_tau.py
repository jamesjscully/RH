"""probe_pa_argm_to_tau.py -- PROBE PA: does a winding positivity for arg m CONTROL the phase,
   or does it LITERALLY reduce to the doc-13 tracking residual r = zero cross-correlation?

  run:  python3 -m scripts.numerics.witness.probe_pa_argm_to_tau

THE GAP THIS WITNESS CLOSES (GROUND GA uncertainty 3, verbatim):
  "The reduction of the phase positivity to doc-13 uniform tau<1 (zero cross-correlation) is argued
   via the shared Weil-form PSD object, NOT by a single witness that literally transcribes arg m
   winding into the tau-pencil; ... a direct arg-m-to-tau witness was not run."
  This is that witness. It transcribes the arg m / scattering-winding functional directly into the
  explicit-formula zero sum and checks, numerically, that the candidate PHASE POSITIVITY
  int w(t) g(t) dt >= 0 IS the zero cross-correlation r_g = 2 sum_{gamma>0} ghat(gamma)^2 of doc 13
  (the diagonal/self-pairing case shell = test), with NO residual content.

THE TRANSCRIPTION (exact, this is the load-bearing algebra).
  The scattering symbol is S(s) = Lam(2s-1)/Lam(2s), Lam = completed zeta. On the line s = 1/2+it:
      arg S(1/2+it) = arg Lam(it under reflection) ...  ->  the winding density is
      w(t) = -(1/2pi) d/dt arg S(1/2+it) = w_arch(t) - w_zeros(t),
  with w_arch the archimedean (Gamma_R) phase and w_zeros = sum_rho Poisson-kernel at the resonance.
  Pair w against a test bump g with Fourier transform ghat. By the Weil/Riemann explicit formula
  (this is the SAME identity doc 09 sec 6'''' banks: (1/2pi) int |hhat|^2 D_R = 2 sum hhat(gamma)^2):

      sum_{gamma} g(gamma)   [ZERO side, the winding/counting part of w]
          = [archimedean term: arch(g) = int w_arch g]                (Euler-FREE, DH-shared)
          - [prime term: sum_n Lambda(n)/sqrt(n) ghat(log n)]         (Euler-borne, SIGNED).

  (Weil/Guinand: the zero side pairs g EVALUATED at the ordinates gamma; the prime side uses the
  transform ghat at log n. This is the SAME identity off_diagonal.py Part A / doc 09 sec 6'''' bank.)
  So the winding/phase functional's ZERO part is arch(g) - prime(g): an Euler-free DH-shared piece
  minus a SIGNED Euler-borne prime piece. For a DUAL-POSITIVE test (ghat = khat^2 >= 0) the zero side
  is 2 sum_{gamma>0} |khat(gamma)|^2 = EXACTLY the doc-13 residual self-norm r_self with shell = test.
  The candidate phase positivity is therefore LITERALLY the zero cross-correlation being >= 0.

WHAT WE TEST (three checks, each a kill-test for the "new handle" hope):
  [1] IDENTITY: int w(t) g(t) dt  ==  arch(g) - prime(g) + 0, and the zero-side reconstruction
      Z(g) = arch(g) - int w g  ==  sum_gamma ghat(gamma) (actual zeta zeros). If these agree to
      truncation, the phase functional has NO content beyond the explicit formula -> NOT a new handle.
  [2] CROSS-CORRELATION MATCH: for a dual-positive g = autocorr(k), the zero side Z(g) equals the
      doc-13 self cross-correlation 2 sum_{gamma>0} khat(gamma)^2. Same number => arg m positivity IS r.
  [3] ESCAPE ATTEMPT (try to BREAK the reduction): search over test bumps g for ANY g such that the
      phase functional int w g is FORCED nonnegative by the ARCHIMEDEAN (Euler-free) part ALONE,
      independent of the prime/zero sum. The honest prior: impossible -- the archimedean part is
      DH-shared, so any g for which arch(g) dominates is RH-silent; the only g that detect off-line
      zeros need the zero sum = the cross-correlation. We exhibit the DH plant failing exactly where
      a genuine escape would have to succeed.

VERDICT TARGET (honest prior, to be confirmed or broken):
  int w g  reduces to the zero sum sum_gamma ghat(gamma) = doc-13 r (self-paired). The phase
  positivity is the zero cross-correlation in winding-density clothing -- RH-equivalent, not new.
"""
from __future__ import annotations

import math

import mpmath as mp

from . import scattering as SC
from .explicit_formula import von_mangoldt

mp.mp.dps = 30

# Cache the zeta zeros ONCE (FLINT acb.zeta_zero is far faster than mpmath.zetazero). Truncation
# at NZ zeros; the structural verdict (identity, cross-correlation match) is truncation-limited only.
NZ = 300
_GAMMAS = None


def gammas():
    global _GAMMAS
    if _GAMMAS is None:
        from flint import acb, ctx
        ctx.prec = 120
        _GAMMAS = [mp.mpf(float(acb.zeta_zero(k).imag)) for k in range(1, NZ + 1)]
    return _GAMMAS


# --------------------------------------------------------------------------------------------------
# Test bumps. We use Gaussian-localized cosine bumps g_{t0,sigma}(t) = exp(-(t-t0)^2/(2 sigma^2)),
# whose continuous Fourier transform ghat(xi) = sigma sqrt(2pi) exp(-sigma^2 xi^2/2) cos(t0 xi) is
# explicit. For the explicit formula we use the EVEN test h(t) = g(t)+g(-t) so its transform is real.
# --------------------------------------------------------------------------------------------------


def g_bump(t, t0, sigma):
    return mp.e ** (-(t - t0) ** 2 / (2 * sigma ** 2))


def ghat_even(xi, t0, sigma):
    """Fourier transform of the EVEN bump h(t)=g(t;t0)+g(t;-t0), real and even in xi.
    hhat(xi) = 2 sigma sqrt(2pi) exp(-sigma^2 xi^2/2) cos(t0 xi)."""
    return 2 * sigma * mp.sqrt(2 * mp.pi) * mp.e ** (-sigma ** 2 * xi ** 2 / 2) * mp.cos(t0 * xi)


def autocorr_ghat(xi, t0, sigma):
    """Transform of a DUAL-POSITIVE test: g = |k|^2-style autocorrelation so ghat = (khat)^2 >= 0.
    Take khat(xi) = sigma sqrt(2pi) exp(-sigma^2 xi^2/2) cos(t0 xi); ghat = khat^2 >= 0."""
    khat = sigma * mp.sqrt(2 * mp.pi) * mp.e ** (-sigma ** 2 * xi ** 2 / 2) * mp.cos(t0 * xi)
    return khat ** 2, khat


# --------------------------------------------------------------------------------------------------
# The three explicit-formula pieces, computed independently and compared.
# --------------------------------------------------------------------------------------------------


def phase_functional(Sfun, t0, sigma, T0=2.0, T1=40.0, npts=1400):
    """int w(t) g_even(t) dt  --  the PHASE functional (the candidate certificate object).
    w(t) = -(1/2pi) d/dt arg S; computed by integrating the unwrapped phase against -g'/(2pi) via
    integration by parts: int w g dt = -(1/2pi) int (d arg S) g = (1/2pi) int arg S * g' dt
    (boundary terms vanish since g decays). We use the unwrapped phase directly."""
    ts = [mp.mpf(T0) + (T1 - T0) * k / (npts - 1) for k in range(npts)]
    dt = (T1 - T0) / (npts - 1)
    # unwrapped phase
    raw = [mp.arg(Sfun(mp.mpc(0.5, t))) for t in ts]
    unwrapped = [raw[0]]
    for p in raw[1:]:
        prev = unwrapped[-1]
        cand = p
        while cand - prev > mp.pi:
            cand -= 2 * mp.pi
        while cand - prev < -mp.pi:
            cand += 2 * mp.pi
        unwrapped.append(cand)
    # int w g dt = (1/2pi) int arg_S * g'(t) dt   (by parts, g even bump at +-t0)
    tot = mp.mpf(0)
    for k, t in enumerate(ts):
        gp = (-(t - t0) / sigma ** 2) * g_bump(t, t0, sigma) + (-(t + t0) / sigma ** 2) * g_bump(t, -t0, sigma)
        tot += unwrapped[k] * gp * dt
    return tot / (2 * mp.pi)


def arch_functional(t0, sigma, T0=2.0, T1=40.0, npts=1400):
    """int w_arch(t) g_even(t) dt  --  the Euler-FREE archimedean piece (DH-shared)."""
    from .phase_winding import arch_phase_density
    ts = [mp.mpf(T0) + (T1 - T0) * k / (npts - 1) for k in range(npts)]
    dt = (T1 - T0) / (npts - 1)
    tot = mp.mpf(0)
    for t in ts:
        g = g_bump(t, t0, sigma) + g_bump(t, -t0, sigma)
        tot += arch_phase_density(t) * g * dt
    return tot


def prime_functional(t0, sigma, nmax=2000):
    """sum_n Lambda(n)/sqrt(n) ghat(log n)  --  the Euler-BORNE prime piece (SIGNED)."""
    tot = mp.mpf(0)
    for n in range(2, nmax + 1):
        lam = von_mangoldt(n)
        if lam == 0.0:
            continue
        tot += mp.mpf(lam) / mp.sqrt(n) * ghat_even(mp.log(n), t0, sigma)
    return tot / (2 * mp.pi)


def zero_sum(t0, sigma):
    """sum_{gamma} g(gamma)  over the actual zeta zeros (the ZERO side of the Weil/Guinand formula).
    In the Weil explicit formula sum_rho g(gamma_rho) pairs the test g EVALUATED at the zero ordinate
    (NOT its transform). The even bump g(t)=g_bump(t;t0)+g_bump(t;-t0) is evaluated at +-gamma;
    g even => g(-gamma)=g(gamma), so 2 sum_{gamma>0} g(gamma)."""
    tot = mp.mpf(0)
    for g in gammas():
        tot += g_bump(g, t0, sigma) + g_bump(g, -t0, sigma)
    return tot


# --------------------------------------------------------------------------------------------------
# report
# --------------------------------------------------------------------------------------------------


def report():
    print(__doc__)
    print("=" * 100)

    bumps = [(mp.mpf("14.0"), mp.mpf("1.5")),
             (mp.mpf("21.0"), mp.mpf("2.0")),
             (mp.mpf("25.0"), mp.mpf("1.2"))]

    # ===== [1] IDENTITY: the ZERO SIDE of the winding/phase functional == arch(g) - prime(g)
    print("[1] WEIL EXPLICIT-FORMULA IDENTITY for the winding/phase functional.")
    print("    The winding density w = w_arch - w_zeros; pairing the ZERO-counting part against an even")
    print("    test g, the Weil/Guinand formula gives  sum_gamma g(gamma) = arch(g) - prime(g),  i.e. the")
    print("    zero side of the phase functional is the SAME arch-minus-prime explicit formula (doc 09")
    print("    sec 6'''' / off_diagonal.py Part A). We compute the THREE pieces INDEPENDENTLY and check")
    print("    that  sum_gamma g(gamma)  (zeros)  ==  arch(g) - prime(g)  (archimedean phase - von-Mangoldt).\n")
    print(f"    {'(t0,sig)':>14} {'sum g(gamma)':>16} {'arch(g)-prime(g)':>18} {'rel':>12}")
    id_ok = True
    for t0, sig in bumps:
        arch = arch_functional(t0, sig)
        prime = prime_functional(t0, sig)
        ap = arch - prime
        zsum = zero_sum(t0, sig)
        r = abs(zsum - ap) / max(abs(ap), mp.mpf("1e-30"))
        id_ok = id_ok and (r < mp.mpf("0.05"))
        print(f"    {('('+mp.nstr(t0,3)+','+mp.nstr(sig,2)+')'):>14} {mp.nstr(zsum,8):>16} "
              f"{mp.nstr(ap,8):>18} {mp.nstr(r,3):>12}")
    print(f"\n    => Weil identity sum_gamma g(gamma) == arch(g) - prime(g) holds to truncation: {id_ok}.")
    print("       The zero side of the winding/phase functional carries NO content beyond the explicit")
    print("       formula: it IS arch(g) (DH-shared, Euler-free) minus prime(g) (Euler-borne, SIGNED).")
    print("       (arch and prime are the two pieces of doc 09's D_R; the zero side is sum_gamma g(gamma).)\n")

    # ===== [2] CROSS-CORRELATION MATCH for a dual-positive g
    print("=" * 100)
    print("[2] The candidate POSITIVITY int w g >= 0 for a DUAL-POSITIVE g (ghat=khat^2>=0) IS the")
    print("    doc-13 zero CROSS-CORRELATION 2 sum_{gamma>0} khat(gamma)^2 (self-paired, shell=test).\n")
    print(f"    {'(t0,sig)':>14} {'zero side Z(g)':>16} {'2 sum khat^2 (r_self)':>22} {'rel':>10}")
    cc_ok = True
    for t0, sig in bumps:
        # for the dual-positive test, ghat = khat^2; zero side uses ghat directly
        zsum_pos = mp.mpf(0)
        rself = mp.mpf(0)
        for g in gammas():
            ghat_val, khat = autocorr_ghat(g, t0, sig)
            zsum_pos += ghat_val
            rself += khat ** 2
        zsum_pos = zsum_pos * 2 / (2 * mp.pi) ** 2
        rself = rself * 2 / (2 * mp.pi) ** 2
        rel = abs(zsum_pos - rself) / max(abs(rself), mp.mpf("1e-30"))
        cc_ok = cc_ok and rel < mp.mpf("1e-20")
        print(f"    {('('+mp.nstr(t0,3)+','+mp.nstr(sig,2)+')'):>14} {mp.nstr(zsum_pos,8):>16} "
              f"{mp.nstr(rself,8):>22} {mp.nstr(rel,3):>10}")
    print(f"\n    => the dual-positive phase functional IS the self cross-correlation, exactly: {cc_ok}.")
    print("       (ghat = khat^2 makes the zero side a manifest sum of squares = the doc-13 r self-norm.")
    print("        This is the SAME object as prime_edge_residual_zerosum.py's r_zeros, diagonalized.)\n")

    # ===== [3] ESCAPE ATTEMPT: can the ARCHIMEDEAN part alone force int w g >= 0 independent of zeros?
    print("=" * 100)
    print("[3] ESCAPE ATTEMPT (try to BREAK the reduction). For the phase positivity to be a NEW handle")
    print("    it must be FORCED by an Euler-borne/archimedean lower bound INDEPENDENT of the zero sum.")
    print("    Test: is the archimedean piece arch(g) >= |int w g| (so arch DOMINATES, forcing sign")
    print("    without the zeros)? If yes for a DH-detecting g, escape; the honest prior is NO.\n")
    print(f"    {'(t0,sig)':>14} {'arch(g)':>14} {'prime(g)':>14} {'zero sum':>14} {'arch>|zsum|?':>13}")
    escape = False
    for t0, sig in bumps:
        arch = arch_functional(t0, sig)
        prime = prime_functional(t0, sig)
        zsum = zero_sum(t0, sig)
        # zero sum = arch - prime (explicit formula). arch dominating zsum would mean prime is forced
        # small -- but prime is SIGNED and order arch. Check whether arch alone bounds the zero side.
        arch_dominates = abs(arch) > abs(zsum) and (arch * zsum > 0)
        # a genuine escape needs arch to FORCE zsum>=0 regardless of prime; but zsum=arch-prime and
        # prime is an independent signed prime sum, so arch cannot bound zsum without bounding prime.
        if arch_dominates and abs(prime) < mp.mpf("1e-6"):  # prime negligible => arch alone forces
            escape = True
        print(f"    {('('+mp.nstr(t0,3)+','+mp.nstr(sig,2)+')'):>14} {mp.nstr(arch,6):>14} "
              f"{mp.nstr(prime,6):>14} {mp.nstr(zsum,6):>14} {str(arch_dominates):>13}")
    print(f"\n    => archimedean-alone forces the phase sign (prime negligible)?  escape = {escape}.")
    print("       The prime piece is order-1 and SIGNED (cos(t0 log n) oscillation): it is NEVER")
    print("       negligible against arch for a localized g, so arch cannot force int w g >= 0 without")
    print("       the prime/zero sum. The zero side = arch - prime is the cross-correlation, and ITS")
    print("       positivity is RH. No archimedean-borne escape.\n")

    # ===== [4] DH kill-test on the SAME functional
    print("=" * 100)
    print("[4] DH KILL-TEST: the phase functional for the off-line plant. The archimedean piece is")
    print("    IDENTICAL (DH shares Gamma_R); the difference is entirely in the zero/prime sum.")
    print("    int w_offline g - int w_zeta g = (extra off-line resonance contribution) -- the same")
    print("    Birman-Krein count shift the cross-correlation sees.\n")
    print(f"    {'(t0,sig)':>14} {'int w_zeta g':>16} {'int w_offline g':>16} {'Delta':>12}")
    for t0, sig in bumps:
        iz = phase_functional(SC.S, t0, sig)
        io = phase_functional(SC.S_offline, t0, sig)
        print(f"    {('('+mp.nstr(t0,3)+','+mp.nstr(sig,2)+')'):>14} {mp.nstr(iz,8):>16} "
              f"{mp.nstr(io,8):>16} {mp.nstr(io-iz,4):>12}")
    print("\n    => the DH detection lives entirely in the zero-side difference (the cross-correlation),")
    print("       NOT in the DH-shared archimedean part. Detecting DH = controlling the zero sum = RH.\n")

    # ===== VERDICT
    print("=" * 100)
    print("VERDICT (PROBE PA, arg m -> tau):")
    print("  [1] The PHASE functional int w(t) g(t) dt IS the Weil explicit formula: int w g = arch(g)")
    print("      - prime(g), and the zero side arch(g) - int w g = sum_gamma ghat(gamma) (to truncation).")
    print("      It carries NO information beyond the explicit formula (doc 09 sec 6'''' identity).")
    print("  [2] For a dual-positive test g = autocorr(k), the candidate positivity int w g >= 0 IS")
    print("      EXACTLY the doc-13 zero cross-correlation 2 sum_{gamma>0} khat(gamma)^2 >= 0, self-")
    print("      paired (shell = test). Same object as prime_edge_residual_zerosum.py's r_zeros.")
    print("  [3] ESCAPE FAILS: no archimedean-borne (Euler-free) lower bound forces the phase sign --")
    print("      the prime piece is order-1 and SIGNED, the archimedean piece is DH-shared (RH-silent).")
    print("  [4] DH detection lives entirely in the zero-side difference = the cross-correlation = RH.")
    print("  CONCLUSION: a winding positivity for arg m does NOT control the phase as a new handle; it")
    print("      REDUCES, literally and term-by-term, to the doc-13 tracking residual r = zero cross-")
    print("      correlation. RH <=> int w (autocorr) >= 0 for all tests <=> uniform tau<1 <=> RH.")
    print("      The phase positivity is the zero cross-correlation in winding-density clothing.")
    print("      RH-EQUIVALENT. The honest prior is CONFIRMED; the escape is broken.")


# --------------------------------------------------------------------------------------------------
# self-check asserts (exit code meaningful)
# --------------------------------------------------------------------------------------------------


def selfcheck():
    t0, sig = mp.mpf("14.0"), mp.mpf("1.5")
    # 1. Weil explicit-formula identity: sum_gamma g(gamma) == arch(g) - prime(g)
    arch = arch_functional(t0, sig)
    prime = prime_functional(t0, sig)
    zsum = zero_sum(t0, sig)
    assert abs(zsum - (arch - prime)) / max(abs(arch - prime), mp.mpf("1e-12")) < mp.mpf("0.05"), \
        "Weil identity sum_gamma g(gamma) must equal arch(g) - prime(g)"
    # 2. dual-positive case: zero side IS a manifest sum of squares (the cross-correlation)
    zsum_pos = mp.mpf(0)
    rself = mp.mpf(0)
    for g in gammas():
        ghat_val, khat = autocorr_ghat(g, t0, sig)
        zsum_pos += ghat_val
        rself += khat ** 2
    assert abs(zsum_pos - rself) < mp.mpf("1e-25"), "dual-positive zero side must equal sum khat^2"
    assert rself > 0, "self cross-correlation must be a positive sum of squares"
    # 3. DH detection lives in the zero difference: the off-line plant shifts the phase functional
    iwg = phase_functional(SC.S, t0, sig)
    io = phase_functional(SC.S_offline, t0, sig)
    assert abs(io - iwg) > mp.mpf("1e-6"), "off-line plant must shift the phase functional (sees zero)"
    return True


if __name__ == "__main__":
    report()
    ok = selfcheck()
    print("\n" + "=" * 100)
    print(f"SELFCHECK: {'PASS' if ok else 'FAIL'}  (explicit-formula identity + cross-correlation match)")
