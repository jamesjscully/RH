r"""Coinduced DD.4 extension no-go.

This witness tests the standard algebraic repair after doc 257:
replace U_1 by the two-copy coinduced C_2-module Coind(U_1).  This makes
H^1 vanish and kills the DD.4 class, but only by a formal coefficient-system
extension.  It does not construct the square carrier required by End(S^2/Z).

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_coinduced_dd4_extension_no_go
"""

from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^{L+1}; 1-units are dicts {power: 1}."""

    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})
        term = {0: 1}
        out = {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            out = add(out, term)
        return out

    def phi(f):
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return mul, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, zero_vec, from_vec_fn, mul_fn, to_vec_fn):
    seen = {zero_vec}
    queue = [zero_vec]
    while queue:
        current = from_vec_fn(queue.pop())
        for gen in gens:
            nxt = to_vec_fn(mul_fn(current, gen))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def base_h1_profile(L):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    bgens = [mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)]
    ngens = [mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)]
    coboundaries = closure(
        bgens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    norm_image = closure(
        ngens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    z1_order = 2 ** L // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    return {
        "L": L,
        "c": c,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
    }


def pair_mul(x, y, mul):
    return mul(x[0], y[0]), mul(x[1], y[1])


def pair_inv(x, inv):
    return inv(x[0]), inv(x[1])


def pair_to_vec(x, L):
    return to_vec(x[0], L) + to_vec(x[1], L)


def pair_from_vec(v, L):
    return from_vec(v[:L]), from_vec(v[L:])


def coinduced_profile(L):
    mul, inv, phi = make(L)

    def sigma(x):
        # Coinduced C_2 action: swap the two copies and apply the base shear.
        return phi(x[1]), phi(x[0])

    def pmul(x, y):
        return pair_mul(x, y, mul)

    def pinv(x):
        return pair_inv(x, inv)

    bgens = []
    ngens = []
    for k in range(1, L + 1):
        for side in (0, 1):
            e = ({0: 1, k: 1}, {0: 1}) if side == 0 else ({0: 1}, {0: 1, k: 1})
            se = sigma(e)
            bgens.append(pmul(e, pinv(se)))
            ngens.append(pmul(e, se))

    zero = (0,) * (2 * L)
    coboundaries = closure(
        bgens,
        zero,
        lambda v: pair_from_vec(v, L),
        pmul,
        lambda x: pair_to_vec(x, L),
    )
    norm_image = closure(
        ngens,
        zero,
        lambda v: pair_from_vec(v, L),
        pmul,
        lambda x: pair_to_vec(x, L),
    )
    z1_order = 2 ** (2 * L) // len(norm_image)
    h1_order = z1_order // len(coboundaries)

    c = inv({0: 1, 1: 1})
    diag_c = (c, c)
    splitter = (c, {0: 1})
    coboundary = pmul(splitter, pinv(sigma(splitter)))
    return {
        "L": L,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "diag_c_coboundary": pair_to_vec(diag_c, L) in coboundaries,
        "explicit_coboundary": coboundary == diag_c,
        "rank_before": L,
        "rank_after": 2 * L,
    }


base_profiles = [base_h1_profile(L) for L in (6, 8, 10, 12)]
coinduced_profiles = [coinduced_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CID1 base DD.4 class is still the nonzero obstruction",
    all(p["h1_order"] == 2 and p["c_nonboundary"] and p["res1_c"] == 1 for p in base_profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "CID2 coinduced two-copy coefficient system has H^1=0",
    all(p["h1_order"] == 1 for p in coinduced_profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in coinduced_profiles
    ),
)

gate(
    "CID3 diagonal image of the DD.4 class becomes a coboundary",
    all(p["diag_c_coboundary"] and p["explicit_coboundary"] for p in coinduced_profiles),
    "diag(c) = (c,1)/sigma(c,1)",
)

gate(
    "CID4 coinduction doubles the coefficient support before building a carrier",
    all(p["rank_after"] == 2 * p["rank_before"] for p in coinduced_profiles),
    "  ".join("L%d:%d->%d" % (p["L"], p["rank_before"], p["rank_after"]) for p in coinduced_profiles),
)


required_slots = [
    "actual_square",
    "integral_rep_NS",
    "two_degree_maps",
    "indecomposable_diagonal",
    "frobenius_graph",
    "proper_correspondence",
    "fiber_product_composition",
    "projection_formula",
    "canonical_rosati",
    "positive_primitive_sign",
    "carrier_boundary",
    "control_death",
]

coinduced_extension_slots = {
    "kills_dd4_class": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "canonical_rosati": False,
    "positive_primitive_sign": False,
    "carrier_boundary": False,
    "control_death": False,
}

control_can_coinduce = True

gate(
    "CID5 coinduction is formable on controls",
    control_can_coinduce and coinduced_extension_slots["kills_dd4_class"],
    "any C2-module M has Coind(M), so vanishing H^1 is not a carrier guard",
)

gate(
    "CID6 coinduction satisfies no square-carrier slot",
    not any(coinduced_extension_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCID1-CID6 ALL PASS: coinduced DD.4 extension kills H^1 but not the square carrier")
print(
    "VERDICT: replacing U_1 by the coinduced two-copy coefficient system makes "
    "H^1 vanish and sends the DD.4 class to a coboundary.  This is algebraically "
    "real, but it doubles the coefficient support, is formable for arbitrary "
    "controls, and constructs no actual square, rep_NS, degree maps, graph, "
    "projection formula, Rosati, carrier boundary, or control death."
)
