"""V (grading bridge), candidate 2: the FULL invariant algebra of the
strict square HZ ^ HZ in GammaSets_*, column-functional shape -- computed.

Setting as in prime_cc_strict_smash_q1.py (CC's category; elements of
(HZ ^ HZ)(1_+) = triples (a, b, S) modulo coend A/B-moves + basepoint).
Q-doc sec 2 exhibited the divided-power invariants Phi_p, Phi'_p (one
Z/p per prime per side). THIS witness computes the full space of
invariants of the COLUMN-FUNCTIONAL shape

    F_h(a, b, S) = Sum_j h(b_j, A_j)  mod m,   A_j = column sums,

h an arbitrary function on a bounded window (and symmetrically rows).

PRE-REGISTERED EXPECTATION (V-doc sec 0, derived by hand BEFORE running):
A-moves preserve the multiset {(b_j, A_j)} exactly; B-moves force
exactly additivity of h in b (columns merge only with equal patterns);
basepoint forms force h(b, 0) = 0 = h(0, A). Hence the expected answer:

    invariants = { h(b, A) = b * g(A) : g : Z minus 0 -> Z/m arbitrary },

i.e. the universal column invariant is the CHARACTER
chi_col(a,b,S) = Sum_j b_j [A_j] in the free abelian group Z[Z \ 0],
and it is multiplicative for the smash-square product (monoid ring of
the multiplicative monoid of nonzero integers). Q's Phi_p = chi_col
post-composed with [A] |-> C(A,p) mod p; e = total = [A] |-> A.

PRE-REGISTERED READINGS (fail-closed):
  V-B1  chi_col (with the A = 0 bucket dropped) is EXACTLY invariant on
        every enumerated coend-move instance (the q1 move plans), and
        chi_row symmetrically.  Expected PASS.  [This alone proves
        b*g(A) is invariant for EVERY g and EVERY modulus m.]
  V-B2  Window kernel: over F_2 and F_3, the kernel of the harvested
        linear constraint system on h equals span{ b * 1_{A=A0} } on
        the INTERIOR of the window (boundary artifacts allowed outside,
        untouched coordinates excluded).  Expected PASS = the
        column-functional invariant algebra is EXACTLY the character
        functionals, no further exotic invariants in this shape.
  V-B3  ORDER 4 EXISTS: h(b, A) = b * 1_{A=1} satisfies every harvested
        integer constraint exactly (hence invariant mod 4), and takes
        the values 1, 2, 3 on explicit classes: a genuine Z/4-valued
        invariant.  Expected PASS.  CONSEQUENCE (doc sec 2): the
        exponent-p picture of the invariant algebra is corrected --
        the algebra carries Z/m data for every m; the cheap "no Z/4
        anywhere so Bokstedt's pi_7 = Z/4 is unreachable" obstruction
        VANISHES.
  V-B4  MONOID RING: chi_col(x * y) = chi_col(x) *_conv chi_col(y)
        (multiplicative convolution [A][A'] = [A A']) on enumerated
        pairs, where x * y is the smash-square product
        (a (x) a', b (x) b', S x S').  Expected PASS.  CONSEQUENCE:
        the strict-square invariant algebra is the MONOID RING
        Z[(Z \ 0, x)] -- the multiplicative monoid of nonzero integers,
        doc 26 sec 2's "THE MONOID", appearing as the universal strict
        invariant.  Separations: chi(L) = [1]+[2] != [3] = chi(C3);
        chi(2x2) = 2[2] != [4] = chi(4x1).

Bulk enumeration counts go to /tmp/v_grading_kernel.log.

Run:
    python3 -m scripts.numerics.witness.prime_cc_grading_invariant_kernel
"""
import itertools
import sys

FAIL = []
LOG = open("/tmp/v_grading_kernel.log", "w")


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


# ------------------------------------------------- core (as in q1 witness)
def push(vec, phi, n_target):
    out = [0] * n_target
    for i, t in enumerate(phi):
        if t != 0:
            out[t - 1] += vec[i]
    return tuple(out)


def pull_S_a(Sp, phi, k, l):
    return frozenset((i, j) for i in range(k) for j in range(l)
                     if phi[i] != 0 and (phi[i] - 1, j) in Sp)


def pull_S_b(Sp, psi, k, l):
    return frozenset((i, j) for i in range(k) for j in range(l)
                     if psi[j] != 0 and (i, psi[j] - 1) in Sp)


def cols(k, l, a, b, S):
    """List of (b_j, A_j) per column."""
    A = [0] * l
    for (i, j) in S:
        A[j] += a[i]
    return [(b[j], A[j]) for j in range(l)]


def rows(k, l, a, b, S):
    B = [0] * k
    for (i, j) in S:
        B[i] += b[j]
    return [(a[i], B[i]) for i in range(k)]


def chi(entries):
    """Character: Sum b [A], A = 0 bucket dropped, zero coeffs dropped."""
    d = {}
    for (v, A) in entries:
        if A != 0 and v != 0:
            d[A] = d.get(A, 0) + v
    return {A: c for A, c in d.items() if c != 0}


def is_basepoint(k, l, a, b, S):
    return all(x == 0 for x in a) or all(x == 0 for x in b) or not S


# ----------------------------------------------------- move enumeration
E2 = (-2, -1, 0, 1, 2)
E3 = (-1, 1, 2)

n_inst = 0
chi_viol = []          # V-B1
constraints = set()    # V-B2: harvested rows on h(b, A), b != 0, A != 0
BWIN, AWIN = 6, 8      # |b| <= BWIN, |A| <= AWIN
n_skipped = 0


def col_row_vec(obj):
    """Constraint contribution: dict (b,A) -> count, b,A != 0; None if
    out of window."""
    k, l, a, b, S = obj
    d = {}
    for (v, A) in cols(k, l, a, b, S):
        if v == 0 or A == 0:
            continue
        if abs(v) > BWIN or abs(A) > AWIN:
            return None
        d[(v, A)] = d.get((v, A), 0) + 1
    return d


def harvest(left, right):
    """Record chi check + h-constraint from one move instance."""
    global n_inst, n_skipped
    n_inst += 1
    cl = chi(cols(*left)) if not is_basepoint(*left) else {}
    cr = chi(cols(*right)) if not is_basepoint(*right) else {}
    rl = chi(rows(*left)) if not is_basepoint(*left) else {}
    rr = chi(rows(*right)) if not is_basepoint(*right) else {}
    if cl != cr or rl != rr:
        if len(chi_viol) < 5:
            chi_viol.append((left, right, cl, cr, rl, rr))
        else:
            chi_viol.append(None)
    dl = col_row_vec(left) if not is_basepoint(*left) else {}
    dr = col_row_vec(right) if not is_basepoint(*right) else {}
    if dl is None or dr is None:
        n_skipped += 1
        return
    diff = dict(dl)
    for key, c in dr.items():
        diff[key] = diff.get(key, 0) - c
    diff = {key: c for key, c in diff.items() if c != 0}
    if diff:
        constraints.add(tuple(sorted(diff.items())))


def run_a_moves(k, kp, l, Ea, Eb):
    cells_p = [(i, j) for i in range(kp) for j in range(l)]
    for phi in itertools.product(range(kp + 1), repeat=k):
        for Sp_bits in range(1 << len(cells_p)):
            Sp = frozenset(c for m, c in enumerate(cells_p)
                           if Sp_bits >> m & 1)
            for a in itertools.product(Ea, repeat=k):
                for b in itertools.product(Eb, repeat=l):
                    left = (kp, l, push(a, phi, kp), b, Sp)
                    right = (k, l, a, b, pull_S_a(Sp, phi, k, l))
                    harvest(left, right)


def run_b_moves(l, lp, k, Ea, Eb):
    cells_p = [(i, j) for i in range(k) for j in range(lp)]
    for psi in itertools.product(range(lp + 1), repeat=l):
        for Sp_bits in range(1 << len(cells_p)):
            Sp = frozenset(c for m, c in enumerate(cells_p)
                           if Sp_bits >> m & 1)
            for a in itertools.product(Ea, repeat=k):
                for b in itertools.product(Eb, repeat=l):
                    left = (k, lp, a, push(b, psi, lp), Sp)
                    right = (k, l, a, b, pull_S_b(Sp, psi, k, l))
                    harvest(left, right)


print("V-B1: exact chi_col / chi_row invariance + constraint harvest")
plans = [
    ("a 2->1 l2", run_a_moves, (2, 1, 2, E2, E2)),
    ("a 1->2 l2", run_a_moves, (1, 2, 2, E2, E2)),
    ("a 2->2 l2", run_a_moves, (2, 2, 2, E2, E2)),
    ("a 3->2 l2", run_a_moves, (3, 2, 2, E3, E3)),
    ("a 2->3 l2", run_a_moves, (2, 3, 2, E3, E3)),
    ("b 2->1 k2", run_b_moves, (2, 1, 2, E2, E2)),
    ("b 1->2 k2", run_b_moves, (1, 2, 2, E2, E2)),
    ("b 2->2 k2", run_b_moves, (2, 2, 2, E2, E2)),
    ("b 3->2 k2", run_b_moves, (3, 2, 2, E3, E3)),
]
for name, fn, args in plans:
    n0 = n_inst
    fn(*args)
    LOG.write(f"{name}: {n_inst - n0} instances\n")
check("chi exactly invariant on all enumerated moves", not chi_viol,
      f"{n_inst} move instances, {len(chi_viol)} violations "
      f"({n_skipped} skipped out-of-window for harvest only); "
      f"{len(constraints)} distinct constraint rows harvested")
LOG.write(f"total {n_inst} instances, {len(constraints)} distinct rows, "
          f"{n_skipped} skipped\n")

# ----------------------------------------------------- V-B2: window kernel
print("\nV-B2: kernel of the constraint system over F_2, F_3 vs b*g(A)")
touched = sorted({key for row in constraints for key, _ in row})
idx = {key: i for i, key in enumerate(touched)}
N = len(touched)
rows_int = []
for row in constraints:
    v = [0] * N
    for key, c in row:
        v[idx[key]] = c
    rows_int.append(v)
LOG.write(f"{N} touched coordinates\n")


def kernel_mod_p(rws, n, p):
    """Gaussian elimination; returns basis of kernel as list of vectors."""
    mat = [[x % p for x in r] for r in rws]
    piv_col, r = [], 0
    for c in range(n):
        piv = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = pow(mat[r][c], p - 2, p) if p > 2 else 1
        mat[r] = [(x * inv) % p for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % p:
                f = mat[i][c]
                mat[i] = [(x - f * y) % p for x, y in zip(mat[i], mat[r])]
        piv_col.append(c)
        r += 1
        if r == len(mat):
            break
    free = [c for c in range(n) if c not in piv_col]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for ri, pc in enumerate(piv_col):
            v[pc] = (-mat[ri][fc]) % p
        basis.append(v)
    return basis


def rank_mod_p(vecs, p):
    mat = [list(v) for v in vecs]
    n = len(mat[0]) if mat else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = pow(mat[r][c], p - 2, p) if p > 2 else 1
        mat[r] = [(x * inv) % p for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % p:
                f = mat[i][c]
                mat[i] = [(x - f * y) % p for x, y in zip(mat[i], mat[r])]
        r += 1
        if r == len(mat):
            break
    return r


# the predicted span: v_{A0}(b, A) = b * 1_{A = A0}, on touched coords
avals = sorted({A for (b, A) in touched})
span = []
for A0 in avals:
    v = [0] * N
    for key, i in idx.items():
        if key[1] == A0:
            v[i] = key[0]
    span.append(v)
# integer check: every span vector annihilates every constraint row exactly
ok_span = all(sum(x * y for x, y in zip(rv, sv)) == 0
              for rv in rows_int for sv in span)
check("b*g(A) annihilates ALL rows over Z (every modulus)", ok_span,
      f"{len(span)} generators x {len(rows_int)} rows, exact integer dot")

interior = [i for i, (b, A) in enumerate(touched)
            if abs(b) <= 2 and abs(A) <= 4]
ok2 = True
detail2 = []
for p in (2, 3):
    ker = kernel_mod_p(rows_int, N, p)
    rs = rank_mod_p(span, p) if span else 0
    proj_ker = [[v[i] for i in interior] for v in ker]
    proj_span = [[v[i] for i in interior] for v in span]
    r_span = rank_mod_p(proj_span, p) if proj_span else 0
    r_both = rank_mod_p(proj_span + proj_ker, p) if proj_ker else r_span
    excess = r_both - r_span
    detail2.append(f"p={p}: dim ker={len(ker)}, span rank={rs}, "
                   f"interior excess={excess}")
    if excess != 0:
        ok2 = False
check("kernel = b*g(A) on interior (F_2 and F_3)", ok2, "; ".join(detail2))

# ----------------------------------------------------- V-B3: order 4
print("\nV-B3: a genuine Z/4-valued invariant (order 4)")
h41 = [0] * N
for key, i in idx.items():
    if key[1] == 1:
        h41[i] = key[0]
ok_inv4 = all(sum(x * y for x, y in zip(rv, h41)) == 0 for rv in rows_int)


def F_h(obj):
    return sum(v for (v, A) in cols(*obj) if A == 1) % 4


vals = [F_h((1, 1, (1,), (w,), frozenset({(0, 0)}))) for w in (1, 2, 3)]
check("h = b*1_{A=1} invariant (Z-exact) and onto Z/4",
      ok_inv4 and vals == [1, 2, 3],
      f"annihilates all rows; values on (1)x(w) single cells: {vals} "
      "=> order-4 invariant exists; exponent-p picture corrected")

# ----------------------------------------------------- V-B4: monoid ring
print("\nV-B4: chi_col is multiplicative for the square product")


def product(x, y):
    k, l, a, b, S = x
    kp, lp, ap, bp, Sp = y
    a2 = tuple(a[i] * ap[ip] for i in range(k) for ip in range(kp))
    b2 = tuple(b[j] * bp[jp] for j in range(l) for jp in range(lp))
    S2 = frozenset((i * kp + ip, j * lp + jp)
                   for (i, j) in S for (ip, jp) in Sp)
    return (k * kp, l * lp, a2, b2, S2)


def conv(c1, c2):
    out = {}
    for A, u in c1.items():
        for Ap, v in c2.items():
            if A * Ap != 0:
                out[A * Ap] = out.get(A * Ap, 0) + u * v
    return {A: c for A, c in out.items() if c != 0}


small = []
for k, l in ((1, 1), (2, 1), (1, 2), (2, 2)):
    cells = [(i, j) for i in range(k) for j in range(l)]
    for Sb in range(1, 1 << len(cells)):
        S = frozenset(c for m, c in enumerate(cells) if Sb >> m & 1)
        for a in itertools.product((-1, 1, 2), repeat=k):
            for b in itertools.product((-1, 1, 2), repeat=l):
                small.append((k, l, a, b, S))
import random
random.seed(0)
pairs = [(random.choice(small), random.choice(small)) for _ in range(4000)]
ok4 = all(chi(cols(*product(x, y)))
          == conv(chi(cols(*x)), chi(cols(*y))) for x, y in pairs)
L = (2, 2, (1, 1), (1, 1), frozenset({(0, 0), (0, 1), (1, 0)}))
C3 = (1, 1, (3,), (1,), frozenset({(0, 0)}))
f22 = (1, 1, (2,), (2,), frozenset({(0, 0)}))
f41 = (1, 1, (4,), (1,), frozenset({(0, 0)}))
sep = (chi(cols(*L)) == {2: 1, 1: 1} and chi(cols(*C3)) == {3: 1}
       and chi(cols(*f22)) == {2: 2} and chi(cols(*f41)) == {4: 1})
check("multiplicativity on 4000 random pairs + separations", ok4 and sep,
      f"chi(xy) = chi(x) *_conv chi(y); chi(L) = [1]+[2], chi(C3) = [3], "
      f"chi(2x2) = 2[2], chi(4x1) = [4]: the monoid ring Z[(Z\\0, x)]")

LOG.close()
print("""
VERDICT (pre-registered): V-B1..V-B4 PASS => the column-functional
invariant algebra of the strict square is EXACTLY the character
chi_col : (HZ ^ HZ)(1_+) -> Z[Z \\ 0] (and chi_row symmetrically):
a FREE abelian group, multiplicative for the square product -- the
monoid ring of the multiplicative monoid of nonzero integers.  Q's
Phi_p = chi composed with the divided power C(., p) mod p; e = total =
chi composed with [A] |-> A.  Corrections to the standing picture:
(1) the algebra carries Z/m data for EVERY m (order 4 exhibited), not
one Z/p per prime -- the cheap exponent obstruction to Bokstedt's
Z/4 at degree 7 vanishes; (2) the algebra is FREE, so NO grading on it
alone can present a torsion tower: any bridge needs grading + a
DIFFERENTIAL (the bar direction, witness prime_cc_grading_bar_degree).
""")
print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
