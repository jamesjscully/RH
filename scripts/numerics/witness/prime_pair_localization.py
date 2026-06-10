"""R-SQ experiment E3a': localization calibration of the phase-free detector.

E3a showed the doubled form separates zeta from DH from coefficients alone,
but could not test LOCALIZATION (DH has off-line zeros at scattered heights,
so every frequency cell was hot). Here we calibrate the instrument on a
controlled object: the zero multiset is zeta's first K ordinates with EXACTLY
ONE pair moved off the line,

    gamma_j -> gamma_j +- i sigma   (gamma_j ~ 30.42, sigma = 0.25),

term replaced by Re[cos((gamma_j + i sigma) t) hhat(gamma_j + i sigma)^2]
(count- and normalization-preserving synthetic perturbation; we are testing
the DETECTOR, not nature - the coefficient-side reality of the mechanism was
established by the DH cell of E3a).

Cells: {on-line, perturbed@30.4} x {test tuned to gamma* = 30, 85.7}.
Fail-closed readings fixed in advance:
  * excess slope ONLY in (perturbed, gamma* = 30): the detector is
    frequency-localized; quantify the threshold.
  * excess in (perturbed, 85.7) too: the square's growth leaks across
    frequency - localization fails, and E3b inherits that the doubled form
    detects globally but cannot point.
  * no excess anywhere: the synthetic perturbation at sigma = 0.25 is below
    the detector's floor at this support - raise sigma until visible and
    report the threshold curve.

Run:
    python3 -m scripts.numerics.witness.prime_pair_localization
"""
import math
import numpy as np

from scripts.numerics.witness.fork_lib import zeta_gammas

c0, hw = 2.0, 0.5
K = 3000
T_MAX, SIG = 5.0, 0.25

ub = np.linspace(c0 - hw, c0 + hw, 4001)
bump0 = np.cos(np.pi * (ub - c0) / (2 * hw)) ** 8
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
gam = zeta_gammas(K)
j_target = int(np.argmin(np.abs(gam - 30.0)))


def p(z):
    return z * z * (z * z + 0.25)


def hhat2_at(zs, gstar):
    """hhat(z)^2 = (p(z) Ghat(z))^2 for the gamma*-modulated test; complex ok."""
    zs = np.atleast_1d(zs)
    bump = bump0 * np.cos(gstar * ub)
    out = np.empty(len(zs), dtype=complex)
    for i in range(0, len(zs), 500):
        zz = zs[i:i + 500][:, None]
        Gh = 2.0 * trap(bump[None, :] * np.cos(zz * ub[None, :]), x=ub, axis=1)
        out[i:i + 500] = (p(zz[:, 0]) * Gh) ** 2
    return out


tg = np.linspace(0.0, T_MAX, 1001)
T0s = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)

print(f"perturbation: gamma_{j_target+1} = {gam[j_target]:.4f} moved off-line, "
      f"sigma = {SIG}; K = {K}")
print("\nD(T0), zero side; slope fit on [3,5]")
print("zeroset      g*     " + "".join(f"D({x:.1f})".rjust(11) for x in T0s) + "   slope")
slopes = {}
for gstar in (30.0, 85.7):
    w_on = hhat2_at(gam, gstar).real            # on-line: hhat real
    zc = gam[j_target] + 1j * SIG
    w_off = hhat2_at(np.array([zc]), gstar)[0]  # complex weight at moved zero
    for label in ("on-line", "perturbed"):
        if label == "on-line":
            Av = np.array([float(np.sum(np.cos(gam * t) * w_on)) for t in tg])
        else:
            Av = np.array([
                float(np.sum(np.cos(gam * t) * w_on)
                      - np.cos(gam[j_target] * t) * w_on[j_target]
                      + np.real(np.cos(zc * t) * w_off)) for t in tg])
        Ds = []
        for T0 in T0s:
            m = tg <= T0
            Ds.append(2.0 * float(trap((1 - tg[m] / T0) * Av[m] ** 2, x=tg[m])))
        xs = np.array([x for x in T0s if x >= 3.0])
        ys = np.log([d for x, d in zip(T0s, Ds) if x >= 3.0])
        slope = float(np.polyfit(xs, ys, 1)[0])
        slopes[(label, gstar)] = slope
        print(f"{label:10s}  {gstar:5.1f} " +
              "".join(f"{d:11.3e}" for d in Ds) + f"   {slope:+.3f}")

print("\n[localization verdict]")
e_near = slopes[("perturbed", 30.0)] - slopes[("on-line", 30.0)]
e_far = slopes[("perturbed", 85.7)] - slopes[("on-line", 85.7)]
print(f"  slope excess at the tuned frequency (30):   {e_near:+.3f}  "
      f"(2 sigma = {2*SIG:.2f} is the asymptotic rate)")
print(f"  slope excess at the far frequency (85.7):   {e_far:+.3f}")
print("""
Reading: excess at 30 and ~none at 85.7 = the phase-free detector is
frequency-localized (pass). Excess both places = leak (constrains E3b).
None anywhere = below threshold at this support; raise sigma.
""")

# --- threshold curve: slope excess vs sigma at the tuned frequency -----------
print("[threshold curve] tuned test (g* = 30), slope excess vs sigma:")
gstar = 30.0
w_on = hhat2_at(gam, gstar).real
base = slopes[("on-line", 30.0)]
for sig in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
    zc = gam[j_target] + 1j * sig
    w_off = hhat2_at(np.array([zc]), gstar)[0]
    Av = np.array([
        float(np.sum(np.cos(gam * t) * w_on)
              - np.cos(gam[j_target] * t) * w_on[j_target]
              + np.real(np.cos(zc * t) * w_off)) for t in tg])
    Ds = []
    for T0 in (3.0, 3.5, 4.0, 4.5, 5.0):
        m = tg <= T0
        Ds.append(2.0 * float(trap((1 - tg[m] / T0) * Av[m] ** 2, x=tg[m])))
    slope = float(np.polyfit(np.array((3.0, 3.5, 4.0, 4.5, 5.0)), np.log(Ds), 1)[0])
    print(f"  sigma = {sig:4.2f}: slope = {slope:+.3f}  excess = {slope - base:+.3f}  "
          f"(asymptotic rate 2 sigma = {2*sig:.2f})")
print("\nDetection threshold at support R=5 = the sigma where excess becomes")
print("clearly positive; compare with the one-variable detection lemma, which")
print("at the same support needs phase engineering or interpolation AT the zero.")
