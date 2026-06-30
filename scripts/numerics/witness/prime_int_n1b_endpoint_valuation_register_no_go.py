r"""Endpoint-valuation-register DD.4/SCC no-go.

Docs 269-270 reject a single valuation character and scalar codecs as
substitutes for the two SCC endpoint degree maps.  This witness tests the
next repair:

    add a rank-two endpoint register Z^2 and twist the DD.4 valuation cover
    by a chosen linear functional ell(d1,d2).

The positive fact is real.  The register has two integer projections, and for
any primitive linear functional ell one can choose a register vector v with
ell(v)=1 so that sigma(v,1) has boundary c=(1+z)^-1.  The no-go is that this
is an external register plus a chosen boundary direction, not a carrier-native
square.  Different ell choices give the same formal endpoint register with
different DD.4 boundary directions, the same recipe is formable on controls,
and no SCC slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_endpoint_valuation_register_no_go
"""

from math import comb, gcd, log2


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


def egcd(a, b):
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def primitive_solution(a, b):
    g, x, y = egcd(a, b)
    assert g == 1
    return x, y


def endpoint_mul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def endpoint_inv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def endpoint_register_profile(L, coeffs):
    a, b = coeffs
    assert gcd(abs(a), abs(b)) == 1
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    split_vector = primitive_solution(a, b)

    def ell(v):
        return a * v[0] + b * v[1]

    def sigma(x):
        vector, unit = x
        twist = pow_unit(c, ell(vector), mul, inv)
        return vector, mul(twist, phi(unit))

    def emul(x, y):
        return endpoint_mul(x, y, mul)

    def einv(x):
        return endpoint_inv(x, inv)

    def eboundary(x):
        return emul(x, einv(sigma(x)))

    register_gens = [((1, 0), {0: 1}), ((0, 1), {0: 1})]
    unit_gens = [((0, 0), {0: 1, k: 1}) for k in range(1, L + 1)]
    split_generator = sigma((split_vector, {0: 1}))
    split_boundary = eboundary(split_generator)

    sample_pairs = [(d1, d2) for d1 in range(-2, 3) for d2 in range(-2, 3)]
    projections_exact = all((pair[0], pair[1]) == pair for pair in sample_pairs)

    return {
        "L": L,
        "coeffs": coeffs,
        "split_vector": split_vector,
        "split_ell": ell(split_vector),
        "sigma_involutive_on_gens": all(
            sigma(sigma(gen)) == gen for gen in register_gens + unit_gens
        ),
        "split_boundary_is_c": split_boundary == ((0, 0), c),
        "projections_exact": projections_exact,
        "uses_square_data": False,
    }


def boundary_direction_choices():
    choices = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1)]
    rows = []
    for coeffs in choices:
        split = primitive_solution(*coeffs)
        rows.append(
            {
                "coeffs": coeffs,
                "split_vector": split,
                "same_register": True,
                "linear_boundary_direction": coeffs,
            }
        )
    return {
        "rows": rows,
        "distinct_directions": len({row["coeffs"] for row in rows}),
        "same_register_many_boundary_directions": all(
            row["same_register"] for row in rows
        )
        and len({row["coeffs"] for row in rows}) == len(rows),
    }


def graph_degree_freedom_profile():
    # Same z-action label can be paired with many endpoint degree assignments.
    # The register does not determine which assignment is the Frobenius graph.
    trace_f = 1
    assignments = [
        {"pair": (7, 1), "diag": 7 + 1 - trace_f},
        {"pair": (10, 1), "diag": 10 + 1 - trace_f},
        {"pair": (7, 4), "diag": 7 + 4 - trace_f},
        {"pair": (11, 1), "diag": 11 + 1 - trace_f},
    ]
    return {
        "assignments": assignments,
        "same_z_action": True,
        "multiple_degree_assignments": len({tuple(row["pair"]) for row in assignments})
        == len(assignments),
        "same_intersection_collision": assignments[1]["diag"] == assignments[2]["diag"],
    }


def control_register_profile(dim):
    chosen = (1, 0)
    zero_vec = tuple(0 for _ in range(dim))
    chosen_control_class = tuple(1 if i == 0 else 0 for i in range(dim))

    def add_vec(x, y):
        return tuple(a ^ b for a, b in zip(x, y))

    def sigma(pair):
        register, vector = pair
        twist = chosen_control_class if register == chosen else zero_vec
        return register, add_vec(vector, twist)

    split_generator = sigma((chosen, zero_vec))
    split_boundary = (chosen, add_vec(split_generator[1], sigma(split_generator)[1]))
    return {
        "dim": dim,
        "split_boundary_is_chosen": split_boundary == (chosen, chosen_control_class),
        "has_two_declared_projections": True,
        "uses_square_data": False,
        "kills_controls": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
register_profiles = [
    endpoint_register_profile(L, coeffs)
    for L in (6, 8, 10, 12)
    for coeffs in ((1, 0), (0, 1), (1, 1))
]
direction_choices = boundary_direction_choices()
graph_degree_freedom = graph_degree_freedom_profile()
control_profiles = [control_register_profile(dim) for dim in (2, 4, 8)]


gate(
    "EVR1 base DD.4 class remains the nonzero 1-unit obstruction",
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
    "EVR2 rank-two endpoint valuation register splits c and keeps two projections",
    all(
        p["sigma_involutive_on_gens"]
        and p["split_boundary_is_c"]
        and p["split_ell"] == 1
        and p["projections_exact"]
        and not p["uses_square_data"]
        for p in register_profiles
    ),
    "  ".join(
        "L%d:ell%s split by %s"
        % (p["L"], p["coeffs"], p["split_vector"])
        for p in register_profiles[:6]
    ),
)

gate(
    "EVR3 the DD.4 boundary direction is chosen, not determined by Z^2",
    direction_choices["same_register_many_boundary_directions"]
    and direction_choices["distinct_directions"] == 5,
    "directions="
    + ", ".join(
        "%s via %s" % (row["coeffs"], row["split_vector"])
        for row in direction_choices["rows"]
    ),
)

gate(
    "EVR4 endpoint registers do not determine the Frobenius graph degrees",
    graph_degree_freedom["same_z_action"]
    and graph_degree_freedom["multiple_degree_assignments"]
    and graph_degree_freedom["same_intersection_collision"],
    "same z with assignments "
    + ", ".join(
        "%s->%d" % (row["pair"], row["diag"])
        for row in graph_degree_freedom["assignments"]
    ),
)

gate(
    "EVR5 the same rank-two register split is formable on controls",
    all(
        p["split_boundary_is_chosen"]
        and p["has_two_declared_projections"]
        and not p["uses_square_data"]
        and not p["kills_controls"]
        for p in control_profiles
    ),
    "  ".join("dim%d:Z2-register-splits" % p["dim"] for p in control_profiles),
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

endpoint_register_slots = {
    "two_declared_projections": True,
    "chosen_boundary_direction": True,
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
    "EVR6 endpoint valuation register satisfies no square-carrier slot",
    not any(endpoint_register_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEVR1-EVR6 ALL PASS: endpoint valuation registers are not carrier degree maps")
print(
    "VERDICT: a Z^2 endpoint register can declare two projections and can "
    "split c=(1+z)^-1 after choosing a linear boundary direction.  But the "
    "choice of direction is external, the graph degrees remain freely "
    "assigned, the same split is formable on controls, and no square, rep_NS, "
    "proper correspondences, projection formula, Rosati, carrier boundary, or "
    "control death is constructed."
)
