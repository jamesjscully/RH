"""Second harness wall (tracker H4): Epstein zeta of a class-number>1 form.

The DH wall catches lemmas blind to the Euler product (DH has *no* product at all).
But "fails for DH" is necessary, not sufficient: having product structure is not
sufficient for RH.  The Epstein zeta Z_Q of the non-principal form Q1=(2,1,3)
(discriminant -23, class number 3) is the witness:

  1. Z_Q1 has NO single Euler product -- its Dirichlet coefficients r_Q1(n)
     (representation numbers) are non-multiplicative, and r_Q1(1)=0.
  2. Yet the genus sum is the Dedekind zeta of Q(sqrt(-23)):
        (1/2)(Z_Q0 + 2 Z_Q1)(s) = zeta_K(s) = zeta(s) * L(s, chi_{-23}),
     a product of two functions that DO have Euler products.
  3. And Z_Q1 is RH-false (Davenport-Heilbronn 1936: zeros in Re s > 1).

So a critical-path lemma must fail for the second wall too: here product-bearing
constituents are present, but the global RH-structure is wrong.  A lemma that uses
"has an Euler product" as its lever passes Z_Q1's *constituents* yet must still
reject Z_Q1 -- which only the finer Selberg-class structure (primitive, degree 1,
Ramanujan) can do.

Run:  python3 -m scripts.numerics.witness.second_wall
"""
from __future__ import annotations

from collections import Counter

from flint import acb, ctx

from .objects import EpsteinZeta

Q0 = (1, 1, 6)   # principal form, disc -23
Q1 = (2, 1, 3)   # non-principal class


def kronecker(n: int, a: int = -23) -> int:
    """Kronecker symbol (a | n) for n >= 1; chi_{-23} is the real primitive char mod 23."""
    if n == 1:
        return 1
    result, nn = 1, n
    if nn % 2 == 0:
        if a % 2 == 0:
            return 0
        t = 1 if a % 8 in (1, 7) else -1
        while nn % 2 == 0:
            nn //= 2
            result *= t
    aa = a % nn
    while aa != 0:
        while aa % 2 == 0:
            aa //= 2
            if nn % 8 in (3, 5):
                result = -result
        aa, nn = nn, aa
        if aa % 4 == 3 and nn % 4 == 3:
            result = -result
        aa %= nn
    return result if nn == 1 else 0


def rep_numbers(form, N: int, M: int = 90) -> Counter:
    """r_Q(n) = #{(m,n)!=0 : Q(m,n)=n} for 1<=n<=N."""
    a, b, c = form
    out: Counter = Counter()
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            q = a * m * m + b * m * n + c * n * n
            if 1 <= q <= N:
                out[q] += 1
    return out


def fact1_no_euler_product(N: int = 40):
    r1 = rep_numbers(Q1, N)
    return {
        "r_Q1(1)": r1[1],
        "needs_f(1)=1_for_product": True,
        "no_euler_product": r1[1] != 1,
        "r(2)*r(3)": r1[2] * r1[3],
        "r(6)": r1[6],
        "non_multiplicative": r1[2] * r1[3] != r1[6],
    }


def fact2_genus_sum_is_dedekind(N: int = 40):
    r0, r1 = rep_numbers(Q0, N), rep_numbers(Q1, N)
    ok = True
    for n in range(1, N + 1):
        a_form = (r0[n] + 2 * r1[n]) // 2
        a_chi = sum(kronecker(d) for d in range(1, n + 1) if n % d == 0)
        if a_form != a_chi:
            ok = False
            break
    return {"checked_n_upto": N, "genus_sum_equals_zeta_times_L": ok}


def fact3_analytic_factorization(svals=(2.0, 3.0, 2.5), M: int = 16, Kterms: int = 4000):
    e0, e1 = EpsteinZeta(*Q0, M=M), EpsteinZeta(*Q1, M=M)

    def Lval(s):
        s = acb(s)
        tot = acb(0)
        for n in range(1, Kterms):
            ch = kronecker(n)
            if ch:
                tot += acb(ch) * ((-s) * acb(n).log()).exp()
        return tot

    rows = []
    for sv in svals:
        lhs = (e0.value(acb(sv)) + 2 * e1.value(acb(sv))) / 2
        rhs = acb(sv).zeta() * Lval(sv)
        rows.append((sv, float(lhs.real), float(rhs.real), float((lhs - rhs).abs_upper())))
    return rows


def summary():
    ctx.prec = 120
    f1 = fact1_no_euler_product()
    f2 = fact2_genus_sum_is_dedekind()
    f3 = fact3_analytic_factorization()
    print("Second wall -- Epstein zeta Z_Q1, Q1=(2,1,3), disc -23, class number 3")
    print(f"  1. no Euler product : r_Q1(1)={f1['r_Q1(1)']} (!=1), "
          f"r(2)r(3)={f1['r(2)*r(3)']} != r(6)={f1['r(6)']}  -> non-multiplicative")
    print(f"  2. genus sum = zeta_K = zeta*L : "
          f"(1/2)(r0+2r1)(n)=sum_d|n (-23/d) for n<= {f2['checked_n_upto']}: "
          f"{f2['genus_sum_equals_zeta_times_L']}")
    print("  3. analytic factorization (1/2)(Z0+2Z1) == zeta*L:")
    for sv, lhs, rhs, diff in f3:
        print(f"       s={sv}: lhs={lhs:.10f} rhs={rhs:.10f} diff={diff:.2e}")
    print("  => product-bearing constituents, yet Z_Q1 has no single product and is")
    print("     RH-false (Davenport-Heilbronn 1936). 'Fails for DH' is not sufficient.")
    return {"fact1": f1, "fact2": f2, "fact3": f3}


if __name__ == "__main__":
    summary()
