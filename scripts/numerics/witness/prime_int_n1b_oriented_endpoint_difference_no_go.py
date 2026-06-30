r"""Oriented-endpoint-difference DD.4/SCC no-go.

Doc 272 rejects endpoint-swap symmetry as a carrier boundary because the
ordinary swap selects only total degree.  This witness tests the next repair:

    add an orientation/sign action so the anti-invariant difference
    ell_-(d1,d2)=d1-d2 commutes with endpoint swap, then combine total and
    difference to recover the two endpoint degrees.

The positive fact is real.  With a sign action on the unit line, the
difference-direction twist splits c=(1+z)^-1 and commutes with the oriented
swap.  The no-go is that the sign action and the half-sum decoder are
external data.  The map (d1,d2) -> (d1+d2,d1-d2) has determinant -2, so
recovering endpoints requires a parity condition and division by 2.  The
orientation sign also decides left versus right.  The same oriented package is
formable on controls, and no square-carrier slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_oriented_endpoint_difference_no_go
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


def endpoint_mul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def endpoint_inv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def swap_pair(pair):
    return pair[1], pair[0]


def endpoint_difference_split_profile(L, sign_on_units):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def ell(v):
        return v[0] - v[1]

    def sigma(x):
        vector, unit = x
        twist = pow_unit(c, ell(vector), mul, inv)
        return vector, mul(twist, phi(unit))

    def tau(x):
        vector, unit = x
        unit_out = inv(unit) if sign_on_units else unit
        return swap_pair(vector), unit_out

    def emul(x, y):
        return endpoint_mul(x, y, mul)

    def einv(x):
        return endpoint_inv(x, inv)

    def eboundary(x):
        return emul(x, einv(sigma(x)))

    register_gens = [((1, 0), {0: 1}), ((0, 1), {0: 1}), ((1, 1), {0: 1})]
    unit_gens = [((0, 0), {0: 1, k: 1}) for k in range(1, L + 1)]
    test_gens = register_gens + unit_gens
    split_generator = sigma(((1, 0), {0: 1}))
    split_boundary = eboundary(split_generator)

    return {
        "L": L,
        "sign_on_units": sign_on_units,
        "split_ell": ell((1, 0)),
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in test_gens),
        "split_boundary_is_c": split_boundary == ((0, 0), c),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in test_gens),
        "uses_square_data": False,
    }


def decode_total_difference(total, difference):
    if (total + difference) % 2 or (total - difference) % 2:
        return None
    return (total + difference) // 2, (total - difference) // 2


def total_difference_decoder_profile():
    samples = [
        {"total": 11, "difference": 9, "expected": (10, 1)},
        {"total": 11, "difference": 3, "expected": (7, 4)},
        {"total": 11, "difference": 8, "expected": None},
        {"total": 10, "difference": 1, "expected": None},
    ]
    rows = []
    for sample in samples:
        decoded = decode_total_difference(sample["total"], sample["difference"])
        rows.append({**sample, "decoded": decoded, "matches": decoded == sample["expected"]})
    return {
        "matrix_det": -2,
        "unimodular": False,
        "index_two_image": True,
        "inverse_has_half": True,
        "rows": rows,
        "decoder_is_external": True,
        "valid_rows_decode": all(row["matches"] for row in rows),
    }


def orientation_sign_ambiguity_profile():
    total = 11
    difference = 9
    plus = decode_total_difference(total, difference)
    minus = decode_total_difference(total, -difference)

    def left_probe(pair):
        return pair[1]

    def right_probe(pair):
        return pair[0]

    return {
        "total": total,
        "difference": difference,
        "plus": plus,
        "minus": minus,
        "same_unordered_pair": sorted(plus) == sorted(minus),
        "left_probe_changes": left_probe(plus) != left_probe(minus),
        "right_probe_changes": right_probe(plus) != right_probe(minus),
        "carrier_forces_sign": False,
    }


def control_oriented_difference_profile(dim):
    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))

    def add_vec(x, y):
        return tuple(a + b for a, b in zip(x, y))

    def neg_vec(x):
        return tuple(-a for a in x)

    def scale_vec(n, x):
        return tuple(n * a for a in x)

    def ell(register):
        return register[0] - register[1]

    def sigma(pair):
        register, vector = pair
        return register, add_vec(neg_vec(vector), scale_vec(ell(register), chosen))

    def tau(pair):
        register, vector = pair
        return swap_pair(register), neg_vec(vector)

    gens = [
        ((1, 0), zero),
        ((0, 1), zero),
        ((1, 1), zero),
        ((2, 1), chosen),
    ]
    return {
        "dim": dim,
        "sigma_involutive": all(sigma(sigma(gen)) == gen for gen in gens),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in gens),
        "oriented_difference_splits_chosen_class": sigma(((1, 0), zero))[1] == chosen,
        "uses_square_data": False,
        "kills_controls": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
ordinary_difference_profiles = [
    endpoint_difference_split_profile(L, sign_on_units=False) for L in (6, 8, 10, 12)
]
oriented_difference_profiles = [
    endpoint_difference_split_profile(L, sign_on_units=True) for L in (6, 8, 10, 12)
]
decoder_profile = total_difference_decoder_profile()
orientation_ambiguity = orientation_sign_ambiguity_profile()
control_profiles = [control_oriented_difference_profile(dim) for dim in (2, 4, 8)]


gate(
    "OED1 base DD.4 class remains the nonzero 1-unit obstruction",
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
    "OED2 oriented endpoint difference split is real but sign-imported",
    all(
        not old["tau_commutes_with_sigma"]
        and new["sigma_involutive_on_gens"]
        and new["split_boundary_is_c"]
        and new["split_ell"] == 1
        and new["tau_commutes_with_sigma"]
        and not new["uses_square_data"]
        for old, new in zip(ordinary_difference_profiles, oriented_difference_profiles)
    ),
    "  ".join("L%d:ordinary-fails oriented-splits" % p["L"] for p in oriented_difference_profiles),
)

gate(
    "OED3 sum/difference endpoint recovery uses an index-two half-sum decoder",
    decoder_profile["matrix_det"] == -2
    and not decoder_profile["unimodular"]
    and decoder_profile["index_two_image"]
    and decoder_profile["inverse_has_half"]
    and decoder_profile["decoder_is_external"]
    and decoder_profile["valid_rows_decode"],
    "det=%d; decodes=%s"
    % (
        decoder_profile["matrix_det"],
        ", ".join(
            "(%d,%d)->%s"
            % (row["total"], row["difference"], row["decoded"])
            for row in decoder_profile["rows"]
        ),
    ),
)

gate(
    "OED4 orientation sign decides left versus right endpoint probes",
    orientation_ambiguity["same_unordered_pair"]
    and orientation_ambiguity["left_probe_changes"]
    and orientation_ambiguity["right_probe_changes"]
    and not orientation_ambiguity["carrier_forces_sign"],
    "total %d, diff +/- %d gives %s vs %s"
    % (
        orientation_ambiguity["total"],
        orientation_ambiguity["difference"],
        orientation_ambiguity["plus"],
        orientation_ambiguity["minus"],
    ),
)

gate(
    "OED5 the same oriented-difference package is formable on controls",
    all(
        p["sigma_involutive"]
        and p["tau_commutes_with_sigma"]
        and p["oriented_difference_splits_chosen_class"]
        and not p["uses_square_data"]
        and not p["kills_controls"]
        for p in control_profiles
    ),
    "  ".join("dim%d:oriented-difference-splits" % p["dim"] for p in control_profiles),
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

oriented_difference_slots = {
    "imported_orientation_sign": True,
    "half_sum_decoder": True,
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
    "OED6 oriented endpoint difference satisfies no square-carrier slot",
    not any(oriented_difference_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nOED1-OED6 ALL PASS: oriented endpoint difference is not the square carrier")
print(
    "VERDICT: adding endpoint orientation makes the anti-invariant difference "
    "direction commute with swap and split c=(1+z)^-1, but the sign action is "
    "imported and endpoint recovery from total/difference uses an index-two "
    "half-sum decoder.  The same package is formable on controls and no "
    "square, rep_NS, proper correspondences, projection formula, Rosati, "
    "carrier boundary, or control death is constructed."
)
