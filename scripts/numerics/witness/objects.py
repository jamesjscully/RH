"""Test-object battery for the refutation harness (tracker H1).

Backend: python-flint (acb ball arithmetic) -> every value is a certified
enclosure [midpoint +/- radius].  This matches the program discipline that
numeric facts used on the spine must become certified finite inequalities.

The point of the battery is the Davenport-Heilbronn function: it shares ζ's
analytic structure (functional equation, analytic continuation) but has NO Euler
product and HAS zeros off the critical line.  Any lemma whose conclusion holds
for DH is therefore RH-neutral or false -- the mechanical core of the harness.
"""
from __future__ import annotations

from flint import acb, arb, ctx

ctx.prec = 200  # bits


def set_prec(bits: int) -> None:
    ctx.prec = bits


def _dh_c() -> arb:
    # c = tan(theta) = (sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1) ~ 0.2840790438...
    r5 = arb(5).sqrt()
    return ((arb(10) - 2 * r5).sqrt() - 2) / (r5 - 1)


def cpow(base, exp):
    """base**exp for acb, via exp(exp*log base); base may be int/acb."""
    b = base if isinstance(base, acb) else acb(base)
    e = exp if isinstance(exp, acb) else acb(exp)
    return (e * b.log()).exp()


class TestObject:
    name = "abstract"
    has_euler_product = False
    functional_equation = False
    rh_true = None

    def value(self, s: acb) -> acb:
        raise NotImplementedError

    def offline_zeros(self):
        return []

    def __repr__(self):
        return f"<{self.name}>"


class Zeta(TestObject):
    name = "zeta"
    has_euler_product = True
    functional_equation = True
    rh_true = True

    def value(self, s):
        return acb(s).zeta()


class DavenportHeilbronn(TestObject):
    """f(s) = 5^{-s} sum_{r=1}^{4} a_r * zeta(s, r/5), a = (1, c, -c, -1)."""

    name = "davenport-heilbronn"
    has_euler_product = False
    functional_equation = True
    rh_true = False  # PROVEN false: off-line zeros exist (incl. Re s > 1)

    # canonical off-line zero (beta ~ 0.808517 > 1/2); matches the literature.
    _cached_offline = [acb("0.8085171824569128708", "85.69934848569795178")]

    def __init__(self):
        c = _dh_c()
        self.coeffs = [arb(1), c, -c, arb(-1)]  # r = 1..4 (a_5 = 0)

    def value(self, s):
        s = acb(s)
        total = acb(0)
        for r, a in enumerate(self.coeffs, start=1):
            total += acb(a) * s.zeta(acb(r) / 5)  # Hurwitz zeta(s, r/5)
        return cpow(5, -s) * total

    def offline_zeros(self):
        return list(self._cached_offline)


class EpsteinZeta(TestObject):
    """Epstein zeta of a positive-definite binary form Q(m,n)=a m^2+b mn+c n^2,
    Z_Q(s) = sum'_{(m,n)!=0} Q(m,n)^{-s}.

    The harness *second wall* (tracker H4).  For class number > 1 (e.g. disc -23,
    the non-principal form (2,1,3)), Z_Q is a non-trivial combination of Hecke
    L-functions -- each of which *has* an Euler product -- yet Z_Q itself has NO
    single Euler product and is RH-false (zeros off the critical line; Davenport-
    Heilbronn 1936, Potter-Titchmarsh 1935).  So "fails for DH" (no product at all)
    is necessary but not sufficient: a critical-path lemma must also fail here, where
    product-bearing constituents are present but the global RH-structure is wrong.

    Evaluated by the Chowla-Selberg / Terras incomplete-gamma expansion (valid for
    all s != 0,1, geometric convergence), validated against the naive lattice sum and
    against Z_{m^2+n^2}=4 zeta(s) beta(s).  Let A=[[a,b/2],[b/2,c]], Delta=det A=
    ac-b^2/4, Q*(v)=v^T A^{-1} v.  Then with Lambda_Q=pi^{-s}Gamma(s)Z_Q,
        Lambda_Q(s) = S1 + S2/sqrt(Delta) + (1/sqrt(Delta))/(s-1) - 1/s,
        S1 = sum'_v (pi Q(v))^{-s}   Gamma(s,   pi Q(v)),
        S2 = sum'_v (pi Q*(v))^{s-1} Gamma(1-s, pi Q*(v)),
    and Z_Q(s) = pi^s Lambda_Q(s) / Gamma(s).
    """

    name = "epstein-disc-23"
    has_euler_product = False   # no SINGLE product; constituents have products
    functional_equation = True
    rh_true = False             # PROVEN false: zeros off the critical line

    # RH-falsity is a theorem (Davenport-Heilbronn 1936: class-number>1 Epstein zetas
    # have infinitely many zeros in Re s > 1).  Those zeros are sparse and at large
    # height -- a |Z_Q| scan over Re s in [0.55,1.4], |Im s|<=80 finds none (floor ~0.14),
    # consistent with the literature -- so none is cached here; pinning one is a follow-up
    # (a high-height argument-principle search).  The wall is instead established
    # structurally by `second_wall.py` (no single Euler product, yet genus sum = zeta*L).
    _cached_offline = []

    def __init__(self, a=2, b=1, c=3, M=16):
        self.a, self.b, self.c = a, b, c
        self.Delta = a * c - b * b / 4.0
        self.M = M  # lattice half-width; Gaussian decay makes this rapidly exact

    def value(self, s, M=None):
        s = acb(s)
        M = self.M if M is None else M
        a, b, c = self.a, self.b, self.c
        sq = acb(self.Delta).sqrt()
        pi = acb.pi()
        S1 = acb(0)
        S2 = acb(0)
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                if m == 0 and n == 0:
                    continue
                piq = pi * acb(a * m * m + b * m * n + c * n * n)
                piqs = pi * acb((c * m * m - b * m * n + a * n * n) / self.Delta)
                S1 += ((-s) * piq.log()).exp() * piq.gamma_upper(s)
                S2 += ((s - 1) * piqs.log()).exp() * piqs.gamma_upper(acb(1) - s)
        lam = S1 + S2 / sq + (1 / sq) / (s - 1) - 1 / s
        return (s * pi.log()).exp() * lam / s.gamma()

    def offline_zeros(self):
        return list(self._cached_offline)


class PlantedZeroZeta(TestObject):
    """RH-false by construction: zeta times an analytic factor vanishing exactly
    at rho, rho-bar (and ~1 at infinity).  Confirms the forward machinery
    correctly fails to converge when an off-line zero is present."""

    name = "planted-zero-zeta"
    has_euler_product = False
    functional_equation = False
    rh_true = False

    def __init__(self, rho):
        self.rho = acb(rho)

    def value(self, s):
        s = acb(s)
        rho, rhob = self.rho, self.rho.conjugate()
        g = (s - rho) * (s - rhob) / ((s - rho + 1) * (s - rhob + 1))
        return s.zeta() * g

    def offline_zeros(self):
        return [self.rho, self.rho.conjugate()]


class TruncatedEuler(TestObject):
    name = "truncated-euler"
    has_euler_product = True  # finite
    functional_equation = False

    def __init__(self, P=50):
        self.P = P
        self.primes = _primes_up_to(P)

    def value(self, s):
        s = acb(s)
        out = acb(1)
        for p in self.primes:
            out *= 1 / (1 - cpow(p, -s))
        return out


def _primes_up_to(n):
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def dh_functional_equation_residual(dh: DavenportHeilbronn, s) -> arb:
    """|f(s) - FE(s)| / |f(s)| for the DH functional equation
       f(s) = 2^s 5^{1/2-s} pi^{s-1} Gamma(1-s) cos(pi s/2) f(1-s)."""
    s = acb(s)
    lhs = dh.value(s)
    rhs = (cpow(2, s) * cpow(5, acb(1) / 2 - s) * cpow(acb.pi(), s - 1)
           * (acb(1) - s).gamma() * (acb.pi() * s / 2).cos() * dh.value(1 - s))
    return (lhs - rhs).abs_lower() and (lhs - rhs).abs_upper() / lhs.abs_lower()


if __name__ == "__main__":
    ctx.prec = 200
    dh = DavenportHeilbronn()
    print("DH constant c =", _dh_c())
    for s in [acb(2, 1), acb("0.3", 4), acb("0.808517182457", "85.699348485698")]:
        d = (dh.value(s)
             - (cpow(2, s) * cpow(5, acb(1) / 2 - s) * cpow(acb.pi(), s - 1)
                * (acb(1) - s).gamma() * (acb.pi() * s / 2).cos() * dh.value(1 - s)))
        print(f"  FE residual at s={s}: |.| <= {d.abs_upper()}")
    rho = dh.offline_zeros()[0]
    print("DH(off-line rho) =", dh.value(rho), " |.| <=", dh.value(rho).abs_upper())
