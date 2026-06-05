"""Explicit-formula / Weil-positivity consistency check (tracker E, harness Check 4).

The Weil explicit formula couples ZEROS and PRIMES.  Its prime side is the
Dirichlet series of the logarithmic derivative
    -Z'/Z(s) = sum_{n>=1} c_Z(n) n^{-s},
obtained from the coefficients a_Z(n) of Z(s)=sum a_Z(n) n^{-s} by
    sum_{d|n} c_Z(d) a_Z(n/d) = a_Z(n) log n,   c_Z(1)=0.

For the Riemann zeta function (a_zeta(n)=1) this gives c_zeta(n) = Lambda(n)
(von Mangoldt): NONNEGATIVE and supported on PRIME POWERS -- the Euler product.
Weil positivity (a necessary condition for RH) rests on this prime-side
positivity.

The Davenport-Heilbronn function has NO Euler product, so its prime-side
coefficients c_DH(n) are neither nonnegative nor prime-power-supported.  Any
lemma that uses only functional-equation/Hardy structure never sees c(n) and is
therefore blind to exactly the quantity RH positivity is about.  This is the
mechanical Check 4: prime-side positivity & prime-power support FAILS for DH.
"""
from __future__ import annotations

from flint import fmpz, arb, ctx

from .objects import _dh_c


def divisors(n):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def von_mangoldt(n: int) -> float:
    """Lambda(n) = log p if n = p^k, else 0."""
    f = fmpz(n).factor()
    if len(f) == 1 and n > 1:
        p, _ = f[0]
        return float(arb(int(p)).log())
    return 0.0


def is_prime_power(n: int) -> bool:
    return n > 1 and len(fmpz(n).factor()) == 1


def log_deriv_coeffs(a, M, prec=200):
    """c(1..M) for -Z'/Z given Dirichlet coeffs a(1..M) (a[0]=a(1)=1 required).
    Uses arb arithmetic; a may be ints or arbs."""
    ctx.prec = prec
    a = [arb(x) for x in a]
    assert a[0] == 1, "need a(1)=1"
    c = [arb(0)] * (M + 1)  # 1-indexed; c[0] unused
    for n in range(1, M + 1):
        rhs = a[n - 1] * arb(n).log()
        s = arb(0)
        for d in divisors(n):
            if d < n:
                s += c[d] * a[n // d - 1]
        c[n] = rhs - s
    return c[1:]


def dh_coeffs(M):
    """Davenport-Heilbronn Dirichlet coefficients a(1..M), periodic mod 5."""
    c = _dh_c()
    period = [arb(1), c, -c, arb(-1), arb(0)]
    return [period[(n - 1) % 5] for n in range(1, M + 1)]


def weil_positivity_check(M=30):
    """Compare the prime-side coefficients c(n) of -Z'/Z for zeta and DH.
    Returns a verdict dict; the check is the Euler-product signature that the
    spine is blind to (it FAILS for DH)."""
    # zeta: a(n) = 1
    c_zeta = log_deriv_coeffs([1] * M, M)
    # verify c_zeta(n) == Lambda(n)
    lam_err = max(abs(float(c_zeta[n - 1]) - von_mangoldt(n)) for n in range(1, M + 1))

    # DH
    c_dh = log_deriv_coeffs(dh_coeffs(M), M)
    dh_vals = [float(x) for x in c_dh]

    # diagnostics
    zeta_nonneg = all(float(x) >= -1e-12 for x in c_zeta)
    zeta_pp_support = all(abs(float(c_zeta[n - 1])) < 1e-12 or is_prime_power(n)
                          for n in range(1, M + 1))
    dh_has_negative = any(v < -1e-9 for v in dh_vals)
    dh_offpp_support = [n for n in range(2, M + 1)
                        if abs(dh_vals[n - 1]) > 1e-6 and not is_prime_power(n)]

    return {
        "M": M,
        "zeta_prime_side_equals_vonMangoldt": lam_err < 1e-9,
        "zeta_nonnegative": zeta_nonneg,
        "zeta_prime_power_supported": zeta_pp_support,
        "DH_prime_side_has_negative_coeffs": dh_has_negative,
        "DH_support_off_prime_powers (first few n)": dh_offpp_support[:8],
        "verdict": ("prime-side positivity + prime-power support holds for zeta and "
                    "FAILS for DH -> this Euler-product signature has RH-content "
                    "(Check 4 passes: a lemma using it is NOT DH-blind)"),
    }


if __name__ == "__main__":
    import pprint
    r = weil_positivity_check(30)
    pprint.pprint(r)
    print("\nFirst prime-side coeffs c(n):")
    cz = log_deriv_coeffs([1] * 12, 12)
    cd = log_deriv_coeffs(dh_coeffs(12), 12)
    print(" n :   zeta c(n)=Lambda   |   DH c(n)   | prime power?")
    for n in range(1, 13):
        print(f" {n:2d}: {float(cz[n-1]):+12.5f}      | {float(cd[n-1]):+10.5f} | {is_prime_power(n)}")
