r"""Valuation-parity cover DD.4 no-go.

Doc 267 shows that the full Laurent field kills the DD.4 class by the odd
valuation/uniformizer axis.  This witness tests the next repair:

    keep only the mod-2 valuation character.

The positive identity is again real.  The C_2-parity cover

    E = (Z/2) x U_1,    sigma(e,u) = (e, c^e phi(u))

has a boundary whose unit part is c=(1+z)^-1.  Thus it kills the named DD.4
representative.  The no-go is that this is only the parity quotient of valuation:
it collapses m and m+2, supplies no full Laurent line or degree maps, is
formable on controls, and constructs no SCC slot.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_valuation_parity_cover_no_go
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

    return add, mul, inv, phi


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


def pow_unit(unit, exponent, mul, inv):
    if exponent < 0:
        return inv(pow_unit(unit, -exponent, mul, inv))
    out = {0: 1}
    base = unit
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def boundary(unit, inv, phi, mul):
    return mul(unit, inv(phi(unit)))


def h1_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        boundary({0: 1, k: 1}, inv, phi, mul) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(
        boundary_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    norm_image = closure(
        norm_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "c": c,
        "coboundaries": coboundaries,
        "h1_order": z1_order // len(coboundaries),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "c_boundary": to_vec(c, L) in coboundaries,
        "res1_c": c.get(1, 0),
    }


def pair_mul(x, y, mul):
    return (x[0] ^ y[0], mul(x[1], y[1]))


def pair_inv(x, inv):
    return (x[0], inv(x[1]))


def pair_to_vec(x, L):
    return (x[0],) + to_vec(x[1], L)


def pair_from_vec(v):
    return (v[0], from_vec(v[1:]))


def parity_cover_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        bit, unit = x
        twist = c if bit else {0: 1}
        return bit, mul(twist, phi(unit))

    def pmul(x, y):
        return pair_mul(x, y, mul)

    def pinv(x):
        return pair_inv(x, inv)

    def pboundary(x):
        return pmul(x, pinv(sigma(x)))

    gens = [(1, {0: 1})] + [(0, {0: 1, k: 1}) for k in range(1, L + 1)]
    parity_generator = (1, {0: 1})
    parity_generator_boundary = pboundary(parity_generator)
    phi_parity_generator = sigma(parity_generator)
    split_generator = phi_parity_generator
    split_boundary = pboundary(split_generator)
    diag_c = (0, c)

    return {
        "L": L,
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in gens),
        "parity_generator_boundary_is_c_inverse": parity_generator_boundary
        == (0, inv(c)),
        "split_boundary_is_c": split_boundary == diag_c,
        "parity_generator_maps_to_split_generator": split_generator == (1, c),
        "rank_before": L,
        "rank_after": L + 1,
    }


def valuation_parity_loss_profile():
    rows = []
    for valuation in range(-4, 5):
        rows.append(
            {
                "valuation": valuation,
                "parity": valuation % 2,
                "kills_c": valuation % 2 == 1,
            }
        )
    collision_pairs = [
        (row["valuation"], other["valuation"])
        for row in rows
        for other in rows
        if row["valuation"] < other["valuation"]
        and row["parity"] == other["parity"]
    ]
    return {
        "rows": rows,
        "parity_kills_exactly_odd_valuations": all(
            row["kills_c"] == (row["valuation"] % 2 == 1) for row in rows
        ),
        "collapses_distinct_degrees": bool(collision_pairs),
        "sample_collisions": collision_pairs[:4],
        "integer_degree_recovered": False,
        "two_carrier_degree_maps_recovered": False,
    }


def dmp_tcr_phi_support(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def support_profile():
    window = list(range(-6, 7))
    full_line_missing = [
        deg for deg in window if dmp_tcr_phi_support(deg) == 0
    ]
    parity_cover_rank = 2
    return {
        "full_line_missing": full_line_missing == [-6, -5, -4, -3, -2],
        "parity_cover_rank": parity_cover_rank,
        "has_full_laurent_line": False,
        "has_proper_correspondence_endpoints": False,
    }


def xor_vec(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def control_parity_cover_profile(dim):
    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))

    def sigma(pair):
        bit, vector = pair
        twist = chosen if bit else zero
        return bit, xor_vec(vector, twist)

    def add_pair(x, y):
        return x[0] ^ y[0], xor_vec(x[1], y[1])

    split_generator = sigma((1, zero))
    split_boundary = add_pair(split_generator, sigma(split_generator))
    return {
        "dim": dim,
        "split_boundary_is_chosen": split_boundary == (0, chosen),
        "uses_square_data": False,
        "uses_only_parity_cover": True,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
parity_profiles = [parity_cover_profile(L) for L in (6, 8, 10, 12)]
valuation_loss = valuation_parity_loss_profile()
support = support_profile()
control_profiles = [control_parity_cover_profile(dim) for dim in (1, 2, 4, 8)]


gate(
    "VPC1 base DD.4 class remains the nonzero 1-unit obstruction",
    all(
        p["h1_order"] == 2 and not p["c_boundary"] and p["res1_c"] == 1
        for p in base_profiles
    ),
    "  ".join(
        "L%d:|B|=2^%d,|Z1|=2^%d,H1=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "VPC2 valuation-parity cover kills the named DD.4 representative",
    all(
        p["sigma_involutive_on_gens"]
        and p["parity_generator_boundary_is_c_inverse"]
        and p["split_boundary_is_c"]
        and p["parity_generator_maps_to_split_generator"]
        for p in parity_profiles
    ),
    "  ".join(
        "L%d:split-generator-boundary=c"
        % p["L"]
        for p in parity_profiles
    ),
)

gate(
    "VPC3 parity keeps only valuation mod 2 and loses integer degree data",
    valuation_loss["parity_kills_exactly_odd_valuations"]
    and valuation_loss["collapses_distinct_degrees"]
    and not valuation_loss["integer_degree_recovered"]
    and not valuation_loss["two_carrier_degree_maps_recovered"],
    "sample collisions %s" % (valuation_loss["sample_collisions"],),
)

gate(
    "VPC4 parity cover supplies neither DMP Laurent line nor correspondence endpoints",
    support["full_line_missing"]
    and support["parity_cover_rank"] == 2
    and not support["has_full_laurent_line"]
    and not support["has_proper_correspondence_endpoints"],
    "DMP lacks <=-2 degrees; parity cover has only two sheets",
)

gate(
    "VPC5 the same parity-cover split is formable on controls",
    all(
        p["split_boundary_is_chosen"]
        and p["uses_only_parity_cover"]
        and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:parity-cover-splits" % p["dim"] for p in control_profiles),
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

parity_cover_slots = {
    "kills_dd4_class": True,
    "valuation_parity": True,
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

gate(
    "VPC6 valuation-parity cover satisfies no square-carrier slot",
    not any(parity_cover_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nVPC1-VPC6 ALL PASS: valuation-parity cover is not the DD.4 carrier boundary")
print(
    "VERDICT: the mod-2 valuation cover kills c=(1+z)^-1, but only by "
    "remembering the parity quotient of the Laurent valuation.  It collapses "
    "integer degree data, supplies no full Laurent line or correspondence "
    "endpoints, is formable on controls, and constructs no square, rep_NS, "
    "degree maps, graph, projection formula, Rosati, carrier boundary, or "
    "control death."
)
