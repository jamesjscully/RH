"""R-INT / gate C5''-infty, H-r3 formulation pass (worker O): numerical
gates for the ANALYTIC HALF of H-r3 (research/work/O-hr3-formulation.md).

The homotopy-theoretic claims of the O-doc (vacuity of the linear residual
Weyl action, Frobenius equivariance, etc.) are not numerical and are argued
in the doc. This witness verifies the analytic theorems the doc proves
about regularization schemes on the full vertical ladder

    Lambda_w = { w + i t nu : nu in Z },   t = 2 pi / log q,  w = s - alpha.

  G1 (window classification, Lemma A0): every pointwise branch scheme --
      end sheets beta -> pi/2 + 2 pi a_+ at the +i*inf end and
      beta -> -pi/2 + 2 pi a_- at the -i*inf end, (a_+, a_-) in Z^2 --
      has Hurwitz-assembled regularized product

          D_{a+,a-}(w) = (-1)^{a_+ + a_-} q^{-(a_+ - a_-) w} (1 - q^{-w}).

      INTEGER vacuum slope only: c = -(a_+ - a_-) in Z. (a_+, a_-) = (0,0)
      is the vertical principal branch = Deninger's Convention (2.1) value
      1 - q^{-w} (J-doc G4); (a_+, a_-) = (0,1) is its C_2-image
      -q^{w}(1 - q^{-w}).
  G2 (rigidity, Theorem A1): in the zeta-class family
      f(w) = e^{b w}(1 - q^{-w}), the negation-naturality demand
      f(-w) = u f(w) (u a w-independent unit) holds iff b = (log q)/2,
      and then u = -1: the symmetric/KMS-1/2 scheme is the UNIQUE
      negation-natural one; in particular no integer-slope (branch)
      scheme is negation-natural.
  G3 (C_2-average, Prop A3): sqrt(D_{0,0} * D_{0,1}) = (unit in mu_4) *
      q^{w/2}(1 - q^{-w}), and the pair-modulus (doc-20 symmetric)
      construction assembles to exactly 2 sinh(w log q / 2) =
      q^{w/2}(1 - q^{-w}) with unit +1.
  G4 (conjugation non-selection, Prop A4): EVERY real-c scheme
      f_c(w) = q^{cw}(1 - q^{-w}) satisfies the Schwarz/conjugation
      constraint f_c(conj w) = conj f_c(w). Conjugation-naturality
      selects NOTHING; the selecting involution is negation w -> -w.
  G5 (principal-value characterization, Prop A5): balanced truncations
      prod_{|nu| <= N}, renormalized by the w-INDEPENDENT constant
      prod (t nu)^2, converge to (2/log q) sinh(w log q/2) = const *
      f_{1/2}(w); a fixed end-offset does not change the limit; a
      ratio-r truncation [-N, rN] drifts by exactly exp(-i (w/t) log r).
  G6 (mu_2 / double cover, Prop A6): recentering alpha by one lattice
      step (w -> w - i t) fixes every integer-c scheme (a function of
      the Frobenius eigenvalue lambda = q^alpha alone) and FLIPS THE
      SIGN of f_{1/2}: the symmetric det needs a choice of lambda^{1/2}
      (it lives on the double cover of the eigenvalue space).
  G7 (finite-level parity vs vacuity, Obstruction O-1): the truncated
      determinant P_N(w) = prod_{|nu| <= N}(w + i t nu) is EXACTLY odd,
      P_N(-w) = -P_N(w) (negation-parity is the regularized shadow of an
      exact finite symmetry); whereas the linear residual Weyl action
      g = diag((-1)^nu) commutes with Theta = diag(w + i t nu) exactly
      (finite model), so conjugation-by-g imposes NO constraint on any
      isomorphism-invariant determinant: the doc's vacuity claim.

PRE-REGISTERED READINGS (fail-closed):
  R-G1: if some window (a_+, a_-) produces a non-integer vacuum slope
        (in particular slope 1/2), Corollary A2 ("no branch convention
        can produce KMS-1/2") is WRONG and the O-doc's strengthening of
        the J-doc scheme separation is withdrawn.
  R-G2: if negation-parity holds for some b != (log q)/2 in the
        zeta-class, or fails at b = (log q)/2, Theorem A1 is wrong and
        the analytic half of H-r3 is NOT a theorem; the O-doc verdict
        is withdrawn.
  R-G3: if the C_2-average of Deninger's scheme and its C_2-image is
        not the symmetric value up to a mu_4 unit, Prop A3 is wrong.
  R-G4: if some real-c scheme violates Schwarz, Prop A4 (conjugation
        selects nothing) is mis-argued and the M-doc's "pair with
        conjugates" gloss may carry selection content after all.
  R-G5: if the balanced renormalized truncation does not converge to
        const * f_{1/2}, the principal-value characterization of the
        symmetric scheme is wrong.
  R-G6: if f_{1/2} is invariant under recentering, the double-cover
        (lambda^{1/2}) obstruction disappears and the O-doc's 2-primary
        carrier requirement is withdrawn.
  R-G7: if P_N fails exact oddness, the finite-symmetry grounding of
        negation-naturality is wrong; if g fails to commute with Theta,
        Obstruction O-1 (vacuity) is wrong and the linear residual Weyl
        action might carry the constraint after all.

Run:
    python3 -m scripts.numerics.witness.prime_int_hr3_scheme_rigidity
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


def D_window(q, w, ap, am):
    """Hurwitz-assembled regularized product of the full vertical ladder
    {w + i t nu : nu in Z}, t = 2 pi/log q, under the pointwise branch
    scheme with end sheets:  beta -> pi/2 + 2 pi a_+   (nu -> +inf),
                             beta -> -pi/2 + 2 pi a_-  (nu -> -inf).

    Assembly (Lemma A0): split nu = 0 / nu >= 1 / nu <= -1; with
    a = -i w / t,
      upper sum = e^{-sigma L_+} zeta_H(sigma, 1 + a),
      lower sum = e^{-sigma L_-} zeta_H(sigma, 1 - a),
      L_+- = log t + i(+-pi/2 + 2 pi a_+-),
    and D = w * exp(L_+ zh0(1+a) - zh_d0(1+a))
              * exp(L_- zh0(1-a) - zh_d0(1-a)).
    """
    t = 2 * math.pi / math.log(q)
    a = -1j * complex(w) / t
    lp = math.log(t) + 1j * (math.pi / 2 + 2 * math.pi * ap)
    lm = math.log(t) + 1j * (-math.pi / 2 + 2 * math.pi * am)
    return (complex(w)
            * cmath.exp(lp * zh0(1 + a) - zh_d0(1 + a))
            * cmath.exp(lm * zh0(1 - a) - zh_d0(1 - a)))


def f_c(c, q, w):
    """The vacuum-term scheme family on the full vertical ladder."""
    return cmath.exp(c * complex(w) * math.log(q)) * (
        1 - cmath.exp(-complex(w) * math.log(q)))


def main():
    qs = [2, 3, 7]
    ws = [0.7 + 0.3j, 0.31 - 1.2j, 1.5, 0.25 + 2.1j]

    print("== G1: window classification -- D_{a+,a-} = "
          "(-1)^{a_+ + a_-} q^{-(a_+ - a_-)w} (1 - q^{-w}), slope in Z ==")
    worst = 0.0
    for q in qs:
        for w in ws:
            for ap in (-1, 0, 1, 2):
                for am in (-1, 0, 1):
                    lhs = D_window(q, w, ap, am)
                    rhs = ((-1) ** (ap + am)
                           * cmath.exp(-(ap - am) * complex(w) * math.log(q))
                           * (1 - cmath.exp(-complex(w) * math.log(q))))
                    worst = max(worst, abs(lhs - rhs) / abs(rhs))
    check("G1 closed form, all windows", worst < TOL,
          f"worst rel err {worst:.2e}")
    # principal window = Deninger value; (0,1) = the C_2-image scheme
    q, w = 3, 0.6 + 0.9j
    err0 = abs(D_window(q, w, 0, 0) - (1 - q ** (-w))) / abs(1 - q ** (-w))
    err1 = abs(D_window(q, w, 0, 1) + q ** w * (1 - q ** (-w))) / abs(
        q ** w * (1 - q ** (-w)))
    check("G1 principal = 1 - q^{-w} (Deninger/J-doc G4)", err0 < TOL,
          f"rel err {err0:.2e}")
    check("G1 C_2-image window = -q^{w}(1 - q^{-w})", err1 < TOL,
          f"rel err {err1:.2e}")

    print("== G2: rigidity -- negation-naturality iff b = (log q)/2, "
          "u = -1 ==")
    ok_all = True
    detail = []
    for q in qs:
        bgrid = [0.0, 0.5 * math.log(q), math.log(q), -math.log(q),
                 0.25 * math.log(q), 0.7391 * math.log(q), 2 * math.log(q)]
        for b in bgrid:
            f = lambda w: cmath.exp(b * complex(w)) * (
                1 - cmath.exp(-complex(w) * math.log(q)))
            w0 = ws[0]
            u = f(-w0) / f(w0)  # forced value of the unit at the anchor
            defect = max(abs(f(-w) - u * f(w)) / abs(f(w)) for w in ws[1:])
            is_nat = defect < 1e-13
            should = abs(b - 0.5 * math.log(q)) < 1e-15
            if is_nat != should:
                ok_all = False
                detail.append(f"(q={q}, b/log q={b / math.log(q)}: "
                              f"defect {defect:.2e})")
            if should and is_nat and abs(u + 1) > 1e-13:
                ok_all = False
                detail.append(f"(q={q}: unit u={u} != -1)")
    check("G2 negation-natural iff b = (log q)/2, with u = -1", ok_all,
          "verified on full (q, b, w) grid" if ok_all else "; ".join(detail))

    print("== G3: C_2-average of Deninger + image = symmetric scheme "
          "(mu_4 unit); pair-modulus assembly = 2 sinh exactly ==")
    for q in (3, 5):
        for w in (0.6 + 0.9j, 1.1 - 0.4j):
            gm = cmath.sqrt(D_window(q, w, 0, 0) * D_window(q, w, 0, 1))
            sym = f_c(0.5, q, w)
            unit = gm / sym
            ok = min(abs(unit - z) for z in (1, -1, 1j, -1j)) < 1e-12
            check(f"G3 sqrt(P+ P-)/f_half in mu_4, q={q} w={w}", ok,
                  f"unit {unit:.6f}")
    # pair-modulus assembly: w * prod_reg (t nu)^2 * prod (1 + w^2/(t nu)^2)
    NMAX = 200000
    for q, w in ((3, 0.35 + 0.2j), (5, 1.1)):
        t = 2 * math.pi / math.log(q)
        head = complex(w) * ((1 / t) * 2 * math.pi)  # prod_reg (t nu)^2 = 2pi/t
        tail = complex(1.0)
        for n in range(1, NMAX + 1):
            tail *= 1 + (complex(w) / (t * n)) ** 2
        val = head * tail
        target = 2 * cmath.sinh(complex(w) * math.log(q) / 2)
        err = abs(val - target) / abs(target)
        check(f"G3 pair-modulus = 2 sinh(w log q/2), q={q}", err < 1e-4,
              f"rel err {err:.2e} (tail-limited)")

    print("== G4: conjugation (Schwarz) holds for EVERY real-c scheme: "
          "no selection ==")
    worst = 0.0
    for q in qs:
        for w in ws:
            for c in (0.0, 0.25, 0.5, 1.0, -0.7):
                lhs = f_c(c, q, complex(w).conjugate())
                rhs = f_c(c, q, w).conjugate()
                worst = max(worst, abs(lhs - rhs) / abs(rhs))
    check("G4 Schwarz f_c(conj w) = conj f_c(w) for all real c",
          worst < 1e-14, f"worst rel err {worst:.2e}")

    print("== G5: principal-value truncation characterization ==")
    q, N = 3, 4000
    t = 2 * math.pi / math.log(q)
    for w in (0.45 - 0.8j, 0.9):
        pn = complex(w)
        for nu in range(1, N + 1):
            pn *= (complex(w) ** 2 + (t * nu) ** 2) / (t * nu) ** 2
        target = (2 / math.log(q)) * cmath.sinh(complex(w) * math.log(q) / 2)
        err = abs(pn - target) / abs(target)
        check(f"G5 balanced truncation -> const * f_half, w={w}",
              err < 1e-4, f"rel err {err:.2e} (O(1/N))")
        # fixed end-offset washes out
        pn_off = pn * (complex(w) + 1j * t * (N + 1)) / (1j * t * (N + 1))
        err_off = abs(pn_off - target) / abs(target)
        check(f"G5 offset-by-1 invariance, w={w}", err_off < 1e-3,
              f"rel err {err_off:.2e} (O(1/N))")
    # ratio-r truncation drifts by exp(-i (w/t) log r)
    w, r = 0.45 - 0.8j, 2
    extra = complex(1.0)
    for nu in range(N + 1, r * N + 1):
        extra *= 1 + complex(w) / (1j * t * nu)
    pred = cmath.exp(-1j * (complex(w) / t) * math.log(r))
    err = abs(extra - pred) / abs(pred)
    check("G5 ratio-2 truncation drift = exp(-i (w/t) log 2)", err < 1e-4,
          f"rel err {err:.2e}")

    print("== G6: recentering w -> w - it: integer-c invariant, "
          "c = 1/2 flips sign (lambda^{1/2} / double cover) ==")
    for q in qs:
        t = 2 * math.pi / math.log(q)
        w = 0.62 + 0.37j
        inv0 = abs(f_c(0, q, w - 1j * t) - f_c(0, q, w)) / abs(f_c(0, q, w))
        inv1 = abs(f_c(1, q, w - 1j * t) - f_c(1, q, w)) / abs(f_c(1, q, w))
        flip = abs(f_c(0.5, q, w - 1j * t) + f_c(0.5, q, w)) / abs(
            f_c(0.5, q, w))
        check(f"G6 q={q} c=0,1 invariant; c=1/2 anti-invariant",
              inv0 < 1e-13 and inv1 < 1e-13 and flip < 1e-13,
              f"defects {inv0:.1e}, {inv1:.1e}, sign-flip {flip:.1e}")

    print("== G7: exact finite-level parity; vacuity of the linear "
          "residual Weyl action ==")
    q, N = 3, 60
    t = 2 * math.pi / math.log(q)

    def p_trunc(w):
        val = complex(w)
        for nu in range(1, N + 1):
            val *= (complex(w) + 1j * t * nu) * (complex(w) - 1j * t * nu)
        return val

    w = 0.7 + 0.3j
    err = abs(p_trunc(-w) + p_trunc(w)) / abs(p_trunc(w))
    check("G7 P_N(-w) = -P_N(w) exactly (finite-level negation parity)",
          err < 1e-13, f"rel err {err:.2e}")
    # finite model of the linear residual Weyl action: g = diag((-1)^nu)
    # commutes with Theta = diag(w + i t nu): commutator is identically 0,
    # so g-conjugation preserves the eigenvalue MULTISET pointwise and
    # imposes no constraint on any isomorphism-invariant determinant.
    worst = 0.0
    for nu in range(-N, N + 1):
        g = (-1) ** nu
        theta = complex(w) + 1j * t * nu
        worst = max(worst, abs(g * theta - theta * g))
    check("G7 [g, Theta] = 0 (linear Weyl action commutes; constraint "
          "is empty)", worst == 0.0, f"max |commutator| {worst:.1e}")

    print()
    if FAIL:
        print(f"FAILED gates: {FAIL}")
    else:
        print("ALL PASS")


main()
sys.exit(0 if not FAIL else 1)
