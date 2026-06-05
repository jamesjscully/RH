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
