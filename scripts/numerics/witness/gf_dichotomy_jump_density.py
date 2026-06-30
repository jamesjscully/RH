"""gf_dichotomy_jump_density -- is the integrality-summability pole intrinsic?

INVESTIGATION (research/global-frobenius, "is the dichotomy fundamental?").

CLAIM UNDER TEST (the load-bearing robustness fact for "side A" of the
candidate fundamentality theorem). The simple pole at s=0 of the
quantization-defect series -- which makes the zeta-regularized total of an
integer dimension DIVERGE -- comes from the JUMP SET of the integer staircase,
and the jump set is GEOMETRIC with density 1/log b for EVERY integer monotone
function D(k) that tracks log_b k to O(1). Hence the pole (the obstruction to
summability) is intrinsic to integrality + scale-tracking, NOT to CC's specific
ceiling dim = ceil(log_3(2n+1)) (Prop 3.3 of arXiv:2205.01391).

WHY THIS IS THE RIGHT TEST. The regularized total is
    Sum_reg D(k) = [a.c. of Sum_k D(k) k^{-s}]_{s=0}
                 = (1/log b)(1/2 log 2pi)        [the finite log-part]
                 + D_delta(s) at s=0,            D_delta(s)=Sum_k delta(k)k^{-s}.
delta(k)=D(k)-log_b k is bounded; its continuation's pole at s=0 is carried by
the atom (jump) set J={k: D(k)>D(k-1)} via Sum_{k in J} k^{-s} ~ 1/(1-b^{-s}),
a simple pole at s=0 with residue 1/log b. If J is geometric with density
1/log b for ALL such D, the pole is universal => Sum_reg D = infinity always
=> no integer dimension theory that tracks the scale is summable. The ONLY
escape is to NOT track log_b -- i.e. to be scale-blind (side B, Efimov
arXiv:2405.12169), which is vacuous for an intersection form.

EXACT ARITHMETIC. Staircases and jump counts are computed with integer-only
operations (b^d vs k comparisons); no floats enter the integer dimension or the
jump set. The defect bound uses math.log only for the O(1) check (reported with
margin), not for any integer decision.

PRE-REGISTERED READINGS (fixed before run, fail-closed):
  R0  ceiling staircase = CC's Prop 3.3 form: D(k)=ceil(log_b k)=min{d: b^d>=k}.
      Verify D(k)-log_b k in [0,1) (the certified ceiling defect range).
  R1  UNIVERSAL JUMP DENSITY: for ceiling, floor, round, and an OFFSET
      staircase (jumps shifted by a non-geometric-looking rule), each tracking
      log_b k to O(1), the jump count J(K)=#{k<=K: D(k)>D(k-1)} satisfies
      J(K)/log K -> 1/log b. Verify |J(K)/log K - 1/log b| -> 0 as K grows
      (K up to 3^16); final relative error < 2e-2 at K=3^16 for every shape.
      => the atom density (hence the s=0 pole) is shape-INDEPENDENT.
  R2  BOUNDED DEFECT: each staircase has sup_k |D(k)-log_b k| <= 2 over the
      range (they all genuinely track the scale).
  R3  SCALE-BLIND CONTROL: a non-tracking integer function (constant D(k)=0,
      and the identity D(k)=k) does NOT have geometric jump density:
      constant has 0 jumps (density 0, summable-but-vacuous = side B);
      identity jumps every step (density ~ K/log K -> infinity, not a
      dimension). Confirms the hypothesis "tracks log_b" is exactly what forces
      the geometric jumps. Expected PASS.
  R4  BASE INDEPENDENCE (scheme leak, G-INT6): repeat R1 for b=2 and b=3; the
      density limit is 1/log b in each base => the obstruction size is
      scheme-laden but always nonzero.

VERDICT TEMPLATE: R0-R4 PASS => the geometric jump density 1/log b (the origin
of the s=0 pole) is universal across staircase shapes and depends only on the
base, not the quantization rule. Combined with the certified analytic step
(prime_cc_quantization_defect: geometric atoms => simple pole at s=0, residue
-1/(2 log b)), this supports "side A" of the fundamentality theorem: ANY integer
monotone dimension tracking the scale has a divergent regularized total. The
dichotomy's side A reduces to an elementary Tauberian lemma; only the
quantification class (which D's count as "dimension theories") is open.
"""

import math
import sys


def ceil_log(k, b):
    """min{d>=0 : b^d >= k}, integer-exact."""
    d, p = 0, 1
    while p < k:
        p *= b
        d += 1
    return d


def floor_log(k, b):
    """max{d>=0 : b^d <= k}, integer-exact."""
    d, p = 0, 1
    while p * b <= k:
        p *= b
        d += 1
    return d


def round_log(k, b):
    """nearest integer to log_b k, decided by b^d vs k geometric midpoints."""
    # log_b k rounds to d iff b^{d-1/2} <= k < b^{d+1/2} iff b^{2d-1} <= k^2 < b^{2d+1}
    d = floor_log(k, b)
    # compare k^2 to b^{2d+1}: if k^2 >= b^{2d+1}, round up
    if k * k >= b ** (2 * d + 1):
        return d + 1
    return d


def offset_log(k, b):
    """an integer staircase tracking log_b k but with a non-ceiling jump rule:
    D(k) = number of j>=1 with floor(b^j * 2 / 3) <= k. Jumps near (3/2) b^{j-1};
    still geometric (ratio b) but offset off the pure powers {b^j}."""
    d, thresh = 0, 1
    # count thresholds t_j = max(1, (2*b^j)//3) that are <= k
    j = 0
    cnt = 0
    while True:
        j += 1
        t = (2 * b ** j) // 3
        if t < 1:
            t = 1
        if t <= k:
            cnt += 1
        else:
            break
    return cnt


def jump_count(D, b, K):
    """#{2<=k<=K : D(k) > D(k-1)} plus 1 if D(1)>D(0):=0."""
    jumps = 0
    prev = 0  # D(0):=0 convention
    for k in range(1, K + 1):
        cur = D(k, b)
        if cur > prev:
            jumps += 1
        prev = cur
    return jumps


def max_defect(D, b, K):
    inv = 1.0 / math.log(b)
    m = 0.0
    for k in range(1, K + 1):
        d = D(k, b) - math.log(k) * inv
        if abs(d) > m:
            m = abs(d)
    return m


def run():
    passed = True

    def check(name, cond, detail=""):
        nonlocal passed
        tag = "PASS" if cond else "FAIL"
        if not cond:
            passed = False
        print(f"  [{tag}] {name}: {detail}")

    print("R0: ceiling staircase = CC Prop 3.3 form; defect in [0,1)")
    b = 3
    K0 = 3 ** 10
    inv = 1.0 / math.log(b)
    bad = 0
    for k in range(1, K0 + 1):
        d = ceil_log(k, b) - math.log(k) * inv
        if d < -1e-12 or d >= 1.0 + 1e-12:
            bad += 1
    check("ceil defect in [0,1)", bad == 0,
          f"violations={bad} over k<=3^10 (CC dim = ceil(log_3(2n+1)))")

    print("R1/R4: universal geometric jump density J(K)/log K -> 1/log b")
    shapes = [("ceil", ceil_log), ("floor", floor_log),
              ("round", round_log), ("offset", offset_log)]
    for b in (2, 3):
        target = 1.0 / math.log(b)
        K = b ** 16
        print(f"  base b={b}, K=b^16={K}, target 1/log b = {target:.6f}")
        for name, D in shapes:
            J = jump_count(D, b, K)
            dens = J / math.log(K)
            relerr = abs(dens - target) / target
            check(f"b={b} {name}: J/logK={dens:.5f}", relerr < 2e-2,
                  f"relerr={relerr:.4f} vs 1/log b={target:.5f}")

    print("R2: bounded defect (each staircase truly tracks the scale)")
    b = 3
    Kd = 3 ** 9
    for name, D in shapes:
        m = max_defect(D, b, Kd)
        check(f"{name} sup|defect|", m <= 2.0, f"sup|D-log_b k|={m:.4f} over k<=3^9")

    print("R3: scale-blind / non-tracking controls do NOT give density 1/log b")
    b = 3
    K = 3 ** 12
    target = 1.0 / math.log(b)
    # constant D(k)=0: zero jumps (summable-but-vacuous = side B)
    Jc = jump_count(lambda k, b: 0, b, K)
    check("constant D=0 has 0 jumps (scale-blind, side B)", Jc == 0,
          f"jumps={Jc}; density 0 != 1/log b -- summable but vacuous")
    # identity D(k)=k: jumps every step, density -> infinity (not a dimension)
    Ji = jump_count(lambda k, b: k, b, K)
    dens_i = Ji / math.log(K)
    check("identity D=k density >> 1/log b (not log-tracking)",
          dens_i > 100 * target,
          f"density={dens_i:.1f} >> {target:.3f}: linear, not logarithmic")

    print()
    if passed:
        print("ALL PASS")
        return 0
    print("SOME FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(run())
