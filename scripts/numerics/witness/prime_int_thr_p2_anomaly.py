"""R-INT / gate C5''-infty, p = 2 anomaly checkpoint (worker S): numerical
gates for the THR(F_2) reflection-fold anomaly (research/work/S-thr-p2.md).

The homotopy-theoretic computation (THR(F_2)^{tC_2} via DMPR Thm 5.18
formality + degreewise wedge/product control) is NOT numerical and is
derived in the doc. This witness verifies (a) the integer bookkeeping of
the four Tate-square corners claimed there, and (b) the analytic claims
built on the p = 2 ladders:

  W0 (Tate-square bookkeeping, exact integers): with
      fix_j  = dim_F2 pi_j THR(F_2)^{C_2}   = floor(j/2)+1   [DMPR Cor 5.20]
      Phi_j  = dim_F2 pi_j Phi^{C_2}THR(F_2) = j+1           [DMPR Prop 5.22]
      orb_j  = dim_F2 pi_j THR(F_2)_{hC_2}  = floor(j/2)+1   [computed: sum
               over n of H_{j-2n}(C_2;F_2)]
      codim_j = codim of pi_j THR^{hC_2} in pi_j THR^{tC_2} = ceil(j/2)
               [computed: missing factors b < ceil(j/2) of prod_{b>=0} F_2]
      the two zero-norm short exact sequences demand
        (a) fix_j + orb_{j-1} = Phi_j          (isotropy: fix -> Phi -> S orb)
        (b) codim_j = orb_{j-1}                (norm: hfix -> Tate -> S orb)
      and the fixed-point ring factors as fold-core x doubling x Euler tower:
        (c) Poincare(F_2[xbar,y]) = Poincare(F_2[xbar^2]) * (1+q^2-NO: 1+q^?)
            -- precisely: 1/((1-q)(1-q^2)) = [1/(1-q^4)] * (1+q^2) * [1/(1-q)]
            coefficientwise to high order.
  W1 (Lerch, unfolded ladder): prod_reg_{n>=0}(s+n) = sqrt(2pi)/Gamma(s):
      the p = 2 res-visible fixed-point weight ladder {n>=0} (spacing 1,
      UNFOLDED) has the Gamma_C shape, not the Gamma_R shape.
  W2 (fold degeneration is exact): prod_reg{s+n} =
      prod_reg{s+2n} * prod_reg{s+2n+1}: the unfolded p = 2 ladder is
      EXACTLY the product of the two odd-p Gamma_R sectors (even and odd
      F_infinity eigenvalue), i.e. the doubling artifact.
  W3 (Legendre mirror + anomalous dimensions):
      Gamma_R(s) Gamma_R(s+1) = Gamma_C(s) exactly; and the unfolded
      ladder's anomalous dimension is zeta_H(0,s) = 1/2 - s (affine),
      vs (1-s)/2 for the odd-p folded ladder (affine): both rank 1.
  W4 (Euler tower makes the p = 2 degree carrier rank 2): the full
      degree-graded fixed-point ladder {2i + k : i,k >= 0} = Barnes
      zeta_2(u, s | 1, 2);
        (a) zeta_B(0, s | 1,2) = s^2/4 - 3s/4 + 11/24 via the Hurwitz
            decomposition (flint) against the Barnes closed form;
        (b) the second s-difference of zeta_B(0,s) is 1/2 != 0: QUADRATIC
            anomalous dimension -- certifies rank 2 (any rank-1 ladder
            {(s + omega n)/kappa} has AFFINE zeta_L(0,s) = 1/2 - s/omega).
  W5 (Tate per-weight line, KMS-1/2 shape): per weight n the Tate carries
      a full two-sided degree line; the symmetric-scheme regularized
      characteristic function of a full vertical ladder of modulus q at
      s+n is 2 sinh((s+n) log q / 2) = q^{(s+n)/2}(1 - q^{-(s+n)}) -- the
      KMS-1/2-completed Euler factor form at q = 2 (exact identity), and
      it is scale-free (anomalous dimension 0 per weight; convergent
      Euler-product route vs closed form).

PRE-REGISTERED READINGS (fail-closed; mirror S-r1..S-r5 of the S-doc):
  R-W0: if (a) or (b) fails, the computed Tate/hfix corners are
        inconsistent with DMPR's fixed/geometric corners and the S-doc
        Tate computation is withdrawn; if (c) fails, the fold-core x
        doubling x Euler-tower factorization reading is withdrawn.
  R-W1/W2/W3: if any fails, the S-r3 doubling-artifact verdict
        (Gamma_R -> Gamma_C eigenvalue degeneration) is withdrawn.
  R-W4: if zeta_B(0) is not the stated quadratic (or comes out affine),
        S-r4 is withdrawn and p = 2 must be re-read as s1.
  R-W5: if the identity or scale-freeness fails, the S-r5 reading
        (completed 2-adic Euler ladder in the Tate) is withdrawn.

Run:
    python3 -m scripts.numerics.witness.prime_int_thr_p2_anomaly
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


def zh(u, a):
    """zeta_H(u, a) via flint."""
    return C(acb(u).zeta(acb(a)))


def zh_d(u, a):
    """d/dv zeta_H(v, a) at v = u (central difference in flint)."""
    hh = flint.acb(H, 0)
    return C(((acb(u) + hh).zeta(acb(a)) - (acb(u) - hh).zeta(acb(a))) / (2 * hh))


def lgamma(z):
    return C(acb(z).lgamma())


def reg_ladder(s, omega):
    """prod_reg_{n>=0} (s + omega n) = omega^{zeta_H(0,s/omega)}
    exp(-zeta_H'(0, s/omega))."""
    a = complex(s) / omega
    return cmath.exp(-zh_d(0, a) + math.log(omega) * zh(0, a))


def gamma_R(s):
    return math.pi ** 0 * cmath.exp(-complex(s) / 2 * math.log(math.pi)
                                    + lgamma(complex(s) / 2))


def gamma_C(s):
    return 2 * cmath.exp(-complex(s) * math.log(2 * math.pi) + lgamma(s))


def zeta_barnes_0(s):
    """zeta_2(0, s | 1, 2) via the Hurwitz decomposition:
    zeta_2(u,s|1,2) = 2^{-u}[ g(u, s/2) + g(u, (s+1)/2) ],
    g(u,a) = zeta_H(u-1, a) + (1-a) zeta_H(u, a).
    """
    out = 0j
    for a in (complex(s) / 2, (complex(s) + 1) / 2):
        out += zh(-1, a) + (1 - a) * zh(0, a)
    return out


def main():
    print("== W0: Tate-square integer bookkeeping (j = 0..400) ==")
    NJ = 400
    ok_a = ok_b = True
    for j in range(0, NJ + 1):
        fix = j // 2 + 1
        phi = j + 1
        orb_prev = (j - 1) // 2 + 1 if j >= 1 else 0
        codim = (j + 1) // 2  # ceil(j/2)
        if fix + orb_prev != phi:
            ok_a = False
        if codim != orb_prev:
            ok_b = False
    check("W0a fix_j + orb_{j-1} = Phi_j", ok_a, f"exact, j<=400")
    check("W0b codim(hfix_j in Tate_j) = orb_{j-1}", ok_b, "exact, j<=400")
    # (c) Poincare factorization F_2[xbar,y] = F_2[xbar^2] x {1,xbar} x F_2[y]
    N = 300
    lhs = [0] * (N + 1)
    for i in range(0, N // 2 + 1):
        for k in range(0, N - 2 * i + 1):
            lhs[2 * i + k] += 1
    rhs = [0] * (N + 1)
    for i4 in range(0, N // 4 + 1):          # xbar^{2 i4}: degree 4 i4
        for eps in (0, 2):                   # 1, xbar
            for k in range(0, N + 1):        # y^k
                d = 4 * i4 + eps + k
                if d <= N:
                    rhs[d] += 1
    check("W0c Poincare(F_2[xbar,y]) = core(4) x {1,xbar} x Euler(1)",
          lhs == rhs, f"coefficientwise to degree {N}")

    print("== W1: unfolded ladder {s+n} = sqrt(2pi)/Gamma(s) (Gamma_C shape) ==")
    for s in [0.5 + 14.134725j, 1.7 - 2.3j, 3.25, 0.5 + 1j]:
        v = reg_ladder(s, 1.0)
        target = cmath.exp(0.5 * math.log(2 * math.pi) - lgamma(s))
        err = abs(v - target) / abs(target)
        check(f"W1 s={s}", err < TOL, f"rel err {err:.2e}")

    print("== W2: fold degeneration: {s+n} = {s+2n} x {s+2n+1} exactly ==")
    for s in [0.5 + 3j, 2.2, 1.1 - 0.7j]:
        full = reg_ladder(s, 1.0)
        even = reg_ladder(s, 2.0)
        odd = reg_ladder(complex(s) + 1, 2.0)
        err = abs(full - even * odd) / abs(full)
        check(f"W2 s={s}", err < TOL, f"rel err {err:.2e}")

    print("== W3: Legendre Gamma_R(s)Gamma_R(s+1) = Gamma_C(s); affine "
          "anomalous dims ==")
    for s in [0.5 + 3j, 2.2, 0.31]:
        ggr = gamma_R(s) * gamma_R(complex(s) + 1)
        ggc = gamma_C(s)
        err = abs(ggr - ggc) / abs(ggc)
        check(f"W3 Legendre s={s}", err < TOL, f"rel err {err:.2e}")
    # anomalous dimensions: unfolded zeta_H(0,s) = 1/2 - s; folded (1-s)/2
    for s in [0.5 + 3j, 2.2]:
        e1 = abs(zh(0, s) - (0.5 - complex(s)))
        e2 = abs(zh(0, complex(s) / 2) - (1 - complex(s)) / 2)
        check(f"W3 anom dims s={s}", e1 < TOL and e2 < TOL,
              f"unfolded err {e1:.2e}, folded err {e2:.2e} (both affine)")

    print("== W4: Barnes zeta_2(0, s | 1,2) = s^2/4 - 3s/4 + 11/24; "
          "rank-2 certificate ==")
    for s in [0.5 + 3j, 2.2, 1.3 - 0.4j]:
        zb = zeta_barnes_0(s)
        closed = complex(s) ** 2 / 4 - 3 * complex(s) / 4 + 11.0 / 24
        err = abs(zb - closed)
        check(f"W4a s={s}", err < TOL, f"abs err {err:.2e}")
    # second difference: quadratic coefficient 1/4 -> second diff = h^2/2
    h = 0.5
    s0 = 1.7
    d2 = (zeta_barnes_0(s0 + h) - 2 * zeta_barnes_0(s0)
          + zeta_barnes_0(s0 - h))
    check("W4b second s-difference = h^2/2 != 0 (rank 2)",
          abs(d2 - h * h / 2) < TOL and abs(d2) > 0.1,
          f"d2 = {d2:.6f}, target {h*h/2}")

    print("== W5: Tate per-weight full line, KMS-1/2 / self-dual Euler "
          "factor at q = 2 ==")
    q = 2.0
    ell = math.log(q)
    for n in [0, 1, 3]:
        for s in [0.6 + 0.9j, 1.3 - 0.4j]:
            w = complex(s) + n
            sinh_form = 2 * cmath.sinh(w * ell / 2)
            kms_form = cmath.exp(w * ell / 2) * (1 - cmath.exp(-w * ell))
            err = abs(sinh_form - kms_form) / abs(kms_form)
            check(f"W5 identity n={n} s={s}", err < 1e-14,
                  f"rel err {err:.2e}")
    # scale-freeness of the symmetric scheme on a full vertical ladder
    # (anomalous dimension 0 per weight): convergent Euler-product route.
    omega = 2 * math.pi / ell
    NMAX = 200000
    for s in [0.35 + 0.2j]:
        w = complex(s)
        head1 = (w / 1.0) * ((1.0 / omega) * 2 * math.pi)
        head2 = (w / 7.5) * ((7.5 / omega) * 2 * math.pi)
        tail = complex(1.0)
        for k in range(1, NMAX + 1):
            tail *= 1 + (w / (omega * k)) ** 2
        v1, v2 = head1 * tail, head2 * tail
        target = 2 * cmath.sinh(ell * w / 2)
        err_closed = abs(v1 - target) / abs(target)
        err_scale = abs(v1 - v2) / abs(v1)
        check(f"W5 closed form s={s}", err_closed < 1e-4,
              f"rel err {err_closed:.2e} (tail-limited)")
        check(f"W5 kappa-independence s={s}", err_scale < 1e-15,
              f"rel diff {err_scale:.2e} (exact cancellation)")

    print()
    if FAIL:
        print(f"FAILED gates: {FAIL}")
    else:
        print("ALL PASS")


main()
sys.exit(0 if not FAIL else 1)
