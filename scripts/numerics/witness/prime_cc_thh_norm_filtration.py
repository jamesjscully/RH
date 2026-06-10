"""AA probe (doc 27 front 3): the strict THH layer of CC's COMPACTIFIED
(normed) object -- does the norm datum put the ARCHIMEDEAN filtration on
V's monoid-ring character?

SETTING (all theorem-sourced, zero free choices -- G-INT6):
  - CC's normed object: ||HZ||_n(F) = {phi in HZ(F) : Sum |phi(x)| <= n}
    (2022 sec 2, (1.3)): the total-mass / l1 filtration of HZ, a
    sub-S[+-1]-module.  The multiplicative structure on norms is THEIRS:
    m : HR(X) ^ HR(Y) -> HR(X ^ Y) restricts to
    ||HR||_lam ^ ||HR||_mu -> ||HR||_{lam*mu} (2022 Lemma 5.1 proof,
    citing their [2] Prop 6.1).  Hence the norm filtration on the strict
    square (HZ ^ HZ)(1_+):
        F_t = union of images of (||HZ||_lam ^ ||HZ||_mu)(1_+),
              lam * mu <= t;     N(x) = min filtration level of x.
  - V's Theorem V.1: the universal strict column invariant is the
    character chi_col(a,b,S) = Sum_j b_j [A_j] into the monoid ring
    Z[Z\\0] (A_j = column sums); multiplicative for the smash product.
  - The archimedean norm on Z[Z\\0]: ||Sum c_A [A]||_arch = Sum |c_A| |A|
    (weight of the generator [A] = |A|, the archimedean absolute value;
    multiplicative on generators: ||[A][A']|| = |A||A'|).

PRE-REGISTERED READING UNDER TEST (fixed before the runs): the CC norm,
transported along V's character, IS the archimedean filtration of the
monoid ring -- i.e. the boundary/compactification datum of CC's object
touches the strict-THH-level invariant exactly as the |.|_infty half of
the product formula, with the p-adic valuations of the SAME character
classes supplying the MIN half (W-doc faces).

GATES (fail-closed; each PASS/FAIL is exit-gated):
  N1  TRANSPORT (contraction): for every bounded representative
      (a, b, S): ||chi_col||_arch <= mass(a)*mass(b), same for chi_row,
      and |e(x)| <= ||chi_col(x)||_arch.  Hand proof one line
      (|A_j| <= mass(a), Sum_j |b_j| <= mass(b)); machine confirmation.
      Expected PASS.
  N2  BAR FILTRATION: the cyclic bar faces d_i (V's witness, incl. the
      cyclic face) preserve the norm filtration EXACTLY on canonical
      representatives: mass-product(face(x)) = mass-product(x).
      (Mechanism: the merged slot is the full outer product, and
      Sum |u_x v_y| = (Sum|u_x|)(Sum|v_y|).)  So the strict cyclic bar
      of the normed object is a norm-filtered cyclic object.  Expected
      PASS (exact equality on enumerated instances, levels 2 and 3).
  N3  MONOID-CLASS EXACTNESS: N([A]-class) = |A| exactly.  Upper: the
      single-cell representative (a=(A), b=(1)).  Lower (hand proof,
      machine-spot-checked): bucket nets are class invariants (V.1), a
      bucket [A] with net 1 forces a column of sum A, so mass(a) >= |A|
      and mass(b) >= 1; search over bounded representatives with
      matching character confirms no representative beats |A|.
      Expected PASS.
  N4  DIFFERENCE-CLASS NORM = MAX FACE VALUE: for the geometric family,
      N([p^i] - [p^j]) = 2 p^max(i,j).  Upper: the shared-row
      representative a = (p^j, p^i - p^j), b = (1, -1),
      S = {(0,0),(1,0),(0,1)} (masses p^i, 2).  Lower (hand proof):
      mass(b) >= |net([p^i])| + |net([p^j])| = 2, mass(a) >= p^max.
      Machine: explicit construction verified; bounded representative
      search finds nothing below 2 p^max.  Expected PASS.
  N5  MAX FACE LORENTZIAN (certified): Gram M[i,j] = log N(class_ij)
      = w*max(i,j)*log p + log2*[i != j], diag w*i*log p, i,j = 0..n.
      Certified signature via arb LDL pivots (every pivot sign must be
      ball-certified).  PRE-REGISTERED EXPECTATION: signature (1, n)
      for ALL p in {2,3,5,7,11}, w in {1,2,3}, n+1 in {3,5,8,13}.
      DISCLOSURE: (p <= 7, w = 1, n+1 <= 12) was explored before gate
      registration (W-doc protocol); p = 11, w in {2,3}, n+1 = 13 are
      unexplored predictions.  NOTE the contrast pre-registered: W's
      analytic error term log(1 - p^-w|i-j|) breaks Lorentz at
      (p,w) = (2,<=2), (3,1); the CC-norm error term +log2*(J - I) is
      predicted to keep (1, n) with NO low-weight anomaly.  Branch if
      FAIL: record the anomaly table against W's w_0 thresholds.
  N6  MIN FACE: v_p(e(class_ij)) = v_p(p^i - p^j) = min(i,j) exactly
      (integer check), and the matrix w*MIN (family i = 1..n) is PD
      (exact integer leading minors, det = a_1 prod(a_{k+1}-a_k));
      with i = 0 included it is PSD with one-dim kernel.  Expected PASS.
  N7  PRODUCT-FORMULA SPLIT (the layer-2 verdict): (a) on monoid
      classes, log N([A]) = Sum_p v_p(A) log p exactly (N([A]) = |A| =
      prod p^{v_p(A)}: exact integer factorization identity for
      2 <= A <= 20000) -- the CC-norm weight is the archimedean half of
      the product formula on the character lattice; (b) Gram-level: the
      two faces of the SAME classes recompose W's rank-2 split exactly:
      (normGram - log2*(J-I))/log p + MINGram/w = u 1^T + 1 u^T with
      u = (w i), the decomposition of the max-Gram lemma (integer
      identity max + min = i + j).  Expected PASS.
  N8  SUPPLY-LADDER CONTACT (doc 19): the norm weight of [p^i] equals
      the cumulative supply ladder: w_infty([p^i]) = i log p =
      Sum_{j=1..i} log|THH_{2j}(F_p)| with |THH_{2j}(F_p)| = p
      (Bokstedt, background).  Exact integer identity p^i = p*...*p.
      The VALUES carry zero choices; the index dictionary (tower step j
      <-> THH degree 2j) is observation-grade (V's missing grading).
  N9  CARRIER GUARD (Epstein): the archimedean face ALONE is
      carrier-blind: for the lattice Z^2 with Q(x,y) = x^2 + 5y^2 (not
      a norm form of an order with mult. closure used here; only the
      metric enters) and the degree-separated family v_i = (3^i, 1),
      the arch-norm Gram log(||v_i|| + ||v_j||) is ALSO Lorentzian
      (1, n) -- expected PASS, and its PASS is the guard's content:
      what dies for Epstein is the OTHER half (no mu => no monoid ring
      V.1(iii), no v_p => no MIN faces, no product formula; the cyclic
      bar faces consume mu at every level) -- textual audit in the doc.

Run:
    python3 -m scripts.numerics.witness.prime_cc_thh_norm_filtration
"""
import itertools
import math
import sys

import flint

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------- level-1 core
def mass(vec):
    return sum(abs(x) for x in vec)


def chi_col(k, l, a, b, S):
    """V.1 character: dict A -> net coefficient (zeros dropped)."""
    A = [0] * l
    for (i, j) in S:
        A[j] += a[i]
    out = {}
    for j in range(l):
        if A[j] != 0 and b[j] != 0:
            out[A[j]] = out.get(A[j], 0) + b[j]
    return {x: c for x, c in out.items() if c != 0}


def chi_row(k, l, a, b, S):
    return chi_col(l, k, b, a, frozenset((j, i) for (i, j) in S))


def arch_norm(ch):
    return sum(abs(c) * abs(A) for A, c in ch.items())


def total(k, l, a, b, S):
    return sum(a[i] * b[j] for (i, j) in S)


# ------------------------------------------------------------------- N1
print("N1: norm transport -- chi is a contraction (CC mass -> arch norm)")
E = (-2, -1, 0, 1, 2)
n1, bad1 = 0, None
for (k, l) in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)):
    cells = [(i, j) for i in range(k) for j in range(l)]
    Es = E if k * l <= 4 else (-1, 1, 2)
    for a in itertools.product(Es, repeat=k):
        for b in itertools.product(Es, repeat=l):
            lam, mu = mass(a), mass(b)
            for Sb in range(1 << len(cells)):
                S = frozenset(c for m, c in enumerate(cells) if Sb >> m & 1)
                cc, cr = chi_col(k, l, a, b, S), chi_row(k, l, a, b, S)
                t = total(k, l, a, b, S)
                if not (arch_norm(cc) <= lam * mu
                        and arch_norm(cr) <= lam * mu
                        and abs(t) <= arch_norm(cc)
                        and abs(t) <= arch_norm(cr)):
                    bad1 = (k, l, a, b, sorted(S))
                    break
                n1 += 1
            if bad1:
                break
        if bad1:
            break
check("||chi||_arch <= mass(a)*mass(b) and |e| <= ||chi||_arch",
      bad1 is None,
      f"{n1} representatives, 0 violations" if bad1 is None
      else f"VIOLATION at {bad1}")

# ------------------------------------------------------------------- N2
print("\nN2: the cyclic bar faces preserve the norm filtration EXACTLY")


def face(obj, i):
    """d_i on the cyclic bar (V's witness): multiply slots (i, i+1);
    d_q cyclic.  Merged slot = full outer product."""
    vecs, S = obj
    q = len(vecs) - 1
    if i < q:
        u, v = vecs[i], vecs[i + 1]
        merged = tuple(u[x] * v[y]
                       for x in range(len(u)) for y in range(len(v)))
        nv = vecs[:i] + (merged,) + vecs[i + 2:]
        nS = frozenset(c[:i] + (c[i] * len(v) + c[i + 1],) + c[i + 2:]
                       for c in S)
    else:
        u, v = vecs[q], vecs[0]
        merged = tuple(u[z] * v[x]
                       for z in range(len(u)) for x in range(len(v)))
        nv = (merged,) + vecs[1:q]
        nS = frozenset((c[q] * len(v) + c[0],) + c[1:q] for c in S)
    return (nv, nS)


def mass_product(obj):
    return math.prod(mass(v) for v in obj[0])


n2, bad2 = 0, None
EV = (-2, 1, 2)
for dims in itertools.product((1, 2), repeat=3):       # level 2: 3 slots
    vec_pools = [list(itertools.product(EV, repeat=d)) for d in dims]
    cell_pool = list(itertools.product(*[range(d) for d in dims]))
    for vecs in itertools.product(*vec_pools):
        for Sb in range(1, 1 << len(cell_pool)):
            S = frozenset(c for m, c in enumerate(cell_pool) if Sb >> m & 1)
            obj = (tuple(vecs), S)
            mp = mass_product(obj)
            for i in range(3):
                if mass_product(face(obj, i)) != mp:
                    bad2 = (dims, vecs, sorted(S), i)
                    break
            n2 += 3
            if bad2:
                break
        if bad2:
            break
    if bad2:
        break
# level 3 spot check (4 slots, dims = 1 or 2 on two slots)
if not bad2:
    for dims in ((1, 1, 1, 2), (2, 1, 2, 1), (1, 2, 2, 1)):
        vec_pools = [list(itertools.product((-1, 2), repeat=d)) for d in dims]
        cell_pool = list(itertools.product(*[range(d) for d in dims]))
        for vecs in itertools.product(*vec_pools):
            for Sb in (1, 3, 5, (1 << len(cell_pool)) - 1):
                S = frozenset(c for m, c in enumerate(cell_pool)
                              if Sb >> m & 1 and m < len(cell_pool))
                if not S:
                    continue
                obj = (tuple(vecs), S)
                mp = mass_product(obj)
                for i in range(4):
                    if mass_product(face(obj, i)) != mp:
                        bad2 = (dims, vecs, sorted(S), i)
                n2 += 4
check("mass-product(d_i x) = mass-product(x), all faces incl. cyclic",
      bad2 is None,
      f"{n2} face instances (levels 2-3), exact equality everywhere"
      if bad2 is None else f"VIOLATION at {bad2}")

# ------------------------------------------------------------------- N3
print("\nN3: monoid-class exactness N([A]) = |A|")


def min_mass_product_for_chi(target_cc, dims_list, entry_bound, cap):
    """Bounded search: minimal mass(a)*mass(b) over representatives with
    chi_col == target_cc, pruned at cap (we only care about reps < cap)."""
    best = None
    Es = tuple(range(-entry_bound, entry_bound + 1))
    for (k, l) in dims_list:
        cells = [(i, j) for i in range(k) for j in range(l)]
        for a in itertools.product(Es, repeat=k):
            ma = mass(a)
            if ma == 0 or ma * 1 >= cap:
                continue
            for b in itertools.product(Es, repeat=l):
                mb = mass(b)
                if mb == 0 or ma * mb >= cap:
                    continue
                for Sb in range(1, 1 << len(cells)):
                    S = frozenset(c for m, c in enumerate(cells)
                                  if Sb >> m & 1)
                    if chi_col(k, l, a, b, S) == target_cc:
                        v = ma * mb
                        if best is None or v < best:
                            best = v
    return best


ok3, msg3 = True, []
for A in (1, 2, 3, 4, 5, 6):
    # upper bound: single cell (a=(A), b=(1)) -> mass product |A|
    cc = chi_col(1, 1, (A,), (1,), frozenset({(0, 0)}))
    ok_up = (cc == {A: 1})
    # search for anything strictly below |A|
    found = min_mass_product_for_chi({A: 1}, [(1, 1), (1, 2), (2, 1), (2, 2)],
                                     max(2, A), cap=A)
    good = ok_up and found is None
    ok3 = ok3 and good
    msg3.append(f"A={A}:{'=' if good else 'BAD'}{A}")
check("N([A]) = |A| (upper attained, bounded search finds nothing below)",
      ok3, ", ".join(msg3))

# ------------------------------------------------------------------- N4
print("\nN4: difference classes N([p^i] - [p^j]) = 2 p^max")
ok4, msg4 = True, []
for (p, i, j) in ((2, 1, 0), (2, 2, 0), (2, 2, 1), (3, 1, 0), (3, 2, 1)):
    hi, lo = p ** i, p ** j
    # explicit shared-row construction
    a, b = (lo, hi - lo), (1, -1)
    S = frozenset({(0, 0), (1, 0), (0, 1)})
    cc = chi_col(2, 2, a, b, S)
    ok_con = (cc == {hi: 1, lo: -1} and mass(a) == hi and mass(b) == 2)
    # bounded search below 2*hi
    found = min_mass_product_for_chi({hi: 1, lo: -1},
                                     [(1, 2), (2, 1), (2, 2)],
                                     hi, cap=2 * hi)
    good = ok_con and found is None
    ok4 = ok4 and good
    msg4.append(f"p^{i}-p^{j}(p={p}):{'=' if good else 'BAD'}{2 * hi}")
check("construction attains 2 p^max; nothing below in bounded search",
      ok4, ", ".join(msg4))

# ------------------------------------------------------------------- N5
print("\nN5: MAX face certified Lorentzian (arb LDL pivot signs)")


def certified_signature(M_entries, prec=300):
    """Signature of a symmetric arb matrix via LDL pivots; None if any
    pivot sign is not ball-certified.  Symmetric Gaussian elimination.
    The index order is REVERSED first (signature is invariant under
    symmetric permutation): the families below have a 0 diagonal entry
    at index 0 (weight of [p^0] = [1] is log 1 = 0), which would
    otherwise give an exactly-zero leading pivot."""
    n = len(M_entries)
    A = [[flint.arb(0) + M_entries[n - 1 - r][n - 1 - c]
          for c in range(n)] for r in range(n)]
    pos = neg = 0
    for k in range(n):
        piv = A[k][k]
        if piv > 0:
            pos += 1
        elif piv < 0:
            neg += 1
        else:
            return None                       # pivot not certified
        for r in range(k + 1, n):
            f = A[r][k] / piv
            for c in range(k, n):
                A[r][c] = A[r][c] - f * A[k][c]
    return (pos, neg)


def log_arb(x):
    return flint.arb(x).log()


ok5, msg5 = True, []
for p in (2, 3, 5, 7, 11):
    lp, l2 = log_arb(p), log_arb(2)
    for w in (1, 2, 3):
        for npts in (3, 5, 8, 13):
            M = [[w * max(i, j) * lp + (l2 if i != j else flint.arb(0))
                  for j in range(npts)] for i in range(npts)]
            sig = certified_signature(M)
            good = (sig == (1, npts - 1))
            ok5 = ok5 and good
            if not good:
                msg5.append(f"(p={p},w={w},n+1={npts})->{sig}")
check("signature (1, n) certified for ALL p in {2,3,5,7,11}, w in "
      "{1,2,3}, n+1 in {3,5,8,13}", ok5,
      "60 instances, every pivot ball-certified, NO low-weight anomaly "
      "(contrast W's w_0(2)=3, w_0(3)=2)" if ok5
      else "anomalies: " + ", ".join(msg5))

# ------------------------------------------------------------------- N6
print("\nN6: MIN face -- v_p exact + PD minors")


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


ok6a = all(vp(p ** i - p ** j, p) == min(i, j)
           for p in (2, 3, 5, 7) for i in range(7) for j in range(7)
           if i != j)
ok6b = True
for w in (1, 2, 3):
    for n in (3, 5, 8, 13):
        a = [w * i for i in range(1, n + 1)]      # family i = 1..n: PD
        Mn = [[min(a[i], a[j]) for j in range(n)] for i in range(n)]
        # exact integer leading principal minors via fraction-free Bareiss
        import fractions
        B = [[fractions.Fraction(x) for x in row] for row in Mn]
        det_ok = True
        for k in range(n):
            sub = [row[:k + 1] for row in B[:k + 1]]
            # quick exact determinant (Gaussian, fractions)
            d = fractions.Fraction(1)
            Sm = [row[:] for row in sub]
            for c in range(k + 1):
                pivr = next((r for r in range(c, k + 1) if Sm[r][c] != 0),
                            None)
                if pivr is None:
                    d = fractions.Fraction(0)
                    break
                if pivr != c:
                    Sm[c], Sm[pivr] = Sm[pivr], Sm[c]
                    d = -d
                d *= Sm[c][c]
                for r in range(c + 1, k + 1):
                    f = Sm[r][c] / Sm[c][c]
                    for cc2 in range(c, k + 1):
                        Sm[r][cc2] -= f * Sm[c][cc2]
            expected = fractions.Fraction(
                a[0] * math.prod(a[m + 1] - a[m] for m in range(k)))
            if d <= 0 or d != expected:
                det_ok = False
        ok6b = ok6b and det_ok
check("v_p(p^i - p^j) = min(i,j) exact; w*MIN is PD "
      "(minors = a_1 prod diffs, exact)", ok6a and ok6b,
      f"v_p exact on p<=7, i,j<=6; minors exact for w in (1,2,3), "
      f"n in (3,5,8,13)")

# ------------------------------------------------------------------- N7
print("\nN7: product-formula split on the character lattice")


def factorize(n):
    out, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


ok7a = all(math.prod(q ** e for q, e in factorize(A).items()) == A
           for A in range(2, 20001))
# Gram-level recomposition: max(i,j) + min(i,j) = i + j (exact), i.e.
# (normGram - log2(J-I))/(w log p) + MIN/w = u 1^T + 1 u^T, u = (i).
ok7b = all(max(i, j) + min(i, j) == i + j
           for i in range(14) for j in range(14))
check("log N([A]) = Sum_p v_p(A) log p (exact, A <= 20000); "
      "MAX + MIN = u1^T + 1u^T (W's rank-2 split)", ok7a and ok7b,
      "the CC-norm weight is the archimedean half; the v_p of the same "
      "classes are the MIN half; they recompose the product formula")

# ------------------------------------------------------------------- N8
print("\nN8: supply-ladder contact (doc 19)")
ok8 = all(p ** i == math.prod(p for _ in range(1, i + 1))
          for p in (2, 3, 5, 7, 11, 13) for i in range(1, 8))
check("w_infty([p^i]) = i log p = cumulative Lambda ladder "
      "(|THH_{2j}(F_p)| = p, background)", ok8,
      "values exact, zero choices; the index dictionary (step j <-> "
      "degree 2j) is OBSERVATION-grade -- the grading is still missing (V)")

# ------------------------------------------------------------------- N9
print("\nN9: carrier guard -- the archimedean face alone is carrier-blind")


def qnorm(v):
    return flint.arb(v[0] * v[0] + 5 * v[1] * v[1]).sqrt()


ok9, msg9 = True, []
for npts in (3, 5, 8, 13):
    vs = [(3 ** i, 1) for i in range(npts)]
    M = [[(qnorm(vs[i]) + qnorm(vs[j])).log() if i != j
          else qnorm(vs[i]).log() for j in range(npts)]
         for i in range(npts)]
    sig = certified_signature(M)
    good = (sig == (1, npts - 1))
    ok9 = ok9 and good
    if not good:
        msg9.append(f"n+1={npts}->{sig}")
check("Epstein-style lattice (x^2+5y^2) arch-norm Gram IS Lorentzian "
      "(1, n)", ok9,
      "carrier-blind PASS = the guard's content: Epstein keeps the MAX "
      "face; it has NO mu (no monoid ring, V.1(iii)), NO v_p (no MIN "
      "faces), NO product formula, NO cyclic bar faces -- the gluing has "
      "one side only" if ok9 else "anomalies: " + ", ".join(msg9))

print("""
VERDICT (pre-registered): N1-N9 PASS => the pre-registered reading is
CONFIRMED at the strict layer: the CC norm, transported along V's
character chi (Theorem V.1), is EXACTLY the archimedean filtration of
the monoid ring Z[Z\\0] (exact on monoid classes, N([A]) = |A|; the bar
faces preserve it exactly), and on the geometric family {[p^i]} the
norm-Gram is the MAX face (certified Lorentzian (1, n), no low-weight
anomaly) while the p-adic valuations of the SAME classes are the MIN
face (PD): the two faces recompose W's rank-2 product-formula split on
one CC-internal object.  The CC norm is the archimedean half of the
product formula at the strict THH layer.  What is still missing is the
DEGREE (V's verdict stands): the filtration supplies weights, not
degrees; the derived version is posed in the doc.
""")

print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
