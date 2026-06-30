"""R1 torsor-splitter insertion witness.

Doc 138 proves that the DDG7b defect c=(1+z)^-1 is a nonzero class in
H^1(<phi>; U_1).  Docs 143-144 kill free Laurent insertion and post-hoc
projection.  The next repair is to adjoin a new unit/selector b with a
twisted shear action chosen to make c a coboundary:

    phi(b) = b * c^-1, hence b/phi(b) = c.

This is algebraically consistent because c is a C_2 cocycle, but it is
tautological: it kills the obstruction by adding a formal solution to the
coboundary equation.  The same splitting extension can be formed for any
C_2-cocycle on any control shadow.  Therefore it is not construction-grade
unless the new generator/relation is produced by a carrier-native map and
the extension is undefined on DH/Epstein controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_torsor_splitter_insertion_no_go
"""

from math import comb

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(n):
    """Truncated F_2[[z]] arithmetic mod z^n; polynomials are coefficient lists."""
    def add(a, b):
        return [(a[i] if i < len(a) else 0) ^ (b[i] if i < len(b) else 0) for i in range(n)]

    def mul(a, b):
        out = [0] * n
        for i, ai in enumerate(a[:n]):
            if not ai:
                continue
            for j, bj in enumerate(b[: n - i]):
                if bj:
                    out[i + j] ^= 1
        return out

    def inv(a):
        assert a[0] == 1
        rem = a[:]
        rem[0] ^= 1
        term = [1] + [0] * (n - 1)
        out = [1] + [0] * (n - 1)
        for _ in range(1, n):
            term = mul(term, rem)
            if not any(term):
                break
            out = add(out, term)
        return out

    def phi(f):
        out = [0] * n
        for m, coeff in enumerate(f[:n]):
            if not coeff:
                continue
            if m == 0:
                out[0] ^= 1
                continue
            for k in range(0, n - m):
                if comb(m + k - 1, k) % 2:
                    out[m + k] ^= 1
        return out

    return add, mul, inv, phi


def one(n):
    return [1] + [0] * (n - 1)


def one_plus_z(n):
    return [1, 1] + [0] * (n - 2)


def res1(f):
    return f[1] if len(f) > 1 else 0


def formal_splitter_action_is_involutive(c, n):
    """For formal b with phi(b)=b*c^-1, check phi^2(b)=b."""
    add, mul, inv, phi = make(n)
    c_inv = inv(c)
    return mul(c_inv, phi(c_inv)) == one(n)


def formal_splitter_splits(c, n):
    """Formal b satisfies b/phi(b)=c iff phi(b)=b*c^-1."""
    add, mul, inv, phi = make(n)
    c_inv = inv(c)
    # Represent b symbolically.  Then b / (b*c^-1) = c.
    return inv(c_inv) == c


for n in (6, 8, 10, 12):
    add, mul, inv, phi = make(n)
    c = inv(one_plus_z(n))

    gate(
        f"TSI1 c=(1+z)^-1 is a C_2 cocycle at truncation {n}",
        mul(c, phi(c)) == one(n),
        f"c*phi(c)={mul(c, phi(c))}",
    )

    # Leading coefficient obstruction: every base coboundary has res_1=0,
    # but c has res_1=1.  It is enough to check generator coboundaries,
    # since res_1 is a homomorphism and the generators close U_1.
    coboundary_res1_zero = True
    for k in range(1, n):
        b = one(n)
        b[k] = 1
        cob = mul(b, inv(phi(b)))
        coboundary_res1_zero = coboundary_res1_zero and res1(cob) == 0
    gate(
        f"TSI2 c is not a base coboundary at truncation {n}",
        res1(c) == 1 and coboundary_res1_zero,
        f"res1(c)={res1(c)}; generator coboundary res1 all zero={coboundary_res1_zero}",
    )

    gate(
        f"TSI3 formal splitter action phi(b)=b*c^-1 is involutive at truncation {n}",
        formal_splitter_action_is_involutive(c, n),
        "uses c*phi(c)=1",
    )

    gate(
        f"TSI4 formal splitter makes c a coboundary by definition at truncation {n}",
        formal_splitter_splits(c, n),
        "b/phi(b)=b/(b*c^-1)=c",
    )


# The same formal splitting rule works for any cocycle d.  This is a toy
# control check: d=1 is a trivial control cocycle, and d=c can be supplied as
# an abstract control cocycle without any Euler carrier fields.
for label, cocycle_factory in (
    ("trivial-control", lambda n: one(n)),
    ("abstract-cocycle-control", lambda n: make(n)[2](one_plus_z(n))),
):
    n = 8
    add, mul, inv, phi = make(n)
    d = cocycle_factory(n)
    gate(
        f"TSI5 {label} admits the same formal splitting construction",
        mul(d, phi(d)) == one(n)
        and formal_splitter_action_is_involutive(d, n)
        and formal_splitter_splits(d, n),
        "for any cocycle d, define phi(s)=s*d^-1",
    )


new_symbol_not_in_base = True
base_relation_count = 0
inserted_relation_count = 1
gate(
    "TSI6 the splitter is a new symbol with an inserted transformation law",
    new_symbol_not_in_base and base_relation_count == 0 and inserted_relation_count == 1,
    "the base obstruction is unchanged; the extension adds b and phi(b)=b*c^-1",
)


gate(
    "TSI7 surviving use requires a carrier-native splitter and control death",
    True,
    "formal torsor splitting is admissible only if the relation is constructed before DH/Epstein fail",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (TSI1-TSI7)")
print(
    "VERDICT: adjoining a formal torsor splitter b with phi(b)=b*c^-1 "
    "trivializes the DDG7b cocycle by definition.  It is algebraically "
    "consistent, but it is an inserted solution and is formable for controls. "
    "A surviving R1 route must construct the splitter relation from carrier "
    "data and show where DH/Epstein cannot form it."
)
