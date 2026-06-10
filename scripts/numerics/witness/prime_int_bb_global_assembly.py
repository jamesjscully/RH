"""PFD step 2 (worker BB): the GLOBAL ASSEMBLY gate - does the EF's
archimedean constant -(1/2) log pi (the 1/(2pi) scale, doc 20 C2) emerge
from the cross-place trace of the product-formula-glued PFD object?

THE OBJECT (research/work/BB-global-assembly.md sec 2): D_glob =
( {G_p}_p, (V_oo, Theta_oo)_kappa ; iota ), where G_p is the glued local
object (Z's construction at p = 2; odd p assumed-structural from doc 24:
two-sided weight lattice, perfect residue pairing m <-> -m, c = 1/2
forced determinant layer p^{w/2}(1 - p^{-w}), vertical spacing
2 pi i/log p, glued trace = lattice comb at p^{-s} = 1, anomalous
dimension 0); the degenerate sector is the half-ladder {nu + s/2}
regularized at UNKNOWN scale kappa,

    D_oo,kappa(s) = prod_reg((nu + s/2)/kappa)
                  = kappa^{-(1-s)/2} sqrt(2pi)/Gamma(s/2),

and iota = the product formula spent as identification (AA Thm AA.1:
log N = sum_p v_p log p exactly on the character lattice). Gate
observable: c_oo(kappa) = -(1/2) log kappa, the constant multiplying
the degenerate sector in the critical-line density.

PRE-REGISTERED READINGS (fixed in the BB doc before first run):
  B1: kappa = pi forced by the assembly  -> K1 discharged globally.
  B2: a different constant forced        -> report exactly + Q-SCHEME.
  B3: no constant determined (assembly still scale-free) -> name the
      exact missing ingredient.  EXPECTED: B3, via Proposition BB.1
      (every banked input is invariant under kappa -> lambda kappa,
      while the observable is not: no function of the inputs can
      determine kappa), sharpened by BB-r1 (FE layer kappa-blind:
      paired anomaly = 1/2 constant) and BB-r2 (the 2pi is present in
      the comb normalization but extractable only by a comb-vs-
      continuum comparison = the archimedean Poisson exchange).

FAIL-CLOSED GATES:
  GB1 (local combs / Poisson at finite places): the Abel-regularized
      glued trace of G_p pairs with Gaussian test functions as the
      lattice comb (2pi/log p) sum_n phi(2pi n/log p), p in {2,3,5}:
      rel err < 1e-5 at eps = 1e-6 AND monotone decreasing in eps.
      (This convergence IS Poisson summation on (log p)Z <-> its dual:
      the exchange works at finite places.)
  GB2 (Prop BB.1, scale-blindness exact):
      (a) full-ladder anomaly zeta_full(0) = 0, |.| < 1e-12 (all p, s);
      (b) glued trace 1/(1-x) + 1/(1-1/x) - 1 == 0 in EXACT rational
          arithmetic (Fraction), several rational x;
      (c) product formula integer-exact: prod_p p^{v_p(A)} == A
          (recomposition) for ALL A <= 20000, and the log identity to
          1e-9 - inputs contain only {log p}, no kappa;
      (d) the observable moves: D_oo,{lambda kappa}/D_oo,kappa =
          lambda^{-(1-s)/2} to 1e-12 (kappa-dependence isolated in the
          degenerate sector).
  GB3 (BB-r1, FE layer kappa-blind): zeta_H(0, s/2) + zeta_H(0,(1-s)/2)
      = 1/2 exactly (< 1e-12, complex grid); the FE-paired ratio
      [D_{lk}(s) D_{lk}(1-s)] / [D_k(s) D_k(1-s)] = lambda^{-1/2},
      CONSTANT IN s, to 1e-12.
  GB4 (comparison only, F-a-flagged): -d/ds log D_oo,kappa(1/2 + it) =
      -(1/2) log kappa + (1/2) psi(1/4 + it/2) (< 1e-5, kappa in
      {1, e, pi, 2pi}); the EF shadow constant -(1/2) log pi selects
      kappa* = pi uniquely (monotone solve, < 1e-12); Q-SCHEME unit
      translation re-witnessed: prod_reg((nu+z)/2pi) = Gamma_C(z)^{-1}
      (Deninger Prop 2.1 line 2, < 5e-13) and classical duplication
      Gamma_R(s) Gamma_R(s+1) = 2 Gamma_C(s) (< 5e-13): pi on the
      folded spacing-2 ladder = 2pi on the unfolded spacing-1 ladder,
      2-powers EF-invisible.
  GB5 (BB-r2, weight = spacing): the comb atom weight extracted by a
      localized Gaussian at t_1 = 2pi/log p equals the spacing:
      weight * log p / (2pi) = 1 to 1e-5 (p = 2, 3) - per-place
      observables are scale-free; the 2pi is present but needs a
      continuum partner to be read off.

Run:
    python3 -m scripts.numerics.witness.prime_int_bb_global_assembly
"""
import cmath
import math
import sys
from fractions import Fraction

import flint

flint.ctx.prec = 333
FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def acb(z):
    z = complex(z)
    return flint.acb(z.real, z.imag)


def C(x):
    return complex(float(x.real.mid()), float(x.imag.mid()))


H = flint.arb(1) / flint.arb(10) ** 30


def zh0(a):
    """zeta_H(0, a) (= 1/2 - a)."""
    return C(acb(0.0).zeta(acb(a)))


def zh_d0(a):
    """d/du zeta_H(u, a) at u = 0 (flint central difference, step 1e-30)."""
    hh = flint.acb(H, 0)
    return C((hh.zeta(acb(a)) - (-hh).zeta(acb(a))) / (2 * hh))


def reg_half(a, kappa):
    """prod_reg_{nu>=0} ((nu + a)/kappa) = kappa^{-zh0(a)} e^{-zh'(0,a)}."""
    return cmath.exp(-zh_d0(a) - math.log(kappa) * zh0(a))


def d_oo(s, kappa):
    """Degenerate-sector determinant D_oo,kappa(s) (ladder a = s/2)."""
    return reg_half(complex(s) / 2.0, kappa)


SQ2PI = math.sqrt(2 * math.pi)
PI = math.pi

# ------------------------------------------------------------------ GB1
print("GB1: glued trace of G_p = lattice comb (Poisson at finite places)")


def comb_pairing(p, eps, t0=0.0, sigma=1.0):
    """<glued trace of G_p (Abel eps-regularized), phi> for the Gaussian
    phi(t) = exp(-(t - t0)^2 / (2 sigma^2)).  The two branches give
    sum_{m in Z} p^{-|m| eps} phihat(m log p) e^{i m log p t0} (real part),
    phihat(u) = sigma sqrt(2pi) exp(-sigma^2 u^2 / 2)."""
    L = math.log(p)
    total = 0.0
    m = 0
    while True:
        ph = sigma * SQ2PI * math.exp(-(sigma * m * L) ** 2 / 2.0)
        if m > 0 and ph < 1e-22:
            break
        term = ph * math.cos(m * L * t0) * math.exp(-m * eps * L)
        total += term if m == 0 else 2 * term
        m += 1
    return total


def comb_target(p, t0=0.0, sigma=1.0):
    """(2pi/log p) sum_n phi(2pi n / log p)."""
    L = math.log(p)
    sp = 2 * PI / L
    total, n = 0.0, 0
    while True:
        tn = n * sp
        v = math.exp(-(tn - t0) ** 2 / (2 * sigma ** 2)) + (
            math.exp(-(-tn - t0) ** 2 / (2 * sigma ** 2)) if n > 0 else 0.0)
        if n > 0 and v < 1e-22:
            break
        total += v
        n += 1
    return sp * total


worst1 = 0.0
mono_ok = True
for p in (2, 3, 5):
    tgt = comb_target(p)
    errs = []
    for eps in (1e-2, 1e-4, 1e-6):
        err = abs(comb_pairing(p, eps) - tgt) / tgt
        errs.append(err)
    mono_ok = mono_ok and (errs[0] >= errs[1] >= errs[2])
    worst1 = max(worst1, errs[2])
    print(f"    p = {p}: rel errs (eps 1e-2,1e-4,1e-6) = "
          f"{errs[0]:.2e}, {errs[1]:.2e}, {errs[2]:.2e}")
check("comb identity", worst1 < 1e-5 and mono_ok,
      f"Abel-limit glued trace -> (2pi/log p) comb; worst rel "
      f"{worst1:.2e}, monotone {mono_ok} (= Poisson on (log p)Z)")

# ------------------------------------------------------------------ GB2
print("\nGB2: Proposition BB.1 - every banked input is kappa-free; the")
print("     observable is not (scale-blindness is exact)")

# (a) full-ladder anomaly = 0 at finite places
worst2a = 0.0
for p in (2.0, 3.0, 5.0):
    om = 2 * PI / math.log(p)
    for s in (0.75, 1.5, 0.5 + 3.0j):
        zv = complex(s)
        f0 = 1.0 + zh0(1 - 1j * zv / om) + zh0(1 + 1j * zv / om)
        worst2a = max(worst2a, abs(f0))
check("(a) G_p scale-free", worst2a < 1e-12,
      f"zeta_full(0) = 0; worst |.| {worst2a:.2e}")

# (b) glued trace == 0, exact rationals
bad_b = []
for x in (Fraction(2, 3), Fraction(5, 7), Fraction(-3, 2), Fraction(10),
          Fraction(1, 10), Fraction(-1, 5), Fraction(99, 100)):
    v = 1 / (1 - x) + 1 / (1 - 1 / x) - 1
    if v != 0:
        bad_b.append((x, v))
check("(b) glued trace = 0 exactly", not bad_b,
      f"1/(1-x) + 1/(1-1/x) - 1 == 0 (Fraction); violations: {bad_b}")

# (c) product formula integer-exact, A <= 20000; values in Q-span{log p}
bad_c = []
worst2c = 0.0
for A in range(2, 20001):
    m, rec, lg = A, 1, 0.0
    pp = 2
    while pp * pp <= m:
        if m % pp == 0:
            e = 0
            while m % pp == 0:
                m //= pp
                e += 1
            rec *= pp ** e
            lg += e * math.log(pp)
        pp += 1
    if m > 1:
        rec *= m
        lg += math.log(m)
    if rec != A:
        bad_c.append(A)
    worst2c = max(worst2c, abs(lg - math.log(A)))
check("(c) product formula exact", not bad_c and worst2c < 1e-9,
      f"prod p^v_p == A recomposed for all A <= 20000; "
      f"worst |log N - sum v_p log p| {worst2c:.2e}; no kappa anywhere")

# (d) the observable moves under kappa -> lambda kappa
worst2d = 0.0
for s in (0.5, 1.0, 0.5 + 14.134725j, 2.5 - 1.0j):
    for lam in (2.0, PI):
        r = d_oo(s, lam * PI) / d_oo(s, PI)
        tgt = lam ** (-(1 - complex(s)) / 2)
        worst2d = max(worst2d, abs(r - tgt) / abs(tgt))
check("(d) observable not kappa-free", worst2d < 1e-12,
      f"D_oo ratio = lambda^(-(1-s)/2), worst rel {worst2d:.2e} -- "
      f"moves while (a)-(c) are bit-identical: B3 by equivariance")

# ------------------------------------------------------------------ GB3
print("\nGB3: BB-r1 - the FE layer of the assembly is kappa-blind")
worst3a = 0.0
for s in (0.3, 0.5, 1.0, 0.5 + 14.134725j, 2.0 - 3.0j):
    v = zh0(complex(s) / 2) + zh0((1 - complex(s)) / 2)
    worst3a = max(worst3a, abs(v - 0.5))
check("paired anomaly = 1/2", worst3a < 1e-12,
      f"zeta_H(0,s/2) + zeta_H(0,(1-s)/2) = 1/2 const; worst {worst3a:.2e}")
worst3b = 0.0
for s in (0.3, 0.5, 1.0, 0.5 + 14.134725j, 2.0 - 3.0j):
    for lam in (2.0, PI):
        num = d_oo(s, lam * PI) * d_oo(1 - complex(s), lam * PI)
        den = d_oo(s, PI) * d_oo(1 - complex(s), PI)
        worst3b = max(worst3b, abs(num / den - lam ** -0.5))
check("FE ratio kappa-independent", worst3b < 1e-12,
      f"paired kappa-dependence = lambda^(-1/2), s-independent; worst "
      f"{worst3b:.2e} -- the FE holds for EVERY kappa (doc 21 sec 4 "
      f"guard, quantitative)")

# ------------------------------------------------------------------ GB4
print("\nGB4: density layer (COMPARISON ONLY, F-a-flagged): the constant")
print("     is -(1/2) log kappa; the EF shadow selects kappa* = pi")
worst4a = 0.0
hs = 1e-6
for kappa in (1.0, math.e, PI, 2 * PI):
    for t in (0.0, 14.134725, 25.0):
        s = 0.5 + 1j * t
        fd = -(cmath.log(d_oo(s + hs, kappa))
               - cmath.log(d_oo(s - hs, kappa))) / (2 * hs)
        dg = 0.5 * C(flint.acb(0.25, t / 2).digamma())
        tgt = -0.5 * math.log(kappa) + dg
        worst4a = max(worst4a, abs(fd - tgt))
check("density = -(1/2)log kappa + (1/2)psi(1/4+it/2)", worst4a < 1e-5,
      f"worst err {worst4a:.2e} over kappa in (1, e, pi, 2pi)")
c_target = -0.5 * math.log(PI)        # EF shadow constant (comparison)
kappa_star = math.exp(-2 * c_target)  # monotone solve of -(1/2)log k = c
check("EF shadow selects kappa* = pi", abs(kappa_star - PI) < 1e-12,
      f"kappa* = {kappa_star:.15f} (unique: -(1/2)log kappa monotone); "
      f"COMPARISON ONLY -- target of the missing theorem, not derived")
worst4c = 0.0
for z in (0.5, 1.0, 2.5, 0.5 + 14.134725j):
    lhs = reg_half(complex(z), 2 * PI)
    rhs = (2 * PI) ** complex(z) / cmath.exp(C(acb(z).lgamma()))
    worst4c = max(worst4c, abs(lhs - rhs) / abs(rhs))
check("unfolded unit: prod((nu+z)/2pi) = Gamma_C(z)^-1", worst4c < 5e-13,
      f"worst rel {worst4c:.2e} (spacing-1 ladder, scale 2pi)")
worst4d = 0.0
for s in (0.3, 1.2, 0.5 + 2.0j):
    s = complex(s)
    gR = lambda z: PI ** (-z / 2) * cmath.exp(C(acb(z / 2).lgamma()))
    gC = (2 * PI) ** (-s) * cmath.exp(C(acb(s).lgamma()))
    worst4d = max(worst4d, abs(gR(s) * gR(s + 1) - 2 * gC) / abs(gC))
check("duplication: Gamma_R Gamma_R(+1) = 2 Gamma_C", worst4d < 5e-13,
      f"worst rel {worst4d:.2e} -- kappa = pi (folded) = 2pi (unfolded), "
      f"2-powers EF-invisible (doc 20 C3)")

# ------------------------------------------------------------------ GB5
print("\nGB5: BB-r2 - comb atom weight = spacing (the 2pi is present but")
print("     per-place unextractable)")
worst5 = 0.0
for p in (2, 3):
    L = math.log(p)
    t1 = 2 * PI / L
    sig = 0.5
    pair = comb_pairing(p, 1e-7, t0=t1, sigma=sig)
    # neighbors at distance >= spacing contribute < e^-160: weight = pair
    weight = pair / 1.0
    ratio = weight * L / (2 * PI)
    worst5 = max(worst5, abs(ratio - 1.0))
    print(f"    p = {p}: atom weight = {weight:.8f}  "
          f"(2pi/log p = {2 * PI / L:.8f})")
check("weight/spacing = 1", worst5 < 1e-5,
      f"worst |ratio - 1| {worst5:.2e}: per-place scale-free; the 2pi "
      f"needs a comb-vs-CONTINUUM comparison (the archimedean Poisson "
      f"exchange) to be read off")

print(f"""
VERDICT (pre-registered): GB1-GB5 PASS => B3, full-value: NO constant is
determined by the assembly -- and provably none CAN be (Prop BB.1: all
banked inputs are exactly invariant under kappa -> lambda kappa while
the gate observable -(1/2) log kappa is not; B3 by equivariance, exact,
independent of all numerics here).  Sharpenings: (BB-r1) the FE-paired
degenerate anomaly is the CONSTANT 1/2, so the assembly's functional
equation holds for every kappa -- the constant is a DENSITY-layer datum
and properness-as-FE is structurally vacuous for it; (BB-r2) the 2pi is
already in the object (comb weight = spacing = 2pi/log p; the Poisson
exchange works at finite places); the single missing ingredient is the
ARCHIMEDEAN Poisson exchange (the self-dual unit / degenerate-sector
coupling), whose required output is kappa = pi (folded) = 2pi (unfolded)
-- the comb normalization itself, transported to the infinite place.
""")
print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
