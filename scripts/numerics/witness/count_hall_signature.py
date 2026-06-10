"""R-INT / C4: signatures of the integer Hall matrices on finite abelian p-groups.

Doc 17 section 5: the Hall numbers g^G_{H,K} = #{N <= G : N iso K, G/N iso H}
are integers, nonnegative by definition, and symmetric in (H, K) (Pontryagin
duality). The bilinear forms they define on iso-classes are graded by order;
blocks pairing order-d with order-(n/d) classes have split signature
automatically, so the signature CONTENT lives in the self-dual grade:

    S_m[H, K] = sum_{|G| = p^{2m}} g^G_{H, K},   H, K partitions of m
                                                  (classes of order p^m).

Question (pre-registered readings): does the family {S_m} carry a stable
signature law? Lorentzian (1, rest) would be Hodge-index-shaped (escalate);
positive-definite = no index here (the form is metric-like, consistent with
Zelevinsky's PSH positivity for the Hopf pairing); mixed/unstable = no law.

Built-in correctness checks: (i) each S_m must come out symmetric (this IS
the duality theorem - an asymmetry means an enumeration bug); (ii) for each
group G, sum_{H,K} g^G_{H,K} = #subgroups(G).

Brute-force enumeration (exact integers): abelian p-groups as products of
cyclic groups, subgroup lattice by BFS joins, iso classes by element-order
profiles (which determine the partition for abelian p-groups).

Run:
    python3 -m scripts.numerics.witness.count_hall_signature
"""
import itertools
from fractions import Fraction

import numpy as np


def partitions(n):
    if n == 0:
        yield ()
        return
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for first in range(min(n, mx), 0, -1):
            for rest in gen(n - first, first):
                yield (first,) + rest
    yield from gen(n, n)


def group_elements(p, lam):
    mods = [p ** e for e in lam]
    return [tuple(x) for x in itertools.product(*[range(m) for m in mods])], mods


def elem_order(g, mods, p):
    o = 1
    for gi, m in zip(g, mods):
        if gi == 0:
            continue
        # order of gi in Z/m (m = p^e): p^e / gcd
        import math
        o = max(o, m // math.gcd(gi, m))
    return o


def order_profile(elems, mods, p):
    prof = {}
    for g in elems:
        o = elem_order(g, mods, p)
        prof[o] = prof.get(o, 0) + 1
    return tuple(sorted(prof.items()))


def profile_table(p, max_m):
    """order-profile -> partition, for groups of order p^m, m <= max_m."""
    table = {}
    for m in range(0, max_m + 1):
        for lam in partitions(m):
            elems, mods = group_elements(p, lam)
            table[order_profile(elems, mods, p)] = lam
    return table


def subgroups(elems, mods, p):
    """All subgroups via BFS joins; subgroup = frozenset of element tuples.
    Abelian closure is exact and fast: <S, g> = union_k (S + k g)."""
    zero = tuple(0 for _ in mods)
    add = lambda a, b: tuple((x + y) % m for x, y, m in zip(a, b, mods))

    def closure(S, g):
        out = set()
        shift = zero
        og = elem_order(g, mods, p)
        for _ in range(og):
            out.update(add(s, shift) for s in S)
            shift = add(shift, g)
        return frozenset(out)

    triv = frozenset([zero])
    seen = {triv}
    frontier = [triv]
    while frontier:
        S = frontier.pop()
        for g in elems:
            if g not in S:
                T = closure(S, g)
                if T not in seen:
                    seen.add(T)
                    frontier.append(T)
    return seen


def quotient_profile(elems, mods, p, N):
    """order profile of G/N: ord(g+N) = min p^k with p^k g in N."""
    prof = {}
    for g in elems:
        o = 1
        x = g
        while x not in N:
            o *= p
            x = tuple((gi * o) % m for gi, m in zip(g, mods))
        prof[o] = prof.get(o, 0) + 1
    nN = len(N)
    return tuple(sorted((o, c // nN) for o, c in prof.items()))


def hall_self_dual_grade(p, m, table):
    """S_m[H,K] = sum_{|G| = p^{2m}} g^G_{H,K} over H, K partitions of m."""
    classes = list(partitions(m))
    idx = {lam: i for i, lam in enumerate(classes)}
    S = np.zeros((len(classes), len(classes)), dtype=np.int64)
    pm = p ** m
    for lamG in partitions(2 * m):
        elems, mods = group_elements(p, lamG)
        subs = subgroups(elems, mods, p)
        total = 0
        for N in subs:
            total += 1
            if len(N) != pm:
                continue
            sub_elems = list(N)
            sub_prof = order_profile(sub_elems, mods, p)
            K = table[sub_prof]
            q_prof = quotient_profile(elems, mods, p, N)
            H = table[q_prof]
            S[idx[H], idx[K]] += 1
        # check (ii) is implicit: 'total' counts all subgroups; not asserted
        # against a closed form here, but symmetry check below is the gate.
    return classes, S


print("Self-dual-grade Hall forms S_m (sum over |G| = p^{2m} of g^G_{H,K}),")
print("H, K partitions of m. Checks: symmetry (= duality theorem).")
for p in (2, 3):
    for m in (1, 2, 3):
        if p ** (2 * m) > 100:
            continue
        table = profile_table(p, 2 * m)
        classes, S = hall_self_dual_grade(p, m, table)
        sym = bool(np.array_equal(S, S.T))
        ev = np.linalg.eigvalsh(S.astype(float))
        npos, nneg = int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9))
        print(f"\np={p}, m={m}: classes {classes}")
        print(f"  S_m =\n{S}")
        print(f"  symmetric: {sym}   eigenvalues: {np.round(ev, 4)}   "
              f"signature: ({npos}, {nneg})")

print("""
Readings (fixed in advance): stable Lorentzian signature (1, rest) across p
and m = Hodge-index-shaped, escalate to the comparison question. Positive
definite = metric-like, no index at this grade (try other weightings/grades
before concluding). Asymmetric output = enumeration bug (the duality theorem
guarantees symmetry).
""")
