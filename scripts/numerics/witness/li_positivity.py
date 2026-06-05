"""Li / Weil positivity discriminator (tracker E3 + E4).

Promotes Check 4 from a prime-side *signature* (explicit_formula.py) to genuine
*positivity*, and engages the Li-coefficient frontier the review flagged (the place
where RH becomes concrete, partially-provable inequalities -- Li 1997;
Bombieri-Lagarias 1999; cf. the de Bruijn-Newman handle, Rodgers-Tao 2020).

Li's criterion:  RH  <=>  lambda_n >= 0 for all n>=1, where
    lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]   (sum over nontrivial zeros, paired).

The mechanism is transparent here.  For a zero rho on the critical line, rho=1/2+i gamma,
    |1 - 1/rho| = |rho - 1| / |rho| = 1   EXACTLY   (|1/2 - 1 + i g| = |1/2 + i g|),
so (1-1/rho)^n stays on the unit circle and each conjugate pair contributes
    2 Re[1 - (1-1/rho)^n]  in  [0, 4]  >= 0.
For an off-line zero with Re rho < 1/2 (which DH HAS, by its functional equation:
the mate of its zero at beta=0.8085 is at beta=0.1915), |1-1/rho| > 1, so the term
grows like |1-1/rho|^n and is driven arbitrarily negative -- lambda_n is unbounded
below, so positivity FAILS.

Numerics (this module): zeta's per-zero contributions stay in [0,4]; DH's off-line
pair first makes its contribution negative at n=521 and reaches ~ -4e7 by n~4e5.
This is exactly Weil positivity separating RH-true (zeta) from RH-false (DH), seen
on the zeros themselves -- not the prime-side signature.

Run:  python3 -m scripts.numerics.witness.li_positivity
"""
from __future__ import annotations

from flint import acb, ctx

from .objects import cpow, DavenportHeilbronn

# DH's off-line zero and its sub-1/2 functional-equation mate (Re = 0.1915 < 1/2).
DH_OFFLINE = acb("0.8085171824569128708", "85.69934848569795178")
DH_OFFLINE_MATE = acb(1) - acb("0.8085171824569128708", "-85.69934848569795178")  # 0.1915 + 85.6993 i


def abs_one_minus_inv(rho) -> float:
    """|1 - 1/rho| = |rho-1|/|rho|; ==1 iff Re rho = 1/2, >1 iff Re rho < 1/2."""
    return float((acb(1) - 1 / acb(rho)).abs_upper())


def pair_contribution(rho, n: int) -> float:
    """Contribution of the conjugate pair {rho, conj(rho)} to lambda_n:
       2 Re[1 - (1 - 1/rho)^n]."""
    rho = acb(rho)
    return 2.0 * float((acb(1) - cpow(acb(1) - 1 / rho, acb(n))).real)


def zeta_li_coefficients(N: int = 8, K: int = 200, prec: int = 200):
    """lambda_n^{(K)} = sum over the first K zeta zeros (paired) for n=1..N.
    Under RH every per-pair contribution is in [0,4], so the partial sums are >= 0."""
    old = ctx.prec
    ctx.prec = prec
    rhos = [acb("0.5") + acb(0, 1) * acb.zeta_zero(k).imag for k in range(1, K + 1)]
    lam = []
    contrib_min = 1e9
    contrib_max = -1e9
    for n in range(1, N + 1):
        tot = 0.0
        for rho in rhos:
            c = pair_contribution(rho, n)
            contrib_min = min(contrib_min, c)
            contrib_max = max(contrib_max, c)
            tot += c
        lam.append(tot)
    ctx.prec = old
    return {"N": N, "K": K, "lambda_partial": lam,
            "per_pair_contrib_range": (contrib_min, contrib_max),
            "all_nonnegative": all(x >= -1e-9 for x in lam)}


def dh_positivity_failure(nmax: int = 400000, prec: int = 150):
    """The off-line DH zero pair (Re=0.1915<1/2) drives lambda_n negative and
    unbounded below.  Returns the first n where its contribution < 0 and the
    minimum over n<nmax."""
    old = ctx.prec
    ctx.prec = prec
    rho = DH_OFFLINE_MATE
    first_neg = None
    worst = (1e18, 0)
    for n in range(1, nmax + 1):
        c = pair_contribution(rho, n)
        if c < worst[0]:
            worst = (c, n)
        if c < 0 and first_neg is None:
            first_neg = (n, c)
    ctx.prec = old
    return {"off_line_mate": (float(rho.real), float(rho.imag)),
            "abs_one_minus_inv": abs_one_minus_inv(rho),
            "first_n_negative": first_neg,
            "min_contribution": worst,
            "unbounded_below": worst[0] < -1.0}


def summary(quick: bool = True):
    ctx.prec = 200
    print("Li / Weil positivity (tracker E3+E4)")
    print("  on-line  Re rho=1/2  -> |1-1/rho| = 1 (exact) -> pair contrib in [0,4] >= 0")
    print("  off-line Re rho<1/2  -> |1-1/rho| > 1         -> contrib unbounded below")
    z = zeta_li_coefficients(N=8, K=150)
    print(f"\n  zeta: lambda_n^(K={z['K']}) for n=1..8:")
    print("    " + "  ".join(f"{x:.3f}" for x in z["lambda_partial"]))
    print(f"    per-pair contributions in [{z['per_pair_contrib_range'][0]:.4f}, "
          f"{z['per_pair_contrib_range'][1]:.4f}]  all_lambda_nonneg={z['all_nonnegative']}")
    nmax = 2000 if quick else 400000
    d = dh_positivity_failure(nmax=nmax)
    print(f"\n  DH off-line mate rho=({d['off_line_mate'][0]:.4f},{d['off_line_mate'][1]:.4f}),"
          f" |1-1/rho|={d['abs_one_minus_inv']:.6f} > 1:")
    print(f"    first n with pair contribution < 0: {d['first_n_negative']}")
    print(f"    min contribution over n<{nmax}: {d['min_contribution']}")
    print("    => DH violates Li/Weil positivity (lambda_n -> -inf); zeta does not.")
    print("    Genuine positivity, read off the zeros -- not the prime-side signature.")
    return {"zeta": z, "dh": d}


if __name__ == "__main__":
    summary(quick=False)
