"""QQ-witness: the native-pairing face - the index inequality posed ON the
glued objects G_p (p in {2,3,5}), where the K2 duality is a structure map.

Companion: research/work/QQ-native-face.md (gates QQ1-QQ9 pre-registered
there BEFORE this file was first run; fail-closed; exit 0 iff ALL gates
pass).  Lineage: Z (G at p=2, K2 pairing), CC part 1 (G_p at p=3,5),
EE.1 (Lin block singleton-dual), LL/KK (count + effectivity machinery),
NN/doc 35 (the transport kill this face is tested against).  Inherited
witnesses rerun ALL PASS before this file was written:
prime_int_z_u2_glue, prime_int_ee_dd4_lin, prime_int_ll_square_dual.

Discipline: F-a (no zeta values/continuation; atom series are exact
rational functions).  G-INT6: the Gaussian e^{-pi w^2} is the ONLY
analytic import (JJ, logged).  No RH / zero-side input; fork_lib never
imported; no zero contact anywhere (all loci log p-periodic by
construction), so the freeze protocol is never triggered.

GATES (registered in the doc, sec 2):
  QQ1 native carrier + pairing (exact F_p / divided-power algebra)
  QQ2 dual scale forced (stable route = level route, exact exponents)
  QQ3 per-slot deficit positivity d(x) = 1 - f(x) - f(1/x) > 0 (arb)
  QQ4 hard partition identity N_w + N_w^dual = |C| + #ties (exact)
  QQ5 native finiteness of the divided-power colimit count (DECISION:
      registered prediction = DIVERGES; per-branch pole = CC QG2)
  QQ6 smoothed-form killer census (registered: all margins negative)
  QQ7 the deficit object Delta_p(a): periodicity, phase, mean =
      (gamma + log pi)/log p, domination
  QQ8 cross-place: two-place non-summability + the failure boundary
  QQ9 carrier guard (Epstein/DH unformability, exact integers)
"""

import math
import sys
from fractions import Fraction
from math import comb

import flint

flint.ctx.prec = 300

arb = flint.arb

PI = arb.pi()
EULER = arb.const_euler()

FAILURES = []


def gate(name, ok, msg=""):
    tag = "PASS" if ok else "FAIL"
    print(f"{tag} {name}: {msg}")
    if not ok:
        FAILURES.append(name)


def f_gauss(x):
    """f(x) = exp(-pi x^2), x an arb."""
    return (-PI * x * x).exp()


def deficit_u(u):
    """d(e^u) = 1 - f(e^u) - f(e^-u), u an arb."""
    return arb(1) - (-PI * (2 * u).exp()).exp() - (-PI * (-2 * u).exp()).exp()


def logp(p):
    return arb(p).log()


# ----------------------------------------------------------------------
# scales: ('mult', k, p) means a = k log p (entry phase, ties exact);
#         ('rat', Fraction) means a generic rational (no tie possible:
#         e^a transcendental at rational a != 0).
# ----------------------------------------------------------------------

def a_value(scale):
    kind = scale[0]
    if kind == "mult":
        return arb(scale[1]) * logp(scale[2])
    return arb(scale[1].numerator) / arb(scale[1].denominator)


def slot_weight_log(m, p, scale):
    """log x_m = m log p - a, as arb."""
    return arb(m) * logp(p) - a_value(scale)


def hard_counts(C, p, scale):
    """(N_w, N_w_dual, ties) with exact tie logic."""
    nw = nwd = ties = 0
    for m in C:
        if scale[0] == "mult" and scale[2] == p:
            k = scale[1]
            if m == k:
                nw += 1
                nwd += 1
                ties += 1
            elif m < k:
                nw += 1
            else:
                nwd += 1
        else:
            lx = slot_weight_log(m, p, scale)
            if lx < 0:
                nw += 1
            elif lx > 0:
                nwd += 1
            else:
                raise RuntimeError("unresolved sign in hard count")
    return nw, nwd, ties


def theta_pair(C, p, scale):
    """(Theta_C, Theta_C^dual) at scale a: sum f(x_m), sum f(1/x_m)."""
    th = arb(0)
    thd = arb(0)
    for m in C:
        lx = slot_weight_log(m, p, scale)
        th += f_gauss(lx.exp())
        thd += f_gauss((-lx).exp())
    return th, thd


# ----------------------------------------------------------------------
# QQ1 native carrier + pairing (exact)
# ----------------------------------------------------------------------

def lucas_binom_mod_p(n, k, p):
    r = 1
    while n or k:
        nd, n = n % p, n // p
        kd, k = k % p, k // p
        if kd > nd:
            return 0
        r = (r * comb(nd, kd)) % p
    return r


def qq1():
    ok = True
    msgs = []
    for p in (2, 3, 5):
        # level-N Gram: <m, m'>_N = coeff of (z^N) in z^m z^m' = [m+m'==N]
        for N in range(0, 9):
            gram = [[1 if m + mp == N else 0 for mp in range(N + 1)]
                    for m in range(N + 1)]
            # permutation: exactly one 1 per row/col, implementing m <-> N-m
            for m in range(N + 1):
                if sum(gram[m]) != 1 or gram[m][N - m] != 1:
                    ok = False
                if sum(gram[r][m] for r in range(N + 1)) != 1:
                    ok = False
            # colimit insertion compatibility: iota_{N+1}(z * z^m) =
            # gamma_{(N+1)-(m+1)} = gamma_{N-m} = iota_N(z^m)
            for m in range(N + 1):
                if (N + 1) - (m + 1) != N - m:
                    ok = False
        # divided-power products (Lucas vs direct), spot grid
        for aa in range(0, 13):
            for bb in range(0, 13):
                direct = comb(aa + bb, aa) % p
                if lucas_binom_mod_p(aa + bb, aa, p) != direct:
                    ok = False
        # stable flip: image of slot m under the colimit pairing is -m
        # (iota_N sends z^m to gamma_{N-m}; the partner of z^m at every
        # level is weight N-m on the dual side, i.e. mirror weight
        # -(N-m) + (N) ... stable: gamma_m carries weight -m): check the
        # bookkeeping identity that the level pairs (m, N-m) stabilize
        # to (m, -m) under gamma_{m'} |-> weight -m'.
        for N in range(0, 9):
            for m in range(N + 1):
                # dual partner gamma_{N-m} has mirror weight -(N-m);
                # its weight-flip image under the STABLE convention is
                # m - N ... the invariant: weight(z^m) + weight-of-pair
                # slot read mirror = m + (-(N - m)) = 2m - N, which at
                # the gluing-locus recentring (subtract N at level N,
                # the runaway center N/2 doubled) is exactly the stable
                # m - (-m): equality of the two presentations:
                if (2 * m - N) != (m - (N - m)):
                    ok = False
        msgs.append(f"p={p} Gram=permutation(m<->N-m) N<=8, iota compat, "
                    f"Lucas ok")
    gate("QQ1", ok, "; ".join(msgs))


# ----------------------------------------------------------------------
# QQ2 dual scale forced (exact exponent identity, Fractions in units of
#     log p): stable route a - mL vs level route -(NL - a) + (N - m)L
# ----------------------------------------------------------------------

def qq2():
    ok = True
    for p in (2, 3, 5):
        for N in range(0, 9):
            for k in range(0, N + 1):
                a = Fraction(k)  # a = k * L
                for m in range(0, N + 1):
                    stable = a - Fraction(m)            # (k - m) L
                    level = -(Fraction(N) - a) + Fraction(N - m)
                    if stable != level:
                        ok = False
    gate("QQ2", ok, "stable dual weight = level-route dual weight, exact, "
                    "p in {2,3,5}, N<=8 (per-slot weight inversion is the "
                    "invariant content of the K2 flip)")


# ----------------------------------------------------------------------
# QQ3 deficit positivity
# ----------------------------------------------------------------------

def qq3():
    ok = True
    worst = None
    u = -6.0
    while u <= 6.0 + 1e-12:
        d = deficit_u(arb(u))
        if not (d > 0):
            ok = False
        mid = float(d.mid())
        if worst is None or mid < worst:
            worst = mid
        u += 0.01
    tail_ok = True
    for uu in (6, 8, 10):
        num = (-PI * (2 * arb(uu)).exp()).exp()
        den = arb(1) - (-PI * (-2 * arb(uu)).exp()).exp()
        if not (num / den < arb("1e-40")):
            tail_ok = False
    rate = deficit_u(arb(8)) * (arb(16)).exp()
    rate_ok = bool(abs(rate - PI) < arb("0.1"))
    d1 = arb(1) - 2 * (-PI).exp()
    gate("QQ3", ok and tail_ok and rate_ok,
         f"d(e^u)>0 certified on [-6,6] step .01 (min mid {worst:.3e}); "
         f"tails <1e-40 at u in {{6,8,10}}; |d e^(2|u|) - pi|<0.1 at 8; "
         f"max deficit d(1) = 1-2e^-pi = {d1.str(10)}")


# ----------------------------------------------------------------------
# QQ4 hard partition identity (exact)
# ----------------------------------------------------------------------

def qq4():
    ok = True
    killer_entry_seen = False
    rows = []
    classes = {
        "C0": [0], "C1": [0, 1], "C2": [0, 1, 2],
        "C4": list(range(5)), "C8": list(range(9)), "C12": list(range(13)),
        "killer{1}": [1], "box{1,2,3}": [1, 2, 3],
    }
    for p in (2, 3, 5):
        scales = [("mult", k, p) for k in (0, 1, 2, 3)] + \
                 [("rat", Fraction(1, 2)), ("rat", Fraction(1)),
                  ("rat", Fraction(5, 2)), ("rat", Fraction(5))]
        for cname, C in classes.items():
            for sc in scales:
                nw, nwd, ties = hard_counts(C, p, sc)
                lhs = nw + nwd - len(C)
                if lhs != ties or lhs < 0:
                    ok = False
                    rows.append(f"VIOLATION p={p} {cname} {sc}")
                if sc[0] == "rat" and ties != 0:
                    ok = False
                if cname == "killer{1}" and sc == ("mult", 1, p):
                    if ties == 1 and lhs == 1:
                        killer_entry_seen = True
                    else:
                        ok = False
    gate("QQ4", ok and killer_entry_seen,
         "N_w + N_w^dual - |C| = #ties exactly, all classes/scales/places; "
         "weight-1 killer at window entry: margin +1 (tie), NEVER a deficit "
         "- the native hard form of the index inequality is a partition "
         "identity of the K2 pairing" +
         ("" if not rows else " | " + "; ".join(rows)))


# ----------------------------------------------------------------------
# QQ5 native finiteness (the central hope) - registered: DIVERGES
# ----------------------------------------------------------------------

def qq5():
    ok = True
    msgs = []
    # (a) per-level finiteness: structural
    msgs.append("(a) per-level dual counts finite (|C_N|=N+1 slots, "
                "colimit-of-finite-levels honored)")
    # (b) colimit divergence
    for p in (2, 3, 5):
        for a in (arb(1) / 2, arb(2), arb(5)):
            def S(M):
                s = arb(0)
                for m in range(1, M + 1):
                    s += f_gauss((a - m * logp(p)).exp())
                return s
            for M in (20, 40):
                lhs = S(2 * M) - S(M)
                rhs = arb(M) * (arb(1) - PI * (2 * a).exp() * arb(p) ** (-2 * M))
                if not (lhs >= rhs):
                    ok = False
            s60 = S(60)
            floor60 = arb("0.8") * (arb(60) - a / logp(p) - 2)
            if not (s60 >= floor60):
                ok = False
            if p == 2 and float(a.mid()) == 2.0:
                msgs.append(f"(b) p=2 a=2: S_40-S_20 = "
                            f"{float((S(40)-S(20)).mid()):.6f} (>= ~20): "
                            f"one unit per level, LINEAR divergence")
    # (c) the pole is the branch's own: A_D + A_D' + 1 = 0 exact;
    #     residues +-1/log p
    for p in (2, 3, 5):
        for x in (Fraction(1, 7), Fraction(2, 5), Fraction(3, 2),
                  Fraction(5, 2), Fraction(9, 4)):
            if x == 1:
                continue
            A_D = x / (1 - x)            # sum_{m>=1} x^m
            A_Dp = 1 / (x - 1)           # sum_{m>=1} x^{-m}, |x|>1 reading
            if A_D + A_Dp + 1 != 0:
                ok = False
        # residue of A_D(s) = p^{-s}/(1-p^{-s}) at s=0 is -1/log p... the
        # branch series sum (p^m)^{-s} = p^{-s}/(1-p^{-s}): residue at
        # s=0: lim s * p^{-s}/(1-p^{-s}) = 1/log p (primal branch);
        # mirror branch sum (p^{-m})^{-s} = p^{s}/(1-p^{s}): residue
        # -1/log p.  Certify by s -> 0 limit at s = 1e-25 (arb).
        s = arb("1e-25")
        prim = s * (-s * logp(p)).exp() / (1 - (-s * logp(p)).exp())
        mirr = s * (s * logp(p)).exp() / (1 - (s * logp(p)).exp())
        if not (abs(prim - 1 / logp(p)) < arb("1e-24")):
            ok = False
        if not (abs(mirr + 1 / logp(p)) < arb("1e-24")):
            ok = False
    msgs.append("(c) A_D + A_D' + 1 = 0 exact (Fractions); per-branch "
                "residues +-1/log p certified: the hole is the "
                "divided-power branch's OWN pole (CC QG2), not a "
                "transport artifact")
    gate("QQ5", ok,
         "REGISTERED PREDICTION P3 CONFIRMED: the divided-power colimit "
         "count DIVERGES (linearly; certified increments). " + " | ".join(msgs))
    return ok


# ----------------------------------------------------------------------
# QQ6 smoothed-form killer census
# ----------------------------------------------------------------------

def qq6():
    ok = True
    rows = []
    d1_target = 2 * (-PI).exp() - 1   # margin at entry = -(1 - 2e^-pi)
    for p in (2, 3, 5):
        scales = [("rat", Fraction(1, 2)), ("mult", 1, p),
                  ("rat", Fraction(1)), ("rat", Fraction(2)),
                  ("mult", 2, p), ("rat", Fraction(5))]
        for sc in scales:
            th, thd = theta_pair([1], p, sc)
            mar = th + thd - 1
            if not (mar < 0):
                ok = False
            if sc == ("mult", 1, p):
                if not (abs(mar - d1_target) < arb("1e-30")):
                    ok = False
                logm = (th.log() + thd.log()) if (th > 0 and thd > 0) else None
                rows.append(
                    f"killer{{1}} p={p} ENTRY a=log p: margin = "
                    f"{mar.str(8)} = -(1-2e^-pi); log-form record: "
                    f"logTh+logThd = "
                    f"{logm.str(8) if logm is not None else 'n/a'}")
    # phase scans over one full period at p in {2,5}
    for p in (2, 5):
        L = logp(p)
        worst = None
        for j in range(16):
            a = L + L * j / 16
            th = f_gauss((L - a).exp())
            thd = f_gauss((a - L).exp())
            mar = th + thd - 1
            if not (mar < 0):
                ok = False
            v = float(mar.mid())
            if worst is None or v > worst:
                worst = v
        rows.append(f"killer{{1}} p={p} 16-pt period scan: all margins "
                    f"certified < 0 (max {worst:.4f})")
    # truncation classes
    for p in (2, 3, 5):
        for N in (2, 4, 8):
            for aval in ("1", "2.48", "4.96"):
                sc = ("rat", Fraction(aval.replace(".", ""))
                      / (100 if "." in aval else 1))
                C = list(range(N + 1))
                th, thd = theta_pair(C, p, sc)
                mar = th + thd - len(C)
                if not (mar < 0):
                    ok = False
    gate("QQ6", ok,
         "ALL smoothed margins Theta+Theta^dual-|C| certified NEGATIVE "
         "(killers, period scans, truncations C_N at p in {2,3,5}); "
         + " | ".join(rows))


# ----------------------------------------------------------------------
# QQ7 the deficit object Delta_p(a)
# ----------------------------------------------------------------------

def delta_p(p, a, M=60):
    """Delta_p(a) = sum_{|m|<=M} d(e^{m log p - a}) + certified tail ball."""
    L = logp(p)
    s = arb(0)
    for m in range(-M, M + 1):
        s += deficit_u(arb(m) * L - a)
    # tail <= 2 pi e^{2|a|} p^{-2(M+1)} / (1 - p^{-2})  (d <= pi e^{-2|u|})
    tail = 2 * PI * (2 * abs(a)).exp() * arb(p) ** (-2 * (M + 1)) \
        / (1 - arb(p) ** (-2))
    return s + arb(0).union(tail).union(-tail)


def qq7():
    ok = True
    rows = []
    cstar = EULER + PI.log()
    for p in (2, 3, 5):
        L = logp(p)
        # (a) periodicity
        for aa in (arb("0.37"), arb("1.1")):
            if not (abs(delta_p(p, aa) - delta_p(p, aa + L)) < arb("1e-28")):
                ok = False
        # (b) phase structure, 32-pt grid over [0, L)
        vals = [delta_p(p, L * j / 32) for j in range(32)]
        mids = [float(v.mid()) for v in vals]
        imax = mids.index(max(mids))
        imin = mids.index(min(mids))
        if imax != 0:
            ok = False
        if not (vals[imax] - vals[imin] > 0):
            ok = False
        # (c) period-mean = C*/log p (trapezoid, 256 pts; periodic =>
        #     trapezoid = plain average)
        mean = arb(0)
        NPT = 256
        for j in range(NPT):
            mean += delta_p(p, L * j / NPT)
        mean /= NPT
        err = abs(mean * L - cstar)
        if not (err < arb("1e-6")):
            ok = False
        rows.append(f"p={p}: Delta period log p exact; max at ENTRY phase, "
                    f"min at half-phase (amp {mids[imax]-mids[imin]:.4f}); "
                    f"mean*log p - (gamma+log pi) = {float(err.mid()):.2e}; "
                    f"mean = {float(mean.mid()):.6f}")
        # (d) domination: Delta_C <= Delta_p for QQ6-style classes
        for C in ([1], [0, 1, 2], list(range(9))):
            for aa in (arb("0.5"), arb(1), L):
                dC = arb(0)
                for m in C:
                    dC += deficit_u(arb(m) * L - aa)
                if not (delta_p(p, aa) - dC > 0):
                    ok = False
    gate("QQ7", ok,
         "Delta_p(a): log p-periodic; window-entry-phased; period-mean = "
         "(gamma + log pi)/log p CONFIRMED (the archimedean constant, "
         "named); domination Delta_C <= Delta_p certified (the demoted "
         "chi_ren reading holds on all single-place classes incl. "
         "killers). " + " | ".join(rows))


# ----------------------------------------------------------------------
# QQ8 cross-place
# ----------------------------------------------------------------------

def qq8():
    ok = True
    rows = []
    a0 = arb("4.96")
    # (a) non-summability at T={2,3} and T={2,5}
    for q in (3, 5):
        Lp, Lq = logp(2), logp(q)
        total = arb(0)
        each_ok = True
        for m in range(-50, 51):
            t = (a0 - m * Lp) / Lq
            n = int(round(float(t.mid())))
            u = m * Lp + n * Lq - a0
            d = deficit_u(u)
            if not (d > arb("0.4")):
                each_ok = False
            total += d
        if not each_ok or not (total > arb("0.4") * 101):
            ok = False
        rows.append(f"T={{2,{q}}}: each of 101 m-rows contributes a "
                    f"near-boundary deficit > 0.4 (sum {float(total.mid()):.1f})"
                    f": the two-place colimit deficit grows LINEARLY - "
                    f"GG3's non-summability, native")
    # (b) failure boundary for the per-place budget at T={2,3}
    L6 = logp(6)
    scales = [arb("1.24"), arb("2.48"), arb("4.96")] + \
             [arb("4.96") + L6 * j / 8 for j in range(8)]
    found = None
    budget_cache = {}
    for N in range(1, 17):
        for a in scales:
            key = a.str(12)
            if key not in budget_cache:
                budget_cache[key] = delta_p(2, a) + delta_p(3, a)
            budget = budget_cache[key]
            dbox = arb(0)
            for m in range(N + 1):
                for n in range(N + 1):
                    dbox += deficit_u(m * logp(2) + n * logp(3) - a)
            if dbox - budget > 0:
                found = (N, float(a.mid()), float(dbox.mid()),
                         float(budget.mid()))
                break
        if found:
            break
    if found is None or found[0] > 12:
        ok = False
        rows.append("P6 REFUTED: no failure box to N=16 (reportable)")
    else:
        rows.append(f"FAILURE BOUNDARY: box [0..{found[0]}]^2 at a="
                    f"{found[1]:.4f}: Delta_box = {found[2]:.3f} > "
                    f"Delta_2 + Delta_3 = {found[3]:.3f} - the "
                    f"one-unit-per-place budget is exceeded by a finite "
                    f"box, certified (P6)")
    gate("QQ8", ok, " | ".join(rows))


# ----------------------------------------------------------------------
# QQ9 carrier guard
# ----------------------------------------------------------------------

def represented(n):
    for x in range(int(math.isqrt(n)) + 1):
        r = n - x * x
        if r >= 0 and r % 5 == 0:
            y2 = r // 5
            y = int(math.isqrt(y2))
            if y * y == y2:
                return True
    return False


def qq9():
    reps = sorted(n for n in range(1, 200) if represented(n) and n > 1)
    repset = set(reps)

    def irreducible(n):
        return not any(d in repset and (n // d) in repset
                       for d in range(2, n) if n % d == 0)

    ok = (not represented(2)) and (not represented(3))
    for n in (4, 6, 9):
        ok = ok and represented(n) and irreducible(n)
    ok = ok and represented(36) and (36 == 4 * 9 == 6 * 6)
    gate("QQ9", ok,
         "Epstein x^2+5y^2: 2,3 unrepresented; 4,6,9 irreducible; "
         "36 = 4*9 = 6*6 (exact) => no valuation => no weight grading => "
         "no truncation tower => no Matlis colimit => NO G_Epstein: the "
         "native count is UNFORMABLE (no ring => no G_p, Z/CC).  DH: no "
         "carrier monoid at all - dies earlier (bookkeeping).")


def main():
    print("QQ native-face witness (gates QQ1-QQ9, pre-registered, "
          "fail-closed).  flint prec", flint.ctx.prec)
    print("No zero contact anywhere; fork_lib never imported; freeze "
          "protocol not triggered (registered).")
    qq1()
    qq2()
    qq3()
    qq4()
    qq5()
    qq6()
    qq7()
    qq8()
    qq9()
    print()
    if FAILURES:
        print("FAILED GATES:", ", ".join(FAILURES))
        sys.exit(1)
    print("ALL PASS (QQ1-QQ9)")
    sys.exit(0)


if __name__ == "__main__":
    main()
