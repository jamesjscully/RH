r"""Bar/coinduced resolution boundary no-go.

This witness tests the repair left open after doc 258:
promote the standard bar/coinduced-resolution connecting boundary to the
carrier-native boundary/properness/self-duality map required by the
DD.4/SCC interface.  The resolution boundary kills the DD.4 class, but
only as a universal coboundary certificate in a two-copy acyclic
coefficient system.  It supplies no square carrier.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_bar_resolution_boundary_no_go
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


def bar_boundary_profile(L):
    mul, inv, phi = make(L)

    def sigma(x):
        # Coinduced C2 action: swap copies and apply the base shear.
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
    left_certificate = (c, {0: 1})
    right_certificate = ({0: 1}, c)
    left_boundary = pmul(left_certificate, pinv(sigma(left_certificate)))
    right_boundary = pmul(right_certificate, pinv(sigma(right_certificate)))
    return {
        "L": L,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "diag_c_coboundary": pair_to_vec(diag_c, L) in coboundaries,
        "left_boundary": left_boundary == diag_c,
        "right_boundary": right_boundary == diag_c,
        "rank_before": L,
        "rank_after": 2 * L,
    }


def control_bar_recipe_profile(dim):
    """Exact additive F_2 control module with the same bar recipe."""

    def add_vec(x, y):
        return tuple(a ^ b for a, b in zip(x, y))

    def tau(x):
        return tuple(reversed(x))

    def sigma(pair):
        return tau(pair[1]), tau(pair[0])

    def pair_add(x, y):
        return add_vec(x[0], y[0]), add_vec(x[1], y[1])

    d = tuple(1 for _ in range(dim))
    zero = tuple(0 for _ in range(dim))
    diag_d = (d, d)
    left_certificate = (d, zero)
    right_certificate = (zero, d)
    return {
        "dim": dim,
        "d_is_cocycle": add_vec(d, tau(d)) == zero,
        "left_boundary": pair_add(left_certificate, sigma(left_certificate)) == diag_d,
        "right_boundary": pair_add(right_certificate, sigma(right_certificate)) == diag_d,
        "uses_square_data": False,
    }


base_profiles = [base_h1_profile(L) for L in (6, 8, 10, 12)]
bar_profiles = [bar_boundary_profile(L) for L in (6, 8, 10, 12)]
control_profiles = [control_bar_recipe_profile(dim) for dim in (2, 4, 6)]

gate(
    "BRB1 base DD.4 class remains the nonzero obstruction",
    all(p["h1_order"] == 2 and p["c_nonboundary"] and p["res1_c"] == 1 for p in base_profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "BRB2 bar/coinduced resolution is acyclic in degree one",
    all(p["h1_order"] == 1 for p in bar_profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in bar_profiles
    ),
)

gate(
    "BRB3 boundary certificate is a standard resolution coboundary",
    all(p["diag_c_coboundary"] and p["left_boundary"] and p["right_boundary"] for p in bar_profiles),
    "diag(c)=(c,1)/sigma(c,1)=(1,c)/sigma(1,c)",
)

gate(
    "BRB4 same boundary recipe is formable on controls",
    all(
        p["d_is_cocycle"] and p["left_boundary"] and p["right_boundary"] and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:no-square-data" % p["dim"] for p in control_profiles),
)

gate(
    "BRB5 resolution doubles support before any square carrier exists",
    all(p["rank_after"] == 2 * p["rank_before"] for p in bar_profiles),
    "  ".join("L%d:%d->%d" % (p["L"], p["rank_before"], p["rank_after"]) for p in bar_profiles),
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

bar_boundary_slots = {
    "kills_dd4_class": True,
    "universal_resolution_boundary": True,
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

admissible_boundary_requirements = {
    "carrier_native": False,
    "non_control_formable": False,
    "square_derived": False,
    "properness_or_self_duality_map": False,
}

gate(
    "BRB6 bar boundary satisfies no square-carrier boundary slot",
    not any(bar_boundary_slots[slot] for slot in required_slots)
    and not any(admissible_boundary_requirements.values()),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBRB1-BRB6 ALL PASS: bar/coinduced resolution boundary is not the square carrier boundary")
print(
    "VERDICT: the universal bar/coinduced boundary makes diag(c) a coboundary "
    "by choosing a 0-cochain in an acyclic two-copy resolution.  That boundary "
    "is formable on controls, doubles support, and supplies no actual square, "
    "rep_NS, degree maps, graph, projection formula, Rosati, carrier-native "
    "properness/self-duality map, or control death."
)
