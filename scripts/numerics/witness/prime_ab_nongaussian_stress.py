"""AB-witness: THE NON-GAUSSIAN STRESS TEST (charter doc 39 move M2).

Companion: research/work/AB-nongaussian-stress.md (gates AB1-AB9
pre-registered there BEFORE this file was first run; fail-closed;
exit 0 iff ALL gates pass).

Swaps the Gaussian unit e^{-pi x^2} for three logged alternatives and
recomputes the decisive dossier rows through ONE general-f code path
(Gaussian column = control, gate AB1):

  (A) QUARTIC  f_A = e^{-pi x^4}          (KK.U's banked unit, not
                                           self-dual)
  (B) BUMP     f_B = exp(1 - 1/(1-x^2))   (compact support: maximal
               on |x| < 1, else 0          contrast class)
  (C) HERMITE  f_C = e^{-pi x^2}(1 + eps H4(sqrt(2pi) x))/(1 + 12 eps)
               eps = 1/100                 (Fourier-SELF-DUAL but not
                                           Gaussian: the sharpest probe)

Rows: S2 shape law (AB3), S3 charge dichotomy (AB4), S4 payment
schedule (AB5), S5 threading per-place/global (AB6/AB7), S6 depth wall
(AB8); unit admissibility AB2; carrier guard AB9.

Discipline: F-a (no zeta values/continuation; Gamma enters only as
closed-form Mellin transforms of the logged units).  No zeros consumed;
fork_lib never imported.  Duals for non-self-dual units are
FE-TRANSPORTED (flagged; for Gaussian and f_C the FE route equals the
paired/Poisson route exactly - certified by AB2's homogeneity gates).
"""

import sys
from fractions import Fraction

import flint

flint.ctx.prec = 300

arb = flint.arb
acb = flint.acb

PI = arb.pi()
EULER = arb.const_euler()
EPS = Fraction(1, 100)          # the Hermite correction (logged, exact)

FAILURES = []


def arbF(fr):
    return arb(fr.numerator) / arb(fr.denominator)


def acbF(fr):
    """acb from Fraction (python-flint's acb ctor rejects Fraction)."""
    return acb(arbF(fr))


def gate(name, ok, msg=""):
    tag = "PASS" if ok else "FAIL"
    print(f"{tag} {name}: {msg}")
    if not ok:
        FAILURES.append(name)


def info(msg):
    print(f"     {msg}")


def contains_zero(z):
    """ball z (acb) contains 0?"""
    return z.real.contains(arb(0)) and z.imag.contains(arb(0))


# ----------------------------------------------------------------------
# the units (G-INT6: THE logged choices; every parameter fixed in the
# memo before the first run)
# ----------------------------------------------------------------------

EPS_A = arbF(EPS)
HNORM = 1 + 12 * EPS_A          # 1 + 12 eps = 28/25


def f_gauss(x):
    return (-PI * x * x).exp()


def f_quartic(x):
    return (-PI * x * x * x * x).exp()


def f_bump(x):
    """exp(1 - 1/(1-x^2)) on [0,1), else 0.  x arb >= 0."""
    lt = x < 1
    ge = x >= 1
    if ge:
        return arb(0)
    if not lt:
        raise ValueError("bump: ball straddles 1 (must not happen)")
    den = 1 - x * x
    return (1 - 1 / den).exp()


def f_hermite(x):
    """e^{-pi x^2}(1 + eps H4(sqrt(2pi) x)) / (1 + 12 eps);
    H4(sqrt(2pi)x) = 64 pi^2 x^4 - 96 pi x^2 + 12."""
    x2 = x * x
    h4 = 64 * PI * PI * x2 * x2 - 96 * PI * x2 + 12
    return (-PI * x2).exp() * (1 + EPS_A * h4) / HNORM


def f_bump_acb(x):
    """bump for acb x (quadrature); caller guards the support."""
    den = 1 - x * x
    return (1 - 1 / den).exp()


class Unit:
    def __init__(self, name, f, x_max, c_tail):
        self.name = name
        self.f = f
        self.x_max = x_max      # f(x) < 1e-50 for x >= x_max
        self.c_tail = c_tail    # d_f(e^u) <= c_tail * e^{-2|u|}
        self.I2 = None          # 2 * int_0^oo f  (set in AB2)


U_G = Unit("gauss", f_gauss, 16, PI)
U_A = Unit("quartic", f_quartic, 3, 2 * PI)
U_B = Unit("bump", f_bump, 1, 2 * PI)
U_C = Unit("hermite", f_hermite, 8, 6 * PI)
UNITS = [U_G, U_A, U_B, U_C]
TEST_UNITS = [U_A, U_B, U_C]


# ----------------------------------------------------------------------
# rigorous quadrature helpers (flint acb_calc; balls propagated)
# ----------------------------------------------------------------------

QTOL = 1e-40


def quad(fn, a, b):
    return acb.integral(fn, a, b, rel_tol=QTOL, abs_tol=QTOL)


def guard_bump(fn):
    """Signal non-holomorphy to acb_calc with NaN (a finite wide ball
    instead CORRUPTS the enclosure - disclosed computational fix after
    run 2; the calibration value is recovered exactly)."""
    def wrapped(x, analytic):
        den = 1 - x * x
        if contains_zero(den):
            return acb(arb('nan'))
        return fn(x)
    return wrapped


def bump_halfmass():
    """int_0^oo f_B = int_0^0.995 + tail (f_B(0.995) < 1e-43)."""
    val = quad(guard_bump(f_bump_acb), 0, acbF(Fraction(995, 1000)))
    tail = arb(0, 1e-43) * arbF(Fraction(5, 1000))
    return val.real + tail


def bump_mellin(xi):
    """2 Re int_0^1 (1 - f_B(x)) x^{i xi - 1} dx via x = e^v on
    [-35, -0.005] + closed-form edge strip + tail balls."""
    xiacb = acb(xi)

    def integrand(v, analytic):
        x = v.exp()
        den = 1 - x * x
        if contains_zero(den):
            return acb(arb('nan'))
        fb = (1 - 1 / den).exp()
        return (1 - fb) * (acb(0, 1) * xiacb * v).exp()

    core = quad(integrand, -35, acbF(Fraction(-5, 1000)))
    if bool(xi == 0):
        strip = acbF(Fraction(5, 1000))
    else:
        ixi = acb(0, 1) * xiacb
        strip = (1 - (-arbF(Fraction(5, 1000)) * ixi).exp()) / ixi
    # tails: |int_{-oo}^{-35}| <= 0.75 * 1.5 e^{-70};  edge f_B-part
    ball = arb(0, 1.2e-30) + arb(0, 1e-43)
    return 2 * (core + strip).real + ball


# ----------------------------------------------------------------------
# closed-form Mellin laws (registered transformation laws, sec 1.3)
# ----------------------------------------------------------------------

def law_gauss(xi):
    """-Re Gamma_R(i xi)."""
    z = acb(0, xi / 2)
    fac = (acb(0, -xi / 2) * acb(PI).log()).exp()
    return -((fac * z.gamma()).real)


def law_quartic(xi):
    """-2 Re fA~(i xi),  fA~(s) = (1/4) pi^{-s/4} Gamma(s/4)."""
    z = acb(0, xi / 4)
    fac = (acb(0, -xi / 4) * acb(PI).log()).exp()
    return -((fac * z.gamma()).real) / 2


def law_hermite(xi):
    """-2 Re fC~(i xi),
    fC~(s) = (1/2) pi^{-s/2} Gamma(s/2)(1 + 4 eps(4s^2 - 4s + 3))/(1+12eps)."""
    s = acb(0, xi)
    poly = 1 + 4 * acb(EPS_A) * (4 * s * s - 4 * s + 3)
    fac = (-(s / 2) * acb(PI).log()).exp()
    val = fac * (s / 2).gamma() * poly / acb(HNORM)
    return -(val.real)


# ----------------------------------------------------------------------
# the deficit object Delta_p^f and its DFT
# ----------------------------------------------------------------------

def d_log(unit, coeff, L):
    """d_f(e^u), u = coeff * L (coeff Fraction != 0 or == 0 exactly)."""
    if coeff == 0:
        # x = 1 exactly: d = 1 - 2 f(1)
        return 1 - 2 * unit.f(arb(1))
    u = arbF(abs(coeff)) * L
    z = (-u).exp()              # z < 1 strictly
    return 1 - unit.f(z) - unit.f(1 / z)


def fourier_coeffs(unit, p, nmax, N=128, M=60):
    """DFT c_0..c_nmax of Delta_p^f over one period; certified tails.

    N: the bump unit uses N = 512 (computational calibration, disclosed:
    its Mellin data decays only e^{-c sqrt(xi)}, c ~ 1.25 measured, so
    the N = 128 alias floor is ~1e-12 - above the registered 1e-15
    tolerance; at N = 512 the alias is < 1e-24.  Predicate untouched.)"""
    L = arb(p).log()
    vals = []
    for j in range(N):
        s = arb(0)
        for m in range(-M, M + 1):
            s += d_log(unit, Fraction(m) - Fraction(j, N), L)
        # tail: 2 C_f e^{2a} p^{-2M} / (1 - p^{-2}),  a <= L
        tail = 2 * unit.c_tail * arb(p) ** 2 * arb(p) ** (-2 * M) \
            / (1 - arb(p) ** -2)
        vals.append(s + arb(0, float(tail.upper())))
    out = []
    for n in range(nmax + 1):
        c = arb(0)
        for j in range(N):
            c += vals[j] * (2 * PI * n * arb(j) / N).cos()
        out.append(c / N)
    return out


# ----------------------------------------------------------------------
# counts and margins (general-f; FE-route duals - exact for self-dual
# units, FE-TRANSPORTED (flagged) for quartic/bump)
# ----------------------------------------------------------------------

def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def theta_comb(unit, p, d, a):
    """sum_{n >= 1, v_p(n) = 0 mod d} f(n e^{-a}) + certified tail ball."""
    t = (-a).exp()
    nmax = int(unit.x_max * float(a.exp())) + 2
    s = arb(0)
    for n in range(1, nmax + 1):
        if vp(n, p) % d == 0:
            s += unit.f(arb(n) * t)
    return s + arb(0, 1e-50)


def theta_full_halfline(unit, u_int):
    """sum_{n >= 1} f(n/u) for integer u (exact rational arguments)."""
    nmax = unit.x_max * u_int + 2
    s = arb(0)
    for n in range(1, nmax + 1):
        s += unit.f(arb(n) / u_int)
    return s + arb(0, 1e-50)


def m_comb(unit, p, d, a):
    """NN/LL margin with covariant chi (rho~ = 2 I_f rho); FE-route dual."""
    theta = 1 + 2 * theta_comb(unit, p, d, a)
    dual = (-a).exp() * (theta - 1)
    rho = (1 - arb(1) / p) / (1 - arb(p) ** (-d))
    rr = unit.I2 * rho
    return theta.log() + (1 + dual).log() - a - (rr * (1 + rr)).log()


def m1_gg(unit, a):
    """GG-repaired d=1 margin: dual_GG = e^{-a} Theta_f (the repair adds
    the hole's own coefficient f(0)/u = 1/u)."""
    theta = 1 + 2 * theta_comb(unit, 2, 1, a)   # d=1: comb = all n
    dual_gg = (-a).exp() * theta
    rr = unit.I2
    return theta.log() + (1 + dual_gg).log() - a - (rr * (1 + rr)).log()


def P_ku(unit, q, a, u_int=None):
    """ku-face comb sum_{w in Z, w(w+1) != 0 mod q} f(|w| e^{-a}).

    u_int: when a = log(u_int) exactly (entry scales), slot weights are
    the EXACT rationals |w|/u_int (the bump's support comparison at
    w = u_int must resolve x = 1 exactly)."""
    if u_int is not None:
        wmax = unit.x_max * u_int + 2
    else:
        t = (-a).exp()
        wmax = int(unit.x_max * float(a.exp())) + 2
    s = arb(0)
    for w in range(-wmax, wmax + 1):
        if w == 0 or (w % q) in (0, q - 1):
            continue
        x = arb(abs(w)) / u_int if u_int is not None else arb(abs(w)) * t
        s += unit.f(x)
    return s + arb(0, 1e-50)


def m_ku(unit, q, a, u_int=None):
    """ku-face margin, covariant chi; D = FE(-transported) dual."""
    Pv = P_ku(unit, q, a, u_int=u_int)
    D = (-a).exp() * Pv
    rho = arb(q - 2) / q
    rr = unit.I2 * rho
    return (1 + Pv).log() + (1 + D).log() - a - (rr * (1 + rr)).log()


def d_hon_entry(unit, q):
    """D^hon_f(q, entry) = (1/u) sum_{|w| > q, comb} f(|w|/u), u = q+1."""
    u = q + 1
    wmax = unit.x_max * u + 2
    s = arb(0)
    for w in range(-wmax, wmax + 1):
        if abs(w) <= q or w == 0 or (w % q) in (0, q - 1):
            continue
        s += unit.f(arb(abs(w)) / u)
    return s / u


def T1(unit):
    """T_f(1) = sum_{m >= 1} f(m)."""
    s = arb(0)
    for m in range(1, unit.x_max + 2):
        s += unit.f(arb(m))
    return s + arb(0, 1e-50)


def E_const(unit):
    """E_f = 2 + 4I/(1+2I) - (1+4T)/(2I) - 2(1+2T)/(1+2I)."""
    I2 = unit.I2
    T = T1(unit)
    return 2 + 2 * I2 / (1 + I2) - (1 + 4 * T) / I2 - 2 * (1 + 2 * T) / (1 + I2)


A496 = arbF(Fraction(124, 25))


# ----------------------------------------------------------------------
# AB2: unit admissibility (run first: it sets I2 on every unit)
# ----------------------------------------------------------------------

def ab2():
    ok = True
    # masses
    U_G.I2 = arb(1)
    info("AB2 gauss: 2I = 1 (exact, Poisson-normalized)")

    quartic_quad = 2 * quad(lambda x, _: (-acb(PI) * x ** 4).exp(), 0, 3).real \
        + arb(0, 1e-100)
    quartic_closed = 2 * arbF(Fraction(5, 4)).gamma() * PI ** arbF(Fraction(-1, 4))
    c = abs(quartic_quad - quartic_closed) < arb(1e-35)
    ok = ok and c
    U_A.I2 = quartic_closed
    info(f"AB2 quartic: 2I = {float(quartic_closed):.10f} closed "
         f"2 Gamma(5/4) pi^-1/4; quadrature agrees to "
         f"{float(abs(quartic_quad - quartic_closed)):.1e}")

    U_B.I2 = 2 * bump_halfmass()
    c = float(U_B.I2.rad()) < 1e-38
    ok = ok and c
    info(f"AB2 bump: 2I = {float(U_B.I2):.10f} (rigorous quadrature, "
         f"rad {float(U_B.I2.rad()):.1e})")

    hermite_quad = 2 * quad(lambda x, _: (
        (-acb(PI) * x * x).exp()
        * (1 + acb(EPS_A) * (64 * acb(PI) ** 2 * x ** 4
                             - 96 * acb(PI) * x * x + 12)) / acb(HNORM)),
        0, 8).real + arb(0, 1e-90)
    c = abs(hermite_quad - 1) < arb(1e-35)
    ok = ok and c
    U_C.I2 = arb(1)
    info(f"AB2 hermite: 2I = 1 EXACT (self-dual + f(0)=1); quadrature "
         f"agrees to {float(abs(hermite_quad - 1)):.1e}")

    # f(0) = 1 (bump by definition; others by formula)
    for u in (U_G, U_A, U_C):
        c = abs(u.f(arb(0)) - 1) < arb(1e-80)
        ok = ok and c
    info("AB2 f(0) = 1 for every unit (bump: by definition)")

    # deficit positivity on the grid + tail clauses
    for u in UNITS:
        worst = arb(10)
        allpos = True
        for j in range(-120, 121):
            uu = Fraction(j, 20)        # u in [-6, 6] step 0.05
            val = d_log(u, uu, arb(1))
            if not (val > 0):
                allpos = False
            if val < worst:
                worst = val
        tail_ok = True
        for uv in (6, 8):
            val = d_log(u, Fraction(uv), arb(1))
            if not (val * (2 * arb(uv)).exp() <= u.c_tail):
                tail_ok = False
        ok = ok and allpos and tail_ok
        info(f"AB2 {u.name}: d_f > 0 on [-6,6] grid (min {float(worst):.3e}), "
             f"tail d e^2|u| <= C_f at |u| = 6, 8")

    # self-duality certificate for f_C; non-self-duality for A, B
    for tdenom in (3, 7):
        th_small = 1 + 2 * theta_full_halfline(U_C, tdenom)  # theta(1/t)
        # theta_C(t) at t = tdenom: few terms
        s = arb(1)
        for w in range(1, U_C.x_max // tdenom + 3):
            s += 2 * U_C.f(arb(w * tdenom))
        c = abs(th_small - tdenom * s) < arb(1e-40)
        ok = ok and c
        info(f"AB2 hermite Poisson: |theta_C(1/{tdenom}) - {tdenom} "
             f"theta_C({tdenom})| = {float(abs(th_small - tdenom*s)):.1e} "
             "< 1e-40 (fhat_C = f_C certified)")
    for u in (U_A, U_B):
        th_small = 1 + 2 * theta_full_halfline(u, 3)
        s = arb(1)
        for w in range(1, max(u.x_max // 3, 1) + 3):
            s += 2 * u.f(arb(w * 3))
        gap = abs(th_small - 3 * s)
        c = gap > arb(0.5)
        ok = ok and c
        info(f"AB2 {u.name} NOT self-dual: |theta(1/3) - 3 theta(3)| = "
             f"{float(gap):.4f} > 0.5 (FE route = genuine transport, flagged)")

    gate("AB2", ok, "units admissible: masses certified, deficits positive, "
         "self-duality split certified (C self-dual; A, B not)")


# ----------------------------------------------------------------------
# AB1: the Gaussian CONTROL through the general-f path
# ----------------------------------------------------------------------

def ab1():
    ok = True
    # shape law
    worst = arb(0)
    for p in (2, 3, 5):
        L = arb(p).log()
        cs = fourier_coeffs(U_G, p, 3)
        for n in range(4):
            if n == 0:
                target = (EULER + PI.log()) / L
            else:
                target = law_gauss(2 * PI * n / L) / L
            diff = abs(cs[n] - target)
            worst = diff if diff > worst else worst
            ok = ok and diff < arb(1e-20)
    info(f"AB1 shape control: worst |c_n - law| = {float(worst):.1e} "
         "(p in {2,3,5}, n in 0..3, tol 1e-20)")

    m1 = m_comb(U_G, 2, 1, arb(2))
    c = abs(m1 + arb(-2).exp() / 2) < arb(0.12) * arb(-2).exp()
    ok = ok and c
    info(f"AB1 killer control: m+(d=1, 2) = {float(m1):+.6e} ~ -e^-2/2")

    m2 = m_comb(U_G, 11, 2, A496)
    c = (m2 < 0) and (abs(m2 + arb(2.214249e-3)) < arb(1e-8))
    ok = ok and c
    info(f"AB1 decision cell control: m+((11;2), 4.96) = {float(m2):+.9e} "
         "(banked -2.214249e-3)")

    me = m_ku(U_G, 3, arb(4).log())
    c = abs(me - arb(0.55653)) < arb(2e-5)
    ok = ok and c
    m121 = m_ku(U_G, 121, A496)
    c2 = abs(m121 - arb(6.4682e-3)) < arb(1e-6)
    ok = ok and c2
    info(f"AB1 ku anchors control: m_ku(3, log4) = {float(me):.6f} "
         f"(banked 0.55653); m_ku(121, 4.96) = {float(m121):.6e} "
         "(banked 6.4682e-3)")

    for (q, banked) in ((25, 0.8175), (121, 0.7561)):
        val = q * m_ku(U_G, q, arb(q + 1).log(), u_int=q + 1)
        c = abs(val - arb(banked)) < arb(2e-3)
        ok = ok and c
        info(f"AB1 entry control: q m_ku({q}, entry) = {float(val):.4f} "
             f"(banked {banked})")

    dh = d_hon_entry(U_G, 121)
    target = arb(119) / 121 * PI.sqrt().erfc()
    c = abs(dh - target) < arb(3) / 122
    ok = ok and c
    info(f"AB1 erfc floor control: D^hon(121, entry) = {float(dh):.6f} vs "
         f"rho erfc(sqrt pi) = {float(target):.6f}")

    a8 = arb(8)
    import math
    for q, p, banked in ((3, 3, 155.7), (121, 11, 3514.4)):
        Lam = arb(p).log()
        m = m_ku(U_G, q, a8)
        needed = (Lam - m) ** 2 / m - arb(2).log()
        avail = int(8 / math.log(q)) * arb(q).log()
        ratio = needed / avail
        c = abs(ratio - arb(banked)) < arb(0.02) * banked
        ok = ok and c
        info(f"AB1 wall control: ratio({q}, 8) = {float(ratio):.1f} "
             f"(banked {banked})")

    for uv in (36, 968):
        theta_s = theta_full_halfline(U_G, uv)
        dual = 2 * theta_s / uv
        val = uv * (dual - U_G.I2) + 1
        c = abs(val) < arb(1e-40)
        ok = ok and c
        info(f"AB1 hole control: |u(dual - 2I) + 1| = {float(abs(val)):.1e} "
             f"at u = {uv}")

    ag, _ = a_g_global(U_G)
    c = (ag > 0) and (abs(ag - arb(3.03e-2)) / arb(3.03e-2) < arb(0.25))
    ok = ok and c
    info(f"AB1 global control: A_g(4.96) = {float(ag):+.6e} (banked +3.03e-2)")

    gate("AB1", ok, "CONTROL: the general-f code path with the Gaussian "
         "reproduces the banked dossier numbers (tautology guard)")


# ----------------------------------------------------------------------
# AB3: the shape law per unit (the S2 row)
# ----------------------------------------------------------------------

def ab3():
    ok = True
    laws = {
        "quartic": (law_quartic, (EULER + PI.log()) / 2, arb(1e-20)),
        "hermite": (law_hermite, EULER + PI.log() + arbF(Fraction(2, 7)),
                    arb(1e-20)),
        "bump": (None, None, arb(1e-15)),
    }
    for u in TEST_UNITS:
        law, cstar, tol = laws[u.name]
        worst = arb(0)
        NDFT = 512 if u.name == "bump" else 128
        for p in (2, 3, 5):
            L = arb(p).log()
            cs = fourier_coeffs(u, p, 3, N=NDFT)
            for n in range(4):
                xi = 2 * PI * n / L
                if u.name == "bump":
                    target = (bump_mellin(arb(0)) if n == 0
                              else bump_mellin(xi)) / L
                else:
                    target = (cstar if n == 0 else law(xi)) / L
                diff = abs(cs[n] - target)
                worst = diff if diff > worst else worst
                ok = ok and diff < tol
                if p == 5:
                    info(f"AB3 {u.name} p=5 n={n}: c_n L = "
                         f"{float(cs[n]*L):+.12f}  own-law = "
                         f"{float(target*L):+.12f}  |diff| = "
                         f"{float(diff):.1e}")
        # Gaussian REJECTION at (p, n) = (5, 1)
        L5 = arb(5).log()
        c1 = fourier_coeffs(u, 5, 1, N=NDFT)[1]
        gtarget = law_gauss(2 * PI / L5) / L5
        gap = abs(c1 - gtarget) * L5
        c = gap > arb(1e-3)
        ok = ok and c
        info(f"AB3 {u.name}: GAUSSIAN LAW REJECTED at (5,1): "
             f"|c_1 L + Re Gamma_R| = {float(gap):.6f} > 1e-3 certified; "
             f"worst own-law |diff| = {float(worst):.1e}")
    gate("AB3", ok, "S2 SHAPE: covariant - c_n log p = -2 Re f~(2 pi i n/"
         "log p), the unit's OWN Mellin data, for all three units "
         "(including the self-dual non-Gaussian); Gamma_R rejected")


# ----------------------------------------------------------------------
# AB4: charge dichotomy per unit (the S3 row)
# ----------------------------------------------------------------------

def ab4():
    ok = True
    tol36 = {"gauss": 1e-40, "quartic": 1e-25, "bump": 1e-3, "hermite": 1e-40}
    tol968 = {"gauss": 1e-40, "quartic": 1e-25, "bump": 1e-25, "hermite": 1e-40}
    for u in UNITS:
        for uv, tol in ((36, tol36[u.name]), (968, tol968[u.name])):
            theta_s = theta_full_halfline(u, uv)
            dual = 2 * theta_s / uv
            val = uv * (dual - u.I2) + 1
            c = abs(val) < arb(tol)
            ok = ok and c
            info(f"AB4 {u.name} hole: u(dual - 2I_f) + 1 = "
                 f"{float(abs(val)):.2e} at u = {uv} (tol {tol:.0e}) "
                 "-> charge -1 x f(0), INTEGER; dual atom 2I_f covariant")
    for q in (9, 25, 121):
        rho = Fraction(q - 2, q)
        M0 = (2 * q - 4) - rho * 2 * q
        c = (M0 == 0) and (Fraction(2 * q - 4) / rho == 2 * q)
        ok = ok and c
    info("AB4 band: M_0(q) = (2q-4) - rho_q 2q = 0 EXACT (Fractions, "
         "q in {9, 25, 121}); f enters only via f(0) = 1: invariant")
    gate("AB4", ok, "S3 CHARGE: INVARIANT - hole = -1 (integer, every "
         "unit), band = 0 (exact); only the unit-of-charge normalization "
         "(2I_f) covaries")


# ----------------------------------------------------------------------
# AB5: payment schedule per unit (the S4 row)
# ----------------------------------------------------------------------

def ab5():
    ok = True
    for u in UNITS:
        kc = 1 / (1 + u.I2)
        for aval in (2, 5):
            a = arb(aval)
            m1 = m_comb(u, 2, 1, a)
            diff = abs(m1 + (-a).exp() * kc)
            c = diff < arb(0.15) * (-a).exp()
            ok = ok and c
        info(f"AB5 {u.name} (a): killer law m+(d=1,a) = -e^-a/(1+2I_f), "
             f"const {float(kc):.6f} (a in {{2,5}}, tol 0.15 e^-a)")

        d1 = d_log(u, Fraction(0), arb(1))
        ident = abs(d1 - (1 - 2 * u.f(arb(1))))
        c = ident < arb(1e-40)
        ok = ok and c
        info(f"AB5 {u.name} (b): entry deficit d_f(1) = 1 - 2 f(1) = "
             f"{float(d1):.6f} (identity {float(ident):.1e})")

        # entry floor
        q = 121
        if u.name == "gauss":
            Ff = PI.sqrt().erfc()
        elif u.name == "quartic":
            Ff = 2 * quad(lambda x, _: (-acb(PI) * x ** 4).exp(),
                          1, 3).real + arb(0, 1e-100)
        elif u.name == "bump":
            Ff = arb(0)
        else:
            Ff = 2 * quad(lambda x, _: (
                (-acb(PI) * x * x).exp()
                * (1 + acb(EPS_A) * (64 * acb(PI) ** 2 * x ** 4
                                     - 96 * acb(PI) * x * x + 12))
                / acb(HNORM)), 1, 8).real + arb(0, 1e-90)
        dh = d_hon_entry(u, q)
        target = arb(q - 2) / q * Ff
        c = abs(dh - target) < arb(5) / (q + 1)
        ok = ok and c
        extra = " (BOTH SIDES EXACTLY 0: compact support kills the floor)" \
            if u.name == "bump" else ""
        info(f"AB5 {u.name} (c): D^hon(121, entry) = {float(dh):.6f} vs "
             f"rho F_f = {float(target):.6f}, F_f = {float(Ff):.7f}{extra}")

        # entry-margin constant law
        Ef = E_const(u)
        for q2 in (25, 121):
            val = q2 * m_ku(u, q2, arb(q2 + 1).log(), u_int=q2 + 1)
            c = abs(val - Ef) < 3 / arb(q2).sqrt()
            ok = ok and c
            info(f"AB5 {u.name} (d): q m_ku({q2}, entry) = {float(val):+.4f} "
                 f"vs E_f = {float(Ef):+.4f} (tol {float(3/arb(q2).sqrt()):.3f})")
    # the registered negative-limit trend for f_C (record + sign)
    Ef_C = E_const(U_C)
    v841 = 841 * m_ku(U_C, 841, arb(842).log(), u_int=842)
    info(f"AB5 RECORD hermite trend: E_C = {float(Ef_C):+.6f} (REGISTERED "
         f"< 0); q m_ku(841, entry) = {float(v841):+.6f} "
         f"(sign {'RESOLVED neg' if v841 < 0 else ('RESOLVED pos' if v841 > 0 else 'unresolved')})"
         " - entry positivity is unit-dependent within the self-dual class")
    gate("AB5", ok, "S4 PAYMENT: covariant with the registered laws - "
         "killer 1/(1+2I_f) (= 1/2 across the self-dual class), entry "
         "deficit 1 - 2f(1), floor rho F_f (vanishes at compact support), "
         "entry constant E_f (= 1 - 6T_f(1) when self-dual)")


# ----------------------------------------------------------------------
# AB6 + AB7: the threading law per unit (the S5 row)
# ----------------------------------------------------------------------

def a_g_global(unit):
    """A_g(4.96): 13 deep slots + 34 k=1 GG balls (covariant chi)."""
    import math
    a = A496
    slots = []
    for p in (2, 3, 5, 7, 11):
        n_p = int(float(a) / math.log(p))
        for k in range(2, n_p + 1):
            slots.append((p, k))
    total = arb(0)
    table = []
    for (p, k) in slots:
        m = m_comb(unit, p, k, a)
        w = 2 * arb(p) ** (arb(-k) / 2)
        total += w * m
        table.append(((p, k), m))
    m1gg = m1_gg(unit, a)
    sieve = [True] * 150
    wsum = arb(0)
    nplaces = 0
    for i in range(2, 150):
        if sieve[i]:
            if i <= float(a.exp()):
                nplaces += 1
                wsum += 2 * arb(i) ** arbF(Fraction(-1, 2))
            for j in range(2 * i, 150, i):
                sieve[j] = False
    total += wsum * m1gg
    return total, (table, m1gg, nplaces)


def ab6_ab7():
    """AB6 gate AS REGISTERED (memo sec 2): all signs arb-resolved; the
    sign census is the VERDICT INPUT (registered prediction: all < 0);
    FAIL only on an unresolvable sign.  A certified flip is reported
    in-row and carried to the memo's verdict table."""
    ok6 = True
    ok7 = True
    flips = []
    for u in UNITS:
        a = A496
        m1 = m_comb(u, 2, 1, a)
        m2 = m_comb(u, 11, 2, a)
        w1 = 2 / arb(11).sqrt()
        w2 = arb(2) / 11
        m1g = m1_gg(u, a)
        A_v = w1 * m1 + w2 * m2
        A_gp = w1 * m1g + w2 * m2
        s1 = "neg" if m1 < 0 else ("pos" if m1 > 0 else "UNRESOLVED")
        s2 = "neg" if m2 < 0 else ("pos" if m2 > 0 else "UNRESOLVED")
        sv = "neg" if A_v < 0 else ("pos" if A_v > 0 else "UNRESOLVED")
        sg = "neg" if A_gp < 0 else ("pos" if A_gp > 0 else "UNRESOLVED")
        resolved = ("UNRESOLVED" not in (s1, s2, sv, sg))
        ok6 = ok6 and resolved
        infeasible = (m1 < 0) and (m2 < 0)
        if not infeasible:
            flips.append(u.name)
        info(f"AB6 {u.name}: m+(d=1) = {float(m1):+.4e} [{s1}]; "
             f"m+((11;2)) = {float(m2):+.4e} [{s2}]; A_11 v = "
             f"{float(A_v):+.4e} [{sv}], g = {float(A_gp):+.4e} [{sg}]; "
             f"per-place LP at the banked cell: "
             f"{'INFEASIBLE (both slot signs < 0, exact)' if infeasible else 'FEASIBLE - REGISTERED PREDICTION VIOLATED (certified flip; verdict input)'}")

        ag, (table, m1gg_val, nplaces) = a_g_global(u)
        sgl = "pos" if ag > 0 else ("neg" if ag < 0 else "UNRESOLVED")
        ok7 = ok7 and (ag > 0)
        info(f"AB7 {u.name}: A_g(4.96) = {float(ag):+.6e} [{sgl}] over 13 "
             f"deep slots + {nplaces} k=1 GG slots (m1_GG = "
             f"{float(m1gg_val):+.2e}, ball rad {float(m1gg_val.rad()):.1e})")

    # RECORD (added after run 3's certified hermite flip, per the memo's
    # registered documentation duty; no gate weight): phase scan of the
    # (11;2) margin over the first half period after window entry
    # a = 2 log 11, gauss vs hermite - is the breakage ABSENT or SHIFTED
    # under the self-dual non-Gaussian unit?
    entry = 2 * arb(11).log()
    period = arb(121).log()
    for u in (U_G, U_C):
        signs = []
        for j in range(12):
            aj = entry + period * j / 24
            m = m_comb(u, 11, 2, aj)
            signs.append("-" if m < 0 else ("+" if m > 0 else "?"))
        info(f"AB6 RECORD {u.name} (11;2) sign over [2log11, 2log11 + "
             f"P/2], P = log 121, 12 pts: {''.join(signs)}")
    if flips:
        info(f"AB6 VERDICT INPUT: certified per-place-feasibility flip at "
             f"the banked cell for: {flips} - the (p;2) window-entry "
             "breakage phase set is UNIT-DEPENDENT (slot data), while the "
             "k=1 (Lambda(p)-class) deficit stays negative for every unit")
    gate("AB6", ok6, "S5 THREADING per-place: all decision signs "
         "arb-RESOLVED (registered structural gate); census above is the "
         "verdict input"
         + (f" - REGISTERED PREDICTION VIOLATED by {flips}" if flips else
            " - all-negative as registered"))
    gate("AB7", ok7, "S5 THREADING global: INVARIANT - A_g(4.96) > 0 "
         "certified under EVERY unit: global feasibility survives the "
         "unit swap")


# ----------------------------------------------------------------------
# AB8: the depth wall per unit (the S6 row)
# ----------------------------------------------------------------------

def ab8():
    import math
    ok = True
    a8 = arb(8)
    for u in UNITS:
        for q, p in ((3, 3), (121, 11)):
            Lam = arb(p).log()
            m = m_ku(u, q, a8)
            if not (m > 0):
                ok = False
                info(f"AB8 {u.name} q={q}: m_ku(q,8) sign not positive - "
                     "REGISTERED PREDICTION VIOLATED")
                continue
            needed = (Lam - m) ** 2 / m - arb(2).log()
            avail = int(8 / math.log(q)) * arb(q).log()
            ratio = needed / avail
            rho = arb(q - 2) / q
            lawc = needed * (-a8).exp() / (u.I2 * rho * Lam * Lam)
            c = ratio > 50
            ok = ok and c
            info(f"AB8 {u.name} q={q}: needed = {float(needed):.1f}, "
                 f"available = {float(avail):.2f}, RATIO = {float(ratio):.1f} "
                 f"(> 50); covariant law const needed e^-8/(rho~ Lam^2) = "
                 f"{float(lawc):.4f}")
    gate("AB8", ok, "S6 DEPTH WALL: INVARIANT - exponential demand vs "
         "linear supply (ratio >> 1) under every unit; only the O(1) "
         "constant covaries (2I_f)")


# ----------------------------------------------------------------------
# AB9: carrier guard
# ----------------------------------------------------------------------

def ab9():
    rep = set()
    for x in range(0, 7):
        for y in range(0, 3):
            n = x * x + 5 * y * y
            if 2 <= n <= 36:
                rep.add(n)
    irreducible = {}
    for n in sorted(rep):
        irr = True
        for d in sorted(rep):
            if d * d > n:
                break
            if n % d == 0 and (n // d) in rep:
                irr = False
                break
        irreducible[n] = irr
    ok = (irreducible.get(4, False) and irreducible.get(6, False)
          and irreducible.get(9, False) and (36 in rep))
    info("AB9 Epstein x^2 + 5y^2: 4, 6, 9 irreducible; 36 = 4*9 = 6*6 -> "
         "no valuation -> no slot ladder -> Delta_p^f UNFORMABLE for "
         "EVERY unit f: the stress test is carrier-bound before any unit "
         "acts.  DH: no carrier monoid (bookkeeping)")
    gate("AB9", ok, "carrier guard: unit-independence of the Euler-product "
         "consumption confirmed")


def main():
    print("=" * 72)
    print("AB NON-GAUSSIAN STRESS WITNESS (gates AB1-AB9, fail-closed)")
    print("units: gauss (CONTROL) | quartic e^-pi x^4 | bump (compact) | "
          "hermite self-dual (eps = 1/100)")
    print("=" * 72)
    ab2()        # sets I2 (admissibility first)
    ab1()        # control column
    ab3()
    ab4()
    ab5()
    ab6_ab7()
    ab8()
    ab9()
    print("=" * 72)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} gates): {FAILURES}")
        sys.exit(1)
    print("RESULT: ALL PASS (AB1-AB9)")
    sys.exit(0)


if __name__ == "__main__":
    main()
