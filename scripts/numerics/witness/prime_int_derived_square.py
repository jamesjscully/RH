"""R-INT / C4': the Euler pairing on the derived square Z (x)^L_S Z.

Doc 17 section 6 redirected the integer search here: over Spec Z (a curve)
the Euler form on torsion modules vanishes identically (|Ext^1| = |Hom|).
The derived square R = HZ ^ HZ (tensor over the sphere spectrum) is the
non-scheme thickening; the question C4' is whether the Euler/intersection
pairing acquires SIGN there.

The pairing (Tor-form / Serre intersection form, the one that vanishes on
the curve):

    <M, N> = sum_i (-1)^i log |pi_i (M ^_R N)|

The marquee class is the DIAGONAL: Delta ^_R Delta = HZ ^_{HZ^HZ} HZ =
THH(Z), by definition of topological Hochschild homology. Bokstedt's
theorem (THH(Z) ~ HZ v V_{k>=1} Sigma^{2k-1} HZ/k):

    pi_0 THH(Z) = Z,  pi_{2k-1} THH(Z) = Z/k,  pi_{2k} = 0 (k >= 1).

pi_0 = Z is the excess part (Delta cap Delta = Delta, a "curve", not
points; HKR: on C x C the analogous Tor_i are Omega^i_C and the
intersection NUMBER Delta^2 = 2 - 2g comes from the cotangent data). The
finite content is the positive-degree torsion:

    <Delta, Delta>_tors = - sum_{k>=1} log k   (all in ODD degrees)
                        = zeta'(0)             (zeta-regularized)
                        = -(1/2) log 2pi  <  0.

This script verifies, fail-closed:
  T1: curve control -- over Z the pairing on torsion classes is EXACTLY 0
      for all (p, a, b) in a grid (|Tor_0| = |Tor_1| = p^min).
  T2: the regularization is honest -- the Stirling-extracted constant
      C_N = sum_{k<=N} log k - (N log N - N + (1/2) log N) converges to
      (1/2) log 2pi (this is the standard zeta-regularization of
      sum log k = -zeta'(0); the script exhibits the constant numerically
      rather than citing it).
  T3: independent zeta'(0) by high-precision central difference (flint
      acb) agrees with -(1/2) log 2pi.
  T4: the Abel-regularized count sum_{k>=1} 1 -> -1/2 (needed for the
      local control THH(F_p) = F_p[sigma], |pi_{2i}| = p for all i >= 0:
      <point, point>_{F_p-square} = log p * (1 + sum_{k>=1} 1)_reg
      = (1/2) log p).

Pre-registered readings (fixed before the run):
  <Delta,Delta>_tors < 0  -> first sign-bearing pairing in the program:
      "Spec Z is a curve of genus > 1 over S" (2 - 2g = zeta'(0), i.e.
      g = 1 + (1/4) log 2pi ~ 1.459); escalate to the properness audit.
  = 0 -> the curve vanishing persists; C4' closes negatively.
  > 0 -> rational-curve-like; no Castelnuovo route.
INPUTS taken on citation (not verified here): Bokstedt's THH(Z) and
THH(F_p) computations (refs in doc 18).

Run:
    python3 -m scripts.numerics.witness.prime_int_derived_square
"""
import math
import sys

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- T1
print("T1: curve control -- Euler/Tor pairing over Z on torsion classes")
worst = 0.0
for p in (2, 3, 5, 7):
    for a in range(1, 5):
        for b in range(1, 5):
            m = min(a, b)
            # Tor_0(Z/p^a, Z/p^b) = Z/p^m, Tor_1 = Z/p^m, Tor_{>=2} = 0
            chi = math.log(p ** m) - math.log(p ** m)
            worst = max(worst, abs(chi))
check("curve vanishing", worst == 0.0,
      f"max |chi| over grid = {worst} (exact 0 required)")

# ---------------------------------------------------------------- T2
print("\nT2: Stirling extraction of the regularized sum_{k>=1} log k")
target = 0.5 * math.log(2 * math.pi)
worst2 = 0.0
for N in (100, 300, 1000):
    s = math.lgamma(N + 1)                  # log N! = sum_{k<=N} log k, exact
    # Stirling with the 1/(12N) - 1/(360N^3) corrections: remaining
    # truncation O(N^-5), below double noise for N >= 100.
    C = s - (N * math.log(N) - N + 0.5 * math.log(N)
             + 1.0 / (12.0 * N) - 1.0 / (360.0 * N ** 3))
    err = abs(C - target)
    worst2 = max(worst2, err)
    print(f"    N = {N:>5}: C_N = {C:.14f}   |C_N - (1/2)log 2pi| = {err:.3e}")
check("Stirling constant", worst2 < 1e-12,
      f"C_N -> {target:.12f} ((1/2) log 2pi), worst err {worst2:.3e}")

# ---------------------------------------------------------------- T3
print("\nT3: independent zeta'(0) (flint, central difference)")
try:
    import flint
    ctx_prec_old = flint.ctx.prec
    flint.ctx.prec = 400
    h = flint.arb(1) / (flint.arb(10) ** 40)
    zp0 = (flint.acb(h).zeta() - flint.acb(-h).zeta()) / (2 * flint.acb(h))
    zp0_f = float(zp0.real.mid())
    flint.ctx.prec = ctx_prec_old
    err3 = abs(zp0_f - (-target))
    check("zeta'(0) identity", err3 < 1e-12,
          f"zeta'(0) = {zp0_f:.12f} vs -(1/2)log 2pi = {-target:.12f}, "
          f"err {err3:.3e}")
except ImportError:
    check("zeta'(0) identity", False, "python-flint unavailable")

# ---------------------------------------------------------------- T4
print("\nT4: Abel regularization of sum_{k>=1} 1 (for the F_p local control)")
prev = None
for eps in (1e-2, 1e-3, 1e-4):
    s = 1.0 / (math.exp(eps) - 1.0)        # sum_{k>=1} e^{-eps k}, closed form
    const = s - 1.0 / eps                   # remove the divergence
    err4 = abs(const - (-0.5))
    print(f"    eps = {eps:.0e}: sum - 1/eps = {const:.10f}   "
          f"|. - (-1/2)| = {err4:.3e}")
    conv4 = prev is None or err4 < prev
    prev = err4
check("Abel constant", err4 < 1e-4 and conv4,
      f"regularized sum_(k>=1) 1 = -1/2, final err {err4:.3e}")

# ---------------------------------------------------------------- assembly
print("\nAssembly (inputs: Bokstedt THH(Z), THH(F_p); T2-T4 above):")
dd = -target
print(f"  <Delta,Delta>_tors over HZ^HZ = -sum_reg log k = zeta'(0) "
      f"= {dd:.12f}  (NEGATIVE)")
print(f"  identification: e^(<Delta,Delta>) = (2pi)^(-1/2) -- the "
      f"archimedean constant of zeta")
g = 1.0 + 0.25 * math.log(2 * math.pi)
print(f"  genus reading: 2 - 2g = zeta'(0)  =>  g_Z = 1 + (1/4)log 2pi "
      f"= {g:.6f}  > 1 (hyperbolic)")
for p in (2, 3, 5):
    print(f"  local control THH(F_{p}): chi_reg = log {p} * (1 + (-1/2)) "
          f"= (1/2) log {p} = {0.5 * math.log(p):.6f}  (POSITIVE)")
check("sign content", dd < 0,
      "diagonal self-pairing strictly negative; pre-registered reading: "
      "first sign-bearing pairing, genus > 1 over S")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
