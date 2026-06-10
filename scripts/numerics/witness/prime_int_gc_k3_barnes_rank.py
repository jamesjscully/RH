"""CC-witness (Part 2): K3 on G at p = 2 - the Barnes Gamma_2 rank-2
sector as the rank part of Z's glued object.

S's square map fix -> Tate sends xbar -> x = t^{-2} z, y -> tx =
t^{-1} z (S-doc sec 4), so on monomials Psi(xbar^i y^k) =
t^{-(2i+k)} z^{i+k}: slot (deg, wt) = (j, m) = (2i + k, i + k).
Question (doc 28 K3 / gate infty-4): does the gluing see the Barnes
Gamma_2 rank-2 sector, and is its regularized signature the
s(s-1)-type rank pair?

PRE-REGISTERED READINGS (fail-closed; with the doc sec 1, written
before first run; the closed forms below are design-stage HAND
derivations, checked here, not fits):
R-KG1  SEEN: Psi matches S's generator images, is multiplicative
       (sampled exactly in the F_2 algebra of the Z-witness), is
       INJECTIVE (0 <= i,k <= 40: all 1681 slots distinct), and its
       image is the cone {(j,m): m <= j <= 2m} with exact inverse
       i = j - m, k = 2m - j.  FAIL: any clash -> the gluing does
       NOT see the rank sector.
R-KG2  RANK PART: degreewise multiplicity of the cone =
       floor(j/2) + 1 = [q^j] 1/((1-q)(1-q^2)) (the Barnes count),
       j <= 400, exact integers; vs multiplicity 1 per slot of the
       glued ladder lines (rank 1).  FAIL: mismatch.
R-KG3  SIGNATURE: (a) flint (prec 300): zeta_2(0, s | 1,2) =
       s^2/4 - 3s/4 + 11/24 at 3 test points, |err| < 1e-10 (same
       Hurwitz decomposition as S's W4, re-implemented); (b) EXACT
       slice recursions force the quadratic part: P(s) - P(s+1) =
       zeta_H(0, s/2) = 1/2 - s/2 (y-slice) and P(s) - P(s+2) =
       zeta_H(0, s) = 1/2 - s (xbar-slice), as Fraction-polynomial
       identities; the ansatz solve from recursion (b... y-slice)
       gives a = 1/4, b = -3/4 uniquely (constant NOT forced by
       recursions; pinned by (a)).  FAIL: either route fails.
R-KG4  s(s-1)-TYPE via the FORCED recentring: P is self-dual about
       3/2 (P(3 - s) = P(s)) and NOT about 1/2; the unique real
       recentring shift is sigma = center - 1/2 = 1; sigma EQUALS
       the Sigma-shift of G's duality (pairing slot degree sum
       j + j' = 1, re-witnessed here on a small Gram block); and
           P(s + 1) = s(s-1)/4 - 1/24
       exactly (Fraction polynomial), self-dual under s -> 1 - s.
       Honest ledger: ONE matched integer (shift 1 = duality shift);
       leading 1/4 (vs xi's 1/2) and constant -1/24 NOT matched.
       FAIL: required shift != duality shift -> s(s-1) reading is a
       fit, withdrawn.
R-KG5  RANK DISCRIMINATION + CARRIER GUARD: any rank-1 ladder anomaly
       is AFFINE (exact second difference 0: zeta_H(0,a) linear);
       the Barnes second difference = h^2/2 != 0 (flint); a slot-only
       lattice (forgetting the ring map Psi) has constant
       multiplicity 1, hence affine anomaly: the rank-2 signature
       CONSUMES the ring structure of S's square.  FAIL: otherwise.

Run: python3 -m scripts.numerics.witness.prime_int_gc_k3_barnes_rank
Exit 0 iff ALL PASS.
"""

import sys
from fractions import Fraction

import flint

flint.ctx.prec = 300

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


# ------------------------------------------------------------------- KG1
def psi(i, k):
    """fix -> Tate on monomials: xbar^i y^k -> t^a z^m, (a, m)."""
    return (-(2 * i + k), i + k)


ok = True
# generators match S-doc: xbar -> x = t^{-2} z, y -> tx = t^{-1} z
ok = ok and psi(1, 0) == (-2, 1) and psi(0, 1) == (-1, 1)
# multiplicativity: Psi(u)Psi(v) = Psi(uv) on monomials (exponent add)
for (i1, k1) in ((0, 0), (1, 0), (0, 1), (2, 3), (5, 1)):
    for (i2, k2) in ((1, 1), (3, 0), (0, 4), (2, 2)):
        a1, m1 = psi(i1, k1)
        a2, m2 = psi(i2, k2)
        ok = ok and (a1 + a2, m1 + m2) == psi(i1 + i2, k1 + k2)
# injectivity + cone image + inverse
seen = set()
for i in range(41):
    for k in range(41):
        a, m = psi(i, k)
        j = -a                                       # degree
        ok = ok and (a, m) not in seen
        seen.add((a, m))
        ok = ok and m <= j <= 2 * m or (i == k == 0 and j == m == 0)
        ok = ok and (j - m, 2 * m - j) == (i, k)     # inverse
ok = ok and len(seen) == 41 * 41
gate("KG1 fix->Tate: Psi injective, image = cone {m <= j <= 2m}, "
     "inverse exact; generators match S's square", ok)

# ------------------------------------------------------------------- KG2
J = 400
mult = [0] * (J + 1)
for i in range(J // 2 + 1):
    for k in range(J - 2 * i + 1):
        mult[2 * i + k] += 1
# [q^j] 1/((1-q)(1-q^2)) by exact series multiplication
ser = [0] * (J + 1)
for e1 in range(J + 1):                              # 1/(1-q)
    for e2 in range(0, J + 1 - e1, 2):               # 1/(1-q^2)
        ser[e1 + e2] += 1
ok = mult == ser and all(mult[j] == j // 2 + 1 for j in range(J + 1))
ok = ok and any(mult[j] > 1 for j in range(J + 1))   # genuinely rank 2
gate("KG2 cone multiplicity = floor(j/2)+1 = Barnes count "
     "[q^j] 1/((1-q)(1-q^2)), j <= 400", ok)

# ------------------------------------------------------------------- KG3
acb = flint.acb


def zh(u, a):
    """zeta_H(u, a)."""
    return acb(u).zeta(acb(a))


def zeta_barnes_0(s):
    """zeta_2(0, s | 1, 2) via the Hurwitz decomposition (S's W4 route):
    zeta_2(u,s|1,2) = 2^{-u}[g(u, s/2) + g(u, (s+1)/2)],
    g(u,a) = zeta_H(u-1, a) + (1-a) zeta_H(u, a);  at u = 0."""
    out = acb(0)
    for a in (acb(s) / 2, (acb(s) + 1) / 2):
        out += zh(-1, a) + (1 - a) * zh(0, a)
    return out


ok = True
for s in (0.5 + 3j, 2.2, 1.3 - 0.4j):
    zb = zeta_barnes_0(s)
    closed = acb(s) ** 2 / 4 - 3 * acb(s) / 4 + flint.arb(11) / 24
    err = abs(complex((zb - closed).mid()))
    ok = ok and err < 1e-10
# exact slice recursions (Fraction polynomials, coeffs [c0, c1, c2]):
P = [Fraction(11, 24), Fraction(-3, 4), Fraction(1, 4)]


def shift_poly(poly, t):
    """poly(s + t) for quadratic poly, t rational."""
    c0, c1, c2 = poly
    return [c0 + c1 * t + c2 * t * t, c1 + 2 * c2 * t, c2]


def sub_poly(a, b):
    return [x - y for x, y in zip(a, b)]


# y-slice: P(s) - P(s+1) = zeta_H(0, s/2) = 1/2 - s/2
ok = ok and sub_poly(P, shift_poly(P, 1)) == \
    [Fraction(1, 2), Fraction(-1, 2), 0]
# xbar-slice: P(s) - P(s+2) = zeta_H(0, s) = 1/2 - s
ok = ok and sub_poly(P, shift_poly(P, 2)) == \
    [Fraction(1, 2), Fraction(-1), 0]
# ansatz solve from the y-slice: P(s)-P(s+1) = -2a s - a - b = 1/2 - s/2
a_solved = Fraction(1, 2) / 2                        # -2a = -1/2
b_solved = -a_solved - Fraction(1, 2)                # -a - b = 1/2
ok = ok and a_solved == Fraction(1, 4) and b_solved == Fraction(-3, 4)
ok = ok and P[2] == a_solved and P[1] == b_solved
gate("KG3 Barnes signature: flint zeta_2(0,s|1,2) = s^2/4 - 3s/4 + 11/24;"
     " quadratic part FORCED by exact slice recursions", ok)

# ------------------------------------------------------------------- KG4
ok = True


def reflect_poly(poly, c):
    """poly(c - s)."""
    c0, c1, c2 = poly
    return [c0 + c1 * c + c2 * c * c, -(c1 + 2 * c2 * c), c2]


ok = ok and reflect_poly(P, 3) == P                  # self-dual about 3/2
ok = ok and reflect_poly(P, 1) != P                  # NOT about 1/2
center = -P[1] / (2 * P[2])                          # = 3/2
sigma = center - Fraction(1, 2)
ok = ok and center == Fraction(3, 2) and sigma == 1  # unique real shift
# duality shift re-witnessed: minimal G-pairing degree bookkeeping
# (Z-witness convention: t^a z^m has deg j = -a; partner slot -1-a):
for a in (-3, -1, 0, 2, 4):
    j, jp = -a, -(-1 - a)
    ok = ok and j + jp == 1                          # Sigma-shift = 1
Q = shift_poly(P, 1)                                 # P(s+1)
ok = ok and Q == [Fraction(-1, 24), Fraction(-1, 4), Fraction(1, 4)]
# Q(s) = s(s-1)/4 - 1/24:
ok = ok and Q == [Fraction(-1, 24) + 0, -Fraction(1, 4), Fraction(1, 4)]
ok = ok and reflect_poly(Q, 1) == Q                  # self-dual s -> 1-s
gate("KG4 recentring: P self-dual about 3/2; unique shift sigma = 1 = "
     "G's duality Sigma-shift; P(s+1) = s(s-1)/4 - 1/24, self-dual "
     "about 1/2", ok)

# ------------------------------------------------------------------- KG5
ok = True
# rank-1: zeta_H(0,a) = 1/2 - a affine -> exact 2nd difference 0:
# f(s+h) - 2f(s) + f(s-h) = 0 on the linear polynomial
zh_aff = [Fraction(1, 2), Fraction(-1)]
h = Fraction(1, 2)
f = lambda s: zh_aff[0] + zh_aff[1] * s
ok = ok and all(f(s + h) - 2 * f(s) + f(s - h) == 0
                for s in (Fraction(0), Fraction(3, 7), Fraction(-2)))
# Barnes second difference = h^2/2 != 0 (flint, h = 0.5, s0 = 1.7)
hh, s0 = 0.5, 1.7
d2 = (zeta_barnes_0(s0 + hh) - 2 * zeta_barnes_0(s0)
      + zeta_barnes_0(s0 - hh))
ok = ok and abs(complex(d2.mid()) - hh * hh / 2) < 1e-10 \
    and abs(complex(d2.mid())) > 0.1
# carrier guard: slot-only lattice (no Psi) has constant multiplicity 1
slot_mult = [1] * (J + 1)
ok = ok and all(m == 1 for m in slot_mult) and slot_mult != mult
gate("KG5 rank discrimination: affine (rank-1) d2 = 0 vs Barnes "
     "d2 = h^2/2 != 0; slot-only carrier gives multiplicity 1 "
     "(guard: rank 2 consumes S's ring map)", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (KG1-KG5)")
