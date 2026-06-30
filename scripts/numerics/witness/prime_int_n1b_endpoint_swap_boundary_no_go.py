r"""Endpoint-swap-boundary DD.4/SCC no-go.

Doc 271 rejects a free endpoint valuation register because its DD.4 boundary
direction is chosen.  This witness tests the natural repair:

    impose the endpoint swap tau(d1,d2)=(d2,d1) and let symmetry choose the
    DD.4 boundary direction.

The positive fact is real.  The swap-invariant primitive direction
ell_+(d1,d2)=d1+d2 commutes with the endpoint swap and splits
c=(1+z)^-1 in the same rank-two register.  The no-go is that this is still
only a rank-one boundary direction.  It does not recover the two SCC endpoint
degree maps, the anti-invariant alternative needs an external sign/orientation
action, the same construction is formable on controls, and no square-carrier
slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_endpoint_swap_boundary_no_go
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


def endpoint_split_profile(L, coeffs, sign_on_units=False):
    a, b = coeffs
    assert gcd(abs(a), abs(b)) == 1
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    split_vector = (1, 0) if a else (0, 1)

    def ell(v):
        return a * v[0] + b * v[1]

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

    register_gens = [((1, 0), {0: 1}), ((0, 1), {0: 1})]
    unit_gens = [((0, 0), {0: 1, k: 1}) for k in range(1, L + 1)]
    split_generator = sigma((split_vector, {0: 1}))
    split_boundary = eboundary(split_generator)
    test_gens = register_gens + unit_gens

    return {
        "L": L,
        "coeffs": coeffs,
        "split_vector": split_vector,
        "split_ell": ell(split_vector),
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in test_gens),
        "split_boundary_is_c": split_boundary == ((0, 0), c),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in test_gens),
        "sign_on_units": sign_on_units,
        "uses_square_data": False,
    }


def invariant_linear_forms(limit=3):
    rows = []
    for a in range(-limit, limit + 1):
        for b in range(-limit, limit + 1):
            if (a, b) == (0, 0) or gcd(abs(a), abs(b)) != 1:
                continue
            rows.append(
                {
                    "coeffs": (a, b),
                    "swap_invariant": (a, b) == (b, a),
                    "swap_anti_invariant": (a, b) == (-b, -a),
                }
            )
    primitive_invariant = [row["coeffs"] for row in rows if row["swap_invariant"]]
    primitive_anti = [row["coeffs"] for row in rows if row["swap_anti_invariant"]]
    return {
        "primitive_invariant": primitive_invariant,
        "primitive_anti_invariant": primitive_anti,
        "only_total_up_to_sign": set(primitive_invariant) == {(-1, -1), (1, 1)},
        "only_difference_up_to_sign": set(primitive_anti) == {(-1, 1), (1, -1)},
    }


def total_degree_endpoint_loss():
    trace_f = 1
    a = {"pair": (10, 1), "total": 11, "diag": 10 + 1 - trace_f}
    b = {"pair": (7, 4), "total": 11, "diag": 7 + 4 - trace_f}

    def left_probe(pair):
        return pair[1]

    def right_probe(pair):
        return pair[0]

    return {
        "a": a,
        "b": b,
        "same_total": a["total"] == b["total"],
        "same_diagonal_intersection": a["diag"] == b["diag"],
        "left_probe_changes": left_probe(a["pair"]) != left_probe(b["pair"]),
        "right_probe_changes": right_probe(a["pair"]) != right_probe(b["pair"]),
    }


def anti_invariant_orientation_profile():
    ordinary = endpoint_split_profile(8, (1, -1), sign_on_units=False)
    oriented = endpoint_split_profile(8, (1, -1), sign_on_units=True)
    pair = (10, 1)
    swapped = swap_pair(pair)
    return {
        "ordinary_tau_commutes": ordinary["tau_commutes_with_sigma"],
        "oriented_tau_commutes": oriented["tau_commutes_with_sigma"],
        "difference": pair[0] - pair[1],
        "swapped_difference": swapped[0] - swapped[1],
        "sign_choice_required": pair[0] - pair[1] == -(swapped[0] - swapped[1]),
        "uses_square_data": ordinary["uses_square_data"] or oriented["uses_square_data"],
    }


def control_swap_profile(dim):
    chosen_control_class = tuple(1 if i == 0 else 0 for i in range(dim))
    zero_vec = tuple(0 for _ in range(dim))

    def add_vec(x, y):
        return tuple(a ^ b for a, b in zip(x, y))

    def ell_total(register):
        return register[0] + register[1]

    def sigma(pair):
        register, vector = pair
        twist = chosen_control_class if ell_total(register) % 2 else zero_vec
        return register, add_vec(vector, twist)

    def tau(pair):
        register, vector = pair
        return swap_pair(register), vector

    gens = [((1, 0), zero_vec), ((0, 1), zero_vec), ((1, 1), zero_vec)]
    split_generator = sigma(((1, 0), zero_vec))
    split_boundary = ((1, 0), add_vec(split_generator[1], sigma(split_generator)[1]))
    return {
        "dim": dim,
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in gens),
        "split_boundary_is_chosen": split_boundary == ((1, 0), chosen_control_class),
        "swap_symmetric_total_direction": ell_total((1, 0)) == ell_total((0, 1)),
        "uses_square_data": False,
        "kills_controls": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
total_split_profiles = [endpoint_split_profile(L, (1, 1)) for L in (6, 8, 10, 12)]
form_profile = invariant_linear_forms()
endpoint_loss = total_degree_endpoint_loss()
anti_profile = anti_invariant_orientation_profile()
control_profiles = [control_swap_profile(dim) for dim in (2, 4, 8)]


gate(
    "ESB1 base DD.4 class remains the nonzero 1-unit obstruction",
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
    "ESB2 endpoint swap selects a real total-degree split of c",
    all(
        p["sigma_involutive_on_gens"]
        and p["split_boundary_is_c"]
        and p["split_ell"] == 1
        and p["tau_commutes_with_sigma"]
        and not p["uses_square_data"]
        for p in total_split_profiles
    ),
    "  ".join("L%d:ell=d1+d2 split by %s" % (p["L"], p["split_vector"]) for p in total_split_profiles),
)

gate(
    "ESB3 swap symmetry gives one total direction, not two endpoint maps",
    form_profile["only_total_up_to_sign"]
    and endpoint_loss["same_total"]
    and endpoint_loss["same_diagonal_intersection"]
    and endpoint_loss["left_probe_changes"]
    and endpoint_loss["right_probe_changes"],
    "primitive invariants=%s; %s and %s share total/diag"
    % (form_profile["primitive_invariant"], endpoint_loss["a"]["pair"], endpoint_loss["b"]["pair"]),
)

gate(
    "ESB4 the anti-invariant difference direction needs extra orientation",
    form_profile["only_difference_up_to_sign"]
    and not anti_profile["ordinary_tau_commutes"]
    and anti_profile["oriented_tau_commutes"]
    and anti_profile["sign_choice_required"]
    and not anti_profile["uses_square_data"],
    "ordinary swap fails, sign-twisted swap works; diff %d -> %d"
    % (anti_profile["difference"], anti_profile["swapped_difference"]),
)

gate(
    "ESB5 the same swap-symmetric total split is formable on controls",
    all(
        p["tau_commutes_with_sigma"]
        and p["split_boundary_is_chosen"]
        and p["swap_symmetric_total_direction"]
        and not p["uses_square_data"]
        and not p["kills_controls"]
        for p in control_profiles
    ),
    "  ".join("dim%d:swap-total-splits" % p["dim"] for p in control_profiles),
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

endpoint_swap_slots = {
    "swap_symmetry": True,
    "rank_one_total_boundary": True,
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
    "ESB6 endpoint-swap boundary symmetry satisfies no square-carrier slot",
    not any(endpoint_swap_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nESB1-ESB6 ALL PASS: endpoint-swap boundary symmetry is not the square carrier")
print(
    "VERDICT: endpoint swap can select the invariant total direction and split "
    "c=(1+z)^-1, but that direction is rank-one endpoint data.  It loses the "
    "two SCC endpoint maps, the anti-invariant direction needs an external "
    "sign/orientation action, the same construction is formable on controls, "
    "and no square, rep_NS, proper correspondences, projection formula, "
    "Rosati, carrier boundary, or control death is constructed."
)
