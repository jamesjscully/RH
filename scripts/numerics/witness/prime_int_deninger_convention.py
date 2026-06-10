"""R-INT / C5'' (a)(iii) + (c)(i): reconciliation of doc 20's regularized
products with Deninger's actual conventions (primary sources, archived:
refs/deninger1991-gamma-factors.pdf = Invent. math. 104 (1991) 245-261;
refs/deninger1992-local-l-factors.pdf = Invent. math. 107 (1992) 135-150;
refs/hesselholt2016-thh-hasse-weil.pdf = arXiv:1602.01980, Section 7).

THE DISCREPANCY UNDER TEST. Doc 20 gate W3 verified

    prod_sym_{n in Z} (z + 2 pi i n / log q) = 2 sinh((log q) z / 2)
                                             = q^{z/2} (1 - q^{-z})

under the SYMMETRIC scheme (pair n with -n into the real factors
z^2 + omega^2 n^2, regularize the paired half-ladder) and attributed the
closed form to "Deninger's local-factor-as-regularized-determinant
identity". Deninger's printed identity (1992, Prop. 2.3 - he calls it "a
miracle"; quoted by Hesselholt as [15, Cor. 2.8] via his Prop. 7.1 and
Remark 7.2) is

    det_inf( (log q / 2 pi i)(s - Theta) | L_lambda ) = 1 - lambda q^{-s},

WITHOUT the self-dual prefactor q^{s/2}. His convention (1992, (2.1)-(2.2)):
rotate the vertical ladder to the real ladder z + nu (nu in Z) by the
complex scale log q/(2 pi i), choose arg(z + a_nu) in (-3pi/2, pi/2] for
|nu| >> 0, i.e. arg(z - nu) = arg(nu - z) - pi on the negative half. The
two schemes differ by EXACTLY q^{z/2} - the half-sum (vacuum-energy /
Weyl-vector) term of the ladder. Consequence checks: with the symmetric
scheme Hesselholt's Theorem A would FAIL already for X = Spec F_q
(zeta = 1/(1-q^{-s}), not 1/(q^{s/2}(1-q^{-s}))): the homotopy-theoretic
theorem as proved selects Deninger's scheme, NOT the symmetric one.

ARCHIMEDEAN CONVENTIONS (1991 paper, Prop. 2.1; 1992 paper, (3.1)-(3.2)):
Deninger defines Gamma_C(z) = (2pi)^{-z} Gamma(z) and

    Gamma_R(z) := 2^{-1/2} pi^{-z/2} Gamma(z/2)        (HIS normalization,
                                                        includes 2^{-1/2}!)
and proves (Prop. 2.1, arguments in (-pi/2, pi/2) for nu >> 0):

    prod_reg_{nu>=0} (nu + z)            = ( Gamma(z)/sqrt(2pi) )^{-1}
    prod_reg_{nu>=0} ((nu + z)/(2pi))    = Gamma_C(z)^{-1}
    prod_reg_{nu>=0} ((2nu + z)/(2pi))   = Gamma_R(z)^{-1}
                                         = sqrt(2) pi^{z/2} / Gamma(z/2).

Doc 20's archimedean ladder prod_reg_{n>=0}(n + s/2) = sqrt(2pi)/Gamma(s/2)
is the UNSCALED (kappa = 1) version; the dictionary to the true Gamma_R
needs the scale anomaly: the half-ladder has ANOMALOUS DIMENSION
zeta_H(0, s/2) = (1-s)/2 != 0, so the value is scale-DEPENDENT, and
Deninger's 1/(2pi) inserts exactly pi^{-s/2} (times 2-power constants).
At finite places the full ladder has anomalous dimension 0: scale-free.
This is the precise content of Hesselholt's remark (1602.01980, intro,
after Theorem A) that "in the archimedean case the scaling factor is
essential". Bonus: the scale anomaly GENERATES the -(1/2) log pi term of
HALF the explicit formula's archimedean supply density (doc 09/19;
the s <-> 1-sbar pairing supplies the factor 2 Re) that doc
20's unscaled ladder was missing.

PRE-REGISTERED READINGS (fail-closed; each gate kills a specific claim):
  R1 (G1-G3): Deninger Prop 2.1's three identities hold as transcribed,
      including the sqrt(2) in Gamma_R^{-1}. If G3 returns
      pi^{z/2}/Gamma(z/2) WITHOUT sqrt(2), the transcription of his
      Gamma_R normalization is wrong and the doc-20 correction note about
      the 2^{-1/2} is withdrawn.
  R2 (G4): under Deninger's convention (two independent implementations:
      his rotated proof steps, and the vertical principal-branch Hurwitz
      continuation) the full-ladder det is 1 - lambda q^{-s}; the
      symmetric scheme gives q^{(s-alpha)/2}(1 - lambda q^{-s}); ratio
      EXACTLY q^{(s-alpha)/2}. If instead the conventions agree, doc 20's
      attribution stands and its correction note is withdrawn.
  R3 (G5): anomalous dimensions: full ladder 0 (scale-free), half-ladder
      (1-s)/2; the doc20 <-> Deninger archimedean ratio is pi^{(1-s)/2}.
  R4 (G6): -d/ds log det of the SCALED real-place ladder on the critical
      line equals -(1/2) log pi + (1/2) psi(1/4 + it/2) - the EF
      archimedean supply density INCLUDING the -log(pi)/2 term (which the
      unscaled doc-20 ladder lacks).
  R5 (G7): Deninger's duplication Gamma_R(s) Gamma_R(s+1) = Gamma_C(s)
      holds with his 2^{-1/2}; the classical Gamma_R gives 2 Gamma_C(s).

Run:
    python3 -m scripts.numerics.witness.prime_int_deninger_convention
"""
import cmath
import math
import sys

import flint

flint.ctx.prec = 333          # internal flint precision; final values are
TOL = 5e-13                   # reported through complex doubles, so the
                              # verification floor is ~1e-15; the claims
                              # under test differ at O(1).
FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def acb(z):
    z = complex(z)
    return flint.acb(z.real, z.imag)


def C(x):
    """flint acb -> python complex (midpoint)."""
    return complex(float(x.real.mid()), float(x.imag.mid()))


H = flint.arb(1) / flint.arb(10) ** 30      # step for d/du at u = 0


def zh(u, a):
    """Hurwitz zeta zeta_H(u, a) = sum_{nu>=0} (nu+a)^{-u}, flint."""
    return acb(u).zeta(acb(a))


def zh0(a):
    """zeta_H(0, a)  (should equal 1/2 - a)."""
    return C(zh(0.0, a))


def zh_d0(a):
    """d/du zeta_H(u, a) at u = 0, central difference at 1e-30 (in flint)."""
    hh = flint.acb(H, 0)
    return C((hh.zeta(acb(a)) - (-hh).zeta(acb(a))) / (2 * hh))


def reg_half(a, kappa=1.0):
    """prod_reg_{nu>=0} ((nu + a)/kappa), kappa > 0 real, Re a > 0.

    zeta_ladder(u) = kappa^u zeta_H(u, a);
    value = kappa^{-zeta_H(0,a)} exp(-zeta_H'(0,a)).
    """
    z0 = zh0(a)
    return cmath.exp(-zh_d0(a) - math.log(kappa) * z0)


def lgamma(z):
    return C(acb(z).lgamma())


def gamma(z):
    return cmath.exp(lgamma(z))


SQ2PI = math.sqrt(2 * math.pi)

ZGRID = [0.5, 1.0, 2.5, 0.5 + 14.134725j, 1.5 - 3.0j]

# ------------------------------------------------------------------ G1
print("G1: Lerch baseline (Deninger 1991 Prop 2.1, line 1; doc 19/20 anchor)")
w = 0.0
for z in ZGRID:
    lhs = reg_half(z, 1.0)
    rhs = SQ2PI / gamma(z)
    w = max(w, abs(lhs - rhs) / abs(rhs))
check("prod(nu+z) = sqrt(2pi)/Gamma(z)", w < TOL, f"worst rel {w:.2e}")

# ------------------------------------------------------------------ G2
print("\nG2: Deninger Prop 2.1 line 2 (complex place)")
w = 0.0
for z in ZGRID:
    lhs = reg_half(z, 2 * math.pi)
    rhs = (2 * math.pi) ** complex(z) / gamma(z)      # = Gamma_C(z)^{-1}
    w = max(w, abs(lhs - rhs) / abs(rhs))
check("prod((nu+z)/2pi) = Gamma_C(z)^-1", w < TOL, f"worst rel {w:.2e}")

# ------------------------------------------------------------------ G3
print("\nG3: Deninger Prop 2.1 line 3 (real place) - HIS Gamma_R has 2^-1/2")
w = wc = 0.0
for z in ZGRID:
    # (2 nu + z)/(2 pi) = (nu + z/2)/pi
    lhs = reg_half(complex(z) / 2.0, math.pi)
    rhs_den = math.sqrt(2) * math.pi ** (complex(z) / 2) / gamma(complex(z) / 2)
    rhs_cls = math.pi ** (complex(z) / 2) / gamma(complex(z) / 2)
    w = max(w, abs(lhs - rhs_den) / abs(rhs_den))
    wc = max(wc, abs(lhs / rhs_cls - math.sqrt(2)))
check("prod((2nu+z)/2pi) = sqrt(2) pi^{z/2}/Gamma(z/2) = Gamma_R^Den(z)^-1",
      w < TOL, f"worst rel {w:.2e}")
check("ratio to CLASSICAL Gamma_R^-1 is sqrt(2)", wc < TOL,
      f"worst |ratio - sqrt2| {wc:.2e} (Deninger's Gamma_R := 2^-1/2 "
      f"pi^-z/2 Gamma(z/2))")

# ------------------------------------------------------------------ G4
print("\nG4: full ladder z + (2pi i/log q) Z - three regularization schemes")
worst_rot = worst_vert = worst_ratio = 0.0
for q in (2.0, 5.0):
    L = math.log(q)
    om = 2 * math.pi / L
    for s in (0.75, 1.5, 0.5 + 3.0j):
        for alpha in (0.0, 0.25):          # lambda = q^alpha
            zv = complex(s) - alpha        # vertical variable s - alpha
            lam = q ** alpha
            target = 1.0 - lam * q ** (-complex(s))

            # (i) Deninger rotated convention, his Prop 2.3 proof steps:
            # z_r = (log q / 2 pi i)(s - alpha); det =
            # prod_{nu>=0}(z_r+nu) * e^{-i pi (zeta_H(0,1-z_r))-count}
            #   * prod_{nu>=1}(nu - z_r)
            zr = L * zv / (2 * math.pi * 1j)
            half_pos = reg_half(zr, 1.0)                  # sqrt2pi/Gamma(zr)
            half_neg = reg_half(1.0 - zr, 1.0)            # sqrt2pi/Gamma(1-zr)
            phase = cmath.exp(-1j * math.pi * (zh0(1.0 - zr)))
            det_rot = half_pos * phase * half_neg
            worst_rot = max(worst_rot, abs(det_rot - target) / abs(target))

            # (ii) vertical ladder, principal branch (-pi, pi]:
            # zeta(u) = zv^-u + om^-u [e^{-i pi u/2} zeta_H(u, 1+a)
            #                        + e^{+i pi u/2} zeta_H(u, 1+b)],
            # a = -i zv/om, b = +i zv/om; det = exp(-zeta'(0)).
            # All arithmetic in flint: the 1e-30 step underflows doubles.
            a = -1j * zv / om
            b = +1j * zv / om
            hh = flint.acb(H, 0)

            def F(u):
                rot = flint.acb(0, -math.pi / 2) * u
                return (acb(zv) ** (-u)
                        + acb(om) ** (-u) * (rot.exp() * u.zeta(acb(1 + a))
                                             + (-rot).exp() * u.zeta(acb(1 + b))))
            dF = (F(hh) - F(-hh)) / (2 * hh)
            det_vert = C((-dF).exp())
            worst_vert = max(worst_vert, abs(det_vert - target) / abs(target))

            # (iii) doc 20 symmetric scheme, assembled from the same
            # primitives: det_sym = zv * [prod_reg(om nu)]^2
            #                          * sinh(pi zv/om)/(pi zv/om)
            reg_om = om ** (-0.5) * SQ2PI         # = om^{zeta(0)} e^{-zeta'(0)}
            x = zv / om
            conv = C(acb(math.pi * x).sinh()) / (math.pi * x)
            det_sym = zv * reg_om ** 2 * conv     # = 2 sinh(L zv / 2)
            ratio = det_sym / det_vert
            worst_ratio = max(worst_ratio,
                              abs(ratio - q ** (zv / 2)) / abs(q ** (zv / 2)))

check("Deninger rotated (Prop 2.3) = 1 - lambda q^-s", worst_rot < TOL,
      f"worst rel {worst_rot:.2e} (NO q^(s/2) prefactor)")
check("vertical principal branch = 1 - lambda q^-s", worst_vert < TOL,
      f"worst rel {worst_vert:.2e} (independent convention, same value)")
check("symmetric/Deninger ratio = q^((s-alpha)/2)", worst_ratio < TOL,
      f"worst rel {worst_ratio:.2e} (the KMS-1/2 prefactor IS the scheme "
      f"difference = the ladder's vacuum-energy term)")

# ------------------------------------------------------------------ G5
print("\nG5: anomalous dimensions (the place dichotomy of scheme-dependence)")
worst_f = 0.0
for q in (2.0, 5.0):
    L = math.log(q)
    om = 2 * math.pi / L
    for s in (0.75, 1.5):
        zv = complex(s)
        a = -1j * zv / om
        b = +1j * zv / om
        f0 = (1.0 + C(zh(0, 1 + a)) + C(zh(0, 1 + b)))   # zeta_full(0)
        worst_f = max(worst_f, abs(f0))
check("full ladder: zeta(0) = 0 (scale-free at finite places)",
      worst_f < TOL, f"worst |zeta_full(0)| {worst_f:.2e}")
worst_h = worst_r = 0.0
for s in (0.5, 1.0, 0.5 + 14.134725j):
    z0 = zh0(complex(s) / 2)
    worst_h = max(worst_h, abs(z0 - (0.5 - complex(s) / 2)))
    # doc20 unscaled / Deninger scaled = pi^{(1-s)/2}
    r = reg_half(complex(s) / 2, 1.0) / reg_half(complex(s) / 2, math.pi)
    worst_r = max(worst_r, abs(r - math.pi ** ((1 - complex(s)) / 2)))
check("half ladder: zeta(0) = (1-s)/2 (scale-DEPENDENT at infinity)",
      worst_h < TOL, f"worst err {worst_h:.2e}")
check("doc20-ladder / Deninger-ladder = pi^((1-s)/2)", worst_r < TOL,
      f"worst err {worst_r:.2e} (the pi^(-s/2) of Gamma_R is PURE scale "
      f"anomaly; constants 2^(+-1/2) are EF-invisible)")

# ------------------------------------------------------------------ G6
print("\nG6: the scale anomaly completes the EF supply: -(1/2)log pi term")
worst6 = worst6u = 0.0
hs = 1e-6
for t in (0.0, 14.134725, 25.0):
    s = 0.5 + 1j * t

    def logdet_scaled(z):
        return cmath.log(reg_half(z / 2, math.pi))

    def logdet_unscaled(z):
        return cmath.log(reg_half(z / 2, 1.0))

    fd = -(logdet_scaled(s + hs) - logdet_scaled(s - hs)) / (2 * hs)
    fdu = -(logdet_unscaled(s + hs) - logdet_unscaled(s - hs)) / (2 * hs)
    dg = 0.5 * C(flint.acb(0.25, t / 2).digamma())
    target = -0.5 * math.log(math.pi) + dg
    worst6 = max(worst6, abs(fd - target))
    worst6u = max(worst6u, abs(fdu - dg))
check("-d/ds log det_scaled = -(1/2)log pi + (1/2)psi(1/4+it/2)",
      worst6 < 1e-6, f"worst err {worst6:.2e} (= half of doc 09's density; "
      f"2 Re from the s <-> 1-sbar pairing)")
check("-d/ds log det_unscaled = (1/2)psi(1/4+it/2) only", worst6u < 1e-6,
      f"worst err {worst6u:.2e} (doc 20's W4: digamma without -log(pi)/2)")

# ------------------------------------------------------------------ G7
print("\nG7: duplication guard for the Gamma_R normalizations")
worst7 = worst7c = 0.0
for s in (0.3, 1.2, 0.5 + 2.0j):
    s = complex(s)
    gden = (lambda z: 2 ** -0.5 * math.pi ** (-z / 2) * gamma(z / 2))
    gcls = (lambda z: math.pi ** (-z / 2) * gamma(z / 2))
    gc = (2 * math.pi) ** (-s) * gamma(s)
    worst7 = max(worst7, abs(gden(s) * gden(s + 1) - gc) / abs(gc))
    worst7c = max(worst7c, abs(gcls(s) * gcls(s + 1) - 2 * gc) / abs(gc))
check("Gamma_R^Den(s) Gamma_R^Den(s+1) = Gamma_C(s)", worst7 < TOL,
      f"worst rel {worst7:.2e}")
check("classical Gamma_R(s) Gamma_R(s+1) = 2 Gamma_C(s)", worst7c < TOL,
      f"worst rel {worst7c:.2e}")

print("""
Summary (readings fixed in advance):
  - Deninger's printed convention gives 1 - lambda q^-s at finite places:
    doc 20's W3 closed form is the SYMMETRIC scheme, NOT Deninger's; the
    self-dual prefactor q^(s/2) is exactly the scheme difference (ladder
    vacuum energy). Hesselholt's Theorem A requires Deninger's scheme
    (Spec F_q check), so homotopy theory as it stands does NOT yet derive
    KMS-1/2 - doc 20 needs a correction note, and C5'' inherits a second
    burden: derive the regularization scheme, not only the ladder.
  - At infinity the half-ladder's anomalous dimension (1-s)/2 makes the
    value scale-dependent; Deninger's 1/(2pi) generates pi^(-s/2) and the
    EF's -(1/2)log pi supply term; constants 2^(+-1/2) are EF-invisible
    normalization freedom (Deninger's own Gamma_R carries 2^(-1/2)).
""")

print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
