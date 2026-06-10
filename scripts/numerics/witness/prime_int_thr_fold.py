"""R-INT / gate C5''-infty, first checkpoint (worker M): numerical gates for
the THR reflection-fold test (research/work/M-thr-fold-test.md).

The homotopy-theoretic inputs (DMPR JEMS 2021 Thm 5.18/Cor 5.19; Quigley-
Shah arXiv:2112.07462 Sec 6) are NOT numerical and are transcribed in the
doc. This witness verifies only the ANALYTIC claims the doc builds on the
folded ladders:

  W1 (fold shape): the regularized characteristic function of the FOLDED
      fixed-point weight ladder {2n : n >= 0} (DMPR Cor 5.19: pi_*
      THR(F_p)^{C_2} = F_p[y], |y| = 4, res y = x^2, i.e. weights 2n),

          prod_reg_{n>=0} (z + 2n)  =  2^{(1-z)/2} sqrt(2pi) / Gamma(z/2),

      is the Gamma_R SHAPE (Gamma(z/2)), per Lerch + zeta_H(0, z/2) =
      (1-z)/2.  [Doc claim r2 carrier.]
  W2 (anomalous dimension dichotomy on the SAME folded data):
      - folded HALF-ladder {z+2n : n>=0}: anomalous dimension
        zeta_L(0) = (1-z)/2 != 0 (scale-DEPENDENT: value(kappa) =
        kappa^{-(1-z)/2} value(1));
      - folded FULL ladder (the TPR(F_p)^{C_2} shadow Z_p[w^{+-1}],
        |w| = 4: full ladder, spacing doubled), symmetric scheme:
        anomalous dimension 0 - the regularized value 2 sinh(ell z / 2)
        is EXACTLY kappa-independent.
      [Doc claim: r2 fails on the Tate-side carrier, passes on the
      fixed-point carrier.]
  W3 (r3 parity lemma, uniqueness of KMS-1/2): in the one-parameter
      family of regularization schemes on the full vertical ladder
      (witness prime_int_deninger_convention.py G4 pins the family),

          f_c(w) = q^{c w} (1 - q^{-w}),     w = s - alpha,

      the reflection (ladder inversion Theta -> -Theta, w -> -w) acts by
          f_c(-w) = - q^{(1-2c) w} f_c(w),
      so f_c has definite parity iff c = 1/2 (odd, f_{1/2} =
      2 sinh(w log q / 2) = the KMS-1/2 / self-dual scheme). Verified on
      a (q, w, c)-grid: parity defect |f_c(-w) + q^{(1-2c)w} f_c(w)| ~ 0
      for all c, and |f_c(-w) + f_c(w)| ~ 0 iff c = 1/2.

PRE-REGISTERED READINGS (fail-closed):
  R-W1: if the closed form fails, the doc's Gamma_R-shape claim for the
        fixed-point fold is wrong; r2 verdict is withdrawn.
  R-W2: if the half-ladder anomalous dimension is not (1-z)/2, or the
        symmetric full-ladder value is kappa-dependent, the place-
        dichotomy reading (doc 20 C2 / J-doc G5) is misapplied here.
  R-W3: if parity holds for some c != 1/2 (or fails at c = 1/2), the r3
        selection lemma is wrong and the r3 verdict is withdrawn.

Run:
    python3 -m scripts.numerics.witness.prime_int_thr_fold
"""
import cmath
import math
import sys

import flint

flint.ctx.prec = 333
TOL = 1e-12
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
    """zeta_H(0, a) = 1/2 - a."""
    return C(acb(0).zeta(acb(a)))


def zh_d0(a):
    """d/du zeta_H(u, a) at u = 0 (central difference in flint)."""
    hh = flint.acb(H, 0)
    return C((hh.zeta(acb(a)) - (-hh).zeta(acb(a))) / (2 * hh))


def reg_folded_half(z, kappa=1.0):
    """prod_reg_{n>=0} ((z + 2n)/kappa).

    zeta_L(u) = (2/kappa)^... : sum (z+2n)^{-u} = 2^{-u} zeta_H(u, z/2);
    with scale kappa: zeta(u) = kappa^u 2^{-u} zeta_H(u, z/2);
    value = exp(-zeta'(0)) = (2/kappa)^{zeta_H(0,z/2)} exp(-zeta_H'(0,z/2)).
    """
    a = complex(z) / 2
    z0 = zh0(a)
    return cmath.exp(-zh_d0(a) + (math.log(2) - math.log(kappa)) * z0)


def lgamma(z):
    return C(acb(z).lgamma())


def reg_full_symmetric(z, ell, kappa=1.0, nmax=4000):
    """Symmetric-scheme regularized product over the full vertical ladder
    {z + i omega n : n in Z}, omega = 2 pi / ell, at scale kappa:

      (z/kappa) * prod_reg_{n>=1} ((z^2 + omega^2 n^2)/kappa^2)

    with prod_reg_{n>=1} (omega^2 n^2 / kappa^2) = (omega^2/kappa^2)^{zeta(0)}
    * (prod_reg n)^2 = (kappa/omega) * 2 pi, and the convergent Euler tail
    prod_{n>=1} (1 + z^2/(omega n)^2) truncated at nmax with the exact
    closed form sinh(pi z/omega)/(pi z/omega) as the comparison target.
    Expected: 2 sinh(ell z / 2), independent of kappa.
    """
    omega = 2 * math.pi / ell
    head = (complex(z) / kappa) * ((kappa / omega) * 2 * math.pi)
    tail = complex(1.0)
    zz = complex(z)
    for n in range(1, nmax + 1):
        tail *= 1 + (zz / (omega * n)) ** 2
    # quadrature of the truncation: multiply by the exact ratio target/partial
    # is NOT done -- we instead check against the closed form with a tail
    # tolerance scaled by 1/nmax.
    return head * tail


def main():
    print("== W1: folded fixed-point ladder {z+2n, n>=0} = "
          "2^{(1-z)/2} sqrt(2pi)/Gamma(z/2) ==")
    for z in [0.5 + 14.134725j, 1.7 - 2.3j, 3.25, 0.5 + 1j]:
        lhs = reg_folded_half(z)
        rhs = cmath.exp(0.5 * math.log(2 * math.pi)
                        + ((1 - z) / 2) * math.log(2) - lgamma(z / 2))
        err = abs(lhs - rhs) / abs(rhs)
        check(f"W1 z={z}", err < TOL, f"rel err {err:.2e}")

    print("== W2a: half-ladder anomalous dimension (1-z)/2 "
          "(scale anomaly kappa^{-(1-z)/2}) ==")
    for z in [0.5 + 3j, 2.2]:
        for kappa in [2.0, math.pi]:
            lhs = reg_folded_half(z, kappa) / reg_folded_half(z)
            rhs = cmath.exp(-math.log(kappa) * (1 - complex(z)) / 2)
            err = abs(lhs - rhs) / abs(rhs)
            check(f"W2a z={z} kappa={kappa:.3f}", err < TOL,
                  f"rel err {err:.2e}")

    print("== W2b: symmetric-scheme FULL ladder: anomalous dimension 0, "
          "value 2 sinh(ell z/2) ==")
    NMAX = 200000
    for (z, ell) in [(0.35 + 0.2j, math.log(2)), (1.1, math.log(5))]:
        target = 2 * cmath.sinh(ell * complex(z) / 2)
        v1 = reg_full_symmetric(z, ell, kappa=1.0, nmax=NMAX)
        v2 = reg_full_symmetric(z, ell, kappa=7.5, nmax=NMAX)
        err_closed = abs(v1 - target) / abs(target)
        err_scale = abs(v1 - v2) / abs(v1)
        # Euler tail converges ~ |z omega^-1|^2/nmax: loose tolerance.
        check(f"W2b closed form z={z} ell={ell:.3f}",
              err_closed < 1e-4, f"rel err {err_closed:.2e} (tail-limited)")
        check(f"W2b kappa-independence z={z}", err_scale < 1e-15,
              f"rel diff {err_scale:.2e} (exact cancellation)")

    print("== W3: parity lemma -- c = 1/2 is the unique reflection-"
          "equivariant scheme ==")
    qs = [2, 3, 7]
    ws = [0.6 + 0.9j, 1.3 - 0.4j, 0.25]
    cs = [0.0, 0.25, 0.5, 0.75, 1.0]

    def f(c, q, w):
        return cmath.exp(c * w * math.log(q)) * (1 - cmath.exp(-w * math.log(q)))

    worst_id = 0.0
    for q in qs:
        for w in ws:
            for c in cs:
                lhs = f(c, q, -w)
                rhs = -cmath.exp((1 - 2 * c) * w * math.log(q)) * f(c, q, w)
                worst_id = max(worst_id, abs(lhs - rhs) / abs(rhs))
    check("W3 identity f_c(-w) = -q^{(1-2c)w} f_c(w) (all c)",
          worst_id < 1e-14, f"worst rel err {worst_id:.2e}")

    ok_unique = True
    detail = []
    for q in qs:
        for w in ws:
            for c in cs:
                defect = abs(f(c, q, -w) + f(c, q, w)) / abs(f(c, q, w))
                is_odd = defect < 1e-13
                if (c == 0.5) != is_odd:
                    ok_unique = False
                    detail.append(f"(q={q}, w={w}, c={c}: defect {defect:.2e})")
    check("W3 parity holds iff c = 1/2",
          ok_unique, "verified on full grid" if ok_unique else "; ".join(detail))

    print()
    if FAIL:
        print(f"FAILED gates: {FAIL}")
    else:
        print("ALL PASS")


main()
sys.exit(0 if not FAIL else 1)
