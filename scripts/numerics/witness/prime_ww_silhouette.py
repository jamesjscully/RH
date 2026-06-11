"""WW-witness: THE SILHOUETTE DOSSIER, consolidated and self-certifying.

Companion: research/work/WW-silhouette-dossier.md (gates WW1-WW14
pre-registered there BEFORE this file was first run; fail-closed;
exit 0 iff ALL gates pass).  Recomputes, in ONE witness, the decisive
numbers of every certificate-grade shadow of the missing unit
(sources: QQ, NN, TT, RR, UU, HH, BB, LL, SS), plus three NEW
pre-registered shadows:

  NS1 (WW2): the FULL Fourier data of the deficit object Delta_p:
       c_n(p) * log p = -Re Gamma_R(2 pi i n / log p)
       (hand-derived Mellin closed form; the unit's complete per-place
       silhouette is the archimedean Euler factor on Re s = 0).
  NS2 (WW4): cross-place spectra disjoint (p^m != q^n exact) +
       covariance records.
  NS3 (WW3): amplitude/parity identity + the amplitude ladder.

Discipline: F-a (no zeta values/continuation; Gamma enters only as the
closed form of a hand-derived Mellin integral of the Gaussian deficit).
No zeros consumed; fork_lib never imported; no freeze needed.
Comparison-only items flagged inline (kappa = pi; HH eigmin citation).

GATES: WW1 mean identity | WW2 NS1 shape law | WW3 NS3 amplitudes |
WW4 NS2 disjoint spectra | WW5 charge dichotomy | WW6 payment schedule |
WW7 erfc entry floor | WW8 threading per-place | WW9 threading global |
WW10 depth wall | WW11 kappa/FE-blindness | WW12 FE-homogenizer |
WW13 joint cancellation | WW14 carrier guard.
"""

import sys
from fractions import Fraction

import flint

flint.ctx.prec = 300

arb = flint.arb
acb = flint.acb

PI = arb.pi()
EULER = arb.const_euler()

FAILURES = []


def arbF(fr):
    """arb from Fraction (python-flint's arb ctor rejects Fraction)."""
    return arb(fr.numerator) / arb(fr.denominator)


def gate(name, ok, msg=""):
    tag = "PASS" if ok else "FAIL"
    print(f"{tag} {name}: {msg}")
    if not ok:
        FAILURES.append(name)


def info(msg):
    print(f"     {msg}")


# ----------------------------------------------------------------------
# shared machinery
# ----------------------------------------------------------------------

def d_of(x):
    """d(x) = 1 - e^{-pi x^2} - e^{-pi/x^2} (per-slot Gaussian deficit)."""
    return arb(1) - (-PI * x * x).exp() - (-PI / (x * x)).exp()


def delta_p(p, a, M=120):
    """Delta_p(a) = sum_{|m|<=M} d(e^{-a} p^m), tail certified into ball.

    Tail: for |m| >= M with the slot far from the window on both sides,
    d(x) <= pi/x^2 (x >= 1) and d(x) <= pi x^2 (x <= 1) termwise; both
    tails are geometric with ratio p^-2.  Bound used:
    2 * pi * e^{2|a|} p^{-2M} / (1 - p^{-2}).
    """
    L = arb(p).log()
    s = arb(0)
    for m in range(-M, M + 1):
        x = (arb(m) * L - a).exp()
        s += d_of(x)
    tail = 2 * PI * (2 * abs(a)).exp() * arb(p) ** (-2 * M) / (1 - arb(p) ** -2)
    return s + arb(0, float(tail.upper()))


def fourier_coeffs(p, nmax, N=128, M=120):
    """DFT coefficients c_0..c_nmax of Delta_p over one period (real, even)."""
    L = arb(p).log()
    vals = [delta_p(p, L * j / N, M=M) for j in range(N)]
    out = []
    for n in range(nmax + 1):
        c = arb(0)
        for j in range(N):
            c += vals[j] * (2 * PI * n * arb(j) / N).cos()
        out.append(c / N)
    return out


def gamma_R_imag(xi):
    """-Re Gamma_R(i xi) = -Re[pi^{-i xi/2} Gamma(i xi/2)] (xi real arb)."""
    z = acb(0, xi / 2)
    fac = (acb(0, -xi / 2) * acb(PI).log()).exp()
    return -((fac * z.gamma()).real)


def theta_jacobi(x, cutoff=Fraction(1, 10) ** 90):
    """theta(x) = sum_{w in Z} e^{-pi w^2 x^2}, term < 1e-90 truncation."""
    s = arb(1)
    w = 1
    while True:
        t = (-PI * arb(w * w) * x * x).exp()
        s += 2 * t
        if t < arb(1e-90):
            break
        w += 1
    return s


def T_half(x):
    """T(x) = sum_{m>=1} e^{-pi m^2 x^2}."""
    return (theta_jacobi(x) - 1) / 2


def G_fn(x):
    """G(x) = 4 x T(x) (SS Lemma C/D)."""
    return 4 * x * T_half(x)


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def comb_margin(p, d, a):
    """NN/LL margin m+ for the single-place comb v_p = 0 mod d at scale a.

    Theta = 1 + 2 sum_{n in S} e^{-pi n^2 e^{-2a}}; dual via certified FE
    Theta^dual(e^a) = e^{-a}(Theta - 1); m+ = log Theta + log(1+dual)
    - a - log(rho(1+rho)), rho = (1-1/p)/(1-p^-d).
    """
    t = (-a).exp()
    nmax = int(16 * float(a.exp())) + 2
    s = arb(0)
    for n in range(1, nmax + 1):
        if vp(n, p) % d == 0:
            s += (-PI * arb(n * n) * t * t).exp()
    theta_c = 1 + 2 * s
    dual = (-a).exp() * (theta_c - 1)
    rho = (1 - arb(1) / p) / (1 - arb(p) ** (-d))
    return theta_c.log() + (1 + dual).log() - a - (rho * (1 + rho)).log()


def m_plus_d1(a):
    """Closed-route m+(d=1, a) = log(1+2q) + log(1 + q - e^{-a}/2),
    q = e^{-pi e^{2a}} (NN P1; equals comb_margin(p, 1, a) for any p)."""
    q = (-PI * (2 * a).exp()).exp()
    return (1 + 2 * q).log() + (1 + q - (-a).exp() / 2).log()


def D_q(q, u, kmax=None):
    """D_q(u) = theta(u) - (1/q) sum_k (1+cos(2 pi k/q)) e^{-pi k^2 u^2/q^2}."""
    if kmax is None:
        kmax = 5
        while float((PI * arb(kmax * kmax) * u * u / (q * q))) < 210 * 2.303:
            kmax += 5
    s = arb(2)  # k = 0 term: (1 + cos 0) = 2
    for k in range(1, kmax + 1):
        s += 2 * (1 + (2 * PI * k / q).cos()) * (-PI * arb(k * k) * u * u / (q * q)).exp()
    return theta_jacobi(u) - s / q


def m_plus_ku(q, a):
    """SS/PP ku-face margin m+(q, a) via the coset dual route."""
    u = a.exp()
    D = D_q(q, u)
    rho = arb(q - 2) / q
    return (1 + u * D).log() + (1 + D).log() - a - (rho * (1 + rho)).log()


# ----------------------------------------------------------------------
# WW1 + WW2: the deficit object's mean and full shape law (NS1)
# ----------------------------------------------------------------------

def ww1_ww2():
    C_star = EULER + PI.log()
    coeffs = {}
    ok1 = True
    msgs1 = []
    for p in (2, 3, 5, 7):
        L = arb(p).log()
        cs = fourier_coeffs(p, 3)
        coeffs[p] = cs
        diff = abs(cs[0] * L - C_star)
        ok1 = ok1 and diff < arb(1e-20)
        msgs1.append(f"p={p}: |c0 L - (gamma+log pi)| = {float(diff):.2e}")
    gate("WW1", ok1, "mean identity c_0 log p = gamma + log pi = "
         f"{C_star} ; " + "; ".join(msgs1))

    ok2 = True
    worst = arb(0)
    for p in (2, 3, 5, 7):
        L = arb(p).log()
        for n in (1, 2, 3):
            xi = 2 * PI * n / L
            target = gamma_R_imag(xi) / L
            diff = abs(coeffs[p][n] - target)
            if diff > worst:
                worst = diff
            ok2 = ok2 and diff < arb(1e-20)
            info(f"WW2 p={p} n={n}: c_n = {float(coeffs[p][n]):+.12e}  "
                 f"-Re GammaR(i xi)/L = {float(target):+.12e}  "
                 f"|diff| = {float(diff):.2e}")
    gate("WW2", ok2, f"NS1 shape law c_n log p = -Re Gamma_R(2 pi i n/log p); "
         f"worst |diff| = {float(worst):.2e} (tol 1e-20)")
    return coeffs


# ----------------------------------------------------------------------
# WW3: NS3 amplitude/parity identity + ladder
# ----------------------------------------------------------------------

def ww3():
    ok = True
    amps = {}
    negfrac = {2: 0.00, 3: 0.00, 5: 0.25, 7: 0.30, 11: 0.35, 13: 0.36}
    for p in (2, 3, 5, 7, 11, 13):
        L = arb(p).log()
        amp = delta_p(p, arb(0)) - delta_p(p, L / 2)
        amps[p] = amp
        # closed-form c1, c3, c5
        c1 = gamma_R_imag(2 * PI * 1 / L) / L
        c3 = gamma_R_imag(2 * PI * 3 / L) / L
        c5 = gamma_R_imag(2 * PI * 5 / L) / L
        tol = 8 * abs(c5) + arb(1e-25)
        diff = abs(amp - 4 * (c1 + c3))
        clause = diff < tol
        ok = ok and clause
        info(f"WW3 p={p}: amp = {float(amp):.6e}  4(c1+c3) = "
             f"{float(4*(c1+c3)):.6e}  |diff| = {float(diff):.2e} "
             f"(tol {float(tol):.2e})  [NN neg-frac {negfrac[p]:.2f}]")
    plist = [2, 3, 5, 7, 11, 13]
    mono = all((amps[plist[i + 1]] - amps[plist[i]]) > 0
               for i in range(len(plist) - 1))
    ok = ok and mono
    gate("WW3", ok, "NS3 parity identity amp = 4 sum_{n odd} c_n + strict "
         f"amplitude monotonicity in p: {[f'{float(amps[p]):.4e}' for p in plist]}; "
         "RECORD: breakage boundary (NN) sits between amp(3) and amp(5)")


# ----------------------------------------------------------------------
# WW4: NS2 disjoint spectra
# ----------------------------------------------------------------------

def ww4():
    pairs = [(2, 3), (2, 5), (3, 5), (2, 7)]
    ok = True
    for (p, q) in pairs:
        for m in range(1, 25):
            for n in range(1, 25):
                if p ** m == q ** n:
                    ok = False
                    info(f"WW4 COLLISION {p}^{m} = {q}^{n}")
    info("WW4 exact: p^m != q^n for all 1 <= m, n <= 24, pairs "
         f"{pairs} (unique factorization)")
    # covariance records (float-grade, FLAGGED).  Computational note
    # (disclosed): Delta_p(a) is evaluated at a mod log p - exact by the
    # certified periodicity (QQ7a / WW1's machinery); run 1 evaluated the
    # truncated lattice sum at raw a >> M log p, outside its truncation
    # window, which is not Delta_p at all.  Predicate untouched.
    import math

    def delta_float(p, a):
        L = math.log(p)
        a = a - math.floor(a / L) * L
        s = 0.0
        for m in range(-40, 41):
            x = math.exp(m * L - a)
            s += 1.0 - math.exp(-math.pi * x * x) - math.exp(-math.pi / (x * x))
        return s

    corr_vals = {}
    for T in (50, 200):
        Ngrid = 4096
        ps, qs = [], []
        for j in range(Ngrid):
            a = T * j / Ngrid
            ps.append(delta_float(2, a))
            qs.append(delta_float(3, a))
        mp = sum(ps) / Ngrid
        mq = sum(qs) / Ngrid
        cov = sum((ps[j] - mp) * (qs[j] - mq) for j in range(Ngrid)) / Ngrid
        sp = math.sqrt(sum((x - mp) ** 2 for x in ps) / Ngrid)
        sq = math.sqrt(sum((x - mq) ** 2 for x in qs) / Ngrid)
        corr_vals[T] = cov / (sp * sq)
        info(f"WW4 corr(Delta_2, Delta_3) over [0,{T}] = {corr_vals[T]:+.4f} "
             "(float-grade, FLAGGED record)")
    ok = ok and abs(corr_vals[200]) < 0.1
    gate("WW4", ok, "NS2 disjoint spectra exact + |corr(200)| = "
         f"{abs(corr_vals[200]):.4f} < 0.1")


# ----------------------------------------------------------------------
# WW5: the -1/0 charge dichotomy
# ----------------------------------------------------------------------

def ww5():
    ok = True
    for uval in (36, 968):
        u = arb(uval)
        val = u * (theta_jacobi(u) - 1 / u - 1) + 1
        clause = abs(val) < arb(1e-40)
        ok = ok and clause
        info(f"WW5 hole charge: u(theta - 1/u - 1) + 1 = {float(abs(val)):.2e} "
             f"at u = {uval}  -> charge = -1 EXACTLY (NN d=1)")
    for q in (3, 9, 25, 121, 169):
        rho = Fraction(q - 2, q)
        M0 = (2 * q - 4) - rho * 2 * q
        clause = (M0 == 0) and (Fraction(2 * q - 4) / rho == 2 * q)
        ok = ok and clause
        info(f"WW5 band charge: M_0({q}) = {M0}, (2q-4)/rho_q = "
             f"{Fraction(2*q-4)/rho} = 2q  -> charge = 0 EXACTLY (TT)")
    # Computational note (disclosed): at u = 8q the certified gap
    # G(u/q) - |H| is ~ pi^2/q^2 relative ~ 1e-89 absolute, below the
    # prec-300 ABSOLUTE error of the order-1 cancellation in D_q - rho;
    # run 1's balls could not resolve it.  Local prec 600 resolves;
    # predicate untouched.
    flint.ctx.prec = 600
    for (q, uval) in ((9, 72), (121, 968)):
        u = arb(uval)
        H = u * (D_q(q, u) - arb(q - 2) / q)
        bound = G_fn(u / q)
        clause = abs(H) <= bound
        ok = ok and clause
        info(f"WW5 surviving face: |H_{q}({uval})| = {float(abs(H)):.2e} <= "
             f"G(u/q) = {float(bound):.2e}  -> c_hole = 0 (SS.1)")
    flint.ctx.prec = 300
    gate("WW5", ok, "charge dichotomy: hole -1 / band 0 / face 0 - integer-"
         "quantized continuum charge")


# ----------------------------------------------------------------------
# WW6: payment schedule
# ----------------------------------------------------------------------

def ww6():
    ok = True
    for aval in (2, 5):
        a = arb(aval)
        m1 = m_plus_d1(a)
        diff = abs(m1 + (-a).exp() / 2)
        clause = diff < arb(0.12) * (-a).exp()
        ok = ok and clause
        info(f"WW6 killer law: m+(d=1, {aval}) = {float(m1):+.6e} "
             f"~ -e^-a/2 = {float(-(-a).exp()/2):+.6e} (|diff| "
             f"{float(diff):.2e} < 0.12 e^-a)")
    a496 = arbF(Fraction(124, 25))
    m1_496 = m_plus_d1(a496)
    ok = ok and (m1_496 < 0)
    info(f"WW6 m+(d=1, 4.96) = {float(m1_496):+.6e} certified < 0")
    d1 = d_of(arb(1))
    target = 1 - 2 * (-PI).exp()
    clause = abs(d1 - target) < arb(1e-60)
    ok = ok and clause
    info(f"WW6 entry deficit d(1) = 1 - 2e^-pi = {float(d1):.6f} "
         f"(identity to {float(abs(d1-target)):.2e})")
    const = 1 - 6 * T_half(arb(1))
    info(f"WW6 SS entry constant 1 - 6T(1) = {float(const):.6f} "
         "(= lim q m+(q, entry))")
    ok = ok and (abs(const - arb(0.740696)) < arb(1e-6))
    for (q, banked) in ((25, 0.8175), (121, 0.7561)):
        entry = arb(q + 1).log()
        val = q * m_plus_ku(q, entry)
        clause = (abs(val - arb(banked)) < arb(2e-3)) and (val > const)
        ok = ok and clause
        info(f"WW6 q m+(q,entry): q={q}: {float(val):.4f} (banked {banked}, "
             "> 0.740696)")
    gate("WW6", ok, "payment schedule: -e^-a/2 law, d(1) = 1 - 2e^-pi = "
         "0.913571..., entry constant 0.740696 = 1 - 6T(1)")


# ----------------------------------------------------------------------
# WW7: the erfc entry floor (TT D2')
# ----------------------------------------------------------------------

def d_hon_entry(q):
    """D^hon_q(q+1) = D_q(q+1) - (1/(q+1)) B_q(1/(q+1))."""
    u = arb(q + 1)
    t = 1 / u
    B = arb(0)
    for w in range(-q, q + 1):
        r = w % q
        if r == 0 or r == q - 1:
            continue
        B += (-PI * arb(w * w) * t * t).exp()
    return D_q(q, u) - B / u


def ww7():
    ok = True
    E1 = PI.sqrt().erfc()
    info(f"WW7 erfc(sqrt pi) = {float(E1):.6f} (the 0.012224 floor)")
    diffs = {}
    for q in (25, 121):
        rho = arb(q - 2) / q
        dh = d_hon_entry(q)
        target = rho * E1
        diff = abs(dh - target)
        diffs[q] = diff
        clause = diff < arb(3) / (q + 1)
        ok = ok and clause
        info(f"WW7 q={q}: D^hon(entry) = {float(dh):.6f} vs rho erfc(sqrt pi)"
             f" = {float(target):.6f} (|diff| = {float(diff):.2e} < "
             f"{float(arb(3)/(q+1)):.2e})")
    ok = ok and (diffs[121] < diffs[25])
    gate("WW7", ok, "entry floor D^hon -> rho_q erfc(sqrt pi) = rho_q * "
         "0.012224; EM excess shrinks with q")


# ----------------------------------------------------------------------
# WW8 + WW9: the threading law
# ----------------------------------------------------------------------

def ww8():
    ok = True
    a = arbF(Fraction(124, 25))
    m_11_2 = comb_margin(11, 2, a)
    clause = (m_11_2 < 0) and (abs(m_11_2 + arb(2.214249e-3)) < arb(1e-8))
    ok = ok and clause
    info(f"WW8 decision cell m+((11;2), 4.96) = {float(m_11_2):+.9e} "
         "(banked -2.214249e-3, certified < 0)")
    m1 = m_plus_d1(a)
    w1 = 2 / arb(11).sqrt()
    w2 = arb(2) / 11
    A_v = w1 * m1 + w2 * m_11_2
    m1_gg_bound = 3 * (-PI * (2 * a).exp()).exp()
    A_g = w1 * arb(0, float(m1_gg_bound.upper())) + w2 * m_11_2
    cv = (A_v < 0) and (abs(A_v + arb(2.52e-3)) < arb(2e-5))
    cg = (A_g < 0) and (abs(A_g + arb(4.03e-4)) < arb(1e-5))
    ok = ok and cv and cg
    info(f"WW8 A_11(4.96) variant v = {float(A_v):+.6e} (banked -2.52e-3), "
         f"variant g = {float(A_g):+.6e} (banked -4.03e-4); both < 0")
    info(f"WW8 per-place LP (p=11, exact from signs): variant v has BOTH "
         f"slot margins < 0 ({float(m1):+.3e}, {float(m_11_2):+.3e}) -> "
         "INFEASIBLE outright: no per-place positive measure exists")
    gate("WW8", ok, "threading per-place: the p=11 family is exactly "
         "infeasible; deficits cannot be paid at the place")


def ww9():
    a = arbF(Fraction(124, 25))
    import math
    slots = []
    for p in (2, 3, 5, 7, 11):
        n_p = int(float(a) / math.log(p))
        for k in range(2, n_p + 1):
            slots.append((p, k))
    total = arb(0)
    for (p, k) in slots:
        m = comb_margin(p, k, a)
        w = 2 * arb(p) ** (arb(-k) / 2)
        total += w * m
        info(f"WW9 slot ({p};{k}): m+ = {float(m):+.6e}, weight "
             f"{float(w):.4f}")
    # k = 1 slots for all p <= e^a contribute exact-0 balls (variant g)
    m1_gg_bound = 3 * (-PI * (2 * a).exp()).exp()
    nplaces = 0
    p = 2
    sieve = [True] * 150
    for i in range(2, 150):
        if sieve[i]:
            if i <= float(a.exp()):
                nplaces += 1
            for j in range(2 * i, 150, i):
                sieve[j] = False
    total += nplaces * arb(0, float(m1_gg_bound.upper()))
    banked = arb(3.03e-2)
    ok = (total > 0) and (abs(total - banked) / banked < arb(0.25))
    gate("WW9", ok, f"threading global: A_g(4.96) = {float(total):+.6e} "
         f"> 0 certified over {len(slots)} deep slots + {nplaces} exact-0 "
         "k=1 slots (banked +3.03e-2, comparison-flagged 25%); the SAME "
         "deficits infeasible per-place are paid cross-place")


# ----------------------------------------------------------------------
# WW10: the depth wall
# ----------------------------------------------------------------------

def ww10():
    import math
    ok = True
    m3e = m_plus_ku(3, arb(4).log())
    c1 = abs(m3e - arb(0.55653)) < arb(2e-5)
    m121 = m_plus_ku(121, arbF(Fraction(124, 25)))
    c2 = abs(m121 - arb(6.4682e-3)) < arb(1e-6)
    ok = ok and c1 and c2
    info(f"WW10 anchors: m+(3, entry) = {float(m3e):.6f} (banked 0.55653); "
         f"m+(121, 4.96) = {float(m121):.6e} (banked 6.4682e-3)")
    a8 = arb(8)
    for q, p in ((3, 3), (121, 11)):
        Lam = arb(p).log()
        m = m_plus_ku(q, a8)
        needed = (Lam - m) ** 2 / m - arb(2).log()
        rho = arb(q - 2) / q
        law = rho * Lam * Lam * a8.exp()
        clause = abs(needed - law) < arb(0.02) * law
        ok = ok and clause
        avail = int(8 / math.log(q)) * arb(q).log()
        info(f"WW10 q={q}: needed depth = {float(needed):.1f} vs law "
             f"rho Lambda^2 e^8 = {float(law):.1f} (2%); available = "
             f"{float(avail):.2f}; ratio = {float(needed/avail):.1f} "
             "(EXPONENTIAL demand, LINEAR supply)")
    for q, p in ((3, 3), (9, 3), (121, 11)):
        Lam = arb(p).log()
        for aval in (arb(q + 1).log(), a8):
            s = Lam - m_plus_ku(q, aval)
            clause = s > 0
            ok = ok and clause
        info(f"WW10 append Schur s = Lambda({q}) - m+ > 0 at entry and a=8 "
             "(the unpaid atom: signature (2,N), not Lorentzian)")
    # discriminant corner
    for (q, p, want_hold) in ((3, 3, True), (9, 3, False)):
        entry = arb(q + 1).log()
        m = m_plus_ku(q, entry)
        Lam = arb(p).log()
        lhs = (Lam - m) ** 2
        rhs = m * (1 * arb(q).log() + arb(2).log())
        holds = bool(rhs - lhs > 0) if want_hold else bool(lhs - rhs > 0)
        ok = ok and holds
        info(f"WW10 DISC({q}, entry, 1): LHS = {float(lhs):.4f} vs RHS = "
             f"{float(rhs):.4f} -> {'HOLDS' if want_hold else 'FAILS'} "
             "as banked (UU corner)")
    gate("WW10", ok, "depth wall: needed rho_q Lambda_p^2 e^a vs available "
         "a; the small-q entry corner is the only slack; Weil's slot "
         "carries one evaluation")


# ----------------------------------------------------------------------
# WW11: kappa = pi (comparison-flagged) + FE-blindness
# ----------------------------------------------------------------------

def ww11():
    ok = True
    for s in (Fraction(1, 3), Fraction(2, 5), Fraction(7, 2)):
        lhs = (Fraction(1, 2) - s / 2) + (Fraction(1, 2) - (1 - s) / 2)
        clause = lhs == Fraction(1, 2)
        ok = ok and clause
    info("WW11 FE-blindness: zeta_H(0,s/2) + zeta_H(0,(1-s)/2) = 1/2 "
         "EXACTLY (Fractions; zeta_H(0,a) = 1/2 - a): kappa enters the "
         "FE-paired layer only as the constant kappa^{-1/2}")
    for sval in (arb(0.7), arb(1.3), arbF(Fraction(5, 2))):
        s = acb(sval)
        gR = lambda z: (acb(PI) ** (-z / 2)) * (z / 2).gamma()
        lhs = gR(s) * gR(s + 1)
        rhs = 2 * (2 * acb(PI)) ** (-s) * s.gamma()
        rel = abs(lhs - rhs) / abs(rhs)
        clause = rel < arb(1e-40)
        ok = ok and clause
    info("WW11 duplication Gamma_R(s) Gamma_R(s+1) = 2 (2pi)^-s Gamma(s) "
         "(rel < 1e-40): pi folded = 2pi unfolded, 2-powers EF-invisible")
    info("WW11 COMPARISON-FLAGGED: c_oo(kappa) = -(1/2) log kappa matches "
         "the EF's -(1/2) log pi iff kappa = pi (BB GB4; the assembly "
         "itself determines NO kappa - Prop BB.1)")
    gate("WW11", ok, "kappa is a density-layer datum; target kappa = pi "
         "(comparison only)")


# ----------------------------------------------------------------------
# WW12: the FE-homogenizer charge
# ----------------------------------------------------------------------

def ww12():
    ok = True
    for x in (Fraction(1, 4), Fraction(1, 9), Fraction(3, 7)):
        val = x / (1 - x) + (1 / x) / (1 - 1 / x) + 1
        clause = val == 0
        ok = ok and clause
    info("WW12 A_D + A_D' + 1 = 0 EXACTLY (rational functions; the +1 is "
         "the unit class counted once)")
    for aval in (Fraction(1, 2), Fraction(1)):
        a = arbF(aval)
        ea = a.exp()
        th_small = theta_jacobi((-a).exp())
        direct = (th_small.log()
                  + (1 + (-a).exp() * (th_small - 1) + (-a).exp()).log()
                  - a - arb(2).log())
        th = theta_jacobi(ea)
        closed = th.log() + ((1 + th) / 2).log()
        clause = (abs(direct - closed) < arb(1e-60)) and (closed > 0)
        ok = ok and clause
        info(f"WW12 GG repair at a={aval}: m+_GG(d=1) = {float(closed):.6e}"
             f" > 0, two routes agree to {float(abs(direct-closed)):.2e} "
             "(repaired dual IS the self-dual Jacobi theta)")
    gate("WW12", ok, "FE-homogenizer: the dual lacks exactly one unit "
         "class; its Fourier dual is the continuum unit")


# ----------------------------------------------------------------------
# WW13: joint-cancellation geometry
# ----------------------------------------------------------------------

def ww13():
    ok = True
    M = [[Fraction(1), Fraction(0), Fraction(1)],
         [Fraction(0), Fraction(1), Fraction(0)],
         [Fraction(1), Fraction(0), Fraction(1)]]
    det3 = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    minors = (M[0][0], M[0][0] * M[1][1] - M[0][1] * M[1][0], det3)
    # charpoly of [[1,0,1],[0,1,0],[1,0,1]]: (1-x)[(1-x)^2 - 1] ... roots 0,1,2
    roots_ok = all(
        ((1 - x) * ((1 - x) * (1 - x) - 1)) == 0 for x in (0, 1, 2))
    ok = ok and roots_ok and (det3 == 0) and (minors[0] > 0) and (minors[1] > 0)
    info(f"WW13 Toeplitz (1,0,1): minors {[str(m) for m in minors]}, "
         "eigenvalues {0,1,2} exact: PSD-boundary admissible direction "
         "isolating the breaking slot (no scalar aggregate dominates)")
    a = arbF(Fraction(31, 25))  # 1.24
    L2, L3 = arb(2).log(), arb(3).log()
    nrows = 0
    minrow = arb(10)
    for m in range(-50, 51):
        base = m * L2 - a
        n_star = int(round(-float(base) / float(L3)))
        # nearest lattice phase = the n minimizing |u| (run 1 of this
        # gate erroneously minimized d itself over the three candidate
        # n's, i.e. evaluated the FARTHEST candidate; disclosed fix,
        # predicate untouched)
        u_best = None
        for n in (n_star - 1, n_star, n_star + 1):
            u = base + n * L3
            if u_best is None or abs(u) < abs(u_best):
                u_best = u
        best = d_of(u_best.exp())
        if best < minrow:
            minrow = best
        if best > arb(0.4):
            nrows += 1
    clause = nrows == 101
    ok = ok and clause
    info(f"WW13 two-place rows (T={{2,3}}, a=1.24): {nrows}/101 rows "
         f"contribute > 0.4 (min {float(minrow):.4f}): colimit deficit "
         "non-summable - GG3, the unit does not assemble per-place")
    info("WW13 CITED (import-flagged, not recomputed): HH H4 - eigmin of "
         "the W_inf block = -0.907 at R = 4.96 while the margin stays "
         "positive: W_inf is SIGNED; the inequality is a joint "
         "cancellation, not a positive budget")
    gate("WW13", ok, "joint-cancellation geometry: exposure exact, "
         "non-summability certified, signed defect cited")


# ----------------------------------------------------------------------
# WW14: carrier guard
# ----------------------------------------------------------------------

def ww14():
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
          and irreducible.get(9, False) and (36 in rep)
          and (4 * 9 == 36) and (6 * 6 == 36))
    info(f"WW14 Epstein x^2+5y^2 represented (2..36): {sorted(rep)}")
    info("WW14 4, 6, 9 irreducible; 36 = 4*9 = 6*6: TWO distinct "
         "factorizations -> no valuation -> no slot ladder p^m (S1, S2, "
         "S10 unformable), no comb (S3-S5), no tower address (S6), no "
         "branch pairing (S8), no d-frame (S9), no spectra (S11)")
    info("WW14 DH: no carrier monoid at all (bookkeeping; dies before "
         "any comb)")
    gate("WW14", ok, "carrier guard: every dossier row consumes unique "
         "factorization; the structure solving the inverse problem must "
         "carry the Euler product")


def main():
    print("=" * 72)
    print("WW SILHOUETTE WITNESS (gates WW1-WW14, fail-closed)")
    print("=" * 72)
    ww1_ww2()
    ww3()
    ww4()
    ww5()
    ww6()
    ww7()
    ww8()
    ww9()
    ww10()
    ww11()
    ww12()
    ww13()
    ww14()
    print("=" * 72)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} gates): {FAILURES}")
        sys.exit(1)
    print("RESULT: ALL PASS (WW1-WW14)")
    sys.exit(0)


if __name__ == "__main__":
    main()
